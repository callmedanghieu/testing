# Phase 5: Contradictions

Every difference between papers was checked. Only differences that concern **the same relationship** and are **not obviously explained by a reporting error** are treated as substantive contradictions.

---

## C1: Sign of sustainability disclosure → cost of equity (P2 negative vs P3 positive)

| Question | Answer |
|---|---|
| 1. Who disagrees? | **P2** (negative: GLS −0.070**, FE −0.138* [Table 3, PDF p.11 / p.1266]) vs **P3** (positive: OLS +10.98***, RE +10.23** [Table 3, PDF p.6 / p.143]). P1 and P5 side with P2 |
| 2. What exactly differs? | Sign of the COE coefficient on a 77-item GRI disclosure index |
| 3. Samples? | Yes. P2: top-100 multi-industry large caps. P3: 58 energy firms, including UPCOM (smaller, less liquid) |
| 4. Periods? | Partly overlapping. P2: 2021–2023. P3: 2019–2023 |
| 5. Measurement? | **IV: essentially the same instrument.** Both use 77 binary GRI items, both report a max score of 0.571 (P2 [Table 2, p.1265]; P3 [Table 1, p.142]). DV: both CAPM with a 10-year Rf, but beta comes from Vietstock in P2 and is self-estimated in P3, and Rf comes from MoF vs Damodaran |
| 6. Methods? | **Yes, and this is decisive.** P2's sign holds in FE. P3's sign **disappears in its own Hausman-preferred FE** (p=0.452). P3 has no year effects; P2 has a COVID (2021) dummy |
| 7. Theoretical assumptions? | P2: signalling (disclosure as a credible signal). P3: legitimacy/stakeholder, with an ex-post compliance-cost and risk-revelation story [PDF p.7 / p.144] |
| 8. Context-dependent? | **Plausible but unproven.** Energy is an environmentally sensitive industry. Legitimacy theory and the "risk revelation" argument predict disclosure there may expose liabilities, which would raise required returns. P5's literature review also cites positive findings in polluting or voluntary settings (Richardson & Welker 2001; Déjean & Martinez 2009) [Table 1, PDF p.4 / p.89] |
| 9. Resolved by anyone? | **No.** P3 does not engage with P2 (P2 was published later), and P2 does not test an industry interaction even though it has the IND dummy |

**Reviewer verdict.** Read most simply, C1 is an artefact of specification:

- P3's positive sign comes from between-firm variation without year effects.
- Over 2021–2023 both disclosure (0.173 → 0.188 [Table 1]) and COE (6.88% → 11.72% [Table 2]) rise in P3's data, so a common time trend can produce a positive pooled coefficient [INFERENCE].

Yet the context-dependence hypothesis (environmentally sensitive firms vs others) is **theoretically meaningful** and **untested**. Neither paper can tell the two explanations apart. **This is a researchable contradiction (→ Gap G4).**

---

## C2: Is the negative disclosure–COE relation robust within firms?

| Paper | Within-firm (FE) estimate | Where significance comes from |
|---|---|---|
| P1 | **Not reported** | GLS [Table 8, PDF p.11 / p.69] |
| P2 (COE) | −0.138* (t=−2.52) | FE and GLS |
| P2 (WACC) | −0.038 (t=−1.34), **n.s.** | GLS only [Table 5, PDF p.13 / p.1268] |
| P3 | +4.79, p=0.452, **n.s.** | OLS/RE only |
| P5 | −45.17 (t=−1.16), **n.s.** | Driscoll-Kraay SE with T=4 [Table 7, PDF p.9 / p.94] |

- **What differs:** the estimator, not the data. In 3 of the 4 disclosure papers, the within-firm estimate on the headline outcome is missing or insignificant.
- **Why it matters:** when disclosure scores move slowly within a firm, FE has little identifying variation, and pooled or GLS estimates are vulnerable to omitted firm traits (size, visibility, governance, state ownership) [INFERENCE].
- **Resolved?** No. No paper discusses the between/within distinction.

**Researchable → Gaps G1 and G2.** Exogenous within-firm changes in disclosure (regulatory mandates) are needed.

---

## C3: State ownership and cost of equity (P2 negative vs P5 positive)

