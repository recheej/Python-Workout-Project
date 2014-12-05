from PyQt4 import QtGui, QtCore
from StartUI import Ui_Dialog
import os,sys

class StartWindow(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        #super(LoginWindow, self).__init__(parent)
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.Picture_3.setPixmap(QtGui.QPixmap(os.getcwd() + '\Hammer Curls.jpg'))
        self.Picture_2.setPixmap(QtGui.QPixmap(os.getcwd() + '\Leg Press.jpg'))
        self.Picture.setPixmap(QtGui.QPixmap(os.getcwd() + '\Dips.jpg'))
