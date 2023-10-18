-- MySQL server
-- shoul creates the MySQL server user user_0d_1
-- should user_0d_1 have all privileges on your MySQL server
-- should the password set to user_0d_1_pwd
-- should not fail if the user user_0d_1 already exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
