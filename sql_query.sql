#!/bin/python3

-- Creates
CREATE TABLE supplier (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR (255) NOT NULL,
    contact_name VARCHAR (255) NOT NULL,
    contact_phone VARCHAR (15) NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR (255) NOT NULL,
    list_price DECIMAL (10, 2) NOT NULL,
    supplier_id INT NOT NULL,
    quantity_in_stock INT NOT NULL,
    last_purchased_date TIMESTAMP
);

-- Inserts
INSERT INTO `supplier` (supplier_id, supplier_name, contact_name, contact_phone)
VALUES
(1, 'Oscar', 'Orellana', '300123456'),
(2, 'Raquel', 'Godina', '300123457'),
(3, 'Robert', 'Tzeker', '300123458'),
(4, 'Viviana', 'Merlo', '300123459'),
(5, 'Lizeth', 'Echevarri', '300123450');

INSERT INTO `products` (product_id, product_name, list_price, supplier_id, quantity_in_stock, last_purchased_date)
VALUES
(1, 'Ordenador', 1100.50, 1, 1000, NULL),
(2, 'Tablet', 200.00, 1, 1000, NULL),
(3, 'Iphone 11', 600.00, 1, 1000, NULL),
(4, 'Windows 12', 150.00, 3, 1000, NULL),
(5, 'Paquete Office', 60.00, 4, 1000, NULL);

-- Create a SQL statement for an inventory of the products in stock, with
--     the name of the supplier
--     number of different products it supplies
--     total of products in stock that it supplies
SELECT supplier.supplier_name as `Name`, COUNT(DISTINCT product_id) as `Number of products`, SUM(quantity_in_stock) as `Total stock`
FROM products
INNER JOIN supplier ON products.supplier_id=supplier.supplier_id
GROUP BY supplier.supplier_id;


