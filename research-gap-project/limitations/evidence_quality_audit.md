# Evidence-Quality Audit (reviewer red flags)

**Purpose.** Before building gaps on "established findings", check whether those findings are internally consistent. Every item cites the table or page where it can be verified. Items marked [INFERENCE] are reviewer interpretations; the rest are directly observable in the PDFs.

## Summary grade

| Paper | Grade | Why |
|---|---|---|
| P2 (JFRA 2026) | **Moderate** | Coherent design and reporting. Short T, ex-post sample, crude COD, identical FE/RE columns in Table 4 |
| P5 (IMFI 2019) | **Low–moderate** | Ex-ante COE and correct timing are strengths. The text contradicts Table 6, and the key result depends on Driscoll-Kraay SE with T=4 |
| P1 (JTS 2024) | **Low** | Impossible descriptive statistics, diagnostics contradicted by text, unlabelled inference statistics |
| P3 (HaUI 2025) | **Low** | Headline sign not supported by its own preferred model; claimed robustness not reported |
| P4 (IJRPR 2023) | **Low** | Variable-coding contradiction on the key governance variable, implausible COE, unexplained loss of 99 observations |

**Implication.** The only finding with moderate support is "sustainability disclosure is associated with lower COE and COD among Vietnamese large caps in 2021–2023" (P2), and even that is associational. Gaps framed as "we know X" must be stated cautiously.

## P1: Lê Thị Nhung (2024)
1. **Impossible SDs** [Table 3, PDF p.9 / p.67]. CSRI: SD 4.172 with range 0.048–0.895. LEV: SD 2.194 with range 0.218–0.839. A standard deviation cannot exceed half the range for bounded data; these values are arithmetically impossible.
2. **Diagnostics vs text** [Table 7, PDF p.11 / p.69]. Heteroskedasticity p=0.2351 and autocorrelation p=0.3065, yet the text says both are present and moves to GLS.
3. **Unlabelled parentheses** [Table 8]. CSRI −6.012*** (−0.09). If the parenthesis is a t-stat, the estimate is insignificant; if it is a p-value, a negative value is impossible.
4. **VIF mismatch.** Text 1.29 vs table 1.25 [PDF p.10 / p.68].
5. **FEM coefficient not reported**, although Hausman and F-tests select FEM [Table 6].
6. [INFERENCE] The COE construction (annual beta, 1-year Rf, constant 2014–2021 MRP [PDF p.6–7 / p.64–65]) means cross-sectional variation is beta only.
7. [INFERENCE] Sample drawn from the 2021 VNR500 list (look-ahead).

## P2: Nguyen & Duong (2026)
1. Negative minimum COE (−0.057) [Table 2, PDF p.10 / p.1265].
2. **Table 4: the FEM and REM columns are identical** for every coefficient and t-statistic [PDF p.12 / p.1267]. Possibly a copy error; it cannot be verified.
3. Table 4 OLS: SDG −0.026 (t=−2.48) carries no star while weaker coefficients do.
4. WACC: FEM insignificant (t=−1.34); significance only in GLS [Table 5].
5. COVID dummy = 2021 is the only time control [Table 1, PDF p.9 / p.1264].
6. Sample: top-100 by end-2023 market cap [PDF p.6 / p.1261], i.e. ex-post selection. Exclusion of financial firms not stated.
7. The "robust test" is in fact a dimension decomposition [PDF p.14 / p.1269], not a robustness check.

## P3: Bùi et al. (2025)
1. **Headline sign unsupported by the preferred model.** Hausman p=0.0000 selects FEM, where PTBVDN = +4.79, p=0.452 [Table 3, PDF p.6 / p.143; verified on the rendered page]. The text nonetheless says "the FEM results show a positive effect" [PDF p.6 / p.143].
2. Robust SE and GMM are described as applied [PDF p.7 / p.144] but no estimates are shown.
3. The F-test is described as choosing "between OLS and REM" [PDF p.5 / p.142]; it selects between OLS and FEM.
4. No year effects in the specification [PDF p.4 / p.141].
5. Negative COE minima in 2019, 2020 and 2022 [Table 2, PDF p.6 / p.143].
6. Leverage negative and highly significant in FE (−1.217***), contrary to levered-beta theory.

