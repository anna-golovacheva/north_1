CREATE TABLE employees
(
employee_id serial PRIMARY KEY,
first_name varchar(20),
last_name varchar(20),
title varchar(100),
birth_date date,
notes varchar(600)
);

CREATE TABLE customers_data
(
customer_id varchar(6) PRIMARY KEY,
company_name varchar(50),
contact_name varchar(50)
);

CREATE TABLE orders_data
(
order_id int PRIMARY KEY,
customer_id varchar(50) REFERENCES customers_data(customer_id),
employee_id int REFERENCES employees(employee_id),
order_date date,
ship_city varchar(30)
);

