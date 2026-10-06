# CATALOG: the canonical catalog of sequences

*Design, version 5 (2026-10-06), by the independent session (Claude Opus 5.5) with Joseph. Partly built: builds 0–2 (§13) implement R, the chart route, the view, the link layer (G and L per link, link states) and O (agreement with order and triad answers); nothing reads it yet. The model is not frozen.*

- *Versions 1–3 were audited de novo (`audits/catalog-design-2026-10-06.md`, `…-v2-…`, `…-v3-…`; findings F1–F12, A1–A11, C1–C10).*
- *The v3 auditor checked version 4 against its own findings (`audits/catalog-design-v4-check-2026-10-06.md`: V1, V2, Q1, Q2). §15 maps that check to this version.*
- *The canary's `choose` answers are sealed until the model is frozen (`audits/SEAL-canary-choose-2026-10-06.md`).*

*METHODOLOGY §2a lists the catalog as concern 6. "METHODOLOGY §n" refers to that file; a bare "§n" is a section of this one.*

## 1. Why

METHODOLOGY §2a says that sequences, branches, ends, cycles and stability are *read off* the tree. What exists instead is a sound store of raw answers indexed by context, and readers that each derive sequences their own way. Each fix in one reader exposed a loss in another:

- **Majority rule.** BEST confirmed links by majority in continue answers alone, so a "none" counted against a link, and morph ladders such as `-=>})|` disappeared.
- **Ranking.** Sorting by length hid every short cross-block run.
- **The cap at 8.** Picks were silently capped at 8 glyphs.
- **The triad era's rows.** 232 of the triad era's 300 last STANDINGS rows appeared nowhere, Joseph's block-fill cycle among them.

Joseph: *"we basically have a 'raw-data context-tree' and a 'canonical statistically sound context-tree' maybe?"*

**What is different from the triad era's global fit**, which was demoted after it merged valid sequences and placed glyphs on links nobody had asked:

- evidence is answers only, itemised;
- untested is a state;
- nothing is folded, merged or cut;
- every contrast is its own part;
- the model is frozen before the canary's `choose` answers are looked at.

**What the freeze protects, exactly.** The seal covers the canary's `choose` answers. Its triad, pick and continue answers were public before the seal and are quoted here (§7b, §14). So the freeze guards against tuning on the discriminator answers only. The rules for the other instruments were written with their canary answers in view.

## 2. What it is for

Recognition is the goal (METHODOLOGY §1). Joseph has said which recognition matters most:

> *"An interpretable rational sequence (given some thought) is fine. Originally I gave more weight to monotonic perceptual sequences that were also monotonic in chart order / code-point magnitude. … It's fine. It's not anything I'm excited about rediscovering. An 'intuitive' sequence that doesn't need internal arithmetic or thinking about the glyph's name and codepoint is (much) better."*

So besides *whether* a run is recognised, the catalog measures what the recognition is **independent of**: the code chart and the glyphs' names. These are measured quantities on every record (§7), never labels.

Joseph's sentence gives one clear order: intuitive is (much) better than the rest. It calls rational sequences and chart-monotone perceptual ones both "fine", and doesn't order them. The default view (§11) follows that: it puts intuitive first and doesn't rank the others against each other. What observable "rational" means is a question for Joseph (§11).

**Why the roster makes this hard.** Claude gives about two thirds of the answers. On runs that walk the chart, its reasons cite the chart about twice as often as Grok's: 0.38 against 0.18 (`spikes/whys-basis-2026-10-06/FINDINGS.md`). That is a difference in what the families *say*. The behavioural instruments of §7 measure what the judgements *rest on*.

## 3. Where it sits

```
probing (1) ──answers──▶ raw tree (2) ──▶ CATALOG (6) ──▶ priority (3): what to ask next
port (4) ────answers──▶       │                     ├──▶ read-offs (5): BEST, SEQUENCES, PROGRESS
                              │                     └──▶ probing (1): measurement findings
```

- **Inputs.** The catalog reads answer records and their tags, never `source` (why a question was asked). Anything it needs from `source`, it derives structurally (§5).
- **Determinism.** The same inputs, recorded as a manifest, and the same frozen model give the same catalog (§13).
- **Readers.** They read the catalog for anything about sequences. Strength and certainty sit side by side (Joseph: *"side-by-side is canonical"*). Ranking keys and views are the reader's job.
- **Supersession.** Once built, its model supersedes the per-reader standard of METHODOLOGY §2a. The two then disagree about seeds, among other things: BEST.md's header says seeds are never evidence, which the catalog reverses.
- **Candidate inputs** are named propositions to score:
  - survey seeds and Joseph's dropspot sequences;
  - the triad era's grown rows (`data/triad-era/growth/r004–r012.json`);
  - triad chains;
  - reasoned continuations;
  - shuffles a mind called coherent.

  **Seed votes are evidence, as their own rater** (§9).

