from PyQt4 import QtGui
import mainPage
import Login

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = Login.LoginWindow()


    #more testing
    window.show()
    app.exec_()
