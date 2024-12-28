import sqlite3


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_category(connection, category):
    sql = '''INSERT INTO categories (code, title) VALUES (?,?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, category)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_store(connection, store):
    sql = '''INSERT INTO stores (title) VALUES (?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, store)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_product(connection, product):
    sql = '''
    INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) 
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def get_stores_name(connection):
    sql = '''
    SELECT store_id, title FROM stores
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def get_products_info(connection, store_id):
    sql = '''
    SELECT 
        p.title AS product_title,
        c.title AS category_title,
        p.unit_price,
        p.stock_quantity
    FROM products p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (store_id,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"Название продукта: {row[0]}")
                print(f"Категория: {row[1]}")
                print(f"Цена: {row[2]}")
                print(f"Количество на складе: {row[3]}")
                print('------------------------------')
        else:
            print("Продукты для данного магазина не найдены.")
    except sqlite3.Error as e:
        print(e)


sql_to_create_categories_table = '''
CREATE TABLE IF NOT EXISTS categories (
    code VARCHAR(2) NOT NULL PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
'''

sql_to_create_stores_table = '''
CREATE TABLE IF NOT EXISTS stores (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL
)
'''

sql_to_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(250) NOT NULL,
    category_code VARCHAR(2) NOT NULL,
    unit_price FLOAT NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER NOT NULL,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES stores (store_id)
)
'''

database_name = 'test_db'
my_connection = create_connection(database_name)

if my_connection is not None:
    print('Successfully connected to database')

    # create_table(my_connection, sql_to_create_categories_table)
    # create_table(my_connection, sql_to_create_stores_table)
    # create_table(my_connection, sql_to_create_products_table)
    #
    # insert_category(my_connection, ('FD', 'Food products'))
    # insert_category(my_connection, ('EL', 'Electronics'))
    # insert_category(my_connection, ('CL', 'Clothes'))
    #
    # insert_store(my_connection, ('Asia',))
    # insert_store(my_connection, ('Globus',))
    # insert_store(my_connection, ('Spar',))
    #
    # insert_product(my_connection, ('Apple', 'FD', 1.5, 100, 1))
    # insert_product(my_connection, ('Laptop', 'EL', 800.0, 10, 2))
    # insert_product(my_connection, ('T-shirt', 'CL', 15.0, 50, 3))

    my_connection.close()