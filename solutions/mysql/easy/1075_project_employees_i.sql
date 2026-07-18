/*
Problem ID : 1075
Title      : Project Employees I
Language   : Python
Solved Date: 2026-07-19
*/
select P.project_id,round(avg(E.experience_years),2) as average_years from Project P,Employee E where P.employee_id=E.employee_id group by P.project_id;