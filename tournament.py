#!/usr/bin/env python

"""
TOURNAMENT MATCHUP APPLICATION
 Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
 for match and player information.
"""

import argparse as arg
import config as cfg
import database as db
import datetime
from decimal import Decimal
from prettytable import PrettyTable
import random
import re
import sys
import time
import tools


"""
Let's check to make sure the user is running at least Python 2.7. Since
this app was coded with that version, it would make sense.
"""

def check_version(sys_version):
    if sys_version < (2, 7):
        message = "Version out of spec."
        print message
        time.sleep(3.0)  # long enough, I think.
        verstat = 1
    else:
        verstat = 0
    return verstat


# PLAYER ORIENTED FUNCTIONS #

"""
Create a new player based on their name and country of origin. We expect
the following:
- Player Name
- Player Country of Origin
"""


def new_player(player_name="", country=""):
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
    tools.logger("Received player name " + player_name, "new_player()")
    # if a country isn't provided.
    if not country:
        raise SystemExit("Country of Origin Not Provided.")
    tools.logger("Received player country " + country, "new_player()")
    print "Creating new entry for %s from %s" % (player_name, country)
    code = player_name[:4].lower() + str(random.randrange(1000001, 9999999))
    start = time.time()
    q = "INSERT INTO players (name, country, code) " \
        "VALUES (\'%s\', \'%s\', \'%s\');" % (player_name, country, code)
    db.query(q)
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Successfully created new entry in %s seconds" % dur[:5]
    tools.logger("Database entry created for " + player_name + " from " +
                 country + ".",
                 "new_player()")
    return 0


"""
Delete an existing player based on their ID. We expect the following:
- Option (edit or delete)
- Player ID
- New Player Name (if edit)
- New Country of Origin (if edit)
"""


def edit_player(option="", player="", new_name="", new_country=""):
    if option == "delete":
        start = time.time()
        q = "SELECT * FROM players WHERE id=%s" % player
        search = db.query(q)
        # if player ID wasn't found in search
        if not search:
            raise AttributeError("Invalid Player ID.")
        q = "DELETE FROM players " \
            "WHERE id = %s" % player
        db.query(q)
        tools.logger("Deleted %s from the database" % player, "edit_player()")
        stop = time.time()
    elif option == "edit":
        if not (new_name and new_country):
            raise AttributeError("EDIT chosen, but new info not given.")
        player_name = new_name
        player_country = new_country
        start = time.time()
        q = "SELECT * FROM players WHERE id=%s" % player
        search = db.query(q)
        # if player ID wasn't found in search
        if not search:
            raise AttributeError("Invalid Player ID.")
        q = "UPDATE players " \
            "SET name=\'%s\', country=\'%s\' " \
            "WHERE id=%s" % (player_name, player_country, player)
        db.query(q)
        tools.logger("Updated %s." % player, "edit_player()")
        stop = time.time()
    else:  # if we're not editing nor deleting, error out
        raise AttributeError("OPTION Not Supported: '%s'" % option)

    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    return 0


"""
Get a list of players based on criteria and display method.
We expect the following:
- Limit to display
"""


def list_players():
    print "List All Players."
    tools.logger("Requesting all players in the database.", "list_players()")
    q = "SELECT * FROM players;"
    results = db.query(q)
    if not results:  # if there aren't any players
        print "No players found."
        status = 1
    else:
        print "Here's a list of all players in the database: "
        start = time.time()
        count = len(results)
        print tools.table_gen(['ID', 'Name', 'Country'], results, "l")
        stop = time.time()

        dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                        rounding="ROUND_UP"))
        tools.logger(("Returned %i results in %s seconds" % (count, dur[:5])),
                     "list_players()")
        print "Returned %s results in %s seconds" % (count, dur[:5])
        status = 0
    return status


# MATCH ORIENTED FUNCTIONS #

"""
Initiate a match. We expect the following:
- ID of Player 1
- ID of Player 2
"""


