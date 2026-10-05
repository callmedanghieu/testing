# Phase 3: Literature Map

**Version 2 (after Batch 2).** Batch 1 statements are kept verbatim where still valid. Where Batch 2 changes them, the original is preserved under "Batch 1 view" and the update is marked **[B2]**.

## 0. What this corpus is

**[B2] Current corpus: 9 unique papers (P1–P9) from 10 files** (one Batch 2 file duplicates P5).

The core question is unchanged: **what firm-level information and governance attributes lower the cost of capital?** Batch 2 widens it:

- **Disclosure → cost of capital (6 papers, all Vietnam):** P1, P2, P3, P5 (Batch 1) + **P6** (CSR, implied COE, mediation/moderation) + **P7** (general annual-report disclosure, implied COE).
- **Governance → cost of equity (3 papers, 3 countries):** P4 (Vietnam) + **P8** (India) + **P9** (Pakistan).
- Periods now span **2001–2023**; samples range from 55 to 319 firms.
- **Methods widen:** system GMM (P6), formal mediation tests (P6), cross-sectional OLS (P7), long pooled panels (P8), industry/year LSDV (P9). **Still no DiD, IV, event study or matching.**
- **Implied (non-CAPM) COE now appears in Vietnam** (P6, P7), alongside the forward earnings yield in P5.

> **Batch 1 view (preserved):** All five papers study one question: what firm-level information and governance attributes lower the cost of capital of Vietnamese listed firms? Four papers (P1, P2, P3, P5) study non-financial disclosure → cost of capital; one (P4) studies governance → COE. All use Vietnamese data (2014–2023, 55–115 firms) and static panel estimators; none uses a quasi-experimental design. The map was narrow and deep: one country, one outcome family, one estimator family.

## 1. Research streams

Papers are grouped by the construct that does the explaining, not by title.

### Stream A: Mandatory-framework CSR / environmental disclosure → cost of equity (Circular 155 era, 2014–2021)
Papers: **P1** (Circular 155 items, 2014–2021), **P5** (GRI-G4 environmental, 2014–2017), **[B2] P6** (GRI-2016, 33 criteria, 2014–2019).

- **Theory:** disclosure reduces information asymmetry, estimation risk and illiquidity (P1 [PDF p.5 / p.63]); social-contract information role (P5 [PDF p.3 / p.88]). **[B2]** P6 adds CSR as risk management (crash and idiosyncratic risk) and SOE multitask vs inefficiency theory [PDF p.2–3 / p.1385–1386].
- **Research question:** does more CSR or environmental disclosure lower COE? **[B2]** P6 also asks *through what* (crash risk) and *for whom* (state ownership).
- **Findings:** negative in all three.
  - P1: GLS −6.012*** [Table 8, PDF p.11 / p.69].
  - P5: significant only with Driscoll-Kraay SEs [Table 7, PDF p.9 / p.94].
  - **[B2]** P6: GMM −0.065*** on implied COE [Table 2, PDF p.7 / p.1390]; crash risk a partial mediator (18.5% of the total effect) [Table 4]; state ownership **attenuates** the effect per the table, though the abstract says "strengthens" [Table 5, PDF p.9 / p.1392].
- **Method:** FE/RE → GLS (P1); XTSCC (P5); **[B2]** system GMM + Sobel (P6). COE is CAPM in P1, a forward earnings yield in P5, and **Easton implied COE with Harris–Wang forecasts in P6**.
- **Limitations:** all three windows straddle Circular 155.
  - P1 chose its window for that reason [PDF p.6 / p.64].
  - P5 shows disclosers rising from 38 (2014) to 115 (2017) [PDF p.8 / p.93].
  - **[B2]** P6 calls Circular 155 "the most essential document for regulating CSR in Vietnam" [PDF p.2 / p.1385].
  - **None exploits the regulatory change.**
  - **[B2]** P6 shows 225 firms with CSR data from 2014 [PDF p.4 / p.1387], so pre-mandate disclosure data exist at scale.

