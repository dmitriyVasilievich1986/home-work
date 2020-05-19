# region Текст задания

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# endregion

max_number = 0


def digit_summary(number):
    if number < 10:
        return number
    return number % 10 + digit_summary(number // 10)


while True:
    print('\nДля завершения введите 0')
    number = int(input('Введите натуральное число: '))
    if number == 0:
        break
    elif digit_summary(number) > digit_summary(max_number):
        max_number = number
print(f'Максимальное число: {max_number}')
print(f'Сумма его цифр: {digit_summary(max_number)}')
