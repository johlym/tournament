#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import config as cfg
import datetime
import psycopg2
import tools


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect(database=cfg.DATABASE_NAME,
                            user=cfg.DATABASE_USERNAME,
                            password=cfg.DATABASE_PASSWORD)


def delete_matches():
    """Remove all the match records from the database."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("")
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def delete_players():
    """Remove all the player records from the database."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("")
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def count_players():
    """Returns the number of players currently registered."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM players;")
    count = cursor.rowcount
    tools.logger("Retrieved " + str(count) + " rows "
                 "from the database.", "trn.count_players()")
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return rows


def register_player(name,country):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO players (name, country) "
                   "VALUES (\'" + name + "\',"
                   " \'" + country + "\');")
    connection.commit()
    cursor.close()
    connection.close()




def player_standings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("")
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def report_match(winner, loser, player_1, player_2):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO matches (player_1, player_2, winner, loser, "
                   "timestamp) "
                   "VALUES (\'" + player_1 + "\', \'" + player_2 + "\',"
                   "\'" + winner + "\', \'" + loser + "\', \'"
                   + timestamp + "\')")
    connection.commit()
    cursor.close()
    connection.close()
    return 0


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


