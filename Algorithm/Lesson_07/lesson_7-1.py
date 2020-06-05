# region Текст задания

"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
"""

# endregion

# импортируем библиотеку
from random import randint

# инициализация констант и переменных
ARRAY_LENGTH = 10
array = [randint(-100, 100) for x in range(ARRAY_LENGTH)]


# инициалиация функции сортировки
def buble_sort(array):
    """Фуникция для пузырьковой сортировки списка.

    Args:
        array (list): несортированый список

    Returns:
        list: отсортированный список
    """
    for cycle in range(len(array)):
        for item in range(len(array) - cycle - 1):
            if array[item] > array[item + 1]:
                array[item], array[item + 1] = array[item + 1], array[item]
    return array


# вывод данных
print(f'Список до сортировки:\n{array}')
print(f'\nСписок после сортировки:\n{buble_sort(array)}')
