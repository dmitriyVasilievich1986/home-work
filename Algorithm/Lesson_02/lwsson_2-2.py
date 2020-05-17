# region Текст задания

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# endregion

# инициализация счетчиков
even_number = 0
odd_number = 0
# ввод числа от пользователя
number = int(input('Введите натуральное число: '))
# вход в цикл проверки на четность
while number != 0:
    if (number % 10) % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    number //= 10
# вывод результата
print(f'Количество четных цифр: {even_number}')
print(f'Количество нечетных цифр: {odd_number}')
