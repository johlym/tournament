-- Create tournament database

CREATE DATABASE tournament;
\c tournament;

-- Create players table

CREATE TABLE players(
ID INT PRIMARY KEY  NOT NULL,
NAME    TEXT    NOT NULL,
COUNTRY TEXT    NOT NULL
)

-- Create matches table

CREATE TABLE matches(
ID INT PRIMARY KEY  NOT NULL,
MATCH_NAME  TEXT    NOT NULL,
PLAYER_1    TEXT    NOT NULL,
PLAYER_2    TEXT    NOT NULL,
WINNER      TEXT    NOT NULL,
TIMESTAMP   TEXT    NOT NULL
)
