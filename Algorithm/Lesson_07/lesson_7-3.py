# region Текст задания

"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""

# endregion

# импортируем библиотеку
from random import randint
from collections import deque

# инициализация констант и переменных
ARRAY_LENGTH = 10
array = [randint(0, 50) for x in range(ARRAY_LENGTH * 2 + 1)]


# инициалиация функции сортировки
def search_median(array):
    """функция поиска медианы списка

            Args:
                array (list): несортированый список

            Returns:
                int: значение медианы
            """
    int_min = deque([0])
    int_max = deque([0])
    while True:
        for a in range(len(array)):
            if array[int_min[-1]] >= array[a] and not a in int_min:
                int_min[-1] = a
            if array[int_max[-1]] <= array[a] and not a in int_max:
                int_max[-1] = a
        if len(int_min) > (len(array) // 2):
            return array[int_min[-1]]
        int_max.append(int_min[0])
        int_min.append(int_max[0])


# другое решение задачи
def list_pop(array):
    while len(array) > 1:
        item_min = array[0]
        item_max = array[0]
        for item in array:
            if item < item_min:
                item_min = item
            if item > item_max:
                item_max = item
        array.remove(item_min)
        array.remove(item_max)
    return array[0]


# вывод результата
print(f'Список до сортировки:\n{array}')
print(f'\nЗначение медианы списка: {search_median(array)}')
array.sort()
print(f'\nОтсортированый список для сравнения:\n{array}')
print(f'Медиана: {array[len(array) // 2]}')
