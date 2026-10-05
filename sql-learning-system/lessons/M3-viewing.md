# M3 · Viewing
*Source: lecture4 (Week 4 · Viewing). Datasets: `longlist`, `rideshare`, `mfa`.*

Story: three joined tables make simple questions painful. A **view** saves a query as a virtual table, which can simplify, aggregate, partition and secure data, and with triggers it can even accept writes.

---

## C3.1 What a view is
*Source: lecture4 L77-104, L244-278, L653-658*

**Level 1: Intuition.** A view is a saved question that you can treat like a table. Each time you look at it, the question is asked again, so the answer is always current and almost no extra space is used.

**Level 2.**
```sql
CREATE VIEW "longlist" AS
SELECT "name", "title" FROM "authors"
JOIN "authored" ON "authors"."id" = "authored"."author_id"
JOIN "books" ON "books"."id" = "authored"."book_id";

SELECT * FROM "longlist";      -- query it like a table
DROP VIEW "longlist";
```
`.schema` lists views alongside tables (L271-273).

**Level 3.** A view is not a copy. New ratings appear in an aggregate view immediately (L514-526). In SQLite, views are read-only (C3.8 shows the workaround).

---

## C3.2 Views to simplify
*Source: lecture4 L106-336*

**Level 1.** Write the complicated join once, then ask simple questions.

**Level 2.** Before: a three-level nested subquery (M0-E08). After: `SELECT "title" FROM "longlist" WHERE "name" = 'Fernanda Melchor';`

**Level 3.** Keep the columns you may need later. The `longlist` view dropped the ids, so it can't be joined to `ratings` (L502-510). Sort in the outer query (`… ORDER BY "title"`) rather than relying on an ORDER BY inside the view (errata #12).

---

## C3.3 Views to aggregate, and views on views
*Source: lecture4 L337-526, L554-603*

**Level 2.**
```sql
CREATE VIEW "average_book_ratings" AS
SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
FROM "ratings" JOIN "books" ON "ratings"."book_id" = "books"."id"
GROUP BY "book_id";
```
A view can be the FROM of another view, for example averages by year built on averages by book.

**Level 3.** Store raw data (individual ratings) and expose summaries through views, not the other way round. You keep the ability to compute other statistics later (L355-370). The "average of averages" by year weights each *book* equally, not each rating. Know which one you mean.

---

## C3.4 Temporary views
*Source: lecture4 L527-632*

**Level 2.** `CREATE TEMPORARY VIEW "average_ratings_by_year" AS …;` lasts only until the connection closes (`.quit`).

**Level 3.** Use it for one session's analysis or to test a view before making it permanent (L615-630). A developer who wants the view part of the database uses plain `CREATE VIEW`.

---

## C3.5 Common table expressions (CTEs)
*Source: lecture4 L633-708*

**Level 1.** A view that exists for a single query.

**Level 2.**
```sql
WITH "average_book_ratings" AS (
    SELECT "book_id", "title", "year", ROUND(AVG("rating"), 2) AS "rating"
    FROM "ratings" JOIN "books" ON "ratings"."book_id" = "books"."id"
    GROUP BY "book_id"
)                                   -- more CTEs: "), name2 AS ( … )"
SELECT "year", ROUND(AVG("rating"), 2) AS "rating"
FROM "average_book_ratings"
GROUP BY "year";
```

**Level 3.** Lifetimes: VIEW lasts until dropped, TEMPORARY VIEW until the connection closes, CTE for one statement. CTEs name intermediate steps, avoid repeating subqueries, and read top to bottom instead of inside-out. Don't put a comma after the last CTE (D3-01).

---

## C3.6 Views to partition
*Source: lecture4 L709-852*

**Level 2.** `CREATE VIEW "2022" AS SELECT "id", "title" FROM "books" WHERE "year" = 2022;`. Names made of digits need quotes (D3-03).

**Level 3.** Partitions suit applications that only ever need one slice of the data (a page per year). Naming is a trade-off between `"2021"` (short, ambiguous) and `books_nominated_in_2021` (clear, long). A single view with a WHERE added at query time is the alternative (L797-811).

---

## C3.7 Views to secure
*Source: lecture4 L853-973*

**Level 2.**
```sql
CREATE VIEW "analysis" AS
SELECT "id", "origin", "destination", 'anonymous' AS "rider"
FROM "rides";
```
A literal column tells the reader that the data exists but has been withheld.

**Level 3.** Expose only what someone needs to know (PII such as rider names stays hidden). **In SQLite this is cosmetic.** Whoever has the file can still `SELECT * FROM "rides"`, because SQLite has no access control. MySQL and PostgreSQL enforce it with `GRANT` (C5.7). Also beware linking ids back to the base table (L952-956).

---

## C3.8 Writing through a view: INSTEAD OF triggers
*Source: lecture4 L974-1336*

**Level 1: Intuition.** The view `current_collections` hides soft-deleted items. People want to `DELETE` from it or `INSERT` into it as if it were a table. INSTEAD OF triggers intercept those writes and translate them into the right change on `collections`.

**Level 2.**
```sql
CREATE VIEW "current_collections" AS
SELECT "id", "title", "accession_number", "acquired" FROM "collections" WHERE "deleted" = 0;

CREATE TRIGGER "delete"                      -- quoted: delete is a keyword
INSTEAD OF DELETE ON "current_collections"
FOR EACH ROW
BEGIN
    UPDATE "collections" SET "deleted" = 1 WHERE "id" = OLD."id";
END;

CREATE TRIGGER "insert_when_exists"
INSTEAD OF INSERT ON "current_collections"
FOR EACH ROW
WHEN NEW."accession_number" IN (SELECT "accession_number" FROM "collections")
BEGIN
    UPDATE "collections" SET "deleted" = 0 WHERE "accession_number" = NEW."accession_number";
END;
```
A third trigger (`WHEN … NOT IN …`) inserts genuinely new items. The lecture assigns it to you (M3-E13).

**Level 3**
* Without `WHERE "id" = OLD."id"`, one DELETE soft-deletes every row (D3-02).
* Match on the natural key (the accession number) for inserts, because the inserted view row has no `id` yet.
* Two triggers with complementary `WHEN` conditions cover both cases. Make sure every possible insert matches exactly one of them.
* Lecture 6 implements the same soft-delete idea with a MySQL stored procedure (C5.4).

**Practice:** M3-E01 … M3-E13 · **Debug:** D3-01 … D3-03 · **Review deck:** R3
