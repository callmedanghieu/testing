-- MySQL translation of the MBTA schema (sources/lecture6.txt L159-923).
-- Run: mysql -u root -p -e 'CREATE DATABASE `mbta`' && mysql -u root -p mbta < mbta.sql
CREATE TABLE `cards` (
    `id` INT AUTO_INCREMENT,
    PRIMARY KEY(`id`)
);

CREATE TABLE `stations` (
    `id` INT AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL UNIQUE,
    `line` ENUM('blue', 'green', 'orange', 'red') NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `swipes` (
    `id` INT AUTO_INCREMENT,
    `card_id` INT,
    `station_id` INT,
    `type` ENUM('enter', 'exit', 'deposit') NOT NULL,
    `datetime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `amount` DECIMAL(5,2) NOT NULL CHECK(`amount` != 0),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`card_id`) REFERENCES `cards`(`id`),
    FOREIGN KEY(`station_id`) REFERENCES `stations`(`id`)
);

-- L860-919: the silver line
ALTER TABLE `stations` MODIFY `line` ENUM('blue', 'green', 'orange', 'red', 'silver') NOT NULL;

-- sample rows (synthetic)
INSERT INTO `cards` () VALUES (), ();
INSERT INTO `stations` (`name`, `line`) VALUES ('Harvard', 'red'), ('Kendall/MIT', 'red'), ('South Station', 'silver');
INSERT INTO `swipes` (`card_id`, `station_id`, `type`, `amount`) VALUES (1, 1, 'deposit', 20.00), (1, 1, 'enter', -2.40);
SHOW TABLES;
DESCRIBE `swipes`;
SELECT `type`, `amount` FROM `swipes`;
