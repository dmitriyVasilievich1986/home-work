# region Текст задания

# Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.

# endregion


def devil_number_cycle(count):
    result = 0
    number = 1
    # инициализация цикла
    while count != 0:
        count -= 1
        result += number  # сначала прибавляем число,
        number /= -2  # затем делим
    return result


def devil_number_double_cycle(count):
    result = 0
    # инициализация цикла
    for cycle in range(count):
        number = 1
        # инициализация внутреннего цикла
        for inner_cycle in range(cycle):
            number /= -2
        result += number
    return result


def devil_number_recursion(count, result=0, number=1):
    if count == 0:
        return result
    result += number
    number /= -2
    return devil_number_recursion(count - 1, result, number)



print(devil_number_cycle(50))
print('*' * 25)
print(devil_number_recursion(50))
print('*' * 25)
print(devil_number_double_cycle(50))

