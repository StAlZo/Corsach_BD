create_order_table = """
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        id_user INTEGER REFERENCES users(id),
        id_auto INTEGER REFERENCES auto(id),
        date_issue TIMESTAMP,
        cout_hour INTEGER,
        end_data TIMESTAMP,
        cost INTEGER)
        """


create_auto_table = """
    CREATE TABLE IF NOT EXISTS auto (
        id SERIAL PRIMARY KEY,
        number varchar,
        id_brand INTEGER REFERENCES brands(id),
        id_model INTEGER REFERENCES model(id),
        location varchar,
        tank integer,
        cost integer,
        free boolean)
        """


create_model_table = """
    CREATE TABLE IF NOT EXISTS model (
        id SERIAL PRIMARY KEY,
        model varchar)
        """


create_user_table = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR,
        last_name VARCHAR,
        number VARCHAR,
        drive_license VARCHAR)
        """


create_brands_table = """
    CREATE TABLE IF NOT EXISTS brands (
        id SERIAL PRIMARY KEY,
        brand varchar)
        """