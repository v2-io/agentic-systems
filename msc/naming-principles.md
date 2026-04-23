# Naming Principles — Multi-Agent Vote Instructions

*This document is the shared-principles and instructions file for a distributed naming-sweep audit of the Agentic Systems research framework (AAD, TST, and adjacent parts). Multiple agents (Opus, Sonnet, Haiku from Claude; Gemini; Codex) each vote independently; then a script aggregates; then a fresh round of agents votes on the aggregate. The principles below apply to every agent in both rounds.*

## Why naming deserves a deliberate pass

Names are the user interface of a theory. Every reader — every future agent with 100% context turnover, every collaborator returning after months, every external reviewer auditing a section out of context — encounters the concepts through their names before they encounter the mathematics. A good name compresses the key intuition into a few syllables that survive working-memory pressure; a poor name forces the reader to re-derive what the concept means on each encounter, paying compounding interest forever.

Two concrete examples from the project make the stakes visible. *Satisfaction gap* and *control regret* are names that do work for the reader — after one exposure, the 2×2 disambiguation table organizes itself in the reader's head because the axes are evocatively and accurately named. By contrast, the *A2' sub-scope α₁ / α₂ / β partition* captures something load-bearing in the theory, but the name is a sequence of subscripts, primes, and Greek letters that requires a decoder ring on every encounter. The mathematics is the same quality in both cases; the naming is not.

**Memorable names are the substrate of communal imagination.** A community can argue about, extend, and apply *directed separation* more easily than it can argue about a thing with a clinical multi-word label, because the name has enough shape for a group of minds to get purchase on collectively. This matters most for a framework whose value is integrative — the work is done when others can wield the concepts without the original authors in the room.

The question is not "should we rename everything." It is: **which names are doing load-bearing work, which are coasting, which are causing friction, and where are the missing memorable-noun slots that would repay a deliberate act of naming?** Assume most names were first passes that got propagated by assuming they were deliberate when they were in incidental.

## Evaluation criteria

For each name you consider, weigh these axes. You do not need to score all of them explicitly; these are the kinds of considerations the notes column should capture when a vote is non-obvious.

1. **Self-descriptive vs. baggage-carrying.** A name can *describe* its referent from scratch ("information bottleneck") or *adopt* existing baggage from an adjacent field ("sector condition", "Lyapunov function"). Both can be right. Self-descriptive wins when the field lacks prior art; baggage-adoption wins when the prior art's structural intuitions should travel with the name. The worst outcome is a name whose *only* content is baggage when the theory means something subtly different.

2. **Familiarity gradient.** How many seconds of unfamiliarity does a trained reader in the adjacent field experience? Zero (they see "Lyapunov" and know what to expect) is usually good but occasionally dangerous (if the usage differs, the name creates false confidence). High unfamiliarity is usually bad but occasionally good (a novel name signals a novel concept).

3. **Memorable-noun potential.** Does the name render as a *thing* that can be named in discussion without paraphrase? "Chronica" is a thing. "The AAD complete interaction history with temporal ordering" is not. The asymmetry compounds across every conversation the community will ever have.

4. **Overload risk.** Does the word collide with other uses in the same project, or in adjacent AI/ML vocabulary? "Hierarchy" appears in Pearl's causal hierarchy, AAD's convention hierarchy, AAD's correlation hierarchy, and approximation tiering — four distinct uses in one framework, which is likely too many.

5. **Scope honesty.** Does the name over-promise relative to what the concept delivers? If a name suggests more generality, exactness, or novelty than the concept provides, it violates the same scope-honesty commitment that the rest of the framework holds itself to.

6. **Aging potential.** Some names harden into standard vocabulary; some drift into embarrassment; some become locked in by citation velocity even when better options become available. Names that are too cute age poorly; names that are too clinical never attract citation in the first place.

7. **Communal-imagination test.** The integrating test: *could a skilled reader, six months after first encounter, refer to this concept in a conversation without looking it up?* If yes, the name is compounding; if no, it is costing.

## Scope of eligible names

