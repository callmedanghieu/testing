-- Access control (sources/lecture6.txt L1786-1920). Run as root in a database named rideshare.
CREATE TABLE `rides` (
    `id` INT AUTO_INCREMENT,
    `origin` VARCHAR(32) NOT NULL,
    `destination` VARCHAR(32) NOT NULL,
    `rider` VARCHAR(32) NOT NULL,
    PRIMARY KEY(`id`)
);
INSERT INTO `rides` (`origin`, `destination`, `rider`) VALUES
('Good Egg Galaxy', 'Honeyhive Galaxy', 'Peach'),
('Castle Courtyard', 'Cascade Kingdom', 'Mario');
CREATE VIEW `analysis` AS
SELECT `id`, `origin`, `destination`, 'anonymous' AS `rider` FROM `rides`;

DROP USER IF EXISTS 'carter';
CREATE USER 'carter' IDENTIFIED BY 'password';      -- demo password only
GRANT SELECT ON `analysis` TO 'carter';
SHOW GRANTS FOR 'carter';
-- REVOKE SELECT ON `analysis` FROM 'carter';
