# region Текст задания

# Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.

# endregion


class ItemDiscount:
    def __init__(self, name, price):
        self._name = name
        self._price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self.name}, цена: {self.price}'


consumables = ItemDiscountReport('item1', 5000.00)
