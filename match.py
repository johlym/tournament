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
import random
import sys
import time
import tools


# PLAYER ORIENTED FUNCTIONS #


# Create a new player based on their name and country of origin.
def new_player():
    tools.logger("Presenting Questionnaire.",
                 "new_player()")
    print "Please enter the player's Name: "
    player_name = raw_input("Player's Name: ")
    tools.logger("Prompted for player name", "new_player()")
    tools.logger("Received player name " + player_name, "new_player()")
    print "Please enter the player's Country of Origin: "
    player_country = raw_input("Country of Origin: ")
    tools.logger("Prompted for player country", "new_player()")
    tools.logger("Received player country " + player_country, "new_player()")
    print "Creating new entry for %s from %s" % (player_name, player_country)
    start = time.time()
    db.register_player(player_name,player_country)
    stop = time.time()
    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                             rounding="ROUND_UP"))
    print "Successfully created new entry in %i seconds" % duration[:5]
    tools.logger("Database entry created for " + player_name + " from " +
           player_country + ".",
           "new_player()")
    tools.logger("Function fully complete.", "new_player()")


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
    tools.logger("Requesting all players in the database.", "list_players()")
    results = db.count_players()
    for row in results:

        print "ID# " + str(row[0]) + " | " \
              "NAME: " + row[1] + " | " \
              "COUNTRY: " + row[2]
    # need to add code to get their win counts.


# Update player information. This needs the player ID from the SQL database.
def update_player(player_id):
    print "Functionality Coming Soon."

# MATCH ORIENTED FUNCTIONS #


# Initiate a match. Player_1 and Player_2 should be IDs.
def go_match():
    player_1 = raw_input("ID# for Player 1: ")
    player_2 = raw_input("ID# for Player 2: ")
    tools.logger("Starting match between " + player_1 + " and " + player_2,
                 "go_match()")
    print "Match between %s and %s" % (player_1, player_2)
    # Randomly pick between one or two.
    random_int = random.randrange(1, 3)
    print random_int
    tools.logger("Generated random number " + str(random_int), "go_match()")
    # If the random number is even: player 1 wins. Else: player 2 wins.
    if random_int == 2:
        # the random number is even:
        print player_1 + "wins!"
        tools.logger("Stated that player 1 wins.", "go_match()")
        winner = player_1
        loser = player_2
    else:
        # the random number is odd:
        print "Player " + player_2 + " wins!"
        tools.logger("Stated that player 2 wins.", "go_match()")
        winner = player_2
        loser = player_1
    db.report_match(winner, loser, player_1, player_2)
    print "Finished."



# Delete an existing match
def delete_match(match_id):
    print "Delete an Existing Match."
    # delete a match from the matches table, using the match ID.


# Get a list of matches based on criteria and display method
def list_matches():
    start = time.time()
    tools.logger("Listing all matches.", "list_matches()")
    print "List All Matches"
    # display all matches in the matches table, (in groups of ten,
    # with names, eventually).
    rows = db.player_standings()
    count = 0
    for row in rows:
        print "ID# " + str(row[0]) + " | " \
              "PLAYER 1: " + str(row[1]) + " | " \
              "PLAYER 2: " + str(row[2]) + " | " \
              "WINNER: " + str(row[3]) + " | " \
              "TIMESTAMP: " + row[4]
        count += 1
    stop = time.time()
    duration = str(Decimal(float(stop - start)).quantize(Decimal('.01'),
                                             rounding="ROUND_UP"))
    tools.logger(("Returned %s results in %s seconds" % (count, duration[
                    :5])), "list_matches")
    print "Returned %s results in %s seconds" % (count, duration[:5])

# Get the latest match's information
def latest_match():
    print "The Latest Match"
    # get the latest match in the matches table and fetch the player names to
    # display who won and lost.


# Rank Players by Number of Wins
def list_win_ranking():
    print "List Ranking of Players by Wins"
    # get list of players and their IDs.
    # for each player, count the number of times they won in every match

# Any good app keeps a log.

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
    new_player()

if args.new_match:
    print "START A NEW MATCH"
    go_match()

if args.delete_player:
    print "DELETE PLAYER"
    data = ''   # need this for a happy IDE.
    delete_player("by_name", data)

if args.list_players:
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
    list_matches()

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

tools.logger("Script completed.", "__main__")