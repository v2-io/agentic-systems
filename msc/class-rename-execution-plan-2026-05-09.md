# Class 1/2/3 → Separated/Coupled/Partial — Execution Plan

**Created:** 2026-05-09 (Joseph + Claude Opus 4.7, 1M context, planning session). Distilled from the §B item-1 seed plan in `TERMINOLOGY-TODO.md`, the rationale block in `msc/naming/naming-rename-plan.md`, the conversation that sized the surface area and added the warning-callout discipline + git-tag step, and the discovery that the terminology-tooling shift (CLAUDE.md §LEXICON discipline) changes how the LEXICON entry lands.

**Purpose.** Stand alone as the executable plan for a (likely fresh-context) session that picks up the rename. Self-contained — should not require reading the conversation that produced it. Authoritative for sequencing and discipline; defers to `msc/naming/naming-rename-plan.md` for the original 2026-05-04 decision rationale and to `terminology/README.md` for tooling specifics.

**Status when executing session opens.** The five [Open questions](#open-questions-needing-josephs-call) below need Joseph's call before surgery starts. They genuinely change the execution shape. Each carries my recommendation but the choice is his.

---

## 1. The Transformation

### What changes

| Old (pre-2026-05-09)                            | New                                  | Property                                                    |
| ----------------------------------------------- | ------------------------------------ | ----------------------------------------------------------- |
| Class 1 — Modular                               | **Class 1 — Separated** *(unchanged number; renamed only)* | Directed separation by construction; estimator and planner separate |
| Class 2 — Fully merged *(was: worst case)*       | **Class 3 — Coupled** *(swapped + renamed)*  | Directed separation fails by construction (LLMs)            |
| Class 3 — Partially modular *(was: middle case)* | **Class 2 — Partial** *(swapped + renamed)*  | Coupling present but bounded; $\kappa_\text{processing} \in (0, \kappa_\text{max})$ |

Two operations bundled because every touched file gets both: **rename** (descriptive labels replacing numerals at the property level) and **swap** (numbering aligns Architecture with the six other AAD ladders that all run cleanest → middle → worst as 1 → 2 → 3). Doing them separately would touch every file twice.

### Axis name

The collective axis is **Goal-Update Coupling Class** (GUC Class). Measured by $\kappa_\text{processing}$ in engineered systems; pattern-attributable in biological systems. Established in `#der-directed-separation` Architectural classification.

### The semantic-reversal trap

**"Class 2" pre-rename means fully merged; post-rename it means partial.** A naive find-replace silently corrupts meaning. Every `Class 2` and `Class 3` occurrence has to be classified before being rewritten:

- *Did the author mean fully-merged?* → becomes **Class 3 = Coupled**.
- *Did the author mean partially modular?* → becomes **Class 2 = Partial**.

Read each occurrence in context before substituting. This is the single biggest risk in the operation.

---

## 2. Rationale (Compact)

**Why the rename.** The numbered classes named *positions in a taxonomy*, not *the property the taxonomy measures*. Cross-architecture R2 voters split across competing English-modifier slates (Modular/Merged/Scaffolded vs. Modular/Integrated/Partially-coupled vs. Modular/Coupled/Partially-modular); the contested-decision cluster surfaced in `r2-patterns.md` §3c. Resolution: name the *property* (the directed-separation property of `#der-directed-separation`) not an architectural realization. `Separated` directly echoes the segment-derived property; a tightly-integrated architecture that happens to be goal-blind is also Separated.

**Why the swap.** The Architecture ladder is currently the visual outlier in `#disc-separability-pattern`'s six-ladder meta-pattern table. Six ladders (Correlation L0/L1/L2; Convention C1/C2/C3; Contraction Tier 1/2/3; Identification Regime A/B/C; Scope Adaptive/Agency/Composite; A2'-scope α₁/α₂/β) all run cleanest → middle → worst as 1 → 2 → 3. Architecture currently runs 1 → 3 → 2 — partially-modular middle case sits at numeric position 3 instead of 2. The swap aligns Architecture's numbering with the meta-pattern.

