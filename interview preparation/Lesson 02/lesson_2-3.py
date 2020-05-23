# region Текст задания

"""
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


# endregion


class ItemDiscount:
    def __init__(self):
        self._name = 'item'
        self._price = 5000.00

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        super().__init__()

    def get_parent_data(self):
        return f'Название: {self.name}, цена: {self.price}'


consumables = ItemDiscount()
print(ItemDiscountReport().get_parent_data())
