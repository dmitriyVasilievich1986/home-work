# region Текст задания

# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

# endregion

# имопрт библиотек
import timeit
import cProfile


# region инициализация функций

# инициализация функции с решетом эратосфена
def sieve_function(number):
    # выбрал такое ограничение диапазона, до 5000 числа работает хорошо,
    # на больших числах диапазона не хватает, нужно увеличивать множитель.
    n = number * 10
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result[number]


# инициализация функции без использования решета эратосфена
def wo_sieve_function(number):
    a = 0
    count = 3
    while True:
        for x in range(2, count):
            if not count % x:
                break
        else:
            a += 1
        if a == number:
            return count
        count += 1


# инициализация main функции
def main(number):
    sieve_function(number)
    wo_sieve_function(number)


# endregion

# проверка самих функций
print(sieve_function(100))
print(wo_sieve_function(100))

# region timeit

print('*' * 25)
print(timeit.timeit('sieve_function(10)', number=10000, globals=globals()))  # 0.2578423
print(timeit.timeit('wo_sieve_function(10)', number=10000, globals=globals()))  # 0.1500497
print('*' * 25)
print(timeit.timeit('sieve_function(50)', number=10000, globals=globals()))  # 1.505755
print(timeit.timeit('wo_sieve_function(50)', number=10000, globals=globals()))  # 2.7216027
print('*' * 25)
print(timeit.timeit('sieve_function(100)', number=10000, globals=globals()))  # 3.1774457
print(timeit.timeit('wo_sieve_function(100)', number=10000, globals=globals()))  # 11.7963184
print('*' * 25)
print(timeit.timeit('sieve_function(250)', number=10000, globals=globals()))  # 8.36702
print(timeit.timeit('wo_sieve_function(250)', number=10000, globals=globals()))  # 94.8030241

# endregion

# region cProfile

print('*' * 25)
cProfile.run('main(10)')
# 1    0.000    0.000    0.000    0.000 lesson_4-2.py:23(sieve_function)
# 1    0.000    0.000    0.000    0.000 lesson_4-2.py:38(wo_sieve_function)
print('*' * 25)
cProfile.run('main(50)')
# 0.000    0.000    0.000    0.000 lesson_4-2.py:23(sieve_function)
# 1    0.000    0.000    0.000    0.000 lesson_4-2.py:38(wo_sieve_function)
print('*' * 25)
cProfile.run('main(100)')
# 1    0.000    0.000    0.000    0.000 lesson_4-2.py:23(sieve_function)
# 1    0.001    0.001    0.001    0.001 lesson_4-2.py:38(wo_sieve_function)
print('*' * 25)
cProfile.run('main(250)')
# 1    0.001    0.001    0.001    0.001 lesson_4-2.py:23(sieve_function)
# 1    0.010    0.010    0.010    0.010 lesson_4-2.py:38(wo_sieve_function)
print('*' * 25)
cProfile.run('main(1000)')
# 1    0.003    0.003    0.004    0.004 lesson_4-2.py:23(sieve_function)
# 1    0.210    0.210    0.210    0.210 lesson_4-2.py:38(wo_sieve_function)

# endregion
