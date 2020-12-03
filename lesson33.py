# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    try:
        if a > c and b > c:
            return float(a + b)
        elif a > b and c > b:
            return float(a + c)
        else:
            return float(b + c)
    except ValueError:
        return 'Your input should be a number'

print(my_func(2, 3, 1))

"""Testing jobs"""
"""print(my_func(1, 2, 3))
print(my_func(1, 3, 2))
print(my_func(3, 2, 1))
print(my_func(2, 1, 3))
print(my_func(3, 1, 2))
print(my_func('a', 'b', 'c'))"""
