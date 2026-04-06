Q1 - Calculate the running total of sales month by month.

SELECT month, amount, SUM(amount) 
OVER (ORDER BY month) AS running_total
FROM sales;

Q2 - Find the salary difference between an employee and the average salary of their department.

SELECT name, department,salary,
AVG(salary) OVER(PARTITION BY department) AS department_AVG,
salary - AVG(salary) OVER(PARTITION BY department) as difference
FROM employees

Q3 - What is the difference between ROW_NUMBER() and RANK()?

ROW_NUMBER :- it is used to assign unique numbers to each rows based on the order the user wants to define them 

EG:-  name	salary	ROW_NUMBER
        A   300      1          
        B	200	     2	      
        C	200	     3 ❗	   
        D	100	     4          
        
        gives all the rows unique numbers even if the rows are same

RANK() :- Rank is used to assign same number to EQUAL values(tie),
but it skips the next number  or rank only if there is a tie

EG:-  name	salary	RANK
        A   300       1
        B	200	      2
        C	200	      2 ❗
        D	100	      4 ❗

    skips the number or rank after the tie 

    