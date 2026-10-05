# Phase 14: Final Top-5 Research Opportunities

Selected after the adversarial review (`research_gaps/ranked_gaps.md`). Novelty and feasibility scores come from Phase 10 (1–5). Overall = Phase-10 mean adjusted for adversarial findings, stated explicitly.

**Universal caveat.** Novelty is judged **relative to the five-paper corpus**. Before committing, run a targeted search (Vietnamese- and English-language) for: Circular 155 + cost of capital + difference-in-differences; voluntary vs mandatory sustainability disclosure Vietnam; Amihud / foreign ownership + ESG disclosure Vietnam. This could not be done from the PDFs alone.

---

## Idea 1 (flagship): Do disclosure mandates lower financing costs in a weak-enforcement market? Evidence from Vietnam's Circular 155 and Circular 96

1. **Research question.** Did mandated environmental and social disclosure lower the cost of equity and debt of Vietnamese listed firms, and was the effect concentrated among firms the mandate forced to disclose more?
2. **Research gap.**
   - All Vietnamese evidence is associational: P1, P2, P3 and P5 use static panels.
   - The within-firm estimates are missing or fragile: P1's FE is unreported, P3's FE is insignificant (p=0.452), and P5's FE is insignificant with conventional SEs (contradiction C2).
   - The mandates already sit inside the sample windows and are unused.
3. **Literature support.**
   - P1 chose 2014–2021 as "before and after Circular 155" but ran no pre/post test [PDF p.6 / p.64].
   - P5: disclosing firms rose from 38 (2014) to 115 (2017) [PDF p.8 / p.93].
   - P2 and P3 reference Circular 96/2020 [PDF p.2 / p.1257; PDF p.2 / p.139].
   - P2 lists endogeneity as unresolved [PDF p.16 / p.1271] and cites a Chinese quasi-natural experiment only in further reading [PDF p.23 / p.1278].
4. **Theoretical framework.** Mandatory-disclosure economics (commitment lowers information risk) vs the boilerplate/compliance-cost view (P3 [PDF p.7 / p.144]); signalling (P2 [PDF p.5 / p.1260]) for the voluntary-crowd-out extension.
5. **Hypotheses.**
   - H1: the post-mandate decline in COE (and COD) increases with the firm's pre-mandate disclosure gap.
   - H1-ext: the pricing of voluntary items falls after mandated items become compulsory (crowd-out).
6. **Variables.**
   - Treatment: GAP_i × POST_t.
   - Outcomes: CAPM COE, implied COE, COD* (interest / interest-bearing debt), Amihud illiquidity.
   - Moderators: state share, ESI.
   - Controls: size, leverage, BTM, ROA, beta (for non-CAPM outcomes); firm FE, industry×year FE.
7. **Data requirements.**
   - Hand-coded mandated-item disclosure for pre/post windows. P1's 33-item Circular 155 list [Table 1, PDF p.7 / p.65] is reusable.
   - Annual reports 2013–2019 (Circular 155) and/or 2018–2023 (Circular 96).
   - Prices and financials from FiinPro-X or Vietstock (as in P2 and P3).
8. **Methodology.** Continuous-treatment DiD and dynamic event study; placebo on items *not* covered by the circular; heterogeneity by state ownership and ESI.
9. **Identification strategy.**
   - No untreated group, so identification comes from treatment intensity. Show flat pre-trends in event-study leads.
   - Address concurrent shocks with industry×year FE.
   - Address size-driven trends with size-decile×year FE and matching on pre-period characteristics.
   - Test anticipation via the issuance year (Circular 155 issued Oct 2015, effective 2016: external, verify).
   - Run Circular 96 as a second, independent shock.
10. **Expected contribution.**
    - First quasi-experimental evidence on Vietnamese disclosure mandates.
    - Tells regulators whether checklist mandates lower capital costs when enforcement is weak.
    - Resolves the within/between fragility in the existing literature.
11. **Main risks.**
    - (a) Pre-2016 reports are thin: P5 found complete reports for only 48 firms in 2014 [PDF p.5 / p.90]. Fallback: Circular 96.
    - (b) A null result, interpreted as boilerplate compliance. Still publishable as a policy finding if the design is tight.
    - (c) A prior Vietnamese DiD study may exist (search needed).
12. **Novelty: 4/5.**
13. **Feasibility: 3.5/5** (hand-collection burden).
14. **Overall: 4.1/5.**

