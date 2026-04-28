# Naming Principles — Multi-Agent Vote Instructions (refined edition)

## Cold-start instruction — read this BEFORE any orientation

**Do not read other agents' brainstorms, vote files, aggregations, or rename-mapping records before voting.** Specifically: do not read any file under `msc/naming/naming-votes/`, `msc/naming/naming-brainstorm-*.md`, `msc/naming/naming-aggregate-*`, `msc/naming/naming-alias-*.md`, `msc/naming/naming-cleanup-*.md`, or `msc/naming/naming-pilot-rename-plan.md`. These will anchor your thinking and collapse the diversity this audit depends on.

This rule fires *first* — before you read CLAUDE.md, TODO.md, OUTLINE.md, FORMAT.md, segment files, or anything else. The instruction is here at the top precisely because earlier rounds discovered that even glancing at a `git status` showing one of those files disclosed enough to anchor an agent's votes. If you've already read any of the excluded files in this session, disclose it explicitly in your principles-observations section (round-1 evidence: this is recoverable as long as it's marked).

Build your list from a *direct* review of the segment files and primary docs (next section).

## Source material

Read these to ground your votes:

- `CLAUDE.md`, `TODO.md`, `OUTLINE.md` (and `01-aad-core/OUTLINE.md`)
- `FORMAT.md`, `NOTATION.md`, `LEXICON.md`, `README.md`
- `PROPOSALS.md` — current architectural portfolio. Read for context, not for naming cues.
- Segment files under `01-aad-core/src/`, `02-tst-core/src/`, `03-logogenic-agents/src/`, `04-logozoetic-agents/src/` — sample widely; do not just scan slugs.
- Your own judgment about what a skilled-reader-six-months-later would struggle to parse aloud.

## Architectural invariants — NOT vote targets

Some structural commitments are now project-level architecture, not subjects of this round's voting. Note them and work *within* them rather than against them.

### Role-prefix discipline

**Every segment slug takes the form `{type-prefix}-{subject-noun}`.** The type prefix derives mechanically from the segment's `type:` frontmatter (one of FORMAT.md's vocabulary: `postulate`, `definition`, `scope`, `formulation`, `derived`, `result`, `corollary`, `hypothesis`, `normative`, `empirical`, `observation`, `discussion`, `measurement`, `proposed-schema`, `derivation`, `worked-example`, `detail`, `sketch`, `aside`). A small `TYPE_TO_PREFIX` mapping in `bin/align-slug` collapses overly-long type tokens into compact slug prefixes (currently `worked-example → example`; see `CLAUDE.md` §"Slug role-prefix mapping").

The pilot validated this discipline (commits `09ace17`, `3aa9e74`). Role-prefix addition is mechanical — `bin/align-slug --all` sweeps the repo. **You vote only on subject-nouns**, not on prefixes.

### Subject-noun-first slug naming

**Slugs name the *thing* the segment defines, not the *role* the segment plays in the argument.** "Condition", "pattern", "framework", "approach" as subject-nouns are placeholders that fail this principle. The subject-noun should be a memorable noun that survives the communal-imagination test (below). Canonical illustration from the pilot: `#scope-condition` named the segment's role (it stated *some condition*); the split into `#scope-adaptive-system` + `#scope-agency` named what each scope actually delimits — adaptive systems and agency, respectively.

### Greek / etymological vocabulary commitment

The framework deliberately uses a coherent Greek-rooted vocabulary for its core nouns: *chronica*, *prolepsis*, *aisthesis*, *aporia*, *epistrophe*, *praxis*, *logogenic*, *logozoetic*. New naming proposals should sit comfortably within this aesthetic register rather than introducing competing registers (clinical-bureaucratic, marketing-feature, mathematical-acronym, etc.). This isn't an absolute prohibition — `directed separation`, `satisfaction gap`, and `control regret` are excellent non-Greek names — but it is a strong preference principle.

### Three-document layout for naming workstream

`doc/naming-principles.md` (this file) holds the principles and instructions. `msc/naming/naming-pilot-rename-plan.md` holds specific rename mappings (landed and pending) — that file is excluded from rename sweeps so the mapping table survives them verbatim. `msc/naming/naming-votes/{agent-id}.md` is where you write your votes. Voters do not modify the pilot-rename-plan; the human reviewer does, after voting concludes.

### Methodology — separate passes for prefix and subject-noun

