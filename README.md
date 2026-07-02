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

**Updating the site:** bump the `V` version constant near the top of the script in `combined_dashboard.html`
whenever content changes — it cache-busts the framed sub-pages so visitors' browsers fetch the new versions
(GitHub Pages' own CDN cache clears within ~10 minutes).

## The models (also openable individually)
- `all_in_model.html` — whole academic pay bill (non-professorial + professorial), per university, with a
  **mix-and-match** tab (one university's grades + another's professoriate), jobs vs the ~150 proposed cuts, plus
  **Summary** and **Sources** tabs.
- `payscale_dashboard.html` — the three non-professorial grades on the common spine, and a cost comparison.
- `career_cost_model.html` — a representative career age 28→professor (fast/middle/slow promotion) and its cost.
- `professorial_model.html` — the professoriate (2-yearly discretionary increments), thirteen institutions.
- `transition_model.html` — how any change would phase in with **no pay cuts** (grandfathering; savings from
  earlier topping-out and lower promotion/entry).
- `monte_carlo.html` — varies the uncertain assumptions (promotion pace, contribution uptake, SL/AP split,
  professorial award rate) 5,000 times across the whole all-in model to give a sensitivity range — surfaced in the
  combined dashboard as **"How sure can we be?"**.

In the combined dashboard, **Mix & match** and **Sources** are top-level tabs (drawn from the all-in model).

## Data
- `national_spine.csv` — verified UCU/UCEA national spine, 2025-26 (+ provisional 2026-27 = +2%).
- `grades.csv`, `grades.json` — each institution's grade structure (normal increment + contribution points).
- `cost_model_results.csv` — non-professorial cost results across scenarios/workforces.
- `sources/` — every published pay scale used (PDF/xlsx), incl. `sources/professorial/`; raw HESA tables.
  (`payscales.xlsx`, the original working spreadsheet, is kept locally but not published in this repo.)

## Staffing (HESA, 2024/25, Table 17)
Exeter's **full-time** academic staff (headcount, not FTE) by salary band mapped to grades (39–52k = Lecturer;
52–70k = SL & AP; 70k+ = professor): E&R (Education & Research) = 750 non-professorial + 470 professors;
E&R + teaching-only = 1,155 + 500; professoriate (all functions) = 510. Part-time staff and research-only staff
are outside the modelled population (~1,655 of Exeter's 2,490 full-time academic staff are modelled).

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
reduced grant co-funding for the externally-funded majority. A rough bound: 545 of the 780 full-time research-only staff
sit in the Lecturer/SL salary bands the model can price; running just those through the same comparison adds roughly
**£2m/yr vs the mean and £4m/yr vs the cheapest structure** (salary only; ~£3–5m with on-costs). The remaining 230 sit on
the research grade below Lecturer, for which peers' scales are not yet collected. Because external funders pay most research
salaries, only part of this would reach Exeter's core budget — flagged as scale, not counted in the headline.

## Important — these are indicative figures
They rest on reasoned assumptions (promotion pace, contribution-point uptake, the 50/50 SL/AP split,
professorial award rates, and an approximate salary-band→grade mapping) for which there is limited hard
sector data. Use them as a **yardstick for the order of magnitude** and to test whether conclusions survive
plausible changes in assumptions — not as precise accounting. Excludes transition/redundancy costs and second-order effects.

## Headline (current data, E&R + teaching, middle assumptions)
On these central assumptions Exeter's modelled all-in academic pay bill ≈ £106m sits at the top of the **thirteen whole
systems** modelled. Holding the workforce fixed and changing only the structure, the modelled difference is — **vs the
Russell Group median structure, the principal benchmark: ≈ 89–105 average-salary-post equivalents across the fast→slow
promotion assumptions (≈ 97 central; ≈ £6.2m/yr in salary, ≈ £8.1m with on-costs)**. A recurring saving of that size roughly **doubles Exeter's 2024/25 operating margin — with no severance
bill** — and it is **convergence with the middle of the peer group, not a race to the bottom** (the floor is the nationally
negotiated spine; half the modelled peers already operate at or below the median). Secondary comparators: vs the mean of
the thirteen ≈ 78–91 (≈ 85 central); vs the lowest (Nottingham) ≈ 125–145 (≈ 134 central); vs the cheapest mix ≈ 152 central
(a bound, not a proposal). These are equivalences for scale (£ ÷ average salary), not
predicted savings or job counts — provided only so the magnitudes can be compared with the **~150 full-time posts** the
June 2026 consultation proposes to cut. Three qualifications travel with these numbers: a structural change **phases in
over roughly five years** (see the transition model); it saves mostly by **paying future hires less**, not by freeing cash
this year; and the modelled population is **full-time staff in the main academic grades** — research-only, part-time
and professional-services staff are not counted, so these are **minimum** estimates of the structural difference.
Indicative.

**Calibration:** with on-costs the modelled bill is ≈£137m — about 35% of the £396.6m total staff costs in Exeter's
2024/25 Annual Report, with the other ~65% being exactly the groups the model excludes (professional services,
research-only, part-time, sub-Lecturer grades, non-salary staff costs). For scale, the structural difference
(≈£5–9m/yr salary, ≈£7–11m/yr with on-costs) is of the same order as Exeter's entire 2024/25 operating surplus
(£8.2m, down from £22.5m — the operating line, not the headline surplus, which was distorted by a one-off pension
provision release in the prior year).

## Which universities are included
The active comparison is **Russell Group** universities in England and Wales on the national pay spine, with available data:
**14 non-professorial structures, 13 professorial, 13 modelled as a whole pay bill.** **Kept in the data but out of the comparison:** the
**Scottish** universities (Edinburgh, Glasgow, Aberdeen — different student-funding model) and **non-Russell-Group comparators**
(Bath; Aberdeen is also Scottish) — retained in `grades.json`/`grades.csv` for transparency. **Excluded by design:** Oxford,
Cambridge, the London institutions (incl. UCL) and Northern Ireland (distinct labour markets / cost bases). Sheffield is on its
**current (Aug 2025)** grade and professorial scales; Durham professorial rungs are interpolated from published bands; Liverpool
professorial pay is not modelled (its published scale is incomplete). Newcastle is modelled on its published IB Professor
scale (spine 53–57) — a short ladder that may understate professorial pay if a professorial zone exists above it.
Manchester's academic grades are 6/7/8 (Lecturer = Grade 6), with the professoriate on Grade 9. York's
professorial Band 2 rungs are interpolated from its published min/max, and its Band 1 increments are automatic (which the
discretionary-review model likely understates); Manchester's professoriate is modelled on Grade 9 zones 9E+9D, with zones
9C–9A excluded as Band-3 analogues.

## Help fill the gaps — and check it yourself
The comparison is only as good as its coverage, and this analysis has limitations. Two asks:

1. **Reuse the data.** The pay structures are provided in machine-readable form (`grades.json`, `grades.csv`, `national_spine.csv`,
   `cost_model_results.csv`) precisely so others can re-run, challenge or extend the analysis rather than take it on trust.
   Corrections and alternative approaches are welcome (open an issue or PR).
2. **Send missing scales.** Most useful: the **professorial** scale for **Liverpool** (we have its main grades but not its professorial bands) —
   and corrections or updates to any scale used here.
   Current published scales for any other institution are welcome too.
