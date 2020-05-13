# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

# ввод трех сторон треугольника
print('Введите размеры трех сторон треугольника')
a = int(input('Длина первой стороны: '))
b = int(input('Длина второй стороны: '))
c = int(input('Длина третьей стороны: '))

# проверка на существование треугольника => на равносторон. => равнобед.
if not ((a + b) > c and (a + c) > b and (b + c) > a):
    print('Треугольник вырожденный')
elif a == b == c:
    print('Треугольник равносторонний')
elif (a == b) or (a == c) or (b == c):
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')
