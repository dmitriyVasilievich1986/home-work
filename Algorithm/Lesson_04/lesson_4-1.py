# region Текст задания

# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# endregion

# импорт библиотек
import timeit
import cProfile


# region инициализация функций


# инициализация функции с 1 циклом
def devil_number_cycle(count):
    result = 0
    number = 1
    # инициализация цикла
    while count != 0:
        count -= 1
        result += number  # сначала прибавляем число,
        number /= -2  # затем делим
    return result


# инициализация функции с вложенным циклом
def devil_number_double_cycle(count):
    result = 0
    # инициализация цикла
    for cycle in range(count):
        number = 1
        # инициализация внутреннего цикла
        # чудовищное решение задачи, конечно))
        for inner_cycle in range(cycle):
            number /= -2
        result += number
    return result


# инициализация рекурсивной функции
def devil_number_recursion(count, result=0, number=1):
    # вначале дефолтный случай
    if count == 0:
        return result
    # затем рекурсивный вызов функцией себя
    result += number
    number /= -2
    return devil_number_recursion(count - 1, result, number)


def main(number):
    devil_number_cycle(number)
    devil_number_recursion(number)
    devil_number_double_cycle(number)


# endregion


# сначала проверяем, что функции вообще работают
print(devil_number_cycle(100))
print(devil_number_recursion(100))
print(devil_number_double_cycle(100))

# region timeit


print('*' * 25)
print(timeit.timeit('devil_number_cycle(50)', number=10000, globals=globals()))  # 0.0527711
print(timeit.timeit('devil_number_recursion(50)', number=10000, globals=globals()))  # 0.0963047
print(timeit.timeit('devil_number_double_cycle(50)', number=10000, globals=globals()))  # 0.6452088
print('*' * 25)
print(timeit.timeit('devil_number_cycle(100)', number=10000, globals=globals()))  # 0.10103309999999999
print(timeit.timeit('devil_number_recursion(100)', number=10000, globals=globals()))  # 0.1987589999999999
print(timeit.timeit('devil_number_double_cycle(100)', number=10000, globals=globals()))  # 2.2830412
print('*' * 25)
print(timeit.timeit('devil_number_cycle(200)', number=10000, globals=globals()))  # 0.20085489999999995
print(timeit.timeit('devil_number_recursion(200)', number=10000, globals=globals()))  # 0.3962030999999997
print(timeit.timeit('devil_number_double_cycle(200)', number=10000, globals=globals()))  # 8.667773
print('*' * 25)
print(timeit.timeit('devil_number_cycle(750)', number=10000, globals=globals()))  # 0.8272431000000005
print(timeit.timeit('devil_number_recursion(750)', number=10000, globals=globals()))  # 1.697936799999999
# и тут я ушел пить чай))
print(timeit.timeit('devil_number_double_cycle(750)', number=10000, globals=globals()))  # 134.20739540000002

# endregion

# region cProfile

print('*' * 25)
cProfile.run('main(50)')
# 1    0.000    0.000    0.000    0.000 lesson_4-1.py:12(devil_number_cycle)
# 1    0.000    0.000    0.000    0.000 lesson_4-1.py:23(devil_number_double_cycle)
# 51/1    0.000    0.000    0.000    0.000 lesson_4-1.py:35(devil_number_recursion)
print('*' * 25)
cProfile.run('main(100)')
# 1    0.000    0.000    0.000    0.000 lesson_4-1.py:12(devil_number_cycle)
# 1    0.000    0.000    0.000    0.000 lesson_4-1.py:23(devil_number_double_cycle)
# 101/1    0.000    0.000    0.000    0.000 lesson_4-1.py:35(devil_number_recursion)
print('*' * 25)
cProfile.run('main(200)')
# 1    0.000    0.000    0.000    0.000 lesson_4-1.py:12(devil_number_cycle)
# 1    0.001    0.001    0.001    0.001 lesson_4-1.py:23(devil_number_double_cycle)
# 201/1    0.000    0.000    0.000    0.000 lesson_4-1.py:35(devil_number_recursion)
print('*' * 25)
cProfile.run('main(750)')
# 1    0.000    0.000    0.000    0.000 lesson_4-1.py:12(devil_number_cycle)
# 1    0.014    0.014    0.014    0.014 lesson_4-1.py:23(devil_number_double_cycle)
# 751/1    0.000    0.000    0.000    0.000 lesson_4-1.py:35(devil_number_recursion)

# endregion

# region Вывод

"""
Для задания было выбрано задание:
    'Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… '
Были сделаны 3 варианта решения задачи:
    1. через еденичный цикл while
    2. через цикл, который содержит вложенный цикл
    3. через рекурсивную функцию
Результат:
     наилучший результат ожидаемо показала функция с 1 циклом.
 ровно в 2 раза медленне работала рекурсивная функция,
 не смог проверить функцию с циклом > 1000 без изменеия
 системног ограничителя, ограничился 750 циклами. очевидно, что
 рекурсивная функция должна быть самой прожорливой в плане оперативной памяти.
 но самый худший вариант показало решение с вложенным циклом, это связано
 с реализацией самого цикла, который увеличивался с ростом основного цикла.
"""

# endregion
