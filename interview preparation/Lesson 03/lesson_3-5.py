# region Текст задания

"""
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений заменить
на значения типа example345 (строка+число).
Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.
Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""

# endregion

import os
from random import randint

LIST_SIZE = 5

a = [''.join([chr(randint(ord('a'), ord('z'))) for x in range(5)]) + ''.join([str(randint(0, 10)) for x in range(3)]) for x in range(LIST_SIZE)]
b = [randint(0, 100) for x in range(LIST_SIZE)]
zip_list = zip(b,a)

print(a)

def open_fileasd(file_path):
    with open(file_path, 'r') as my_file:
        for line in my_file.readlines():
            print(line, end='')

def save_zip_in_file(zip_list):
    file_path = fr'{os.getcwd()}/zip.txt'
    with open(file_path, 'w') as my_file:
        for item in zip_list:
            my_file.writelines(f'{item[0]}  {item[1]}\n')
    open_fileasd(file_path)

# save_zip_in_file(zip_list)