## 4. Objects and canonical forms

- **A link** is `c → x` at its own context `c`. Shown contexts for continue, inhibit, triad and choose run 2–8 glyphs (the probe's cap, chosen without evidence). Picks run up to 24. A link at a long context and at its suffix are different propositions, and nothing pools them.
- **A run** is an ordered list of distinct glyphs, of any length; a run and its reverse are one sequence. Its **canonical orientation** puts first the end with the smaller code-point tuple.
- **Which runs are records:**
  - every candidate input (§3);
  - every run asked whole (cohere or order);
  - every maximal run whose links each carry evidence (§8);
  - every contiguous window of these that was itself asked whole.

  Full-prefix maximal runs are paths in a trie, so their number is bounded by the links with evidence. Runs extended through stable suffix links (§8, state 2) aren't bounded that way. The build reports their count.
- **"Evidence" for a link** is at least `EVIDENCE_MIN` answers (any family) naming or recognising it. It is set to 1, chosen without evidence. The v3 audit measured that requiring 2 instead cuts the contexts with two or more continuations from about 2,034 to about 95. Records carry their answer counts, so a reader can raise the threshold. The catalog itself doesn't cut.
- **Containment** is a stored relation, never a deletion.
- **A branch** follows METHODOLOGY §3: a context (≥ 2 glyphs) at which two continuations each have evidence. Two runs are branches of each other when both pass through that context and continue differently.
- **A cycle** follows METHODOLOGY §3: a path returning to a context state, every step determined, counted once manifested. Its canonical form is the smallest code-point tuple over all rotations of the period, both orientations.
  - The runs along its period are records too, related to the cycle by containment.
  - Manifestability is bounded by the caps. A mind manifests period P by writing 2P minus the shown glyphs (at most 24 written from at most 8 shown), so P ≤ 16.
- **Long runs.** Whole-run questions show at most 24 glyphs. A longer run's whole-run evidence comes from its windows that were asked, and its record says which stretches are covered.

## 5. Inputs

| records | how they enter |
|---|---|
| continue (shown), pick, `next` (rank kept) | G, generation (§6) |
| written continuations | G, one unit per answer |
| inhibit | L, link recognition |
| cohere | R, whole-run recognition |
| order lines, triad middles | O, order of a set; and independence evidence at contested positions (§7) |
| choose | D, discriminator positions (§7) |
| `between` (1,370, triad era) | B, a two-sided fill; never a link |
| pick nulls (`tags.null`, about 1,860 answered) | G's null: how often a repeat, and how much spread, chance gives. Never link evidence. A forced, medium-effort condition, which is a stated mismatch for continue |
| seed votes | Seed, as its own rater, clustered by seed. Ported: the survey seeds, and Joseph's own dropspot sequences (family `human`, mind `joseph`). Agent-written dropspot sequences and generated lattices are candidates only, the rule `port/port_seeds.py` already follows |
| reasoned answers (`sonnet55r`) | by what they contain (`spikes/reasoned-pass-2026-10-06/FINDINGS.md`). A continuation reached after a code-point range lookup marks its link **chart-reached**, a fact (§7). "None" is end evidence. Continuations are candidates. Never evidence of a felt link |
| the muse family (Glimmer, 257 triad-era triad answers; off the roster since) | O, as its own rater |
| name-only order answers (to build, §12) | the name route's prediction (§7a) |
| reflections | apart (METHODOLOGY §3) |
| `call-failed` (about 108,000, nearly all in the void rounds; reasons `is_error`, `timeout`, …) | excluded. Usage limits found after 2026-10-06 also carry reason `limit` |
| `tool-attempt` (about 720) | a rater measurement (METHODOLOGY §4), not link evidence |
| `unparsed`, `other`, unassigned code points | their own outcomes. A continuation into unassigned code points is an arithmetic marker (§7) |
| a continuation that reaches the 24-glyph cap, or its soft target (`tags.soft_target`, from c096) | **censored, not ended**. Whether stopping at the target is censoring is measurable: compare where walks stop by target |
| duplicate answer IDs | one record per ID |

**Controls, identified structurally:**

- Shuffles (`tags.control: shuffled`) are paired with runs by glyph set. The pairing is many-to-many and stored as such.
- Chart windows are `tags.control: chart`.
- Near and far decoys are `tags.control: near` / `far`.
- L's control is the near decoys. The skip-test rate (a "yes" to the glyph two steps on) is reported beside it as an upper bound only. It isn't a clean negative (`▁ ▃ ▅ ▇` is a sequence too), and its status as a skip test depends on which run is meant, so no answer is ever used both as a control and as evidence.

## 6. Recognition parts

Each part makes one claim against one contrast, and carries strength and certainty (§9).

| part | claim | evidence | contrast |
|---|---|---|---|
| **R** | this order of these glyphs is recognised | cohere | the same glyphs shuffled; false-positive rates by chart class (contiguous, monotone, other) |
| **O** | the set is ordered this way | order lines and every asked triple | a Plackett–Luce model, reversal-invariant, with "only two", "none" and "extra" as their own outcomes |
| **L** | `x` comes directly after `c` | inhibit | near decoys (skip tests reported beside) |
| **G** | minds produce `x` after `c` unprompted | continue, picks, `next` | a likelihood of naming counts, calibrated on the tendril branches (§9) |
| **B** | `x` fills the gap between two runs | between | none yet |
| **Seed** | a surveyor proposed this run | seed votes | its rater's reliability (§9) |

R recognises, but it can't tell the look from the chart. Code-point order is strongly felt, so chart walks lead on R by construction (Claude says yes 0.97, 0.79 and 0.59 by chart class).

## 7. What the recognition is independent of

### 7a. Contested positions

**Where the chart makes a claim.** Measured (`spikes/contested-positions-2026-10-06/FINDINGS.md`, canary excluded): triad middles depart from the code-point median 0.13 of the time when all three glyphs share a Unicode block, and 0.69 when they span three blocks, which is chance. So the chart's order is something minds respond to between glyphs of *one block*. Between blocks it is close to arbitrary for them. The catalog therefore counts the chart route only where its alternative pairs glyphs of one block (Unicode 16 `Blocks.txt`, hashed).

**The chart route, per position of a run:**

- **A step** `a → b`, after `p → a`. The chart's candidate is `c`, the code point next to `a` in the direction from `p` to `a`. That direction rule is chosen without evidence; at a reversal of direction the other neighbour is a temptation too (it is accepted 0.46–0.61 when asked), and it isn't covered.
  - *chart-congruent* if `c = b`;
  - *no candidate* if `c` is unassigned or already in the run;
  - **contested** if `c` is in the same block as `a`;
  - *uncontested* otherwise. After `▀` going down, `c` is `╿`, a box-drawing piece: preferring the run's glyph to it tests nothing.
- **A triple** `a b c` of consecutive glyphs. The chart's alternative is the code-point order.
  - *chart-congruent* if `b` is the code-point median;
  - **contested** if putting `b` in the middle splits a pair of glyphs that share a block and are adjacent in code-point order. In a one-block triple, every departure does. In a two-block triple, only the lone glyph in the middle does (measured: 0.20 of two-block middles);
  - *uncontested* otherwise. A two-block triple whose middle departs only by which end the lone glyph sits at is uncontested. Those departures aren't at chance (0.26 against the median's 0.53), but nothing says what they rest on.

