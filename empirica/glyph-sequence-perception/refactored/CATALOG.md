# CATALOG: the canonical catalog of sequences

*Design, version 4 (2026-10-06), by the independent session (Claude Opus 5.5) with Joseph. Not built. Versions 1–3 were audited de novo (`audits/catalog-design-2026-10-06.md`, `…-v2-…`, `…-v3-…`; findings F1–F12, A1–A11, C1–C10). §15 maps version 3's findings to this version. The canary's discriminator answers are sealed until the model is frozen (`audits/SEAL-canary-choose-2026-10-06.md`). METHODOLOGY §2a lists the catalog as concern 6. "METHODOLOGY §n" refers to that file; a bare "§n" is a section of this one.*

## 1. Why

METHODOLOGY §2a says that sequences, branches, ends, cycles and stability are *read off* the tree. What exists instead is a sound store of raw answers indexed by context, and readers that each derive sequences their own way, each fix in one exposing a loss in another:

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
- the model is frozen before the canary is looked at.

## 2. What it is for

Recognition is the goal (METHODOLOGY §1). Joseph has said which recognition matters most:

> *"An interpretable rational sequence (given some thought) is fine. Originally I gave more weight to monotonic perceptual sequences that were also monotonic in chart order / code-point magnitude. … It's fine. It's not anything I'm excited about rediscovering. An 'intuitive' sequence that doesn't need internal arithmetic or thinking about the glyph's name and codepoint is (much) better."*

So besides *whether* a run is recognised, the catalog measures what the recognition is **independent of**: the code chart and the glyphs' names. These are measured quantities on every record (§7), never labels. Joseph's ranking (intuitive above rational above chart-congruent) is the **default view** a reader computes from them (§11). It is not stored as a verdict, and it never ranks *undecided* against *decided*.

**Why the roster makes this hard.** Claude gives about two thirds of the answers. On runs that walk the chart, its reasons cite the chart about twice as often as Grok's: 0.38 against 0.18 (`spikes/whys-basis-2026-10-06/FINDINGS.md`). That is a difference in what the families *say*, and the behavioural instruments of §7 measure what the judgements *rest on*.

## 3. Where it sits

```
probing (1) ──answers──▶ raw tree (2) ──▶ CATALOG (6) ──▶ priority (3): what to ask next
port (4) ────answers──▶       │                     ├──▶ read-offs (5): BEST, SEQUENCES, PROGRESS
                              │                     └──▶ probing (1): measurement findings
```

- **Inputs.** The catalog reads answer records and their tags, never `source` (why a question was asked). Anything it needs from `source`, it derives structurally (§5).
- **Determinism.** The same inputs, recorded as a manifest, and the same frozen model give the same catalog (§13).
- **Readers.** They read the catalog for anything about sequences. Strength and certainty sit side by side (Joseph: *"side-by-side is canonical"*), and ranking keys and views are the reader's job.
- **Supersession.** Once built, its model supersedes the per-reader standard of METHODOLOGY §2a. The two then disagree about seeds, among other things: BEST.md's header says seeds are never evidence, which the catalog reverses.
- **Candidate inputs** are named propositions to score:
  - survey seeds and Joseph's dropspot sequences;
  - the triad era's grown rows (`../data/growth/r004–r012.json`);
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

  Maximal runs come from the tree's links, so their number is bounded by the links with evidence, not by the candidates.
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
| order lines, triad middles | O, order of a set; and chart-independence evidence where they depart from code-point order (§7) |
| choose | D, discriminator positions (§7) |
| `between` (1,370, triad era) | B, a two-sided fill; never a link |
| pick nulls (`tags.null`, about 1,860 answered) | G's null: how often a repeat, and how much spread, chance gives. Never link evidence. A forced, medium-effort condition, which is a stated mismatch for continue |
| seed votes | Seed, as its own rater, clustered by seed. Ported: the survey seeds, and Joseph's own dropspot sequences (family `human`, mind `joseph`). Agent-written dropspot sequences and generated lattices are candidates only, the rule `port/port_seeds.py` already follows |
| reasoned answers (`sonnet55r`) | by what they contain (`spikes/reasoned-pass-2026-10-06/FINDINGS.md`). A continuation reached after a code-point range lookup marks its link **chart-reached**, a fact (§7). "None" is end evidence. Continuations are candidates. Never evidence of a felt link |
| the muse family (Glimmer, 257 triad-era triad answers; off the roster since) | O, as its own rater |
| reflections | apart (METHODOLOGY §3) |
| `call-failed` (about 108,000, nearly all in the void rounds; reasons `is_error`, `timeout`, …) | excluded. Usage limits found after 2026-10-06 also carry reason `limit` |
| `tool-attempt` (about 720) | a rater measurement (METHODOLOGY §4), not link evidence |
| `unparsed`, `other`, unassigned code points | their own outcomes. A continuation into unassigned code points is an arithmetic marker (§7) |
| a continuation that reaches the 24-glyph cap | **censored, not ended** |
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

