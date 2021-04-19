from app.models import Item, Basket


def test_new_item():
    item = Item('order-1', 'Macbook Air', 1199.99, 1, 'Electronics')

    assert item.sku == 'order-1'
    assert item.name == 'Macbook Air'
    assert item.price == 1199.99
    assert item.quantity == 1
    assert item.category == 'Electronics'


def test_new_basket():
    item1 = Item('order-1', 'Macbook Air', 1199.30, 1, 'Electronics')
    item2 = Item('order-2', 'Airpods', 199.20, 1, 'Electronics')
    item3 = Item('order-3', 'Nike Air Max', 128.50, 1, 'Shoes')

    basket = Basket()
    basket.add_to_basket(item1)
    basket.add_to_basket(item2)
    basket.add_to_basket(item3)

    assert len(basket.items) == 3
    assert basket.total == 1527
    assert basket.items[1].name == 'Airpods'