**The name route, measured.** The name-only order question (§12) shows the glyphs' Unicode names, scrambled, without the glyphs, and asks for an order. Per set:

- **uninformative** if the answers are mostly "none" or show no concentration about any order (Plackett–Luce concentration below a frozen threshold);
- otherwise, at each step and triple, **name-congruent** where the names' modal order agrees with the run, and **contested** where it predicts a different step or middle.

Only contested positions can earn positive name independence. "Names predict nothing" gives nothing on this route, not a free pass.

**Before the name route counts, the question is validated.** These minds know the Unicode database. Given "UPPER HALF BLOCK" they can recall the glyph and often its code point, so a name-only order could be the chart order recalled through names. Two validation sets are asked first:

- sets whose names' meaning orders them one way and whose code points order them another (fractions across two blocks; digit "dresses" spread over several blocks);
- sets whose names are uninformative.

If name-only orders follow the code points on the first set, the question measures chart recall, and the name route is reported **unmeasured** for every run. The validation's result is a precondition of the freeze (§13).

**Undiscriminable.** A run with no contested position on a route is undiscriminable on that route. That's a fact, stated, never a low score. 781 of the 2,430 runs asked whole are contiguous in code points, so they have no contested chart position at all: the bottom-up ramp `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`, the circled numerals, the dice, the moon phases. Most named alphabets and numbers will be name-congruent everywhere, in the same way.

**The canary's chart positions, from the glyphs alone** (written before the seal is opened):

| position | the chart's candidate | state |
|---|---|---|
| `▁ … ▇ █` | | chart-congruent |
| `█ → 🮆` | `▉` (same block as `█`) | contested |
| `🮆 → 🮅` | `🮇` (up from `🮆`, after the jump up from `█`) | contested |
| `🮅 → 🮄` | | chart-congruent |
| `🮄 → ▀` | `🮃` | contested |
| `▀ → 🮃` | `╿` (another block) | uncontested |
| `🮃 → 🮂` | `🮄`, already in the run | no candidate |
| `🮂 → ▔` | `🮁` | contested |
| triple `🮄 ▀ 🮃` | `🮃` as middle; `▀` is the lone glyph in the middle | contested |
| the other triples | | congruent or uncontested |