### 7a. Positions where the routes disagree: facts from the glyphs

Some positions in a run can discriminate the look from the chart or the name; others can't. Which is which is a fact about the glyphs, not about anything asked. At each step `a → b` and each consecutive triple, the catalog computes two facts:

- **Chart-congruent:** `b` is the code-chart neighbour of `a` in the run's direction (±1 code point), and the triple's middle is its code-point median.
- **Name-congruent:** the Unicode names alone predict the step. This isn't decided by a hand-written rule: it is *measured* by the name-only order question (§12). When minds order the glyphs' *names*, with no glyphs shown, the order they give is the name route's prediction.

A position is **chart-discriminating** where it isn't chart-congruent, and **name-discriminating** where it isn't name-congruent. A run with no discriminating position on a route is **undiscriminable on that route**. That's a fact, stated, never a low score. 781 of the 2,430 runs asked whole are contiguous in code points, so they have no chart-discriminating interior position at all: the bottom-up ramp `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`, the circled numerals, the dice, the moon phases.

**Where names describe the look, nothing can separate the two.** The canary's glyphs are named LOWER ONE EIGHTH BLOCK … FULL BLOCK … UPPER SEVEN EIGHTHS BLOCK … UPPER ONE EIGHTH BLOCK. Their names describe their shapes, so the name route and the look route predict the same order everywhere along it. For such runs, name independence is undiscriminable, and the record says so. Joseph's criterion can then be judged only on the chart route, which does discriminate at `🮄 → ▀`.

### 7b. Chart independence: a signed quantity

At chart-discriminating positions, these instruments measure whether the recognition goes against the chart. Each gives a signed preference: +1 is fully against the chart, 0 is no preference, −1 is fully for it.

- **D: discriminator positions** (the `choose` question, built). A forced choice between the chart's next glyph and the run's glyph (or another alternative). Two qualifications:
  - **A felt chart candidate.** Where the chart candidate is *itself* recognised at that context (L beyond its control, or picked), the position measures a **branch preference** between two felt continuations. It's recorded as one and doesn't count toward chart independence. At `█`, the chart's `▉` begins the horizontal ladder `█ ▉ ▊ ▋ ▌ ▍ ▎ ▏`, which first-impression minds recognise, so `█ → 🮆` against `▉` is a branch position.
  - **A D control.** The same pair shown after a neutral context (decoy against decoy, METHODOLOGY §4a) measures each candidate's standalone pull. D's preference is read against it.
