import maya.cmds as cmds
#Settings Control
def create(n,suf):
    n=str(n+suf)
    c=[]
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40\
                ],\
                point = [\
                            (0.0, 2.43, 2.61),\
                            (0.49, 1.95, 2.53),\
                            (0.98, 1.49, 2.36),\
                            (1.47, 1.07, 2.11),\
                            (0.98, 1.07, 2.11),\
                            (0.49, 1.07, 2.11),\
                            (0.49, 0.7, 1.79),\
                            (0.49, 0.4, 1.4),\
                            (0.49, 0.18, 0.96),\
                            (0.49, 0.05, 0.49),\
                            (0.49, 0.0, 0.0),\
                            (0.49, 0.05, -0.49),\
                            (0.49, 0.18, -0.96),\
                            (0.49, 0.4, -1.4),\
                            (0.49, 0.7, -1.79),\
                            (0.49, 1.07, -2.11),\
                            (0.98, 1.07, -2.11),\
                            (1.47, 1.07, -2.11),\
                            (0.98, 1.49, -2.36),\
                            (0.49, 1.95, -2.53),\
                            (0.0, 2.43, -2.61),\
                            (-0.49, 1.95, -2.53),\
                            (-0.98, 1.49, -2.36),\
                            (-1.47, 1.07, -2.11),\
                            (-0.98, 1.07, -2.11),\
                            (-0.49, 1.07, -2.11),\
                            (-0.49, 0.7, -1.79),\
                            (-0.49, 0.4, -1.4),\
                            (-0.49, 0.18, -0.96),\
                            (-0.49, 0.05, -0.49),\
                            (-0.49, 0.0, 0.0),\
                            (-0.49, 0.05, 0.49),\
                            (-0.49, 0.18, 0.96),\
                            (-0.49, 0.4, 1.4),\
                            (-0.49, 0.7, 1.79),\
                            (-0.49, 1.07, 2.11),\
                            (-0.98, 1.07, 2.11),\
                            (-1.47, 1.07, 2.11),\
                            (-0.98, 1.49, 2.36),\
                            (-0.49, 1.95, 2.53),\
                            (0.0, 2.43, 2.61)\
                ]\
              ))
    cmds.rename(c[0],n)
    c[0]=n
    return c