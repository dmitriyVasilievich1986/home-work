# region Текст задания

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# endregion

# region Формирование массива

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# endregion

# инициализация переменных
number_min_first = array[0]
number_min_second = array[0]

# инициализация цикла поиска минимального числа
for item in array:
    if item < number_min_first:
        number_min_second, number_min_first = number_min_first, item

# выводим список
print(f'Массив для поиска:\n{array}')
# выводим результат
print(f'Наименьшее число в массиве: {number_min_first}')
print(f'Второе наименьшее число в массиве: {number_min_second}')
