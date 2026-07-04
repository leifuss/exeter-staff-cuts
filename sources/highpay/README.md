# Comparator high-pay data — drop accounts here

To extend the **High pay** tab from Exeter-only to a peer comparison, we need each
comparator's disclosure of staff earning **£100,000+** (by salary band), which every
UK university publishes in its annual accounts under "Remuneration of higher-paid staff".

**This session cannot download the PDFs** (the environment's egress policy blocks
outbound fetching to university sites). So the workflow is:

1. **Download** each university's *Annual Report and Financial Statements* for the
   financial year **ending 31 July 2025** (the "2024/25" year — the most recent). See
   `urls.md` for the located links.
2. **Save** each into this folder as `<university>.pdf` — lowercase, no spaces:
   `bristol.pdf`, `leeds.pdf`, `cardiff.pdf`, `birmingham.pdf`, `york.pdf`,
   `warwick.pdf`, `nottingham.pdf`, `southampton.pdf`, `liverpool.pdf`, `durham.pdf`,
   `manchester.pdf`, `newcastle.pdf`, `sheffield.pdf`. (Exeter is already in the data.)
3. **Run** `python3 sources/highpay/extract_highpay.py` — it pulls out only the page(s)
   carrying the £100k+ note into `highpay_extract.txt`, so the band tables can be
   transcribed without wading through 100-page PDFs.

The transcribed band tables then feed a per-university comparison in `highpay.html`.

**Normaliser:** raw £100k+ counts aren't comparable across universities of different
size, so the comparison will express them as **£100k+ staff per 1,000 academic (or
total) staff** as well as raw counts — the academic-staff denominator comes from the
same accounts (the "staff numbers" / average FTE note) or HESA.

The PDFs themselves are large and need not be committed; only the extracted tables and
the resulting data matter. Add them to `.gitignore` if you prefer to keep them local.
