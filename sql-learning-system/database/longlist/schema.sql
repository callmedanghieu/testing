-- longlist: the relational version of the International Booker longlist
-- (sources/lecture1.txt L36-55, L149-208; used again in lecture2 L66-106 and lecture4).
CREATE TABLE "authors" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "publishers" (
    "id" INTEGER,
    "publisher" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "translators" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "books" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "publisher_id" INTEGER,
    "year" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("publisher_id") REFERENCES "publishers"("id")
);

-- junction tables: authors <-> books and translators <-> books are many-to-many
CREATE TABLE "authored" (
    "author_id" INTEGER,
    "book_id" INTEGER,
    FOREIGN KEY("author_id") REFERENCES "authors"("id"),
    FOREIGN KEY("book_id") REFERENCES "books"("id")
);

CREATE TABLE "translated" (
    "translator_id" INTEGER,
    "book_id" INTEGER,
    FOREIGN KEY("translator_id") REFERENCES "translators"("id"),
    FOREIGN KEY("book_id") REFERENCES "books"("id")
);

-- one row per individual rating (one-to-many: a book has many ratings)
CREATE TABLE "ratings" (
    "book_id" INTEGER,
    "rating" INTEGER NOT NULL CHECK("rating" BETWEEN 1 AND 5),
    FOREIGN KEY("book_id") REFERENCES "books"("id")
);
