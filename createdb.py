__author__ = 'jlyman'

import psycopg2


def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect(database='tournament', user='postgres')


def drop():
    co = connect()
    cu = co.cursor()
    cu.execute("DROP TABLE IF EXISTS players;")
    cu.execute("DROP TABLE IF EXISTS matches;")
    cu.execute("DROP TABLE IF EXISTS auditlog;")
    co.commit()
    cu.close()
    co.close()
    return 0


def truncate(table):
    co = connect()
    cu = co.cursor()
    cu.execute("TRUNCATE " + table + ";")
    co.commit()
    cu.close()
    co.close()


# Create database contents
def create():
    co = connect()
    cu = co.cursor()
    cu.execute("CREATE TABLE players(id serial NOT NULL,"
               "name text NOT NULL, country text "
               "NOT NULL, code text, CONSTRAINT players_pkey PRIMARY KEY (id))"
               "WITH (OIDS=FALSE);")
    cu.execute("ALTER TABLE players OWNER TO postgres;")
    cu.execute("CREATE TABLE matches (id serial NOT NULL, "
               "player_1 text NOT NULL, player_2 "
               "text NOT NULL, winner text NOT NULL, "
               "\"timestamp\" text NOT NULL,"
               "CONSTRAINT matches_pkey PRIMARY KEY (id))"
               "WITH (OIDS=FALSE);")
    cu.execute("ALTER TABLE matches OWNER TO postgres;")
    cu.execute("CREATE TABLE auditlog ("
               "id serial NOT NULL,"
               "entry text NOT NULL,"
               "action text NOT NULL,"
               "unique_id text NOT NULL,"
               "\"timestamp\" text NOT NULL,"
               "CONSTRAINT auditlog_pkey PRIMARY KEY (id)) WITH (OIDS=FALSE);")
    cu.execute("ALTER TABLE auditlog OWNER TO postgres;")
    co.commit()
    cu.close()
    co.close()
    return 0

if __name__ == "__main__":
    drop()
    create()
