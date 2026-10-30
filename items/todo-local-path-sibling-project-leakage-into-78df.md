---
kind: item
provenance: imported
source: TODO.md:425
section: 'TODO — Miscellaneous & details › 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits — remaining open items › Group (a) — Build-pipeline / cross-cutting hygiene'
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:26:49Z by Claude Opus 5.5 (item rechecker, t2-todo)
owner: F.3
---

# Local-path / sibling-project leakage into publishable mono — codex Cross-File #3. Per `~/src/...`, audit-folder, search-log, and absolute-path references in seg

Imported verbatim (relative links rebased) from `TODO.md` line 425, section *TODO — Miscellaneous & details › 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits — remaining open items › Group (a) — Build-pipeline / cross-cutting hygiene*. Not yet re-checked against HEAD: `vsect recheck item:todo-local-path-sibling-project-leakage-into-78df --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **Local-path / sibling-project leakage into publishable mono** — codex Cross-File #3. Per `~/src/...`, audit-folder, search-log, and absolute-path references in segments leak into mono builds. Either strip at build time or rewrite to stable citations / archived excerpts. (`CURRENT-VOL1.md` as of 2026-08-22 still embeds at least one absolute path in a figure include; the `--public` flag strips Working Notes, not local paths.)
