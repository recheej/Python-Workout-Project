from PyQt4 import QtGui
from LoginUI import Ui_MainWindow
from mainPage import mainPage
from SignUp import SignUpWindow
import database


class LoginWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        #super(LoginWindow, self).__init__(parent)
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_clicked)
        self.pushButton_2.clicked.connect(self.openSignUp)

    def login_clicked(self):

        user_name = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())

        if (user_name.isspace() or password.isspace()) or (user_name == "" or password == ""):
            self.label_validation.setText("Both fields required")
            return

        sql_statement = "select * from User where User_Name = '%s' and Password = '%s'" % (user_name, password)

        results = database.select(sql_statement)

        if len(results) == 0:

            self.label_validation.setText("No records matching that username and password")

            return


        user_id = results[0][0]
        self.openMainpage(user_id)

    def openMainpage(self, user_id):
        self.win = mainPage(user_id=user_id)
        self.close()
        self.win.show()

    def openSignUp(self):
        self.win = SignUpWindow()
        self.win.show()
