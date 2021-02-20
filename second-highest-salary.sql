# Write your MySQL query statement below
# select distinct Salary as SecondHighestSalary from Employee order by Salary desc
# limit 1 offset 1

select max(Salary) as SecondHighestSalary from Employee where Salary < (Select MAX(Salary) from Employee)
