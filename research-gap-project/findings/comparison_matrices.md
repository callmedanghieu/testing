# Phase 4: Comparison Matrices

✓ = used / tested · ○ = mentioned only · — = absent. All cells trace to the pages in `source_traceability/claims_register.md`.

## 4.1 Theory

| Theory | P1 | P2 | P3 | P4 | P5 | Notes |
|---|---|---|---|---|---|---|
| Information asymmetry / disclosure–CoC (liquidity, estimation risk) | ✓ [p.63] | ✓ | ○ [p.139] | ○ | ○ | The dominant implicit mechanism, never measured |
| Signalling | ○ [p.70] | ✓ main [p.1260] | — | — | — | |
| Legitimacy | — | ✓ | ✓ [p.140] | — | ○ (social contract) | Legitimacy can predict a *weaker* or *positive* effect for reactive disclosers; nobody derives that prediction |
| Stakeholder | — | ✓ | ✓ | — | ○ | |
| Agency | — | ✓ | — | ✓ | — | |
| Resource dependence, institutional | — | ✓ | — | — | — | |
| Stewardship ("management theory") | — | — | — | ○ [p.3093] | — | Named as competing; not tested |
| CSR over-investment / agency cost of CSR | ○ [p.62–63] | ○ (Goss & Roberts [p.1261]) | ○ (compliance cost [p.144]) | — | ○ (negative-NPV CSR [p.89]) | **The competing view is cited in four papers and tested in none** |

**Assessment.**
- Theory is listed, not used to discriminate between predictions. P2 cites six theories that all predict a negative sign, so the result cannot separate them.
- No paper derives a condition under which the theories disagree, such as legitimacy-seeking disclosure by polluters versus signalling by clean firms.
- Mechanisms are underdeveloped. "Reduces information asymmetry" is asserted in every conclusion, but no paper measures asymmetry (spreads, analyst dispersion, illiquidity, investor base).

## 4.2 Variables and proxies

| Construct | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| Disclosure framework | Circular 155, 33 items | GRI-2016, 77 items | GRI, 77 items | — | GRI-G4 environmental |
| Scoring | binary presence | binary presence | binary presence | — | binary presence |
| Quality / credibility dimension | — | — (greenwashing discussed [p.1271]) | — (quality concerns [p.144]) | — | — |
| Mandatory vs voluntary split | all mandatory items | mixed, not split | mixed (15 items in Circ.155 [p.141]), not split | — | mixed, not split |
| COE proxy | CAPM: 1-yr Rf, constant MRP | CAPM: 10-yr Rf, Vietstock beta | CAPM: 10-yr Rf (Damodaran) | CAPM: rolling 12-m beta | Forward E/P ("PEG") |
| COD | — | interest / total liabilities | — | — | — |
| Timing of disclosure vs COE | contemporaneous | contemporaneous | contemporaneous | n/a | price after report release ✓ |
| Year effects | — (μ only) | COVID dummy only | — | ✓ year dummies | — |
| State ownership | — | GOV dummy (>50%) | — | — | SOE % |
| Foreign ownership | — | — | — | — | FOR % |
| Industry sensitivity | — | IND (ESI) | energy-only sample | food-only sample | — |
| Governance | — | — | board size, Big4 | 6 variables | — |

**Same construct, different measures.**
- "Disclosure" is a 33-item compliance checklist (P1), a 77-item GRI checklist (P2, P3) or an environmental-only checklist (P5).
- "COE" is CAPM with a 1-year Rf and constant MRP (P1), CAPM with a 10-year Rf (P2, P3, P4), or an earnings yield (P5).

These choices are not innocuous:

- Under CAPM with a common Rf and MRP, the **cross-sectional variation in COE is only beta**, so "disclosure → COE" is really "disclosure → beta" [INFERENCE].
- Information-risk theory (estimation risk, which P1 itself cites [p.63]) predicts effects on expected returns beyond beta. A CAPM proxy is therefore a weak test of the mechanism the papers invoke [INFERENCE].
- Several distributions are implausible: negative COE (P2 min −0.057 [Table 2, p.1265]; P3 negative minima [Table 2, p.143]), a mean COE of 38% (P4 [Table 2, p.3089]), and a mean of 135 with min −414 (P5 [Table 4, p.92]).

**Consistently omitted:**
- Disclosure quality or assurance.
- Mechanism variables (liquidity, analyst coverage, information asymmetry).
- Firm and year fixed effects together (only P4 has both, and it is not a disclosure paper).
- Lags.
- Any instrument or exogenous shock.

## 4.3 Data

