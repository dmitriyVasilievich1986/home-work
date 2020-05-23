# region Текст задания

# Усовершенствовать родительский класс таким образом,
# чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.

# endregion


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self._name}, цена: {self._price}'


consumables = ItemDiscountReport('item1', 5000.00)
print(consumables.get_parent_data())
