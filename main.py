# age = int(input("введите возраст:"))
#
# ask_name = False
#
# if age > 50:
#     print("вам больше 50!")
#     ask_name = True
# elif age >= 18:
#     print("Вам сюда можно :)")
#     ask_name = True
# else:
#     print("уходите111! :С")
#     print("уходите111! :С")
#
# ask_weather = False
#
# if ask_name:
#     name = input("введите имя:")
#     if name == "Pavel":
#         print("hello,", name)
#         ask_weather = True
#     elif name == "Alex":
#         print("hi!", name)
#         ask_weather = True
#     elif name == "Bob":
#         print("nice to see you,", name)
#         ask_weather = True
#     else:
#         print("уходите111! :С")
#
# if ask_weather:
#     weather = input("какая на улице погода?")
#
#     if weather == "дождь":
#         print("мы остаёмся дома и никуда не идём")
#     elif weather == "снег":
#         print("идём лепить снеговика")
#     elif weather == "пасмурно":
#         print("берём зонт и идём гулять")
#     else:
#         print("я не знаю что вам предложить")
#
#
# print("Пока!")


# name = ""
# try_number = 0
# while name != "Bob" or try_number <= 3:
#     name = input("введите имя:")
#     if name != "Bob":
#         print("Вы не БОБ уже ", try_number, "раз! :(")
#     try_number = try_number + 1
#
# print("привет БОБ!")

print("Hello, %s. You have %i friends" % ("Bob", 5))
