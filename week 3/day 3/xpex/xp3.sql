-- SELECT * FROM language

-- SELECT 
-- film.title AS film_title,
-- film.description AS film_description,
-- language.name AS language_name
-- FROM film
-- JOIN language
-- ON film.language_id = language.language_id;


-- SELECT 
-- film.title AS film_title,
-- film.description AS film_description,
-- language.name AS language_name
-- FROM language LEFT JOIN film
-- ON film.language_id = language.language_id;

-- CREATE TABLE new_film (
--     new_fimid SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (name)
-- VALUES 
-- ('When Harry Met Sally'), 
-- ('Interstellar'), 
-- ('The Notebook');

-- CREATE TABLE customer_review (
--     review_id SERIAL PRIMARY KEY,         
--     film_id INT NOT NULL,                  
--     language_id INT NOT NULL,             
--     title VARCHAR(255) NOT NULL,           
--     score INT CHECK (score >= 1 AND score <= 10),  
--     review_text TEXT,                     
--     last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
--     FOREIGN KEY (film_id) REFERENCES new_film 
--         ON DELETE CASCADE,               
--     FOREIGN KEY (language_id) REFERENCES language(language_id)  
-- );

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES 
-- (1, 1, 'Great Movie', 9, 'I loved this film. The plot and acting were amazing!'),
-- (2, 1, 'Not Bad', 7, 'Good film but could use some improvements in pacing.');

-- INSERT INTO new_film (name) VALUES ('The Matrix');
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (1, 1, 'Amazing!', 10, 'One of the best sci-fi movies ever.');

--DELETE FROM new_film WHERE new_fimid = 1;

--exercise 2
-- UPDATE film
-- SET language_id = 2 
-- WHERE film_id IN (1, 2); 
-- SELECT * FROM film WHERE film_id IN (1, 2);








