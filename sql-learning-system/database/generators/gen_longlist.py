"""Generate database/longlist/seed.sql.

Reconstruction of the CS50 SQL `longlist.db` used in Lecture 4 (views).
Facts preserved from the lecture transcript (sources/lecture4.txt):
  * books are International Booker Prize longlisted titles, 2018-2023
  * author "Han Kang" has author id 31 and wrote book id 74 "The White Book"   (L41-49)
  * "Fernanda Melchor" has author id 24 and wrote "Paradais" and "Hurricane Season" (L136, L297)
  * "Minor Detail" has book id 34 and was longlisted in 2021                    (L827-834)
  * 13 books were longlisted in 2023                                             (L732)
  * ratings are individual 1-5 star ratings; slide example: book 1 avg 3.67, book 2 avg 2.5 (L374-384)
Everything else (ordering inside a year, the other ids, every individual rating)
is reconstructed or synthetic. The original file has 78 books; years where
the full longlist could not be reconstructed with confidence have 12 books.
Run:  python3 database/generators/gen_longlist.py
"""
import random
from pathlib import Path

BOOKS = {  # year: [(book_id, title, author), ...]
    2023: [(1, "Boulder", "Eva Baltasar"), (2, "Whale", "Cheon Myeong-kwan"),
           (3, "The Gospel According to the New World", "Maryse Condé"),
           (4, "Standing Heavy", "GauZ'"), (5, "Time Shelter", "Georgi Gospodinov"),
           (6, "Is Mother Dead", "Vigdis Hjorth"), (7, "Still Born", "Guadalupe Nettel"),
           (8, "Pyre", "Perumal Murugan"), (9, "The Birthday Party", "Laurent Mauvignier"),
           (10, "While We Were Dreaming", "Clemens Meyer"),
           (11, "The Words That Remain", "Stênio Gardel"), (12, "Phenotypes", "Paulo Scott"),
           (13, "A System So Magnificent It Is Blinding", "Amanda Svensson")],
    2022: [(14, "Heaven", "Mieko Kawakami"), (15, "Elena Knows", "Claudia Piñeiro"),
           (16, "The Book of Mother", "Violaine Huisman"), (17, "Tomb of Sand", "Geetanjali Shree"),
           (18, "A New Name: Septology VI-VII", "Jon Fosse"),
           (19, "The Books of Jacob", "Olga Tokarczuk"),
           (20, "Love in the Big City", "Sang Young Park"), (21, "Paradais", "Fernanda Melchor"),
           (22, "The Pear Field", "Nana Ekvtimishvili"),
           (23, "Happy Stories, Mostly", "Norman Erikson Pasaribu"),
           (24, "More Than I Love My Life", "David Grossman"), (25, "After the Sun", "Jonas Eika"),
           (26, "Cursed Bunny", "Bora Chung")],
    2021: [(27, "At Night All Blood Is Black", "David Diop"),
           (28, "The Dangers of Smoking in Bed", "Mariana Enriquez"),
           (29, "The Employees", "Olga Ravn"), (30, "In Memory of Memory", "Maria Stepanova"),
           (31, "When We Cease to Understand the World", "Benjamín Labatut"),
           (32, "The War of the Poor", "Éric Vuillard"), (33, "I Live in the Slums", "Can Xue"),
           (34, "Minor Detail", "Adania Shibli"), (35, "An Inventory of Losses", "Judith Schalansky"),
           (36, "Summer Brother", "Jaap Robben"), (37, "Wretchedness", "Andrzej Tichý"),
           (38, "The Perfect Nine", "Ngũgĩ wa Thiong'o")],
    2020: [(40, "The Discomfort of Evening", "Marieke Lucas Rijneveld"),
           (41, "The Enlightenment of the Greengage Tree", "Shokoofeh Azar"),
           (42, "Hurricane Season", "Fernanda Melchor"), (43, "The Memory Police", "Yoko Ogawa"),
           (44, "Tyll", "Daniel Kehlmann"), (45, "Little Eyes", "Samanta Schweblin"),
           (46, "Red Dog", "Willem Anker"),
           (47, "The Adventures of China Iron", "Gabriela Cabezón Cámara"),
           (48, "Mac and His Problem", "Enrique Vila-Matas"),
           (49, "Faces on the Tip of My Tongue", "Emmanuelle Pagano"),
           (50, "The Other Name: Septology I-II", "Jon Fosse"),
           (51, "The Remainder", "Alia Trabucco Zerán"), (52, "Serotonin", "Michel Houellebecq")],
    2019: [(53, "Celestial Bodies", "Jokha Alharthi"), (54, "The Years", "Annie Ernaux"),
           (55, "Drive Your Plow Over the Bones of the Dead", "Olga Tokarczuk"),
           (56, "The Shape of the Ruins", "Juan Gabriel Vásquez"),
           (57, "The Pine Islands", "Marion Poschmann"),
           (58, "The Faculty of Dreams", "Sara Stridsberg"),
           (59, "Love in the New Millennium", "Can Xue"),
           (60, "Jokes for the Gunmen", "Mazen Maarouf"),
           (61, "Mouthful of Birds", "Samanta Schweblin"), (62, "At Dusk", "Hwang Sok-yong"),
           (63, "The Death of Murat Idrissi", "Tommy Wieringa"),
           (64, "Four Soldiers", "Hubert Mingarelli")],
    2018: [(66, "Flights", "Olga Tokarczuk"), (67, "Frankenstein in Baghdad", "Ahmed Saadawi"),
           (68, "The World Goes On", "László Krasznahorkai"),
           (69, "Like a Fading Shadow", "Antonio Muñoz Molina"),
           (70, "Vernon Subutex 1", "Virginie Despentes"), (71, "The Impostor", "Javier Cercas"),
           (72, "The Stolen Bicycle", "Wu Ming-Yi"), (73, "Die, My Love", "Ariana Harwicz"),
           (74, "The White Book", "Han Kang"), (75, "Go, Went, Gone", "Jenny Erpenbeck"),
           (76, "The 7th Function of Language", "Laurent Binet"),
           (77, "The Flying Mountain", "Christoph Ransmayr")],
}
FIXED_AUTHOR_IDS = {"Fernanda Melchor": 24, "Han Kang": 31}  # from the lecture


