# Write your MySQL query statement below
delete p1.* from Person p1, person p2 where
p1.Id > p2.Id and
p1.Email = p2.Email
