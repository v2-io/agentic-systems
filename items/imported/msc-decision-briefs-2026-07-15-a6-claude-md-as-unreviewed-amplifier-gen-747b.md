---
kind: item
provenance: imported
source: msc/decision-briefs-2026-07-15.md:48
section: Decision briefs — 2026-07-15 (the valve) › Policy calls
owner: ""
opened: 2026-10-30T20:17:42Z
opened-by: Claude Fable 5.1
---

# A6 — CLAUDE.md as unreviewed amplifier: generate what's derivable + a review cadence?

Imported verbatim (relative links rebased) from `msc/decision-briefs-2026-07-15.md` line 48, section *Decision briefs — 2026-07-15 (the valve) › Policy calls*. Not yet re-checked against HEAD: `vsect recheck item:msc-decision-briefs-2026-07-15-a6-claude-md-as-unreviewed-amplifier-gen-747b --outcome holds|stale|landed|not-an-item --why …`.


*Since the 2026-07-07 census:* Decision itself unchanged (G5's three sub-items still open since 2026-05-19). But the 2026-07-14 cycle strengthened the machinery around it: `bin/refresh-all --check` now diff-verifies all 6 generated outputs (51bd02c), 6 weeks of generated-doc staleness was cleared (e62c3ae), and agents.sop got a manual unstaling pass (0d20b87) — proving both that generation-with-check works and that hand-maintained portions rot without a ritual.

**What:** Approve a standing fix for the auto-loaded CLAUDE.md (= `doc/sop/agents.sop.md`) — the doc every agent treats as gospel and you never read. Your 2026-05-19 observation: a predecessor's "minor" exception there silently overrode a correct principle for weeks (the ref/ source-of-truth sanction, excised 2026-05-30 under D-1).

**Context:** The one confirmed defect is fixed; what remains open (`INTEGRATION-CLEANUP-TODO.md` §G5) is structural: nothing prevents the next such defect. The repo already generates README/LEXICON/FINDINGS from sources, and as of 2026-07-14 `bin/refresh-all --check` catches generated-doc staleness mechanically. CLAUDE.md is still 100% hand-asserted.

**Options:** (1) Generate the derivable portions (File-Org map, SOP index, tracker list — the parts that drift most) from repo state, + a light cadence (e.g., you skim the hand-asserted remainder once per major cycle). (2) Cadence only — cheaper, rests on ritual. (3) Status quo — rests on agent virtue, which G5 explicitly says cannot hold.

**Lead recommendation:** Option 1. Uncertainty: how much is truly derivable is unproven (~est. a third); the disposition/conventions prose is not, so the cadence half is needed regardless.

**Pointer:** `INTEGRATION-CLEANUP-TODO.md` §F6/§G5; census cluster 04/07.
