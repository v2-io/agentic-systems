# Check: CATALOG.md version 4 against the v3 audit's findings

*2026-10-06, Claude Opus 5.5, the author of the v3 audit (`catalog-design-v3-2026-10-06.md`). This isn't de novo: I came to version 4 knowing my own findings, and some of what it does is what I suggested. One of those suggestions turned out wrong (V1 below). Written for the coordinating session and Joseph before anything is built. I changed no file but this one and touched no process.*

*The seal. I read no `choose` answers. None exist yet: at 13:29 round c095 had only just been planned, and no `data/answers/` file holds the kind. Every aggregate below leaves out any answer whose context or candidate contains a canary glyph (`▁ ▂ ▃ ▄ ▅ ▆ ▇ █ 🮆 🮅 🮄 ▀ 🮃 🮂 ▔ ▉`). The only canary-specific numbers are pick, continue and triad answers already quoted in the v3 audit and in v4 itself.*

Labels as before: **[measured]**, **[checked]**, **[reasoned]**.

## The short answer

Version 4 is a real structural improvement. Measured quantities replace stored tiers, "undiscriminable" is a stated fact, the tests are procedural, the provenance is complete, and the seal was put in place before c095 could record. C3, C6, C7, C9 and C10 are essentially resolved. Two things are not:

1. **The rule that sets aside D positions where the chart candidate is felt is triggered by chart-following itself** (V1). This was my suggestion in v3, and it's wrong. First-impression minds accept the chart's next glyph 0.79–0.82 of the time, against 0.03 for near decoys. So "L beyond its control, or picked" holds wherever minds follow the chart, and the instrument stops seeing what it exists to see. A version that works reverses the rule's role: a felt chart candidate blocks only the conclusion *for* the chart, and it is what makes a preference *against* the chart informative.
2. **Positive independence is cheap at positions where the chart was never a temptation** (V2). After `▀`, going down, the chart's next glyph is `╿`, a box-drawing piece. Preferring the run's glyph to it says nothing about the chart. Triads show the same thing: half of all middles in triples spanning several blocks depart from the code-point median, close to the two thirds a random middle would give.

On the two questions you couldn't settle alone:

- **The default view's rule** (Q1) has a gap: no category for recognition that leans on the *names*. Its categories overlap with no precedence. It counts "undiscriminable" as a pass, so the canary could come out "intuitive" on evidence that name arithmetic predicts equally well. And "rational" by provenance reads *not generating* as evidence, which METHODOLOGY's one-way rule forbids. Its value would also change with the asking history.
- **The name-only order question** (Q2) measures whether the names *suffice* to produce an order, as a mind that can recall glyphs and code points from names would produce it. It doesn't measure whether a mind *relied* on names when shown the glyphs. It is informative only in a narrow middle band, and it needs a validation set before it is trusted.

---

## Q1. Is the default view's rule coherent?

§11's rule, read as written [reasoned]:

- **A gap: leaning on names.** "Chart-leaning" covers chart independence negative with certainty. Nothing covers *name* independence negative with certainty. A run that follows the names' order against the look, with its chart independence positive, is not intuitive (one route isn't positive or undiscriminable), not chart-congruent, not chart-leaning and not undecided (its answers are conclusive). It falls out of the view. Joseph's sentence puts the name and the code point side by side, so the view needs a "name-leaning" category on the same footing as "chart-leaning".
- **Overlaps with no precedence.**
  - A run proposed only by deliberating generators can at the same time have negative chart independence (chart-leaning) or unasked discriminating positions (undecided). Most will have the latter, since most runs aren't contiguous.
  - A contiguous run proposed by a generator mind, without a lookup, is both rational and chart-congruent. The reasoned pass's sheets *without* a range lookup still went to the chart neighbour 0.30 of the time.

  The rule needs either an order of evaluation or exclusive definitions.
