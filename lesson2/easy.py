"""
1. Вы продолжаете посиделки с друзьями/приятелями/родственниками/корешами.
Почти всё в холодильнике уже съедено. Вам выпала участь пойти в магазин, 
пока гости долизывают лёд из морозилки.
В магазине вам предложили купить супы быстрого приготовления по скидке. 
Дёшево и сердито! Вы скупаете все супы, что есть. Пересчитываете их и решаете, 
можно ли возвращаться к гостям с покупками или придётся идти в следующий магазин.

Задание:
Создать переменную number_of_people, 
где будет храниться количество оголодавших гостей.
Создать переменную number_of_soups, 
где будет храниться доступное в магазине количество супов.

В случае если количество супов больше количества гостей, 
выведите сколько целых упаковок супа достанется каждому.

Иначе если количество супов недостаточно, 
выведите сообщение сколько супов вы купили и сколько ещё не хватает.
"""

# Код:
print('Вы выходите из магазина "ПятёрОчка" и начинаете судорожно пересчитывать упаковки в пакете')
number_of_people = input("Вспомните количество гостей:")
number_of_soups = input("Какое количество супов вы закупили:")

if "тут пишем наше условие возвращения домой":
	# тут считаем сколько всем достанется и останется
	print("Всем достанется", "сколько??", "А ещё останется", "сколько??")
else:
	# тут выводим сколько есть и сколько ещё не хватает
	print("В пакете сейчас", "сколько??", "А ещё нужно", "сколько??")


"""
2. Вы всё ещё начинающий тренер покемонов.
Вы решили что будете ловить только тех покемонов, 
имя которых начинается с букв "А", "К", "Р" и "Х").

Задание: 
В переменную pokemon_name пользователь вводит название покемона.
Если оно соответствует условиям, то мы его ловим.
Если нет, то отпускаем.

Примечание:
используйте or для составления условия
"""

# Код:
print("Вы пробираетесь по болотам и слышите как справа от Вас что-то булькнуло...")
print("Вы бросате покебол в кусты в надежде поймать булькающего там покемона...")
print("Похоже это удача! Вы кого-то поймали! Но нужен ли он Вам?")
pokemon_name = input("Что это за покемон??")
if "ваше условие":
	print("Вы поймали", pokemon_name, "Какой-то он влажный..")
else:
	print("Покемон", pokemon_name, "Вам не нужен, пусть булькает дальше")
