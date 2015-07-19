-- Create tournament database

CREATE DATABASE tournament;
\c tournament;

-- Table: players

-- DROP TABLE players;

CREATE TABLE players
(
  id serial NOT NULL,
  name text NOT NULL,
  country text NOT NULL,
  code text,
  CONSTRAINT players_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE players
  OWNER TO postgres;


-- Table: matches

-- DROP TABLE matches;

CREATE TABLE matches
(
  id serial NOT NULL,
  player_1 text NOT NULL,
  player_2 text NOT NULL,
  winner text NOT NULL,
  "timestamp" text NOT NULL,
  CONSTRAINT matches_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE matches
  OWNER TO postgres;


-- Table: auditlog

-- DROP TABLE auditlog;

CREATE TABLE auditlog
(
  id serial NOT NULL,
  entry text NOT NULL,
  action text NOT NULL,
  unique_id text NOT NULL,
  "timestamp" text NOT NULL,
  CONSTRAINT auditlog_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE auditlog
  OWNER TO postgres;