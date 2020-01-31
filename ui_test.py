# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui',
# licensing of 'test.ui' applies.
#
# Created: Fri Jan 31 23:47:48 2020
#      by: pyside2-uic  running on PySide2 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(606, 125)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(40, 20, 151, 31))
        self.widget1.setObjectName("widget1")
        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(260, 20, 151, 31))
        self.widget2.setObjectName("widget2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))

