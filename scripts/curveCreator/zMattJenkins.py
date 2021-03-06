import maya.cmds as cmds
#Settings Control
def create(n,suf):
    n=str(n+suf)
    c=[]
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\
                ],\
                point = [\
                            (0.16, 0.27, -0.05),\
                            (0.16, 0.26, 0.27),\
                            (0.08, 0.26, 0.27),\
                            (0.08, 0.27, -0.27),\
                            (0.34, 0.27, 0.01),\
                            (0.6, 0.27, -0.27),\
                            (0.6, 0.26, 0.27),\
                            (0.52, 0.26, 0.27),\
                            (0.52, 0.27, -0.05),\
                            (0.34, 0.27, 0.13),\
                            (0.16, 0.27, -0.05)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\
                ],\
                point = [\
                            (0.15, 0.27, -0.08),\
                            (0.15, 0.26, 0.26),\
                            (0.09, 0.26, 0.26),\
                            (0.09, 0.27, -0.24),\
                            (0.34, 0.27, 0.02),\
                            (0.59, 0.27, -0.24),\
                            (0.59, 0.26, 0.26),\
                            (0.53, 0.26, 0.26),\
                            (0.53, 0.27, -0.08),\
                            (0.34, 0.27, 0.11),\
                            (0.15, 0.27, -0.08)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3\
                ],\
                point = [\
                            (0.94, 0.27, 0.09),\
                            (1.1, 0.27, 0.09),\
                            (1.02, 0.27, -0.07),\
                            (0.94, 0.27, 0.09)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3\
                ],\
                point = [\
                            (0.96, 0.27, 0.08),\
                            (1.08, 0.27, 0.08),\
                            (1.02, 0.27, -0.04),\
                            (0.96, 0.27, 0.08)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7\
                ],\
                point = [\
                            (1.14, 0.26, 0.18),\
                            (0.9, 0.26, 0.18),\
                            (0.85, 0.26, 0.27),\
                            (0.76, 0.26, 0.27),\
                            (1.02, 0.27, -0.27),\
                            (1.28, 0.26, 0.27),\
                            (1.19, 0.26, 0.27),\
                            (1.14, 0.26, 0.18)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7\
                ],\
                point = [\
                            (1.15, 0.26, 0.17),\
                            (0.89, 0.26, 0.17),\
                            (0.84, 0.26, 0.26),\
                            (0.78, 0.26, 0.26),\
                            (1.02, 0.27, -0.24),\
                            (1.26, 0.26, 0.26),\
                            (1.2, 0.26, 0.26),\
                            (1.15, 0.26, 0.17)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8\
                ],\
                point = [\
                            (1.29, 0.27, -0.27),\
                            (1.73, 0.27, -0.27),\
                            (1.73, 0.27, -0.17),\
                            (1.55, 0.27, -0.17),\
                            (1.55, 0.26, 0.27),\
                            (1.46, 0.26, 0.27),\
                            (1.46, 0.27, -0.17),\
                            (1.29, 0.27, -0.17),\
                            (1.29, 0.27, -0.27)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8\
                ],\
                point = [\
                            (1.3, 0.27, -0.26),\
                            (1.72, 0.27, -0.26),\
                            (1.72, 0.27, -0.18),\
                            (1.54, 0.27, -0.18),\
                            (1.54, 0.26, 0.26),\
                            (1.47, 0.26, 0.26),\
                            (1.47, 0.27, -0.18),\
                            (1.3, 0.27, -0.18),\
                            (1.3, 0.27, -0.26)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8\
                ],\
                point = [\
                            (1.88, 0.27, -0.27),\
                            (2.32, 0.27, -0.27),\
                            (2.32, 0.27, -0.17),\
                            (2.14, 0.27, -0.17),\
                            (2.14, 0.26, 0.27),\
                            (2.06, 0.26, 0.27),\
                            (2.06, 0.27, -0.17),\
                            (1.88, 0.27, -0.17),\
                            (1.88, 0.27, -0.27)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8\
                ],\
                point = [\
                            (1.89, 0.27, -0.26),\
                            (2.31, 0.27, -0.26),\
                            (2.31, 0.27, -0.18),\
                            (2.13, 0.27, -0.18),\
                            (2.13, 0.26, 0.26),\
                            (2.07, 0.26, 0.26),\
                            (2.07, 0.27, -0.18),\
                            (1.89, 0.27, -0.18),\
                            (1.89, 0.27, -0.26)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21\
                ],\
                point = [\
                            (2.91, 0.26, 0.16),\
                            (2.94, 0.26, 0.18),\
                            (2.97, 0.26, 0.18),\
                            (3.01, 0.26, 0.18),\
                            (3.04, 0.26, 0.16),\
                            (3.06, 0.27, 0.13),\
                            (3.06, 0.27, 0.09),\
                            (3.06, 0.27, -0.08),\
                            (3.06, 0.27, -0.27),\
                            (3.11, 0.27, -0.27),\
                            (3.15, 0.27, -0.27),\
                            (3.15, 0.27, -0.08),\
                            (3.15, 0.27, 0.09),\
                            (3.15, 0.26, 0.17),\
                            (3.1, 0.26, 0.22),\
                            (3.05, 0.26, 0.27),\
                            (2.97, 0.26, 0.27),\
                            (2.9, 0.26, 0.27),\
                            (2.85, 0.26, 0.22),\
                            (2.88, 0.26, 0.18),\
                            (2.91, 0.26, 0.16),\
                            (2.91, 0.26, 0.16)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20\
                ],\
                point = [\
                            (2.91, 0.26, 0.17),\
                            (2.94, 0.26, 0.18),\
                            (2.97, 0.26, 0.18),\
                            (3.01, 0.26, 0.18),\
                            (3.05, 0.26, 0.16),\
                            (3.07, 0.27, 0.13),\
                            (3.07, 0.27, 0.09),\
                            (3.07, 0.27, -0.09),\
                            (3.07, 0.27, -0.26),\
                            (3.11, 0.27, -0.26),\
                            (3.14, 0.27, -0.26),\
                            (3.14, 0.27, -0.09),\
                            (3.14, 0.27, 0.09),\
                            (3.14, 0.26, 0.16),\
                            (3.09, 0.26, 0.21),\
                            (3.05, 0.26, 0.26),\
                            (2.97, 0.26, 0.26),\
                            (2.9, 0.26, 0.26),\
                            (2.86, 0.26, 0.21),\
                            (2.89, 0.26, 0.19),\
                            (2.91, 0.26, 0.17)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\
                ],\
                point = [\
                            (3.65, 0.27, -0.27),\
                            (3.65, 0.27, -0.17),\
                            (3.39, 0.27, -0.17),\
                            (3.39, 0.27, -0.04),\
                            (3.65, 0.27, -0.04),\
                            (3.65, 0.27, 0.05),\
                            (3.39, 0.27, 0.05),\
                            (3.39, 0.26, 0.18),\
                            (3.65, 0.26, 0.18),\
                            (3.65, 0.26, 0.27),\
                            (3.3, 0.26, 0.27),\
                            (3.3, 0.27, -0.27),\
                            (3.65, 0.27, -0.27)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\
                ],\
                point = [\
                            (3.64, 0.27, -0.26),\
                            (3.64, 0.27, -0.18),\
                            (3.38, 0.27, -0.18),\
                            (3.38, 0.27, -0.04),\
                            (3.64, 0.27, -0.04),\
                            (3.64, 0.27, 0.03),\
                            (3.38, 0.27, 0.03),\
                            (3.38, 0.26, 0.18),\
                            (3.64, 0.26, 0.18),\
                            (3.64, 0.26, 0.26),\
                            (3.31, 0.26, 0.26),\
                            (3.31, 0.27, -0.26),\
                            (3.64, 0.27, -0.26)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\
                ],\
                point = [\
                            (3.81, 0.27, -0.27),\
                            (4.16, 0.27, 0.06),\
                            (4.16, 0.27, -0.27),\
                            (4.25, 0.27, -0.27),\
                            (4.25, 0.26, 0.27),\
                            (4.25, 0.26, 0.27),\
                            (4.25, 0.26, 0.27),\
                            (3.89, 0.27, -0.05),\
                            (3.89, 0.26, 0.27),\
                            (3.81, 0.26, 0.27),\
                            (3.81, 0.27, -0.27)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8\
                ],\
                point = [\
                            (3.82, 0.27, -0.24),\
                            (4.17, 0.27, 0.08),\
                            (4.17, 0.27, -0.26),\
                            (4.24, 0.27, -0.26),\
                            (4.24, 0.26, 0.24),\
                            (3.88, 0.27, -0.08),\
                            (3.88, 0.26, 0.26),\
                            (3.82, 0.26, 0.26),\
                            (3.82, 0.27, -0.24)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\
                ],\
                point = [\
                            (4.57, 0.27, 0.01),\
                            (4.84, 0.26, 0.27),\
                            (4.71, 0.26, 0.27),\
                            (4.48, 0.27, 0.04),\
                            (4.48, 0.26, 0.27),\
                            (4.4, 0.26, 0.27),\
                            (4.4, 0.27, -0.27),\
                            (4.48, 0.27, -0.27),\
                            (4.48, 0.27, -0.03),\
                            (4.71, 0.27, -0.27),\
                            (4.84, 0.27, -0.27),\
                            (4.57, 0.27, 0.01)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\
                ],\
                point = [\
                            (4.56, 0.27, 0.01),\
                            (4.82, 0.26, 0.26),\
                            (4.71, 0.26, 0.26),\
                            (4.47, 0.27, 0.01),\
                            (4.47, 0.26, 0.26),\
                            (4.41, 0.26, 0.26),\
                            (4.41, 0.27, -0.26),\
                            (4.47, 0.27, -0.26),\
                            (4.47, 0.27, -0.01),\
                            (4.71, 0.27, -0.26),\
                            (4.82, 0.27, -0.26),\
                            (4.56, 0.27, 0.01)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4\
                ],\
                point = [\
                            (4.99, 0.27, -0.27),\
                            (5.08, 0.27, -0.27),\
                            (5.08, 0.26, 0.27),\
                            (4.99, 0.26, 0.27),\
                            (4.99, 0.27, -0.27)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4\
                ],\
                point = [\
                            (5.0, 0.27, -0.26),\
                            (5.07, 0.27, -0.26),\
                            (5.07, 0.26, 0.26),\
                            (5.0, 0.26, 0.26),\
                            (5.0, 0.27, -0.26)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\
                ],\
                point = [\
                            (5.23, 0.27, -0.27),\
                            (5.58, 0.27, 0.06),\
                            (5.58, 0.27, -0.27),\
                            (5.67, 0.27, -0.27),\
                            (5.67, 0.26, 0.27),\
                            (5.67, 0.26, 0.27),\
                            (5.67, 0.26, 0.27),\
                            (5.32, 0.27, -0.05),\
                            (5.32, 0.26, 0.27),\
                            (5.23, 0.26, 0.27),\
                            (5.23, 0.27, -0.27)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8\
                ],\
                point = [\
                            (5.24, 0.27, -0.24),\
                            (5.59, 0.27, 0.08),\
                            (5.59, 0.27, -0.26),\
                            (5.66, 0.27, -0.26),\
                            (5.66, 0.26, 0.24),\
                            (5.31, 0.27, -0.08),\
                            (5.31, 0.26, 0.26),\
                            (5.24, 0.26, 0.26),\
                            (5.24, 0.27, -0.24)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51\
                ],\
                point = [\
                            (5.97, 0.27, 0.05),\
                            (5.91, 0.27, 0.05),\
                            (5.86, 0.27, 0.01),\
                            (5.82, 0.27, -0.04),\
                            (5.82, 0.27, -0.1),\
                            (5.82, 0.27, -0.17),\
                            (5.86, 0.27, -0.21),\
                            (5.91, 0.27, -0.27),\
                            (5.97, 0.27, -0.27),\
                            (6.12, 0.27, -0.27),\
                            (6.26, 0.27, -0.27),\
                            (6.26, 0.27, -0.21),\
                            (6.26, 0.27, -0.17),\
                            (6.12, 0.27, -0.17),\
                            (5.97, 0.27, -0.17),\
                            (5.96, 0.27, -0.17),\
                            (5.93, 0.27, -0.16),\
                            (5.92, 0.27, -0.14),\
                            (5.91, 0.27, -0.13),\
                            (5.91, 0.27, -0.1),\
                            (5.91, 0.27, -0.08),\
                            (5.93, 0.27, -0.07),\
                            (5.94, 0.27, -0.04),\
                            (5.97, 0.27, -0.04),\
                            (6.04, 0.27, -0.04),\
                            (6.1, 0.27, -0.04),\
                            (6.17, 0.27, -0.04),\
                            (6.21, 0.27, 0.01),\
                            (6.26, 0.27, 0.05),\
                            (6.26, 0.27, 0.12),\
                            (6.26, 0.26, 0.18),\
                            (6.21, 0.26, 0.23),\
                            (6.17, 0.26, 0.27),\
                            (6.1, 0.26, 0.27),\
                            (5.96, 0.26, 0.27),\
                            (5.82, 0.26, 0.27),\
                            (5.82, 0.26, 0.23),\
                            (5.82, 0.26, 0.18),\
                            (5.96, 0.26, 0.18),\
                            (6.1, 0.26, 0.18),\
                            (6.12, 0.26, 0.18),\
                            (6.14, 0.26, 0.17),\
                            (6.16, 0.26, 0.15),\
                            (6.17, 0.27, 0.13),\
                            (6.17, 0.27, 0.12),\
                            (6.17, 0.27, 0.09),\
                            (6.15, 0.27, 0.07),\
                            (6.13, 0.27, 0.05),\
                            (6.1, 0.27, 0.05),\
                            (6.04, 0.27, 0.05),\
                            (5.97, 0.27, 0.05),\
                            (5.97, 0.27, 0.05)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50\
                ],\
                point = [\
                            (5.97, 0.27, 0.03),\
                            (5.91, 0.27, 0.03),\
                            (5.87, 0.27, -0.0),\
                            (5.83, 0.27, -0.05),\
                            (5.83, 0.27, -0.11),\
                            (5.83, 0.27, -0.17),\
                            (5.87, 0.27, -0.21),\
                            (5.91, 0.27, -0.26),\
                            (5.97, 0.27, -0.26),\
                            (6.12, 0.27, -0.26),\
                            (6.25, 0.27, -0.26),\
                            (6.25, 0.27, -0.21),\
                            (6.25, 0.27, -0.18),\
                            (6.12, 0.27, -0.18),\
                            (5.97, 0.27, -0.18),\
                            (5.96, 0.27, -0.18),\
                            (5.92, 0.27, -0.17),\
                            (5.91, 0.27, -0.15),\
                            (5.9, 0.27, -0.13),\
                            (5.9, 0.27, -0.11),\
                            (5.9, 0.27, -0.08),\
                            (5.92, 0.27, -0.06),\
                            (5.93, 0.27, -0.04),\
                            (5.97, 0.27, -0.04),\
                            (6.04, 0.27, -0.04),\
                            (6.1, 0.27, -0.04),\
                            (6.17, 0.27, -0.04),\
                            (6.2, 0.27, 0.01),\
                            (6.25, 0.27, 0.05),\
                            (6.25, 0.27, 0.11),\
                            (6.25, 0.26, 0.17),\
                            (6.2, 0.26, 0.22),\
                            (6.17, 0.26, 0.26),\
                            (6.1, 0.26, 0.26),\
                            (5.96, 0.26, 0.26),\
                            (5.83, 0.26, 0.26),\
                            (5.83, 0.26, 0.23),\
                            (5.83, 0.26, 0.18),\
                            (5.96, 0.26, 0.18),\
                            (6.1, 0.26, 0.18),\
                            (6.12, 0.26, 0.18),\
                            (6.15, 0.26, 0.17),\
                            (6.17, 0.26, 0.15),\
                            (6.18, 0.27, 0.13),\
                            (6.18, 0.27, 0.11),\
                            (6.18, 0.27, 0.08),\
                            (6.16, 0.27, 0.06),\
                            (6.13, 0.27, 0.03),\
                            (6.1, 0.27, 0.03),\
                            (6.04, 0.27, 0.03),\
                            (5.97, 0.27, 0.03)\
                ]\
              ))
    cmds.rename(c[0],n)
    c[0]=n
    return c