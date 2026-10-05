-- bank: Lecture 5 L1145-1159 (transactions) and Lecture 6 L2002-2007 (SQL injection)
CREATE TABLE "accounts" (
    "id" INTEGER,
    "name" TEXT NOT NULL,
    "balance" INTEGER NOT NULL CHECK("balance" >= 0),
    PRIMARY KEY("id")
);
