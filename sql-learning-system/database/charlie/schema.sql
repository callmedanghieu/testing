-- charlie: the first, NON-normalized table sketched at the start of Lecture 2
-- (sources/lecture2.txt L147-199). Used for the normalization exercises.
-- Deliberately poor design: names repeat, stations repeat, no real keys.
CREATE TABLE "log" (
    "id" INTEGER,
    "name" TEXT,
    "station" TEXT,
    "action" TEXT,
    "fare" NUMERIC,
    "balance" NUMERIC,
    PRIMARY KEY("id")
);
