__author__ = 'jlyman'

# extra but useful stuff

import datetime, tournament as trn, uuid

# the ability to log behaviors is always nice.

def logger(entry, action):
    unique_id = str(uuid.uuid4())
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    connection = trn.connect()
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