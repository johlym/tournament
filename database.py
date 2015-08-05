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


def delete_match(match_id):
    # Remove all the match records from the database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM matches WHERE id = " + str(match_id) + ";")
    connection.commit()
    cursor.close()
    connection.close()


def delete_all_matches():
    # Clears the match database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM matches;")
    connection.commit()
    cursor.close()
    connection.close()


def delete_all_players():
    # Clears the match database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM players;")
    connection.commit()
    cursor.close()
    connection.close()


def count_matches():
    # Counts the number of matches in the database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(winner) FROM matches ")
    number = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return number


def count_wins(player_code):
    # Remove all the player records from the database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(winner)"
                   "FROM matches "
                   "WHERE winner LIKE '%" + player_code + "%';")
    number = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return number


# A fancy multi-purpose function that we can use to search ANY of the tables,
#  provided we give the right criteria.

def search(table, criteria, keyword):
    connection = connect()
    cursor = connection.cursor()
    # Search using various identifiers in the table requested
    if criteria == "ID": # by ID
        cursor.execute("SELECT * FROM " + table + " "
                       "WHERE " + criteria + " = " + keyword + ";")
    elif criteria == "LOGS": # search for logs
        cursor.execute("SELECT * FROM " + table + " "
                       "ORDER BY id DESC LIMIT " + str(keyword) + ";")
    elif criteria == "LATEST": # latest entry
        cursor.execute("SELECT * FROM " + table + " "
                       "ORDER BY id DESC LIMIT 1;")
    elif criteria == "ALL": # everything
        cursor.execute("SELECT * FROM " + table + ";")
    elif criteria == "LIMIT": # everything with user-defined limit
        cursor.execute("SELECT * FROM " + table + " "
                       "ORDER BY id DESC LIMIT " + str(keyword) + ";")
    else:
        cursor.execute("SELECT * FROM " + table + " "
                       "WHERE " + criteria + " LIKE \'%" + keyword + "%\';")
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rows


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
