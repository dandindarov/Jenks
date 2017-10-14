import maya.cmds as cmds
#Settings Control
def create(n,suf):
    n=str(n+suf)
    c=[]
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110\
                ],\
                point = [\
                            (2.53, 0.18, -0.0),\
                            (2.52, 0.27, -0.0),\
                            (2.8, 0.42, -0.0),\
                            (2.94, 0.51, -0.0),\
                            (2.9, 0.73, -0.0),\
                            (2.84, 0.94, -0.0),\
                            (2.75, 1.15, -0.0),\
                            (2.59, 1.15, -0.0),\
                            (2.27, 1.12, -0.0),\
                            (2.23, 1.2, -0.0),\
                            (2.03, 1.51, -0.0),\
                            (1.97, 1.58, -0.0),\
                            (2.13, 1.85, -0.0),\
                            (2.2, 2.0, -0.0),\
                            (2.05, 2.17, -0.0),\
                            (1.88, 2.31, -0.0),\
                            (1.7, 2.44, -0.0),\
                            (1.56, 2.35, -0.0),\
                            (1.31, 2.15, -0.0),\
                            (1.23, 2.2, -0.0),\
                            (0.9, 2.35, -0.0),\
                            (0.81, 2.38, -0.0),\
                            (0.8, 2.7, -0.0),\
                            (0.77, 2.86, -0.0),\
                            (0.56, 2.92, -0.0),\
                            (0.33, 2.95, -0.0),\
                            (0.11, 2.96, -0.0),\
                            (0.04, 2.81, -0.0),\
                            (-0.06, 2.51, -0.0),\
                            (-0.15, 2.5, -0.0),\
                            (-0.51, 2.45, -0.0),\
                            (-0.6, 2.43, -0.0),\
                            (-0.79, 2.69, -0.0),\
                            (-0.89, 2.82, -0.0),\
                            (-1.11, 2.74, -0.0),\
                            (-1.31, 2.65, -0.0),\
                            (-1.5, 2.53, -0.0),\
                            (-1.48, 2.37, -0.0),\
                            (-1.4, 2.06, -0.0),\
                            (-1.48, 2.01, -0.0),\
                            (-1.76, 1.77, -0.0),\
                            (-1.82, 1.7, -0.0),\
                            (-2.11, 1.82, -0.0),\
                            (-2.27, 1.87, -0.0),\
                            (-2.41, 1.7, -0.0),\
                            (-2.54, 1.51, -0.0),\
                            (-2.63, 1.31, -0.0),\
                            (-2.52, 1.19, -0.0),\
                            (-2.29, 0.97, -0.0),\
                            (-2.32, 0.88, -0.0),\
                            (-2.44, 0.53, -0.0),\
                            (-2.45, 0.44, -0.0),\
                            (-2.76, 0.38, -0.0),\
                            (-2.92, 0.33, -0.0),\
                            (-2.94, 0.11, -0.0),\
                            (-2.94, -0.11, -0.0),\
                            (-2.92, -0.34, -0.0),\
                            (-2.76, -0.38, -0.0),\
                            (-2.45, -0.44, -0.0),\
                            (-2.44, -0.53, -0.0),\
                            (-2.32, -0.88, -0.0),\
                            (-2.29, -0.97, -0.0),\
                            (-2.52, -1.19, -0.0),\
                            (-2.63, -1.31, -0.0),\
                            (-2.54, -1.51, -0.0),\
                            (-2.41, -1.7, -0.0),\
                            (-2.27, -1.87, -0.0),\
                            (-2.11, -1.83, -0.0),\
                            (-1.82, -1.71, -0.0),\
                            (-1.76, -1.78, -0.0),\
                            (-1.48, -2.01, -0.0),\
                            (-1.4, -2.07, -0.0),\
                            (-1.48, -2.38, -0.0),\
                            (-1.5, -2.54, -0.0),\
                            (-1.31, -2.66, -0.0),\
                            (-1.11, -2.74, -0.0),\
                            (-0.89, -2.82, -0.0),\
                            (-0.79, -2.7, -0.0),\
                            (-0.6, -2.43, -0.0),\
                            (-0.51, -2.46, -0.0),\
                            (-0.15, -2.5, -0.0),\
                            (-0.06, -2.51, -0.0),\
                            (0.04, -2.81, -0.0),\
                            (0.11, -2.96, -0.0),\
                            (0.33, -2.95, -0.0),\
                            (0.56, -2.93, -0.0),\
                            (0.77, -2.86, -0.0),\
                            (0.8, -2.7, -0.0),\
                            (0.81, -2.38, -0.0),\
                            (0.9, -2.35, -0.0),\
                            (1.23, -2.2, -0.0),\
                            (1.31, -2.15, -0.0),\
                            (1.56, -2.36, -0.0),\
                            (1.7, -2.44, -0.0),\
                            (1.88, -2.31, -0.0),\
                            (2.05, -2.17, -0.0),\
                            (2.2, -2.0, -0.0),\
                            (2.13, -1.86, -0.0),\
                            (1.97, -1.58, -0.0),\
                            (2.03, -1.51, -0.0),\
                            (2.23, -1.2, -0.0),\
                            (2.27, -1.12, -0.0),\
                            (2.59, -1.15, -0.0),\
                            (2.75, -1.15, -0.0),\
                            (2.84, -0.94, -0.0),\
                            (2.9, -0.73, -0.0),\
                            (2.94, -0.51, -0.0),\
                            (2.8, -0.42, -0.0),\
                            (2.52, -0.27, -0.0),\
                            (2.53, -0.18, -0.0),\
                            (2.53, 0.18, -0.0)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110\
                ],\
                point = [\
                            (2.52, 0.18, 0.0),\
                            (2.51, 0.28, 0.0),\
                            (2.79, 0.43, 0.0),\
                            (2.93, 0.51, 0.0),\
                            (2.89, 0.73, 0.0),\
                            (2.83, 0.94, 0.0),\
                            (2.74, 1.14, 0.0),\
                            (2.59, 1.14, 0.0),\
                            (2.26, 1.11, 0.0),\
                            (2.22, 1.2, 0.0),\
                            (2.02, 1.5, 0.0),\
                            (1.96, 1.58, 0.0),\
                            (2.12, 1.85, 0.0),\
                            (2.19, 2.0, 0.0),\
                            (2.04, 2.16, 0.0),\
                            (1.87, 2.3, 0.0),\
                            (1.7, 2.43, 0.0),\
                            (1.57, 2.34, 0.0),\
                            (1.31, 2.14, 0.0),\
                            (1.23, 2.19, 0.0),\
                            (0.9, 2.34, 0.0),\
                            (0.8, 2.37, 0.0),\
                            (0.79, 2.7, 0.0),\
                            (0.76, 2.85, 0.0),\
                            (0.56, 2.91, 0.0),\
                            (0.33, 2.94, 0.0),\
                            (0.12, 2.95, 0.0),\
                            (0.05, 2.81, 0.0),\
                            (-0.05, 2.5, 0.0),\
                            (-0.15, 2.49, 0.0),\
                            (-0.51, 2.44, 0.0),\
                            (-0.6, 2.42, 0.0),\
                            (-0.8, 2.68, 0.0),\
                            (-0.89, 2.81, 0.0),\
                            (-1.11, 2.73, 0.0),\
                            (-1.31, 2.64, 0.0),\
                            (-1.49, 2.52, 0.0),\
                            (-1.47, 2.37, -0.0),\
                            (-1.39, 2.06, 0.0),\
                            (-1.47, 2.0, 0.0),\
                            (-1.75, 1.76, 0.0),\
                            (-1.82, 1.69, 0.0),\
                            (-2.11, 1.81, 0.0),\
                            (-2.27, 1.86, 0.0),\
                            (-2.4, 1.69, 0.0),\
                            (-2.53, 1.51, 0.0),\
                            (-2.62, 1.31, 0.0),\
                            (-2.51, 1.2, -0.0),\
                            (-2.28, 0.97, 0.0),\
                            (-2.31, 0.88, 0.0),\
                            (-2.43, 0.53, 0.0),\
                            (-2.44, 0.43, 0.0),\
                            (-2.76, 0.37, 0.0),\
                            (-2.91, 0.32, 0.0),\
                            (-2.93, 0.11, 0.0),\
                            (-2.93, -0.11, 0.0),\
                            (-2.91, -0.33, -0.0),\
                            (-2.76, -0.37, -0.0),\
                            (-2.44, -0.43, -0.0),\
                            (-2.43, -0.53, -0.0),\
                            (-2.31, -0.88, -0.0),\
                            (-2.28, -0.97, 0.0),\
                            (-2.51, -1.2, 0.0),\
                            (-2.62, -1.31, 0.0),\
                            (-2.53, -1.51, -0.0),\
                            (-2.4, -1.69, -0.0),\
                            (-2.27, -1.86, 0.0),\
                            (-2.11, -1.82, 0.0),\
                            (-1.82, -1.7, 0.0),\
                            (-1.75, -1.77, -0.0),\
                            (-1.47, -2.0, -0.0),\
                            (-1.39, -2.07, 0.0),\
                            (-1.47, -2.38, 0.0),\
                            (-1.49, -2.53, 0.0),\
                            (-1.31, -2.65, -0.0),\
                            (-1.11, -2.73, -0.0),\
                            (-0.89, -2.81, 0.0),\
                            (-0.8, -2.69, 0.0),\
                            (-0.6, -2.42, 0.0),\
                            (-0.51, -2.45, -0.0),\
                            (-0.15, -2.49, -0.0),\
                            (-0.05, -2.5, -0.0),\
                            (0.05, -2.81, -0.0),\
                            (0.12, -2.95, 0.0),\
                            (0.33, -2.94, 0.0),\
                            (0.56, -2.92, 0.0),\
                            (0.76, -2.85, 0.0),\
                            (0.79, -2.7, 0.0),\
                            (0.8, -2.37, 0.0),\
                            (0.9, -2.34, 0.0),\
                            (1.23, -2.19, 0.0),\
                            (1.31, -2.14, 0.0),\
                            (1.57, -2.35, -0.0),\
                            (1.7, -2.43, 0.0),\
                            (1.87, -2.3, 0.0),\
                            (2.04, -2.16, 0.0),\
                            (2.19, -2.0, 0.0),\
                            (2.12, -1.86, 0.0),\
                            (1.96, -1.58, 0.0),\
                            (2.02, -1.5, 0.0),\
                            (2.22, -1.2, 0.0),\
                            (2.26, -1.11, 0.0),\
                            (2.59, -1.14, 0.0),\
                            (2.74, -1.14, 0.0),\
                            (2.83, -0.94, 0.0),\
                            (2.89, -0.73, 0.0),\
                            (2.93, -0.51, 0.0),\
                            (2.79, -0.43, 0.0),\
                            (2.51, -0.28, 0.0),\
                            (2.52, -0.18, 0.0),\
                            (2.52, 0.18, 0.0)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111\
                ],\
                point = [\
                            (2.51, 0.18, 0.0),\
                            (2.5, 0.28, 0.0),\
                            (2.79, 0.44, 0.0),\
                            (2.92, 0.52, 0.0),\
                            (2.88, 0.73, 0.0),\
                            (2.82, 0.93, 0.0),\
                            (2.74, 1.13, 0.0),\
                            (2.59, 1.13, 0.0),\
                            (2.26, 1.1, 0.0),\
                            (2.21, 1.19, 0.0),\
                            (2.01, 1.5, 0.0),\
                            (1.95, 1.58, 0.0),\
                            (2.11, 1.86, 0.0),\
                            (2.18, 2.0, 0.0),\
                            (2.04, 2.16, 0.0),\
                            (1.87, 2.29, 0.0),\
                            (1.7, 2.42, 0.0),\
                            (1.57, 2.33, 0.0),\
                            (1.31, 2.13, 0.0),\
                            (1.22, 2.18, 0.0),\
                            (0.89, 2.33, 0.0),\
                            (0.79, 2.37, 0.0),\
                            (0.78, 2.7, 0.0),\
                            (0.75, 2.84, 0.0),\
                            (0.56, 2.9, 0.0),\
                            (0.33, 2.93, 0.0),\
                            (0.12, 2.94, 0.0),\
                            (0.06, 2.8, 0.0),\
                            (-0.05, 2.49, 0.0),\
                            (-0.15, 2.48, 0.0),\
                            (-0.51, 2.43, 0.0),\
                            (-0.61, 2.41, 0.0),\
                            (-0.81, 2.68, 0.0),\
                            (-0.9, 2.8, 0.0),\
                            (-1.1, 2.72, 0.0),\
                            (-1.3, 2.63, 0.0),\
                            (-1.48, 2.52, 0.0),\
                            (-1.46, 2.37, -0.0),\
                            (-1.38, 2.05, 0.0),\
                            (-1.47, 1.99, 0.0),\
                            (-1.75, 1.76, 0.0),\
                            (-1.81, 1.68, 0.0),\
                            (-2.12, 1.8, 0.0),\
                            (-2.26, 1.85, 0.0),\
                            (-2.39, 1.69, 0.0),\
                            (-2.52, 1.5, 0.0),\
                            (-2.61, 1.31, 0.0),\
                            (-2.51, 1.2, -0.0),\
                            (-2.27, 0.98, 0.0),\
                            (-2.3, 0.87, 0.0),\
                            (-2.42, 0.53, 0.0),\
                            (-2.43, 0.42, 0.0),\
                            (-2.76, 0.36, 0.0),\
                            (-2.9, 0.31, 0.0),\
                            (-2.92, 0.11, 0.0),\
                            (-2.92, -0.11, 0.0),\
                            (-2.9, -0.32, -0.0),\
                            (-2.76, -0.36, -0.0),\
                            (-2.43, -0.42, -0.0),\
                            (-2.42, -0.53, -0.0),\
                            (-2.3, -0.87, -0.0),\
                            (-2.27, -0.98, 0.0),\
                            (-2.51, -1.2, 0.0),\
                            (-2.61, -1.31, 0.0),\
                            (-2.52, -1.5, -0.0),\
                            (-2.39, -1.69, -0.0),\
                            (-2.26, -1.85, 0.0),\
                            (-2.12, -1.81, 0.0),\
                            (-1.81, -1.69, 0.0),\
                            (-1.75, -1.77, -0.0),\
                            (-1.47, -1.99, -0.0),\
                            (-1.38, -2.06, 0.0),\
                            (-1.46, -2.38, 0.0),\
                            (-1.48, -2.53, 0.0),\
                            (-1.3, -2.64, -0.0),\
                            (-1.1, -2.72, -0.0),\
                            (-0.9, -2.8, 0.0),\
                            (-0.81, -2.69, 0.0),\
                            (-0.61, -2.41, 0.0),\
                            (-0.51, -2.44, -0.0),\
                            (-0.15, -2.48, -0.0),\
                            (-0.05, -2.49, -0.0),\
                            (0.06, -2.8, -0.0),\
                            (0.12, -2.94, 0.0),\
                            (0.33, -2.93, 0.0),\
                            (0.56, -2.91, 0.0),\
                            (0.75, -2.84, 0.0),\
                            (0.78, -2.7, 0.0),\
                            (0.79, -2.37, 0.0),\
                            (0.89, -2.33, 0.0),\
                            (1.22, -2.18, 0.0),\
                            (1.31, -2.13, 0.0),\
                            (1.57, -2.34, -0.0),\
                            (1.7, -2.42, 0.0),\
                            (1.87, -2.29, 0.0),\
                            (2.04, -2.16, 0.0),\
                            (2.18, -2.0, 0.0),\
                            (2.11, -1.87, 0.0),\
                            (1.95, -1.58, 0.0),\
                            (2.01, -1.5, 0.0),\
                            (2.21, -1.19, 0.0),\
                            (2.26, -1.1, 0.0),\
                            (2.59, -1.13, 0.0),\
                            (2.74, -1.13, 0.0),\
                            (2.82, -0.93, 0.0),\
                            (2.88, -0.73, 0.0),\
                            (2.92, -0.52, 0.0),\
                            (2.79, -0.44, 0.0),\
                            (2.5, -0.28, 0.0),\
                            (2.51, -0.18, 0.0),\
                            (2.51, 0.18, 0.0),\
                            (2.51, 0.18, 0.0)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16\
                ],\
                point = [\
                            (-1.04, 1.6, 0.0),\
                            (-0.64, 1.6, 0.0),\
                            (-0.25, 1.6, 0.0),\
                            (0.24, 1.6, 0.0),\
                            (0.91, 1.3, 0.0),\
                            (1.33, 0.83, 0.0),\
                            (1.52, 0.25, 0.0),\
                            (1.52, -0.04, 0.0),\
                            (1.52, -0.4, 0.0),\
                            (1.26, -0.98, 0.0),\
                            (0.82, -1.38, 0.0),\
                            (0.24, -1.6, 0.0),\
                            (-0.09, -1.6, 0.0),\
                            (-0.56, -1.6, 0.0),\
                            (-1.04, -1.6, 0.0),\
                            (-1.04, -0.0, 0.0),\
                            (-1.04, 1.6, 0.0)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16\
                ],\
                point = [\
                            (-0.16, -1.13, 0.0),\
                            (0.1, -1.13, 0.0),\
                            (0.53, -0.98, 0.0),\
                            (0.85, -0.7, 0.0),\
                            (1.03, -0.28, 0.0),\
                            (1.03, -0.01, 0.0),\
                            (1.03, 0.28, 0.0),\
                            (0.83, 0.71, 0.0),\
                            (0.5, 0.99, 0.0),\
                            (0.1, 1.13, 0.0),\
                            (-0.11, 1.13, 0.0),\
                            (-0.33, 1.13, 0.0),\
                            (-0.55, 1.13, 0.0),\
                            (-0.55, -0.0, 0.0),\
                            (-0.55, -1.13, 0.0),\
                            (-0.36, -1.13, 0.0),\
                            (-0.16, -1.13, 0.0)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16\
                ],\
                point = [\
                            (-1.06, 1.62, 0.0),\
                            (-0.65, 1.62, 0.0),\
                            (-0.25, 1.62, 0.0),\
                            (0.24, 1.62, 0.0),\
                            (0.92, 1.32, 0.0),\
                            (1.34, 0.84, 0.0),\
                            (1.54, 0.25, 0.0),\
                            (1.54, -0.04, 0.0),\
                            (1.54, -0.4, 0.0),\
                            (1.28, -0.99, 0.0),\
                            (0.83, -1.4, 0.0),\
                            (0.24, -1.62, 0.0),\
                            (-0.09, -1.62, 0.0),\
                            (-0.57, -1.62, 0.0),\
                            (-1.06, -1.62, 0.0),\
                            (-1.06, -0.0, 0.0),\
                            (-1.06, 1.62, 0.0)\
                ]\
              ))
    c.append(cmds.curve(degree = 1,\
                knot = [\
                        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16\
                ],\
                point = [\
                            (-0.16, -1.15, 0.0),\
                            (0.1, -1.15, 0.0),\
                            (0.54, -1.0, 0.0),\
                            (0.87, -0.71, 0.0),\
                            (1.05, -0.29, 0.0),\
                            (1.05, -0.01, 0.0),\
                            (1.05, 0.28, 0.0),\
                            (0.84, 0.72, 0.0),\
                            (0.51, 1.01, 0.0),\
                            (0.1, 1.15, 0.0),\
                            (-0.11, 1.15, 0.0),\
                            (-0.34, 1.15, 0.0),\
                            (-0.57, 1.15, 0.0),\
                            (-0.57, -0.0, 0.0),\
                            (-0.57, -1.15, 0.0),\
                            (-0.37, -1.15, 0.0),\
                            (-0.16, -1.15, 0.0)\
                ]\
              ))
    cmds.rename(c[0],n)
    c[0]=n
    return c