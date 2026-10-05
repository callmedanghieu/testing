# Phase 4: Comparison Matrices (v2, after Batch 2)

✓ = used / tested · ○ = mentioned only · — = absent. Columns P1–P5 are Batch 1 and unchanged; **P6–P9 are Batch 2 [B2]**. Cells trace to `source_traceability/claims_register.md`. P8 has no printed page numbers, so its citations are PDF pages.

## 4.1 Theory

| Theory | P1 | P2 | P3 | P4 | P5 | P6 [B2] | P7 [B2] | P8 [B2] | P9 [B2] | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| Information asymmetry / disclosure–CoC (liquidity, estimation risk) | ✓ [p.63] | ✓ | ○ [p.139] | ○ | ○ | ✓ [p.1385] | ✓ main: adverse selection, estimation risk, public/private info [p.64–65] | — | ○ | The dominant mechanism. **[B2]** Still never measured directly; P6 measures crash risk instead |
| Signalling | ○ [p.70] | ✓ main [p.1260] | — | — | — | ○ (CSR as a signal to long-term investors [p.1386]) | — | — | ○ (governance as a signal of investor protection [p.142–143]) | |
| Legitimacy | — | ✓ | ✓ [p.140] | — | ○ (social contract) | — | — | — | — | Legitimacy can predict a *weaker* or *positive* effect for reactive disclosers; nobody derives that prediction |
| Stakeholder | — | ✓ | ✓ | — | ○ | ○ | — | — | — | |
| Agency | — | ✓ | — | ✓ | — | — | — | ✓ [PDF p.2–3] | ✓ | |
| Resource dependence, institutional | — | ✓ | — | — | — | — | — | — | — | |
| Stewardship ("management theory") | — | — | — | ○ [p.3093] | — | — | — | — | — | Named as competing; not tested |
| CSR over-investment / agency cost of CSR | ○ [p.62–63] | ○ (Goss & Roberts [p.1261]) | ○ (compliance cost [p.144]) | — | ○ (negative-NPV CSR [p.89]) | ○ ("CSR implies costs for firms" [p.1384]) | — | — | — | **Cited in five papers, tested in none** |
| **[B2]** CSR as risk management / crash risk | ○ (risk reduction [p.62]) | — | — | — | — | ✓ tested as mediator | — | — | — | First tested mechanism in the corpus |
| **[B2]** SOE multitask vs SOE inefficiency | — | ○ (state ownership advantages [p.1263]) | — | — | ○ (state protection [p.94]) | ✓ (H3) [p.1386] | — | — | — | Competing SOE predictions stated explicitly only in P6 |
| **[B2]** Law & finance / investor protection (substitution vs complementarity) | ○ (Breuer; Feng [p.62]) | ○ | — | — | — | ○ (Breuer 2018 cited) | — | ○ (La Porta [PDF p.7]) | ○ (Klapper & Love; Chen et al. 2004 [p.144, 146]) | Country-level moderation discussed, never tested |

**Assessment.**
- *Batch 1 (preserved):* theory is listed, not used to discriminate between predictions. No paper derives a condition under which theories disagree. "Reduces information asymmetry" is asserted but never measured.
- **[B2]** P6 is the first paper to state **competing** predictions (SOE multitask → stronger effect vs SOE inefficiency → weaker) and test them. P7 gives the cleanest statement of the disclosure-economics channels, but tests none of them separately.
- **[B2]** P9's literature review gives a theory with **conditional** predictions: disclosure lowers COE only where investor protection is strong, governance only where it is weak (Chen et al. 2004) [PDF p.8 / p.146]. If disclosure and governance are substitutes or complements, interaction tests become meaningful (→ G7).

## 4.2 Variables and proxies

