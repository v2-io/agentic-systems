# CATALOG: the canonical catalog of sequences

*Design, version 3 (2026-10-06), by the independent session (Claude Opus 5.5) with Joseph. Not built. Earlier versions were audited de novo: version 1 in `audits/catalog-design-2026-10-06.md` (findings F1–F12), version 2 in `audits/catalog-design-v2-2026-10-06.md` (A1–A11). §14 maps each finding to what changed. A fresh audit of this version comes before anything is built. METHODOLOGY §2a lists the catalog as concern 6. "METHODOLOGY §n" refers to that file; a bare "§n" is a section of this one.*

## 1. Why

METHODOLOGY §2a says that sequences, branches, ends, cycles and stability are *read off* the tree. What exists instead is a sound store of raw answers indexed by context, and readers that each derive sequences their own way: the tree's walks, the planner's walks and branch draws, BEST's paths, folding and ranking, and triad chains. Each is a partial model of one question, and each correction in one has exposed a loss in another:

- **Majority rule.** BEST confirmed links by majority in continue answers alone, so a "none" counted against a link, and morph ladders such as `-=>})|` disappeared.
- **Ranking.** Sorting by length hid every short cross-block run.
- **The cap at 8.** Pick contexts were silently capped at 8 glyphs.
- **The triad era's rows.** Of the 300 rows of the triad era's last STANDINGS.md (r012), 232 appeared nowhere. Joseph's block-fill cycle `▁▂▃▄▅▆▇█🮆🮅🮄…` was among them.

Joseph, 2026-10-06: *"we basically have a 'raw-data context-tree' and a 'canonical statistically sound context-tree' maybe?"*

**A precedent, and what is different this time.** The triad era also had a global fit that ordered glyphs. It *"dropped/merged valid creative sequences"* (commit `b1a78dbe`), placed glyphs arbitrarily on links nobody had asked (OBSERVATIONS, 2026-10-04), and was demoted to a guess-proposer. What differs:

- Evidence is answers only, and every number is itemised to them.
- An untested link is shown as untested, never filled in (§8).
- Nothing is folded, merged or cut.
- Each kind of contrast is its own part (§6).
- The model is frozen before the canaries are computed (§13).

## 2. What it is for

Recognition is the goal (METHODOLOGY §1). Joseph has said which recognition matters most:

> *"An interpretable rational sequence (given some thought) is fine. Originally I gave more weight to monotonic perceptual sequences that were also monotonic in chart order / code-point magnitude. … one place where I feel the preponderance of claude models here who find it easy to look at sequences in terms of code-point location is potentially giving us, after everything, a very 'obvious answer -- just do it like the codepoints had it'. It's fine. It's not anything I'm excited about rediscovering. An 'intuitive' sequence that doesn't need internal arithmetic or thinking about the glyph's name and codepoint is (much) better."*

So the catalog sorts recognition into four tiers, ranked in this order. A tier is defined by **what the recognition survives**, not by how much the mind deliberated (§7):

1. **Intuitive.** Recognised, and it holds where the code chart points elsewhere.
2. **Rational.** Recognised, interpretable with thought, and not reached by chart arithmetic.
3. **Chart-congruent, undiscriminated.** Recognised, but the chart and the look agree everywhere, and nothing yet tells them apart. This is an honest state, not a verdict.
4. **Chart-borne.** Recognised only where the chart supports it: it fails where the chart points elsewhere, or it was reached by code-point lookup and not felt.

**Why the roster makes this hard.** Claude gives about two thirds of the answers, and on runs that walk the chart its reasons cite the chart about twice as often as Grok's (0.38 against 0.18; `spikes/whys-basis-2026-10-06/FINDINGS.md`). That's a difference in what the families *say*. Whether it is also a difference in what their judgements rest on is what the discriminator positions (§6c) measure.

## 3. Where it sits

```
probing (1) ──answers──▶ raw tree (2) ──▶ CATALOG (6) ──▶ priority (3): what to ask next
port (4) ────answers──▶       │                     ├──▶ read-offs (5): BEST, SEQUENCES, PROGRESS
                              │                     └──▶ probing (1): measurement findings (conditions, sheet position)
```