### Stream B: GRI/SDG sustainability disclosure → cost of capital (Circular 96 / green-growth era, 2019–2023)
Papers: **P2** (top-100, COE/COD/WACC, 2021–2023) and **P3** (energy, COE, 2019–2023). *Unchanged by Batch 2.*

- **Theory:** P2 lists six theories and treats signalling as primary [PDF p.5 / p.1260]. P3 uses legitimacy and stakeholder theory [PDF p.3 / p.140].
- **Findings:** opposite signs on COE. P2 is negative (GLS −0.070**, FEM −0.138*) [Table 3, PDF p.11 / p.1266]. P3 is positive in OLS/REM but **insignificant in FE** (p=0.452) [Table 3, PDF p.6 / p.143].
- **Method:** same 77-item GRI frame, both maximum 0.571; both CAPM COE.
- **Limitations:** short panels, ex-post selection (P2), no year effects (P3), crude COD (P2).
- **[B2] Effect of Batch 2:** P6 and P7 add two more negative Vietnamese estimates using *implied* COE. P3's positive sign is now the only non-negative disclosure–COE result among six Vietnamese papers (see contradiction C1 update).

### Stream C: Governance → cost of equity (now cross-country)
Papers: **P4** (Vietnam, food, 2015–2022), **[B2] P8** (India, BSE 500, 2001–2016), **[B2] P9** (Pakistan, KSE, 2003–2007).

- **Theory:** agency in all three. P4 adds stewardship as a foil [PDF p.9–10 / p.3093–3094]. **[B2]** P8 adds law and finance [PDF p.7]. P9 adds investor-protection **substitution vs complementarity** (Klapper & Love; Chen et al. 2004) [PDF p.6, 8 / p.144, 146].
- **Findings:** weak and inconsistent across countries.
  - P4: 3 of 6 variables at 10%, with a duality coding contradiction [Table 8, PDF p.9 / p.3093].
  - **[B2]** P8: composite index negative (−0.089, p=0.021), with board composition, audit committee and ownership sub-indices driving it [Table III, PDF p.15].
  - **[B2]** P9: composite score positive and insignificant (p=0.85–0.91); only board size marginal [Tables 6, 9, 10].
- **Method:** FE + cluster (P4); pooled OLS (P8); industry/year LSDV (P9). COE: CAPM (P4, P9); **undefined (P8)**.
- **Measurement insights [B2]:**
  - P8 scores items 1 only when the firm exceeds the mandatory minimum [PDF p.9].
  - P9 notes that "independence" labels are uninformative where law does not distinguish independent from non-executive directors [PDF p.23 / p.161].
- **Links to A/B/D:** P3 controls for board size and Big4; P2 and P6 for state ownership. **Still no paper models governance as a moderator of disclosure credibility in Vietnam.** P9's literature review shows this has been studied in cross-country emerging-market work (Chen et al. 2004, disclosure and governance jointly) [PDF p.8 / p.146].

### [B2] Stream D (new): General (financial / annual-report) disclosure → implied cost of equity
Paper: **P7** (225 HOSE firms, FY2015 cross-section).

- **Theory:** three classic disclosure channels (adverse selection, estimation risk, public/private information) [PDF p.1–2 / p.64–65]. This is the most explicit statement of disclosure-economics theory in the corpus.
- **Finding:** Botosan-score disclosure lowers residual-income implied COE (−0.0016***, t=−4.33) [Table 3, PDF p.5 / p.68]. Beta does not explain implied COE (p=0.672; r=−0.027) [Tables 2–3].
- **Why a separate stream:** the construct is *financial/annual-report transparency*, not CSR. P7 is the Vietnamese baseline the CSR papers should be compared against: does CSR disclosure add anything beyond general disclosure quality? No paper in the corpus controls for general disclosure when estimating the CSR effect.

### [B2] Cross-cutting theme (new): Mechanism and moderation
- **First mechanism test in the corpus:** P6 (crash risk mediates CSR → COE).
- **First formally tested moderator:** P6 (state ownership).
- **Not tested:** the liquidity, adverse-selection and investor-base channels theorised in P1 [p.63] and P7 [p.64–65].

## 2. Cross-cutting map elements

