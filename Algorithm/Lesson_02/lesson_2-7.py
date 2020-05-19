# region Текст задания

# Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n — любое натуральное число.

# endregion

# ввод и инициализация переменных
n = int(input('Введите натуральное число: '))
left = 0
right = n * (n + 1) / 2
# цикл подсчета левой стороны формулы
while n > 0:
    left += n
    n -= 1
# проверка формулы
if left == right:
    print(f'Выражение {left} = {right}: верно')     # можно было оставить только эту часть)
else:
    print(f'Выражение {left} = {right}: не верно')
