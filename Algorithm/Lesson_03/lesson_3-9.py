# region Текст задания

# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# endregion

# region Формирование матрицы

import random

ROW = 10
COLUMN = 10
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(COLUMN)] for x in range(ROW)]

# endregion

# инициализируем переменную
number_max = 0

# инициализация словаря для нахождения минимальных значений в каждом столбце
min_in_column = {}
for item in range(len(matrix)):
    min_in_column[item] = matrix[item][0]

# цикл вывода матрицы и поиска минимальных значений в столбцах
print('\nРезультирующая матрица:')
# не уверен что лучше этот вариант или
# for y in range(len(matrix))
# и потом поиск по индексу?
# или они равнозначны и указывают на один участок памяти?
for y in matrix:
    for a, x in enumerate(y):
        print(f'{x:<6}', end='')
        if x < min_in_column[a]:
            min_in_column[a] = x
    print()

# цикл поиска наибольшего значения среди минимальных значений
for item in min_in_column.values():
    if item > number_max:
        number_max = item
# вывод результата
print(f'Максимальное число среди минимальных в каждом столбце матрицы: {number_max}')