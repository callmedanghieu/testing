# SQL learning system: built from your CS50 SQL lectures 0-6

A complete, tested study system made **from the seven lecture transcripts you provided** (CS50's *Introduction to Databases with SQL*, weeks 0 Querying, 1 Relating, 2 Designing, 3 Writing, 4 Viewing, 5 Optimizing, 6 Scaling).
The transcripts are the source of truth. Every lesson, exercise, debugging item and review card points back to exact transcript lines, and every SQL answer has been executed.

| | |
|---|---|
| Modules | 7, one per lecture (module *n* = week *n*) |
| Concepts | 64, each with three-level explanations ([knowledge map](curriculum/knowledge_map.md)) |
| Practice exercises | 105 (103 from the lectures, 2 generated) |
| Debugging items | 32 broken queries/schemas to diagnose and fix (15 from the lectures, 17 generated) |
| Review cards | 80 (quick review, concept check, predict-the-output, debugging, query-writing) |
| Datasets | 10, recreated from the lectures (longlist0, longlist, sea_lions, mbta, charlie, mfa, votes, rideshare, movies, bank) |
| Errata | 26 places where a lecture statement fails when executed ([source-issues.md](analysis/source-issues.md)) |

## Start practising

**In the browser (no install):** open `app/index.html` (keep the `vendor/` folder next to it). SQLite runs inside the page.
The workflow for every exercise: read the question (with the transcript excerpt it comes from) → write SQL → **Run** → inspect → **Check** (compared with the reference result or database state) → feedback → **Hint** 1/2/3 → retry. The **Solution** stays locked until you've made an attempt or used all hints.

**In the terminal (Python 3 only):**
```bash
python3 tools/practice.py              # dashboard + what to do next
python3 tools/practice.py M0-E01       # interactive: type SQL, then :run  :check  :hint  :expected  :solution  :source
python3 tools/practice.py review M3    # spaced-repetition review
python3 tools/build_db.py              # real .db files for `sqlite3 database/mfa.db`
python3 tools/labs.py locks            # two-connection / file-size / CSV-import demos (locks, vacuum, timer, injection, import)
```

## How to use it (suggested routine)

1. Follow the route in [curriculum/roadmap.md](curriculum/roadmap.md): **M0 → M1 → M2 → M3 → M4 → M5 → M6**. Each module page in [curriculum/modules/](curriculum/modules/) lists objectives, concepts, common mistakes, practice, challenge items and **mastery criteria**.
2. For each concept: read the lesson ([lessons/](lessons/)) at all three levels (Intuition → SQL → Practical reasoning), then do the exercises *without* peeking. Take hints one level at a time.
3. When a module's practice is done, do its debugging items, then its review deck. Repeat the deck on days 1, 3, 7, 14 and 30 (the app and CLI schedule this for you).
4. Move on only when you meet the module's mastery criteria.
5. Whenever something surprises you, open the source excerpt (in the app) or `sources/lectureN.txt` at the cited line, and check [analysis/source-issues.md](analysis/source-issues.md).

## What's inside

```
sql-learning-system/
├── README.md                    ← you are here
├── sources/                     the 7 transcripts, byte-identical (every reference is file:line)
├── analysis/
│   ├── inventory.md             Phase 1: document inventory, sections with line ranges, repeated concepts
│   └── source-issues.md         errata & contradictions, each verified by execution
├── curriculum/
│   ├── knowledge_map.md         Phase 2: concept tree + per-concept records (definition, prereqs, syntax, example, mistakes, difficulty, source)
│   ├── roadmap.md               Phase 3: dependency graph, sequence, spaced-review plan, gaps in the material
│   └── modules/M0-M6.md         Phase 4: the 10-part module pages (generated)
├── lessons/M0-M6-*.md           Phase 9: 3-level explanations for every concept
├── database/                    Phase 5: schema.sql + seed.sql per dataset, CSVs, MySQL/Postgres scripts (see database/README.md)
├── content/                     SINGLE SOURCE OF TRUTH: exercises, debugging, review, module definitions (YAML)
├── exercises/source/            Phase 6: exercises taken from the lectures (generated pages)
├── exercises/generated/         exercises written for this system, clearly labelled
├── hints/  solutions/           Phase 8: progressive hints and reference solutions with expected output
├── debugging/                   Phase 11: error-training items
├── review/                      Phase 10: review decks
├── source-mapping/              Phase 12: source→concept, concept→source, item index
├── progress/                    your progress file (terminal trainer) + how to track mastery
├── app/                         Phase 7: the browser trainer (index.html, engine.js, vendor/sql-asm.js)
├── tools/                       build, engine, CLI trainer, labs, DB builder, server starter
└── tests/                       Phase 14: system, server, engine-parity and browser tests
```

**SOURCE vs GENERATED.** Every exercise has an origin label:
* `SOURCE · demo`: the lecturer does this on screen; you reproduce it.
* `SOURCE · question`: the lecturer asks the class this question.
* `SOURCE · assigned`: the lecture explicitly leaves this to you (lecture1 L1461-1466 and L1559-1600, lecture4 L1331-1335, lecture6 L1258-1265).
* `GENERATED`: written for this system to reinforce a concept the lectures cover. It still cites where that concept appears.

Source and generated exercises are kept in separate folders, and the tests fail if one ever lands on the wrong page.

## Editing and rebuilding

Edit `content/*.yaml` (or lessons, knowledge map), then:
```bash
python3 tools/build.py                          # regenerates all pages, app/data.json, app/index.html
python3 -m unittest tests.test_system -v        # 39 checks, stdlib only
tools/start_servers.sh && python3 -m unittest tests.test_servers -v   # MySQL(MariaDB)/PostgreSQL material
node tests/test_engine.js                       # browser engine agrees with the Python engine on every item
NODE_PATH=$(npm root -g) node tests/test_app_browser.js   # end-to-end UI test (needs Playwright)
```
`./run_tests.sh` runs everything that is available on your machine.

## Limitations (honest list)

* **Material coverage.** All seven weeks (0-6) are included; the second upload's copies of lectures 2 and 4 were identical to the first and were dropped. Window functions, CASE, isolation levels and formal normal forms are not in the material, so there are no lessons or debugging items for them ([roadmap § Gaps](curriculum/roadmap.md#gaps-in-the-source-material)).
* **Datasets are reconstructions.** Values the lecture states (ids, titles, balances, accession numbers) are preserved and test-verified. Everything else (other ids, all ratings, swipes, extra rides, the *placeholder* artist) is synthetic and labelled in each seed file. The longlist ratings are engineered so the lectures' printed results come out (averages, top-10s, HAVING results, lecture 4's per-year averages); the one exception is the distinct-publisher count (30 here, 33 in lecture 0).
* **Scale.** `movies` has 19 movies, not 400k. `python3 tools/build_db.py --big` / `tools/labs.py timer` add 300k synthetic rows to reproduce the timing effect.
* **Servers.** MySQL items are self-checked in the trainer and executed on **MariaDB 10.11** in the tests. A few outputs (e.g. `DESCRIBE`) differ cosmetically from MySQL 8.
* **Shell-only features** (`.import`, `.timer`, `.read`, two connections, `du -b`) can't run in a browser. They are covered by `tools/labs.py` and labelled self-check items.
* **Progress** in the web app lives in your browser (`localStorage`). Use *Progress backup* to copy it out. The terminal trainer writes `progress/progress.json`.
* Transcripts contain speech-recognition noise (`[? … ?]`, `[INAUDIBLE]`). Quotes in references match the transcript text, noise included.