| Dimension | Coverage |
|---|---|
| Countries | Vietnam only (all five) |
| Exchanges | HOSE/HNX (P1, P2, P5); +UPCOM (P3); unspecified (P4) |
| Industries | Multi-industry non-financial (P1, P5); top-100 multi-industry (P2); energy (P3); food (P4) |
| Firm types | Large firms (P1 VNR500, P2 top-100 market cap); SOE/foreign variation only as controls |
| Periods | 2014–2017 (P5), 2014–2021 (P1), 2015–2022 (P4), 2019–2023 (P3), 2021–2023 (P2). **No sample extends past 2023** |
| Panel length | T = 3 (P2), 4 (P5), 5 (P3), 8 (P1, P4) |
| Sources | Hand-coded reports (all); Investing.com, Vietstock, FiinPro-X, FiinGroup |

## 4.4 Methodology

| Method | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| Pooled OLS | ✓ | ✓ | ✓ | ✓ | — |
| Fixed effects | ✓ (coef. not reported) | ✓ | ✓ (insignificant) | ✓ (final) | ✓ |
| Random effects | ✓ | ✓ | ✓ | ✓ | ✓ |
| FGLS | ✓ final | ✓ final | — | — | — |
| Robust / cluster / Driscoll-Kraay SE | — | — | claimed | cluster | XTSCC (T=4) |
| GMM | — | — | claimed, not reported | — | — |
| Instrumental variables | — | — | — | — | — |
| Difference-in-differences | — | — | — | — | — |
| Event study | — | — | — | — | — |
| Propensity score / matching | — | — | — | — | — |
| Natural / quasi-natural experiment | — | — (cites Zhao & Huang 2024, a China quasi-experiment, in further reading [p.1278]) | — | — | — |
| Machine learning / text analysis | — | — | — | — | — |
| Lagged IV | — | — (acknowledged [p.1271]) | — | — | — |

**Patterns and weaknesses.**

1. Every paper follows the same template: OLS → FE/RE → Hausman → fix heteroskedasticity. None treats endogeneity, which P2 itself calls the main future task [p.1271].
2. Final inference often rests on FGLS or SE corrections rather than within-firm variation:
   - P2's WACC result is significant in GLS but not in FE [Table 5].
   - P5's result becomes significant only with Driscoll-Kraay SE at T=4 [Table 7].
   - P3's sign comes from OLS/RE, not from the Hausman-preferred FE [Table 3].
   - P1 never reports its FE coefficient.
3. Reverse causality is never discussed: lower-COE, larger, better-resourced firms can afford to disclose more.
4. A natural identification source, mandated disclosure (Circular 155; Circular 96), sits inside the sample windows of P1, P5, P2 and P3 and is never used.

## 4.5 Findings classification (main relationships)

| Relationship | P1 | P2 | P3 | P4 | P5 | Overall |
|---|---|---|---|---|---|---|
| Disclosure → COE | **Negative** (GLS) | **Negative** (GLS & FE) | **Positive** in OLS/RE; **insignificant** in FE | — | **Negative** only with DK-SE; insignificant in FE | **Mixed / fragile**: negative in large-cap multi-industry samples, positive or null in energy |
| Disclosure → COD | — | Negative (GLS & FE) | — | — | — | Single study |
| Disclosure → WACC | — | Negative (GLS); insignificant (FE) | — | — | — | Single study, fragile |
| Environmental disclosure → COE | (embedded in index) | Negative (−0.090***) | (energy; total index positive) | — | Negative (fragile) | Context-dependent |
| Social disclosure → COE | — | Insignificant (−0.030) | — | — | — | Single study |
| Economic disclosure → CoC | — | Insignificant | — | — | — | Single study |
| State ownership → COE | — | Negative (GOV −0.014*) | — | — | **Positive** (SOE +43.3***) | **Contradictory** |
| Foreign ownership → COE | — | — | — | — | Positive | Single study |
| Board size → COE | — | — | Positive in OLS (p=0.058), n.s. in FE | Negative (p=0.065) | — | Contradictory, weak |
| Big4 → COE | — | — | Negative in OLS/RE, n.s. in FE | — | — | Single, fragile |
| CEO duality → COE | — | — | — | Ambiguous (coding conflict) | — | Uninterpretable |
| Leverage → COE | Positive | Insignificant | **Negative** (FE ***) | Positive | Positive | Mostly positive; P3 anomaly |
| Size → COE | Negative | Insignificant | Positive in OLS/RE | Negative (10%) | Negative | Mixed |
| ROA/ROE → COE | — | Insignificant | Negative in OLS | **Positive** *** | — | Contradictory |

The control-variable contradictions (leverage, ROA, size) matter. The capital-structure prediction that leverage raises the cost of equity is basic theory, yet P3 reports the opposite sign. This points to **measurement noise in CAPM-based COE in Vietnam** [INFERENCE], and that noise affects the disclosure coefficients too.
