#!/usr/bin/env python

"""
TOURNAMENT MATCHUP APPLICATION
 Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
 for match and player information.
"""

import argparse as arg
import config as cfg
import datetime
from decimal import Decimal
from prettytable import PrettyTable
import psycopg2
import random
import re
import sys
import time
import tools


def check_version(sys_version):
    """
    Let's check to make sure the user is running at least Python 2.7. Since
    this app was coded with that version, it would make sense.
    """
    # Check if python version is less than 2.7
    if sys_version < (2, 7):
        # if so, let the user know.
        message = "Version out of spec."
        print message
        time.sleep(3.0)  # Wait before proceeding through the app.
        verstat = 1
    else:
        verstat = 0
    return verstat


def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect(database=cfg.DATABASE_NAME,
                            user=cfg.DATABASE_USERNAME,
                            password=cfg.DATABASE_PASSWORD)


def registerPlayer(player_name="", country=""):
    """
    Create a new player based on their name and country of origin. We expect
    the following:
    - Player Name
    - Player Country of Origin
    """
    connection = connect()
    cursor = connection.cursor()
    # We perform some regex actions to check the input. Odd inputs can cause
    # problems, so it's best to catch them now.
    # check for numbers in player name
    if re.search('[0-9]', player_name):
        raise AttributeError("Player name is invalid (contains numbers)")
    # check if player name is shorter than 2 char.
    if len(player_name) < 2:
        raise AttributeError("Player name is less than 2 characters.")
    # player name is missing surname
    if " " not in player_name:
        raise AttributeError("Player name is invalid. (missing surname)")
    # player name shouldn't contain symbols
    if re.search('[!@#$%^&*\(\)~`+=]', player_name):
        raise AttributeError("Player name is invalid. (contains symbol(s))")
    # if a country isn't provided.
    if not country:
        raise SystemExit("Country of Origin Not Provided.")
    print "Creating new entry for %s from %s" % (player_name, country)
    code = player_name[:4].lower() + str(random.randrange(1000001, 9999999))
    start = time.time()
    # Unlike other queries in this app, we don't use the % symbol,
    # which allows psycopg2 to auto-escape any crazy single-quote-containing
    # names. This way, one can add all the O'Malleys and O'Neals they desire!
    cursor.execute("INSERT INTO players (name, country, code) "
                   "VALUES (%s, %s, %s);", (player_name, country,
                                                         code))
    stop = time.time()
    # Using the start and stop time values above, we can print out how long
    # it took to complete this action.
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Successfully created new entry in %s seconds" % dur[:5]
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def deletePlayer(player=""):
    """
    Delete an existing player based on their ID. We expect the following:
    - Option (edit or delete)
    - Player ID
    - New Player Name (if edit)
    - New Country of Origin (if edit)
    """
    connection = connect()
    cursor = connection.cursor()
    start = time.time()
    player = str(player)
    cursor.execute("SELECT * FROM players WHERE id=%s", (player,))
    search = cursor.fetchall()
    # if player ID wasn't found in search, raise an exception.
    if not search:
        raise LookupError("Invalid Player ID or ID Not Found.")
    cursor.execute("DELETE FROM players WHERE id = %s", (player,))
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def deletePlayers():
    """Deletes ALL players from the database."""
    connection = connect()
    cursor = connection.cursor()
    start = time.time()
    # empty the players table
    cursor.execute("TRUNCATE players;")
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def editPlayer(player="", new_name="", new_country=""):
    """Edit a player in the database, based on 'player',
    and using 'new_name' and 'new_country'."""
    connection = connect()
    cursor = connection.cursor()
    # if both a name and country aren't provided, raise an exception.
    if not (new_name and new_country):
        raise AttributeError("New Information Not Provided.")
    player_name = new_name
    player_country = new_country
    start = time.time()
    # look up the player based on the ID provided.
    cursor.execute("SELECT * FROM players WHERE id=%s", (player,))
    search = cursor.fetchall()
    # if player ID wasn't found in search, raise an exception.
    if not search:
        raise LookupError("Invalid Player ID.")
    cursor.execute("UPDATE players "
                   "SET name=%s, country=%s "
                   "WHERE id=%s", (player_name, player_country, player))
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def listPlayers():
    """
    Get a list of players based on criteria and display method.
    We expect the following:
    - Limit to display
    """
    connection = connect()
    cursor = connection.cursor()
    print "List All Players."
    cursor.execute("SELECT * FROM players;")
    results = cursor.fetchall()
    count = 0
    if not results:  # if there aren't any players
        print "No players found."
        status = 1
    else:
        print "Here's a list of all players in the database: "
        start = time.time()
        # Start building the output table.
        table = PrettyTable(['ID', 'NAME', 'COUNTRY'])
        table.align = 'l' # left-align the table contents.
        # Loop through the data and generate a table row for each iteration.
        for row in results:
            count += 1
            table.add_row([row[0], row[1], row[2]])
        # Finally, print the table.
        print table
        stop = time.time()
        dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                        rounding="ROUND_UP"))
        print "Returned %s results in %s seconds" % (count, dur[:5])
        connection.commit()
        cursor.close()
        connection.close()
        status = 0
    return status


