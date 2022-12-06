from data_base.db import create_connection
from data_base.db_select import select_model_for_insert_auto, select_brand_for_insert_auto


def add_user_db(number, name, lastname, drive_license):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO users (name, last_name, number, drive_license) VALUES "
                   f"('{name}', '{lastname}', {number}, {drive_license})")
    con.commit()
    cursor.close()
    con.close()


def add_auto_db(number, brand, location, tank, cost, free, model):
    con = create_connection()
    cursor = con.cursor()
    id_model = select_model_for_insert_auto(model)
    id_brand = select_brand_for_insert_auto(brand)
    cursor.execute(f"INSERT INTO auto (number, id_brand, id_model, location, tank, cost, free) VALUES"
                   f"('{number}', {id_brand[0]}, {id_model[0]}, '{location}', {tank}, {cost}, {bool(free)})")
    con.commit()
    cursor.close()
    con.close()


def add_model_db(model):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO model (model) VALUES ('{model}')")
    con.commit()
    cursor.close()
    con.close()


def add_brand_db(brand):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO brands (brand) VALUES ('{brand}')")
    con.commit()
    cursor.close()
    con.close()


def add_order_db(cost, number_user, number_car, cout_hour, date_issue, end_date):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO orders (id_user, id_auto, cout_hour, cost, date_issue, end_data) VALUES "
                   f"("
                   f"(SELECT id FROM users WHERE number = '{number_user}'),"
                   f"(SELECT id FROM auto WHERE number = '{number_car}'),"
                   f"'{cout_hour}',"
                   f"'{cost}',"
                   f"'{date_issue}',"
                   f"'{end_date}'"
                   f")"
                   )
    con.commit()
    cursor.close()
    con.close()
