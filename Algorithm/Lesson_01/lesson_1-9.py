# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# ввод трех цифр
print('Введите три разных числа')
int1 = int(input('Введите первое число: '))
int2 = int(input('Введите второе число: '))
int3 = int(input('Введите третье число: '))

# алгоритм проверки числа на соответствие условиям
if (int1 > int2 or int1 > int3) and (int1 < int2 or int1 < int3):
    print(f'Значение среднего числа: {int1}')
elif (int2 > int1 or int2 > int3) and (int2 < int1 or int2 < int3):
    print(f'Значение среднего числа: {int2}')
else:
    print(f'Значение среднего числа: {int3}')