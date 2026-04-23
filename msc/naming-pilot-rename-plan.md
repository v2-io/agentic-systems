# Naming Pilot — Rename Mapping Details

Live record of specific rename mappings for the role-prefix pilot workstream.
This file is **excluded** from `bin/rename-slug`'s substitution patterns
(`msc/naming-*.md` glob) so the mappings below survive future renames verbatim
and remain legible as a historical record of which names were executed.

See `TODO.md §"Active — Naming Discipline"` for the surrounding strategic plan
(insights, role-prefix discipline, post-pilot workstream).

## Landed — role-prefix pilot complete (2026-04-23)

| Date       | Old slug                        | New slug                                 | Executed by       | Notes |
|------------|---------------------------------|------------------------------------------|-------------------|-------|
| 2026-04-23 | `ai-agent-as-act-agent`         | `scope-logogenic-agent`                  | `bin/rename-slug` | Resolves `-act-agent` relic; taxonomy-conformant (logogenic is the class). Type: `definition` → `scope`; H1 + formal tag updated. |
| 2026-04-23 | `developer-as-act-agent`        | `scope-developer-agent`                  | `bin/rename-slug` | Resolves `-act-agent` relic; covers human AND AI developers in the software context (not narrowed to humans). Type: `definition` → `scope`; status: `exact` → `axiomatic` (resolves Finding 14 Option A); H1 + formal tag updated. |
| 2026-04-23 | `composition-scope-condition`   | `scope-composite-agent`                  | `bin/rename-slug` | Prefix + subject-noun; subject class is the composite agent, not the "condition". H1 + formal tags + prose references updated. |
| 2026-04-23 | `scope-condition` *(split)*     | `scope-adaptive-system` + `scope-agency` | manual + `bin/rename-slug` | Semantic split. The original segment defined two nested scopes ($\mathcal{S}_\text{adaptive}$ and $\mathcal{S}_\text{agency}$); downstream segments depend on one or the other, not on an abstract "condition". Executed as: script-driven rename to `scope-agency` (majority case), hand-authored `scope-adaptive-system.md` with adaptive content, 6 hand re-routings for adaptive-dependent files, one split-reference cleanup in `causal-structure.md`. |
| 2026-04-23 | `identifiability-floor`         | `discussion-identifiability-floor`       | `bin/rename-slug` | Pure role-prefix add; subject-noun already strong. |
| 2026-04-23 | `separability-pattern`          | `discussion-separability-pattern`        | `bin/rename-slug` | Pure role-prefix add. Subject-noun substitution to `separability-ladder` (Round-1 consensus) deferred to refined Round 1 + Round 2. |
| 2026-04-23 | `additive-coordinate-forcing`   | `discussion-additive-coordinate-forcing` | `bin/rename-slug` | Pure role-prefix add. Subject-noun substitution to `forced-coordinates` (Round-1 consensus; addresses Čencov-instance scope-honesty concern) deferred to refined Round 1 + Round 2. |

Seven slug changes total, one of which (scope-condition) was a 1:2 semantic split.
Nine total segment files moved or created; 01-aad-core lint-clean after every step.

## Deferred to refined Round 1 / Round 2

Subject-noun substitutions on the three meta-segments surfaced in Round 1 as
consensus renames but deserve the voting process rather than ad-hoc landing
during the role-prefix pilot. They are:

- `discussion-separability-pattern` → `discussion-separability-ladder` (Round-1 consensus; "ladder" more evocative than "pattern" for the three-rung shape).
- `discussion-additive-coordinate-forcing` → `discussion-forced-coordinates` (Round-1 consensus; current "additive" does not cover the Čencov-Fisher instance).
- A future broader pass over all non-role-prefix slugs (the subject-noun sweep that the pilot was meant to pave the way for).

## Deferred / resolved separately

- The `aad-agent` vs `adaptive-agent` family debate was superseded by the
  taxonomy-conformant move to `scope-logogenic-agent` and `scope-developer-agent`.
  No remaining open question on these two destinations.
- `ASF` vs `Agentic Systems Framework` umbrella naming — Round 1 agents misread
  `ASF` as debt when it is the intentional parent-level name (AAD is Part I;
  TST is Part II). Re-surface in refined Round 1 with correct framing.

## Pilot-validation observations (worth folding into refined Round 1 principles)

- **Role-prefix reads cleanly in cross-references.** `#scope-agency`, `#scope-composite-agent`, `#discussion-identifiability-floor` etc. read naturally in prose and sharpen the dependency graph. No awkward cases surfaced.
- **Semantic splits require hand work, not script.** The `scope-condition` split was worth it (the old name named nothing), but needed segment-authoring + per-reference classification. Tooling can assist on the bulk rename; the split judgment is irreducibly manual. Recommend: keep `bin/rename-slug` as a 1:1 tool only.
- **Formal-tag labels don't auto-update.** Tags like `*[Definition (slug)]*` embed the slug as a literal string. The mechanical rename doesn't touch them; `bin/rename-slug`'s stale-text scan surfaces them as warnings and the executing agent updates by hand. Low-cost convention.
- **H1 / opening-sentence framing drift.** Slug changes from `definition` to `scope` type imply H1 shifts (`# Definition: X as AAD Agent` → `# Scope: X Agent`) that the regex cannot detect. The "review the moved file" framing reminder in `bin/rename-slug` output is the right UX.
- **Script batch-mode re-planning.** Early batches failed when a later pair's edit list referenced a file that an earlier pair had already moved. Fix landed in this commit: re-plan each pair immediately before applying. Documented inline in the script.

## Why this file exists separately from TODO.md

`bin/rename-slug` performs global regex substitutions across live repo content.
TODO.md is live — references in its body must update with the rename. But a
*table of rename mappings themselves* would be catastrophically corrupted by
a rename sweeping through it (the old-slug column would get rewritten to match
the new-slug column). So rename-specific tables live here, and the script's
`msc/naming-*.md` exclusion glob keeps this file frozen.

When a new rename lands or a pending row changes status, update this file by
hand.
