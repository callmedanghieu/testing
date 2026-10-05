# Final Research-Gap Analysis

**Scope:** the complete literature set: 9 unique papers from 10 files, uploaded in two batches.

**Stance:** skeptical journal reviewer. A gap survives only if it is (i) unresolved across the *whole* corpus, (ii) theoretically consequential, (iii) testable with obtainable data, and (iv) not redundant with another surviving gap.

**Reproducibility:**
- Counts come from `corpus_coding.csv` via `tally.py` (output in `corpus_tallies.md`).
- Scores are in `final_gap_ranking.csv`.
- Page claims are verified in `../source_traceability/claims_register.md` (147 claims, 0 failures).
- Page format: `[PDF p.X / p.Y]`, or a bare printed page `[p.Y]`. P8 has PDF pages only.

---

## 0. Bottom line

We reviewed nine papers on how disclosure and governance relate to the cost of capital: seven from Vietnam, one from India, one from Pakistan. The literature agrees on one **direction**: more disclosure goes with a lower cost of equity in Vietnam. Five of six Vietnamese disclosure papers report it, including both papers that use implied cost of equity.

The literature cannot say:

- **whether** that relationship is causal;
- **what** about disclosure is priced;
- **through which channel** it works;
- **whether** the dominant cost-of-equity measure (CAPM) can capture it at all.

The corpus's defining weakness is plain in the numbers. **None of the nine papers uses a quasi-experiment, while six of them have a disclosure or governance reform inside their own sample window and leave it unused.**

After re-evaluating 15 candidate gaps against all nine papers:

- **5 survive.**
- **4 are merged** into stronger gaps.
- **6 are rejected.**

The strongest opportunity is to use Vietnam's disclosure mandates (Circular 155/2015; Circular 96/2020) to identify the causal effect of mandated environmental and social disclosure on the cost of capital. Designed with a compliance-gap intensity measure, the same study can test whether markets price beyond-compliance disclosure rather than compliance (the second-ranked gap).

---

## 1. The evidence base

| Stream | Papers | Construct → outcome | Evidence grade |
|---|---|---|---|
| A. Circular-155-era CSR / environmental disclosure | P1 (2024), P5 (2019), P6 (2022) | CSR disclosure → COE | P6 moderate; P5 low–moderate; P1 low |
| B. GRI/SDG sustainability disclosure | P2 (2026), P3 (2025) | Sustainability disclosure → COE / COD / WACC | P2 moderate; P3 low |
| C. Governance (cross-country) | P4 Vietnam (2023), P8 India (2019), P9 Pakistan (2009) | Governance → COE | P8 low–moderate; P4, P9 low |
| D. General disclosure | P7 (2017) | Annual-report disclosure → implied COE | low–moderate |

### Design features across the corpus (from `corpus_tallies.md`)

| Feature | Count | Papers |
|---|---|---|
| Quasi-experiment (DiD / event / RD) | **0/9** | — |
| External instrument | **0/9** | — |
| Regulatory shock inside window, unused | **6/9** | P1, P2, P3, P5, P6, P8 |
| CAPM-based COE | 5/9 | P1, P2, P3, P4, P9 |
| Implied / ex-ante COE | 3/9 | P5, P6, P7 |
| Negative COE values in sample | **5/8** | P2, P3, P4, P5, P9 |
| Full year effects | 2/9 | P4, P9 |
| Firm-FE estimate reported | 4/9 | P2, P3, P4, P5 |
| Mechanism formally tested | 1/9 | P6 |
| Moderator formally tested | 1/9 | P6 |
| CSR papers using a binary item-count index | **5/5** | P1, P2, P3, P5, P6 |
| CSR papers measuring disclosure quality | **0/5** | — |
| CSR papers controlling for general disclosure | **0/5** | — |
| Cost of debt studied | 1/9 | P2 |
| Headline claim not supported by own preferred estimate | **5/9** | P3, P4, P5, P6, P9 |

The last row matters for a reviewer. In five of nine papers, the abstract or conclusion says more than the preferred estimate supports. The details are in `../limitations/evidence_quality_audit.md`:

