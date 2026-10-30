---
kind: item
provenance: imported
source: TODO.md:45
section: TODO — Miscellaneous & details › Strengthen-first candidates from the 2026-05-30/31 gold-lift sweep
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:def-unity-dimensions, segment:result-unity-closure-mapping]
rechecked: 2026-10-30T20:23:54Z by Claude Opus 5.5 (item rechecker, pilot)
owner: C.1 integrator (unassigned)
restated: "F146 (U_M normalization) landed in f8d9151a; what holds is F154: #result-unity-closure-mapping states the linear-Gaussian epsilon_x = 0 result without its invariance hypothesis (the condition sits in the next sentence), and six 526815 findings (F151-F156) remain un-adjudicated in its off-ramp Working Note."
---

# `#def-unity-dimensions` (A13 F146) — $U_M = I/H$ not normalized to $[0,1]$ as the label implies; `#result-unity-closure-mapping` (A13 F154) — the $\varepsilon_x

Imported verbatim (relative links rebased) from `TODO.md` line 45, section *TODO — Miscellaneous & details › Strengthen-first candidates from the 2026-05-30/31 gold-lift sweep*. Not yet re-checked against HEAD: `vsect recheck item:todo-def-unity-dimensions-a13-f146-u-m-i-h-no-6bb8 --outcome holds|stale|landed|not-an-item --why …`.

- `#def-unity-dimensions` (A13 F146) — $U_M = I/H$ not normalized to $[0,1]$ as the label implies; `#result-unity-closure-mapping` (A13 F154) — the $\varepsilon_x = 0$ claim needs projection-range invariance, not just consistent projections.

Also raised in (wn-01-gold drain, 2026-10-30): #def-unity-dimensions Working Notes Off-ramp line 154 (526815 F146-F150). F146 is in canon (line 34). F147-F150 are still unstated at HEAD 86489b0b. U_O as pairwise value correlation (line 40) is undefined for zero-variance value functions and depends on the distribution and policy. The U_Sigma KL ratio (line 50) can have a zero denominator or an infinite numerator and leave [0,1] without clipping. U_obs (line 56) misses complementary-private-plus-routed and synergistic observation. U_f = 1 - d (lines 64-66) presumes a d normalized to [0,1] that the candidate distances do not supply. These are soft metric conventions, the same kind of fix as F151-F156.
