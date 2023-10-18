-- MySQL server
-- should ists all the cities in hbtn_0d_usa database
-- should display: cities.id - cities.name - states.name
-- should result must be sorted in ascending order by cities.id
-- should can use only one SELECT statement
-- should name will be passed as an argument

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id=states.id
ORDER BY cities.id
