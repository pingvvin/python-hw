# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def inf(name,surname,dob,city,email,phone):
    return f'Name: {name.capitalize()}; Surname: {surname.capitalize()}; ' \
           f'Date of birth: {dob}; City: {city}; Email: {email}; Phone: {phone}'

print(inf(name='stanislav', surname='yablunovskyi', dob='07/02/1994', city='Krakow', email='yablunovskyi@gmail.com', phone='5506415'))