- P3: the FE estimate is insignificant (p=0.452) [Table 3, p.143].
- P4: CEO duality is coded one way and interpreted the other [p.3086 vs p.3093].
- P5: the result is significant only with Driscoll-Kraay SEs at T=4 [Table 7, p.94].
- P6: the moderation direction differs between abstract and table [p.1384 vs Table 5, p.1392].
- P9: the governance score is insignificant, yet the conclusion claims an effect [Tables 9–10 vs p.163].

**Consequence.** Existing "findings" are treated below as *claims to be tested*, not as settled premises.

---

## 2. What is established, and how firmly

| # | Finding | Support | Confidence |
|---|---|---|---|
| E1 | In Vietnam, more disclosure goes with a **lower** cost of equity | 5 of 6 Vietnamese disclosure papers: P2 FE −0.138* [Table 3, p.1266]; P6 GMM −0.065*** with implied COE [Table 2, p.1390]; P7 −0.0016*** with implied COE [Table 3, p.68]; P1 [Table 8, p.69]; P5 [Table 7, p.94]. Exception: P3 [Table 3, p.143] | **Moderate for direction; low for magnitude and causality.** Holds across CAPM and implied proxies |
| E2 | Environmental disclosure carries more of the effect than social or economic disclosure | P2 only [Table 6, p.1270] | Low (single study) |
| E3 | Disclosure goes with a lower **cost of debt** | P2 only [Table 4, p.1267], crude proxy [p.1271] | Low |
| E4 | CAPM-based and implied cost of equity **diverge** in these markets | P7: beta does not explain implied COE (p=0.672; r=−0.027) [Tables 2–3, p.68]; P7's theoretical argument [p.66]; size changes sign with the proxy (C6) | Moderate as a *warning*; not yet tested on a common sample |
| E5 | Governance lowers the cost of equity | India negative but COE undefined (P8 [Table III]); Pakistan null (P9 [Tables 6, 9, 10]); Vietnam weak (P4 [Table 8]) | **Not established in any country** |
| E6 | Disclosure levels in Vietnam are low and rising | P3 Table 1 [p.142]; P5 [p.93]; P7 27/105 [Table 1, p.67]; P2 Appendix [p.1279] | High (descriptive) |

---

## 3. Contradictions: final status

| ID | Contradiction | Papers | Final status | Disposition |
|---|---|---|---|---|
| C1 | Sign of disclosure → COE | P2, P1, P5, P6, P7 (−) vs P3 (+) | **Largely resolved in direction.** P3 is an isolated, within-firm-insignificant outlier. Its cause (no year effects, CAPM beta, or industry context) is unexplained | Heterogeneity test inside F3; not a standalone gap |
| C2 | Within-firm robustness | P1 (FE unreported), P3 (n.s.), P5 (n.s. without DK-SE), P2 WACC (n.s.) | **Unresolved** | Core motivation for F1 |
| C3 / C10 | State ownership: main effect and moderation | P2 (−), P6 (−) vs P5 (+); P6 moderation abstract vs table | **Unresolved but narrow**: direction of moderation contested inside one paper | Pre-registered moderator in F1 / F3 |
| C4 | Board size | P4 (−, 10%), P9 (−, 10%), P3 (+ OLS) | Weakly negative, low stakes | Rejected |
| C5 | CEO duality | P4 internal coding | Reporting error | Rejected |
| C6 | Control-variable signs by COE proxy | Size + with implied (P6, P7), − with CAPM (P1, P4, P9) | **Unresolved; measurement-driven** | Design standard |
| C7 | E / S / Ec dimensions | P2 vs Shad et al. (cited in P2 [p.1257]) | Single study | Rejected (G10) |
| C8 | Composite governance index | P8 India (−) vs P9 Pakistan (n.s.) | Mostly measurement-driven (index logic; DV undefined vs CAPM) | Governance arm of F2 |
| C9 | Board independence | P8 (−) vs P9 (n.s.) vs P4 (n.s.) | Label-vs-substance explanation (P9 [p.161]) | Governance arm of F2 |
| C11 | Crash-risk mediation arithmetic | P6 internal [Tables 3–4, p.1391] | Reporting inconsistency | Motivates F4 |
| C12 | Availability of analyst forecasts in Vietnam | P7 (2017), P4 (2023) vs P6 (2022) | **Resolved**: temporal and source-specific; implied COE is feasible | Supports the design standard |

---

## 4. Unresolved questions, by gap type

