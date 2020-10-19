# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу
# декоратора @property.

from abc import ABC, abstractmethod

class Coat(ABC):
    @abstractmethod
    def __init__(self, size):
        self.size = size
    @abstractmethod
    def calc_exp(self):
        self._result = (self.size / 6.5) + 0.5
        return f'{round(self._result,3)} square meters of tissue needed for a unit'

    def __mul__(self, other):
        self.other = other
        return f'{round(self._result * other,3)} square meters of tissue needed for {other} units'


class Costum(Coat):
    def __init__(self, height):
        self.height = height

    def calc_exp(self):
        self._result = (self.height * 2) + 0.3
        return f'{round(self._result, 3)} square meters of tissue needed for a unit'

c = Costum(4)
c.calc_exp()
print(c.calc_exp())

