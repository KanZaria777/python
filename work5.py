def addition_of_string_numbers():
    sum = 0
    condition = False
    while condition == False:
        stringNumber = input('Press K or k to exit.\nEnter your numbers separated by space: ')
        # TODO дописать проверку строки на наличие только цифр
        stringNumber = stringNumber.replace(' ', '')
        # пришлось нагуглить этот метод, так сразу и не скажешь, что так можно было
        tui = 0
        for i in range(len(stringNumber)):
            if stringNumber[i] == 'K' or stringNumber[i] == 'k':
                condition = True
                break
            else:
                tui = tui + int(stringNumber[i])
                #TODO попробовать добавить float+  проверку для красивого результата
    # tui переменная испльзуемая для вывода числа из цикла в функцию, так сказать временный вариант
        sum = sum + tui
        print(f'Current sum is {sum}.')
    print(f'Your final sum is {sum}.')

addition_of_string_numbers()


