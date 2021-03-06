# region Текст задания

"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


# endregion


# region инициализация классов

# инициализация родительского класса
class ItemDiscount:
    def __init__(self):
        """конструктор класса"""
        # инкапсуляция аттрибутов класса
        self._name = 'item'
        self._price = 5000.00


# инициализация класса наследника
class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        """конструктор класса с использованием конструктора родителя"""
        super().__init__()

    def get_parent_data(self):
        """функиця возвращает строку с названием товара и его ценой"""
        # попытка вызвать аттрибуты без использования инкапсуляции
        return f'Название: {self.name}, цена: {self.price}'


# endregion


# инициализация экземпляра класса
consumables = ItemDiscount()
# вызов функции класса наследника,
# без вызова функции - скрипт компилируется без ошибок
# а pylint нашел ошибку
print(ItemDiscountReport().get_parent_data())
