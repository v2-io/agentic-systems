# TERMINOLOGY-TODO

Live execution queue for naming-cycle decisions that have been **made** (interactively curated through Phase 5, 2026-05-04) but not yet **executed**. The decisions and their rationale live in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md); this file is the action checklist.

**Lifecycle.** When an item executes and lands in a commit, it is *removed* from this file and a corresponding entry in [`CHANGELOG.md`](CHANGELOG.md) records what landed. Small batches are fine — especially for the LEXICON additions, where 5–10 entries per commit reads cleanly. The file shrinks as work happens; when empty (or down to deferred residue), the naming cycle's execution phase is complete.

**Pre-flight per item.** For each rename, read the rationale in `naming-rename-plan.md` first (linked per row) — the operational notes there often catch edge cases (segment H1 forms, dual references, pedagogically-useful "Old (New)" first-use) that the brief executable summary here doesn't surface.

**Ordering.** Slug renames first (mechanical, tool-driven), then prose-vocabulary renames (LEXICON entry + segment sweep), then LEXICON additions (no rename, just commitment of vocabulary). Within each section: roughly easiest-first, but interleavable. The Class 1/2/3 → Separated/Coupled/Partial item is the largest single piece (touches ~8 segments + README + CLAUDE.md) and warrants its own commit.

---

## A. Slug renames (via `bin/rename-slug`)

Each row: `bin/rename-slug OLD NEW` plus segment H1 update + `*[Type (slug)]*` formal-tag review + cross-reference scan (the script reports stale-text warnings; H1 / opening-sentence / formal tags are touched by hand). The `msc/naming/` directory is excluded from the script's substitution patterns, so this file and `naming-rename-plan.md` are not corrupted by the sweep.

- [ ] **`deriv-strategic-dynamics` → `deriv-edge-credence-dynamics`** *(F1 citability fix; qualifier-add)*
  "Strategic dynamics" collides with game-theory generic term. The segment derives the dynamics of *edge credences* $p_{ij}$ within the strategy DAG. Pairs with `#def-strategy-dag` and `#hyp-edge-update-via-gain`.

