from psycopg2 import OperationalError
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from data_base.config import HOST, USER, PASSWORD, DB_NAME


def create_connection():
    con = None
    try:
        con = psycopg2.connect(host=HOST,
                               password=PASSWORD,
                               user=USER,
                               database=DB_NAME
                               )

        with con.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print(f'Server version: {cursor.fetchone()}')
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    finally:
        pass
    return con


