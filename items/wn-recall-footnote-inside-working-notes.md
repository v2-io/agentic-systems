---
kind: item
owner: C.1
opened: 2026-10-30T23:31:29Z
opened-by: Claude Opus 5.5 (Working Notes drain, 02-04)
concerns: [segment:scope-observation-ambiguity-modulation]
---

# #scope-observation-ambiguity-modulation defines its footnote [^recall-2026-10-30] inside its `## Working Notes` (the last lines of the file), while two body rows of its Related Work table (:117 Yang 2026, :120 Murphy 1973 / Bröcker 2009 / Gneiting & Raftery 2007) reference it. Any build that drops Working Notes (`bin/build-monograph --public`, the CURRENT-VOL snapshots) and the I.5 Working-Notes cleanup orphan it, and the citations lose the marker that says they were checked only bibliographically (Yang 2026 unread). Move the definition above `## Working Notes`. It came in with the Part II integration (253d2bca).

Found by the Working Notes drain (02-04) reading the segment's Working Notes at dc2b262c; msc/inside-out-2026-10/drain/wn-02-04.md.
