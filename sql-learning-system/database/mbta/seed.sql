-- Station names are real MBTA subway stations; card ids and every swipe are SYNTHETIC.
-- Fare 2.40 is the fare quoted in Lecture 2 (L1083) and Lecture 6 (L598).
-- (Park Street is on both the red and green lines in reality; the Lecture 2 schema allows one line per station.)
INSERT INTO "cards" ("id") VALUES (1), (2), (3), (4), (5), (6);

INSERT INTO "stations" ("id", "name", "line") VALUES
(1, 'Alewife', 'red'),
(2, 'Harvard', 'red'),
(3, 'Kendall/MIT', 'red'),
(4, 'Park Street', 'red'),
(5, 'Downtown Crossing', 'orange'),
(6, 'Jackson Square', 'orange'),
(7, 'Government Center', 'blue'),
(8, 'Aquarium', 'blue'),
(9, 'Boylston', 'green'),
(10, 'Copley', 'green'),
(11, 'Braintree', 'red');

INSERT INTO "swipes" ("id", "card_id", "station_id", "type", "datetime", "amount") VALUES
(1, 1, 3, 'deposit', '2023-10-02 07:55:10', 20),
(2, 1, 3, 'enter',   '2023-10-02 07:56:02', -2.40),
(3, 2, 2, 'deposit', '2023-10-02 08:01:44', 10),
(4, 2, 2, 'enter',   '2023-10-02 08:02:15', -2.40),
(5, 3, 1, 'enter',   '2023-10-02 08:10:00', -2.40),
(6, 4, 4, 'deposit', '2023-10-02 08:15:31', 5),
(7, 4, 4, 'enter',   '2023-10-02 08:16:05', -2.40),
(8, 1, 6, 'exit',    '2023-10-02 08:20:12', -0.50),
(9, 5, 7, 'deposit', '2023-10-02 09:00:00', 20),
(10, 5, 7, 'enter',  '2023-10-02 09:01:30', -2.40),
(11, 2, 4, 'enter',  '2023-10-02 17:30:41', -2.40),
(12, 3, 2, 'enter',  '2023-10-02 17:45:09', -2.40),
(13, 1, 3, 'enter',  '2023-10-03 07:58:20', -2.40),
(14, 6, 9, 'deposit','2023-10-03 08:30:00', 15),
(15, 6, 9, 'enter',  '2023-10-03 08:30:40', -2.40),
(16, 4, 5, 'enter',  '2023-10-03 12:05:55', -2.40),
(17, 5, 8, 'enter',  '2023-10-03 13:14:07', -2.40),
(18, 6, 10, 'enter', '2023-10-03 18:02:33', -2.40),
(19, 1, 4, 'enter',  '2023-10-03 18:10:12', -2.40),
(20, 2, 2, 'deposit','2023-10-04 07:40:00', 20),
(21, 2, 3, 'enter',  '2023-10-04 07:41:18', -2.40),
(22, 3, 1, 'deposit','2023-10-04 08:00:00', 10),
(23, 3, 1, 'enter',  '2023-10-04 08:00:30', -2.40),
(24, 4, 11, 'exit',  '2023-10-04 09:12:45', -0.50);
