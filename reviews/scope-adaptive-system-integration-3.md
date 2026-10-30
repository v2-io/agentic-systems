---
kind: review
author:
  name: Claude Opus 5.5 (A.1 integrator)
  role: integrator
sources:
  - spikes/epistemic-target-ontology/08-reread-integration.md
written: 2026-10-30T21:11:13Z
---

# 2026-10-30: rederive of segment:scope-adaptive-system

## C1 (check)
- target: segment:scope-adaptive-system
- act: rederive
- line: derivation
- criterion: (h')'s corrected counterexample: known law, state (t, x_t) with x_2 = x_1 and x_t fresh-uniform for t >= 3, o_2 = 1{x_2 in Q}, otherwise constant. Is nothing invariant (so theta is a point mass and Omega is infinite), and is the loop out at t = 1 under Lebesgue on x_1 and in under half Lebesgue plus half a dense atomic measure on the rationals, which has the same support?
- committed: after
- outcome: confirmed
- recheck: 08 section 1.2; the fresh draws make x_t and every function of it non-invariant; Lebesgue gives o_2 = 0 a.s., the mixture a fair coin determined by x_1
- at: 75565b20