def q(s):
    return "'" + s.replace("'", "''") + "'"


def main():
    rows = [(bid, t, a, y) for y, lst in BOOKS.items() for (bid, t, a) in lst]
    rows.sort()
    # Assign author ids in order of first appearance, skipping the fixed ids.
    author_ids, next_id = dict(FIXED_AUTHOR_IDS), 1
    for _, _, a, _ in rows:
        if a in author_ids:
            continue
        while next_id in FIXED_AUTHOR_IDS.values():
            next_id += 1
        author_ids[a] = next_id
        next_id += 1
    rng = random.Random(2023)
    out = ["-- GENERATED by database/generators/gen_longlist.py -- do not edit by hand.",
           "-- Titles/years/authors: real International Booker longlists (partial reconstruction).",
           "-- Ratings: SYNTHETIC (random, seeded). Averages will NOT match the numbers said in Lecture 4.",
           ""]
    for a, i in sorted(author_ids.items(), key=lambda kv: kv[1]):
        out.append(f"INSERT INTO authors (id, name) VALUES ({i}, {q(a)});")
    for bid, t, a, y in rows:
        out.append(f"INSERT INTO books (id, title, year) VALUES ({bid}, {q(t)}, {y});")
    for bid, t, a, y in rows:
        out.append(f"INSERT INTO authored (author_id, book_id) VALUES ({author_ids[a]}, {bid});")
    for bid, *_ in rows:
        if bid == 1:
            ratings = [4, 3, 4]          # slide example: average 3.67
        elif bid == 2:
            ratings = [2, 3]             # slide example: average 2.5
        else:
            mean = rng.uniform(2.9, 4.4)
            ratings = [max(1, min(5, round(rng.gauss(mean, 0.9)))) for _ in range(rng.randint(6, 30))]
        out.append("INSERT INTO ratings (book_id, rating) VALUES "
                   + ", ".join(f"({bid}, {r})" for r in ratings) + ";")
    Path(__file__).resolve().parents[1].joinpath("longlist", "seed.sql").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
