# Phase 6: Limitations

**Labels:** **[EXPLICIT]** = stated by the authors (with page). **[INFERENCE]** = reviewer judgement from the research design. The line-by-line red flags are in `evidence_quality_audit.md`.

## A. Explicit limitations (author-acknowledged)

| Paper | Limitation | Source |
|---|---|---|
| P1 | Only the aggregate CSR-disclosure effect is examined | [PDF p.13 / p.71] |
| P2 | 77-item scoring may be inconsistent across reporting styles, so the index may be biased | [PDF p.16 / p.1271] |
| P2 | COD = interest expense / total debt, not actual loan rates | [PDF p.16 / p.1271] |
| P2 | No lagged effects | [PDF p.16 / p.1271] |
| P2 | Endogeneity not addressed (stated as future work) | [PDF p.16 / p.1271] |
| P3 | No limitations section. Discussion concedes that information quality (authenticity, measurement consistency) does not yet earn investor trust | [PDF p.7 / p.144] |
| P4 | None stated | — |
| P5 | Small sample (n=115), not highly representative | [PDF p.10 / p.95] |
| P5 | Non-financial firms only | [PDF p.10 / p.95] |
| P5 | GRI-G4 criteria partly unsuited to Vietnam | [PDF p.10 / p.95] |

## B. Methodological limitations [INFERENCE]

1. **No causal identification in any paper.** Static panels only. No IV, DiD, event study or matching. Reverse causality (low-COE firms disclose more) and omitted variables (visibility, size, governance, state ownership) are unaddressed. (All papers; method sections P1 [p.67], P2 [p.1262], P3 [p.142], P4 [p.3089], P5 [p.92–93].)
2. **Inference rests on between-firm variation or SE corrections.** P1 reports GLS only. P2's WACC result fails in FE. P3's result fails in FE. P5's result is significant only with Driscoll-Kraay SE at T=4, which are unreliable with very short panels. (See contradictions C2.)
3. **Timing mismatch.** Disclosure for year *t* is published in the annual report around Q1–Q2 of *t+1*, while CAPM betas use year-*t* returns. Effect can precede cause (P1, P2, P3). Only P5 aligns prices with report release [PDF p.6 / p.91].
4. **Missing or incomplete year effects.** P1 and P3 have none. P2 has only a 2021 dummy. Disclosure trends upward over time (P3 Table 1; P5 [p.93]; P2 Appendix [p.1279]) while CAPM inputs (Rf, MRP) move with macro conditions, so spurious time correlation is likely.
5. **Model-selection mechanics over economics.** Hausman, then GLS or robust SE, as a ritual. Diagnostic results are sometimes contradicted by the text (P1 Table 7) or not reported at all (P3 robust/GMM).
6. **No mechanism tests.** Information asymmetry is asserted but never measured: no bid–ask spread, Amihud illiquidity, analyst coverage or dispersion, institutional or foreign ownership change.

## C. Data limitations [INFERENCE unless marked]

| Issue | Detail |
|---|---|
| Sample size | 55–115 firms; T = 3–8 |
| Sample selection | Look-ahead/survivorship: P1 uses the 2021 VNR500 list for 2014–2021; P2 uses end-2023 market cap for 2021–2023. P5 "random" sampling conditions on complete annual reports [p.90] |
| Measurement of disclosure | Binary presence/absence only (P1 [p.65], P2 [p.1263], P3 [p.141], P5 [p.91]). No quality, specificity, quantification or assurance. P2 [EXPLICIT] concedes scoring inconsistency |
| Measurement of COE | CAPM in 4 of 5 papers. P1 uses a constant MRP across 2014–2021. P4 notes forward EPS is unavailable in Vietnam [p.3087]. Implausible values: negative COE (P2, P3, P4, P5), mean 38% (P4), mean 135 (P5) |
| Measurement of COD | Only P2, with a crude proxy [EXPLICIT] |
| Missing variables | Disclosure quality/assurance; foreign ownership limits; analyst coverage; liquidity; political connections; SOE as a moderator |
| Geography | Vietnam only (this is by design, not a flaw) |
| Time | Nothing after 2023. The 2022–2023 rate/credit stress, which P3's Table 2 COE jump may reflect, is barely covered and never modelled |
| Industry | P3 energy-only and P4 food-only, so their findings cannot generalise; P1, P2 and P5 cannot speak to industry heterogeneity without interactions |

## D. Theoretical limitations [INFERENCE]

1. **Theory as a list, not a test.** P2 cites six theories that all predict "negative" [p.1259–1260], so its results cannot discriminate among them.
2. **The competing view is never modelled.** The CSR over-investment/agency-cost view (P1 [p.62–63]), costly CSR (P2 citing Goss & Roberts [p.1261]), compliance costs and risk revelation (P3 [p.144]) and decoupling or negative-NPV CSR (P5 [p.89]) all predict a positive or null effect. No paper states when that view should dominate.
3. **Signalling without signal costliness.** P2 calls signalling the foundational theory [p.1260], yet signalling requires discretionary, costly or verifiable signals. Indices that count mandated items (P1 entirely; P2, P3 and P5 partly) conflate compliance with signalling.
4. **No account of who prices the disclosure.** The investor base (foreign institutions vs domestic retail) and the lenders (state-owned banks) are absent from the theory, though both are central to Vietnam's institutional setting.
5. **Governance and disclosure are treated as separate silos** (P4 vs P1–P3, P5). Their complementarity or substitution, for example governance making disclosure credible, is never theorised.

## E. External validity limitations [INFERENCE]

