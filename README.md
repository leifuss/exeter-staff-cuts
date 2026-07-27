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

**Deploying:** the site is served by GitHub Pages from `main` via the Actions workflow in
`.github/workflows/deploy-pages.yml` (Settings → Pages → Source = "GitHub Actions"). The workflow uses
`concurrency: cancel-in-progress: true`, so a new deploy supersedes any stuck one rather than queuing behind it.
You can also trigger it manually from the Actions tab ("Deploy Pages" → "Run workflow"). To keep well under the
Pages build rate limit (~10/hour), batch several content changes into one merge rather than merging each separately.

**Updating the site:** bump the `V` version constant near the top of the script in `combined_dashboard.html`
whenever content changes — it cache-busts the framed sub-pages so visitors' browsers fetch the new versions
(GitHub Pages' own CDN cache clears within ~10 minutes).

## The models (also openable individually)
- `all_in_model.html` — whole academic pay bill (non-professorial + professorial), per university, with a
  **mix-and-match** tab (one university's grades + another's professoriate), jobs vs the ~150 proposed cuts, plus
  **Summary** and **Sources** tabs.
- `payscale_dashboard.html` — the three non-professorial grades on the common spine, and a cost comparison.
- `career_cost_model.html` — a representative career age 28→professor (fast/middle/slow promotion) and its cost.
- `professorial_model.html` — the professoriate, all fourteen institutions, modelled on each university's **documented
  progression mechanisms** (the default — several peers give automatic annual increments; Exeter's biennial merit review is
  among the slowest in the set, so Exeter ranks mid-pack here). A like-for-like uniform biennial baseline is kept in the code
  but no longer shown, pending validation against peers' £100k+ disclosures.
- `transition_model.html` — how any change would phase in with **no pay cuts** (grandfathering; savings from
  earlier topping-out and lower promotion/entry).
- `monte_carlo.html` — varies the uncertain assumptions (promotion pace, contribution uptake, SL/AP split,
  professorial award rate) 5,000 times across the whole all-in model to give a sensitivity range — surfaced in the
  combined dashboard as **"How sure can we be?"**.
- `flex_fte_model.html` — a **voluntary alternative lever**: incentivising higher-paid professors to move to part-time
  (e.g. 0.8 FTE) in exchange for a **guaranteed annual increment** (capped at the top of their band). Because £100k+ pay is
  heavily taxed (and the personal-allowance / childcare cliffs sit right in the professorial bulge), the **take-home cost to
  the professor is far smaller than the university's all-in saving** — a recurring, severance-free saving. Interactive: set
  salary, target FTE, band cap, children and take-up; all tax/NI/USS assumptions are editable. Illustrative and strictly voluntary.
- `highpay.html` — five years of the annual reports' **£100k+ staff** table (2019/20–2024/25): the raw count has
  tripled (135 → 404); against a pay-award-adjusted threshold the real growth is ≈30%, concentrated in 2023/24 —
  alongside severance and key-management-pay series from the same accounts.

In the combined dashboard, **Mix & match** and **Sources** are top-level tabs (drawn from the all-in model).

## Data
- `national_spine.csv` — verified UCU/UCEA national spine, 2025-26 (+ provisional 2026-27 = +2%).
- `grades.csv`, `grades.json` — each institution's grade structure (normal increment + contribution points).
- `cost_model_results.csv` — non-professorial cost results across scenarios/workforces.
- `sources/` — every published pay scale used (PDF/xlsx), incl. `sources/professorial/`; raw HESA tables; the
  University's Annual Reports 2020/21–2024/25 (used for the high-pay series and the calibration).
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
plausible changes in assumptions — not as precise accounting. Excludes transition/redundancy costs and second-order
effects.

**The non-professorial model has now been validated** against Exeter's actual distribution of staff across spine points
(2023, `ExeterSPdist.csv`). Two results: (a) the modelled **mean salary per grade matches the real distribution to within
1.3%** (Lecturer −0.0%, SL +1.1%, AP +1.3%), and the observed shape — progress up the normal points, then bunch at the
ceiling / first contribution point — is the mechanism the model assumes; (b) the **headline saving is robust**, landing
between **£4.7m and £4.9m/yr** across every combination of contribution-point and grade-mix assumption tested, with Exeter
the dearest structure in all of them. Two calibration notes fall out: contribution-point uptake is **not uniform** (actual
≈37% Lecturer, 13% SL, 10% AP vs the 30% assumed — the errors largely cancel), and the **50/50 SL:AP split is too
AP-heavy** (actual ≈3:1), which is what inflates the absolute bill below. Published figures keep the 50/50 split, so the
**£4.7m headline is the conservative end** of the validated range. **The per-head professorial cost ranking has been retired** as unreliable: calibrated against Exeter's own accounts,
the modelled progression assumption can put Exeter "below median" or "dearest" depending on an un-pin-downable rate (see
`docs/deprecated/professorial-ranking.md`). The professoriate is now described by evidence-backed facts, not a modelled ranking
(high floor; slower *documented* cadence; most £100k+ by headcount but upper-mid by FTE; growth mostly award-drift), with the one
concrete professorial saving being the voluntary **0.8 FTE lever**.

## Headline (current data, E&R + teaching, middle assumptions)
The robust, quantified finding is on the **non-professorial grades** (Lecturer / SL / AP): Exeter's structure is the
**dearest of the fourteen** English and Welsh Russell Group systems, and realigning just those grades to the **Russell Group
median structure** would save ≈ **£4.7m/yr in salary (≈£6m with on-costs; ~84 average-salary posts)**, recurring, with **no
severance bill** — from lower entry points and longer lower grades, so it touches **no current member of staff** (it means
paying *future* hires slightly less at given stages). It is **convergence with the middle of the peer group, not a race to the
bottom**, and these are equivalences for scale (£ ÷ average salary), not predicted job counts — provided so the magnitude can be
weighed against the **~150 full-time posts** the June 2026 consultation proposes to cut.

For the **professoriate**, we make **no per-head cost ranking** (see the note below): the evidence supports a high floor, a
slower *documented* progression, the most £100k+ staff per academic by headcount (upper-mid by FTE), and recent growth that is
mostly national pay-award drift — but not a claim that it is dearer or cheaper than peers, and so no professorial structural
saving. The one concrete professorial-side saving is the voluntary **0.8 FTE lever**. (An all-in modelled bill combining both
layers is still on the All-in tab, but its professorial component inherits the ranking's unreliability — read it as indicative.) Three qualifications travel with these numbers: a
structural change **phases in over roughly five years** (see the transition model); it saves mostly by **paying future hires
less**, not by freeing cash this year; and the modelled population is **full-time staff in the main academic grades** —
research-only, part-time and professional-services staff are not counted. Indicative.

**Note on the professorial layer.** We deliberately make **no per-head cost ranking** for the professoriate. The Professorial tab
still *models* one, but calibrating that model against Exeter's own accounts showed it is unreliable: its progression assumption
can place Exeter "below median" or "dearest" depending on a rate that a single year of accounts cannot pin down (the £100k+ data
can't separate progression *speed* from the professoriate's *age*). The retired ranking and the reasons are documented in
`docs/deprecated/professorial-ranking.md`. What we assert instead are four evidence-backed claims:
1. **High floor, slower documented cadence** — Exeter's professorial entry (£78,189) is 3rd-highest of 14; its published
   progression is biennial merit where several peers give automatic annual increments (a description of the rules, not a
   measured rate).
2. **Most £100k+ by headcount, upper-mid by FTE** — 162 per 1,000 academics (highest) vs 102 (4th of 9) on FTE; the headcount
   lead is partly a part-time artefact (0.63 FTE/head).
3. **Growth is ~70% pay-award drift** across a fixed £100k line (~30% real, concentrated in 2023/24).
4. **Incentivised within-band part-time saves money** — a full-time £100k+ move to 0.8 FTE saves ~20% of a six-figure salary
   for a fraction of the cost (~8:1); pure employer-side arithmetic, independent of 1–3. This is the professorial-side saving
   the site leads with (the **0.8 FTE lever** tab).

**Calibration:** with on-costs the modelled bill is ≈£137m — about 35% of the £396.6m total staff costs in Exeter's
2024/25 Annual Report, with the other ~65% being exactly the groups the model excludes (professional services,
research-only, part-time, sub-Lecturer grades, non-salary staff costs). **Read that £137m as an over-estimate of the
modelled population's cost:** checked against the real spine-point distribution, the 50/50 SL:AP split inflates the
*absolute* non-professorial bill by ≈**9.7%** (modelled mean £56,357/head vs actual £51,394). Correcting the mix to the
observed ≈3:1 brings the modelled mean to within **0.6%** of actual — and *raises* the structural saving slightly
(£4.74m → £4.88m), because the error is a level effect that largely cancels when comparing structures. For scale, the
structural difference vs the median (≈£4.7–4.9m/yr salary, ≈£6m with on-costs) is comparable to Exeter's 2024/25 operating
surplus (£8.2m, down from £22.5m — the operating line, not the headline surplus, which was distorted by a one-off pension
provision release in the prior year).

## Which universities are included
The active comparison is **Russell Group** universities in England and Wales on the national pay spine, with available data:
**14 non-professorial structures, 13 professorial, 13 modelled as a whole pay bill** (Durham is non-professorial only — its professoriate is excluded, see below). **Kept in the data but out of the comparison:** the
**Scottish** universities (Edinburgh, Glasgow, Aberdeen — different student-funding model) and **non-Russell-Group comparators**
(Bath; Aberdeen is also Scottish) — retained in `grades.json`/`grades.csv` for transparency. **Excluded by design:** Oxford,
Cambridge, the London institutions (incl. UCL) and Northern Ireland (distinct labour markets / cost bases). Sheffield is on its
**current (Aug 2025)** grade and professorial scales; **Durham's professoriate is excluded** from the professorial and all-in
comparisons — it publishes only indicative bands with no scale of the spot salaries actually awarded, so it cannot be priced
reliably (and nothing suggests it pays professors less), so it appears as a non-professorial structure only; Liverpool's
professoriate is modelled on its published Level 1 scale (SP55–59, automatic) plus its off-scale range to £99,001;
Levels 2–4 (spot salaries to £145k+) are excluded like other Band-3 analogues. Newcastle is modelled on its published IB Professor
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
2. **Send missing scales.** Coverage is complete. Most useful now: **corrections** to any scale used here, and **documentation of professorial
   progression rules** (automatic vs merit, review frequency), which are poorly published and materially affect the
   professorial comparison.
   Current published scales for any other institution are welcome too.
