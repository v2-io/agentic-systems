# TERMINOLOGY-TODO

Live execution queue for naming-cycle decisions that have been **made** (interactively curated through Phase 5, 2026-05-04) but not yet **executed**. The decisions and their rationale live in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md); this file is the action checklist.

**Scope note (2026-05-09).** This file's queue is the high-confidence subset — items that already have decisions and only need execution. The broader naming program is a multi-cycle arc: the R2 cohort produced **629 distinct currents**; only **58 are marked** with a `rename_status` decision (44 from the 2026-05-04 manual curation pass + 14 from the 2026-05-09 GUC rename execution). **~511 currents remain unrouted** — they have not yet been evaluated for canonicalize / rename / add-alias / exclude. Many are quick dispositions; a substantial number are genuine rename candidates. Tracked at [`PRACTICA.md`](PRACTICA.md) §"Current naming conventions refactor" item 13. This file (TERMINOLOGY-TODO) only carries items that have already been routed.

**Lifecycle.** When an item executes and lands in a commit, it is *removed* from this file and a corresponding entry in [`CHANGELOG.md`](CHANGELOG.md) records what landed. Small batches are fine — especially for the LEXICON additions, where 5–10 entries per commit reads cleanly. The file shrinks as work happens; when empty (or down to deferred residue), the naming cycle's execution phase is complete.

**Pre-flight per item.** For each rename, read the rationale in `naming-rename-plan.md` first (linked per row) — the operational notes there often catch edge cases (segment H1 forms, dual references, pedagogically-useful "Old (New)" first-use) that the brief executable summary here doesn't surface.

**Ordering.** Slug renames first (mechanical, tool-driven), then prose-vocabulary renames (terminology entry + segment sweep), then terminology additions (no rename, just commitment of vocabulary). Within each section: roughly easiest-first, but interleavable. The Class 1/2/3 → Separated/Coupled/Partial item is the largest single piece (touches ~8 segments + README + CLAUDE.md) and warrants its own commit.

**Tooling note (2026-05-09).** "LEXICON entry" rows below mean *entries in the `terminology/` system*, not hand-edits to `LEXICON.md` (which is now auto-generated — see CLAUDE.md §LEXICON discipline). For each row:
1. Edit (or scaffold via `bin/term add <slug>`) `terminology/entries/<slug>.md` — YAML frontmatter (term, brief, status, source, see_also, etc.) + markdown body for the longer prose definition.
2. Record the naming decision via `bin/term decide <slug> <action> --by <decider> --note "<rationale pointer>"` (actions: `canonicalize` / `rename` / `add-alias` / `add-cite` / `update-gloss` / `nuance-flag`).
3. `bin/term render --output LEXICON.md` (or whatever target the workflow specifies) to regenerate.
4. `bin/term lint` to surface schema or cross-ref issues.
The LEXICON.md output is the same artifact rows below describe; what changed is *how it's produced*. See `terminology/README.md` for full schema.

---

## A. Slug renames (via `bin/rename-slug`)

Each row: `bin/rename-slug OLD NEW` plus segment H1 update + `*[Type (slug)]*` formal-tag review + cross-reference scan (the script reports stale-text warnings; H1 / opening-sentence / formal tags are touched by hand). The `msc/naming/` directory is excluded from the script's substitution patterns, so this file and `naming-rename-plan.md` are not corrupted by the sweep.

