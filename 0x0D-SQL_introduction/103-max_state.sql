-- MySQL server20
-- should Import in hbtn_0c_0 database from temperatures
-- should displays the max temperature of each state (ordered by State name)

SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
