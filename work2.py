'''
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
'''

with open('work2.txt', 'r', encoding='UTF-8') as file_obj:
    count_lines = 0
    count_words = 0

    for line in file_obj:
        count_lines += 1
        line_words = len(line.strip().split()) # разобраться, что это значит
        print(f'В {count_lines} строке - {line_words} слов.')
        count_words += line_words

    print(f'Всего строк в документе {count_lines}.')
    print(f'Всего в документе {count_words} слов.')