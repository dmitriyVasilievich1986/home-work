# region Текст задания

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

# endregion

# region Формирование массива

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# endregion

# выводим список
print(f'Массив для поиска:\n{array}')
# инициализация переменной
index_max = 0
# инициализация поиска максимального из отрицателдьных чисел
for item in [x for x in array if x < 0]:
    if abs(item) > abs(index_max):
        index_max = item
# вывод результата
print(f'\nСамое большое из отрицательных чисел в массиве: {index_max}, его положение в массиве: {array.index(index_max)}')
