Q1 - Show the difference between ROW_NUMBER(), RANK(), and DENSE_RANK() using the employees table, ordered by salary descending.

SELECT name, department,salary,
ROW_NUMBER() OVER(ORDER BY salary) AS row_number,
RANK() OVER(ORDER BY salary) AS rank,
DENSE_RANK() OVER(ORDER BY salary) AS dense_rank
FROM employees


Q2 - Rank employees by salary within each department. Use all three — ROW_NUMBER, RANK, DENSE_RANK.

SELECT name, department, salary,
ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS roww_number,
RANK() OVER(PARTITION BY department ORDER BY salary DESC)AS rank,
DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) as dense_rank
FROM employees

Q3 - Find the top 1 highest paid employee in each department using RANK().

SELECT * FROM (SELECT name, department,salary,
RANK() OVER(PARTITION BY department ORDER BY salary) AS TOP_rank
FROM employees) WHERE TOP_rank = 1;


Q4 - Using LEAD() and LAG(), show each month's sales amount along with the previous and next month's amount.

SELECT month, amount, 
LAG(amount) OVER(ORDER BY month) AS last_amount,
LEAD(amount) OVER(ORDER BY month) AS next_amount
FROM sales

Q5 - Show the running total of orders region by region, ordered by date.

SELECT region, amount, order_date,
SUM(amount) OVER(PARTITION BY region ORDER by order_date) AS running_total
FROM orders

Q6 - Rank customers by order amount within their region.

SELECT customer,amount, 
RANK() OVER(PARTITION BY region ORDER BY amount) as rnk
FROM orders

Q7 - Show each orders amount along with the previous and next order amount within the same region.

SELECT region, amount,
LAG(amount) OVER(PARTITION BY region ORDER BY order_date) as previous_order,
LEAD(amount) OVER(PARTITION BY region ORDER BY order_date) AS next_order
FROM orders

Q8 - Find the highest order amount per region, shown alongside every row.

SELECT *, MAX(amount)
OVER(PARTITION BY region) AS Highest_Amount
FROM orders


Q9 - Show each orders amount and the difference between that order and the previous order in the same region.

SELECT region, amount,
LAG(amount) OVER(PARTITION BY region ORDER BY order_date) AS previous_amount,
amount - LAG(amount) OVER(PARTITION BY region ORDER BY order_date) AS diffrence
FROM orders


Q10 -  find the top 2 orders by amount in each region.

SELECT * FROM(SELECT region, amount,
RANK() OVER(PARTITION BY region ORDER BY amount DESC) AS rnk
FROM orders) WHERE rnk <=2

Q11 - Show each customer, their amount, and what percentage their order is of the total region sales.

SELECT customer, amount, region, 
SUM(amount) OVER(PARTITION BY region) AS total_sales,
amount*100 / SUM(amount) OVER(PARTITION BY region) AS percentage 
FROM orders


