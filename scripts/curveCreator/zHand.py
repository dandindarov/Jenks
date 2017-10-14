import maya.cmds as cmds
#Settings Control
def create(n,suf):
    n=str(n+suf)
    c=[]
    c.append(cmds.curve(degree = 3,\
                knot = [\
                        0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 80, 80\
                ],\
                point = [\
                            (-2.1, 0.39, 0.0),\
                            (-2.03, 0.32, 0.0),\
                            (-1.9, 0.18, 0.0),\
                            (-1.72, -0.06, 0.0),\
                            (-1.58, -0.31, 0.0),\
                            (-1.47, -0.58, 0.0),\
                            (-1.39, -0.86, 0.0),\
                            (-1.35, -1.15, 0.0),\
                            (-1.3, -1.44, 0.0),\
                            (-1.21, -1.72, 0.0),\
                            (-1.1, -1.98, 0.0),\
                            (-0.95, -2.25, 0.0),\
                            (-0.65, -2.32, 0.0),\
                            (-0.37, -2.37, 0.0),\
                            (-0.07, -2.36, 0.0),\
                            (0.21, -2.3, 0.0),\
                            (0.48, -2.18, 0.0),\
                            (0.72, -2.01, 0.0),\
                            (0.93, -1.8, 0.0),\
                            (1.17, -1.65, 0.0),\
                            (1.43, -1.5, 0.0),\
                            (1.59, -1.25, 0.0),\
                            (1.73, -0.99, 0.0),\
                            (1.96, -0.82, 0.0),\
                            (2.31, -0.77, 0.0),\
                            (2.2, -0.41, 0.0),\
                            (1.94, -0.26, 0.0),\
                            (1.64, -0.32, 0.0),\
                            (1.39, -0.48, 0.0),\
                            (1.18, -0.65, 0.0),\
                            (0.9, -0.85, 0.0),\
                            (0.64, -0.63, 0.0),\
                            (0.64, -0.33, 0.0),\
                            (0.63, -0.04, 0.0),\
                            (0.67, 0.25, 0.0),\
                            (0.71, 0.54, 0.0),\
                            (0.77, 0.82, 0.0),\
                            (0.82, 1.11, 0.0),\
                            (0.84, 1.41, 0.0),\
                            (0.82, 1.69, 0.0),\
                            (0.69, 1.98, 0.0),\
                            (0.34, 2.01, 0.0),\
                            (0.25, 1.66, 0.0),\
                            (0.2, 1.43, 0.0),\
                            (0.16, 1.07, 0.0),\
                            (0.14, 0.89, 0.0),\
                            (0.09, 0.41, 0.0),\
                            (0.01, 0.62, 0.0),\
                            (0.06, 0.97, 0.0),\
                            (0.04, 1.23, 0.0),\
                            (0.04, 1.53, 0.0),\
                            (-0.0, 1.82, 0.0),\
                            (-0.06, 2.1, 0.0),\
                            (-0.27, 2.37, 0.0),\
                            (-0.6, 2.26, 0.0),\
                            (-0.63, 1.94, 0.0),\
                            (-0.65, 1.66, 0.0),\
                            (-0.63, 1.38, 0.0),\
                            (-0.6, 1.05, 0.0),\
                            (-0.59, 0.83, 0.0),\
                            (-0.52, 0.41, 0.0),\
                            (-0.63, 0.37, 0.0),\
                            (-0.7, 0.81, 0.0),\
                            (-0.77, 1.01, 0.0),\
                            (-0.84, 1.33, 0.0),\
                            (-0.94, 1.59, 0.0),\
                            (-1.02, 1.87, 0.0),\
                            (-1.34, 2.06, 0.0),\
                            (-1.54, 1.79, 0.0),\
                            (-1.48, 1.49, 0.0),\
                            (-1.45, 1.2, 0.0),\
                            (-1.36, 0.93, 0.0),\
                            (-1.27, 0.63, 0.0),\
                            (-1.2, 0.4, 0.0),\
                            (-1.05, 0.01, 0.0),\
                            (-1.36, 0.29, 0.0),\
                            (-1.5, 0.49, 0.0),\
                            (-1.71, 0.73, 0.0),\
                            (-1.91, 0.9, 0.0),\
                            (-2.28, 0.96, 0.0),\
                            (-2.31, 0.6, 0.0),\
                            (-2.16, 0.46, 0.0),\
                            (-2.1, 0.39, 0.0)\
                ]\
              ))
    cmds.rename(c[0],n)
    c[0]=n
    return c