Broad. Any named thing — *or* currently-unnamed-but-recurring thing that would benefit from a name — anywhere in the project is eligible. Specifically:

- **Segment slugs.** The canonical identifiers like `#strategy-dag`, `#additive-coordinate-forcing`, `#separability-pattern`.
- **Concept names in prose.** Phrases like "satisfaction gap", "adaptive reserve", "directed separation", "orient cascade".
- **Symbol names.** Greek letters and subscripts that carry semantic load: α₁, α₂, β, η*, ρ, U_o, κ_processing, ε*, etc. Ask whether the symbol's English equivalent ("adaptive-gain regime" for α₂, "adaptive reserve" for Δρ*) would read better in prose.
- **Pattern and region names — including ones that don't yet have names.** The sector-persistence region in parameter space. The 1-anchor-plus-3-theorem structure. The cycle-as-a-whole. The inferential-force cascade across the C1/C2/C3 hierarchy. If you find yourself writing a paraphrase twice, it probably deserves a name.
- **Top-level document names and their sections.** README.md headings, NOTATION.md entries, FORMAT.md convention names, TODO.md section titles, CLAUDE.md section headers, OUTLINE.md part names. These are read more than any individual segment.
- **Segment section headers.** `## Formal Expression`, `## Epistemic Status`, `## Discussion`, `## Working Notes`, `## What Is Derived`. These are *public API* for outline-filtering under the presentation-neutral-segment affordance (see `PROPOSALS.md` §H.5). Renaming a header ripples; be deliberate.
- **The framework name itself** (AAD — *Adaptation and Actuation Dynamics*). Framework renames are expensive, but the current name has a known asymmetry (the "Actuation" half is a weaker fit than "Adaptation" for what Section II covers). Eligible, but treat with care, as naming collisions have already significantly narrowed our options.
- **msc/ files, reflections, spike names.** Even if a rename is not planned, brainstorming alternatives for the record is valuable — it makes the historical naming choices legible.
- **Unnamed methodologies or principles.** "Strengthen-first posture", "scope-honesty-as-architecture", "calibration laboratory framing" — these are working-vocabulary principles that may or may not have memorable forms. Propose alternatives or keep-votes.
- **Missing mental-model analogs or metaphors.** If explanations repeatedly reach for an intuition ("the agent as a projection whose contraction rate must exceed its target's drift") that isn't crystallized in a name, propose one. These are the highest-value discoveries because they don't exist yet.

**Rule of thumb:** if you would use the name (or paraphrase) repeatedly in a conversation about the theory, it's eligible.

## How to vote — table format

Write your votes as a markdown table with four columns:

```
| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| ... | ... | ... | ... |
```

### Weight scale

- **+3** — strong preference (strong rename *or* strong keep)
- **+1** — weak preference
- **-1** — explicit rejection (you considered this candidate change and reject it)

**Absence is not a vote.** Not including a name in your table means "no opinion." Vote explicitly for anything you considered, whether keep or change. This lets the aggregation distinguish "nobody thought about this" from "several agents looked and declined to change it."

### Example votes

**Explicit keep** (new-name = current-name, weight +3):

```
| satisfaction gap | satisfaction gap | +3 | Crispest named pair in the project; the 2×2 diagnostic works because the names work. Do not touch. |
```

**Strong rename** (new-name ≠ current-name, weight +3):

```
| #additive-coordinate-forcing | #forced-coordinates | +3 | Current name is Cauchy-FE-only; the Čencov metric-layer instance is not Cauchy-FE. "Forced coordinates" covers both machineries and preserves scope honesty. |
```

**Weak rename** (new-name ≠ current-name, weight +1):

```
| #strategic-composition | #equilibrium-composition | +1 | Reduces the "strategic" overload in Section III. Narrower and more scope-honest than "game-theoretic-composition". |
```

**Explicit rejection of a considered alternative** (weight -1):

```
| #separability-pattern | separability-staircase | -1 | Whimsical; fails the communal-imagination test. I'd rather #separability-ladder (see separate row). |
```

