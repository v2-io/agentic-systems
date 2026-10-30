---
kind: review
author:
  name: Claude Opus 5.5 (item rechecker, lane p-process)
  role: rechecker
sources:
  - msc/inside-out-2026-10/items-recheck/p-process.md
written: 2026-10-30
---

# Item re-check lane p-process (process, tooling and decision trackers): findings on segments

KR I.3, under the top intent *"Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself"*. The four trackers of this lane are about process, so they name few segments. Deleting them turned up one canon referrer, and it is an instance of the pilot's section 2.8 pattern: a Working Note whose status line is false.

## F1 (finding)
- target: segment:disc-w1-structural-bound-boundary

Working-Note status signal: the Working Note at line 87 says the exact-enumeration simulation behind the $\Theta(\varepsilon^2)$ flatness (`spikes/sim-w1-w2-boundary.py`, figure `spikes/w1-w2-boundary.png`) "sits unintegrated in `spikes/`, blocking on the sim-integration process (G3 in `INTEGRATION-CLEANUP-TODO.md`)". Nothing blocks it. The sim-integration process has existed since 2026-07-16: the `empirica/` registry (`empirica/README.md`) and the principle in `doc/sop/spikes.sop.md` §0a point 5. The tracker it names was deleted on 2026-10-30, and "G3" there was the citation work, not simulations (that was G4). The status also hides a real defect in the body. Lines 49 and 61 state the toy's result (monotone, smooth, $\Theta(\varepsilon^2)$, flat to first order) and draw a design implication from it, and the reader has no recorded run to check it against. Under §0a point 5, the sim should enter `empirica/` with a MANIFEST and RUNS entry, and the body should cite `empirica:<slug>`, or state the toy's parameters in full, self-contained. The Working Note line should then go. The work is ledger item `w1-boundary-toy-sim-unregistered` (owner F.3).
