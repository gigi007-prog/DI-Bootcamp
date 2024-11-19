--CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

--SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )


-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)

-- SELECT * FROM SecondTab

-- Q1. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- output will be 0

-- Q2. What will be the OUTPUT of the following statement?
--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- the ouput will be 3 because it would count the three ids and stopp at null

-- Q3. What will be the OUTPUT of the following statement?
--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- output will be 0

-- Q4. What will be the OUTPUT of the following statement?
--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- output will be 3 
