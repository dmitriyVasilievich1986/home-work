# region Текст задания

# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# endregion

# импорт библиотек
import re
from collections import deque

# инициализация списков
result = deque([0])
first_sum = deque(re.findall('.', (input('Введите первое число в 16-ричной системе: ')).lower()))
second_sum = deque(re.findall('.', (input('Введите второе число в 16-ричной системе: ')).lower()))

# выравниваем списки по длине
if first_sum > second_sum:
    second_sum.appendleft('0')
else:
    first_sum.appendleft('0')
# переворачиваем, чтобы проще было считать
first_sum.reverse()
second_sum.reverse()


# инициализируем функцию подсчета двух чисел
def hex_summary(a, b, c):
    my_dict = {re.findall(r'.', '0123456789abcdef')[b]: b for b in range(0, 16)}
    output = my_dict[a] + my_dict[b]
    if output > 15:
        c[0] += output - 16
        c.appendleft(1)
    else:
        c[0] += output
        c.appendleft(0)
    c[1] = list(my_dict.keys())[c[1]]
    return c


# вызов функции
for cycle in range(len(first_sum)):
    hex_summary(first_sum[cycle], second_sum[cycle], result)
result.popleft()
# вывод результата
print(result)
