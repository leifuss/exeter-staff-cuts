#!/usr/bin/env python3
"""Extract the "£100,000+ staff" note from university financial-statement PDFs.

Why: every UK HE provider's annual accounts include a note (usually titled
"Remuneration of higher-paid staff" / "Employees earning £100,000 or more")
listing headcount by salary band. Those PDFs are 100+ pages; this pulls out
ONLY the page(s) that carry that note, so the small band table can be read
without loading the whole document into context.

Usage:
  1. Drop each comparator's 2024/25 accounts (financial year ENDING 31 July 2025)
     into this folder as  <university>.pdf   e.g.  bristol.pdf, leeds.pdf ...
  2. Run:  python3 sources/highpay/extract_highpay.py
  3. It writes the matched pages to  highpay_extract.txt  and prints a one-line
     summary per file (page numbers found, whether band figures are present).

Then the band tables are transcribed into highpay.html's per-university data.
"""
import re, glob, os
from pypdf import PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
# keywords that flag the high-pay note (formats vary a lot across providers)
KEYS = re.compile(r'100,000|higher[- ]paid|remuneration of (?:higher|staff|employees)'
                  r'|fell within the following|basic salary.{0,40}band'
                  # also grab the staff-numbers note, for the per-1,000-staff denominator
                  r'|average staff number|staff numbers by|full[- ]time equivalent staff number', re.I)
# a salary band figure like 100,000 / 105,000 / £110,000 ... up to ~£300k
BAND = re.compile(r'£?\s*[12][0-9]{2},000')

def extract(path):
    name = os.path.basename(path)
    try:
        reader = PdfReader(path)
    except Exception as e:
        return name, f"[!] could not open ({e})", ""
    pages_out, hit_pages, band_count = [], [], 0
    for i, pg in enumerate(reader.pages):
        try:
            t = pg.extract_text() or ""
        except Exception:
            t = ""
        if KEYS.search(t):
            hit_pages.append(i + 1)
            band_count += len(BAND.findall(t))
            keep = "\n".join(l for l in t.splitlines() if l.strip())
            pages_out.append(f"--- {name} page {i+1} ---\n{keep}\n")
    if not hit_pages:
        return name, "NO high-pay note found — open manually and search '100,000'", ""
    return name, f"pages {hit_pages}  ({band_count} band figures seen)", "\n".join(pages_out)

def main():
    pdfs = sorted(glob.glob(os.path.join(HERE, "*.pdf")))
    if not pdfs:
        print("No PDFs in", HERE, "— drop <university>.pdf files here first.")
        return
    out = []
    print(f"{'file':22} result")
    print("-" * 60)
    for p in pdfs:
        name, summary, text = extract(p)
        print(f"{name:22} {summary}")
        if text:
            out.append(text)
    dest = os.path.join(HERE, "highpay_extract.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("\nMatched pages written to", dest)

if __name__ == "__main__":
    main()
