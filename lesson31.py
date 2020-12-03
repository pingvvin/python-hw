# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def dvd():
    try:
        a = float(input("Enter your divident: "))
        b = float(input("Enter your divisor: "))
        res = a / b
        return res
    except ZeroDivisionError:
        return 'You can not divide by zero. Try again'
    except ValueError:
        return 'Your input should be a number.'

print(dvd())
