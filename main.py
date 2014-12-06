from PyQt4 import QtGui
import Fitness

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = Fitness.FitnessApp()
    
    window.show()
    app.exec_()
