# M0 · Querying
*Source: lecture0 (Week 0 · Querying). Dataset: `longlist0`, a single `longlist` table of the 78 books longlisted for the International Booker Prize, 2018-2023.*

Story: a librarian and an avid reader want answers from one table of books. Which ones are from 2023? Which aren't hardcover? Which have "love" in the title? What are the ten best rated? Every question becomes a query.

---

## C0.1 Databases, DBMSs and SQL
*Source: lecture0 L28-169*

**Level 1: Intuition.** A table is a very old idea (rows = items, columns = attributes). Spreadsheets hold tables too. A **database** adds scale (millions of rows), frequent updates, and fast search. A **DBMS** (database management system) is the program you talk to: SQLite, MySQL, PostgreSQL, Oracle and others. **SQL**, the Structured Query Language, is the language you talk in. With it you **c**reate, **r**ead, **u**pdate and **d**elete data (CRUD).

**Level 2.** `sqlite3 longlist.db` opens a database file. The prompt changes to `sqlite>`, and you can type SQL ending in `;`. `.quit` leaves.

**Level 3.** Trade-offs between DBMSs (L132-154): proprietary systems come with support, while open-source ones are free but you run them yourself. MySQL and PostgreSQL are heavier and more featureful, while SQLite is light and everywhere (phones, desktop apps, websites). This course starts in SQLite and reaches MySQL and PostgreSQL in M6.

---

## C0.2 SELECT and FROM
*Source: lecture0 L251-360*

**Level 1.** "Show me these columns of that table."

**Level 2.**
```sql
SELECT * FROM "longlist";                  -- every column
SELECT "title", "author" FROM "longlist";  -- just two
```
* **Identifiers** (table and column names) go in **double quotes**. **Strings** go in **single quotes** (L304-315).
* Write SQL keywords in UPPERCASE. It isn't required, but it makes long queries readable (L338-360).

**Level 3.** Select only the columns you need. In SQLite, a double-quoted name that matches no column is silently treated as a *string*, so a typo like `"pubsliher"` prints the word instead of an error (L1363-1377, debugging D0-03).

---

## C0.3 LIMIT
*Source: lecture0 L366-396*

`SELECT "title" FROM "longlist" LIMIT 5;` returns at most 5 rows. Use it to peek. Without ORDER BY you get the rows "in whatever order they were added". That is fine for a peek, but don't rely on it for anything else.

---

## C0.4 WHERE, not-equals and NOT
*Source: lecture0 L397-515*

**Level 1.** Ask a yes/no question of every row, and keep the "yes" rows.

**Level 2.**
```sql
SELECT "title", "author" FROM "longlist" WHERE "year" = 2023;
SELECT "title", "format" FROM "longlist" WHERE "format" != 'hardcover';   -- also: <>
SELECT "title", "format" FROM "longlist" WHERE NOT "format" = 'hardcover';
```
Numbers are not quoted (`2023`), and strings are (`'hardcover'`).

**Level 3.** `!=` and `<>` are identical, and `!=` is more common. NOT negates a whole condition, which helps when the condition is complex.

---

## C0.5 AND, OR and parentheses
*Source: lecture0 L517-564*

```sql
SELECT "title", "format" FROM "longlist"
WHERE ("year" = 2022 OR "year" = 2023) AND "format" != 'hardcover';
```
**Level 3.** AND is evaluated before OR. Without the parentheses the query means `2022 OR (2023 AND not hardcover)` and lets 2022 hardcovers through (D0-02). Long queries can continue on the next line; the shell waits for the `;`.

---

## C0.6 NULL
*Source: lecture0 L587-633*

**Level 1.** NULL means "no value here", not zero and not an empty string.

**Level 2.** `WHERE "translator" IS NULL` finds the 2 books without a translator, and `IS NOT NULL` finds the others.

**Level 3.** `= NULL` is never true (D0-01). Aggregates such as `COUNT("translator")` skip NULLs, which is why it returns 76 while `COUNT(*)` returns 78 (C0.10).

---

## C0.7 LIKE, % and _
*Source: lecture0 L638-830, L951-971*

| Pattern | Matches |
|---|---|
| `'%love%'` | "love" anywhere (Love in the Big City, More Than I Love My Life, …) |
| `'The %'` | starts with the word "The" |
| `'P_re'` | P + one character + re → Pyre |
| `'T___'` | T + exactly three characters → Tyll |

**Level 3.** `LIKE` ignores case for ASCII letters, while `=` is case-sensitive (`= 'pyre'` finds nothing). Make patterns as specific as your intent. `'The%'` also matches "There…" and "They…".

---

## C0.8 Ranges and BETWEEN
*Source: lecture0 L834-930*

```sql
WHERE "year" >= 2019 AND "year" <= 2022
WHERE "year" BETWEEN 2019 AND 2022          -- inclusive at both ends
WHERE "rating" > 4.0 AND "votes" > 10000     -- 4 books
WHERE "pages" < 300
```
**Level 3.** Replace chains of `OR "year" = …` with a range (the lecturer calls the OR chain badly designed). You need to know a column's type to compare it well. Here year and votes are integers and rating is a real number (L937-950).

---

## C0.9 ORDER BY
*Source: lecture0 L976-1130*

```sql
SELECT "title", "rating", "votes" FROM "longlist"
ORDER BY "rating" DESC, "votes" DESC
LIMIT 10;
```
* The default is **ASC** (smallest first). The lecturer's first "top 10" showed the worst books (3.05 … 3.42).
* A second key breaks ties. *When We Cease to Understand the World* and *Still Born* both have 4.14, and votes decide their order.
* On text, ASC means A→Z and DESC means Z→A.

---

## C0.10 Aggregate functions, ROUND and AS
*Source: lecture0 L1131-1343*

```sql
SELECT ROUND(AVG("rating"), 2) AS "average rating" FROM "longlist";   -- 3.75
SELECT MAX("rating"), MIN("rating"), SUM("votes") FROM "longlist";    -- 4.52, 3.05, > 600,000
SELECT COUNT(*), COUNT("translator") FROM "longlist";                  -- 78, 76
```
**Level 1.** An aggregate turns many rows into one value. `ROUND(x, 2)` tidies the number, and `AS` gives the column a readable name.
**Level 3.** `COUNT(*)` counts rows, while `COUNT(column)` counts non-NULL values. On text, MAX and MIN compare **alphabetically**, not by length: MAX = *Wretchedness*, MIN = *A New Name…* (the lecture misspeaks here, see errata #19). Per-group aggregates (GROUP BY) come in M1.

---

## C0.11 DISTINCT
*Source: lecture0 L1344-1401*

`SELECT DISTINCT "publisher" FROM "longlist";` lists each publisher once, and `SELECT COUNT(DISTINCT "publisher") FROM "longlist";` counts them. Plain `COUNT("publisher")` counts a publisher once per book (D0-04).

**Practice:** M0-E01 … M0-E18 · **Debug:** D0-01 … D0-04 · **Review deck:** R0
