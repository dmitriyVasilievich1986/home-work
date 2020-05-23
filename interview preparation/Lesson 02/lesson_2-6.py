# region Текст задания

"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
"""


# endregion


# region инициализация классов

# инициализация родительского класса
class ItemDiscount:
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
    def __init__(self, price=5000.00, discount=1):
        """конструктор класса с использованием конструктора родителя"""
        super().__init__(price)
        self._discount = discount

    def __str__(self):
        """функция возвращает строку с названием товара и его ценой, с учетом скидки"""
        return f'Название: {self.name}, цена со скидкой: {self.price * self._discount}'

    def get_parent_data(self):
        """функиця возвращает строку с названием товара и его ценой"""
        return f'Название: {self.name}, цена: {self.price}'

    # первый вариант функции get_info
    def get_info(self):
        """функиця возвращает строку с названием товара и его ценой"""
        return self


class ItemNameInfo(ItemDiscountReport):
    def __init__(self):
        """конструктор класса с использованием конструктора родителя"""
        super().__init__()

    # второй вариант функции get_info
    def get_info(self):
        """функиця возвращает строку с названием товара"""
        return f'Название: {self.name}'


class ItemPriceInfo(ItemDiscountReport):
    def __init__(self):
        """конструктор класса с использованием конструктора родителя"""
        super().__init__()

    # третий вариант функции get_info
    def get_info(self):
        """функиця возвращает строку с ценой товара"""
        print(f'Цена: {self.price}')


# endregion


# вызов функии во всех трех классах
print(ItemDiscountReport().get_info())
print(ItemNameInfo().get_info())
ItemPriceInfo().get_info()
