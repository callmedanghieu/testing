"""Validate the whole learning system.

    python3 -m unittest tests.test_system -v        (stdlib only)

Covers: database setup and relationships, faithfulness to lecture facts, every reference solution,
non-trivial checkers, broken debugging queries really being broken, predict-the-output answers,
source references (line ranges exist AND quoted words appear), origin labels, learning sequence,
concept coverage, verified errata, generated pages, and (when Node is available) the browser engine.
"""
import re
import shutil
import sqlite3
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import content as C  # noqa: E402
import sqlcheck as S  # noqa: E402

EXS, DBG, REV = C.exercises(), C.debugging(), C.review()
ALL = EXS + DBG
MOD_INDEX = {m: i for i, m in enumerate(C.MODULES)}


class TestDatabases(unittest.TestCase):
    def test_every_dataset_builds_with_fk_integrity(self):
        for name in S.DATASETS:
            with self.subTest(name):
                conn = S.fresh_db(name)
                self.assertEqual(conn.execute("PRAGMA foreign_key_check").fetchall(), [], name)
                self.assertEqual(conn.execute("PRAGMA integrity_check").fetchone()[0], "ok")
                tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
                self.assertTrue(tables)
                for t in tables:
                    self.assertGreater(conn.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0], 0, f"{name}.{t} empty")

    def test_relationships_declared(self):
        expected = {("longlist", "authored"): {"authors", "books"}, ("longlist", "ratings"): {"books"},
                    ("mbta", "swipes"): {"cards", "stations"}, ("mfa", "created"): {"artists", "collections"},
                    ("movies", "stars"): {"movies", "people"}, ("movies", "ratings"): {"movies"}}
        for (db, table), parents in expected.items():
            conn = S.fresh_db(db)
            got = {r[2] for r in conn.execute(f"PRAGMA foreign_key_list('{table}')")}
            self.assertEqual(got, parents, f"{db}.{table}")
        cascade = {r[6] for r in S.fresh_db("mfa").execute("PRAGMA foreign_key_list('created')")}
        self.assertEqual(cascade, {"CASCADE"})

    def test_facts_from_the_lectures(self):
        L = S.fresh_db("longlist")
        q = lambda c, sql: c.execute(sql).fetchall()
        self.assertEqual(q(L, "SELECT id FROM authors WHERE name='Fernanda Melchor'"), [(24,)])        # lecture4 L136
        self.assertEqual(q(L, "SELECT id FROM authors WHERE name='Han Kang'"), [(31,)])                 # L41
        self.assertEqual(q(L, "SELECT b.id, b.title FROM books b JOIN authored a ON a.book_id=b.id WHERE a.author_id=31"),
                         [(74, "The White Book")])                                                       # L41-49
        self.assertEqual(q(L, "SELECT year FROM books WHERE id=34 AND title='Minor Detail'"), [(2021,)])  # L827-834
        self.assertEqual(q(L, "SELECT COUNT(*) FROM books WHERE year=2023"), [(13,)])                    # L732
        self.assertEqual(q(L, "SELECT ROUND(AVG(rating),2) FROM ratings GROUP BY book_id HAVING book_id IN (1,2) ORDER BY book_id"),
                         [(3.67,), (2.5,)])                                                              # L383-384
        M = S.fresh_db("movies")
        self.assertEqual(q(M, "SELECT id, year FROM movies WHERE title='Cars'"), [(317219, 2006)])         # lecture5 L123
        self.assertEqual(q(M, "SELECT id FROM people WHERE name='Tom Hanks'"), [(158,)])                  # L56
        self.assertEqual(q(M, "SELECT id FROM movies WHERE title='Toy Story'"), [(114709,)])              # L56
        self.assertEqual(q(M, "SELECT m.id FROM movies m JOIN stars s ON s.movie_id=m.id JOIN people p ON p.id=s.person_id "
                              "WHERE p.id=68338 AND m.title='Frozen'"), [(2294629,)])                     # L68-75
        B = S.fresh_db("bank")
        self.assertEqual(q(B, "SELECT name, balance FROM accounts ORDER BY id"), [("Alice", 10), ("Bob", 20), ("Charlie", 30)])
        V = S.fresh_db("votes")
        self.assertEqual(q(V, "SELECT COUNT(*) FROM votes"), [(20,)])                                     # lecture3 L1210
        R = S.fresh_db("rideshare")
        self.assertIn(("Good Egg Galaxy", "Honeyhive Galaxy", "Peach"), q(R, "SELECT origin, destination, rider FROM rides"))
        Cc = S.fresh_db("charlie")
        self.assertEqual(q(Cc, "SELECT name, station, fare, balance FROM log WHERE id=1"), [("Charlie", "Kendall/MIT", 0.1, 0.05)])
        F = S.fresh_db("mfa")
        self.assertEqual(q(F, "SELECT id FROM collections WHERE title='Imaginative Landscape'"), [(2,)])  # lecture6 L1228
        self.assertEqual(q(F, "SELECT accession_number FROM collections WHERE title='Farmers Working at Dawn'"), [("11.6152",)])

    def test_csv_files_match_seed(self):
        import csv
        votes = [r[0] for r in list(csv.reader(open(ROOT / "database/csv/votes.csv")))[1:]]
        self.assertEqual(sorted(votes), sorted(r[0] for r in S.fresh_db("votes").execute("SELECT title FROM votes")))

    def test_build_db_creates_files(self):
        import build_db
        build_db.build_all()
        for name in S.DATASETS:
            c = sqlite3.connect(S.DB_DIR / f"{name}.db")
            self.assertTrue(c.execute("SELECT COUNT(*) FROM sqlite_master").fetchone()[0] > 0)


