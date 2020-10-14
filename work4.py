'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл
на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

ratio = {'One' : 'Один',
         'Two' : 'Два',
         'Three' : 'Три',
         'Four' : 'Четыре'}

with open('work4.txt', 'r', encoding='UTF-8') as or_words, \
    open('work4-1.txt', 'w', encoding='UTF-8') as tr_words:
    for line in or_words:
        word, sep, num = line.strip().split()
        if word in ratio:
            word = ratio[word]
        tr_words.write(f'{word} - {num}\n')