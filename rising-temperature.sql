# Write your MySQL query statement below
select distinct t1.id as id
from Weather t1, Weather t2
where DATEDIFF(t1.Recorddate,t2.Recorddate) = 1
and t1.Temperature > t2.Temperature
