from lib.order_repository import OrderRepository
from lib.order import Order
from datetime import datetime, date
"""
Test all returns all items
"""
def test_all_returns_all_items(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    order_repository = OrderRepository(db_connection)

    result = order_repository.all()

    expected = [
        Order(1, 'Charlie Barkington', date(2025,6,10)),
        Order(2, 'Mittens Whiskers', date(2025,6,11)),
        Order(3, 'Goldie Finley', date(2025,6,12)),
        Order(4, 'Hopper McFluff', date(2025,6,12)),
        Order(5, 'Polly Crackers', date(2025,6,13)),
        Order(6, 'Rex Von Woof', date(2025,6,14)),
        Order(7, 'Flopsy Bunbun', date(2025,6,14)),
        Order(8, 'Captain Meow', date(2025,6,15)),
        Order(9, 'Spike Tailspin', date(2025,6,16)),
        Order(10, 'Bubbles Swimmy', date(2025,6,16))
    ]

    assert result == expected

"""
Test find returrns selected order
"""
def test_find_returns_selcted_order(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    order_repository = OrderRepository(db_connection)

    result = order_repository.find(5)

    expected = [
        Order(5, 'Polly Crackers', date(2025,6,13))
    ]

    assert result == expected


"""
Test find_by_item returrns selected order
"""
def test_find_by_item_returns_selcted_order(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    order_repository = OrderRepository(db_connection)

    result = order_repository.find_by_item(6)

    expected = [
        Order(5, 'Polly Crackers', date(2025,6,13))
    ]

    assert result == expected

"""
Test create adds order
"""
def test_create_adds_order(db_connection):
    db_connection.connect()
    db_connection.seed("seeds/shop_manager.sql")

    order_repository = OrderRepository(db_connection)
    order = Order(None, 'Maggie Ralfie', date(2025,6,18))

    order_repository.create(order)

    result = order_repository.all()

    expected = [
        Order(1, 'Charlie Barkington', date(2025,6,10)),
        Order(2, 'Mittens Whiskers', date(2025,6,11)),
        Order(3, 'Goldie Finley', date(2025,6,12)),
        Order(4, 'Hopper McFluff', date(2025,6,12)),
        Order(5, 'Polly Crackers', date(2025,6,13)),
        Order(6, 'Rex Von Woof', date(2025,6,14)),
        Order(7, 'Flopsy Bunbun', date(2025,6,14)),
        Order(8, 'Captain Meow', date(2025,6,15)),
        Order(9, 'Spike Tailspin', date(2025,6,16)),
        Order(10, 'Bubbles Swimmy', date(2025,6,16)),
        Order(11, 'Maggie Ralfie', date(2025,6,18))
    ]

    assert result == expected