| Question | Answer |
|---|---|
| Who | **P2**: majority-state dummy lowers COE (−0.014* [Table 3, PDF p.11 / p.1266]; text [PDF p.12 / p.1267]). **P5**: state share raises COE (+43.31*** under XTSCC [Table 7, PDF p.9 / p.94]) |
| Measurement | Dummy (>50%) vs continuous %. CAPM COE vs forward E/P |
| Period | 2021–2023 vs 2014–2017. The equitisation and divestment environment may differ; that is external context and needs verification |
| Theory | P2: SOEs get soft credit and implicit guarantees [PDF p.8 / p.1263]. P5: SOEs are "protected by the state" and still have higher COE [PDF p.9 / p.94]. **The same premise yields opposite predictions** |
| Context-dependent? | Likely. P2's literature review also cites Li & Liu (2018): SOEs benefit **more** from CSR disclosure [PDF p.5 / p.1260]. P5's literature review cites Xu et al. (2014): the CSR → COE effect is **weaker** in SOEs [PDF p.6–7 / p.91–92]. **The moderating role of state ownership is contested in the cited international work and untested in Vietnam** |
| Resolved? | No. In both papers SOE is a control, never an interaction |

**Researchable → Gap G9** (a moderator of disclosure effects, not a main effect).

---

## C4: Board size → cost of equity (P3 vs P4): weak

- **P4:** −0.064 (p=0.065) [Table 8, PDF p.9 / p.3093]. **P3:** +0.56 (p=0.058) in OLS, insignificant in FE [Table 3, PDF p.6 / p.143].
- Both results are at the 10% level, in different industries, and P3 uses board size only as a control.

**Not a meaningful contradiction.** Both estimates are fragile, and board size → COE is not a frontier question. Rejected as a gap.

---

## C5: CEO duality → cost of equity (internal to P4)

- DUAL is coded 1 = separate roles [PDF p.2 / p.3086, two passages: "Data collection" and "2.2.1"]. The coefficient is +0.215 (p=0.077), yet it is interpreted as "duality raises COE" [PDF p.9 / p.3093].
- Taken at face value, the estimate says **separation** raises COE, which supports the stewardship view P4 dismisses.

**A reporting/coding inconsistency, not a literature contradiction.** It cannot ground a gap, but it shows that P4's governance evidence should not be treated as established.

---

## C6: Leverage and profitability → cost of equity (controls)

- **Leverage:** positive in P1, P4 and P5; negative and significant in P3's FE (−1.217***) [Table 3, PDF p.6 / p.143]; insignificant for COE in P2.
- **Profitability:** ROA positive in P4 (+2.27***); ROE negative in P3 (OLS); ROA insignificant in P2.

**Interpretation [INFERENCE].** Levered-beta theory predicts that leverage raises the CAPM cost of equity. A significantly negative FE coefficient, and profitability raising COE, are red flags for the COE construct.

**Researchable as a measurement problem → Gap G2**, not as a substantive contradiction.

---

## C7: Environmental vs social vs economic dimensions (P2 internal; P1 call)

- P2 is the only paper to decompose. Environment matters for all outcomes, social only for COD and WACC, economic for none [Table 6, PDF p.15 / p.1270].
- P2 cites Shad et al. (2020): environmental reporting lowers COD but not COE [PDF p.2 / p.1257]. That is a **cross-country contradiction with P2's own Vietnamese finding** that the environment lowers COE too.
- P1 calls for dimension-level work [PDF p.13 / p.71].

**Weak as a standalone gap.** P2 has already decomposed, so another decomposition is near-replication. It is better folded into G4 and G6 as heterogeneity.

---

## Summary

| ID | Relationship | Substantive? | Most likely source of disagreement | Becomes |
|---|---|---|---|---|
| C1 | Disclosure → COE sign | **Yes** | Within/between estimator + missing year FE, or industry context | G4 (and G2) |
| C2 | Within-firm robustness | **Yes** | Estimator choice; slow-moving disclosure; endogeneity | G1, G2 |
| C3 | State ownership | **Yes** | Measurement, period, competing theory | G9 |
| C4 | Board size | No (both weak) | Noise | Rejected |
| C5 | CEO duality | No (coding error) | Reporting | Rejected |
| C6 | Leverage / ROA | As measurement | Noisy CAPM COE | G2 |
| C7 | E/S/Ec dimensions | Weak | Single study | Folded into G4/G6 |

---
---

# Batch 2 Update (added; Batch 1 analysis above unchanged)

## Updates to existing contradictions

