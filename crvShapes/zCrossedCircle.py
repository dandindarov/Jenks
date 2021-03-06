import maya.cmds as cmds
#Settings Control
def create(n,suf):
    n=str(n+suf)
    c=[]
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66\
                ],\
                point = [\
                            (-2.0, -0.0, 0.0),\
                            (-1.98, -0.0, 0.31),\
                            (-1.9, -0.0, 0.62),\
                            (-1.78, -0.0, 0.91),\
                            (-1.62, -0.0, 1.18),\
                            (-1.41, -0.0, 1.41),\
                            (-1.18, -0.0, 1.62),\
                            (-0.91, -0.0, 1.78),\
                            (-0.62, -0.0, 1.9),\
                            (-0.31, -0.0, 1.98),\
                            (-0.0, 0.0, 2.0),\
                            (0.31, 0.0, 1.98),\
                            (0.62, 0.0, 1.9),\
                            (0.91, 0.0, 1.78),\
                            (1.18, 0.0, 1.62),\
                            (1.41, 0.0, 1.41),\
                            (1.62, 0.0, 1.18),\
                            (1.78, 0.0, 0.91),\
                            (1.9, 0.0, 0.62),\
                            (1.98, 0.0, 0.31),\
                            (2.0, 0.0, -0.0),\
                            (-0.0, -0.0, -0.0),\
                            (-2.0, -0.0, 0.0),\
                            (-1.98, 0.0, -0.31),\
                            (-1.9, 0.0, -0.62),\
                            (-1.78, 0.0, -0.91),\
                            (-1.62, 0.0, -1.18),\
                            (-1.41, 0.0, -1.41),\
                            (-1.18, 0.0, -1.62),\
                            (-0.91, 0.0, -1.78),\
                            (-0.62, 0.0, -1.9),\
                            (-0.31, 0.0, -1.98),\
                            (-0.0, 0.0, -2.0),\
                            (-0.0, -0.0, -0.0),\
                            (-0.0, -0.0, 2.0),\
                            (0.31, -0.0, 1.98),\
                            (0.62, -0.0, 1.9),\
                            (0.91, -0.0, 1.78),\
                            (1.18, -0.0, 1.62),\
                            (1.41, -0.0, 1.41),\
                            (1.62, -0.0, 1.18),\
                            (1.78, -0.0, 0.91),\
                            (1.9, -0.0, 0.62),\
                            (1.98, -0.0, 0.31),\
                            (2.0, -0.0, -0.0),\
                            (1.98, -0.0, -0.31),\
                            (1.9, -0.0, -0.62),\
                            (1.78, -0.0, -0.91),\
                            (1.62, -0.0, -1.18),\
                            (1.41, -0.0, -1.41),\
                            (1.18, -0.0, -1.62),\
                            (0.91, -0.0, -1.78),\
                            (0.62, -0.0, -1.9),\
                            (0.31, -0.0, -1.98),\
                            (-0.0, -0.0, -2.0),\
                            (-0.31, -0.0, -1.98),\
                            (-0.62, -0.0, -1.9),\
                            (-0.91, -0.0, -1.78),\
                            (-1.18, -0.0, -1.62),\
                            (-1.41, -0.0, -1.41),\
                            (-1.62, -0.0, -1.18),\
                            (-1.78, -0.0, -0.91),\
                            (-1.9, -0.0, -0.62),\
                            (-1.98, -0.0, -0.31),\
                            (-2.0, -0.0, -0.0),\
                            (-2.0, -0.0, 0.06),\
                            (-2.0, -0.0, 0.0)\
                ]\
              ))
    cmds.rename(c[0],n)
    c[0]=n
    return c