def go_match(p1="", p2=""):
    p1_code = ''
    p2_code = ''
    p1_name = ''
    p2_name = ''
    # if both players aren't provided
    if not (p1 and p2):
        raise AttributeError("Both player IDs need to be provided.")
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
    tools.logger("Starting match between " + p1 + " and " + p2,
                 "go_match()")
    q = "SELECT * FROM players WHERE id=%s" % p1
    code_lookup = db.query(q)
    if not code_lookup:  # if player 1 can't be found
        raise LookupError("Player 1 ID does not exist.")
    for row in code_lookup:
        p1_code = row[3]
        q = "SELECT * FROM players WHERE code=\'%s\'" % p1_code
        player_name = db.query(q)
        for result in player_name:
            p1_name = result[1]
    q = "SELECT * FROM players WHERE id=%s" % p2
    code_lookup = db.query(q)
    if not code_lookup:  # if player 2 can't be found
        raise LookupError("Player 2 ID does not exist.")
    for row in code_lookup:
        p2_code = row[3]
        q = "SELECT * FROM players WHERE code=\'%s\'" % p2_code
        player_name = db.query(q)
        for result in player_name:
            p2_name = result[1]
    print "%s vs. %s... " % (p1_name, p2_name),
    if (not p1_name) or (not p2_name):
        raise ValueError("One of the two players you entered doesn't exist.")
    # Randomly pick between one or two.
    random_int = random.randrange(1, 3)
    tools.logger("Generated random number " + str(random_int), "go_match()")
    # If the random number is even: player 1 wins. Else: player 2 wins.
    if random_int == 2:
        # the random number is even:
        print p1_name + " wins!"
        tools.logger("Stated that player 1 wins.", "go_match()")
        winner = p1_code
    else:
        # the random number is odd:
        print "Player " + p2_name + " wins!"
        tools.logger("Stated that player 2 wins.", "go_match()")
        winner = p2_code
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    q = "INSERT INTO matches (player_1, player_2, winner, timestamp) " \
        "VALUES (\'%s\', \'%s\', \'%s\', \'%s\');" % (p1, p2, winner, ts)
    db.query(q)
    tools.logger("Reported win to database.", "go_match()")
    status = 0
    return status


"""
match up each of the players in the database and swiss-ify them.
"""

def swiss_match():
    bye = ''
    round_number = 0
    start = time.time()
    q = "SELECT * FROM players;"
    players_list = db.query(q)
    # Count the number of players in the list
    count = len(players_list)
    if count == 0:
        raise ValueError("No players found.")
    tools.logger("Found %i players in list for swiss matchups." % count,
                 "swiss_match()")
    # If there isn't an even amount:
    if count % 2:
        print count
        tools.logger("Popping off the odd player (#%i) out." % count,
                     "swiss_match()")
        # simple math.
        bye = players_list[count - 1]
        players_list.pop(count - 1)
        print len(players_list)
    """ Since it's technically pure coincidence that the entries were in order,
    we need to explicitly sort them. Defaults to the ID for sorting as it's
    the first non-symbol in each entry.
    If we did the list organization in the database, it would require extra
    cycles in the code to get the data right. """
    players_list = sorted(players_list)
    players_list1 = players_list[:len(players_list)/2]
    players_list2 = players_list[len(players_list)/2:]
    # Flip the second dict; faster than using the reversed() builtin.
    players_list2 = sorted(players_list2, reverse=True)
    tx = PrettyTable(["TEAM A", "TEAM B"])
    # some master table settings we need to declare for formatting purposes
    tx.align = "c"
    tx.hrules = False
    tx.vrules = False
    tx.left_padding_width = 0
    tx.right_padding_width = 0
    ta = tools.table_gen(['ID', 'Name', 'Country'], players_list1, "l")
    tb = tools.table_gen(['ID', 'Name', 'Country'], players_list2, "l")
    tx.add_row([ta, tb])
    tools.logger("Generated COMPLETE table for display", "swiss_match()")
    print tx
    if bye:
        print "Bye: " + bye[1]
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    # smoosh (technical term) the two lists together and make them fight
    # for their dinner!
    start = time.time()
    for a, b in zip(players_list1, players_list2):
        round_number += 1
        print "Round %i: " % round_number,
        tools.logger("Initiating round %i against go_match()" %
                     round_number, "swiss_match()")
        go_match(p1=str(a[0]), p2=str(b[0]))
        tools.logger("Completed round %i against go_match()" %
                     round_number, "swiss_match()")
        stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    print "Swiss matchups complete."
    status = 0
    return [status, count, bye]


"""
Delete an existing match. We expect the following:
- Match ID
"""


def delete_match(match=""):
    if not match:
        raise ValueError("An ID # is required.")
    start = time.time()
    q = "DELETE FROM matches where id=%s" % (match)
    db.query(q)
    tools.logger("Deleted match %s from the database", "delete_match()")
    stop = time.time()

    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % dur[:5]
    return 0


"""
Display all historical matches.
"""


