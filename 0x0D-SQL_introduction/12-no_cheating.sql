-- MySQL server
-- should updates the score of Bob to 10 in the table second_table
-- should not use Bob’s id value
-- should the database name will be passed as an argument

UPDATE second_table
SET
    score = 10
WHERE
    name = "Bob";
