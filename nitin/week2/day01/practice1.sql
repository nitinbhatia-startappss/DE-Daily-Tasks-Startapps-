# Q1 — Find all customers who have never placed an order
You have two tables: customers and orders.
A customer who has never ordered will not have a matching row in the orders table.


SELECT name FROM customers
left join orders on customers.id = orders.customer_id
where orders.total IS NULL;


# Q2 Get the names of all customers along with their order totals. Customers with no orders should also appear.

SELECT name,total FROM customers
LEFT join orders
on customers.id = orders.customer_id


# Q3 Find the total amount spent by each customer. Show their name and the sum of their orders.

SELECT name, SUM(total) AS total_sum
FROM customers
LEFT JOIN orders
on customers.id = orders.customer_id
GROUP by name


# Q4. Get all unique names combined from both customers and premium_customers.

SELECT name FROM customers
UNION
SELECT name from premium_customers


# Q5. Find customers who have placed more than one order. Show their name and order count.

SELECT name, COUNT(total) FROM customers
LEFT JOIN orders
on customers.id = orders.customer_id
GROUP by name
HAVING COUNT(total) > 1


# Q6. Get all names from both customers and premium_customers keeping duplicates, but only show names that start with the letter 'A' or 'C'.

SELECT name FROM customers
where name like 'A%'OR name LIKE 'C%'
UNION ALL
SELECT name FROM premium_customers
where name like 'A%'OR name LIKE 'C%'

# Q7. Find the customer who has spent the most money in total. Show their name and total amount spent.

SELECT name, sum(total) AS total_sum
FROM customers
left JOIN orders 
on customers.id = orders.customer_id
GROUP BY name
order by total_sum DESC
LIMIT 1

# Q8. Find all customers who have placed exactly one order.

SELECT name from customers
LEFT JOIN orders
on customers.id = orders.customer_id
GROUP by name
HAVING COUNt(orders.id) = 1;

# Q9. Get the names of customers who are in both customers and premium_customers tables.

SELECT name FROM customers
INTERSECT 
SELECT name FROM premium_customers

# Q10. Show each customers name and their number of orders. Include customers with zero orders and show 0 instead of NULL for them.

SELECT name, COALESCE(COUNT(orders.id), 0) AS total_orders from customers
left JOIN orders
on customers.id = orders.customer_id
GROUP by name



