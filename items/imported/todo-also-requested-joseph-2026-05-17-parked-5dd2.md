---
kind: item
provenance: imported
source: TODO.md:488
section: TODO — Miscellaneous & details › 2026-05-17 — scrbook appendix numbering (PARKED mid-fix to focus on self-actuation; pickup-ready)
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
---

# Also requested (Joseph 2026-05-17), parked with this: appendices in the ToC should read *as if they were segments* (section-register indent/weight) while stayin

Imported verbatim (relative links rebased) from `TODO.md` line 488, section *TODO — Miscellaneous & details › 2026-05-17 — scrbook appendix numbering (PARKED mid-fix to focus on self-actuation; pickup-ready)*. Not yet re-checked against HEAD: `vsect recheck item:todo-also-requested-joseph-2026-05-17-parked-5dd2 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **Also requested (Joseph 2026-05-17), parked with this:** appendices in the ToC should read *as if they were segments* (section-register indent/weight) while staying `\chapter` in the body. Mechanism already exists in kaobook: `\asfAppendixToCremap` (`mono/kaobook/preamble/environments.tex:318-328`) — a one-time `\addcontentsline` chapter→section redirect fired at `\appendix` time. Port the identical macro to scrbook (define in `mono/scrbook/preamble/environments.tex`, emit right after the `\thechapter` rebind in `typeset_scrbook.rb`). Non-intrusive, proven.
