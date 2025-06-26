
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
| orders                | customer_name, date

Table: items


Table: orders
