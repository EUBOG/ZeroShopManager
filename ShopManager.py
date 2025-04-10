class Store:
    def __init__(self, name, address, items=None):
        self.name = name  # наименование магазина
        self.address = address  # адрес магазина
        self.items = items if items is not None else {}  # Словарь товаров и их цен

    def add_item(self, item, item_price):
        self.items[item] = item_price  # Добавление товара и его цены в словарь

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]  # Удаление товара из словаря
            print(f"Товар '{item}' удалён из списка .")
        else:
            print(f"Товар '{item}' не найден в списке.")

    def get_price(self, item):
        if item in self.items:
            item_price = self.items[item]  # Получаем цену товара
            print(f"Цена товара '{item}' = '{item_price}' руб.")
        else:
            print(f"None. Поснение: Товар '{item}' не найден в списке.")

    def correct_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price # Новая цена
            print(f"Новая цена товара '{item}' = '{new_price}' руб.")
        else:
            print(f"Товар '{item}' не найден в списке.")

# Работаем
manit = Store("Манит", "Улица Фруктовая, 8")
googlever = Store("Гугливер", "Улица Овощная, 88")
eighty = Store("Восьмёрочка", "Улица Цифровая, 16")
manit.add_item("Яблоко", 50)
manit.add_item("Банан", 70)
manit.add_item("Киви", 80)
manit.add_item("Ананас", 100)
manit.add_item("Виноград", 90)
googlever.add_item("Яблоко", 60)
googlever.add_item("Банан", 78)
googlever.add_item("Киви", 89)
eighty.add_item("Яблоко", 55)
eighty.add_item("Банан", 75)
eighty.add_item("Киви", 85)

print(f"Ассортимент manit:", manit.items)  # {'Яблоко': 50, 'Банан': 70, 'Киви': 80, 'Ананас': 100, 'Виноград': 90}
print(f"Ассортимент googlever:", googlever.items)
print(f"Ассортимент eighty:", eighty.items)

manit.remove_item("Яблоко")
print(f"Ассортимент manit:", manit.items)  # Яблока в списке быть не должно {'Банан': 70, 'Киви': 80, 'Ананас': 100, 'Виноград': 90}

manit.remove_item("Груша")  # Товар 'Груша' не найден в списке.

manit.get_price("Банан") # Запрос цены бананов
manit.get_price("Урюк") # Запрос цены урюка

manit.correct_price("Банан", 75)
print(manit.items)  # {'Банан': 75, 'Киви': 80, 'Ананас': 100, 'Виноград': 90}
