-- MySQL server
-- should creates the table id_not_null
-- should id_not_null containe id and name on the description
-- should name will be passed as an argument
-- should not fail if the table id_not_null already exists

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
