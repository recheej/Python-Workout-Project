from FitnessUI import Ui_PyFitness
from PyQt4 import QtCore, QtGui
from user import User
from workout_info import WorkoutInfo
from workout_session import WorkoutSession
import os,sys
import database
import MySQLdb
import random



#self.stackedWidget.setCurrentIndex(0)
#self.tabWidget.setCurrentIndex(0)
class FitnessApp(QtGui.QMainWindow, Ui_PyFitness):

    def __init__(self, parent=None):
        #super(LoginWindow, self).__init__(parent)
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.user_id = None
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.login_clicked)
        self.pushButton_2.clicked.connect(self.openSignUp)
        self.pushButtonSignUp.clicked.connect(self.sign_up_clicked)
        self.pushButtonCancel.clicked.connect(self.backToLogin)
        self.radioButtonPlan.clicked.connect(self.EnableCheckBoxes)
        self.pushButtonCreate.clicked.connect(self.openCreate)
        self.pushButtonProgress.clicked.connect(self.openProgress)
        self.pushButtonStart.clicked.connect(self.openStart)
        self.pushButtonSubmit.clicked.connect(self.create_plan_clicked)
        self.pushButtonCreateCancel.clicked.connect(self.backToMain)
        self.pushButtonSave1.clicked.connect(self.nextTab)
        self.pushButtonSave2.clicked.connect(self.nextTab)
        self.pushButtonSave3.clicked.connect(self.nextTab)
        self.pushButtonStatsBack.clicked.connect(self.backToMain)
        self.exercise_dict = {'Chest': ['Incline Bench Press (Barbell)', 'Flat Bench Press (Barbell)'],
         'Back':['Lat Pull Down', 'Seated Cable Row'],
         'Bicep':['Hammer Curls', 'Preacher Curl'],
         'Tricep':['Kick Backs','Dips'],
         'Legs':['Squats', 'Leg Press'],
         'Core(abs)':['Heel Touches', 'Leg Raises'],
         'Shoulders':['Military Press (Dumbbell)', 'Rear Deltoid Flyes']}
        

    def backToLogin(self):
        self.stackedWidget.setCurrentIndex(0)
       
    def login_clicked(self):

        user_name = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())

        if (user_name.isspace() or password.isspace()) or (user_name == "" or password == ""):
            self.label_validation.setText("Both fields required")
            return

        sql_statement = "select * from User where User_Name = '%s' and Password = '%s'" % (user_name, password)

        results = database.select(sql_statement)

        if len(results) == 0:

            self.label_validation.setText("No user found.")

            return
        
        self.user_id = results[0][0]
        self.stackedWidget.setCurrentIndex(2)

    def openSignUp(self):
        self.stackedWidget.setCurrentIndex(1)

    def sign_up_clicked(self):
        self.line_edits = []
        self.line_edits.append(self.lineEditPassword)
        self.line_edits.append(self.lineEditName)
        self.line_edits.append(self.lineEditLastName)
        self.line_edits.append(self.lineEditAge)
        self.line_edits.append(self.lineEditWeight)
        self.line_edits.append(self.lineEditUsername)
        self.line_edits.append(self.lineEditPassword)

        self.label_validation.setText("")
        for line_edit in self.line_edits:
            if line_edit.text() == "":
                self.label_validationSign.setText("All fields required.")
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
        else:
            #If we successfully signed up we should set a message on log in page
            self.stackedWidget.setCurrentIndex(0)
            self.label_validationSign.setText("Sign up SUCCESSFUL!")
            
    def DisableCheckBoxes(self):
         self.checkBoxChest.setEnabled(False)
         self.checkBoxChest_2.setEnabled(False)
         self.checkBoxChest_3.setEnabled(False)
         self.checkBoxBack.setEnabled(False)
         self.checkBoxBack_2.setEnabled(False)
         self.checkBoxBack_3.setEnabled(False)
         self.checkBoxBiscep.setEnabled(False)
         self.checkBoxBiscep_2.setEnabled(False)
         self.checkBoxBiscep_3.setEnabled(False)
         self.checkTricep.setEnabled(False)
         self.checkTricep_2.setEnabled(False)
         self.checkTricep_3.setEnabled(False)
         self.checkBoxLegs.setEnabled(False)
         self.checkBoxLegs_2.setEnabled(False)
         self.checkBoxLegs_3.setEnabled(False)
         self.checkBoxCore.setEnabled(False)
         self.checkBoxCore_2.setEnabled(False)
         self.checkBoxCore_3.setEnabled(False)
         self.checkBoxShoulders.setEnabled(False)
         self.checkBoxShoulders_2.setEnabled(False)
         self.checkBoxShoulders_3.setEnabled(False)
         self.checkBoxChest.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxChest_2.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxChest_3.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxBack.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxBack_2.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxBack_3.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxBiscep.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxBiscep_2.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxBiscep_3.setCheckState(QtCore.Qt.Unchecked)
         self.checkTricep.setCheckState(QtCore.Qt.Unchecked)
         self.checkTricep_2.setCheckState(QtCore.Qt.Unchecked)
         self.checkTricep_3.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxLegs.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxLegs_2.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxLegs_3.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxCore.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxCore_2.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxCore_3.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxShoulders.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxShoulders_2.setCheckState(QtCore.Qt.Unchecked)
         self.checkBoxShoulders_3.setCheckState(QtCore.Qt.Unchecked)
         self.radioButtonPlan.setChecked(False)
         
         

    def EnableCheckBoxes(self):
         self.checkBoxChest.setEnabled(True)
         self.checkBoxChest_2.setEnabled(True)
         self.checkBoxChest_3.setEnabled(True)
         self.checkBoxBack.setEnabled(True)
         self.checkBoxBack_2.setEnabled(True)
         self.checkBoxBack_3.setEnabled(True)
         self.checkBoxBiscep.setEnabled(True)
         self.checkBoxBiscep_2.setEnabled(True)
         self.checkBoxBiscep_3.setEnabled(True)
         self.checkTricep.setEnabled(True)
         self.checkTricep_2.setEnabled(True)
         self.checkTricep_3.setEnabled(True)
         self.checkBoxLegs.setEnabled(True)
         self.checkBoxLegs_2.setEnabled(True)
         self.checkBoxLegs_3.setEnabled(True)
         self.checkBoxCore.setEnabled(True)
         self.checkBoxCore_2.setEnabled(True)
         self.checkBoxCore_3.setEnabled(True)
         self.checkBoxShoulders.setEnabled(True)
         self.checkBoxShoulders_2.setEnabled(True)
         self.checkBoxShoulders_3.setEnabled(True)
         
    def create_workout(self, d, g):

        new_workout = WorkoutInfo()
        new_workout.user_id = self.user_id
        new_workout.day = d
        new_workout.muscle_group = g
        new_workout.exercise = self.exercise_dict[g][random.randint(0, len(self.exercise_dict[g])-1)]
        new_workout.sets = 3
        new_workout.reps = 1
        new_workout.goal_sets = 3
        new_workout.goal_reps = 1
        new_workout.weights = 1

        database.insert_workout(new_workout)
         
    def create_plan_clicked(self):

        workouts = database.get_workouts(self.user_id, 1, 1)

        checkboxes = self.findChildren(QtGui.QCheckBox)

        counter = 0
        for i in range(0, 3):

            day_checkboxes = checkboxes[counter: counter + 7]

            workout_counter = 0
            for checkbox in day_checkboxes:

                if checkbox.isChecked():

                    workout_counter += 1

                    workout_session = WorkoutSession()

                    workout_session.workout_number = workout_counter
                    workout_session.day_number = i + 1
                    workout_session.user_id = self.user_id

                    muscle_group = str(checkbox.text())
                    workout_session.muscle_group = muscle_group

                    exercises = self.exercise_dict[muscle_group]
                    random_exercise = exercises[random.randint(0, len(exercises))]
                    workout_session.exercise = random_exercise

                    database.insert_workout_session(workout_session)

            counter += 7

        self.stackedWidget.setCurrentIndex(2)
        self.DisableCheckBoxes()
            
    def backToMain(self):
        if (self.stackedWidget.currentIndex() == 3):
            self.DisableCheckBoxes()
        self.stackedWidget.setCurrentIndex(2)

    def openCreate(self):
        self.stackedWidget.setCurrentIndex(3)
    def openProgress(self):
        self.stackedWidget.setCurrentIndex(5)
    def openStart(self):
        self.stackedWidget.setCurrentIndex(4)
        self.createStartPage()

    def createStartPage(self):
        sql_statement = "select * from User where User_Id = %s" %self.user_id
        results = database.select(sql_statement)
        if len(results) == 0:
            print 'none'
        day = results[0][8]
        actualDay = (day%3)+1

        sql_statement_2 = "select * from Workout_Info where User_Id = %s and Day = %d" %(self.user_id, actualDay)
        results_2 = database.select(sql_statement_2)

        self.Picture_3.setPixmap(QtGui.QPixmap(os.getcwd() + '\\' + results_2[2][3] + '.jpg'))
        self.labelWorkout3.setText(results_2[2][3])
        self.Picture_2.setPixmap(QtGui.QPixmap(os.getcwd() + '\\' + results_2[1][3] + '.jpg'))
        self.labelWorkout2.setText(results_2[1][3])
        self.Picture.setPixmap(QtGui.QPixmap(os.getcwd() + '\\' + results_2[0][3]+ '.jpg'))
        self.labelWorkout1.setText(results_2[0][3])
        
    def nextTab(self):
        if self.tabWidget.currentIndex() == 2:
            self.stackedWidget.setCurrentIndex(2)
            self.tabWidget.setCurrentIndex(0)
        else:
            self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()+1)