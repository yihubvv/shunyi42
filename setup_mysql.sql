CREATE DATABASE IF NOT EXISTS book_42_01
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'bookmanager'@'localhost'
  IDENTIFIED BY 'mysql';

ALTER USER 'bookmanager'@'localhost'
  IDENTIFIED BY 'mysql';

GRANT ALL PRIVILEGES ON book_42_01.* TO 'bookmanager'@'localhost';

FLUSH PRIVILEGES;