| Construct | P1 | P2 | P3 | P4 | P5 | P6 [B2] | P7 [B2] | P8 [B2] | P9 [B2] |
|---|---|---|---|---|---|---|---|---|---|
| Disclosure framework | Circular 155, 33 items | GRI-2016, 77 items | GRI, 77 items | — | GRI-G4 environmental | GRI-2016, 33 criteria (6/8/19) | Botosan (1997) annual-report index, 105 points | — | — |
| Scoring | binary presence | binary presence | binary presence | — | binary presence | binary presence | weighted points | governance: binary, **1 only if above mandatory minimum** | banded 1–5 scores, weights 55/45 |
| Quality / credibility dimension | — | — (greenwashing [p.1271]) | — (quality concerns [p.144]) | — | — | — | partial (projected information and MD&A items) | n/a | n/a (independence labels uninformative [p.161]) |
| Mandatory vs voluntary split | all mandatory items | mixed, not split | mixed (15 items in Circ.155), not split | — | mixed, not split | mixed, not split | mixed, not split | **governance: voluntary-only by design** | — |
| COE proxy | CAPM: 1-yr Rf, constant MRP | CAPM: 10-yr Rf, Vietstock beta | CAPM: 10-yr Rf (Damodaran) | CAPM: rolling 12-m beta | Forward E/P ("PEG") | **Implied: Easton + Harris–Wang forecasts** | **Implied: residual income, self-forecasts** | **Undefined** | CAPM: 2-yr monthly beta |
| COD | — | interest / total liabilities | — | — | — | — | — | — | — |
| Timing of disclosure vs COE | contemporaneous | contemporaneous | contemporaneous | n/a | price after report release ✓ | not stated | price 3 months after year-end (partly aligned) | not stated | contemporaneous |
| Year effects | — (μ only) | COVID dummy only | — | ✓ year dummies | — | — (industry only) | n/a (cross-section) | — (industry only) | ✓ year dummies |
| Firm effects | FE/GLS | FE/GLS | FE | FE | FE | GMM (dynamic) | n/a | — (pooled) | — (industry dummies only) |
| State ownership | — | GOV dummy (>50%) | — | — | SOE % | **SOE % as moderator** | — | (promoter-ownership item in index) | (ownership concentration) |
| Foreign ownership | — | — | — | — | FOR % | — | — | (foreign institutional ownership item in index) | — |
| Industry sensitivity | — | IND (ESI) | energy-only sample | food-only sample | — | 8 industry dummies | — | industry dummies | 15 industry dummies |
| Governance | — | — | board size, Big4 | 6 variables | — | — | — | 43-item CGI, 7 sub-indices | 5 attributes + CGS |
| **[B2]** Mediator | — | — | — | — | — | CRASH (DUVOL) | — | — | — |

**Same construct, different measures (updated).**
- "Disclosure" now has five operationalisations: Circular 155 checklist (P1), 77-item GRI (P2, P3), 33-criterion GRI (P6), environmental-only (P5), and the Botosan general-disclosure index (P7).
- "COE" now has five: CAPM in three variants (P1; P2–P4; P9), forward E/P (P5), Easton implied (P6), residual-income implied (P7), and undefined (P8).
- **[B2] New evidence that the COE proxy matters:**
  - P7 finds beta unrelated to implied COE (r = −0.027, n.s.; coefficient p=0.672) [Tables 2–3, PDF p.5 / p.68]. CAPM-COE, which varies cross-sectionally only through beta, may therefore capture little of what implied-COE measures.
  - The firm-size sign also lines up partly with the proxy (see 4.5).
- *Batch 1 (preserved):* under CAPM with common Rf/MRP, cross-sectional COE variation is only beta [INFERENCE]; implausible distributions in P2, P3, P4, P5.
- **[B2]** P9 adds another negative CAPM-COE minimum (Ke min −0.93 [Table 2, PDF p.11 / p.149]).
- **[B2]** P6 and P7 report plausible implied-COE distributions: means 10.8% and 14.84%, no negatives [P6 Table 1; P7 Table 1].

