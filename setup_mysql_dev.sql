-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS coconut;
CREATE USER IF NOT EXISTS 'dcaro'@'localhost' IDENTIFIED BY 'dcaro';
GRANT ALL PRIVILEGES ON `coconut`.* TO 'dcaro'@'localhost';
FLUSH PRIVILEGES;