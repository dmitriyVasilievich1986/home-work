# region Текст задания

"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


# endregion


class ItemDiscount:
    def __init__(self):
        self._name = 'item'
        self._price = 5000.00


class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        super().__init__()

    def get_parent_data(self):
        return f'Название: {self.name}, цена: {self.price}'


consumables = ItemDiscount()
print(ItemDiscountReport().get_parent_data())
