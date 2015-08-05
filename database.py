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


def sql(fileinput):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(fileinput)
    connection.commit()
    cursor.close()
    connection.close()


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


def count_players():
    # Returns the number of players currently registered.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM players;")
    count = cursor.rowcount
    tools.logger("Retrieved " + str(count) + " rows "
                 "from the tournament.players.", "trn.count_players()")
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rows


def player_standings():
    # Return player ranking, limiting to the top five players.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("select winner, count(winner) "
                   "FROM matches "
                   "GROUP BY winner "
                   "ORDER BY count desc "
                   "LIMIT 5;")
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rows
