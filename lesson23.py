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
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']
    print(F"Your month name is {months[x-1].capitalize()}")

def dict_identifier(x):
    months = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july',
              8:'august', 9:'september', 10:'october', 11:'november', 12:'december'}
    print(F"Your month name is {months.get(x).capitalize()}")


list_identifier(a)
dict_identifier(a)
