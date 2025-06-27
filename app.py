from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository
from lib.item import Item
from lib.order import Order
from datetime import date

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/shop_manager.sql")

# Create repos
item_repository = ItemRepository(connection)
order_repository = OrderRepository(connection)

def main_menu():
    print("Welcome to our Pet Shop!")
    print("What would you like to do?")
    print(" 1 = List all the shop items")
    print(" 2 = Create a new item")
    print(" 3 = Find the quantity for an item")
    print(" 4 = List all orders")
    print(" 5 = Create a new order")
    print(" 6 = List items for a specific order")
    print(" 7 = List the orders for a specific item")
    print(" 0 = exit")

def list_all_items():
    items = item_repository.all()
    print("Here's a list of all shop items:")
    for item in items:
        print(f" #{item.id} {item.name} - Unit price: {item.unit_price} - Quantity: {item.quantity}")

def create_item(item_name, item_price, item_quantity):
    item = Item(None, item_name, int(item_price), int(item_quantity))
    item_repository.create(item)

def find_quantity():
    print("Please enter item id")
    item_id = input()
    items = item_repository.find(item_id)
    item = items[0]  # find returns a list with one item
    print(f"Item: {item.name} - Quantity: {item.quantity}")

def list_all_orders():
    orders = order_repository.all()
    print("Here's a list of all orders:")
    for order in orders:
        print(f" #{order.id} Customer: {order.customer_name} - Date: {order.order_date}")

def create_order(order_name, order_date):
    order = Order(None, order_name, order_date)
    order_repository.create(order)

def list_items_for_order(order_id):
    items = item_repository.find_by_item(order_id)
    print(f"Items in order #{order_id}:")
    for item in items:
        print(f" - {item.name} (Unit price: {item.unit_price}, Quantity: {item.quantity})")

def list_orders_for_item(item_id):
    orders = order_repository.find_by_item(item_id)
    print(f"Orders for item #{item_id}:")
    for order in orders:
        print(f" - Order #{order.id} by {order.customer_name} on {order.order_date}")

def run_app():
    while True:
        main_menu()
        choice = input("Please make a choice: ")
        match choice:
            case "1":
                list_all_items()
            case "2":
                print("Please enter an item name")
                item_name = input()
                print("Please enter an item price")
                item_price = input()
                print("Please enter an item quantity")
                item_quantity = input()
                create_item(item_name, item_price, item_quantity)
                print("Item created")
            case "3":
                find_quantity()
            case "4":
                list_all_orders()
            case "5":
                print("Please enter an order name")
                order_name = input()
                print("Please enter an order date")
                order_date = input()
                create_order(order_name, order_date)
                print("Order created")
            case "6":
                print("Please enter id for order")
                order_id = input()
                list_items_for_order(order_id)
            case "7":
                print("Please enter item id")
                item_id = input()
                list_orders_for_item(item_id)
            case "0":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_app()