USE SQL_PRACTICE;
SELECT * FROM CUSTOMERS;
SELECT * FROM DEPARTMENTS;
SELECT * FROM EMPLOYEES;
SELECT * FROM LOGS;
SELECT * FROM ORDER_ITEMS;
SELECT * FROM ORDERS;
SELECT * FROM PRODUCTS;
SELECT * FROM SUPPLIERS;

-- SELECT, INSERT, DELETE, UPDATE

-- Select all columns from the employees table.
SELECT * FROM EMPLOYEES;

-- Select only name, salary, and city from employees.
SELECT NAME, SALARY, CITY FROM EMPLOYEES;

-- Insert a new department: dept_id=9, dept_name='Data Science', budget=500000, location='Bangalore', head_id=NULL.
INSERT INTO DEPARTMENTS(DEPT_ID, DEPT_NAME, BUDGET, LOCATION, HEAD_ID)
VALUES (9, 'Data Science', 500000, 'Bangalore', NULL);

-- Insert a new employee: emp_id=41, name='Riya Kapoor', dept_id=1, manager_id=3, 
salary=125000, hire_date='2023-05-15', job_title='Engineer', city='Bangalore'.
INSERT INTO EMPLOYEES(EMP_ID, NAME, DEPT_ID, MANAGER_ID,SALARY,HIRE_DATE,JOB_TITLE,
    CITY) VALUES (41, "Riya Kapoor", 1, 3, 125000, "2023-05-15","Engineer","Bangalore");

-- Update the salary of emp_id=4 to 135000.
UPDATE EMPLOYEES SET SALARY = 150000 WHERE EMP_ID = 4;

-- Update the location of dept_id=3 to 'Mumbai'.
UPDATE DEPARTMENTS SET LOCATION = 'MUMBAI' WHERE DEPT_ID = 3;

-- Delete the employee with emp_id=41 (the one you just inserted).
DELETE FROM EMPLOYEES WHERE EMP_ID = 41;

-- Delete all orders with status='Cancelled'.
DELETE FROM ORDERS WHERE STATUS = "CANCELLED";

-- Update all employees in dept_id=7 (Support) with a 5% salary raise.


-- Select all products where stock_qty is NULL.