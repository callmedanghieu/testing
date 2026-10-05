# Page Mapping and Citation Convention

All citations in this workspace use **`[PDF p.X / p.Y]`**: page X of the PDF file and printed journal page Y. Where only one number is given (e.g. `[p.1265]`), it is the **printed** page.

| ID | Short cite | File | PDF pages | Printed = PDF + | Notes |
|---|---|---|---|---|---|
| P1 | Lê Thị Nhung (2024) | `206fdb74-187-b5pdf-1711106205.pdf` | 13 | 58 | PDF pp.1–2 = issue contents; article PDF pp.3–13 = pp.61–71. **Tables 1–8 are images** (visually verified) |
| P2 | Nguyen & Duong (2026) | `ef2e1594-…Vietnam-s-listed.pdf` | 25 | 1255 | Article pp.1256–1280 |
| P3 | Bùi et al. (2025) | `5fd254be-uffile-upload-no-title32076.pdf` | 9 | 137 | pp.138–146. The score formula is an image |
| P4 | Vu & Pham (2023) | `8922477b-IJRPR20495.pdf` | 11 | 3084 | pp.3085–3095. Tables 6–7 (Hausman, Wald) are images; values are restated in the text |
| P5 | Le, Nguyen & Le (2019) | `8a8e6b0c-The_impact_of_corporate_social_responsibility_on_t.pdf` | 11 | 85 | PDF p.1 = publisher cover sheet; pp.87–96 |

**Where to check a claim:** open `papers/text/<file>.txt` and search for `===== PAGE X =====`, or run `python3 verify_claims.py`.

**Page-level evidence unavailable:** none of the claims used in the gap analysis lacks a page reference. Statements about Vietnamese law (effective dates of Circular 155/2015 and Circular 96/2020), foreign-ownership limits, green-credit instruments and external econometric methods are **not in the corpus**. They are labelled "external, verify" wherever they appear.
