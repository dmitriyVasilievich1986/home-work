# region Текст задания

# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
# и заканчивая 127-м включительно. Вывод выполнить в табличной форме:
# по десять пар "код-символ" в каждой строке.

# endregion

# инициализация констант и переменных
START_POSITION = 32
END_POSITION = 127
start = START_POSITION


# инициализация рекурсивной функции
def print_ASCII_table(start, stop):
    """
        Рекурсивная функия принимает диапазон начальной и конечной позиций.
            выводит в консоль все значения и символьные представления
            в диапазоне указанных значений.
        Принимает: start= целое число,
                    stop= целое число
        """
    print(f'{start}\t{chr(start)}')
    if start == stop:
        return
    print_ASCII_table(start + 1, stop)


# инициализация цикла вывода таблиц символов
while True:
    stop = start + 9  # включительно start и stop получается 10
    print('код\tсимвол')
    if stop > END_POSITION:  # если достигнут конец, то выходим из цикла
        print_ASCII_table(start, END_POSITION)
        break
    print_ASCII_table(start=start, stop=stop)
    start = stop
    print()