**Consistently omitted (updated):**
- Disclosure quality or assurance.
- Liquidity and investor-base mechanisms (crash risk now covered by P6).
- Firm and year FE together in any *disclosure* paper.
- Lags.
- Exogenous shocks.
- **[B2] General disclosure as a control when estimating CSR effects** (P7's construct is never controlled for in P1–P3, P5, P6).

## 4.3 Data

| Dimension | Coverage |
|---|---|
| Countries | *Batch 1:* Vietnam only. **[B2]:** Vietnam (P1–P7), India (P8), Pakistan (P9) |
| Exchanges | HOSE/HNX (P1, P2, P5); +UPCOM (P3); unspecified (P4); **[B2]** HOSE only (P7); Vietnam all exchanges (P6); BSE 500 (P8); KSE (P9) |
| Industries | Multi-industry non-financial (P1, P5, **P6, P7, P8, P9**); top-100 (P2); energy (P3); food (P4); **P9 textile-dominated (57/114)** |
| Firm types | Large firms (P1, P2; **[B2] P6 industry leaders covering ≥90% of industry assets; P8 BSE 500**); SOE variation as a moderator only in **P6** |
| Periods | 2014–2017 (P5), 2014–2021 (P1), 2015–2022 (P4), 2019–2023 (P3), 2021–2023 (P2); **[B2]** 2014–2019 (P6), 2015 (P7), 2001–2016 (P8), 2003–2007 (P9). **Still nothing after 2023** |
| Panel length | T = 3 (P2), 4 (P5), 5 (P3, **P9**), **6 (P6)**, 8 (P1, P4), **16 (P8)**; **cross-section (P7)** |
| Sources | Hand-coded reports (all); Investing.com, Vietstock, FiinPro-X, FiinGroup; **[B2] Refinitiv Eikon, with 1–2-year analyst forecasts for Vietnam (P6); FiinPro (P7); CMIE ProwessIQ (P8)** |

## 4.4 Methodology

| Method | P1 | P2 | P3 | P4 | P5 | P6 [B2] | P7 [B2] | P8 [B2] | P9 [B2] |
|---|---|---|---|---|---|---|---|---|---|
| Pooled / cross-sectional OLS | ✓ | ✓ | ✓ | ✓ | — | ○ (mentioned) | ✓ (White SE) | ✓ final | ✓ |
| Fixed effects (firm) | ✓ (coef. not reported) | ✓ | ✓ (insignificant) | ✓ (final) | ✓ | — | — | estimated for Hausman only | — (industry dummies called "FE") |
| Random effects | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | estimated for Hausman only | — |
| FGLS | ✓ final | ✓ final | — | — | — | — | — | — | — |
| Robust / cluster / Driscoll-Kraay SE | — | — | claimed | cluster | XTSCC (T=4) | (GMM) | White | — | — |
| GMM | — | — | claimed, not reported | — | — | **✓ system GMM, lagged DV** | — | — | — |
| Instrumental variables (external) | — | — | — | — | — | — (internal GMM instruments only) | — | — | — |
| Difference-in-differences | — | — | — | — | — | — | — | — | — |
| Event study | — | — | — | — | — | — | — | — | — |
| Propensity score / matching | — | — | — | — | — | — | — | — | — |
| Natural / quasi-natural experiment | — | — (cites China quasi-experiment [p.1278]) | — | — | — | — | — | — | — |
| Machine learning / text analysis | — | — | — | — | — | — | — | — | — |
| Lagged IV | — | — (acknowledged [p.1271]) | — | — | — | — | — | — | — |
| **[B2]** Formal mediation (Baron–Kenny / Sobel) | — | — | — | — | — | ✓ | — | — | — |
| **[B2]** Moderation (interaction term) | — | — | — | — | — | ✓ (mean-centred) | — | — | — |
| **[B2]** Rank / non-parametric regression | — | — | — | — | — | — | ✓ | — | — |
| **[B2]** Industry/year LSDV | — | — | — | — | — | (industry dummies) | — | (industry dummies) | ✓ |

**Patterns and weaknesses (Batch 1, preserved).**
1. Same template everywhere: OLS → FE/RE → Hausman → fix heteroskedasticity. None treats endogeneity.
2. Final inference often rests on FGLS or SE corrections rather than within-firm variation (P2 WACC, P5, P3, P1).
3. Reverse causality never discussed.
4. Mandated disclosure (Circular 155; Circular 96) sits inside the windows of P1, P5, P2, P3 and is never used.

**[B2] Updates.**
5. **P6 is the first paper to address endogeneity** (system GMM, Hansen/AR(2) reported). But GMM's internal instruments (lagged levels/differences) do not solve reverse causality from persistent firm traits as convincingly as an external shock would. No year effects are reported [INFERENCE].
6. **P6 also straddles Circular 155** without exploiting it. That makes three Vietnamese papers (P1, P5, P6) with the shock inside their window.
7. **Governance papers use even weaker designs:** pooled OLS (P8, 16-year panel, interpolated data) and industry-dummy LSDV (P9). India's Clause 49 / Companies Act 2013 and Pakistan's 2002 Code fall inside or just before their windows, and P9 itself attributes its results to a post-Code "transition phase" [PDF p.1 / p.139]. Neither paper uses those reforms for identification.
8. **P7 shows a cross-sectional design** can be reasonably clean (implied COE, robust SE, rank regression) but cannot address firm heterogeneity.

## 4.5 Findings classification (main relationships)

| Relationship | P1 | P2 | P3 | P4 | P5 | P6 [B2] | P7 [B2] | P8 [B2] | P9 [B2] | Overall (v2) |
|---|---|---|---|---|---|---|---|---|---|---|
| Disclosure → COE | **Negative** (GLS) | **Negative** (GLS & FE) | **Positive** OLS/RE; **n.s.** FE | — | **Negative** only with DK-SE | **Negative** (GMM, implied, −0.065***) | **Negative** (cross-section, implied, −0.0016***) | — | — | **Predominantly negative (5 of 6 Vietnamese papers)**; P3 sole exception and not robust within firms. *Batch 1 verdict was "mixed / fragile"* |
| Disclosure → COD | — | Negative | — | — | — | — | — | — | — | Single study |
| Disclosure → WACC | — | Negative (GLS); n.s. (FE) | — | — | — | — | — | — | — | Single study, fragile |
| Environmental disclosure → COE | (embedded) | Negative (−0.090***) | (energy; total positive) | — | Negative (fragile) | (embedded in 33 criteria) | — | — | — | Context-dependent |
| Social disclosure → COE | — | n.s. | — | — | — | — | — | — | — | Single study |
| Economic disclosure → CoC | — | n.s. | — | — | — | — | — | — | — | Single study |
| **[B2]** CSR disclosure → crash risk | — | — | — | — | — | Negative (−0.204***) | — | — | — | Single study |
| **[B2]** Crash risk → COE | — | — | — | — | — | Positive (+0.142***) | — | — | — | Single study |
| State ownership → COE | — | Negative (GOV −0.014*) | — | — | **Positive** (SOE +43.3***) | Negative (−0.000***; magnitude unreported) | — | — | — | **Contradictory** (2 negative vs 1 positive) |
| **[B2]** State ownership × disclosure → COE | — | — | — | — | — | **Attenuates** per Table 5 (+0.000***); abstract says "strengthens" | — | — | — | Single study, internally inconsistent |
| Foreign ownership → COE | — | — | — | — | Positive | — | — | — | — | Single study |
| **[B2]** Composite governance index → COE | — | — | — | — | — | — | — | **Negative** (−0.089, p=0.021) | **Positive, n.s.** (p=0.85–0.91) | **Contradictory** across India and Pakistan |
| Board independence / composition → COE | — | — | — | n.s. | — | — | — | Negative (board composition sub-index, p=0.036) | Positive, n.s. | **Contradictory**; measurement validity questioned (P9) |
| **[B2]** Audit committee → COE | — | — | — | — | — | — | — | Negative (p=0.035) | Positive, n.s. | Contradictory |
| Board size → COE | — | — | Positive OLS (p=0.058), n.s. FE | Negative (p=0.065) | — | — | — | (control, not reported) | Negative (p≈0.09) | Weakly negative (2 of 3 at 10%) |
| Big4 → COE | — | — | Negative OLS/RE, n.s. FE | — | — | — | — | (in audit sub-index) | — | Single, fragile |
| CEO duality → COE | — | — | — | Ambiguous (coding conflict) | — | — | — | — | — | Uninterpretable |
| Leverage → COE | Positive | n.s. | **Negative** (FE ***) | Positive | Positive | n.s. (−0.004) | — | n.s. (−0.031) | — | Mostly positive or n.s.; P3 anomaly |
| Size → COE | Negative | n.s. | Positive OLS/RE | Negative (10%) | Negative | **Positive*** (implied)** | **Positive** (implied)** | Positive (p=0.067) | **Negative** (CAPM) | **Mixed; partly aligned with the COE proxy**: both implied-COE papers positive, 3 of 4 CAPM papers with a significant sign negative |
| ROA/ROE → COE | — | n.s. | Negative OLS | **Positive** *** | — | **Positive*** | — | — | n.s. | Contradictory |
| **[B2]** Beta → COE (non-CAPM DV) | — | — | — | — | Positive (XTSCC) | — | **n.s.** (implied) | — | — | Beta does not explain implied COE in P7 |

**Implications.**
- *Batch 1 (preserved):* control-variable contradictions point to measurement noise in CAPM-based COE in Vietnam [INFERENCE].
- **[B2]** Batch 2 strengthens this. In P7, beta does not predict implied COE, and size flips sign between implied-COE papers (P6, P7: positive) and most CAPM papers (P1, P4, P9: negative). The disclosure coefficient survives across proxies (negative in both implied-COE papers), which raises confidence in the *direction* of the disclosure effect. Its *magnitude and mechanism* remain proxy-dependent [INFERENCE].


---
---

# Appendix: v1 (Batch 1) text, verbatim

The complete Batch 1 version of this file, kept unchanged for the record. The v2 sections above supersede it only where marked [B2].

<details><summary>Show v1 text</summary>

## [v1] Phase 4: Comparison Matrices

✓ = used / tested · ○ = mentioned only · — = absent. All cells trace to the pages in `source_traceability/claims_register.md`.

### [v1] 4.1 Theory

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

### [v1] 4.2 Variables and proxies

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

### [v1] 4.3 Data

| Dimension | Coverage |
|---|---|
| Countries | Vietnam only (all five) |
| Exchanges | HOSE/HNX (P1, P2, P5); +UPCOM (P3); unspecified (P4) |
| Industries | Multi-industry non-financial (P1, P5); top-100 multi-industry (P2); energy (P3); food (P4) |
| Firm types | Large firms (P1 VNR500, P2 top-100 market cap); SOE/foreign variation only as controls |
| Periods | 2014–2017 (P5), 2014–2021 (P1), 2015–2022 (P4), 2019–2023 (P3), 2021–2023 (P2). **No sample extends past 2023** |
| Panel length | T = 3 (P2), 4 (P5), 5 (P3), 8 (P1, P4) |
| Sources | Hand-coded reports (all); Investing.com, Vietstock, FiinPro-X, FiinGroup |

### [v1] 4.4 Methodology

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

### [v1] 4.5 Findings classification (main relationships)

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

</details>
