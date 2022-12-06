
from psycopg2 import OperationalError




class Table:

    def __init__(self, connection, query):
        #connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)

            print("Query executed successfully")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        finally:
            connection.commit()
            #connection.close()