"""Generate the International Booker longlist datasets:

  database/longlist0/seed.sql   week-0 single table "longlist"           (sources/lecture0.txt)
  database/longlist/seed.sql    week-1+ relational version               (sources/lecture1.txt, lecture2, lecture4)

The book list (78 titles, 2018-2023), authors, translators and publishers are a best-effort reconstruction
of the real longlists. Everything the lectures STATE about the data is reproduced and asserted below
(see FACTS); every other number (votes, pages, format, individual ratings) is SYNTHETIC and engineered
only so that the lectures' query results come out the same.

Run:  python3 database/generators/gen_longlist.py
"""
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# id, title, author, translator(s) (None = no separate translator), publisher (None = not reconstructed), year
BOOKS = [
    (1, "Boulder", "Eva Baltasar", "Julia Sanches", "And Other Stories", 2023),
    (2, "Whale", "Cheon Myeong-kwan", "Chi-Young Kim", "Europa Editions", 2023),
    (3, "The Gospel According to the New World", "Maryse Condé", "Richard Philcox", "World Editions", 2023),
    (4, "Standing Heavy", "GauZ'", "Frank Wynne", "MacLehose Press", 2023),
    (5, "Time Shelter", "Georgi Gospodinov", "Angela Rodel", "Weidenfeld & Nicolson", 2023),
    (6, "Is Mother Dead", "Vigdis Hjorth", "Charlotte Barslund", "Verso", 2023),
    (7, "Still Born", "Guadalupe Nettel", "Rosalind Harvey", "Fitzcarraldo Editions", 2023),
    (8, "The Birthday Party", "Laurent Mauvignier", "Daniel Levin Becker", "Fitzcarraldo Editions", 2023),
    (9, "Pyre", "Perumal Murugan", "Aniruddhan Vasudevan", "Pushkin Press", 2023),
    (10, "While We Were Dreaming", "Clemens Meyer", "Katy Derbyshire", "Fitzcarraldo Editions", 2023),
    (11, "The Words That Remain", "Stênio Gardel", "Bruna Dantas Lobato", None, 2023),
    (12, "A System So Magnificent It Is Blinding", "Amanda Svensson", "Nichola Smalley", "Scribe", 2023),
    (13, "Ninth Building", "Zou Jingzhi", "Jeremy Tiang", "Sinoist Books", 2023),
    (14, "Heaven", "Mieko Kawakami", "Sam Bett, David Boyd", "Picador", 2022),
    (15, "Elena Knows", "Claudia Piñeiro", "Frances Riddle", "Charco Press", 2022),
    (16, "The Book of Mother", "Violaine Huisman", "Leslie Camhi", "Scribe", 2022),
    (17, "Tomb of Sand", "Geetanjali Shree", "Daisy Rockwell", "Tilted Axis Press", 2022),
    (18, "A New Name: Septology VI-VII", "Jon Fosse", "Damion Searls", "Fitzcarraldo Editions", 2022),
    (19, "The Books of Jacob", "Olga Tokarczuk", "Jennifer Croft", "Fitzcarraldo Editions", 2022),
    (20, "Love in the Big City", "Sang Young Park", "Anton Hur", "Tilted Axis Press", 2022),
    (21, "Paradais", "Fernanda Melchor", "Sophie Hughes", "Fitzcarraldo Editions", 2022),
    (22, "Phenotypes", "Paulo Scott", "Daniel Hahn", "And Other Stories", 2022),
    (23, "Happy Stories, Mostly", "Norman Erikson Pasaribu", "Tiffany Tsao", "Tilted Axis Press", 2022),
    (24, "More Than I Love My Life", "David Grossman", "Jessica Cohen", "Jonathan Cape", 2022),
    (25, "After the Sun", "Jonas Eika", "Sherilyn Nicolette Hellberg", "Lolli Editions", 2022),
    (26, "Cursed Bunny", "Bora Chung", "Anton Hur", "Honford Star", 2022),
    (27, "At Night All Blood Is Black", "David Diop", "Anna Moschovakis", "Pushkin Press", 2021),
    (28, "The Dangers of Smoking in Bed", "Mariana Enriquez", "Megan McDowell", "Granta", 2021),
    (29, "The Employees", "Olga Ravn", "Martin Aitken", "Lolli Editions", 2021),
    (30, "When We Cease to Understand the World", "Benjamín Labatut", "Adrian Nathan West", "Pushkin Press", 2021),
    (31, "The War of the Poor", "Éric Vuillard", "Mark Polizzotti", None, 2021),
    (32, "I Live in the Slums", "Can Xue", "Karen Gernant, Chen Zeping", "Yale University Press", 2021),
    (33, "In Memory of Memory", "Maria Stepanova", "Sasha Dugdale", "Fitzcarraldo Editions", 2021),
    (34, "Minor Detail", "Adania Shibli", "Elisabeth Jaquette", "Fitzcarraldo Editions", 2021),
    (35, "An Inventory of Losses", "Judith Schalansky", "Jackie Smith", "MacLehose Press", 2021),
    (36, "Summer Brother", "Jaap Robben", "David Doherty", "World Editions", 2021),
    (37, "Wretchedness", "Andrzej Tichý", "Nichola Smalley", "Scribe", 2021),
    (38, "The Perfect Nine", "Ngũgĩ wa Thiong'o", None, "Harvill Secker", 2021),   # self-translated
    (39, "The Pear Field", "Nana Ekvtimishvili", "Elizabeth Heighway", "Peirene Press", 2021),
    (40, "The Discomfort of Evening", "Marieke Lucas Rijneveld", "Michele Hutchison", "Faber & Faber", 2020),
    (41, "The Enlightenment of the Greengage Tree", "Shokoofeh Azar", None, "Europa Editions", 2020),  # translator anonymous
    (42, "Hurricane Season", "Fernanda Melchor", "Sophie Hughes", "Fitzcarraldo Editions", 2020),
    (43, "The Memory Police", "Yoko Ogawa", "Stephen Snyder", "Harvill Secker", 2020),
    (44, "Tyll", "Daniel Kehlmann", "Ross Benjamin", "riverrun", 2020),
    (45, "Little Eyes", "Samanta Schweblin", "Megan McDowell", "Oneworld", 2020),
    (46, "Red Dog", "Willem Anker", "Michiel Heyns", "Pushkin Press", 2020),
    (47, "The Adventures of China Iron", "Gabriela Cabezón Cámara", "Iona Macintyre, Fiona Mackintosh", "Charco Press", 2020),
    (48, "Mac and His Problem", "Enrique Vila-Matas", "Margaret Jull Costa, Sophie Hughes", "Harvill Secker", 2020),
    (49, "Faces on the Tip of My Tongue", "Emmanuelle Pagano", "Sophie Lewis, Jennifer Higgins", "Peirene Press", 2020),
    (50, "The Other Name: Septology I-II", "Jon Fosse", "Damion Searls", "Fitzcarraldo Editions", 2020),
    (51, "The Eighth Life", "Nino Haratischvili", "Charlotte Collins, Ruth Martin", "Scribe", 2020),
    (52, "Serotonin", "Michel Houellebecq", "Shaun Whiteside", "William Heinemann", 2020),
    (53, "Celestial Bodies", "Jokha Alharthi", "Marilyn Booth", "Sandstone Press", 2019),
    (54, "The Years", "Annie Ernaux", "Alison L. Strayer", "Fitzcarraldo Editions", 2019),
    (55, "Drive Your Plow Over the Bones of the Dead", "Olga Tokarczuk", "Antonia Lloyd-Jones", "Fitzcarraldo Editions", 2019),
    (56, "The Shape of the Ruins", "Juan Gabriel Vásquez", "Anne McLean", "MacLehose Press", 2019),
    (57, "The Pine Islands", "Marion Poschmann", "Jen Calleja", "Serpent's Tail", 2019),
    (58, "The Faculty of Dreams", "Sara Stridsberg", "Deborah Bragan-Turner", "MacLehose Press", 2019),
    (59, "Love in the New Millennium", "Can Xue", "Annelise Finegan Wasmoen", "Yale University Press", 2019),
    (60, "Jokes for the Gunmen", "Mazen Maarouf", "Jonathan Wright", "Granta", 2019),
    (61, "Mouthful of Birds", "Samanta Schweblin", "Megan McDowell", "Oneworld", 2019),
    (62, "At Dusk", "Hwang Sok-yong", "Sora Kim-Russell", "Scribe", 2019),
    (63, "The Death of Murat Idrissi", "Tommy Wieringa", "Sam Garrett", "Scribe", 2019),
    (64, "Four Soldiers", "Hubert Mingarelli", "Sam Taylor", None, 2019),
    (65, "The Remainder", "Alia Trabucco Zerán", "Sophie Hughes", "And Other Stories", 2019),
    (66, "The 7th Function of Language", "Laurent Binet", "Sam Taylor", "Harvill Secker", 2018),
    (67, "The Impostor", "Javier Cercas", "Frank Wynne", "MacLehose Press", 2018),
    (68, "Vernon Subutex 1", "Virginie Despentes", "Frank Wynne", "MacLehose Press", 2018),
    (69, "Go, Went, Gone", "Jenny Erpenbeck", "Susan Bernofsky", "Portobello Books", 2018),
    (70, "Die, My Love", "Ariana Harwicz", "Sarah Moses, Carolina Orloff", "Charco Press", 2018),
    (71, "The World Goes On", "László Krasznahorkai", "John Batki, Ottilie Mulzet, George Szirtes", "Tuskar Rock Press", 2018),
    (72, "Like a Fading Shadow", "Antonio Muñoz Molina", "Camilo A. Ramirez", "Tuskar Rock Press", 2018),
    (73, "The Flying Mountain", "Christoph Ransmayr", "Simon Pare", "Seagull Books", 2018),
    (74, "The White Book", "Han Kang", "Deborah Smith", "Portobello Books", 2018),
    (75, "Frankenstein in Baghdad", "Ahmed Saadawi", "Jonathan Wright", "Oneworld", 2018),
    (76, "The Stolen Bicycle", "Wu Ming-Yi", "Darryl Sterk", "Text Publishing", 2018),
    (77, "The Dinner Guest", "Gabriela Ybarra", "Natasha Wimmer", "Harvill Secker", 2018),
    (78, "Flights", "Olga Tokarczuk", "Jennifer Croft", "Fitzcarraldo Editions", 2018),
]
FIXED_AUTHOR_IDS = {"Eva Baltasar": 23, "Fernanda Melchor": 24, "GauZ'": 27, "Han Kang": 31,
                    "Laurent Mauvignier": 44, "Olga Tokarczuk": 58}            # lecture1 L403-408, L758-760, L808-835; lecture4 L41, L136
