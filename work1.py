number1 = float(input("Insert the number: "))
number2 = float(input("Insert the number: "))

def division(num1, num2):
    '''
        Эта функция выдает результат деления двух чисел.
    '''
    try:
        result = num1 / num2
        if num1 % num2 != 0:
            print(f"Division result: {result:.2f}")
        else:
            result = int(result)
            print(f"Division result: {result}")
    except ZeroDivisionError:
        print("I am very sorry, it will not be possible to divide by zero.")

division(number1, number2)

