---
kind: item
owner: F.3
opened: 2026-10-30T21:27:42Z
opened-by: Claude Opus 5.5 (item rechecker, lane p-process)
concerns: [segment:disc-w1-structural-bound-boundary]
---

# #disc-w1-structural-bound-boundary's body (lines 49 and 61) states the result of an exact-enumeration toy (leak monotone, smooth, Theta(epsilon^2), flat to first order) and draws a design implication from it, but the simulation (spikes/sim-w1-w2-boundary.py, figure spikes/w1-w2-boundary.png) has no recorded run and is not registered. Under spikes.sop.md §0a point 5: enter it in empirica/ with a MANIFEST and RUNS entry and cite empirica:<slug> from the body, or state the toy's parameters in full in the body. Then drop the Working Note that calls it blocked.

Found deleting INTEGRATION-CLEANUP-TODO.md: the segment's Working Note was the tracker's only canon referrer, and it said the sim was blocked on a process that has existed since 2026-07-16.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork B1): re-ran `spikes/sim-w1-w2-boundary.py` at `cbd2f345`. All computations complete (Experiment 1 at $s = 0.40$, $\varepsilon = 0$: actual leak 0.11871 bits, circular bound 0, selection certificate 0.53100 bits, DPI check true); only the final plot write fails unless the working directory is the asf root, because it saves to the relative path `spikes/w1-w2-boundary.png`. The empirica entry should fix the path. Its companions `spikes/sim_guc_classes.py` and `spikes/sim_guc_boundaries.py` (the latter imports the former, so it needs the `spikes/` directory on the path) are in the same state and ground `#der-directed-separation:108`; see `item:der-directed-separation-108-says-boundary-2-clas`. The three-way-tradeoff sim is `item:disc-exploit-explore-deliberate-s-epistemic-stat`.
