---
kind: item
provenance: imported
source: TODO.md:489
section: TODO — Miscellaneous & details › 2026-05-17 — scrbook appendix numbering (PARKED mid-fix to focus on self-actuation; pickup-ready)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:29:32Z by Claude Opus 5.5 (item rechecker, t2-todo)
owner: unassigned
restated: 'Appendix numbering: option (1), one continuing \AlphAlph counter, is what ships; decide whether per-group numbering (A.1..., B.1...) is worth the change for ~45 appendices, and record the reason either way.'
---

# Design decision Joseph flagged — pick before finishing. Either (1) continue the single established `\AlphAlph` counter across both groups (group 2 → AN, AO, …);

Imported verbatim (relative links rebased) from `TODO.md` line 489, section *TODO — Miscellaneous & details › 2026-05-17 — scrbook appendix numbering (PARKED mid-fix to focus on self-actuation; pickup-ready)*. Not yet re-checked against HEAD: `vsect recheck item:todo-design-decision-joseph-flagged-pick-befo-2649 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **Design decision Joseph flagged — pick before finishing.** Either **(1)** continue the single established `\AlphAlph` counter across both groups (group 2 → AN, AO, …); or **(2)** restructure appendices into per-group numbering — e.g. `A.1`–`A.10`, `B.1`–`B.10` (group letter + within-group number, counter resets per `*Appendices*` group). Option (2) also addresses the legibility smell of ~45 flat appendices and would make the second-group collapse moot (per-group reset sidesteps the >26 overflow entirely). Monograph-convention call, not mechanical — Joseph's decision gates the final implementation.