- **"Undiscriminable" counts as passing a route.** Intuitive requires each route to be "positive with certainty or undiscriminable", with at least one positive. For the canary, v4 asserts that the name route is undiscriminable (§7a) and that the chart route discriminates at `🮄 → ▀`. A preference for `▀` there would make the canary "intuitive". But FIVE EIGHTHS to HALF is exactly what name arithmetic predicts, and Joseph's criterion excludes "thinking about the glyph's name". Undiscriminable means *we can't tell whether it rested on names*, not that it didn't. The honest view label is "independent of the chart; name route undiscriminable", shown as such rather than folded into "intuitive". The same holds symmetrically for runs contiguous in code points whose name route turns out positive.
- **"Rational" by provenance has two problems.**
  - **It reads non-generation as evidence.** "Proposed *only* by deliberating generators" requires that no first-impression mind proposed the run. METHODOLOGY §1 and §2a: *"A mind that doesn't write `x` has said nothing about `x`."* The rule turns that silence into a property of the run.
  - **It depends on the asking history.** Whether a first-impression mind has proposed a run depends on whether the planner ever showed one the right context. One more continue question can move a run out of "rational" without anything about its perception changing. (The planner's choices are concern 3. The view would let them decide a concern-6 category.)
  - **Provenance isn't defined for several sources** [measured, cohere answers on real runs by `source.from`]: 1,667 come from tree walks, 1,640 from written momentum, 1,383 from pick branches (the generator minds) and 1,358 from *reordered* shuffles. A reordered run was proposed by the fate generator and then recognised, so no mind proposed it. Seeds were proposed by surveyors with deliberation, and the canary by Joseph plus the session's completion. The rule doesn't say what any of these is.
- **Two undefined steps.**
  - How a run's signed independence is built from its positions. §7b is per position, while §10 and §11 use a per-record value. Weakest position, strongest, or weighted mean gives different answers for the canary, and the choice has to be frozen.
  - What "recognised … L beyond its contrast" means for a run, since L is per link.

**What might hold for "rational"** [reasoned]. Joseph's words are "an interpretable rational sequence (given some thought)". That is a property of how the run is *recognised*, not of who found it. Three options, best first:

1. Ask Joseph what observable he means. This is a definitional choice about his own ranking.
2. Define it on the assigned deliberation contrast: recognised by `haiku45` (31000) and not, beyond its control, by `haiku45nt` (0). This is identified only within Haiku, and it should be stated that way. It also brings deliberation back as a *measured* condition, which is what A3 objected to only when it stood in for "intuitive".
3. Leave "rational" out of the default view until an instrument exists, and show "recognised; independence undecided" instead.

## Q2. What the name-only order question measures

**What it measures** [reasoned]. Shown a scramble of names such as UPPER HALF BLOCK, UPPER FIVE EIGHTHS BLOCK and so on, a mind orders the *descriptions*. That tells you whether the names suffice for an order. It doesn't tell you whether a mind shown the *glyphs* reached its order through their names. The chart analogue would be: give a mind the code points and see whether it can sort them. Trivially yes, and that tells you nothing about reliance. The question gives the name route's *prediction*, which is what §7a uses it for, and that use is sound. But two properties limit it.

1. **Names are a route back to glyphs and code points.** The minds in this study know the Unicode database. Given "CIRCLED DIGIT FOUR" or "UPPER HALF BLOCK" they can recall the glyph and often its code point. The whys spike found Claude's reasons citing code points in 0.38 of its yes answers on contiguous runs. So the name-only order may be the chart order recalled through names. Where the two disagree, it can be checked: sets whose names' meaning orders them one way and whose code points order them another. Fractions across two blocks are the clean case, though the canary's glyphs are that case. Digit "dresses" spread over several blocks are another. If name-only orders follow the code points there, the question measures chart recall, and the name route isn't separated from the chart route at all.
2. **It is informative only in a narrow middle band** [measured, a crude proxy]. Among the 2,430 runs asked whole, glyph names that share one template and vary only in a number or letter word cover 27% of the contiguous runs and 5% of the others. For templated runs, the name-only order will match everywhere, so the name route is undiscriminable. For most other runs (punctuation, arrows, morphs like `-=>})|`), names carry no order. The name-only answer will then be "none" or scattered. A run whose names predict nothing is "name-discriminating" by §7a's definition, so recognising it in order earns *positive* name independence for free. That is the V2 problem on the name route. The informative case, where names predict an order *different from* the run's, is the narrow band in between.

**What might hold.**

- Separate three outcomes per position: names predict this step (congruent), names predict a different step (discriminating), names predict nothing (uninformative). Only the second can earn positive name independence.
- Validate before trusting. Ask name-only orders on sets where name meaning and code-point order disagree, and on sets whose names are uninformative. Report how often each is reproduced before any run's name independence is computed from it. The freeze could include that validation's result as a precondition.
- **The canary's name status is asserted, not measured.** §7a says name-congruence "isn't decided by a hand-written rule", then states the canary is name-congruent everywhere. At `█`, though, the names put LEFT SEVEN EIGHTHS (`▉`) and UPPER SEVEN EIGHTHS (`🮆`) on an equal footing as "seven eighths". Whether names predict `🮆` there depends on reading the LOWER-to-UPPER axis word, which is a judgement. The canary's name route should wait for the question like every other run's. Asserting it now pre-commits how the canary is evaluated, before the freeze.

---

## V1. The felt-chart-candidate rule silences the chart (C2, traded)

**What v4 says.** §7b: where the chart candidate "is itself recognised at that context (L beyond its control, or picked)", the D position is a branch preference and doesn't count. That is the wording I proposed in v3.

**What the data show** [measured, inhibit answers, canary glyphs excluded]:

| candidate | Claude yes | Grok yes | Gemini yes |
|---|---|---|---|
| the chart's next glyph, in the run's direction | 0.82 (2,099) | 0.79 (778) | 0.80 (56) |
| the chart neighbour the other way | 0.46 (85) | 0.61 (28) | — |
| a real candidate not adjacent in the chart | 0.24 (2,445) | 0.22 (907) | 0.30 (47) |
| near decoys (L's control) | 0.03 | 0.01 | 0.03 |

Chart neighbours were asked because something proposed them, so this is a selected set. Even so, its acceptance rate is more than three times that of other proposed candidates, and about 25 times the control's. "L beyond its control" will hold for almost every chart neighbour that is asked, and "or picked" adds every position where a pick went to the chart. At the canary's remaining position, `🮄 → ▀` against `🮃`, the chart's `🮃` was picked 8 times at `… 🮄` and written first at `🮆 🮅 🮄` by several minds (c005, c008). Whether that disqualifies the position depends on how exactly "at that context" is matched. Either way, the rule makes the instrument's validity depend on the outcome it measures.

**What might hold: asymmetric inference** [reasoned].

- **A preference *for* the run's glyph against a felt chart candidate is the strongest evidence D can give.** The chart offered something minds do accept, and they chose otherwise. A felt chart candidate is what makes the position informative, not what disqualifies it.
- **A preference *for* the chart candidate is ambiguous when that candidate continues a recognised branch.** It might be chart-following, or a felt branch that happens to be chart-congruent. Record it as a branch preference, and don't count it as negative chart independence. For `█ → 🮆` against `▉` this is exactly right: `🮆` would be evidence against the chart, and `▉` would be no evidence either way.

## V2. Positions where the chart was never a temptation (C5, traded)

**D.** A chart-discriminating position whose chart candidate is unrelated to the run (`╿` after `… 🮄 ▀`, going down) gives a near-certain preference for the run's glyph. It measures only that the context fits its run. The D control (a neutral context) doesn't fix this, since it measures standalone pull, not the pull of chart adjacency. A position is a real test only when the chart candidate is **contested**. Two possible tests: a fact from the glyphs (the chart candidate is in the same Unicode block, or has the same name template, as the run's glyphs around it), or a measurement (the chart candidate is named or recognised at that context, the V1 condition read the right way round).

**Triads** [measured, canary excluded]:

| triple | middles | departing from the code-point median |
|---|---|---|
| all three in one Unicode block | 10,164 | 0.13 |
| across several blocks | 1,598 | 0.51 |

A random middle departs two times in three, so departures across blocks are close to chance, and they make up 37% of all departures. Within a block, where the code-point median is a real alternative, departures are rarer and informative. The 2,290 and 229 in §7b mix the two. The same block rule (or the contested condition) should gate triads and order lines too. V1's asymmetry applies to them as well: a triad whose code-point median is itself a felt middle shouldn't count *for* the chart.

**Why it matters.** With V1 and V2 together as written, a recognised non-monotone run would earn positive chart independence mostly at trivial positions, and lose its contested positions to the felt-candidate rule. Under §11 that tilts "intuitive" toward exactly the runs whose instruments can't see the chart.

## The v3 findings, one by one

| finding | status in v4 | what remains |
|---|---|---|
| C1, tier rules | **appears resolved, partly traded** | no stored tiers (resolved). The view rule has its own gap, overlaps and undefined aggregation (Q1). §7a still says discriminating positions are "a fact about the glyphs", but name-congruence is now measured and the branch qualification depends on answers. Both are now partly data |
| C2, what D discriminates | **traded** | V1. The name route was added (Q2) |
| C3, substitution | **resolved in the design** | "a non-lookalike glyph of the same broad kind" should be drawn by a stated rule (fated, from a defined pool), not chosen by hand. Otherwise the control is a hand pick |
| C4, contiguous runs | **appears resolved** | §2 still ranks "intuitive above rational above chart-congruent", while §15 says chart-congruent is "not below rational". Joseph's quote calls both rational and chart-monotone sequences "fine", so the order between them is the session's reading. Worth asking him |
| C5, triad departures | **resolved, with a new problem** | V2 (departures across blocks are near chance). The canary's triads aren't sealed and are quoted in §7b and §14, so §1's "frozen before the canary is looked at" holds for `choose` only. Say so |
| C6, tests | **resolved** | test 2 went back to split-half, which the v2 audit (A10) found nearly unable to fail. A held-out-rounds version (fit through round N, predict the control rates of later rounds by class) would test stability that matters, without the population problem |
| C7, provenance | **resolved** | one omission: the triad era's grown rows from r004 place `▀` between `🮄` and `🮃` (`█ 🮆 🮅 🮄 ▀ 🮃 🮂 🮁`). "Include `▉` and end at `🮀` or `🮁`" reads as if they lacked it |
| C8, the model | **mostly resolved** | D's strength is written as $2p - 1$ (baseline 0.5) and also "against the D control's baseline". Pick one; with a baseline $b$, something like $(p - b)/(1 - b)$ for $p \geq b$, and the mirror for $p \lt b$. Family weights come from "R's other class, or D where it exists", which needs a rule for when each applies. How raters *within* a family combine (Sonnet and `haiku45nt` have very different false-positive rates) is no longer stated, now that v3's hierarchical priors are gone |
| C9, inputs | **resolved** | I checked G's calibration set for a usable rejected class. Of 480 tendril-branch runs asked whole, 174 drew mostly "no" [measured]. So it exists, though at a median of 3 answers per run it is thin |
| C10, objects | **resolved** | "bounded by the links with evidence" is true of the full-prefix runs (paths in a trie), not in general of runs extended through stable suffix links. A count during the build would settle it |

## Smaller points

- **"Chart-congruent" names one route** for a category defined by *both* routes being undiscriminable. "Undiscriminable" would say what it is.
- **"Positive with certainty"** in §11 needs its Bayes-factor threshold listed among the frozen parameters chosen without evidence.
- **The seal file's list** is the right set for `choose`. Since §7b's canary-specific inputs (triads, picks) are already public, the seal's real protection is against tuning on D. That's worth one sentence in the seal, so nobody later reads it as covering more.

## What I didn't do

I fitted nothing, and read no `choose` answers (none exist). The name-template proxy in Q2 is crude (one varying token; fraction names that vary in two tokens are missed), so read its 27% and 5% as orders of magnitude. I checked v4 against my own findings and the two questions. I didn't re-audit unchanged sections from scratch, and a fresh reader would see v4 differently from someone who shaped it.
