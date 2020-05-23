# region Текст задания

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# endregion

# инициализация констант
START_POSITION = 2
STOP_POSITION = 99

# инициализация словаря для сравнения и хранения счетчика
digit_count = {}
for item in range(2, 10):       # keys - число для сравнения
    digit_count[item] = 0       # value - счетчик
# инициализируем цикл проверки кратности чисел
for cycle in range(START_POSITION, STOP_POSITION):
    for item in digit_count.keys():
        if not cycle % item:
            digit_count[item] += 1
# выводим полученный результат
print(f'В диапазоне чисел от {START_POSITION} до {STOP_POSITION}')
for item in digit_count.keys():
    print(f'Числу {item} кратно {digit_count[item]} чисел.')
