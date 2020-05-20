# region Текст задания

# Определить, какое число в массиве встречается чаще всего.

# endregion

# region Формирование массива

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# endregion


# инициализация функции вывода результата
def print_result(result):
    max_count = list(result.keys())[0]
    for item in result.keys():
        if result[item] > result[max_count]:
            max_count = item
    print(f'Число {max_count} встречалось {result[max_count]} раз')


# функция через сортировку списка
def array_sort(array):
    result = {}
    for item in set(array):
        result[item] = 1
    array.sort()
    for item in range(len(array) - 1):
        if array[item] == array[item + 1]:
            result[array[item]] += 1
    return result


# функция через встроенный метод count
def array_count(array):
    result = {}
    for item in set(array):
        result[item] = array.count(item)
    return result


# Функция через цикл
def array_cycle(array):
    result = {}
    for item in set(array):
        result[item] = 0
    for item in range(len(array)):
        result[array[item]] += 1
    return result


# сначала проверяем что вообще есть повторяющиеся числа
if len(array) == len(set(array)):
    print('Все числа встречаются один раз')
else:
    # выводим все функции
    print(f'Массив для поиска\n{array}\n')
    print_result(array_count(array))
    print_result(array_cycle(array))
    print_result(array_sort(array))
