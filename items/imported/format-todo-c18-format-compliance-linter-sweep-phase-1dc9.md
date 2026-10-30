---
kind: item
provenance: imported
source: FORMAT-TODO.md:171
section: 'FORMAT-TODO.md — Cross-Cutting Conventions: Citations, Cross-Refs, Footnotes, Sidenotes, Margin-Notes › Workstream C — Discipline + structural distinctions'
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
---

# C18. FORMAT-compliance linter sweep. Phase 5 of the prior plan. [Tooling note 2026-08-24: `bin/lint-md` is deprecated — the gate is `md-press --math --check` et

Imported verbatim (relative links rebased) from `FORMAT-TODO.md` line 171, section *FORMAT-TODO.md — Cross-Cutting Conventions: Citations, Cross-Refs, Footnotes, Sidenotes, Margin-Notes › Workstream C — Discipline + structural distinctions*. Not yet re-checked against HEAD: `vsect recheck item:format-todo-c18-format-compliance-linter-sweep-phase-1dc9 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **C18. FORMAT-compliance linter sweep.** Phase 5 of the prior plan. [Tooling note 2026-08-24: `bin/lint-md` is deprecated — the gate is `md-press --math --check` etc. (`git-hygiene.sop.md`); this sweep's mechanical layer should run through md-press, with any lint-md-only categories filed as md-press gaps.] `bin/lint-md --fix` for auto-fixable categories (hard-wraps, emphasis-underscores, `_` in `\text{}`); manual / agent-driven sweep for the rest (math compatibility issues — `|` / `\|` / `<` / `>` / `*` in math; `\text` outside `$`; etc.). ~200+ findings across the corpus.
