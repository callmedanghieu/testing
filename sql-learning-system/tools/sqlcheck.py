"""Core engine shared by the CLI trainer, the build and the tests.

Every exercise runs against a FRESH in-memory copy of its dataset, so nothing
you try can damage anything. The browser app (app/index.html) re-implements
exactly these rules in JavaScript; tests/test_system.py keeps them honest.

Exercise kinds
  query      run your SQL; compare the result of your LAST row-returning statement
             with the reference solution's (order matters only if ordered: true)
  modify     run your SQL (INSERT/UPDATE/DELETE/CREATE ...); then run the exercise's
             probe statements and check queries on both databases and compare
  error      your statement must FAIL with an error containing `expect_error`
  injection  you supply only an INPUT string; it is pasted into an unsafe query template
  selfcheck  not executable in SQLite (MySQL / PostgreSQL / design); compare with the reference
"""
from __future__ import annotations

import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_DIR = ROOT / "database"
DATASETS = ["longlist", "mbta", "charlie", "mfa", "votes", "rideshare", "movies", "bank"]


def dataset_sql(name: str) -> str:
    d = DB_DIR / name
    seed = d / "seed.sql"
    return (d / "schema.sql").read_text() + "\n" + (seed.read_text() if seed.exists() else "")


def fresh_db(name: str | None, path: str = ":memory:") -> sqlite3.Connection:
    conn = sqlite3.connect(path, isolation_level=None)  # autocommit; BEGIN/COMMIT work as typed
    conn.execute("PRAGMA foreign_keys = ON")              # see analysis/source-issues.md #4
    if name:
        conn.executescript(dataset_sql(name))
    return conn


def split_statements(script: str) -> list[str]:
    """Split a script into complete statements, also when several share one line.
    Cuts only at a ';' that completes a statement, so semicolons inside strings,
    comments and trigger bodies (BEGIN ... END) are respected."""
    out, buf = [], ""
    for ch in script:
        buf += ch
        if ch == ";" and sqlite3.complete_statement(buf):
            if buf.strip().strip(";").strip() and not _only_comments(buf.rstrip(";")):
                out.append(buf.strip())
            buf = ""
    if buf.strip() and not _only_comments(buf):
        out.append(buf.strip())  # last statement without a semicolon
    return out


def _only_comments(s: str) -> bool:
    return all(not ln.strip() or ln.strip().startswith("--") for ln in s.splitlines())


class Result:
    def __init__(self, columns=None, rows=None, error=None):
        self.columns, self.rows, self.error = columns, rows, error
        self.notes = []

    def __repr__(self):
        return f"Result(cols={self.columns}, rows={self.rows}, error={self.error})"


def run_script(conn: sqlite3.Connection, script: str, continue_on_error: bool = False) -> Result:
    """Run statements in order. Returns the last row-returning statement's
    result, or the first error (execution stops at the first error, like the
    sqlite3 shell with .bail on). With continue_on_error the script keeps
    going, as in the interactive shell, and errors are collected in .notes."""
    last = Result(columns=None, rows=None)
    notes = []
    for stmt in split_statements(script):
        try:
            cur = conn.execute(stmt)
            if cur.description is not None:
                last = Result([d[0] for d in cur.description], cur.fetchall())
        except sqlite3.Error as e:
            if not continue_on_error:
                return Result(last.columns, last.rows, error=str(e))
            notes.append(f"{stmt.splitlines()[0][:60]} -> {e}")
    last.notes = notes
    return last


def norm_value(v):
    if isinstance(v, bool):
        v = int(v)
    if isinstance(v, (int, float)):
        r = round(float(v), 6)
        return int(r) if r.is_integer() else r
    if isinstance(v, bytes):
        return v.hex()
    return v


def norm_rows(rows):
    return [tuple(norm_value(v) for v in r) for r in (rows or [])]


def _sort_key(row):
    return tuple((0, "") if v is None else (1, f"{float(v):+025.6f}") if isinstance(v, (int, float)) else (2, str(v))
                 for v in row)


def compare(user: Result, ref: Result, ordered: bool = False) -> tuple[bool, str]:
    if user.error:
        return False, f"Your SQL raised an error: {user.error}"
    if user.columns is None:
        return False, "Your SQL did not return any rows/columns. End with a SELECT."
    if ref.columns is not None and len(user.columns) != len(ref.columns):
        return False, (f"Column count differs: you returned {len(user.columns)} "
                       f"({', '.join(user.columns)}), expected {len(ref.columns)} ({', '.join(ref.columns)}).")
    u, r = norm_rows(user.rows), norm_rows(ref.rows)
    if ordered and u == r:
        return True, "Correct."
    us, rs = sorted(u, key=_sort_key), sorted(r, key=_sort_key)
    if us == rs:
        if ordered:
            return False, "Right rows, wrong order. Check your ORDER BY."
        return True, "Correct."
    msg = [f"Expected {len(r)} row(s); you returned {len(u)}."]
    missing = [x for x in rs if x not in us][:3]
    extra = [x for x in us if x not in rs][:3]
    if missing:
        msg.append("Missing e.g. " + "; ".join(map(str, missing)))
    if extra:
        msg.append("Unexpected e.g. " + "; ".join(map(str, extra)))
    if len(us) != len(set(us)) and len(rs) == len(set(rs)):
        msg.append("You have duplicate rows - check your JOIN or consider DISTINCT / GROUP BY.")
    return False, " ".join(msg)


def plan_text(conn, query: str) -> str:
    rows = conn.execute("EXPLAIN QUERY PLAN " + query).fetchall()
    return " | ".join(r[-1] for r in rows)


