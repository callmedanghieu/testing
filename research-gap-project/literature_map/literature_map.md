# Phase 3: Literature Map

## 0. What this corpus is

All five papers study one question: **what firm-level information and governance attributes lower the cost of capital of Vietnamese listed firms?**

- Four papers (P1, P2, P3, P5) study **non-financial (CSR / environmental / sustainability) disclosure → cost of capital**.
- One paper (P4) studies **board and CEO governance structure → cost of equity**.
- Every paper uses Vietnamese data. The periods run from 2014 to 2023 and the samples from 55 to 115 firms.
- Every paper uses static panel estimators (pooled OLS / FE / RE / GLS). None uses a quasi-experimental design.

The map is therefore narrow and deep: one country, one outcome family, one estimator family. That shapes what counts as a credible gap (see `research_gaps/`).

## 1. Research streams

The papers are grouped by the construct that does the explaining, not by title.

### Stream A: Mandatory-framework CSR / environmental disclosure → cost of equity (Circular 155 era, 2014–2021)
Papers: **P1** (CSR index built on Circular 155 items, 2014–2021) and **P5** (GRI-G4 environmental index, 2014–2017).

- **Theory:** disclosure reduces information asymmetry, estimation risk and illiquidity (P1 [PDF p.5 / p.63]); social-contract information role (P5 [PDF p.3 / p.88]).
- **Research question:** does more CSR/environmental disclosure lower COE?
- **Findings:** negative in both. P1 reports GLS −6.012*** [Table 8, PDF p.11 / p.69]. P5's negative estimate is significant only after Driscoll-Kraay SEs [Table 7, PDF p.9 / p.94].
- **Method:** FE/RE → GLS (P1) or XTSCC (P5). COE is CAPM-based in P1 and an ex-ante forward earnings yield in P5.
- **Limitations:** both windows straddle Circular 155. P1 chooses its window for that reason [PDF p.6 / p.64], and P5 shows disclosing firms rising from 38 (2014) to 115 (2017) [PDF p.8 / p.93]. Neither exploits the regulatory change. Fragile inference, and no mechanism tested.

### Stream B: GRI/SDG sustainability disclosure → cost of capital (Circular 96 / green-growth era, 2019–2023)
Papers: **P2** (top-100 firms, COE/COD/WACC, 2021–2023) and **P3** (energy firms, COE, 2019–2023).

- **Theory:** P2 lists six theories and treats signalling as primary [PDF p.5 / p.1260]. P3 uses legitimacy and stakeholder theory [PDF p.3 / p.140].
- **Research question:** does the breadth of GRI disclosure lower COE, COD and WACC?
- **Findings:** opposite signs on COE. P2 is negative (GLS −0.070**, FEM −0.138*) [Table 3, PDF p.11 / p.1266]. P3 is positive in OLS/REM but **insignificant in FE** (p=0.452) [Table 3, PDF p.6 / p.143].
- **Method:** both build the index from the same 77 binary GRI items (P2 [PDF p.8 / p.1263]; P3 [PDF p.4 / p.141]), and both report a maximum score of 0.571. Both use CAPM COE.
- **Limitations:** short panels (3 and 5 years), ex-post sample selection (P2), no year effects (P3), and a crude COD proxy (P2, acknowledged [PDF p.16 / p.1271]).

### Stream C: Governance structure → cost of equity
Paper: **P4** (55 food firms, 2015–2022).

- **Theory:** agency vs stewardship [PDF p.9–10 / p.3093–3094].
- **Findings:** weak. Three of six governance variables are significant at 10% only [Table 8, PDF p.9 / p.3093], and the CEO-duality sign is misinterpreted (coding issue).
- **Links to A/B:** P3 controls for board size and Big4 auditor [PDF p.5 / p.142]; P2 controls for state ownership. **No paper links governance with disclosure** (as a moderator of disclosure credibility, for example).

## 2. Cross-cutting map elements