Going forward, role-prefix addition (mechanical, via `bin/align-slug`) and subject-noun renaming (judgment-heavy, via voting + `bin/rename-slug`) are executed in separate cycles. Bundling them creates two failure modes: the segment's prose drifts out of step with its new identity, and voters cannot vote cleanly on the noun choice when the prefix is decided in the same cycle. **This round votes only on subject-nouns** (and on the other vote categories below — canonicalizations, aliases, name-unnamed-thing). Do not propose role-prefix changes; those are the script's job.

## Why naming deserves a deliberate pass

Names are the user interface of a theory. Every reader — every future agent with 100% context turnover, every collaborator returning after months, every external reviewer auditing a section out of context — encounters the concepts through their names before they encounter the mathematics. A good name compresses the key intuition into a few syllables that survive working-memory pressure; a poor name forces the reader to re-derive what the concept means on each encounter, paying compounding interest forever.

Two concrete examples from the project make the stakes visible. *Satisfaction gap* and *control regret* are names that do work for the reader — after one exposure, the 2×2 disambiguation table organizes itself in the reader's head because the axes are evocatively and accurately named. By contrast, the *A2' sub-scope α₁ / α₂ / β partition* captures something load-bearing in the theory, but the name is a sequence of subscripts, primes, and Greek letters that requires a decoder ring on every encounter. The mathematics is the same quality in both cases; the naming is not.

**Memorable names are the substrate of communal imagination.** A community can argue about, extend, and apply *directed separation* more easily than it can argue about a thing with a clinical multi-word label, because the name has enough shape for a group of minds to get purchase on collectively. This matters most for a framework whose value is integrative — the work is done when others can wield the concepts without the original authors in the room.

The question is not "should we rename everything." It is: **which names are doing load-bearing work, which are coasting, which are causing friction, and where are the missing memorable-noun slots that would repay a deliberate act of naming?** Assume most names were first passes that got propagated by assuming they were deliberate when they were incidental.

## Vote categories

Each vote belongs to exactly one of these categories. Marking the category in your notes column lets the aggregation distinguish them and lets the human reviewer apply the right judgment at landing time.

