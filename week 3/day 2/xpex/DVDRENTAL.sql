--SELECT * FROM customer

--SELECT first_name || ' ' || last_name AS full_name FROM customer;

--SELECT DISTINCT create_date FROM customer;

--SELECT * FROM customer ORDER BY first_name DESC;

--SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;

--SELECT address, phone FROM address WHERE district='Texas';

--SELECT * FROM film WHERE film_id IN (15,150);

--SELECT film_id, title, description, length, rental_rate FROM film WHERE title='Interstellar'

--SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE 'In%';

--SELECT * FROM film ORDER BY rental_rate ASC LIMIT 10;

--SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
--FROM customer
--JOIN payment ON customer.customer_id = payment.customer_id
--ORDER BY customer.customer_id ASC;

--SELECT film.film_id, film.title FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.film_id IS NULL;

--SELECT city.city, country.country FROM city JOIN country ON city.country_id = country.country_id;


