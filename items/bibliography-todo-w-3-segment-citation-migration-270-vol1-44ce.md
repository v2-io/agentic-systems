---
kind: item
provenance: imported
source: BIBLIOGRAPHY-TODO.md:131
section: 'containing exactly the assembled current volume markdown, then runs: › Workstreams ASF needs to own'
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T20:27:08Z by Claude Opus 5.5 (item rechecker, pilot)
owner: F.2 / F.3 (citations reach the bodies faithfully)
---

# W-3. Segment citation migration (~270 Vol1 prose references)

Imported verbatim (relative links rebased) from `BIBLIOGRAPHY-TODO.md` line 131, section *containing exactly the assembled current volume markdown, then runs: › Workstreams ASF needs to own*. Not yet re-checked against HEAD: `vsect recheck item:bibliography-todo-w-3-segment-citation-migration-270-vol1-44ce --outcome holds|stale|landed|not-an-item --why …`.


Per-segment, author-pass (NOT mechanical regex). For each prose reference in Vol1 (and ~70 more across Vols 2–4):

1. Identify the work (look up in relata: `relata search <author keyword>` or `relata possible-duplicates --title "..."`).
2. If it exists in relata: add a formal natbib-compatible cite if the work should appear in the bibliography; preserve rich scholarly prose around that cite when useful. For load-bearing dependencies, include a locator where available and add a relata verification event as promotion work proceeds.
3. If it doesn't exist in relata: `relata add <new-bibkey>` (scaffold) or paste BibTeX on stdin; fill in fields; then proceed with step 2.

Foundational AAT works still worth checking during migration: quick `relata search` probes on 2026-06-04 did not surface Sutton & Barto's *Reinforcement Learning*, Koller & Friedman's PGM textbook, or Bishop's PRML by those author names; Da Costa active-inference works and Hafez works do surface now. Treat this as a search prompt, not proof of absence: look up each first cite in relata, add the entry if genuinely missing, then proceed with the citation judgment above.

**Substantial — multi-session per-volume work; Vol1 dense, Vols 2–4 lighter.**
