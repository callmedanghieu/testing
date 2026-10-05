"""Terminal SQL trainer: read → write → run → compare → feedback → hints → retry.

    python3 tools/practice.py                 # dashboard + what to do next
    python3 tools/practice.py list [M2]       # all exercises (and debugging items) with your status
    python3 tools/practice.py M2-E13          # interactive session for one item
    python3 tools/practice.py check M2-E13 my.sql   # grade a file non-interactively (exit code 0 = pass)
    python3 tools/practice.py review [M2]     # spaced-repetition review in the terminal
    python3 tools/practice.py due             # review cards due today

Progress is saved in progress/progress.json (plain JSON; commit it if you like).
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import content as C  # noqa: E402
import sqlcheck as S  # noqa: E402

PROGRESS = C.ROOT / "progress" / "progress.json"
ORDER = ["M0", "M1", "M2", "M3", "M4", "M5"]


def load_progress():
    try:
        return json.loads(PROGRESS.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"items": {}, "cards": {}}


def save_progress(p):
    PROGRESS.parent.mkdir(exist_ok=True)
    PROGRESS.write_text(json.dumps(p, indent=2, sort_keys=True))


def all_items():
    return {e["id"]: e for e in C.exercises() + C.debugging()}


def status(p, iid):
    s = p["items"].get(iid, {})
    if s.get("passed"):
        return "✔ solved" + (" (with solution)" if s.get("saw_solution") else f" (hints used: {s.get('hints', 0)})")
    if s.get("self_done"):
        return "✔ self-checked"
    if s.get("attempts"):
        return f"… {s['attempts']} attempt(s)"
    return "· new"


def show_table(res: S.Result, limit=20):
    if res.error:
        print(f"  ERROR: {res.error}")
        return
    if res.columns is None:
        print("  (statement ran; no result set)")
        return
    rows = res.rows or []
    cols = res.columns
    cells = [[("NULL" if v is None else str(v)) for v in r] for r in rows[:limit]]
    widths = [min(40, max([len(c)] + [len(r[i]) for r in cells])) for i, c in enumerate(cols)]
    print("  " + " | ".join(c[:40].ljust(w) for c, w in zip(cols, widths)))
    print("  " + "-+-".join("-" * w for w in widths))
    for r in cells:
        print("  " + " | ".join(v[:40].ljust(w) for v, w in zip(r, widths)))
    if len(rows) > limit:
        print(f"  … {len(rows) - limit} more rows ({len(rows)} total)")
    if not rows:
        print("  (no rows)")


def show_item(e):
    print("=" * 78)
    print(f"{e['id']} · {e['title']}")
    print(f"[{C.ORIGINS[e['origin']]}]")
    print("Source: " + "; ".join(f"{C.ref_label(r)} “{r.get('quote', '')}”" for r in e["source"]))
    print(f"Concepts: {', '.join(e['concepts'])} · Difficulty: {'★' * e['difficulty']} · Dataset: {e.get('db') or 'empty'}")
    print("-" * 78)
    print(textwrap.indent(e["prompt"].strip(), "  "))
    if e.get("template"):
        print(f"\n  Template: {e['template']}\n  (type only the INPUT that replaces {{input}})")
    if e.get("broken"):
        print("\n  Broken SQL to fix:\n" + textwrap.indent(e["broken"].strip(), "    "))


HELP = """Commands (on their own line):
  :run       execute your current SQL against a fresh copy of the dataset and show the result
  :check     grade your current SQL
  :hint      reveal the next hint (3 levels)      :solution  reveal the reference solution
  :expected  show the expected output             :source    print the transcript lines
  :show      show your current SQL                :clear     start your SQL over
  :schema    show the dataset schema              :quit      leave