## P4: Vu & Pham (2023)
1. **DUAL coding contradiction.** Coded 0 = CEO is chair, 1 = separate [PDF p.2 / p.3086, two passages: "Data collection" and "2.2.1"]; Table 1 expects "+" [PDF p.4 / p.3088]; the positive estimate is read as "duality raises COE" [PDF p.9 / p.3093]. Under the stated coding, the estimate means separation raises COE.
2. COE mean 0.38 (38%), SD 0.545, range −0.811 to 1.308 [Table 2, PDF p.5 / p.3089].
3. 440 observations described, **341 used** [Tables 4, 5, 8], with no explanation.
4. Board size: mean 5.748 [Table 2] vs "average … is 7 people" [PDF p.10 / p.3094].
5. GROWTH 95% CI [.542, .546] excludes its point estimate .294 [Table 8, PDF p.9 / p.3093].
6. "F test that all u_i=0: F(12,269)" [Table 5, PDF p.7 / p.3091]. [INFERENCE] A numerator df of 12 implies 13 panel units, not 55.
7. Interviews are cited as the basis for adding variables [PDF p.1 / p.3085]; no method is reported.
8. Abstract and conclusion claim governance lowers COE, but only 3 of 6 governance variables are significant, all at 10%, and one is mis-signed (item 1).

## P5: Le, Nguyen & Le (2019)
1. **Text vs table.** The text says REM shows a *positive* significant relation [PDF p.8 / p.93]; Table 6 shows CED = −62.49 [verified on the rendered page].
2. REM t=−1.66 is marked ** (5%), although |t|<1.96.
3. FEM CED −45.17: t=−1.16 (conventional) vs t=−6.93 (XTSCC) [Tables 6–7, PDF p.8–9 / p.93–94]. [INFERENCE] Driscoll-Kraay SEs need a reasonably long T; with T=4 they are unreliable, so the significance is fragile.
4. COE = FEPS(t+1)/P [PDF p.6 / p.91] is a forward earnings yield, not Easton's PEG (P4 shows the PEG formula [PDF p.3 / p.3087]). Mean 135.46, min −414.1, max 1015.3; units unstated [Table 4, PDF p.7 / p.92].
5. The title says "CSR"; the construct measured is environmental disclosure only.
6. Of the firms, 38 disclosed in 2014 and 115 in 2017 [PDF p.8 / p.93], so CED variation is dominated by the Circular 155 transition [INFERENCE].

## Cross-paper observation
P2 and P3 both use 77 binary GRI items and both report a maximum disclosure score of exactly 0.571 (P2 Table 2; P3 Table 1, year 2023). This is consistent with a shared or equivalent scoring instrument, and possibly the same top-scoring firm-year [INFERENCE; not verifiable from the PDFs]. **Consequence:** the sign contradiction between P2 and P3 (C1) cannot be blamed on different disclosure instruments.

---
---

# Batch 2 Audit (added; Batch 1 audit above unchanged)

## Summary grade: Batch 2

| Paper | Grade | Why |
|---|---|---|
| P6 (CSR&EM 2022) | **Moderate** | Implied COE, system GMM with diagnostics, formal mediation and moderation, larger sample. But the abstract contradicts the table on the moderation direction, mediation arithmetic is inconsistent, key coefficients are printed as 0.000, and no year effects are reported |
| P7 (IJFR 2017) | **Low–moderate** | Coherent theory and design for a cross-section; implied COE; robust SE and rank regression. Single year, no endogeneity treatment, self-generated forecasts |
| P8 (MAJ 2019) | **Low–moderate** | Large panel, careful index with reliability (Cronbach α). But the **dependent variable is never defined**, missing data are interpolated, it claims causality from pooled OLS, and it mislabels FE |
| P9 (LJE 2009) | **Low** | Conclusions contradict its own estimates; text contradictions; swapped descriptive rows; negative CAPM COE; "FE" = industry dummies |

**Updated implication (v2).**
- *Batch 1:* the only moderately supported finding was "disclosure ↔ lower COE/COD among large Vietnamese firms 2021–2023" (P2).
- **After Batch 2,** the direction of the **disclosure → COE** relation in Vietnam is supported by two moderate-grade papers using different proxies, P2 (CAPM, FE) and P6 (implied, GMM), plus the coherent P7 cross-section.
- It is still **associational**.
- **Governance → COE** has no moderate-grade support in any country in the corpus.

