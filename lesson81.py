# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    updated = []

    @classmethod
    def to_num(cls, date_input):
        for i in date_input.split("-"):
            cls.updated.append(int(i))
        print(cls.updated)

    @staticmethod
    def timstmp_check(date_input):
        try:
            if (int(date_input.split("-")[0]) >= 30) and (int(date_input.split("-")[1]) == 2):
                print(f'February has only 29 days')
            elif (0 < int(date_input.split("-")[1]) < 12) and \
                    (0 < int(date_input.split("-")[0]) <= 31) and (1900 < int(date_input.split("-")[2]) < 2100):
                pass
            else:
                print(f'"{date_input}" - Incorrect timestamp value. Input should be in format dd-mm-yyyy')
        except ValueError:
            print(f'"{date_input}" - Value error. Please check you input')


#Data.timstmp_check('07-02-1994')
Data.to_num('07-02-1994')
Data.timstmp_check('30-02-1994')
Data.timstmp_check('07-02-199s')