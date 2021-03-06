# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/Jenks/maya/scripts/Jenks/scripts/curveCreator/newCurveUI.ui'
#
# Created: Wed Sep 21 14:09:48 2016
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 190)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.crvDegreeGrp = QtWidgets.QGroupBox(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crvDegreeGrp.sizePolicy().hasHeightForWidth())
        self.crvDegreeGrp.setSizePolicy(sizePolicy)
        self.crvDegreeGrp.setMinimumSize(QtCore.QSize(170, 85))
        self.crvDegreeGrp.setMaximumSize(QtCore.QSize(170, 85))
        self.crvDegreeGrp.setObjectName("crvDegreeGrp")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.crvDegreeGrp)
        self.gridLayout_5.setHorizontalSpacing(45)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.crvDegree3Rad = QtWidgets.QRadioButton(self.crvDegreeGrp)
        self.crvDegree3Rad.setObjectName("crvDegree3Rad")
        self.gridLayout_5.addWidget(self.crvDegree3Rad, 1, 0, 1, 1)
        self.crvDegree2Rad = QtWidgets.QRadioButton(self.crvDegreeGrp)
        self.crvDegree2Rad.setObjectName("crvDegree2Rad")
        self.gridLayout_5.addWidget(self.crvDegree2Rad, 0, 2, 1, 1)
        self.crvDegree5Rad = QtWidgets.QRadioButton(self.crvDegreeGrp)
        self.crvDegree5Rad.setObjectName("crvDegree5Rad")
        self.gridLayout_5.addWidget(self.crvDegree5Rad, 1, 2, 1, 1)
        self.crvDegree1Rad = QtWidgets.QRadioButton(self.crvDegreeGrp)
        self.crvDegree1Rad.setChecked(True)
        self.crvDegree1Rad.setObjectName("crvDegree1Rad")
        self.gridLayout_5.addWidget(self.crvDegree1Rad, 0, 0, 1, 1)
        self.crvDegree7Rad = QtWidgets.QRadioButton(self.crvDegreeGrp)
        self.crvDegree7Rad.setObjectName("crvDegree7Rad")
        self.gridLayout_5.addWidget(self.crvDegree7Rad, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.crvDegreeGrp, 0, 0, 2, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.createBtn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createBtn.sizePolicy().hasHeightForWidth())
        self.createBtn.setSizePolicy(sizePolicy)
        self.createBtn.setMinimumSize(QtCore.QSize(120, 50))
        self.createBtn.setMaximumSize(QtCore.QSize(100, 50))
        self.createBtn.setObjectName("createBtn")
        self.gridLayout_2.addWidget(self.createBtn, 1, 1, 1, 1)
        self.copyBtn = QtWidgets.QPushButton(MainWindow)
        self.copyBtn.setMinimumSize(QtCore.QSize(60, 23))
        self.copyBtn.setMaximumSize(QtCore.QSize(60, 23))
        self.copyBtn.setObjectName("copyBtn")
        self.gridLayout_2.addWidget(self.copyBtn, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.periodicChk = QtWidgets.QCheckBox(MainWindow)
        self.periodicChk.setObjectName("periodicChk")
        self.gridLayout_2.addWidget(self.periodicChk, 2, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        self.txtField = QtWidgets.QTextEdit(MainWindow)
        self.txtField.setEnabled(True)
        self.txtField.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.txtField.setReadOnly(True)
        self.txtField.setObjectName("txtField")
        self.gridLayout.addWidget(self.txtField, 3, 0, 1, 3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Curve To Python", None, -1))
        self.crvDegreeGrp.setTitle(QtWidgets.QApplication.translate("MainWindow", "Curve Degree", None, -1))
        self.crvDegree3Rad.setText(QtWidgets.QApplication.translate("MainWindow", "3 Cubic", None, -1))
        self.crvDegree2Rad.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.crvDegree5Rad.setText(QtWidgets.QApplication.translate("MainWindow", "5", None, -1))
        self.crvDegree1Rad.setText(QtWidgets.QApplication.translate("MainWindow", "1 Linear", None, -1))
        self.crvDegree7Rad.setText(QtWidgets.QApplication.translate("MainWindow", "7", None, -1))
        self.createBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Generate Python", None, -1))
        self.copyBtn.setText(QtWidgets.QApplication.translate("MainWindow", "Copy", None, -1))
        self.periodicChk.setText(QtWidgets.QApplication.translate("MainWindow", "Periodic", None, -1))