class TestContent(unittest.TestCase):
    def test_schema_and_references(self):
        errs = [e for ex in EXS for e in C.validate_exercise(ex)]
        for d in DBG:
            self.assertIsInstance(d.get("bug_type"), str, f"{d['id']}: bug_type must be a string (quote YAML null)")
            for k in ("id", "module", "title", "bug_type", "origin", "concepts", "kind", "broken", "hints", "solution", "diagnosis", "source"):
                if k not in d:
                    errs.append(f"{d.get('id')}: missing {k}")
            errs += [f"{d['id']}: {m}" for r in d["source"] if (m := C.check_ref(r))]
        for it in REV:
            if it.get("source") and (m := C.check_ref(it["source"])):
                errs.append(f"{it['id']}: {m}")
        self.assertEqual(errs, [])

    def test_unique_ids_and_naming(self):
        ids = [x["id"] for x in ALL + REV]
        self.assertEqual(len(ids), len(set(ids)))
        for e in EXS:
            self.assertTrue(e["id"].startswith(e["module"] + "-E"), e["id"])
        for d in DBG:
            self.assertTrue(d["id"].startswith("D" + d["module"][1]), d["id"])

    def test_every_item_has_a_source_reference(self):
        for x in ALL:
            self.assertTrue(x["source"], x["id"])
        for it in REV:
            if it["type"] in ("quick", "concept", "predict"):
                self.assertIn("source", it, it["id"])

    def test_generated_items_are_labelled(self):
        for e in EXS:
            page = (ROOT / "exercises" / ("generated" if e["origin"] == "generated" else "source") / f"{e['module']}.md").read_text()
            self.assertIn(f"### {e['id']} ", page, f"{e['id']} not on its {'generated' if e['origin']=='generated' else 'source'} page")
            self.assertIn(C.ORIGINS[e["origin"]].split(" · ")[0], page)
            other = (ROOT / "exercises" / ("source" if e["origin"] == "generated" else "generated") / f"{e['module']}.md").read_text()
            self.assertNotIn(f"### {e['id']} ", other, f"{e['id']} leaked onto the wrong page")

    def test_source_origins_cite_the_lecture_of_their_module(self):
        lecture_of = {"M1": "lecture2", "M2": "lecture3", "M3": "lecture4", "M4": "lecture5", "M5": "lecture6"}
        for x in ALL:
            if x["origin"] != "generated" and x["module"] in lecture_of:
                self.assertIn(lecture_of[x["module"]], {r["file"] for r in x["source"]}, x["id"])

    def test_learning_sequence(self):
        """An item may only use concepts from its own or earlier modules; prerequisites point backwards."""
        import yaml
        mods = yaml.safe_load((C.CONTENT / "modules.yaml").read_text())
        for x in ALL:
            for c in x["concepts"]:
                self.assertLessEqual(int(c[1]), int(x["module"][1]), f"{x['id']} uses later concept {c}")
        for m, mod in mods.items():
            for p in mod["prerequisites"]:
                if p != "none":
                    self.assertLess(MOD_INDEX[p], MOD_INDEX[m])
            for ch in mod["challenge"]:
                self.assertIn(ch, {e["id"] for e in EXS})
        for m in C.MODULES:   # difficulty should not start at the top
            diffs = [e["difficulty"] for e in EXS if e["module"] == m]
            self.assertLessEqual(diffs[0], 2, f"{m} starts too hard")

    def test_concept_coverage(self):
        import build
        concepts = build.concept_sources()
        self.assertEqual(len(concepts), 49)
        used = {c for x in ALL for c in x["concepts"]}
        self.assertEqual(sorted(set(concepts) - used), [], "concepts without any practice item")
        for cid, c in concepts.items():
            self.assertTrue(c["refs"], f"{cid} has no source ref")
            for r in c["refs"]:
                self.assertIsNone(C.check_ref(r), cid)

    def test_three_progressive_hints_never_give_the_whole_solution(self):
        for x in ALL:
            sol = re.sub(r"\s+", " ", x["solution"]).strip().rstrip(";")
            for i, h in enumerate(x["hints"][:2]):
                self.assertNotIn(sol, h, f"{x['id']} hint {i + 1} reveals the full solution")