| Dimension | Concern |
|---|---|
| Countries | Single frontier/emerging market. Findings may not transfer to markets with different investor protection. P1 itself cites Breuer et al. (effect limited to strong-protection countries) and Feng et al. (2015) (effect absent in Asia) [PDF p.4 / p.62], which makes Vietnam's negative findings theoretically surprising and in need of explanation |
| Industries | Energy (P3) and food (P4) single-industry results do not generalise. Multi-industry papers do not test heterogeneity |
| Firms | Large caps dominate (P1, P2). Small UPCOM firms appear only in P3 |
| Economic conditions | 2014–2023 includes COVID (P2 dummy). No test of whether the disclosure effect changes with market stress, though P3's literature review notes that crisis-period effects may weaken [PDF p.3 / p.140] |

---
---

# Batch 2 Additions (Batch 1 sections A–E above unchanged)

## A. Explicit limitations: Batch 2 papers

| Paper | Limitation | Source |
|---|---|---|
| P6 | Non-financial firms from one developing market; may not generalise to other institutional settings | [PDF p.10 / p.1393] |
| P6 | Future work: other developing countries; SOEs in high-polluting industries; cross-national samples | [PDF p.10 / p.1393] |
| P7 | No limitations section. Concedes self-generated forecasts, because analyst forecasts were unavailable in Vietnam | [PDF p.3 / p.66] |
| P8 | None stated | — |
| P9 | Governance score limited by unavailability of published governance data | [PDF p.25 / p.163] |
| P9 | Future work: more governance variables; estimate Ke with other models | [PDF p.25 / p.163] |
| P9 | True board independence cannot be determined from published statements | [PDF p.24 / p.162] |

## B. Methodological limitations [INFERENCE]

7. **GMM is not a substitute for exogenous variation (P6).** System GMM with internal instruments addresses dynamic panel bias. It is weaker against persistent omitted traits correlated with both CSR disclosure and COE. Year effects are not reported, and Circular 155 sits inside the 2014–2019 window unused.
8. **Mediation by Baron–Kenny / Sobel (P6)** identifies correlational paths, not causal mechanisms. The mediator (crash risk) is itself endogenous to the same firm traits. The reported path arithmetic is inconsistent (contradiction C11).
9. **Cross-section (P7)** cannot separate disclosure from time-invariant firm quality. The assumption that disclosure policy is stable over time is untested [PDF p.4 / p.67].
10. **Undefined dependent variable (P8):** the COE estimation method is never described, so the result cannot be replicated or interpreted.
11. **"Fixed effects" mislabelled (P8, P9).** P8 reports pooled OLS but discusses FE [PDF p.16]. P9's "fixed effects" are industry dummies [PDF p.14–15 / p.152–153]. Neither controls for firm heterogeneity.
12. **Governance reforms not used for identification (P8, P9):** India Clause 49 / Companies Act 2013; Pakistan Code 2002, which P9 calls a "transition phase" [PDF p.1 / p.139].

## C. Data limitations [INFERENCE unless marked]

| Issue | Detail |
|---|---|
| Sample selection | P6 keeps industry leaders (≥90% of industry assets) and drops negative-earnings firms from the Easton estimation [PDF p.4 / p.1387; App. A]. P8 interpolates/extrapolates missing data and back-fills index replacements [PDF p.8]. P9's sample is textile-dominated (57/114) [PDF p.9 / p.147] |
| Measurement of COE | Implied COE via model-based forecasts (P6 Harris–Wang; P7 ROE × plowback), which can tie COE mechanically to profitability and payout. CAPM with negative values (P9 min −0.93). **Undefined (P8)** |
| Measurement of governance | Above-mandatory scoring (P8) vs banded percentage scores (P9) vs raw attributes (P4). Independence labels may be uninformative (P9 [EXPLICIT, p.161]) |
| Missing variables | General disclosure is never controlled for in the CSR papers. Investor protection (country level) is discussed in P9 but untestable within single-country designs |
| Geography | Now 3 countries, but **no paper is cross-national**, and measures are not comparable |
| Time | Batch 2 adds older periods (2001–2007, P8/P9; 2015, P7; 2014–2019, P6). **Still nothing after 2023** |

## D. Theoretical limitations [INFERENCE]

6. **Mechanism theory now partly operationalised (P6) but narrowly.** Crash risk is one of several channels. P7's trilogy (adverse selection, estimation risk, public/private information) remains untested in Vietnam.
7. **SOE theory gives opposite predictions** (multitask vs inefficiency; P6 [p.1386]). P6's own reporting conflict leaves the question open.
8. **Governance–disclosure interplay remains untheorised in Vietnam**, though P9 points to the substitution/complementarity logic of Chen et al. (2004) [PDF p.8 / p.146].
9. **CSR disclosure vs general disclosure.** No theory or test separates CSR-specific information from general transparency (P7 construct vs P1–P3, P5, P6 constructs).

## E. External validity limitations [INFERENCE]

| Dimension | Concern |
|---|---|
| Countries | India and Pakistan governance papers widen geography but use incompatible designs. They support "results are institution-dependent" (P9's investor-protection argument) rather than generalisation |
| Industries | P9 textile-dominated; P6 industry leaders only; P7 HOSE-only |
| Firms | P6 and P8 skew to large firms; small and UPCOM firms remain under-represented (only P3) |
| Economic conditions | P9 shows large year effects (2007 dummy −0.287) [Table 6], so CAPM-COE is strongly time-varying. Designs without year effects (P1, P3, P6) are exposed to this |
