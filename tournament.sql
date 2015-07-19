-- Create tournament database

CREATE DATABASE tournament;
\c tournament;

-- Create players table

CREATE TABLE players(
ID SERIAL PRIMARY KEY  NOT NULL,
NAME    TEXT    NOT NULL,
COUNTRY TEXT    NOT NULL
);

-- Create matches table

CREATE TABLE matches(
ID SERIAL PRIMARY KEY  NOT NULL,
PLAYER_1    TEXT    NOT NULL,
PLAYER_2    TEXT    NOT NULL,
WINNER      TEXT    NOT NULL,
TIMESTAMP   TEXT    NOT NULL
);

CREATE TABLE auditlog(
ID SERIAL PRIMARY KEY  NOT NULL,
entry  TEXT    NOT NULL,
action  TEXT    NOT NULL,
unique_id    TEXT    NOT NULL,
timestamp    TEXT    NOT NULL
);
