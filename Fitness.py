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
        self.pushButtonSave1.clicked.connect(self.saveProgress)
        self.pushButtonSave2.clicked.connect(self.saveProgress)
        self.pushButtonSave3.clicked.connect(self.saveProgress)
        self.pushButtonStatsBack.clicked.connect(self.backToMain)
        self.exercise_dict = {'Chest': ['Incline Bench Press (Barbell)', 'Flat Bench Press (Barbell)'],
         'Back':['Lat Pull Down', 'Seated Cable Row'],
         'Bicep':['Hammer Curls', 'Preacher Curl'],
         'Tricep':['Kick Backs','Dips'],
         'Legs':['Squats', 'Leg Press'],
         'Core(abs)':['Heel Touches', 'Leg Raises'],
         'Shoulders':['Military Press (Dumbbell)', 'Rear Deltoid Flyes']}

        self.checkBoxList1 = [self.checkBoxChest,
            self.checkBoxBack,
            self.checkBoxBiscep,
            self.checkTricep,
            self.checkBoxLegs,
            self.checkBoxCore,
            self.checkBoxShoulders
            ]

        #Check Box List for Column 2/Day 2
        self.checkBoxList2 = [self.checkBoxChest_2,
                self.checkBoxBack_2,
                self.checkTricep_2,
                self.checkBoxBiscep_2,
                self.checkBoxLegs_2,
                self.checkBoxCore_2,
                self.checkBoxShoulders_2
                ]

        #Check Box List for Column 3/ Day 3
        self.checkBoxList3 = [self.checkBoxChest_3,
                self.checkBoxBack_3,
                self.checkBoxBiscep_3,
                self.checkTricep_3,
                self.checkBoxLegs_3,
                self.checkBoxCore_3,
                self.checkBoxShoulders_3
                ]
        #Loop through check list 1 for clicks
        for item in self.checkBoxList1:
            item.clicked.connect(self.LimitCheckNumber)

        #Loop through check list 2 for clicks
        for item in self.checkBoxList2:
            item.clicked.connect(self.LimitCheckNumber)

        #Loop through check list 3 for clicks
        for item in self.checkBoxList3:
            item.clicked.connect(self.LimitCheckNumber)            

        #initialize counters 1-3 for amount of check boxes checked    
        self.checkCounter1 = 0
        self.checkCounter2 = 0
        self.checkCounter3 = 0
        
     #LimitCheckNumber checks number of boxes checked and disables and enables as necessary
    def LimitCheckNumber(self):
        #Check Box List 1
        for item in self.checkBoxList1:
            if item.isChecked():
                self.checkCounter1 += 1   
        if self.checkCounter1 == 3:
            for item in self.checkBoxList1:
                if item.isChecked() == False:
                    item.setEnabled(False)
        if self.checkCounter1 < 3:
            for item in self.checkBoxList1:
                if item.isChecked() == False:
                    item.setEnabled(True)
        self.checkCounter1 = 0


        #Check Box List 2
        for item in self.checkBoxList2:
            if item.isChecked():
                self.checkCounter2 += 1   
        if self.checkCounter2 == 3:
            for item in self.checkBoxList2:
                if item.isChecked() == False:
                    item.setEnabled(False)
        if self.checkCounter2 < 3:
            for item in self.checkBoxList2:
                if item.isChecked() == False:
                    item.setEnabled(True)
        self.checkCounter2 = 0


        #Check Box List 3
        for item in self.checkBoxList3:
            if item.isChecked():
                self.checkCounter3 += 1   
        if self.checkCounter3 == 3:
            for item in self.checkBoxList3:
                if item.isChecked() == False:
                    item.setEnabled(False)
        if self.checkCounter3 < 3:
            for item in self.checkBoxList3:
                if item.isChecked() == False:
                    item.setEnabled(True)
        self.checkCounter3 = 0
        
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
         
    def create_plan_clicked(self):

        sql_statement = "UPDATE User SET Count = 1 Where User_ID = %d" % self.user_id
        database.update(sql_statement)
        database.delete_workout(self.user_id)
        checkboxes = self.findChildren(QtGui.QCheckBox)
        checkboxes.reverse()

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

                    if muscle_group == "Biscep":
                        muscle_group = "Bicep"

                    workout_session.muscle_group = muscle_group

                    exercises = self.exercise_dict[muscle_group]
                    random_exercise = exercises[random.randint(0, len(exercises) - 1)]
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
        sql_statement = "select * from User where User_Id = %d" %self.user_id

        results = database.select(sql_statement)
        
        info = database.get_stat_info(self.user_id)

        self.progressBar.setValue((results[0][8] / 18) * 100)
       
        workoutlist = []
        count = 1
        for workout in info:
            count = False
            if workoutlist:
                              
                for item in workoutlist:
                    
                    if item[0].exercise == workout.exercise:
                        count = True
                        item.append(workout)
                        break
                if count:
                    pass
                else:
                    exercise1 = []
                    exercise1.append(workout)
                    workoutlist.append(exercise1)
            else:
                exercise = []
                exercise.append(workout)
                workoutlist.append(exercise)
        
        
        self.tableWidget.setRowCount(len(workoutlist))
        self.tableWidget.setColumnCount(4)
        for item in range(len(workoutlist)):
            
            itemName = QtGui.QTableWidgetItem(workoutlist[item][0].exercise)
            self.tableWidget.setItem(item,0, itemName)
            max1 = min1 = workoutlist[item][0].weight
            reps = 0
            size = len(workoutlist[item])
            for work in workoutlist[item]:
                if work.weight < min1:
                    min1 = work.weight
                if max1 < work.weight:
                    max1 = work.weight
                reps += work.set_one
                reps += work.set_two
                reps += work.set_three
            finalReps = reps/(3*size)
            
            itemStartName = QtGui.QTableWidgetItem(str(min1))
            self.tableWidget.setItem(item,1, itemStartName)
            
            itemEndName = QtGui.QTableWidgetItem(str(max1))
            self.tableWidget.setItem(item,2, itemEndName)

            itemRepsName = QtGui.QTableWidgetItem(str(finalReps))
            self.tableWidget.setItem(item,3, itemRepsName)
        
        self.stackedWidget.setCurrentIndex(5)
    def openStart(self):
        self.createStartPage()
        self.stackedWidget.setCurrentIndex(4)
        

    def createStartPage(self):
        workout_sessions = database.get_current_workouts(self.user_id)

        self.Picture_3.setPixmap(QtGui.QPixmap(os.getcwd() + '\\' + workout_sessions[2].exercise + '.jpg'))
        self.labelWorkout3.setText(workout_sessions[2].exercise)
        self.Picture_2.setPixmap(QtGui.QPixmap(os.getcwd() + '\\' + workout_sessions[1].exercise + '.jpg'))
        self.labelWorkout2.setText(workout_sessions[1].exercise)
        self.Picture.setPixmap(QtGui.QPixmap(os.getcwd() + '\\' + workout_sessions[0].exercise + '.jpg'))
        self.labelWorkout1.setText(workout_sessions[0].exercise)
        
    def nextTab(self):
        if self.tabWidget.currentIndex() == 2:
            self.stackedWidget.setCurrentIndex(2)
            self.tabWidget.setCurrentIndex(0)

            database.update_count(self.user_id)
            count_results = database.get_count(self.user_id)
            count = count_results[0][0]
            if count % 3 == 1:
                for i in range(0, 3):

                    workout_counter = 0
                    for j in range (0,3):

                        workout_counter += 1

                        workout_session = WorkoutSession()

                        workout_session.workout_number = workout_counter
                        workout_session.day_number = count + i
                        workout_session.week_number = ((count - 1) / 3) + 1
                        workout_session.user_id = self.user_id

                        sql_statement = "SELECT Muscle_Group, Exercise from Workout_Session WHERE User_ID = %d AND Week_Number = 1 AND Workout_Number = %d AND Day_Number = %d" % \
                                       (self.user_id, workout_session.workout_number, i + 1)
                        results = database.select(sql_statement)

                        workout_session.muscle_group = results[0][0]
                        workout_session.exercise = results[0][1]
                        database.insert_workout_session(workout_session)

        else:
            self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex()+1)
    def saveProgress(self):

        workout_sessions = database.get_current_workouts(self.user_id)
        weight = -1
        set1 = -1
        set2 = -1
        set3 = -1
        week = -1
        day = -1
        workout_number = -1

        if self.tabWidget.currentIndex() == 0:

            week = workout_sessions[0].week_number
            day = workout_sessions[0].day_number
            workout_number = 1

            weight = self.lineEditWeight_2.text()
            set1 = self.lineEditSet1.text()
            set2 = self.lineEditSet2.text()
            set3 = self.lineEditSet3.text()

        if self.tabWidget.currentIndex() == 1:

            week = workout_sessions[1].week_number
            day = workout_sessions[1].day_number
            workout_number = 2

            weight = self.lineEditWeight_3.text()
            set1 = self.lineEditSet1_2.text()
            set2 = self.lineEditSet2_2.text()
            set3 = self.lineEditSet3_2.text()

        if self.tabWidget.currentIndex() == 2:

            week = workout_sessions[2].week_number
            day = workout_sessions[2].day_number
            workout_number = 3

            weight = self.lineEditWeight_4.text()
            set1 = self.lineEditSet1_3.text()
            set2 = self.lineEditSet2_3.text()
            set3 = self.lineEditSet3_3.text()

        sql_statement = "UPDATE Workout_Session SET Weight = %d, Set_1 = %d, Set_2 = %d, Set_3 = %d WHERE Workout_Number = %d and Week_Number = %d and Day_Number = %d and User_ID = %d" % \
                        (int(weight), int(set1), int(set2), int(set3), workout_number, week, day, self.user_id)

        completed = database.update(sql_statement)

        self.nextTab()