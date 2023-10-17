-- MySQL server
-- should creates a table called first_table in the current database
-- should the database name will be passed as an argument
-- should not fail If the table first_table already exists
-- should not use the SELECT or SHOW statements

CREATE TABLE IF NOT EXISTS first_table(
    id INT,
    name VARCHAR(256)
);
