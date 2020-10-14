'''
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

with open('work1.txt', 'w', encoding='UTF-8') as file_obj:
    a = True
    while a:
        a = input('Enter data to write to file:\n')
        file_obj.write(f'{a} \n')

#TODO добавить вывод содержимового