---

## Idea 2: Signal or boilerplate? Pricing of voluntary vs mandated sustainability disclosure

1. **Research question.** Do equity investors and lenders price beyond-mandate (voluntary) sustainability disclosure more than disclosure required by regulation?
2. **Research gap.** The theory in use (signalling) predicts that only discretionary disclosure matters. Every Vietnamese index pools mandated and voluntary items, so the theories cannot be told apart.
3. **Literature support.**
   - P2 calls signalling the foundational theory [PDF p.5 / p.1260] and uses 77 unsplit GRI items [PDF p.8 / p.1263].
   - P1 uses only Circular 155 items [Table 1, PDF p.7 / p.65].
   - P3 notes 15 GRI items appear in the Circular 155 appendix [PDF p.4 / p.141].
   - P5's literature review: effects differ for voluntary vs compulsory disclosure [PDF p.4 / p.89].
4. **Theoretical framework.** Signalling (costly, discretionary signals) vs information-asymmetry reduction (any credible information).
5. **Hypothesis.** H2: β_voluntary < β_mandated ≤ 0. Equality supports pure information-asymmetry theory.
6. **Variables.** VOL and MAND shares of items; outcomes COE (two proxies) and COD*; moderators ESI and state share; standard controls with firm + year FE.
7. **Data requirements.** GRI coding on 2019–2025 reports (the P2/P3 frame [Appendix, PDF p.24 / p.1279]); mapping to the Circular 96 annual-report appendix (verify item list).
8. **Methodology.** FE panel with a coefficient-equality test; item-level "switch" test, where items that become mandated serve as within-item before/after comparisons.
9. **Identification strategy.** Firm FE removes stable disclosure propensity. The switch test uses regulatory reclassification of items, which is plausibly exogenous to a given firm's COE. Pre-trend checks at the item level.
10. **Expected contribution.** A direct theory test that also matters for policy: whether expanding mandatory item lists has a pricing payoff.
11. **Main risks.** Few items switch status, so the switch test has low power. Voluntary disclosers are larger and better governed, so selection must be absorbed by FE.
12. **Novelty: 4/5.**
13. **Feasibility: 4.5/5.**
14. **Overall: 4.1/5.**

---

## Idea 3: Who prices sustainability information in a retail-dominated market? Liquidity vs investor-clientele channels

1. **Research question.** Does sustainability disclosure lower COE in Vietnam by improving stock liquidity (information asymmetry) or by attracting foreign and institutional investors?
2. **Research gap.** The mechanism is asserted in every disclosure paper's conclusion and measured in none (mechanism gap; `white_space.md`, Matrix 4).
3. **Literature support.**
   - Information-asymmetry conclusion: P1 [PDF p.12 / p.70]; P2 [PDF p.11 / p.1265; PDF p.14 / p.1269].
   - Liquidity theory: P1 [PDF p.5 / p.63]; P3 [PDF p.2 / p.139].
   - Institutional-ownership channel cited by P1 (Dhaliwal et al. 2011) [PDF p.4 / p.62].
   - Foreign ownership appears only as a control (P5, Table 7 [PDF p.9 / p.94]).
4. **Theoretical framework.** Disclosure–liquidity (Diamond–Verrecchia); investor recognition / clientele.
5. **Hypotheses.**
   - H3a: disclosure lowers illiquidity, which mediates the COE effect.
   - H3b: disclosure raises foreign ownership, and the COE effect is stronger where foreign-ownership headroom exists.
6. **Variables.**
   - IV: disclosure index.
   - Mediators: Amihud ratio, zero-return days, price synchronicity, Δforeign ownership.
   - Moderator: foreign-ownership-limit headroom (external institutional feature, verify).
   - DV: COE.
   - Controls: size, free float, turnover, state share; firm + year FE.
7. **Data requirements.** Daily trading and ownership data (FiinPro-X / Vietstock); disclosure scores (reuse the P2/P3 frame).
8. **Methodology.** FE panel; staged mediation with bootstrap CIs; release-window tests (channel variables measured in the months after report release).
9. **Identification strategy.**
   - Mediation is not causal by itself. Strengthen with:
     - timing (the channel must move after release);
     - a cross-sectional prediction (headroom) that omitted firm quality does not predict;
     - Idea 1's mandate shock as an exogenous disclosure shifter.