FIXED_PUBLISHER_IDS = {"Fitzcarraldo Editions": 5, "MacLehose Press": 12}       # lecture1 L521, L645
SELF_TRANSLATED = {38: "Ngũgĩ wa Thiong'o"}                                     # lecture1 L1539-1542

rng = random.Random(2023)


def q(s):
    return "NULL" if s is None else "'" + str(s).replace("'", "''") + "'"


def assign_ids(names, fixed):
    ids, nxt = dict(fixed), 1
    for n in names:
        if n in ids:
            continue
        while nxt in fixed.values():
            nxt += 1
        ids[n] = nxt
        nxt += 1
    return ids


def spread(n, total, lo=1, hi=5):
    """n integers in [lo, hi] summing to total, with a natural-looking spread."""
    base, extra = divmod(total, n)
    vals = [base] * n
    for i in rng.sample(range(n), extra):
        vals[i] += 1
    for _ in range(n * 2):
        i, j = rng.randrange(n), rng.randrange(n)
        if i != j and vals[i] < hi and vals[j] > lo:
            vals[i] += 1
            vals[j] -= 1
    rng.shuffle(vals)
    return vals


def cents_values(n, total_cents, lo, hi):
    """n prices in cents within [lo, hi] (inclusive) with an exact total."""
    vals = [rng.randint(lo, hi) for _ in range(n)]
    diff = total_cents - sum(vals)
    while diff:
        i = rng.randrange(n)
        step = 1 if diff > 0 else -1
        if lo <= vals[i] + step <= hi:
            vals[i] += step
            diff -= step
    return vals


