# DEPRECATED: the model-based professorial cost ranking

**Status:** retired 2026-07 in favour of four evidence-backed claims (see below). The per-head
professorial £ ranking is kept in the code (the Professorial tab still computes it) but is **no longer
used to assert where Exeter's professoriate sits vs peers**, because it cannot be made fair.

## Why it was retired
The Professorial tab prices each university's professoriate by *modelling* progression (documented
mechanism × award rate) over a career, then ranks per-head cost. Two problems made the ranking
unsafe:

1. **The progression assumption is not identifiable from the data.** Exeter's default was "biennial
   discretionary merit." Calibrated against Exeter's own 2024/25 accounts, that default predicts ~0% of
   professors ever reach £100k+, but ~40% actually do (≈179 FTE sit in the £102–129k scale range). So
   the default was clearly too slow — yet a single-year cross-section can't separate progression *speed*
   from the *age/tenure* of the professoriate, so we can't pin the true rate either.
2. **Correcting Exeter alone is invalid.** Re-running Exeter with near-automatic progression into Band 2
   (and the full SP54–71 ladder, which the model had truncated at SP66/£111,459) moved its modelled
   per-head from ≈£82,540 to ≈£99–101k — i.e. from *10th of 13* to *dearest*. But the same correction
   almost certainly applies to peers, so re-ranking Exeter alone just flips the artefact.

Net: the model can say the professoriate is "below median" **or** "dearest" depending on an
un-pin-downable assumption. So we stopped claiming a professorial cost ranking (or a professorial
structural saving) at all.

## The old copy it replaced (for reference / possible restoration)

**Old splash bullet (combined_dashboard.html):**
> The professoriate is a separate choice. Once each university's own documented progression rules are
> applied (several peers award automatic annual increments where Exeter runs a slower biennial merit
> review), Exeter's professoriate already sits around or below the middle of the group — so there is
> little or no structural saving there against the median. Exeter could realign the grade structure and
> leave the professoriate untouched entirely.

**Old README claims:** professoriate "ranks about 11th of 14"; all-in gap vs median "≈ £2.0m/yr"
(the professorial component of that all-in figure inherits the same unreliability); "documented
mechanisms place Exeter mid-pack."

## What replaced it — four defensible claims
1. **High floor, slower *documented* cadence.** Exeter's professorial entry (£78,189) is 3rd-highest of
   14; its published progression is biennial discretionary merit where several peers give automatic
   annual increments. (Floor = robust; "slower" = a description of the rules, not a measured effective rate.)
2. **Most £100k+ by headcount, upper-mid by FTE.** 162 per 1,000 academics (highest) on headcount; 102
   (4th of 9) on FTE — the headcount lead is partly a part-time artefact (0.63 FTE/head).
3. **Recent £100k+ growth is ~70% pay-award drift** across a fixed £100k line (~30% real, concentrated
   in 2023/24).
4. **Incentivised within-band part-time saves money** — for any full-time £100k+ member of staff, a
   move to 0.8 FTE saves ~20% of a six-figure salary while a within-band increment costs a fraction
   (~8:1). This is pure employer-side arithmetic, independent of 1–3, and is the professorial-side
   saving the site now leads with (the **0.8 FTE lever** tab).

The **non-professorial** structural finding (Exeter's grade structure is the dearest; ≈£4.7m/yr vs the
RG median) is unaffected by any of this and remains the robust, quantified headline lever.
