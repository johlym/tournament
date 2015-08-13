__author__ = 'jlyman'

# CONFIGURATION FILE
# Contains all configuration variables and other constants used frequently
# throughout the application.

##########################
# DATABASE CONFIGURATION #
##########################

# Change if your database isn't on the same server
DATABASE_LOCATION = 'localhost'

# Change this to whatever you want. The app calls this setting every time it
# needs to connect. If you change this, make sure to change it in
# tournament.sql, too!
DATABASE_NAME = 'tournament'

# The standard PostgreSQL port. Only change if your setup uses a different
# port number.
DATABASE_PORT = '5432'

# The standard PostgreSQL install will likely create a username/password
# combination of postgres/postgres. Change this to whatever your setup is
# using.
DATABASE_USERNAME = 'postgres'
DATABASE_PASSWORD = 'postgres'

###################
# APP INFORMATION #
###################

# Some information about the app and its author.
APP_DESCRIPTION = '''
TOURNAMENT MATCHUP APPLICATION
Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
for match and player information.'''
APP_AUTHOR = 'Johnathan Lyman'
APP_AUTHOR_SHORT = __author__
APP_COPYRIGHT = 'Public Domain'
APP_VERSION = '1.0'
APP_TITLE = 'PyTournament'
