# region Текст задания

"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан
и записан в файл таким образом, чтобы каждая строка файла содержала текстовое
и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""

# endregion

# импортируем библиотеки
import os
from random import randint

# инициализируем константу
LIST_SIZE = 5

# инициализируем списки
a = [''.join(chr(randint(ord('a'), ord('z'))) for x in range(5)) for x in range(LIST_SIZE)]
b = [randint(0, 100) for x in range(LIST_SIZE)]
zip_list = zip(b, a)


# инициализируем функцию построчного чтения файла
def open_fileasd(file_path):
    with open(file_path, 'r') as my_file:
        for line in my_file.readlines():
            print(line, end='')


# инициализируем функцию построчной записи файла
def save_zip_in_file(zip_list):
    file_path = fr'{os.getcwd()}/zip.txt'
    with open(file_path, 'w') as my_file:
        for item in zip_list:
            my_file.writelines(f'{item[0]}  {item[1]}\n')
    open_fileasd(file_path)


# вызов функции
save_zip_in_file(zip_list)