10. **Expected contribution.** Turns an association into an explanation. Identifies the investor clientele that rewards disclosure, which matters for market-upgrade policy discussions (P3 mentions the market-upgrade goal [PDF p.2 / p.139]).
11. **Main risks.**
    - Bid–ask and analyst data are thin, which forces low-frequency proxies.
    - Headroom may correlate with size and sector (absorb with industry×year FE).
    - Foreign ownership caps data needs verification.
12. **Novelty: 4/5.**
13. **Feasibility: 4/5.**
14. **Overall: 3.9/5.**

---

## Idea 4: Hard vs soft environmental disclosure in environmentally sensitive industries: legitimacy or signalling?

1. **Research question.** Is sustainability disclosure priced differently in environmentally sensitive industries, and does quantified (hard) disclosure lower COE while narrative (soft) disclosure does not?
2. **Research gap.** Contradiction C1 (P2 negative in large caps vs P3 positive in energy) is unresolved. P2's ESI dummy is never interacted. Disclosure quality is never measured.
3. **Literature support.**
   - P2 Table 3 [PDF p.11 / p.1266] and Table 5 (IND −0.015***) [PDF p.13 / p.1268].
   - P3 Table 3 [PDF p.6 / p.143] and its risk-revelation and compliance-cost argument [PDF p.7 / p.144].
   - P2 cites Li & Liu (2018) on sensitive industries [PDF p.5 / p.1260].
   - P5's literature review gives positive-sign explanations (decoupling, negative-NPV CSR, lack of trust) [PDF p.4 / p.89] and cites Clarkson et al. (2008) [refs, PDF p.10 / p.95].
   - P2 raises greenwashing [PDF p.16 / p.1271].
4. **Theoretical framework.** Legitimacy theory (reactive, soft disclosure by exposed firms) vs signalling / discretionary-disclosure theory (hard, verifiable disclosure by good performers).
5. **Hypotheses.**
   - H4a: HARD_env lowers COE in both ESI and non-ESI firms.
   - H4b: SOFT_env has a null or positive effect for ESI firms.
6. **Variables.** HARD_env, SOFT_env (from GRI 301–308 items); ESI (NAICS, per P2 Table 1); outcomes COE and COD*; standard controls plus firm + year FE.
7. **Data requirements.** 2019–2025 reports; re-code environmental items as quantified vs narrative.
8. **Methodology.** FE panel with triple interactions. Two replication arms: P3's energy sample and P2's top-100. Show that the C1 sign difference disappears once year FE and the hard/soft split are added.
9. **Identification strategy.** Firm + year FE; lagged disclosure; Idea 1's mandate as a shifter of soft disclosure (mandated items are mostly soft).
10. **Expected contribution.** Resolves C1. Gives a direct legitimacy-vs-signalling test with a disclosure-quality dimension the Vietnamese literature lacks.
11. **Main risks.**
    - Hard/soft coding needs reliability checks (two coders, kappa).
    - Too few hard disclosures, given that the Appendix shows low environmental coverage [PDF p.24 / p.1279].
    - A null interaction (pre-register predictions).
12. **Novelty: 3.5/5.**
13. **Feasibility: 4/5.**
14. **Overall: 3.7/5.**

---

## Idea 5: Do lenders read sustainability reports? The creditor channel in a bank-dominated market

1. **Research question.** Does sustainability (especially environmental) disclosure lower the interest rate Vietnamese firms pay on interest-bearing debt, and does this differ by state ownership?
2. **Research gap.** One Vietnamese COD estimate exists (P2), using a proxy the authors concede is flawed. No study isolates interest-bearing debt or a lender-relevant moderator.
3. **Literature support.**
   - P2 COD results [Table 4, PDF p.12 / p.1267; Table 6, PDF p.15 / p.1270] and the stated limitation [PDF p.16 / p.1271].
   - P3's call for COD work [PDF p.8 / p.145].
   - P2's discussion of green-credit obstacles [PDF p.3 / p.1258].
   - P2 cites a U-shape (Ye & Zhang 2011) and a costly-CSR view (Goss & Roberts 2011) [PDF p.6 / p.1261].
4. **Theoretical framework.** Lender monitoring and default-risk assessment; resource dependence (P2 [PDF p.4 / p.1259]); soft budget constraint for SOEs.
5. **Hypotheses.**
   - H5a: disclosure in report t lowers COD* in t+1.
   - H5b: the effect is weaker for majority-SOE firms (implicit guarantees).
