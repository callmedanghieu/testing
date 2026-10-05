# M4 · Optimizing
*Source: lecture5 (Week 5 · Optimizing). Datasets: `movies` (IMDb sample; `--big` for timing), `bank`.*

Story: IMDb has 400k movies, and every search costs server time multiplied by many users. Indexes trade **space** for **time**. Then the second half: many users at once, where transactions and locks keep the data consistent.

---

## C4.1 Measuring: .timer and scans
*Source: lecture5 L124-211*

**Level 1.** Measure before optimizing. Without help, SQLite answers `WHERE "title" = 'Cars'` by looking at every row, top to bottom. That is a **scan** (linear search).

**Level 2.** `.timer on` in the shell prints `real` (stopwatch time), `user` (CPU time spent on your query) and `sys` (time in the operating system) after each statement.

**Level 3.** 0.084 s seems fast until thousands of users run it every minute and you pay per second of server time (L153-168). Focus on `real`.

---

## C4.2 Indexes and EXPLAIN QUERY PLAN
*Source: lecture5 L214-348*

**Level 1: Intuition.** Like a textbook's index, a database index is a separate, **sorted** list of a column's values with pointers back to the rows. Find "Cars" in the sorted list quickly, then jump to the row.

**Level 2.**
```sql
CREATE INDEX "title_index" ON "movies" ("title");
EXPLAIN QUERY PLAN SELECT * FROM "movies" WHERE "title" = 'Cars';
-- QUERY PLAN
-- `--SEARCH movies USING INDEX title_index (title=?)
DROP INDEX "title_index";
-- `--SCAN movies
```

**Level 3**
* Read plans from the innermost subquery outward. **SCAN** means reading everything, and **SEARCH** means using an index.
* **Primary keys are indexed automatically** (`USING INTEGER PRIMARY KEY`). Other columns aren't (L338-348).
* Index the columns your WHERE clauses (and joins) filter on. An index on another column does nothing (D4-02).
* Indexes appear in `.schema` (L929-941).

---

## C4.3 Multi-column and covering indexes
*Source: lecture5 L349-542*

**Level 1.** If the index itself contains everything the query needs, SQLite never has to visit the table. Answering from the book's index without turning to the pages is the fastest case.

**Level 2.**
```sql
CREATE INDEX "name_index"   ON "people" ("name");
CREATE INDEX "person_index" ON "stars"  ("person_id", "movie_id");
-- SEARCH people USING COVERING INDEX name_index (name=?)
-- SEARCH stars  USING COVERING INDEX person_index (person_id=?)
-- SEARCH movies USING INTEGER PRIMARY KEY (rowid=?)
```

**Level 3.** Column order matters. The column you filter on must come **first** (`person_id`), and the extra column (`movie_id`) rides along for coverage (D4-01). On the full IMDb data: 0.197 s → 0.004 s. `name_index` is covering on its own because every index entry also stores the rowid, which here is `people.id`.

---

## C4.4 B-trees and the cost of indexes
*Source: lecture5 L543-861*

**Level 1.** Sorting the table itself would break the ids that other tables rely on (L626-648). So the index is a sorted **copy** of the column, plus row pointers, split into nodes that form a balanced tree: a root node, inner nodes, and leaves.

**Level 2 (the search).** Looking for *Turning Red*: at the root, is it before *Frozen*? No. Before *Soul*? No. So go to the last child node, then find *Turning Red* in it, along with its row number. Each step discards most of the remaining candidates (binary-search style), so even millions of rows take only a few steps.

**Level 3: Trade-offs**
* **Space:** an index is extra data ("paying in pages", L558-563).
* **Write time:** every INSERT/UPDATE/DELETE must also update every affected index, finding the right place in the tree (L852-861).
* So don't index every column "just in case" (L350-357). Index what your real queries need.

---

## C4.5 Partial indexes
*Source: lecture5 L862-942*

**Level 2.** `CREATE INDEX "recents" ON "movies" ("title") WHERE "year" = 2023;`

**Level 3.** A smaller index, useful when most queries target a known subset (this year's movies). SQLite uses it only when the query's WHERE implies the index's WHERE (`year = 2023`). For `year = 1998` it is back to a scan (D4-03).

---

## C4.6 VACUUM
*Source: lecture5 L943-1048*

**Level 1.** Deleting rows or dropping an index doesn't shrink the file. The space is only marked as reusable. `VACUUM;` rebuilds the file and returns the free pages to the operating system.

**Level 2.** `du -b movies.db` (Unix, size in bytes) → `DROP INDEX …` (same size) → `VACUUM;` → smaller. The lecture went from 158 MB to 100 MB. Try `python3 tools/labs.py vacuum`.

**Level 3.** VACUUM rewrites the whole database, which takes time on big files. Run it occasionally, after large deletions. Once vacuumed, the deleted bytes are no longer recoverable from the file (L1031-1041).

---

## C4.7 Transactions and ACID
*Source: lecture5 L1049-1330*

**Level 1: Intuition.** Alice pays Bob $10 in two updates. Between them, an observer sees $70 in a $60 bank. A transaction makes the pair happen **all at once or not at all**.

**Level 2.**
```sql
BEGIN TRANSACTION;
UPDATE "accounts" SET "balance" = "balance" + 10 WHERE "id" = 2;
UPDATE "accounts" SET "balance" = "balance" - 10 WHERE "id" = 1;
COMMIT;                 -- save; or ROLLBACK; to undo everything since BEGIN
```
ACID:
* **Atomicity**, all or nothing.
* **Consistency**, constraints hold. Here `CHECK("balance" >= 0)` makes the debit fail, and you ROLLBACK.
* **Isolation**, concurrent transactions don't interfere.
* **Durability**, committed data survives crashes.

**Level 3**
* ROLLBACK works only inside a transaction. Without BEGIN you must undo by hand (L1289-1305, D4-04).
* In SQLite a failed statement does **not** end the transaction. You decide to COMMIT or ROLLBACK.
* Identify accounts by id, not name, since there can be two Alices (L1239-1248).

---

## C4.8 Race conditions and isolation
*Source: lecture5 L1331-1455*

**Level 1.** Charlie ($30) clicks *transfer $30 to Alice* on two laptops at once. Both transfers check his balance before either one subtracts, so Alice receives $60 and withdraws it at an ATM.

**Level 2.** The fix is design: each transfer (check, credit, debit) is **one transaction**, and transactions run **sequentially (isolated)**. The second transfer then sees $0, fails its constraint, and rolls back.

**Level 3.** Any "read a value, decide, then write" sequence is vulnerable if the read happens outside the transaction that writes. Real systems serialize with locks (C4.9), possibly with timestamp ordering (L1509-1523).

---

## C4.9 Locks
*Source: lecture5 L1456-1553*

| SQLite lock | Meaning |
|---|---|
| UNLOCKED | nobody is using the database |
| SHARED | reading; many connections may hold it at once |
| EXCLUSIVE | writing; no one else may read or write |

`BEGIN EXCLUSIVE TRANSACTION;` takes the exclusive lock up front. Another connection then gets `Runtime error: database is locked`. Run `python3 tools/labs.py locks` to see it.

**Level 3.** SQLite locks the **whole database** (coarse granularity). Other DBMSs can lock tables or rows. Hold exclusive locks as briefly as possible, since everyone else waits.

**Practice:** M4-E01 … M4-E11 · **Debug:** D4-01 … D4-04 · **Review deck:** R4
