# SQL knowledge map (derived from the five transcripts)

This map is extracted from the source lectures. It is not a generic SQL syllabus. Topics the lectures never cover (for example window functions, OUTER JOINs, normal-form theory beyond the heuristic) are **absent on purpose**; see [roadmap.md § Gaps](roadmap.md#gaps-in-the-source-material).
Difficulty: ★ recall · ★★ apply · ★★★ combine · ★★★★ design/judgement.
Source refs use `lectureN Lstart-end` (the files in `sources/`).

```
SQL (CS50 SQL, weeks 2-6)
├── M0 Query toolkit (prerequisite; used in every lecture, taught in the missing weeks 0-1)
│   ├── C0.1 SELECT / FROM / LIMIT
│   ├── C0.2 WHERE: =, !=, <, >, IN, IS NULL, LIKE
│   ├── C0.3 ORDER BY
│   ├── C0.4 Aggregates (COUNT, AVG, ROUND) + GROUP BY
│   ├── C0.5 Subqueries (nested, IN (...), = (...))
│   └── C0.6 JOIN ... ON (many-to-many through a junction table)
├── M1 Designing (lecture2)
│   ├── C1.1 sqlite3 shell: .schema, .read, .quit, .mode, schema.sql workflow
│   ├── C1.2 Normalizing (entities in their own tables)
│   ├── C1.3 Relationships & ER diagrams (one/many, junction tables)
│   ├── C1.4 CREATE TABLE / DROP TABLE
│   ├── C1.5 Storage classes vs type affinities
│   ├── C1.6 Table constraints: PRIMARY KEY (single, composite, rowid), FOREIGN KEY
│   ├── C1.7 Column constraints: NOT NULL, UNIQUE, DEFAULT, CHECK
│   └── C1.8 ALTER TABLE: RENAME TO, ADD/RENAME/DROP COLUMN
├── M2 Writing (lecture3)
│   ├── C2.1 INSERT INTO (single row, implicit primary key)
│   ├── C2.2 Constraints at write time (UNIQUE / NOT NULL failures)
│   ├── C2.3 Multi-row INSERT; INSERT INTO ... SELECT
│   ├── C2.4 .import CSV (existing table / new temp table)
│   ├── C2.5 DELETE ... WHERE (IS NULL, dates, subqueries)
│   ├── C2.6 Foreign keys on delete: RESTRICT, NO ACTION, SET NULL, SET DEFAULT, CASCADE
│   ├── C2.7 UPDATE ... SET ... WHERE (subqueries)
│   ├── C2.8 Data cleaning: trim(), upper()/lower(), LIKE patterns
│   ├── C2.9 Triggers: BEFORE/AFTER INSERT/UPDATE/DELETE, OLD/NEW
│   └── C2.10 Soft deletion
├── M3 Viewing (lecture4)
│   ├── C3.1 Views: CREATE VIEW / DROP VIEW
│   ├── C3.2 Views to simplify (hide joins)
│   ├── C3.3 Views to aggregate (and views on views)
│   ├── C3.4 Temporary views
│   ├── C3.5 Common table expressions (WITH)
│   ├── C3.6 Views to partition
│   ├── C3.7 Views to secure (and their SQLite limits)
│   └── C3.8 INSTEAD OF triggers (WHEN conditions) on views
├── M4 Optimizing (lecture5)
│   ├── C4.1 Measuring: .timer, scan vs search
│   ├── C4.2 Indexes: CREATE/DROP INDEX, EXPLAIN QUERY PLAN
│   ├── C4.3 Multi-column & covering indexes
│   ├── C4.4 B-trees and index trade-offs (space, write cost)
│   ├── C4.5 Partial indexes
│   ├── C4.6 VACUUM
│   ├── C4.7 Transactions: BEGIN / COMMIT / ROLLBACK, ACID
│   ├── C4.8 Race conditions & isolation
│   └── C4.9 Locks: shared / exclusive, BEGIN EXCLUSIVE
└── M5 Scaling (lecture6)
    ├── C5.1 Database servers (MySQL, PostgreSQL) vs embedded SQLite; CLIs
    ├── C5.2 MySQL types: integers, CHAR/VARCHAR/TEXT, ENUM/SET, date/time, FLOAT/DOUBLE/DECIMAL
    ├── C5.3 MySQL ALTER TABLE ... MODIFY
    ├── C5.4 Stored procedures (DELIMITER, IN parameters, CALL)
    ├── C5.5 PostgreSQL types: SERIAL, CREATE TYPE ... ENUM, TIMESTAMP, NUMERIC, MONEY
    ├── C5.6 Scaling: vertical vs horizontal; replication; sharding
    ├── C5.7 Access control: CREATE USER, GRANT, REVOKE
    └── C5.8 SQL injection & prepared statements
```

---

## Concept records

### M0: Query toolkit (prerequisite)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C0.1 | SELECT / LIMIT | Read columns from a table; LIMIT caps the rows returned | none | C0.3 | `SELECT col, ... FROM t LIMIT n;` | `SELECT "author", "title" FROM "longlist" LIMIT 5;` | `SELECT *` on a 400k-row table; forgetting the semicolon in the shell | ★ | lecture2 L38-48; lecture5 L91-103 |
| C0.2 | WHERE filters | Keep rows where a condition is true | C0.1 | C2.5, C2.7 | `= != < > IN (...) IS NULL LIKE 'pat%'` | `SELECT * FROM "movies" WHERE "title" = 'Cars';` | `= NULL` instead of `IS NULL`; expecting `=` to be case-insensitive | ★ | lecture5 L118; lecture3 L734-741; lecture3 L1374-1394 |
| C0.3 | ORDER BY | Sort the result | C0.1 | C3.2 | `ORDER BY col [ASC/DESC]` | `SELECT "name", "title" FROM "longlist" ORDER BY "title";` | assuming tables have an inherent order | ★ | lecture4 L317-330 |
| C0.4 | Aggregates + GROUP BY | Collapse rows into groups and compute one value per group | C0.1 | C3.3 | `SELECT g, COUNT(*), ROUND(AVG(x), 2) FROM t GROUP BY g;` | `SELECT "book_id", ROUND(AVG("rating"), 2) AS "rating" FROM "ratings" GROUP BY "book_id";` | selecting a non-grouped column; forgetting that GROUP BY on text is case-sensitive | ★★ | lecture4 L371-433; lecture3 L1229-1256 |
| C0.5 | Subqueries | A query nested inside another; its result feeds the outer query | C0.2 | C0.6, C2.5, C2.7 | `WHERE id IN (SELECT ...)`, `WHERE id = (SELECT ...)` | Fernanda Melchor's titles via 3-level nesting | `=` when the subquery returns several rows (SQLite silently uses the first) | ★★ | lecture4 L127-192; lecture5 L364-394 |
| C0.6 | JOIN ... ON | Combine rows of tables whose key columns match | C0.5 | C1.3, C3.2 | `FROM a JOIN b ON a.id = b.a_id` | `authors JOIN authored ON authors.id = authored.author_id JOIN books ON books.id = authored.book_id` | joining on the wrong columns → duplicate or empty results | ★★ | lecture4 L202-240, L438-466 |

### M1: Designing (lecture2)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C1.1 | sqlite3 shell & schema files | Dot-commands are shell commands, not SQL; keep your schema in a re-runnable file | none | C1.4 | `sqlite3 mbta.db`, `.schema [t]`, `.read schema.sql`, `.quit` | `.read schema.sql` then `.schema` | ending dot-commands with `;`; editing only in the prompt | ★ | lecture2 L23-110, L659-720 |
| C1.2 | Normalizing | Reduce redundancy: each entity in its own table; a table's columns describe only that entity | C1.4 | C1.3 | heuristic, not syntax | Charlie/Alice/Bob fare log split into riders and stations | storing the same fact in many rows; mixing entities in one table | ★★★★ | lecture2 L192-263 |
| C1.3 | Relationships & ER diagrams | One-to-one / one-to-many / many-to-many; a many-to-many needs a junction (associative) table | C1.2 | C0.6, C1.6 | crow's-foot notation | riders ↔ stations through `visits`; cards → swipes ← stations | putting a list of ids in one column instead of a junction table | ★★★ | lecture2 L265-346, L425-444, L1060-1090 |
| C1.4 | CREATE / DROP TABLE | Define a table and its columns; delete a table and its data | C1.1 | C1.5-C1.8 | `CREATE TABLE t ("c" TYPE, ..., constraints);` `DROP TABLE t;` | `CREATE TABLE "riders" ("id" INTEGER, "name" TEXT, PRIMARY KEY("id"));` | trailing comma after the last item; `DROP` instead of `ALTER` | ★ | lecture2 L348-468, L647-658 |
| C1.5 | Storage classes vs type affinities | Values have a storage class (NULL, INTEGER, REAL, TEXT, BLOB); columns have an affinity (TEXT, NUMERIC, INTEGER, REAL, BLOB) that converts inserted values when it can | C1.4 | C5.2 | `typeof(x)` shows the storage class | inserting `'25'` into an INTEGER column stores `25` | believing SQLite types are strict; storing money as REAL; untyped column = BLOB affinity (not NUMERIC, see errata #1) | ★★ | lecture2 L475-640, L1335-1347 |
| C1.6 | PRIMARY KEY / FOREIGN KEY | PK uniquely identifies rows (unique, not null); FK must match a PK value in the referenced table | C1.4 | C2.6 | `PRIMARY KEY("id")`, `PRIMARY KEY("a","b")`, `FOREIGN KEY("x") REFERENCES "t"("id")` | visits: FK rider_id → riders(id), station_id → stations(id); implicit `rowid` | composite PK that forbids legitimate repeats (repeat visits); assuming FKs are enforced without `PRAGMA foreign_keys=ON` | ★★ | lecture2 L769-913 |
| C1.7 | Column constraints | NOT NULL, UNIQUE, DEFAULT value, CHECK(expr) | C1.6 | C2.2 | `"amount" NUMERIC NOT NULL CHECK("amount" != 0)`, `DEFAULT CURRENT_TIMESTAMP` | swipes table | redundant constraints on PKs; FK columns DO accept NULL (errata #3) | ★★ | lecture2 L915-1022, L1231-1305 |
| C1.8 | ALTER TABLE | Change a table's schema in place | C1.4 | C2.10, C5.3 | `ALTER TABLE t RENAME TO u; ADD COLUMN c T; RENAME COLUMN a TO b; DROP COLUMN c;` | visits → swipes; `ttpe` → `type` | trying to change a column's type/constraints in SQLite (not supported, rebuild instead) | ★ | lecture2 L1094-1180 |

### M2: Writing (lecture3)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C2.1 | INSERT INTO | Add a row; values align with the listed columns | C1.4 | C2.3 | `INSERT INTO t (c1, c2) VALUES (v1, v2);` | `INSERT INTO "collections" ("title", "accession_number", "acquired") VALUES ('Spring Outing', '14.76', '1914-01-08');` | supplying the PK yourself and colliding; misaligned columns/values | ★ | lecture3 L67-246 |
| C2.2 | Constraint violations | The DBMS rejects writes that break constraints | C1.7, C2.1 | C4.7 | n/a | `UNIQUE constraint failed`, `NOT NULL constraint failed` | treating the error as a bug instead of a guardrail | ★ | lecture3 L247-312 |
| C2.3 | Multi-row INSERT / INSERT ... SELECT | Insert many rows in one statement, or the result of a query | C2.1, C0.1 | C2.4 | `VALUES (...), (...);` / `INSERT INTO t (cols) SELECT ... FROM s;` | moving rows from `temp` into `collections` | column count/order mismatch between INSERT list and SELECT list | ★★ | lecture3 L313-364, L570-603 |
| C2.4 | .import CSV | Load a CSV file into a table (shell command) | C1.1 | C2.3 | `.import --csv --skip 1 mfa.csv collections` / `.import --csv mfa.csv temp` | import, then INSERT…SELECT to get generated ids | importing the header row as data; blanks become '' not NULL | ★★ | lecture3 L381-663 |
| C2.5 | DELETE | Remove rows matching a condition | C0.2 | C2.6, C2.10 | `DELETE FROM t WHERE cond;` | `DELETE FROM "collections" WHERE "acquired" < '1909-01-01';` | **no WHERE deletes everything**; `= NULL` | ★ | lecture3 L670-819 |
| C2.6 | FK actions on delete | What happens to referencing rows when a referenced row is deleted | C1.6, C2.5 | C3.8 | `FOREIGN KEY(a) REFERENCES t(id) ON DELETE CASCADE` (RESTRICT / NO ACTION / SET NULL / SET DEFAULT) | deleting "Unidentified artist" cascades to `created` | expecting CASCADE without declaring it; forgetting the 2-step manual delete otherwise | ★★★ | lecture3 L820-1052 |
| C2.7 | UPDATE | Change column values in matching rows | C0.2, C0.5 | C2.8 | `UPDATE t SET c = v [, ...] WHERE cond;` | re-attribute *Farmers Working at Dawn* to Li Yin via two subqueries | no WHERE updates every row | ★★ | lecture3 L1093-1196 |
| C2.8 | Data cleaning | Use scalar functions and patterns to normalize messy text | C2.7, C0.4 | C0.2 | `trim()`, `upper()`, `lower()`, `LIKE 'Fa%'` | votes.csv tally | over-broad LIKE patterns (`'Fa%'` matches other titles in bigger data) | ★★★ | lecture3 L1197-1486 |
| C2.9 | Triggers | Statements that run automatically before/after an INSERT/UPDATE/DELETE, once per affected row | C2.1-C2.7 | C3.8 | `CREATE TRIGGER n AFTER INSERT ON t FOR EACH ROW BEGIN ... ; END;` with `NEW.col` / `OLD.col` | `sell` (BEFORE DELETE → log 'sold'), `buy` (AFTER INSERT → log 'bought') | using NEW in a DELETE trigger (only OLD exists); forgetting `;` before END | ★★★ | lecture3 L1494-1693 |
| C2.10 | Soft deletion | Mark rows deleted (a flag) instead of removing them | C1.8, C2.7 | C3.8, C5.4 | `ALTER TABLE t ADD COLUMN "deleted" INTEGER DEFAULT 0;` `UPDATE ... SET "deleted" = 1` | Farmers Working at Dawn soft-deleted | forgetting to filter `deleted = 0` everywhere; privacy/GDPR implications | ★★ | lecture3 L1694-1793 |

### M3: Viewing (lecture4)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C3.1 | View | A virtual table defined by a query; stored in the schema, re-run on each use | C0.1 | all of M3 | `CREATE VIEW name AS SELECT ...;` `DROP VIEW name;` | `SELECT * FROM "longlist";` on the view | thinking a view stores a copy of the data | ★ | lecture4 L77-104, L244-278, L653-658 |
| C3.2 | Simplifying view | Hide a multi-table join behind one name | C3.1, C0.6 | C0.5 | `CREATE VIEW "longlist" AS SELECT "name", "title" FROM ... JOIN ...;` | Fernanda's books in one line | dropping key columns you'll later need for joins (L502-510) | ★★ | lecture4 L106-336 |
| C3.3 | Aggregating view; view on view | Store a summary query; build further views on it | C3.1, C0.4 | C3.4 | `CREATE VIEW "average_book_ratings" AS SELECT ..., ROUND(AVG(...),2) ... GROUP BY ...;` | average ratings per book, then per year | expecting it to need refreshing (it is always current) | ★★ | lecture4 L337-526, L554-603 |
| C3.4 | Temporary view | A view that lasts only for the current connection | C3.1 | C3.5 | `CREATE TEMPORARY VIEW ...` | `average_ratings_by_year` gone after `.quit` | relying on it in a later session | ★ | lecture4 L527-632 |
| C3.5 | CTE | A named query that exists only for one statement | C3.1 | C0.5 | `WITH a AS (...), b AS (...) SELECT ... FROM a ...;` | per-year averages from a per-book CTE | a trailing comma after the last CTE | ★★ | lecture4 L633-703 |
| C3.6 | Partitioning view | One view per logical slice of a table | C3.1, C0.2 | C4.5 | `CREATE VIEW "2022" AS SELECT ... WHERE "year" = 2022;` | views "2021", "2022" | numeric-looking names need quotes; ambiguous names | ★ | lecture4 L709-811 |
| C3.7 | Securing view | Expose only the columns someone needs | C3.1 | C5.7 | `SELECT "id", "origin", "destination", 'anonymous' AS "rider" FROM "rides"` | rideshare `analysis` view | SQLite cannot stop anyone reading the base table (no access control) | ★★ | lecture4 L853-968 |
| C3.8 | INSTEAD OF triggers on views | Translate writes on a (read-only) view into writes on base tables | C2.9, C2.10, C3.1 | C5.4 | `CREATE TRIGGER n INSTEAD OF DELETE ON v FOR EACH ROW [WHEN cond] BEGIN ... END;` | soft-delete & re-insert through `current_collections` | forgetting the WHERE inside the trigger (updates every row); needing two INSERT triggers (exists / not exists) | ★★★★ | lecture4 L974-1336 |

### M4: Optimizing (lecture5)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C4.1 | Measuring queries; scans | `.timer on` reports real/user/sys time; without an index SQLite scans every row | C0.2 | C4.2 | `.timer on` | 'Cars' lookup: 0.084 s | optimizing without measuring | ★ | lecture5 L124-211 |
| C4.2 | Index + EXPLAIN QUERY PLAN | A separate sorted structure that lets SQLite *search* instead of *scan* | C4.1 | C4.3-C4.5 | `CREATE INDEX "title_index" ON "movies" ("title");` `EXPLAIN QUERY PLAN SELECT ...;` `DROP INDEX ...;` | 0.084 s → 0.01 s; plan shows `USING INDEX title_index` | indexing a column the query doesn't filter on; forgetting PKs already have one | ★★ | lecture5 L214-348 |
| C4.3 | Covering index | An index containing every column the query needs, so the table is never read | C4.2 | C0.5 | `CREATE INDEX "person_index" ON "stars" ("person_id", "movie_id");` | Tom Hanks query 0.197 s → 0.004 s | wrong column order (filter column must come first) | ★★★ | lecture5 L349-542 |
| C4.4 | B-trees & trade-offs | Indexes are balanced trees of sorted values + row pointers: fast lookups, but more space and slower writes | C4.2 | C4.6 | n/a | movie-title tree walkthrough | indexing every column "just in case" | ★★★ | lecture5 L543-861 |
| C4.5 | Partial index | An index over only the rows matching a WHERE | C4.2 | C3.6 | `CREATE INDEX "recents" ON "movies" ("title") WHERE "year" = 2023;` | used for `year = 2023`, not for `year = 1998` | expecting it to help queries outside its condition | ★★★ | lecture5 L862-942 |
| C4.6 | VACUUM | Return freed pages to the OS (deleting only marks space reusable) | C4.4 | | `VACUUM;` | 158 MB → 100 MB after dropping indexes | expecting DROP/DELETE alone to shrink the file | ★ | lecture5 L943-1042 |
| C4.7 | Transactions / ACID | A unit of work that happens entirely or not at all | C2.7, C1.7 | C4.8 | `BEGIN TRANSACTION; ...; COMMIT;` / `ROLLBACK;` | Alice pays Bob $10; CHECK(balance ≥ 0) forces ROLLBACK | ROLLBACK outside a transaction; forgetting to COMMIT | ★★★ | lecture5 L1049-1330 |
| C4.8 | Race conditions / isolation | Concurrent read-decide-write sequences can interleave and corrupt state; isolate them | C4.7 | C4.9 | (design) | Charlie's double transfer + Alice's ATM withdrawal | checking a balance outside the transaction that spends it | ★★★★ | lecture5 L1331-1455 |
| C4.9 | Locks | SQLite: UNLOCKED, SHARED (many readers), EXCLUSIVE (one writer, no readers) | C4.8 | | `BEGIN EXCLUSIVE TRANSACTION;` | second connection: `database is locked` | holding an exclusive lock longer than needed | ★★ | lecture5 L1456-1553 |

### M5: Scaling (lecture6)

| ID | Concept | Definition | Prereq | Related | Syntax | Example from the materials | Common mistakes | Diff | Source |
|---|---|---|---|---|---|---|---|---|---|
| C5.1 | Database servers | MySQL/PostgreSQL run as servers with users and their own CLIs | C1.1 | C5.7 | `mysql -u root -h 127.0.0.1 -P 3306 -p`; `SHOW DATABASES; USE x; SHOW TABLES; DESCRIBE t;` / `psql`, `\l`, `\c`, `\dt`, `\d t`, `\q` | creating `mbta` on both | using SQLite's double quotes for MySQL identifiers (MySQL uses backticks) | ★ | lecture6 L40-156, L159-352, L1288-1490 |
| C5.2 | MySQL types | Explicit, strict column types | C1.5 | C5.5 | `INT AUTO_INCREMENT`, `VARCHAR(32)`, `ENUM('a','b')`, `DATETIME`, `DECIMAL(5,2)` | cards / stations / swipes in MySQL | FLOAT for money; DECIMAL(M,D) misread (errata #7) | ★★ | lecture6 L183-852 |
| C5.3 | ALTER TABLE ... MODIFY | Redefine an existing column (MySQL) | C1.8, C5.2 | | `ALTER TABLE stations MODIFY line ENUM(...) NOT NULL;` | adding the silver line | omitting existing ENUM values or NOT NULL in the new definition | ★★ | lecture6 L853-923 |
| C5.4 | Stored procedures | Named, stored SQL routines with parameters (MySQL) | C2.7, C2.10 | C2.9 | `DELIMITER //` `CREATE PROCEDURE sell(IN sold_id INT) BEGIN ...; END//` `CALL sell(2);` | `current_collection`, `sell` | forgetting to change the delimiter; selling an already-sold item twice | ★★★ | lecture6 L947-1278 |
| C5.5 | PostgreSQL types | SERIAL, custom ENUM types, TIMESTAMP/INTERVAL, NUMERIC(p,s), MONEY | C5.2 | | `CREATE TYPE "swipe_type" AS ENUM ('enter','exit','deposit');` `DEFAULT now()` | Postgres swipes table | expecting MySQL-style inline ENUM | ★★ | lecture6 L1293-1477 |
| C5.6 | Scaling strategies | Vertical (bigger server) vs horizontal (more servers): replication (leader/follower, sync/async, read replicas), sharding | C5.1 | | (architecture) | profile-photo upload; names A-I / J-R / S-Z | async replication's data-loss risk; shard hotspots; single point of failure | ★★★★ | lecture6 L1494-1785 |
| C5.7 | Access control | Users and privileges | C5.1, C3.7 | | `CREATE USER 'carter' IDENTIFIED BY '...'; GRANT SELECT ON rideshare.analysis TO 'carter'; REVOKE ...` | analyst can read the view but not `rides` | `GRANT ALL ON *.*` in production | ★★ | lecture6 L1786-1920 |
| C5.8 | SQL injection & prepared statements | Untrusted input concatenated into SQL can change the query; bind it as a parameter instead | C0.2 | | `PREPARE s FROM 'SELECT ... WHERE id = ?'; SET @id = 1; EXECUTE s USING @id;` | `' OR 1=1`, `1 UNION SELECT * FROM accounts` | building SQL with string formatting (Python f-strings, L2138-2147) | ★★★ | lecture6 L1921-2148 |
