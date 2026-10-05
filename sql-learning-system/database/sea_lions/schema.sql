-- sea_lions: the JOIN demo from sources/lecture1.txt L1031-1404.
-- No foreign key on purpose: migrations also holds sea lions that are no longer tracked (L1100-1105, L1186-1193).
CREATE TABLE "sea_lions" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "migrations" (
    "id" INTEGER,
    "distance" INTEGER,
    "days" INTEGER
);
