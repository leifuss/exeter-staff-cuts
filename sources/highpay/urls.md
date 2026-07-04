# Comparator 2024/25 accounts — located download links

Financial year **ending 31 July 2025** (the "2024/25" year — most recent published).
Save each as `<university>.pdf` in this folder, then run `extract_highpay.py`.
Confidence flags are from a web search only — the links were **not** fetch-verified in
this environment (outbound fetching is blocked), so confirm each opens the right document.

| University | Confidence | Link |
|---|---|---|
| Bristol | high | https://www.bristol.ac.uk/media-library/sites/finance/documents/UoB_ARFS2025_WEB.pdf |
| Leeds | high | https://www.leeds.ac.uk/download/downloads/id/3533/annual-report-and-accounts-2024-25.pdf |
| Cardiff | high | https://www.cardiff.ac.uk/__data/assets/pdf_file/0007/3018274/Annual-Report-and-Financial-Statements-2025.pdf |
| Birmingham | high | https://www.birmingham.ac.uk/documents/finance/uob-annual-report-and-accounts-2024-25.pdf |
| York | high | https://www.york.ac.uk/media/staffhome/marketing/corporatepublications/2025-Annual-Report-and-Financial-Statements.pdf |
| Warwick | medium | https://warwick.ac.uk/services/finance/resources/accounts/accounts2425_-_with_cover.pdf |
| Nottingham | high | https://www.nottingham.ac.uk/fabs/finance/documents/financialstatements/2025-university-of-nottingham-report-accounts-signed.pdf |
| Southampton | high | https://www.southampton.ac.uk/~assets/doc/finance/financial-statements-2024-25.pdf |
| Liverpool | high | https://www.liverpool.ac.uk/media/livacuk/finance/financial-statements-2024-2025.pdf |
| Durham | high | https://www.durham.ac.uk/media/durham-university/professional-services/finance-service/Annual-report-and-financial-statements-for-the-year-ended-31-July-2025-(PDF-version).pdf |
| Manchester | high | https://documents.manchester.ac.uk/display.aspx?DocID=78079 |
| Newcastle | high | https://www.ncl.ac.uk/mediav8/freedom-of-information/files/IAR-2425.pdf |
| Sheffield | low (landing page) | https://sheffield.ac.uk/finance/annual-report-financial-statements |

## Important: check the disclosure BASIS before comparing
UK providers do **not** all band the £100k+ note on the same basis. Exeter's table (the
one already in the tool) is "Remuneration of higher-paid staff, **excluding employer's
pension contributions** (except salary sacrifice), excluding the VC" — headcount **and**
FTE, sums to 404. Peers vary on: excl. vs incl. employer pension; basic salary vs total
remuneration; whether the VC is included; headcount vs FTE; and treatment of taxable
benefits. `extract_highpay.py` preserves each note's exact wording — record the stated
basis per university and only compare like-for-like, otherwise the comparison is
apples-to-oranges and would flatter or penalise Exeter purely on definition. (Also grab
each university's academic-staff FTE from the same accounts for the per-1,000 normaliser.)
