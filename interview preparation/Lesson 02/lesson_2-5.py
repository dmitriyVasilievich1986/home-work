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

    # переопределяем функцию str
    def __str__(self):
        """функция возвращает строку с названием товара и его ценой, с учетом скидки"""
        return f'Название: {self.name}, цена со скидкой: {self.price * self._discount}'

    def get_parent_data(self):
        """функиця возвращает строку с названием товара и его ценой"""
        return f'Название: {self.name}, цена: {self.price}'


# endregion


# инициализация экземпляра класса
consumables = ItemDiscount()
# вызов функции класса наследника с передачей скидки
print(ItemDiscountReport(discount=0.8))