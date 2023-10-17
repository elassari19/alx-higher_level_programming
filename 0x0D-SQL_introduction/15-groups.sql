-- MySQL server
-- should lists the number of records with the same score in the table second_table
-- should display the score and the number of records for this score with the label number in the result
-- should be sorted by the number of records
-- should the database name will be passed as an argument

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