[F1 batch rationale block: `naming-rename-plan.md` §"Pending subject-noun renames — additions (2026-05-04, batch F1 citability fixes)"](msc/naming/naming-rename-plan.md#pending-subject-noun-renames--additions-2026-05-04-batch-f1-citability-fixes).

---

## B. Prose-vocabulary renames (LEXICON entry + segment-prose sweep)

These do *not* use `bin/rename-slug` — the legacy form is prose vocabulary, not a slug. Each row: add/update LEXICON entry + sweep affected segments.

- [ ] **Class 1/2/3 → Separated/Coupled/Partial; "Goal-Update Coupling Class" axis name; coordinated Class 2 ↔ 3 numbering swap** *(largest item; multi-segment; warrants its own commit)*
  - LEXICON entry "Goal-Update Coupling Class" with three values + meta-pattern alignment note (Class 1 = separable core, Class 2 = structured repair, Class 3 = general open) + pointer to `#der-directed-separation`.
  - Numbering swap: Class 1 = Separated *(unchanged)*; **Class 2 (was 3) = Partial**; **Class 3 (was 2) = Coupled**. Brings Architecture into ordering-alignment with the other six ladders in `#disc-separability-pattern`.
  - Prose-cleanup pass — segments touched once for *both* the rename AND the swap:
    - `01-aad-core/src/der-directed-separation.md` (canonical home; reorder + rename)
    - `01-aad-core/src/deriv-observation-ambiguity-bias-bound.md` (currently "Class-2 ambiguity bias bound" → "Class-3 ambiguity bias bound") — *coordinate with slug rename in §A*
    - `01-aad-core/src/scope-observation-ambiguity-modulation.md`
    - `01-aad-core/src/result-section-ii-survival.md` (Class 1/2/3 survival classification table — reorder)
    - `03-logogenic-agents/` segments (logogenic = Class 2 fully-coupled → Class 3 — multiple segments)
    - `01-aad-core/src/disc-separability-pattern.md` (Architecture row in meta-pattern table — update Class numbering)
    - `README.md` (*Position & Lineage* and *Maturity Gradient* paragraphs) — note: README is auto-generated; edit `doc/readme/src/_*.md` partials and rebuild via `bin/build-readme`
    - `CLAUDE.md` (Section II preamble Class N references)
  - Numbered backup retained where pedagogically useful: "**Separated** (Class 1)" on first use, then "Separated" thereafter.
  - **Migration note in Working Notes** for any segment whose Class N reference *changes semantic meaning* (Class 2 ↔ Class 3) — one-line note documenting the 2026-05-04 swap so future readers can decode archival references. Removed at `candidate` stage per FORMAT.md Gate 4.
  - [Full rationale + meta-pattern table](msc/naming/naming-rename-plan.md#vocabulary-commitments--non-slug-lexicon--prose-pass-2026-05-04).

- [ ] **"Knowledge Type" axis (Static / Learning)**
  - LEXICON entry for "Knowledge Type" axis with two values, gloss of each, pointer to where it activates in the agent ontology.
  - Prose-discipline note: avoid "online/offline" and "fixed/adaptive" as informal synonyms — they drift the framing.
  - Activation tier deferred pending the broader four-axis ontology review at `msc/domain-unification-2026-05-04/`; the axis-name commitment lands independently.
  - [Rationale](msc/naming/naming-rename-plan.md#vocabulary-commitments--non-slug-lexicon--prose-pass-2026-05-04).

- [ ] **`grafting` → `strategic grafting`** *(citability; structural-change vocabulary)*
  - LEXICON entry under structural-change vocabulary (paired with `pruning` and `reweighting` from `#form-structural-change-as-parametric-limit`).
  - Prose pass through segments referencing the operation; segment `#form-structural-change-as-parametric-limit` updated to use "strategic grafting" canonically (with first-encounter cite of bare "grafting" if useful for prior-art readers).

- [ ] **`logozoetic agent` → `Emergent Logozoetic Intelligence (ELI)`** *(class-label rename; precedent already at directory level)*
  - LEXICON Agent Classes table — Tier 6 row update.
  - Prose pass through ~6 segments using "logozoetic agent" as class-name.
  - First-use form "Emergent Logozoetic Intelligence (ELI)", "ELI" thereafter.
  - Directory-level precedent already landed (commit `fa63616`, 2026-05-01: `04-logozoetic-agents/` → `04-eli/`).

- [ ] **`alignment uncertainty` → `teleological-unity uncertainty`** *(F1; AI-safety-overload fix)*
  - Prose pass through `#hyp-communication-gain` (definition site for $U_{\text{align},ji}$), `#def-unity-dimensions` (cross-reference), any `old-tf-appendix-f-multi-agent` discussions still cited.
  - Connects to the project's unity vocabulary ($U_M$ / $U_O$ / $U_\Sigma$); the term is specifically uncertainty about $U_O$.
  - **Followup flag** (not part of this rename): broader question of reframing the four uncertainty terms in the communication-gain formula through the unity vocabulary — queued separately in `mini-lexicon-todo.md`.

- [ ] **`plan confidence` → `strategy-plan confidence`** *(F1; symbol $\hat{P}_\Sigma$ pair)*
  - LEXICON "Terms to Be Added" entry promoted to canonical with new name; symbol $\hat{P}_\Sigma$ stays; pair binds in NOTATION.md as well.

- [ ] **`effective disturbance` → `regime-typed effective disturbance`** *(F1; control-theory generic-fix)*
  - Prose pass through `#der-interaction-channel-classification` (recipient-side four-regime decomposition).
  - The "regime-typed" qualifier is the AAD-distinctive content: $\rho_B^{\text{eff}}$ decomposes by regime (Informative / magnitude-shock / structural-shock / ambient-noise) with three independent boundaries.

- [ ] **`routing structure` → `multi-agent routing structure`** *(F1; networking-generic fix)*
  - Prose pass through `#scope-multi-agent` (defines $R_t = (\mathcal{N}_t, \{c_t^{(j \to i)}\})$).
  - The goal-blind-routing distinction lives within this concept and is load-bearing for `#hyp-directed-separation-under-composition`.

[F1 prose-batch rationale](msc/naming/naming-rename-plan.md#prose-vocabulary-renames--additions-2026-05-04-batch-f1-citability-fixes).

---

## C. LEXICON additions — confirmed canonicalize commitments

Per-batch LEXICON entries (no rename, no prose sweep — just the entry). Add each term with: one-line gloss, symbol if applicable, segment cross-reference. Group LEXICON additions into existing thematic tables where they fit (Cycle Phases / Agent Classes / Core Quantities / Structural Concepts / etc.); add new tables only where genuinely new.

Each batch below is a natural commit unit. Mark a row landed = remove it; add a CHANGELOG entry for the batch.

### C1. Clean canonicalize — batch 1 (29 entries)

[Rationale (master batch 1)](msc/naming/naming-rename-plan.md#clean-canonicalize--no-substantive-flag-29-entries).

- [ ] control regret · chronica · satisfaction gap · strategy DAG · adaptive reserve · adversarial destabilization · strategic tempo · team persistence · temporal optimality · credit assignment boundary · atomic changeset · event driven dynamics · persistence cost · coupled update dynamics · moral continuity · adaptive gain dynamics · adaptive system · agency · composite agent · variational sector condition · continuous operation · interiority default · developer agent · discrete sector condition · experiential training · multi timescale stability · proprium mapping · strategy persistence · coherence coupling

### C2. Greek-cycle phase consolidations (5 entries)

[Rationale](msc/naming/naming-rename-plan.md#greek-cycle-phase-consolidations-5-entries).

- [ ] aporia (ἀπορία) (productive perplexity) · epistrophe (ἐπιστροφή) (turning-toward) · aisthesis (αἴσθησις) (perception) · praxis (πρᾶξις) (informed action) · prolepsis (πρόληψις) (anticipation)

  Form: `latinized (greek) (english-translation)`. Capitalization decision deferred; LEXICON entries should reflect that deferral (note in entry, not capitalization-policy choice). The Cycle Phases table in LEXICON already has these in usable shape; this commitment is the affirmation that the form is canonical and the capitalization-decision is the only open question.

### C3. Canonicalize with nuance flagged — batch 1 (5 entries)

[Rationale](msc/naming/naming-rename-plan.md#canonicalize-with-nuance-flagged-5-entries).

- [ ] **adaptive tempo** — competing alt "tempo" (canon w=3); LEXICON entry should mention the bare-form alt was considered.
- [ ] **logogenic agent** — competing alt "Section III logogenic agent" (canon w=3); LEXICON entry should mention the qualifier-form was considered.
- [ ] **change investment** — citability borderline (criterion 9; review the LEXICON gloss to make sure the AAD-specific scope is visible).
- [ ] **implementation time** — citability borderline (criterion 9; same shape as above).
- [ ] **exponential cognitive load** — weak signal (2 votes / 2 archs); LEXICON entry should briefly note the weak base.

### C4. FORMAT.md / process-vocabulary canonicalize (no LEXICON action)

[Rationale](msc/naming/naming-rename-plan.md#format-md--process-vocabulary-canonicalize-2026-05-04). 

These five terms (`epistemic status`, `working note`, `discussion`, `formal expression`, `type formulation`) are already canonical via FORMAT.md itself. The commitment is *no-drift*, not LEXICON-add. **No commit action; this row exists so the curation trail is complete.** Mark and remove when reading; or leave as a permanent reminder. Joseph's call.

- [ ] *Acknowledged: epistemic status / working note / discussion / formal expression / type formulation are FORMAT.md-defined; no LEXICON entry.*

### C5. Compound and paired-vocabulary canonicalize (8 entries)

[Rationale](msc/naming/naming-rename-plan.md#compound-and-paired-vocabulary-canonicalize-2026-05-04). Each row commits a binding (slug ↔ prose, symbol ↔ prose, term + alias) — LEXICON entry preserves the pair structure.

- [ ] **recursive update** — bare prose handle canonical; verbose `recursive update derivation` is the segment-title form for `#deriv-recursive-update`. LEXICON entry on the bare form.
- [ ] **worked example bandit** ↔ `#example-bandit` — paired-vocabulary; both slug short-form AND prose form (segment-title) are canonical. LEXICON entry preserves the pair shape.
- [ ] **worked example kalman** ↔ `#example-kalman` — same shape.
- [ ] **worked example l1** ↔ `#example-L1` — same shape.
- [ ] **worked example strategy** ↔ `#example-strategy` — same shape.
- [ ] **logostratum** with allowed prose aliases "LLM Substrate" / "LLM model" — project-specific term (PROPRIUM lineage); aliases provide less-foreign English handle for casual prose. Canonicalize-with-add-alias hybrid.
- [ ] **$\mathcal{T}$** ↔ "adaptive tempo" — symbol-to-prose binding (NOTATION.md row already exists; LEXICON cross-ref). Add-alias-style canonicalize.
- [ ] **stability-plasticity feasibility window** — full phrase is citation form (CLS-prior-art-anchored: McClelland-McNaughton-O'Reilly 1995; French 1999); `feasibility window` is sanctioned in-segment short form once the full term has been introduced. LEXICON entry preserves both forms.

### C6. Clean canonicalize — batch 2 (12 entries)

[Rationale](msc/naming/naming-rename-plan.md#clean-canonicalize--additions-from-second-pass-curation-2026-05-04-batch-2).

- [ ] temporal software theory · auftragstaktik · epistemic shadow · extreme transition motif · logogenic · logozoetic · macro step ratio · matrix exploration bonus · operational persistence · structural persistence · trust meta model · deliberation threshold

### C7. Canonicalize with nuance flagged — batch 2 (3 entries)

[Rationale](msc/naming/naming-rename-plan.md#canonicalize-with-nuance-flagged--additions-2026-05-04-batch-2).

- [ ] **canonical formulation** — rename×1 on keep was confirmed-miscat; LEXICON entry stands.
- [ ] **teleological unity** — symbol-tagged variant `Teleological unity $U_O$` proposed; resolution: keep "teleological unity" as bare prose form; $U_O$ is its own NOTATION row. LEXICON entry should make the symbol-prose pair visible.
- [ ] **system availability** — citability fails (criterion 9) — accepted under route (d) "adopted-standard term"; cite engineering reliability literature on first encounter in segment `#def-system-availability`. LEXICON entry should note the adopted-standard discipline.

### C8. Clean canonicalize — batch 3 (10 entries)

[Rationale](msc/naming/naming-rename-plan.md#clean-canonicalize--additions-2026-05-04-batch-3).

- [ ] contraction over drift principle · conceptual alignment · edge credence · purposeful substate · stability plasticity window · task terminal stance · default signal function · loop · strategy description length · transition opacity

  Note: `loop` is already in LEXICON's Cycle Phases table (loop = structural topology vs cycle = one traversal); this commitment is affirmation, not a new entry — verify the existing entry matches and remove this row.

### C9. Canonicalize with nuance flagged — batch 3 (1 entry)

[Rationale](msc/naming/naming-rename-plan.md#canonicalize-with-nuance-flagged--additions-2026-05-04-batch-3).

- [ ] **epistemic opacity** — auditor-flagged philosophy-of-mind baggage (`epistemic opacity` carries phenomenology / qualia connotations from philosophy-of-mind that AAD does not adopt). Canonicalize stands; LEXICON entry should briefly note the baggage and clarify AAD's narrower meaning (informational rather than phenomenological).

### C10. Clean canonicalize — batch 4 (2 entries)

[Rationale](msc/naming/naming-rename-plan.md#clean-canonicalize--additions-2026-05-04-batch-4).

- [ ] communication gain (`#hyp-communication-gain`)
- [ ] update gain (`#emp-update-gain`)

### C11. Compound and paired-vocabulary — batch 4 (1 entry)

[Rationale](msc/naming/naming-rename-plan.md#compound-and-paired-vocabulary-canonicalize--additions-2026-05-04-batch-4).

- [ ] **$H_b$** ↔ "agent opacity" (segment `#der-agent-opacity`)
  - NOTATION primary on the symbol with prose handle: "$H_b$ — Agent opacity ..."
  - LEXICON reverse-primary on the prose with symbol cross-ref: "Agent opacity ($H_b$) — ..."
  - Segment `#der-agent-opacity` flagged for audit: define with the label "agent opacity" explicitly and use the prose form consistently.
  - Same shape as $\mathcal{T}$ ↔ adaptive tempo.

### C12. Adopted-standard canonicalize — batch F2 (5 entries)

[Rationale](msc/naming/naming-rename-plan.md#adopted-standard-canonicalize--accept-term-cite-prior-art-on-first-encounter-2026-05-04-batch-f2).

These pass Criterion 9 via route (d): accept the term and discipline first-encounter cite of the prior-art reference. AAD-distinctive content lives in *what AAD does within the term*, not in re-coining the scope.

Each item: LEXICON entry + first-encounter cite added to the source segment (in Discussion or opening prose, per FORMAT.md §Findings — Related Work).

- [ ] **action selection** (`#der-action-selection`) — cite Sutton & Barto 2018 (*Reinforcement Learning: An Introduction*, 2nd ed., MIT Press); Russell & Norvig (*AIMA*).
- [ ] **causal structure** (`#post-causal-structure`) — cite Pearl 2009 (*Causality: Models, Reasoning, and Inference*, 2nd ed., CUP); Spirtes, Glymour & Scheines 2000 (*Causation, Prediction, and Search*, MIT Press).
- [ ] **multi agent** (`#scope-multi-agent`) — cite Shoham & Leyton-Brown 2008 (*Multiagent Systems*, CUP); Stone & Veloso 2000 (*Auton. Robots* 8(3): 345-383).
- [ ] **equilibrium convergence** — cite Monderer & Shapley 1996 (*Games and Economic Behavior* 14(1): 124-143, potential games); Rosen 1965 (*Econometrica* 33(3): 520-534, concave $n$-person games); Nash 1950 (*PNAS* 36(1): 48-49). Used in `#deriv-strategic-composition`.
- [ ] **feature** (`#def-feature`) — software-engineering canonical (any SE foundations text); TST narrowing in `#def-feature` ("unit of coherent change") provides domain-specific tightening.

### C13. Clean canonicalize — batch G (1 entry, late-confirmed reconciliation)

[Rationale](msc/naming/naming-rename-plan.md#clean-canonicalize--additions-2026-05-04-batch-g--late-confirmed-reconciliation).

- [ ] **cycle vs loop** — canonicalize the *pair-distinction* itself as load-bearing AAD vocabulary. The pair, not either word alone, is the citation handle. LEXICON's existing Cycle Phases table already carries the loop/cycle gloss — verify present in the right shape and remove this row.

---

## D. Open-question residue (the 13 to-canonicalize rows still pending decision)

Listed here as a pointer, not as actions — these are pre-execution decisions that come *before* the queue above grows further. See [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md) §Table for the 13 rows: most carry `D` in the Confirm column (specification bound, adaptive cycle, operationalization, etc.), and one carries `???` (separable core / structured repair / general open — separability triad-rung naming, ties into [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md)). When those decisions land, new rows will be added to the appropriate section above.

---

## How this file relates to other naming-cycle files

- [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md) — **Decisions and rationale.** The decision record: what was decided, when, why, with full operational-landing notes. This file (TERMINOLOGY-TODO.md) extracts the *executable summary*; rename-plan retains the *full reasoning*. Each row above links back.
- [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md) — **Pre-decision residue.** The remaining 13 rows still pending Joseph's routing call.
- [`msc/naming/master-list-curated.json`](msc/naming/master-list-curated.json) — **Master vote-aggregation source.** `rename_status` field tracks per-current canonicalize / rename / excluded status (88+ marked).
- [`PRACTICA.md`](PRACTICA.md) §"🌟 Current naming conventions refactor" — **Strategic pipeline.** Items 9 (final decisions on 13) → 10 (execute renaming surgery) → 11 (land canonicalize commitments) name the phase this file operationalizes.
- [`CHANGELOG.md`](CHANGELOG.md) — **Where landed batches go.** When items here are committed, the corresponding CHANGELOG entry captures the batch shape and substance.
