-- CREATE TABLE items(
-- items_id SERIAL PRIMARY KEY, 
-- item_name VARCHAR (100) NOT NULL,
-- item_price DECIMAL (10,2) NOT NULL
-- );


-- INSERT INTO items (item_name, item_price)
-- VALUES 
-- ('small desk', 100),
-- ('large desk', 300),
-- ('fan', 80);

-- CREATE TABLE customers(
-- customers_id SERIAL PRIMARY KEY,
-- customers_fname VARCHAR (50),
-- customers_lname VARCHAR (50)
-- );

-- INSERT INTO customers (customers_fname,customers_lname)
-- VALUES
-- ('Greg', 'Jones'),
-- ('Sandra','Jones'),
-- ('Scott','Scott'),
-- ('Trevor','Green'),
-- ('Melanie','Johnson');

-- SELECT * FROM customers

-- SELECT * FROM items WHERE item_price>80;

-- SELECT * FROM items WHERE item_price<=300;

-- SELECT * FROM customers WHERE customers_lname='Smith';
-- there is no one with the last name of smith so it will print only the fields

-- SELECT * FROM customers WHERE customers_lname='Jones';

--SELECT * FROM customers WHERE customers_fname!='Scott';

--SELECT * FROM items ORDER BY item_price ASC;

--SELECT * FROM items ORDER BY item_price DESC;

--SELECT customers_fname, customers_lname FROM customers ORDER BY customers_fname ASC LIMIT 3;

--SELECT customers_lname FROM customers ORDER BY customers_lname DESC 