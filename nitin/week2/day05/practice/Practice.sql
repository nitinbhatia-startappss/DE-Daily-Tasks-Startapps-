Q1 - What is the total sales per month?

SELECT strftime('%Y-%m', order_date) as month,
SUM(oi.quantity * oi.price) AS total_sales
FROM order_items oi
JOIN orders o
on oi.order_id = o.id
GROUP BY month
ORDER BY month ASC

Q2 - Show each months sales alongside the previous months sales using LAG.

with monthly_sales AS (SELECT strftime('%Y-%m', order_date) as month,
SUM(oi.quantity * oi.price) as total_sales
FROM order_items oi JOIN orders o 
on o.id = oi.order_id
GROUP BY month
order by month ASC)
SELECT month , total_sales,
LAG(total_sales) OVER(order by month) AS last_month_sales
FROM monthly_sales

Q3 — top 3 customers by total sales overall

SELECT name,
SUM(oi.quantity * oi.price) as total_sales
FROM customers c
JOIN orders o 
on c.id = o.customer_id
JOIN order_items oi 
on o.id = oi.order_id
GROUP BY c.name
order by total_sales DESC
limit 3

Q4 — same thing but top 3 customers per month.

WITH top_G AS (
    SELECT name, strftime('%Y-%m', order_date) AS month,
    SUM(oi.quantity * oi.price) AS total_sales
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    GROUP BY c.name, month
),
ranked AS (
    SELECT month, name, total_sales,
        DENSE_RANK() OVER(PARTITION BY month ORDER BY total_sales DESC) AS rnk
    FROM top_G
)
SELECT month, name, total_sales, rnk
FROM ranked
WHERE rnk <= 3
ORDER BY month, rnk






