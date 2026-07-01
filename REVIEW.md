# Independent review of the pay-structure analysis

*A critical review of the analysis, modelling and presentation in this repository, with
prioritised recommendations. Written July 2026 against the repo at commit `73ab66e`.
Every file/line reference below was checked against the source.*

---

## Verdict in brief

**1. The overall analysis** is transparent, primary-sourced and unusually well-caveated,
and its central normalisation — hold Exeter's workforce fixed, vary only the pay-scale
structure — is the right way to compare structures. Its main weakness is not the
arithmetic but the gap between what the model measures (the *geometry* of pay scales)
and what the headline framing invites readers to conclude (that the cuts are
unnecessary). The finding that Exeter's structure is the dearest of the ten modelled
systems appears robust across the scenarios tested; the *policy* inference layered on
top of it needs more qualification than it currently gets at the point of use.

**2. The modelling** is internally consistent — no computational errors were found — but
it is a structural counterfactual, **not** a salary-bill comparison, and several
load-bearing assumptions (promotion pace, the 50/50 SL/AP split, contribution-point
uptake, the 40% professorial award rate, the HESA band→grade mapping) are reasoned
rather than evidenced. The model is never calibrated against Exeter's actual published
staff costs, and its uncertainty analysis, though present, covers only part of the model
and is hidden from the main site.

**3. The presentation** is better than most advocacy material: consistent colour
semantics, a genuinely well-baselined headline chart, explained jargon, and interactive
assumptions. But a lay reader is still exposed to truncated bar-chart axes that
visually inflate differences, an unexplained core acronym ("E&R"), point estimates
where ranges exist, caveats tucked into collapsed panels and prose, and — most
seriously — **two different figures for the size of the cuts (125 and 150) used
interchangeably**, including within a single page. Since "posts saved vs posts cut" is
the site's central comparison, that inconsistency undermines the exact number the whole
argument leans on.

---

## What was reviewed

The repository is a self-contained static site (GitHub Pages, no build step): seven HTML
dashboards with all modelling as inline JavaScript and all data inlined, plus
machine-readable data (`grades.json`, `grades.csv`, `national_spine.csv`,
`cost_model_results.csv`), archived source pay scales in `sources/`, and HESA DT025
Table 17 extracts for Exeter (2024/25). The working spreadsheet `payscales.xlsx` is
deliberately not published. There are no notebooks or scripts; the dashboards are the
model.

---

## 1. The overall analysis

### What it does well

- **The core normalisation is sound and clearly explained.** Because all comparators sit
  on the same national spine, applying one fixed workforce to each structure isolates
  structural differences and avoids the naive "their average salary vs ours" comparison.
  The site says this repeatedly and accurately.
- **Provenance is exemplary.** Every structure is transcribed from an archived published
  pay scale (`sources/`), linked to the live HR page, and released in machine-readable
  form with an explicit invitation to check and challenge (README "Help fill the gaps").
  A `confidence` field per transcription is a nice touch.
- **The robustness instinct is right.** Fast/middle/slow promotion scenarios, an
  on-costs toggle, two workforce definitions, and a 5,000-run Monte Carlo all exist. The
  qualitative ranking (Exeter at or near the top; Birmingham/Nottingham/Warwick near the
  bottom) does survive the scenario grid in `cost_model_results.csv` — although Leeds
  flips to *dearer than Exeter* under slow promotion, which usefully shows the ranking
  of near neighbours is assumption-sensitive even if the extremes are not.
- **Honest concessions.** The README concedes the biggest lever "largely means paying
  *new* staff less … a recruitment trade-off, not a free saving" (README lines 51–52),
  that research-only staff are "flagged, not counted", and that figures are indicative.

### Where it is weaker

