# Write your MySQL query statement below
select c.id,c.movie,ci.description,ci.rating 
from cinema  c
join cinema ci
on c.id=ci.id
where c.id%2=1 and ci.description !='boring'
order by c.rating DeSC;