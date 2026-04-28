# Link and File Hygiene Findings

Date: 2026-04-28

Scope: active root docs, generated README sources, component outlines, current `doc/`,
`msc/`, `ref/`, `spikes/`, and current segment files. I treated `_obs/`, old
segment files, and explicit rename/provenance records as historical unless they
are still presented as current instructions.

Non-goal: this pass only records findings and recommendations. It does not
rewrite the referenced files.

## Executive Summary

The refactor is mostly coherent around the big moves (`msc/naming/...`,
`ref/agentic-tft/...`, `spikes/...`, and generated README sources). The remaining
high-value cleanup is concentrated in four areas:

1. Active docs still describe `TODO.md` as having an Archive even though
   `TODO.md` now says the archive has been collapsed.
2. `CHANGELOG.md` contains a cluster of clickable links to missing
   `project_*.md` and `session_*.md` artifacts.
3. A few current instructions still point readers to pre-move `msc/` paths or
   the old root `CLAUDE-2.md`.
4. Some segment-local links still use pre role-prefix filenames such as
   `agent-identity.md`, `directed-separation.md`, and
   `adversarial-exponent-regimes.md`.

Several apparent issues should be left alone: old paths in `LOG.md`, `_obs/`,
rename records, and source-material spikes are generally historical provenance,
not current navigation.

## Checks Run

- Compared the worktree rename map with `git status --short`,
  `git diff --name-status --find-renames`, and
  `git diff --cached --name-status --find-renames`.
- Read the active roots and generated sources: `README.md`,
  `README-auditor.md`, `TODO.md`, `PROPOSALS.md`, `CHANGELOG.md`, `CLAUDE.md`,
  `FORMAT.md`, `PRACTICA.md`, `LEXICON.md`, `OUTLINE.md`,
  `MIGRATION-MAP.md`, `doc/readme/src/*.md`, `doc/de-novo-audit-instructions.md`,
  and `doc/naming-principles.md`.
- Scanned current `msc/`, `ref/`, `spikes/`, component outlines, and segment
  files for moved-path references and markdown links.
- Ran `bin/build-readme --check`: passed; generated README files match their
  sources.
- Ran `bin/lint-outline`: failed on one ordering violation and one orphan
  segment; details below.
- Ran `bin/lint-md`: produced many style/rendering warnings. It is useful for
  typography and math hygiene, but it is too broad/noisy to be the primary
  source for this link/path audit.

## Findings

### 1. Active Docs Still Refer to `TODO.md` Archive

Classification: true stale active references.

`TODO.md` now says the archive has been collapsed:

| File | Line(s) | Current claim |
| --- | ---: | --- |
| `TODO.md` | 3 | "Archive collapsed" |

But active docs still describe `TODO.md` as containing an archive or archived
findings:

| File | Line(s) | Issue |
| --- | ---: | --- |
| `CHANGELOG.md` | 5, 9, 12 | The relation block still describes `TODO.md` section Archive as active. |
| `CHANGELOG.md` | 264 | Links to `TODO.md#archive--work-landed`, which no longer exists. |
| `CLAUDE.md` | 24, 29, 180, 195 | Tells agents to use `TODO.md` for archived findings / Archive records. |
| `README-auditor.md` | 35 | Says `TODO.md` has active and archived findings. |
| `doc/readme/src/_auditor-instructions.md` | 14 | Source of the generated README-auditor claim above. |

Recommendation:

- Update active docs to say that current work is in `TODO.md`, consolidated
  change history is in `CHANGELOG.md`, frozen archaeology is in `LOG.md`, and
  extracted audit finding records are in `audits/pending-findings-YYYY-MM-DD.md`.
- Remove or retarget `CHANGELOG.md`'s `TODO.md#archive--work-landed` link.
- Update `doc/readme/src/_auditor-instructions.md`, then rebuild README outputs
  with `bin/build-readme`.

Historical note:

- `LOG.md:7` and `LOG.md:192` also mention `TODO.md` Archive, but `LOG.md` is
  explicitly frozen archaeology. Leave those as-is unless adding a short
  editorial note at the top of `LOG.md`.

### 2. `CHANGELOG.md` Links to Missing Project/Session Artifacts

Classification: true broken links in an active root doc.

These entries are formatted as local markdown links, but no matching
`project_*.md` or `session_*.md` files are present in the repository.