class TestExecution(unittest.TestCase):
    def test_every_reference_solution_passes(self):
        for x in ALL:
            if x["kind"] == "selfcheck":
                continue
            with self.subTest(x["id"]):
                ok, msg = S.evaluate(x, x["solution"])
                self.assertTrue(ok, f"{x['id']}: {msg}")

    def test_known_expected_outputs(self):
        for e in EXS:
            if "expected_known" in e:
                with self.subTest(e["id"]):
                    out = S.reference_output(e)
                    got = sorted(map(tuple, S.norm_rows(out["rows"])), key=S._sort_key)
                    exp = sorted(map(tuple, S.norm_rows(e["expected_known"])), key=S._sort_key)
                    self.assertEqual(got, exp)

    def test_checkers_are_not_trivially_satisfied(self):
        for x in ALL:
            if x["kind"] in ("modify", "query"):
                with self.subTest(x["id"]):
                    ok, _ = S.evaluate(x, "SELECT 1;")
                    self.assertFalse(ok, f"{x['id']}: an empty answer passes")
            if x["kind"] == "error":
                ok, _ = S.evaluate(x, "SELECT 1;")
                self.assertFalse(ok)
            if x["kind"] == "injection":
                ok, _ = S.evaluate(x, "1" if "id" in x["template"] else "wrong")
                self.assertFalse(ok)

    def test_broken_debugging_queries_are_really_broken(self):
        for d in DBG:
            if d["kind"] == "selfcheck":
                continue
            with self.subTest(d["id"]):
                ok, msg = S.evaluate(d, d["broken"])
                self.assertFalse(ok, f"{d['id']}: the broken query passes the checker")

    def test_plan_checks_match_lesson_claims(self):
        conn = S.fresh_db("movies")
        conn.executescript('CREATE INDEX "name_index" ON "people" ("name");'
                           'CREATE INDEX "person_index" ON "stars" ("person_id", "movie_id");')
        plan = S.plan_text(conn, 'SELECT "title" FROM "movies" WHERE "id" IN (SELECT "movie_id" FROM "stars" WHERE '
                                 '"person_id" = (SELECT "id" FROM "people" WHERE "name" = \'Tom Hanks\'))')
        for needle in ("SEARCH people USING COVERING INDEX name_index", "SEARCH stars USING COVERING INDEX person_index",
                       "SEARCH movies USING INTEGER PRIMARY KEY"):
            self.assertIn(needle, plan)

    def test_predict_the_output_answers(self):
        for it in REV:
            if it["type"] != "predict":
                continue
            with self.subTest(it["id"]):
                c = S.fresh_db(it.get("db"))
                if it.get("setup"):
                    c.executescript(it["setup"])
                out = S.format_result(S.run_script(c, it["sql"]), it["sql"])
                exp = it["choices"][it["answer"]]
                self.assertTrue(out.startswith(exp) if exp.startswith("ERROR") else out == exp, f"{it['id']}: got {out!r}")

    def test_review_pointers_and_answers(self):
        ids = {x["id"] for x in ALL}
        for it in REV:
            if it["type"] in ("debug", "write"):
                self.assertIn(it["ref"], ids, it["id"])
            if it["type"] in ("concept", "predict"):
                self.assertLess(it["answer"], len(it["choices"]))
                self.assertEqual(len(set(it["choices"])), len(it["choices"]), f"{it['id']} duplicate choices")


