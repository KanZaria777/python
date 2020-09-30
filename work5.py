my_list = [1, 3, 5, 4, 9, 2, 56]
print(f"Rating - {my_list}")
#print("To exit enter <Leave>.")
user_data = float(input("To exit dial - 666999.\nInsert the number: "))

while user_data != 666999:
    #if float.is_integer(user_data): Попытка реализовать ввод цифр с плавающей точкой
        #int(user_data) к сожалению пока не удачно
    for el in range(len(my_list)):
        if my_list[el] == user_data:
            my_list.insert(el + 1, user_data)
            break
        elif my_list[0] < user_data:
            my_list.insert(0, user_data)
        elif my_list[-1] > user_data:
            my_list.append(user_data)
        elif my_list[el] > user_data and my_list[el +1] < user_data:
            my_list.insert(el + 1, user_data)
    print(f"Current list - {my_list}")
    user_data = int(input("Insert the number: "))