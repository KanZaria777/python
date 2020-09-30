user_data = int(input("Введите желаемое количество элементов списка: "))
my_list = []

i = 0
el =0
i_el = 1 #человеческий счетчик

while i < user_data:
    my_list.append(input(f'Введите {i_el} значение списка: '))
    i += 1
    i_el += 1

for element in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1] + my_list[el]
    el += 2
print(my_list)