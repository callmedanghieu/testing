-- Titles, accession numbers and acquisition dates: as stated in Lecture 3 L144-221, L346-359.
-- Ids follow Lecture 3 L1140-1145 (Farmers Working at Dawn = 1), Lecture 4 L980-989 and Lecture 6 L1228 (Imaginative Landscape = 2).
-- Artists: Li Yin = 1 and "Unidentified artist" = 3 come from Lecture 3 L848-856, L1104-1144.
-- Artist 2 and the attributions for collections 3 and 4 are PRACTICE PLACEHOLDERS, not museum records.
INSERT INTO "collections" ("id", "title", "accession_number", "acquired") VALUES
(1, 'Farmers Working at Dawn', '11.6152', '1911-08-03'),
(2, 'Imaginative Landscape', '56.496', NULL),
(3, 'Profusion of Flowers', '56.257', '1956-04-12'),
(4, 'Spring Outing', '14.76', '1914-01-08');

INSERT INTO "artists" ("id", "name") VALUES
(1, 'Li Yin'),
(2, 'Placeholder Artist'),
(3, 'Unidentified artist');

INSERT INTO "created" ("artist_id", "collection_id") VALUES
(1, 2),
(3, 1),
(2, 3),
(2, 4);