| Type | Unresolved question | Evidence that it is unresolved | Goes to |
|---|---|---|---|
| **Theoretical** | Is the disclosure discount a *signalling* effect, which needs discretionary disclosure, or an *information-asymmetry* effect, which works with any disclosure? | P2 declares signalling foundational [p.1260] but pools mandated and voluntary items; P1 measures only mandated items [Table 1, p.65]; 15 GRI items overlap Circular 155 (P3 [p.141]) | **F2** |
| Theoretical | Do legitimacy and signalling give opposite predictions for polluters' narrative disclosure? | P3's ex-post risk-revelation story [p.144]; decoupling explanations in P5's review [p.89]; never derived or tested | F3 |
| Theoretical | Are disclosure and governance substitutes or complements? | Conditional logic from Chen et al. (2004) cited in P9 [p.146]; never tested within Vietnam | F2 (H2c) |
| Theoretical | Does state ownership amplify (multitask) or dampen (inefficiency / soft budget) the disclosure effect? | P6 states both [p.1386] and reports contradictory directions | Moderator |
| **Methodological** | Is any disclosure–COE effect causal? | 0/9 quasi-experiments; 0/9 external instruments; 6/9 unused in-window reforms | **F1** |
| Methodological | Are results robust to firm + year effects and correct timing? | 2/9 with full year effects; disclosure dated contemporaneously with COE in most papers (only P5 aligns to report release [p.91]) | Design standard |
| **Measurement** | Can CAPM-COE test a disclosure effect at all? | 5/9 papers use CAPM; 5/8 report negative COE; P7: CAPM excludes information risk [p.66], and beta does not explain implied COE | Design standard |
| Measurement | Is the *quantity* or the *verifiability* of disclosure priced? Is CSR disclosure incremental to general transparency? | 5/5 binary counts; 0/5 quality; 0/5 control for general disclosure, though P7 shows general disclosure lowers implied COE | **F3** |
| Measurement | Do governance labels measure governance? | P9: independence labels are uninformative [p.161]; P8: above-mandatory scoring [PDF p.9] | F2 |
| **Contextual** | Does the effect differ in environmentally sensitive industries? | P3's energy outlier; P2's ESI dummy never interacted [Table 5]; P6 suggests polluting SOEs as future work [p.1393] | F3 |
| **Mechanism** | Which channel carries the effect: liquidity / adverse selection, investor base, or crash risk? | 1/9 tests a channel (P6, crash risk) with inconsistent arithmetic (C11); P7's channels [pp.64–65] are untested | **F4** |
| **Empirical** | Do lenders price disclosure? | 1/9 studies COD (P2) with a proxy the authors call flawed [p.1271] | **F5** |
| Temporal | Does the relation hold after 2023? | No sample extends past 2023 | Design note (extend the panel) |

---

## 5. Re-evaluation of all 15 candidate gaps

| Candidate | Prior rank (v2) | Final verdict | Reviewer rationale |
|---|---|---|---|
| G1 Mandated disclosure as quasi-experiment | 1 | **KEEP → F1** (absorbs G14) | The corpus's central weakness (C2; 0/9 quasi-experiments) with an obvious, in-window source of variation. P6's 225-firm panel from 2014 [p.1387] answers the main feasibility objection |
| G6 Mandated vs voluntary disclosure | 2 | **KEEP → F2** (absorbs G13, G7) | The only gap that *discriminates between theories the corpus already invokes*. P8's above-mandatory scoring [PDF p.9] gives a measurement template |
| G3 Mechanism | 3 | **KEEP → F4**, re-scoped | P6 makes a crash-risk-only paper near-replication. A channel horse race still has value. Mediation without exogenous variation is weak, so ranked below F3 |
| G4 Sensitive industries / hard vs soft | 4 | **KEEP → F3**, re-framed | The C1 contradiction alone is a weak motivation (P3 is low-grade). The durable gap is universal: **no CSR paper measures what kind of disclosure is priced**, and none nets out general transparency (P7) |
| G7 Governance as credibility moderator | 5 | **MERGE into F2** | Standalone novelty capped by Chen et al. (2004), cited in P9 [p.146] |
| G5 Cost of debt | 6 | **KEEP → F5**, conditional | Real empirical gap (1/9), but incremental to P2 unless lender-side variation can be measured |
| G14 Reforms as quasi-experiments | 7 | **MERGE into F1** | India novelty low (Black & Khanna 2007, cited in P8 [PDF p.16]); Vietnamese governance-reform dates unverified |
| G2 COE construct validity | 8 | **MERGE into design standard** | The most pervasive weakness, but redundant as a paper: every surviving gap must report CAPM *and* implied COE |
| G13 Governance labels vs substance | 9 | **MERGE into F2** | It is the governance half of the beyond-compliance theory |
| G8 Time variation | 10 | **REJECT** (standalone) | No mechanism for time variation beyond generic stress. Year effects become mandatory instead |
| G9 SOE moderator | 11 | **REJECT** (standalone) | Already tested (P6, Table 5); only the direction remains. Kept as a moderator |
| G15 Cross-country moderation | 12 | **REJECT** | Infeasible with comparable measures; cross-country work already cited (P1 [p.62]; P9 [p.146]) |
| G10 E/S/Ec decomposition | 13 | **REJECT** | Replication of P2 Table 6 |
| G11 Non-linearity | — | **REJECT** | Atheoretical |
| G12 Board structure re-run | — | **REJECT** | Adds nothing that P4 and P9 lack |

