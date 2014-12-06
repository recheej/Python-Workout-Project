__author__ = 'reche_000'
from user import User

import MySQLdb
from workout_session import WorkoutSession


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

def delete(sql_statement):

    db = db_instance()
    cursor = db.cursor()

    try:

        cursor.execute(sql_statement)

        db.commit()

        cursor.close()

        db.close()

        return True

    except MySQLdb.Error as e:

        cursor.close()
        db.close()

        print e
        return e




def insert_user(user):

    sql_statement = "insert into User (Last_Name, First_Name, Age, Weight, Gender, User_Name, Password, Count) values " + \
        "('%s', '%s', '%d', '%d', '%s', '%s', '%s', '%d')" % (user.last_name,
        user.first_name, user.age, user.weight, user.gender, user.user_name, user.password, user.count)

    return insert(sql_statement)


def insert_workout(workout_info):

    sql_statement = "insert into Workout_Info (User_ID, Muscle_Group, Exercise, Day) " + \
        "values (%d, '%s', '%s', %d)" % (workout_info.user_id,
        workout_info.muscle_group, workout_info.exercise, workout_info.day)

    return insert(sql_statement)


def delete_workout(user_id):

    sql_statement = "delete from Workout_Info where User_ID = %d" % (user_id)

    return delete(sql_statement)


def get_workouts(user_id, week_number, day_number):

    sql_statement = "select * from Workout_Session where User_ID = %d and Week_Number = %d and Day_Number = %d" %(user_id,
        week_number, day_number)

    workouts = select(sql_statement)

    workout_sessions = []

    for workout in workouts:

        workout_session = WorkoutSession()

        workout_session.workout_number = int(workout[0])
        workout_session.week_number = int(workout[1])
        workout_session.day_number = int(workout[2])
        workout_session.user_id = int(workout[3])
        workout_session.muscle_group = workout[4]
        workout_session.exercise = workout[5]
        workout_session.set_one = int(workout[6])
        workout_session.set_two = int(workout[7])
        workout_session.set_three = int(workout[8])

        workout_sessions.append(workout_session)

    return workout_sessions


def insert_workout_session(workout_session):

    sql_statement = "insert into Workout_Session (Workout_Number, Week_Number, Day_Number, User_ID, Muscle_Group, " + \
        "Exercise, Set_1, Set_2, Set_3, Weight) values (%d, %d, %d, %d, '%s', '%s', %d, %d, %d, %d)" % (workout_session.workout_number,
        workout_session.week_number, workout_session.day_number, workout_session.user_id, workout_session.muscle_group,
        workout_session.exercise, workout_session.set_one, workout_session.set_two, workout_session.set_three, workout_session.weight)

    return insert(sql_statement)