---
kind: item
provenance: imported
source: PROPOSALS.md:123
section: PROPOSALS — Architectural Portfolio › §C. Soon — prereqs nearly met
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:disc-separability-pattern]
rechecked: 2026-10-30T21:30:34Z by Claude Opus 5.5 (item rechecker, q-proposals lane)
owner: F.1
restated: 'Decide whether #disc-additive-coordinate-forcing and #disc-separability-pattern get shorter speakable names (#cauchy-coordinates, #separability-ladder), through the naming process with F.4''s ''does this already have a name elsewhere?'' check first.'
---

# C.4 SP-19 — Naming consolidation pass

Imported verbatim (relative links rebased) from `PROPOSALS.md` line 123, section *PROPOSALS — Architectural Portfolio › §C. Soon — prereqs nearly met*. Not yet re-checked against HEAD: `vsect recheck item:proposals-c-4-sp-19-naming-consolidation-pass-9020 --outcome holds|stale|landed|not-an-item --why …`.


Top Priority-2 items from `msc/naming/naming-brainstorm-2026-04-24.md` (inner path in [`.archive/msc-naming-2026-08-22.tar.gz`](../../.archive/msc-naming-2026-08-22.tar.gz)): (a) `#additive-coordinate-forcing` → `#cauchy-coordinates` (shorter, more speakable); (b) `#disc-separability-pattern` → `#separability-ladder`; (c) paired trio "**floor / ladder / Cauchy-coordinates**"; (d) template-family naming (sector / contraction / dissipativity). Rides with Bundle 1 (framework-face reframe) — naming is the implementation layer of the reframe.

**Prereq:** Joseph-level naming decision (judgment-call territory; worth an explicit naming-cycle check-in before landing). **Execution:** 1 session.

Primary aspect: approachability / teachability. Secondary: beauty. **Value: +3 framework.**

**Independence: low.** Renames propagate through every cross-reference in the codebase; touches ~20+ segments and the OUTLINE files. Must serialize with *all* segment-editing work (including Bundle 1 and C-BP1+C-BP4). Best landed as a single atomic commit pass after other in-flight work quiesces.

---