Anything else is appended to your SQL buffer."""


def session(e, p):
    st = p["items"].setdefault(e["id"], {})
    show_item(e)
    buf = e.get("broken", "").strip() + "\n" if e.get("broken") else ""
    if buf:
        print("\n(The broken SQL is pre-loaded in your buffer. Use :clear to start over.)")
    print("\n" + HELP + "\n")
    hints_shown = st.get("hints", 0)
    while True:
        try:
            line = input("sql> " if not buf else "...> ")
        except EOFError:
            line = ":quit"
        cmd = line.strip()
        if cmd == ":quit":
            break
        if cmd == ":help":
            print(HELP)
        elif cmd == ":show":
            print(buf or "(empty)")
        elif cmd == ":clear":
            buf = ""
        elif cmd == ":schema":
            print(S.dataset_sql(e["db"]).split("INSERT")[0] if e.get("db") else "(empty database)")
            if e.get("setup"):
                print("-- setup:\n" + e["setup"])
        elif cmd == ":source":
            for r in e["source"]:
                a, _, b = str(r["lines"]).partition("-")
                lines = C.source_lines(r["file"])
                print(f"--- {C.ref_label(r)}")
                for i in range(int(a), int(b or a) + 1):
                    print(f"{i:5}  {lines[i - 1]}")
        elif cmd == ":hint":
            if hints_shown < 3:
                print(f"Hint {hints_shown + 1}: {e['hints'][hints_shown]}")
                hints_shown += 1
                st["hints"] = max(st.get("hints", 0), hints_shown)
            else:
                print("No more hints. :solution shows the reference answer.")
        elif cmd == ":solution":
            if input("Reveal the solution? Try one more time first? [y/N] ").lower().startswith("y"):
                print(e["solution"])
                if e.get("explanation"):
                    print("Why: " + e["explanation"].strip())
                st["saw_solution"] = True
        elif cmd == ":expected":
            out = S.reference_output(e)
            print(json.dumps(out, indent=1, default=str)[:3000] if out else "Self-check item.")
        elif cmd == ":run":
            if e["kind"] == "injection":
                sql = e["template"].replace("{input}", buf.strip())
                print("  Running: " + sql)
            else:
                sql = buf
            show_table(S.run_script(S.prepare(e), sql, e.get("continue_on_error", False)))
        elif cmd == ":check":
            if e["kind"] == "selfcheck":
                print("Self-check item. Compare with :solution, then mark it done.")
                if input("Mark as done? [y/N] ").lower().startswith("y"):
                    st["self_done"] = True
                    save_progress(p)
                continue
            st["attempts"] = st.get("attempts", 0) + 1
            ok, msg = S.evaluate(e, buf)
            print(("✔ " if ok else "✘ ") + msg)
            if ok:
                st["passed"] = True
                st["passed_on"] = dt.date.today().isoformat()
                if e.get("explanation"):
                    print("Why it works: " + e["explanation"].strip())
                if e.get("diagnosis"):
                    print("Diagnosis: " + e["diagnosis"].strip())
            else:
                print("Try again, or :hint for a nudge.")
            save_progress(p)
        else:
            buf += line + "\n"
    save_progress(p)


def cmd_list(p, module=None):
    items = all_items()
    for m in ORDER:
        if module and m != module:
            continue
        print(f"\n{m} · {C.MODULE_TITLES[m]}")
        for iid, e in items.items():
            if e.get("module") == m:
                tag = "GEN" if e["origin"] == "generated" else "SRC"
                print(f"  {iid:7} {tag} {'★' * e['difficulty']:4} {e['title'][:48]:48} {status(p, iid)}")


def next_item(p):
    for e in C.exercises() + C.debugging():
        s = p["items"].get(e["id"], {})
        if not (s.get("passed") or s.get("self_done")):
            return e
    return None


def cmd_dashboard(p):
    items = all_items()
    done = sum(1 for i in items if p["items"].get(i, {}).get("passed") or p["items"].get(i, {}).get("self_done"))
    print(f"SQL learning system: {done}/{len(items)} items done; {len(due_cards(p))} review cards due.")
    for m in ORDER:
        ids = [i for i, e in items.items() if e["module"] == m]
        d = sum(1 for i in ids if p["items"].get(i, {}).get("passed") or p["items"].get(i, {}).get("self_done"))
        print(f"  {m} {C.MODULE_TITLES[m]:30} {'█' * d}{'░' * (len(ids) - d)} {d}/{len(ids)}")
    n = next_item(p)
    if n:
        print(f"\nNext up: {n['id']} · {n['title']}. Run: python3 tools/practice.py {n['id']}")


INTERVALS = {"again": 1, "hard": 3, "good": 7, "easy": 14}


def due_cards(p):
    today = dt.date.today().isoformat()
    out = []
    for it in C.review():
        c = p["cards"].get(it["id"])
        if c and c["due"] <= today:
            out.append(it)
    return out


def ask_card(it):
    if it["type"] == "quick":
        print(it["front"])
        input("  (think, then Enter to reveal) ")
        print("  → " + it["back"])
    elif it["type"] in ("concept", "predict"):
        if it["type"] == "predict":
            print(f"Dataset {it.get('db') or 'empty'}" + (f", after setup:\n{it['setup']}" if it.get("setup") else ""))
            print(it["sql"].strip() + "\nWhat is printed?")
        else:
            print(it["question"])
        for i, ch in enumerate(it["choices"]):
            print(f"  {chr(65 + i)}. {ch}")
        ans = input("  Your answer: ").strip().upper()[:1]
        right = chr(65 + it["answer"])
        print(("  ✔ " if ans == right else f"  ✘ Answer: {right}. ") + it["why"].strip())
    else:
        print(f"Do {it['ref']} without hints: python3 tools/practice.py {it['ref']}")


def cmd_review(p, module=None, only_due=False):
    deck = due_cards(p) if only_due else [it for it in C.review() if not module or it["module"] == module]
    if not deck:
        print("Nothing to review." + (" Come back later!" if only_due else ""))
        return
    for it in deck:
        print("\n" + "-" * 60 + f"\n{it['id']}")
        ask_card(it)
        r = input("  Rate: (a)gain (h)ard (g)ood (e)asy, or q to stop: ").strip().lower()[:1]
        if r == "q":
            break
        rating = {"a": "again", "h": "hard", "g": "good", "e": "easy"}.get(r, "good")
        c = p["cards"].get(it["id"], {"interval": 0})
        interval = INTERVALS[rating] if rating == "again" or c["interval"] == 0 else max(INTERVALS[rating], c["interval"] * 2)
        p["cards"][it["id"]] = {"interval": interval,
                                "due": (dt.date.today() + dt.timedelta(days=interval)).isoformat(),
                                "last": rating}
        save_progress(p)


def main(argv):
    p = load_progress()
    items = all_items()
    if not argv:
        return cmd_dashboard(p)
    if argv[0] == "list":
        return cmd_list(p, argv[1] if len(argv) > 1 else None)
    if argv[0] == "review":
        return cmd_review(p, argv[1] if len(argv) > 1 else None)
    if argv[0] == "due":
        return cmd_review(p, only_due=True)
    if argv[0] == "check":
        e = items[argv[1]]
        ok, msg = S.evaluate(e, Path(argv[2]).read_text())
        print(("PASS: " if ok else "FAIL: ") + msg)
        if ok:
            p["items"].setdefault(e["id"], {})["passed"] = True
            save_progress(p)
        return 0 if ok else 1
    if argv[0] in items:
        return session(items[argv[0]], p)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) or 0)
