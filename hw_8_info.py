import hw_8 as db
connect_to_db = db.create_countries('''home_work_8.db''')
db.get_cities(connect_to_db)
while True:
    user = int(input('Введите число города чтобы узнать где живет этот ученик введите (0) для выхода: '))
    if user == 0:
        break
    else:
        db.get_students_with_city_names(connect_to_db,user )
        continue