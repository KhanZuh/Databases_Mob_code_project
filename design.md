```sql
-- Databse schema

-- From user stoires - two main entites 
-- Items (shop inventory)
-- Orders (customer purchases)

-- Analyze the relationships
-- Can one ITEM have many ORDERS? → Yes (same item can be ordered multiple times)
-- Can one ORDER have many ITEMS? → ? --> "I want to assign each order to their corresponding item" - this suggests each order is for ONE specific item. --> So this is a One-to-Many relationship: One Item → Many Orders

-- Attributes
-- From user stories

-- Items: 
-- name (string)
-- unit_price (number)
-- quantity (number - stock level)

-- Orders:
-- customer_name (string)
-- order_date (date)
-- item_id (foreign key to items table)

-- Design decisions
-- Data types:
-- unit_price: INTEGER to store price in pence/cents 
-- quantity: INTEGER (whole numbers of items)
-- order_date: DATE type
-- names: TEXT/VARCHAR

-- Sample Data Thinking:
-- Items: vacuum cleaner, coffee machine, etc.
-- Orders: different customers buying these items on different dates
```


```
┌─────────────────┐         ┌─────────────────┐
│     ITEMS       │         │     ORDERS      │
├─────────────────┤         ├─────────────────┤
│ id (PK)         │◄────────┤ id (PK)         │
│ name            │    │    │ customer_name   │
│ unit_price      │    │    │ order_date      │
│ quantity        │    │    │ item_id (FK)    │
└─────────────────┘    │    └─────────────────┘
                       │
                    One-to-Many
                 (One item can have 
                  many orders)
```
