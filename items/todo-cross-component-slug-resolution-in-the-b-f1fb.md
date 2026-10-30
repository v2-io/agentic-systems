---
kind: item
provenance: imported
source: TODO.md:424
section: 'TODO — Miscellaneous & details › 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits — remaining open items › Group (a) — Build-pipeline / cross-cutting hygiene'
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:26:49Z by Claude Opus 5.5 (item rechecker, t2-todo)
owner: H.2
restated: 'bin/lib resolves #slug only against the building volume''s own outline (ingest.rb:226, assemble.rb:103,383); cross-volume references render as literal ''#slug''. Decide the rendering for cross-volume refs (resolve to ''Vol. 1, Result 4.2''-style labels from all four outlines) and implement.'
---

# Cross-component `#slug` resolution in the build — open question. The two 2026-05-12 cases (`hyp-checkpoint-forking-failure-modes`, `hyp-experiential-training`)

Imported verbatim (relative links rebased) from `TODO.md` line 424, section *TODO — Miscellaneous & details › 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits — remaining open items › Group (a) — Build-pipeline / cross-cutting hygiene*. Not yet re-checked against HEAD: `vsect recheck item:todo-cross-component-slug-resolution-in-the-b-f1fb --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **Cross-component `#slug` resolution in the build — open question.** The two 2026-05-12 cases (`hyp-checkpoint-forking-failure-modes`, `hyp-experiential-training`) were fixed by OUTLINE wiring (2026-07-14), not by the resolver; whether `bin/build-monograph` resolves references against every component `src/` or only the volume's own was not determined (2026-08-22). Settle by reading `bin/lib`, then either close or fix.
