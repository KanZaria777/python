'''
name = input("Enter your name: ")
surname = input("Enter your surname: ")
year_of_birth = input("Enter your year of birth: ")
city = input("Enter the city where you live: ")
e_mail = input("Your email inbox: ")
phone = input("Your mobile phone number: )
Изначально был невнимателен и почти написал функцию на создание словаря через ввод:D
40 минут ломал над этим голову
'''
def func_user_data (name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])
print(func_user_data(name = 'KanZaria', phone = '+999999999',
                     city = 'Saint-Peterburg', email = 'kanzaria777@gmail.com',
                     surname = 'Its a secret^^', year = '199*'))