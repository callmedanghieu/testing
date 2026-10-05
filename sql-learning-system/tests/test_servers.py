"""Execute the Lecture 6 material on real servers: MariaDB (MySQL-compatible) and PostgreSQL.

    tools/start_servers.sh && python3 -m unittest tests.test_servers -v

Skips (does not fail) when the servers are not running.
"""
import os
import shutil
import subprocess
import sys
import unittest
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import content as C  # noqa: E402

BASE = os.environ.get("SQLSRV_DIR", "/tmp/sqlsrv")
MYSQL = ["mysql", f"--socket={BASE}/mysql.sock", "-uroot"]
PSQL = ["psql", "-h", BASE, "-p", "5433", "-U", "postgres", "-v", "ON_ERROR_STOP=1", "-X", "-q"]


def mysql_up():
    return shutil.which("mysql") and subprocess.run(MYSQL + ["-e", "SELECT 1"], capture_output=True).returncode == 0


def pg_up():
    return shutil.which("psql") and subprocess.run(PSQL + ["-c", "SELECT 1"], capture_output=True).returncode == 0


def run(engine, db, script):
    if engine == "mysql":
        cmd = MYSQL + [db]
    else:
        cmd = PSQL + ["-d", db]
    return subprocess.run(cmd, input=script, capture_output=True, text=True)


class ServerDB:
    def __init__(self, engine):
        self.engine, self.name = engine, "t_" + uuid.uuid4().hex[:10]

    def __enter__(self):
        if self.engine == "mysql":
            subprocess.run(MYSQL + ["-e", f"CREATE DATABASE `{self.name}`"], check=True)
        else:
            subprocess.run(PSQL + ["-c", f'CREATE DATABASE "{self.name}"'], check=True)
        return self.name

    def __exit__(self, *a):
        if self.engine == "mysql":
            subprocess.run(MYSQL + ["-e", f"DROP DATABASE `{self.name}`"])
        else:
            subprocess.run(PSQL + ["-c", f'DROP DATABASE "{self.name}"'])


def server_items():
    return [e for e in C.exercises() + C.debugging() if e.get("engine")]


class TestServerSolutions(unittest.TestCase):
    def check_item(self, e):
        with ServerDB(e["engine"]) as db:
            if e.get("verify_setup"):
                r = run(e["engine"], db, e["verify_setup"])
                self.assertEqual(r.returncode, 0, f"{e['id']} setup: {r.stderr}")
            r = run(e["engine"], db, e["solution"] + "\n" + e.get("verify_after", ""))
            try:
                self.assertEqual(r.returncode, 0, f"{e['id']} solution failed: {r.stderr}")
                for needle in e.get("verify_expect", []):
                    self.assertIn(needle, r.stdout, f"{e['id']}: expected {needle!r} in output:\n{r.stdout}")
                for needle in e.get("verify_absent", []):
                    self.assertNotIn(needle, r.stdout, f"{e['id']}: {needle!r} must not appear")
                if e.get("verify_fail"):
                    bad = run(e["engine"], db, e["verify_fail"])
                    self.assertNotEqual(bad.returncode, 0, f"{e['id']}: constraint should reject: {e['verify_fail']}")
                if e.get("broken"):  # debugging item: the broken version must fail
                    bad = run(e["engine"], db, "DROP PROCEDURE IF EXISTS `current_collection`;\n" + e["broken"])
                    self.assertNotEqual(bad.returncode, 0, f"{e['id']}: broken version should fail")
            finally:
                if e.get("verify_cleanup"):
                    run(e["engine"], db, e["verify_cleanup"])

    @unittest.skipUnless(mysql_up(), "MariaDB/MySQL not running (tools/start_servers.sh)")
    def test_mysql_items(self):
        items = [e for e in server_items() if e["engine"] == "mysql"]
        self.assertGreaterEqual(len(items), 7)
        for e in items:
            with self.subTest(e["id"]):
                self.check_item(e)

    @unittest.skipUnless(pg_up(), "PostgreSQL not running (tools/start_servers.sh)")
    def test_postgres_items(self):
        items = [e for e in server_items() if e["engine"] == "postgres"]
        self.assertGreaterEqual(len(items), 1)
        for e in items:
            with self.subTest(e["id"]):
                self.check_item(e)


class TestScalingScripts(unittest.TestCase):
    @unittest.skipUnless(mysql_up(), "MariaDB/MySQL not running")
    def test_mysql_scripts(self):
        expect = {
            "mbta.sql": ["swipes", "decimal(5,2)", "-2.40"],
            "mfa_procedures.sql": ["Farmers Working at Dawn", "sold"],
            "rideshare_access.sql": ["GRANT SELECT ON"],
            "bank_injection.sql": ["Charlie", "1292"],
        }
        for f, needles in expect.items():
            with self.subTest(f), ServerDB("mysql") as db:
                r = run("mysql", db, (ROOT / "database/scaling/mysql" / f).read_text())
                self.assertEqual(r.returncode, 0, r.stderr)
                for n in needles:
                    self.assertIn(n, r.stdout)
                if f == "mfa_procedures.sql":  # sold item 2 is hidden by the procedure
                    proc_out = r.stdout.split("Farmers Working at Dawn", 1)[1]
                    self.assertNotIn("Imaginative Landscape\t56.496", proc_out.split("sold")[0])
                if f == "bank_injection.sql":  # prepared statement returns ONLY Alice (errata #8)
                    after = r.stdout.split("Charlie\t30", 1)[1]
                    self.assertIn("Alice", after)
                    self.assertNotIn("Bob", after)
        run("mysql", "mysql", "DROP USER IF EXISTS 'carter';")

    @unittest.skipUnless(pg_up(), "PostgreSQL not running")
    def test_postgres_script(self):
        with ServerDB("postgres") as db:
            r = run("postgres", db, (ROOT / "database/scaling/postgres/mbta.sql").read_text())
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("deposit", r.stdout)
            self.assertIn("-2.40", r.stdout)

    @unittest.skipUnless(mysql_up(), "MariaDB/MySQL not running")
    def test_errata_mysql_claims(self):
        with ServerDB("mysql") as db:
            r = run("mysql", db, "SET sql_mode='STRICT_ALL_TABLES'; CREATE TABLE d (a DECIMAL(5,1), b DECIMAL(5,2));"
                                 "INSERT INTO d VALUES (9999.9, 999.99); SELECT * FROM d;")
            self.assertIn("9999.9", r.stdout)      # errata #7: DECIMAL(5,1) holds 9999.9
            r = run("mysql", db, "INSERT INTO d VALUES (99999.9, 0);")
            self.assertNotEqual(r.returncode, 0)   # … but not 99999.9
            r = run("mysql", db, "CREATE TABLE a (id INT PRIMARY KEY); CREATE TABLE c (aid INT, FOREIGN KEY (aid) "
                                 "REFERENCES a(id) ON DELETE NO ACTION); INSERT INTO a VALUES (1); INSERT INTO c VALUES (1);"
                                 "DELETE FROM a WHERE id = 1;")
            self.assertNotEqual(r.returncode, 0)   # errata #18: NO ACTION still refuses


if __name__ == "__main__":
    unittest.main()
