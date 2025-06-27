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
customer_name VARCHAR,
order_date DATE
);


CREATE TABLE items_orders (
item_id INT,
order_id INT,
CONSTRAINT fk_item FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE,
CONSTRAINT fk_order FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE,
PRIMARY KEY (item_id, order_id)
);

-- Insert fake pet shop items
INSERT INTO items (name, unit_price, quantity) VALUES ('Squeaky Bone Toy', 5, 50);
INSERT INTO items (name, unit_price, quantity) VALUES ('Catnip Mouse', 3, 100);
INSERT INTO items (name, unit_price, quantity) VALUES ('Premium Dog Food - Beef', 25, 30);
INSERT INTO items (name, unit_price, quantity) VALUES ('Tropical Fish Flakes', 7, 40);
INSERT INTO items (name, unit_price, quantity) VALUES ('Hamster Wheel', 15, 10);
INSERT INTO items (name, unit_price, quantity) VALUES ('Bird Seed Mix', 8, 25);
INSERT INTO items (name, unit_price, quantity) VALUES ('Rabbit Hutch Straw', 6, 15);
INSERT INTO items (name, unit_price, quantity) VALUES ('Flea Collar - Large', 12, 20);
INSERT INTO items (name, unit_price, quantity) VALUES ('Tennis Ball Pack (3)', 10, 35);
INSERT INTO items (name, unit_price, quantity) VALUES ('Aquarium Castle Decoration', 18, 5);


-- Insert fake pet shop orders
INSERT INTO orders (customer_name, order_date)VALUES('Charlie Barkington', '2025-06-10');
INSERT INTO orders (customer_name, order_date)VALUES('Mittens Whiskers', '2025-06-11');
INSERT INTO orders (customer_name, order_date)VALUES('Goldie Finley', '2025-06-12');
INSERT INTO orders (customer_name, order_date)VALUES('Hopper McFluff', '2025-06-12');
INSERT INTO orders (customer_name, order_date)VALUES('Polly Crackers', '2025-06-13');
INSERT INTO orders (customer_name, order_date)VALUES('Rex Von Woof', '2025-06-14');
INSERT INTO orders (customer_name, order_date)VALUES('Flopsy Bunbun', '2025-06-14');
INSERT INTO orders (customer_name, order_date)VALUES('Captain Meow', '2025-06-15');
INSERT INTO orders (customer_name, order_date)VALUES('Spike Tailspin', '2025-06-16');
INSERT INTO orders (customer_name, order_date)VALUES('Bubbles Swimmy', '2025-06-16');

-- Insert data linking items to orders
INSERT INTO items_orders (item_id, order_id) VALUES(1, 1);  -- Charlie Barkington ordered a Squeaky Bone Toy
INSERT INTO items_orders (item_id, order_id) VALUES(3, 1);  -- Charlie Barkington ordered Premium Dog Food - Beef
INSERT INTO items_orders (item_id, order_id) VALUES(9, 1);  -- Charlie Barkington ordered Tennis Ball Pack (3)

INSERT INTO items_orders (item_id, order_id) VALUES(2, 2);  -- Mittens Whiskers ordered a Catnip Mouse
INSERT INTO items_orders (item_id, order_id) VALUES(4, 2);  -- Mittens Whiskers ordered Tropical Fish Flakes

INSERT INTO items_orders (item_id, order_id) VALUES(4, 3);  -- Goldie Finley ordered Tropical Fish Flakes
INSERT INTO items_orders (item_id, order_id) VALUES(10, 3); -- Goldie Finley ordered Aquarium Castle Decoration

INSERT INTO items_orders (item_id, order_id) VALUES(5, 4);  -- Hopper McFluff ordered a Hamster Wheel
INSERT INTO items_orders (item_id, order_id) VALUES(7, 4);  -- Hopper McFluff ordered Rabbit Hutch Straw

INSERT INTO items_orders (item_id, order_id) VALUES(6, 5);  -- Polly Crackers ordered Bird Seed Mix

INSERT INTO items_orders (item_id, order_id) VALUES(1, 6);  -- Rex Von Woof ordered a Squeaky Bone Toy
INSERT INTO items_orders (item_id, order_id) VALUES(3, 6);  -- Rex Von Woof ordered Premium Dog Food - Beef
INSERT INTO items_orders (item_id, order_id) VALUES(8, 6);  -- Rex Von Woof ordered Flea Collar - Large

INSERT INTO items_orders (item_id, order_id) VALUES(7, 7);  -- Flopsy Bunbun ordered Rabbit Hutch Straw

INSERT INTO items_orders (item_id, order_id) VALUES(2, 8);  -- Captain Meow ordered a Catnip Mouse

INSERT INTO items_orders (item_id, order_id) VALUES(9, 9);  -- Spike Tailspin ordered Tennis Ball Pack (3)

INSERT INTO items_orders (item_id, order_id) VALUES(4, 10); -- Bubbles Swimmy ordered Tropical Fish Flakes
INSERT INTO items_orders (item_id, order_id) VALUES(10, 10);-- Bubbles Swimmy ordered Aquarium Castle Decoration