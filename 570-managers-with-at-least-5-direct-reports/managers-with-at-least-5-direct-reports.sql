# Write your MySQL query statement below
select e.name
from employee as e 
join employee as em
on e.id =em.managerId
group by em.managerId
having count(em.managerId)>=5;