**Weak framings rejected outright** (they would not survive desk review):
- "First study of X in industry Y / country Z".
- "Test crash-risk mediation in another country" (P6 future research).
- "Replicate P8's governance index in Vietnam".
- "Religion / gender diversity" (P2 future research [p.1272]).
- "Use a larger sample or longer period".

---

## 6. Final ranking

| Rank | ID | Research gap | Types | Nov | Imp | Th | Emp | Data | Feas | Id | Pub | **/40** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **F1** | Causal effect of mandated E&S disclosure (Circular 155 / 96) | methodological, empirical, data | 4 | 5 | 3 | 5 | 4 | 4 | 4 | 5 | **34** |
| 2 | **F2** | Beyond-compliance signalling: voluntary disclosure and substantive governance vs compliance | theoretical, measurement | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 4 | **32** |
| 3 | **F3** | What is priced: verifiable vs narrative disclosure, net of general transparency; sensitive-industry heterogeneity | measurement, contextual, contradiction | 3 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | **29** |
| 4 | **F4** | Channel horse race: liquidity / adverse selection vs investor base vs crash risk | mechanism | 3 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | **29** |
| 5 | **F5** | Creditor channel with a valid cost-of-debt measure | empirical, measurement | 4 | 4 | 3 | 4 | 3 | 4 | 2 | 3 | **27** |

**Tie-break F3 over F4:**
- F3's gap is universal (5/5 papers) and resolves C1.
- F4's novelty is reduced by P6.
- F4's identification is weaker unless it is embedded in F1.

---

## 7. Top research questions

### RQ1 (F1): Do disclosure mandates lower financing costs in a weak-enforcement market?

