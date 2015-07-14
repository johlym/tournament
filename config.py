__author__ = 'jlyman'

# CONFIGURATION FILE
# Contains all configuration variables and other constants used frequently
# throughout the application.

APP_DESCRIPTION = '''
TOURNAMENT MATCHUP APPLICATION
Simulates 1-on-1 matchups and swiss ranked matches. Queries a pgSQL database
for match and player information.'''
APP_AUTHOR = 'Johnathan Lyman'
APP_AUTHOR_SHORT = __author__
APP_COPYRIGHT = 'Public Domain'
APP_VERSION = '0.1'
APP_TITLE = 'PyTournament'

DATABASE_LOCATION = 'localhost'
DATABASE_NAME = 'tournament'
DATABASE_PORT = '5432'
DATABASE_USERNAME = 'postgres'
DATABASE_PASSWORD = 'postgres'