| # | Element | Batch 1 content (preserved) | [B2] Additions |
|---|---|---|---|
| 1 | Major themes | Disclosure → CoC (P1, P2, P3, P5); governance → COE (P4); E/S/Ec heterogeneity (P2 T6); environmentally sensitive sectors (P3, P2 IND) | General disclosure → implied COE (P7); mechanism/moderation (P6); cross-country governance (P8, P9); governance index construction (P8, P9) |
| 2 | Major theories | Information asymmetry (P1, P2, P3); signalling (P2, P1); legitimacy (P2, P3); stakeholder (P2, P3); agency (P2, P4); resource dependence, institutional (P2); stewardship (P4) | Disclosure-economics trilogy (P7); CSR-as-risk-management and crash risk (P6); SOE multitask (P6); law and finance (P8); investor-protection substitution/complementarity (P9) |
| 3 | Main research questions | Does disclosure lower COE / COD / WACC? Does governance lower COE? | Through which channel (P6)? For which owners (P6)? Does general disclosure lower implied COE (P7)? Does a composite governance index lower COE in India and Pakistan (P8, P9)? |
| 4 | Common IVs | Binary-item disclosure indices: Circular 155 (P1, 33), GRI-2016 (P2, P3, 77), GRI-G4 environmental (P5) | GRI-2016, 33 criteria (P6); Botosan 105-point index (P7); governance indices: 43-item beyond-compliance (P8), weighted 4-attribute CGS (P9) |
| 5 | Common DVs | CAPM COE (P1, P2, P3, P4); forward E/P (P5); COD, WACC (P2) | **Implied COE**: Easton + Harris–Wang (P6), residual income (P7); CAPM (P9); undefined (P8) |
| 6 | Mechanisms | Asserted, never measured (P1, P2, P3) | **Crash risk measured and tested (P6)**; liquidity, adverse selection and investor base still unmeasured |
| 7 | Moderators | None formally tested; controls only | **State ownership tested (P6)**; country investor protection discussed but not tested (P9 lit review) |
| 8 | Datasets | Hand-coded reports; Investing.com, Vietstock, FiinPro-X, FiinGroup | Refinitiv Eikon, including 1- and 2-year analyst forecasts for Vietnamese firms (P6 [PDF p.4 / p.1387]); FiinPro (P7); CMIE ProwessIQ (P8); hand-collected Pakistani data (P9) |
| 9 | Methodologies | Static panels; GMM mentioned but unreported (P3); no DiD/IV/event/PSM/lags | System GMM + Sobel (P6); cross-sectional OLS + rank regression (P7); pooled OLS (P8); LSDV (P9). **Still no DiD, IV, event study, PSM** |
| 10 | Samples | 55–115 firms; large caps; single industries | 225 (P6, P7), 319 (P8), 114 (P9); India and Pakistan added |
| 11 | Dominant finding | Disclosure associated with lower CoC (P1, P2, P5); P3 exception | **Strengthened:** 5 of 6 Vietnamese disclosure papers negative, including both implied-COE papers. **Governance → COE: mixed** across P4, P8, P9 |

## 3. Conceptual diagram (text form, v2)

```
            THEORY                              MECHANISM                                   OUTCOME
  Signalling / Info-asymmetry  ─┐                                                           COE: CAPM ≈ beta (P1-P4, P9)
  Legitimacy / Stakeholder      ├─►  CSR / sustainability disclosure ──► crash risk [TESTED, P6] ──► COE: implied (P6, P7), fwd E/P (P5)
  Agency / Resource dependence ─┘    [P1,P2,P3,P5,P6]                ─?─► liquidity / adverse selection [untested]
                                                                      ─?─► investor base (foreign/institutional) [untested]
  Disclosure-economics trilogy ───►  General disclosure (P7) ──────────────────────────────► COE: implied (P7)
                                         ▲ never jointly modelled with CSR disclosure
  Agency / Law & finance ─────────►  Governance: individual (P4, P9) / composite (P8, P9) ───► COE (CAPM P4/P9; undefined P8)
                                         ▲ (governance as credibility moderator of disclosure: absent in VN;
                                            cross-country version cited in P9: Chen et al. 2004)

  Moderators: state ownership TESTED (P6, attenuates per table); otherwise controls only (P2 GOV, P5 SOE, P5 FOR, P2 IND)
  Regulatory shocks inside sample windows, unused: Circular 155/2015 (P1, P5, P6); Circular 96/2020 (P2, P3);
       India Clause 49 / Companies Act 2013 (P8 window); Pakistan Code of CG 2002 (P9 attributes results to "transition phase")
```

