user_data = int(input("Введите количество секунд которые моя программа "
                'конвертирует по принципу "чч:мм:сс":'))

hours = user_data // 3600
minutes = (user_data - hours * 3600) // 60
seconds =  user_data - (hours * 3600 + minutes * 60)

print(f"Время {hours}:{minutes}:{seconds}")