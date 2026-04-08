import sys
import os
from sqlalchemy import text

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_setup import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def run_query(query, title):
    print(f"\n🔹 {title}")
    result = session.execute(text(query))
    for row in result:
        print(row)


# 1. Month-over-Month Growth

query1 = """
WITH monthly_sales AS (
    SELECT 
        strftime('%Y-%m', order_date) AS month,
        SUM(quantity * price) AS total_sales
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    GROUP BY month
),
growth AS (
    SELECT 
        month,
        total_sales,
        LAG(total_sales) OVER (ORDER BY month) AS prev_month_sales
    FROM monthly_sales
)
SELECT 
    month,
    total_sales,
    ROUND(
        (total_sales - prev_month_sales) * 100.0 / prev_month_sales, 
        2
    ) AS growth_percentage
FROM growth;
"""

# 2. Top 3 Customers per Month

query2 = """
WITH customer_monthly AS (
    SELECT 
        strftime('%Y-%m', o.order_date) AS month,
        c.name,
        SUM(oi.quantity * oi.price) AS total_spent
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    GROUP BY month, c.name
),
ranked AS (
    SELECT *,
        DENSE_RANK() OVER (
            PARTITION BY month 
            ORDER BY total_spent DESC
        ) AS rank
    FROM customer_monthly
)
SELECT *
FROM ranked
WHERE rank <= 3;
"""

# 3. Avg Time Between Orders

query3 = """
WITH ranked_orders AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY order_date
        ) AS rn
    FROM orders
),
first_second AS (
    SELECT 
        a.customer_id,
        a.order_date AS first_order,
        b.order_date AS second_order
    FROM ranked_orders a
    JOIN ranked_orders b 
        ON a.customer_id = b.customer_id
    WHERE a.rn = 1 AND b.rn = 2
)
SELECT 
    AVG(
        julianday(second_order) - julianday(first_order)
    ) AS avg_days_between_orders
FROM first_second;
"""


run_query(query1, "Month-over-Month Growth")
run_query(query2, "Top 3 Customers Per Month")
run_query(query3, "Average Time Between Orders")