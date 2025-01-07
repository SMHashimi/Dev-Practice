SELECT * FROM books;
SELECT title FROM books WHERE title LIKE "%stories%";
SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1;
SELECT CONCAT(title, "-", released_year) AS summary FROM books ORDER BY released_year DESC LIMIT 3;
SELECT title, author_lname FROM books WHERE author_lname LIKE "% %";
SELECT title, released_year, stock_quantity FROM books ORDER BY stock_quantity ASC LIMIT 3;
SELECT author_lname, COUNT(*) FROM books GROUP BY author_lname;
SELECT released_year FROM books;
SELECT released_year, COUNT(*) FROM books GROUP BY released_year;
SELECT COUNT(*) FROM books;
SELECT MIN(pages) FROM books;
SELECT MAX(released_year) FROM books;
SELECT MIN(author_lname) FROM books;
SELECT MIN(author_lname), MAX(author_lname) FROM books;
SELECT title, pages FROM books ORDER BY pages DESC;
SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1;
SELECT title, pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);
SELECT title, pages FROM books WHERE pages = 634;
SELECT MIN(released_year) FROM books;
SELECT title, released_year FROM books WHERE released_year = (SELECT MIN(released_year) FROM books);
SELECT author_fname, author_lname FROM books;
SELECT author_fname, author_lname FROM books ORDER BY author_lname;
SELECT CONCAT(author_fname, " ", author_lname) AS author, COUNT(*) FROM books GROUP BY author;
SELECT author_lname, MAX(released_year), MIN(released_year) FROM books GROUP BY author_lname;
SELECT
    author_lname,
    COUNT(*) AS books_written,
    MAX(released_year) AS earliest_release,
    MIN(released_year)
FROM books GROUP BY author_lname;
SELECT
    author_lname,
        author_fname,
    COUNT(*) AS books_written,
    MAX(released_year) AS latest_release,
    MIN(released_year) AS earliest_release
FROM books GROUP BY author_lname, author_fname;
SELECT SUM(pages) FROM books;
SELECT author_lname, SUM(pages) FROM books GROUP BY author_lname;
SELECT SUM(author_lname) FROM books;
SELECT AVG(pages) FROM books;
SELECT AVG(released_year) FROM books;
SELECT AVG(stock_quantity) FROM books;
SELECT released_year, AVG(stock_quantity) FROM books GROUP BY released_year;
-- Exercise 
SELECT COUNT(*) FROM books;
SELECT released_year, COUNT(*) FROM books GROUP BY released_year;
SELECT SUM(stock_quantity) FROM books;
SELECT author_fname, author_lname, AVG(released_year) FROM books GROUP BY author_fname, author_lname;
SELECT author_fname, author_lname, pages FROM books WHERE pages = (SELECT MAX(pages) FROM books);

-- Char vs VARCHAR;  CHAR  has fixed length
CREATE TABLE friends (name VARCHAR(10));
INSERT INTO friends (name)
    VALUES ("tom"), ("juan pablo"), ("james");
CREATE TABLE state(abbr CHAR(2));
INSERT INTO state(abbr)
    VALUES ("CA"), ("NY");
SELECT * FROM state;
SELECT * FROM parent;
INSERT INTO parent(children) VALUES (1.5);
SELECT * FROM parent;
CREATE TABLE products (price DECIMAL(5, 2));
SELECT * FROM products;
INSERT INTO products (price) VALUES(5.026);
SELECT * FROM products;
CREATE TABLE numbers (x FLOAT, y DOUBLE) ;
INSERT INTO numbers (x, y) VALUES (1.123, 1.123 );
INSERT INTO numbers (x, y) VALUES (1.123456, 1.123045678);
SELECT * FROM numbers;
-- DATE - YYYY-MM-DD OR YYYY-MM-DD HH:MM:SS
-- Working with DATES
CREATE TABLE people(
    name VARCHAR(50),
    birthdate DATE,
    birthtime TIME,
    birthdt DATETIME);
INSERT INTO people (name, birthdate, birthtime, birthdt)
    VALUES ("Lulu", "1997-04-11", "09:36:45", "1997-04-11 09:36:45");
INSERT INTO people (name, birthdate, birthtime, birthdt)
    VALUES ("Juan", "2020-08-11", "23:36:45", "2020-08-11 23:36:45");
