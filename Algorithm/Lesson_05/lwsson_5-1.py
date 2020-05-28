# region Текст задания

# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

# endregion

# импортируем библиотеку
from collections import defaultdict, Counter

# инициализация словаря
my_list = Counter()

# запрос данных от пользователя
company_count = int(input('Введите количество отчетных компаний: '))
for count in range(company_count):
    company_name = input('Введите название фирмы: ')
    for x in range(1, 5):
        my_list[company_name] += float(input(f'Введите доход за {x} квартал: '))
    my_list[company_name] /= 4

# вывод информации о фирмах
print('\nДоход компаний выше или равно среднему:')
for a in range(len(my_list) // 2, len(my_list)):
    print(f'Фирма {list(my_list.keys())[a]}, средний доход за год: {my_list[list(my_list.keys())[a]]}')
if len(my_list) // 2 > 0:
    print('\nДоход компаний ниже среднего:')
    for a in range(len(my_list) // 2):
        print(f'Фирма {list(my_list.keys())[a]}, средний доход за год: {my_list[list(my_list.keys())[a]]}')