def week0_table():
    """Ratings (Goodreads-style averages) and votes for the single longlist table, engineered to lecture0's results."""
    rating = {}
    rating[51] = 452                                   # MAX: The Eighth Life 4.52 (lecture0 L1037, L1243)
    rating[7] = rating[30] = 414                       # Still Born / When We Cease … tie at 4.14 (L1043-1075)
    rating[19] = 406                                   # The Books of Jacob is 10th: 4.06 (L1037-1038)
    for b, r in zip([14, 17, 33, 43, 54, 74], [445, 438, 427, 419, 411, 408]):
        rating[b] = r                                  # six more above 4.06 → Jacob is exactly 10th
    rating[37] = 305                                   # MIN 3.05 (L1003, L1249)
    for b, r in zip([31, 52, 63, 66, 72, 11, 25, 57], [318, 324, 329, 333, 336, 338, 339, 341]):
        rating[b] = r                                  # nine below 3.42 …
    rating[64] = 342                                   # … so the 10th lowest is 3.42 (L1003)
    free = [b for b, *_ in BOOKS if b not in rating]
    target_total = 29279                               # AVG = 292.79 / 78 = 3.7537179487… (L1166)
    vals = cents_values(len(free), target_total - sum(rating.values()), 343, 400)
    rating.update(zip(free, vals))
    votes = {b: rng.randint(400, 9000) for b, *_ in BOOKS}
    votes[69] = 592                                    # Go, Went, Gone (L1256)
    for b, v in {51: 15710, 30: 23418, 19: 11265, 43: 41260}.items():
        votes[b] = v                                   # exactly 4 books: rating > 4.0 AND votes > 10,000 (L910-919)
    votes[7] = 4102                                    # Still Born: fewer votes than When We Cease (tie-break, L1072-1075)
    while sum(votes.values()) <= 600_000:              # "over 600,000" votes in total (L1267)
        b = rng.choice([b for b in votes if b not in (69, 51, 30, 19, 43, 7) and rating[b] <= 400])
        votes[b] += 1500
    fmt = {b: rng.choice(["hardcover", "paperback", "paperback"]) for b, *_ in BOOKS}
    pages = {b: rng.randint(120, 700) for b, *_ in BOOKS}
    return rating, votes, fmt, pages


