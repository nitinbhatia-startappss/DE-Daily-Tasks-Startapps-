Q1 — Find departments where the average salary is higher than the company-wide average salary.

SELECT department, AVG(salary)
FROM employees
GROUP by department
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees)employees)


Q2 - Find the top 3 products by total revenue in each region.

WITH regional_revenue AS (
    SELECT p.name, s.region, SUM(s.revenue) AS total_revenue
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY p.name, s.region
),
ranked AS (
    SELECT name, region, total_revenue,
           RANK() OVER (PARTITION BY region ORDER BY total_revenue DESC) AS rnk
    FROM regional_revenue
)
SELECT * FROM ranked
WHERE rnk <= 3;

Q3 - Find regions where the total revenue is higher than the average total revenue across all regions.

WITH region_total AS(
    SELECT region, SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY region
)
SELECT region, total_revenue
FROM region_total
WHERE total_revenue > (SELECT AVG(total_revenue)
                        FROM region_total)


Q4 - Find the highest paid employee in each department.

WITH ranked AS (
    SELECT name, department,salary, 
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS
    rnk FROM employees
)
SELECT name, department, salary
FROM ranked
WHERE rnk = 1;


