from data_base.create_table import create_table
from data_base.db import create_connection
from data_base.models import create_user_table, create_model_table, create_auto_table, create_order_table, create_brands_table

if __name__ == '__main__':
    con = create_connection()

    create_table(con, create_user_table)
    create_table(con, create_model_table)
    create_table(con, create_auto_table)
    create_table(con, create_order_table)
    create_table(con, create_brands_table)
    con.close()


