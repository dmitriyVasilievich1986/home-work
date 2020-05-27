# region Текст задания

"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел
до и после запятой. Если они совпадают,
программа должна возвращать значение True, иначе False.
"""

# endregion

import re

while True:
    try:
        number = float(input('\nВведите число: '))
    except ValueError:
        print('Вы ввели не число')
        continue    
    if number == int(number):
        print('Целое число')
        continue    
    new_list = re.split(r'[.]', str(number))
    if int(new_list[0]) == int(new_list[1]):
        print(f'Число {number} имеет равные числа до и после запятой')
    else:
        print(f'Число {number} имеет неравные числа до и после запятой')