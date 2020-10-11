# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open("lesson51.txt",'w')

with open("lesson51.txt",'w') as f_obj:
    while True:
        i = input("Enter your line of text: ")
        if i == "":
            print("Program closed")
            break
        else:
            f_obj.write(i+'\n')