def list_matches():
    name = ''
    tools.logger("Listing all matches.", "list_matches()")
    print "List All Matches"
    # display all matches in the matches table, (in groups of ten,
    # with names, eventually).
    start = time.time()
    q = "SELECT * FROM matches;"
    results = db.query(q)
    count = len(results)
    if count == 0:
        raise SystemExit("No matches found.")
    # print tools.table_gen(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'],
    #                      results, "l")
    table = PrettyTable(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'])
    table.align = 'l'
    for row in results:
        count += 1
        q = "SELECT * FROM players WHERE code=\'%s\'" % row[3]
        player = db.query(q)
        for entry in player:
            name = entry[1]
        if name == '':
            name = "[PLAYER DELETED]"
        table.add_row([count, row[0], row[1], row[2], name, row[4]])
    print table
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, dur[:5])),
                 "list_matches")
    print "Returned %s results in %s seconds" % (count, dur[:5])
    return 0

"""
Get the latest match's information
"""


def latest_match():
    print "The Latest Match"
    name = ''
    count = 0
    returned_id = 0
    start = time.time()
    q = "SELECT * FROM matches ORDER BY id DESC LIMIT 1"
    results = db.query(q)
    tools.logger("Retrieved latest result.", "lookup")
    table = PrettyTable(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'])
    table.align = 'l'
    for row in results:
        count += 1
        q = "SELECT * FROM players WHERE code=\'%s\'" % row[3]
        player = db.query(q)
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
    tools.logger(("Returned %i results in %s seconds" % (count, dur[:5])),
                 "list_matches")
    print "Returned %s results in %s seconds" % (count, dur[:5])
    return returned_id


"""
Get the latest match's information. We expect the following:
- Match ID
"""


def lookup_match(match=""):
    if not match:
        raise SystemExit("Missing a match ID.")
    if re.search('[A-Za-z]', str(match)):
        raise AttributeError("Match ID contains letter(s)")
    if re.search('[!@#$%^&*\(\)~`+=]', str(match)):
        raise AttributeError("Match ID contains symbol(s)")
    count = 0
    # defining 'name' here prevents "UnboundLocalError: referenced before
    # assignment" that comes up if we lookup and the player was deleted.
    name = ''
    start = time.time()
    q = "SELECT * FROM matches WHERE id=%s" % match
    results = db.query(q)
    if not results:
        raise SystemExit("No Match Found.")
    tools.logger("Retrieved latest result.", "lookup")
    table = PrettyTable(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'])
    table.align = 'l'
    for row in results:
        count += 1
        q = "SELECT * FROM players WHERE code=\'%s\'" % row[3]
        player = db.query(q)
        for entry in player:
            name = entry[1]
        if name == '':
            name = "[PLAYER DELETED]"
        table.add_row([count, row[0], row[1], row[2], name, row[4]])
    print table
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, dur[:5])),
                 "list_matches")
    print "Returned %s results in %s seconds" % (count, dur[:5])
    return 0


"""
Rank Players by Number of Wins.
"""

def list_win_ranking():
    print "List Ranking of Players by Wins"
    count = 0
    name = ''
    # get list of players and their IDs
    # for each player, count the number of times they won in every match
    start = time.time()
    q = "SELECT winner, count(winner) FROM matches GROUP BY winner " \
        "ORDER BY count DESC " \
        "LIMIT 5"
    results = db.query(q)
    if not results:
        raise SystemExit("No Matches Found to Rank.")
    table = PrettyTable(['#', 'PLAYER', 'WINS'])
    table.align = 'l'
    for row in results:
        count += 1
        q = "SELECT * FROM players WHERE code=\'%s\'" % row[0]
        player = db.query(q)
        if not player:
            name = "[PLAYER DELETED]"
        for p in player:
            name = p[1]
        table.add_row([count, name, row[1]])
    print table
    stop = time.time()
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, dur[:5])),
                 "list_matches")
    print "Returned %s results in %s seconds" % (count, dur[:5])
    return 0


"""
Any good app keeps a log. We can optionally display all with see_all.
"""

