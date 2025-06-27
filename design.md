
# Extract nouns from the user stories or specification

As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed.

As a shop manager
So I can manage orders
I want to be able to create a new order.

```
Nouns:
items, name, unit price, quantity, orders, customer name, date
```
# Infer the Table Name and Columns

| Record                | Properties          |
| --------------------- | ------------------  |
| items                 | name, unit_price, quantity
| orders                | customer_name, date, 

<!-- items can be a property of order-->
<!--  or is a join table needed here with both foreign_keys -->
<!-- Need to come back -->

Table: items
- id: SERIAL    
- name: VARCHAR
- unit_price: INT
- quantity: INT

Table: orders
- id: SERIAL
- customer_name: VARCHAR
- date: DATE

 
# Design the many-to-many relationship

Can one Item have many orders --> ✅
Can order have many items --> ✅

# Design the Join table

The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The naming convention is `table1_table2`.

```
Join table for tables: items and orders
Join table name: items_orders
Columns: item_id, order_id
```

# Write the sequel

<!-- Create the first table  -->
```sql
id SERIAL PRIMARY KEY,
CREATE TABLE items (
name VARCHAR,
unit_price INT,
quantity INT
);
```


<!-- Create the second -->
```sql
CREATE TABLE orders (
id SERIAL PRIMARY KEY,
customer_name VARCHAR
);
```


<!-- Create the join table  -->
```sql
CREATE TABLE items_orders (
item_id INT,
order_id,
CONSTRAINT fk_item FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE,
CONSTRAINT fk_order FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
PRIMARY KEY (item_id, order_id)
);
```