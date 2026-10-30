---
kind: item
owner: C.4
opened: 2026-10-30T23:23:41Z
opened-by: Claude Opus 5.5 (spike drain lead)
concerns: [segment:impl-orient-cascade, segment:deriv-observation-ambiguity-bias-bound]
---

# Apply the epsilon-programme's telescoping-with-contraction mechanism (Theorem E3) to the open propagated-residual bound in #impl-orient-cascade's Working Notes (:77, 2026-05-31: 'a dedicated propagated-residual bound ... is an open strengthening, not attempted'). spikes/spike-epsilon-programme-2026-08-24/extension-cascade-residual-sketch.md does this at sketch tier. Within one cycle the propagation is a Lipschitz product, which is mechanical. Across cycles, a per-update bias b = C kappa I (#deriv-observation-ambiguity-bias-bound) and per-cycle contraction beta give cumulative displacement at most min(n b, b/(1-beta)), so the hypothesized steady state is C kappa I/(1-beta). The sketch names three gaps before this is a result, and the epsilon verifier (de-novo-feedback-1.md F8) judged the second one load-bearing: (1) derive beta < 1 for the cascade's epistemic map from canon (#result-contraction-template, the Fisher-gain segments) rather than assume it; (2) the norms differ, since b is stated in W_2/Fisher-Rao while the telescoping is a TV fact, so either contract in b's metric or carry the comparison losses; (3) an adversarial accumulator belief (beta -> 1) to confirm the blow-up is real. Strengthen first; land at the tier that survives, or record why it fails.

An open strengthening with a ready mechanism and named gaps, otherwise unowned. Drained 2026-10-30.
