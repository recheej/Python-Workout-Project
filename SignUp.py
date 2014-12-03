from PyQt4 import QtGui
from SignUpUI import Ui_SignUp
from user import User
import database
import MySQLdb


class SignUpWindow(QtGui.QWidget, Ui_SignUp):

    def __init__(self, parent=None):
        #super(LoginWindow, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pushButtonSignUp.clicked.connect(self.sign_up_clicked)
        self.pushButtonCancel.clicked.connect(self.cancel_clicked)

        self.line_edits = []
        self.line_edits.append(self.lineEditPassword)
        self.line_edits.append(self.lineEditName)
        self.line_edits.append(self.lineEditLastName)
        self.line_edits.append(self.lineEditAge)
        self.line_edits.append(self.lineEditWeight)
        self.line_edits.append(self.lineEditUsername)
        self.line_edits.append(self.lineEditPassword)

    def cancel_clicked(self):
        self.close()

    def sign_up_clicked(self):

        self.label_validation.setText("")
        for line_edit in self.line_edits:
            if line_edit.text() == "":
                self.label_validation.setText("All fields required.")
                return

        new_user = User()

        new_user.first_name = str(self.lineEditName.text())
        new_user.last_name = str(self.lineEditLastName.text())
        new_user.age = int(self.lineEditAge.text())
        new_user.weight = int(self.lineEditWeight.text())
        new_user.user_name = str(self.lineEditUsername.text())
        new_user.password = str(self.lineEditPassword.text())

        error = database.insert_user(new_user)

        if error:

            if isinstance(error, MySQLdb.IntegrityError):
                if "Duplicate entry" in error.args[1]:
                    #If we have a duplicate entry
                    self.label_validation.setText("Sorry that username is already taken.")
