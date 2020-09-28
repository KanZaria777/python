number = abs(int(input("Введите целое положительное число:")))

max = number % 10

while number >= 1:
    number = number // 10
    if number % 10 >  max:
        max = n % 10
    if number > 9:
        continue
    else:
        print(f"Максимальное число: {max}")
        break