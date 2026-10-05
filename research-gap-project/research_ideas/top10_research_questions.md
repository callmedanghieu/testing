# Phase 11: Top-10 Gaps as Research Questions

Order follows `research_gaps/ranked_gaps.md` (Phase 10 scores, before the adversarial re-ordering).

**Common design standard (from G2), applies to every RQ below:**
- (i) firm + year fixed effects at minimum;
- (ii) disclosure dated by report release, with outcomes measured *after* release;
- (iii) at least two COE proxies: CAPM plus a non-CAPM measure (model-based implied COE, or a forward earnings yield as in P5 [PDF p.6 / p.91]);
- (iv) SEs clustered by firm, and no Driscoll-Kraay SEs with T<10;
- (v) no ex-post sample selection (avoid the VNR500-2021 / top-100-2023 designs of P1 [p.64] and P2 [p.1261]).

Items marked **(external, verify)** are institutional or method facts not contained in the five PDFs.

---

## 1. G1: Causal effect of mandated E&S disclosure

- **Gap.** All evidence is associational (5/5 static panels). Two mandates fall inside sample windows: Circular 155 (P1 [p.64], P5 [p.88, 93]) and Circular 96/2020 (P2 [p.1257], P3 [p.139]). Neither is used for identification.
- **RQ.** Did mandated environmental and social disclosure under Circular 155/2015 (and its replacement, Circular 96/2020) lower the cost of capital of Vietnamese listed firms, and was the effect larger for firms the mandate forced to disclose more?
- **Theory.** Mandatory disclosure theory: commitment to disclosure reduces information risk. Against it, the proprietary-cost and boilerplate view (P3's compliance-cost argument [p.144]).
- **Mechanism.** Firms with large pre-mandate disclosure gaps become more transparent, which lowers investors' estimation risk and information asymmetry and so lowers required returns.
- **H1.** After the mandate, cost of equity falls more for firms with a larger pre-mandate gap to the mandated item list.
- **H1b (competing).** If disclosure is boilerplate, there is no differential effect.
- **Variables.**
  - IV: GAP_i = 1 − (pre-mandate share of mandated items disclosed), interacted with POST_t.
  - DV: COE (CAPM, implied); COD (G5 measure).
  - Moderators: SOE share (G9), ESI industry (G4).
  - Mediators: illiquidity, foreign ownership (G3).
  - Controls: size, leverage, BTM, ROA, beta (when DV ≠ CAPM).
- **Measurement.** Code the Circular 155 appendix items (P1's 33-item list [Table 1, p.65] is a ready template) for the pre-period 2013–2015 and the post-period 2016–2019. For Circular 96, code its item list over 2018–2020 vs 2021–2023.
- **Data.** Annual reports from company websites and HOSE/HNX portals; prices from FiinPro-X or Vietstock.
- **Methodology.** Continuous-treatment DiD and event study (year-by-GAP coefficients); firm FE and industry×year FE.
- **Identification threats.**
  - (a) No untreated group: rely on intensity, and show flat pre-trends.
  - (b) Concurrent 2016 shocks: industry×year FE; placebo on non-mandated GRI items.
  - (c) GAP correlated with size or opacity trends: size-decile×year FE; matching on pre-period characteristics.
  - (d) Anticipation: Circular 155 was issued in Oct 2015 (external, verify), so test the 2015 lead.
- **Contribution.** First causal estimate of Vietnamese disclosure mandates on financing costs. Informs whether mandate expansion buys lower capital costs in weak-enforcement markets.

## 2. G6: Mandated vs voluntary disclosure (signal vs boilerplate)

- **Gap.** P2 rests on signalling [p.1260] but mixes mandated and voluntary items. P1 measures only mandated items [p.65]. P3 notes a 15-item overlap with Circular 155 [p.141]. P5's literature review says effects differ by voluntary vs compulsory disclosure [p.89].
- **RQ.** Do investors and lenders price voluntary (beyond-mandate) sustainability disclosure differently from mandated disclosure?
- **Theory.** Signalling: only costly, discretionary disclosure separates types. Information-asymmetry theory: any credible information reduces risk.
- **Mechanism.** Voluntary items are costly to fake or produce, so they are informative about underlying sustainability and risk management.
- **H2.** The coefficient on voluntary disclosure is more negative than the coefficient on mandated disclosure (β_vol < β_mand ≤ 0). Under pure information-asymmetry theory, β_vol = β_mand.
- **Variables.**
  - IV: VOL_i,t (share of non-mandated GRI items); MAND_i,t (share of mandated items).
  - DV: COE (multiple proxies), COD.
  - Moderator: ESI.
  - Controls: as in RQ1.
- **Measurement.** Map P2/P3's 77 GRI items [Appendix, p.1279] onto the Circular 96 annual-report appendix (external, verify the item list).
- **Data.** 2019–2025 annual and sustainability reports; feasible because P2 and P3 already coded this frame.
- **Methodology.** FE panel with a coefficient-equality test, plus G1 timing (items that move from voluntary to mandated after a circular).
- **Identification.** Both components are endogenous. Use firm FE, and the within-item switch (an item's price effect before vs after it becomes mandated) as the sharpest test.
- **Contribution.** Turns "disclosure lowers COE" into a test that separates the theories. Policy relevance: does mandating more items matter?

## 3. G3: Mechanism (information asymmetry and investor clientele)

- **Gap.** The mechanism is asserted in P1 [p.70] and P2 [p.1265, 1268–1269] and measured nowhere.
- **RQ.** Through which channel does sustainability disclosure affect COE in Vietnam: stock liquidity and information asymmetry, or a shift in the investor base toward foreign and institutional holders?
- **Theory.** Disclosure–liquidity (Diamond & Verrecchia, cited in P1 [p.63] and P3 [p.139]); investor recognition and clientele (Dhaliwal et al. 2011 on institutional ownership, cited in P1 [p.62]).
- **Mechanism.** Disclosure → lower Amihud illiquidity / fewer zero-return days and/or higher foreign ownership → lower required return.
- **H3a.** Disclosure increases liquidity, and liquidity mediates part of the COE effect.
- **H3b.** Disclosure increases foreign ownership, and the COE effect is larger where foreign-ownership-limit headroom exists (external institutional detail, verify).
- **Variables.**
  - IV: disclosure index.
  - Mediators: Amihud ratio, zero-return days, price synchronicity, Δforeign ownership.
  - DV: COE.
  - Moderator: foreign-ownership-limit headroom.
  - Controls: size, turnover, free float, state ownership.
- **Data.** FiinPro-X / Vietstock daily prices and volumes, ownership, foreign room.
- **Methodology.** FE panel; staged mediation with bootstrap; channel tests on outcomes measured *after* report release; G1 shock as a first stage when available.
- **Identification.** Mediators are endogenous. Use timing (does the channel move in the release window?) and cross-sectional predictions (headroom) that are hard to explain by omitted firm quality.
- **Contribution.** First mechanism evidence for Vietnam. Identifies *who* prices ESG information in a retail-heavy market.

## 4. G4: Sensitive industries (legitimacy vs signalling; hard vs soft disclosure)

- **Gap.** Contradiction C1 (P2 negative vs P3 positive in energy). P2's ESI dummy is never interacted [Table 5]. Clarkson et al. (2008) discretionary-disclosure logic is cited in P5's references [p.95] but never applied.
- **RQ.** Is sustainability disclosure priced differently in environmentally sensitive industries, and does the answer depend on whether disclosure is hard (quantified, verifiable) or soft (narrative)?
- **Theory.** Legitimacy theory: soft disclosure by polluters is reactive and discounted, or reveals liabilities. Signalling / discretionary disclosure: hard disclosure by good performers is credible.
- **Mechanism.** Hard disclosure reduces uncertainty about environmental liabilities; soft disclosure by high-exposure firms raises investor attention to risk (P3's risk-revelation idea [p.144]).
- **H4a.** The effect of hard environmental disclosure on COE is negative in ESI and non-ESI firms alike.
- **H4b.** Soft environmental disclosure by ESI firms has a null or positive effect.
- **Variables.**
  - IV: HARD_env, SOFT_env.
  - Moderator: ESI (NAICS, as in P2 [Table 1]).
  - DV: COE, COD.
  - Controls: standard, plus emissions intensity where disclosed.
- **Measurement.** Code each GRI 300-series item (P2 Appendix [p.1279]) as quantified (numbers, targets, time series) vs narrative.
- **Data.** Annual and sustainability reports, 2019–2025.
- **Methodology.** FE panel with triple interactions; robustness on energy-only (replicating P3) and on the top-100 (replicating P2).
- **Identification.** Selection into hard disclosure: control for lagged environmental performance proxies; G1 timing.
- **Contribution.** Resolves C1 and tests legitimacy vs signalling directly.

## 5. G9: State ownership as moderator

- **Gap.** C3: P2 GOV (−) vs P5 SOE (+); conflicting cited evidence (Li & Liu 2018 in P2 [p.1260] vs Xu et al. 2014 in P5 [p.91–92]).
- **RQ.** Does state ownership amplify or dampen the cost-of-capital effect of sustainability disclosure?
- **Theory.** Soft budget constraint / implicit guarantee: SOE risk is already state-backed, so disclosure is less valuable. Visibility / legitimacy: SOEs face political scrutiny, so their disclosure is more credible.
- **H5.** β(disclosure × state share) > 0 (dampening). The alternative is < 0.
- **Variables.** Disclosure × state share %; DV COE and COD; controls as above.
- **Data.** Ownership from FiinPro-X.
- **Methodology.** FE with the interaction; within-firm divestment events (equitisation and state divestment, external, verify) as shifts in the moderator.
- **Identification.** Divestment timing may be endogenous. Use announced-schedule divestments.
- **Contribution.** Resolves C3. Best embedded in RQ1 or RQ3.

## 6. G5: Creditor channel with a valid COD measure

- **Gap.** Only P2 studies COD, with interest/total liabilities (acknowledged [p.1271]). P3 calls for COD work [p.145].
- **RQ.** Do Vietnamese lenders price sustainability disclosure into the interest rate firms pay on interest-bearing debt?
- **Theory.** Lender risk assessment and resource dependence (P2 [p.1259, 1261]).
- **Mechanism.** Disclosure lowers lenders' monitoring costs and perceived default/environmental-liability risk.
- **H6.** Disclosure (especially environmental) lowers interest expense / average interest-bearing debt.
- **Variables.**
  - DV: COD* = interest expense / average(short- + long-term borrowings).
  - IV: disclosure (E, S).
  - Moderators: SOE share, bank-dependence.
  - Controls: leverage, interest coverage, tangibility, size, ROA, maturity mix.
- **Data.** FS notes on borrowings (Vietnamese FS report borrowings separately; verify per firm); bond-issuance data where available.
- **Methodology.** FE panel; COD measured in year t+1 after disclosure in report t; event-window bond spreads as an extension.
- **Identification.** Reverse causality: lagged disclosure, G1 shock.
- **Contribution.** Corrects the only Vietnamese COD estimate. Tests the creditor channel in a bank-dominated system.

## 7. G7: Disclosure credibility and governance interplay

- **Gap.** Binary quantity indices in all four disclosure papers. Greenwashing (P2 [p.1271]), trust in quality (P3 [p.144]) and decoupling (P5 [p.89]) are raised but not measured. Governance (P4) is siloed.
- **RQ.** Is sustainability disclosure priced only when credible, meaning quantified, consistent over time and backed by strong governance?
- **Theory.** Agency theory (governance as a monitor of reporting); discretionary disclosure theory.
- **H7.** The COE effect of disclosure is stronger where board independence is higher and the auditor is Big4.
- **Variables.** Disclosure × governance (board independence, Big4, from P3/P4 definitions); quality score.
- **Data.** Annual reports; governance sections.
- **Methodology.** FE with interactions.
- **Identification.** Governance is endogenous; regulatory changes in board-independence rules could serve (external, verify).
- **Contribution.** Links the governance and disclosure streams. **Data-constrained** (little assurance variation in Vietnam [INFERENCE]).

## 8. G2: COE construct validity and timing

- **Gap.** CAPM COE ≈ beta. Implausible distributions (P2, P3, P4, P5). Anomalous control signs (P3 leverage; P4 ROA). Calls for alternatives (P2 [p.1271], P3 [p.145]). Forward EPS unavailable (P4 [p.3087]).
- **RQ.** Does the disclosure–cost-of-equity relation in Vietnam survive non-CAPM cost-of-equity measures and correct timing, and does it operate through systematic risk or information risk?
- **Theory.** Information-risk pricing vs CAPM.
- **H8.** Disclosure lowers implied COE beyond its effect on beta.
- **Measurement.** CAPM; model-based implied COE using cross-sectional earnings forecasts (external method, verify suitability); realised returns in factor regressions (portfolio sorts on disclosure); beta vs idiosyncratic volatility decomposition.
- **Data.** Prices, financials 2014–2025.
- **Methodology.** FE panels across proxies; portfolio tests.
- **Identification.** Measurement focus, not causal.
- **Contribution.** Validates or invalidates the core dependent variable of the Vietnamese literature. Best as a section of RQ1–RQ4.

## 9. G8: Time variation and market stress

- **Gap.** One COVID dummy (P2). P3's COE swings [Table 2]. P3's literature review: effects weaken in crises [p.140].
- **RQ.** Is the cost-of-capital benefit of disclosure larger or smaller during market stress?
- **Theory.** Insurance view of CSR (P1 cites the Godfrey 2005 moral-capital argument [p.62]) vs the "luxury" view.
- **H9.** Disclosure's COE benefit is larger in stress years (insurance).
- **Data and method.** Extend to 2025; disclosure × stress-year interactions; firm FE.
- **Identification.** Stress is common to all firms; the identifying variation is cross-sectional exposure.
- **Contribution.** Moderate; best as heterogeneity within RQ1 or RQ3.

## 10. G10: E/S/Ec decomposition (downgraded)

- **Gap.** Asked for by P1 [p.71]; already done by P2 [Table 6].
- **RQ.** Does the dimension ranking (environment > social > economic) found by P2 hold with firm + year FE and non-CAPM COE?
- **Contribution.** Replication only. **Recommended only as a robustness section** inside RQ2 or RQ4.

---
---

# Batch 2 Revision (v2): Top-10 Research Questions

**v2 top 10 by score:** G1 (34), G6 (33), G3 (30), G4 (29), G7 re-framed (29), G5 (28), G14 (28), G2 (27), G13 (26), G8 (25).

**Dropped from the top 10 since v1:** G9 (now a resolution question, since P6 tested it) and G10 (replication). Their v1 write-ups above are preserved for the record.

**Common design standard (v2, tightened).** Everything in v1, plus:
- (vi) report **CAPM and at least one implied COE** side by side. Precedents: P6 uses Easton + Harris–Wang [PDF p.4 / p.1387]; P7 uses residual income [PDF p.3 / p.66]. P7 finds that beta does not explain implied COE [Tables 2–3].
- (vii) **control for general disclosure** (P7's Botosan-type construct) when estimating CSR-disclosure effects.
- (viii) report **economically scaled** interaction coefficients (P6 prints 0.000).

## Revisions to existing RQs

### 1. G1: Causal effect of mandated disclosure (revised)
- **Gap evidence (added):** P6 (2014–2019) also straddles Circular 155, which it calls "the most essential document for regulating CSR in Vietnam" [PDF p.2 / p.1385], and uses GMM rather than the shock. That makes three Vietnamese papers (P1, P5, P6) with the shock unused.
- **Data (revised):** P6 assembled CSR disclosure for 225 firms from 2014 [PDF p.4 / p.1387], so a pre-mandate window is feasible at scale. P5's 48-firm figure was specific to its sampling.
- **Measurement (added):** borrow **P8's above-mandatory scoring** [PDF p.9] to separate each firm's pre-mandate compliance gap (items later required) from beyond-compliance disclosure.
- **Extension (G14):** a governance arm, if comparable Vietnamese governance reforms exist (external, verify). P8 and P9 show such reforms exist elsewhere and were never used for identification [P8 PDF p.4–6; P9 PDF p.1 / p.139].

### 2. G6: Mandated vs voluntary disclosure (revised)
- **Theory (added):** a unified "beyond-compliance" hypothesis. Investors price what firms do *beyond* what is required, both for disclosure (G6) and for governance (G13; P8 precedent).
- **H2b (new):** the voluntary-disclosure discount on COE is larger where beyond-compliance governance is stronger (credibility complementarity; G7).
- **Control (added):** general disclosure (P7 construct), so "voluntary CSR disclosure" is not just general transparency.

### 3. G3: Mechanism (re-scoped)
- **Gap (revised):** crash risk has been tested once (P6: CSRD → CRASH −0.204***, CRASH → COE +0.142***, Sobel indirect −0.006 [Tables 3–4, PDF p.8 / p.1391]), with inconsistent arithmetic (C11). The liquidity / adverse-selection, estimation-risk and investor-base channels theorised in P7 [PDF p.1–2 / p.64–65] and P1 [p.63] remain untested.
- **RQ (revised):** which channel carries the disclosure → COE effect in Vietnam: liquidity / adverse selection, investor base, or crash risk?
- **Method (revised):** simultaneous multi-mediator model (not sequential Baron–Kenny), with bootstrap indirect effects. Mediators are measured *after* report release. Report path coefficients consistently, fixing the C11 problem.
- **Contribution (revised):** builds directly on P6. A reviewer will compare against it, so the paper must show where crash risk ranks among competing channels.

### 4. G4: Sensitive industries (sharper target)
- **Gap (added):** P3 is now the only positive estimate among six Vietnamese papers. P6 proposes SOEs in high-polluting industries as future research [PDF p.10 / p.1393].
- **H4c (new):** the soft-disclosure penalty in sensitive industries is larger for state-owned firms (SOE multitask theory predicts stronger legitimacy-seeking; P6 [PDF p.3 / p.1386]).

### 8. G2: COE construct validity (strengthened)
- **Gap evidence (added):**
  - P7: CAPM cannot test disclosure effects [PDF p.3 / p.66]; beta does not explain implied COE (r=−0.027; p=0.672) [Tables 2–3, PDF p.5 / p.68].
  - The size sign aligns partly with the COE proxy (C6).
  - Implied COE is feasible: P6, P7, and Refinitiv forecasts (C12).
- **RQ (revised):** in the same Vietnamese panel, how strongly do CAPM-COE and implied-COE agree, and which disclosure findings survive each?

## New RQs (Batch 2)

### 5 (v2). G7 re-framed: Governance as the credibility channel for CSR disclosure
- **Gap.** CSR disclosure and governance are studied in separate silos in Vietnam (P1–P3, P5–P6 vs P4). The cross-country logic exists: Chen et al. (2004), as cited in P9 [PDF p.8 / p.146], find disclosure effects only under strong investor protection and governance effects only under weak protection. P9 shows governance labels may be invalid [PDF p.23 / p.161].
- **RQ.** Is the cost-of-equity benefit of CSR disclosure larger in Vietnamese firms with *substantive* governance (beyond-compliance board and audit-committee practices)?
- **Theory.** Agency theory: governance monitors reporting. Credibility / discretionary disclosure: verified information is priced.
- **Mechanism.** Strong boards and audit committees lower the probability that CSR disclosure is cheap talk, so investors update more on it.
- **H7.** β(CSR disclosure × substantive governance) < 0. The competing **substitution** hypothesis is > 0.
- **Variables.**
  - IV: CSR disclosure (P6 / P2 frame).
  - Moderator: beyond-compliance governance index (P8 logic) vs compliance index (P4 logic).
  - DV: implied + CAPM COE.
  - Controls: general disclosure (P7), size, leverage, state share, firm + year FE.
- **Data.** Annual-report governance sections; Refinitiv / FiinPro.
- **Identification.** Governance is endogenous. Use lagged governance and mandate timing (Idea 1) as a shifter of disclosure, holding governance fixed.
- **Contribution.** Links two siloed streams in the Vietnamese literature and tests complementarity vs substitution within one country. **Novelty is capped** by the cross-country work cited in P9.

### 7 (v2). G14 (new): Governance- and disclosure-code reforms as quasi-experiments
- **Gap.** India (Clause 49, Companies Act 2013) and Pakistan (Code 2002) reforms fall in or before the windows of P8 and P9, which use pooled OLS / LSDV. P9 attributes its null to a reform "transition phase" [PDF p.1 / p.139] without testing it.
- **RQ.** Do governance-code reforms lower the cost of equity, and more for firms with larger pre-reform compliance gaps?
- **Theory.** Mandatory governance as commitment; compliance-cost / boilerplate counter-view.
- **H14.** The post-reform COE decline increases with the pre-reform governance gap.
- **Data.** Pre/post governance scores (P8-style index); reform dates (external, verify).
- **Method.** Intensity DiD / event study.
- **Identification.** Concurrent shocks; anticipation. P8 cites an India Clause 49 event study (Black & Khanna 2007) [PDF p.16], so **India-specific novelty is low**.
- **Contribution.** For a Vietnam programme, this is best as the governance arm of Idea 1. It is not recommended standalone.

### 9 (v2). G13 (new): Compliance labels vs substantive governance
- **Gap.** Governance → COE is null or weak with compliance-type measures (P4 [Table 8]; P9 [Tables 6, 10]) and negative with an above-mandatory index (P8 [Table III]). P9: independence labels are uninformative [PDF p.23 / p.161].
- **RQ.** Does governance measured as beyond-compliance practice predict COE in Vietnam where compliance-label measures do not?
- **Theory.** Beyond-compliance signalling. Label vs substance (P9).
- **H13.** A beyond-compliance index predicts lower implied COE; a compliance-label index does not.
- **Variables.**
  - Two governance indices built from the same annual reports: compliance (P4 variables) and beyond-compliance (P8 logic, adapted to Vietnamese rules; external, verify).
  - Substantive independence proxies: tenure, affiliations.
- **Method.** FE panel; horse race of the two indices; implied + CAPM COE.
- **Identification.** Associational; strengthen with governance-rule changes if available.
- **Contribution.** Explains null governance findings (C8, C9). Forms the governance half of the beyond-compliance theory (with G6).
