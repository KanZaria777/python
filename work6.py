primary_indicator = int(input("Сколько километров пробежал спортсмен в 1ый день:"))
target = int(input("Сколько километров в день,он хочет пробегать:"))

days = 1
distance = target

while primary_indicator < target:
    primary_indicator = primary_indicator +  primary_indicator * 0.1
    days += 1
    distance = distance + primary_indicator

print(f"На {days} день результат будет достигнут.Точный результат: {round(primary_indicator, 3)} километра.")
#Так как результат точный, я решил, что будет разумно использовать 3 цифры после запятой.
