# Progress

* **Terminal trainer** (`tools/practice.py`) writes `progress.json` here: which items you solved, attempts, how many hints you used, whether you looked at the solution, and your review-card schedule. It is plain JSON, safe to commit so your progress survives a fresh checkout.
* **Web trainer** keeps the same structure in your browser. *Progress backup* in the app copies it out, and pasting a `progress.json` restores it.

## Mastery checklist

Tick these as you go (criteria come from each module page in `curriculum/modules/`):

- [ ] M0: M0-E08 and M0-E10 solved without hints; D0-02 explained; deck R0 ≥ 80%
- [ ] M1: full mbta schema from a blank file (M1-E12); typeof() predictions R1-04/05/08; composite-key trap (M1-E04/D1-04)
- [ ] M2: votes cleaned in ≤ 6 statements (M2-E13); sell/buy triggers from memory (M2-E14); D2-02/03/06 spotted fast
- [ ] M3: current_collections with three INSTEAD OF triggers (M3-E11…E13); view-on-view rewritten as a CTE (M3-E05)
- [ ] M4: two covering indexes for the Tom Hanks query (M4-E03); ROLLBACK recovery (M4-E07); race condition explained (M4-E08)
- [ ] M5: mbta in MySQL and Postgres; double-sale-proof `sell` (M5-E06); sync vs async choice (R5-06); injection + fix (M5-E08/E09)

## Spaced review

Day 1, 3, 7, 14, 30 after finishing a module. Details are in `curriculum/roadmap.md#spaced-review-plan`. `python3 tools/practice.py due` shows today's cards.