**Why now.** The class-coercion segments that landed earlier today (2026-05-09) — `#der-class-coercion-via-wrapping`, `#disc-adversarial-coupling-pressure` — use the old vocabulary throughout. Doing the rename next prevents accumulating retrofit debt. Every cycle of new content under old vocabulary makes the eventual rename heavier.

**Full rationale source.** `msc/naming/naming-rename-plan.md` lines 92–116 carry the original 2026-05-04 decision record with the meta-pattern alignment audit and the per-property naming-rationale that defeated the competing slates.

---

## 3. Surface Area

The full canonical surface as of 2026-05-09 — **reverify with a fresh grep at execution time**, files may have been added or removed:

```bash
grep -l -E "Class[ -]?[123]\b|class[- ]?[123]\b|fully.merged|partially.modular" \
  --include="*.md" -r 01-aad-core/ 02-tst-core/ 03-logogenic-agents/ 04-eli/ \
  doc/ CLAUDE.md README.md README-auditor.md LEXICON.md NOTATION.md \
  HISTORICAL-CONTEXT.md FINDINGS.md PROPOSALS.md TODO.md PRACTICA.md \
  TERMINOLOGY-TODO.md CHANGELOG.md LOG.md
```

### Direct-edit files (canonical source)

**01-aad-core segments (17):**
- `der-directed-separation.md` ⭐ canonical home (32+ occurrences; the architectural classification table, the κ operationalization, the Pearl-blanket discussion, the composite-level inheritance)
- `der-class-coercion-via-wrapping.md` ⭐ heavy-touch (15+ occurrences; landed today; uses old vocab throughout)
- `result-section-ii-survival.md` ⭐ heavy-touch (the "Class 2" survival classification table)
- `disc-separability-pattern.md` ⭐ meta-pattern Architecture row (label-edit; column order stays cleanest → middle → worst — see [Open Question 3](#3-meta-pattern-table))
- `deriv-observation-ambiguity-bias-bound.md` (segment titled "Class-2 ambiguity bias bound" → "Class-3 ambiguity bias bound" given the swap; check for slug-related references)
- `def-value-object.md`, `der-agent-opacity.md`, `der-interaction-channel-classification.md`, `der-tempo-composition.md`, `deriv-strategic-composition.md`, `deriv-update-detection-latency.md`, `disc-adversarial-coupling-pressure.md` (landed today), `disc-exploit-explore-deliberate.md`, `disc-identifiability-floor.md`, `disc-independence-audit.md`, `example-strategy.md`, `hyp-directed-separation-under-composition.md`, `scope-composite-agent.md`

**02-tst-core segments (1):** `scope-developer-agent.md`

**03-logogenic-agents segments (8):** `def-coupled-update-dynamics.md`, `der-logogenic-as-wrapping.md`, `result-coupled-diagnostic-framework.md`, `result-section-ii-survival.md` (note: this file is in 03 not 01 — verify), `scope-channel-collapse.md`, `scope-logogenic-agent.md`, `scope-observation-ambiguity-modulation.md`, `scope-scaffolded-logogenic.md` — *these are typically the segments where logogenic = Class 2 fully-coupled becomes Class 3 Coupled (semantic reversal applies)*

**04-eli segments (4):** `def-auxilia-hierarchy.md`, `def-imperium-arbitrium-split.md`, `scope-eli.md`, `scope-moral-continuity.md`

**OUTLINE files (2):** `01-aad-core/OUTLINE.md`, `03-logogenic-agents/OUTLINE.md`

**README partials (4) — edit these, not README.md directly:** `doc/readme/src/_findings-summary.md`, `_known-issues.md`, `_maturity-gradient.md`, `_position-and-lineage.md`

**Root docs (~7):**
- `CLAUDE.md` — Architectural Decision #5 + Known Fragilities + any other Class-N references
- `NOTATION.md` — symbol-reference rows mentioning Class N
- `PROPOSALS.md` — any architectural-proposal cross-references to Class N
- `HISTORICAL-CONTEXT.md` — any historical narrative mentioning Class N
- `CHANGELOG.md` — header note + new cycle entry
- `LOG.md` — header warning callout (frozen archaeology)
- `doc/naming-principles.md` — if Class N is used as an example

**Plan files (collapse-and-defer):**
- `TERMINOLOGY-TODO.md` §B item 1 — collapse row to defer to this plan doc
- `PRACTICA.md` Cycle priority order #1 — keep strategic mention, add pointer
- `TODO.md` Naming pipeline §"Prose-vocabulary renames pending" — collapse row to defer

### Auto-regenerated (do not edit directly; will pick up changes from sources)

- `LEXICON.md` — generated from `terminology/entries/<slug>.md` via `bin/term render` (see CLAUDE.md §LEXICON discipline)
- `README.md`, `README-auditor.md` — generated from `doc/readme/src/` partials via `bin/build-readme`
- `FINDINGS.md` — generated from segment-level `## Findings` sections via `bin/extract-findings`

### Frozen archaeology (do not edit; gets warning callouts only)

`_obs/`, `msc/` (except this plan and the rename-plan), `audits/`, `spikes/`, `ref/`, the entire `msc/AUDIT-WORKING-*/` cycle workspaces, naming-vote files, etc. Their Class-N references stay frozen at old meaning. The warning callouts (see [§7](#7-warning-callout-discipline)) are the rosetta stone for future readers.

---

## 4. Open Questions Needing Joseph's Call

These genuinely change the execution shape. Resolve before surgery starts.

### 1. Single commit vs. batched

**Question.** TERMINOLOGY-TODO says "warrants its own commit." Treat as one big commit (whole surface in one shot), or batched by region (e.g., `01-aad-core` canonical → `03-logogenic-agents` → `04-eli` + `02-tst-core` → root docs + README rebuild) with a CHANGELOG entry tying them together at the end?

**Trade-off.** Single commit: cleaner narrative; one revert button; no intermediate states where some files use old vocab and some use new. Batched: smaller blast radius per commit; bisectable if a regression appears; intermediate states are temporarily inconsistent but each batch lands consistently within itself.

**My recommendation.** **Batched, ordered as 01-aad-core canonical (heaviest, surfaces issues first) → 03-logogenic-agents → 02-tst-core + 04-eli → root docs + README/LEXICON regenerate → CHANGELOG entry + git tag.** Each batch a coherent commit; single CHANGELOG entry written at the end summarizing the arc.

### 2. Surface scope

**Question.** TERMINOLOGY-TODO §B explicitly lists ~8 segments + README + CLAUDE.md. The fresh grep surfaces ~30 segments + 2 OUTLINEs + 4 partials + ~7 root docs (see §3 above). Treat all canonical-surface occurrences as in-scope, or stick to the explicit list and let the rest float?

**Trade-off.** Letting the rest float means future readers encounter mixed vocabulary across the corpus until a follow-on cleanup cycle. Treating all in-scope means the rename closes cleanly but the touch-radius is ~3× larger.

**My recommendation.** **All canonical-surface occurrences in scope.** The corpus carries its own consistency cost; mixed vocabulary across segments is a chronic friction-source for future readers and audits. The semantic-reversal nature of this swap *especially* benefits from a single closing pass.

### 3. Meta-pattern table

**Question.** `#disc-separability-pattern`'s Architecture row currently has columns `Class 1 | Class 3 | Class 2` (cleanest→middle→worst). Post-swap the column *order* stays cleanest→middle→worst but the *labels* inside become `Class 1 | Class 2 | Class 3`. Confirm: this is just label-edits, no column reorder?

**My recommendation.** **Confirm. Label-edits only, no reorder.** The column semantics (separable core / structured repair / general open) don't change; the swap aligns the numerals with the column order, which is the whole point of the swap.

### 4. LEXICON / terminology-entry timing

**Question.** Land the `terminology/entries/goal-update-coupling-class.md` (axis entry) + per-value entries first (so segments can reference them during sweep), or sweep prose first and add the entries in the same commit?

**Trade-off.** Entries first: cross-references resolve during the sweep; `bin/term lint` won't complain. Prose first: lets the sweep's discoveries shape the entry's gloss (some prose contexts may surface clarifications worth capturing in the entry).

**My recommendation.** **Entries first, in the first commit of the batch sequence.** They're small (3–4 entries), don't risk the semantic-reversal trap, and being able to cross-reference them from segment prose during the sweep is operationally useful. If the sweep surfaces clarifications, refine the entry in the final commit before the CHANGELOG entry.

### 5. Migration-note discipline

**Question.** Add a one-line Working Notes migration note in *every* segment whose Class-N reference changes semantic meaning, or only in segments where the change is most likely to confuse (the heaviest-cited ones)?

**TERMINOLOGY-TODO says** *"Migration note in Working Notes for any segment whose Class N reference changes semantic meaning (Class 2 ↔ Class 3) — one-line note documenting the 2026-05-04 swap so future readers can decode archival references. Removed at `candidate` stage per FORMAT.md Gate 4."* — i.e., the discipline already commits to the broader form.

**My recommendation.** **Apply to every segment whose Class-N reference changes semantic meaning** (i.e., every segment that mentions Class 2 = fully-merged or Class 3 = partially-modular under the old vocabulary; not every segment that just mentions Class 1, which is unchanged). The note is one line, removed at candidate stage, and it's the per-segment local rosetta-stone alongside the global warning callouts. Segments that only mention Class 1 don't need a note since Class 1 is unchanged in number.

---

## 5. Execution Sequence (Once Questions Settle)

Assuming the recommendations above are accepted; modify per Joseph's calls.

### Phase 0: Pre-flight

1. **Reverify surface area.** Re-run the grep from §3 against the current tree.
2. **Reverify naming-rename-plan.md is intact.** Lines 92–116 are the original rationale source.
3. **Read `terminology/README.md`** if not already familiar with `bin/term` — entry creation, decision events, render workflow.
4. **Read CLAUDE.md §LEXICON discipline** — terminology system is now the canonical source for prose vocabulary; LEXICON.md is auto-generated.

### Phase 1: Terminology entries (first commit)

1. Create `terminology/entries/goal-update-coupling-class.md` (axis entry):
   - frontmatter: `slug: goal-update-coupling-class`, `term: Goal-Update Coupling Class`, `brief: ...`, `tags: [structural_concepts, agent_classes]`, `source_type: asf`, `primary_source: 01-aad-core/src/der-directed-separation.md`, `see_also: [directed-separation, class-coercion]`
   - body: short prose definition (one-line gloss minimum, paragraph plus three-value summary preferred), explicit meta-pattern alignment note (`Class 1 = separable core, Class 2 = structured repair, Class 3 = general open` per `#disc-separability-pattern`), pointer to `#der-directed-separation`.
2. Create per-value entries `separated.md` / `coupled.md` / `partial.md` if landing the per-value-entry shape (recommended unless Joseph wants axis-only).
3. Record decisions:
   ```bash
   bin/term decide goal-update-coupling-class canonicalize --by joseph \
     --note "Class 1/2/3 → Separated/Coupled/Partial rename + Class 2↔3 swap, 2026-05-09. Aligns Architecture ladder with the six other AAD ladders per #disc-separability-pattern meta-pattern audit. Source rationale: msc/naming/naming-rename-plan.md lines 92–116."
   bin/term decide separated rename --by joseph --from class-1 --to separated \
     --note "Class 1 number unchanged; rename only. See goal-update-coupling-class entry for the full rename + swap context."
   bin/term decide partial rename --by joseph --from class-3 --to class-2-partial \
     --note "Class 3 → Class 2 (number swap) + → Partial (rename). Semantic-reversal: 'Class 2' pre-2026-05-09 meant fully merged."
   bin/term decide coupled rename --by joseph --from class-2 --to class-3-coupled \
     --note "Class 2 → Class 3 (number swap) + → Coupled (rename). Semantic-reversal: 'Class 3' pre-2026-05-09 meant partially modular."
   ```
4. `bin/term lint` — should be clean.
5. `bin/term render --output LEXICON.md --force` (the `--force` only because LEXICON.md is currently still hand-authored — until terminology bootstrap migration completes, the renderer's clobber-guard trips; see `terminology/README.md` §"Generating LEXICON.md").
6. Commit: `Add: Goal-Update Coupling Class terminology entries (Separated / Partial / Coupled)`.

### Phase 2: 01-aad-core segments (heaviest batch; ~17 files)

Per-file workflow:
1. Read the segment top-to-bottom.
2. Classify every `Class N` occurrence: which of {1=Separated, 2=fully-merged, 3=partially-modular} did the author mean?
3. Apply the rename + swap:
   - `Class 1` / `modular` → `Class 1 (Separated)` on first segment use, `Separated` thereafter; pedagogical "Old (New)" form retained where useful.
   - `Class 2 (fully merged)` / `fully merged` → `Class 3 (Coupled)` on first use, `Coupled` thereafter.
   - `Class 3 (partially modular)` / `partially modular` → `Class 2 (Partial)` on first use, `Partial` thereafter.
4. For `der-directed-separation.md`:
   - Update the architectural-classification table (rows reorder by number).
   - Update the κ-operationalization paragraph and "Distribution dependence" paragraph (κ values keyed to classes).
   - Update the "Class-1 by structure vs. Class-1 by behavior" subsection (Class 1 unchanged; check Class-2/3 references in W₂ and the composite-level inheritance subsection — the Class 2 fully-coupled inheritance becomes Class 3 Coupled inheritance).
   - Update the "Implications for theory scope" bullets — same swap.
   - Findings section: brief + impact + novelty-claim + related-work table all reference Class N.
5. For `der-class-coercion-via-wrapping.md`:
   - Heavy-touch. Most "Class 2" / "Class 3" references in this segment refer to "fully merged or partially modular components" being wrapped — read each carefully.
   - W₀ / W₂ / W₁ regime hierarchy and the structural-vs-behavioral distinction is independent of the rename; check.
6. For `disc-separability-pattern.md`:
   - Architecture row in the "Current instances" table: `Class 1 | Class 3 | Class 2` → `Class 1 | Class 2 | Class 3`. Column order unchanged.
7. **Add migration note** to Working Notes for every segment whose Class-N reference changed semantic meaning:
   ```markdown
   - **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
   ```
8. Run `bin/lint-outline` (or whatever the project's segment lint expects).
9. Commit per heavy-touch segment or per cluster — sub-batch the 17 files into 3–5 commits if the diff per file is large.

### Phase 3: 03-logogenic-agents segments (~8 files)

Same per-file workflow. Note: many segments here describe logogenic agents as "Class 2 fully-coupled" — these are the heaviest semantic-reversal cases (becoming Class 3 Coupled). `result-section-ii-survival.md` if present here is a heavy-touch segment.

### Phase 4: 02-tst-core + 04-eli segments (~5 files)

Same workflow. These are typically light-touch — single-mention references to logogenic / merged agents.

### Phase 5: OUTLINE files (~2 files)

`01-aad-core/OUTLINE.md` and `03-logogenic-agents/OUTLINE.md` — outline-table rows referencing Class N.

### Phase 6: Root docs + README partials

1. `CLAUDE.md` — Architectural Decision #5, Known Fragilities, any other Class-N references.
2. `NOTATION.md` — symbol-reference rows.
3. `PROPOSALS.md`, `HISTORICAL-CONTEXT.md`, `doc/naming-principles.md`.
4. `doc/readme/src/_findings-summary.md`, `_known-issues.md`, `_maturity-gradient.md`, `_position-and-lineage.md`.
5. **Add warning callouts** to LOG.md header, CHANGELOG.md header (per [§7](#7-warning-callout-discipline)).
6. Run `bin/build-readme` (or `bin/refresh-all` for the auto-extracted partials too).
7. Commit: `Update: root docs + README partials for GUC rename`.

### Phase 7: Plan-file collapse

1. `TERMINOLOGY-TODO.md` §B item 1 — collapse to a one-line "landed; see CHANGELOG entry" pointer (or remove the row entirely if landed completely).
2. `PRACTICA.md` Cycle priority order #1 — mark complete, point to CHANGELOG entry.
3. `TODO.md` Naming pipeline — same treatment.
4. Commit: `Tracking: collapse plan-file entries for landed GUC rename`.

### Phase 8: CHANGELOG + git tag

1. **CHANGELOG entry** — substantive narrative for the cycle: rationale (rename + swap), what landed, the warning-callout discipline, the migration-note convention, the terminology-system landing, the meta-pattern alignment achieved. Cross-reference to this plan doc.
2. **Tag the parent of the rename's first commit** (the last "old vocabulary" commit):
   ```bash
   git tag pre-guc-rename-2026-05-09 <SHA-of-parent>
   ```
   This gives the warning callouts a stable anchor (`Anything older than tag pre-guc-rename-2026-05-09 has the old terminology...`).
3. Push tag if the project's tag-push convention is in use.

### Phase 9: Verification

1. `grep -E "Class[ -]?[123]\b|fully.merged|partially.modular"` across the canonical surface — expected: zero residual matches outside frozen archaeology and the warning callouts themselves.
2. `bin/lint-outline` clean across all components.
3. `bin/term lint` clean.
4. `bin/build-readme`, `bin/refresh-all` — verify rebuilt READMEs and FINDINGS.md.
5. Spot-check `der-directed-separation.md` reads cleanly top-to-bottom.

---

## 6. The Warning Callout

**Format** (Joseph's spec, 2026-05-09):

```markdown
> [!warning]
> Anything older than tag `pre-guc-rename-2026-05-09` (or commit `<SHA>`), which landed on 9 May 2026, uses the old terminology for Goal-Update Coupling classes. The mapping:
>
> | historical | actual current     | sometimes AKA  |
> | ---------- | ------------------ | -------------- |
> | Class 1    | GUC Class 1: Separated | Modular        |
> | Class 2    | GUC Class 3: Coupled   | Undirected     |
> | Class 3    | GUC Class 2: Partial   | Operational    |
```

The "sometimes AKA" column carries informal labels (Modular / Undirected / Operational) that may surface in less-formal artifacts (reflections, casual notes); they're not canonical but are likely to appear in archaeology.

### Where the callout lands

- **README.md** — as a partial in `doc/readme/src/` (probably `_position-and-lineage.md` or a dedicated `_terminology-warning.md`); near where Class N first surfaces in the public-facing narrative.
- **README-auditor.md** — same partial; auditor variant gets the same callout.
- **CLAUDE.md** — at or near Architectural Decision #5 (where the Class N taxonomy is named).
- **`der-directed-separation.md`** — at the top of the Architectural classification subsection, since this is the canonical home and any archaeological cross-reference will land here.
- **`result-section-ii-survival.md`** — heavy archaeological cross-reference target.
- **LOG.md** — header (frozen pre-2026-04-24 archaeology with many Class-N references).
- **CHANGELOG.md** — header (post-2026-04-24 archaeology has fewer Class-N references but the callout is the canonical pointer for cycle-by-cycle archaeology).

### Where it does NOT land

- Frozen archaeology directories themselves (`_obs/`, `msc/AUDIT-WORKING-*/`, `audits/`, `spikes/`, `ref/`, naming-vote files). These directories are off-limits for direct edits per the project's archaeology-preservation discipline. The callouts at the README / CLAUDE / canonical-segment level are sufficient — anyone reading frozen archaeology will have already passed through one of those anchors.

---

## 7. Risks / Vigilance Points

1. **Semantic-reversal corruption.** The single biggest risk. Every `Class 2` and `Class 3` reference must be classified before substitution. Naive find-replace will silently invert meaning. *Mitigation:* per-segment manual read; classify each occurrence; apply the swap consciously; add migration note to Working Notes for transparency.

2. **Heavy segments where the rename intersects with active content.** `der-class-coercion-via-wrapping.md` (landed today) uses the old vocabulary in its W₀/W₂/W₁ regime hierarchy and class-A/B/C admissibility partition — the regime letters and admissibility classes are *independent of* the GUC rename, but visual proximity in the segment may cause confusion during the sweep. Read carefully.

3. **The `#disc-separability-pattern` Architecture row.** The whole point of the swap is to align this row's numerals with the column order. Verify the table reads correctly post-edit: `Class 1 | Class 2 | Class 3` left-to-right, monotonically aligned with the cleanest → middle → worst columns.

4. **Migration notes accumulating.** Every Working-Notes migration note is removed at `candidate` stage per FORMAT.md Gate 4. After the rename lands, segments that promote to candidate in subsequent cycles will shed their migration notes. This is the intended discipline — the notes exist to bridge the rename, not to persist forever.

5. **Auto-regenerated files.** `LEXICON.md`, `README.md`, `README-auditor.md`, `FINDINGS.md` regenerate from upstream sources. Don't edit them directly. Run `bin/term render` (LEXICON), `bin/build-readme` (READMEs), `bin/extract-findings` (FINDINGS) — or `bin/refresh-all` for the README pipeline. Verify the regenerated files actually picked up the rename.

6. **The terminology-tooling shift's `--force` flag.** `bin/term render --output LEXICON.md` currently refuses to clobber the hand-authored LEXICON.md per `terminology/README.md`'s clobber-guard. Until the LEXICON-bootstrap migration completes (separate work, queued), the rename's LEXICON regeneration may need `--force`. Confirm the workflow with `terminology/README.md` §"Generating LEXICON.md" before running.

7. **Frozen archaeology temptation.** Files in `_obs/`, `msc/AUDIT-WORKING-*/`, `audits/`, `spikes/`, `ref/` will appear in grep results with old Class-N references. **Do not edit them.** These are frozen by project discipline. The warning callouts are what makes them readable — not retroactive surgery.

---

## 8. References

- **`TERMINOLOGY-TODO.md` §B item 1** — the seed plan; this doc supersedes the inline detail there.
- **`msc/naming/naming-rename-plan.md` lines 92–116** — original 2026-05-04 decision rationale and meta-pattern alignment audit. Authoritative for *why*.
- **`PRACTICA.md` Cycle priority order #1** — strategic-portfolio entry naming this as the active priority.
- **`terminology/README.md`** — schema + tooling for `bin/term`; especially §"Schema", §"Recording a decision", §"Generating LEXICON.md".
- **`CLAUDE.md` §LEXICON discipline** — terminology system as the canonical source for prose vocabulary.
- **`#der-directed-separation`** (`01-aad-core/src/der-directed-separation.md`) — canonical home for the architectural classification.
- **`#disc-separability-pattern`** (`01-aad-core/src/disc-separability-pattern.md`) — meta-pattern table whose Architecture row drives the swap.
- **`FORMAT.md` Gate 4** — migration-note discipline (notes removed at candidate stage).
- **`bin/build-readme`, `bin/refresh-all`, `bin/term`, `bin/lint-outline`, `bin/extract-findings`** — the tooling that regenerates downstream artifacts.

---

*This plan is the authoritative execution document for the Class 1/2/3 → Separated/Coupled/Partial rename + Class 2 ↔ 3 swap. Update in place during execution if discoveries warrant; preserve the decision trail. After the rename lands, this document remains as the historical record — referenced from the CHANGELOG entry and from any future audit trying to understand how the GUC rename was executed.*