- **The measured quantity and the argued conclusion are different things.** The model
  answers: "what would Exeter's current workforce cost on each peer's scale geometry?"
  The Overview argues: "the scale of the cuts looks less like a necessity than a
  choice" (`combined_dashboard.html` line 60). Getting from the first to the second
  requires at least three further premises the model does not establish: (a) that the
  structural saving is *achievable* (it requires new hires on lower pay, i.e. a
  recruitment-market trade-off); (b) that it is *timely* (the repo's own transition
  model shows the saving ramping over roughly five years, while the deficit is now);
  and (c) that a steady-state structural saving is *fungible* with an immediate
  cash-savings target. All three qualifications exist somewhere on the site, but none
  is attached to the headline where the "≈134 posts vs ~125 cuts" juxtaposition is
  made. A sceptical reader (or the university's finance office) will spot this gap
  immediately, and it is the most likely line of rebuttal.
- **Coverage is thinner than the framing suggests.** The active whole-system comparison
  is ten institutions. Manchester and Newcastle — two of the largest non-London English
  Russell Group members, both on the national spine — are absent. To the repo's credit
  this is acknowledged, but only in the "Help fill the gaps" section at the bottom of
  the README (lines 89–90). At the point where the headline claim is made ("the most
  expensive of the English and Welsh Russell Group systems that could be modelled"),
  the reader is not told that two major systems are missing, and a casual reader will
  hear "most expensive in the Russell Group".
- **No external calibration.** The modelled all-in Exeter bill (≈£106m on central
  settings) is never compared with anything observable — Exeter's financial statements,
  or HESA staff-cost data. Even a rough reconciliation ("our modelled figure is X% of
  the academic staff costs in the 2024/25 accounts; the difference is part-time staff,
  research-only staff and non-pay elements") would substantially strengthen
  credibility, and its absence is conspicuous in an analysis this careful about
  everything else.

## 2. The modelling — does it accurately represent salary-bill differentials?

**Short answer: it does not model salary-bill differentials, and mostly does not claim
to.** It holds Exeter's workforce fixed by construction, so it cannot detect differences
in staff composition, seniority profile, discipline mix or actual grade distribution
between institutions — which are the main drivers of real pay-bill differences. As a
model of *"what Exeter's workforce would cost under each structure"* it is internally
coherent; as evidence about what peers actually spend it is silent. Any sentence on the
site that could be read as "Exeter's pay bill is higher than its peers'" over-claims;
the wording is mostly careful, but the distinction will be lost on exactly the
non-technical audience the site addresses (see §3).

### Verified mechanics (no bugs found)

The two engines are simple and correct as implemented:

- **Engine A** (`payscale_dashboard.html`): expected salary per grade as a weighted
  average over *normal* spine points (scenario weights: bottom/even/top), blended by
  workforce, optional on-costs (`s + 0.15·max(0, s−5000) + 0.145·s + 0.005·s` — NI,
  USS, levy; disclosed on-page). Contribution points are ignored entirely here.
- **Engine B** (`all_in_model.html:136–147`, reused by the career, transition and
  Monte Carlo pages): a representative person takes one listed increment per year for
  `TEN` years per grade (fast 4/6/7, middle 5/7/8, slow 6/8/9 — line 131), then sits at
  the ceiling with probability `1−cp` or on the **first** contribution point with
  probability `cp` (default 30%).
- **Professorial model** (`professorial_model.html:52–55`): everyone starts at the band
  floor at 48, faces a biennial review with award probability `p` (default 40%), climbs
  one rung per success (binomial expectation), averaged over 20 years.
- The Monte Carlo's normalisation, the binomial, and the triangular sampler are all
  correctly implemented; `cost_model_results.csv` is consistent with Engine A.

### Load-bearing assumptions with little evidence behind them

These are the settings the headline actually depends on, roughly in order of leverage:

1. **Promotion pace** (`TEN`) — pure stipulation. The scenario spread (bottom vs top in
   `cost_model_results.csv`) moves the Birmingham gap from ≈104.6 to ≈68.5 posts on the
   larger workforce, i.e. ±25% around the central figure. The Monte Carlo varies pace,
   but only within the stipulated 4–6/6–8/7–9 ranges.
2. **The HESA band→grade mapping.** Staff are bucketed by *salary band*, not grade:
   £39.1–52.2k → Lecturer, £52.2–69.8k → SL & AP (split **50/50**, hard-coded as
   277.5/277.5 and 367.5/367.5 in `all_in_model.html:129`), £69.8k+ → professor. Band
   boundaries are HESA's, not Exeter's grade boundaries, so e.g. a professor below
   £69.8k is counted as SL/AP and a senior AP above it as a professor. The mapping is
   disclosed (README lines 60–65) but its error is never estimated, and it is not
   varied in the Monte Carlo (the SL/AP split is; the band mapping is not).
3. **Population exclusions.** The headline workforce is *full-time* academic staff
   (HESA Table 17 covers full-time only) in the three grades plus professoriate. All
   780 research-only staff and the ~60 teaching-only staff below £39.1k are excluded,
   and part-time staff are excluded entirely by the data source. Two consequences:
   (a) the model's own caveat text describing an "FTE … basis"
   (`all_in_model.html:184, 262`) is not strictly right — this is a full-time headcount
   basis, not FTE; (b) the modelled population (1,155 + 500) is well under half of
   Exeter's 2,490 full-time academic staff, which readers deserve to see stated
   plainly next to the £106m figure.
4. **Contribution-point uptake (30%) and the first-point-only simplification.** Engine B
   prices the tail using only the first contribution point (`c[0]`,
   `all_in_model.html:136`). Exeter has the longest contribution tails in the set
   (grade H: six points up to spine 56), so this simplification *understates Exeter's
   cost* — conservative in the analysis's favour, and worth saying explicitly where the
   headline appears, because it is one of the few biases that helps rather than hurts
   the argument.
5. **The professorial model's granularity artefact.** "One rung per successful review"
   means a rung on Nottingham's 12-step ladder is worth several times a rung on
   Southampton's 36-step ladder, so cross-institution professorial rankings partly
   reflect ladder *granularity* rather than generosity. The page caveats this, but the
   professorial layer also carries two hand-adjustments — Birmingham's scale uprated
   ×1.13 from 2021, Durham's rungs interpolated from band min/max — and the
   professorial award rate is **not** varied in the Monte Carlo. Given professors are
   ~30% of the modelled headcount and a large share of the bill, this layer is the
   least reliable part of the model and deserves either its own sensitivity treatment
   or a more prominent health warning.
6. **Skip-scale increment conflation.** Taking "one listed point per year" makes
   skip-heavy scales (Birmingham's Lecturer grade runs 28, 29, 30, 33, 36) climb faster
   in £ per year than contiguous scales. This inflates the modelled cost of the
   *cheaper* structures — again conservative for the headline gap — but it distorts
   peer-vs-peer comparisons, and the "years in grade" clock is not truly comparable
   across differently shaped scales.

### Smaller technical points

- **The cuts denominator is inconsistent** (detailed in §3): ~150 in
  `combined_dashboard.html:53,130` and `all_in_model.html:31`; ~125 in
  `all_in_model.html:163,184,196,225,262` and README lines 23 and 72.
- **The static hero chart is out of sync with the model.** The hand-coded Overview SVG
  shows Nottingham at "≈ 140 posts" (`combined_dashboard.html:128`) while the README
  headline says ≈134 (line 70) — different assumption vintages. Frozen numbers in a
  hand-edited SVG will keep drifting from the live model.
- **Exeter is missing from the local-extension salary map** (`ext`,
  `all_in_model.html:129`): every other institution using points above 51 has its own
  published values there, but Exeter's contribution points 52–56 fall back to generic
  national values. Currently harmless (Engine B only ever prices Exeter's tier-3
  `c[0]` = 51, and Engine A ignores contribution points) but it is a latent
  inconsistency that will silently bite if the contribution-tail modelling is ever
  deepened.
- **The uniform +2% for 2026-27** is fine as a disclosed placeholder; it rescales
  everything equally and does not affect rankings.

### Overall on accuracy

Within its own terms — a like-for-like structural comparison — the model is competent,
conservative in several places, and honest about most of its limits. What it is **not**
is an estimate of achievable savings or of actual pay-bill differences, and the two
biggest gaps between the model and reality (the professorial layer, and the excluded
research-only/part-time population) both sit outside the Monte Carlo, so the published
sensitivity range is narrower than the true uncertainty. Headline figures should be
presented as ranges spanning at least the scenario grid, and ideally a widened Monte
Carlo, rather than as "≈ 82 / ≈ 134" point values.

## 3. Presentation for a non-quantitative audience

### What works

- **The best chart on the site is the most important one**: the all-in model's
  zero-centred diverging bars ("Exeter = 0", cheaper left in green, dearer right in
  red, `all_in_model.html:164–169`). The baseline is explicit, the encoding is honest,
  and it should be the template for the rest.
- **Consistent visual language** (Exeter always amber; green = cheaper, red = dearer)
  and consistent units (£, £m, %, "equivalent average-salary posts").
- **Good glossing of genuinely hard concepts**: the national spine, on-costs (with the
  exact NI/USS/levy breakdown), contribution points, discretionary professorial
  reviews, and the median are all explained in plain language on the pages that use
  them.
- **Interactivity as pedagogy**: letting readers move promotion pace or award rate and
  watch the numbers move is the single most effective uncertainty communication on the
  site — arguably more effective for this audience than the Monte Carlo.

### What doesn't

1. **The 125 vs 150 inconsistency is the most damaging presentation defect.** The
   Overview tells readers "around 150 full-time posts" are being cut and the hero
   chart's footnote repeats "~150" (`combined_dashboard.html:53,130`); the model pages
   and README compare against "~125 cuts". The site's entire rhetorical structure is
   "structural difference ≈ size of cuts", so a 20% wobble in the comparator — visible
   to anyone who reads two pages — hands critics an easy way to dismiss the whole
   thing. If the two numbers are genuinely different things (e.g. FTE announced in the
   consultation vs posts at risk per UCU), say so once, pick one for all comparisons,
   and cite it.
2. **Truncated axes on the per-head bar charts.** The cost-per-head bars start their
   scale at 90–96% of the minimum value rather than zero
   (`payscale_dashboard.html:254`, `career_cost_model.html:167,183`,
   `professorial_model.html:67`), so a ~8% per-head difference can render as a bar
   twice as long. Every bar does carry an exact £ label and an Exeter reference line,
   but the stated audience reads bar lengths, not labels. Either zero-base these or —
   better — re-express them as difference-from-Exeter diverging bars like the all-in
   chart, where a non-zero baseline is the honest choice rather than a distortion.
3. **The only visual uncertainty display is hidden.** `monte_carlo.html` (histogram,
   median, 5th–95th band) is deliberately not linked from the combined dashboard
   (README lines 30–31). The result: every figure a normal visitor sees is a point
   estimate, with uncertainty carried only by the word "indicative". For a lay
   audience, "somewhere between X and Y posts" is *more* credible than "≈ 134", not
   less. Surface the Monte Carlo, and quote its range in the headline sentences.
4. **Unexplained core jargon.** "E&R" appears throughout the controls and captions
   ("E&R only (750 staff)") and is never once expanded to "Education & Research"
   — it is Exeter-internal HR vocabulary, opaque even to academics elsewhere. "FTE"
   is used without expansion (and, per §2, inaccurately). HESA and USS are never
   spelled out. One glossary box, or first-use expansions, fixes this.
5. **Caveats are structurally skippable.** The key qualifications (savings accrue over
   ~5 years; mostly via paying future staff less; population excludes research-only and
   part-time staff) live in the README, in collapsed `<details>` panels
   (`all_in_model.html:126`), or on other tabs. The hero chart footnote carries only
   the mildest caveat. The pattern throughout: **the claim is on the chart; the
   qualification is somewhere else.** For a non-critical audience, whatever is not on
   the chart does not exist. The three caveats above belong in the hero chart's own
   annotation and in the Overview's opening paragraph.
6. **The hero chart has no numeric axis** — only "≈ N posts" end labels — and its
   frozen values already disagree with the README (140 vs 134). Generating it from the
   same data as the live dashboards (or at minimum regenerating it whenever data
   changes) would fix both.
7. **"Equivalent posts" itself.** The metric is caveated at every appearance, which is
   creditable, but converting £ to "posts" and placing it beside the cuts number is
   still an invitation to read it as "jobs that could be saved" — the site knows this,
   because that reading is its argument. The honest fix is not more disclaimers but
   the timing/new-hires qualification attached at the point of comparison (see
   recommendation 4), because that is the substantive reason the equivalence is not a
   retention offset.

## Recommendations

In priority order. The first three are quick fixes; none of the rest requires new data
except (7) and (9).

### Correctness and consistency (do first)

1. **Unify the cuts figure.** Pick one sourced number (or explain the 125/150
   distinction once), then use it everywhere:
   `combined_dashboard.html:53,130`, `all_in_model.html:31` vs `:163,184,196,225,262`,
   README:23,72.
2. **Re-sync or dynamise the Overview hero SVG.** Its frozen values (Nottingham ≈140)
   contradict the README headline (≈134). Either generate it with the same JS/data as
   the other charts or add a build note pinning which settings produced it.
3. **Fix the latent Exeter gap in the `ext` local-extension map**
   (`all_in_model.html:129` and `grades.json` `ext_salary`) so Exeter's points 52–56
   use its published values like every other institution's.

### Methodology

4. **Attach the three load-bearing qualifications to the headline itself** — wherever
   "≈ N posts vs the cuts" appears (hero footnote, `ans1` in `all_in_model.html`,
   README headline): *(a)* saving phases in over ~5 years (your own transition model),
   *(b)* it accrues mostly by paying future hires less, *(c)* the modelled population
   is full-time staff in the main academic grades (~1,655 of 2,490 full-time academic
   staff; research-only and part-time staff excluded).
5. **Report ranges, not points.** Quote the Monte Carlo 5th–95th band (and the
   fast/slow scenario spread) in the headline sentences: "roughly X–Y average-salary
   posts" is both more honest and more defensible than "≈ 134".
6. **Widen the sensitivity analysis** to the two biggest unpropagated uncertainties:
   the professorial award rate (currently fixed at 40% while professors carry a large
   share of the bill) and the band→grade mapping / SL-AP boundary. Extending
   `monte_carlo.html` to sample these is a modest change with a big credibility payoff.
7. **Add a calibration check.** Reconcile the modelled ≈£106m (with on-costs setting
   stated) against Exeter's published staff costs (financial statements or HESA
   finance record), itemising the wedge (part-time, research-only, non-modelled
   grades, non-pay staff costs). This is the single strongest credibility upgrade
   available.
8. **Correct the "FTE" wording.** HESA Table 17 is full-time headcount; either re-label
   the basis accordingly or rebuild the workforce from an FTE source (HESA staff FTE
   tables) — currently the caveat text claims a basis the data doesn't support.
9. **Quantify (even roughly) the research-only exclusion.** You already hold the band
   distribution for the 780 research-only staff; a crude structural costing with wide
   error bars would let the headline say "excluded, worth roughly £X–Y" instead of
   "flagged, not counted" — and would pre-empt the objection that exclusions were
   chosen to flatter the result (they weren't; they mostly *understate* the gap, which
   is worth saying out loud).
10. **State coverage at the point of claim.** Where the site says "most expensive of
    the … systems that could be modelled", add "(ten systems; Manchester and Newcastle
    not yet covered)" rather than leaving that to the README's final section.

### Presentation for the lay audience

11. **Zero-base or re-express the per-head bar charts** as difference-from-Exeter
    diverging bars (`payscale_dashboard.html:254`, `career_cost_model.html:167,183`,
    `professorial_model.html:67`), matching the all-in chart's honest baseline.
12. **Surface `monte_carlo.html` as a tab in the combined dashboard**, retitled in
    plain language (e.g. "How sure can we be?"), with one sentence explaining that the
    spread comes from varying the assumptions nobody can pin down.
13. **Add a short glossary / first-use expansions**: E&R, FTE, HESA, USS, spine point,
    on-costs, contribution point. One box on the Overview and title-attributes in the
    controls would cover it.
14. **Put a plain-English "What this shows / what it doesn't" box at the top of the
    Overview** — five bullets: same national spine everywhere; we price Exeter's own
    staff on each university's structure; Exeter's structure is the dearest of the ten
    we could model; the difference is comparable in scale to the cuts, but it phases in
    over years and comes mostly from paying future staff less; this is a comparison,
    not a costed alternative plan. That one box would do more for the stated audience
    than every caveat currently on the site combined.
15. **Give the hero chart a numeric axis** (posts, with gridlines) so its magnitudes
    can be read without relying solely on the end labels.

---

*Method note: this review was produced by reading every HTML dashboard, data file and
document in the repository and tracing the model code by hand; the model was not
re-executed. Line numbers refer to commit `73ab66e`.*
