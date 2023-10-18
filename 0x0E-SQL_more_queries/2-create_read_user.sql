-- MySQL server2
-- should creates the database hbtn_0d_2 and the user user_0d_2
-- should user_0d_2 have all privileges on your MySQL server
-- should the password set to user_0d_2_pwd
-- should not fail if the user user_0d_2 already exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
