# CATALOG: the canonical catalog of sequences

*Design, version 2 (2026-10-06), by the independent session (Claude Opus 5.5) with Joseph. Not built. Version 1 was audited de novo the same day (`audits/catalog-design-2026-10-06.md`, findings F1–F12). §13 maps each finding to what changed. A fresh audit of this version comes before anything is built. METHODOLOGY §2a lists the catalog as concern 6. References to "METHODOLOGY §n" are to that file; a bare "§n" is a section of this one.*

## 1. Why

METHODOLOGY §2a says that sequences, branches, ends, cycles and stability are *read off* the tree. What exists instead is a sound store of raw answers indexed by context, and readers that each derive sequences their own way: the tree's walks, the planner's walks and branch draws, BEST's paths, folding and ranking, and triad chains. Each is a partial model of one question, and each correction in one has exposed a loss in another. In two days:

- **Majority rule.** BEST confirmed links by majority in continue answers alone, so a "none" counted against a link. Morph ladders such as `-=>})|` disappeared.
- **Ranking.** Sorting by length hid every short cross-block run. Equal family weighting ranked a run two families confirmed below one only Claude had answered.
- **The cap at 8.** Pick contexts were silently capped at 8 glyphs.
- **The triad era's rows.** No reader generated candidates from the ported triads. Joseph's block-fill cycle `▁▂▃▄▅▆▇█🮆🮅🮄…`, which the triad era grew in r004–r006, appeared nowhere.

Joseph, 2026-10-06: *"would it make sense … to somehow create a script that gives a 'canonical' source of all 'possibly meaningful sequences + cycles', deduplicated, same-directioned, canonical starting point for cycles, every plausible branch getting its own 'record', and the edges in the chain being determined from the raw data in a defensible and proper way, auditable, giving the ultimate score for that branch/sequence etc.? … or is that what context-tree was already supposed to be and we basically have a 'raw-data context-tree' and a 'canonical statistically sound context-tree' maybe?"*

**A precedent, and what is different this time.** The triad era also had a global fit that ordered glyphs. It *"dropped/merged valid creative sequences"* (commit `b1a78dbe`), placed glyphs arbitrarily on links nobody had asked (OBSERVATIONS, 2026-10-04), and was demoted to a guess-proposer. The catalog is the second global model proposed as the source of sequences. What differs:

- Evidence is answers only, and every number is itemised to them.
- An untested link is shown as untested, never filled in by a prior (§7).
- Nothing is folded, merged or cut: containment and branches are relations (§4).
- Each kind of contrast is its own part of a record, never pooled into one rate (§6b).

## 2. What it is for

Recognition is the goal (METHODOLOGY §1), and Joseph has said which recognition matters most:

> *"An interpretable rational sequence (given some thought) is fine. Originally I gave more weight to monotonic perceptual sequences that were also monotonic in chart order / code-point magnitude. … one place where I feel the preponderance of claude models here who find it easy to look at sequences in terms of code-point location is potentially giving us, after everything, a very 'obvious answer -- just do it like the codepoints had it'. It's fine. It's not anything I'm excited about rediscovering. An 'intuitive' sequence that doesn't need internal arithmetic or thinking about the glyph's name and codepoint is (much) better."*

So the catalog must keep three things apart, and rank them in this order:

1. **Intuitive recognition.** It holds without deliberation and without the code chart.
2. **Rational recognition.** It is interpretable given some thought.
3. **Chart-borne recognition.** Code-point order, with nothing else holding it.

The roster makes this harder. Claude gives about two thirds of the answers, and its minds most readily read glyphs as chart positions. The rater model (§6c) and the contrast parts (§6b) exist largely so that volume from one family and fluency with the chart can't stand in for perception.

## 3. Where it sits

```
probing (1) ──answers──▶ raw tree (2) ──▶ CATALOG (6) ──▶ priority (3): what to ask next
port (4) ────answers──▶       │                     ├──▶ read-offs (5): BEST, SEQUENCES, PROGRESS
                              │                     └──▶ probing (1): measurement findings (sheet position, conditions)
```