**Multiple alternatives for one current-name** (rank within the decision):

```
| #additive-coordinate-forcing | #forced-coordinates | +3 | ... |
| #additive-coordinate-forcing | #cauchy-coordinates | -1 | Undersells the Čencov 4th primary instance (not Cauchy-FE). |
| #additive-coordinate-forcing | #coordinate-forcing | +1 | Verb form; fine alternative if #forced-coordinates doesn't land. |
```

**Naming a currently-unnamed thing:**

```
| [unnamed: the sector-persistence region in parameter space] | persistence envelope | +1 | Engineering vocabulary, geometrically evocative. Currently referenced as "the region where the persistence condition holds" — verbose and non-memorable. |
```

**Header-name rename rejection:**

```
| ## Working Notes | ## Development Notes | -1 | "Working Notes" is established across FORMAT.md and every segment; rename would churn without benefit. Keep. |
```

**Symbol-to-English proposal:**

```
| α₁ (A2' fixed-gain sub-scope) | derived-gain regime | +1 | "This lands in α₁" is cryptic in prose; "this lands in the derived-gain regime" reads naturally. Keep α₁ as shorthand symbol. |
```

**Methodology or principle:**

```
| "strengthen-first posture" | "attempt the improbable" | -1 | "Strengthen-first" is actionable and precise; "attempt the improbable" is aspirational but less directive. Keep the current name. |
```

**Top-level document section:**

```
| README.md "What This Is" | README.md "What AAD Is" | +1 | Current section reads generically; naming the framework in the heading anchors the reader. Minor, opportunistic. |
```

**Framework name:**

```
| AAD (Adaptation and Actuation Dynamics) | AAD (Adaptation and Actuation Dynamics) | +3 | Recent rename (2026-04-16); further churn dilutes identity. The "Actuation" imperfection is real but a Section II preamble clarification handles it more cheaply than another rename. |
```

## Cold-start instruction (critical)

**Do not read other agents' brainstorms or vote files.** Do not read `msc/naming-brainstorm-2026-04-24.md` or any file under `msc/naming-votes/` — they will anchor your thinking and collapse the diversity this audit depends on.

Build your list from direct review of:

- `CLAUDE.md`, `TODO.md`, `OUTLINE.md` (and `01-aad-core/OUTLINE.md`)
- `FORMAT.md`, `NOTATION.md`, `LEXICON.md`, `README.md`
- `PROPOSALS.md` (current architectural portfolio — read for context, not for naming cues)
- Segment files under `01-aad-core/src/` , `02-tst-core/src/` and others — sample widely
- Your own judgment about what a skilled-reader-six-months-later would struggle to parse aloud

Unique discoveries are especially valuable. If you find an unnamed recurring pattern, formula, methodology, or metaphor that the theory uses but doesn't name, propose a name for it — that's where new memorable-noun slots get opened.

## What to return

Write your votes to `msc/naming-votes/{your-agent-id}.md` (create the directory if it doesn't exist). Use an agent-id that identifies your model clearly — e.g., `opus-1m`, `sonnet-4-6`, `haiku-4-5`, `gemini-2-5-pro`, `codex-gpt-5`.

Your file should contain:

1. **Brief header** identifying your model and a one-line summary of your approach (e.g., "Haiku 4.5 — focused on segment-slug legibility and symbol-to-English opportunities").
2. **The votes table** (the main content).
3. **Optional: principles-observations section** at the end. If during your review you noticed the principles file itself is under-specified on some axis — e.g., "I kept making decisions based on Greek-vocabulary aesthetics, which isn't explicit in the principles" — flag it here. These observations feed back into a refined principles document before round 2.

**Expected length:** 60+ rows. If under 20 it's probably an indication that you haven't looked hard enough. If the list is getting long, that's fine, but *be very thoughtful*. Quality over quantity.

## Meta-principle

Naming is irreducibly aesthetic. There is no derivation that settles it; there is only the accumulated judgment of many readers. Your vote is one data point among several. Be confident where you are; be honest where you are not; use the weight scale to express the difference.