1. **Rename.** The current name fails (overclaims, underclaims, is hard to remember, collides with another use, doesn't survive the renamed-from-now-sounds-weird test). Propose a replacement subject-noun.
2. **Keep.** The current name is right and shouldn't be changed. Voted explicitly so the aggregation distinguishes "considered and kept" from "no opinion expressed." High-weight keeps protect names whose churn would cost more than it returns.
3. **Canonicalize.** The current concept *has* a name, but prose paraphrases it three different ways across the repo. Vote canonicalize to commit: "going forward, always reference this as X — stop paraphrasing." Distinct from keep because keep doesn't address paraphrase drift.
4. **Add-alias.** The current name is fine for one register but a parallel name in another register would help. Most common case: a Greek/symbol name (α₁, α₂, $\Delta\rho^*$) gets an English alias for use in prose ("the derived-gain regime", "the adaptive reserve"). Symbol stays as shorthand; alias enters prose. Note: the symbol+alias pair becomes a maintained convention.
5. **Name-unnamed-thing.** A recurring pattern, region, formula, methodology, or metaphor that the theory uses repeatedly but never named. Propose a memorable-noun name for it. These are the highest-value discoveries because the slot is empty — no displacement cost, pure clarity gain.

## Evaluation criteria

For each name you consider, weigh these axes. You do not need to score all of them explicitly; these are the kinds of considerations the notes column should capture when a vote is non-obvious.

1. **Self-descriptive vs. baggage-carrying.** A name can *describe* its referent from scratch ("information bottleneck") or *adopt* existing baggage from an adjacent field ("sector condition", "Lyapunov function"). Both can be right. Self-descriptive wins when the field lacks prior art; baggage-adoption wins when the prior art's structural intuitions should travel with the name. The worst outcome is a name whose *only* content is baggage when the theory means something subtly different.

2. **Familiarity gradient.** How many seconds of unfamiliarity does a trained reader in the adjacent field experience? Zero (they see "Lyapunov" and know what to expect) is usually good but occasionally dangerous (if the usage differs, the name creates false confidence). High unfamiliarity is usually bad but occasionally good (a novel name signals a novel concept).

3. **Memorable-noun potential.** Does the name render as a *thing* that can be named in discussion without paraphrase? "Chronica" is a thing. "The AAD complete interaction history with temporal ordering" is not. The asymmetry compounds across every conversation the community will ever have.

4. **Overload risk.** Does the word collide with other uses in the same project, or in adjacent AI/ML vocabulary? "Hierarchy" appears in Pearl's causal hierarchy, AAD's convention hierarchy, AAD's correlation hierarchy, and approximation tiering — four distinct uses in one framework, which is likely too many.

5. **Scope honesty.** Does the name over-promise relative to what the concept delivers? If a name suggests more generality, exactness, or novelty than the concept provides, it violates the same scope-honesty commitment that the rest of the framework holds itself to.

   *Special case for meta-segments.* When a segment names a project-wide pattern (the meta-segments under `01-aad-core/src/discussion-*.md`), scope-honesty dominates memorability. A memorable-but-narrow name (e.g., `#cauchy-coordinates` for what is now `#discussion-additive-coordinate-forcing`) is worse than an awkward-but-accurate name (`#discussion-forced-coordinates`) when the narrow name fails to cover one of the four primary instances. The Round-1 lesson: meta-pattern names reach across many segments; over-narrow ones force prose qualifications elsewhere.

6. **Aging potential.** Some names harden into standard vocabulary; some drift into embarrassment; some become locked in by citation velocity even when better options become available. Names that are too cute age poorly; names that are too clinical never attract citation in the first place.

7. **Communal-imagination test.** The integrating test: *could a skilled reader, six months after first encounter, refer to this concept in a conversation without looking it up?* If yes, the name is compounding; if no, it is costing.

8. **Renamed-from-now-sounds-weird test.** Imagine the project six months from now, the proposed name installed and in routine use. Does the *old* name now sound quaint, dated, or naive — clearly inferior, *of course we renamed it*? Or does the *new* name sound forced, pretentious, like a thing someone tried to make happen? Strong renames pass this test in the first direction; weak renames fail it in the second.

## Scope of eligible names

Broad. Any named thing — *or* currently-unnamed-but-recurring thing that would benefit from a name — anywhere in the project is eligible.

### Naming layers (be aware which layer your vote operates on)

Friction often comes from mixing layers. Note in your vote which layer you're operating on:

- **Slug layer.** Canonical identifiers like `#strategy-dag`, `#discussion-additive-coordinate-forcing`, `#scope-agency`. Subject-nouns only this round (per architectural invariants); prefix is set by `type:`.
- **Prose-symbol layer.** Default English forms used when prose references a symbol (`α₁` → "the derived-gain regime"). Add-alias votes typically operate here.
- **Framing-vocabulary layer.** The high-level posture words: "scope-honesty-as-architecture", "calibration laboratory", "strengthen-first posture", "integrating framework". These shape how the project presents itself in introductions and abstracts.
- **Public-API layer.** Section header names (`## Formal Expression`, `## Epistemic Status`, `## Discussion`, `## Working Notes`), framework name (`AAD`, `ASF`), document titles. Read more than any individual segment; rename is expensive.

### Eligible categories

- **Segment subject-nouns.** Slug suffix after the role-prefix. (`#discussion-separability-pattern` → vote on `separability-pattern`; the `discussion-` is fixed by type.)
- **Concept names in prose.** Phrases like "satisfaction gap", "adaptive reserve", "directed separation", "orient cascade".
- **Symbol-to-English aliases.** α₁, α₂, β, η*, ρ, U_o, κ_processing, ε*, etc. — propose English aliases via add-alias category.
- **Pattern and region names — including ones that don't yet have names.** The sector-persistence region in parameter space. The cycle-as-a-whole. The inferential-force cascade across the C1/C2/C3 hierarchy. Use name-unnamed-thing category.
- **Top-level document names and their sections.** README.md headings, NOTATION.md entries, FORMAT.md convention names, TODO.md section titles, CLAUDE.md section headers, OUTLINE.md part names.
- **Framework name itself** (AAD, ASF). Renames here are expensive; treat with extreme care. Note that ASF is the *intentional* parent-level name (AAD is Part I, TST is Part II); earlier rounds misread it as debt.
- **Methodologies and principles.** "Strengthen-first posture", "scope-honesty-as-architecture", "calibration-laboratory framing".

### Acronym discipline

Every new acronym carries a maintenance cost: future readers must memorize it; collisions with adjacent literatures must be checked (recall the ACT → AAD rename forced by the AI Consciousness Test collision); tooling must reference it consistently. Propose new acronyms only when (a) the expanded form will be used 10+ times in nearby prose, (b) the acronym survives the communal-imagination test on its own (without expansion), and (c) you've spot-checked for collisions in the AI/ML / control / cognitive-science literatures. When in doubt: don't add an acronym; the unrolled phrase compounds less interest than a forgettable initialism.

**Rule of thumb:** if you would use the name (or paraphrase) repeatedly in a conversation about the theory, it's eligible.

## How to vote — table format

Write your votes as a markdown table with five columns:

```
| current-name | new-name-candidate | category | weight | notes |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
```

The `category` column is one of: `rename`, `keep`, `canonicalize`, `add-alias`, `name-unnamed`. Use the same category vocabulary (no abbreviations).

### Weight scale

- **+3** — strong preference. Strong rename; load-bearing keep; name urgently needed.
- **+2** — moderate preference. Visible improvement; defended-keep against a reasonable alternative.
- **+1** — weak preference. Mild improvement; acceptable-keep.
- **−1** — explicit rejection. You considered this candidate and reject it.

The +2 level was added after Round 1 (where +1/+3 collapsed "acceptable-keep" and "load-bearing-keep" into the same bucket). Use +2 deliberately when the strength of conviction is between weak and strong — the difference matters for aggregation.

**Absence is not a vote.** Not including a name in your table means "no opinion." Vote explicitly for anything you considered, whether keep or change. This lets the aggregation distinguish "nobody thought about this" from "several agents looked and declined to change it."

### Example votes

**Strong rename:**
```
| #discussion-additive-coordinate-forcing | #discussion-forced-coordinates | rename | +3 | Current "additive" doesn't cover the Čencov-Fisher 4th instance; "forced-coordinates" covers both Cauchy-FE and Čencov machineries. Scope-honesty for meta-segment dominates. |
```

**Defended keep:**
```
| satisfaction gap | satisfaction gap | keep | +3 | Crispest named pair in the project; the 2×2 diagnostic works because the names work. Rename would lose load-bearing prose conventions. |
```

**Canonicalize (commit to existing name; stop paraphrasing):**
```
| "calibration laboratory" | "calibration laboratory" | canonicalize | +3 | Currently appears as "richest operationalization domain", "best operationalization domain", and "calibration laboratory" across CLAUDE.md and TST OUTLINE. Standardize on the third. |
```

**Add-alias (symbol + English):**
```
| α₁ (A2' fixed-gain sub-scope) | "derived-gain regime" | add-alias | +1 | "This lands in α₁" reads cryptically in prose; "this lands in the derived-gain regime" reads naturally. Keep α₁ as shorthand symbol. |
```

**Name-unnamed-thing:**
```
| [unnamed: the sector-persistence region in parameter space] | "persistence envelope" | name-unnamed | +2 | Engineering vocabulary, geometrically evocative. Currently referenced as "the region where the persistence condition holds" — verbose and non-memorable. |
```

**Explicit rejection:**
```
| #discussion-separability-pattern | #discussion-separability-staircase | rename | -1 | "Staircase" is whimsical and fails the communal-imagination test. "Ladder" (separate row) is the right metaphor. |
```

**Multiple alternatives for one current-name (rank with weight):**
```
| #discussion-additive-coordinate-forcing | #discussion-forced-coordinates | rename | +3 | Best fit per scope-honesty and meta-segment criteria. |
| #discussion-additive-coordinate-forcing | #discussion-cauchy-coordinates | rename | -1 | Undersells the Čencov 4th instance (not Cauchy-FE). |
| #discussion-additive-coordinate-forcing | #discussion-coordinate-forcing | rename | +1 | Verb form; acceptable alternative if forced-coordinates doesn't land. |
```

## What to return

Write your votes to `msc/naming/naming-votes/{your-agent-id}.md` (create the file if it doesn't exist). Use an agent-id that identifies your model clearly — e.g., `opus-4-7-r2`, `sonnet-4-6-r2`, `haiku-4-5-r2`, `gemini-2-5-pro-r2`, `codex-gpt-5-r2`. The `r2` suffix marks this as the refined-Round-1 contribution.

Your file should contain:

1. **Brief header** identifying your model and a one-line summary of your approach (e.g., "Sonnet 4.6 refined Round 1 — focused on subject-nouns failing the renamed-from-now-sounds-weird test.").
2. **The votes table** (the main content).
3. **Optional but encouraged: principles-observations section** at the end. Did you find this principles file under-specified anywhere? Did you find yourself making decisions on a criterion that isn't named here? Did the cold-start instruction work for you, or was it under-protective? These observations feed into future principles refinement.

**Expected length:** 60+ rows. If under 20, you probably haven't looked hard enough. If approaching 200, prioritize quality over count. Symbol-to-English aliases and name-unnamed-thing entries count toward the total but should be reasoned, not mechanical.

## Meta-principle

Naming is irreducibly aesthetic. There is no derivation that settles it; there is only the accumulated judgment of many readers. Your vote is one data point among several; the multi-architecture aggregation across this round + future rounds is how the project converges. Be confident where you are; be honest where you are not; use the weight scale to express the difference.
