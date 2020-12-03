# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных
# пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

a = '2 3 @ 4 as'
toggle = True
sum = 0
while toggle:
    a = input('Enter your numbers list separating with spaces (add @ to stop adding numbers): ')
    for i in a.split(' '):
        try:
            if i != '@':
                sum += int(i)
            else:
                toggle = False
                break
        except ValueError:
            print(f'"{i}" is not a number but program will keep adding other numbers')
            pass

    print(f'Our result is: {sum}')