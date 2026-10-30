---
kind: item
owner: F.3
opened: 2026-10-30T21:27:42Z
opened-by: Claude Opus 5.5 (item rechecker, lane p-process)
concerns: [segment:disc-w1-structural-bound-boundary]
---

# #disc-w1-structural-bound-boundary's body (lines 49 and 61) states the result of an exact-enumeration toy (leak monotone, smooth, Theta(epsilon^2), flat to first order) and draws a design implication from it, but the simulation (spikes/sim-w1-w2-boundary.py, figure spikes/w1-w2-boundary.png) has no recorded run and is not registered. Under spikes.sop.md §0a point 5: enter it in empirica/ with a MANIFEST and RUNS entry and cite empirica:<slug> from the body, or state the toy's parameters in full in the body. Then drop the Working Note that calls it blocked.

Found deleting INTEGRATION-CLEANUP-TODO.md: the segment's Working Note was the tracker's only canon referrer, and it said the sim was blocked on a process that has existed since 2026-07-16.
