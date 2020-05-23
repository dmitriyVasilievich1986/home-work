# region Текст задания

"""
Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
"""


# endregion


# region инициализация классов

# инициализация родительского класса
class ItemDiscount:
    # изменение цены товара при инициализации класса
    def __init__(self, price=5000.00):
        """конструктор класса"""
        self._name = 'item'
        self._price = price

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
    def __init__(self, price):
        """конструктор класса с использованием конструктора родителя"""
        super().__init__(price)

    def get_parent_data(self):
        """функиця возвращает строку с названием товара и его ценой"""
        return f'Название: {self.name}, цена: {self.price}'


# endregion


# инициализация экземпляра класса
consumables = ItemDiscount(100.00)
# вызов аттрибута класса
print(consumables.price)
# вызов функции класса наследника
print(ItemDiscountReport(100.00).get_parent_data())
