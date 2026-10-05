# Phases 10 and 13: Scoring, Ranking and Adversarial Review

## Phase 10: Scores (1 = weak, 5 = strong)

Criteria: **Nov** novelty · **Imp** academic importance · **Th** theoretical contribution · **Emp** empirical contribution · **Data** data availability · **Feas** methodological feasibility · **Id** identification strength · **Pub** publication value. Overall = sum / 40, also shown as the mean.

| Rank | Gap | Nov | Imp | Th | Emp | Data | Feas | Id | Pub | Sum | Mean |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **G1** Causal effect of mandated E&S disclosure (Circular 155 / 96) | 4 | 5 | 3 | 5 | 3 | 4 | 4 | 5 | **33** | 4.13 |
| 2 | **G6** Mandated vs voluntary disclosure (signalling test) | 4 | 4 | 5 | 4 | 4 | 5 | 3 | 4 | **33** | 4.13 |
| 3 | **G3** Mechanism: information asymmetry / investor base | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | **31** | 3.88 |
| 4 | **G4** Sensitive industries: legitimacy vs signalling; hard vs soft | 3 | 4 | 4 | 4 | 4 | 4 | 2 | 4 | **29** | 3.63 |
| 5 | **G9** State ownership as moderator | 3 | 4 | 4 | 3 | 5 | 5 | 2 | 3 | **29** | 3.63 |
| 6 | **G5** Cost of debt with a valid measure | 4 | 4 | 3 | 4 | 3 | 4 | 2 | 4 | **28** | 3.50 |
| 7 | **G7** Disclosure credibility / governance interplay | 4 | 5 | 4 | 4 | 2 | 3 | 2 | 4 | **28** | 3.50 |
| 8 | **G2** COE construct validity and timing | 3 | 4 | 3 | 4 | 2 | 3 | 3 | 3 | **25** | 3.13 |
| 9 | **G8** Time variation / market stress | 3 | 3 | 3 | 3 | 4 | 4 | 2 | 3 | **25** | 3.13 |
| 10 | G10 E/S/Ec decomposition | 2 | 3 | 3 | 3 | 4 | 4 | 2 | 2 | 23 | 2.88 |
| — | G11 Non-linearity | 2 | 2 | 3 | 2 | 5 | 5 | 1 | 2 | 22 | 2.75 (rejected) |
| — | G12 Governance → COE re-run | 1 | 2 | 2 | 2 | 4 | 4 | 1 | 1 | 17 | 2.13 (rejected) |

**Tie-breaks.**
- G1 ranks above G6 because its identification is stronger.
- G4 ranks above G9 because its empirical and publication value is higher and it resolves an observed contradiction.
- G5 ranks above G7 because its data are more feasible.

**Note on G2.** G2 scores lower as a standalone paper but is a **design requirement for every other gap**. Any new study that keeps CAPM-only COE, contemporaneous timing and no year FE inherits the weaknesses documented in C2 and C6.

---

## Phase 13: Adversarial review of the top gaps

Questions: (1) already answered? (2) mere replication? (3) too narrow? (4) merely geographic? (5) data realistic? (6) causal ID possible? (7) novel to a reviewer? (8) theoretically important? (9) result obvious? (10) stronger question hidden behind it?

### G1: Mandated disclosure as a quasi-experiment
1. **Within this corpus, no.** Outside the corpus, the international mandatory-CSR-reporting literature (China, EU and others) exists, and P2 cites a Chinese quasi-experiment [PDF p.23 / p.1278]. **A literature search for any Vietnamese Circular-155 DiD study is required before claiming novelty.** It could not be done from the PDFs.
2. No. A design change is not a replication.
3. No. Policy-level question.
4. Partly geographic. Mitigated because Vietnam offers a **compliance-intensity** design (mandate on all listed firms at once, heterogeneous pre-mandate gaps) and weak enforcement, which tests whether mandates without enforcement move prices.
5. **Main risk.** Pre-2016 disclosure must be hand-coded from 2013–2015 annual reports. P5 found complete reports for only 48 firms in 2014 [PDF p.5 / p.90]. Restrict to firms with reports available, or use the Circular 96 change (2020 vs 2021+), where coverage is better.
6. Partially. There is no untreated group, so the design relies on intensity. Threats: concurrent 2016 shocks, mean reversion, differential trends by size. Address with event-study pre-trends, size-by-year FE and placebo items not covered by the circular.
7. Yes, if the Vietnamese prior-literature check comes back clean.
8. Yes: mandatory disclosure theory vs voluntary disclosure theory.
9. Not obvious. Weak enforcement could produce a null; boilerplate compliance could produce no price effect.
10. **Stronger question:** *does mandated disclosure change the cost of capital only for firms whose forced disclosure was informative (high pre-mandate opacity), and does it crowd out voluntary signalling?* That merges G1 with G6.

**Verdict: keep, rank 1** (conditional on the novelty search).

