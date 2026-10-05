# Phase 1: Document inventory

All five files are **English lecture transcripts** (plain text, one spoken line per text line, no headings or page numbers) of Carter Zenke's *CS50's Introduction to Databases with SQL* (Harvard, 2023).
Because there are no pages, **every reference in this system is `file:line`**, using the copies in [`../sources/`](../sources/), which are byte-identical to the uploads. Line numbers are 1-based, as shown by any editor.

| Short name | Uploaded file | Lines | Lecture (CS50 SQL week) | Datasets used |
|---|---|---|---|---|
| `lecture2` | `cs50_sql_lecture2-720p-en.txt` | 1391 | Week 2: **Designing** | `longlist.db` (glimpse), `mbta.db` (built from scratch) |
| `lecture3` | `cs50_sql_lecture3-720p-en.txt` | 1793 | Week 3: **Writing** | `mfa.db`, `mfa.csv`, `votes.csv` |
| `lecture4` | `cs50_sql_lecture4-720p-en.txt` | 1336 | Week 4: **Viewing** | `longlist.db`, `rideshare.db`, `mfa.db` |
| `lecture5` | `cs50_sql_lecture5-720p_MBR-en.txt` | 1562 | Week 5: **Optimizing** | `movies.db` (IMDb), `bank.db` |
| `lecture6` | `cs50_sql_lecture6-720p_MBR-en.txt` | 2169 | Week 6: **Scaling** | MySQL `mbta`, `mfa`, `rideshare`, `bank`; PostgreSQL `mbta` |

**Not in the material set:** weeks 0 (*Querying*) and 1 (*Relating*). The five lectures constantly *use* `SELECT`, `WHERE`, `LIKE`, `ORDER BY`, `LIMIT`, `GROUP BY`, aggregates, `IN`, subqueries and `JOIN`, but never *teach* them. This system therefore adds Module 0, a prerequisite toolkit. It is built only from queries that appear in these five transcripts, and every Module 0 exercise is labeled GENERATED.

---

## lecture2: Designing (1391 lines)

