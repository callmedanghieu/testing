# SQL knowledge map (derived from the seven transcripts)

This map is extracted from the source lectures. It is not a generic SQL syllabus. Topics the lectures never cover (for example window functions, CASE, normal-form theory beyond the heuristic) are **absent on purpose**; see [roadmap.md § Gaps](roadmap.md#gaps-in-the-source-material).
Difficulty: ★ recall · ★★ apply · ★★★ combine · ★★★★ design/judgement.
Source refs use `lectureN Lstart-end` (the files in `sources/`).

```
SQL (CS50 SQL, weeks 0-6)
├── M0 Querying (lecture0)
│   ├── C0.1 Databases, DBMSs and SQL (why not spreadsheets; CRUD)
│   ├── C0.2 SELECT, FROM, identifiers vs strings, keyword style
│   ├── C0.3 LIMIT
│   ├── C0.4 WHERE: =, != / <>, NOT
│   ├── C0.5 AND, OR and parentheses
│   ├── C0.6 NULL: IS NULL / IS NOT NULL
│   ├── C0.7 LIKE with % and _ (case-insensitive matching)
│   ├── C0.8 Ranges: <, >, <=, >=, BETWEEN … AND …
│   ├── C0.9 ORDER BY (ASC/DESC, several keys)
│   ├── C0.10 Aggregate functions: COUNT, AVG, MIN, MAX, SUM; ROUND; AS
│   └── C0.11 DISTINCT
├── M1 Relating (lecture1)
│   ├── C1.1 Relational databases; one-to-one, one-to-many, many-to-many
│   ├── C1.2 ER diagrams (crow's foot notation)
│   ├── C1.3 Primary keys and foreign keys (ISBN vs surrogate id; junction tables)
│   ├── C1.4 Subqueries (nested queries)
│   ├── C1.5 IN
│   ├── C1.6 JOIN … ON (INNER JOIN)
│   ├── C1.7 OUTER JOINs: LEFT, RIGHT, FULL
│   ├── C1.8 NATURAL JOIN
│   ├── C1.9 Sets: UNION, INTERSECT, EXCEPT
│   └── C1.10 GROUP BY and HAVING
├── M2 Designing (lecture2)
│   ├── C2.1 sqlite3 shell: .schema, .read, .quit, .mode, schema.sql workflow
│   ├── C2.2 Normalizing (entities in their own tables)
│   ├── C2.3 Relationships & ER diagrams (one/many, junction tables)
│   ├── C2.4 CREATE TABLE / DROP TABLE
│   ├── C2.5 Storage classes vs type affinities
│   ├── C2.6 Table constraints: PRIMARY KEY (single, composite, rowid), FOREIGN KEY
│   ├── C2.7 Column constraints: NOT NULL, UNIQUE, DEFAULT, CHECK
│   └── C2.8 ALTER TABLE: RENAME TO, ADD/RENAME/DROP COLUMN
├── M3 Writing (lecture3)
│   ├── C3.1 INSERT INTO (single row, implicit primary key)
│   ├── C3.2 Constraints at write time (UNIQUE / NOT NULL failures)
│   ├── C3.3 Multi-row INSERT; INSERT INTO ... SELECT
│   ├── C3.4 .import CSV (existing table / new temp table)
│   ├── C3.5 DELETE ... WHERE (IS NULL, dates, subqueries)
│   ├── C3.6 Foreign keys on delete: RESTRICT, NO ACTION, SET NULL, SET DEFAULT, CASCADE
│   ├── C3.7 UPDATE ... SET ... WHERE (subqueries)
│   ├── C3.8 Data cleaning: trim(), upper()/lower(), LIKE patterns
│   ├── C3.9 Triggers: BEFORE/AFTER INSERT/UPDATE/DELETE, OLD/NEW
│   └── C3.10 Soft deletion
├── M4 Viewing (lecture4)
│   ├── C4.1 Views: CREATE VIEW / DROP VIEW
│   ├── C4.2 Views to simplify (hide joins)
│   ├── C4.3 Views to aggregate (and views on views)
│   ├── C4.4 Temporary views
│   ├── C4.5 Common table expressions (WITH)
│   ├── C4.6 Views to partition
│   ├── C4.7 Views to secure (and their SQLite limits)
│   └── C4.8 INSTEAD OF triggers (WHEN conditions) on views
├── M5 Optimizing (lecture5)
│   ├── C5.1 Measuring: .timer, scan vs search
│   ├── C5.2 Indexes: CREATE/DROP INDEX, EXPLAIN QUERY PLAN
│   ├── C5.3 Multi-column & covering indexes
│   ├── C5.4 B-trees and index trade-offs (space, write cost)
│   ├── C5.5 Partial indexes
│   ├── C5.6 VACUUM
│   ├── C5.7 Transactions: BEGIN / COMMIT / ROLLBACK, ACID
│   ├── C5.8 Race conditions & isolation
│   └── C5.9 Locks: shared / exclusive, BEGIN EXCLUSIVE
└── M6 Scaling (lecture6)
    ├── C6.1 Database servers (MySQL, PostgreSQL) vs embedded SQLite; CLIs
    ├── C6.2 MySQL types: integers, CHAR/VARCHAR/TEXT, ENUM/SET, date/time, FLOAT/DOUBLE/DECIMAL
    ├── C6.3 MySQL ALTER TABLE ... MODIFY
    ├── C6.4 Stored procedures (DELIMITER, IN parameters, CALL)
    ├── C6.5 PostgreSQL types: SERIAL, CREATE TYPE ... ENUM, TIMESTAMP, NUMERIC, MONEY
    ├── C6.6 Scaling: vertical vs horizontal; replication; sharding
    ├── C6.7 Access control: CREATE USER, GRANT, REVOKE
    └── C6.8 SQL injection & prepared statements
```

---

## Concept records

### M0: Querying (lecture0)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C0.1 | Databases, DBMSs, SQL | A database organizes data so you can create, read, update and delete it; a DBMS (SQLite, MySQL, PostgreSQL, …) is the software you use to do that; SQL is the Structured Query Language | none | C6.1 | `sqlite3 longlist.db` | why move from spreadsheets: scale, frequent updates, speed | thinking SQL *is* the database | ★ | lecture0 L64-169 |
| C0.2 | SELECT / FROM | Return chosen columns (or `*`) from a table | C0.1 | C0.3 | `SELECT "title", "author" FROM "longlist";` | titles and authors of 78 books | single quotes on identifiers; lowercase keywords hurt readability | ★ | lecture0 L251-360 |
| C0.3 | LIMIT | Cap the number of rows returned | C0.2 | C0.9 | `... LIMIT 5;` | peek at 5 titles | assuming a meaningful order without ORDER BY | ★ | lecture0 L366-396 |
| C0.4 | WHERE, =, != / <>, NOT | Keep only rows where a condition is true; negate it | C0.2 | C3.5, C3.7 | `WHERE "year" = 2023`, `WHERE "format" != 'hardcover'`, `WHERE NOT ...` | books of 2023; non-hardcovers | quoting numbers; double quotes on string values | ★ | lecture0 L397-515 |
| C0.5 | AND / OR / parentheses | Combine conditions into compound ones | C0.4 | C0.8 | `WHERE ("year" = 2022 OR "year" = 2023) AND "format" != 'hardcover'` | 2022-23 paperbacks | forgetting that AND binds before OR (D0-02) | ★★ | lecture0 L517-564 |
| C0.6 | NULL | The absence of a value; test with IS NULL / IS NOT NULL | C0.4 | C0.10, C2.7 | `WHERE "translator" IS NULL` | 2 books without translator | `= NULL` (never true); COUNT(col) skips NULLs | ★ | lecture0 L587-633 |
| C0.7 | LIKE, % and _ | Approximate text matching: `%` any run, `_` one character; case-insensitive | C0.4 | C3.8 | `WHERE "title" LIKE '%love%'`, `LIKE 'P_re'` | 4 "love" titles; Pyre; Tyll | `'The%'` also matching "There…"; using = for patterns | ★★ | lecture0 L638-830, L951-971 |
| C0.8 | Ranges and BETWEEN | Numeric comparisons; BETWEEN is inclusive | C0.4 | C5.5 | `WHERE "year" BETWEEN 2019 AND 2022`, `"rating" > 4.0 AND "votes" > 10000` | 2019-2022 books; top-rated with many votes | chaining many ORs; forgetting BETWEEN includes both ends | ★ | lecture0 L834-930 |
| C0.9 | ORDER BY | Sort results ascending (default) or DESC, by one or more keys | C0.2 | C4.2 | `ORDER BY "rating" DESC, "votes" DESC LIMIT 10` | top 10, ties broken by votes; titles Z→A | expecting DESC by default; relying on table order | ★★ | lecture0 L976-1130 |
| C0.10 | Aggregate functions | Collapse many rows into one value: COUNT, AVG, MIN, MAX, SUM; tidy with ROUND and AS | C0.6 | C1.10 | `SELECT ROUND(AVG("rating"), 2) AS "average rating" FROM "longlist";` | 3.75 average; 78 vs 76 with COUNT(translator) | COUNT(col) vs COUNT(*); MAX/MIN on text is alphabetical | ★★ | lecture0 L1131-1343 |
| C0.11 | DISTINCT | Remove duplicate values from a result (also inside COUNT) | C0.10 | C1.9 | `SELECT COUNT(DISTINCT "publisher") FROM "longlist";` | distinct publishers | counting duplicates (D0-04); misspelled double-quoted column silently becomes a string (D0-03) | ★ | lecture0 L1344-1401 |

### M1: Relating (lecture1)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C1.1 | Relationships | Tables relate one-to-one, one-to-many or many-to-many | C0.2 | C2.3 | (design) | authors ↔ books (many-to-many); book → ratings (one-to-many) | the "honor system" (row n of one table ↔ row n of another); one big table with repeated authors | ★★ | lecture1 L48-146 |
| C1.2 | ER diagrams | Entities as boxes, relationships as lines; crow's foot: circle = zero, bar = one, foot = many | C1.1 | C2.3 | (notation) | longlist: authors, books, publishers, translators, ratings | reading cardinality in only one direction | ★★ | lecture1 L147-246 |
| C1.3 | Primary and foreign keys | A primary key uniquely identifies rows; a foreign key is that key stored in another table to link them | C1.1 | C2.6 | `books.id` ↔ `ratings.book_id`; `authored(author_id, book_id)` | ISBN vs surrogate ids; (23, 1) = Eva wrote Boulder | ISBNs as keys (size, leading zeros); changing ids | ★★ | lecture1 L247-482 |
| C1.4 | Subqueries | A query in parentheses whose result feeds the outer query; runs innermost first | C0.4 | C1.6, C3.5, C3.7 | `WHERE "publisher_id" = (SELECT "id" FROM "publishers" WHERE ...)` | Fitzcarraldo/MacLehose books; who wrote The Birthday Party | hard-coding ids; `=` when several rows come back | ★★ | lecture1 L491-861 |
| C1.5 | IN | Membership in a set of values (often a subquery) | C1.4 | C1.9 | `WHERE "id" IN (SELECT "book_id" FROM "authored" WHERE ...)` | Fernanda Melchor's two books | using `=` for a list (D1-04) | ★★ | lecture1 L862-985 |
| C1.6 | JOIN … ON | Combine rows of two tables where the ON condition holds; plain JOIN = INNER JOIN (unmatched rows dropped) | C1.3 | C4.2 | `FROM "sea_lions" JOIN "migrations" ON "migrations"."id" = "sea_lions"."id"` | sea lions with their migrations | joining on the wrong columns (D1-01); duplicate rows from one-to-many joins (D1-02) | ★★ | lecture1 L1022-1162 |
| C1.7 | OUTER JOINs | LEFT / RIGHT / FULL keep unmatched rows of the left / right / both tables, filling NULLs | C1.6 | C0.6 | `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN` | Jolee kept; untracked migrations kept | INNER JOIN where "every row" was required (D1-08); RIGHT/FULL need SQLite ≥ 3.39 | ★★ | lecture1 L1208-1379 |
| C1.8 | NATURAL JOIN | Join on all same-named columns, keeping one copy | C1.6 | | `FROM "sea_lions" NATURAL JOIN "migrations"` | no ON clause, one id column | silent meaning change if another shared column appears | ★ | lecture1 L1380-1404 |
| C1.9 | Sets: UNION / INTERSECT / EXCEPT | Combine result sets: either, both, one-but-not-the-other | C0.11 | C1.5 | `SELECT "name" FROM "authors" INTERSECT SELECT "name" FROM "translators";` | authors ∪ translators with a profession column; Ngũgĩ; Hughes ∩ Jull Costa | different column counts (D1-09); operator order when chaining | ★★★ | lecture1 L1408-1663 |
| C1.10 | GROUP BY / HAVING | Collapse rows into groups and aggregate per group; HAVING filters groups | C0.10 | C4.3 | `SELECT "book_id", ROUND(AVG("rating"), 2) FROM "ratings" GROUP BY "book_id" HAVING ... ORDER BY ...` | per-book averages (3.77, 3.97, 3.04); books above 4.0; counts per book | WHERE on an aggregate (D1-07); aggregating without GROUP BY (D1-03); GROUP BY on uncleaned text | ★★★ | lecture1 L1664-1839 |

### M2: Designing (lecture2)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C2.1 | sqlite3 shell & schema files | Dot-commands are shell commands, not SQL; keep your schema in a re-runnable file | none | C2.4 | `sqlite3 mbta.db`, `.schema [t]`, `.read schema.sql`, `.quit` | `.read schema.sql` then `.schema` | ending dot-commands with `;`; editing only in the prompt | ★ | lecture2 L23-110, L659-720 |
| C2.2 | Normalizing | Reduce redundancy: each entity in its own table; a table's columns describe only that entity | C2.4 | C2.3 | heuristic, not syntax | Charlie/Alice/Bob fare log split into riders and stations | storing the same fact in many rows; mixing entities in one table | ★★★★ | lecture2 L192-263 |
| C2.3 | Relationships & ER diagrams | One-to-one / one-to-many / many-to-many; a many-to-many needs a junction (associative) table | C2.2 | C1.6, C2.6 | crow's-foot notation | riders ↔ stations through `visits`; cards → swipes ← stations | putting a list of ids in one column instead of a junction table | ★★★ | lecture2 L265-346, L425-444, L1060-1090 |
| C2.4 | CREATE / DROP TABLE | Define a table and its columns; delete a table and its data | C2.1 | C2.5-C2.8 | `CREATE TABLE t ("c" TYPE, ..., constraints);` `DROP TABLE t;` | `CREATE TABLE "riders" ("id" INTEGER, "name" TEXT, PRIMARY KEY("id"));` | trailing comma after the last item; `DROP` instead of `ALTER` | ★ | lecture2 L348-468, L647-658 |
| C2.5 | Storage classes vs type affinities | Values have a storage class (NULL, INTEGER, REAL, TEXT, BLOB); columns have an affinity (TEXT, NUMERIC, INTEGER, REAL, BLOB) that converts inserted values when it can | C2.4 | C6.2 | `typeof(x)` shows the storage class | inserting `'25'` into an INTEGER column stores `25` | believing SQLite types are strict; storing money as REAL; untyped column = BLOB affinity (not NUMERIC, see errata #1) | ★★ | lecture2 L475-640, L1335-1347 |
| C2.6 | PRIMARY KEY / FOREIGN KEY | PK uniquely identifies rows (unique, not null); FK must match a PK value in the referenced table | C2.4 | C3.6 | `PRIMARY KEY("id")`, `PRIMARY KEY("a","b")`, `FOREIGN KEY("x") REFERENCES "t"("id")` | visits: FK rider_id → riders(id), station_id → stations(id); implicit `rowid` | composite PK that forbids legitimate repeats (repeat visits); assuming FKs are enforced without `PRAGMA foreign_keys=ON` | ★★ | lecture2 L769-913 |
| C2.7 | Column constraints | NOT NULL, UNIQUE, DEFAULT value, CHECK(expr) | C2.6 | C3.2 | `"amount" NUMERIC NOT NULL CHECK("amount" != 0)`, `DEFAULT CURRENT_TIMESTAMP` | swipes table | redundant constraints on PKs; FK columns DO accept NULL (errata #3) | ★★ | lecture2 L915-1022, L1231-1305 |
| C2.8 | ALTER TABLE | Change a table's schema in place | C2.4 | C3.10, C6.3 | `ALTER TABLE t RENAME TO u; ADD COLUMN c T; RENAME COLUMN a TO b; DROP COLUMN c;` | visits → swipes; `ttpe` → `type` | trying to change a column's type/constraints in SQLite (not supported, rebuild instead) | ★ | lecture2 L1094-1180 |

### M3: Writing (lecture3)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C3.1 | INSERT INTO | Add a row; values align with the listed columns | C2.4 | C3.3 | `INSERT INTO t (c1, c2) VALUES (v1, v2);` | `INSERT INTO "collections" ("title", "accession_number", "acquired") VALUES ('Spring Outing', '14.76', '1914-01-08');` | supplying the PK yourself and colliding; misaligned columns/values | ★ | lecture3 L67-246 |
| C3.2 | Constraint violations | The DBMS rejects writes that break constraints | C2.7, C3.1 | C5.7 | n/a | `UNIQUE constraint failed`, `NOT NULL constraint failed` | treating the error as a bug instead of a guardrail | ★ | lecture3 L247-312 |
| C3.3 | Multi-row INSERT / INSERT ... SELECT | Insert many rows in one statement, or the result of a query | C3.1, C0.2 | C3.4 | `VALUES (...), (...);` / `INSERT INTO t (cols) SELECT ... FROM s;` | moving rows from `temp` into `collections` | column count/order mismatch between INSERT list and SELECT list | ★★ | lecture3 L313-364, L570-603 |
| C3.4 | .import CSV | Load a CSV file into a table (shell command) | C2.1 | C3.3 | `.import --csv --skip 1 mfa.csv collections` / `.import --csv mfa.csv temp` | import, then INSERT…SELECT to get generated ids | importing the header row as data; blanks become '' not NULL | ★★ | lecture3 L381-663 |
| C3.5 | DELETE | Remove rows matching a condition | C0.4 | C3.6, C3.10 | `DELETE FROM t WHERE cond;` | `DELETE FROM "collections" WHERE "acquired" < '1909-01-01';` | **no WHERE deletes everything**; `= NULL` | ★ | lecture3 L670-819 |
| C3.6 | FK actions on delete | What happens to referencing rows when a referenced row is deleted | C2.6, C3.5 | C4.8 | `FOREIGN KEY(a) REFERENCES t(id) ON DELETE CASCADE` (RESTRICT / NO ACTION / SET NULL / SET DEFAULT) | deleting "Unidentified artist" cascades to `created` | expecting CASCADE without declaring it; forgetting the 2-step manual delete otherwise | ★★★ | lecture3 L820-1052 |
| C3.7 | UPDATE | Change column values in matching rows | C0.4, C1.4 | C3.8 | `UPDATE t SET c = v [, ...] WHERE cond;` | re-attribute *Farmers Working at Dawn* to Li Yin via two subqueries | no WHERE updates every row | ★★ | lecture3 L1093-1196 |
| C3.8 | Data cleaning | Use scalar functions and patterns to normalize messy text | C3.7, C1.10 | C0.4 | `trim()`, `upper()`, `lower()`, `LIKE 'Fa%'` | votes.csv tally | over-broad LIKE patterns (`'Fa%'` matches other titles in bigger data) | ★★★ | lecture3 L1197-1486 |
| C3.9 | Triggers | Statements that run automatically before/after an INSERT/UPDATE/DELETE, once per affected row | C3.1-C3.7 | C4.8 | `CREATE TRIGGER n AFTER INSERT ON t FOR EACH ROW BEGIN ... ; END;` with `NEW.col` / `OLD.col` | `sell` (BEFORE DELETE → log 'sold'), `buy` (AFTER INSERT → log 'bought') | using NEW in a DELETE trigger (only OLD exists); forgetting `;` before END | ★★★ | lecture3 L1494-1693 |
| C3.10 | Soft deletion | Mark rows deleted (a flag) instead of removing them | C2.8, C3.7 | C4.8, C6.4 | `ALTER TABLE t ADD COLUMN "deleted" INTEGER DEFAULT 0;` `UPDATE ... SET "deleted" = 1` | Farmers Working at Dawn soft-deleted | forgetting to filter `deleted = 0` everywhere; privacy/GDPR implications | ★★ | lecture3 L1694-1793 |

### M4: Viewing (lecture4)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C4.1 | View | A virtual table defined by a query; stored in the schema, re-run on each use | C0.2 | all of M4 | `CREATE VIEW name AS SELECT ...;` `DROP VIEW name;` | `SELECT * FROM "longlist";` on the view | thinking a view stores a copy of the data | ★ | lecture4 L77-104, L244-278, L653-658 |
| C4.2 | Simplifying view | Hide a multi-table join behind one name | C4.1, C1.6 | C1.4 | `CREATE VIEW "longlist" AS SELECT "name", "title" FROM ... JOIN ...;` | Fernanda's books in one line | dropping key columns you'll later need for joins (L502-510) | ★★ | lecture4 L106-336 |
| C4.3 | Aggregating view; view on view | Store a summary query; build further views on it | C4.1, C1.10 | C4.4 | `CREATE VIEW "average_book_ratings" AS SELECT ..., ROUND(AVG(...),2) ... GROUP BY ...;` | average ratings per book, then per year | expecting it to need refreshing (it is always current) | ★★ | lecture4 L337-526, L554-603 |
| C4.4 | Temporary view | A view that lasts only for the current connection | C4.1 | C4.5 | `CREATE TEMPORARY VIEW ...` | `average_ratings_by_year` gone after `.quit` | relying on it in a later session | ★ | lecture4 L527-632 |
| C4.5 | CTE | A named query that exists only for one statement | C4.1 | C1.4 | `WITH a AS (...), b AS (...) SELECT ... FROM a ...;` | per-year averages from a per-book CTE | a trailing comma after the last CTE | ★★ | lecture4 L633-703 |
| C4.6 | Partitioning view | One view per logical slice of a table | C4.1, C0.4 | C5.5 | `CREATE VIEW "2022" AS SELECT ... WHERE "year" = 2022;` | views "2021", "2022" | numeric-looking names need quotes; ambiguous names | ★ | lecture4 L709-811 |
| C4.7 | Securing view | Expose only the columns someone needs | C4.1 | C6.7 | `SELECT "id", "origin", "destination", 'anonymous' AS "rider" FROM "rides"` | rideshare `analysis` view | SQLite cannot stop anyone reading the base table (no access control) | ★★ | lecture4 L853-968 |
| C4.8 | INSTEAD OF triggers on views | Translate writes on a (read-only) view into writes on base tables | C3.9, C3.10, C4.1 | C6.4 | `CREATE TRIGGER n INSTEAD OF DELETE ON v FOR EACH ROW [WHEN cond] BEGIN ... END;` | soft-delete & re-insert through `current_collections` | forgetting the WHERE inside the trigger (updates every row); needing two INSERT triggers (exists / not exists) | ★★★★ | lecture4 L974-1336 |

### M5: Optimizing (lecture5)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C5.1 | Measuring queries; scans | `.timer on` reports real/user/sys time; without an index SQLite scans every row | C0.4 | C5.2 | `.timer on` | 'Cars' lookup: 0.084 s | optimizing without measuring | ★ | lecture5 L124-211 |
| C5.2 | Index + EXPLAIN QUERY PLAN | A separate sorted structure that lets SQLite *search* instead of *scan* | C5.1 | C5.3-C5.5 | `CREATE INDEX "title_index" ON "movies" ("title");` `EXPLAIN QUERY PLAN SELECT ...;` `DROP INDEX ...;` | 0.084 s → 0.01 s; plan shows `USING INDEX title_index` | indexing a column the query doesn't filter on; forgetting PKs already have one | ★★ | lecture5 L214-348 |
| C5.3 | Covering index | An index containing every column the query needs, so the table is never read | C5.2 | C1.4 | `CREATE INDEX "person_index" ON "stars" ("person_id", "movie_id");` | Tom Hanks query 0.197 s → 0.004 s | wrong column order (filter column must come first) | ★★★ | lecture5 L349-542 |
| C5.4 | B-trees & trade-offs | Indexes are balanced trees of sorted values + row pointers: fast lookups, but more space and slower writes | C5.2 | C5.6 | n/a | movie-title tree walkthrough | indexing every column "just in case" | ★★★ | lecture5 L543-861 |
| C5.5 | Partial index | An index over only the rows matching a WHERE | C5.2 | C4.6 | `CREATE INDEX "recents" ON "movies" ("title") WHERE "year" = 2023;` | used for `year = 2023`, not for `year = 1998` | expecting it to help queries outside its condition | ★★★ | lecture5 L862-942 |
| C5.6 | VACUUM | Return freed pages to the OS (deleting only marks space reusable) | C5.4 | | `VACUUM;` | 158 MB → 100 MB after dropping indexes | expecting DROP/DELETE alone to shrink the file | ★ | lecture5 L943-1042 |
| C5.7 | Transactions / ACID | A unit of work that happens entirely or not at all | C3.7, C2.7 | C5.8 | `BEGIN TRANSACTION; ...; COMMIT;` / `ROLLBACK;` | Alice pays Bob $10; CHECK(balance ≥ 0) forces ROLLBACK | ROLLBACK outside a transaction; forgetting to COMMIT | ★★★ | lecture5 L1049-1330 |
| C5.8 | Race conditions / isolation | Concurrent read-decide-write sequences can interleave and corrupt state; isolate them | C5.7 | C5.9 | (design) | Charlie's double transfer + Alice's ATM withdrawal | checking a balance outside the transaction that spends it | ★★★★ | lecture5 L1331-1455 |
| C5.9 | Locks | SQLite: UNLOCKED, SHARED (many readers), EXCLUSIVE (one writer, no readers) | C5.8 | | `BEGIN EXCLUSIVE TRANSACTION;` | second connection: `database is locked` | holding an exclusive lock longer than needed | ★★ | lecture5 L1456-1553 |

### M6: Scaling (lecture6)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C6.1 | Database servers | MySQL/PostgreSQL run as servers with users and their own CLIs | C2.1 | C6.7 | `mysql -u root -h 127.0.0.1 -P 3306 -p`; `SHOW DATABASES; USE x; SHOW TABLES; DESCRIBE t;` / `psql`, `\l`, `\c`, `\dt`, `\d t`, `\q` | creating `mbta` on both | using SQLite's double quotes for MySQL identifiers (MySQL uses backticks) | ★ | lecture6 L40-156, L159-352, L1288-1490 |
| C6.2 | MySQL types | Explicit, strict column types | C2.5 | C6.5 | `INT AUTO_INCREMENT`, `VARCHAR(32)`, `ENUM('a','b')`, `DATETIME`, `DECIMAL(5,2)` | cards / stations / swipes in MySQL | FLOAT for money; DECIMAL(M,D) misread (errata #7) | ★★ | lecture6 L183-852 |
| C6.3 | ALTER TABLE ... MODIFY | Redefine an existing column (MySQL) | C2.8, C6.2 | | `ALTER TABLE stations MODIFY line ENUM(...) NOT NULL;` | adding the silver line | omitting existing ENUM values or NOT NULL in the new definition | ★★ | lecture6 L853-923 |
| C6.4 | Stored procedures | Named, stored SQL routines with parameters (MySQL) | C3.7, C3.10 | C3.9 | `DELIMITER //` `CREATE PROCEDURE sell(IN sold_id INT) BEGIN ...; END//` `CALL sell(2);` | `current_collection`, `sell` | forgetting to change the delimiter; selling an already-sold item twice | ★★★ | lecture6 L947-1278 |
| C6.5 | PostgreSQL types | SERIAL, custom ENUM types, TIMESTAMP/INTERVAL, NUMERIC(p,s), MONEY | C6.2 | | `CREATE TYPE "swipe_type" AS ENUM ('enter','exit','deposit');` `DEFAULT now()` | Postgres swipes table | expecting MySQL-style inline ENUM | ★★ | lecture6 L1293-1477 |
| C6.6 | Scaling strategies | Vertical (bigger server) vs horizontal (more servers): replication (leader/follower, sync/async, read replicas), sharding | C6.1 | | (architecture) | profile-photo upload; names A-I / J-R / S-Z | async replication's data-loss risk; shard hotspots; single point of failure | ★★★★ | lecture6 L1494-1785 |
| C6.7 | Access control | Users and privileges | C6.1, C4.7 | | `CREATE USER 'carter' IDENTIFIED BY '...'; GRANT SELECT ON rideshare.analysis TO 'carter'; REVOKE ...` | analyst can read the view but not `rides` | `GRANT ALL ON *.*` in production | ★★ | lecture6 L1786-1920 |
| C6.8 | SQL injection & prepared statements | Untrusted input concatenated into SQL can change the query; bind it as a parameter instead | C0.4 | | `PREPARE s FROM 'SELECT ... WHERE id = ?'; SET @id = 1; EXECUTE s USING @id;` | `' OR 1=1`, `1 UNION SELECT * FROM accounts` | building SQL with string formatting (Python f-strings, L2138-2147) | ★★★ | lecture6 L1921-2148 |
