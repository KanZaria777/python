print("Введите число и я выведу вам"
      " его по следующему примеру: n+nn+nnn=sum")
number = input()

sum = (number + int(str(number) + str(number)) + int(str(number) + str(number)+ str(number)))

print(f"Сумма чисел n + nn + nnn = {sum}")
#powershell ругается мол,строки можно сложить только со строками,не с цифрами.
#но ведь я все перевожу потом в int.
