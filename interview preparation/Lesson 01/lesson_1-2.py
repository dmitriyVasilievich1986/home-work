# region Текст задания

"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее

Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""

from os import listdir


# endregion

# инициализация функции вывода файлов
def print_directory_contents(sPath):
    """
    Рекурсивная функция принимает в качестве аргумента имя папки sPath.
        Выводит содержимое папки и вложенных подпапок.
    Принимает: строковая переменная sPath
    """
    # инициализация цикла прохода по содержимому папки
    for item in listdir(sPath):
        try:
            print_directory_contents(f'{sPath}\\{item}')
        except NotADirectoryError:
            print(f'Путь - {sPath}\t\tФайл - {item}')


# вызов функции
print_directory_contents(r'C:\Users\d.shcherbachenya\Documents\Python\home-work\Algorithm')
