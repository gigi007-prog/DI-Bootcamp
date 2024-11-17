--THIS IS A COMMENT
-- CREATE TABLE actors(
-- actor_id SERIAL PRIMARY KEY,
-- first_namem VARCHAR(50) NOT NULL,
-- last_name VARCHAR(50) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL)

 

-- INSERT INTO actors(first_namem, last_name, age, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5)

 -- INSERT INTO actors(first_namem, last_name, age, number_oscars)
 -- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_namem, last_name, age, number_oscars)
-- VALUES ('Scarlett', 'Johansson', '11/22/1984', 1)



--SELECT * FROM actors


-- INSERT INTO actors (first_namem, last_name, age, number_oscars)
-- VALUES ('Brad', 'Pitt', '10/08/1970', 3)

-- SELECT last_name, number_oscars FROM actors WHERE number_oscars>2 ORDER BY number_oscars DESC

-- UPDATE actors
-- SET first_namem='Angelina',
-- last_name='Jolie'
-- WHERE first_namem='Brad';

-- DELETE FROM actors
-- WHERE first_namem ='George' 

-- SELECT COUNT(*) AS total_actors
-- FROM actors

-- INSERT INTO actors (first_namem, last_name, age, number_oscars)
-- VALUES('Daisy','','','')
-- we cant run this it shows syntax error because when we created the table we specified that it is no null