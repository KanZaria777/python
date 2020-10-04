'''
numberOne = float(input("Enter the first number: "))
numberTwo = float(input("Enter the second number: "))
numberThree = float(input("Enter the third number: "))
'''

def sum (num1, num2, num3):
    '''
        Сумма двух больших значений
        И последующее приведение результата в порядок
    '''
    #Верно ли я произвел комментирование функции или не по делу? То что она работает в Help() понятно.
    if num1 >= num3 and num2 >= num3:
        result = num1 + num2
    elif  num1 > num2 and num1 < num3:
        result = num1 + num3
    else:
        result =  num2 + num3

    if result % 1 != 0:
        print(f'{result:.2f}')
    else:
        print(int(result))

sum(float(input("Enter the first number: ")), float(input("Enter the second number: ")), float(input("Enter the third number: ")))