def ratings_table():
    """Individual 1-5 ratings per book, engineered to lecture1/lecture4 query results."""
    year_of = {b: y for b, _, _, _, _, y in BOOKS}
    r = {1: 377, 2: 397, 3: 304, 5: 406, 10: 404}     # lecture1 L1737, L1769-1770 (rounded averages ×100)
    capped = {4, 6, 7, 8, 9}                           # ≤ 4.00: not in the HAVING > 4.0 list (L1765-1770)
    year_target = {2018: 375, 2019: 364, 2021: 369, 2022: 387, 2023: 378}   # lecture4 L581-586
    by_year = defaultdict(list)
    for b, *_, y in BOOKS:
        by_year[y].append(b)
    for y, books in by_year.items():
        free = [b for b in books if b not in r]
        for b in free:
            r[b] = rng.randint(330, 400) if b in capped else rng.randint(330, 430)
        if y in year_target:                           # nudge free books by 0.01 until the year average is exact
            diff = year_target[y] * len(books) - sum(r[b] for b in books)
            while diff:
                b = rng.choice(free)
                step = 1 if diff > 0 else -1
                if 300 <= r[b] + step <= (400 if b in capped else 470):
                    r[b] += step
                    diff -= step
    counts = {1: 2779, 2: 176}                         # lecture1 L1799-1800
    sums = {1: 10488}                                  # 10488 / 2779 = 3.774019431… (lecture4 L409)
    for b in r:
        counts.setdefault(b, rng.randint(100, 160))
    for b, n in counts.items():
        if b not in sums:
            s = round(r[b] * n / 100)
            while round(s / n * 100) != r[b]:          # make ROUND(AVG, 2) land exactly on the target
                s += 1 if s / n * 100 < r[b] else -1
            sums[b] = s
    # overall AVG(rating) = 3.83644 (lecture1 L1685): rebalance with a 2020 book (no year average was stated)
    bal = 52
    rest_s = sum(v for b, v in sums.items() if b != bal)
    rest_n = sum(v for b, v in counts.items() if b != bal)
    best = None
    for n in range(100, 2000):
        s = round(3.83644 * (rest_n + n) - rest_s)
        if n <= s <= 5 * n and abs((rest_s + s) / (rest_n + n) - 3.83644) < 5e-6:
            best = (n, s)
            break
    assert best, "could not balance overall average"
    counts[bal], sums[bal] = best
    return {b: spread(counts[b], sums[b]) for b in counts}