def state_snapshot(conn, ex: dict) -> list:
    """Probes then checks, as a comparable list."""
    snap = []
    for p in ex.get("probes", []):
        try:
            conn.execute(p)
            snap.append(("probe", p, "ok"))
        except sqlite3.Error as e:
            snap.append(("probe", p, "error"))
    for c in ex.get("check", []):
        if isinstance(c, dict) and "plan" in c:
            text = plan_text(conn, c["plan"])
            for needle in c.get("contains", []):
                snap.append(("plan", needle, needle.upper() in text.upper()))
            for needle in c.get("not_contains", []):
                snap.append(("plan-not", needle, needle.upper() not in text.upper()))
        else:
            try:
                cur = conn.execute(c)
                rows = norm_rows(cur.fetchall())
                snap.append(("check", c, sorted(rows, key=_sort_key)))
            except sqlite3.Error as e:
                snap.append(("check", c, "error: " + str(e).split(":")[0]))
    return snap


def prepare(ex: dict) -> sqlite3.Connection:
    conn = fresh_db(ex.get("db"))
    if ex.get("setup"):
        conn.executescript(ex["setup"])
    return conn


def evaluate(ex: dict, user_sql: str) -> tuple[bool, str]:
    """Grade user_sql for exercise ex. Returns (passed, feedback)."""
    kind = ex["kind"]
    if kind == "selfcheck":
        return False, "Self-check exercise: compare your answer with the reference solution."
    for word in ex.get("require", []):
        if word.upper() not in user_sql.upper():
            return False, f"This exercise asks you to use {word}."
    if kind == "injection":
        tpl = ex["template"]
        u = run_script(prepare(ex), tpl.replace("{input}", user_sql.strip()))
        r = run_script(prepare(ex), tpl.replace("{input}", ex["solution"].strip()))
        return compare(u, r, ex.get("ordered", False))
    if kind == "error":
        u = run_script(prepare(ex), user_sql)
        if not u.error:
            return False, "Your statement succeeded, but this exercise wants it to be rejected."
        if ex["expect_error"].lower() not in u.error.lower():
            return False, f"It failed, but with a different error: {u.error}"
        return True, f"Correct. SQLite refused it: {u.error}"
    if kind == "query":
        u = run_script(prepare(ex), user_sql)
        r = run_script(prepare(ex), ex["solution"])
        return compare(u, r, ex.get("ordered", False))
    if kind == "modify":
        uc, rc = prepare(ex), prepare(ex)
        coe = ex.get("continue_on_error", False)
        u = run_script(uc, user_sql, coe)
        if u.error:
            return False, f"Your SQL raised an error: {u.error}"
        if uc.in_transaction:
            return False, "A transaction is still open: you never ran COMMIT (or ROLLBACK)."
        r = run_script(rc, ex["solution"], coe)
        assert not r.error, (ex["id"], r.error)
        us, rs = state_snapshot(uc, ex), state_snapshot(rc, ex)
        if us == rs:
            return True, "Correct. The database ends up in the expected state."
        for a, b in zip(us, rs):
            if a != b:
                if a[0] == "probe":
                    return False, (f"Test statement `{a[1]}` was {'accepted' if a[2] == 'ok' else 'rejected'} "
                                   f"by your database but {'accepted' if b[2] == 'ok' else 'rejected'} by the reference.")
                if a[0] in ("plan", "plan-not"):
                    return False, f"Query plan check failed: expected the plan {'to contain' if a[0]=='plan' else 'NOT to contain'} '{a[1]}'."
                return False, f"After your SQL, `{a[1]}` returns {a[2]!s:.200} but expected {b[2]!s:.200}"
        return False, "Database state differs from the expected state."
    raise ValueError(kind)


def reference_output(ex: dict):
    """The expected output shown to learners (computed, never typed by hand)."""
    kind = ex["kind"]
    if kind in ("query",):
        r = run_script(prepare(ex), ex["solution"])
        return {"columns": r.columns, "rows": [list(x) for x in (r.rows or [])], "error": r.error}
    if kind == "injection":
        r = run_script(prepare(ex), ex["template"].replace("{input}", ex["solution"].strip()))
        return {"columns": r.columns, "rows": [list(x) for x in (r.rows or [])], "error": r.error}
    if kind == "modify":
        c = prepare(ex)
        run_script(c, ex["solution"], ex.get("continue_on_error", False))
        outs = []
        for q in ex.get("check", []):
            if isinstance(q, str):
                cur = c.execute(q)
                outs.append({"query": q, "columns": [d[0] for d in cur.description], "rows": [list(x) for x in cur.fetchall()]})
            else:
                outs.append({"query": "EXPLAIN QUERY PLAN " + q["plan"], "plan": plan_text(c, q["plan"])})
        return {"checks": outs}
    if kind == "error":
        r = run_script(prepare(ex), ex["solution"])
        return {"error": r.error}
    return None


def format_result(res: Result, sql: str = "") -> str:
    """Canonical one-line rendering used by predict-the-output cards (mirrored in the app).
    For EXPLAIN QUERY PLAN only the plan's detail column is shown."""
    if res.error:
        return "ERROR: " + res.error
    if not res.rows:
        return "(no rows)"
    rows = res.rows
    if "EXPLAIN QUERY PLAN" in sql.upper():
        rows = [(r[-1],) for r in rows]
    def cell(v):
        if v is None:
            return "NULL"
        if isinstance(v, float) and v.is_integer():
            return str(int(v))
        return str(v)
    return "; ".join(" | ".join(cell(v) for v in r) for r in rows)
