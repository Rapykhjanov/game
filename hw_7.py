import sqlite3


def create_products(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
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


def insert_product(connection, product):
    sql = '''INSERT INTO product
    (product_title, price, quantity)
     VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(connection, product):
    try:
        sql = '''UPDATE product SET quantity = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} IN UPDATE_QUANTITY function')


def update_price(connection, product):
    try:
        sql = '''UPDATE product SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} IN UPDATE_PRICE function')


def delete_product_by_id(connection, id):
    try:
        sql = '''DELETE FROM product WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} IN DELETE_PRODUCT_BY_ID function')


def select_all(connection):
    try:
        sql = '''SELECT * FROM product'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} IN SELECT_ALL function')


def select_by_price_and_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM product WHERE price <= ? AND quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} IN SELECT_BY_PRICE_AND_QUANTITY function')


def select_by_name(connection):
    try:
        sql = '''SELECT * FROM product WHERE product_title LIKE '%Smart%' '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} IN SELECT_BY_NAME function')


sql_to_create_product_table = '''
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

database_name = 'hw7.db'
my_connection = create_products(database_name)
if my_connection is not None:
    print('Successfully connected to database')
    # create_table(my_connection, sql_to_create_product_table)
    # insert_product(my_connection, ('Laptop', 750.00, 10))
    # insert_product(my_connection, ('Smartphone', 500.00, 25))
    # insert_product(my_connection, ('Wireless Headphones', 120.00, 15))
    # insert_product(my_connection, ('Gaming Mouse', 45.00, 30))
    # insert_product(my_connection, ('Mechanical Keyboard', 80.00, 20))
    # insert_product(my_connection, ('LED Monitor 24"', 150.00, 12))
    # insert_product(my_connection, ('External Hard Drive 1TB', 65.00, 18))
    # insert_product(my_connection, ('Smart Watch', 200.00, 8))
    # insert_product(my_connection, ('Bluetooth Speaker', 70.00, 10))
    # insert_product(my_connection, ('Desk Lamp', 30.00, 50))
    # insert_product(my_connection, ('Office Chair', 120.00, 7))
    # insert_product(my_connection, ('Electric Scooter', 300.00, 5))
    # insert_product(my_connection, ('Coffee Maker', 100.00, 10))
    # insert_product(my_connection, ('Air Purifier', 180.00, 6))
    # insert_product(my_connection, ('Portable Power Bank', 40.00, 25))
    # update_price(my_connection, (100, 2))
    # update_quantity(my_connection, (10, 14))
    # delete_product_by_id(my_connection, 1)
    # select_all(my_connection)
    # select_by_price_and_quantity(my_connection, (100, 30))
    # select_by_name(my_connection)
    my_connection.close()
