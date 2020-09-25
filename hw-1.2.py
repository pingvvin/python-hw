# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

x = int(input('Enter your seconds amount to be converted: '))


def hms(a):
    hour = a // 3600
    mins = (a - (int(hour) * 3600))//60
    secs = a - ((int(hour) * 3600) + (int(mins)*60))
    if len(str(hour)) == 1:
        hour = f'0{hour}'
    if len(str(mins)) == 1:
        mins = f'0{mins}'
    if len(str(secs)) == 1:
        secs = f'0{secs}'
    return f"\nYour result has been converted to format 'hh:mm:ss' : \n\n{hour}:{mins}:{secs}"

print(hms(x))