The canary's name route waits for the name-only question like every other run's. At `█`, LEFT SEVEN EIGHTHS (`▉`) and UPPER SEVEN EIGHTHS (`🮆`) are both "seven eighths", so whether names predict `🮆` there is something to measure, not assert.

### 7b. Independence at a position

At contested positions, each instrument gives a preference for the run's glyph (or middle) over the route's alternative. **Answers are pooled into one estimate per position first**; only that estimate is interpreted.

- **D, discriminator positions** (the `choose` question, built). A forced choice between the chart's candidate and the run's glyph. Read against a **D control** (built): the same pair after a neutral context, which measures each candidate's standalone pull.
- **Triad middles** at contested triples, from data that already exist. For the canary's `🮄 ▀ 🮃`, the middle given was `▀` from Gemini 3 of 3, Grok 3 of 3 and Claude 4 of 5 (public before the seal).
- **Order lines** at the contested positions of the sets they order.
- **Lookalike substitution** (built, §12), against a matched control. A glyph is swapped for a Unicode confusable from another block, and the same position is swapped for a control glyph drawn by a fated rule: uniformly from the confusable's own block, excluding glyphs confusable with the original and glyphs already in the run. The signal is the difference, since R alone is near ceiling. Confusables preserve identity, not style (`data/unicode/README.md`), so for styled letters it measures independence from the chart via identity, not via the look. Coverage is 454 of 1,203 monotone runs, and almost none of the canary: only `█` and `▔` have confusables.
- **On the name route**, the same instruments with the names' predicted glyph or middle as the alternative. A `choose` between the run's glyph and the names' prediction is to build (§12).

**Interpreting a position's estimate: asymmetric, by design.** First-impression minds accept the chart's next glyph 0.79–0.82 of the time when asked, against 0.03 for near decoys. So the chart's candidate is usually itself a felt continuation, and a preference for it has two readings.

- **For the run's glyph, with certainty: positive.** The strongest evidence D gives. The chart offered something minds do accept, and they chose otherwise.
- **For the alternative, with certainty, where the alternative is not itself felt there: negative.** "Felt there" means: the alternative has L beyond its control, or G evidence (≥ `EVIDENCE_MIN` picks or written continuations), at the position's context or a suffix of it of at least 2 glyphs.
- **For the alternative, with certainty, where it is felt there: a branch preference.** It might be chart-following, or a felt branch that happens to lie along the chart. It's recorded and counts neither way. At `█`, the chart's `▉` begins the horizontal ladder `█ ▉ ▊ ▋ ▌ ▍ ▎ ▏`. So `▉` preferred to `🮆` would say nothing against the canary, and `🮆` preferred to `▉` would be evidence for it.
- **Otherwise: inconclusive.**

This isn't biased toward finding independence. A mind that follows the chart produces position estimates that favour the chart. Those become negative or branch preferences, never positive. What the asymmetry costs is power: D rarely establishes leaning on the chart, because the chart's candidate is usually felt. That is stated on every record where it applies.

**Markers, recorded as facts and never counted as preferences:**

- chart-reached links (reasoned lookups);
- continuations into unassigned code points at a run's ends: minds extend the run by arithmetic. That is a fact about generation past the run, not about its own recognition.

### 7c. A run's state on a route

From its positions' interpretations, by a frozen rule:

| state | rule |
|---|---|
| **positive** | at least one contested position positive, and none negative. "Positive" here uses the multiplicity-corrected threshold: the position's Bayes factor must reach `K` times the number of contested positions asked on that route (`K` chosen without evidence, §13) |
| **negative** | at least one negative, and none positive |
| **mixed** | both |
| **undiscriminable** | no contested position (§7a) |
| **unmeasured** | the name route, while the name-only question is unvalidated or failed validation |
| **chart or branch** | at least one branch preference with certainty, and none positive or negative. The route's alternative was preferred, but it is also a felt continuation, so chart-following and a felt branch can't be told apart |
| **undecided** | contested positions exist, but none is positive, negative or a branch preference yet: unasked or inconclusive |

The record lists every position with its instruments, estimate and interpretation, so a reader can apply a different rule.

## 8. Link states

Every link in a record carries one of five states:

1. evidence at its own full-prefix context;
2. **stable**: evidence at a suffix, with lengthening tested up to the 8-glyph cap and no flip (METHODOLOGY §3);
3. evidence at a suffix only, lengthening untested;
4. **pick evidence beyond 8 glyphs**: picks at contexts of 9–24 glyphs, which shown questions can't reach;
5. none.

Nothing fills in states 3 or 5. A run's parts come from whole-run evidence, and its links' states and parts are summarised, never multiplied into a product.

## 9. The model

