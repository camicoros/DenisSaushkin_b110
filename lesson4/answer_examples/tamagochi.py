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


def read_data_from_file(file_name):
    print_with_dots("Открываем сохранение")
    with open(file_name, "r", encoding="utf-8") as f:
        name = f.readline().replace('\n', '')
        health = f.readline()
        if health:
            health = int(health)
        else:
            health = MAX_HEALTH
        happiness = f.readline()
        if happiness:
            happiness = int(happiness)
        else:
            happiness = MAX_HAPPINESS

    return name, health, happiness


def write_data_to_file(file_name, name, health, happiness):
    print_with_dots("Сохраняем прогресс")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(name + '\n')
        f.write(str(health) + '\n')
        f.write(str(happiness) + '\n')


def clear_file(file_name):
    print_with_dots("Очистка файла")
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_data(file_name):
    print_with_dots("Получаем данные из файла")
    health = 100
    happiness = 50
    if os.path.isfile(file_name):
        name, health, happiness = read_data_from_file(file_name)
    else:
        print_with_dots("Файла не существует")
        name = input("Введите имя питомца: ")
        write_data_to_file(file_name, name, health, happiness)

    return name, health, happiness


def calculate_energy_left(total_energy, min_energy_cost, max_energy_cost):
    return total_energy - min(random.randint(min_energy_cost, max_energy_cost), total_energy)


def simulate_activity(activity,  min_health_cost, max_health_cost, min_happiness_cost, max_happiness_cost, name, health, happiness, daily_energy):
    print_with_dots(f"{name}: {activity}")
    health = min(MAX_HEALTH, random.choice([health + random.randint(min_health_cost, max_health_cost), health - random.randint(min_health_cost, max_health_cost)]))
    happiness = min(MAX_HAPPINESS, random.choice([happiness + random.randint(min_happiness_cost, max_happiness_cost), happiness - random.randint(min_happiness_cost, max_happiness_cost)]))
    daily_energy = calculate_energy_left(daily_energy, min_health_cost, min_happiness_cost)
    write_data_to_file("tamagochi.txt", name, health, happiness)
    return health, happiness, daily_energy


def play_game(name, health, happiness, daily_energy):
    min_health_cost = 20
    max_health_cost = 50
    min_happiness_cost = 20
    max_happiness_cost = 50
    game_choice = random.choice(["играет в дурака", "играет в лото", "ведёт наблюдение за утками", "занимается шпионской деятельностью"])
    health, happiness, daily_energy = simulate_activity(game_choice, min_health_cost, max_health_cost, min_happiness_cost, max_happiness_cost,  name, health, happiness, daily_energy)
    return health, happiness, daily_energy


def sleep(name, health, happiness, daily_energy):
    min_health_cost = 20
    max_health_cost = 50
    min_happiness_cost = 20
    max_happiness_cost = 50
    sleep_choice = random.choice(["жёстко спит", "быстро-быстро спит", "дремлет", "пускает слюни"])
    health, happiness, daily_energy = simulate_activity(sleep_choice, min_health_cost, max_health_cost,
                                                        min_happiness_cost, max_happiness_cost, name, health, happiness,
                                                        daily_energy)
    return health, happiness, daily_energy


def eat(name, health, happiness, daily_energy):
    min_health_cost = 20
    max_health_cost = 50
    min_happiness_cost = 20
    max_happiness_cost = 50
    food_choice = random.choice(["жрёт макароны", "рубает капусту", "наслаждается сиропом", "хомячит крекеры"])
    health, happiness, daily_energy = simulate_activity(food_choice, min_health_cost, max_health_cost,
                                                        min_happiness_cost, max_happiness_cost, name, health, happiness,
                                                        daily_energy)
    return health, happiness, daily_energy


if __name__ == "__main__":
    # проверяем, существует ли файл с параметрами тамагоча
    # если нет, то создаём
    # спрашиваем у пользователя имя питомца, заполняем начальные значения
    # иначе читаем данные
    daily_energy = MAX_ENERGY
    print_with_dots("Начинаем игру")
    print_with_dots("Формируем питомца")
    tamagochi_name, tamagochi_health, tamagochi_happiness = get_data("tamagochi.txt")

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
            health, happiness, daily_energy = play_game(tamagochi_name, tamagochi_health, tamagochi_happiness, daily_energy)
        elif choice == "2":
            health, happiness, daily_energy = sleep(tamagochi_name, tamagochi_health, tamagochi_happiness, daily_energy)
        elif choice == "3":
            health, happiness, daily_energy = eat(tamagochi_name, tamagochi_health, tamagochi_happiness, daily_energy)
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
            print_with_dots(f"{tamagochi_name} потратил все очки энергии")
        else:
            print_with_dots(f"{tamagochi_name} что-то сделал и всё сломалось")
    sys.exit()


