-- MySQL server
-- should creates the table force_name on your MySQL server
-- should force_name containe id and name in the description
-- should name will be passed as an argument
-- should not fail if the table force_name already exists

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);