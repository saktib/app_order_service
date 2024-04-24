use testdb;

INSERT INTO users (user_name, user_pass)
VALUES ('john_doe', 'password123'),
       ('jane_smith', 'secretpass');

INSERT INTO product (product_name, product_price, product_quantity)
VALUES ('T-Shirt', 19.99, 100),
       ('Coffee Mug', 9.95, 50);

INSERT INTO order (user_id, product_id, order_quantity, order_price, total_price)
SELECT 1, 1, 2, 40, 40  -- Assuming user_id 1 and product_id 1 exist
FROM product
WHERE product_id = 1;