def reportMatch(p1="", p2=""):
    """
    Initiate a match. We expect the following:
    - ID of Player 1
    - ID of Player 2
    """
    connection = connect()
    cursor = connection.cursor()
    # Because we use these in if statements, to make sure we're as pythonic
    # as possible, we need to explicity generate them, first. It's bad python
    # to assume they'll be generated in the logic below.
    p1_code = ''
    p2_code = ''
    p1_name = ''
    p2_name = ''
    # if both players aren't provided
    if not (p1 and p2):
        raise AttributeError("Both player IDs need to be provided.")
    # We perform some regex actions to check the input. Odd inputs can cause
    # problems, so it's best to catch them now.
    # if player 1's ID contains one or more letters
    if re.search('[A-Za-z]', str(p1)):
        raise AttributeError("Player 1 ID contains letter(s).")
    # if player 2's ID contains one or more letters
    if re.search('[A-Za-z]', str(p2)):
        raise AttributeError("Player 2 ID contains letter(s).")
    # if player 1's ID contains one or more symbols
    if re.search('[!@#$%^&*\(\)~`+=]', str(p1)):
        raise AttributeError("Player 1 ID is invalid. (contains symbol(s))")
    # if player 2's ID contains one or more symbols
    if re.search('[!@#$%^&*\(\)~`+=]', str(p2)):
        raise AttributeError("Player 2 ID is invalid. (contains symbol(s))")
    cursor.execute("SELECT * FROM players WHERE id=%s", (p1,))
    code_lookup = cursor.fetchall()
    if not code_lookup:  # if player 1 can't be found
        raise LookupError("Player 1 ID does not exist.")
    # Correlate a player's unique code to their name
    for row in code_lookup:
        p1_code = row[3]
        cursor.execute("SELECT * FROM players "
                                     "WHERE code=%s", (p1_code,))
        player_name = cursor.fetchall()
        for result in player_name:
            p1_name = result[1]
    cursor.execute("SELECT * FROM players WHERE id=%s", (p2,))
    code_lookup = cursor.fetchall()
    if not code_lookup:  # if player 2 can't be found
        raise LookupError("Player 2 ID does not exist.")
    # and again for player 2
    for row in code_lookup:
        p2_code = row[3]
        cursor.execute("SELECT * FROM players "
                                     "WHERE code=%s", (p2_code,))
        cursor.execute("SELECT * FROM players WHERE id=%s", (p2,))
        player_name = cursor.fetchall()
        for result in player_name:
            p2_name = result[1]
    print "%s vs. %s... " % (p1_name, p2_name),
    if (not p1_name) or (not p2_name):
        raise ValueError("One of the two players you entered doesn't exist.")
    # In this world, the first player always wins. One could call this
    # function and randomly choose who's is first position in order to make
    # it fair.
    winner = p1_code
    loser = p2_code
    print "Winner: %s" % p1_name
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    cursor.execute("INSERT INTO matches (player_1, player_2, "
                   "timestamp) "
                   "VALUES (%s, %s, %s);", (winner, loser, ts))
    connection.commit()
    cursor.close()
    connection.close()
    status = 0
    return status


