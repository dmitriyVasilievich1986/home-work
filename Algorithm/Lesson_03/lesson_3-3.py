# region Текст задания

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# endregion

# region Формирование массива

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# endregion

# инициализация переменных
number_min = 0
number_max = 0

# цикл прохода массива и сравнения с болишм, меньшим числом
for item in range(len(array)):
    if array[item] > array[number_max]:         # сравниваем числа в массиве,
        number_max = item                       # а сохраняем именно индекс, не само число
    elif array[item] < array[number_min]:
        number_min = item

# вывод результата
print(f'Массив до изменеия\n{array}')
array[number_min], array[number_max] = array[number_max], array[number_min]
print(f'Массив после перестановки\n{array}')

