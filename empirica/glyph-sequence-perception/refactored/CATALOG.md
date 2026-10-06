# CATALOG: the canonical catalog of sequences

*Design, 2026-10-06, by the independent session (Claude Opus 5.5) with Joseph. Not built. A proposal to be critiqued before any of it is built (§9). METHODOLOGY §2a lists it as concern 6.*

## 1. Why

METHODOLOGY §2a says that sequences, branches, ends, cycles and stability are *read off* the tree. What exists instead is a sound store of raw answers indexed by context, and readers that each derive sequences their own way:

- the tree's walks;
- the planner's walks, root lists and branch draws;
- BEST's strongest-branch paths, folding and ranking;
- the triad chains written on 2026-10-06.

Each is a different partial model of one question, and each correction in one reader has exposed a loss in another. In two days:

- **Majority rule.** BEST confirmed links by majority in continue answers alone, so a "none" counted against a link. Morph ladders such as `-=>})|` disappeared.
- **Merging.** BEST merged overlapping runs into 190-glyph monsters.
- **Ranking.** Sorting by length hid every short cross-block run. Equal family weighting ranked a run two families confirmed below one only Claude had answered.
- **The cap at 8.** Pick contexts were silently capped at 8 glyphs, so the tendrils stopped there.
- **The triad era's rows.** The tree used its 19,665 ported triads only to test runs found otherwise. 232 of the triad era's 300 top rows appeared nowhere, Joseph's block-fill cycle `▁▂▃▄▅▆▇█🮆🮅🮄…` among them.

Joseph, 2026-10-06:

> *"would it make sense … to somehow create a script that gives a 'canonical' source of all 'possibly meaningful sequences + cycles', deduplicated, same-directioned, canonical starting point for cycles, every plausible branch getting its own 'record', and the edges in the chain being determined from the raw data in a defensible and proper way, auditable, giving the ultimate score for that branch/sequence etc.? (I'll bet, for example, you could figure out the bayesian prior from the triads that is more defensible n-gram branching chains) … or is that what context-tree was already supposed to be and we basically have a 'raw-data context-tree' and a 'canonical statistically sound context-tree' maybe?"*

That is the diagnosis. There should be two layers:

1. **The raw context tree** (concern 2): answers, tagged, nothing derived.
2. **The catalog** (concern 6): derived once from the raw tree by one stated statistical model.

Joseph again: *"It gives us an additional distinct concern but should actually end up being (if done right) the more correct* input *to the probing concern and the rating+extraction (best/reading) concern."*

## 2. Where it sits

```
probing (1) ──answers──▶ raw tree (2) ──▶ CATALOG (6) ──▶ priority (3): what to ask next
port (4) ────answers──▶       │                     └──▶ read-offs (5): BEST, SEQUENCES, PROGRESS
```

- **What it reads.** The catalog reads only answer records and their tags, never `source` (why a question was asked), as the tree does.
- **Rebuildable.** It is deterministic: the same answers and the same model version give the same catalog, byte for byte.
- **Its readers.** The planner and the read-offs read the catalog, not the raw tree, for anything about sequences. The planner may still read raw facts it needs to avoid repeating a question, such as which contexts were asked.
- **Separation is kept.** The catalog knows nothing of priority or display. A reader that wants a different view, such as BEST's length sections, makes it from catalog records, never by re-deriving links.
- **Seeds are never evidence.** Survey seeds, dropspot seeds and the triad era's grown rows (`../data/growth/*.json`) may enter only as *candidate propositions*: things the catalog scores. Evidence comes from answers alone.

## 3. Objects and canonical forms

- **A link** is `c → x`: glyph `x` comes directly after context `c`, an oriented run of 1–24 glyphs. Links at different contexts are different propositions, as in the tree. A link at a long context is not the same claim as at its suffix.
- **A run** is an ordered list of distinct glyphs. A run and its reverse are one sequence (§2). Its **canonical orientation** puts first whichever end gives the smaller tuple of code points. A display may reorient it; ascending numeric value is BEST's habit.
- **A cycle** is a run whose last glyph is followed by its first, with ≥ 4 distinct glyphs (§3). Its **canonical form** is the smallest code-point tuple over all rotations of both orientations.
- **A branch record** is a run that shares a prefix with another run and then continues differently. It records the branch point (the shared context) and the glyphs that separate them. Every plausible branch is its own record, and nothing is folded away.
- **Containment** (one run inside another) is a stored relation, not a deletion. Readers decide what to show.

## 4. Evidence channels

Every answer becomes one or more evidence rows about propositions.

| channel | asked | the answer says | about | negative evidence | its control |
|---|---|---|---|---|---|
| continue, shown | what comes next? | first glyph `x` | link `c → x` | none: the answer gives evidence about an end, not against `x` (§2a) | null contexts; chart neighbours |
| continue, written | (later glyphs of an answer) | `x` after a context the mind wrote itself | link | as above | as above |
| pick | a single character that extends it (forced) | `x`, sampled | link | as above | null contexts asked the same way |
| inhibit | does `x` come directly after? | yes / no / can't tell | link | "no" | near and far decoys |
| cohere | does this look like a coherent sequence? | yes / no / can't tell | run | "no" | the same glyphs shuffled; chart windows (a measurement) |
| order | put this set in order | lines, ties, gaps, extra, none | run, adjacent pairs, set | none; extra; lines that break the order | sets with no order (to build) |
| triad | which is in the middle? | middle / only two / none | triple (betweenness) | another middle; none | (none yet) |
| next, between | (triad era) | proposals | link; two-sided fill | none | none |

Reflections (§3) are kept apart and never grow a sequence.

## 5. The model

### 5a. Weight of evidence

