# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор списка.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

ll = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new = [ll[i] for i in range(1,len(ll)) if ll[i] > ll[i-1]]

print(new)