- **Triad departures, from data that already exist.** A triple whose middle is given as other than its code-point median is a behavioural departure from the chart. Of 12,888 triad middles, 2,290 (17.8%) depart; by family, Claude 0.18, Gemini 0.19, Grok 0.16. 229 triples with at least 3 middles have a modal departing middle. For the canary's `▀ 🮃 🮅`, the code-point median is `🮃`, and the middle given was `▀` from Gemini 3 of 3, Grok 3 of 3 and Claude 4 of 5. These answers enter chart independence now, before any `choose` answer.
- **Order lines** that put a set in an order other than code-point order, at the positions where they differ.
- **Lookalike substitution** (to build, §12), against a matched control. A glyph swapped for a Unicode confusable from another block is compared with the same position swapped for a non-lookalike glyph of the same broad kind. The instrument's signal is the difference, since R alone is near ceiling. Confusables preserve identity, not style (`data/unicode/README.md`), so for styled letters it measures independence from the chart via identity, not via the look. Coverage is 454 of 1,203 monotone runs, and almost none of the canary: only `█` and `▔` have confusables.
- **Markers, recorded as facts and never counted as preferences:**
  - chart-reached links (reasoned lookups);
  - continuations into unassigned code points at a run's ends: minds extend the run by arithmetic. That is a fact about generation past the run, not about its own recognition.

### 7c. Name independence

The same, on the name route: at name-discriminating positions, does recognition follow the names' order or depart from it? The instruments are the name-only order question (§12) and the triad and order departures from the names' order. Most named alphabets and numbers are name-congruent everywhere, as the chart is for contiguous runs. That is honest, and it is stated.

### 7d. Discrimination status

Per run, per route:

- the discriminating positions (from §7a);
- which have been asked, and by which instruments;
- the preferences found.

This is the state of knowledge, kept apart from the quantities.

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

$c_r$ is the false-positive rate from that part's controls (for R, by chart class). Only the product $\beta_{ri}$ is identified, so **strength is reported on the identified scale**: the expected excess yes rate, Abbott's $(p - c)/(1 - c)$, per family, with its interval. There is no unanchored $\theta$.

- **Certainty** is a Bayes factor for $\beta \gt 0$ against $\beta = 0$, with a stated uniform prior on $\beta$, itemised by answer for the hand audit. For L it is reported per control (near decoys; skip tests as the upper bound).
- **"Can't tell"** is a third category with its own rates per rater.
- **Combining families.** Each family's strength is estimated within the family. Families are combined as a mean weighted by **discrimination measured where the chart can't help**: on R's "other" chart class, where Claude is 0.31 and Grok 0.26, or on D where it exists. Never on contiguous runs, where discrimination partly is chart-reading (0.85 against 0.62). The all-answers likelihood is reported beside it.
- **Raters** are minds in **assigned** conditions: thinking budget (`haiku45nt` 0, `haiku45` 31000), effort (the generator minds at medium), prompt variant, protocol era. Self-chosen zero thinking (Sonnet, Opus) is a covariate of the item, not a condition. **Sheet position and size** are covariates too, and their estimated effects go to probing (concern 1).
- **Seed raters** (each surveyor, and Joseph) are not pooled with the first-impression minds of their family. Joseph's point that recognition is easier than generation enters as a measured prior. A generator's weight on chart independence is the rate at which raters of another family, in an assigned no-deliberation condition, recognise its runs beyond the class-matched control. It applies only to runs without whole-run evidence of their own, and is unidentified, and stated as such, until a non-Claude assigned no-deliberation rater has answered. Gemini Flash is answering the new kinds first from 2026-10-06.

**D and the other signed quantities.** The preference $p$ for the run's glyph over the chart's, against the D control's baseline. Strength is $2p - 1$ in $[-1, 1]$. Certainty is a Bayes factor against $p$ at its baseline. Families are combined as above.

**O.** Plackett–Luce worths with a reversal-invariant likelihood (a sequence and its reverse are one), fitted per family. Its strength is the concentration about the hypothesised order.

**G.** The likelihood ratio of a link's naming counts under links that other parts recognise, against links they reject. It is calibrated only on the **tendril branches**: links asked whatever their generation, which the v3 audit found are covered roughly flatly by pick share (0.16–0.23). Branch shares are raw, per rater, with intervals. The reason a question was asked isn't needed for this, so METHODOLOGY's rule that the catalog doesn't know why a question was asked stands untouched.

## 10. A record

