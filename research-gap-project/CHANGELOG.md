# Changelog

Each batch is added without deleting earlier content. Superseded statements are kept and marked ("Batch 1 view", "v1", "preserved"). Batch 2 additions are marked **[B2]** or appear under "Batch 2" headings.

## Final analysis (all batches complete)

- Added `final_analysis/`:
  - `FINAL_RESEARCH_GAP_REPORT.md`
  - `final_gap_ranking.csv` (15 candidates scored, with verdicts)
  - `corpus_coding.csv` (each paper coded on 22 design features)
  - `tally.py` → `corpus_tallies.md`
- All 15 candidate gaps re-evaluated against the 9-paper corpus:
  - **5 kept:** F1 = G1+G14; F2 = G6+G13+G7; F3 = G4 re-framed; F4 = G3; F5 = G5.
  - **4 merged:** G7, G13 → F2; G14 → F1; G2 → design standard.
  - **6 rejected:** G8, G9, G10, G11, G12, G15.
- **Change vs v2:** G4 is re-framed from "resolve the P3 contradiction" (weak, since P3 is low-grade) to a universal measurement gap: 0/5 CSR papers measure disclosure quality or control for general disclosure. It now ranks above the mechanism gap.
- Earlier files are unchanged; `research_gaps/ranked_gaps.md` points to the final report.

## Batch 2: 4 new papers + 1 duplicate

**Files received:** `c9acc018-thuy2022.pdf`, `0f2c53f6-IMFI_2019_03_Le.pdf`, `1b16cfff-12231-42481-1-SM.pdf`, `f57fe841-srivastava2019.pdf`, `a7eaed52-6_Zulfiqar_Shah2.pdf`

| ID | Paper | Country | What it adds |
|---|---|---|---|
| P6 | Thuy et al. (2022), *CSR&EM* | Vietnam | Implied COE (Easton + Harris–Wang); system GMM; **first mechanism test** (crash risk); **first moderator test** (state ownership) |
| P7 | Nguyen & Nguyen (2017), *IJFR* | Vietnam | General (non-CSR) disclosure; residual-income implied COE; explicit argument that CAPM cannot test disclosure effects; beta does not explain implied COE |
| P8 | Srivastava et al. (2019), *MAJ* | India | Composite governance index scored only above the mandatory minimum; COE measure undefined |
| P9 | Shah & Butt (2009), *Lahore J. Econ.* | Pakistan | CAPM-COE governance study (cited by P4 and P8); null composite effect; "independence label" measurement-validity argument |
| — | `IMFI_2019_03_Le.pdf` | — | **Duplicate of P5** (identical article body; checked automatically). Logged, not counted |

**New streams and themes:** Stream D (general disclosure → implied COE); Stream C becomes cross-country; mechanism and moderation as a cross-cutting theme; governance-index construction; beyond-compliance measurement.

**Contradictions:**
- **Updated:** C1 (now 5 negative vs 1 positive), C3 (moderation tested), C6 (control signs line up partly with the COE proxy).
- **New:** C8 (composite governance: India vs Pakistan), C9 (board independence, label vs substance), C10 (SOE moderation direction; P6 contradicts itself), C11 (P6 mediation arithmetic), C12 (availability of analyst forecasts in Vietnam).

**Gap re-scoring (v2):**
- G1 33→34 (feasibility ↑)
- G3 31→30 (re-scoped)
- G7 28→29 (re-framed)
- G2 25→27 (evidence-backed, feasible)
- G9 29→25 (downgraded: tested by P6)
- New: G13 (26), G14 (28), G15 (24)
- **Top-5 identity and order unchanged.**

**Methods newly present:** system GMM, Baron–Kenny/Sobel mediation, mean-centred interaction, cross-sectional OLS with rank regression, industry/year LSDV. **Still absent in all 9 papers:** DiD, event study, external IV, matching.

**Files changed:**
- `literature_database/`: `papers_batch2.py` (new); `build_database.py` imports it and adds a `batch` field; JSON/CSV regenerated (9 papers + duplicate log); `paper_inventory.md` gets a Batch 2 section.
- `literature_map/literature_map.md`: v2, with Batch 1 statements preserved.
- `findings/comparison_matrices.md`: v2, with P6–P9 columns; `findings_classification.csv` gets 22 rows and a `batch` column.
- `contradictions/`, `limitations/`, `research_gaps/`, `research_ideas/`: Batch 2 sections appended.
- `source_traceability/`: 63 new claims (147 total, all verified) and an automated duplicate check; `page_mapping.md` and `gap_evidence_map.md` extended.
- `README.md`: v2 synthesis added; v1 synthesis preserved.

**Verification notes:** minus signs were lost in the text extraction of P6 and P8 tables, so all coefficient signs used were checked on the rendered PDF pages. P8 has no printed page numbers (online-first), so its citations use PDF pages. P9's PDF metadata title is wrong; its content was identified from the text.

## Batch 1: 5 papers
Initial workspace: P1–P5 (Vietnam). Phases 1–16 built. 84 claims verified.
