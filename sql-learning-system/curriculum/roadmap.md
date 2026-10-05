# Learning roadmap

## Dependency graph (concept level)

Arrows point from a concept to the concepts that need it. Concept IDs are defined in [knowledge_map.md](knowledge_map.md).

```mermaid
graph LR
  subgraph M0[M0 Query toolkit]
    C01[C0.1 SELECT] --> C02[C0.2 WHERE] --> C05[C0.5 Subqueries] --> C06[C0.6 JOIN]
    C01 --> C03[C0.3 ORDER BY]
    C01 --> C04[C0.4 GROUP BY]
  end
  subgraph M1[M1 Designing]
    C11[C1.1 shell & schema.sql] --> C14[C1.4 CREATE TABLE]
    C14 --> C15[C1.5 types] --> C16[C1.6 PK/FK] --> C17[C1.7 column constraints]
    C14 --> C12[C1.2 normalizing] --> C13[C1.3 relationships]
    C14 --> C18[C1.8 ALTER TABLE]
  end
  subgraph M2[M2 Writing]
    C21[C2.1 INSERT] --> C22[C2.2 violations] --> C23[C2.3 multi-row / INSERT SELECT] --> C24[C2.4 .import]
    C25[C2.5 DELETE] --> C26[C2.6 ON DELETE]
    C27[C2.7 UPDATE] --> C28[C2.8 cleaning]
    C29[C2.9 triggers]
    C210[C2.10 soft delete]
  end
  subgraph M3[M3 Viewing]
    C31[C3.1 view] --> C32[C3.2 simplify] & C33[C3.3 aggregate] & C36[C3.6 partition] & C37[C3.7 secure]
    C33 --> C34[C3.4 temp view] --> C35[C3.5 CTE]
    C38[C3.8 INSTEAD OF]
  end
  subgraph M4[M4 Optimizing]
    C41[C4.1 timer/scan] --> C42[C4.2 index] --> C43[C4.3 covering] & C44[C4.4 B-tree] & C45[C4.5 partial]
    C44 --> C46[C4.6 VACUUM]
    C47[C4.7 transactions] --> C48[C4.8 races] --> C49[C4.9 locks]
  end
  subgraph M5[M5 Scaling]
    C51[C5.1 servers] --> C52[C5.2 MySQL types] --> C53[C5.3 MODIFY] & C55[C5.5 Postgres types]
    C51 --> C54[C5.4 procedures] & C56[C5.6 scaling] & C57[C5.7 access control]
    C58[C5.8 injection]
  end
  C02 --> C14
  C16 --> C21
  C17 --> C22
  C02 --> C25 & C27
  C05 --> C25 & C27 & C23
  C04 --> C28 & C33
  C06 --> C32
  C18 --> C210
  C27 --> C210
  C21 --> C29
  C29 --> C38
  C210 --> C38
  C02 --> C41
  C05 --> C43
  C17 --> C47
  C27 --> C47
  C15 --> C52
  C210 --> C54
  C37 --> C57
  C02 --> C58
```

## Recommended sequence

The lectures' own order (design → write → view → optimize → scale) is already a sound progression, so it is **kept**. Five changes were made:

1. **Module 0 added in front.** All five lectures assume weeks 0-1 (SELECT, WHERE, GROUP BY, subqueries, JOIN). Without them, lecture 4's views and lecture 5's Tom Hanks query are unreadable. Every M0 exercise is built from a query that appears in these transcripts.
2. **In M1, constraints are grouped by kind**, not by when they were spoken. The lecture introduces NOT NULL/UNIQUE (L915-1022), detours into the CharlieCard redesign, and then returns to CHECK/DEFAULT (L1231-1305). Here C1.7 holds all four.
3. **In M2, "UPDATE for re-attribution" and "UPDATE for cleaning" are separate steps** (C2.7 → C2.8), because cleaning also needs GROUP BY and LIKE.
4. **Soft deletion spans M2 → M3 → M5**, as in the sources: flag (lecture3) → view + INSTEAD OF triggers (lecture4) → stored procedure (lecture6). The exercises follow this arc, so you revisit one design three times with new tools.
5. **Two optional shortcuts.** Transactions (C4.7-C4.9) depend only on M1-M2, and SQL injection (C5.8) depends only on M0. If you work with a production app, you can study them early.

| Step | Module | Core concepts | Est. study time | Exercises (source + generated) | Gate to move on (mastery criteria) |
|---|---|---|---|---|---|
| 0 | [M0 Query toolkit](modules/M0.md) | C0.1-C0.6 | 2-3 h | 10 + 6 debugging | All M0 practice exercises pass without the final hint |
| 1 | [M1 Designing](modules/M1.md) | C1.1-C1.8 | 4-5 h | 13 + 4 debugging | You can write the full mbta schema from a blank file |
| 2 | [M2 Writing](modules/M2.md) | C2.1-C2.10 | 5-6 h | 15 + 6 debugging | votes cleanup and the sell/buy triggers from memory |
| 3 | [M3 Viewing](modules/M3.md) | C3.1-C3.8 | 4-5 h | 13 + 3 debugging | current_collections with all three INSTEAD OF triggers |
| 4 | [M4 Optimizing](modules/M4.md) | C4.1-C4.9 | 4-5 h | 12 + 4 debugging | Reach a covering-index plan for the Tom Hanks query; explain ACID with the bank example |
| 5 | [M5 Scaling](modules/M5.md) | C5.1-C5.8 | 4-6 h | 11 + 2 debugging | Translate mbta to MySQL and Postgres; explain sync vs async replication; demo injection vs a bound parameter |

## Spaced review plan

Use the review decks in [`../review/`](../review/) (or the **Review** tab in the app). After finishing a module, review it on this schedule, counting from the day you finish it:

| When | What |
|---|---|
| Day 1 (same day) | The module's quick-review and concept-check items |
| Day 3 | Predict-the-output items + 2 debugging items |
| Day 7 | Re-solve 3 exercises from the module **without hints** (pick ones you needed hints for) |
| Day 14 | Mixed deck: this module + all earlier modules |
| Day 30 | Write one full solution from scratch for the module's capstone (listed in each module page) |

The app's Review tab records your self-rating (Again / Hard / Good / Easy) for each card and schedules the next review: Again = 1 day, Hard = 3 days, Good = 7 days, Easy = 14 days. Each successful review doubles the interval.

## Gaps in the source material

These are **not** taught in the five transcripts, so this system does not invent lessons for them. Learn them from another source when needed:
- Weeks 0-1 content as *teaching* (M0 is only a toolkit recap): LEFT/RIGHT/FULL OUTER JOIN, set operations other than the UNION in the injection demo, `CASE`, `HAVING`, `DISTINCT`, NULL handling in aggregates.
- **Window functions** (`OVER`, `PARTITION BY`, `RANK`, ...): never mentioned. No window-function lessons or debugging items exist here.
- Recursive CTEs, `UPSERT`/`ON CONFLICT`, `RETURNING`, JSON functions, date arithmetic functions.
- Formal normal forms (1NF/2NF/3NF), which lecture2 L251-254 mentions only by name.
- Isolation *levels* (READ COMMITTED, SERIALIZABLE, ...) and MVCC; lecture5 covers only SQLite's database-level locks.
- Stored-procedure control flow (IF / loops) and OUT parameters: lecture6 L1254-1277 only names them.
