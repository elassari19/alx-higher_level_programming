-- MySQL server
-- should creates the database hbtn_0d_usa and the table states
-- should states containe id and name on the description
-- should not fail if the table hbtn_0d_usa already exists
-- should not fail if the table states already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
