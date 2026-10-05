# M1 · Relating
*Source: lecture1 (Week 1 · Relating). Datasets: `longlist` (authors, books, publishers, translators, authored, translated, ratings) and `sea_lions` (sea_lions, migrations).*

Story: the single table of M0 repeats authors and can't say which book has which ratings. Splitting it into related tables fixes that, and then you need subqueries, JOINs, sets and groups to ask questions across tables.

---

## C1.1 Relational databases and relationships
*Source: lecture1 L48-146*

**Level 1.** Put authors in one table and books in another. Now you need a reliable way to say *who wrote what*. The "honor system" (row 1 of authors goes with row 1 of books) breaks the first time someone adds a row to only one table (L70-83). One big table repeats Olga Tokarczuk once per book (L90-106).

**Level 2: the three relationships.**

| Relationship | Meaning | Example |
|---|---|---|
| one-to-one | each A has exactly one B, and vice versa | (a simplifying assumption the lecture rejects) |
| one-to-many | one A has many B, each B has one A | a book has many ratings; a publisher, many books |
| many-to-many | A has many B, and B has many A | authors ↔ books, translators ↔ books |

**Level 3.** Choosing the relationship is a design decision (L220-235). Lecture 2 makes you choose (M2).

---

## C1.2 ER diagrams
*Source: lecture1 L147-246*

Entities are boxes, relationships are lines labelled with verbs (*wrote*, *published*, *translated*), and the line ends carry **crow's-foot** marks:

| Mark | Meaning |
|---|---|
| circle | zero (optional) |
| bar | one (at least one) |
| three-pronged foot | many |

Read each line in both directions: "an author wrote one to many books" and "a book was written by one to many authors". A book can have *zero* to many translators.

---

## C1.3 Primary keys and foreign keys
*Source: lecture1 L247-482*

**Level 1.** A librarian can't find "The Birthday Party" by title alone, because there are several books with that name and several editions. A unique number solves it.

**Level 2.**
* **Primary key**: unique for every row of its table (`books.id`).
* **Foreign key**: a primary key copied into another table to point at a row (`ratings.book_id` → `books.id`).
* **Many-to-many** needs a junction table: `authored(author_id, book_id)`. The row `(23, 1)` means author 23 (Eva Baltasar) wrote book 1 (*Boulder*).

**Level 3.** The ISBN is unique, but it is a poor key. As text it is about 17 bytes copied into every referencing row, and as a number it loses leading zeros. A made-up integer id is small and stable. Ids from different tables may share values (author 1 and book 1 are fine) because each column knows which table it refers to (L419-438). Avoid changing ids (L465-481).

---

## C1.4 Subqueries
*Source: lecture1 L491-861*

**Level 1.** Answer in steps. First find Fitzcarraldo Editions' id, then the books with that publisher id.

**Level 2.**
```sql
SELECT "title" FROM "books" WHERE "publisher_id" = (
    SELECT "id" FROM "publishers" WHERE "publisher" = 'Fitzcarraldo Editions'
);

SELECT "name" FROM "authors" WHERE "id" = (            -- many-to-many: three tables
    SELECT "author_id" FROM "authored" WHERE "book_id" = (
        SELECT "id" FROM "books" WHERE "title" = 'The Birthday Party'
    )
);
```
The innermost query runs first. Indent each level for readability. Indentation is not required, but it is good style (L945-967).

**Level 3.** A subquery replaces hard-coded ids (`= 5`) that break silently. If the inner query finds nothing, the outer one returns nothing too (L603-610). The wrong table name gives `no such table` (D1-06).

---

## C1.5 IN
*Source: lecture1 L862-985*

```sql
SELECT "title" FROM "books" WHERE "id" IN (
    SELECT "book_id" FROM "authored" WHERE "author_id" = (
        SELECT "id" FROM "authors" WHERE "name" = 'Fernanda Melchor'
    )
);
```
Rule of thumb: use `=` when exactly one value can come back, and `IN` when it may be several. A foreign key may repeat in a junction table (a book with three authors has three rows), but a primary key never repeats (L987-1020).

---

## C1.6 JOIN … ON
*Source: lecture1 L1022-1162*

**Level 1.** Extend each row of one table with the matching row of another, where the keys line up.

**Level 2.**
```sql
SELECT * FROM "sea_lions"
JOIN "migrations" ON "migrations"."id" = "sea_lions"."id";
```
**Level 3.** A plain JOIN is an **INNER JOIN**. Rows without a match on the other side are dropped (Jolee disappears). The result is a temporary result set; it isn't stored (L1357-1379). For a many-to-many query, join through the junction table: authors JOIN authored JOIN books (M1-E13).

---

## C1.7 OUTER JOINs: LEFT, RIGHT, FULL
*Source: lecture1 L1208-1379*

| Join | Keeps unmatched rows from | sea lions example |
|---|---|---|
| `LEFT JOIN` | the left table (written first) | Jolee kept, with NULL distance |
| `RIGHT JOIN` | the right table (after JOIN) | untracked migrations kept, with NULL name |
| `FULL JOIN` | both | everything |

With several joins, each JOIN's left side is everything to its left (L1340-1355). RIGHT and FULL JOIN need SQLite 3.39 or newer.

---

## C1.8 NATURAL JOIN
*Source: lecture1 L1380-1404*

`SELECT * FROM "sea_lions" NATURAL JOIN "migrations";` joins on every column with the same name (here `id`) and shows it only once. It is short but fragile, so prefer an explicit `ON` in real code. When the key columns have different names, write `ON a.x = b.y` (L1626-1638).

---

## C1.9 Sets: UNION, INTERSECT, EXCEPT
*Source: lecture1 L1408-1663*

| Operator | Venn region | Example |
|---|---|---|
| `UNION` | in either | all authors and translators (add `'author' AS "profession"` to label) |
| `INTERSECT` | in both | Ngũgĩ wa Thiong'o; the book Hughes and Jull Costa both translated |
| `EXCEPT` | in the first, not the second | authors who are not translators |

**Level 3.** Both sides need the same number of columns (and the same kind of data). Chained operators run left to right, so the lecture's homework, *in exactly one set*, needs subqueries (M1-E18). UNION removes duplicates, and UNION ALL keeps them.

---

## C1.10 GROUP BY and HAVING
*Source: lecture1 L1664-1839*

```sql
SELECT "book_id", ROUND(AVG("rating"), 2) AS "average rating"
FROM "ratings"
GROUP BY "book_id"
HAVING "average rating" > 4.0
ORDER BY "average rating" DESC;
```
**Level 1.** GROUP BY collapses the rows of each book into one, and the aggregate is computed per group.
**Level 2.** Clause order: `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT`.
**Level 3.** WHERE filters **rows** before grouping, and HAVING filters **groups** after (D1-07). Without GROUP BY, `AVG` covers the whole table, giving one number (D1-03). Swap AVG for COUNT to get ratings per book (book 1 has 2,779).

**Practice:** M1-E01 … M1-E23 · **Debug:** D1-01 … D1-09 · **Review deck:** R1
