#!/usr/bin/env python

__author__ = 'jlyman'

# TOURNAMENT MATCHUP APPLICATION
# Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
# for match and player information.

# ordering imports alphabetically is good a good pythonism.

import argparse as arg
import config as cfg
import database as db
from decimal import Decimal
from prettytable import PrettyTable
import random
import sys
import time
import tools


# PLAYER ORIENTED FUNCTIONS #


# Create a new player based on their name and country of origin.
def new_player():
    print "Please enter the player's Name: "
    player_name = raw_input("Player's Name: ")
    tools.logger("Received player name " + player_name, "new_player()")
    print "Please enter the player's Country of Origin: "
    player_country = raw_input("Country of Origin: ")
    tools.logger("Received player country " + player_country, "new_player()")
    print "Creating new entry for %s from %s" % (player_name, player_country)
    code = player_name[:4].lower() + str(random.randrange(1000001, 9999999))
    start = time.time()
    db.register_player(player_name, player_country, code)
    stop = time.time()
    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                             rounding="ROUND_UP"))
    print "Successfully created new entry in %s seconds" % duration[:5]
    tools.logger("Database entry created for " + player_name + " from " +
                 player_country + ".",
                 "new_player()")


# Delete an existing player based on their ID.
def edit_player(option):
    # Check by ID
    method = "0"
    count = 0
    start = 0
    stop = 0
    by = ''
    existing_name = ''
    existing_country = ''
    criteria = ''
    # A quick and dirty way to keep asking until we get the right answer is via
    # a WHILE loop. So long as the user DOESN'T give us "1" or "2",
    # we'll keep bugging them.

    # ONE IF BY LAND, TWO IF BY SEA
    # -- Henry Wadsworth Longfellow's "Paul Revere's Ride"
    while not any(word in method for word in ['1', '2']):
        print "In order to change a player's record, first we need to look " \
              "them up " \
              "and make sure they're actually there."
        print "Here are your options:"
        print "1. By ID"
        print "2. By Name"
        method = raw_input("Please choose: ")
        # 1 if by land (ID)
        if method == "1":
            by = "ID"
            print "Looking up player by ID..."
            criteria = raw_input("Please enter the player's ID: ")
        # 2 if by sea (name)
        if method == "2":
            by = "name"
            print "Looking up player by Name..."
            criteria = raw_input("Please enter the player's Name: ")

        start = time.time()
        results = db.search("players", by, criteria)
        table = PrettyTable(['#', 'Unique ID', 'Name', 'Country'])
        table.align = "l"
        for row in results:
            count += 1
            table.add_row([count, row[0], row[1], row[2]])
        print table
        stop = time.time()

    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, duration[:5])),
                 "edit_player()")
    print "Returned %s results in %s seconds" % (count, duration[:5])
    print ""
    if option == "delete":
        player = raw_input("Which player do you want to delete? [ID]")
        start = time.time()
        db.delete_player(player)
        tools.logger("Deleted %s from the database" % player, "edit_player()")
        stop = time.time()
    if option == "edit":
        player = raw_input("Which player do you want to edit? [ID]")
        new_name = raw_input("New Player Name [leave blank for no change]: ")
        new_country = raw_input("New Country [leave blank for no change]: ")
        existing = db.search("players", "ID", player)
        for row in existing:
            existing_name = row[1]
            existing_country = row[2]
        print "Editing %s..." % player
        if not new_name:
            player_name = existing_name
        else:
            player_name = new_name
        if not new_country:
            player_country = existing_country
        else:
            player_country = new_country
        start = time.time()
        db.update_player(player, player_name, player_country)
        tools.logger("Updated %s." % player, "edit_player()")
        stop = time.time()

    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % duration[:5]


# Get a list of players based on criteria and display method.
def list_players():
    count = 0
    print "List All Players."
    print "Here's a list of all players in the database: "
    print "=============================================="
    tools.logger("Requesting all players in the database.", "list_players()")
    start = time.time()
    results = db.search("players", "ALL", "null")
    # table = PrettyTable(['#', 'Unique ID', 'Name', 'Country', 'Wins'])
    table = PrettyTable(['#', 'Unique ID', 'Name', 'Country', 'Code'])
    table.align = "l"
    for row in results:
        count += 1
        # wins = db.count_wins(row[3])
        # for win in wins:
        #     wincount = win[0]
        # table.add_row([count, row[0], row[1], row[2], wincount])
        table.add_row([count, row[0], row[1], row[2], row[3]])
    print table
    stop = time.time()

    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, duration[:5])),
                 "list_players()")
    print "Returned %s results in %s seconds" % (count, duration[:5])


# MATCH ORIENTED FUNCTIONS #


