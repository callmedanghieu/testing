-- longlist0: the week-0 SINGLE table of International Booker longlisted books (sources/lecture0.txt).
-- One row per book, every attribute in one table (lecture1 L84-106 explains why this gets redundant).
-- The original also had isbn and publication-date columns; lecture 0 never queries them, so they are omitted here.
CREATE TABLE "longlist" (
    "title" TEXT,
    "author" TEXT,
    "translator" TEXT,
    "format" TEXT,
    "pages" INTEGER,
    "publisher" TEXT,
    "year" INTEGER,
    "votes" INTEGER,
    "rating" REAL
);
