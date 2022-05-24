-- Answer to question 1 which is 2 Wahlbergs
select last_name
from actor
where last_name like 'Wahlberg'

-- Answer to question 2 which is 5560
select amount
from payment
where amount between 3.99 and 5.99;

-- Answer to question 3 which is 9
select film_id, count(film_id)
from inventory
group by film_id
order by film_id;

-- Answer to question 4 which is 0 (assuming it's customer table)
select last_name from customer
where last_name like 'William';

-- Answer to question 5 which is 1-8040
select staff_id, count(staff_id)
from rental
group by staff_id
order by staff_id

-- Answer to question 6 which is ??
select * from city

-- Answer to question 7 which is film 508, 16 actors
select film_id, count(actor_id)
from film_actor
group by film_id
order by film_id

-- Answer to question 8 which is 13
--select * from customer
select count(last_name), store_id
from customer
where last_name like '%es'
group by store_id 
having store_id = 1

-- Answer to question 9 which is 3
select amount, count(amount)
from payment
where customer_id between 380 and 430
group by amount
having count(rental_id) > 250

-- Answer to question 10 which is 5 ratings with PG-13 having the most.
select rating, count(rating)
from film
group by rating

