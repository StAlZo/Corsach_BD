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


def select_order():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute(f"SELECT auto.number, users.number, orders.end_data FROM orders, users, auto "
                   f"WHERE id_user = users.id AND id_auto = auto.id")
    order = cursor.fetchall()
    cursor.close()
    con.close()
    return order


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