SELECT * FROM people;
INSERT INTO people (name, birthdate, birthtime, birthdt)
    VALUES ("Hazel", CURDATE(), CURTIME(), NOW());
SELECT birthdate, YEAR(birthdate), DAY(birthdate), DAYOFWEEK(birthdate), DAYOFYEAR(birthdate), MONTHNAME(birthdate) FROM people;
-- Let's use the format "April 11 2000" instead of "2000-02-11"
SELECT CONCAT(MONTHNAME(birthdate), ", ", DAY(birthdate), ", ", YEAR(birthdate)) FROM people;
SELECT CURDATE() FROM people;
SELECT CURDATE(), birthdate, DATEDIFF(CURDATE(), birthdate) FROM people;
SELECT DATE_ADD(CURDATE(), INTERVAL 1 DAY);
SELECT DATE_SUB(CURDATE(), INTERVAL 1 MONTH);
-- Let's check if you are allowed to drink alcohol
SELECT name, birthdate, DATE_ADD(birthdate, INTERVAL 18 YEAR) FROM people;
CREATE TABLE captions (
    text VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO captions (text)
    VALUES ("Beautiful sunset");
INSERT INTO captions (text)
    VALUES ("just me and the girls chilling");
SELECT * FROM captions2;
UPDATE captions2 SET TEXT = "I love live!!!!!!!!" ;
SELECT * FROM captions2;
-- Logical Operators
-- For example, select all the books NOT published in 2017 or select all birthdays BETWEEN 1990 AND 1992
-- or select all the items that are in stock and priced below $19.99
SELECT * FROM books;
SELECT title, released_year FROM books WHERE released_year != "1981";
SELECT title FROM books WHERE title LIKE "% %";
SELECT title FROM books WHERE title NOT LIKE "% %";
SELECT * FROM books WHERE released_year >= 2016;
SELECT * FROM books WHERE released_year < 1985 ORDER BY released_year;
SELECT * FROM books WHERE author_lname = "Eggers";
SELECT * FROM books WHERE author_lname = "Eggers" AND released_year > 2010 AND title LIKE "%novel%";
SELECT title, pages FROM books WHERE CHAR_LENGTH(title) > 30 AND pages > 500;
SELECT 1 < 5 OR 45 = 234;
SELECT title, released_year FROM books WHERE released_year <= 2015 AND released_year >= 2004 ORDER BY released_year;
SELECT title, pages FROM books WHERE pages BETWEEN 200 AND 300 ORDER BY pages;
-- Comparing DATES
SELECT * FROM people;
-- Extract people born before 1999
SELECT * FROM people WHERE birthdate < "2005-01-01";
-- or
SELECT * FROM people WHERE YEAR(birthdate) < 2005;
SELECT * FROM people WHERE HOUR(birthtime) > 12;
SELECT CAST("09:00:00" AS TIME);
SELECT * FROM people WHERE birthtime BETWEEN "12:00:00" AND "16:00:00";
SELECT * FROM people WHERE HOUR(birthtime) BETWEEN 8 AND 20; 
SELECT title, author_lname FROM books WHERE author_lname = "Carver" OR author_lname = "Lahiri" OR author_lname = "Smith" ORDER BY author_lname;
-- IN
SELECT title, author_lname FROM books WHERE author_lname IN ("Carver", "Lahiri", "Smith") ORDER BY author_lname;
SELECT * FROM books;
SELECT title, released_year FROM books WHERE stock_quantity IN ("10", "154");
SELECT title, author_lname FROM books WHERE author_lname NOT IN ("Carver", "Lahiri", "Smith") ORDER BY author_lname;
-- %
SELECT 10 % 4;
SELECT title, released_year FROM books WHERE released_year >= 2000 AND released_year % 2 = 1;
SELECT title, released_year,
    CASE 
        WHEN released_year >= 1989 THEN "Young"
        ELSE "Old"
        END AS Genre
FROM books;
SELECT title, stock_quantity,
    CASE
        WHEN stock_quantity BETWEEN 0 AND 50 THEN "*"
        WHEN stock_quantity BETWEEN 51 AND 100 THEN "**"
        ELSE "***"
    END AS Stock
FROM books;
SELECT * FROM books;
SELECT author_fname, author_lname, COUNT(*) FROM books GROUP BY author_fname, author_lname;
SELECT author_fname, author_lname,
    CASE
        WHEN COUNT(*) = 1 THEN "1 Book"
        ELSE CONCAT(COUNT(*), " Books")
    END AS count
FROM books
WHERE author_lname IS NOT NULL
GROUP BY author_fname, author_lname;
--  MORE CONSTRAINTS
SELECT * FROM contacts;
SELECT * FROM users;
CREATE TABLE palindromes (
    word VARCHAR(100) CHECK(REVERSE(word) = word);
 INSERT INTO palindromes (word)
    VALUES ("racecar");
-- The below will create an error
 INSERT INTO palindromes (word)
    VALUES ("apple");
CREATE TABLE companies (
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    CONSTRAINT name_address UNIQUE(name, address)
    );
-- Consider the example of Saleprice and purchase price - as an your assignment
-- adding a column to an existing table 
ALTER TABLE companies
    ADD COLUMN phone VARCHAR(15);
ALTER TABLE companies
    ADD COLUMN employee_count INT NOT NULL;
SELECT * FROM companies;
-- Drop a column from a TABLE
ALTER TABLE companies
    DROP COLUMN employee_count;
-- Renaming a table in a
RENAME TABLE companies TO suppliers;
-- or
ALTER TABLE suppliers RENAME TO companies;
SELECT * FROM companies;
-- Renaming a column in a table
SELECT * FROM companies;
ALTER TABLE companies
    RENAME COLUMN name TO Name;
 ALTER TABLE companies
    RENAME COLUMN address TO Address;
-- Modification in a TABLE
ALTER TABLE companies
    MODIFY Name VARCHAR(100);
ALTER TABLE companies
    MODIFY Name VARCHAR(120);
-- One to Many Relationships
-- For example, a teacher can have multiple students. Each student has only one teacher
-- Or, an order is placed by one person.
-- Foreign key is a references to another table within a given table
SHOW DATABASES;
USE chicken_coop;
SELECT DATABASE();
DESC orders;
DESC customers;
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50)
    );
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_data DATE,
    amount DECIMAL(8,2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE);
INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016-02-10', 99.99, 1),
       ('2017-11-11', 35.50, 1),
       ('2014-12-12', 800.67, 2),
       ('2015-01-03', 12.50, 2),
       ('1999-04-11', 450.25, 5);
SELECT id FROM customers WHERE last_name = "George";
SELECT * FROM orders WHERE customer_id = 1;
-- Cross Joins or Cartesian Join - In this join, every single row from a table (customers) is combined with another table row (orders)
SELECT * FROM  orders WHERE customer_id = (SELECT id FROM customers WHERE last_name = "George");
-- Another way to exemplify it
SELECT * FROM customers, orders;
-- INNER JOINS - Finding overlap between columns of tables. In our case, the customere ID and the order's customer_id is the same
USE shop;
SELECT first_name, last_name, order_date, amount, customer_id FROM customers
    JOIN orders ON orders.customer_id = customers.id;
-- INNER JOIN; GROUP BY; Finding the total purchase by each customer
SELECT first_name, last_name, SUM(amount) AS total FROM customers
    JOIN orders ON orders.customer_id = customers.id
    GROUP BY first_name, last_name
    ORDER BY total;
-- LEFT JOIN; customers as our left table and orders as our right table - we are going to take every single row from the left side, every row from customers
-- and then if there is any corresponding order data, we will join that, but if not, we wil have a bunch of NULLS 
-- As a conclusion, everything from the left side and then any overlap from the right side - Customers who have not bought anything 
SELECT first_name, last_name, order_date, amount FROM customers
    LEFT JOIN orders ON orders.customer_id = customers.id;
-- LEFT JOIN; GROUP BY; Finding the total purchase by each customer
SELECT first_name, last_name, IFNULL(SUM(amount), 0) AS total_spent FROM customers
    LEFT JOIN orders ON orders.customer_id = customers.id
    GROUP BY first_name, last_name
    ORDER BY total_spent;
-- RIGHT JOIN - It is impossible 
SELECT first_name, last_name, IFNULL(SUM(amount), 0) AS total_spent FROM customers
    RIGHT JOIN orders ON orders.customer_id = customers.id
    GROUP BY first_name, last_name
    ORDER BY total_spent;
-- DELETION OF A CUSTOMER - CASCADE
-- We cannot delete a customer directly from the customers table because the customers has order in the orders table.
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_data DATE,
    amount DECIMAL(8,2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE);