- **Inputs.** The catalog reads answer records and their tags only, never `source` (why a question was asked). §5 says which records count.
- **Determinism.** The same inputs, recorded as a manifest of file hashes, and the same model version give the same catalog (§10).
- **Readers.** Priority and the read-offs read the catalog for anything about sequences. A reader that wants a view, such as BEST's length sections or a ranking key, makes it from catalog records and never re-derives links. Strength and certainty sit side by side on every record (§6a); choosing the ranking key is the read-off's job.
- **Probing.** Rater conditions and sheet-position effects, once estimated (§6c), are measurement-validity findings for concern 1.
- **Candidate inputs** may be named propositions to score: survey and dropspot seeds, the triad era's grown rows (`../data/growth/r004–r012.json`), triad chains, and shuffles a mind called coherent. **Seed votes are evidence, as their own rater** (§6c). Joseph's standing direction is that seeds are tagged votes, *"segregate those out if we need a more pure analysis"*. Grown rows and chains are candidates only: they were derived by rules, not answered.

## 4. Objects and canonical forms

- **A link** is `c → x` at its own context `c` (an oriented run, any length that was asked). A link at a long context and the same link at its suffix are different propositions. Nothing pools long contexts into short ones, so k\* and stability (METHODOLOGY §3) read from per-context counts as before.
- **A run** is an ordered list of distinct glyphs, of any length. A run and its reverse are one sequence (METHODOLOGY §2). Its **canonical orientation** puts first whichever end gives the smaller tuple of code points; a display may reorient it.
- **Which runs are records:**
  - every candidate input (§3);
  - every run asked whole (cohere or order);
  - every maximal run of links that each carry evidence of their own (§7);
  - every contiguous window of these that was itself asked whole.

  That is a stated rule, not a cut on score: a run with weak evidence is a record with a weak score. Sub-runs that were never asked and never proposed are not records, which keeps the count linear in the candidates rather than quadratic in length.