- **Identity:** canonical form, glyphs, kind, relations (containment, branch, cycle).
- **Recognition parts (§6):** strength and certainty, per family and combined.
- **Independence (§7):** chart and name, signed strength and certainty, with the instruments behind them.
- **Discrimination status (§7d)** and markers (chart-reached links, unassigned continuations).
- **Link states (§8)** and coverage.
- **Evidence:** the answer IDs behind every number.
- **The model version and fitted rates.**

## 11. Readers and the default view

**The default view, Joseph's ranking.** A labelled reader computation, not stored. Its rule is frozen with the model:

- **Intuitive:** recognised (R, O or L beyond its contrast), with chart independence and name independence each either positive with certainty or **undiscriminable**, and at least one of them positive.
- **Rational:** recognised, not intuitive, and proposed only by deliberating generators (reasoned or generator minds), as its tags show, and not chart-reached.
- **Chart-congruent:** recognised, with both routes undiscriminable. For example `▁ ▂ ▃ ▄ ▅ ▆ ▇ █`.
- **Chart-leaning:** recognised, with chart independence negative with certainty.
- **Undecided:** discriminating positions exist but haven't been asked, or the answers are inconclusive. Not ranked against the others.

Under this rule, deliberation never decides a run's place. "Rational" reads the *provenance of the candidate*, which is a fact about who proposed it, not about how the recognising mind answered.

**Other readers:**

- **Priority (3)** asks where it would move a record most: an unasked discriminating position, a D control, a name-only order for a run with name-discriminating positions, an untested link inside a strong run. Certainty grows with asking, and that's stated wherever priority uses it.
- **BEST** becomes a view of the catalog.

## 12. Probing additions

| addition | status |
|---|---|
| D, discriminator positions (`choose`) | built 2026-10-06 |
| D controls: the same pair after a neutral context | to build |
| **The name-only order question.** Show the glyphs' Unicode *names*, scrambled, without the glyphs; ask for the order (the order question's wording). It measures the name route (§7a). | to build |
| Lookalike substitution, with a matched non-lookalike substitution as its control | to build |
| **Joseph's basis question.** After the verdict, in a separate turn where the adapter allows. Open first ("what did you notice that made it look that way, or not?"), then plain options: how the symbols look / what they stand for or are called / where they sit in the character encoding / can't say / **other: ___**. No value words. On a fated random half of sheets. Validated against D, not trusted on consistency with its own reply. | to build |
| **Joseph's two-shot framing.** Consent turn, then "immediate impressions … independent of …", with fated wording, never naming Unicode. A tagged condition; outcome the chart-class gap. | to build; needs multi-turn adapter calls |
| Thinking text saved by the Claude and Grok adapters | to build |
| a continue null; order nulls (sets with no order) | to build |
| **A probing finding to pass on.** 5,290 continue answers stop at exactly 24 glyphs, against 248 at 23. The prompt's "(up to 24)" anchors walks to the cap. Changing it would be a tagged prompt version, Joseph's call. | for Joseph |

Two things are out of scope. **Images** (Joseph: *"completely orthogonal to the unicode-token-perception issue"*). **Earlier minds' reasons**, used only in generator passes and never as evidence.

## 13. Engine, determinism, freeze

**Engine.** Python computes, Postgres 18 stores and serves:

- `answers` (one row per answer ID);
- `evidence` (part, proposition, answer, rater, contribution);
- `raters`, `rates`, `records`, `relations`.

Each build goes into a versioned schema, and an atomic switch makes it current.

**The manifest:**

- hashes of every answer file;
- the candidate inputs (`../data/growth/`, `../data/seeds/`);
- the Unicode reference files (`data/unicode/`);
- the Unicode version;
- Python, numpy and scipy versions;
- the model version.

**Fits** use EM with a fixed initialisation, order and tolerance, and sums are taken in a fixed order.

**The freeze.** Before the canary's sealed answers are queried, these are committed with a date:

- every parameter marked "chosen without evidence";
- the parts and their contrasts;
- the priors and the family combination rule;
- the default view's rule;
- the tolerances;
- the code computing the canary.

The commit hash goes into the seal file.

## 14. Acceptance tests

They test the catalog, not the minds.

