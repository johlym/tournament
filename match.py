#!/usr/bin/env python

__author__ = 'jlyman'

# TOURNAMENT MATCHUP APPLICATION
# Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
# for match and player information.

import argparse as arg
import config as cfg
import time
import datetime
import sys
import tournament as trn
import uuid


# PLAYER ORIENTED FUNCTIONS #


# Create a new player based on their name and country of origin.
def new_player(player_name, player_country):
    if not player_name:
        print "You forgot the Player's Name."
        player_name = raw_input("Player's Name: ")
        logger("Prompted for player name", "new_player()")
        logger("Received player name " + player_name, "new_player()")
    if not player_country:
        print "You forgot the Player's Country of Origin."
        player_country = raw_input("Country of Origin: ")
        logger("Prompted for player country", "new_player()")
        logger("Received player country " + player_country, "new_player()")
    print "Creating new entry for %s from %s" % (player_name, player_country)
    start = time.time()
    trn.register_player(player_name,player_country)
    stop = time.time()
    duration = stop - start
    print "Successfully created new entry in %d seconds" % duration
    logger("Database entry created for " + player_name + " from " +
           player_country + ".",
           "new_player()")
    logger("Function fully complete.", "new_player()")

# Delete an existing player based on their ID.
def delete_player(method, data):
    # Check by ID
    if method == "by_id":
        # Check if ID is valid
        if id == "0" or 0:
            raise ValueError('ID Number 0 is invalid.')
        print "Looking Up Player with ID# %s" % data
    # Check by name
    elif method == "by_name":
        if data == '':
            data = raw_input("Enter the Player\'s Name: ")
        print "Looking Up Player with Name %s" % data
    # Anything else is a no-go.
    else:
        raise NotImplementedError('The method %s is unsupported.', method)
    return 0


# Get a list of players based on criteria and display method.
def list_players():
    print "List All Players."
    print "Here's a list of all players in the database: "
    print "=============================================="
    for row in trn.count_players():
        print "ID# " + str(row[0]) + " | " \
              "NAME: " + row[1] + " | " \
              "COUNTRY: " + row[2]


# Update player information
def update_player(match_id):
    print "Update Player Information."

# MATCH ORIENTED FUNCTIONS #

# Create a new match
def new_match(player_1, player_2, match_name):
    print "Create a New Match."


# Start a match
def go_match(player_1, player_2, match_name):
    print "Start a Match."


# Delete an existing match
def delete_match(match_id):
    print "Delete an Existing Match."


# Get a list of matches based on criteria and display method
def list_matches(criteria, method):
    print "List All Matches"


# Get the latest match's information
def latest_match():
    print "The Latest Match"

# Rank Players by Number of Wins
def list_win_ranking():
    print "List Ranking of Players by Wins"

# Any good app keeps a log.
def logger(entry, action):
    unique_id = str(uuid.uuid4())
    timestamp = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    connection = trn.connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO auditlog "
                   "(entry, action, unique_id, timestamp) "
                   "VALUES (\'" + entry + "\',"
                   "\'" + action + "\',"
                   " \'" + unique_id + "\',"
                   " \'" + timestamp + "\');")
    connection.commit()
    cursor.close()
    connection.close()


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

parser.add_argument('--player-name',
                    dest='player_name',
                    action='store',
                    help='Your Player\'s Name. Useful for --new-player, '
                         '--new-match, --delete-player, --get-results-by')

parser.add_argument('--player-country',
                    dest='player_country',
                    action='store',
                    help='Your Player\'s Country of Origin')

# NEW MATCH function
parser.add_argument('--new-match',
                    dest='new_match',
                    action='store_true',
                    default=False,
                    help='Create a new match.')

# GET LATEST RESULTS function
parser.add_argument('--get-latest-result',
                    dest='get_latest_result',
                    action='store_true',
                    default=False,
                    help='Get the results from the latest match.')

# GET LATEST RESULTS function
parser.add_argument('--get-result',
                    dest='get_result',
                    action='store',
                    help='Get the results from a specific match by ID.')

# DELETE PLAYER function
parser.add_argument('--delete-player',
                    dest='delete_player',
                    action='store_true',
                    default=False,
                    help='Delete a player from the match system with prompts.')

parser.add_argument('--delete-player-by-id',
                    dest='delete_player_id',
                    action='store',
                    help='Delete a player from the match system by ID')

# DELETE MATCH function
parser.add_argument('--delete-match',
                    dest='delete_match_id',
                    action='store',
                    help='Delete a match from the match system by ID.')

# LIST RESULTS function
parser.add_argument('--list-results',
                    dest='list_results',
                    action='store_true',
                    default=False,
                    help='List Results from a recent match.')

# LIST PLAYERS function
parser.add_argument('--list-players',
                    dest='list_players',
                    action='store_true',
                    default=False,
                    help='List all players.')

args = parser.parse_args()


# ROUTING LOGIC #

if args.new_player:
    print "CREATE A NEW PLAYER"
    new_player(args.player_name, args.player_country)

if args.new_match:
    print "START A NEW MATCH"
    new_match(args.match_players[0],args.match_players[1], args.match_name)

if args.delete_player:
    print "DELETE PLAYER"
    data = ''   # need this for a happy IDE.
    delete_player("by_name", data)

if args.list_players:
    print "LIST PLAYERS"
    list_players()

if args.delete_player_id:
    print "DELETE PLAYER BY ID"
    id_number = args.delete_player_id
    if not args.delete_player_id > 0:
        id_number = raw_input("Player ID Number [Leave Blank if Unknown]:")
    delete_player("by_id", id_number)

if args.delete_match_id:
    print "DELETE MATCH"

if args.list_results:
    print "LIST RESULTS"

if args.get_result:
    print "GET RESULT BY ID"
    if args.get_result < 1:
        print "The ID Number has to be 1 or greater."
    print "Looking up match results by ID number %s" % args.get_results_by_id

if args.get_latest_result:
    print "GET THE LATEST MATCH RESULT"
    latest_match()


# IF NO ARGUMENTS #
# Sometimes people need a bit of help...

if len(sys.argv) == 1:
    print "We understand that sometimes you just don't know what to do. " \
          "That's ok, here ya go. Now go have fun!"
    raw_input("Press any key to see the argument help.")
    print parser.print_help()