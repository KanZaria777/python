'''
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('work3.txt', 'r', encoding="UTF-8") as file_obj:
    number_stuff = 0
    sum_salary = 0
    for line in file_obj:
        surname, salary = line.strip().split()
        #превращает каждую строку в список,из которой мы достанем зп и фамилию
        salary = int(salary)
        number_stuff += 1
        sum_salary += salary
        if salary < 20000:
            print(f'{surname} salary is less than 20000')
    print(f'Average salary is {round(sum_salary / number_stuff, 2)}')


