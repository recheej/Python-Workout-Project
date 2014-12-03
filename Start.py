from PyQt4 import QtGui, QtCore
from StartUI import Ui_Dialog

class StartWindow(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        #super(LoginWindow, self).__init__(parent)
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