| Lines | Section (inferred from speech) | Content |
|---|---|---|
| 13-110 | Under the hood of longlist.db | `sqlite3 file.db`, `SELECT ... LIMIT 5`, `.schema`, `.schema books`, `.quit` |
| 112-263 | Design challenge: the Boston subway (MBTA) | Charlie/Alice/Bob fare table (L147-191); redundancy critique; **normalizing** (L243-263) |
| 265-346 | Relationships | riders ↔ stations many-to-many; ER diagram notation (crow's foot, "at least one", "zero to many") |
| 348-468 | CREATE TABLE | `CREATE TABLE riders (id, name)`; stations; visits junction table; indentation style |
| 469-590 | Storage classes | NULL, INTEGER, REAL, TEXT, BLOB; **fares as integer vs text vs real** trade-off |
| 591-767 | Type affinities | TEXT, NUMERIC, INTEGER, REAL, BLOB; conversion on insert; `DROP TABLE`; **schema.sql + `.read`** workflow; no BOOLEAN (use 0/1) |
| 769-914 | Table constraints | `PRIMARY KEY`, `FOREIGN KEY ... REFERENCES`, composite PK, implicit `rowid`, comma rules |
| 915-1046 | Column constraints | `CHECK`, `DEFAULT`, `NOT NULL`, `UNIQUE`; redundancy with PK |
| 1047-1230 | Redesign: CharlieCards | cards / swipes / stations; `ALTER TABLE ... RENAME TO / ADD COLUMN / RENAME COLUMN / DROP COLUMN` |
| 1231-1305 | Constraints applied | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP`, `CHECK(amount != 0)`, `CHECK(type IN (...))` |
| 1306-1391 | Q&A + wrap-up | dropping referenced tables, portability to MySQL/Postgres, default affinity (stated **incorrectly**; see source-issues #1) |

Audience questions used as exercises: L199-221 (redundancies), L307-327 (same ids in two tables), L329-346 (ER cardinality), L446-468 (missing keys), L553-589 (fare type), L868-895 (comma rule), L897-913 (visits id), L1012-1022 (PK implies NOT NULL/UNIQUE), L1335-1347 (no type given).

## lecture3: Writing (1793 lines)

| Lines | Section | Content |
|---|---|---|
| 10-90 | CRUD; MFA collections | the `INSERT INTO table (cols) VALUES (...)` shape |
| 91-246 | INSERT | explicit ids, then omitted id → automatic primary key; next id after deletes |
| 247-312 | Constraints on insert | UNIQUE failure, NOT NULL failure |
| 313-380 | Multi-row INSERT | faster and atomic |
| 381-605 | CSV import | `.import --csv --skip 1`; importing into a new table `temp`, then `INSERT INTO ... SELECT`, `DROP TABLE temp` |
| 606-669 | Q&A | column order; a constraint failure aborts the whole multi-row insert; **CSV blanks are '' not NULL** |
| 670-819 | DELETE | `DELETE FROM ... WHERE`; `IS NULL`; date comparison `acquired < '1909-01-01'` |
| 820-1092 | Deleting with FOREIGN KEYs | FK error; two-step delete via subquery; `ON DELETE RESTRICT / NO ACTION / SET NULL / SET DEFAULT / CASCADE`; AUTOINCREMENT (stated **incorrectly**; see #2) |
| 1093-1196 | UPDATE | re-attribute an artwork via subqueries; `UPDATE ... SET ... WHERE` |
| 1197-1452 | Cleaning data (votes.csv) | `GROUP BY` is case-sensitive; `trim()`, `upper()`, `LIKE 'Fa%'`, targeted fixes |
| 1453-1493 | Q&A | `lower()`, scalar functions, alternative: a category column |
| 1494-1683 | Triggers | `CREATE TRIGGER name BEFORE/AFTER INSERT/UPDATE OF/DELETE ON t FOR EACH ROW BEGIN ... END`; `OLD`, `NEW`; sell / buy log |
| 1694-1793 | Soft deletion | `ALTER TABLE ... ADD COLUMN deleted INTEGER DEFAULT 0`; ethics (GDPR, right to be forgotten) |

## lecture4: Viewing (1336 lines)

| Lines | Section | Content |
|---|---|---|
| 14-104 | Why views | many-to-many recap; **view = virtual table defined by a query**; simplify / aggregate / partition / secure |
| 106-336 | Simplifying | nested-subquery version vs JOIN version; `CREATE VIEW longlist AS ...`; ordering a view |
| 337-526 | Aggregating | `AVG`, `ROUND(...,2)`, `GROUP BY book_id`, joined with books → `average_book_ratings`; views reflect new data |
| 527-632 | Temporary views | `CREATE TEMPORARY VIEW average_ratings_by_year` built on a view; gone after `.quit` |
| 633-708 | CTEs | `WITH name AS (...) SELECT ...`; `DROP VIEW` |
| 709-852 | Partitioning | `CREATE VIEW "2022" AS ... WHERE year = 2022`; naming trade-off; **views cannot be updated** |
| 853-973 | Securing | rideshare PII; `'anonymous' AS "rider"`; SQLite has no access control |
| 974-1336 | Soft deletes + views + triggers | `current_collections`; `INSTEAD OF DELETE` trigger; conditional `INSTEAD OF INSERT ... WHEN NEW.accession_number IN (...)`; **assigned exercise** at L1331-1335 |

## lecture5: Optimizing (1562 lines)

| Lines | Section | Content |
|---|---|---|
| 10-123 | IMDb data | people / movies / stars / ratings; `LIMIT 5`; search for 'Cars' |
| 124-211 | Timing and scans | `.timer on`; real / user / sys time; linear search = table **scan** |
| 214-348 | Indexes | book-index metaphor; `CREATE INDEX ... ON t (col)`; `EXPLAIN QUERY PLAN`; `DROP INDEX`; PKs are auto-indexed |
| 349-542 | Multi-table + covering indexes | Tom Hanks nested subquery; index `people(name)`, `stars(person_id)`; covering index `stars(person_id, movie_id)`; 0.197 s → 0.004 s |
| 543-861 | B-trees and trade-offs | why indexes cost space; sorted copy + row pointers; binary search; nodes / root / leaves; slower inserts |
| 862-942 | Partial indexes | `CREATE INDEX recents ON movies (title) WHERE year = 2023`; used only when the WHERE matches |
| 943-1048 | VACUUM | dropped data is only marked free; `du -b`; `VACUUM` 158 MB → 100 MB |
| 1049-1330 | Transactions | Alice pays Bob; ACID; `BEGIN TRANSACTION` / `COMMIT` / `ROLLBACK`; CHECK violation → rollback |
| 1331-1455 | Race conditions | double-transfer attack; isolation = sequential transactions |
| 1456-1562 | Locks | UNLOCKED / SHARED / EXCLUSIVE; `BEGIN EXCLUSIVE TRANSACTION` → "database is locked"; granularity |

## lecture6: Scaling (2169 lines)

| Lines | Section | Content |
|---|---|---|
| 10-156 | Scalability; MySQL server | embedded vs server DBMS; `mysql -u root -h 127.0.0.1 -P 3306 -p`; `SHOW DATABASES` |
| 159-352 | MySQL integers | `CREATE DATABASE`, `USE`; TINYINT…BIGINT ranges; UNSIGNED; `AUTO_INCREMENT`; backticks; `SHOW TABLES`, `DESCRIBE` |
| 353-581 | MySQL strings | CHAR vs VARCHAR(M) vs TEXT sizes; BLOB; **ENUM vs SET**; stations table |
| 583-852 | Dates and numbers | DATE / TIME / DATETIME / TIMESTAMP / YEAR (fsp); FLOAT vs DOUBLE PRECISION; **DECIMAL(M,D)**; swipes table; `MUL`; MySQL is stricter than SQLite's affinities |
| 853-946 | ALTER TABLE ... MODIFY | add the silver line to an ENUM |
| 947-1280 | Stored procedures | `DELIMITER //`, `CREATE PROCEDURE current_collection() BEGIN ... END`, `CALL`; `sell(IN sold_id INT)`; IF / loops; **assigned exercise** at L1258-1265 |
| 1281-1493 | PostgreSQL | `psql`, `\l`, `\c`, `\dt`, `\d`, `\q`; SMALLINT / INT / BIGINT; SERIAL; `CREATE TYPE ... AS ENUM`; TIMESTAMP, INTERVAL, NUMERIC(p,s), MONEY; `now()` |
| 1494-1785 | Scaling strategies | vertical vs horizontal; replication (single-leader, multi-leader, leaderless; synchronous vs asynchronous; read replica); sharding (hotspots, single point of failure) |
| 1786-1920 | Access control | `CREATE USER`, `GRANT SELECT ON rideshare.analysis TO ...`, `REVOKE`, `GRANT ALL ON *.*` |
| 1921-2148 | SQL injection | `' OR 1=1`, `UNION SELECT`; prepared statements `PREPARE ... FROM '... ?'`, `SET @id`, `EXECUTE ... USING @id` |
| 2149-2169 | Course recap | |

---

## Repeated concepts across documents

| Concept | Appears in |
|---|---|
| MFA collections + soft delete | lecture3 L1694-1793 → lecture4 L974-1336 (view + triggers) → lecture6 L955-1100 (stored procedure) |
| MBTA cards/stations/swipes | lecture2 (SQLite design) → lecture6 L57-852 (MySQL), L1288-1477 (Postgres) |
| Rideshare PII | lecture4 L863-968 (view; SQLite cannot restrict) → lecture6 L1840-1900 (MySQL GRANT finally restricts it) |
| Bank accounts | lecture5 (transactions, race conditions, locks) → lecture6 (injection, prepared statements) |
| Subqueries vs JOIN | lecture3 L938-961, L1151-1165; lecture4 L139-192 vs L202-240; lecture5 L376-394 |
| Constraints as guardrails | lecture2 L777-1022, L1231-1305; lecture3 L247-312; lecture5 L1153 (CHECK balance ≥ 0 drives ROLLBACK) |
| Transactions | promised in lecture3 L634-638, delivered in lecture5 L1049-1330 |
| Triggers | lecture3 L1494-1683 (BEFORE/AFTER) → lecture4 L1103-1330 (INSTEAD OF, WHEN) |
| Type systems | lecture2 (SQLite storage classes/affinities) → lecture6 (MySQL/Postgres strict types) |

## Differences and contradictions

See [`source-issues.md`](source-issues.md). Each item there was checked by running SQLite 3.45, MariaDB 10.11 or PostgreSQL 16. The most important ones:
- lecture3 says AUTOINCREMENT makes SQLite reuse unused ids. It is the opposite.
- lecture2 says a column with no type has NUMERIC affinity. It has BLOB ("no") affinity.
- lecture2 implies foreign-key columns can't be NULL. They can.
- lecture6 says DECIMAL(5,1) allows ±999.99. That is DECIMAL(5,2).
