# M0 · Query toolkit (prerequisite)

> **Why this module exists.** The five lectures you provided (weeks 2-6) assume you can already read data with `SELECT`, filter, group, nest queries and join tables. Those were taught in weeks 0-1, which are **not** in your material set. This module is a compact refresher built only from queries that appear in your transcripts, so you can follow every later module.
> Datasets: `longlist`, `movies`, `mfa`, `votes`.

---

## C0.1 SELECT, FROM, LIMIT
*Source: lecture2 L38-48 · lecture5 L91-103*

**Level 1: Intuition.** A table is a grid. `SELECT` says which columns you want to see, and `FROM` says which grid. `LIMIT` says "just show me the first few", which is how the lecturer peeks at a 400,000-row table without flooding the screen.

**Level 2: SQL**
```sql
SELECT "title", "year"      -- columns to return (* = all)
FROM "books"                -- table to read
LIMIT 5;                    -- at most 5 rows
```
* Column and table names go in **double quotes** in SQLite (identifiers); text values go in **single quotes**.
* The statement ends with `;`, and the sqlite3 shell waits until it sees one.

**Level 3: Practical reasoning.** Peek with `LIMIT` before running anything heavy. Without `ORDER BY`, "the first five" is whatever order SQLite reads rows in. It is usually insertion order, but that is not guaranteed.

---

## C0.2 WHERE: filtering rows
*Source: lecture5 L116-123 (`=`) · lecture3 L734-741 (`IS NULL`) · lecture3 L798-808 (dates) · lecture3 L1374-1394 (`LIKE`)*

**Level 1: Intuition.** WHERE is a question asked of every row, and only rows answering "yes" stay.

**Level 2: SQL**
```sql
SELECT * FROM "movies" WHERE "title" = 'Cars';                 -- exact match
SELECT * FROM "collections" WHERE "acquired" IS NULL;          -- missing value
SELECT * FROM "collections" WHERE "acquired" < '1909-01-01';   -- YYYY-MM-DD text compares like dates
SELECT * FROM "votes" WHERE "title" LIKE 'Fa%';                -- pattern; % = any characters; case-insensitive
SELECT * FROM "books" WHERE "id" IN (21, 42);                  -- membership in a list
```

**Level 3: Practical reasoning**
* **NULL is "unknown"**. `= NULL` is never true, so use `IS NULL` / `IS NOT NULL`. A comparison with NULL (`NULL < '1909-01-01'`) is also not true, so such rows silently drop out of the result.
* `=` on text is exact and case-sensitive. `LIKE` ignores case (for ASCII) and supports `%` and `_`.
* Patterns can match more than you intended. The lecturer warns that `'Fa%'` is only safe on a tiny data set.

---

## C0.3 ORDER BY
*Source: lecture4 L317-330*

**Level 1.** Tables have no meaningful order. If order matters, ask for it.
**Level 2.** `SELECT "name", "title" FROM "longlist" ORDER BY "title";` Add `DESC` for descending, and list several columns to break ties.
**Level 3.** Always put `ORDER BY` on the *outer* query whose output you read. An ORDER BY inside a view is not a guarantee in standard SQL (errata #12).

---

## C0.4 Aggregates and GROUP BY
*Source: lecture4 L371-433 · lecture3 L1229-1256*

**Level 1: Intuition.** "Squash many rows into one number": the average rating of each book, or the number of votes for each title. GROUP BY decides *what each output row stands for*.

**Level 2: SQL**
```sql
SELECT "book_id", ROUND(AVG("rating"), 2) AS "rating"
FROM "ratings"
GROUP BY "book_id";
```
* `AVG`, `COUNT`, `SUM`, `MIN` and `MAX` compute over the rows of each group.
* `ROUND(x, 2)` keeps 2 decimals, and `AS` names the output column.

**Level 3: Practical reasoning**
* No GROUP BY means the whole table is one group, which yields one row (debugging D0-04).
* GROUP BY on text is **exact**. `'Spring Outing'` and `' spring outing'` are different groups, which is why the votes must be cleaned first (M2-E13).
* Keeping the raw individual ratings, rather than only averages, lets you compute other statistics later (min, max, median; L355-370).

---

## C0.5 Subqueries
*Source: lecture4 L127-192 · lecture5 L364-394*

**Level 1: Intuition.** Answer a question in steps. The answer to the inner question becomes part of the outer question. "Which titles … whose ids are among the books … written by the author whose name is Fernanda Melchor?"

**Level 2: SQL**
```sql
SELECT "title" FROM "books"
WHERE "id" IN (                              -- many rows → IN
    SELECT "book_id" FROM "authored"
    WHERE "author_id" = (                    -- exactly one row → =
        SELECT "id" FROM "authors"
        WHERE "name" = 'Fernanda Melchor'
    )
);
```
Read it **inside-out**. Indent each level (the lecturer uses 4 spaces per level) so you can see the structure.

**Level 3: Practical reasoning.** Use `IN` whenever the subquery may return several rows. With `=`, SQLite silently takes the first row (debugging D0-05). Subqueries avoid hard-coding ids like 24, so the query keeps working if ids change. Lecture 3 uses the same pattern inside `DELETE` and `UPDATE`.

---

## C0.6 JOIN … ON
*Source: lecture4 L59-73 (visual), L202-240 (SQL)*

**Level 1: Intuition.** Line two tables up side by side wherever a primary key in one equals a foreign key in the other, "touching your fingertips together" (L68).

**Level 2: SQL**
```sql
SELECT "name", "title"
FROM "authors"
JOIN "authored" ON "authors"."id" = "authored"."author_id"   -- PK = FK
JOIN "books"    ON "books"."id"   = "authored"."book_id";    -- PK = FK
```

**Level 3: Practical reasoning**
* A many-to-many relationship always needs **two** joins through the junction table.
* Joining on the wrong pair of columns usually *doesn't error*. It just returns wrong rows, because ids from different tables share numbers (debugging D0-02).
* Joining to the "many" side (e.g. ratings) repeats the "one" side once per match (debugging D0-03).
* JOIN vs subquery: both work. Lecture 4 shows the JOIN, saved as a view, is far easier to reuse.

**Practice:** M0-E01 … M0-E10 · **Debug:** D0-01 … D0-06 · **Review deck:** R0
