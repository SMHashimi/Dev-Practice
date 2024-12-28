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



