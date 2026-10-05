# Practice databases

Each dataset recreates one the lectures use. **Values the lecture states are preserved exactly**, and `tests/test_system.py::test_facts_from_the_lectures` checks them. Everything else is reconstructed or synthetic, and each `seed.sql` says which is which.

| Dataset | Used in | Tables | Preserved from the lectures | Synthetic / reconstructed |
|---|---|---|---|---|
| `longlist0` | lecture0 | longlist (one wide table: title, author, translator, format, pages, publisher, year, votes, rating) | Real International Booker longlist titles 2018-2023 (78 books); 2 books without translator; AVG rating 3.75, MAX 4.52 (*The Eighth Life*), MIN 3.05, > 600,000 votes; 4 books with rating > 4 and votes > 10,000; *Pyre*, *Tyll* | Format, pages, votes and ratings are engineered so the lecture's results come out; 30 distinct publishers, not the lecture's 33 |
| `longlist` | lecture1, lecture4 (and lecture2 glimpse) | authors, publishers, translators, books, authored, translated, ratings | Same 78 books; Eva Baltasar = author 23 → book 1 *Boulder*; Fitzcarraldo Editions = publisher 5, MacLehose Press = 12; *The Birthday Party* = book 8 by Laurent Mauvignier (44); Fernanda Melchor = 24 (Paradais, Hurricane Season); Han Kang = 31 → book 74 *The White Book*; *Minor Detail* = 34 (2021); Ngũgĩ wa Thiong'o both author and translator; Hughes ∩ Jull Costa = one book; 13 books in 2023 | Other ids; 13,359 individual ratings, engineered so book 1 averages 3.77 (2,779 ratings), the HAVING > 4 query returns books 5 and 10, and lecture4's per-year averages match. The *slides'* toy values (3.67 / 2.5) are not reproduced, see errata #23 |
| `sea_lions` | lecture1 L1022-1404 | sea_lions, migrations | Ayah, Spot, Tiger, Mabel, Rick, Jolee and their ids; Jolee has no migration, and two migrations (11735, 11736) have no sea lion | Distances and days |
| `mbta` | lecture2, lecture6 | cards, stations, swipes | Final lecture-2 schema; fare 2.40; real station names | Card ids and every swipe |
| `charlie` | lecture2 L147-199 | log | Every value of the first draft table (Charlie, Alice, Bob) | — |
| `mfa` | lecture3, lecture4, lecture6 | collections, artists, created | Titles, accession numbers, dates; Farmers = 1, Imaginative Landscape = 2; Li Yin = 1, Unidentified artist = 3; ON DELETE CASCADE | Artist 2 ("Placeholder Artist") and the attributions of items 3-4 |
| `votes` | lecture3 L1197-1452 | votes | 20 votes; the typo/space/case variants named in the lecture; final counts 6 (Farmers) and 5 (Imaginative) | Exact list and the 5/4 split of the other two titles |
| `rideshare` | lecture4, lecture6 | rides | Rows 1-2 (Peach, Mario) | Rows 3-6 |
| `movies` | lecture5 | people, movies, stars, ratings | Tom Hanks 158, Kristen Bell 68338, Toy Story 114709, Frozen 2294629, Cars 317219 (2006) | Size (19 movies, not 400k), other person ids, ratings/votes |
| `bank` | lecture5, lecture6 | accounts | Alice 10, Bob 20, Charlie 30; CHECK(balance >= 0) | — |

CSV files in `csv/` reproduce the lecture's imports: `mfa.csv` (with ids), `mfa_noid.csv` (without; note the blank date), and `votes.csv`.
`scaling/` holds the MySQL and PostgreSQL versions from lecture 6 ([scaling/README.md](scaling/README.md)).

## Build

```bash
python3 tools/build_db.py          # database/<name>.db for every dataset → sqlite3 database/mfa.db
python3 tools/build_db.py --big    # + database/movies_big.db (300k synthetic movies) for the timing lab
```
The trainers never touch these files. Every exercise runs on a fresh in-memory copy, with `PRAGMA foreign_keys = ON`.

## Relationships

```mermaid
erDiagram
  authors ||--o{ authored : writes
  books ||--o{ authored : "written by"
  books ||--o{ ratings : receives
  publishers ||--o{ books : publishes
  translators ||--o{ translated : translates
  books ||--o{ translated : "translated by"
  cards ||--o{ swipes : makes
  stations ||--o{ swipes : "happens at"
  artists ||--o{ created : creates
  collections ||--o{ created : "created by"
  people ||--o{ stars : "acts in"
  movies ||--o{ stars : features
  movies ||--o| ratings : has
```
