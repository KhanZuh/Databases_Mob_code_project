from lib.item import Item

"""
Post constructs with an id, name, unit_price and quantity
"""
def test_item_constructs():
    item = Item(1, 'Squeaky Bone Toy', 5, 50)
    assert item.id == 1
    assert item.name == 'Squeaky Bone Toy'
    assert item.unit_price == 5
    assert item.quantity == 50



"""
We can format item to strings nicely
"""
def test_item_format_nicely():
    item = Item(1, 'Squeaky Bone Toy', 5, 50)
    assert str(item) == "Item(id=1, name='Squeaky Bone Toy', unit_price=5, quantity=50)"


"""
We can compare two identical items
And have them be equal
"""
def test_items_are_equal():
    item1 = Item(1, 'Squeaky Bone Toy', 5, 50)
    item2 = Item(1, 'Squeaky Bone Toy', 5, 50)
    assert item1 == item2
