# region Текст задания

"""
Написать программу, которая будет содержать функцию
для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться
имя файла с расширением. В функции необходимо реализовать
поиск полного пути по имени файла, а затем «выделение»
из этого пути имени файла (без расширения).
"""

# endregion

import re

def find_filename_by_path(path):
    return re.split(r'[/,.]', path)[-2]

print(find_filename_by_path(r"c:/Users/Professional/Documents/Projects/Python/home-work/interview preparation/Lesson 03/lesson_3-1.py"))