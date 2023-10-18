-- MySQL server
-- should ists all the cities of California
-- should result must be sorted in ascending order by cities.id
-- should not use the JOIN keyword
-- should name will be passed as an argument

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = "California"
);
