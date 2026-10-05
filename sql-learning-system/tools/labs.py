"""Hands-on labs for the demos that need two connections, a file on disk, or the sqlite3 shell.

    python3 tools/labs.py locks       # lecture5 L1456-1553  BEGIN EXCLUSIVE blocks a second connection
    python3 tools/labs.py vacuum      # lecture5 L943-1042   DROP INDEX doesn't shrink the file; VACUUM does
    python3 tools/labs.py timer       # lecture5 L124-286    scan vs index, timed
    python3 tools/labs.py injection   # lecture6 L1921-2148  string-built SQL vs bound parameters
    python3 tools/labs.py import      # lecture3 L381-603    .import CSV, both ways (needs the sqlite3 CLI)
    python3 tools/labs.py all
"""
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_db  # noqa: E402
import sqlcheck as S  # noqa: E402

TMP = Path(tempfile.mkdtemp(prefix="sql-labs-"))


def say(s=""):
    print(s, flush=True)


def lab_locks():
    say("## Lab: locks (lecture5 L1534-1546)")
    path = TMP / "bank.db"
    S.fresh_db("bank", str(path)).close()
    a = sqlite3.connect(path, isolation_level=None)
    b = sqlite3.connect(path, isolation_level=None, timeout=0)
    say("A> BEGIN EXCLUSIVE TRANSACTION;")
    a.execute("BEGIN EXCLUSIVE TRANSACTION")
    say('B> SELECT * FROM "accounts";')
    try:
        b.execute('SELECT * FROM "accounts"').fetchall()
        say("   (unexpected) B could read")
        locked = False
    except sqlite3.OperationalError as e:
        say(f"   B gets: {e}")
        locked = "locked" in str(e)
    say("A> COMMIT;")
    a.execute("COMMIT")
    say('B> SELECT * FROM "accounts";')
    say("   " + str(b.execute('SELECT * FROM "accounts"').fetchall()))
    return locked


def size(p):
    return p.stat().st_size


def lab_vacuum(n=120_000):
    say("## Lab: VACUUM (lecture5 L943-1042)")
    path = build_db.build_big(n, TMP / "movies_vacuum.db")
    c = sqlite3.connect(path, isolation_level=None)
    for sql in ['CREATE INDEX "title_index" ON "movies" ("title")',
                'CREATE INDEX "person_index" ON "stars" ("person_id", "movie_id")',
                'CREATE INDEX "name_index" ON "people" ("name")']:
        c.execute(sql)
    s0 = size(path)
    say(f"with 3 indexes:       {s0:>12,} bytes")
    for idx in ("title_index", "person_index", "name_index"):
        c.execute(f'DROP INDEX "{idx}"')
    s1 = size(path)
    say(f"after DROP INDEX x3:  {s1:>12,} bytes  (unchanged: pages only marked free)")
    c.execute("VACUUM")
    s2 = size(path)
    say(f"after VACUUM:         {s2:>12,} bytes  (space returned to the OS)")
    return s1 == s0 and s2 < s1


def lab_timer(n=300_000):
    say("## Lab: timing a scan vs an index search (lecture5 L124-286)")
    path = build_db.build_big(n, TMP / "movies_timer.db")
    c = sqlite3.connect(path, isolation_level=None)
    q = "SELECT * FROM \"movies\" WHERE \"title\" = 'Cars'"

    def timed():
        t = time.perf_counter()
        for _ in range(20):
            c.execute(q).fetchall()
        return (time.perf_counter() - t) / 20

    plan0, t0 = S.plan_text(c, q), timed()
    c.execute('CREATE INDEX "title_index" ON "movies" ("title")')
    plan1, t1 = S.plan_text(c, q), timed()
    say(f"before index: {t0 * 1000:8.3f} ms   plan: {plan0}")
    say(f"after index:  {t1 * 1000:8.3f} ms   plan: {plan1}")
    say(f"speed-up ≈ {t0 / max(t1, 1e-9):.0f}x")
    return t1 < t0


def lab_injection():
    say("## Lab: SQL injection vs bound parameters (lecture6 L1921-2148)")
    c = S.fresh_db("bank")
    evil = "1 UNION SELECT * FROM accounts"
    unsafe = f"SELECT * FROM accounts WHERE id = {evil}"
    say(f"UNSAFE  f-string: {unsafe}")
    leaked = c.execute(unsafe).fetchall()
    say(f"        → {leaked}")
    say('SAFE    c.execute("SELECT * FROM accounts WHERE id = ?", (evil,))')
    safe = c.execute("SELECT * FROM accounts WHERE id = ?", (evil,)).fetchall()
    say(f"        → {safe}   (the input is data, never parsed as SQL)")
    say("        (MySQL returns Alice here instead: it converts '1 UNION…' to the number 1; see analysis/source-issues.md #8)")
    return len(leaked) == 3 and safe == []


def lab_import():
    say("## Lab: .import (lecture3 L381-603)")
    exe = shutil.which("sqlite3")
    if not exe:
        say("The sqlite3 command-line shell is not installed; skipping (install it, e.g. apt install sqlite3).")
        return None
    csv_dir = S.DB_DIR / "csv"
    db = TMP / "mfa_import.db"
    schema = (S.DB_DIR / "mfa" / "schema.sql").read_text().split('CREATE TABLE "artists"')[0]
    script = f"""{schema}
.import --csv --skip 1 {csv_dir / 'mfa.csv'} collections
SELECT COUNT(*) FROM "collections";
DELETE FROM "collections";
.import --csv {csv_dir / 'mfa_noid.csv'} temp
INSERT INTO "collections" ("title", "accession_number", "acquired")
SELECT "title", "accession_number", NULLIF("acquired", '') FROM "temp";
DROP TABLE "temp";
SELECT "id", "title", "accession_number", quote("acquired") FROM "collections";
"""
    say(script)
    out = subprocess.run([exe, str(db)], input=script, capture_output=True, text=True)
    say(out.stdout + out.stderr)
    return "5" in out.stdout.splitlines()[0] and "NULL" in out.stdout and out.returncode == 0


LABS = {"locks": lab_locks, "vacuum": lab_vacuum, "timer": lab_timer, "injection": lab_injection, "import": lab_import}

if __name__ == "__main__":
    which = sys.argv[1:] or ["all"]
    names = list(LABS) if which == ["all"] else which
    for n in names:
        LABS[n]()
        say()
