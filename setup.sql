-- Script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS <database_name>;
CREATE USER IF NOT EXISTS '<user_name>'@'<user_host>' IDENTIFIED BY '<user_password>';
GRANT SELECT ON performance_schema.* TO '<user_name>'@'<user_host>';
GRANT ALL PRIVILEGES ON webdev_db.* TO '<user_name>'@'<user_host>';
FLUSH PRIVILEGES;