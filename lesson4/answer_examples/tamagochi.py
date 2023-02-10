"""
Поели.. теперь можно и поспать!
Поспали.. теперь можно и поесть!)

Реализуем аналог тамагочи.
Основной функционал. Данные о состоянии питомца хранятся в файле. Они постоянно обновляются по ходу работы программы.
Характеристики питомца:
    - Имя питомца.
    - Жизненная энергия - максимум 100. Изначально 100. Если опустится ниже 0 - питомец отправится в Вальгаллу.
    - Настроение - максимум 100. Изначально 50. Если опустится ниже 0 - питомец уйдёт в депрессию.

Игра идёт по дням.
Каждый день питомцу даётся 100 очков действия.
Каждое действие (игра, кормёжка, сон) отнимает определённое количество очков действия и
влияет на характеристики питомца.
Вам придётся организовать досуг подопечного и не убить его в процессе. Продержитесь как можно дольше!
После того как питомец перейдёт в неиграбельное состояние - итоговый результат записывается в таблицу лидеров.

"""

import datetime
import random
import time
import os
import sys

MAX_HEALTH = 100
MAX_HAPPINESS = 100
MAX_ENERGY = 100


def print_with_dots(phrase):
    print(phrase, end="")
    time.sleep(0.2)
    print(".", end="")
    time.sleep(0.2)
    print(".", end="")
    time.sleep(0.2)
    print(".")
    time.sleep(0.2)


def read_data_from_file(file_name):
    print_with_dots("Открываем сохранение")
    with open(file_name, "r", encoding="utf-8") as f:
        name = f.readline().replace('\n', '')

        _health = f.readline()
        if _health:
            _health = int(_health)
        else:
            _health = MAX_HEALTH

        _happiness = f.readline()
        if _happiness:
            _happiness = int(_happiness)
        else:
            _happiness = MAX_HAPPINESS

        _energy = f.readline()
        if _energy:
            _energy = int(_energy)
        else:
            _energy = MAX_ENERGY

        _date = f.readline()
        if _date:
            _date = datetime.datetime.strptime(_date.replace('\n', ''), "%d.%m.%Y %H:%M:%S")
        else:
            _date = datetime.datetime.now()

    return name, _health, _happiness, _energy, _date


def write_data_to_file(file_name, name, health, happiness, energy):
    print_with_dots("Сохраняем прогресс")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(name + '\n')
        f.write(str(health) + '\n')
        f.write(str(happiness) + '\n')
        f.write(str(energy) + '\n')
        date = datetime.datetime.now()
        f.write(datetime.datetime.strftime(date, "%d.%m.%Y %H:%M:%S") + '\n')
    return name, health, happiness, energy, date


def clear_file(file_name):
    print_with_dots("Очистка файла")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("")


def get_data(file_name):
    print_with_dots("Получаем данные из файла")
    if os.path.isfile(file_name) and os.stat(file_name).st_size > 0:
        name, health, happiness, energy, date = read_data_from_file(file_name)
    else:
        print_with_dots("Файла не существует либо он пуст")
        name = input("Введите имя питомца: ")
        name, health, happiness, energy, date = write_data_to_file(file_name, name, MAX_HEALTH, MAX_HAPPINESS, MAX_ENERGY)

    return name, health, happiness, energy, date


def calculate_property(total_val, activity_val, max_val):
    return min(total_val + activity_val, max_val)


def simulate_activity(activity, name, health, happiness, daily_energy):
    activity_val = random.choice(list(activity.keys()))
    activity_choice = activity[activity_val]
    print_with_dots(f"{name}: {activity_val}")
    health = calculate_property(health, activity_choice["health"], MAX_HEALTH)
    happiness = calculate_property(happiness, activity_choice["happiness"], MAX_HAPPINESS)
    daily_energy = calculate_property(daily_energy, activity_choice["daily_energy"], MAX_ENERGY)
    write_data_to_file("tamagochi.txt", name, health, happiness, daily_energy)
    return health, happiness, daily_energy


def play_game(name, health, happiness, daily_energy):
    values = {
        "играет в дурака": {
            "health": -10,
            "happiness": 20,
            "daily_energy": -20,
        },
        "наблюдает за утками": {
            "health": -50,
            "happiness": 50,
            "daily_energy": -50,
        },
        "пускает мыльные пузыри": {
            "health": -30,
            "happiness": 40,
            "daily_energy": -10,
        },
        "конструирует замок из песка": {
            "health": -20,
            "happiness": 10,
            "daily_energy": -40,
        }
    }
    health, happiness, daily_energy = simulate_activity(values, name, health, happiness, daily_energy)
    return health, happiness, daily_energy


