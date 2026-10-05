# Progress

* **Terminal trainer** (`tools/practice.py`) writes `progress.json` here: which items you solved, attempts, how many hints you used, whether you looked at the solution, and your review-card schedule. It is plain JSON, safe to commit so your progress survives a fresh checkout.
* **Web trainer** keeps the same structure in your browser. *Progress backup* in the app copies it out, and pasting a `progress.json` restores it.

## Mastery checklist

Tick these as you go (criteria come from each module page in `curriculum/modules/`):

- [ ] M0: M0-E05, M0-E13, M0-E17 solved without hints; D0-01/D0-02 explained; deck R0 ≥ 80%
- [ ] M1: the two lecture assignments (M1-E17 title lookup, M1-E18 symmetric difference); INNER/LEFT/FULL row counts predicted (R1-04/05); WHERE vs HAVING (D1-07)
- [ ] M2: full mbta schema from a blank file (M2-E12); typeof() predictions R2-04/05/08; composite-key trap (M2-E04/D2-04)
- [ ] M3: votes cleaned in ≤ 6 statements (M3-E13); sell/buy triggers from memory (M3-E14); D3-02/03/06 spotted fast
- [ ] M4: current_collections with three INSTEAD OF triggers (M4-E11…E13); view-on-view rewritten as a CTE (M4-E05)
- [ ] M5: two covering indexes for the Tom Hanks query (M5-E03); ROLLBACK recovery (M5-E07); race condition explained (M5-E08)
- [ ] M6: mbta in MySQL and Postgres; double-sale-proof `sell` (M6-E06); sync vs async choice (R6-06); injection + fix (M6-E08/E09)

## Spaced review

Day 1, 3, 7, 14, 30 after finishing a module. Details are in `curriculum/roadmap.md#spaced-review-plan`. `python3 tools/practice.py due` shows today's cards.
