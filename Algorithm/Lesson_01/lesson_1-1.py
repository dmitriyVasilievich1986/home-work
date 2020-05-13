# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# просим пользователя ввести число
number = int(input('Введите целое трехзначное число: '))

# разбиваем число на цифры
digit1 = number // 100
digit2 = (number - digit1 * 100) // 10
digit3 = number % 10

# находим сумму и произведение
summary = digit1 + digit2 + digit3
multiplication = digit1 * digit2 * digit3

# вывод значений
print(f'Сумма цифр {digit1}+{digit2}+{digit3}={summary}')
print(f'Произведение цифр {digit1}*{digit2}*{digit3}={multiplication}')
