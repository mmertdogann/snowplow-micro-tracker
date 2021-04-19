class Basket:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_to_basket(self, item):
        self.items.append(item)
        self.calculate_total(item)

    def calculate_total(self, item):
        self.total += item.price * item.quantity

    def get_items(self):
        item_list = []

        for item in self.items:
            item_list.append(item.__dict__)

        return item_list


class Item:
    def __init__(self, sku, name, price, quantity, category):
        self.sku: str = sku
        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.category: str = category

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Category: {self.category}"
