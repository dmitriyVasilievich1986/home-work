
# region Текст задания

# Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию
# дочернего (функция, отвечающая за отображение информации о товаре в одной строке).

# endregion


class ItemDiscount:
    def __init__(self):
        self._name = 'item'
        self._price = 5000.00


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар: {self._name}, цена: {self._price}'


consumables = ItemDiscountReport()
print(consumables.get_parent_data())
