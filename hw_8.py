import sqlite3


def create_countries(db_name):
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


def insert_country(connection, country):
    sql = '''INSERT INTO countries (title) VALUES (?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, country)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_city(connection, city):
    sql = '''INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, city)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def insert_student(connection, student):
    sql = '''INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, student)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def get_students_with_city_names(connection, city_id):
    sql = (
        f'SELECT students.id, students.first_name, students.last_name, cities.title, countries.title, cities.area '
        f'FROM (students JOIN cities ON students.city_id = cities.id) '
        f'JOIN countries ON countries.id = cities.country_id WHERE cities.id = {city_id} ')
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(f"Student: {row[1]} {row[2]}, City: {row[3]} Country: {row[4]} Area: {row[5]}")
    except sqlite3.Error as e:
        print(e)


def get_cities(connection):
    query = '''
    SELECT id, title FROM cities
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_country_table = '''
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL
)
'''

sql_to_create_city_table = '''
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    area FLOAT DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
)
'''
sql_to_create_student_table = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name TEXT DEFAULT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities (id)
)
'''

database_name = 'home_work_8.db'
my_connection = create_countries(database_name)

if my_connection is not None:
    print('Successfully connected to database')
    # create_table(my_connection, sql_to_create_country_table)
    # create_table(my_connection, sql_to_create_city_table)
    # create_table(my_connection, sql_to_create_student_table)
    #
    # insert_country(my_connection, ('Kyrgyzstan',))
    # insert_country(my_connection, ('USA',))
    # insert_country(my_connection, ('China',))
    # insert_country(my_connection, ('France',))
    # insert_country(my_connection, ('Germany',))
    # insert_country(my_connection, ('Japan',))
    # insert_country(my_connection, ('Brazil',))
    #
    # insert_city(my_connection, ('Bishkek', 127.0, 1))
    # insert_city(my_connection, ('New York', 789.0, 2))
    # insert_city(my_connection, ('Beijing', 400.0, 3))
    # insert_city(my_connection, ('Paris', 105.4, 4))
    # insert_city(my_connection, ('Berlin', 120.6, 5))
    # insert_city(my_connection, ('Tokyo', 622.5, 6))
    # insert_city(my_connection, ('Rio de Janeiro', 112.3, 7))
    #
    # insert_student(my_connection, ('John', 'Doe', 3))
    # insert_student(my_connection, ('Alice', 'Johnson', 6))
    # insert_student(my_connection, ('Carlos', 'Perez', 5))
    # insert_student(my_connection, ('Maria', 'Chen', 4))
    # insert_student(my_connection, ('Anna', 'Schmidt', 1))
    # insert_student(my_connection, ('Taro', 'Yamamoto', 7))
    # insert_student(my_connection, ('Fatima', 'Khan', 2))
    # insert_student(my_connection, ('Liam', 'Brown', 1))
    # insert_student(my_connection, ('Sofia', 'Martinez', 3))
    # insert_student(my_connection, ('Chen', 'Wei', 6))
    # insert_student(my_connection, ('Omar', 'Ahmed', 5))
    # insert_student(my_connection, ('Elena', 'Popova', 7))
    # insert_student(my_connection, ('Raj', 'Patel', 4))
    # insert_student(my_connection, ('Isabella', 'Rossi', 2))
    # insert_student(my_connection, ('James', 'Wilson', 1))
    # insert_student(my_connection, ('Sardor', 'Rapykhjanov', 1))
    # get_students_with_city_names(my_connection)
    # get_cities(my_connection)
    my_connection.close()