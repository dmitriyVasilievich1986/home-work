# region Текст задания

"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
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

    def get_info(self):
        return self


class ItemNameInfo(ItemDiscountReport):
    def __init__(self):
        super().__init__()

    def get_info(self):
        return f'Название: {self.name}'


class ItemPriceInfo(ItemDiscountReport):
    def __init__(self):
        super().__init__()

    def get_info(self):
        print(f'Цена: {self.price}')


print(ItemDiscountReport().get_info())
print(ItemNameInfo().get_info())
ItemPriceInfo().get_info()