**Recognition parts (yes/no).** For rater $r$ and item $i$:

$$P(\text{yes}_{ri}) = c_r + (1 - c_r)\, \beta_{ri}, \qquad \beta_{ri} = s_r\, \theta_i$$

$c_r$ is the false-positive rate from that part's controls (for R, by chart class). Only the product $\beta_{ri}$ is identified, so **strength is reported on the identified scale**: the expected excess yes rate, Abbott's $(p - c)/(1 - c)$, with its interval. There is no unanchored $\theta$.

- **Certainty** is a Bayes factor for $\beta \gt 0$ against $\beta = 0$, with a stated uniform prior on $\beta$, itemised by answer for the hand audit. For L it is reported per control (near decoys; skip tests as the upper bound).
- **"Can't tell"** is a third category with its own rates per rater.
- **Within a family.** Each rater's strength is estimated with its own $c_r$ (Sonnet and `haiku45nt` have very different false-positive rates). The family's strength is the precision-weighted mean of its raters' estimates, as BEST computes it now.
- **Across families.** A mean weighted by each family's **discrimination on R's "other" chart class**, where the chart can't help: Claude 0.31, Grok 0.26. Never on contiguous runs, where discrimination partly is chart-reading (0.85 against 0.62). The all-answers likelihood is reported beside it.
- **Raters** are minds in **assigned** conditions: thinking budget (`haiku45nt` 0, `haiku45` 31000), effort (the generator minds at medium), prompt variant, protocol era. Self-chosen zero thinking (Sonnet, Opus) is a covariate of the item, not a condition. **Sheet position and size** are covariates too, and their estimated effects go to probing (concern 1).
- **Seed raters** (each surveyor, and Joseph) are not pooled with the first-impression minds of their family. Joseph's point that recognition is easier than generation enters as a measured prior. A generator's weight on independence is the rate at which raters of another family, in an assigned no-deliberation condition, recognise its runs beyond the class-matched control. It applies only to runs without whole-run evidence of their own, and is unidentified, and stated as such, until a non-Claude assigned no-deliberation rater has answered. Gemini Flash is answering the new kinds first from 2026-10-06.

**Preferences at a position (§7b).** $p$ is the share of answers choosing the run's glyph or middle; $b$ is the baseline. For D, $b$ is the D control's share for the run's glyph. Without a D control, $b = 0.5$, and the position is marked uncontrolled. For triads and order lines at a contested position, $b$ is the share a uniform choice among the set's possible middles or orders would give. Strength is

$$\delta = \begin{cases} (p - b)/(1 - b) & p \geq b \\ (p - b)/b & p \lt b \end{cases}$$

in $[-1, 1]$. Certainty is a Bayes factor for $p \neq b$ in the observed direction, at a uniform prior on $p$. Families combine as above.

**O.** Plackett–Luce worths with a reversal-invariant likelihood (a sequence and its reverse are one), fitted per family. Its strength is the concentration about the hypothesised order.

**G.** The likelihood ratio of a link's naming counts under links that other parts recognise, against links they reject. It is calibrated only on the **tendril branches**: links asked whatever their generation, which the v3 audit found are covered roughly flatly by pick share (0.16–0.23). The rejected class exists but is thin: 174 of 480 branch runs asked whole drew mostly "no", at a median of 3 answers each. Branch shares are raw, per rater, with intervals. The reason a question was asked isn't needed for this, so METHODOLOGY's rule that the catalog doesn't know why a question was asked stands untouched.

## 10. A record

- **Identity:** canonical form, glyphs, kind, relations (containment, branch, cycle).
- **Recognition parts (§6):** strength and certainty, per family and combined.
- **Independence (§7):** per route, its state, and every position with its instruments, estimate and interpretation.
- **Markers:** chart-reached links, unassigned continuations.
- **Deliberation contrast**, where asked: recognition by `haiku45` (31000) against `haiku45nt` (0), each beyond its control. Identified within Haiku only, and stated so.
- **Link states (§8)** and coverage.
- **Evidence:** the answer IDs behind every number.
- **The model version and fitted rates.**

## 11. Readers and the default view

**The default view.** A labelled reader computation, not stored, its rule frozen with the model. Only recognised runs appear: R, O or L beyond its contrast with certainty. Groups are exclusive and evaluated in this order, and each shows both routes' states.

1. **Intuitive:** both routes positive.
2. **Independent where measurable:** one route positive and the other undiscriminable. For example, "independent of the chart; the name route undiscriminable". Not folded into intuitive: undiscriminable means *we can't tell* whether the recognition rested on that route.
3. **Leaning:** either route negative or mixed. For example "leans on the chart", "leans on the names", "mixed on the chart".
4. **Chart or branch:** either route "chart or branch" (§7c), with no route negative or mixed. The alternative the route offered was preferred, and it is also felt.
5. **Undiscriminable:** both routes undiscriminable. For example `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`.
6. **Undecided:** everything else (a route undecided or unmeasured, with no route negative, mixed or "chart or branch"). Shown apart and never ranked against the decided groups. Where one route is positive, it says so.

