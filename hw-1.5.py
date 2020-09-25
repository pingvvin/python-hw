# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

rev = int(input("Enter your revenue amount: "))
cost = int(input("Enter your costs amount: "))

if (rev-cost)>0:
    print(f"\nYour company is profitable. Your net profit equals to: {rev - cost}")
    print(f"Also your profitability rate equals to: {round((rev - cost)/rev*100,2)}%")
    emp = int(input("\n Enter the number of employess in your company: "))
    print(f"The amount of profit per employee: {round((rev-cost)/emp,2)}")
elif(rev-cost) == 0:
    print("You do not have profits or losses")
else:
    print(f"Your company have losses. They are equal to: {rev-cost}")