from PyQt4 import QtGui
from mainPageUI import mainWindow
from CreatePlan import CreatePlanWindow
from StatsPage import StatsWindow
from Start import StartWindow

class mainPage(QtGui.QWidget, mainWindow):
    def __init__(self, parent=None, user_id=None):
        #super(mainPage, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButtonCreate.clicked.connect(self.openCreate)
        self.pushButtonProgress.clicked.connect(self.openProgress)
        self.pushButtonStart.clicked.connect(self.openStart)
        self.winS = None
        self.winC = None
        self.winP = None
        self.user_id = user_id

    def openCreate(self):
        if self.winC is None:
            self.winC = CreatePlanWindow(user_id=self.user_id)
            self.winC.show()
        else:
            self.winC.show()
    def openProgress(self):
        if self.winP is None:
            self.winP = StatsWindow()
            self.winP.show()
        else:
            self.winP.show()
    def openStart(self):
        if self.winS is None:
            self.winS = StartWindow()
            self.winS.show()
        else:
            self.winS.show()
