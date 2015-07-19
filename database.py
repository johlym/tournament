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


def delete_matche():
    # Remove all the match records from the database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("")
    connection.commit()
    cursor.close()
    connection.close()


def delete_player(player_id):
    # Remove all the player records from the database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM players WHERE id = " + player_id + ";")
    connection.commit()
    cursor.close()
    connection.close()


def update_player(player_id, name, country):
    # Remove all the player records from the database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("UPDATE players "
                   "SET name='" + name + "', country='" + country + "'"
                   "WHERE id=" + player_id + ";")
    connection.commit()
    cursor.close()
    connection.close()


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
    if criteria == "ID":
        cursor.execute("SELECT * FROM " + table + " "
                       "WHERE " + criteria + " = " + keyword + ";")
    elif criteria == "LOGS":
        cursor.execute("SELECT * FROM " + table + " "
                       "ORDER BY id DESC LIMIT " + str(keyword) + ";")
    elif criteria == "LATEST":
        cursor.execute("SELECT * FROM " + table + " "
                       "ORDER BY id DESC LIMIT 1;")
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


def register_player(name, country, code):
    # Registers a new player in the database.
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO players (name, country, code) "
                   "VALUES (\'" + name + "\',"
                   " \'" + country + "\', \'" + code + "\');")
    connection.commit()
    cursor.close()
    connection.close()


def player_standings():
    # Returns a list of the players and their win records, sorted by wins.
    #
    # The first entry in the list should be the player in first place,
    # or a player tied for first place if there is currently a tie.

    # Returns:
    #  A list of tuples, each of which contains (id, name, wins, matches):
    #    id: the player's unique id (assigned by the database)
    #    name: the player's full name (as registered)
    #    wins: the number of matches the player has won
    #    matches: the number of matches the player has played
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("select winner, count(winner) "
                   "FROM matches "
                   "GROUP BY winner "
                   "ORDER BY count desc;")
    count = cursor.rowcount
    tools.logger("Retrieved " + str(count) + " rows "
                 "from tournament.matches.", "trn.player_standings()")
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rows


def report_match(winner, player_1, player_2):
    # Records the outcome of a single match between two players.
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO matches (player_1, player_2, winner, "
                   "timestamp) "
                   "VALUES (\'" + player_1 + "\', \'" + player_2 + "\',"
                   "\'" + winner + "\', \'" + timestamp + "\')")
    connection.commit()
    cursor.close()
    connection.close()


def swiss_pairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


