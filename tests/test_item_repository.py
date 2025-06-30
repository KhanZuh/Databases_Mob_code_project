from lib.item_repository import ItemRepository
from lib.item import Item

"""
Test all returns all items
"""
def test_all_returns_all_items(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    item_repository = ItemRepository(db_connection)

    result = item_repository.all()

    expected = [
        Item(1, 'Squeaky Bone Toy', 5, 50),
        Item(2, 'Catnip Mouse', 3, 100),
        Item(3, 'Premium Dog Food - Beef', 25, 30),
        Item(4, 'Tropical Fish Flakes', 7, 40),
        Item(5, 'Hamster Wheel', 15, 10),
        Item(6, 'Bird Seed Mix', 8, 25),
        Item(7, 'Rabbit Hutch Straw', 6, 15),
        Item(8, 'Flea Collar - Large', 12, 20),
        Item(9, 'Tennis Ball Pack (3)', 10, 35),
        Item(10, 'Aquarium Castle Decoration', 18, 5)
    ]

    assert result == expected

"""
Test find returrns selected item
"""
def test_find_returns_selcted_items(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    item_repository = ItemRepository(db_connection)

    result = item_repository.find(5)

    expected = [
        Item(5, 'Hamster Wheel', 15, 10)
    ]

    assert result == expected


"""
Test find_by_item returrns selected order
"""
def test_find_by_order_returns_selcted_item(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    item_repository = ItemRepository(db_connection)

    result = item_repository.find_by_order(6)

    expected = [
        Item(1, 'Squeaky Bone Toy', 5, 50),
        Item(3, 'Premium Dog Food - Beef', 25, 30),
        Item(8, 'Flea Collar - Large', 12, 20)
    ]

    assert result == expected

"""
Test create adds item
"""
def test_create_adds_item(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    item_repository = ItemRepository(db_connection)
    order = Item(None, 'Squeaky Burger', 5, 25)

    item_repository.create(order)

    result = item_repository.all()

    expected = [
        Item(1, 'Squeaky Bone Toy', 5, 50),
        Item(2, 'Catnip Mouse', 3, 100),
        Item(3, 'Premium Dog Food - Beef', 25, 30),
        Item(4, 'Tropical Fish Flakes', 7, 40),
        Item(5, 'Hamster Wheel', 15, 10),
        Item(6, 'Bird Seed Mix', 8, 25),
        Item(7, 'Rabbit Hutch Straw', 6, 15),
        Item(8, 'Flea Collar - Large', 12, 20),
        Item(9, 'Tennis Ball Pack (3)', 10, 35),
        Item(10, 'Aquarium Castle Decoration', 18, 5),
        Item(11, 'Squeaky Burger', 5, 25)
    ]

    assert result == expected