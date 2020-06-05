# region Текст задания

"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

# endregion

# импортируем библиотеку
from random import random
from collections import deque

# инициализация констант и переменных
ARRAY_LENGTH = 10
array = [round(random() * 50, 2) for x in range(ARRAY_LENGTH)]

# инициалиация функции сортировки
def merge_sort(array):
    """рекурсивная функция сортировки методом слияния

    Args:
        array (list): несортированый список
    """
    def _merge(left, right):
        """внутренняя функция слияния списков

        Args:
            left (deque): левая часть для слияния
            right (deque): правая часть для слияния

        Returns:
            deque: список после слияния
        """
        while len(left) and len(right):
            if left[0] < right[0]:
                output.append(left.popleft())
            else:
                output.append(right.popleft())
        while len(left):
            output.append(left.popleft())
        while len(right):
            output.append(right.popleft())
        return output

    output = deque()
    if len(array) <= 1:
        return array
    # это главный минус сортировки слиянием - использование памяти
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:len(array)])
    # рекурсивный вызов функции
    output = _merge(deque(left), deque(right))
    return list(output)


print(f'Список до сортировки:\n{array}')
print(f'\nСписок после сортировки:\n{merge_sort(array)}')
