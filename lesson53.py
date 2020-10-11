# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('lesson53.txt','r') as file_obj:
    tot = 0
    peop = 0
    for line in file_obj:
        sal = line.split()
        if int(sal[1]) >= 20000:
            print(f'{sal[0]} has salary at least 20000')
        tot +=int(sal[1])
        peop += 1
    print(f'Average salary is: {tot/peop}')