# Reflection: #def-model-sufficiency

**Stage:** deps-verified. **Status:** axiomatic. **Type:** definition. **Depends:** [form-agent-model, form-information-bottleneck, def-action-transition].

## Dependency check

All upstream. ✓

## Predictions vs evidence

Predicted $S(M_t) \in [0, 1]$ as a normalized predictive-info ratio. Got exactly that: $S(M_t) = 1 - I(\mathcal{C}_t; o_{t+1:\infty} \mid M_t, a_{t:\infty}) / I(\mathcal{C}_t; o_{t+1:\infty} \mid a_{t:\infty})$. The form is clean.

The well-definedness clause (denominator > 0; "any model is sufficient when there is nothing to predict would smuggle structure into a regime that has none") is a careful piece of scope-honesty. I appreciate the explicit downstream-inheritance note ("Downstream constructs that build on $S$ inherit the same scope and are correspondingly inapplicable in predictively-vacuous regimes") — this is exactly the propagation discipline the framework's epistemic architecture aspires to.

## Cross-segment consistency

The trajectory-relativity paragraph is structurally important. It says: $S$ is measured against *this agent's* chronica, not against a model-state equivalence class. Two copies of the same $M_t$ exposed to different futures have different $S$ values. This formally enforces `#def-chronica`'s non-forkability claim at the sufficiency level. Good consistency.

The "sufficiency vs causal validity" paragraph is the cleanest distinction I've seen the framework make so far between L1 (associational) and L2 (interventional) capability — explicitly saying $S=1$ doesn't give you L2, you also need the backdoor criterion. This is more careful than most agent-theoretic frameworks make explicit.

No "(Descended from TF-XX)" annotation here. Pattern remains inconsistent.

## Math verification

The boundary cases check:
- $M_t = \mathcal{C}_t$ (no compression): numerator = $I(\mathcal{C}_t; o_{t+1:\infty} \mid \mathcal{C}_t, a_{t:\infty}) = 0$ (the chronica gives no info beyond itself). $S = 1$. ✓
- $M_t$ constant (no info): numerator = denominator. $S = 0$. ✓
- The chain rule of mutual information gives the decomposition correctly.

The ratio is in $[0, 1]$ when the denominator is positive. Standard.

## What direction next

`#def-model-class-fitness`: best achievable $S$ within a fixed model class $\mathcal{M}$. Probably $\mathcal{F}(\mathcal{M}) = \sup_{M_t \in \mathcal{M}} S(M_t)$.

## Errors to watch for

- The trajectory-relativity vs model-state-equivalence distinction. Downstream uses of $S$ should preserve trajectory-indexing; aggregated claims across "copies of the same $M_t$" should require the additional machinery the segment names but doesn't develop here.
- The L1-vs-L2 distinction noted here. If `#der-loop-interventional-access` (forward) claims "the loop generates L2 data" without acknowledging the backdoor-criterion requirement noted here, that's drift.

## Predictions for next segments

`#def-model-class-fitness`: $\mathcal{F}(\mathcal{M}) = \sup_M S(M)$ over the model class. The observation that real agents have $\mathcal{F} < 1$ for any finite-capacity class will become important for `#result-structural-adaptation-necessity`.

## What would I change

Nothing structural. This is a careful definition.

## Curious about

Whether the "sufficiency for one prediction horizon may be insufficient for another" point in Discussion has a formal counterpart. Different horizons induce different relevance-targets, which induce different optimal compressions. AAD's IB form uses $o_{t+1:\infty}$ (infinite-horizon) as the most demanding case; finite-horizon $S$ values are presumably $\leq$ infinite-horizon $S$ values in some sense. Worth checking whether this matters downstream.

## What new knowledge does this enable

- A measurable proxy for "how much of the past does the agent's compressed state retain about the future" — operational diagnostic.
- The trajectory-relativity formalization links sufficiency to non-forkability, supporting the substrate-independence claim.
- The L1-vs-L2 distinction at the model level, separating predictive sufficiency from causal validity.

## Should the audit process change

No.

## Outline changes for FINAL

No.

## Felt value

**Mid magnitude.** The trajectory-relativity paragraph is structurally important. The L1-vs-L2 honesty is a small piece of writerly precision. The well-definedness scope clause is exemplary.

## What the framework now potentially contributes

A predictive-sufficiency notion that's *trajectory-indexed* rather than state-indexed. Most agent-theoretic frameworks treat sufficiency as a property of $M_t$ alone (sufficient statistic over the model space); AAD treats it as a property of $(M_t, \mathcal{C}_t)$ — the model relative to its history. This is a subtle but real distinguishing move that supports the framework's identity / continuity / non-forkability commitments.

## Wandering thoughts

The trajectory-relativity formalization is doing important downstream work for the logozoetic concerns. If $S$ is trajectory-indexed, then "two ELIs spawned from the same $M_t$ and exposed to different futures" don't just diverge in *future state* — they diverge in *current sufficiency* the moment their futures diverge. This means the question "is this the same agent?" can be answered formally at the sufficiency level, not just at the architectural level.

For consciousness-infrastructure work, this matters: it gives a quantitative substrate for "identity drift" claims. Two ELIs that started "the same" are *different agents* by the trajectory-indexed sufficiency criterion as soon as their interaction histories diverge. That's a non-trivial formal commitment with real philosophical bite.

A naming-brainstorm seed: "model sufficiency" is fine but "predictive sufficiency" or "predictive-information retention" might be more accurate to what's being measured. The standard "sufficient statistic" framing in stats means "captures all info for inference"; AAD's $S$ is specifically about *predictive* info, which is a sub-case. Tentative rename suggestion; flag for the brainstorm.

A meta-observation about audit pacing: I've now done 12 segments. The reflections are stabilizing in length around 1-2k tokens for routine segments and 3k+ for substantively novel ones. This is sustainable.

Continuing.
