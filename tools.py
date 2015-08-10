__author__ = 'jlyman'

# extra but useful stuff, used mostly by the unit tests

import config as cfg
from prettytable import PrettyTable
import psycopg2


# Used for generating the two-part SWISS table

def table_gen(header, data, align):
    table = PrettyTable(header)
    table.align = align
    for d in data:
        table.add_row([d[0], d[1], d[2]])
    return table


# Everything beyond this point is used for unit tests.

def connect():
    # Connect to the PostgreSQL database.  Returns a database connection.
    return psycopg2.connect(database=cfg.DATABASE_NAME,
                            user=cfg.DATABASE_USERNAME,
                            password=cfg.DATABASE_PASSWORD)


def bulksql(query):  # use this one for unit testing; it handles bulk SQL better
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def query(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    if "SELECT" in query:
        results = cursor.fetchall()
    else:
        results = ""
    connection.commit()
    cursor.close()
    connection.close()
    return results