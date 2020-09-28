variableOne = 12
variableTwo = "Записываю сюда буковки"

print(variableOne)
print(variableTwo)

user_data1 = input("Введите что-нибудь:")
user_data2 = input("Введите какое-то число:")

print(f"{user_data1} <= Это ваш первый ввод.")

if user_data2.isdigit():
    print(f"{user_data2} <= А это ваше число!")
else:
    print("Вроде бы я просил ввести число!")
    print(f"А теперь я даже не знаю, что это... {user_data2}")
# Думал изучить сомастоятельно функции для python чтобы не дубливать код
#но решил не грузиться излишне, думаю по одному примеру достаточно с: