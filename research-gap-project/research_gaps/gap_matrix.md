# Phases 7–9: Gap Detection and the Research-Gap Matrix

## Phase 7: Systematic screen by gap type

| Gap type | Screen result | Candidate(s) |
|---|---|---|
| 1. Theoretical | Theories are listed but never discriminated. Signalling is invoked without separating discretionary from mandated disclosure. The competing cost/legitimacy view is cited in 4 papers and tested in 0 | **G6**, **G4**, G7 |
| 2. Empirical | COD and WACC: one study (P2) with a crude COD. Mediating channels: none | **G5**, **G3** |
| 3. Contradictory evidence | Disclosure–COE sign (P2 vs P3); SOE sign (P2 vs P5) | **G4**, **G9** |
| 4. Methodological | 5/5 static panels; 0 quasi-experiments, though mandated-disclosure shocks fall inside the windows | **G1** |
| 5. Measurement | CAPM-COE ≈ beta; implausible COE distributions; timing mismatch; binary quantity-only indices | **G2**, G7 |
| 6. Contextual | Vietnam only (by design). Within Vietnam: energy vs large caps, SOE vs private, never tested as moderators | G4, G9 |
| 7. Temporal | Nothing after 2023. Stress periods not modelled beyond one COVID dummy | G8 |
| 8. Mechanism | Information-asymmetry mechanism asserted in every conclusion, measured in none | **G3** |
| 9. Heterogeneity | No interactions in any paper | G4, G9, G3 |
| 10. Data | Pre/post-mandate disclosure panels hand-collectable; foreign-ownership and FOL data, trading data, FS notes on borrowings available but unused | G1, G3, G5 |

## Phase 8: Weak-gap filter (rejected or downgraded before the matrix)

| Candidate | Why rejected / downgraded |
|---|---|
| "No study of disclosure → COE in Vietnam industry X" (e.g., food, banking) | Purely geographic or sectoral; no theoretical reason the mechanism should differ. **Rejected** |
| "Board size / CEO duality → COE in Vietnam" (extend P4) | Long-studied internationally; P4's evidence is unreliable; a re-run adds no theory. **Rejected (G12)** |
| "Test a U-shaped disclosure–COE relation" (Ye & Zhang cited by P2 [PDF p.6 / p.1261]) | Atheoretical curve-fitting without a mechanism for the turning point. **Rejected (G11)** |
| "Decompose disclosure into E/S/Ec" (P1 call [PDF p.13 / p.71]) | Already done by P2 [Table 6]; replication. **Downgraded (G10)**, folded into G6/G4 |
| "Religion / gender diversity" (P2 future research [PDF p.17 / p.1272]) | No link to any unresolved issue in this corpus. **Rejected** |
| "Use a larger sample / longer period" (P2, P5) | "More research is needed" type. Folded into design standards (G2), not a gap |

## Phase 9: Research-gap matrix

Page references: `[PDF p.X / p.Y]`. Full claim log: `source_traceability/claims_register.md`.