def swissPairings():
    """
    match up each of the players in the database and swiss-ify them.
    """
    connection = connect()
    cursor = connection.cursor()
    # Because we use these in if statements, to make sure we're as pythonic
    # as possible, we need to explicity generate them, first. It's bad python
    # to assume they'll be generated in the logic below.
    bye = ''
    player_pairs = []
    round_number = 0
    start = time.time()
    # get the player list
    cursor.execute("SELECT * FROM players;")
    players_list = cursor.fetchall()
    # Count the number of players in the list
    count = len(players_list)
    if count == 0:
        raise ValueError("No players found.")
    # If there isn't an even amount:
    if count % 2:
        print count
        # simple math.
        # Since we need an even number of players, someone gets popped off.
        # Sorry, someone!
        bye = players_list[count - 1]
        players_list.pop(random.randrange(0,count))
        print len(players_list)
    # Since it's technically pure coincidence that the entries were in order,
    # we need to explicitly sort them. Defaults to the ID for sorting as it's
    # the first non-symbol in each entry.
    # If we did the list organization in the database, it would require extra
    # cycles in the code to get the data right.
    players_list1 = players_list[:len(players_list)/2]
    players_list2 = players_list[len(players_list)/2:]
    # Flip the second dict; faster than using the reversed() builtin.
    tx = PrettyTable(["TEAM A", "TEAM B"])
    # some master table settings we need to declare for formatting purposes
    tx.align = "c"
    tx.hrules = False
    tx.vrules = False
    tx.left_padding_width = 0
    tx.right_padding_width = 0
    # We have a special function to generate a table for our tables.
    # YO DAWG, I HEARD YOU LIKE TABLES... SO I PUT A TABLE IN YOUR TABLE.
    ta = tools.table_gen(['ID', 'Name', 'Country'], players_list1, "l")
    tb = tools.table_gen(['ID', 'Name', 'Country'], players_list2, "l")
    tx.add_row([ta, tb])
    print tx
    # Here's that special someone that got popped off earlier. We at least
    # acknowledge they're important, sort of.
    if bye:
        print "Bye: " + bye[1]
    # smoosh (technical term) the two lists together and make them fight
    # for their dinner!
    for a, b in zip(players_list1, players_list2):
        round_number += 1
        print "Round %i: " % round_number,
        # create a match for the two players matched up in each iteration
        reportMatch(p1=str(a[0]), p2=str(b[0]))
        player_pairs.append([a[0], a[1], b[0], b[1]])
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    print "Swiss matchups complete."
    connection.commit()
    cursor.close()
    connection.close()
    status = 0
    return player_pairs


def deleteMatch(match=""):
    """
    Delete an existing match. We expect the following:
    - Match ID
    """
    connection = connect()
    cursor = connection.cursor()
    if not match:
        raise ValueError("An ID # is required.")
    start = time.time()
    cursor.execute("DELETE FROM matches where id=%s", (match,))
    stop = time.time()

    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def deleteMatches():
    """
    Delete ALL matches from the database.
    """
    connection = connect()
    cursor = connection.cursor()
    start = time.time()
    cursor.execute("TRUNCATE matches;")
    stop = time.time()

    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    connection.commit()
    cursor.close()
    connection.close()
    return 0


