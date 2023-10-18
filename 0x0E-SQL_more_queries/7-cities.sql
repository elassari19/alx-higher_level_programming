-- MySQL server
-- should creates the database hbtn_0d_usa and the table cities
-- should cities containe id and name on the description
-- should not fail if the table hbtn_0d_usa already exists
-- should not fail if the table cities already exists

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
