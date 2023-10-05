-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name text NOT NULL,
	last_name text NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers
(
    customer_id varchar(10) PRIMARY KEY,
    company_name varchar(40) NOT NULL,
	contact_name text NOT NULL
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(10) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date NOT NULL,
	ship_city text NOT NULL
)
