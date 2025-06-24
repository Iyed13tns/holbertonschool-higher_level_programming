-- This script creates a user with all privileges on all databases and tables.

CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
FLUSH PRIVILEGES;