## 4. Chronology of evidence

| Paper | Country | Sample period | Regulatory regime referenced in paper |
|---|---|---|---|
| P9 [B2] | Pakistan | 2003–2007 | Code of Corporate Governance 2002 [PDF p.1–2 / p.139–140] |
| P8 [B2] | India | 2001–2016 | Clause 49 (2000, revised 2014); Companies Act 2013 [PDF p.4–6] |
| P5 | Vietnam | 2014–2017 | Circular 155/2015 [PDF p.2–3 / p.87–88] |
| P7 [B2] | Vietnam | 2015 (cross-section) | none |
| P6 [B2] | Vietnam | 2014–2019 | Circular 155/2015; SSC–IFC 2013 sustainability-reporting handbook [PDF p.2 / p.1385] |
| P1 | Vietnam | 2014–2021 | Circular 155/2015, window chosen "before and after" [PDF p.6 / p.64] |
| P4 | Vietnam | 2015–2022 | n/a (governance) |
| P3 | Vietnam | 2019–2023 | Circular 155, Circular 96/2020, Resolution 136/NQ-CP [PDF p.2–4 / p.139–141] |
| P2 | Vietnam | 2021–2023 | Circular 96/2020; Decision 1658/QD-TTg [PDF p.2, 6 / p.1257, 1261] |

Effective dates are not stated in the Vietnamese papers. Circular 155 is commonly cited as effective from 1 Jan 2016 and Circular 96/2020 from 1 Jan 2021. **This is external knowledge; verify against the legal texts.**


---
---

# Appendix: v1 (Batch 1) text, verbatim

The complete Batch 1 version of this file, kept unchanged for the record. The v2 sections above supersede it only where marked [B2].

<details><summary>Show v1 text</summary>

## [v1] Phase 3: Literature Map

### [v1] 0. What this corpus is

All five papers study one question: **what firm-level information and governance attributes lower the cost of capital of Vietnamese listed firms?**

- Four papers (P1, P2, P3, P5) study **non-financial (CSR / environmental / sustainability) disclosure → cost of capital**.
- One paper (P4) studies **board and CEO governance structure → cost of equity**.
- Every paper uses Vietnamese data. The periods run from 2014 to 2023 and the samples from 55 to 115 firms.
- Every paper uses static panel estimators (pooled OLS / FE / RE / GLS). None uses a quasi-experimental design.

The map is therefore narrow and deep: one country, one outcome family, one estimator family. That shapes what counts as a credible gap (see `research_gaps/`).

### [v1] 1. Research streams

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

### [v1] 2. Cross-cutting map elements

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

### [v1] 3. Conceptual diagram (text form)

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

### [v1] 4. Chronology of evidence

| Paper | Sample period | Regulatory regime referenced in paper |
|---|---|---|
| P5 | 2014–2017 | Circular 155/2015 [PDF p.2–3 / p.87–88] |
| P1 | 2014–2021 | Circular 155/2015, window chosen "before and after" [PDF p.6 / p.64] |
| P4 | 2015–2022 | n/a (governance) |
| P3 | 2019–2023 | Circular 155, Circular 96/2020, Resolution 136/NQ-CP [PDF p.2–4 / p.139–141] |
| P2 | 2021–2023 | Circular 96/2020; Decision 1658/QD-TTg green growth 2021–2030 [PDF p.2, 6 / p.1257, 1261] |

Effective dates are not stated in the papers. Circular 155 is commonly cited as effective from 1 Jan 2016 and Circular 96/2020 from 1 Jan 2021. **This is external knowledge and must be verified against the legal texts before use.**

</details>
