import test_info as db

connect_to_db = db.create_connection('test_db')

db.get_stores_name(connect_to_db)

while True:
    try:
        user = int(input("Вы можете отобразить список продуктов по "
                         "выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0: "))
        if user == 0:
            print("Выход из программы.")
            break
        else:
            db.get_products_info(connect_to_db, user)
    except ValueError:
        print("Пожалуйста, введите корректный числовой идентификатор магазина.")