| Gap ID | Research stream | Existing evidence | Missing knowledge | Evidence of gap | Why it matters | Possible solution | Key papers |
|---|---|---|---|---|---|---|---|
| **G1** Causal effect of mandated E&S disclosure | A, B | Disclosure *associated* with lower COE: P1 [Table 8, p.69], P2 [Table 3, p.1266], P5 [Table 7, p.94] | Whether **mandated** E&S disclosure **causes** a lower cost of capital, and for which firms | Windows straddle Circular 155: P1 chose 2014–2021 for that reason [PDF p.6 / p.64] but ran no pre/post test; P5 shows disclosers rising from 38 (2014) to 115 (2017) [PDF p.8 / p.93]. P2 and P3 straddle Circular 96/2020 [p.1257; p.141]. All five use static panels; P2 lists endogeneity as unresolved [PDF p.16 / p.1271] and cites a Chinese quasi-natural experiment (Zhao & Huang 2024) only in further reading [PDF p.23 / p.1278] | Whether mandating ESG reporting lowers financing costs is a live policy question, since Vietnam keeps tightening rules. Associational evidence cannot answer it, and within-firm estimates are fragile (C2) | Intensity DiD / event study: firms' pre-mandate distance to the Circular 155 item list = treatment intensity; outcomes before vs after; repeat for Circular 96 | P1, P5, P2, P3 |
| **G2** Construct validity of COE (CAPM ≈ beta) and timing | A, B, C | 4/5 papers use CAPM COE (P1 [p.64–65], P2 [p.1262], P3 [p.141], P4 [p.3086]); P5 uses forward E/P [p.91] | Whether the disclosure → COE result survives (a) non-CAPM COE, (b) correct timing, (c) firm + year FE; and whether it runs through **beta** or through **information risk** | Implausible COE: negative minima (P2 [Table 2, p.1265], P3 [Table 2, p.143], P4 [Table 2, p.3089], P5 [Table 4, p.92]); P4 mean 38%; P1 constant MRP [p.65]. Anomalous controls (leverage negative in P3 FE [Table 3, p.143]; ROA positive in P4 [Table 8]). Authors call for alternative COE: P2 [p.1271], P3 [p.145]. Forward EPS unavailable in Vietnam (P4 [p.3087]) | P1 and P2 invoke information-asymmetry and estimation-risk theory [p.63; p.1259], but CAPM COE only moves through beta, so the measure does not test the mechanism claimed | Triangulate CAPM, model-based implied COE (cross-sectional earnings forecasts, external method), realised-return factor tests; align disclosure release dates; decompose effects on beta vs idiosyncratic risk vs ICC | P1, P2, P3, P4, P5 |
| **G3** Mechanism: information asymmetry and investor base | A, B | All disclosure papers *assert* information-asymmetry reduction (P1 [p.70], P2 [p.1265, p.1268–1269]) | Whether disclosure lowers COE **through** lower information asymmetry or illiquidity, or through a changed **investor base** (foreign / institutional) | No paper measures spreads, illiquidity, analyst coverage or ownership change. The liquidity channel is theorised (P1 [p.63]; P3 [p.139]); FOR is a control only (P5 [Table 7, p.94]) | Without a mechanism, a negative coefficient is compatible with reverse causality and omitted visibility. Mechanism evidence is what top journals require | Mediation and channel tests: disclosure → Amihud / zero-return days / synchronicity / foreign ownership → COE; heterogeneity by foreign-ownership-limit headroom (external institutional detail) | P1, P2, P3, P5 |
| **G4** Context-dependence in environmentally sensitive industries | B (C1) | P2: negative in large caps; ESI dummy lowers WACC [Table 5, p.1268], no interaction. P3: positive in energy (OLS/RE) [Table 3, p.143]. P5 lit: positive findings in polluting or voluntary settings [Table 1, p.89] | Whether disclosure has **opposite or weaker** effects in environmentally sensitive industries, and whether **hard** (quantified) vs **soft** (narrative) environmental disclosure explains it | Contradiction C1 unresolved; P2 cites Li & Liu (2018): stronger effect in sensitive industries [PDF p.5 / p.1260]; P3 offers an untested risk-revelation story [PDF p.7 / p.144]; P5 cites Clarkson et al. (2008) discretionary-disclosure theory [refs, PDF p.10 / p.95] | Legitimacy theory and signalling make **opposite** predictions here, so this is a genuine theory test, not a geographic replication | Disclosure × ESI interaction in a broad panel; split items into hard vs soft (Clarkson et al. 2008 logic); firm + year FE | P2, P3, P5 |
| **G5** Cost of debt in a bank-dominated system | B | Only P2 tests COD: −0.029* [Table 4, p.1267]; E sub-index −0.013*** [Table 6] | Whether disclosure lowers the **actual price of bank and bond debt**, and whether state-owned banks price it | P2 concedes COD = interest/total liabilities is crude [PDF p.16 / p.1271]; P3 calls for COD work [PDF p.8 / p.145]; P2 discusses green credit obstacles [PDF p.3 / p.1258] | In a credit-dominated financing system, the creditor channel may matter more than the equity channel. The current proxy divides by non-interest-bearing liabilities (payables), which is noise | COD = interest expense / average interest-bearing borrowings (from FS notes); bond yield spreads where available; test E-disclosure × post-green-credit-policy (verify specific SBV instruments) | P2, P3 |
| **G6** Mandatory compliance vs voluntary (beyond-compliance) disclosure | A, B | Indices mix mandated and voluntary items: P1 all mandated (33 Circ.155 items [Table 1, p.65]); P3 notes 15 GRI items overlap Circ.155 [p.141]; P2 uses 77 GRI items, unsplit | Whether markets price **discretionary** disclosure differently from **mandated** disclosure, as signalling theory requires | P2 calls signalling the "most foundational" theory [PDF p.5 / p.1260] but never isolates discretionary signals; P5 lit: effect varies by voluntary vs compulsory disclosure [PDF p.4 / p.89] | This is a sharp theory test. Signalling predicts only costly, voluntary disclosure lowers COE; information-asymmetry theory predicts both do. The answer tells regulators whether mandating more items buys lower financing costs | Split each firm's index into mandated (Circ.155 / Circ.96 items) and voluntary (other GRI items); compare coefficients; combine with G1 timing | P1, P2, P3, P5 |
| **G7** Disclosure credibility (quality, assurance, governance) | A, B, C | All indices are binary presence counts (P1 [p.65], P2 [p.1263], P3 [p.141], P5 [p.91]); P4 governance → COE in a separate silo | Whether **credible** disclosure (quantified, assured, governance-backed) is priced, and whether disclosure without credibility is ignored or penalised | Greenwashing flagged (P2 [p.1271]); investor trust in quality lacking (P3 [p.144]); decoupling explanation (P5 lit [p.89]); assurance determinants cited (P2 [p.1257]). P3 controls for Big4 but never interacts it | Explains *why* the same disclosure volume can have opposite effects; connects governance (P4) and disclosure (P1–P3) | Quality scoring (quantitative vs narrative; targets; assurance); interactions with board independence or Big4; text-based specificity measures | P2, P3, P4, P5 |
| **G8** Time variation and market conditions | B | COVID dummy only (P2 [Table 1]); P3 COE swings 6.9% → 11.7% (2021–2023) [Table 2, p.143] | Whether the disclosure premium varies with market stress (COVID, 2022–23 credit stress: external context) | P3 lit: effects may weaken in crises [PDF p.3 / p.140]; nothing after 2023 | Tests whether disclosure acts as insurance (stronger in stress) or a luxury (weaker in stress) | Interact disclosure with stress-period indicators; extend the panel to 2024–2025 | P2, P3 |
| **G9** State ownership as a moderator | A, B (C3) | SOE: negative COE (P2 [Table 3]); positive COE (P5 [Table 7]) | Whether state ownership **amplifies or dampens** the disclosure effect | International evidence cited in the corpus conflicts: Li & Liu (2018) stronger in SOEs (P2 [p.1260]) vs Xu et al. (2014) weaker (P5 [p.91–92]); never interacted in Vietnam | Vietnam's equitisation makes state ownership a first-order institutional feature; competing theories (soft budget constraint vs visibility/legitimacy) | Disclosure × state-ownership % interaction; within-firm changes from divestments | P2, P5 |
| G10 E/S/Ec decomposition | B | Done by P2 [Table 6] | Little beyond replication | P1 call [p.71] | Low marginal value | Fold into G4/G6 as heterogeneity | P1, P2 |
| G11 Non-linearity | B | Cited only (P2 [p.1261]) | Mechanism for a turning point | None | Low | **Rejected** | P2 |
| G12 Governance structure → COE | C | P4 weak/inconsistent | Only a re-run | — | Low | **Rejected**; governance re-enters as a credibility moderator in G7 | P4 |

---
---

# Batch 2 Update to Phases 7–9 (Batch 1 matrix above unchanged)

## Phase 7 (v2): Re-screen by gap type after Batch 2

| Gap type | What Batch 2 changes | Candidates (v2) |
|---|---|---|
| 1. Theoretical | P6 states competing SOE predictions. P7 states the disclosure-economics trilogy. P9 introduces the substitution/complementarity logic between disclosure, governance and investor protection | G6, G4, **G7 (re-framed)** |
| 2. Empirical | No Batch 2 paper studies COD/WACC. Liquidity and investor-base channels still untested | G5, G3 (re-scoped) |
| 3. Contradictory evidence | Disclosure–COE sign now 5:1 (C1 narrower). SOE moderation tested but self-contradictory (C10). Governance index sign differs India vs Pakistan (C8) | G4, G9 (downgraded), G13 |
| 4. Methodological | GMM arrives (P6), but still **no DiD/IV/event study in 9 papers**. A third Vietnamese paper straddles Circular 155 unused (P6). India/Pakistan governance reforms also unused | **G1 (strengthened)**, **G14 (new)** |
| 5. Measurement | Implied COE appears in Vietnam (P6, P7). Beta does not explain implied COE (P7). Size sign aligns partly with the proxy (C6). Governance measurement validity questioned (P9). Above-mandatory scoring precedent (P8) | **G2 (strengthened)**, **G13 (new)** |
| 6. Contextual | India and Pakistan added, but designs are incompatible | G15 (new, low) |
| 7. Temporal | Older periods added; nothing after 2023 | G8 |
| 8. Mechanism | **First mechanism test (crash risk, P6)**, with inconsistent arithmetic (C11). Liquidity, adverse selection and investor base untested | G3 (re-scoped) |
| 9. Heterogeneity | First moderator test (SOE, P6) | G9 (downgraded), G4 |
| 10. Data | Refinitiv carries 1–2-year forecasts for Vietnamese firms (P6, C12). P6 shows CSR data for 225 firms from 2014, so pre-mandate panels are feasible | G1 feasibility ↑, G2 feasibility ↑ |

## Phase 8 (v2): Weak-gap filter, additional rejections

| Candidate | Why rejected / downgraded |
|---|---|
| "Replicate P8's governance index in Vietnam" | Index construction alone is not a gap. P8's DV is undefined, so even the benchmark is uninterpretable. **Rejected**; the measurement *validity* question survives as G13 |
| "Test crash risk as a mediator in another country" (P6 future research [p.1393]) | Geographic replication of a mechanism whose Vietnamese evidence is itself inconsistent. **Rejected** as a standalone gap; a credible *re-test* in Vietnam is folded into G3 |
| "State ownership moderates CSR → COE" as a novel test | **Downgraded (G9):** P6 already tests it. Remaining value is resolution, with economically scaled coefficients and better identification |
| "Cross-national CSR → COE study" (P6 future research) | Data-intensive, and P9/P1 already cite cross-country results (Chen et al. 2004; Breuer et al. 2018). **Low priority (G15)** |

## Phase 9 (v2): Impact of Batch 2 on existing gaps

| Gap | Batch 1 status | Batch 2 evidence | v2 status |
|---|---|---|---|
| **G1** Causal effect of mandated disclosure | Unused shock inside P1, P5, P2, P3 windows; feasibility risk (P5: 48 firms in 2014) | P6's 2014–2019 window also straddles Circular 155, which P6 calls the key CSR regulation [PDF p.2 / p.1385], yet no DiD. **P6 has CSR data for 225 firms from 2014** [PDF p.4 / p.1387]. P9 attributes its results to a post-reform "transition phase" [PDF p.1 / p.139] without testing it | **Strengthened.** Novelty unchanged (still 0 quasi-experiments in 9 papers); **data feasibility upgraded** |
| **G2** COE construct validity | Design standard; implied COE thought infeasible (P4) | P7: CAPM cannot test disclosure [PDF p.3 / p.66]; beta does not explain implied COE [Tables 2–3]. P6/P7 show implied COE is feasible; Refinitiv carries 1–2-year forecasts [PDF p.4 / p.1387]. Size sign aligns partly with the proxy (C6) | **Strengthened and feasible.** Still no within-sample CAPM-vs-implied comparison in any paper |
| **G3** Mechanism | Asserted, never measured | Crash-risk channel tested (P6), but the arithmetic is inconsistent (C11). P7's channels remain untested | **Re-scoped:** liquidity / adverse selection / investor-base channels, plus a credible horse race against crash risk. Novelty ↓ one notch |
| **G4** Sensitive industries | C1 unresolved | P3 now the sole positive estimate among 6 Vietnamese papers. P6 proposes SOEs in high-polluting industries as future research [PDF p.10 / p.1393]. Still no ESI interaction anywhere | **Unchanged, sharper target** |
| **G5** Cost of debt | One study (P2) | No Batch 2 paper studies COD | **Unchanged** |
| **G6** Mandated vs voluntary | Untested | P8 scores governance only *above* the mandatory minimum [PDF p.9], a design precedent. P6 notes Vietnam's legal framework "has not yet mandated full implementation of CSR activities" and urges supplementing required disclosures [PDF p.10 / p.1393]. Still no split of *disclosure* items | **Unchanged score; stronger precedent** |
| **G7** Credibility / governance interplay | Data-constrained (assurance rare) | P9 cites Chen et al. (2004): disclosure lowers COE only under strong investor protection, governance only under weak [PDF p.8 / p.146]. P8/P9 governance measures are feasible as moderators. **But Chen et al. already studied disclosure + governance jointly in emerging markets** | **Re-framed** to "governance as a credibility moderator of CSR disclosure in Vietnam". Feasibility ↑, novelty capped by the cited cross-country work |
| **G8** Time variation | One COVID dummy | P9 year dummies show large CAPM-COE time variation [Table 6] | Unchanged (supports the year-FE design standard) |
| **G9** SOE moderator | Untested; C3 | **Tested by P6** (attenuation per table; "strengthens" per abstract) | **Downgraded** to a resolution question |
| G10–G12 | Weak / rejected | — | Unchanged |

## Phase 9 (v2): New gap rows

| Gap ID | Research stream | Existing evidence | Missing knowledge | Evidence of gap | Why it matters | Possible solution | Key papers |
|---|---|---|---|---|---|---|---|
| **G13** Governance measurement validity: compliance labels vs substantive governance | C | Governance → COE weak or null with compliance-type measures: P4 (individual attributes, 10% only) [Table 8]; P9 (independence n.s., CGS n.s.) [Tables 6, 10]. Negative with above-mandatory index: P8 [Table III] | Whether governance lowers COE when measured as *substantive / beyond-compliance* practice rather than formal labels, in Vietnam | P9: independence labels are uninformative where law does not distinguish INEDs [PDF p.23 / p.161]; P8: scores only above-mandatory practice [PDF p.9]; P4: BOARDP mean 0.156, n.s. [Table 2]; C8, C9 | Explains why governance → COE findings are null in some markets. Same logic as G6 (compliance vs voluntary) applied to governance, so the two together form one theory of "beyond-compliance" signals | Build a Vietnamese beyond-compliance governance index (P8 logic) vs a compliance index (P4 logic); compare predictive power for implied COE; test independence substance (tenure, ties) vs label | P4, P8, P9 |
| **G14** Governance / disclosure mandates as quasi-experiments | C (and A/B) | Governance reforms named but unused: India Clause 49 / Companies Act 2013 (P8 [PDF p.4–6]); Pakistan Code 2002 (P9 [PDF p.1–2 / p.139–140]). Disclosure mandates unused (G1) | Causal effect of governance-code reforms on COE in the region, and in Vietnam if comparable reforms exist (external, verify) | P9 attributes its null to the reform "transition phase" [PDF p.1 / p.139] but never tests pre/post. P8 lists a reform timeline [PDF p.4–6] and uses pooled OLS | Converts the governance stream's weakest feature (identification) into a design | Event-study / DiD around reform dates, with compliance-gap intensity; for Vietnam, best folded into Idea 1 as a governance extension | P8, P9 (+ G1 papers) |
| **G15** Cross-country institutional moderation | A, C | Single-country designs only; investor-protection conditionality cited (P1 Breuer/Feng [p.62]; P9 Klapper & Love, Chen et al. [p.144, 146]) | Whether disclosure and governance effects on COE depend on country investor protection | Corpus spans 3 countries with non-comparable designs; P6 calls for cross-national samples [PDF p.10 / p.1393] | Theory-relevant but already studied in cited cross-country work | Harmonised multi-country panel | P1, P6, P8, P9 |