**Reading group 3 against group 4.** D can rarely show leaning on the chart: the chart's glyph is accepted about 80% of the time, so it is nearly always felt, and a preference for it is a branch preference (§7b). Runs that really do follow the chart mostly land in group 4, not group 3. A near-empty "leaning" group doesn't mean few runs rely on the chart. (Pointed out by a side agent, 2026-10-06.) The instrument that can show leaning is lookalike substitution (§7b): if recognition falls to the non-lookalike control's level when a glyph is swapped for a confusable from another block, it rested on something the swap changed: the code point, or details of the look that confusables don't keep (they preserve identity, not style). Leaning is the likelier reading where the two glyphs look alike in the rendering minds see, and the instrument can't separate the two otherwise. It comes first among the additions (§12).

Joseph's sentence ranks group 1 first. Groups 2–5 are listed in that order for display only: his "fine" covers both rational and chart-monotone sequences, and the view doesn't rank them.

**"Rational" isn't a group yet.** Version 4 defined it by who proposed a run. That reads a mind's *not* generating something as evidence, which METHODOLOGY's one-way rule forbids, and it would move with the asking history. Joseph's words, "interpretable rational sequence (given some thought)", describe how a run is *recognised*. Two measured readings exist:

- recognised only with deliberation: the deliberation contrast in the record (§10), identified within Haiku only;
- the recognition leans on the chart or the names: group 3, and possibly group 4.

Which one he means is his to say. Until then, the record carries both, and the view shows groups 3 and 4 under their descriptive names.

**Other readers:**

- **Priority (3)** asks where a question would move a record most: an unasked contested position, a D control, a name-only order for a run with possible name-contested positions, an untested link inside a strong run. Uncontested positions aren't asked. Certainty grows with asking, and that's stated wherever priority uses it.
- **BEST** becomes a view of the catalog.

## 12. Probing additions

| addition | status |
|---|---|
| D, discriminator positions (`choose`) | built 2026-10-06; asked only at contested positions from c096 (§7a) |
| D controls: the same pair after a neutral context (three fresh glyphs from blocks other than either candidate's; tag `control: neutral`), 20 a round, each pair once | built 2026-10-06, from c096 |
| **The name-only order question.** Show the glyphs' Unicode *names*, scrambled, without the glyphs; ask for the order (the order question's wording). The name route's prediction (§7a). Its two validation sets come first (`NAME_VALIDATION` in `priority/plan.py`: six sets whose names' meaning and code points disagree, such as `⁰¹²³⁴`, `🕐🕜🕑🕝🕒` and `⓪①②③④`, and three whose names carry no order), then Joseph's seed, ordered seeds and recognised runs; runs longer than 12 in overlapping windows; 30 a round | built 2026-10-06, from c096 |
| `choose` between the run's glyph and the names' predicted glyph, at name-contested positions | to build, after the name-only question |
| Lookalike substitution, with the fated control of §7b. The one instrument that can show leaning on the chart (§11). 20 pairs a round, from recognised runs (yes share ≥ 0.5, chosen without evidence) strictly monotone in code points; one interior position, fated; tags `control: lookalike` / `lookalike-ctl` and `of`; never on a sheet with its run or its pair | built 2026-10-06, from c096 |
| **Joseph's basis question.** After the verdict, in a separate turn where the adapter allows. Open first ("what did you notice that made it look that way, or not?"), then plain options: how the symbols look / what they stand for or are called / where they sit in the character encoding / can't say / **other: ___**. No value words. On a fated random half of sheets. Validated against D, not trusted on consistency with its own reply | to build |
| **Joseph's two-shot framing.** Consent turn, then "immediate impressions … independent of …", with fated wording, never naming Unicode. A tagged condition; outcome the chart-class gap | to build; needs multi-turn adapter calls |
| Thinking text saved by the Claude and Grok adapters | to build |
| a continue null; order nulls (sets with no order) | to build |
| **The soft target.** 5,290 continue answers stopped at exactly 24 glyphs, against 248 at 23: the prompt's "(up to 24)" anchored walks to the cap. Joseph's change: "around N or fewer", N uniform 3–24 per sheet, recorded per answer (`tags.soft_target`) | built 2026-10-06, from c096 |

Two things are out of scope. **Images** (Joseph: *"completely orthogonal to the unicode-token-perception issue"*). **Earlier minds' reasons**, used only in generator passes and never as evidence.

## 13. Engine, determinism, freeze

**Engine.** Python computes, Postgres 18 stores and serves:

