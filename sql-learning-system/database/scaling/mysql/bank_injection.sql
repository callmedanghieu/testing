-- SQL injection and prepared statements (sources/lecture6.txt L1921-2148).
CREATE TABLE `accounts` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL,
    `balance` INT NOT NULL CHECK(`balance` >= 0),
    PRIMARY KEY(`id`)
);
INSERT INTO `accounts` (`name`, `balance`) VALUES ('Alice', 10), ('Bob', 20), ('Charlie', 30);

-- What a careless app would run after pasting the input "1 UNION SELECT * FROM accounts":
SELECT * FROM `accounts` WHERE `id` = 1 UNION SELECT * FROM `accounts`;

-- Prepared statement: the input is bound as data
PREPARE `balance_check` FROM 'SELECT * FROM `accounts` WHERE `id` = ?';
SET @id = '1 UNION SELECT * FROM accounts';
EXECUTE `balance_check` USING @id;   -- only Alice: MySQL converts the string to 1 (warning 1292), see errata #8
SHOW WARNINGS;
DEALLOCATE PREPARE `balance_check`;
