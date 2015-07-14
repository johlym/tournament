__author__ = 'jlyman'

# TOURNAMENT MATCHUP APPLICATION
# Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
# for match and player information.

import argparse as arg
import config as cfg
import datetime as dt
import psycopg2
import sys
import tournament as trn


# PLAYER ORIENTED FUNCTIONS #


# Create a new player based on their name and country of origin.
def new_player(player_name, player_country):
    if not player_name:
        print "You forgot the Player's Name."
        player_name = raw_input("Player's Name: ")
    if not player_country:
        print "You forgot the Player's Country of Origin."
        player_country = raw_input("Country of Origin: ")
    print "Creating new entry for %s from %s" % (player_name, player_country)
    print "Created new entry."

# Delete an existing player based on their ID.
def delete_player():
    print "Delete an Existing Player."


# Get a list of players based on criteria and display method.
def list_players(criteria, method):
    print "List All Players."


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


# Rank Players by Number of Wins
def list_win_ranking():
    print "List Ranking of Players by Wins"


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
parser.add_argument('--get-results',
                    dest='get_results',
                    action='store_true',
                    default=False,
                    help='Get the results from a match.')

# DELETE PLAYER function
parser.add_argument('--delete-player',
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

# LIST RESULTS BY FILTER function
parser.add_argument('--get-results-by',
                    dest='get_results_by',
                    action='store',
                    help='Get Results from a recent match by FILTER.')

# LIST PLAYERS function
parser.add_argument('--list-players',
                    dest='list_players',
                    action='store_true',
                    default=False,
                    help='List all players.')

args = parser.parse_args()


# ROUTING LOGIC #

if args.new_player == True:
    print "CREATE A NEW PLAYER"
    new_player(args.player_name, args.player_country)
    print "Done."

if args.new_match == True:
    print "START A NEW MATCH"
    new_match(args.match_players[0],args.match_players[1], args.match_name)


# IF NO ARGUMENTS #
# Sometimes people need a bit of help...

if len(sys.argv) == 1:
    print "We understand that sometimes you just don't know what to do. " \
          "That's ok, here ya go. Now go have fun!"
    print parser.print_help()