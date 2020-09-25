# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 2. Считаем 2 + 22 + 222 = 246.

n = input('Enter your number: ')
print(f"Your 'n+nn+nnn' result equals to:  {int(n)+int(n+n)+int(n+n+n)}")