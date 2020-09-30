# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


while True:
    try:
        a = int(input('Enter the number of your month: '))
        break
    except:
        print("Incorrect input. Please add number between 1 and 12.")


def list_identifier(x):
    seas = ['winter', 'spring', 'summer', 'autumn']
    if x in range(1,3) or x == 12:
        print(f'Your season is {seas[0].capitalize()}')
    elif x in range(3,6):
        print(f'Your season is {seas[1].capitalize()}')
    elif x in range(6, 9):
        print(f'Your season is {seas[2].capitalize()}')
    elif x in range(9,12):
        print(f'Your season is {seas[3].capitalize()}')
    else:
        pass


def dict_identifier(x):
    seas = {1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 6:'summer', 7:'summer',
              8:'summer', 9:'autumn', 10:'autumn', 11:'autumn', 12:'winter'}
    print(F"Your season is {seas.get(x).capitalize()}")


list_identifier(a)
dict_identifier(a)
