__author__ = 'jlyman'

# TOURNAMENT MATCHUP APPLICATION
# Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
# for match and player information.

import argparse as arg
import config as cfg
import datetime as dt
import psycopg2
import tournament as trn


# PLAYER ORIENTED FUNCTIONS #


# Create a new player based on their name and country of origin.
def new_player(player_name, player_country):
    print "Create a New Player."


# Delete an existing player based on their ID.
def delete_player(player_id):
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
                    help='')
# NEW MATCH function
parser.add_argument('--new-match',
                    dest='new_match',
                    action='store_true',
                    help='')
# EXECUTE MATCH function
# GET LATEST RESULTS function
# DELETE PLAYER function
# DELETE MATCH function
# LIST RESULTS BY PLAYER function
# LIST RESULTS BY DATE function
# LIST PLAYERS function

args = parser.parse_args()