| File | Line | Missing link target |
| --- | ---: | --- |
| `CHANGELOG.md` | 209 | `session_2026_03_11_tst_conversion.md` |
| `CHANGELOG.md` | 212 | `project_fresh_eyes_2026_03_14.md` |
| `CHANGELOG.md` | 219 | `project_soc_composition.md` |
| `CHANGELOG.md` | 222 | `project_section_iii_unity_closure.md` |
| `CHANGELOG.md` | 225 | `project_2026_04_22_audit_cycle.md` |
| `CHANGELOG.md` | 228 | `project_2026_04_22_strengthening_cycle.md` |
| `CHANGELOG.md` | 231 | `project_2026_04_22_23_cascading_strengthening.md` |
| `CHANGELOG.md` | 234 | `project_2026_04_23_brainstorm_cycle.md` |
| `CHANGELOG.md` | 237 | `project_2026_04_23_gap_ab_cycle_and_promotion.md` |
| `CHANGELOG.md` | 240 | `project_2026_04_23_sp2_citation_audit.md` |
| `CHANGELOG.md` | 243 | `project_2026_04_24_consolidation_and_naming.md` |
| `CHANGELOG.md` | 246 | `project_2026_04_25_audit_session.md` |
| `CHANGELOG.md` | 249 | `project_2026_04_25_audit_extraction.md` |
| `CHANGELOG.md` | 252 | `project_2026_04_24_pressure_point_cycle.md` |

Recommendation:

- If these were never meant to be repository files, convert the bracket links to
  plain labels.
- If they correspond to real records now folded into other artifacts, replace
  the links with the current targets, likely `LOG.md`, `audits/pending-findings-*`,
  `spikes/INDEX.md`, or the relevant audit/proposal file.
- Because this is a concentrated cluster, it is a good candidate for one
  focused cleanup commit.

### 3. Current Audit Instructions Still Mention Pre-Move Paths

Classification: stale current instructions.

| File | Line(s) | Issue |
| --- | ---: | --- |
| `doc/de-novo-audit-instructions.md` | 182 | Says agentic-TFT source materials and naming artifacts are under `msc/`; current paths are `ref/agentic-tft/agentic-tft-*.md` and `msc/naming/...`. |
| `doc/de-novo-audit-instructions.md` | 183 | Says root `CLAUDE-2.md` is transitional; it has moved to `_obs/CLAUDE-2-superseded-2026-04-28.md`. |
| `msc/naming/naming-aggregate-round2.md` | 7 | Says to follow `msc/naming-principles.md`; current path is `doc/naming-principles.md`. |

Recommendation:

- Update `doc/de-novo-audit-instructions.md` because it is current user-facing
  process guidance.
- For `msc/naming/naming-aggregate-round2.md`, either update the path or mark
  the file explicitly as an old round-2 input artifact. It still reads like
  executable instructions, so the current stale path is easy to trip over.

Historical note:

- `CHANGELOG.md` references to old `msc/de-novo-audit-instructions.md` and
  `msc/naming-principles.md` mostly occur in dated history entries. Those should
  usually stay historical. Optional: add a current-path parenthetical only where
  the line is serving as current navigation.

### 4. Segment Links Still Use Pre Role-Prefix Filenames

Classification: true broken relative links in current segment files.

`01-aad-core/src/deriv-bias-bound.md` contains many links that omit the current
role prefixes. Examples:

| Line(s) | Old target | Likely current target |
| ---: | --- | --- |
| 16, 28, 86, 173 | `agent-identity.md` | `scope-agent-identity.md` |
| 22, 68 | `directed-separation.md` | `der-directed-separation.md` |
| 28 | `agent-model.md` | `form-agent-model.md` |
| 28, 127, 173, 205 | `additive-coordinate-forcing.md` | `disc-additive-coordinate-forcing.md` |
| 93 | `strategy-cost-regret-bound.md` | `deriv-strategy-cost-regret-bound.md` |
| 127, 209 | `identifiability-floor.md` | `disc-identifiability-floor.md` |
| 207 | `variational-sector-condition.md` | `deriv-variational-sector-condition.md` |
| 245 | `gain-sector-bridge.md` | `der-gain-sector-bridge.md` |
| 253 | `information-bottleneck.md` | `form-information-bottleneck.md` |

`01-aad-core/src/obs-simulation-results.md` has the same pattern:

| Line(s) | Old target | Likely current target |
| ---: | --- | --- |
| 32-37 | `adversarial-exponent-regimes.md` | `result-adversarial-exponent-regimes.md` |
| 32-37 | `observation-gates-advantage.md` | `obs-gates-advantage.md` |
| 32-37 | `per-dimension-persistence.md` | `result-per-dimension-persistence.md` |

Recommendation:

- Fix these directly; they appear to be leftovers from the filename role-prefix
  sweep, not historical references.
- After fixing, run a narrow link check over `01-aad-core/src/*.md` and
  `bin/lint-outline`.

### 5. Logogenic OUTLINE Prose Contradicts Its Links

Classification: stale prose; links are already correct.

| File | Line(s) | Issue |
| --- | ---: | --- |
| `03-logogenic-agents/OUTLINE.md` | 38, 40 | Says the working documents are "in `msc/`", but the table links to `../ref/agentic-tft/...`. |

Recommendation:

- Change the prose to say the working documents are in `ref/agentic-tft/`.
- The table links themselves should be left alone; they already point at the
  moved files.

### 6. `LEXICON.md` Has a Stale README Anchor and Old Section Numbering

Classification: current-doc drift.

| File | Line(s) | Issue |
| --- | ---: | --- |
| `LEXICON.md` | 3 | Links to `README.md#lexicon`, but `README.md` has no `#lexicon` heading. |
| `LEXICON.md` | 29-30 | Describes Logogenic/Logozoetic AAD as "Section V"; current top-level structure uses `03-logogenic-agents/` and `04-logozoetic-agents/`. |
| `01-aad-core/src/scope-agent-identity.md` | 57 | Refers readers to "Section V" for AI/logogenic agents. |
| `02-tst-core/src/der-dual-optimization.md` | 93 | Refers to "Section V" for logogenic agents. |

Recommendation:

- Retarget the README link to `README.md#overview-of-concepts` or remove it and
  describe `LEXICON.md` as the canonical full lexicon.
- Replace current-doc "Section V" references with `03-logogenic-agents/`,
  `04-logozoetic-agents/`, or "the logogenic/logozoetic parts", depending on
  the local context.

Historical note:

- "Section V" language in `spikes/` can stay unless those spikes are promoted;
  it is part of the source-material trail.

### 7. `PRACTICA.md` Uses Obsidian Wikilinks

Classification: low-risk active-doc consistency issue.

`PRACTICA.md:7-13` uses wikilinks such as `[[TODO]]`, `[[PROPOSALS]]`, and
`[[01-aad-core/OUTLINE|AAD OUTLINE]]`. The rest of the root docs primarily use
GitHub-style markdown links.

Recommendation:

- Convert the root navigation block to normal markdown links if GitHub/plain
  markdown navigation is the target.
- This is not semantically urgent; it is a consistency and clickability cleanup.

### 8. `FORMAT.md` Has Small Convention Drift

Classification: current-doc typo/path convention issues.

| File | Line(s) | Issue |
| --- | ---: | --- |
| `FORMAT.md` | 442, 498 | Refers to `notation.md`; actual root file is `NOTATION.md`. |
| `FORMAT.md` | 460-461 | Example says root-file links use `src/slug-name.md`; from repository root, component segment links need a component prefix such as `01-aad-core/src/...`. |
| `FORMAT.md` | 467 | The "write X not Y" examples are identical, so the rule is not actionable. |

Recommendation:

- Change `notation.md` to `NOTATION.md`.
- Clarify whether `src/slug-name.md` is intended for component-root outlines
  only.
- Correct the identical examples around tag spacing.

False positive note:

- Link checkers will flag example targets such as `slug-name.md` and
  `src/slug-name.md`; those are documentation examples, not actual broken
  links.

### 9. Outline Lint Still Finds Two Structural Issues

Classification: true structural hygiene findings from tooling.

`bin/lint-outline` currently reports:

| Type | Detail |
| --- | --- |
| Ordering violation | `deriv-causal-ib-lmi` depends on `deriv-fisher-whitened-update-rule`; `deriv-causal-ib-lmi` must come after `deriv-fisher-whitened-update-rule` in section A. |
| Orphan segment | `01-aad-core/src/deriv-directional-survival-exploration.md` exists but is not referenced in the outline. |

Recommendation:

- Reorder the affected outline rows or adjust dependencies if the dependency is
  wrong.
- Decide whether `deriv-directional-survival-exploration.md` should be added to
  the outline, moved into a parked/old location, or explicitly documented as an
  intentional orphan.