6. **Variables.**
   - DV: COD* = interest expense / average interest-bearing borrowings.
   - IV: E and S disclosure.
   - Moderator: state share.
   - Controls: leverage, interest coverage, tangibility, size, ROA, short-term debt share; firm + year FE.
7. **Data requirements.** FS notes on borrowings (verify consistency across firms); disclosure scores; optional bond-issuance terms.
8. **Methodology.** FE panel with lead-lag structure; robustness on the P2 proxy to show how measurement changes the result.
9. **Identification strategy.**
   - Lagged disclosure.
   - Idea 1's mandate shock.
   - Green-credit policy timing as a cross-sectional shifter for ESI firms (verify specific SBV instruments and dates; not in corpus).
10. **Expected contribution.** First valid measure of the creditor channel in Vietnam. Tests whether ESG information reaches lenders in a credit-dominated system.
11. **Main risks.**
    - No loan-level data, so bank-side heterogeneity is unobservable.
    - Heavy state-bank lending may mute pricing (itself a finding).
    - Interest capitalisation distorts interest expense.
12. **Novelty: 4/5.**
13. **Feasibility: 3.5/5.**
14. **Overall: 3.5/5.**

---

## How the five ideas fit together

```
Idea 1 (mandate shock)  ── provides exogenous disclosure variation to ──►  Ideas 2, 3, 4, 5
Idea 2 (signal vs boilerplate) ── is the key heterogeneity test inside ──► Idea 1
Idea 3 (mechanism)      ── explains WHY Ideas 1/2/4 work (or don't)
Idea 4 (hard vs soft, ESI) ── resolves contradiction C1
Idea 5 (creditor channel) ── extends all of the above from equity to debt
Design standard G2 (multi-proxy COE, correct timing, firm+year FE) applies to all five.
```

A realistic programme: Idea 2 first (cheapest data, reuses the P2/P3 GRI frame), then Idea 1 (the flagship, needing pre-mandate hand-collection), with Ideas 3 and 4 as sections or companion papers.

---
---

# Batch 2 Revision (v2): Top-5 Research Opportunities

**The identity and order of the top 5 are unchanged after Batch 2.** Each idea is revised below with new literature support, design changes, risk updates and re-scored values. The v1 write-ups above remain the base text.

## Idea 1 (flagship) v2: Disclosure mandates as a quasi-experiment
- **New literature support:**
  - P6 (2014–2019, 225 firms) straddles Circular 155, calls it "the most essential document for regulating CSR in Vietnam" [PDF p.2 / p.1385], and still estimates GMM without exploiting it.
  - That makes 0 quasi-experiments in 9 papers.
  - P9 attributes its null to a post-reform "transition phase" [PDF p.1 / p.139], the kind of claim only a pre/post design can test.
