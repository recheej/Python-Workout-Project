# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartPlanPage.ui'
#
# Created: Thu Dec 04 17:35:34 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(592, 501)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.label = QtGui.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(90, 10, 331, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.labelWorkoutName = QtGui.QLabel(self.tab1)
        self.labelWorkoutName.setGeometry(QtCore.QRect(70, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelWorkoutName.setFont(font)
        self.labelWorkoutName.setObjectName(_fromUtf8("labelWorkoutName"))
        self.pushButton = QtGui.QPushButton(self.tab1)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 91, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.layoutWidget = QtGui.QWidget(self.tab1)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 180, 113, 111))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelWeight = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.labelWeight.setFont(font)
        self.labelWeight.setObjectName(_fromUtf8("labelWeight"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelWeight)
        self.lineEditWeight = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditWeight.setObjectName(_fromUtf8("lineEditWeight"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditWeight)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditSet1 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSet1.setObjectName(_fromUtf8("lineEditSet1"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditSet1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEditSet2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSet2.setObjectName(_fromUtf8("lineEditSet2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditSet2)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEditSet3 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditSet3.setObjectName(_fromUtf8("lineEditSet3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditSet3)
        self.Picture = QtGui.QLabel(self.tab1)
        self.Picture.setGeometry(QtCore.QRect(250, 90, 291, 351))
        self.Picture.setObjectName(_fromUtf8("Picture"))
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.labelWorkoutName_2 = QtGui.QLabel(self.tab_2)
        self.labelWorkoutName_2.setGeometry(QtCore.QRect(70, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelWorkoutName_2.setFont(font)
        self.labelWorkoutName_2.setObjectName(_fromUtf8("labelWorkoutName_2"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 180, 113, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelWeight_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.labelWeight_2.setFont(font)
        self.labelWeight_2.setObjectName(_fromUtf8("labelWeight_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelWeight_2)
        self.lineEditWeight_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditWeight_2.setObjectName(_fromUtf8("lineEditWeight_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditWeight_2)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEditSet1_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditSet1_2.setObjectName(_fromUtf8("lineEditSet1_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditSet1_2)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEditSet2_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditSet2_2.setObjectName(_fromUtf8("lineEditSet2_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditSet2_2)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEditSet3_2 = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEditSet3_2.setObjectName(_fromUtf8("lineEditSet3_2"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditSet3_2)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 331, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 310, 91, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.Picture_2 = QtGui.QLabel(self.tab_2)
        self.Picture_2.setGeometry(QtCore.QRect(250, 90, 291, 351))
        self.Picture_2.setObjectName(_fromUtf8("Picture_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.labelWorkoutName_3 = QtGui.QLabel(self.tab_3)
        self.labelWorkoutName_3.setGeometry(QtCore.QRect(70, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelWorkoutName_3.setFont(font)
        self.labelWorkoutName_3.setObjectName(_fromUtf8("labelWorkoutName_3"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 180, 113, 111))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.layoutWidget_2)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.labelWeight_3 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.labelWeight_3.setFont(font)
        self.labelWeight_3.setObjectName(_fromUtf8("labelWeight_3"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelWeight_3)
        self.lineEditWeight_3 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditWeight_3.setObjectName(_fromUtf8("lineEditWeight_3"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditWeight_3)
        self.label_9 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEditSet1_3 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditSet1_3.setObjectName(_fromUtf8("lineEditSet1_3"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditSet1_3)
        self.label_10 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEditSet2_3 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditSet2_3.setObjectName(_fromUtf8("lineEditSet2_3"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditSet2_3)
        self.label_11 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lineEditSet3_3 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditSet3_3.setObjectName(_fromUtf8("lineEditSet3_3"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEditSet3_3)
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(90, 10, 331, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 310, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.Picture_3 = QtGui.QLabel(self.tab_3)
        self.Picture_3.setGeometry(QtCore.QRect(250, 90, 291, 351))
        self.Picture_3.setObjectName(_fromUtf8("Picture_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Do 3 sets of as many reps as you can.", None))
        self.labelWorkoutName.setText(_translate("Dialog", "Workout Name", None))
        self.pushButton.setText(_translate("Dialog", "Save Progress", None))
        self.labelWeight.setText(_translate("Dialog", "Weight:", None))
        self.label_3.setText(_translate("Dialog", "Set 1: ", None))
        self.label_4.setText(_translate("Dialog", "Set 2: ", None))
        self.label_5.setText(_translate("Dialog", "Set 3:", None))
        self.Picture.setText(_translate("Dialog", "l", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Workout 1", None))
        self.labelWorkoutName_2.setText(_translate("Dialog", "Workout Name", None))
        self.labelWeight_2.setText(_translate("Dialog", "Weight:", None))
        self.label_6.setText(_translate("Dialog", "Set 1: ", None))
        self.label_7.setText(_translate("Dialog", "Set 2: ", None))
        self.label_8.setText(_translate("Dialog", "Set 3:", None))
        self.label_2.setText(_translate("Dialog", "Do 3 sets of as many reps as you can.", None))
        self.pushButton_2.setText(_translate("Dialog", "Save Progress", None))
        self.Picture_2.setText(_translate("Dialog", "l", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Workout 2", None))
        self.labelWorkoutName_3.setText(_translate("Dialog", "Workout Name", None))
        self.labelWeight_3.setText(_translate("Dialog", "Weight:", None))
        self.label_9.setText(_translate("Dialog", "Set 1: ", None))
        self.label_10.setText(_translate("Dialog", "Set 2: ", None))
        self.label_11.setText(_translate("Dialog", "Set 3:", None))
        self.label_12.setText(_translate("Dialog", "Do 3 sets of as many reps as you can.", None))
        self.pushButton_3.setText(_translate("Dialog", "Save Progress", None))
        self.Picture_3.setText(_translate("Dialog", "l", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Workout 3", None))

