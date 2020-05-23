# region Текст задания

"""
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы (вторая и третья строка после объявления дочернего класса).
"""


# endregion


class ItemDiscount:
    def __init__(self, price=5000.00):
        self._name = 'item'
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, price=5000.00, discount=1):
        super().__init__(price)
        self._discount = discount

    def __str__(self):
        return f'Название: {self.name}, цена со скидкой: {self.price * self._discount}'

    def get_parent_data(self):
        return f'Название: {self.name}, цена: {self.price}'


consumables = ItemDiscount()
print(ItemDiscountReport(discount=0.8))
