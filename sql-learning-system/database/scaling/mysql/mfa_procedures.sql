-- Stored procedures on the MFA collection (sources/lecture6.txt L947-1278).
CREATE TABLE `collections` (
    `id` INT AUTO_INCREMENT,
    `title` VARCHAR(64) NOT NULL,
    `accession_number` VARCHAR(16) NOT NULL UNIQUE,
    `acquired` DATE,
    PRIMARY KEY(`id`)
);
INSERT INTO `collections` (`title`, `accession_number`, `acquired`) VALUES
('Farmers Working at Dawn', '11.6152', '1911-08-03'),
('Imaginative Landscape', '56.496', NULL),
('Profusion of Flowers', '56.257', '1956-04-12'),
('Spring Outing', '14.76', '1914-01-08');

-- L1019-1036: soft-delete flag; TINYINT because it only holds 0/1
ALTER TABLE `collections` ADD COLUMN `deleted` TINYINT DEFAULT 0;

-- L1056-1090: a procedure without parameters
DELIMITER //
CREATE PROCEDURE `current_collection`()
BEGIN
    SELECT `title`, `accession_number`, `acquired` FROM `collections` WHERE `deleted` = 0;
END//
DELIMITER ;

-- L1140-1157: transactions log
CREATE TABLE `transactions` (
    `id` INT AUTO_INCREMENT,
    `title` VARCHAR(64) NOT NULL,
    `action` ENUM('bought', 'sold') NOT NULL,
    PRIMARY KEY(`id`)
);

-- L1166-1239: a procedure with an IN parameter (lecture version: no guard against double sales)
DELIMITER //
CREATE PROCEDURE `sell`(IN `sold_id` INT)
BEGIN
    UPDATE `collections` SET `deleted` = 1 WHERE `id` = `sold_id`;
    INSERT INTO `transactions` (`title`, `action`)
    VALUES ((SELECT `title` FROM `collections` WHERE `id` = `sold_id`), 'sold');
END//
DELIMITER ;

CALL `sell`(2);
CALL `current_collection`();
SELECT * FROM `transactions`;