### G6: Mandated vs voluntary components
1. Not in the corpus. P1 measures only mandated items; P2 and P3 do not split.
2. No. A new decomposition with a theory-derived prediction.
3. Moderate breadth, but theory-relevant.
4. No. The theory test is general; Vietnam's checklist-style mandate makes the split unusually clean.
5. Yes. Items can be mapped to the Circular 155 appendix (P3 notes the 15-item overlap [p.141]); GRI coding is already established (P2, P3).
6. Weak on its own: both components are endogenous. Strengthened when combined with the G1 timing.
7. Yes. Reviewers increasingly ask "is it signal or boilerplate?"
8. **High.** It separates signalling from pure information-asymmetry accounts.
9. No. Both outcomes (voluntary > mandated, or equal) are plausible and informative.
10. Merges naturally with G1 (see above).

**Verdict: keep, rank 2.**

### G3: Mechanism
1. Not in the corpus.
2. No.
3. No.
4. No. The mechanism question is general.
5. Mostly. Trading data (FiinPro-X, Vietstock) give Amihud illiquidity and zero-return days; ownership data give foreign/state shares. **Bid–ask spreads and analyst data are thin in Vietnam**, so use low-frequency illiquidity proxies.
6. Mediation is not causal by itself. Strengthen with G1 timing (do channel variables move first?) and with cross-sectional predictions (larger effect where foreign-ownership headroom exists).
7. Yes.
8. Yes. It turns an association into an explanation.
9. Not obvious. An investor-base channel could dominate the liquidity channel, or neither could operate.
10. Possibly: *who* prices sustainability information in a retail-dominated market? That sharpens G3 into an investor-clientele question.

**Verdict: keep, rank 3.**

### G4: Sensitive-industry context
1. Not resolved. C1 is open.
2. Partly a re-estimation. Novelty comes from (a) the explicit legitimacy-vs-signalling prediction and (b) the hard/soft disclosure split.
3. Narrow if limited to energy; fine in a broad panel with interactions.
4. No.
5. Yes. ESI classification is already in P2 (NAICS) and GRI coding is established.
6. Weak (associational). Use firm + year FE and the G1 shock for credibility.
7. Moderately. Reviewers know the "environmentally sensitive industries" literature, so novelty depends on the hard/soft angle.
8. Yes.
9. Risk that a null interaction is uninformative. Pre-register the competing predictions.
10. Yes: *does quantified environmental performance disclosure lower COE while narrative disclosure by polluters raises it?* This is the stronger version.

**Verdict: keep, rank 4**, reframed around hard vs soft disclosure.

### G9: State ownership as moderator
1. International evidence conflicts (cited in P2 and P5); untested in Vietnam.
2. Partly replicates China studies.
3. Narrow as a standalone paper.
4. **Risk of being seen as geographic.**
5. Excellent data.
6. Weak; divestment events help.
7. Moderately.
8. Moderate.
9. No.
10. Better embedded as a moderator in G3 or G4 than as a standalone paper.

**Verdict: downgrade to a moderator inside top ideas, not a standalone top-5 idea.**

### G5: Cost of debt
1. Only P2, with a crude proxy.
2. Not if the measure is fixed and the creditor channel is theorised.
3. No.
4. No. Bank-dominated financing is a general setting.
5. **Feasible.** Vietnamese financial statements report borrowings separately from payables, so interest-bearing debt can be extracted (verify per firm); bond data are partial.
6. Weak without a shock. Green-credit policy changes could serve (verify instruments and dates).
7. Yes, for an emerging bank-based market.
8. Moderate–high: do lenders, especially state-owned banks, read ESG disclosure?
9. Not obvious.
10. *Do state-owned and private banks price disclosure differently?* That needs loan-level data, which is likely unavailable.

**Verdict: keep, rank 5 in the final top 5** (it replaces G9).

### G7: Credibility
1. Not in the corpus.
2. No.
3. No.
4. No.
5. **Weak.** External assurance of Vietnamese sustainability reports is rare, so the variable has little variation [INFERENCE]. Text-based specificity measures need Vietnamese NLP.
6. Weak.
7. Yes.
8. High.
9. No.
10. Partly subsumed by G4 (hard vs soft) and G6.

**Verdict: important but data-constrained. Fold its feasible part (quantified vs narrative) into G4.**

### G2: COE measurement
- A standalone paper risks being seen as methodological housekeeping.
- **Verdict: not a top-5 idea, but a mandatory design standard.**

### G8: Time variation
- Mainly a temporal extension; one-off stress dummies give weak identification.
- **Verdict: downgrade. Usable as heterogeneity inside G1/G3.**

### G10: E/S/Ec decomposition
- Replication of P2 Table 6.
- **Verdict: reject as a standalone gap.**

---

## Final ordering after adversarial review

1. **G1 (flagship):** causal effect of mandated E&S disclosure (Circular 155 / Circular 96), with the G6 split as the key heterogeneity test
2. **G6:** signal vs boilerplate, i.e. whether voluntary (beyond-mandate) disclosure is priced differently from mandated items (feasible on 2019–2025 data even without pre-mandate collection)
3. **G3:** mechanism, i.e. investor clientele and information asymmetry
4. **G4 (+ G7 feasible part):** hard vs soft environmental disclosure in sensitive industries (resolves C1)
5. **G5:** creditor channel with a valid COD measure

Moderators embedded across ideas: **G9** (state ownership), **G8** (stress periods). Design standard for all: **G2**.
