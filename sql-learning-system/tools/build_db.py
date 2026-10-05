"""Build the practice databases as real files you can open with `sqlite3`.

    python3 tools/build_db.py          # database/<name>.db for every dataset
    python3 tools/build_db.py --big    # also database/movies_big.db (300k synthetic movies) for timing labs
"""
import random
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sqlcheck as S  # noqa: E402


def build_all():
    for name in S.DATASETS:
        path = S.DB_DIR / f"{name}.db"
        path.unlink(missing_ok=True)
        conn = S.fresh_db(name, str(path))
        conn.close()
        print("built", path.relative_to(S.ROOT))


def build_big(n_movies=300_000, path=None):
    """Pad the movies sample with synthetic rows so .timer differences become visible (lecture5 L124-286)."""
    path = Path(path or S.DB_DIR / "movies_big.db")
    path.unlink(missing_ok=True)
    conn = S.fresh_db("movies", str(path))
    rng = random.Random(5)
    words = ["Night", "River", "Last", "Red", "Garden", "Storm", "City", "Silent", "Golden", "Winter",
             "Echo", "Paper", "Glass", "Wild", "Hidden", "Blue", "Iron", "Summer", "Lost", "Bright"]
    conn.execute("BEGIN")
    conn.executemany('INSERT INTO "movies" ("id", "title", "year") VALUES (?, ?, ?)',
                     ((20_000_000 + i, f"{rng.choice(words)} {rng.choice(words)} {i}", rng.randint(1950, 2023))
                      for i in range(n_movies)))
    conn.executemany('INSERT INTO "people" ("id", "name", "birth") VALUES (?, ?, ?)',
                     ((30_000_000 + i, f"Person {i}", rng.randint(1930, 2010)) for i in range(n_movies // 2)))
    conn.executemany('INSERT INTO "stars" ("movie_id", "person_id") VALUES (?, ?)',
                     ((20_000_000 + rng.randrange(n_movies), 30_000_000 + rng.randrange(n_movies // 2))
                      for _ in range(n_movies * 2)))
    conn.execute("COMMIT")
    conn.close()
    print("built", path, f"({path.stat().st_size // 1_000_000} MB)")
    return path


if __name__ == "__main__":
    build_all()
    if "--big" in sys.argv:
        build_big()
