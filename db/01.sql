CREATE DATABASE scalable;
use scalable;
create table if not exists users
(
    user_id   serial primary key,
    user_name varchar(255) not null unique,
    user_pass varchar(255) not null
);

create table if not exists cart
(
    cart_id        serial
        primary key,
    user_id        integer not null,
    product_id     integer not null,
    order_quantity integer not null
);

INSERT INTO users (user_name, user_pass)
VALUES ('john_doe', 'password123'),
       ('jane_smith', 'secretpass');

INSERT INTO producttable (product_name, product_price, product_quantity)
VALUES ('T-Shirt', 19.99, 100),
       ('Coffee Mug', 9.95, 50);

INSERT INTO ordertable (user_id, product_id, order_quantity, order_price, total_price)
SELECT 1, 1, 2, 40, 40  -- Assuming user_id 1 and product_id 1 exist
FROM producttable
WHERE product_id = 1;