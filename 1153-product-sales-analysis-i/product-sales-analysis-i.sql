# Write your MySQL query statement below
select p.product_name,s.year,s.price
from sales s
INNER JOIN PRODUCT P
WHERE p.product_id=s.product_id;