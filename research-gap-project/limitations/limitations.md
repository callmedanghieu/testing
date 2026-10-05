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