-- MANY TO MANY RELATIONSHIPS - Consider REVIEWERS, REVIEWER, and SERIES Tables
CREATE TABLE reviewers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
    );
CREATE TABLE series (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    released_year YEAR,
    genre VARCHAR(100)
    );
CREATE TABLE reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(2, 1),
    series_id INT,
    reviewer_id INT,
    FOREIGN KEY (series_id) REFERENCES series(id) ON DELETE CASCADE,
    FOREIGN KEY (reviewer_id) REFERENCES reviewers(id) ON DELETE CASCADE
    );
SELECT title, genre, rating FROM series
    JOIN reviews ON series.id = reviews.series_id;
SELECT title, AVG(rating) FROM series
    JOIN reviews ON series.id = reviews.series_id
    GROUP BY title;
SELECT title, ROUND(AVG(rating), 2) AS avg_rating FROM series
    JOIN reviews ON series.id = reviews.series_id
    GROUP BY title
    ORDER BY avg_rating ASC;
SELECT first_name, last_name, rating FROM reviewers
    JOIN reviews ON reviews.reviewer_id = reviewers.id;
SELECT title, genre, IFNULL(rating, "Not Rated") AS ratings FROM series
    LEFT JOIN reviews on reviews.series_id = series.id;
SELECT title AS Unreviewed_series, IFNULL(rating, "Not Rated") AS ratings FROM series
    LEFT JOIN reviews on reviews.series_id = series.id
    WHERE rating IS NULL;
SELECT genre, ROUND(AVG(rating), 2) AS avg_rating FROM series
    JOIN reviews ON series.id = reviews.series_id
    GROUP BY genre
    ORDER BY avg_rating ASC;
-- A little bit harder example than the previous ones
SELECT title, rating, CONCAT(first_name, " ", last_name) AS reviewer FROM series
    JOIN reviews ON reviews.reviewer_id = series.id
    JOIN reviewers ON reviews.reviewer_id = reviewers.id;
SELECT title, rating, CONCAT(first_name, " ", last_name) AS reviewer FROM reviews
    JOIN series ON reviews.series_id = series.id
    JOIN reviewers ON reviews.reviewer_id = reviewers.id
-- CREATE VIEW - ALTER VIEW - CREATE OR REPLACE VIEW
-- The line below detects series that have only one review
SELECT title, AVG(rating) FROM full_reviews GROUP BY title HAVING COUNT(rating) > 1; 
-- WITH ROLLUP
SELECT title, SUM(rating), AVG(rating) FROM full_reviews GROUP BY title WITH ROLLUP;
-- SQL MODES
SELECT @@GLOBAL.sql_mode;
SELECT @@SESSION.sql_mode;
-- FULL GROUP BY or ONLY FULL GROUP BY - You are only allowed to reference or to select columns that are either aggregate function columns (AVG, COUNT, SUM) 
-- OR, columns that you have already named GROUP BY CLAUSE
-- WINDOW FUNCTIONS
SELECT department, AVG(salary) OVER() FROM employees;
SELECT emp_no, department, salary, AVG(salary) OVER() FROM employees;
SELECT emp_no, department, salary, MIN(salary) OVER(), MAX(salary) OVER() FROM employees;
-- CUMULATIVE SALARY using a WINDOW FUNCTION
SELECT emp_no,
    department,
    salary,
    SUM(salary) OVER(PARTITION BY department ORDER BY salary DESC) AS rolling_dept_salary,
    SUM(salary) OVER(PARTITION BY department) AS total_dept_salary
    FROM employees;
SELECT
    emp_no,
    department,
    salary,
    ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS dept_row_number,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS dept_salary_rank,
    RANK() OVER(ORDER BY salary DESC) AS overall_rank,
    DENSE_RANK() OVER(ORDER BY salary DESC) AS overall_dense_rank
    FROM employees ORDER BY department;
-- CREATING TRIGGERS
CREATE DATABASE trigger_demo;
USE trigger_demo;
SELECT DATABASE();
CREATE TABLE users(
    username VARCHAR(100),
    age INT);
DELIMITER $$
CREATE TRIGGER must_be_adult
     BEFORE INSERT ON users FOR EACH ROW
     BEGIN
          IF NEW.age < 18
          THEN
              SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Must be an adult!';
          END IF;
     END;
$$
DELIMITER ;    