- **Research gap.** All nine papers rely on static or dynamic panels. Within-firm estimates are fragile or missing (C2). Circular 155 falls inside the windows of P1 (chosen "before and after" Circular 155 [p.64]), P5 (38 → 115 disclosing firms, 2014–2017 [p.93]) and P6 (which calls it "the most essential document for regulating CSR in Vietnam" [p.1385]). Circular 96 falls inside the windows of P2 and P3 [p.1257; p.139]. None uses it.
- **Research question.** Did mandated environmental and social disclosure lower the cost of equity (and debt) of Vietnamese listed firms, and was the decline larger for firms the mandate forced to disclose more?
- **Theory.** Mandatory-disclosure economics: commitment reduces estimation risk and adverse selection. P7 sets out the channels [pp.64–65]. The competing view is boilerplate compliance (P3's compliance-cost argument [p.144]).
- **Mechanism.** Firms with large pre-mandate gaps release new information, so investors' estimation risk falls and required returns fall.
- **Hypotheses.**
  - H1: ΔCOE(post) is more negative the larger the pre-mandate compliance gap.
  - H1-alt (boilerplate): no differential effect.
  - H1b: the effect is smaller where pre-mandate voluntary disclosure was already high (links to RQ2).
- **Variables.**
  - Treatment: GAP_i × POST_t. GAP_i = 1 − pre-mandate share of items later required. Score with P1's 33-item Circular-155 list [Table 1, p.65] and P8-style above/below-mandate coding [PDF p.9].
  - Outcomes: implied COE (P6 Easton + Harris–Wang [p.1387]; P7 residual income [p.66]) **and** CAPM COE; COD* (RQ5); Amihud illiquidity.
  - Moderators: state share (P6 SOE %), environmentally sensitive industry (P2 IND).
  - Controls: size, leverage, book-to-market, ROA, general disclosure (P7); firm FE; industry × year FE.
- **Data.** Annual reports 2013–2019 (Circular 155) and/or 2018–2023 (Circular 96). P6 shows CSR data for 225 firms from 2014 [p.1387]. Market data from Refinitiv / FiinPro / Vietstock, all used in the corpus.
- **Design.** Continuous-treatment DiD and dynamic event study, with P6's GMM estimate as the benchmark the causal estimate is compared against.
- **Identification threats and responses.**
  1. All listed firms are treated at once (external, verify). Rely on intensity and show flat event-study leads.
  2. GAP correlates with size and opacity. Add size-decile × year FE and pre-period matching.
  3. Concurrent shocks. Add industry × year FE, plus a placebo on GRI items the circular does not cover.
  4. Anticipation (issuance before the effective date: external, verify). Test the lead year.
  5. Mean reversion. Control for pre-period COE trends.
- **Contribution.** First causal estimate in the corpus. Tells regulators whether checklist mandates lower capital costs when enforcement is weak. Replaces the between-firm correlations that drive E1.
- **What would kill it.**
  - A prior Vietnamese DiD on Circular 155 (search required).
  - Insufficient pre-2016 report coverage. Fallback: Circular 96.
- **Minimum viable version.** Circular 96, 2018–2023, reusing the 77-item GRI frame from P2 / P3.

### RQ2 (F2): Do markets price beyond-compliance rather than compliance?

- **Research gap.** The corpus invokes signalling (P2 [p.1260]) but cannot test it, because every disclosure index pools mandated and voluntary items. P8 shows how to score governance only *above* the legal minimum [PDF p.9]. P9 shows compliance labels carry no information [p.161]. P6 notes CSR is "not yet mandated" in full and urges firms to go beyond required disclosures [p.1393].
- **Research question.** Do equity investors price voluntary, beyond-mandate sustainability disclosure and substantive governance, while ignoring disclosure and governance that merely comply?
- **Theory.** Signalling (costly, discretionary signals separate firm types) vs information-asymmetry reduction (any credible information lowers risk). Agency theory for the governance arm.
- **Hypotheses.**
  - H2a: β_voluntary < β_mandated ≤ 0. Equality supports pure information asymmetry.
  - H2b: a beyond-compliance governance index predicts lower COE; a compliance-label index does not.
  - H2c (complementarity): the voluntary-disclosure discount is larger where beyond-compliance governance is stronger. The substitution alternative predicts the opposite.
  - H2d (switch test): an item's price effect falls after it becomes mandatory (needs RQ1 timing).
- **Variables.**
  - VOL and MAND shares from mapping the 77 GRI items onto the Circular 155 / 96 appendices (P3 notes 15 overlapping items [p.141]; verify against the legal text).
  - Governance: compliance index (P4 variables) vs beyond-compliance index (P8 logic adapted to Vietnamese rules; external, verify).
  - Outcomes: implied + CAPM COE.
  - Controls: general disclosure (P7), firm + year FE.
- **Design.** FE panel with coefficient-equality tests; item-level switch test around Circular 96 (or 155).
- **Identification.** Firm FE absorbs stable disclosure propensity. The switch test uses regulatory reclassification, plausibly exogenous to a single firm's COE. Residual concern: time-varying firm quality → lagged regressors, pre-trend checks.
- **Contribution.** Turns E1 into a theory test. Gives a single theory ("beyond-compliance signals") covering both disclosure and governance. Explains the null governance results (C8, C9).
- **What would kill it.** Too few items switch status, so the switch test has low power. In that case, report H2a–H2c and present H2d as exploratory.

### RQ3 (F3): What exactly about sustainability disclosure is priced?

- **Research gap.** Every CSR paper measures disclosure as a binary item count (5/5). None measures verifiability (0/5), and none controls for general financial transparency (0/5), even though P7 shows general disclosure lowers implied COE [Table 3, p.68]. The only sign contradiction (C1: P3 positive in energy [Table 3, p.143]) is unexplained. P5's review offers decoupling and lack-of-trust explanations [p.89]. P2 raises greenwashing [p.1271]. P3 says investors do not trust disclosure quality [p.144].
- **Research question.** Is the cost-of-equity discount driven by verifiable (quantified) sustainability information incremental to general transparency, and does narrative disclosure by environmentally sensitive firms carry no discount, or a premium?
- **Theory.** Discretionary-disclosure theory (Clarkson et al. 2008, cited in P5's references [p.95]): verifiable disclosure is credible. Legitimacy theory: reactive narrative disclosure by exposed firms is discounted, or reveals liabilities.
- **Hypotheses.**
  - H3a: HARD disclosure lowers COE after controlling for general disclosure.
  - H3b: SOFT disclosure has no effect once general disclosure is controlled.
  - H3c: in environmentally sensitive industries, SOFT disclosure has a null or positive effect (legitimacy).
  - H3d (exploratory): H3c is stronger for SOEs (multitask theory, P6 [p.1386]).
- **Variables.**
  - HARD and SOFT environmental / social scores, from re-coding GRI 300/400 items as quantified vs narrative.
  - General-disclosure score (P7 / Botosan-type).
  - ESI dummy (P2 [Table 1]).
  - Outcomes: implied + CAPM COE.
  - Firm + year FE.
- **Design.** FE panel with interactions. Two replication arms: P3's energy sample and P2's large-cap sample, to show whether C1 disappears under implied COE + year FE + hard/soft separation.
- **Identification.** Associational. Strengthened by using RQ1's mandate (mandated items are mostly soft) as a shifter of soft disclosure.
- **Contribution.** Establishes *what* is priced. Corrects an omitted-variable problem shared by all five CSR papers. Resolves C1.
- **What would kill it.** Too few hard disclosures. The P2 appendix shows low coverage of quantitative environmental topics [p.1279]. Report coverage first, and require inter-coder reliability.

### RQ4 (F4): Through which channel does disclosure lower the cost of equity?

- **Research gap.** Every disclosure paper asserts an information-asymmetry mechanism (e.g., P1 [p.70], P2 [p.1269]). One tests a channel: crash risk (P6 [Tables 3–4, p.1391]), with inconsistent path arithmetic (C11). The channels P7 sets out (adverse selection, estimation risk, public/private information [pp.64–65]) and the investor-base channel (Dhaliwal et al. 2011, cited in P1 [p.62]) are untested.
- **Research question.** Does disclosure lower COE mainly through stock liquidity / adverse selection, through a shift in the investor base, or through lower crash risk?
- **Hypotheses.**
  - H4a: disclosure lowers Amihud illiquidity and zero-return days, which carry part of the effect.
  - H4b: disclosure raises foreign / institutional ownership, with larger effects where foreign-ownership headroom exists (external institutional detail, verify).
  - H4c: crash risk mediates after the other channels are controlled (re-test of P6).
- **Design.** Simultaneous multi-mediator model with bootstrap CIs; mediators measured *after* report release. Preferably estimated as event-study outcomes inside RQ1, so the channel moves only when disclosure is exogenously shifted.
- **Identification.** Weak as stand-alone mediation. Credible only (a) inside RQ1, or (b) through cross-sectional predictions, such as headroom, that omitted firm quality would not produce.
- **Contribution.** Turns E1 from an association into an explanation. Ranks P6's crash-risk channel against the alternatives.
- **What would kill it.**
  - Thin spread and analyst data in Vietnam, forcing low-frequency proxies.
  - Failure to engage P6.

### RQ5 (F5): Do lenders price sustainability disclosure?

- **Research gap.** One paper studies the cost of debt (P2) using interest expense / total liabilities, which its authors concede is flawed [p.1271]. P3 calls for cost-of-debt work [p.145]. P2 discusses green-credit obstacles [p.1258].
- **Research question.** Does sustainability (especially environmental) disclosure in year t lower the interest rate on interest-bearing debt in year t+1, and is the effect weaker for state-owned firms?
- **Hypotheses.**
  - H5a: disclosure_t lowers COD*_{t+1}.
  - H5b: the effect is weaker for majority state-owned firms (implicit guarantees).
- **Variables.** COD* = interest expense / average interest-bearing borrowings (from FS notes); E and S disclosure; leverage, coverage, tangibility, size, ROA, maturity mix; firm + year FE.
- **Design.** Lead–lag FE panel. RQ1's mandate as a shifter. The P2 proxy reported side by side to show how measurement changes the result.
- **Identification.** Weak without lender-side data.
- **Contribution.** Corrects the only Vietnamese cost-of-debt estimate in the corpus.
- **Why conditional.** Without lender identity (state vs private banks), a reviewer may see this as an improved replication of P2. Upgrade it only if loan- or bond-level data can be obtained.

---

## 8. Mandatory design standard (replaces G2 and G8 as standalone gaps)

Every study above must:

1. Report **CAPM and at least one implied COE**, and explain any divergence. Justification: P7 [p.66; Tables 2–3], C6, and 5/8 papers with negative COE.
2. Date disclosure by **report release**, with outcomes measured after release. P5 is the precedent [p.91].
3. Include **firm and year fixed effects**. Only 2/9 papers have year effects; P9's year dummies show large CAPM-COE swings [Table 6, p.155].
4. **Control for general disclosure** when estimating CSR effects (P7 construct; 0/5 CSR papers do this).
5. Report **economically scaled** interaction coefficients (P6 prints 0.000 [Table 5]).
6. Avoid **ex-post sample selection** (P1 VNR500-2021 [p.64]; P2 top-100 at end-2023 [p.1261]).
7. Avoid Driscoll-Kraay SEs with very short T (P5, T=4) and claims of causality from pooled OLS (P8).

---

## 9. Adversarial check on the final five

| Test | F1 | F2 | F3 | F4 | F5 |
|---|---|---|---|---|---|
| Already answered in the corpus? | No (0/9) | No | No | Partly (P6, crash risk only) | Partly (P2, crude) |
| Merely a replication? | No | No | Partly (C1 arm), but the core is new | Risk, unless it is a horse race | **Risk** |
| Merely geographic? | Partly. Mitigated by the weak-enforcement checklist mandate | No (theory test) | No | No | Partly |
| Data realistic? | Yes (P6 panel from 2014; Circular 96 fallback) | Yes (GRI frame exists) | Yes, if hard items are not too rare | Mostly (low-frequency liquidity proxies) | Mostly (FS notes) |
| Causal identification? | **Moderate–good** (intensity DiD) | Moderate (switch test) | Weak alone; good inside F1 | Weak alone; good inside F1 | Weak |
| Result obvious? | No (boilerplate null plausible) | No | No | No | No |
| Stronger question behind it? | "Mandates and beyond-compliance signals" (F1 + F2) | Same | "Is the CSR discount just transparency?" | Folded into F1 | Lender identity |
| **Survives?** | **Yes** | **Yes** | **Yes** | **Yes, best embedded in F1** | **Conditionally** |

---

## 10. Recommended programme

1. **Paper 1 (flagship): F1 + F2 together.** "Do disclosure mandates lower the cost of capital, and do markets reward compliance or beyond-compliance?"
   - The compliance-gap measure (F1's treatment) and the mandated/voluntary split (F2) come from the **same hand-coded item matrix**, so one data build serves both.
   - F4's channels can be reported as event-study outcomes.
2. **Paper 2: F3.** "Verifiable vs narrative sustainability disclosure, net of general transparency." It reuses Paper 1's item coding, plus a hard/soft re-coding and a general-disclosure score.
3. **Paper 3 (optional): F5.** Only if lender-side or bond-level data are obtainable.

**Shared first step:** build a firm–year–item disclosure matrix (GRI items × Circular 155 / 96 mapping × hard/soft flag) for 2013–2023, alongside CAPM and implied COE. Every surviving gap depends on it.

---

## 11. Caveats

- **Novelty is judged against these nine papers only.** Before committing, search the international mandatory-CSR-reporting literature and any Vietnamese studies of Circular 155 / 96 using DiD or event-study designs. This cannot be done from the PDFs.
- **External facts need verification before use:** effective dates and item lists of Circular 155/2015 and Circular 96/2020; Vietnamese governance regulations; foreign-ownership limits; green-credit instruments; and the suitability of the Harris–Wang / residual-income forecast models.
- **Inferences** (marked [INFERENCE] in the underlying files) are reviewer judgements, not author statements.
