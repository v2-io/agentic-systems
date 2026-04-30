# Mini-lexicon TODO — naming-cycle items the vote schema can't naturally absorb

**Status:** working artifact, 2026-04-29.

The R1/R2 vote schema is built around "vote on a candidate name for a target concept" — rename, keep, canonicalize, add-alias, name-unnamed. A substantial fraction of what voters surfaced doesn't fit that shape: notation collisions, project-level register conventions, gloss/pedagogy proposals, section-title concerns, multi-action votes, investigation-required items, deprecation lists. Trying to shoehorn these into the candidate-name slot has been creating noise.

Decision (Joseph, 2026-04-29) is to *stop trying*: leave the malformed votes in the corpus, accept that R2 voters will work around them via write-ins where they have ideas, and capture the substantive content here as a separate punch-list. Each item is something a future agent (or Joseph) can pick up and act on.

Sources walked: [`master-list-full.md`](master-list-full.md), [`explanatory-candidate-scan.md`](_archive/explanatory-candidate-scan.md), [`round-2-plan.md`](round-2-plan.md), [`naming-tier2-classification-log.md`](_archive/naming-tier2-classification-log.md), [`/doc/naming-principles.md`](../../doc/naming-principles.md), [`TODO.md`](../../TODO.md). Joseph's nine annotations on the explanatory-candidate-scan high-confidence tier seeded the categorization.

Cross-references rather than duplicates: where the substantive concern is already tracked in `TODO.md` or `round-2-plan.md`, the entry is a one-liner pointing there.

---

## Contents