class TestErrata(unittest.TestCase):
    """Re-verify the SQLite errata in analysis/source-issues.md."""

    def q(self, script):
        c = S.fresh_db(None)
        return S.run_script(c, script)

    def test_1_untyped_column_has_blob_affinity(self):
        self.assertEqual(self.q("CREATE TABLE t(x); INSERT INTO t VALUES ('10'); SELECT typeof(x) FROM t;").rows, [("text",)])

    def test_2_autoincrement_never_reuses(self):
        base = "INSERT INTO a(v) VALUES (1),(2),(3); DELETE FROM a WHERE id=3; INSERT INTO a(v) VALUES (4); SELECT max(id) FROM a;"
        self.assertEqual(self.q("CREATE TABLE a(id INTEGER PRIMARY KEY, v);" + base).rows, [(3,)])
        self.assertEqual(self.q("CREATE TABLE a(id INTEGER PRIMARY KEY AUTOINCREMENT, v);" + base).rows, [(4,)])

    def test_3_fk_column_accepts_null(self):
        r = self.q("CREATE TABLE p(id INTEGER PRIMARY KEY); CREATE TABLE c(pid INTEGER REFERENCES p(id));"
                   "INSERT INTO c VALUES (NULL); SELECT COUNT(*) FROM c;")
        self.assertEqual(r.rows, [(1,)])

    def test_4_fk_off_by_default(self):
        self.assertEqual(sqlite3.connect(":memory:").execute("PRAGMA foreign_keys").fetchone(), (0,))

    def test_5_unquoted_accession_loses_zero(self):
        self.assertEqual(self.q("CREATE TABLE m(a TEXT); INSERT INTO m VALUES (06.1899); SELECT a FROM m;").rows, [("6.1899",)])

    def test_6_trigger_named_delete_needs_quotes(self):
        r = self.q("CREATE TABLE x(id INTEGER PRIMARY KEY); CREATE VIEW v AS SELECT * FROM x;"
                   "CREATE TRIGGER delete INSTEAD OF DELETE ON v BEGIN SELECT 1; END;")
        self.assertIn("syntax error", r.error)

    def test_11_views_read_only_in_sqlite(self):
        r = self.q("CREATE TABLE p(id); CREATE VIEW v AS SELECT * FROM p; UPDATE v SET id = 1;")
        self.assertIn("because it is a view", r.error)

    def test_18_no_action_still_refuses(self):
        r = self.q("CREATE TABLE a(id INTEGER PRIMARY KEY); CREATE TABLE c(aid INTEGER REFERENCES a(id) ON DELETE NO ACTION);"
                   "INSERT INTO a VALUES (1); INSERT INTO c VALUES (1); DELETE FROM a WHERE id = 1;")
        self.assertIn("FOREIGN KEY constraint failed", r.error)

    def test_errata_numbers_exist(self):
        text = (ROOT / "analysis/source-issues.md").read_text()
        for n in (1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 18):
            self.assertIn(f"| {n} |", text)


class TestBuildAndTools(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(ROOT / "tools/build.py")], check=True, capture_output=True)

    def test_generated_pages_exist(self):
        for m in C.MODULES:
            for d in ("exercises/source", "exercises/generated", "hints", "solutions", "review", "debugging", "curriculum/modules"):
                self.assertTrue((ROOT / d / f"{m}.md").exists(), f"{d}/{m}.md")
        for f in ("source-mapping/source_to_concept.md", "source-mapping/concept_index.md", "source-mapping/exercise_index.md",
                  "app/index.html", "app/artifact.html", "app/data.json"):
            self.assertTrue((ROOT / f).exists(), f)

    def test_readme_numbers_match_content(self):
        readme = (ROOT / "README.md").read_text()
        n_src = sum(e["origin"] != "generated" for e in EXS)
        d_src = sum(d["origin"] != "generated" for d in DBG)
        self.assertIn(f"| Practice exercises | {len(EXS)} ({n_src} from the lectures, {len(EXS) - n_src} generated) |", readme)
        self.assertIn(f"| Debugging items | {len(DBG)} broken", readme)
        self.assertIn(f"({d_src} from the lectures, {len(DBG) - d_src} generated)", readme)
        self.assertIn(f"| Review cards | {len(REV)} ", readme)

    def test_app_bundle_contains_everything(self):
        html = (ROOT / "app/index.html").read_text()
        for x in ALL + REV:
            self.assertIn(f'"{x["id"]}"', html)
        self.assertIn("SQLEngine", html)
        self.assertNotIn("/*__DATA__*/", html)
        self.assertTrue((ROOT / "app/vendor/sql-asm.js").exists())

    def test_cli_check_command(self):
        sol = ROOT / "progress" / "_test_solution.sql"
        sol.write_text(next(e for e in EXS if e["id"] == "M0-E08")["solution"])
        try:
            r = subprocess.run([sys.executable, str(ROOT / "tools/practice.py"), "check", "M0-E08", str(sol)],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("PASS", r.stdout)
        finally:
            sol.unlink()
            (ROOT / "progress" / "progress.json").unlink(missing_ok=True)

    def test_labs(self):
        import labs
        self.assertTrue(labs.lab_locks())
        self.assertTrue(labs.lab_injection())
        self.assertTrue(labs.lab_vacuum(n=40_000))
        if shutil.which("sqlite3"):
            self.assertTrue(labs.lab_import())

    @unittest.skipUnless(shutil.which("node"), "node not installed")
    def test_browser_engine_parity(self):
        r = subprocess.run(["node", str(ROOT / "tests/test_engine.js")], capture_output=True, text=True, timeout=600)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
