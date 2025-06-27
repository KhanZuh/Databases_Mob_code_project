from lib.order import Order

"""
Post constructs with an id, customer_name and order_date
"""
def test_order_constructs():
    order = Order(1, 'Charlie Barkington', '2025-06-10')
    assert order.id == 1
    assert order.customer_name == 'Charlie Barkington'
    assert order.order_date == '2025-06-10'



"""
We can format order to strings nicely
"""
def test_order_format_nicely():
    order = Order(1, 'Charlie Barkington', '2025-06-10')
    assert str(order) == "Order(id=1, customer_name='Charlie Barkington', order_date='2025-06-10')"


"""
We can compare two identical orders
And have them be equal
"""
def test_orders_are_equal():
    order1 = Order(1, 'Charlie Barkington', '2025-06-10')
    order2 = Order(1, 'Charlie Barkington', '2025-06-10')
    assert order1 == order2