def main():
    authors = assign_ids([a for _, _, a, *_ in BOOKS], FIXED_AUTHOR_IDS)
    publishers = assign_ids([p for *_, p, _ in BOOKS if p], FIXED_PUBLISHER_IDS)
    tnames = []
    for b, _, _, t, _, _ in BOOKS:
        for n in (t.split(", ") if t else [SELF_TRANSLATED[b]] if b in SELF_TRANSLATED else []):
            if n not in tnames:
                tnames.append(n)
    translators = {n: i + 1 for i, n in enumerate(tnames)}
    rating0, votes0, fmt0, pages0 = week0_table()
    ratings = ratings_table()

    head = ["-- GENERATED by database/generators/gen_longlist.py -- do not edit by hand.",
            "-- Titles, years, authors, translators, publishers: best-effort reconstruction of the real 2018-2023 longlists.",
            "-- Numbers (votes, pages, format, ratings) are SYNTHETIC, engineered so the lectures' query results reproduce.", ""]
    w0 = head + [f'INSERT INTO "longlist" ("title", "author", "translator", "format", "pages", "publisher", "year", "votes", "rating") VALUES']
    rows = []
    for b, t, a, tr, p, y in BOOKS:
        rows.append(f"({q(t)}, {q(a)}, {q(tr)}, {q(fmt0[b])}, {pages0[b]}, {q(p)}, {y}, {votes0[b]}, {rating0[b] / 100:.2f})")
    w0.append(",\n".join(rows) + ";")
    (ROOT / "longlist0" / "seed.sql").write_text("\n".join(w0) + "\n")

    out = list(head)
    for name, i in sorted(authors.items(), key=lambda kv: kv[1]):
        out.append(f'INSERT INTO "authors" ("id", "name") VALUES ({i}, {q(name)});')
    for name, i in sorted(publishers.items(), key=lambda kv: kv[1]):
        out.append(f'INSERT INTO "publishers" ("id", "publisher") VALUES ({i}, {q(name)});')
    for name, i in translators.items():
        out.append(f'INSERT INTO "translators" ("id", "name") VALUES ({i}, {q(name)});')
    for b, t, a, tr, p, y in BOOKS:
        out.append(f'INSERT INTO "books" ("id", "title", "publisher_id", "year") VALUES ({b}, {q(t)}, {publishers[p] if p else "NULL"}, {y});')
    for b, t, a, *_ in BOOKS:
        out.append(f'INSERT INTO "authored" ("author_id", "book_id") VALUES ({authors[a]}, {b});')
    for b, _, _, tr, _, _ in BOOKS:
        names = tr.split(", ") if tr else ([SELF_TRANSLATED[b]] if b in SELF_TRANSLATED else [])
        for n in names:
            out.append(f'INSERT INTO "translated" ("translator_id", "book_id") VALUES ({translators[n]}, {b});')
    for b in sorted(ratings):
        vals = ratings[b]
        for k in range(0, len(vals), 400):
            out.append('INSERT INTO "ratings" ("book_id", "rating") VALUES '
                       + ", ".join(f"({b}, {v})" for v in vals[k:k + 400]) + ";")
    (ROOT / "longlist" / "seed.sql").write_text("\n".join(out) + "\n")
    print(f"longlist0: {len(BOOKS)} rows; longlist: {len(authors)} authors, {len(publishers)} publishers, "
          f"{len(translators)} translators, {sum(map(len, ratings.values()))} ratings")


if __name__ == "__main__":
    main()