### C1 update: disclosure → COE sign is now 5 negative vs 1 positive among Vietnamese papers
- **New evidence:** P6 (GMM, implied COE: −0.065*** [Table 2, PDF p.7 / p.1390]) and P7 (cross-section, implied COE: −0.0016*** [Table 3, PDF p.5 / p.68]) are both negative. Both use **non-CAPM** COE, so the negative sign is not an artefact of CAPM beta.
- **Effect on C1:** P3's positive sign is now more isolated. The two explanations from Batch 1 (missing year effects / between-firm variation, vs industry context) still apply.
- Batch 2 adds a third explanation: **COE proxy.** P3 uses CAPM, so the positive coefficient means disclosure goes with *higher beta* in energy firms. That could be a systematic-risk story specific to energy (e.g., commodity exposure correlated with both disclosure pressure and beta) rather than an information-risk story [INFERENCE].
- **Still unresolved:** no paper tests a disclosure × environmentally-sensitive-industry interaction. P6 includes energy firms but only as an industry dummy, and itself proposes "state-owned firms in high-polluting industries" as future research [PDF p.10 / p.1393]. **G4 stands, with a sharper target.**

### C3 update: state ownership; now a moderator test exists, and it conflicts with its own abstract
- **Main effect:** P6 SOE −0.000*** [Table 5] joins P2 (negative) against P5 (positive): 2 negative vs 1 positive.
- **Moderation (new):** P6 tests CSRD × SOE. The interaction is **positive** (+0.000***, t=3.20) while CSRD is negative, which means state ownership **attenuates** the disclosure benefit [Table 5, PDF p.9 / p.1392].
  - P6's conclusion agrees: "state ownership mediate and attenuate" [PDF p.9 / p.1392].
  - P6's abstract says the opposite: "state ownership strengthens the negative impact" [PDF p.1 / p.1384]. So does H3 ("negative relationship is stronger when the state holds higher ownership") [PDF p.3–4 / p.1386–1387].
- **Cited China evidence still conflicts** (Li & Liu 2018: stronger in SOEs; Xu et al. 2015: weaker), restated by P6 [PDF p.3 / p.1386].
- **Verdict:** C3 is **partly addressed but not resolved**. The only Vietnamese test reports an unscaled coefficient (0.000) and contradicts itself on direction. **G9 is downgraded** (no longer untested) but survives as a *resolution* question.

### C6 update: control-variable signs line up partly with the COE proxy
- **Size.** Positive with implied COE (P6 +0.013***; P7 +0.0067**) and with P8's undefined COE (+0.082, p=0.067). Negative with CAPM in P1, P4 and P9 (−0.0078, p=0.018); positive with CAPM only in P3's OLS.
- **Beta.** Does not explain implied COE (P7: p=0.672; r=−0.027) [Tables 2–3, PDF p.5 / p.68].
- **ROA.** Positive in P6 and P4; negative or n.s. in P3, P9 and P2.
- **Interpretation [INFERENCE].** CAPM-COE (≈ beta) and implied COE are not measuring the same thing in these markets. P7 argues this from theory: CAPM excludes information risk, so it cannot test a disclosure effect [PDF p.3 / p.66]. **This turns G2 from a design note into evidence-backed measurement sensitivity.**

## New contradictions introduced by Batch 2

### C8: Composite governance index → COE (P8 India negative vs P9 Pakistan null/positive)
| Question | Answer |
|---|---|
| Who | **P8:** CGI −0.089 (p=0.021) [Table III, PDF p.15]. **P9:** CGS +0.0018 / +0.0028 (p=0.91 / 0.85) [Tables 9–10, PDF p.20, 22 / p.158, 160] |
| Samples / periods | India BSE 500, 319 firms, 2001–2016 vs Pakistan KSE, 114 firms (57 textile), 2003–2007 |
| Measurement | **Index:** 43 binary items scored only when above the mandatory minimum, 7 sub-indices (P8) vs a 4-attribute banded score weighted 55/45 (P9). **COE:** undefined (P8) vs CAPM (P9) |
| Methods | Pooled OLS (P8) vs industry/year LSDV (P9) |
| Theory | Both agency. P9 adds investor-protection conditionality [PDF p.6, 8 / p.144, 146] |
| Context-dependent? | Plausible. P9 attributes its null to (i) offsetting components, (ii) family-dominated textile firms where investors ignore governance, (iii) the post-2002 Code "transition phase" [PDF p.1, 24 / p.139, 162] |
| Resolved? | No. The papers do not cite each other's findings (P8 cites P9 only for R² magnitude [PDF p.17]) |

