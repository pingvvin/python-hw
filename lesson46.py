# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

# Iterator for generating integers starting from mentioned until mentioned

def int_func(start,stop):
    for el in count(start):
        if el>stop:
            break
        else:
            print(el)

# Iterator for list defined earlier

def cyc_iter(inp,ex):
    с = 0
    for el in cycle(inp):
        if с > ex:
            break
        print(el)
        с += 1

int_func(10,12)
cyc_iter(['john', 'snow'], 10)
