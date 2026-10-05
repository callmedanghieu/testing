# M2 · Writing
*Source: lecture3 (Week 3 · Writing). Datasets: `mfa` (Museum of Fine Arts), `votes`. CSVs: `database/csv/`.*

Story: the MFA logs new acquisitions (INSERT), imports a CSV, sells pieces (DELETE) despite foreign keys, corrects attributions and cleans messy vote data (UPDATE), automates a sales log (TRIGGER), and finally keeps history with soft deletes.

---

## C2.1 INSERT INTO
*Source: lecture3 L65-246*

**Level 1.** Add a new row: say where, which columns, and what values.

**Level 2.**
```sql
INSERT INTO "collections" ("title", "accession_number", "acquired")
VALUES ('Spring Outing', '14.76', '1914-01-08');
```
* Value *n* goes into column *n*. You may list columns in any order, as long as the values match (L612-630).
* Leave out an `INTEGER PRIMARY KEY` and SQLite assigns **max(id) + 1**.

**Level 3**
* Let the database generate ids. Choosing them yourself risks collisions.
* Gaps after deletes are normal. Without AUTOINCREMENT, a deleted *maximum* id can be reused. With AUTOINCREMENT, an id is never reused (the lecture states this backwards, errata #2).
* Quote identifiers that look numeric (`'06.1899'`), or the leading zero is lost (errata #5).

---

## C2.2 Constraints at write time
*Source: lecture3 L247-312*

**Level 1.** The constraints you designed in M1 now *refuse* bad writes.

**Level 2.** `Runtime error: UNIQUE constraint failed: collections.accession_number` and `NOT NULL constraint failed: collections.title`. Nothing is written.

**Level 3.** Read the error message. It names the constraint and the column, and it means a guardrail worked, not that SQL is broken.

---

## C2.3 Multi-row INSERT and INSERT … SELECT
*Source: lecture3 L313-364, L570-603, L632-638*

**Level 2.**
```sql
INSERT INTO "collections" ("title", "accession_number", "acquired") VALUES
('Imaginative Landscape', '56.496', NULL),
('Peonies and Butterfly', '06.1899', '1906-01-01');

INSERT INTO "collections" ("title", "accession_number", "acquired")
SELECT "title", "accession_number", "acquired" FROM "temp";
```

**Level 3.** A multi-row insert is faster than many single inserts and **atomic**: if one row violates a constraint, no row is inserted. That is the first glimpse of transactions (M4). With `INSERT … SELECT`, the column lists must line up by position.

---

## C2.4 Importing CSV files
*Source: lecture3 L381-663*

**Level 1.** You often receive data as a CSV (comma-separated values). The sqlite3 shell can load it directly.

**Level 2.**
```text
.import --csv --skip 1 mfa.csv collections   -- table exists: skip the header row
.import --csv mfa_noid.csv temp              -- table doesn't exist: header becomes column names
```
then `INSERT INTO "collections" (...) SELECT ... FROM "temp";` and `DROP TABLE "temp";`

**Level 3**
* `.import` is a shell command, so it doesn't run in the browser trainer. Try it in the terminal with `database/csv/*.csv`, or let `tools/labs.py import` run it for you.
* Importing into a new table makes **every column TEXT**, and **blank fields become `''`, not NULL** (L640-663). Fix them with `NULLIF(col, '')` or `UPDATE … SET col = NULL WHERE col = ''`.
* Prefer CSVs without ids, and let the table generate the primary keys (L501-515).

---

## C2.5 DELETE
*Source: lecture3 L670-819*

**Level 1.** Remove the rows that match a condition.

**Level 2.**
```sql
DELETE FROM "collections" WHERE "title" = 'Spring Outing';
DELETE FROM "collections" WHERE "acquired" IS NULL;
DELETE FROM "collections" WHERE "acquired" < '1909-01-01';
```

**Level 3**
* `DELETE FROM t;` with no WHERE deletes **everything** (D2-01). First run the same WHERE as a SELECT.
* Choose the condition that expresses your *intent*. "Acquired before 1909" should use the date, not `id >= 5`, which only matches by coincidence (L783-792).
* Rows whose date is NULL are not "before 1909", so they survive the date DELETE.

---

## C2.6 Foreign keys when deleting
*Source: lecture3 L820-1052*

**Level 1.** If `created` says *artist 3 painted artwork 1*, deleting artist 3 would leave a reference to nobody. The database stops you, unless you declare what should happen instead.

**Level 2.**
```sql
FOREIGN KEY("artist_id") REFERENCES "artists"("id") ON DELETE CASCADE
```

| Action | Effect when the referenced row is deleted |
|---|---|
| RESTRICT | refuse the delete |
| NO ACTION | no *special* action, but the foreign-key check still runs, so the delete **fails** (the lecture says it would be allowed; errata #18) |
| SET NULL | referencing column becomes NULL |
| SET DEFAULT | referencing column gets its default |
| CASCADE | referencing rows are deleted too |

Without an action, delete in two steps, children first:
```sql
DELETE FROM "created" WHERE "artist_id" = (SELECT "id" FROM "artists" WHERE "name" = 'Unidentified artist');
DELETE FROM "artists" WHERE "name" = 'Unidentified artist';
```

**Level 3.** CASCADE is convenient but powerful, since one DELETE can remove many rows in other tables. Use it where the child rows mean nothing without the parent, as with authorship links. The lecturer's first attempt deleted from the wrong table (D2-02).

---

## C2.7 UPDATE
*Source: lecture3 L1093-1196*

**Level 2.**
```sql
UPDATE "created"
SET "artist_id" = (SELECT "id" FROM "artists" WHERE "name" = 'Li Yin')
WHERE "collection_id" = (SELECT "id" FROM "collections" WHERE "title" = 'Farmers Working at Dawn');
```
`SET` may list several `col = value` pairs. Values can be expressions or subqueries.

**Level 3.** As with DELETE, a forgotten WHERE changes every row (D2-03). To fix a typo, UPDATE the row (L369-380). Never delete and re-insert it.

---

## C2.8 Cleaning data
*Source: lecture3 L1197-1486*

**Level 1.** Twenty typed votes give far more than four groups, because of stray spaces, inconsistent capitals and typos. Clean systematically, re-checking with GROUP BY after each step.

**Level 2.**
```sql
UPDATE "votes" SET "title" = trim("title");     -- leading/trailing whitespace
UPDATE "votes" SET "title" = upper("title");    -- one capitalization
UPDATE "votes" SET "title" = 'FARMERS WORKING AT DAWN' WHERE "title" LIKE 'Fa%';
UPDATE "votes" SET "title" = 'IMAGINATIVE LANDSCAPE' WHERE "title" = 'IMAGINTIVE LANDSCAPE';
```
Other scalar functions: `lower()`, `length()`, `replace()`, `substr()`, … (search "SQLite scalar functions", L1464-1468).

**Level 3.** Go from broad fixes (all rows) to narrow ones. Make patterns as specific as the data allows, because `'Fa%'` would also rewrite a *Fan Painting* (D2-06). An alternative is to keep the raw titles and add a category column (L1471-1486).

---

## C2.9 Triggers
*Source: lecture3 L1494-1693*

**Level 1.** "Whenever X happens to this table, also do Y", automatically, for every affected row.

**Level 2.**
```sql
CREATE TRIGGER "sell"
BEFORE DELETE ON "collections"
FOR EACH ROW
BEGIN
    INSERT INTO "transactions" ("title", "action") VALUES (OLD."title", 'sold');
END;
```
* Timing: `BEFORE` / `AFTER`. Event: `INSERT`, `UPDATE OF column`, or `DELETE` (`INSTEAD OF` comes in M3).
* `OLD.col` is the row before the change (UPDATE, DELETE). `NEW.col` is the row after (INSERT, UPDATE).
* The body may hold several statements, each ending with `;` (L1688-1693).

**Level 3.** Triggers keep logs and derived tables in sync without relying on every program to remember. The cost is hidden behaviour, so name triggers clearly and document them in `schema.sql`. A trigger that references `NEW` on DELETE is accepted when created but fails on every delete (D2-05).

---

## C2.10 Soft deletion
*Source: lecture3 L1694-1793*

**Level 2.**
```sql
ALTER TABLE "collections" ADD COLUMN "deleted" INTEGER DEFAULT 0;
UPDATE "collections" SET "deleted" = 1 WHERE "title" = 'Farmers Working at Dawn';
SELECT * FROM "collections" WHERE "deleted" = 0;      -- every query must remember this filter
```

**Level 3.** History is preserved and recoverable. The cost is that every query must filter, which motivates the view in M3. The ethical question: for personal data, a soft delete may not honour "the right to be forgotten" (GDPR). Decide case by case.

**Practice:** M2-E01 … M2-E15 · **Debug:** D2-01 … D2-06 · **Review deck:** R2
