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