# Initiate a match. Player_1 and Player_2 should be IDs.
def go_match():
    player_1_code = ''
    player_2_code = ''
    player_1 = raw_input("ID# for Player 1: ")
    player_2 = raw_input("ID# for Player 2: ")
    tools.logger("Starting match between " + player_1 + " and " + player_2,
                 "go_match()")
    code_lookup = db.search("players", "ID", player_1)
    for row in code_lookup:
        player_1_code = row[3]
    code_lookup = db.search("players", "ID", player_2)
    for row in code_lookup:
        player_2_code = row[3]
    print "Match between %s and %s" % (player_1, player_2)
    # Randomly pick between one or two.
    random_int = random.randrange(1, 3)
    print random_int
    tools.logger("Generated random number " + str(random_int), "go_match()")
    # If the random number is even: player 1 wins. Else: player 2 wins.
    if random_int == 2:
        # the random number is even:
        print player_1 + " wins!"
        tools.logger("Stated that player 1 wins.", "go_match()")
        winner = player_1_code
    else:
        # the random number is odd:
        print "Player " + player_2 + " wins!"
        tools.logger("Stated that player 2 wins.", "go_match()")
        winner = player_2_code
    db.report_match(winner, player_1, player_2)
    tools.logger("Reported win to database.", "go_match()")
    print "Finished."


def swiss_match():
    # create a new match using the swiss paring system.
    print ""


# Delete an existing match
def delete_match():
    count = 0
    print "In order to delete a match, first we need to look it up " \
          "and make sure it's actually there."
    start = time.time()
    results = db.search("matches", "ALL", "null")
    table = PrettyTable(['#', 'ID', 'Winner Code', 'Timestamp'])
    table.align = "l"
    for row in results:
        count += 1
        table.add_row([count, row[0], row[3], row[4]])
    print table
    stop = time.time()

    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, duration[:5])),
                 "delete_match()")
    print "Returned %s results in %s seconds" % (count, duration[:5])
    print ""
    match = raw_input("Which match do you want to delete? [ID]")
    start = time.time()
    db.delete_match(match)
    tools.logger("Deleted %s from the database" % match, "delete_match()")
    stop = time.time()

    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    print "Complete. Operation took %s seconds." % duration[:5]


# Display all historical matches.
def list_matches():
    count = 0
    tools.logger("Listing all matches.", "list_matches()")
    print "List All Matches"
    # display all matches in the matches table, (in groups of ten,
    # with names, eventually).
    start = time.time()
    results = db.search("matches", "ALL", "null")

    table = PrettyTable(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'])
    table.align = 'l'
    for row in results:
        count += 1
        player = db.search("players", "CODE", row[3])
        for entry in player:
            name = entry[1]
        if name == '':
            name = "[PLAYER DELETED]"
        table.add_row([count, row[0], row[1], row[2], name, row[4]])
    print table
    stop = time.time()
    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, duration[:5])),
                 "list_matches")
    print "Returned %s results in %s seconds" % (count, duration[:5])


# Get the latest match's information
def latest_match():
    print "The Latest Match"
    count = 0
    start = time.time()
    results = db.search("matches", "LATEST", count)
    tools.logger("Retrieved latest result.", "lookup")
    table = PrettyTable(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'])
    table.align = 'l'
    for row in results:
        count += 1
        player = db.search("players", "CODE", row[3])
        for entry in player:
            name = entry[1]
        if name == '':
            name = "[PLAYER DELETED]"
        table.add_row([count, row[0], row[1], row[2], name, row[4]])
    print table
    stop = time.time()
    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, duration[:5])),
                 "list_matches")
    print "Returned %s results in %s seconds" % (count, duration[:5])


# Get the latest match's information
def lookup_match():
    match = raw_input("Please enter a match ID to lookup: ")
    print "Match Lookup"
    count = 0
    # prevents "UnboundLocalError: referenced before assignment"
    # that comes up if we lookup and the player was deleted.
    name = ''
    start = time.time()
    results = db.search("matches", "ID", match)
    tools.logger("Retrieved latest result.", "lookup")
    table = PrettyTable(['#', 'ID#', 'P1 ID', 'P2 ID', 'WINNER', 'TIME'])
    table.align = 'l'
    for row in results:
        count += 1
        player = db.search("players", "CODE", row[3])
        for entry in player:
            name = entry[1]
        if name == '':
            name = "[PLAYER DELETED]"
        table.add_row([count, row[0], row[1], row[2], name, row[4]])
    print table
    stop = time.time()
    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, duration[:5])),
                 "list_matches")
    print "Returned %s results in %s seconds" % (count, duration[:5])


# Rank Players by Number of Wins
def list_win_ranking():
    print "List Ranking of Players by Wins"
    # get list of players and their IDs.
    # for each player, count the number of times they won in every match


