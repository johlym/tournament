__author__ = 'jlyman'

import psycopg2

def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect(database='tournament', user='postgres')

# Create database contents
connection = connect()
cursor = connection.cursor()
cursor.execute("CREATE TABLE players(id serial NOT NULL,"
               "name text NOT NULL, country text "
               "NOT NULL, code text, CONSTRAINT players_pkey PRIMARY KEY (id))"
               "WITH (OIDS=FALSE);")
cursor.execute("ALTER TABLE players OWNER TO postgres;")
cursor.execute("CREATE TABLE matches (id serial NOT NULL, "
               "player_1 text NOT NULL, player_2 "
               "text NOT NULL, winner text NOT NULL, "
               "\"timestamp\" text NOT NULL,"
               "CONSTRAINT matches_pkey PRIMARY KEY (id))"
               "WITH (OIDS=FALSE);")
cursor.execute("ALTER TABLE matches OWNER TO postgres;")
cursor.execute("CREATE TABLE auditlog ("
              "id serial NOT NULL,"
              "entry text NOT NULL,"
              "action text NOT NULL,"
              "unique_id text NOT NULL,"
              "\"timestamp\" text NOT NULL,"
              "CONSTRAINT auditlog_pkey PRIMARY KEY (id)) WITH (OIDS=FALSE);")
cursor.execute("ALTER TABLE auditlog OWNER TO postgres;")
connection.commit()
cursor.close()
connection.close()