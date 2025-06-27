from lib.order import Order

class OrderRepository:
    def __init__(self, data_connection):
        self.connection = data_connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM orders")
        return [Order(
            row["id"],
            row["customer_name"],
            row["order_date"]
        ) for row in rows]
    
    def find(self, order_id):
        rows = self.connection.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        return [Order(rows[0]["id"], rows[0]["customer_name"], rows[0]["order_date"])]
    
    def find_by_item(self, item_id):
        rows = self.connection.execute("""
                                        SELECT orders.id AS order_id, orders.customer_name, orders.order_date
                                        FROM orders
                                        JOIN items_orders ON items_orders.order_id = orders.id
                                        JOIN items ON items.id = items_orders.item_id
                                        WHERE items.id = %s """, (item_id,))
        return [Order(
            row["order_id"],
            row["customer_name"],
            row["order_date"]
        ) for row in rows]
    
    def create(self, order):
        self.connection.execute("INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)", (order.customer_name, order.order_date))