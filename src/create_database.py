#
# create_database.py
#
# Desc: Creates local SQLite Database for Political Stance Tweets Project

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"/Users/pjrooney/SQLite/db/political_tweets.db")  # Change to your SQL Directory