| # | Element | Content (with sources) |
|---|---|---|
| 1 | Major themes | Disclosure → cost of capital (P1, P2, P3, P5); governance → COE (P4); dimension heterogeneity E/S/Ec (P2 Table 6); industry focus on environmentally sensitive sectors (P3 energy, P2 IND dummy) |
| 2 | Major theories | Information asymmetry / disclosure economics (P1, P2, P3); signalling (P2, P1 conclusion); legitimacy (P2, P3); stakeholder (P2, P3); agency (P2, P4); resource dependence and institutional (P2 only); stewardship (P4, as a foil) |
| 3 | Main research questions | Does disclosure lower COE (all four disclosure papers)? Does it lower COD and WACC (P2 only)? Does governance lower COE (P4)? |
| 4 | Common IVs | Binary-item disclosure indices: Circular 155 (P1, 33 items), GRI-2016 (P2, P3, 77 items), GRI-G4 environmental (P5) |
| 5 | Common DVs | CAPM COE (P1, P2, P3, P4); ex-ante earnings-yield COE (P5); COD and WACC (P2 only) |
| 6 | Mechanisms (asserted, **never measured**) | Information asymmetry (P1 [PDF p.12 / p.70], P2 [PDF p.14 / p.1269]); agency costs (P2); risk reduction (P1); compliance costs and risk revelation (P3 [PDF p.7 / p.144]) |
| 7 | Moderators | **None formally tested in any paper.** Candidates appear only as controls: state ownership (P2 GOV, P5 SOE), ESI industry (P2 IND), foreign ownership (P5), Big4 and board size (P3) |
| 8 | Datasets | Hand-coded annual and sustainability reports (all); market data from Investing.com (P1), Vietstock (P2), FiinPro-X (P3), FiinGroup (P4), unspecified (P5) |
| 9 | Methodologies | Static panel: OLS / FE / RE with Hausman → GLS (P1, P2), FE + robust (P3), FE + cluster (P4), FE + Driscoll-Kraay (P5). GMM is mentioned but not reported (P3). **No DiD, IV, event study, PSM or lag structure** |
| 10 | Samples | 55–115 firms; large caps (P1 VNR500, P2 top-100), single industries (P3 energy, P4 food), "random" non-financial firms (P5) |
| 11 | Dominant finding | Disclosure is associated with lower cost of capital (P1, P2, P5). Exception: P3 (positive, but not robust within firms) |

## 3. Conceptual diagram (text form)

```
            THEORY (asserted)                MECHANISM (never measured)          OUTCOME (measured)
  Signalling / Info-asymmetry  ─┐
  Legitimacy / Stakeholder      ├─►  Disclosure breadth (binary item count) ─?─► info asymmetry ─?─► COE (CAPM ≈ beta)
  Agency / Resource dependence ─┘    [P1 Circ.155; P2,P3 GRI-77; P5 GRI-env]      liquidity          COE (ex-ante E/P, P5)
                                                                                  investor base      COD = int/liab (P2)
  Agency vs Stewardship ─────────►  Board structure (P4) ───────────────────────?──────────────────► COE (CAPM)
                                                ▲
                       never linked ────────────┘  (governance as a credibility moderator of disclosure: absent)

  Context controls only: state ownership (P2 −, P5 +), ESI industry (P2), foreign ownership (P5), COVID (P2)
  Regulatory shocks present in the sample windows but unused: Circular 155/2015 (P1, P5 windows); Circular 96/2020 (P2, P3 windows)
```

## 4. Chronology of evidence

| Paper | Sample period | Regulatory regime referenced in paper |
|---|---|---|
| P5 | 2014–2017 | Circular 155/2015 [PDF p.2–3 / p.87–88] |
| P1 | 2014–2021 | Circular 155/2015, window chosen "before and after" [PDF p.6 / p.64] |
| P4 | 2015–2022 | n/a (governance) |
| P3 | 2019–2023 | Circular 155, Circular 96/2020, Resolution 136/NQ-CP [PDF p.2–4 / p.139–141] |
| P2 | 2021–2023 | Circular 96/2020; Decision 1658/QD-TTg green growth 2021–2030 [PDF p.2, 6 / p.1257, 1261] |

Effective dates are not stated in the papers. Circular 155 is commonly cited as effective from 1 Jan 2016 and Circular 96/2020 from 1 Jan 2021. **This is external knowledge and must be verified against the legal texts before use.**
