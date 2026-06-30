# Academic pay structures — Russell Group & comparator universities

A like-for-like comparison of academic **pay structures**, built entirely from each university's own
**publicly published** pay scales. Every university is on the same nationally-negotiated pay spine, so a given
spine point pays the same salary everywhere — only the *structure* (grade lengths, entry points, overlaps)
differs. To compare structures fairly, one fixed workforce (Exeter's) is applied to each, so nothing about
individuals changes — only the design of the scale.

This is public data and a comparison, **not a verdict**. It makes no claim that anyone is overpaid and takes
no view on how any university should respond. Whether a higher- or lower-than-sector structure justifies
redundancies — or whether budget pressure should be met structurally, through redundancy, or elsewhere, and at
which levels — is for management and the recognised unions to weigh together. Academic pay also cannot be judged
in isolation: executive and senior-management remuneration warrants equal scrutiny (not compiled here).

## Start here
Live site: **https://leifuss.github.io/exeter-staff-cuts/** (served via GitHub Pages).

Or open **`combined_dashboard.html`** locally — it holds all six models as tabs, plus an Overview and a Sources tab.
Keep the whole folder together (the dashboards load each other in frames and link to `sources/`).

## The models (also openable individually)
- `all_in_model.html` — whole academic pay bill (non-professorial + professorial), per university, with a
  **mix-and-match** tab (one university's grades + another's professoriate), jobs vs the ~125 cuts, plus
  **Summary** and **Sources** tabs.
- `payscale_dashboard.html` — the three non-professorial grades on the common spine, and a cost comparison.
- `career_cost_model.html` — a representative career age 28→professor (fast/middle/slow promotion) and its cost.
- `professorial_model.html` — the professoriate (2-yearly discretionary increments), ten institutions.
- `transition_model.html` — how any change would phase in with **no pay cuts** (grandfathering; savings from
  earlier topping-out and lower promotion/entry).
- `monte_carlo.html` — varies the uncertain assumptions thousands of times to give a sensitivity range
  (kept in the repo but not currently surfaced in the combined dashboard).

In the combined dashboard, **Mix & match** and **Sources** are top-level tabs (drawn from the all-in model).

## Data
- `national_spine.csv` — verified UCU/UCEA national spine, 2025-26 (+ provisional 2026-27 = +2%).
- `grades.csv`, `grades.json` — each institution's grade structure (normal increment + contribution points).
- `cost_model_results.csv` — non-professorial cost results across scenarios/workforces.
- `sources/` — every published pay scale used (PDF/xlsx), incl. `sources/professorial/`; raw HESA tables.
  (`payscales.xlsx`, the original working spreadsheet, is kept locally but not published in this repo.)

## Staffing (HESA, 2024/25, Table 17)
Exeter's workforce by salary band mapped to grades (39–52k = Lecturer; 52–70k = SL & AP; 70k+ = professor):
E&R = 750 non-professorial + 470 professors; E&R + teaching-only = 1,155 + 500; professoriate (all functions) = 510.

## What drives the difference
The gap is driven, in descending order, by: **grade entry points** (Exeter's Lecturer grade starts at spine point 34 vs
27–32 for most peers — the single biggest lever); **grade length** (Exeter's short 3/5/3-increment grades top out fast and
park staff at the ceiling, where longer grades keep them climbing); the **contribution-point tail** above each ceiling
(Warwick has none); and **ceiling height / overlap**. Gaps in the spine don't save money — they slightly raise it by
accelerating progression. The cleanest lever is lower entry points and longer lower grades, which touch no current staff.
Note this largely means paying *new* staff less at given stages — a recruitment trade-off, not a free saving.

## Research-only staff (not modelled)
The models cover the three academic grades plus the professoriate, not research-only staff (research associates/fellows, who
sit on the grade below Lecturer). Likely **additional** savings exist there — direct for internally-funded posts, and as
reduced grant co-funding for the externally-funded majority — but quantifying needs the internal/external split, funder mix,
and research-grade scales. Flagged, not counted in the headline.

## Important — these are indicative figures
They rest on reasoned assumptions (promotion pace, contribution-point uptake, the 50/50 SL/AP split,
professorial award rates, and an approximate salary-band→grade mapping) for which there is limited hard
sector data. Use them as a **yardstick for the order of magnitude** and to test whether conclusions survive
plausible changes in assumptions — not as precise accounting. Birmingham's professorial scale is uprated
from 2021. Excludes transition/redundancy costs and second-order effects.

## Headline (current data, E&R + teaching, middle assumptions)
On these central assumptions Exeter's modelled all-in academic pay bill ≈ £106m sits at the top of the **ten whole systems**
modelled. Holding the workforce fixed and changing only the structure, the modelled difference is: vs the mean of the ten
≈ 82 average-salary-post equivalents; vs the lowest (Nottingham) ≈ 134; vs the cheapest mix ≈ 152 (more at the cheaper
structures' own pay). These are equivalences for scale (£ ÷ average salary), not predicted savings or job counts — provided
only so the magnitudes can be compared with the ~125 posts announced. Indicative.

## Which universities are included
The active comparison is **Russell Group** universities in England and Wales on the national pay spine, with available data:
**12 non-professorial structures, 10 also modelled as a whole pay bill.** **Kept in the data but out of the comparison:** the
**Scottish** universities (Edinburgh, Glasgow, Aberdeen — different student-funding model) and **non-Russell-Group comparators**
(Bath; Aberdeen is also Scottish) — retained in `grades.json`/`grades.csv` for transparency. **Excluded by design:** Oxford,
Cambridge, the London institutions (incl. UCL) and Northern Ireland (distinct labour markets / cost bases). Sheffield is on its
**current (Aug 2025)** grade and professorial scales; Durham professorial rungs are interpolated from published bands; Liverpool
professorial pay is not modelled (its published scale is incomplete).

## Help fill the gaps — and check it yourself
The comparison is only as good as its coverage, and this analysis has limitations. Two asks:

1. **Reuse the data.** The pay structures are provided in machine-readable form (`grades.json`, `grades.csv`, `national_spine.csv`,
   `cost_model_results.csv`) precisely so others can re-run, challenge or extend the analysis rather than take it on trust.
   Corrections and alternative approaches are welcome (open an issue or PR).
2. **Send missing scales.** Most useful: the Russell Group members not yet covered — especially **Newcastle** and **Manchester** —
   and the **professorial** scales for **York and Liverpool** (we have their main grades but not their professorial bands).
   Current published scales for any other institution are welcome too.
