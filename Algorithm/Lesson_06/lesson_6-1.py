# region Текст задания

"""
    Подсчитать, сколько было выделено памяти под переменные
    в ранее разработанных программах в рамках первых трех уроков.
    Проанализировать результат и определить программы
    с наиболее эффективным использованием памяти.
    """

"""
    Сформировать из введенного числа обратное по порядку входящих
    в него цифр и вывести на экран.
    Например, если введено число 3486, надо вывести 6843.
    """

# endregion


# импортируем библиотеки
from re import findall
from calculate_memory import input_list


# инициализация константы
NUMBER = 123456789

# region функции

# инициализация функции через цикл
def reverse_number_cycle(number):
    output = 0
    while number:
        output = output * 10 + number % 10
        number //= 10
    return [output, number]


# инициализация функции через регулярные выражения
def reverse_number_regexp(number):
    temporal = str(number)
    reg_number = findall('.', temporal)
    reg_number.reverse()
    result = ''.join(reg_number)
    output = int(result)
    return [output, temporal, reg_number, result]


# инициализация функции через приведения числа к строке
def reverse_number_string(number):
    temporal = str(number)
    result = [temporal[x] for x in range(len(temporal) - 1, -1, -1)]
    reverse_number = ''.join(result)
    output = int(reverse_number)
    return [output, temporal, result, reverse_number]

# endregion


# вызов всех функций для получения результат
print(reverse_number_string(NUMBER)[0])
print(reverse_number_regexp(NUMBER)[0])
print(reverse_number_cycle(NUMBER)[0])


# вызов функции подсчета затрат памяти
print("*" * 50)
print(input_list(reverse_number_cycle(NUMBER)))     # 52
print(input_list(reverse_number_regexp(NUMBER)))    # 594
print(input_list(reverse_number_string(NUMBER)))    # 594

"""
Вывод:
    полученный результат говорит об однозначном преимуществе
    через одиночный цикл.
    два остальных решения вроде сделал по разному, но по резульатам 
    затрат памяти очевидно, что решения по сути одинаковые... 
"""