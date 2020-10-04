numberOne = float(input('Enter the first number: '))
numberTwo = int(input('Please enter a negative integer: '))

while numberTwo >= 0:
    print('You just had to enter a negative number...')
    numberTwo = int(input('Please enter a negative integer: '))

def exponentiation(x, y):
    result = x ** y
    print(result)
'''
def exponentiation1(x, y):
    i = 0
    while i <= y:
        x += x * i   
'''


exponentiation(numberOne, numberTwo)
