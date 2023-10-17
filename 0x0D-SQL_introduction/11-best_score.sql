-- MySQL server
-- sould lists all records with a score >= 10 in the table second_table
-- should display both the score and the name
-- should be ordered by score
-- should the database name will be passed as an argument

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
