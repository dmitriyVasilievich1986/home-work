# region Текст задания

"""
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


# endregion


# region инициализация классов

# инициализация родительского класса
class ItemDiscount:
    def __init__(self):
        """конструктор класса"""
        self._name = 'item'
        self._price = 5000.00

    # инициализация геттеров для получения скрытых аттрибутов
    @property
    def name(self):
        """геттер аттрибута _name"""
        return self._name

    @property
    def price(self):
        """геттер аттрибута _price"""
        return self._price


# инициализация класса наследника
class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        """конструктор класса с использованием конструктора родителя"""
        super().__init__()

    def get_parent_data(self):
        """функиця возвращает строку с названием товара и его ценой"""
        return f'Название: {self.name}, цена: {self.price}'


# endregion


# инициализация экземпляра класса
consumables = ItemDiscount()
# вызов функции класса наследника
print(ItemDiscountReport().get_parent_data())
