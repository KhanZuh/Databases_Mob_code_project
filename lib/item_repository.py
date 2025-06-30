from lib.item import Item

class ItemRepository:
    def __init__(self, data_connection):
        self.connection = data_connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM items")
        return [Item(
            row["id"],
            row["name"],
            row["unit_price"],
            row["quantity"]
        ) for row in rows]
    
    def find(self, item_id):
        rows = self.connection.execute("SELECT * FROM items WHERE id = %s", (item_id,))
        return [Item(rows[0]["id"], rows[0]["name"], rows[0]["unit_price"], rows[0]["quantity"])]
    
    def find_by_order(self, order_id):
        rows = self.connection.execute("""
                                        SELECT items.id AS item_id, items.name, items.unit_price, items.quantity
                                        FROM items
                                        JOIN items_orders ON items_orders.item_id = items.id
                                        JOIN orders ON orders.id = items_orders.order_id
                                        WHERE orders.id = %s """, (order_id,))
        return [Item(
            row["item_id"],
            row["name"],
            row["unit_price"],
            row["quantity"]
        ) for row in rows]
    
    
    def create(self, item):
        self.connection.execute("INSERT INTO items (name, unit_price, quantity) VALUES (%s, %s, %s)", (item.name, item.unit_price, item.quantity))
        