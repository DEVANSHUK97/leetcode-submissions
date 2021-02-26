# Write your MySQL query statement below
select
D.Name as Department, E.Name as Employee, F.Salary as Salary
from
Employee E, Department D, (select Max(Salary) as Salary, DepartmentId from Employee group by DepartmentId) F
where
E.DepartmentId = D.Id and D.Id = F.DepartmentId and E.Salary = F.Salary