[F1 batch rationale block: `naming-rename-plan.md` §"Pending subject-noun renames — additions (2026-05-04, batch F1 citability fixes)"](msc/naming/naming-rename-plan.md#pending-subject-noun-renames--additions-2026-05-04-batch-f1-citability-fixes).

*All §A items landed.*

---

## B. Prose-vocabulary renames (LEXICON entry + segment-prose sweep)

These do *not* use `bin/rename-slug` — the legacy form is prose vocabulary, not a slug. Each row: add/update LEXICON entry + sweep affected segments.

*All §B items landed.* The Class 1/2/3 → Separated/Coupled/Partial bundle (with the coordinated Class 2 ↔ 3 swap and the "Goal-Update Coupling Class" axis name) executed on the `guc-rename-2026-05-09` topical branch. See CHANGELOG entry for the cycle narrative; execution plan archived at [`msc/class-rename-execution-plan-2026-05-09.md`](msc/class-rename-execution-plan-2026-05-09.md); live tracking at [`msc/class-rename-tracking-2026-05-09.md`](msc/class-rename-tracking-2026-05-09.md).

[F1 prose-batch rationale](msc/naming/naming-rename-plan.md#prose-vocabulary-renames--additions-2026-05-04-batch-f1-citability-fixes).

---

## C. Terminology additions — confirmed canonicalize commitments

Per-batch terminology entries (no rename, no prose sweep — just the entry). Each row: scaffold `terminology/entries/<slug>.md` (`bin/term add <slug>` if starting from blank), populate the frontmatter (term, brief, status, source, tags, see_also) + body (one-line gloss minimum, longer prose where worthwhile, segment cross-reference), then `bin/term decide <slug> canonicalize --by <decider>` to record the commitment. After a batch lands, `bin/term render --output LEXICON.md` regenerates the LEXICON view. Tagging via `tags:` drives the LEXICON's thematic sectioning (Cycle Phases / Agent Classes / Core Quantities / Structural Concepts / etc.); reuse existing tags where they fit.

Each batch below is a natural commit unit. Mark a row landed = remove it; add a CHANGELOG entry for the batch.



### C4. FORMAT.md process-vocabulary — LEXICON entries + no-drift links

[Original rationale](msc/naming/naming-rename-plan.md#format-md--process-vocabulary-canonicalize-2026-05-04) (original framing was "no LEXICON action"; now reversed — entries will be added).

**Scope change (2026-05-10).** These terms are being added to the LEXICON notwithstanding their definition in FORMAT.md. FORMAT.md remains authoritative for the *process* content; the LEXICON entries carry the concise definition and cross-link back to FORMAT.md. Any change to a term's meaning must be applied to both files — **no-drift discipline** applies. Execution for each term:
1. Scaffold `terminology/entries/<slug>.md` + populate (brief drawn from FORMAT.md; body cross-references FORMAT.md as authoritative).
2. `bin/term decide <slug> canonicalize --by joseph`.
3. In FORMAT.md: add a link from the first canonical mention of each term to `terminology/entries/<slug>.md` (inline link or footnote-style).
4. Add a comment near the top of FORMAT.md noting that key terms are cross-linked to `terminology/` and that changes must not drift.

**C4a — Original 5 (was the whole of old C4):**
- [ ] **epistemic status** — the `## Epistemic Status` section in a segment; describes what is derived vs hypothesized, and the max attainable status. Slug: `epistemic-status-section` (to distinguish from the frontmatter field).
- [ ] **formal expression** — the `## Formal Expression` section; contains the segment's mathematical content with equation-level tags. Slug: `formal-expression-section`.
- [ ] **discussion** (section) — the `## Discussion` section; interpretation, connections, brief conceptual framing. Slug: `discussion-section` (to distinguish from `type: discussion`).
- [ ] **working notes** — the `## Working Notes` section; active development questions removed at candidate stage. Slug: `working-notes-section`.
- [ ] **findings** (section) — the optional `## Findings` section; curated catalog entries for externally-notable contributions. Slug: `findings-section`.

**C4b — Segment type vocabulary** (`type:` frontmatter values, 18 entries). Each entry: brief definition from FORMAT.md's type table; tag `segment_types`; source FORMAT.md. These appear in every segment's frontmatter — worth lexiconizing so the vocabulary is navigable without opening FORMAT.md.
- [ ] postulate · definition · scope · formulation · derived · result · corollary · hypothesis · normative · empirical · observation · discussion · measurement · proposed-schema · derivation · worked-example · sketch · aside

**C4c — Epistemic status vocabulary** (`status:` frontmatter values, 8 entries). Tag `epistemic_vocabulary`. Source FORMAT.md.
- [ ] axiomatic · exact · robust-qualitative · heuristic · conditional · empirical (status) · discussion-grade · sketch (status)

  Note: `empirical` and `sketch` appear as both type and status; entries should cover both senses or cross-reference. Slug disambiguation: `type-empirical` / `status-empirical` or single entry with both senses noted.

**C4d — Stage vocabulary** (`stage:` frontmatter values, 7 entries). Tag `process_vocabulary`. The stage ladder is encountered in OUTLINE.md tables and segment frontmatter constantly.
- [ ] missing · draft · deps-verified · claims-verified · format-clean · candidate

  Note: `old` (stage) is implied by the `old-*` filename prefix; may not need a separate entry since it's already documented under the filename convention.

**C4e — Promotion gate vocabulary** (4 entries). Tag `process_vocabulary`. Named gates are referenced in audit and review conversations frequently.
- [ ] **dependency audit** (Gate 1) · **content review** (Gate 2) · **mechanical review** (Gate 3) · **working notes disposition** (Gate 4)

**C4f — Findings schema fields** (9 entries). Tag `findings_vocabulary`. These appear in the `## Findings` sections of mature segments and in audit discussions.
- [ ] **brief** (Feynman-criterion field) · **impact** (findings field) · **novelty claim** · **related work** (findings field) · **search log**
- [ ] Claim postures (open set; 5 established): **synthesis** · **differentiation** · **novelty** · **transfer** · **recognition**
- [ ] Search log depth tiers (6): **not-conducted** · **cursory** · **targeted** · **nominally-comprehensive** · **comprehensive** · **intuition-only**

**C4g — Three rings (epistemic triage analysis)** (3 entries). Tag `epistemic_vocabulary`. Referenced in audit discussions and CLAUDE.md conventions.
- [ ] **inevitability core** · **canonical formulations** (ring) · **empirical/heuristic/discussion ring**

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

## E. Future terminology-system enhancements (`bin/term` evolution)

Tooling improvements surfaced during rename-cycle execution. Land independently from the naming-cycle queue above — they affect how the renderer behaves, not which terms canonicalize.

- **`sequence-id:` field for within-group ordering override** (surfaced 2026-05-09 during GUC rename Phase 1). Currently `bin/term render` sorts entries alphabetically by `term:` within each `tags:`-driven section. This makes axis-keyed entries render out of taxonomy order — e.g., the GUC three-value axis renders alphabetically (Coupled / Partial / Separated) in the Agent Classes section rather than monotonically (Class 1: Separated → Class 2: Partial → Class 3: Coupled). A `sequence-id:` field (integer or compound — e.g., `goal-update-coupling.1` / `.2` / `.3`) would let entries opt into a within-group ordering override; entries without `sequence-id:` continue to sort alphabetically by `term:`. Same field would serve future axis-keyed taxonomies (Knowledge Type axis, Contraction Tier 1/2/3, Identification Regime A/B/C, etc.). Implementation sketch: extend the renderer's per-section sort to read `sequence-id:` first, fall back to alphabetic by `term:`. Cross-section entries (multi-tagged) would carry one `sequence-id:` per relevant axis or use a single value where the ordering applies in all sections.

## D. Open-question residue (the 13 to-canonicalize rows still pending decision)

Listed here as a pointer, not as actions — these are pre-execution decisions that come *before* the queue above grows further. See [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md) §Table for the 13 rows: most carry `D` in the Confirm column (specification bound, adaptive cycle, operationalization, etc.), and one carries `???` (separable core / structured repair / general open — separability triad-rung naming, ties into [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md)). When those decisions land, new rows will be added to the appropriate section above.

---

## How this file relates to other naming-cycle files

- [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md) — **Decisions and rationale.** The decision record: what was decided, when, why, with full operational-landing notes. This file (TERMINOLOGY-TODO.md) extracts the *executable summary*; rename-plan retains the *full reasoning*. Each row above links back.
- [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md) — **Pre-decision residue.** The remaining 13 rows still pending Joseph's routing call.
- [`msc/naming/master-list-curated.json`](msc/naming/master-list-curated.json) — **Master vote-aggregation source.** `rename_status` field tracks per-current canonicalize / rename / excluded status (88+ marked).
- [`PRACTICA.md`](PRACTICA.md) §"🌟 Current naming conventions refactor" — **Strategic pipeline.** Items 9 (final decisions on 13) → 10 (execute renaming surgery) → 11 (land canonicalize commitments) name the phase this file operationalizes.
- [`CHANGELOG.md`](CHANGELOG.md) — **Where landed batches go.** When items here are committed, the corresponding CHANGELOG entry captures the batch shape and substance.