Intentional forward reference:

- `01-aad-core/OUTLINE.md:217` links `src/worked-example-cam.md` and marks it
  `missing`. Because the outline row explicitly says `missing`, this looks like
  an intentional forward placeholder rather than a broken link to fix in this
  pass.

### 10. README Source Partials Need Generated-Context Link Checking

Classification: tooling recommendation, not a content bug.

Raw path checks against `doc/readme/src/_*.md` produce false positives because
those partials are assembled into root-level README files before their links are
meant to resolve. `bin/build-readme --check` passes, so the generated outputs are
currently in sync.

Examples:

| Partial | Apparent issue | Why it is probably false-positive |
| --- | --- | --- |
| `doc/readme/src/_navigation.md` | Links such as `#cross-domain-joining` do not exist in the partial itself. | The anchor exists after README assembly. |
| `doc/readme/src/_*.md` | Root-relative links look wrong when interpreted relative to `doc/readme/src/`. | They are intended to resolve from generated root README files. |

Recommendation:

- If `bin/lint-readme` is added, it should validate links and anchors in the
  generated README outputs, not the raw partial files alone.
- This aligns with `TODO.md:147`, which already calls for README slug and
  cross-reference validation.

### 11. `msc/brainstorm-findings.md` Anchor Looks Suspect

Classification: likely broken intra-file anchor; medium/low priority.

| File | Line | Link |
| --- | ---: | --- |
| `msc/brainstorm-findings.md` | 23 | `#speculative--worth-flagging-s1s8` |

The target heading is `Speculative / "Worth Flagging" Section (S1-S8)` in
rendered ASCII terms, so the exact GitHub anchor likely includes `section` and
may differ around punctuation.

Recommendation:

- Verify the rendered anchor and retarget the link.
- Alternatively add a manual HTML anchor before the target heading if stable
  cross-renderer behavior matters.

## Historical or Provenance References That Look OK

These references should generally not be mass-edited:

- `LOG.md` references to old paths and `TODO.md` Archive. The file is frozen
  archaeology and should preserve what the session record said at the time.
- `_obs/*` references to old structure, old proposed names, and superseded
  documents.
- `spikes/*` references that preserve older section numbering or candidate
  structure, unless a spike is being promoted into active manuscript text.
- `msc/naming/name-transition-aad.md` references to old ACT/AAD names and
  transitional paths. This is the authoritative rename/provenance record, so it
  should preserve old names intentionally.
- `msc/naming/naming-cleanup-scan-codex-2.md:48`, which explicitly says the
  name-transition document should preserve old names.
- `spikes/INDEX.md:5`, which says material moved from `msc/SPIKES.md` to
  `spikes/INDEX.md`. That is a historical move note and is accurate.
- `CHANGELOG.md` dated entries that mention old `msc/de-novo-audit-instructions.md`
  or `msc/naming-principles.md` as part of a past migration. Only change them if
  the line is also being used as current navigation.
- Bare source-material mentions inside `ref/agentic-tft/*` that are not markdown
  links. These often function as provenance notes rather than local navigation.

## Recommended Fix Order

1. Fix active navigation and process docs:
   `CLAUDE.md`, `CHANGELOG.md`, `doc/de-novo-audit-instructions.md`,
   `doc/readme/src/_auditor-instructions.md`, `03-logogenic-agents/OUTLINE.md`,
   `LEXICON.md`, `PRACTICA.md`, and `FORMAT.md`.
2. Rebuild README outputs with `bin/build-readme` and confirm with
   `bin/build-readme --check`.
3. Fix current segment-local links in
   `01-aad-core/src/deriv-bias-bound.md` and
   `01-aad-core/src/obs-simulation-results.md`.
4. Resolve the two `bin/lint-outline` findings: the dependency ordering issue
   and the orphan segment.
5. Decide what the missing `CHANGELOG.md` project/session links should become:
   plain labels, links into `LOG.md`, links into `audits/`, or restored files.
6. Add or extend a focused link checker that understands generated README
   context, intentional missing outline rows, and example links in `FORMAT.md`.

## Verification Snapshot

- `bin/build-readme --check`: passed.
- `bin/lint-outline`: failed with one ordering violation and one orphan segment.
- `bin/lint-md`: noisy; useful but not specific enough for this audit.
- No source docs were modified during this audit pass.
