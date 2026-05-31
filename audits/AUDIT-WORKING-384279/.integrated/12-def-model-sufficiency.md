# 12 — def-model-sufficiency

*Type: definition. Status: axiomatic. Stage: deps-verified. Depends: [form-agent-model, form-information-bottleneck, def-action-transition].*

## Predictions vs evidence
Predicted: $S(M_t) \in [0, 1]$ predictive-information ratio. Found: exactly that — $S(M_t) = 1 - \frac{I(\mathcal{C}_t; o_{t+1:\infty} \mid M_t, a_{t:\infty})}{I(\mathcal{C}_t; o_{t+1:\infty} \mid a_{t:\infty})}$.

## Math verification
- $S = 1$: numerator = 0 (no extra info in $\mathcal{C}_t$ given $M_t$, i.e., $M_t$ sufficient statistic) → ratio = 0 → $S=1$. ✓
- $S = 0$: numerator = denominator (model useless, all info still in $\mathcal{C}_t$) → ratio = 1 → $S=0$. ✓
- Conditional MI is non-negative, and adding $M_t$ to conditioning can only reduce or preserve MI (data processing), so $0 \leq \text{num} \leq \text{denom}$ → $S \in [0, 1]$. ✓
- Well-definedness clause: denominator > 0. Addressed correctly. ✓

## Prose-coherence
Clean. Five sub-points in Discussion (task / accuracy distinction / not-causal / policy-relative / trajectory-relative) are all substantive and non-redundant. The "sufficiency ≠ accuracy" distinction is methodologically important — a model can be a perfect sufficient statistic of biased data and still produce wrong predictions; sufficiency tracks information retention, not truth.

## Cross-segment consistency
Forward-refs `#def-mismatch-signal`, `#def-value-object`, `#der-causal-hierarchy-requirement`, `#def-model-class-fitness`, `#result-structural-adaptation-necessity`, `#scope-agent-identity`. Trajectory-relativity (line 49) links cleanly back to the non-forkability claim in def-chronica + scope-agent-identity.

## Watch list
- The "sufficiency does not imply causal validity" caveat (line 45) requires the backdoor criterion via `#def-value-object`. Need to verify when I reach that segment that the backdoor connection is made explicit.
- The policy-relativity argument (line 47) is consistent with the IB segment's policy-relativity argument (line 48 of form-information-bottleneck). Cross-segment coherence is good.

## Next-segment predictions
`#def-model-class-fitness`. Will introduce $\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M_t \mid \text{...})$ or similar — the best achievable sufficiency within the class. Will reference structural-adaptation-necessity.

## What I'd change
Nothing substantive. The "sufficiency ≠ accuracy" / "predictive ≠ causal" / "policy-relative" / "trajectory-relative" axes are all flagged carefully. Strong.

## Wandering thoughts (brief)

**On the predictive-not-causal caveat (line 45).** This is a small but load-bearing point. A reader who isn't careful might think "if the model has S=1, it has all the predictive info — therefore it can do interventional queries." That's wrong, and the segment names the wrong reasoning explicitly. Naming wrong reasoning prevents future bugs at the cost of dense prose. The right call for a framework that cares about Level 2 validity.