- `answers` (one row per answer ID);
- `evidence` (part, proposition, answer, rater, contribution);
- `raters`, `rates`, `records`, `positions`, `relations`.

Each build goes into a versioned schema, and an atomic switch makes it current.

**The manifest:**

- hashes of every answer file;
- the candidate inputs (`data/triad-era/growth/`, `data/seeds/`);
- the Unicode reference files (`data/unicode/`);
- the Unicode version;
- the Python version (the engine is pure Python: no numpy or scipy, so nothing outside the manifest moves its sums);
- the code's hashes and the git commit;
- the model version.

**Fits** use EM with a fixed initialisation, order and tolerance, and sums are taken in a fixed order.

**Build 2** (`catalog/order.py`, 2026-10-06; the build now takes about a minute) adds O. Every answer bearing on a run is a unit that agrees with its order or not, against its own chance baseline: an asked triple of the run's glyphs answered with a middle (1/3), and an order answer whose main line places at least 3 of the run's glyphs (2/m! for m glyphs). Strength is the excess over chance common to a family's units, with the same Bayes factor as R and L. "Only two", "none", glyphs put in "extra", ties and lines too short count as their own outcomes, never against the order. **This departs from §9**, which specifies a Plackett–Luce fit with "concentration about the hypothesised order"; that concentration isn't defined closely enough to compute without inventing it, while this scores a given order on the one standard and doesn't find the best order. The fit stays open. First reading: O is scored on 6,996 of 7,761 records and certain on 4,325; `①…⑩` at 0.98 (Claude 134/135 units, Grok 61/61, Gemini 73/73); shuffled block ramps that some mind called coherent, asked as runs, near 0.01.

**Build 1** (`catalog/links.py`, 2026-10-06; the build takes about 13 seconds) adds the link layer: every link `c → x` at its own context (79,220 at c101), with G in its three channels (shown, written, picked; raw per family, nothing pooled across context lengths) and L against each rater's near decoys (Abbott; a Bayes factor, as R); and the state (§8) of every link of every record, the better reading direction kept, summarised on the record (`link_states`, `weakest_link`, `flips`). Two readings fixed in building it: state 2 needs the longest showable context (the full prefix, or its last 8 glyphs) shown to minds with no other glyph on top; a flip is a longer asked context whose top answer is another glyph ("none" is an end, not a flip). First reading: 1,641 of the 2,990 runs asked whole have a link no mind was ever asked about (state 5), mostly short runs from pick branches, seeds and reordered shuffles: they were recognised whole while their links were never put as continuations.

**Build 0** (`catalog/build.py`, 2026-10-06; about 6 seconds; schema `catalog` in database `empirica_glyph_sequence`, beside the triad era's `public`). Its docstring lists what it implements and what not yet. Built: R; the chart route's contested steps (D) and triples; route states; the view; lookalike as a run-level count. Not yet: O, L and G as record parts, B, seed raters, link states, maximal runs from links, order lines as position evidence. The name route is "unmeasured" for every run until its validation is read, so every recognised run is "undecided" in the view for now. Choices made in building it, each to be frozen:

- **R's controls are indexed by glyph set,** contiguous or not, because a shuffle controls a set, not an order. A contiguous run takes the contiguous-set rate, and a monotone run the other.
- **R's certainty** uses one $\beta$ common to a run's raters, with each rater's own $c_r$ (a simplification of §9's $s_r \theta_i$).
- **D pools** the answers at the position's context and its suffixes down to 2 glyphs. The D control's baseline is the Jeffreys mean of the control's share.
- **Triad preferences** count only answers naming the run's middle or the code-point median. A preference for the median is always "chart or branch": build 0 has no test of whether the median is felt as a middle.
- **The seal** drops every sealed answer before anything is computed, until the seal file records the frozen commit.

**The freeze.** Before the canary's sealed answers are queried, these are committed with a date:

- every parameter marked "chosen without evidence", including `EVIDENCE_MIN`, the step-direction rule, `K`, and the Bayes-factor threshold for "with certainty" on every part;
- the contested-position rule (§7a) and the interpretation rule (§7b);
- the route-state rule (§7c) and the default view's rule (§11);
- the name-only question's validation result, or the name route marked unmeasured;
- the parts and their contrasts;
- the priors and the family combination rule;
- the tolerances;
- the code computing the canary.

The commit hash goes into the seal file.

## 14. Acceptance tests

They test the catalog, not the minds.

