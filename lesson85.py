# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from lesson84 import *

stock = []

stock_item = {}

#method moves printers scanners to stock dictionary
#added check for count when moving items to stock
def move_items(x,count):
    partition = x.information().split(': ')
    stock_item[partition[0]] = partition[1]
    partition = x.information2().split(': ')
    stock_item[partition[0]] = partition[1]
    if str(count).isnumeric() == True:
        stock_item['Count'] = int(count)
    else:
        print('Wrong count input')
    stock.append(stock_item)

t = Printer('Xerox a25','a123-1')
move_items(t,3)

x = Scanner('Cannon g25','666',1000,1400)
move_items(x,'2s')

print(stock)






#{printer:{'model': ' ',
#          'serial number': ' '
#          }
#}