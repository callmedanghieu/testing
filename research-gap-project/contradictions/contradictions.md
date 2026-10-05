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
