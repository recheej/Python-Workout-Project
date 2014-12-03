__author__ = 'reche_000'
from user import User

import MySQLdb


def db_instance():

    host_name = "recheejinstance.cx1ynpvooriw.us-west-2.rds.amazonaws.com"
    user_name = "recheej"
    password = "usf_dev1992"
    db_name = "WorkoutDB"

    db = MySQLdb.connect(host_name, user_name, password, db_name)

    return db


def select(sql_statement):

    database = db_instance()
    cursor = database.cursor()

    try:
        cursor.execute(sql_statement)

        print "SUCCESSFUL SELECT"

        results = cursor.fetchall()

        cursor.close()
        database.close()

        return results

    except MySQLdb.Error as e:

        print e

        database.rollback()
        cursor.close()
        database.close()

        return e


def insert(sql_statement):

    #inserts something into the database. Returns false and prints error if something went wrong

    database = db_instance()
    cursor = database.cursor()

    try:

        cursor.execute(sql_statement)

        database.commit()

        print "SUCCESSFUL INSERTION"

        cursor.close()

        database.close()

        return None

    except MySQLdb.Error as e:

        database.rollback()

        print str(e)

        cursor.close()
        database.close()

        return e


def insert_user(user):

    sql_statement = "insert into User (Last_Name, First_Name, Age, Weight, Gender, User_Name, Password) values " + \
        "('%s', '%s', '%d', '%d', '%s', '%s', '%s')" % (user.last_name,
        user.first_name, user.age, user.weight, user.gender, user.user_name, user.password)

    return insert(sql_statement)


def insert_workout(workout_info):

    sql_statement = "insert into Workout_Info (User_ID, Muscle_Group, Exercise, Sets, Reps, Goal_Sets, Goal_Reps, Weight, Day) " + \
        "values ('%d', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d')" % (workout_info.user_id,
        workout_info.muscle_group, workout_info.exercise, workout_info.sets, workout_info.reps, workout_info.goal_sets,
        workout_info.goal_reps, workout_info.weights, workout_info.day)

    insert(sql_statement)