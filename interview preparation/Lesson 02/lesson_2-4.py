# region Текст задания

"""
Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
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
    def __init__(self, price=5000.00):
        super().__init__(price)

    def get_parent_data(self):
        return f'Название: {self.name}, цена: {self.price}'


consumables = ItemDiscount(100.00)
print(consumables.price)
print(ItemDiscountReport(100.00).get_parent_data())