**Verdict.** Mostly **measurement-driven**: different index logic and an undefined or CAPM DV. The cross-country comparison is not interpretable as-is. For a Vietnam-focused programme it motivates **G13 (governance measurement validity)**, not a cross-country replication.

### C9: Board independence → COE (P8 negative vs P9 positive n.s. vs P4 n.s.)
- **P8:** board composition sub-index (16 items, including the independent share) −0.068 (p=0.036) [Table III].
- **P9:** board independence +0.001 (p=0.939) [Table 6]. **P4:** BOARDP n.s. [Table 8].
- **P9's own explanation:** Pakistani law does not distinguish independent from non-executive directors, so firms label all NEDs as independent and the variable carries no information [PDF p.23 / p.161].
- **Verdict.** A **measurement-validity contradiction.** The P9 mechanism (label vs substance) is testable for Vietnam, where P4's mean independent share is 0.156 [Table 2, PDF p.5 / p.3089]. → **G13.**

### C10: State-ownership moderation direction (P6 internal; P6 vs cited China studies)
See the C3 update. This is listed separately because it is a **new relationship (a moderation)** with an **internal** contradiction (abstract/H3 vs table/conclusion) and an **external** one (Li & Liu 2018 vs Xu et al. 2015, both restated by P6 [PDF p.3 / p.1386]). → **G9 (resolution).**

### C11: Mediation evidence internally inconsistent (P6)
- Adding the mediator **increases** the direct effect's magnitude (−0.065 → −0.067) [Table 3, PDF p.8 / p.1391]. With a negative indirect path (−0.204 × +0.142 < 0), the direct effect should *shrink*.
- The Sobel table reports indirect −0.006, total 0.033 and direct 0.027 [Table 4]. These match neither the Table 3 path product (≈ −0.029) nor the Table 3 coefficients (0.065 / 0.067).
- **Verdict.** The *existence* of a crash-risk channel is suggested, not established. Mechanism evidence remains thin → **G3** keeps value, re-scoped to (a) the liquidity and investor-base channels and (b) a credible re-test of crash risk.

### C12: Are analyst earnings forecasts available for Vietnamese firms? (data-availability contradiction)
| Paper | Claim |
|---|---|
| P7 (2017) | "a systematic service of providing earnings forecasts by financial analysts is still unavailable in Vietnam" [PDF p.3 / p.66] |
| P4 (2023) | "expected earnings are not available in the Vietnamese market", so PEG is rejected [PDF p.3 / p.3087] |
| **P6 (2022)** | "Refinitiv Eikon normally reports 1- and 2-year ahead forecasts of earnings ... for Vietnam listed firms", though 3-year forecasts are scarce [PDF p.4 / p.1387] |

- **Explanation:** most likely **temporal and source-specific** (coverage grew between 2015 and the 2020s, and differs between Vietnamese databases and Refinitiv) [INFERENCE].
- **Why it matters:** implied-COE measures **are feasible** for Vietnamese research. Two papers already use model-based forecasts that need no analyst data (P6 Harris–Wang; P7 residual income), and analyst-based forecasts exist for covered firms. **This removes the main feasibility objection to G2's design standard.**

## Batch 2 summary

| ID | Relationship | Substantive? | Most likely source | Becomes |
|---|---|---|---|---|
| C1 (upd.) | Disclosure → COE sign | Yes, narrower | P3 isolated; year FE / industry / CAPM-beta explanations | G4, G2 |
| C3 (upd.) | State ownership | Yes | Moderation now tested but self-contradictory | G9 (downgraded to resolution) |
| C6 (upd.) | Control signs by COE proxy | Yes, as measurement | CAPM ≠ implied COE | G2 (strengthened) |
| C8 | Composite governance → COE (India vs Pakistan) | Weak as a substantive conflict | Index logic + DV definition | G13 |
| C9 | Board independence | Yes, as measurement | Label vs substance (P9) | G13 |
| C10 | SOE moderation direction | Yes | Internal reporting conflict; China conflict | G9 |
| C11 | Crash-risk mediation arithmetic | Reporting | Inconsistent tables | G3 (re-scoped) |
| C12 | Analyst-forecast availability | Data / temporal | Coverage growth; database differences | G2 feasibility ↑ |
