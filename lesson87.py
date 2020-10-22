# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    #Complex numbers should be in format '2x+1' where first part should contain variable
    def __init__(self, n):
        self.n = n

    def __add__(self, m):
        piece = self.n.split('+')
        piece2 = m.split('+')
        print(f'{int(piece[0][:len(piece[0])-1]) + int(piece2[0][:len(piece2[0])-1])}'
              f'{piece2[0][len(piece2[0])-1:]}+{int(piece[1])+int(piece2[1])}')

    def __sub__(self, m):
        piece = self.n.split('+')
        piece2 = m.split('+')
        print(f'{int(piece[0][:len(piece[0])-1]) - int(piece2[0][:len(piece2[0])-1])}'
              f'{piece2[0][len(piece2[0])-1:]}+{int(piece[1])-int(piece2[1])}')


    def __mul__(self, m):
        piece = self.n.split('+')
        piece2 = m.split('+')
        print(f'{int(piece[1])*int(piece2[1]) - int(piece[0][:len(piece[0])-1]) * int(piece2[0][:len(piece2[0])-1])}'
              f'{piece2[0][len(piece2[0])-1:]}+{int(piece[1])*int(piece2[0][:len(piece2[0])-1]) + int(piece2[1]) * int(piece[0][:len(piece[0])-1])}')


# Не осилил замену плюсиков поэтоми при отрицательных числах будет появляться строка формата 2х+-3 что теоретически можно понять

test = Complex('1x+2')

test.__add__('31x+41')
test.__sub__('31x+41')
test.__mul__('3x+4')