1. **Determinism.** Rebuilding from the same manifest gives identical catalogs.
2. **Control rates, held out by round.** For each control class, fit through round N and predict the control rates of later rounds by chart class, within the interval. (A split-half test was nearly unable to fail, per the v2 audit, A10. Transfer across classes, such as chart windows from shuffles, is reported but isn't a test: chart windows are a different population.)
3. **The canary, procedurally.** The catalog's quantities and default view at the canary's positions (§7a's table) follow from the listed answers by the frozen rules, and a hand audit agrees. The canary's outcome is **reported as a finding** with its full provenance, which is:
   - Joseph typed `▁▂▃▄▅▆▇█🮆🮅🮄…`, and the completion `… ▀ 🮃 🮂 ▔` is the session's;
   - survey seeds disagree: fable-1 `🮂 🮃 ▀ 🮄 🮅 🮆 █` includes `▀`, while sonnet5-1 `🮂 🮃 🮄 🮅 🮆` and grok-1 `🮃 🮄 🮆` follow the chart and leave it out;
   - the triad era's grown rows place `▀` between `🮄` and `🮃`, as the completion does: r004 `█ 🮆 🮅 🮄 ▀ 🮃 🮂 🮁`; r005–r011 `_ ‗ ▁ ▂ ▃ ▄ ▅ ▆ ▇ ▉ █ 🮆 🮅 🮄 ▀ 🮃 🮂 🮀`; r012 `▁ ▂ ▃ ▄ ▅ ▆ ▇ ▉ █ 🮆 🮅 🮄 ▀ 🮃 🮂 🮁`. They put `▉` between `▇` and `█`, and end at `🮀` or `🮁`, not `▔`. The session wrote its completion after its own tool output had shown triad-era rows with `🮄 ▀ 🮃` in them, so the two aren't independent;
   - the triads favour `▀` between `🮃` and `🮅` (Gemini 3/3, Grok 3/3, Claude 4/5);
   - ten generator picks after `… 🮄` (two Claude minds, c087) went `🮃` ×8 and `▀` ×2;
   - at `▁ … █`, the generator picks went `▉` ×4 (Grok), `▀` ×5 (Haiku) and `▁` ×5 (Sonnet), and none picked `🮆`.
4. **Chart-borne candidates, procedurally.** The same for `🨀 🨁 🨂 …` (contiguous, so undiscriminable on the chart route, which is the honest report) and the reasoned `♖ ♕ ♔ → ♓` (chart-reached).
5. **The triad era, informatively.** Of the 4,905 grown rows, the fraction with whole-run evidence, and what their parts and independence say.
6. **Agreement with what is plain.** BEST's current recognised and rejected sets agree with the catalog, and every disagreement is explained.
7. **Hand audit.** A sample of records is recomputed from the listed answers and rates.
8. **Posterior predictive checks.** Item-level spread against the model, with overdispersion reported.
9. **Stability.** When one more round is added, quantities whose evidence didn't change move by less than their own interval. Quantities whose evidence changed are listed, since asking is outcome-dependent.

## 15. Changes from version 4, by the check's findings

- **V1, the felt-chart-candidate rule.** Reversed. A felt chart candidate now makes a preference *against* the chart informative, and it makes a preference *for* the chart ambiguous (a branch preference). Answers are pooled per position before interpretation, so the asymmetry costs power and doesn't bias toward independence (§7b). That cost, a nearly empty leaning group, is made visible: "chart or branch" is a route state and a view group of its own (§7c, §11).
- **V2, positions the chart never contested.** A position counts only where the chart's alternative pairs glyphs of one Unicode block, grounded in a measurement (`spikes/contested-positions-2026-10-06/`). Triads are gated the same way (§7a). The planner is to stop asking uncontested steps (§12).
- **Q1, the default view.** Exclusive groups in a stated order. A leaning group covers the names as well as the chart. "Undiscriminable" is no longer a pass: a run positive on one route and undiscriminable on the other is its own group. "Rational" by provenance is withdrawn; the question of what it means goes to Joseph, with two measured readings carried in the record. Per-run aggregation is a frozen rule with a multiplicity correction (§7c, §11).
- **Q2, the name-only question.** Three outcomes per set or position; only contested positions earn positive independence. Validated against chart recall before it counts. The canary's name status is measured, not asserted (§7a).
- **C1.** §7a's positions are facts from the glyphs on the chart route, and measured on the name route; the text now says which.
- **C3.** The substitution control is drawn by a fated rule from a defined pool (§7b).
- **C4.** §2 no longer orders rational against chart-congruent; Joseph's quote orders only intuitive above the rest.
- **C5.** Two-block and three-block triples are gated (§7a). §1 says the seal covers `choose` only.
- **C6.** Test 2 holds out later rounds instead of splitting in half.
- **C7.** The r004 row with `▀` is in the provenance.
- **C8.** One formula for D's strength, with the baseline stated. Family weights from R's "other" class only. Raters within a family combine by precision-weighted mean, each with its own false-positive rate.
- **C10.** The bound on maximal runs holds for full-prefix runs; the build counts the rest.
- **Smaller points.** "Chart-congruent" as a view group is renamed "undiscriminable". The certainty thresholds are listed among the frozen parameters.
