# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = input('Enter a positive number: ')

m = 0
i = 0
while i <= len(str(n))-1:
    if int(n[i]) > m:
        m = int(n[i])
    i += 1


print(f"Your maximum digit in the number is: {m}")
