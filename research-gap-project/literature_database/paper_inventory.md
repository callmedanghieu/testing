# Phase 1: Paper Inventory

Five PDFs were reviewed in full. The text was extracted page by page (`papers/text/*.txt`, with `===== PAGE n =====` markers). Tables that are images (Paper 1, Tables 1–8) and the decisive tables of Papers 3 and 5 were checked against the rendered pages.

**Citation format:** `[PDF p.X / p.Y]` means page X of the PDF file and printed journal page Y. See `source_traceability/page_mapping.md`.

The machine-readable versions are `literature_database.json` and `literature_matrix.csv`, both generated from `build_database.py`.

---

## P1: Lê Thị Nhung (2024)

| Field | Content |
|---|---|
| File | `206fdb74-187-b5pdf-1711106205.pdf` (13 pp.; PDF pp.1–2 are the issue's table of contents) |
| Title | *Công bố thông tin trách nhiệm xã hội và chi phí vốn cổ phần: bằng chứng thực nghiệm từ các doanh nghiệp Việt Nam* (CSR Disclosure and Cost of Equity Capital: Empirical Evidence from Vietnamese Enterprises) |
| Author | Lê Thị Nhung, Academy of Policy and Development |
| Year / Source | 2024; *Tạp chí Khoa học Thương mại* (Journal of Trade Science) No. 187, pp. 61–71 |
| DOI | 10.54404/JTS.2024.187V.05 [PDF p.3 / p.61] |
| Topic | CSR disclosure → cost of equity |
| Research question | Does the level of CSR disclosure reduce the cost of equity of Vietnamese listed firms? [PDF p.4 / p.62] |
| Abstract | 93 VNR500 listed firms, 2014–2021, panel estimation; CAPM COE; content-analysis CSR index; better CSR disclosure means lower COE [PDF p.3 / p.61] |
| Keywords / JEL | disclosure, cost of equity, social responsibility; G30, G32 |
| Theory | Disclosure–cost-of-capital theory via three channels: liquidity, estimation risk, and public vs private information [PDF p.5 / p.63]. Presents the CSR risk-reduction view against the CSR over-investment/agency-cost view [PDF p.4–5 / p.62–63] but does not test one against the other |
| Hypothesis | H1: CSR disclosure is negatively related to COE [PDF p.6 / p.64] |
| Data source | Annual/SD/CSR reports (hand-coded); prices, VNINDEX and 1-year bond yields from Investing.com [PDF p.6 / p.64] |
| Sample | 93 of the VNR500-2021 firms on HOSE/HNX, excluding finance/banking; 744 firm-years [PDF p.6 / p.64] |
| Country / industry / period | Vietnam / non-financial, multi-industry / 2014–2021 |
| DV | CAPM COE: Rf = 1-year bond, annual beta, MRP = 2014–2021 average [PDF p.6–7 / p.64–65] |
| IV | CSRI: 33 binary items from Circular 155/2015 (environment 18, labour 10, community 5) [Table 1, PDF p.7 / p.65] |
| Moderators / mediators | None |
| Controls | GROWTH, SIZE, LEV, BTM [Table 2, PDF p.8 / p.66] |
| Method | Pooled OLS / FEM / REM → Hausman p=0.0002 → FEM → GLS [Tables 6–8, PDF p.10–11 / p.68–69] |
| Main findings | CSRI −6.012***; SIZE −2.230*; LEV +0.795***; BTM +2.134** [Table 8, PDF p.11 / p.69] |
| Robustness | None |
| Limitations (explicit) | Aggregate effect only [PDF p.13 / p.71] |
| Future research | CSR dimensions [PDF p.13 / p.71] |
| Reviewer flags | See `limitations/evidence_quality_audit.md`: SDs larger than the variables' ranges, diagnostic p-values that contradict the text, unlabelled parentheses, FEM coefficient never reported |

## P2: Nguyen & Duong (2026)

| Field | Content |
|---|---|
| File | `ef2e1594-…Vietnam-s-listed.pdf` (25 pp.) |
| Title | The impact of sustainability reporting on the cost of capital: evidence from Vietnam's listed companies |
| Authors | Huu Cuong Nguyen; Hien Khanh Duong (University of Economics, University of Da Nang) |
| Year / Source | 2026 (received Sep 2024, accepted Jan 2025); *Journal of Financial Reporting and Accounting* 24(3), 1256–1280 |
| DOI | 10.1108/JFRA-09-2024-0642 |
| Research questions | RQ1–RQ3: effect of SD disclosure on COD, COE and WACC [PDF p.3 / p.1258] |
| Theory | Agency, signalling (called "most foundational"), resource dependence, legitimacy, stakeholder, institutional [PDF p.4–5 / p.1259–1260] |
| Hypotheses | H1 (COE −), H2 (COD −), H3 (WACC −) [PDF p.5–6 / p.1260–1261] |
| Data | Hand-coded reports; Vietstock beta and MRP; MoF bond yields [PDF p.6–7 / p.1261–1262] |
| Sample | Top-100 firms by market cap at 31 Dec 2023, 2021–2023, 300 firm-years [PDF p.6 / p.1261] |
| DV | COE (CAPM, 10-year Rf); COD = interest/total liabilities; WACC [PDF p.7–8 / p.1262–1263] |
| IV | SDG: 77 binary GRI-2016 items; E/Ec/S sub-indices [PDF p.8 / p.1263; Table 6] |
| Controls | FSIZE, LEV, TobinQ, CASH, ROA, AGE, GOV, IND (ESI), COVID (=2021) [Table 1, PDF p.9 / p.1264] |
| Method | OLS / FEM / REM → GLS [PDF p.7 / p.1262] |
| Main findings | COE GLS −0.070**, FEM −0.138*; COD GLS −0.029*; WACC GLS −0.033***, FEM n.s. [Tables 3–5]; environment sub-index strongest [Table 6, PDF p.15 / p.1270] |
| Robustness | Dimension decomposition only |
| Limitations (explicit) | Scoring consistency; crude COD; no lags [PDF p.16 / p.1271] |
| Future research | Longer period, broader sample, endogeneity, lags, alternative COE, actual loan rates [PDF p.16 / p.1271]; religion, gender [PDF p.17 / p.1272] |

## P3: Bùi Thị An Bình et al. (2025)

| Field | Content |
|---|---|
| File | `5fd254be-uffile-upload-no-title32076.pdf` (9 pp.) |
| Title | *Tác động của công bố thông tin phát triển bền vững tới chi phí sử dụng vốn chủ sở hữu của các doanh nghiệp công nghiệp năng lượng trên TTCK Việt Nam* |
| Authors | Bùi Thị An Bình, Nguyễn Thị Thùy Dương, Lê Thị Kiều Linh, Nguyễn Bá Đức Mạnh, Nguyễn Huyền Thương (National Economics University) |
| Year / Source | 2025; *HaUI Journal of Science and Technology* 61(6), 138–146 |
| DOI | 10.57001/huih5804.2025.229 |
| Theory | Legitimacy, stakeholder [PDF p.3 / p.140]; Diamond–Verrecchia liquidity [PDF p.2 / p.139] |
| Hypothesis | H1: SD disclosure → COE negative [PDF p.4 / p.141] |
| Sample | 58 energy firms (HOSE/HNX/UPCOM), 2019–2023, 290 obs [PDF p.5 / p.142] |
| DV / IV | CAPM COE (10-year Rf from Damodaran) / 77-item GRI index (15 items overlap Circular 155) [PDF p.4 / p.141] |
| Controls | SIZE, ROE, board size, Big4, LEV |
| Method | OLS, REM, FEM; Hausman → FEM; robust/GMM claimed [PDF p.5–7 / p.142–144] |
| Main finding | Claimed positive effect; OLS +10.98***, REM +10.23**, **FEM +4.79, p=0.452** [Table 3, PDF p.6 / p.143] |
| Explanation offered | Short-run compliance costs; disclosure reveals risk [PDF p.7 / p.144] |
| Future research | Other industries; DGM-based COE; cost of debt [PDF p.8 / p.145] |

## P4: Vu & Pham (2023)

| Field | Content |
|---|---|
| File | `8922477b-IJRPR20495.pdf` (11 pp.) |
| Title | Research on the Impact of Governance Structure on the Cost of Equity Capital of Food Businesses Listed on the Vietnam Stock Market |
| Authors | Thuy Thi Thanh Vu; Thuy Thi Pham (University of Labour and Social Affairs) |
| Year / Source | 2023; *Int. J. of Research Publication and Reviews* 4(12), 3085–3095 |
| DOI | 10.55248/gengpi.4.1223.123524 |
| Theory | Agency vs stewardship ("management theory") [PDF p.9–10 / p.3093–3094] |
| Sample | 55 food firms, 2015–2022, 440 obs described, 341 used [PDF p.2, 9 / p.3086, 3093] |
| DV | CAPM COE, rolling 12-month beta; PEG rejected because expected EPS is unavailable in Vietnam [PDF p.3 / p.3087] |
| IVs | Board size, independence, DUAL, tenure, meetings, remuneration/nomination committee |
| Method | OLS/REM/FEM → FE with clustered SE [PDF p.8–9 / p.3092–3093] |
| Main findings | Board size −0.064 (p=0.065), committee −0.455 (p=0.083), DUAL +0.215 (p=0.077); others n.s. [Table 8] |
| Limitations / future research | None stated |

## P5: Le, Nguyen & Le (2019)

| Field | Content |
|---|---|
| File | `8a8e6b0c-The_impact_of_corporate_social_responsibility_on_t.pdf` (11 pp.; PDF p.1 is a cover sheet) |
| Title | The impact of corporate social responsibility on the cost of equity: an analysis of Vietnamese listed companies |
| Authors | Xuan Quynh Le; Ngoc Tien Nguyen; Thy Ha Van Le (Quy Nhon University) |
| Year / Source | 2019; *Investment Management and Financial Innovations* 16(3), 87–96 |
| DOI | 10.21511/imfi.16(3).2019.09 |
| Theory | No formal framework; information/social-contract role of disclosure [PDF p.3 / p.88] |
| Sample | 115 non-financial firms, 2014–2017, 460 obs [PDF p.5 / p.90] |
| DV | Ex-ante COE = forecast EPS(t+1)/price after report release [PDF p.6 / p.91] |
| IV | Environmental disclosure index (GRI G4, binary) [PDF p.6 / p.91] |
| Controls | SIZE, LEV, EPS growth, LIQUID, SOE %, FOR %, BETA [Table 3, PDF p.7 / p.92] |
| Method | REM/FEM → Hausman → FEM → XTSCC [PDF p.8–9 / p.93–94] |
| Main finding | FEM −45.17 (t=−1.16) becomes −45.17*** (t=−6.93) under XTSCC [Tables 6–7] |
| Limitations (explicit) | Small sample, non-financial only, GRI not suited to Vietnam [PDF p.10 / p.95] |
| Future research | Circular-155-based index [PDF p.10 / p.95] (P1 later builds one) |

---
---

# Batch 2 Inventory (added; Batch 1 entries above unchanged)

Five files were received in Batch 2. **Four are new papers (P6–P9). One is a duplicate of P5:** `0f2c53f6-IMFI_2019_03_Le.pdf` has identical whitespace-normalised text except one added Web of Science link on the cover sheet. It is logged in `literature_database.json → duplicate_files` and not counted.

Page maps:
- P6: printed = PDF + 1383.
- P7: printed = PDF + 63.
- P8: no printed pages (online-first), cite PDF pages.
- P9: printed = PDF + 138.

Minus signs were lost in the text extraction of P6 and P8 tables, so their coefficient signs were **verified on the rendered pages**.

## P6: Thuy, Khuong, Canh & Liem (2022)

| Field | Content |
|---|---|
| File | `c9acc018-thuy2022.pdf` (12 pp.) |
| Title | The mediating effect of stock price crash risk on the relationship between CSR and cost of equity moderated by state ownership: Moderated-mediation analysis |
| Authors | Cao Thi Mien Thuy, Nguyen Vinh Khuong, Nguyen Thi Canh, Nguyen Thanh Liem (UEL, VNU-HCM) |
| Year / Source | 2022; *Corporate Social Responsibility and Environmental Management* 29(5), 1384–1395 |
| DOI | 10.1002/csr.2276 |
| Research question | Does crash risk mediate, and does state ownership moderate, CSR disclosure → COE? [PDF p.2 / p.1385] |
| Theory | Information asymmetry; CSR as risk management (idiosyncratic and crash risk); investor base; SOE multitask vs inefficiency [PDF p.2–3 / p.1385–1386] |
| Hypotheses | H1 CSRD → COE (−); H2 crash risk mediates; H3 the negative effect is stronger with higher state ownership [PDF p.3–4 / p.1386–1387] |
| Data / sample | 225 non-financial firms with CSR data 2014–2019, 1,340 firm-years (GMM N=816); Refinitiv Eikon [PDF p.4 / p.1387] |
| DV | **Implied COE**: Easton (2004) with Harris & Wang (2013) cross-sectional earnings forecasts [PDF p.4 / p.1387; App. A] |
| IV | CSRD: 33 GRI-2016 criteria (6 Ec / 8 E / 19 S) [PDF p.5 / p.1388] |
| Mediator / moderator | CRASH (DUVOL) / SOE % (mean-centred interaction) |
| Controls | SIZE, LEV, TANG, ROA, GROW, AGE, industry dummies (no year effects reported) |
| Method | **System GMM**; Baron–Kenny; Sobel / delta / Monte Carlo [PDF p.5–8 / p.1388–1391] |
| Main findings | CSRD −0.065*** [Table 2]; CSRD → CRASH −0.204***; CRASH → COE +0.142***; Sobel indirect −0.006 (p=0.029) [Tables 3–4]; SOE × CSRD +0.000*** [Table 5] |
| Limitations (explicit) | One developing market, non-financial only [PDF p.10 / p.1393] |
| Future research | Other developing countries; SOEs in high-polluting industries; cross-national [PDF p.10 / p.1393] |
| Reviewer flags | Abstract says SOE "strengthens" the effect, but the table shows attenuation; mediation arithmetic inconsistent; coefficients printed as 0.000 (see `limitations/evidence_quality_audit.md`) |

## P7: Nguyen & Nguyen (2017)

| Field | Content |
|---|---|
| File | `1b16cfff-12231-42481-1-SM.pdf` (7 pp.) |
| Title | Impact of Corporate Disclosure on Cost of Equity Capital in Vietnam |
| Authors | Dung Viet Nguyen; Lan Thi Ngoc Nguyen (Foreign Trade University) |
| Year / Source | 2017; *International Journal of Financial Research* 8(4), 64–70 |
| DOI | 10.5430/ijfr.v8n4p64 |
| Theory | Three disclosure–CoC channels: adverse selection, estimation risk, public/private information [PDF p.1–2 / p.64–65] |
| Sample | 225 non-financial HOSE firms, FY2015 cross-section; FiinPro [PDF p.4 / p.67] |
| DV | **Implied COE**: residual-income model, 2-year horizon, self-generated forecasts [PDF p.3–4 / p.66–67] |
| IV | Botosan (1997) annual-report disclosure score (105 points) — **general, not CSR, disclosure** |
| Controls | Beta, P/B, ln market cap |
| Method | Cross-sectional OLS, White SE; stepwise and rank regressions [PDF p.5–6 / p.68–69] |
| Main findings | DSCORE −0.0016*** (t=−4.33); beta n.s.; size + [Table 3]; rank regression confirms [Table 4] |
| Key argument | CAPM cannot test a disclosure effect: if the model's factors exclude information risk, there is no reason to link its expected returns to disclosure [PDF p.3 / p.66] |
| Limitations / future research | None stated |

## P8: Srivastava, Das & Pattanayak (2019)

| Field | Content |
|---|---|
| File | `f57fe841-srivastava2019.pdf` (21 pp.) |
| Title | Impact of corporate governance attributes on cost of equity: Evidence from an emerging economy |
| Authors | Varnita Srivastava; Niladri Das; Jamini Kanta Pattanayak |
| Year / Source | 2019; *Managerial Auditing Journal* (online-first) |
| DOI | 10.1108/MAJ-01-2018-1770 |
| Country | **India** (first non-Vietnamese paper in the corpus) |
| Theory | Agency; law and finance [PDF p.2–3, 7] |
| Hypothesis | H1: governance → COE (−) [PDF p.7] |
| Sample | 319 non-financial S&P BSE 500 firms, 2001–2016, 5,104 firm-years; ProwessIQ; interpolation of missing data [PDF p.8] |
| DV | COE (%), **construction never described** |
| IV | CGI: 43 binary items scored 1 only when **above the mandatory minimum**; 7 sub-indices [PDF p.9, 11–13] |
| Method | Pooled OLS (after Hausman and BP-LM) [PDF p.15] |
| Main findings | CGI −0.089 (p=0.021); board composition −0.068; audit committee −0.061; ownership structure −0.130 [Table III, PDF p.15] |
| Limitations | None stated. Future research: other valuation measures [PDF p.18] |

## P9: Shah & Butt (2009)

| Field | Content |
|---|---|
| File | `a7eaed52-6_Zulfiqar_Shah2.pdf` (33 pp.; PDF metadata title is wrong) |
| Title | The Impact of Corporate Governance on the Cost of Equity: Empirical Evidence from Pakistani Listed Companies |
| Authors | Syed Zulfiqar Ali Shah; Safdar Ali Butt |
| Year / Source | 2009; *Lahore Journal of Economics* 14(1), 139–171 (cited by P4 and P8) |
| Country | **Pakistan** |
| Theory | Agency; signalling of investor protection; investor-protection substitution/complementarity (Klapper & Love; Chen et al. 2004) [PDF p.4–8 / p.142–146] |
| Sample | 114 non-financial KSE firms, 2003–2007 (57 textile) [PDF p.9 / p.147] |
| DV | CAPM COE, 2-year monthly beta [PDF p.11 / p.149] |
| IV | Ownership concentration, managerial ownership, board independence, audit committee independence, board size; weighted CGS [App. B] |
| Method | OLS; industry-dummy and industry+year-dummy LSDV [PDF p.12–22 / p.150–160] |
| Main findings | Only size robustly negative; board size −0.017 (p≈0.09); **CGS positive, n.s.** (p=0.85–0.91) [Tables 4–10] |
| Limitations (explicit) | Governance score limited by data [PDF p.25 / p.163] |
| Future research | More governance variables; other Ke models [PDF p.25 / p.163] |
