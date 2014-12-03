# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectViewPage.ui'
#
# Created: Sun Nov 23 21:11:27 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class mainWindow(object):
    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(663, 552)
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 70, 661, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(100, 80, 20, 471))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(130, 100, 77, 151))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonCreate = QtGui.QPushButton(self.widget)
        self.pushButtonCreate.setObjectName(_fromUtf8("pushButtonCreate"))
        self.verticalLayout.addWidget(self.pushButtonCreate)
        self.pushButtonStart = QtGui.QPushButton(self.widget)
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.verticalLayout.addWidget(self.pushButtonStart)
        self.pushButtonProgress = QtGui.QPushButton(self.widget)
        self.pushButtonProgress.setObjectName(_fromUtf8("pushButtonProgress"))
        self.verticalLayout.addWidget(self.pushButtonProgress)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButtonCreate.setText(_translate("Form", "Create Plan", None))
        self.pushButtonStart.setText(_translate("Form", "Start Plan", None))
        self.pushButtonProgress.setText(_translate("Form", "View Progress", None))

