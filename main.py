from PyQt4 import QtGui
import mainPage
import Login

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = Login.LoginWindow()

    #this is a test comment
    print 2

    #more testing
    window.show()
    app.exec_()
