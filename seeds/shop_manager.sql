DROP TABLE IF EXISTS items_orders;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS items;

CREATE TABLE items (
id SERIAL PRIMARY KEY,
name VARCHAR,
unit_price INT,
quantity INT
);




CREATE TABLE orders (
id SERIAL PRIMARY KEY,
customer_name VARCHAR
);





CREATE TABLE items_orders (
item_id INT,
order_id INT,
CONSTRAINT fk_item FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE,
CONSTRAINT fk_order FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
PRIMARY KEY (item_id, order_id)
);