def display_log(see_all=False):
    count = 20
    print "Displaying last 20 entries."
    start = time.time()
    q = "SELECT * FROM auditlog ORDER BY id DESC LIMIT %s" % str(count)
    results = db.query(q)
    if not results:
        raise SystemExit("No log entries.")
    tools.logger("Retrieved results x20.", "display_log()")
    table = PrettyTable(['#', 'ENTRY', 'ACTION', 'UNIQUE ID', 'TIMESTAMP'])
    table.align = 'l'
    for row in results:
        table.add_row([row[0], row[1], row[2], row[3], row[4]])
    tools.logger("Created audit log table.", "display_log()")
    print table
    stop = time.time()
    tools.logger("Printed audit log table.", "display_log()")
    dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                    rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, dur[:5])),
                 "display_log()")
    print "Returned %s results in %s seconds" % (count, dur[:5])
    if see_all:
        tools.logger("User requested ALL entries.", "display_log()")
        count = 9999999
        start = time.time()
        q = "SELECT * FROM auditlog ORDER BY id DESC LIMIT %s" % str(count)
        results = db.query(q)
        tools.logger("Retrieved results x9999999.", "display_log()")
        table = PrettyTable(['#', 'ENTRY', 'ACTION', 'UNIQUE ID', 'TIMESTAMP'])
        table.align = 'l'
        for row in results:
            table.add_row([row[0], row[1], row[2], row[3], row[4]])
        tools.logger("Created audit log table.", "display_log()")
        print table
        stop = time.time()
        tools.logger("Printed audit log table.", "display_log()")
        dur = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                        rounding="ROUND_UP"))
        tools.logger(("Returned max %i results in %s seconds" %
                      (count, dur[:5])), "display_log()")
        print "Returned %s results in %s seconds" % (count, dur[:5])
    else:
        print "Ok."
    return 0


"""
Using command-line arguments to control actions. User can use flags to run
certain, pre-defined scenarios. This will also allow for reuse of code where
applicable.
"""


def argument_parser():
    parser = arg.ArgumentParser(description=cfg.APP_DESCRIPTION)

    # NEW PLAYER function
    parser.add_argument('--new-player', '-n',
                        dest='new_player',
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
                        dest='swiss_match',
                        action='store_true',
                        default=False,
                        help='Create a new match with swiss pairing.')

    # GET LATEST RESULTS function
    parser.add_argument('--latest-match', '-l',
                        dest='latest_match',
                        action='store_true',
                        default=False,
                        help='Get the results from the latest match.')

    # GET LATEST RESULTS function
    parser.add_argument('--lookup-match', '-r',
                        dest='lookup_match',
                        action='store',
                        metavar='ID',
                        help='Get the results from a specific match.')

    # DELETE PLAYER function
    parser.add_argument('--delete-player', '-d',
                        dest='delete_player',
                        action='store',
                        metavar='ID',
                        help='Remove a player from the match system.')

    # EDIT PLAYER function
    parser.add_argument('--edit-player', '-e',
                        dest='edit_player',
                        action='store',
                        metavar='ID',
                        help='Edit a player\'s exiting information.')

    # DELETE MATCH function
    parser.add_argument('--delete-match', '-f',
                        dest='delete_match',
                        action='store',
                        metavar='ID',
                        help='Remove a match from the match system.')

    # LIST RESULTS function
    parser.add_argument('--list-matches', '-k',
                        dest='list_matches',
                        action='store_true',
                        default=False,
                        help='List Results from a recent match.')

    # LIST PLAYERS function
    parser.add_argument('--list-players', '-p',
                        dest='list_players',
                        action='store_true',
                        default=False,
                        help='List all players.')

    # LIST RANKED function
    parser.add_argument('--list-ranking', '-t',
                        dest='list_ranking',
                        action='store_true',
                        default=False,
                        help='List rankings.')

    # VIEW AUDIT LOG function
    parser.add_argument('--audit-log', '-a',
                        dest='audit_log',
                        action='store_true',
                        default=False,
                        help='Display the Audit Logs.')

    return parser


# ROUTING LOGIC #
def main():
    parser = argument_parser()
    args = parser.parse_args()
    if args.new_player:
        new_player(player_name=(args.new_player[0] + ' ' + args.new_player[1]),
                   country=args.new_player[2])

    if args.new_match:
        players = args.new_match
        go_match(p1=players[0], p2=players[1])

    if args.swiss_match:
        swiss_match()

    if args.delete_player:
        edit_player(option="delete",
                    player=str(args.delete_player))

    if args.edit_player:
        edit_player(option="edit",
                    player=str(args.edit_player))

    if args.list_players:
        list_players()

    if args.delete_match:
        delete_match(match=str(args.delete_match))

    if args.list_matches:
        list_matches()

    if args.lookup_match:
        lookup_match(match=str(args.lookup_match))

    if args.latest_match:
        latest_match()

    if args.list_ranking:
        list_win_ranking()

    if args.audit_log:
        display_log()

    # IF NO ARGUMENTS #

    # Print all options.

    if len(sys.argv) == 1:
        parser.print_help()


if __name__ == "__main__":
    check_version(sys.version_info)
    main()