Every proposition `H` (a link is felt; a run is recognised) carries log-odds. Each piece of evidence `E` adds its **weight of evidence**, the log likelihood ratio (I. J. Good; Turing's decibans):

$$\log\frac{P(H \mid E_1 \ldots E_n)}{P(\lnot H \mid E_1 \ldots E_n)} = \log\frac{P(H)}{P(\lnot H)} + \sum_i W(E_i), \qquad W(E) = \log\frac{P(E \mid H)}{P(E \mid \lnot H)}$$

This is the audit form Joseph asked for. A link's score is a sum, and each term is an answer or a group of answers, so a record can list *why* it has its score, channel by channel and family by family. The sum assumes the pieces are conditionally independent given `H`; §5f says where that fails and what is done about it.

### 5b. Raters: families as noisy judges (Dawid–Skene)

Each family `f` answering a yes/no channel `k` (inhibit, cohere, and order or triad recast as "matches the proposition or not") is a rater with two rates:

- **Sensitivity** $s_{fk} = P(\text{yes} \mid H)$.
- **False-positive rate** $e_{fk} = P(\text{yes} \mid \lnot H)$.

A "yes" then weighs $\log(s/e)$, and a "no" weighs $\log((1-s)/(1-e))$. "Can't tell" weighs 0.

- **The false-positive rates come straight from the controls.** Shuffles measure $e$ for cohere: Claude 0.21, Grok 0.39 so far. Near decoys measure it for inhibit. The study already collects these; it has simply never used them as rates.
- **The sensitivities are estimated** by expectation–maximisation over all propositions at once (Dawid & Skene 1979). The controls anchor what would otherwise be unidentifiable.
- **Family weighting falls out of the data.** A family that discriminates well (high $s$, low $e$) weighs more, and one that says yes to everything weighs little. Joseph: equal family weighting *"was never a goal so much as a choice given no other understanding."*

### 5c. Generation: a predictive context tree

Continue answers and picks don't say yes or no. They name one continuation among many possible ones. The principled model for "what comes next after this context" over a context tree is a **hierarchical Pitman–Yor process**: each context's distribution over next symbols backs off to its suffix's distribution, down to a base distribution. This is Teh's hierarchical Pitman–Yor language model (2006) and the "sequence memoizer" of Wood et al. (2009), which is exactly a statistically sound variable-order context tree.

- **The categories** at each context are every glyph named there plus "end" (a "none").
- **Branches** are the categories with real posterior mass. A context whose distribution is flat against the null contexts is the high-entropy case of METHODOLOGY §4a.
- **One-way evidence (§2a).** Naming `x` is evidence for `c → x`: its weight is the posterior probability of `x` at `c` against the probability the null contexts give a named glyph. Not naming `x` lowers only `x`'s share, never below the prior, because a valid continuation can lose to a valid branch.

### 5d. Joseph's triad prior

*"I'll bet, for example, you could figure out the bayesian prior from the triads that is more defensible n-gram branching chains."*

A triad answer says `y` lies between `x` and `z`, a statement about the second-order transition `x y → z` (and `z y → x`). So triads give the hierarchical model its prior pseudo-counts at contexts ending `x y`:

$$\alpha_{xy \to z} = \lambda \cdot b(y \mid x, z)$$

Here `b` is the betweenness support (the estimated share naming `y` the middle of `{x, y, z}`, per family, combined as in 5b). Order lines add the same for each adjacent pair in a line.

The concentration `λ` is not chosen. It is fitted by empirical Bayes, maximising how well the prior predicts held-out continue and pick answers. If the triads say nothing about generation, the fitted `λ` goes to zero, and that is itself a finding.

This is how the triad era's knowledge comes back. Its 19,665 triads shape every two-glyph context's branching, so `█ 🮆 🮅 🮄` gets prior mass from the triads that found it, even where generation answers "none".

### 5e. A run's score

Recognition is the goal (METHODOLOGY §1). A run's catalog score is the posterior log-odds that it is **recognised as a sequence**. Three kinds of evidence go into it:

- **Whole-run evidence:** cohere answers and order lines for its exact set, weighted as raters (5b).
- **Its links:** each link's posterior from 5b and 5c. A run is a sequence only if every link is felt, so the links enter as the probability that they all hold.
- **Its triples:** betweenness for each consecutive triple.

Every record also keeps the parts apart:

- recognition (whole-run channels);
- generation (the path's probability under 5c, as mean log-probability per step);
- betweenness;
- per-family weights of evidence;
- answer counts.

A reader can then rank by the overall score and still show where it comes from. "Recognised but not generated" (the morph case) is visible as a strong recognition part with a weak generation part.

### 5f. Dependence, and what is done about it

The sum in 5a overcounts correlated evidence. The known correlations:

- **Within a family.** Two Claude minds aren't independent raters, so the family is the rater (5b). Repeated answers by a family to one proposition enter as a beta-binomial count, not as independent votes.
- **Within a sheet.** Answers on one sheet share a context. The sheet position and size are tagged, and their effect can be estimated and, if real, modelled.
- **Nested contexts.** A link at `a b c` and at `b c` aren't independent claims. The hierarchical model (5c) handles that by construction.
- **Links within a run.** Link evidence and whole-run evidence partly restate each other. The run score combines them by the rule stated in 5e (all links hold, and the whole is recognised) rather than by adding them twice.

Where a correlation isn't modelled, the record says so. A weight of evidence that rests on an independence assumption carries a flag.

## 6. A record

Each catalog record (a link, run, cycle or branch) carries:

- **Identity:** canonical form, glyphs, kind, containment relations.
- **Score:** posterior log-odds and probability, the overall score.
- **Parts:** recognition, generation and betweenness, each with its weight of evidence in decibans, per family.
- **Evidence:** the answer IDs behind every term, so any number can be recomputed by hand.
- **Coverage:** answers per family and channel. Absent evidence is shown as absent, never as zero.
- **Model version** and the fitted rates (`s`, `e`, `λ`, discount and strength) it was scored under.

## 7. Engine: Postgres 18

The engine is a separate question from whether the statistics are right. It matters because a fast, transactional store makes the weights easy to inspect, change and audit. Joseph: *"having it lightning fast and the underlying model with certain ACID properties or something might allow for ideation on the WoE edge-weight side to be a lot more smooth and easy to communicate, implement, and audit."*

**Size.** Through c085 there are 237,734 answer records (~229 MB of JSONL): 114,162 continue, 33,717 cohere, 23,379 triad, 22,465 pick, 21,432 inhibit, 10,111 order, 6,248 next, 1,370 between and 4,850 seed votes. Postgres 18.6 runs locally (`psql-18`). This is small for it.

**The proposed shape:**

- **`answers`:** the canonical records, loaded from `data/answers/*.jsonl`, immutable, keyed by `aid`. The JSONL ledgers stay the truth; the table is rebuilt from them.
- **`evidence`:** one row per (proposition, answer): channel, family, outcome, and the weight of evidence under the current model. A view sums it into each proposition's score, which is the audit trail itself.
- **`rates`:** the fitted rater rates and hyperparameters, per model version.
- **`links`, `runs`, `members`:** the catalog records. Paths of ≤ 24 glyphs over these are recursive common table expressions; no graph database is needed at this size. (Apache AGE adds graph queries to Postgres if that ever changes.)
- **The model fitting** (EM for the raters, the Pitman–Yor fit) runs in Python with numpy and writes a build back in **one transaction**. Readers always see a whole build, never a half-written one, and builds can be compared by version.

The JSONL-over-Python path stays as the reference implementation until the database reproduces it, record for record.

## 8. Readers once it exists

- **Priority (3)** reads scores and their uncertainty. The most valuable next question is the one that would move a promising record's score most (expected information gain), which replaces the hand-set tiers and shares over time. That change is for METHODOLOGY §5 to make, and for Joseph to ratify.
- **Read-offs (5).** BEST becomes a view of the catalog: sections, sorting and marks over records whose scores come from 5e. SEQUENCES and PROGRESS do likewise.
- **The canary.** The acceptance test for the whole design is in §9.

## 9. Before building

**An independent critique of the statistics.** An agent that hasn't written this design, briefed with it and the raw answer format (via `~/src/arch/SPIKE-PROMPT.template.md`), says where the model is wrong, weakly identified or overclaimed. The author is not the only verifier of their own model.

**Acceptance tests, stated before the build:**

1. **Determinism.** Rebuilding twice gives identical catalogs.
2. **Controls score as controls.** Shuffled runs, decoys and null contexts get low scores, at the rate their own families produce false positives.
3. **The canary.** `▁ ▂ ▃ ▄ ▅ ▆ ▇ █` and the top-down `█ 🮆 🮅 🮄 ▀ 🮃 🮂 ▔` appear as records with their evidence, and the full cycle is scored once its answers arrive.
4. **The triad era accounted for.** Every one of the 4,905 distinct rows grown in r001–r012 is either a catalog record with a score or explained. In particular, so are the 232 top rows the current pipeline lost.
5. **The links agree with what is already known.** Where BEST's current verdicts rest on plain evidence (a link every family names), the catalog agrees; where it disagrees, the disagreement is explained.
6. **Audit by hand.** For a sample of records, recomputing the score from the listed answers and rates gives the stored number.

## 10. Open questions

- **The run's prior** (the base rate of "a run is a sequence") and the link's prior. These can be fitted from candidates of each source, or stated.
- **Order lines with ties and gaps** as evidence about a run: a tie is a claim about steps; a gap is a claim that a glyph is missing.
- **Chart order versus felt order.** The whys say both families often recognise runs *by the code chart*. Whether a chart-based "yes" should weigh as recognition for signa is Joseph's call. The catalog can carry it as a separate part if the order question on sets where chart order and visible order disagree gives a measurement.
- **The thinking budget as a rater condition.** Is the same family at another effort a different rater?