- **Containment** between records is a stored relation, never a deletion.
- **A branch** is a pair of records sharing a terminal sub-run (at either end, in either orientation) and then continuing differently. It records the shared run and the glyphs that separate them.
- **A cycle** follows METHODOLOGY §3. A cycle is a path that returns to a context state with every step determined, so a period may repeat glyphs (the bouncing spinner `- \ | / - / | \`). It counts only once a mind has *manifested* it. Its canonical form is the smallest code-point tuple over all rotations of the period, in both orientations.
- **Long runs.** Whole-run questions show at most 24 glyphs (`probe.MAX_RUN`), but runs are not bounded. A longer run's whole-run evidence comes from its windows that were asked, and its record says which stretches are covered. Coverage is a fact about the record, not a score.

## 5. Inputs: which records count

| records | how they enter |
|---|---|
| real answers (continue, pick, inhibit, cohere, order, triad, next, between) | evidence |
| `call-failed` (about 107,000, nearly all from the void rounds c028–c079) | excluded: a failure is no answer |
| `limit` (usage limits) | excluded |
| `tool-attempt` (673) | its own outcome: the mind did not answer from impression (METHODOLOGY §4); kept as a rater-condition finding, not evidence about a link |
| `unparsed`, `other` (not a glyph), unassigned code points | their own outcomes; never glyphs |
| reasoned (`sonnet55r`), no-lookup, the protocols `gsp-0.1` and `ctx-0.1` | evidence, as distinct rater conditions (§6c) |
| reflections | apart: the minds' grammar of sequences, never evidence about a link (METHODOLOGY §3) |
| seed votes | evidence, as their own rater (§6c) |
| the muse family (Glimmer, 257 triad-era answers) | evidence, its own rater |
| duplicate answer IDs | one record per ID (46 triad-era records were identical repeats) |

`GAP` in a `between` context is a structure, not a glyph.

## 6. The model

### 6a. Two quantities per part

Every part of a record carries both quantities. They are never collapsed into one.

- **Strength** is how strongly the minds converge, beyond the matched control. Per rater it is the rate beyond the control's rate, as a share of what is possible beyond it: Abbott's correction, $(p - c)/(1 - c)$. It is combined over raters as in §6c, with its interval.
- **Certainty** is how sure we are that the strength is above zero: a weight of evidence in decibans, itemised by answer.

A run at 60% and a run at 95% both become certain as answers accumulate; only strength keeps them apart. Certainty also grows with how often a run was asked, which the planner chooses. METHODOLOGY §2a: *"Agreement is the perceptual quantity … The interval is how sure we are of it"*. Joseph, 2026-10-06: *"side-by-side is canonical."*

### 6b. Parts: each claim with its own contrast

There is no single "false" population. What a "yes" is worth depends on what it is contrasted with. Claude calls shuffled runs coherent 21% of the time, chart windows 84%, and real candidates 75% [measured, the audit]. So each part names its contrast and takes its own control:

| part | claim | evidence | contrast / control |
|---|---|---|---|
| **R-shuffle** | this order of these glyphs is recognised | cohere | the same glyphs shuffled |
| **R-chart** | recognised beyond what code-point order alone explains | cohere and order questions on runs whose visible order and code-point order disagree | the same glyphs in code-point order (a new control; §11) |
| **O** | the set is ordered this way | order lines and triads, through an ordering model (§6e) | lines and middles that break the order; "only two", "none" |
| **L-near** | `x` comes directly after `c` | inhibit | near decoys (same chart neighbourhood) |
| **L-skip** | `x` comes *directly* after, not just later | inhibit | skip tests (the glyph two steps on): plausible, in-sequence, wrong |
| **G** | minds produce `x` after `c` unprompted | continue (shown), picks; written answers as one unit per answer (§6d) | a measured likelihood of being named (§6d) |
| **Seed** | a surveyor proposed this run | seed votes | its rater's reliability, estimated from the other parts (§6c) |

**How Joseph's ordering is applied:**

- **Intuitive** recognition is R-shuffle, L-near and G evidence from raters in conditions without deliberation (§6c), together with R-chart wherever its control exists.
- **Rational** recognition is the same parts from deliberating raters (thinking on, reasoned).
- **Chart-borne** recognition is a run whose R-chart part is near zero while R-shuffle is high. It is recognised because the chart is in order.

Every record also carries a descriptive **chart-congruence** fact: whether the run is monotone in code points, and its largest code-point step. It is a fact, not a part, and it lets a read-off show chart-borne runs as such.

### 6c. Raters: minds in conditions, pooled toward their family

Within Claude, "yes" to shuffles runs from 0.11 (Sonnet) to 0.34 (Haiku with thinking off). On near decoys it runs from 0.002 to 0.061 [measured, the audit]. So:

- **A rater is a mind in a condition:** thinking budget, effort, prompt variant, protocol era. Seed sources (per surveyor) are raters too, and so is Joseph when he proposes a run.
- **Pooling.** Raters are pooled toward their family with a hierarchical prior, so a thinly observed rater borrows strength from its siblings. A family with many minds can't outvote another by volume: each family's pooled contribution enters once, weighted by its own measured discrimination.
- **Rates come from data.** Each rater, on each part, has a true-positive and a false-positive rate per response category: yes, no and can't tell (Dawid–Skene with three categories, fitted by EM). The false-positive rates come from that part's own controls. The true-positive rates come from items the other parts and raters support, with held-out controls used to check calibration (§12).
- **Conditions as measurements.** Whether a condition matters (thinking off against on, low effort against medium) is read off the fit, not assumed. This answers METHODOLOGY §4's question of whether the thinking budget is a probing factor.
- **Seeds.** Seeds weigh as their measured reliability says, which may be more than an ordinary generator: Joseph, *"it can weigh slightly more than the usual generative mind's sequence, and it has more n-gram length to work with."* A survey seed is reasoned generation, so it counts fully as recognition and less as evidence that the recognition is intuitive.
- **Rater-by-item effects are findings, not noise.** Gemini Flash leaving `▁` out of the fill ramp, probably for tokenizer reasons (OBSERVATIONS, 2026-10-04), is an example. Residual checks (§12) flag items where one rater departs from its own rates, and they are listed, not absorbed.

### 6d. Generation, one-way, with a measured likelihood

Generation is evidence one way (METHODOLOGY §2a): naming `x` counts for `c → x`, and not naming it is never a rejection. Rather than assert that rule, the catalog measures it.

- **The likelihood of being named.** For links that the other parts recognise, how often are they named at their context? From the audit's first look, the median share of first continuations naming such a link is 0.5, and 14% are never named. G's weight for a link is the likelihood ratio of its naming counts under that distribution against the distribution for links the other parts reject. So "not named" becomes weak evidence, of a size the data set, and the morph case (recognised, rarely named) stays recognisable.
- **Branch shares.** At each context, the share of answers naming each continuation, "end" included. These come from interpolated Kneser–Ney, which is closed-form, deterministic and recomputable from counts. Raw per-context counts sit beside them for k\* and stability.
- **Written answers.** One continue answer that writes a 24-glyph chart walk is one piece of evidence about that run, not 23 independent links. Written continuations enter G clustered by answer.
- **No continue null exists yet.** The only nulls are forced picks at medium effort, a different condition. A continue null needs tagged random contexts asked the continue way, a probing addition (§11).

### 6e. Order of a set: triads and order lines

Triads and order lines are evidence about the **order of a set**, not about adjacency (METHODOLOGY §6: *"A middle says `q` lies between `p` and `r`, not that `q` is adjacent to either"*). They enter part O through a model of orderings: a Mallows or Plackett–Luce likelihood of each rater's middles and lines given a hypothesised order. "Only two", "none" and "extra" are their own outcomes. Two consequences:

- **Every asked triple counts**, consecutive or long-range, so the long-range triads the triad era asked bear on a run.
- **Nothing becomes a transition prior.** No pseudo-counts are added to generation.

The triad era's knowledge comes back by two routes: its rows and chains are *candidates* (§3), and its triads and lines are *evidence of order* (O). Neither is evidence of adjacency.

### 6f. Dependence

Where independence is assumed, the record says so. The known dependencies and how each is handled:

| dependence | treatment |
|---|---|
| within a family; minds in conditions | hierarchical pooling (§6c) |
| one written answer, many links | clustered: one unit per answer (§6d) |
| nested contexts | none: each context is its own proposition (§4) |
| a link inside many runs | the evidence table records it; a run's parts use its own whole-run evidence, and its links' parts are reported, not multiplied (§7) |
| across channels within one mind | parts are kept apart, so a mind's continue, pick, inhibit and cohere answers about one run aren't summed into one certainty |
| errors correlated across families (all learned the Unicode charts) | the R-chart part: cross-family agreement on chart walks earns nothing there |
| within a sheet (position, size, neighbours) | tagged; estimated as rater-condition effects (§6c) |

## 7. Untested is a state

Every link in a record carries one of three states:

- **evidence at its own context**, from any part;
- **evidence only at a suffix** (shorter context): reported as such, never substituted;
- **none.**

A run's record lists its untested links. No prior, backoff or neighbouring evidence fills them in. A run's parts are never a product of link probabilities. That product would penalise length ($0.95^{20} \approx 0.36$), against Joseph's direction that length organises and does not rank. It would also pull a long run with one untested link toward the prior. A run's parts come from whole-run evidence (R, O), and its links are summarised as counts by state and the weakest supported link.

## 8. A record

Each record (a link, run, cycle or branch) carries:

- **Identity:** canonical form, glyphs, kind, containment and branch relations.
- **Parts (§6b):** strength and certainty for each, with per-rater contributions.
- **Facts:** chart congruence, coverage per part (answers per rater), link states (§7).
- **Evidence:** the answer IDs behind every number.
- **Model version** and the fitted rates it was scored under.

## 9. Readers

- **Priority (3)** reads parts and their certainty. The most valuable next question is the one most likely to move a record's *intuitive* parts: R-chart controls for chart-congruent candidates, conditions without deliberation, untested links inside strong runs. Replacing the hand-set tiers with this is for METHODOLOGY §5 to decide and Joseph to ratify.
- **Read-offs (5).** BEST becomes a view of the catalog, showing strength and certainty side by side. Its ranking key is its own, and one overall number only if Joseph asks for one.
- **Probing (1)** receives the condition and sheet-position findings (§6c).

## 10. Engine and determinism

**Size.** Through c090 there are about 143,500 real answers. The rest of the ~251,000 records are failures (§5). Postgres 18.6 runs locally (`psql-18`). This is small for it.

**Shape:**

- **`answers`:** loaded from `data/answers/*.jsonl`, one row per answer ID. The JSONL ledgers stay the truth.
- **`evidence`:** one row per (part, proposition, answer, rater), with its contribution.
- **`raters`, `rates`:** the fitted rates per model version.
- **`records`, `relations`:** the catalog.
- **Builds.** Each build is written into a versioned schema, and an atomic switch makes it current, so readers always see a whole build.

**Determinism:**

- **A manifest:** the hashes of every input file, the Unicode version and the model version, stored with the build.
- **Closed form where possible:** Kneser–Ney for branch shares, EM with a fixed initialisation, a fixed order and a stated tolerance for the raters.
- **Sums** are done in Python in a fixed order (or as `numeric`), never by a parallel float aggregate.

**Reference implementation.** The JSONL-over-Python path stays as the reference until the database reproduces it record for record.

## 11. Probing additions it needs

- **The R-chart control.** Runs whose visible order and code-point order disagree, asked both ways: in the run's order, and with the same glyphs in code-point order. For cohere and the order question alike. Candidates come from recognised runs that aren't monotone in code points, and from places where the picks preferred the chart (the canary: after `🮄`, `🮃` ×8, `▀` ×2).
- **A continue null.** Random contexts asked the continue way, tagged as nulls.
- **Order-question nulls.** Sets with no order, so part O has a false-positive rate.

## 12. Before building

**A fresh de novo audit of this version.** It is briefed only that the design is new and unbuilt.

**Acceptance tests, stated before the build:**

1. **Determinism.** Rebuilding from the same manifest gives identical catalogs.
2. **Calibration on held-out controls.** Fit each part's rates on half its controls; the other half must score at its own false-positive rate within the interval.
3. **The canary, positively.** On the intuitive parts, `▁ ▂ ▃ ▄ ▅ ▆ ▇ █` and the top-down `█ 🮆 🮅 🮄 ▀ 🮃 🮂 ▔` must rank in the upper quarter of recognised runs of their length band, and so must the full cycle once its answers are in.
4. **The canary, negatively.** Chart walks the study treats as chart-borne (`🨀 🨁 🨂 …`, the `Ý Þ ß à` crossing) must score lower on R-chart than the felt runs of test 3. This test needs §11's control, and it is the reason to build that control first.
5. **The triad era accounted for.** All 4,905 distinct rows grown in r004–r012 are records with parts, or each is explained.
6. **Agreement with what is plain.** Where BEST's current recognised and rejected sets rest on plain evidence, the catalog agrees, and every disagreement is explained.
7. **Hand audit.** For a sample of records, recomputing each part from the listed answers and rates gives the stored numbers.
8. **Posterior predictive checks.** The rater model reproduces the observed spread of yes counts per item. Overdispersion is reported, not hidden.
9. **Stability.** Records' parts move little when one more round is added, and the top of each section is insensitive to which half of the controls was used.

## 13. Changes from version 1, by audit finding

- **F1, the contrast class.** Parts with their own controls (§6b); the R-chart part and its control (§11); chart congruence as a fact.
- **F2, raters.** Minds in conditions, pooled toward families; three response categories; rater-by-item residuals listed (§6c).
- **F3, generation.** No Pitman–Yor posterior. A measured one-way likelihood (§6d), Kneser–Ney branch shares, raw counts per context. The continue-null claim is removed and the null is listed as needed (§11).
- **F4, triads.** Evidence of order through an ordering model (§6e), never an adjacency prior.
- **F5, the run layer.** Stated enumeration rule, containment and branches (§4); no length bound on runs; no product of links; untested as a state (§7).
- **F6, two quantities.** Strength and certainty side by side (§6a).
- **F7, dependence.** The table in §6f.
- **F8, inputs.** §5; size corrected (§10).
- **F9, seeds.** Restored as evidence, as a rater (§3, §6c).
- **F10, cycles.** METHODOLOGY §3's definition and manifestation rule (§4).
- **F11, tests.** Rewritten (§12).
- **F12, references.** "METHODOLOGY §n" throughout; the probing reader added (§3, §9); the precedent addressed (§1).
