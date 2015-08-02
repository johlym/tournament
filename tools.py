__author__ = 'jlyman'

# extra but useful stuff

import datetime
import database as db
import uuid
from prettytable import PrettyTable

# the ability to log behaviors is always nice.


def logger(entry, action):
    unique_id = str(uuid.uuid4())
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    connection = db.connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO auditlog "
                   "(entry, action, unique_id, timestamp) "
                   "VALUES (\'" + entry + "\',"
                   "\'" + action + "\',"
                   " \'" + unique_id + "\',"
                   " \'" + timestamp + "\');")
    connection.commit()
    cursor.close()
    connection.close()


def table_gen(header, data, align):
    table = PrettyTable(header)
    table.align = align
    for d in data:
        table.add_row([d[0], d[1], d[2]])
    return table
