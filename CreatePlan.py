from PyQt4 import QtGui
from CreatePlanUI import Ui_CreatePlan
from workout_info import WorkoutInfo
import database


class CreatePlanWindow(QtGui.QWidget, Ui_CreatePlan):
     def __init__(self, parent=None, user_id=None):
        #super(LoginWindow, self).__init__(parent)
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.radioButtonPlan.clicked.connect(self.EnableCheckBoxes)
        self.pushButtonSubmit.clicked.connect(self.create_plan_clicked)
        self.user_id = user_id

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
        new_workout.exercise = "temp"
        new_workout.sets = 1
        new_workout.reps = 1
        new_workout.goal_sets = 1
        new_workout.goal_reps = 1
        new_workout.weights = 1

        database.insert_workout(new_workout)
         
     def create_plan_clicked(self):

        if self.checkBoxChest.isChecked():
            self.create_workout(1, "Chest")
        if self.checkBoxChest_2.isChecked():
            self.create_workout(2, "Chest")
        if self.checkBoxChest_3.isChecked():
            self.create_workout(3, "Chest")
        if self.checkBoxBack.isChecked():
            self.create_workout(1, "Back")
        if self.checkBoxBack_2.isChecked():
            self.create_workout(2, "Back")
        if self.checkBoxBack_3.isChecked():
            self.create_workout(3, "Back")
        if self.checkBoxBiscep.isChecked():
            self.create_workout(1, "Bicep")
        if self.checkBoxBiscep_2.isChecked():
            self.create_workout(2, "Bicep")
        if self.checkBoxBiscep_3.isChecked():
            self.create_workout(3, "Bicep")
        if self.checkTricep.isChecked():
            self.create_workout(1, "Tricep")
        if self.checkTricep_2.isChecked():
            self.create_workout(2, "Tricep")
        if self.checkTricep_3.isChecked():
            self.create_workout(3, "Tricep")
        if self.checkBoxLegs.isChecked():
            self.create_workout(1, "Legs")
        if self.checkBoxLegs_2.isChecked():
            self.create_workout(2, "Legs")
        if self.checkBoxLegs_3.isChecked():
            self.create_workout(3, "Legs")
        if self.checkBoxCore.isChecked():
            self.create_workout(1, "Core")
        if self.checkBoxCore_2.isChecked():
            self.create_workout(2, "Core")
        if self.checkBoxCore_3.isChecked():
            self.create_workout(3, "Core")
        if self.checkBoxShoulders.isChecked():
            self.create_workout(1, "Shoulders")
        if self.checkBoxShoulders_2.isChecked():
            self.create_workout(2, "Shoulders")
        if self.checkBoxShoulders_3.isChecked():
            self.create_workout(3, "Shoulders")

         
