# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# ввод двух символов
print('Введите два символа')
lit1 = ord(input('Первый символ: '))
lit2 = ord(input('Второй символ: '))

# вывод положения символов и расстояния между
print(f'Положение символа {chr(lit1)}: {lit1 - ord("a") + 1}')
print(f'Положение символа {chr(lit2)}: {lit2 - ord("a") + 1}')
print(f'Количество букв между символом {chr(lit1)} и {chr(lit2)}: {lit2 - lit1 - 1}')