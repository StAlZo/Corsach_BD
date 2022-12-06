from data_base.table import Table
from data_base.config import TABLE


def create_table(connection, query):
    if TABLE:
        table = Table(connection, query)
    else:
        print(f"the table is already there")