# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class Zeroex:
    @staticmethod
    def check(divident,divisor):
        try:
            print(int(divident)/int(divisor))
        except ZeroDivisionError:
             print('Please change your divisor. You can not divide by 0')
        except ValueError:
            print('Please use numbers in divident and divisor')


Zeroex.check(30, 1)
Zeroex.check(10, 0)
