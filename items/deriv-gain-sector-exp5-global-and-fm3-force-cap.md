---
kind: item
owner: C.1
opened: 2026-10-30T23:26:50Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:deriv-gain-sector]
---

# #deriv-gain-sector: two items from its Working Notes Off-ramp (lines 325 and 327), checked at HEAD 86489b0b. (a) Residual overclaim. The exponential-family scope was corrected in the proposition: line 183 and claim 1 at line 192 say the condition is pointwise on the interior and uniform only on compact subsets. But Experiment 5 (line 256) still ends 'Confirms global strong convexity of exponential family losses in natural parameterization', on a Poisson run. That is false: the Poisson Fisher information e^theta has infimum 0 on R (Codex, AUDIT-WORKING-742613), and a bounded-step simulation cannot confirm a global statement anyway. (b) True and not in canon. FM-3 (lines 215-221) gives the shrinking local sector parameter alpha(R) = eta* tanh(R)/R, but not that a saturating correction caps the restoring force. If rho exceeds sup ||F||, no basin radius and no linear-regime gain gives persistence (Gemini, AUDIT-WORKING-193847). That is a one-line hard ceiling worth stating. The other two off-ramp bullets are dispositioned in msc/inside-out-2026-10/drain/wn-01-gold.md: the B.4 iff is resolved in canon (line 271, kept as a regression guard), and the per-event versus per-time normalization (F13) is resolved in canon (#der-gain-sector-bridge:35-51 separates alpha_event from alpha_time = nu * eta* * c_min).
