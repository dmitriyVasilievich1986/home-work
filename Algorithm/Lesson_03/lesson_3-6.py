# region Текст задания

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# endregion

# region Формирование массива

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# endregion

# импортируем функцию из библиотеки
from functools import reduce

# инициализация переменных
number_min = 0
number_max = 0

# цикл прохода массива и сравнения с болишм, меньшим числом
for item in range(len(array)):
    if array[item] > array[number_max]:         # сравниваем числа в массиве,
        number_max = item                       # а сохраняем именно индекс, не само число
    elif array[item] < array[number_min]:
        number_min = item

# вывод начального массива
print(f'Массив для поиска:\n{array}')
# проверяем на вхождение в границы массива
if abs(number_max - number_min) < 2:
    print('Нет множества')
else:
    # вывод результата
    new_array = array[number_min + 1:number_max] if number_max > number_min else array[number_max + 1:number_min]
    print(f'Массив от {array[number_min]} до {array[number_max]}, исключая границы:\n{new_array}')
    print(f'Сумма всех значений полученного массива: {reduce(lambda x, y: x + y, new_array)}')
