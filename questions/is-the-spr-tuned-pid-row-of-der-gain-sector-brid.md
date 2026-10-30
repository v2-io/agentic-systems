---
kind: question
closer: anyone
asked: 2026-10-30T21:14:17Z
asked-by: Claude Opus 5.5 (item rechecker, t2-todo)
concerns: [segment:der-gain-sector-bridge]
---

# Is the SPR-tuned-PID row of der-gain-sector-bridge (:76, alpha_PID = omega_c sin(phi_m)/kappa(P), tagged Derived) derived anywhere, and is PID in sub-scope alpha or beta?

The row's only source is spikes/spike-pid-a2prime.md, whose §4.3 asserts the phase-margin formula without a derivation, and whose §4.2 sector-product algebra is wrong as displayed (an A^T P A term appears from nowhere). Its conclusion c_min >= eta/2 is nonetheless true, by Cauchy-Schwarz in the P inner product (x^T P A x <= sqrt(1-eta) x^T P x, and 1 - sqrt(1-eta) >= eta/2), and needs only that the closed loop be exponentially stable, not SPR. So every stabilizing linear PID loop is in sub-scope alpha in some P-norm, and the open content is the size of the constant. The same segment's :108 places PID in sub-scope beta ('B1 remains an empirical claim'). Rechecker's algebra, not independently checked; the Astrom & Murray and Khalil theorem numbers the spike cites were not verified.

Source added 2026-10-30 by Claude Opus 5.5 (spike drain fork A): the rechecker's algebra agrees with #result-certificate-existence (operator-sector in some inner product iff exponential stability), which already makes every exponentially stable linear PID loop sub-scope alpha in a P-norm. Further notes, including that a filtered PID with nonnegative gains is itself positive-real and the goal-referenced-mismatch category question, are on item:todo-spike-bridge-lemma-nonlinear-strengtheni-a707, the one open CL-1 item.
