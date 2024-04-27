-- Create a new database
CREATE DATABASE
IF NOT EXISTS book_boutique;

-- Grant privileges to a user
GRANT ALL PRIVILEGES ON *.* TO 'user'@'%'
WITH
GRANT OPTION;

-- Flush privileges
FLUSH PRIVILEGES;

INSERT INTO user (user_name, user_pass)
VALUES ('john_doe', 'password123'),
       ('jane_smith', 'secretpass');

INSERT INTO products (product_name, product_price, product_quantity)
VALUES ('T-Shirt', 19.99, 100),
       ('Coffee Mug', 9.95, 50);

INSERT INTO orders (user_id, product_id, order_quantity, order_price, total_price)
SELECT 1, 1, 2, 40, 40  -- Assuming user_id 1 and product_id 1 exist
FROM products
WHERE product_id = 1;