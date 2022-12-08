from data_base.db import create_connection


def select_auto(brand, model):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM auto, brands, model WHERE id_brand = brands.id AND brands.brand = '{brand}' AND "
                   f"id_model = model.id AND model.model = '{model}'")
    auto = cursor.fetchall()
    cursor.close()
    con.close()
    return auto


def select_auto_for_form():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT auto.number, brands.brand, model.model, location, cost FROM auto, brands, model "
                   f"WHERE id_brand = brands.id AND "
                   f"id_model = model.id ")
    auto = cursor.fetchall()
    cursor.close()
    con.close()
    return auto


def select_order():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT auto.number, users.number, orders.end_data, users.name, users.last_name, users.drive_license, brands.brand, model.model "
                   f"FROM orders, users, auto, model, brands "
                   f"WHERE id_user = users.id AND id_auto = auto.id AND id_model = model.id AND id_brand = brands.id")
    order = cursor.fetchall()
    cursor.close()
    con.close()
    print(type(order))
    return order


def select_user():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    user = cursor.fetchall()
    cursor.close()
    con.close()
    return user


def select_model():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM model")
    model = cursor.fetchall()
    cursor.close()
    con.close()
    return model


def select_brand():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM brands")
    brand = cursor.fetchall()
    cursor.close()
    con.close()
    return brand


def select_price(number):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT cost FROM auto WHERE number = '{number}'")
    price = cursor.fetchall()
    cursor.close()
    con.close()
    return price[0][0]


def select_model_for_addmodel(brand):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT model FROM model")
    model = cursor.fetchall()
    cursor.close()
    con.close()
    return model


def select_brand_for_insert_auto(brand):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT id FROM brands WHERE brand='{brand}'")
    id = cursor.fetchone()
    cursor.close()
    con.close()
    return id


def select_model_for_insert_auto(model):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT id FROM model WHERE model='{model}'")
    id = cursor.fetchone()
    cursor.close()
    con.close()
    return id






