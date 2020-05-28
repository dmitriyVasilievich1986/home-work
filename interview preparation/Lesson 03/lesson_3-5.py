# region Текст задания

"""
Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""

# endregion

# импортируем библиотеки
import re
import os
from random import randint

# инициализируем константу
LIST_SIZE = 5

# инициализируем списки
a = [''.join([chr(randint(ord('a'), ord('z'))) for x in range(5)]) + ''.join([str(randint(0, 9)) for x in range(3)]) for
     x in range(LIST_SIZE)]
b = [randint(0, 100) for x in range(LIST_SIZE)]
zip_list = zip(b, a)


# инициализируем функцию построчного чтения файла
def open_fileasd(file_path):
    path = fr'{os.getcwd()}/zip2.txt'
    try:
        os.remove(path)
    except:
        pass
    with open(file_path, 'r') as my_file:
        for line in my_file.readlines():
            with open(path, 'a') as save_file:
                save_file.writelines(
                    re.sub(r'\b\d+', ''.join(chr(randint(ord('a'), ord('z'))) for x in range(5)), line))


# инициализируем функцию построчной записи файла
def save_zip_in_file(zip_list):
    file_path = fr'{os.getcwd()}/zip.txt'
    with open(file_path, 'w') as my_file:
        for item in zip_list:
            my_file.writelines(f'{item[0]}  {item[1]}\n')
    open_fileasd(file_path)


# вызов функции
save_zip_in_file(zip_list)