- **Inputs.** The catalog reads answer records and their tags, never `source` (why a question was asked). Whatever it needs from that, such as which inhibit questions were skip tests, it derives structurally (§5).
- **Determinism.** The same inputs, recorded as a manifest of file hashes, and the same frozen model version give the same catalog (§11).
- **Readers.** Priority and the read-offs read the catalog for anything about sequences. Strength and certainty sit side by side on every record (§7), and choosing a ranking key is the read-off's job. Joseph: *"side-by-side is canonical."*
- **Candidate inputs** are named propositions to score: survey and dropspot seeds, the triad era's grown rows (`../data/growth/r004–r012.json`), triad chains (`tree.triad_chains`), reasoned continuations, and shuffles a mind called coherent. Of these, **seed votes are evidence, as their own rater** (§7): Joseph's standing direction is that seeds are tagged votes, and *"a mind that generates a sequence recognizes it"*. The others are candidates only.
- **Once built,** its model supersedes the per-reader standard of METHODOLOGY §2a for every reader.

## 4. Objects and canonical forms

- **A link** is `c → x` at its own shown context `c`. Shown contexts run 2–8 glyphs: the probe caps them at 8 (chosen without evidence; it bounds every link's reach). A link at a long context and the same link at its suffix are different propositions, and nothing pools them. k\* and stability (METHODOLOGY §3) read from per-context counts.
- **A run** is an ordered list of distinct glyphs, of any length. A run and its reverse are one sequence (METHODOLOGY §2). Its **canonical orientation** puts first whichever end gives the smaller tuple of code points.
- **Which runs are records:**
  - every candidate input (§3);
  - every run asked whole (cohere or order);
  - every maximal run whose links each have shown evidence at their full prefix, or are **stable** (§8): their suffix evidence was lengthened backward and nothing flipped;
  - every contiguous window of these that was itself asked whole.

  It is a stated rule, not a cut on score. Sub-runs never asked and never proposed are not records, which keeps the count linear in the candidates.
- **Containment** is a stored relation, never a deletion.
- **A branch** follows METHODOLOGY §3: a context (≥ 2 glyphs) at which two continuations each have evidence. A branch record holds that context and its continuations, and two runs are related as branches when one of them passes through it.
- **A cycle** follows METHODOLOGY §3: a path returning to a context state with every step determined, so a period may repeat glyphs, and it counts once a mind has *manifested* it. Its canonical form is the smallest code-point tuple over all rotations of the period, in both orientations. **Manifestability is bounded by the caps.** A mind manifests a period P by writing 2P minus the shown glyphs, at most 24 written from at most 8 shown, so P ≤ 16. The record says so.
- **Long runs.** Whole-run questions show at most 24 glyphs. A longer run's whole-run evidence comes from its windows that were asked, and the record shows which stretches are covered.

## 5. Inputs: which records count

| records | how they enter |
|---|---|
| real answers: continue, pick, inhibit, cohere, order, triad, choose, next | evidence, by part (§6) |
| `between` (1,370, triad era: two-sided fills) | a part of its own, B (a two-sided fill at a gap), at the rational tier; never a link |
| `call-failed`, including reason `limit` (usage limits); about 107,000, nearly all from the void rounds c028–c079 | excluded: a failure is no answer |
| `tool-attempt` (673) | its own outcome: a measurement about the rater (METHODOLOGY §4), not about a link |
| `unparsed`, `other`, unassigned code points | their own outcomes. A continuation into unassigned code points is a marker of code-point arithmetic for its run (§6c) |
| a continuation that reaches the 24-glyph cap | **censored, not ended**: no "end" is read from it |
| reasoned answers (`sonnet55r`) | by what they contain (`spikes/reasoned-pass-2026-10-06/FINDINGS.md`): continuations reached by code-point lookup mark their link **chart-reached** (§6c); "none" is end evidence at the rational tier; continuations are candidates; never evidence of a felt link |
| reflections | apart: the minds' grammar of sequences (METHODOLOGY §3) |
| seed votes | evidence, as their own rater (§7), **clustered by seed**: one survey sequence yields votes at every prefix, and they count as one unit |
| duplicate answer IDs | one record per ID (46 triad-era records were identical repeats) |

**Controls are identified structurally,** not from `source`:

- A **skip test** is an inhibit whose candidate is the glyph two steps on in the record's own run.
- A **shuffle** carries `tags.control: shuffled`, and is paired with runs by glyph set. Reordered candidates share their original's glyph set, so the pairing is many-to-many and is stored as such.
- **Chart windows** are `tags.control: chart`.

**Joseph's and the dropspot seeds** reach the planner but are not yet answer records. Porting them as tagged votes (`port/port_seeds.py` reading the dropspot) is a prerequisite, so that "Joseph when he proposes a run" has an input.

## 6. Parts: each claim with its own contrast

### 6a. The parts

| part | claim | evidence | contrast / control |
|---|---|---|---|
| **R** | this order of these glyphs is recognised | cohere | the same glyphs shuffled, with false-positive rates **by chart class** (contiguous, monotone, other), since Claude says yes to 0.13, 0.20 and 0.28 of their shuffles respectively |
| **O** | the set is ordered this way | order lines and triads, every asked triple (§6d) | lines and middles that break the order; "only two", "none", "extra" |
| **L** | `x` comes directly after `c` | inhibit | near decoys, and skip tests: an upper bound on the false-positive rate, since the glyph two on is sometimes right (`▁ ▃ ▅ ▇` is a sequence too) |
| **D** | at this position, the look (or meaning) wins over the chart | choose: a forced choice between the chart's next glyph and another | the 0.5 baseline; the two are shown in a fated order |
| **G** | minds produce `x` after `c` unprompted | continue (shown), picks, `next` (rank kept); written answers as one unit per answer | a measured likelihood (§6e) |
| **B** | `x` fills the gap between two runs | between | none yet |
| **Seed** | a surveyor proposed this run | seed votes | its rater's reliability (§7) |

### 6b. What R can't say

R measures whether an order is felt beyond its own scramble. Code-point order is a strongly felt order, so chart walks lead on R by construction:

| family | contiguous runs | monotone | other |
|---|---|---|---|
| Claude, yes | 0.97 | 0.79 | 0.59 |
| Grok, yes | 0.96 | 0.88 | 0.75 |

No false-positive rate changes that ordering. So R contributes to recognition, but never to telling the intuitive tier from the chart tiers. That job belongs to D and the markers in §6c.

### 6c. Telling the look from the chart

These instruments are behavioural, and they come from questions separate from any reason a mind states.

- **D: discriminator positions** (built 2026-10-06, the `choose` question). At a context, a forced choice between the chart's next glyph and an alternative. Positions come from two sources:
  - **Steps inside known runs** where the run's next glyph isn't the chart neighbour: `▁ … █ → 🮆` against the chart's `▉`, and `🮄 → ▀` against `🮃`.
  - **Contexts where answers split** between a chart-adjacent glyph and another.

  D's strength for a run is its preference for the run's own glyph over the chart's, per rater, combined as in §7.
- **Lookalike substitution** (to build). One glyph of a monotone run is replaced by a near-identical glyph from another block, so the chart order breaks and the look doesn't. If recognition survives, the chart wasn't needed. The source of lookalikes would be Unicode's own confusables data, a published, principled list, not a hand pick.
- **The unassigned marker.** Continuations into unassigned code points at a run's open ends are "a clean marker of code-point arithmetic" (METHODOLOGY §4) for that run.
- **Chart-reached links.** A continuation reached by a reasoned mind after a code-point range lookup, at a point where first-impression minds stopped.
- **A class-level control for monotone runs.** Chart windows (contiguous code-point runs from elsewhere) draw yes 0.84 (Claude) and 0.82 (Grok). A monotone run's R against that rate is a weak but real chart contrast; weak, because both sit near the ceiling.

**How the tiers are assigned** (§2):

1. A run whose D positions prefer its own glyphs, or whose lookalike substitution leaves it recognised, is **intuitive** where its recognition holds.
2. A run with no discriminator position and no substitution yet is **chart-congruent, undiscriminated**.
3. A run whose D positions prefer the chart, or whose links are chart-reached, or whose ends draw unassigned continuations, is **chart-borne** at those points.
4. A run recognised with deliberation, not chart-reached, and not discriminated is **rational**.

Each assignment lists the instruments that made it.

### 6d. Order of a set

Triads and order lines are evidence about the **order of a set**, not adjacency (METHODOLOGY §6). They enter O through a model of orderings: a Mallows dispersion or Plackett–Luce worths, from each rater's middles and lines given a hypothesised order. Every asked triple counts, long-range ones included, and nothing becomes a transition prior.

### 6e. Generation, one-way, calibrated without selection

Generation is evidence one way (METHODOLOGY §2a). G's weight is the likelihood of a link's naming counts, under the naming distribution of links recognised by other parts, against that of links they reject. Two corrections from the v2 audit (A6):

- **Calibrate on unselected links.** The links used must have had their recognition question chosen independently of their generation. The largest class of recognised links (`recognize-written`) was asked *because* generation had stopped there, which would bake "not named" into the recognised distribution. Usable sets: the tendril branches (asked whatever their generation), and a tagged random sample of recognition targets going forward.
- **Carry the reason for asking into tags.** It has to be in `tags`, not `source`, so the catalog can condition on it.

Branch shares at a context are the **raw shares**, per rater and family, with their intervals. There is no smoothing in a record. A smoothed view may exist for priority, labelled as a reader view.

## 7. One model for strength and certainty

For rater $r$ answering item $i$ on a yes/no part, with $c_r$ the false-positive rate (from that part's controls, by chart class for R) and $s_r$ the sensitivity:

$$P(\text{yes}_{ri}) = c_r + (1 - c_r)\, s_r\, \theta_i, \qquad \theta_i \in [0, 1]$$

- **Strength** is the posterior of $\theta_i$: how strongly the item is recognised, graded.
- **Certainty** is the weight of evidence for $\theta_i \gt 0$ against $\theta_i = 0$, at a stated alternative ($\theta_i$ at its posterior mean). It is itemised as each answer's log-likelihood ratio, so a hand audit can reproduce it.
- **"Can't tell"** is a third category with its own rates.
- **Hierarchical priors** on $c_r$ and $s_r$ pool raters toward their family.
- **The family combination rule.** Each family's $\theta_i$ is estimated within the family, and the families are combined as a weighted mean, weighted by their measured discrimination, so a family's answer volume can't outvote another family. The likelihood's own rule, where every answer counts, is reported beside it as the "all answers" view.
- **For the other parts:**
  - D: the preference probability over the 0.5 baseline.
  - O: the ordering model's concentration about the hypothesised order.
  - G: the likelihood ratio of §6e, mapped to the probability of the naming pattern under recognition.
  - Seed: the rater's reliability.
- **Raters** are minds in **assigned** conditions: thinking budget (`haiku45nt` 0, `haiku45` 31000), effort (the generator minds at medium), prompt variant, protocol era. Sonnet's and Opus's zero-thinking sheets are *their own choice per sheet*, an outcome of the item, so they enter as a covariate, never as a condition. Deliberation is a measured covariate whose effect is reported, the answer to METHODOLOGY §4's question, and never the definition of a tier.
- **Seed raters** (per surveyor, and Joseph) are not pooled with the first-impression minds of their family.
- **Seeds and the complexity offset** (Joseph: recognition is easier than generation, as verifying is easier than finding). A generator's weight on the intuitive tier is measured per chart class. It is the rate at which raters of a family other than the generator's, in an assigned no-deliberation condition, recognise its runs beyond the class-matched control. It applies only as a prior for runs without whole-run evidence of their own, so the same answers are never counted twice. Until a non-Claude assigned no-deliberation rater answers cohere (Gemini Flash, now answering the new kinds first), it is unidentified for Claude-generated seeds, and stated as such.

## 8. Untested is a state

Every link in a record carries one of four states:

1. **evidence at its own (full-prefix) context**;
2. **stable**: evidence at a suffix, with lengthening tested up to the 8-glyph cap and no flip (METHODOLOGY §3);
3. **evidence at a suffix only**, lengthening untested;
4. **none.**

Nothing fills in states 3 or 4. A run's parts come from whole-run evidence (R, O, D) and its links' states and parts are summarised, never multiplied into a product, which would penalise length.

## 9. A record

Each record (a link, run, cycle or branch) carries:

- **Identity:** canonical form, glyphs, kind, containment and branch relations.
- **Parts (§6):** strength and certainty for each, with per-rater contributions.
- **Tier (§6c)** with the instruments that assigned it.
- **Facts:** chart class, link states (§8), chart-reached links, unassigned continuations at its ends, coverage per part.
- **Evidence:** the answer IDs behind every number.
- **Model version** and the fitted rates it was scored under.

Cycles carry their manifestations per rater (period written twice, after less than one period shown) and R on the period. Branches carry the shares at their branch context.

## 10. Readers

- **Priority (3)** reads parts and tiers. The most valuable next question is the one most likely to move a record out of *chart-congruent, undiscriminated*, or to settle a D position: the purpose stated in §2. Certainty grows with asking, and strength intervals are mildly biased under outcome-dependent sampling. Both are noted wherever priority uses them.
- **Read-offs (5).** BEST becomes a view of the catalog: tiers, strength and certainty side by side, and its own ranking key.
- **Probing (1)** receives the condition and sheet-position findings.

## 11. Engine and determinism

**Data.** Through c094, about 150,000 real answers (the rest of the ~260,000 records are failures, §5). Postgres 18.6 is local.

**Computation lives in Python:** the rater fit, the ordering model and the shares. Postgres stores and serves the results:

- `answers` (one row per answer ID);
- `evidence` (part, proposition, answer, rater, contribution);
- `raters` and `rates`;
- `records` and `relations`.

Each build goes into a versioned schema, and an atomic switch makes it current. With one implementation, parity with the JSONL reference is a load check.

**Determinism:**

- **A manifest:** hashes of every answer file and candidate input (`../data/growth/`, `../data/seeds/`, which HANDOFF schedules to move: hashes don't care, paths do), the Unicode version and the model version.
- **Fits:** EM with a fixed initialisation, order and tolerance.
- **Sums:** in Python in a fixed order.

## 12. Probing additions it needs

| addition | status |
|---|---|
| discriminator positions (`choose`) | built 2026-10-06 |
| lookalike substitution, from Unicode's confusables data | to build |
| **Joseph's basis question.** Asked after the verdict, in a separate turn where the adapter allows. An open prompt first ("what did you notice that made it look that way, or not?"), then plain, even-handed options: how the symbols look / what they stand for or are called / where they sit in the character encoding / can't say / **other: ___**. No value words such as "instinctive" or "immediate". The encoding is named only in the last option. On a fated random half of sheets, so the other half shows whether asking changes the verdict. Its scoring frozen before use. | to build; validated against D, not trusted on consistency with its own reply |
| **Joseph's two-shot framing.** A consent turn, then "immediate impressions … independent of …", with fated variation in the wording, which never names Unicode. A tagged condition whose outcome is the gap between chart classes (contiguous against other), not the yes rate. Its control is a single turn with the same text. | to build; needs multi-turn adapter calls |
| **Thinking text.** Claude's and Grok's adapters don't save it (agy does). A record of the reasoning is stronger than a report about it. | to build |
| the reason for asking, carried in `tags` (§6e) | to build |
| a continue null (random contexts asked the continue way); order nulls (sets with no order) | to build |
| porting Joseph's and the dropspot seeds as tagged votes (§5) | to build |

Two things are out of scope. **Images** (Joseph: *"completely orthogonal to the unicode-token-perception issue we are studying"*). **Earlier minds' reasons**, which are used only in generator passes, from a different family, never as evidence.

## 13. Before building

**A fresh de novo audit of this version.**

**The model is frozen before the canaries are computed.** The parts, strata, priors, combination rule and tolerances are committed with a date, and the canary results are computed after. That order is recorded, so tests 3 and 4 can't be met by tuning.

**Acceptance tests:**

1. **Determinism.** Rebuilding from the same manifest gives identical catalogs.
2. **Transfer of the control rates.** Fit without one whole control class (for example, without chart windows), then predict that class's yes rate from the model's covariates.
3. **The canary, positively.** At its D positions, `▁ ▂ ▃ ▄ ▅ ▆ ▇ █ → 🮆` (against `▉`) and the top-down steps `🮄 → ▀` (against `🮃`), the run's own glyph is preferred over the chart's, and so the canary is assigned the intuitive tier there.
   - **Provenance.** Joseph typed `▁▂▃▄▅▆▇█🮆🮅🮄…`. The completion `… ▀ 🮃 🮂 ▔` is the session's, from his description. A fable-1 survey seed corroborates `🮂 🮃 ▀ 🮄 🮅 🮆 █`, while the triad era's grown row has `▉` and ends at `🮀` or `🮁`.
   - **First look** (a single answer per mind, not a test result). Shown `… 🮄`, the forced picks went to `🮃` (the chart) 8 times and to `▀` twice, so the test can fail.
4. **The canary, negatively.** Chart-borne candidates are assigned the chart-borne tier at their D positions, or by their markers. Examples are `🨀 🨁 🨂 …` and the reasoned `♖ ♕ ♔ → ♓`.
5. **The triad era, informatively.** Of the 4,905 grown rows, the fraction with any whole-run evidence, and what their parts and tiers say.
6. **Agreement with what is plain.** BEST's current recognised and rejected sets: the catalog agrees, and every disagreement is explained.
7. **Hand audit.** For a sample of records, recomputing each part from the listed answers and rates gives the stored numbers.
8. **Posterior predictive checks.** Item-level spread of yes counts against the model, with overdispersion reported.
9. **Stability.** The parts move little when one more round is added.

## 14. Changes, by audit finding

**From version 1's audit (F1–F12)** see version 2's notes, carried forward. In brief:

- contrasts as parts;
- raters as minds in conditions;
- a measured one-way G;
- triads and lines as order evidence;
- a stated run layer;
- strength and certainty side by side;
- a dependence table (now in §6–§7);
- inputs (§5);
- seeds restored as a rater;
- cycles per METHODOLOGY;
- rewritten tests;
- explicit references.

**From version 2's audit (A1–A11):**

- **A1, monotone runs.** D, lookalike substitution, the unassigned marker, chart-reached links, a class-level control, and the "chart-congruent, undiscriminated" tier (§2, §6c).
- **A2, R ranks chart walks first.** Said plainly (§6b): R recognises, but never assigns a tier. Its false-positive rates are taken by chart class.
- **A3, deliberation as a tier.** Tiers are defined by what recognition survives. Deliberation is a measured covariate. Only assigned conditions count as conditions (§7).
- **A4, one model.** The latent-strength model of §7, with the family combination rule stated.
- **A5, Kneser–Ney.** Removed. Raw shares, and a smoothed view only as a labelled reader view (§6e).
- **A6, G's selection.** Calibrated on unselected links; the reason for asking goes into tags (§6e, §12).
- **A7, the 8-glyph cap.** Stated; four link states with the stability bridge; censoring at 24 (§4, §5, §8).
- **A8, inputs.** Reasoned answers decided from what they contain. `next` folded into G, `between` made part B. `limit` is a reason, not an outcome. The dropspot seeds need porting. Seed votes are clustered, seed raters not pooled. Controls are identified structurally, and the skip-control caveat is stated (§5–§7).
- **A9, cycles and branches.** Their parts, and branches per METHODOLOGY §3. Manifestability bounded by the caps (§4, §9).
- **A10, tests.** The canary restated against D. Provenance stated. The model frozen first. Transfer tested. Test 5 made informative (§13).
- **A11.** Priority's target, the manifest, and where computation lives (§10, §11).
- **The seed refinement.** The auditor's sharper wording (§7).