## P6: Thuy et al. (2022)
1. **Direction conflict on the moderation.** The abstract says state ownership "strengthens the negative impact" [PDF p.1 / p.1384], and H3 says the negative relation is "stronger when the state holds higher ownership" [PDF p.3–4 / p.1386–1387]. Table 5 shows CSRD −0.057*** with INTERACTION **+0.000*** (t=3.20)** [PDF p.9 / p.1392], i.e. attenuation. The conclusion says "attenuate" and "mixed moderating role" [PDF p.9 / p.1392]. *Signs verified on the rendered page.*
2. **Unscaled coefficients.** SOE −0.000*** and INTERACTION 0.000*** [Table 5], so economic magnitude cannot be evaluated.
3. **Mediation arithmetic** [Tables 3–4, PDF p.8 / p.1391]. The direct effect *grows* in magnitude when the mediator enters (−0.065 → −0.067). The path product (−0.204 × 0.142 ≈ −0.029) ≠ the Sobel indirect effect (−0.006). Table 4's "total 0.033 / direct 0.027" do not match Table 3.
4. **No year effects reported**, in a window (2014–2019) that straddles Circular 155, a law P6 calls "the most essential document for regulating CSR in Vietnam" [PDF p.2 / p.1385].
5. **Selection.** Industry leaders only (≥90% of industry assets) [PDF p.4 / p.1387]. Firms with negative earnings are excluded from the Easton estimation [Appendix A, PDF p.12 / p.1395].
6. [INFERENCE] 100–120 instruments for 225 groups; the Hansen p-values (0.10–0.60) should be read with instrument-proliferation caution.
7. **The text says "OLS regression, GMM and stability tests through surrogate variables"** [PDF p.9 / p.1392], but no OLS or surrogate-variable results are shown.

## P7: Nguyen & Nguyen (2017)
1. Single-year cross-section (FY2015) [PDF p.4 / p.67]; disclosure policy assumed stable without evidence.
2. [INFERENCE] Forecasts are generated as growth = ROE × plowback [PDF p.3 / p.66], which links implied COE to profitability and payout. If disclosure correlates with these, the disclosure coefficient may partly reflect the forecast model.
3. Only three controls (beta, P/B, size); no industry controls.
4. **Strength:** the clearest theory section in the corpus. It explicitly explains why CAPM cannot test disclosure effects [PDF p.3 / p.66]. Reports a rank-regression robustness check [Table 4, PDF p.6 / p.69].

## P8: Srivastava, Das & Pattanayak (2019)
1. **Dependent variable undefined.** No description of how COE is estimated anywhere in the paper; verified by full-text search for CAPM, beta, implied, Easton, Ohlson, risk premium and risk-free.
2. **Missing data interpolated or extrapolated;** index-replacement firms filled with prior constituents' data [PDF p.8], producing a "balanced" panel of 5,104 firm-years.
3. **Claims causality** ("The causal relationship tested using this method is the first one done in India" [PDF p.2]) from pooled OLS.
4. Text says "Using panel data and the fixed effects regression models justifies the consideration of unobserved factors" [PDF p.16], but the reported model is pooled OLS (Hausman → RE; BP-LM → pooled) [PDF p.15].
5. The ownership-structure sub-index (−0.130, p=0.049) is significant in Table III [PDF p.15] but omitted from the abstract and discussion.
6. "Robustness" regresses CGI on ROA and P/E, which does not test the COE result.
7. **Strength:** transparent index items with means and Cronbach's α [Table I, PDF p.12–13]; above-mandatory scoring [PDF p.9].

## P9: Shah & Butt (2009)
1. **Conclusion contradicts the estimates.** "We conclude that good corporate governance reduces a company's cost of equity" [PDF p.25 / p.163], while CGS is positive and insignificant (p=0.913, 0.855) [Tables 9–10] and only board size is marginal (p≈0.09) [Tables 5–6].
2. **Abstract overstates.** It reports directional relationships for MO, BI, ACI and CG [PDF p.1 / p.139] that are all insignificant in every table.
3. **Self-contradiction.** "Managerial ownership has a negative impact ... i.e., a higher number of shares ... held by board members leads to a higher cost of equity" [PDF p.23 / p.161].
4. **Table 2 rows swapped** (Maximum −0.93; Minimum 1.91) [PDF p.11 / p.149]. Ke ranges from −0.93 to 1.91 (negative CAPM COE). Log total assets has a minimum of 3.59, implausible next to a mean of 18.57.
5. **"Fixed effects" are industry dummies** [PDF p.14 / p.152], not firm effects.
6. **Strength:** an explicit, testable measurement-validity argument about director-independence labels [PDF p.23–24 / p.161–162]. Reports full regression output including year dummies, which reveal strong time variation in CAPM-COE [Table 6].

## Cross-paper observations (Batch 2)
- **Two Vietnamese disclosure papers now use implied COE** (P6, P7), and both find a negative disclosure effect. Together with P2's within-firm CAPM result, the *direction* is robust to the COE proxy. The *magnitude* is not comparable across papers.
- **Duplicate file:** `0f2c53f6-IMFI_2019_03_Le.pdf` = P5. It was audited once and not double-counted.
- **Citation network inside the corpus:**
  - P4 and P8 cite P9 (Shah & Butt 2009).
  - P3 cites P7 (Nguyen & Nguyen 2017 = P3's ref. [13]).
  - P3 cites a different, Vietnamese-language Cao Thị Miên Thùy et al. (2022) paper (ref. [3]), not P6.
  - The corpus is partly self-referential, so "consistent findings" are not fully independent evidence [INFERENCE].
