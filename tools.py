__author__ = 'jlyman'

# extra but useful stuff

import datetime
import database as db
import uuid
from prettytable import PrettyTable


def table_gen(header, data, align):
    table = PrettyTable(header)
    table.align = align
    for d in data:
        table.add_row([d[0], d[1], d[2]])
    return table