1. **Determinism.** Rebuilding from the same manifest gives identical catalogs.
2. **Control rates, within population.** For each control class, fit on half and predict the other half within the interval. (Transfer across classes, such as chart windows from shuffles, is reported but isn't a test: chart windows are a different population.)
3. **The canary, procedurally.** The catalog's quantities and default view at the canary's positions follow from the listed answers by the frozen rules, and a hand audit agrees. The canary's outcome is **reported as a finding** with its full provenance, which is:
   - Joseph typed `▁▂▃▄▅▆▇█🮆🮅🮄…`, and the completion `… ▀ 🮃 🮂 ▔` is the session's;
   - survey seeds disagree: fable-1 `🮂 🮃 ▀ 🮄 🮅 🮆 █` includes `▀`, while sonnet5-1 `🮂 🮃 🮄 🮅 🮆` and grok-1 `🮃 🮄 🮆` follow the chart and leave it out;
   - the triad era's grown rows include `▉` and end at `🮀` or `🮁`;
   - the triads favour `▀` between `🮃` and `🮅` (Gemini 3/3, Grok 3/3, Claude 4/5);
   - ten generator picks after `… 🮄` (two Claude minds, c087) went `🮃` ×8 and `▀` ×2;
   - at `▁ … █`, the generator picks went `▉` ×4 (Grok), `▀` ×5 (Haiku) and `▁` ×5 (Sonnet), and none picked `🮆`.
4. **Chart-borne candidates, procedurally.** The same for `🨀 🨁 🨂 …` (contiguous, so undiscriminable on the chart route, which is the honest report) and the reasoned `♖ ♕ ♔ → ♓` (chart-reached).
5. **The triad era, informatively.** Of the 4,905 grown rows, the fraction with whole-run evidence, and what their parts and independence say.
6. **Agreement with what is plain.** BEST's current recognised and rejected sets agree with the catalog, and every disagreement is explained.
7. **Hand audit.** A sample of records is recomputed from the listed answers and rates.
8. **Posterior predictive checks.** Item-level spread against the model, with overdispersion reported.
9. **Stability.** When one more round is added, quantities whose evidence didn't change move by less than their own interval. Quantities whose evidence changed are listed, since asking is outcome-dependent.

## 15. Changes from version 3, by audit finding

- **C1, tier rules against definitions.** There are no stored tiers. Recorded instead: independence quantities, facts about discriminating positions, and discrimination status. The tiers become a default view with a frozen rule (§11). That rule defines "rational" by the candidate's provenance, not by deliberation. Undecided is never ranked. Markers are facts, not tier rules.
- **C2, what D discriminates.** D positions where the chart candidate is itself felt count as branch preferences. D gets a control. The name route is added: name-congruence measured by the name-only order question, and the honest case where names describe the look (§7).
- **C3, substitution.** A matched non-lookalike control. Coverage and the identity-not-style limit stated.
- **C4, contiguous runs.** "Undiscriminable" is a fact, not a rank. Chart-congruent runs are a view category of their own, not below "rational".
- **C5, triad departures.** Used now, as chart-independence evidence.
- **C6, tests.** Procedural; the canary is a finding; the freeze is defined against the seal.
- **C7, provenance.** Full and accurate, the disagreeing seeds included.
- **C8, the model.** Strength on the identified scale. Family weights where the chart can't help. Certainty as a Bayes factor at a stated prior, per control for L. D on a signed scale. Open choices made: Plackett–Luce, reversal-invariant; "can't tell" as its own category; the G mapping; sheet covariates.
- **C9, inputs.** Dropspot scope follows the port's rule. Pick nulls are G's null. Muse is its own rater. `limit` stated correctly. G calibrated on tendril branches, so METHODOLOGY's rule about why-asked stands. Skip tests reported, never both control and evidence.
- **C10, objects.** Picks beyond 8 are a fifth link state. `EVIDENCE_MIN` is named. The branch relation follows METHODOLOGY. The 24-glyph anchoring is a probing finding. Cycles relate to their period's runs.
