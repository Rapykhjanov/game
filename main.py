from configparser import ConfigParser
from logic import play_game


def load_settings():
    config = ConfigParser()
    config.read('settings.ini')

    try:
        min_number = config.getint('game', 'min_number')
        max_number = config.getint('game', 'max_number')
        attempts = config.getint('game', 'attempts')
        initial_capital = config.getint('game', 'initial_capital')
        return min_number, max_number, attempts, initial_capital
    except Exception as e:
        print(f"Ошибка загрузки настроек: {e}")
        exit(1)


if __name__ == "__main__":
    settings = load_settings()
    play_game(*settings)