from random import randrange

print(sorted(list({el for el in range(20, 241) if el % 21 == 0 or el % 20 == 0})))

'''
Ниже представлен вариант сортировки для удобства и дальнейшего использования гдето
my_set = {el for el in range(20, 241) if el % 21 == 0 or el % 20 == 0}
my_list = list(my_set)
Это в две
my_list.sort()
print(my_list)
Это в одну строку
print(sorted(my_list))
'''
