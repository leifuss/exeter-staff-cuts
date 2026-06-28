# Russell Group academic pay — Exeter cost models

Interactive models estimating how much of Exeter's academic pay bill is attributable to its **pay
structure** rather than to paying people more on the same national spine. Each model applies Exeter's own
workforce to other Russell Group universities' published pay structures, so the only thing that varies is
the system, not the people.

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
- `transition_model.html` — how savings phase in with **no pay cuts** (grandfathering; savings from earlier
  topping-out and lower promotion/entry).
- `monte_carlo.html` — varies the uncertain assumptions 5,000 times to give a credible range.

## Data
- `national_spine.csv` — verified UCU/UCEA national spine, 2025-26 (+ provisional 2026-27 = +2%).
- `grades.csv`, `grades.json` — each institution's grade structure (normal increment + contribution points).
- `cost_model_results.csv` — non-professorial cost results across scenarios/workforces.
- `sources/` — every published pay scale used (PDF/xlsx), incl. `sources/professorial/`; raw HESA tables.
- `payscales.xlsx` — original master spreadsheet.

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
Exeter's all-in academic pay bill ≈ £106m — the **most expensive of the 10 modelled systems**. (Scottish universities,
including the dearer Edinburgh, are excluded from the comparison; see below.) Holding the workforce fixed and changing only
the pay system would save, relative to: the mean of the 10 modelled systems ≈ 84 equivalent average-salary posts; the lowest
system (Nottingham) ≈ 134; the cheapest mix ≈ 154 (more at the cheaper structures' own pay) — of the same order as the
~125 posts being cut.

## Which universities are included
English and Welsh Russell Group universities on the national pay spine with available pay data (13 non-professorial structures,
10 also professorial). **Excluded by design:** Oxford, Cambridge and the London institutions (incl. UCL), and Northern Ireland
(distinct labour markets / cost bases); and the **Scottish universities (Edinburgh, Glasgow, Aberdeen)**, which operate under a
different student-funding model — their data is retained in `grades.json`/`grades.csv` but kept out of the comparison. Some other
Russell Group universities are omitted because pay data was not available. Sheffield is included on its **2004** grade architecture
(salaries above point 51 uprated/approximate); Durham professorial rungs are interpolated from published bands; Liverpool
professorial pay is not modelled (its published scale is incomplete).
