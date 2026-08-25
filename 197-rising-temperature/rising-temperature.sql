# Write your MySQL query statement below
select w.id as id
from weather w
join weather wm
where Datediff(w.recordDate,wm.recordDate)=1
AND w.temperature>wm.temperature; 