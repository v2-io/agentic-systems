# SUPERSEDED — 2026-05-01

This directory was `tools/role-encounter/` — a YAML-config-driven tool for producing per-role file-encounter orderings (auditor, naming-voter, normal contributor) plus a generated cross-tab table and per-role views.

## Why it was shelved

The role-encounter tool was solving the wrong problem. The project already had `doc/readme/` liquid templates + `bin/build-readme` + auto-extraction tooling — the authoritative source for "what's in the project, who's reading it, in what order." The role-encounter tool built a parallel meta-document layer next to that infrastructure rather than extending it. Result: file/directory information ended up scattered across CLAUDE.md, role instruction docs, READMEs, the role-encounter table, and the per-role views — the opposite of the consolidation it was meant to provide.

The reframe (2026-05-01 conversation): the right artifact is **per-role README files** generated from the existing liquid pipeline. `README.md` (master), `README-auditor.md`, `README-voter.md`, etc. — each composing a shared auto-generated project-tree partial plus role-specific onboarding partials. Instructions content currently in `doc/de-novo-audit-instructions.md`, `naming-principles.md`, `naming-cycle-methodology.md` migrates into `doc/readme/src/_<topic>.md` partials and gets composed into the appropriate role README.

## What's worth keeping for archaeology / reuse

- **The appendix-after-first-mention algorithm** (`bin/build-encounter-table` lines around the segment-walk + appendix hoist). If a future tool needs to render segments in linear order with appendices placed after their first surfacing point, this logic is correct and tested.
- **The OUTLINE-walk machinery** in `bin/build-encounter-table` — reuses `bin/lint-outline`'s dependency graph; emits ordered segment lists per component. Could be lifted if a future tool needs OUTLINE-aware traversal.
- **The naming-context-map view** at `views/naming-context-map.md` — a metadata-only Phase-1 best-effort version of "for each naming target, the segment that defines it + recursive depends chain." Was over-engineered for what Phase 1 needed; the Phase 2 semantic-index version (per `spikes/spike-local-embedding-benchmark/FINDINGS.md`) supersedes this with proper anchoring.

## Lessons (saved as feedback memory)

The pattern: **when a problem framing produces tooling that parallels existing infrastructure rather than extends it, the framing is probably wrong.** This was the lesson from the over-engineering — the right test at the brief stage was *"why isn't this just an extension to `bin/build-readme`?"* Recorded as `feedback_problem_framing_paralleling_test.md` in project memory.

## Related artifacts

- `msc/role-encounter-plan.md` — the planning doc that drove this work. Captures the design discussion; preserved as session archaeology, not authoritative.
- `spikes/spike-local-embedding-benchmark/` — the Phase 2 embedding spike. Independent of this superseded work; semantic-index findings still apply to the future per-role README work and to the naming-context-map.
- `msc/handoff-2026-05-01.md` — session handoff that documents this shelving in the broader context.