- **Data risk downgraded.** P6 shows CSR disclosure data for 225 firms from 2014 [PDF p.4 / p.1387]. The main v1 risk (P5's 48 firms in 2014) is substantially reduced.
- **Design upgrades:**
  - (a) Measure each firm's pre-mandate **compliance gap** with P8-style above-mandatory scoring [PDF p.9].
  - (b) Outcomes: CAPM **and** implied COE (P6 Easton + Harris–Wang; P7 residual income), since they can diverge (P7 [Tables 2–3]).
  - (c) Control for general disclosure (P7).
  - (d) Use P6's GMM estimate as the benchmark the DiD estimate is compared against.
- **Extension:** governance-reform arm (G14), if Vietnamese reform dates qualify (external, verify).
- **Scores:** Novelty 4/5 (unchanged) · Feasibility **4/5** (↑ from 3.5) · Overall **4.3/5** (↑ from 4.1).

## Idea 2 v2: Signal or boilerplate, within a "beyond-compliance" theory
- **New literature support:**
  - P8 operationalises beyond-compliance *governance* by scoring 1 only above the mandatory minimum [PDF p.9], and finds governance lowers COE in India [Table III].
  - P6 stresses that Vietnam's framework "has not yet mandated full implementation of CSR activities" and urges firms to supplement required disclosures [PDF p.10 / p.1393].
  - P9 shows compliance labels (independence) carry no price signal [PDF p.23 / p.161].
- **Reframed RQ:** do investors price beyond-compliance disclosure (and beyond-compliance governance) while ignoring compliance-level disclosure and governance?
- **Added hypothesis H2b:** voluntary disclosure is priced more where beyond-compliance governance is stronger (credibility complementarity; G7/G13).
- **Added control:** general disclosure (P7). Otherwise, "voluntary CSR disclosure" may just be general transparency (white-space Matrix 3, v2).
- **Scores:** Novelty 4/5 · Feasibility 4.5/5 · Overall **4.2/5** (↑ from 4.1, for stronger theory framing).

## Idea 3 v2: Channel horse race (re-scoped)
- **What changed:** P6 tests crash risk as a mediator (Sobel indirect −0.006, 18.5% of the total effect [Table 4, PDF p.8 / p.1391]). Its path arithmetic is inconsistent (C11). Idea 3 can no longer claim "first mechanism test" in Vietnam.
- **Revised RQ:** which channel carries the disclosure → COE effect: liquidity / adverse selection, estimation risk, investor base (foreign / institutional), or crash risk?
- **Theory (added):** P7 gives the explicit three-channel framework (adverse selection, estimation risk, public/private information) [PDF p.1–2 / p.64–65].
- **Method (revised):** simultaneous multi-mediator model with bootstrap CIs; crash risk (DUVOL, as in P6 [App. B]) included as a competing mediator; consistent reporting of path products.
- **Main risk (added):** reviewers will expect explicit engagement with P6.
- **Scores:** Novelty **3.5/5** (↓ from 4) · Feasibility 4/5 · Overall **3.7/5** (↓ from 3.9).

## Idea 4 v2: Hard vs soft environmental disclosure in sensitive industries
- **What changed:** P6 and P7 add two more negative estimates (implied COE), so P3's positive sign is now the only exception among six Vietnamese papers. That makes the industry-context explanation a sharper, falsifiable target. P6 suggests studying SOEs in high-polluting industries [PDF p.10 / p.1393].
- **Added hypothesis H4c:** the soft-disclosure penalty in sensitive industries is larger for SOEs (SOE multitask theory, P6 [PDF p.3 / p.1386]).
- **Added replication arm:** re-estimate P3's energy sample with implied COE and year FE. If the positive sign disappears, C1 is a CAPM/specification artefact; if it persists with hard/soft separation, it is substantive.
- **Scores:** Novelty 3.5/5 · Feasibility 4/5 · Overall **3.8/5** (↑ from 3.7, for a sharper falsification target).

## Idea 5 v2: Creditor channel
- **No Batch 2 paper studies the cost of debt.** The gap is unchanged; Batch 2 adds no new support or competition.
- **Minor addition:** P9 frames high WACC as the core deterrent for family firms [PDF p.3 / p.141], which supports a WACC/COD extension conceptually, but provides no evidence.
- **Scores:** unchanged (Novelty 4/5 · Feasibility 3.5/5 · Overall 3.5/5).

## Runners-up after Batch 2 (not in the top 5, with reasons)
| Gap | Score | Why not top 5 |
|---|---|---|
| G7 (governance as credibility moderator) | 29 | Overlaps G6/G13; novelty capped by Chen et al. (2004) cited in P9 [PDF p.8 / p.146]. **Embedded as H2b in Idea 2** |
| G14 (reforms as quasi-experiments) | 28 | Governance arm of Idea 1. India-specific novelty low (P8 cites Black & Khanna 2007 [PDF p.16]) |
| G13 (governance measurement validity) | 26 | Strong as the governance half of Idea 2's beyond-compliance theory; narrow alone |
| G9 (SOE moderation) | 25 | Tested by P6; remains a moderator inside Ideas 1, 3, 4 |

## How the five ideas fit together (v2)
```
Idea 1 (mandate shock, compliance-gap intensity) ── exogenous disclosure variation ──► Ideas 2, 3, 4, 5
Idea 2 (beyond-compliance: disclosure + governance) ── key heterogeneity test inside Idea 1
Idea 3 (channel horse race incl. P6's crash risk) ── explains WHY
Idea 4 (hard vs soft, ESI, SOE) ── resolves C1 (P3 now sole outlier)
Idea 5 (creditor channel) ── extends to debt
Design standard G2 v2: CAPM + implied COE, release-dated disclosure, firm+year FE, control for general disclosure (P7),
                       economically scaled interactions (unlike P6's 0.000)
```
