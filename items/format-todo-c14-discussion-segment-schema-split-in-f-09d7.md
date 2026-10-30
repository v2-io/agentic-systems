---
kind: item
provenance: imported
source: FORMAT-TODO.md:167
section: 'FORMAT-TODO.md — Cross-Cutting Conventions: Citations, Cross-Refs, Footnotes, Sidenotes, Margin-Notes › Workstream C — Discipline + structural distinctions'
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:23:03Z by Claude Opus 5.5 (item rechecker, lane p-process)
owner: A.3
restated: Write the schema for intro, impl-* and disc-* segments into format.sop.md, replacing the 2026-07-14 cadence exemption (line 314), and reconcile it with A.3, which requires every live segment, the impl-*/intro layer included, to carry an Epistemic Status.
---

# C14. Discussion-segment schema split in FORMAT.md. Already flagged. Claim-segment schema (Formal Expression / Epistemic Status / Discussion / Findings required)

Imported verbatim (relative links rebased) from `FORMAT-TODO.md` line 167, section *FORMAT-TODO.md — Cross-Cutting Conventions: Citations, Cross-Refs, Footnotes, Sidenotes, Margin-Notes › Workstream C — Discipline + structural distinctions*. Not yet re-checked against HEAD: `vsect recheck item:format-todo-c14-discussion-segment-schema-split-in-f-09d7 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **C14. Discussion-segment schema split in FORMAT.md.** Already flagged. Claim-segment schema (Formal Expression / Epistemic Status / Discussion / Findings required) vs discussion-segment schema (body-only, subheads optional). The Discussion-as-chapter-intro renderer mode (commit `8da83cd`) suppresses subheads at render-time; the source still has them. FORMAT.md should split the schema so authors don't have to fake it.

Also raised in (WN-01 drain, 2026-10-30, Claude Opus 5.5): The impl-* and intro segments state their epistemic standing in Working Notes today: #impl-persistence-and-limits 'Scope of this segment' ('claims are as strong as their source segments and the synthesis adds no independent epistemic status'), #persistence-and-limits-intro, #the-cycle-in-motion-intro and #the-reality-model-intro ('carries no formal claim of its own'). These sentences are the Epistemic Status A.3 asks for.
