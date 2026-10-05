# Research-Gap Project: Disclosure, Governance and the Cost of Capital in Vietnam

A systematic review of 5 papers (provided PDFs) to identify research gaps that are defensible and feasible. The PDFs are the only source of truth. Every load-bearing claim is page-referenced and machine-checked (`source_traceability/`).

## Executive synthesis

**We reviewed 5 papers.** All use Vietnamese listed-firm data (2014–2023, 55–115 firms, T = 3–8).

**The literature splits into 3 research streams:**

- **A. Mandatory-framework CSR / environmental disclosure → cost of equity** (Circular 155 era): P1 (Lê Thị Nhung 2024), P5 (Le, Nguyen & Le 2019).
- **B. GRI/SDG sustainability disclosure → cost of equity, debt and WACC** (Circular 96 / green-growth era): P2 (Nguyen & Duong 2026, JFRA), P3 (Bùi et al. 2025).
- **C. Board/CEO governance → cost of equity:** P4 (Vu & Pham 2023).

**The strongest established findings**, appropriately hedged:

1. **Among large Vietnamese listed firms, sustainability disclosure is *associated* with a lower cost of equity and debt** (P2 FE −0.138* on COE [Table 3, p.1266]; COD −0.029* [Table 4, p.1267]). P1 [Table 8, p.69] and P5 [Table 7, p.94] point the same way, with weaker evidence.
2. **Environmental disclosure carries most of the effect; economic disclosure carries none** (P2 Table 6 [p.1270]). This rests on a single study.
3. **Disclosure levels in Vietnam are low and rising** (P3 Table 1 [p.142]; P5 [p.93]; P2 Appendix [p.1279]). They rose sharply across the Circular 155 transition (P5: 38 → 115 disclosing firms, 2014–2017).

**The evidence base is weaker than the papers' conclusions suggest** (`limitations/evidence_quality_audit.md`):

- In 3 of 4 disclosure papers, the within-firm (FE) estimate on the headline outcome is either not reported (P1) or insignificant (P3 p=0.452; P5 t=−1.16).
- 4 of 5 papers measure COE with CAPM, so cross-sectional COE variation is just beta, and their distributions include impossible values.
- No paper uses a quasi-experiment, lags, or a mechanism test.

**Three important unresolved issues remain:**

1. **Causality.** Two disclosure mandates (Circular 155/2015; Circular 96/2020) fall inside the existing sample windows. P1 even chose its window "before and after Circular 155" [p.64]. **No one has used them to identify a causal effect.**
2. **Which theory?** Papers cite signalling as foundational (P2 [p.1260]) yet pool mandated and voluntary items, so signalling cannot be separated from simple information-asymmetry reduction. The competing cost/legitimacy view is cited in four papers and tested in none.
3. **Mechanism and context.** The information-asymmetry mechanism is asserted in every conclusion and measured in no table. The one sign contradiction (P2 negative vs P3 positive in energy, contradiction C1) is unresolved and may reflect either a legitimacy-vs-signalling context effect or a missing-year-effect artefact.

**Gap 1 is particularly promising** because it turns an existing policy change into an identification strategy: firms' pre-mandate distance to the Circular 155 item list gives a continuous treatment intensity. It answers a live policy question (do disclosure mandates lower financing costs in a weak-enforcement market?) and fixes the literature's central weakness, its reliance on between-firm correlations. Combined with Gap 2 (pricing of voluntary vs mandated items), it also yields a sharp theory test. Its main risk is collecting data from pre-2016 annual reports; Circular 96 (2021) offers a better-covered fallback.

## Top-5 research opportunities

| # | Idea | Gap | Novelty | Feasibility | Overall |
|---|---|---|---|---|---|
| 1 | Disclosure mandates as a quasi-experiment (Circular 155 / 96), continuous-intensity DiD | G1 (+G6) | 4 | 3.5 | **4.1** |
| 2 | Signal or boilerplate: voluntary vs mandated items | G6 | 4 | 4.5 | **4.1** |
| 3 | Mechanism: liquidity vs foreign/institutional investor clientele | G3 | 4 | 4 | **3.9** |
| 4 | Hard vs soft environmental disclosure in sensitive industries (resolves C1) | G4 (+G7) | 3.5 | 4 | **3.7** |
| 5 | Creditor channel with a valid COD measure | G5 | 4 | 3.5 | **3.5** |

Design standard for all five (G2): multiple COE proxies, disclosure dated by report release, firm + year FE, no ex-post sample selection, no Driscoll-Kraay SEs with T<10.

**Before committing to any idea**, run a targeted literature search beyond this corpus (see the caveat in `research_ideas/top5_research_ideas.md`). Novelty here is judged relative to the five provided papers.

## Workspace map

```
research-gap-project/
├── papers/                      5 source PDFs + text/ (page-tagged extractions) + README
├── literature_database/
│   ├── literature_matrix.csv    Phase 2: one row per paper, 21 fields
│   ├── literature_database.json Phase 2: machine-readable, full inventory incl. reviewer flags
│   ├── build_database.py        single source for CSV + JSON
│   └── paper_inventory.md       Phase 1: field-by-field inventory with page refs
├── literature_map/literature_map.md            Phase 3: streams, theories, variables, diagram
├── findings/
│   ├── comparison_matrices.md   Phase 4: theory / variables / data / methods / findings
│   └── findings_classification.csv
├── contradictions/contradictions.md            Phase 5: C1–C7 with the 9-question protocol
├── limitations/
│   ├── limitations.md           Phase 6: explicit vs inferred (A–E)
│   └── evidence_quality_audit.md  Internal-consistency red flags per paper
├── research_gaps/
│   ├── gap_matrix.md            Phases 7–9: gap screen, weak-gap filter, matrix
│   ├── ranked_gaps.md           Phases 10 & 13: scores, ranking, adversarial review
│   └── white_space.md           Phase 12: theory×context, outcome×design, construct, mechanism matrices
├── research_ideas/
│   ├── top10_research_questions.md  Phase 11
│   └── top5_research_ideas.md       Phase 14
└── source_traceability/         Phase 16
    ├── claims.py / verify_claims.py   84 claims with verbatim anchors; script checks each on its page
    ├── claims_register.md / .csv      79 text-verified + 5 visually verified (image tables)
    ├── gap_evidence_map.md            which papers establish vs. leave open each gap
    └── page_mapping.md                PDF page ↔ printed page
```

## Reproduce

```bash
python3 literature_database/build_database.py      # regenerate CSV + JSON
python3 source_traceability/verify_claims.py       # re-check every anchor against the PDF text (exit 1 on failure)
```

## Conventions

- `[PDF p.X / p.Y]` = PDF page X / printed page Y. A bare `[p.Y]` = printed page.
- **[INFERENCE]** = reviewer judgement, not an author statement.
- **(external, verify)** = institutional or method facts not contained in the five PDFs, such as legal effective dates, foreign-ownership limits, green-credit instruments and econometric methods. Verify these before citing.