# Any good app keeps a log.
def display_log():
    tools.logger("Displaying log entries.", "display_log()")
    count = 20
    print "Displaying last 20 entries."
    start = time.time()
    results = db.search("auditlog", "LOGS", count)
    tools.logger("Retrieved results x20.", "display_log()")
    table = PrettyTable(['#', 'ENTRY', 'ACTION', 'UNIQUE ID', 'TIMESTAMP'])
    table.align = 'l'
    for row in results:
        table.add_row([row[0], row[1], row[2], row[3], row[4]])
    tools.logger("Created audit log table.", "display_log()")
    print table
    stop = time.time()
    tools.logger("Printed audit log table.", "display_log()")
    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                         rounding="ROUND_UP"))
    tools.logger(("Returned %i results in %s seconds" % (count, duration[:5])),
                 "display_log()")
    print "Returned %s results in %s seconds" % (count, duration[:5])
    all = raw_input("Want to see all entries? [Yes/No]: ")
    if all == "Yes":
        tools.logger("User requested ALL entries.", "display_log()")
        count = 9999999
        start = time.time()
        results = db.search("auditlog", "LOGS", count)
        tools.logger("Retrieved results x9999999.", "display_log()")
        table = PrettyTable(['#', 'ENTRY', 'ACTION', 'UNIQUE ID', 'TIMESTAMP'])
        table.align = 'l'
        for row in results:
            table.add_row([row[0], row[1], row[2], row[3], row[4]])
        tools.logger("Created audit log table.", "display_log()")
        print table
        stop = time.time()
        tools.logger("Printed audit log table.", "display_log()")
        duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                                        rounding="ROUND_UP"))
        tools.logger(("Returned %i results in %s seconds" %
                      (count, duration[:5])), "display_log()")
        print "Returned %s results in %s seconds" % (count, duration[:5])
    else:
        print "Ok."

# Using command-line arguments to control actions. User can use flags to run
# certain, pre-defined scenarios. This will also allow for reuse of code where
# applicable.

parser = arg.ArgumentParser(description=cfg.APP_DESCRIPTION)
# NEW PLAYER function
parser.add_argument('--new-player',
                    dest='new_player',
                    action='store_true',
                    default=False,
                    help='Create a new player. Use --player-name and '
                         '--player-country if you would like to specify those'
                         'pieces of information ahead of time.')

# NEW MATCH function
parser.add_argument('--new-match',
                    dest='new_match',
                    action='store_true',
                    default=False,
                    help='Create a new match.')

parser.add_argument('--swiss-match',
                    dest='swiss_match',
                    action='store_true',
                    default=False,
                    help='Create a new match with swiss pairing.')

# GET LATEST RESULTS function
parser.add_argument('--latest-match',
                    dest='latest_match',
                    action='store_true',
                    default=False,
                    help='Get the results from the latest match.')

# GET LATEST RESULTS function
parser.add_argument('--lookup-match',
                    dest='lookup_match',
                    action='store_true',
                    help='Get the results from a specific match by ID.')

# DELETE PLAYER function
parser.add_argument('--delete-player',
                    dest='delete_player',
                    action='store_true',
                    default=False,
                    help='Delete a player from the match system with prompts.')

# DELETE PLAYER function
parser.add_argument('--edit-player',
                    dest='edit_player',
                    action='store_true',
                    default=False,
                    help='Edit a player\'s exiting information')

# DELETE MATCH function
parser.add_argument('--delete-match',
                    dest='delete_match',
                    action='store_true',
                    help='Delete a match from the match system by ID.')

# LIST RESULTS function
parser.add_argument('--list-matches',
                    dest='list_matches',
                    action='store_true',
                    default=False,
                    help='List Results from a recent match.')

# LIST PLAYERS function
parser.add_argument('--list-players',
                    dest='list_players',
                    action='store_true',
                    default=False,
                    help='List all players.')

# VIEW AUDIT LOG function
parser.add_argument('--audit-log',
                    dest='audit_log',
                    action='store_true',
                    default=False,
                    help='Display the Audit Logs.')

args = parser.parse_args()


# ROUTING LOGIC #

if args.new_player:
    new_player()

if args.new_match:
    go_match()

if args.swiss_match:
    swiss_match()

if args.delete_player:
    edit_player("delete")

if args.edit_player:
    edit_player("edit")

if args.list_players:
    list_players()

if args.delete_match:
    delete_match()

if args.list_matches:
    list_matches()

if args.lookup_match:
    lookup_match()

if args.latest_match:
    latest_match()

if args.audit_log:
    display_log()


# IF NO ARGUMENTS #
# Sometimes people need a bit of help...

if len(sys.argv) == 1:
    print "Sometimes you just don't know what to do. " \
          "That's ok, here ya go. Now go have fun!"
    raw_input("Press any key to see the argument help.")
    print parser.print_help()