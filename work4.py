my_string = input("Enter your string: ")
my_word = []
numbering = 1
dot = "."

for el in range(my_string.count(' ') + 1):
    # не доконца понимаю, что возвращает и тд,но это работает
    # видимо он определяет количество объектов пробелами,и так как объектов всегда на 1 больше чем пробелов
    #то +1
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {numbering}{dot} {my_word [el]}")
        numbering += 1
    else:
        print(f" {numbering}{dot} {my_word [el] [0:10]}")
        numbering += 1