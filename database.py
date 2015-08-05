#!/usr/bin/env python
# 
# database.py -- implementation of a Swiss-system tournament
# based on tournament.py from udacity.
#

import config as cfg
import datetime
import psycopg2
import tools


def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect(database=cfg.DATABASE_NAME,
                            user=cfg.DATABASE_USERNAME,
                            password=cfg.DATABASE_PASSWORD)


def query(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    if "SELECT" in query:
        results = cursor.fetchall()
    else:
        results = ""
    connection.commit()
    cursor.close()
    connection.close()
    return results


def bulksql(query):  # use this one for unit testing; it handles bulk SQL better
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
