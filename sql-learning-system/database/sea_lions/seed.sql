-- Names (Ayah, Spot, Tiger, Mabel, Rick, Jolee) and ids 10484 / 11728 are from lecture1 L1049, L1170-1171.
-- Which name has which id, the other ids, and all distances/days are SYNTHETIC.
-- As in the lecture: Jolee has no migration, and two migrations belong to sea lions not in "sea_lions".
INSERT INTO "sea_lions" ("id", "name") VALUES
(10484, 'Ayah'),
(11728, 'Spot'),
(11729, 'Tiger'),
(11732, 'Mabel'),
(11734, 'Rick'),
(11790, 'Jolee');

INSERT INTO "migrations" ("id", "distance", "days") VALUES
(10484, 1000, 107),
(11728, 1531, 56),
(11729, 1370, 37),
(11732, 1622, 62),
(11734, 1491, 58),
(11735, 2723, 82),
(11736, 1571, 52);