def latest_match():
    """
    Get the latest match's information
    """
    connection = connect()
    cursor = connection.cursor()
    print "The Latest Match"
    name = ''
    count = 0
    returned_id = 0
    start = time.time()
    cursor.execute("SELECT * FROM matches ORDER BY id DESC LIMIT 1")
    results = cursor.fetchall()
    # Generate the table
    table = PrettyTable(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'])
    table.align = 'l'
    for row in results:
        count += 1
        # Generate the rows for the table
        cursor.execute("SELECT * FROM players "
                       "WHERE code=%s", (row[3],))
        player = cursor.fetchall()
        for entry in player:
            name = entry[1]
        if name == '':
            name = "[PLAYER DELETED]"
        table.add_row([count, row[0], row[1], row[2], name, row[4]])
        returned_id = row[0]
    print table
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Returned %s results in %s seconds" % (count, dur[:5])
    connection.commit()
    cursor.close()
    connection.close()
    return returned_id


def playerStandings():
    """
    Rank players by the number of wins. Get the list of wins and total
    matches for each player.
    """
    # Because we use these in if statements, to make sure we're as pythonic
    # as possible, we need to explicity generate them, first. It's bad python
    # to assume they'll be generated in the logic below.
    count = 0
    returned_blob = []
    connection = connect()
    cursor = connection.cursor()
    start = time.time()
    cursor.execute("SELECT * from players;")
    player_blob = cursor.fetchall()
    table = PrettyTable(["ID", "PLAYER", "WINS", "MATCHES"])
    table.align = "l"
    for player in player_blob:
        count += 1
        # Count the number of times the player has won (they are present in
        # player_1 column inside tournament.matches).
        cursor.execute("SELECT count(*) "
                       "FROM matches "
                       "WHERE player_1=%s", (player[3],))
        wins_blob = cursor.fetchall()
        wins_num = wins_blob[0][0]
        # Count the number of times the player has lost (they are present in
        # player_2 column inside tournament.matches).
        cursor.execute("SELECT count(*) "
                       "FROM matches "
                       "WHERE player_2=%s", (player[3],))
        losses_blob = cursor.fetchall()
        matches_num = losses_blob[0][0] + wins_num
        table.add_row([player[0], player[1], wins_num, matches_num])
        returned_blob.append([player[0], player[1], wins_num, matches_num])
    print table
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Returned %s results in %s seconds" % (count, dur[:5])
    return returned_blob


def countPlayers():
    """A function needed to fulfill the requirements of Udacity's
    tournament_test.py. This function gets used to count the number of
    players in the Players table."""
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(id) FROM players;")
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result[0][0]


def argument_parser():
    """
    Using command-line arguments to control actions. User can use flags to run
    certain, pre-defined scenarios. This will also allow for reuse of code where
    applicable.
    """
    parser = arg.ArgumentParser(description=cfg.APP_DESCRIPTION)

    # NEW PLAYER function
    parser.add_argument('--new-player', '-n',
                        dest='registerPlayer',
                        action='store',
                        nargs='+',
                        metavar='FIRST LAST COUNTRY',
                        help='Create a new player.')

    # NEW MATCH function
    parser.add_argument('--new-match', '-m',
                        dest='new_match',
                        action='store',
                        nargs="+",
                        metavar='ID#1 ID#2',
                        help='Create a new match. Provide two player IDs.')

    # SWISS MATCHUP function
    parser.add_argument('--swiss-match', '-s',
                        dest='swissPairings',
                        action='store_true',
                        default=False,
                        help='Create a new match with swiss pairing.')

    # GET LATEST RESULTS function
    parser.add_argument('--latest-match', '-l',
                        dest='latest_match',
                        action='store_true',
                        default=False,
                        help='Get the results from the latest match.')

    # DELETE PLAYER function
    parser.add_argument('--delete-player', '-d',
                        dest='deletePlayer',
                        action='store',
                        metavar='ID',
                        help='Remove a player from the match system.')

    # EDIT PLAYER function
    parser.add_argument('--edit-player', '-e',
                        dest='editPlayer',
                        action='store',
                        nargs='+',
                        metavar='ID NEWNAME NEWCOUNTRY',
                        help='Edit a player\'s exiting information.')

    # DELETE MATCH function
    parser.add_argument('--delete-match', '-f',
                        dest='deleteMatch',
                        action='store',
                        metavar='ID',
                        help='Remove a match from the match system.')

    # LIST PLAYERS function
    parser.add_argument('--list-players', '-p',
                        dest='listPlayers',
                        action='store_true',
                        default=False,
                        help='List all players.')

    # LIST RANKED function
    parser.add_argument('--list-ranking', '-t',
                        dest='list_ranking',
                        action='store_true',
                        default=False,
                        help='List rankings.')

    return parser


# ROUTING LOGIC #
def main():
    """
    We'll use this function to call up all our other functions, based on the
    action parameter provided on the command line.
    """
    parser = argument_parser()
    args = parser.parse_args()
    if args.registerPlayer:
        registerPlayer(player_name=(args.registerPlayer[0] + ' ' + args.registerPlayer[1]),
                   country=args.registerPlayer[2])

    if args.new_match:
        players = args.new_match
        reportMatch(p1=players[0], p2=players[1])

    if args.swiss_match:
        swissPairings()

    if args.deletePlayer:
        deletePlayer(player=str(args.delete_player))

    if args.editPlayer:
        name = "%s %s" % (args.editPlayer[1], args.editPlayer[2])
        editPlayer(player=str(args.editPlayer[0]),
                    new_name=name, new_country=args.editPlayer[3])

    if args.list_players:
        listPlayers()

    if args.deleteMatch:
        deleteMatch(match=str(args.deleteMatch))

    if args.latest_match:
        latest_match()

    if args.list_ranking:
        playerStandings()

    # IF NO ARGUMENTS #

    # Print all options.

    if len(sys.argv) == 1:
        parser.print_help()


if __name__ == "__main__":
    check_version(sys.version_info)
    main()
