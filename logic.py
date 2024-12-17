import random


def play_game(min_number, max_number, attempts, initial_capital):
    capital = initial_capital
    secret_number = random.randint(min_number, max_number)

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Ваш стартовый капитал: {capital} единиц.")
    print(f"Угадайте число от {min_number} до {max_number} за {attempts} попыток.\n")

    for attempt in range(1, attempts + 1):
        print(f"\nПопытка {attempt} из {attempts}. Ваш текущий капитал: {capital}.")

        try:
            guess = int(input("Введите число: "))
            bet = int(input("Введите вашу ставку: "))
        except ValueError:
            print("Ошибка: вводите только числа!")
            continue

        if bet > capital or bet <= 0:
            print("Ставка должна быть положительной и не превышать ваш капитал!")
            continue

        if guess == secret_number:
            print(f"Поздравляем! Вы угадали число {secret_number}.")
            capital += bet
            print(f"Ваш выигрыш: {bet * 2}. Текущий капитал: {capital}.")
            break
        else:
            print(
                f"Вы не угадали. Загаданное число было {secret_number}." if attempt == attempts else "Попробуйте снова!")
            capital -= bet

        if capital <= 0:
            print("Вы потеряли весь капитал. Игра окончена.")
            break

    print(f"\nИгра завершена. Ваш итоговый капитал: {capital}.")