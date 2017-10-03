import maya.cmds as cmds

from Jenks.scripts.rigModules import utilityFunctions as utils
from Jenks.scripts.rigModules import ikFunctions as ikFn
from Jenks.scripts.rigModules import ctrlFunctions as ctrlFn
from Jenks.scripts.rigModules.suffixDictionary import suffix
from Jenks.scripts.rigModules import orientJoints

reload(utils)
reload(orientJoints)

def createLayeredSplineIK(jnts, name, rig=None, side='C', extraName='', ctrlLayers=2, parent=None):
    moduleName = utils.setupBodyPartName(extraName, side)
    extraName = '{}_'.format(extraName) if extraName else ''
    col = utils.getColors(side)
    ## create base layer jnts
    tmpCrv = utils.createCrvFromObjs(jnts, crvName='tmpCrv')
    ctrlGrp = utils.newNode('group', name='{}{}Ctrls'.format(extraName, name), side=side,
                            parent=rig.ctrlsGrp.name if rig else None, skipNum=True)
    mechGrp = utils.newNode('group', name='{}{}Mech'.format(extraName, name), side=side,
                            parent=rig.mechGrp.name if rig else None, skipNum=True)
    baseJnts = utils.createJntsFromCrv(tmpCrv, numOfJnts=4, side=side,
                                       name='{}{}_baseLayer'.format(extraName, name))
    if rig:
        cmds.parent(jnts[0], rig.skelGrp.name)
    cmds.parent(baseJnts[0], mechGrp.name)
    ## parent locs to base jnts
    ## base layer ctrls
    baseLayerLocs = []
    baseLayerCtrls = []
    baseCtrlParent = ctrlGrp.name
    for each in baseJnts:
        baseLoc = utils.newNode('locator', name='{}{}_baseLayer'.format(extraName, name),
                                side=side)
        baseLoc.parent(each, relative=True)
        baseLayerLocs.append(baseLoc)
        baseCtrl = ctrlFn.ctrl(name='{}{}_baseLayer'.format(extraName, name), guide=each,
                               side=side, parent=baseCtrlParent)
        baseCtrl.constrain(each)
        baseCtrl.modifyShape(shape='cube', color=12, scale=(1, 1, 1))
        baseLayerCtrls.append(baseCtrl)
        baseCtrlParent = baseCtrl.ctrlEnd

    ## mid layer crv FROM BASE JNTS
    midCrv = utils.createCrvFromObjs(baseJnts, crvName='{}_midLayer'.format(name),
                                     side=side, extraName=extraName)
    ## create mid jnts
    midJnts = utils.createJntsFromCrv(tmpCrv, numOfJnts=7, side=side,
                                      name='{}{}_midLayer'.format(extraName, name))
    cmds.parent(midJnts[0], mechGrp.name)
    cmds.delete(tmpCrv)
    ## parent locs to mid jnts
    ## create mid ctrls - parent constrain root grp to mid jnts
    midLayerLocs = []
    midLayerCtrls = []
    midCtrlParent = ctrlGrp.name
    for each in midJnts:
        midCtrl = ctrlFn.ctrl(name='{}{}_midLayer'.format(extraName, name), guide=each,
                               side=side, parent=midCtrlParent)
        cmds.parentConstraint(each, midCtrl.rootGrp.name, mo=1)
        midCtrl.modifyShape(shape='sphere', color=11, scale=(0.4, 0.4, 0.4))
        midLayerCtrls.append(midCtrl)
        midLoc = utils.newNode('locator', name='{}{}_midLayer'.format(extraName, name),
                               side=side)
        midLoc.parent(midCtrl.ctrlEnd, relative=True)
        midLayerLocs.append(midLoc)
        midCtrlParent = midCtrl.ctrlEnd
    ## ik spline mid crv to mid jnts
    midIKSpline = ikFn.ik(sj=midJnts[0], ej=midJnts[-1],
                          name='{}{}_midLayerIK'.format(extraName, name), side=side)
    midIKSpline.createSplineIK(crv=midCrv, parent=mechGrp.name)
    midIKSpline.addStretch(operation='both', mode='length',
                           globalScaleAttr=rig.scaleAttr if rig else None)
    midIKSpline.advancedTwist(baseLayerCtrls[0].ctrlEnd, endObj=baseLayerCtrls[-1].ctrlEnd,
                              wuType=4)
    ## connect mid crv cvs to base locators
    for i, each in enumerate(baseLayerLocs):
        cmds.connectAttr('{}.wp'.format(each.name), '{}Shape.cv[{}]'.format(midCrv, i))
    ## create skin crv FROM MID JNTS
    skinCrv = utils.createCrvFromObjs(midJnts, crvName='{}_skinLayer'.format(name),
                                      side=side, extraName=extraName)
    ## ik spline skin crv to skin jnts
    skinIKSpline = ikFn.ik(sj=jnts[0], ej=jnts[-1],
                           name='{}{}_skinLayerIK'.format(extraName, name), side=side)
    skinIKSpline.createSplineIK(crv=skinCrv, parent=mechGrp.name)
    skinIKSpline.addStretch(operation='both', mode='length',
                            globalScaleAttr=rig.scaleAttr if rig else None)
    skinIKSpline.advancedTwist(midLayerCtrls[0].ctrlEnd, endObj=midLayerCtrls[-1].ctrlEnd,
                               wuType=4)
    ## connect skin crv cvs to mid locators
    for i, each in enumerate(midLayerLocs):
        cmds.connectAttr('{}.wp'.format(each.name), '{}Shape.cv[{}]'.format(skinCrv, i))

    ##
