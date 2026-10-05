# M2 · Designing
*Source: lecture2 (Week 2 · Designing). Datasets: `charlie` (the first draft table), `mbta` (final design).*

Story of the lecture: represent Boston's subway (the MBTA). Start with one messy table of riders paying fares, split it into entities, relate them, add types and constraints, then redesign around **CharlieCards** because the MBTA tracks cards, not people.

---

## C2.1 The sqlite3 shell and schema files
*Source: lecture2 L23-110, L659-720*

**Level 1.** The `sqlite3` program has its own **dot-commands** for housekeeping. They are not SQL. Keep your design in a `schema.sql` file you can edit and re-run, instead of retyping CREATE TABLEs.

**Level 2.**
```text
sqlite3 mbta.db          -- open (or create) a database file
.schema                  -- show every CREATE statement
.schema books            -- just one table
.read schema.sql         -- run every statement in a file
.mode table              -- boxed output (Q&A, L739-741)
.quit
```
Dot-commands take **no semicolon** and run only in the shell (not in this trainer's editor).

**Level 3.** The workflow from the lecture is: edit `schema.sql` → `DROP TABLE` the old tables → `.read schema.sql`. Version-control that file. It is the documentation of your database.

---

## C2.2 Normalizing
*Source: lecture2 L147-263*

**Level 1: Intuition.** The first table had rows like *Charlie · Kendall/MIT · enter · $0.10 · $0.05 left*. Names and station names repeat, two different Charlies are indistinguishable, and renaming a station means editing many rows. Normalizing splits facts so that each one is stored **once**.

**Level 2.** There is no syntax. It is a design process with two heuristics from the lecture:
1. Put each **entity** (rider, station) in **its own table** with its own primary key.
2. Every column you add to a table should describe **only that entity**.

**Level 3.** The lecture names 1NF/2NF/3NF but stays with the heuristics (formal normal forms are a gap, see the roadmap). The payoff: queries are easier to write, data is easier to change in one place, and anomalies (two Charlies) disappear.

---

## C2.3 Relationships and ER diagrams
*Source: lecture2 L265-346, L425-444, L1060-1090*

**Level 1.** Ask how many of B one A can have, and how many of A one B can have. A rider visits many stations, and a station has many riders, so the relationship is **many-to-many**.

**Level 2.** In crow's-foot notation: a single bar means *exactly one / at least one*, a circle means *zero*, and three prongs mean *many*. A many-to-many relationship is implemented with a **junction table** (also called an associative entity or join table):
```sql
CREATE TABLE "visits" ("rider_id" INTEGER, "station_id" INTEGER, ...);
```
Each row says "this rider visited this station".

**Level 3.** The cardinalities are judgement calls. The class debated whether a station must have at least one rider (L329-346). In the CharlieCard redesign, each **swipe** belongs to exactly one card and one station, while cards and stations have many swipes.

---

## C2.4 CREATE TABLE and DROP TABLE
*Source: lecture2 L348-468, L647-658*

**Level 1.** CREATE TABLE writes down the shape of a table: its name, its columns, and their rules. DROP TABLE throws the table and all of its rows away.

**Level 2.**
```sql
CREATE TABLE "riders" (
    "id" INTEGER,          -- column name + type affinity
    "name" TEXT,           -- comma between items …
    PRIMARY KEY("id")      -- … but none after the last one
);
DROP TABLE "riders";
```

**Level 3.** The trailing-comma error is the most common syntax slip (debugging D2-01). DROP is irreversible. To change a table that already holds data, prefer ALTER TABLE (C2.8).

---

## C2.5 Storage classes vs type affinities
*Source: lecture2 L475-640, L754-767, L1335-1347*

**Level 1: Intuition.** In SQLite, **values** carry a type (the storage class), and **columns** have a *preference* (the affinity) that converts incoming values when it reasonably can.

**Level 2.**

| Storage classes (values) | Type affinities (columns) |
|---|---|
| NULL, INTEGER, REAL, TEXT, BLOB | TEXT, NUMERIC, INTEGER, REAL, BLOB |

```sql
CREATE TABLE "t" ("amount" INTEGER);
INSERT INTO "t" VALUES ('25');        -- stored as integer 25
INSERT INTO "t" VALUES ('red line');  -- can't convert, so it is stored as TEXT
SELECT typeof("amount") FROM "t";
```
* An INTEGER storage class covers 1- to 8-byte integers, and SQLite picks the size for you (L495-512).
* There is no BOOLEAN. Use INTEGER 0/1 (L754-766).
* Dates are TEXT `'YYYY-MM-DD'` or NUMERIC.

**Level 3: Practical reasoning**
* **Money:** the class compared fares as INTEGER (exact cents), TEXT `'$0.10'` (can't add), and REAL 0.10 (imprecise). Prefer integer cents, or DECIMAL in MySQL (C6.2).
* A column with **no declared type** has BLOB ("no") affinity, not NUMERIC as the lecture says (errata #1).
* SQLite is permissive and MySQL is strict (lecture6 L844-852). Don't rely on SQLite to reject bad types; use CHECK constraints if it matters.

---

## C2.6 Table constraints: PRIMARY KEY and FOREIGN KEY
*Source: lecture2 L769-913, L1311-1318*

**Level 1.** A primary key is a row's unique name tag. A foreign key is a reference to another table's name tag, and the database refuses references to rows that don't exist.

**Level 2.**
```sql
CREATE TABLE "visits" (
    "id" INTEGER,
    "rider_id" INTEGER,
    "station_id" INTEGER,
    PRIMARY KEY("id"),
    FOREIGN KEY("rider_id") REFERENCES "riders"("id"),
    FOREIGN KEY("station_id") REFERENCES "stations"("id")
);
```
* **Composite key:** `PRIMARY KEY("rider_id", "station_id")` makes the *pair* unique.
* Every SQLite table without an explicit integer PK still has a hidden **`rowid`** you can query (L840-845).

**Level 3**
* The composite key is wrong for visits, because people revisit stations (M2-E04, D2-04). Choose keys that match the real-world uniqueness rule.
* **SQLite only enforces foreign keys after `PRAGMA foreign_keys = ON;`** (errata #4). This trainer always turns it on.
* Different tables may reuse the same id values (riders 1, 2, 3 and stations 1, 2, 3). That is fine (L310-326).

---

## C2.7 Column constraints: NOT NULL, UNIQUE, DEFAULT, CHECK
*Source: lecture2 L915-1022, L1231-1305*

**Level 1.** These are guardrails that stop bad data at the door.

**Level 2.**
```sql
"name"     TEXT NOT NULL UNIQUE,
"type"     TEXT NOT NULL CHECK("type" IN ('enter', 'exit', 'deposit')),
"datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
"amount"   NUMERIC NOT NULL CHECK("amount" != 0)
```

**Level 3**
* PRIMARY KEY already implies NOT NULL and UNIQUE, so don't repeat them (L958-966).
* **Foreign-key columns do accept NULL.** Add NOT NULL if the link is mandatory (errata #3, debugging D2-03).
* Write CHECK expressions carefully. `"type" = 'enter' OR 'exit'` does not mean what it says (D2-02).
* The lecture's closing story is a reminder to design constraints so a rider can always get *off* the train (L1365-1380).

---

## C2.8 ALTER TABLE
*Source: lecture2 L1094-1180*

**Level 1.** Change a table's structure in place, keeping its rows.

**Level 2.**
```sql
ALTER TABLE "visits" RENAME TO "swipes";
ALTER TABLE "swipes" ADD COLUMN "type" TEXT;
ALTER TABLE "swipes" RENAME COLUMN "ttpe" TO "type";
ALTER TABLE "swipes" DROP COLUMN "type";
```

**Level 3.** SQLite's ALTER TABLE cannot change a column's type or constraints. To do that, rebuild the table, or in MySQL use `MODIFY` (C6.3). Existing rows get NULL in a new column, or the column's DEFAULT (used for soft deletes in C3.10).

**Practice:** M2-E01 … M2-E12 · **Debug:** D2-01 … D2-04 · **Review deck:** R2
