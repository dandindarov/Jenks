# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Docs/maya/2016/scripts/UHRFTools_UI_TV.ui'
#
# Created: Mon Sep 07 14:00:51 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1440, 800)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1440, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1440, 800))
       # MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
       # MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 650, 231, 141))
        self.groupBox.setObjectName("groupBox")
        self.btnUpdatePaths = QtGui.QPushButton(self.groupBox)
        self.btnUpdatePaths.setGeometry(QtCore.QRect(120, 80, 101, 51))
        self.btnUpdatePaths.setObjectName("btnUpdatePaths")
        self.rbLocal = QtGui.QRadioButton(self.groupBox)
        self.rbLocal.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.rbLocal.setChecked(True)
        self.rbLocal.setObjectName("rbLocal")
        self.rbRenderFarm = QtGui.QRadioButton(self.groupBox)
        self.rbRenderFarm.setGeometry(QtCore.QRect(10, 110, 92, 17))
        self.rbRenderFarm.setObjectName("rbRenderFarm")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 211, 51))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(28)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnRefresh = QtGui.QPushButton(self.centralwidget)
        self.btnRefresh.setGeometry(QtCore.QRect(1030, 20, 81, 51))
        self.btnRefresh.setObjectName("btnRefresh")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1090, 650, 341, 141))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btnSpool = QtGui.QPushButton(self.groupBox_4)
        self.btnSpool.setGeometry(QtCore.QRect(230, 80, 101, 51))
        self.btnSpool.setObjectName("btnSpool")
        self.cboJobType = QtGui.QComboBox(self.groupBox_4)
        self.cboJobType.setGeometry(QtCore.QRect(10, 110, 121, 22))
        self.cboJobType.setObjectName("cboJobType")
        self.cboJobType.addItem("")
        self.cboJobType.addItem("")
        self.cboFrameNum = QtGui.QComboBox(self.groupBox_4)
        self.cboFrameNum.setGeometry(QtCore.QRect(140, 110, 81, 22))
        self.cboFrameNum.setObjectName("cboFrameNum")
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 191, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 321, 61))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtGui.QFrame(self.groupBox_4)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 321, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(740, 650, 341, 141))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lblWorkspace = QtGui.QLabel(self.groupBox_5)
        self.lblWorkspace.setGeometry(QtCore.QRect(120, 50, 181, 21))
        self.lblWorkspace.setObjectName("lblWorkspace")
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 21))
        self.label_4.setObjectName("label_4")
        self.lblSceneName = QtGui.QLabel(self.groupBox_5)
        self.lblSceneName.setGeometry(QtCore.QRect(120, 20, 181, 21))
        self.lblSceneName.setObjectName("lblSceneName")
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.label_6.setObjectName("label_6")
        self.lblRenderer = QtGui.QLabel(self.groupBox_5)
        self.lblRenderer.setGeometry(QtCore.QRect(120, 80, 181, 21))
        self.lblRenderer.setObjectName("lblRenderer")
        self.lblFrameRange = QtGui.QLabel(self.groupBox_5)
        self.lblFrameRange.setGeometry(QtCore.QRect(120, 110, 181, 21))
        self.lblFrameRange.setObjectName("lblFrameRange")
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 111, 21))
        self.label_8.setObjectName("label_8")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 650, 481, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.cbMissingTextures = QtGui.QCheckBox(self.groupBox_3)
        self.cbMissingTextures.setEnabled(False)
        self.cbMissingTextures.setGeometry(QtCore.QRect(310, 40, 151, 17))
        self.cbMissingTextures.setChecked(False)
        self.cbMissingTextures.setObjectName("cbMissingTextures")
        self.cbNoJpg = QtGui.QCheckBox(self.groupBox_3)
        self.cbNoJpg.setEnabled(False)
        self.cbNoJpg.setGeometry(QtCore.QRect(310, 60, 151, 17))
        self.cbNoJpg.setChecked(False)
        self.cbNoJpg.setObjectName("cbNoJpg")
        self.cbTurtle = QtGui.QCheckBox(self.groupBox_3)
        self.cbTurtle.setEnabled(False)
        self.cbTurtle.setGeometry(QtCore.QRect(310, 80, 151, 17))
        self.cbTurtle.setChecked(False)
        self.cbTurtle.setObjectName("cbTurtle")
        self.cbNoUncached = QtGui.QCheckBox(self.groupBox_3)
        self.cbNoUncached.setEnabled(False)
        self.cbNoUncached.setGeometry(QtCore.QRect(310, 100, 151, 17))
        self.cbNoUncached.setChecked(False)
        self.cbNoUncached.setObjectName("cbNoUncached")
        self.cbProject = QtGui.QCheckBox(self.groupBox_3)
        self.cbProject.setEnabled(False)
        self.cbProject.setGeometry(QtCore.QRect(310, 20, 151, 17))
        self.cbProject.setChecked(False)
        self.cbProject.setObjectName("cbProject")
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 251, 51))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.lblQCFeedback = QtGui.QLabel(self.groupBox_3)
        self.lblQCFeedback.setGeometry(QtCore.QRect(10, 90, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        self.lblQCFeedback.setFont(font)
        self.lblQCFeedback.setAlignment(QtCore.Qt.AlignCenter)
        self.lblQCFeedback.setWordWrap(True)
        self.lblQCFeedback.setObjectName("lblQCFeedback")
        self.line = QtGui.QFrame(self.groupBox_3)
        self.line.setGeometry(QtCore.QRect(273, 20, 20, 111))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1120, 10, 311, 61))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(220, 20, 81, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(50, 40, 121, 16))
        self.label_12.setObjectName("label_12")

        w = QtGui.QWidget()
        p = w.palette()
        

        self.LegColourFarm = QtGui.QWidget(self.groupBox_2)
        self.LegColourFarm.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.LegColourFarm.setAutoFillBackground(True)
        self.LegColourFarm.setObjectName("LegColourFarm")
        p.setColor(w.backgroundRole(), QtGui.QColor(0,200,0))
        self.LegColourFarm.setPalette(p)

        self.legColourLocal = QtGui.QWidget(self.groupBox_2)
        self.legColourLocal.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.legColourLocal.setAutoFillBackground(True)
        self.legColourLocal.setObjectName("legColourLocal")
        p.setColor(w.backgroundRole(), QtGui.QColor(200,200,0))
        self.legColourLocal.setPalette(p)

        self.legColourTex = QtGui.QWidget(self.groupBox_2)
        self.legColourTex.setGeometry(QtCore.QRect(180, 20, 31, 16))
        self.legColourTex.setAutoFillBackground(True)
        self.legColourTex.setObjectName("legColourTex")
        p.setColor(w.backgroundRole(), QtGui.QColor(200,0,0))
        self.legColourTex.setPalette(p)

        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1421, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "UH Render Farm Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Workspace", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUpdatePaths.setText(QtGui.QApplication.translate("MainWindow", "Update Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.rbLocal.setText(QtGui.QApplication.translate("MainWindow", "Local", None, QtGui.QApplication.UnicodeUTF8))
        self.rbRenderFarm.setText(QtGui.QApplication.translate("MainWindow", "Render Farm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Selecting a Location and press the update button you can swap your paths from being local to being renderfarm ready. ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "RenderFarm Tools v2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Submit Job to Renderfarm", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSpool.setText(QtGui.QApplication.translate("MainWindow", "Submit To Farm", None, QtGui.QApplication.UnicodeUTF8))
        self.cboJobType.setItemText(0, QtGui.QApplication.translate("MainWindow", "Full Render", None, QtGui.QApplication.UnicodeUTF8))
        self.cboJobType.setItemText(1, QtGui.QApplication.translate("MainWindow", "Test Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Select Job Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "The UH Renderfarm is for NON-COMMERCIAL USE ONLY.  You must collect all files from the renderfarm storage server within a week of job completion to avoid deletion.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "File Summary:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblWorkspace.setText(QtGui.QApplication.translate("MainWindow", "Project Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Project Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Scene Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSceneName.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Renderer:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRenderer.setText(QtGui.QApplication.translate("MainWindow", "Renderer", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFrameRange.setText(QtGui.QApplication.translate("MainWindow", "Renderer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Frame Range:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Automated Quality Checks", None, QtGui.QApplication.UnicodeUTF8))
        self.cbMissingTextures.setText(QtGui.QApplication.translate("MainWindow", "No Missing Textures", None, QtGui.QApplication.UnicodeUTF8))
        self.cbNoJpg.setText(QtGui.QApplication.translate("MainWindow", "No Illegal Textures", None, QtGui.QApplication.UnicodeUTF8))
        self.cbTurtle.setText(QtGui.QApplication.translate("MainWindow", "Turtle not loaded", None, QtGui.QApplication.UnicodeUTF8))
        self.cbNoUncached.setText(QtGui.QApplication.translate("MainWindow", "No Uncached Dynamics", None, QtGui.QApplication.UnicodeUTF8))
        self.cbProject.setText(QtGui.QApplication.translate("MainWindow", "Project Set Correctly", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "If your Scene passes all quality checks then the boxes on the right will all be ticked (you cannot edit these yourselves)  only then will the send to tractor button be unlocked", None, QtGui.QApplication.UnicodeUTF8))
        self.lblQCFeedback.setText(QtGui.QApplication.translate("MainWindow", "Failed", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Missing Texture", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Paths good for Farm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Paths good for Local", None, QtGui.QApplication.UnicodeUTF8))
