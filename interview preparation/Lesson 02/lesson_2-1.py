# region Текст задания

"""
Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре:
название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке. Проверить работу программы,
создав экземпляр (объект) родительского класса.
"""


# endregion


class ItemDiscount:
    def __init__(self):
        self.name = 'item'
        self.price = 5000.00


class ItemDiscountReport(ItemDiscount):
    def __init__(self):
        super().__init__()

    def get_parent_data(self):
        return f'Название: {self.name}, цена: {self.price}'


consumables = ItemDiscount()
print(ItemDiscountReport().get_parent_data())
