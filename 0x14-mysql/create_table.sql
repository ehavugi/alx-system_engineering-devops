CREATE DATABASE IF NOT EXISTS tyrell_corp;
use tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50)
);

INSERT INTO nexus6 (name) VALUES('Leon');

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
