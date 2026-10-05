-- longlist: International Booker Prize longlist (CS50 SQL "longlist.db", relational version)
-- Source: sources/lecture4.txt L14-31 (authors / books / authored many-to-many), L344-392 (ratings)
CREATE TABLE "authors" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id")
);

CREATE TABLE "books" (
    "id" INTEGER,
    "title" TEXT NOT NULL,
    "year" INTEGER NOT NULL,
    PRIMARY KEY("id")
);

-- junction table: an author can write many books, a book can have many authors
CREATE TABLE "authored" (
    "author_id" INTEGER,
    "book_id" INTEGER,
    FOREIGN KEY("author_id") REFERENCES "authors"("id"),
    FOREIGN KEY("book_id") REFERENCES "books"("id")
);

-- one row per individual rating (Lecture 4 L352-370: keep individual ratings, compute averages)
CREATE TABLE "ratings" (
    "book_id" INTEGER,
    "rating" INTEGER NOT NULL CHECK("rating" BETWEEN 1 AND 5),
    FOREIGN KEY("book_id") REFERENCES "books"("id")
);
