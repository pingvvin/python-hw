# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

with open('lesson52.txt','r') as file_obj:
    i = 1
    for line in file_obj:
        print(f'{len(line.split())} words in row {i}')
        i += 1