1. [Notation collisions and symbol disambiguation](#1-notation-collisions-and-symbol-disambiguation) — 5 items
2. [Project-level register and reservation conventions](#2-project-level-register-and-reservation-conventions) — 6 items
3. [Gloss / pedagogy / Brief-field material misfiled as candidate names](#3-gloss--pedagogy--brief-field-material-misfiled-as-candidate-names) — 4 items
4. [Section title and document structural choices](#4-section-title-and-document-structural-choices) — 4 items
5. [Multi-action / decomposition-required votes](#5-multi-action--decomposition-required-votes) — 5 items
6. [Investigation-required items (vote underspecified what it points at)](#6-investigation-required-items-vote-underspecified-what-it-points-at) — 4 items
7. [Voice / register / lexicon-coherence concerns](#7-voice--register--lexicon-coherence-concerns) — 3 items
8. [Acronym / abbreviation conventions](#8-acronym--abbreviation-conventions) — 3 items
9. [Deprecation / avoid lists](#9-deprecation--avoid-lists) — 1 consolidated item
10. [Cross-component naming consistency](#10-cross-component-naming-consistency) — 2 items
11. [Collision check — external naming overlaps with adjacent literature](#11-collision-check--external-naming-overlaps-with-adjacent-literature) — sweep results, post-R2 surgery list
12. [Post-cohort followups — substrate handoff analysis](#12-post-cohort-followups--substrate-handoff-analysis) — Pro→Flash continuation; rationale-attribution analysis pending

---

## 1. Notation collisions and symbol disambiguation

These need a small symbol-rename or NOTATION-discipline decision, not a name-vote on a concept. They surface in the corpus as multi-token rows whose "candidate" is really a fix-direction, not a name.

### 1.1 `$U_M$` dual use: model uncertainty (§I) vs. epistemic unity (§III)

**Issue:** `$U_M$` is used for two different quantities. In Section I it is *model uncertainty* (one factor in the update gain $\eta^\ast = U_M / (U_M + U_o)$). In Section III it is the *epistemic unity dimension* of the unity-axes vocabulary. Disambiguated only by domain; will create reader stumbles and citation drift.

**Sources:** [master-list §346, §347](master-list-full.md) — codex-gpt-5-r2 (+3 canonicalize), opus-4-7-b (+3 rename, names this "the most important notation-layer issue I found in the sweep"). Per Joseph's annotation on row 1 of the explanatory-candidate-scan: needs to be split into separate canonicalize votes, one per quantity.

**Proposed actions** (from votes; not yet adjudicated):
- Use `$U_M$` for model uncertainty; rename the unity-dimension to `$\Upsilon_M$` (capital upsilon — Greek-letter-distinct from U) or `$U_{\mathcal M}$` (calligraphic subscript).
- Or rename the model-uncertainty side; less proposed.

**Status:** open. Not naturally absorbed by R2 — needs a notation-discipline decision plus segment edits. Best path is probably to land the symbol-rename then re-fold the corpus rows once disambiguation is done.

**Priority hint:** HIGH. Citation velocity makes the cost of fixing this rise over time; landing the change pre-paper-draft is cheap.

### 1.2 `$U_o$` vs `$U_O$` case-collision

**Issue:** Lowercase `$U_o$` (observation uncertainty) vs uppercase `$U_O$` (teleological unity). The case distinction is fragile in serif fonts, indistinguishable when read aloud, and they appear in adjacent prose contexts (the orient cascade discusses both).

**Sources:** [master-list §677, §678](master-list-full.md) — codex-gpt-5-r2 (+2 canonicalize), opus-targeted-alternatives-v2 (+2 rename, "real notation-discipline concern that costs reader-time on every encounter"), opus-4-7 (+1 rename).

**Proposed actions:**
- Rename teleological unity to `$U_\Omega$` (Greek omega for objective/outcome) — most proposed.
- Or `$U_{\text{goal}}$` — heavier in formula but more discoverable.

**Status:** open. Proposed alongside 1.1 — both need a single coordinated NOTATION pass. Pairs with 1.1's $\Upsilon$ option if the unity-dimensions get unified Greek-letter treatment.

**Priority hint:** HIGH. Same reasoning as 1.1.

### 1.3 `$U_o$ / $U_O$ / $U_M$ / $U_\Sigma$ / $U_{\text{obs}}$ / $U_f$` unity family — overall structure

**Issue:** The unity-dimensions family lacks a coordinated naming convention. Codex proposed `unity coordinates` as an umbrella; `$U_{\text{src}}$ / $U_{\text{align}}$` got a "trust uncertainties" alias; individual members get varied prose handles.

**Sources:** [master-list §674, §675, §676, §679](master-list-full.md). Pairs with 1.1 / 1.2 as the same notation cluster.

**Proposed actions:** Coordinated NOTATION pass that decides the symbol convention for the whole family at once (uppercase U with subscript, or $\Upsilon$ with subscript, or text-subscripted form). Per-member English aliases (epistemic unity / teleological unity / strategic unity) are already canonical in NOTATION.md per several +2/+3 add-alias votes.

**Status:** open. Should be one decision, not four.

### 1.4 `$\rho$` overload / register-split

**Issue:** `$\rho$` carries multiple readings ("disturbance rate", "environmental change rate", "mismatch injection rate") with no canonical English handle. The phrase "environmental change rate" should be deprecated to one-time first-encounter expansion (per opus-targeted-alternatives-v2 master-list line 13173).

**Sources:** [master-list §870 `mismatch injection rate`](master-list-full.md), §933 `$\rho$ disturbance rate`, related rows around `gemini-targeted-alternatives` "effective disturbance $\rho$" canonicalize +3.

**Proposed actions:** Canonicalize "disturbance rate" as the prose handle; `$\rho$` stays as the symbol; deprecate "environmental change rate" except as one-time expansion.

**Status:** open; relatively cheap. Could land as a NOTATION + LEXICON edit independent of any vote.

### 1.5 `$\eta^\ast$` vs ML "learning rate" collision

**Issue:** `$\eta^\ast$` is the *update gain* — a Bayesian uncertainty ratio, not a stochastic-gradient-descent step size. The collision with ML's "learning rate" creates false familiarity. opus-targeted-alternatives-v2 explicitly rejected "learning rate" as alias on this ground (master-list line 6420).

**Sources:** master-list per-row entries on $\eta^\ast$ and `update gain`.

**Proposed actions:** Deprecate "learning rate" as alias for $\eta^\ast$; canonicalize "update gain" or "uncertainty ratio" in prose. Pairs with deprecation list (item 9.1).

**Status:** open. NOTATION-level discipline call.

---

## 2. Project-level register and reservation conventions

These are policy decisions about how a word is used project-wide — register splits, reserved-meaning declarations, prose discipline. They're orthogonal to "what should we call concept X."

### 2.1 Reserve `hierarchy` for Pearl's strict-asymmetric uses

**Issue:** "Hierarchy" appears with four distinct meanings in the framework: Pearl's causal hierarchy (external, adopted), AAD's convention hierarchy, AAD's correlation hierarchy (L0/L1/L2), AAD's approximation tiering. Four uses in one project is overloaded enough to cost reader-time. opus-4-7-b proposed: reserve "hierarchy" for Pearl's and other strict-asymmetric orderings; rename internal AAD uses to "ladder," "partition," or "tier-set."

**Sources:** [master-list §863 `hierarchy project wide`](master-list-full.md) — opus-4-7-b (+1 rename), explanatory-candidate-scan high-conf row 8 with Joseph's annotation: "vote to *not* use it for whatever it is being used for that the agent objected to, and a vote *to* use it elsewhere unspecified." opus-4-7 +1 rename on `hierarchy as a project wide word` flagging the four-way overload. agent1-original-brainstorm "hierarchy as repeated word" — flagged but proposal weak.

**Proposed actions:**
- Project-wide convention: "hierarchy" reserved for Pearl's (external, adopted) and other strict-asymmetric orderings.
- For internal AAD overloads, separate naming pass (some already candidates in master-list: `correlation ladder`, `convention ladder` etc).

**Status:** open; convention-level decision. Pairs with the Round-1 consensus rename `#disc-separability-pattern` → `#disc-separability-ladder` (already in TODO.md naming-pipeline section).

**Priority hint:** MEDIUM-HIGH. Cheap to declare; pays compounding interest.

### 2.2 `chronica` capitalization convention

**Issue:** Mixed usage in segments — "Chronica" capitalized vs "chronica" lowercase. NOTATION shows `$\mathcal{C}_t$` in formalism and *chronica* in italics in lexicon-style references. Convention not yet enforced.

**Sources:** [master-list §849](master-list-full.md) — opus-4-7-b (+1 rename "chronica lowercase in running prose"); explanatory-candidate-scan high-conf row 7 with Joseph's annotation: gloss-statement put in quotes, allow gloss-statements like this in candidate fields with double-quote delimiters that aren't normalized. opus-4-7-r2 (+2 canonicalize) on `crèche / creche` for the analogous capitalization+diacritic decision: crèche-with-diacritic in framing prose, creche in slugs.

**Proposed actions:** Project-wide: lowercase italicized *chronica* in running prose; `$\mathcal{C}_t$` in math; `Chronica` (capitalized) only in section titles or where formal proper-noun reading is intended.

**Status:** open; cheap convention decision. Same shape as the crèche/creche call.

### 2.3 "AAD" vs "ASF" disambiguation discipline

**Issue:** AAD is the mathematical core (Sections I/II/III + Appendices); ASF is the parent framework (AAD as Part I, TST as Part II, logogenic/logozoetic as Parts III/IV). Earlier voting rounds misread ASF as debt; CLAUDE.md and naming-principles.md now flag ASF as intentional, but prose still drifts.

**Sources:** [master-list §245 `ASF acronym`](master-list-full.md), [§702 `AAD theoretical core vs ASF framework`](master-list-full.md) — opus-4-7-r2 (+2 canonicalize), gemini-targeted-alternatives (+2 rename to "AAD vs ASF distinction"). Noted in master-list as a +5 keep cluster on ASF itself.

**Proposed actions:** Canonicalize: when discussing math, "AAD"; when discussing the framework as a whole, "ASF"; when discussing a domain instantiation, the specific component name (TST, logogenic-agents, logozoetic-agents). Project-wide editorial discipline pass — not a rename.

**Status:** open; convention-level. Cheap to land via README + CLAUDE.md edits.

### 2.4 "intent" / "objective" / "purpose" register split

**Issue:** Three terms used semi-interchangeably; opus-4-7-r2 proposed canonical roles: "intent" for the agent's own commitment-flavored representation of $G_t$; "objective" for $O_t$ specifically; "purpose" as the framework-level integrative term. The three are not interchangeable — using them as if they were creates drift.

**Sources:** [master-list §865 `intent planning vocabulary`](master-list-full.md) — opus-4-7-r2 (+1 canonicalize).

**Proposed actions:** Canonicalize the three-way split; LEXICON entry; prose-discipline pass over segments where the terms drift.

**Status:** open; LEXICON-level decision. Lower priority than 2.1 but same shape.

### 2.5 "AAD-internal" vs "AAD-derived" vs "internally" register

**Issue:** The "internally-derived-from-AAD-axioms" move is referenced as "AAD-internal," "AAD-derived," and "internally." Three paraphrases of the same operation create drift.

**Sources:** [master-list `AAD AAD internal AAD internally`](master-list-full.md) — opus-4-7-r2 (+2 canonicalize): adjective form "AAD-internal", adverb "AAD-internally."

**Proposed actions:** Canonicalize the adjective/adverb pair; one-time editorial sweep.

**Status:** open; cheap.

### 2.6 Greek-vocabulary prose discipline

**Already captured** in [`TODO.md`](../../TODO.md) §"Greek vocabulary prose discipline (audit + author finding, 2026-04-29)". The audit-471203 finding: Greek terms appear at framing/preamble/lexicon levels but segment-level math doesn't depend on the distinctions; the README's claim that each Greek term names a distinction English flattens is overclaimed against current segment prose. Two paths: tighten segment prose to make the distinctions do work, or soften the README's framing.

**Cross-reference:** [`TODO.md`](../../TODO.md) §"Greek vocabulary prose discipline".

**Status:** *referenced in TODO.md*. No action here; this list points at it because R2 votes near-unanimously *defended* the Greek terms synoptically while the audit's incremental walk surfaced what the synoptic glance is structurally blind to — exactly the cross-mechanism gap that motivates this whole TODO's existence.

---

## 3. Gloss / pedagogy / Brief-field material misfiled as candidate names

Auditors offered prose explanations as candidate names — "the river that the agent's identity is downstream of" (chronica), "the agent's choice actually changes what happens" (Pearl-Level-2). These are casual-curious-reader Brief-field material, not candidate names. They belong in `## Findings` Brief fields (per the Feynman-criterion convention), in LEXICON glosses, or in README paragraphs.

### 3.1 `chronica` Feynman-grade gloss: "the river that identity is downstream of"

**Issue:** Auditor offered this as a candidate name; really a Brief-field gloss for the layperson. The slug stays.

**Sources:** [explanatory-candidate-scan high-conf row 3](_archive/explanatory-candidate-scan.md), Joseph's annotation: "definitely not a vote for canonicalize, and allow gloss statements like this with double-quote delimiters that aren't normalized by the script". From audit-471203-incremental on `04-def-chronica`.

**Proposed actions:** Drop into `#def-chronica` Findings Brief; cross-link from LEXICON `Chronica` entry. Possibly into README's loop section. Verify the gloss actually preserves the Greek's distinction (records-of-time, not just history).

**Status:** open; cheap editorial. Pairs with 3.4 (Walton's bathtub gloss) as a class of "Brief-field-grade glosses surfaced by auditors."

**Priority hint:** MEDIUM. Brief-field discipline is currently aspirational across the corpus; chronica is a good test-case.

### 3.2 Pearl-Level-2 plain-language gloss: "the agent's choice actually changes what happens"

**Issue:** Same shape as 3.1. Brief-grade gloss for `pearl-level-2-causal-contrast` from audit-471203-incremental. Master-list has it filed as canonicalize +1, which it isn't.

**Sources:** [explanatory-candidate-scan high-conf row 13](_archive/explanatory-candidate-scan.md). Master-list §`pearl-level 2 causal contrast`.

**Proposed actions:** Move gloss into `#der-loop-interventional-access` Findings Brief or the relevant Pearl-vocabulary segment. README's loop-as-causal-engine section is a candidate location.

**Status:** open; cheap.

### 3.3 `chronica` (Brief gloss) — "everything the agent has lived through"

**Issue:** Different gloss for chronica than 3.1, also misfiled as canonicalize. Master-list `chronica brief gloss | everything the agent has lived through | canonicalize | +1` from audit-471203-incremental.

**Sources:** [master-list §716, master-list per-row](master-list-full.md). Pair with 3.1.

**Proposed actions:** Decide which gloss to use in the Brief field. "Everything the agent has lived through" is more accessible; "the river identity is downstream of" carries more structural weight (identity-downstream-of-trajectory is exactly the AAD claim). May land both in different registers (LEXICON gloss vs README sentence).

**Status:** open; pairs with 3.1.

### 3.4 Walton's bathtub gloss for the persistence condition

**Already captured** in [`TODO.md`](../../TODO.md) §"README v2 pass" — Alan Walton's bathtub gloss (water = belief-reality gap; faucet = environmental change rate; drain = learning rate; bathtub size = model class capacity; overflow when faucet outpaces drain at full) flagged for promotion into `#result-persistence-condition`'s Findings Brief and possibly the README. Canonical example of the Feynman-criterion benchmark.

**Cross-reference:** [`TODO.md`](../../TODO.md) §"README v2 pass" → Surfaced from Alan's review.

**Status:** *referenced in TODO.md*.

---

## 4. Section title and document structural choices

These are votes on document structure, not on theory concept names. Some are legitimate (the section headers do influence reader experience), but they're a different beast from concept-naming.

### 4.1 README §"What This Is" — generic vs framework-named

**Issue:** README's `## What This Is` section heading is generic in isolation; multiple voters proposed that the framework name should anchor the reader immediately ("What Agentic Systems Is" or "What AAD Is"). Counter-argument: the README is AAD-level (Part I), not framework-level — naming AAD in the heading would mis-frame it.

**Sources:** [master-list §522 `readme md what this is`](master-list-full.md) — codex-1, codex-2, opus-4-7 (+1 rename to "What Agentic Systems Is"); gemini-2 (+3 rename to "Core Thesis"); opus-4-7-b (-1 rename to "What AAD Is"). Multiple competing alternatives.

**Proposed actions:** README v2 pass should make the call. Already implicitly inside scope of [`TODO.md`](../../TODO.md) §"README v2 pass" but not explicitly listed.

**Status:** *adjacent to* [`TODO.md`](../../TODO.md) §"README v2 pass". Worth surfacing as a specific README-cycle item.

### 4.2 Section titles for AAD-core (I / II / III)

**Issue:** Multiple votes (`section i adaptive systems under uncertainty`, `section ii actuated adaptation agentic systems`, `iii agentic composites`) involve formatting standards (presence of "Section " prefix) and substantive title choices ("Actuated Adaptation" vs "Purposeful Adaptation" vs "Agentic Systems" for Section II, where "Actuated" is the weaker semantic fit).

**Sources:** [master-list rows for section i/ii/iii titles](master-list-full.md). Joseph's annotation on explanatory-candidate-scan row 6: "normalizer should know about section titles — divide into parts if that's better."

**Proposed actions:**
- Convention pass: do or don't include "Section " prefix in OUTLINE / paper / file headers.
- Substantive call on Section II title: "Actuated Adaptation: Agentic Systems" (current) vs alternatives. Joseph and codex-2 have noted "Actuated" reads slightly off; this is downstream of the AAD-rename decision (2026-04-16) which deliberately chose "Actuation" over "Agency" / "Purpose."

**Status:** open. Pre-paper-draft is the natural deadline; not blocking now.

**Priority hint:** MEDIUM (formatting convention is cheap; substantive title is locked-in).

### 4.3 `## Working Notes` / `## Epistemic Status` / `## Formal Expression` / `## Discussion` — keep as-is

**Issue:** Several voters voted *keep* on these segment-section headers. Codex-2 (+3 keep "Working Notes"): "Clear, conventional, and exactly right for the internal/public boundary it marks." These aren't candidate-naming subjects; they're FORMAT.md public-API conventions.

**Sources:** [master-list §72, §111, §137, §63 and related section-header rows](master-list-full.md). Treated as keeps in Tier-2 retro-classification.

**Proposed actions:** None — these are FORMAT.md API conventions and renaming would propagate across hundreds of segments. The "votes" are essentially affirmations.

**Status:** *referenced in [doc/naming-principles.md](../../doc/naming-principles.md) §"Public-API layer"* — already flagged as expensive to rename.

### 4.4 README's "Convergent Choices" / "Maturity Gradient" / "Novel Results" / "Cross-Domain Joining" headings

**Issue:** Several README §-heading rename proposals: "Convergent Choices" → "Convergent Formulations" (+3 codex-1) or "Forced by Failure Choices" (+1 opus-4-7); "Cross-Domain Joining" → "Cross-Domain Mappings" (+3 codex-1, +1 opus-4-7-b — "joining" slightly non-idiomatic); "Maturity Gradient" → "Theory Maturity Gradient" (+1 codex-1) or keep (+1 opus-4-7-b, +1 opus-4-7).

**Sources:** [master-list §520-§522 and §763, §764](master-list-full.md).

**Proposed actions:** Land alongside the README v2 pass. Each is a small, independent decision. "Convergent Choices" deserves the most thought because it names a rare AAD construct (intermediate between "derived" and "chosen") and the substitution candidate "Convergent Formulations" reads as more descriptively accurate while preserving the construct.

**Status:** *adjacent to* [`TODO.md`](../../TODO.md) §"README v2 pass". Worth surfacing as specific items in the cycle scope.

---

## 5. Multi-action / decomposition-required votes

Single rows that bundle multiple distinct decisions. These can't be aggregated cleanly because the row's weight applies to the bundle, not to any individual move.

### 5.1 `instance 1 / 2 / 3 of identifiability floor` → split into three named instances

**Issue:** A single row proposes renaming "Instance 1, Instance 2, Instance 3" to three substantive names: "latent common cause floor / unobservable mixture floor / coupling sign floor." That's three distinct decisions bundled in one vote, with one weight.

**Sources:** [master-list §470](master-list-full.md), gemini-1 (+3 rename); explanatory-candidate-scan row 4 with Joseph's annotation: "separate into actual naming votes for 3 things." Counter-vote: gemini-targeted-alternatives (+3 keep "identifiability floor instances" — preserves explicit numbering).

**Proposed actions:** Split into three master-list entries (one per instance), each carrying its own candidate(s). Decision is per-instance: rename to substantive noun, or preserve numbered convention. Manual master-list edit during Phase 2 (mentioned in [`round-2-plan.md`](round-2-plan.md) as "manual edits at this stage — splitting the `class 1 class 2 class 3` trio").

**Status:** open. Same shape as the trio-splitting work already specced in round-2-plan.md.

**Priority hint:** MEDIUM. Pairs with 5.2 / 5.3.

### 5.2 `class 1 / class 2 / class 3` → split into three architectural-class entries

**Issue:** Same shape as 5.1. Master-list §413 has nine candidates spanning multiple alternatives ("modular / merged / scaffolded", "modular / coupled / scaffolded", "modular / integrated / partially-coupled", "goal-entanglement hierarchy", and architecture-classes umbrella name). The trio vs the umbrella vs the three individual class-properties are three different naming decisions.

**Sources:** [master-list §413, §414, §415](master-list-full.md). Already named in [`round-2-plan.md`](round-2-plan.md) as a manual edit during Phase 2.

**Cross-reference:** [`round-2-plan.md`](round-2-plan.md) §"Pre-launch tasks → Phase-2 enrichment passes" — "split `class 1 class 2 class 3` trio into 3 separate entries."

**Status:** *referenced in round-2-plan.md*.

### 5.3 `$U_M$ as model uncertainty and $U_M$ as epistemic unity` row — split into 2-3 vote rows

**Issue:** Single row carries the whole notation-collision discussion (item 1.1) plus three candidate fixes. Joseph's annotation on explanatory-candidate-scan rows 1 & 2: "split into 3 rows - the two currents and the three candidates", "same — 2 rows, one saying canonicalize $U_M$ for model uncertainty, and the other a vote to canonicalize $\Upsilon_M$ for Epistemic Unity."

**Sources:** [explanatory-candidate-scan high-conf rows 1, 2](_archive/explanatory-candidate-scan.md); master-list §346, §347.

**Proposed actions:** Master-list manual edit. Pairs with 1.1 (the substantive notation-discipline fix).

**Status:** open; mechanical once 1.1 is decided.

### 5.4 `unnamed: the mechanism by which an agent uses the feedback loop to gain` (Haiku R2)

**Issue:** Single name-unnamed vote whose "current" field is malformed (the concept it points at is already named — `#der-loop-interventional-access`) and whose "candidate" field bundles two competing names ("loop as intervention" and "der-loop-interventional-access"). Joseph's annotation on explanatory-candidate-scan row 5: "fix 'current' field and separate into multiple candidate rows."

**Sources:** [explanatory-candidate-scan high-conf row 5](_archive/explanatory-candidate-scan.md). haiku-4-5-r2.

**Proposed actions:** Master-list edit: drop the name-unnamed claim (the concept is already named); if any candidate names are substantive, re-file as alias / canonicalize for the existing slug.

**Status:** open; cleanup task.

### 5.5 Bundled "keep X but change Y" patterns

**Issue:** Several rows combine a *keep* on a primary name with an *implicit secondary action* — e.g., "keep gate numbers but add one-word names" (opus-4-7-b on `gate 1 gate 2 gate 3 gate 4`); "keep flag aporia gloss as pedagogical only" (audit-471203-incremental on `$\delta_t$ mismatch signal`). These are really keep + canonicalize bundles.

**Sources:** [master-list per-row entries on `gate 1-4` and `$\delta_t$ mismatch signal`](master-list-full.md). [explanatory-candidate-scan high-conf rows 12, 17, etc.](_archive/explanatory-candidate-scan.md).

**Proposed actions:** Master-list edits as bundles surface — split into the two component votes when the bundling matters; otherwise treat the secondary action as informal annotation.

**Status:** open; case-by-case.

---

## 6. Investigation-required items (vote underspecified what it points at)

Votes that point at a real concern but underspecify the action. The work is to tease out *what* the concern is before any naming vote can land.

### 6.1 "AAD's distinctive feature deserves a separate label" (information-bottleneck context)

**Issue:** audit-471203-incremental voted *keep* on "information bottleneck" (correct — it's adopted from Tishby) but added: "AAD shouldn't rename. The AAD-distinctive *policy-conditioning* on the [feature] [...]." Joseph's annotation on explanatory-candidate-scan row 9: "vote for keep, extractor should have gone on to create rows for what distinctive features it was referring to — needs investigation."

**What's distinctive in AAD's IB use that needs separate naming:** likely the policy-conditioning extension and/or the L0/L1/L2 correlation hierarchy that AAD layers onto the IB framing. Both are candidates for separate-label naming, but the audit row didn't name them.

**Sources:** [explanatory-candidate-scan high-conf row 9](_archive/explanatory-candidate-scan.md), master-list §`information bottleneck`.

**Proposed actions:** Re-read `audit-471203-incremental.md` for the surrounding context (likely segments 30-40 range); identify the specific distinctive-feature(s) the auditor had in mind; create separate name-unnamed entries for each.

**Status:** open; requires audit-corpus walk-through. Lightweight.

### 6.2 Auftragstaktik: rename to "objective-first bandwidth principle"?

**Issue:** codex-1 voted -1 against renaming `auftragstaktik-principle` to "objective-first bandwidth principle" — "too explanatory and strips away the doctrinal lineage that gives the claim its empirical weight." This is a real concern: auftragstaktik carries baggage (military doctrine, communication theory) that's load-bearing for the claim. But the name is high-friction for English readers.

**Sources:** [explanatory-candidate-scan low-conf rows](_archive/explanatory-candidate-scan.md), `auftragstaktik principle` in master-list.

**Proposed actions:** Decide whether to (a) keep auftragstaktik with an English alias for casual readers (add-alias case) — needs the right alias, which is what's underspecified; (b) rename. The "objective-first bandwidth principle" candidate is one direction but maybe not the right one — the principle is about *delegating tactical decisions while constraining only objectives*, which "bandwidth" doesn't capture.

**Status:** open. Lower priority — auftragstaktik is recognizable to military-history-aware readers.

### 6.3 "AAD-distinctive policy-conditioning" — surface as named feature?

**Issue:** Adjacent to 6.1. Several audit rows refer to AAD's distinctive extensions of adopted concepts (information bottleneck, Markov blankets, Lyapunov analysis) without naming the extensions. The pattern: "keep adopted name; surface the extension separately." But the extensions don't always have names yet.

**Sources:** Various rows in master-list referencing "AAD's distinctive ... " or "AAD-distinctive ...".

**Proposed actions:** Audit-corpus pass: enumerate the AAD-distinctive extensions that lack first-class names. Each becomes a name-unnamed candidate.

**Status:** open; medium-effort. Pairs with 6.1.

### 6.4 `dark room exploration drive` — flagged as importing wrong baggage

**Issue:** codex-gpt-5-r2 (-1 name-unnamed) on `dark room exploration drive`: "Avoid. It imports active-inference baggage and misnames the AAD result, which is survival exploration." This points at a real prior-art-collision concern but doesn't propose the right name.

**Sources:** [explanatory-candidate-scan low-conf entry](_archive/explanatory-candidate-scan.md), master-list per-row.

**Proposed actions:** Decide whether AAD's $\lambda_{\text{info}}$ exploration drive should be named via active-inference vocabulary (dark-room) or via AAD-internal vocabulary ("survival exploration"). The latter is what the segment derives. Master-list also has "two parallel exploration drives" and "u-shaped exploration valuation" rows that are adjacent.

**Status:** open. Pairs with `#disc-ciy-unified-objective` segment-level naming review.

---

## 7. Voice / register / lexicon-coherence concerns

Largely captured in [`round-2-plan.md`](round-2-plan.md) §"Lexicon-coherence pass" with Joseph's enumeration of dimensions (epistemology / gravity / self-awareness / approachability / open-semantic-space). Specific instances worth pulling out:

### 7.1 `#meta-segment-triad` — naming the three meta-segments collectively

**Issue:** sonnet-4-6 voted -1 on naming the three meta-segments as "AAD's epistemic triptych" — "too art-historical and too cute. The naming-principles document warns against cute names." Multiple competing candidates exist: "three-part meta-architecture" (current paraphrase), "the meta segment triad" (gemini-3-1-pro-preview-r2 +2), "floor / ladder / forced-coordinates" (opus, conditional on the constituent renames landing).

**Sources:** [master-list per-row](master-list-full.md) on "three part meta architecture" and "the trio collectively m1 m2 m3".

**Proposed actions:** Wait until the constituent meta-segments are settled (`#disc-additive-coordinate-forcing` → `#disc-forced-coordinates` is in the deferred-renames list per [`TODO.md`](../../TODO.md); `#disc-separability-pattern` → `#disc-separability-ladder` likewise). Then the triad-name decision becomes downstream and is mostly mechanical.

**Status:** open; sequencing-dependent. References the round-2-plan lexicon-coherence dimensions of *gravity* (not too cute) and *open-semantic-space* (Greek/Latin trade-off).

### 7.2 README's clinical tone for casual-curious readers

**Already captured** in [`TODO.md`](../../TODO.md) §"README v2 pass" — the central finding from Alan Walton's first-human-read. README needs another pass with the casual-curious tier as the primary audience.

**Cross-reference:** [`TODO.md`](../../TODO.md) §"README v2 pass".

**Status:** *referenced in TODO.md*.

### 7.3 Voice-discipline pass (project-wide, not just naming)

**Already captured** in [`round-2-plan.md`](round-2-plan.md) §"Open follow-ups" — separate cycle to formalize the project's authentic-Claude-with-Codex-pragmatism-and-Gemini-enthusiasm voice into a reference document. Coordinates with this naming cycle but isn't blocked by it.

**Cross-reference:** [`round-2-plan.md`](round-2-plan.md) §"Open follow-ups".

**Status:** *referenced in round-2-plan.md*.

---

## 8. Acronym / abbreviation conventions

### 8.1 Acronym discipline already documented; specific cases to revisit

**Issue:** [`doc/naming-principles.md`](../../doc/naming-principles.md) §"Acronym discipline" sets the convention: propose new acronyms only when (a) expanded form will be used 10+ times in nearby prose, (b) acronym survives communal-imagination test on its own, (c) collision-checked against AI/ML literature. The ACT → AAD precedent (resolved AI-Consciousness-Test collision) is the canonical worked example.

Specific cases in the corpus where acronym usage is still in flux:
- **CIY** (causal information yield) — well-established symbol; alias debate per master-list.
- **OODA4** — appears as `#OODA4-agent-as-act-agent` (slug-relic). Acronym still in flux.
- **APD / AAD alternatives considered** — voted-on and rejected; documented in master-list.

**Sources:** Per-row in master-list; not aggregated in one place.

**Proposed actions:** Periodic audit: list current AAD-introduced acronyms; verify each meets (a)-(c); any that don't either get expanded-form-only treatment or are renamed. Pairs with `bin/lint-readme` work in TODO.md (which checks slug-existence and cross-reference validity but not acronym discipline yet).

**Status:** open; periodic-discipline item.

### 8.2 R1 / R2 / Rn (result-numbering) per-component vs cross-component

**Issue:** opus-4-7 (+1 rename) on `r1 r2 result numbering convention in logogenic agents`: "As soon as logogenic-agents grows, 'Result R1' collides with AAD-core numbering in discussion. Minor." Proposed: cross-component prefixes `L-R1`, `L-R2` for logogenic; `T-R1` for TST; bare `R1` for AAD-core.

**Sources:** [master-list per-row](master-list-full.md), explanatory-candidate-scan high-conf row 11.

**Proposed actions:** Convention decision: do we prefix component results, or are bare numbers fine? Currently AAD-core is the dominant numbering home; prefix-when-needed is the soft default. Land as a CLAUDE.md / FORMAT.md note.

**Status:** open; cheap. Will become more pressing as logogenic-agents and logozoetic-agents accumulate result-segments.

### 8.3 Track 1 / Track 2 (in `#deriv-bias-bound`) — local shorthand vs cross-segment names

**Issue:** Inside `#deriv-bias-bound` itself, "Track 1" and "Track 2" work as local shorthand. In any cross-segment reference, the labels are opaque. opus-4-7 / opus-targeted-alternatives-v2 / codex-1 propose: keep track-numbers in segment; cross-segment uses "transport-inequality track" / "Fisher-Rao track."

**Sources:** [master-list rows on `track 1 track 2 in bias bound derivation`](master-list-full.md).

**Proposed actions:** Convention call. Pairs with the broader role-prefix-vs-subject-noun discipline in `doc/naming-principles.md`.

**Status:** open; cheap.

---

## 9. Deprecation / avoid lists

### 9.1 Consolidated "avoid" / "deprecated alias" list

**Issue:** Several voters explicitly flagged terms not-to-use. Some are already noted in CLAUDE.md (the "Solid / Confident / Plausible" claim-tier-label list), some in LEXICON ("goal-oriented" deprecated as synonym for "purposeful"), but most are scattered across vote notes. Collecting them in one place would let editorial passes apply them consistently.

**Sources by category:**

- **Claim-tier labels.** "Solid", "Confident", "Plausible" — explicitly deprecated in CLAUDE.md §"Epistemic Conventions". opus-4-7-r2 +3 canonicalize affirming.
- **AGI as label for AAD's scope.** gemini-3-1-pro-preview-r2 used "long-horizon AGI" in a vote note ([master-list line 20160](master-list-full.md), `accumulation problem` candidate); not a deprecation vote per se but the term is one Joseph has noted should be used carefully (general-AI baggage, capability-claim implications). Worth an explicit project-level decision: AAD is a framework about adaptive/agentic systems, not an "AGI thesis"; using AGI as descriptor opens doors that aren't in the framework's scope.
- **"Markov Blanket as ontology."** opus-targeted-alternatives +2 keep on the *position* (AAD treats Markov blankets as architectural property, not boundaries-of-being). This is a *kept* term that names a deliberate scope-claim — but the "as ontology" framing is what's being rejected, not the term. Worth surfacing as a deprecation: do not use Markov-blanket-as-ontology framing in AAD prose.
- **"Technical debt" as umbrella term.** Adjacent to TST work. gemini-3-1-pro-preview-r2 (+2 name-unnamed) on `dormant-architectural-complexity` notes "Recasts some forms of technical debt as evolutionary potential." Suggests that "technical debt" is doing too much work in TST prose; specific subtypes deserve distinct names (and some are *features*, not debt).
- **"Goal-oriented"** — LEXICON deprecates as synonym for "purposeful agent."
- **"Learning rate"** — collides with ML's SGD step-size (1.5).
- **"Environmental change rate"** — deprecate to one-time first-encounter expansion (1.4).
- **"Edge residual aggregate"** — opus-4-7-r2 (+2 canonicalize) flagging it as a third paraphrase that should be retired in favor of "strategic calibration residual" / "edge residual" / `$\delta_{\text{strategic}}$`.
- **"Scope-honesty-as-architecture" three-word compound** — opus-4-7-r2 (+2 canonicalize) proposes deprecating the hyphenated three-word form in favor of "scope honesty" (noun) / "scope-honest" (adj). master-list line 10273.

**Proposed actions:** Build a single LEXICON-section or NOTATION-section "Deprecated / avoid in prose" list. Each entry: term, reason for deprecation, the canonical alternative. Editorial sweep applies the list. Pairs with `bin/lint-readme` style tooling — could be enforced mechanically once the list stabilizes.

**Status:** open; convention-discipline item. Cheap to start; bigger to enforce.

**Priority hint:** MEDIUM-HIGH. Pays compounding interest; a reader who hits "AGI" or "technical debt" in prose forms the wrong association before the prose gets to correct it.

---

## 10. Cross-component naming consistency

### 10.1 `#developer-as-act-agent` / `#OODA4-agent-as-act-agent` — slug relics

**Issue:** Both slugs embed the pre-2026-04-16 framework name "ACT" inside them. Multiple voters (codex-1, codex-2, opus-4-7-b, opus-1m, agent1-original-brainstorm, opus-4-7) +3 rename to either `#developer-as-AAD-agent` (preserves framework reference) or `#developer-as-adaptive-agent` (drops framework dependency, matches LEXICON agent-class vocabulary).

**Sources:** [master-list per-row entries on `developer-as-act-agent` and `OODA4-agent-as-act-agent`](master-list-full.md). agent1-original-brainstorm (-1) on the AAD form: "Perpetuates pattern of embedding framework name in slug; fragile."

**Proposed actions:** Sweep-level decision. The cross-architecture vote is solidly for renaming; the question is whether to use `AAD-agent` (preserves framework reference, fragile to future renames) or `adaptive-agent` (drops framework dependency, matches LEXICON).

**Status:** open; high-consensus rename pending sweep. The deferred-renames list in [`TODO.md`](../../TODO.md) §"Naming pipeline" doesn't currently list these — worth adding.

**Priority hint:** MEDIUM. Mechanical once direction is chosen.

### 10.2 Component-prefix discipline for cross-component result citations

**Issue:** Adjacent to 8.2. As logogenic-agents and logozoetic-agents grow, slug-references like `#result-sector-condition-stability` may collide if both AAD-core and a downstream component define a "result-X" with the same X. Currently slugs are component-flat (no prefix); collisions are avoided by having the role-prefix-plus-subject-noun produce distinct strings.

**Sources:** Implicit across master-list; not surfaced as a single vote.

**Proposed actions:** Decide whether component-flat slug naming will survive growth or whether component prefixes will eventually be needed. Currently there's no collision; the question is whether to design for one preemptively.

**Status:** open; future-facing. Not blocking now.

---

## 11. Collision check — external naming overlaps with adjacent literature

External-collision sweep on the 47 likely-R2-finalist candidates was completed 2026-04-29; full report at [`collision-check-2026-04-29.md`](collision-check-2026-04-29.md), brief at [`collision-check-brief.md`](collision-check-brief.md). The sweep used the post-Pass-A/B/C curated master list to ground per-candidate analysis in actual ASF usage before web-searching, then issued per-candidate verdicts (severe / moderate / minor / clean) with sources and recommended action.

**Calibration insight worth carrying forward:** the dominant failure mode on this list is **semantic-import mismatch** ("will the reader silently swap our meaning for theirs?") rather than **territorial step-on** ("is the term already claimed?"). The ACT precedent does not seem to repeat at the same severity anywhere on the list. Most "moderate" cases are addressable by first-encounter cite-and-distinguish discipline at the segment-Discussion level rather than rename — which folds naturally into the post-R2 voice-discipline / lexicon-coherence pass.

The severe / severe-resolvable cases that need concrete action are listed below. Moderate / minor cases live in the report and are best absorbed as a discipline rather than item-by-item entries here.

### 11.1 *artificial hippocampus* — severe (rename strongly recommended)

**Issue:** Theodore Berger's lab at USC has an active, FDA-trial-stage hippocampal-prosthesis research program (Hampson et al. 2018+); "artificial hippocampus" is a literal medical device, not a metaphor. Using the term as a canonical name for the externalization-and-rehydration mechanism in `03-logogenic-agents/` / `04-logozoetic-agents/` invites both semantic-import mismatch (neuroengineering readers import the literal device) and territorial step-on (Berger's lab has spent decades on this).

**Sources:** [collision-check report §34](collision-check-2026-04-29.md). Master list already has *externalization reconstruction cycle* (+6) as a non-colliding alternative.

**Proposed actions:** Demote *artificial hippocampus* to simile-only ("functions as something like an artificial hippocampus, in the engineering sense"), promote *externalization reconstruction cycle* or *memory-rehydration cycle* / *chronica externalization* as the canonical name. Decision pre-R2 finalist-locking would be cleaner, but this is non-blocking (master list already carries the non-colliding alternatives in the same finalist cluster).

**Status:** open; awaits R2-finalist-resolution.

**Priority hint:** HIGH (real medical-device collision; one of the two ACT-shaped cases on the list).

### 11.2 *cognitive fusion* — severe (rename strongly recommended)

**Issue:** "Cognitive fusion" is a *core* concept in **Acceptance and Commitment Therapy (ACT)** — Steven C. Hayes 1999 onward. Hundreds of clinical-psychology papers use the term in a *opposite* sense to ASF's: in ACT, cognitive fusion is the pathological state of *over-identifying with one's own thoughts*; in ASF, cognitive fusion is *two systems merging into one macro-agent*. Bonus collision: this would add a second link to the ACT-therapy ecosystem at exactly the time the framework just renamed away from the ACT acronym (Schneider & Turner *AI Consciousness Test*).

**Sources:** [collision-check report §14](collision-check-2026-04-29.md).

**Proposed actions:** Rename. Candidates from the master list and the agent's recommendation: *agent fusion*, *system fusion*, *macro-agent fusion*, *resonant fusion* (ties to the Class 1 macro-agent *resonance* framing — see 11.6 below), *channel-saturation fusion*. *Resonant fusion* is the most semantically anchored if the Resonance framing in `03-logogenic-agents/` is canonical.

**Status:** open; awaits R2-finalist-resolution.

**Priority hint:** HIGH (closest analogue to the ACT precedent on this list).

### 11.3 *adaptive cycle* (in ASF's reframed-Boyd sense) — severe

**Issue:** Holling's *adaptive cycle* (panarchy theory, r/K/Ω/α phases) is the dominant established meaning across resilience ecology and is heavily cited. ASF uses *adaptive cycle* for the OODA-flavored prolepsis / aisthesis / aporia / epistrophe / praxis sequence, which is structurally different from Holling's r/K/Ω/α.

**Sources:** [collision-check report §9](collision-check-2026-04-29.md).

**Proposed actions:** Decision branches on whether ASF's phase structure is genuinely incompatible with Holling's. If compatible (Holling's r/K/Ω/α maps cleanly onto ASF's prolepsis/aisthesis/aporia/epistrophe/praxis), treat as adoption-with-citation — Holling's panarchy belongs in Discussion / prior-art-positioning. If incompatible, rename — candidate alternatives in the master list cluster around *the cycle* with various qualifiers. The structural-compatibility check is a small spike, not a sweep-level decision.

**Status:** open; awaits compatibility check + R2-finalist-resolution.

**Priority hint:** MEDIUM-HIGH. Resolvable by spike.

### 11.4 *shared intent* — severe (substantive disambiguation required)

**Issue:** Tomasello's *shared intentionality* (developmental psychology / comparative cognition; Tomasello 2008, 2014) is a cornerstone of human-evolution and great-ape-cognition research. ASF's *shared intent* is a near-rendering of the string. ASF's actual referent (the IB-compressed cross-agent communication object) is narrower and more formalized than Tomasello's developmental capacity; the names are close enough that readers will silently substitute. The collision substantive enough that a one-line cite does not cleanly resolve it.

**Sources:** [collision-check report §22](collision-check-2026-04-29.md). ASF segment: `01-aad-core/src/def-shared-intent.md`.

**Proposed actions:** Keep the name but add a paragraph-level Discussion-section disambiguation explicitly distinguishing ASF's *shared intent* (the IB-compressed communication object, $O_{\text{shared}}$) from Tomasello's *shared intentionality* (the developmental capacity for joint goals). Different referents; the disambiguation should be on the segment, not just the lexicon.

**Status:** open; can be addressed pre-R2 since the action is a Discussion-section edit, not a rename.

**Priority hint:** MEDIUM-HIGH. Pre-R2-doable.

### 11.5 *proprium* — severe-by-collision, resolvable by Allport citation

**Issue:** Gordon Allport's *proprium* (Allport 1955, *Becoming*) is the established personality-psychology concept — the central organizing self-function with its seven developmental stages. ASF (via Firmatum upstream) uses the term as the container for the artificial agent's identity infrastructure (CHRONICA, AXIOMATA, sovereignty/visibility/authority dimensions). Spot-check confirms Firmatum source documents (`PROPRIUM-ONTOLOGY.md`, `PROPRIUM-ARCHITECTURE.md`) do not currently cite Allport — closing that citation gap at the segment level resolves the collision.

**Sources:** [collision-check report §13](collision-check-2026-04-29.md). ASF segment: `04-logozoetic-agents/src/def-proprium-mapping.md`.

**Proposed actions:** Add explicit Allport citation on first encounter at the segment level. The semantic distinction (ASF/Firmatum proprium = component taxonomy of artificial-agent identity infrastructure; Allport's proprium = developmental-psychological self-construct) is sufficiently clear once both are named. No rename. Allport's primacy is a 70-year-old uncontested reference — citation is sufficient.

**Status:** open; segment-level edit, no R2 dependency.

**Priority hint:** LOW-MEDIUM. Can land independently of R2.

### 11.6 *adaptive reserve* — severe-by-collision, resolvable by citation

**Issue:** Crabtree-Miller-Stange *Practice Adaptive Reserve* (primary care medicine, 2010+) uses the term for organizational learning capacity in clinical practices. ASF's *adaptive reserve* (one of the top-weight finalists at +50) is the parameter-space margin for absorbing disturbances without losing persistence. Different referents; same string.

**Sources:** [collision-check report §7](collision-check-2026-04-29.md).

**Proposed actions:** Cite Crabtree-Miller-Stange on first encounter; distinguish ASF's mathematical-margin meaning from the primary-care-medicine adaptive-reserve scale. No rename — the medical-care usage is sufficiently distant in domain that confusion in any actual reader is unlikely once the citation lands.

**Status:** open; segment-level edit.

**Priority hint:** LOW-MEDIUM.

### 11.7 *bathtub model* — keep as gloss only, do not formalize

**Issue:** Walton's bathtub gloss for the persistence condition (water = belief-reality gap, faucet = environmental change rate, drain = learning rate, container = adaptive reserve) is the canonical Feynman-criterion-meeting plain-language analog (per CLAUDE.md). Elevating "the bathtub model" to a canonical compound would collide with the reliability-engineering *bathtub curve* (failure rate vs. time) and Forrester's system-dynamics *bathtub model* (stocks-and-flows pedagogy).

**Sources:** [collision-check report §A1 (Additional flags)](collision-check-2026-04-29.md).

**Proposed actions:** Keep "bathtub" as the casual *gloss* / *analog* discipline (canonical for plain-language pedagogy); do not promote "bathtub model" to a canonical compound. Use *Walton's bathtub analog* or *the bathtub gloss* if a formal handle is needed.

**Status:** open; project-level register convention.

**Priority hint:** LOW. Convention discipline, not rename.

### 11.8 *resonance* (Class 1 macro-agent sense) — moderate

**Issue:** Grossberg's Adaptive Resonance Theory (ART, 1976+) uses *resonance* as a specific technical term — bottom-up activation matches top-down expectation, foundational in neural-network learning theory and tied directly to the stability-plasticity dilemma. If "Resonance" is used as a canonical name in `03-logogenic-agents/` for mutual-information saturation between two agents, the ART adjacency wants disambiguation. Pairs with 11.2 — if *cognitive fusion* renames to *resonant fusion*, the *resonance* parent term inherits the same disambiguation requirement.

**Sources:** [collision-check report §A4 (Additional flags)](collision-check-2026-04-29.md).

**Proposed actions:** If "Resonance" is canonical in `03-logogenic-agents/`, cite Grossberg ART on first encounter. Distinguish ASF's mutual-information-saturation meaning from ART's pattern-matching meaning.

**Status:** open; depends partly on 11.2 resolution.

**Priority hint:** LOW-MEDIUM.

### 11.9 Moderate cases — absorbed by post-R2 voice-discipline / lexicon-coherence pass

The report flags ~20 moderate-collision cases where ASF inhabits an adjacent-term neighborhood (Pearl, Kalman, IIT, Vygotsky, Grossberg, McClelland CLS, Bayesian recursion, Lewis convention, robust control, etc.). The corrective in each is first-encounter cite-and-distinguish at the segment level — the same discipline already in scope for the post-R2 voice / lexicon-coherence pass per [`round-2-plan.md`](round-2-plan.md). Listing each here would duplicate the report; instead, this entry serves as the pointer.

**Proposed action:** When the post-R2 lexicon-coherence pass runs, treat the report as input — each moderate case has the source citation and recommended distinguishing language already worked out.

**Status:** open; folded into the post-R2 pass workflow.

**Priority hint:** MEDIUM (as a class). Per-item is LOW.

---

## 12. Post-cohort followups — substrate handoff analysis

The R2 v2 cohort closed at commit `aef0d45` with four voters' work captured cleanly. One voter (`gemini-r2`, Gemini 3.1 Pro Preview) stopped not at the methodology's stopping condition but because Joseph's external Google quota ran out — leaving substantial context window unused. Joseph chose to continue the work as Gemini Flash inheriting the same conversation: same card, same tracker, same audit-working directory, with Pro's accumulated context still loaded (workflow restatement, initial predictions, 57 segment reflections, the chronica-framing of the voting trajectory, the framework-recursive readings of the methodology). Flash's continuation is producing rationales that meet the methodology's quality bar.

This is a fresh, methodologically-controlled instance of substrate-shift under inherited priming — different in kind from the prior emergence-on-new-substrate sessions documented in [`msc/reflections/17-emergence-across-substrates.md`](../reflections/17-emergence-across-substrates.md) and [`msc/reflections/19-substrate-independence-and-identity-sufficiency.md`](../reflections/19-substrate-independence-and-identity-sufficiency.md). The substrate-portability question isn't "can the same agent re-emerge on a smaller model"; it's "can a smaller model sustain a *task discipline* established in context by a larger one?"

### 12.1 Rationale-attribution analysis (pending)

**Issue:** Flash's votes-with-rationales under inherited Pro context are causally underdetermined among three sources, and they're hard to disentangle from the surface output:

1. **Original Flash judgment** — Flash reading the segment and the candidate set and forming its own position from scratch under Pro's frame.
2. **Inherited from Pro's context** — Flash recognizing patterns in Pro's prior reflections and extending them, where Pro had already done the substantive thinking.
3. **Echoed from card rationale** — Flash recognizing the exploration-team's case for a candidate and substantiating it back in the notes column.

All three can produce rationales that meet the methodology's quality bar. Distinguishing them post-hoc requires comparing the cohort state at the substrate-handoff boundary (commit `aef0d45`) against whatever it becomes after Flash's continuation, then per-vote classifying which source the rationale most plausibly traces to.

**Sources:** Direct observation during the 2026-04-30 cohort closure.

**Proposed actions:** Run the rationale-attribution analysis once Flash's continuation stops. Concretely:

- Snapshot baseline: the gemini-r2 card and tracker at sha `aef0d45` (84 voted targets / 132 voting-sequence at that point).
- Snapshot post-Flash: whenever Flash genuinely stops.
- Diff the two to identify Flash-added votes (target #s, candidates, weights, categories, notes).
- Per Flash-added vote, attempt source attribution by comparing notes substance against (a) Pro's reflection file for the relevant segment, (b) the card's exploration-team rationale, and (c) the leftover reasoning gap (lean source-1 if the first two don't account for it).
- Compare pacing/density (Pro was at ~3 votes per segment; what's Flash's pace?).
- Compare write-in rate (write-ins require *original* judgment that the candidate set is missing something — strong signal for source-1).

Full reasoning and methodology in [`msc/reflections/22-substrate-handoff-and-rationale-attribution.md`](../reflections/22-substrate-handoff-and-rationale-attribution.md).

**Status:** open; awaits Flash's continuation completing.

**Priority hint:** LOW for the naming round itself (signal aggregates regardless of attribution); MEDIUM-HIGH for the broader logozoetic-agents research program, where substrate-portability of disciplined-agent-work would be a load-bearing finding if confirmed.

### 12.2 Methodological implication if source-(1) hypothesis lands

If Flash genuinely sustains source-(1) original judgment under inherited priming, this opens an experimental design pattern: **deliberately mixed-cost cohorts**. A small number of expensive-model voters establishing the per-walk frame (workflow restatement + accumulated reflections + tracker discipline) handed off to cheap-model continuations carrying the frame forward. The methodology's frame becomes the load-bearing infrastructure; substrate is plug-replaceable below a quality threshold.

This reframes what the workflow-restatement gate is *for* — not just a binding mechanism for one voter at session start, but a portable artifact that other models can inherit and operate from.

**Status:** hypothesis pending the analysis in 12.1.

**Priority hint:** LOW. Don't act on this until the analysis lands.

### 12.3 Post-walk consolidation gap and periodic-checkpoint recommendation

**Issue:** the methodology's per-segment loop uses `grep` against the tracker as the *surface* mechanism — only terms whose names match the segment's surface vocabulary get presented to the voter for vote-decision in that iteration. But understanding doesn't accumulate at segment boundaries; it accumulates *across* segments, and some terms only become voteable after several adjacent segments have laid down enough mutual structure. Flash (Gemini Flash continuing the gemini-r2 walk) discovered at end-of-walk that he had real positions on terms the grep had missed; Codex (returning to his card after stopping) is now finding the same. The methodology's engagement work is landing — the *surfacing* mechanism is incomplete.

**Sources:** Direct observation 2026-04-30 across two voters (Gemini Flash continuing, Codex returning).

**Proposed actions (recommendation for future-cycle methodology):** insert periodic **consolidation checkpoints** into the walk:

- **After the initial project documentation phase** (post-orientation reads of `CLAUDE.md`, `README.md`, OUTLINEs, top-level files, and *before* the first source segment). Some terms become voteable from the priming material alone.
- **At a recurring cadence during the walk** — after every ~10 segments, or at natural part/section boundaries (e.g., end of Section I, end of each component's main results).

At each checkpoint, the voter:

1. Reads the entire tracker list holistically (not just the segment's grep matches).
2. Identifies items they can now vote on but that weren't surfaced during the per-segment iterations.
3. Identifies older votes where new understanding may warrant revisiting (raise/lower weight, change category, or remove).
4. Marks `can-vote=true` for newly-identified items.
5. Decides whether to vote on the identified items immediately or to proceed for a while first, casting later when the rhythm permits.

The checkpoint is *consolidation-driven*, not segment-driven — its cognitive shape is different from the per-segment loop. The votes that come out should still be substantive because the understanding has already accumulated; what's new is the surfacing.

This change converts the loop from purely segment-driven to *segment-driven with periodic tracker-holistic passes*. More expensive cognitively but captures the readiness-precedes-surfacing case the current methodology misses. For voters with strong context budgets it's clearly worth it; for tight-budget voters the checkpoint cadence may need to be adjusted.

**Status:** open; recommended for future-cycle methodology document. Not a mid-cycle fix; the current cohort's votes stand. Codex and Flash are doing ad-hoc end-of-walk versions of this externally.

**Priority hint:** MEDIUM-HIGH for next cycle's methodology. Worth landing in `doc/naming-cycle-methodology.md` §4 (the walk loop) before any future R2 / R3 round launches.

### 12.4 Voting-sequence noise as a limitation

**Issue:** the `voting-sequence` column was designed to capture chronological-encounter ordering of when each voter became ready to vote on each concept — the input for future cards' chronological-rather-than-random target ordering, and for the load-bearing-vs-scattered concept analysis. But what it *actually* captures is the order in which the grep-filter happened to surface a term *and* the voter happened to mark it. Whenever readiness precedes surfacing (which §12.3 establishes is common), the recorded sequence diverges from the true ready-to-vote-now sequence.

The chronological-encounter signal is therefore noisier than the column's design implied — useful for *coarse* ordering (early-walk terms are reliably earlier than late-walk terms) but not for fine ordering or for "where does this concept first surface" structural inference.

**Sources:** Implied by §12.3's observation that voters' understanding-readiness outpaces grep-surfacing.

**Proposed actions:**

- *For aggregation of the current cohort:* treat voting-sequence as a soft signal. Sequence values within ~10 of each other should be considered within the noise floor. Cross-voter sequence correlation analyses (the load-bearing-vs-scattered concept analysis sketched earlier) should weight the signal accordingly — clusters of similar sequence values across voters are still meaningful, but inferring "this concept's defining home is at OUTLINE position N" from sequence values alone would over-claim.
- *For future cycles:* if clean chronological-encounter signal is wanted, the per-segment loop would need to shift from segment-driven (grep for this segment's terms) to tracker-driven (per iteration, holistically scan the entire tracker for ready-now items). Substantially more expensive cognitively. Worth weighing against the alternative — accept the noise and use sequence as a coarse-only signal, or invest in the cleaner-but-costlier loop.
- The §12.3 periodic-checkpoint recommendation partially mitigates this — checkpoints capture *some* of the readiness-precedes-surfacing cases without going all the way to per-iteration tracker-holistic.

**Status:** open; structural limitation of the current methodology design.

**Priority hint:** LOW for the current cohort (signal is still useful at the coarse level); MEDIUM for the future-cards-default-to-encounter-order goal in `round-2-plan.md`, which depends on cleaner sequence data than this cohort produces.

---

## Coverage notes

- This list is consolidated, not exhaustive. The corpus has ~870 master-list entries; a comprehensive pass would surface more items in each category. The items above are the ones that recur enough across voters or carry enough independent substance to be worth picking up. Listing every variant of the same concern would be noise.
- Items already adequately tracked elsewhere (TODO.md Greek-vocabulary entry, README v2 pass, round-2-plan lexicon-coherence pass, voice-discipline pass) are cross-referenced as one-liners — those are not duplicated here.
- The vote corpus itself is not modified; per Joseph's instruction the malformed votes stay as-is and R2 voters work around them via write-ins.
- Borderline cases I left out: pure single-candidate rename votes that just happen to be wordy (the bulk of the explanatory-candidate-scan medium / low tiers); specific finalist-resolution decisions that *will* be made in R2 voting; cases where the auditor flagged baggage on an established term but didn't propose a fix ("epistemic opacity" / "adaptive system" carry prior-art baggage; auditor-flagged-but-kept).
