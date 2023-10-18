-- MySQL server
-- should creates the table unique_id
-- should unique_id containe id and name on the description
-- should name will be passed as an argument
-- should not fail if the table unique_id already exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