def sleep(name, health, happiness, daily_energy):
    values = {
        "жёстко спит": {
            "health": 10,
            "happiness": -20,
            "daily_energy": -20,
        },
        "быстро-быстро спит": {
            "health": 0,
            "happiness": -10,
            "daily_energy": -20,
        },
        "дремлет": {
            "health": 30,
            "happiness": 40,
            "daily_energy": -20,
        },
        "пускает слюни": {
            "health": -20,
            "happiness": 10,
            "daily_energy": -20,
        },
        "считает овец": {
            "health": 10,
            "happiness": -10,
            "daily_energy": -20,
        }
    }
    health, happiness, daily_energy = simulate_activity(values, name, health, happiness, daily_energy)
    return health, happiness, daily_energy


def eat(name, health, happiness, daily_energy):
    values = {
        "жрёт макароны": {
            "health": 10,
            "happiness": -20,
            "daily_energy": -20,
        },
        "рубает капусту": {
            "health": 0,
            "happiness": -10,
            "daily_energy": -20,
        },
        "наслаждается сиропом": {
            "health": 30,
            "happiness": 40,
            "daily_energy": -20,
        },
        "хомячит крекеры": {
            "health": -20,
            "happiness": 10,
            "daily_energy": -20,
        },
        "употребляет шашлындос": {
            "health": 10,
            "happiness": -10,
            "daily_energy": -20,
        }
    }
    health, happiness, daily_energy = simulate_activity(values, name, health, happiness, daily_energy)
    return health, happiness, daily_energy


def refill_daily_energy(energy, date):
    if energy <= 0 and date.date() < datetime.date.today():
        energy = MAX_ENERGY
    return energy


if __name__ == "__main__":
    # проверяем, существует ли файл с параметрами тамагоча
    # если нет, то создаём
    # спрашиваем у пользователя имя питомца, заполняем начальные значения
    # иначе читаем данные
    print_with_dots("Начинаем игру")
    print_with_dots("Формируем питомца")
    tamagochi_name, tamagochi_health, tamagochi_happiness, daily_energy, date = get_data("tamagochi.txt")

    daily_energy = refill_daily_energy(daily_energy, date)

    while tamagochi_health > 0 and tamagochi_happiness > 0 and daily_energy > 0:
        print("-" * 15, tamagochi_name.upper(), "-" * 15)
        print(f"Осталось дневной энергии: {daily_energy}/{MAX_ENERGY}")
        print(f"Здоровье питомца: {tamagochi_health}/{MAX_HEALTH}")
        print(f"Счастье питомца: {tamagochi_happiness}/{MAX_HAPPINESS}")
        print("Выберите действие:")
        print("1. Игра")
        print("2. Сон")
        print("3. Еда")
        print("4. Выход")

        choice = input("Введите номер действия: ")
        if choice == "1":
            tamagochi_health, tamagochi_happiness, daily_energy = play_game(tamagochi_name, tamagochi_health, tamagochi_happiness, daily_energy)
        elif choice == "2":
            tamagochi_health, tamagochi_happiness, daily_energy = sleep(tamagochi_name, tamagochi_health, tamagochi_happiness, daily_energy)
        elif choice == "3":
            tamagochi_health, tamagochi_happiness, daily_energy = eat(tamagochi_name, tamagochi_health, tamagochi_happiness, daily_energy)
        else:
            print_with_dots("Запущен процесс гибернации")
            sys.exit()
    else:
        if tamagochi_health <= 0:
            print_with_dots(f"{tamagochi_name} отправился в Вальгаллу")
            clear_file("tamagochi.txt")
        elif tamagochi_happiness <= 0:
            print_with_dots(f"{tamagochi_name} ушёл в депрессию")
            clear_file("tamagochi.txt")
        elif daily_energy <= 0:
            print_with_dots(f"{tamagochi_name} потратил все очки энергии. Возвращайтесь завтра")
        else:
            print_with_dots(f"{tamagochi_name} что-то сделал и всё сломалось")
    sys.exit()


