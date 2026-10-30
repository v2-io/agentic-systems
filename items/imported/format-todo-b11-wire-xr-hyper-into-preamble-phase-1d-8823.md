---
kind: item
provenance: imported
source: FORMAT-TODO.md:158
section: 'FORMAT-TODO.md — Cross-Cutting Conventions: Citations, Cross-Refs, Footnotes, Sidenotes, Margin-Notes › Workstream B — Cross-refs, footnotes, sidenotes, margin-notes'
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
---

# B11. Wire `xr-hyper` into preamble. Phase 1d. The `.aux` files are persisted from the scrbook target (`01-aat-core/aat.aux` etc.); `xr-hyper` reads sibling-volu

Imported verbatim (relative links rebased) from `FORMAT-TODO.md` line 158, section *FORMAT-TODO.md — Cross-Cutting Conventions: Citations, Cross-Refs, Footnotes, Sidenotes, Margin-Notes › Workstream B — Cross-refs, footnotes, sidenotes, margin-notes*. Not yet re-checked against HEAD: `vsect recheck item:format-todo-b11-wire-xr-hyper-into-preamble-phase-1d-8823 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **B11. Wire `xr-hyper` into preamble.** Phase 1d. The `.aux` files are persisted from the scrbook target (`01-aat-core/aat.aux` etc.); `xr-hyper` reads sibling-volume `.aux` for cross-volume label resolution. Fallback form pending open question 4. `.aux` staleness detection: warn or error when a sibling `.aux` was written against a different sibling-volume semver than the one being referenced.
