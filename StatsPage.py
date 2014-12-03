from PyQt4 import QtGui
from StatsPageUI import Ui_Stats

class StatsWindow(QtGui.QWidget, Ui_Stats):
    def __init__(self, parent=None):
        #super(mainPage, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
