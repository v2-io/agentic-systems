# Reflection: #def-causal-information-yield

**Stage:** deps-verified. **Status:** exact. **Type:** definition. **Depends:** [def-pearl-causal-hierarchy, der-action-selection, def-mismatch-signal].

## Dependency check

All upstream. ✓

## Predictions vs evidence

Predicted CIY as some interventional information rate. Got something more careful: $\text{CIY}(a; M) = \mathbb{E}_{a' \sim q}[D_{KL}(P(o \mid do(a), M) \| P(o \mid do(a'), M))]$, plus the explicit honest distinction that **CIY measures action-distinguishability, not learning value (EIG)**. The two coincide under high $U_M$, diverge under low $U_M$. The framework treats CIY as a surrogate for EIG with $\lambda$-weighted uncertainty-gating.

This is a *more nuanced* segment than I'd predicted, and the explicit naming of the surrogate role is exactly the form-shaping-for-verification discipline applied honestly.

## Cross-segment consistency

Forward-refs `#disc-ciy-unified-objective`, `#form-information-bottleneck`, `#hyp-communication-gain`, `#result-structural-adaptation-necessity`, `#result-sector-condition-stability`, `#der-adversarial-destabilization`.

**Two diff-voice instances in this segment:**
1. "(Descended from TF-08.)" — **ninth instance** of the pattern.
2. "Distributed tempo, topology analysis, and game-theoretic integration are Section III content not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`)" — **tenth instance**, this one referencing an `old-*` source file by name in Discussion. This is more pronounced diff-voice — explicitly admitting "not yet extracted from old material."

## Math verification

$\text{CIY}(a; M) \geq 0$ (expected KL, nonneg by construction). $= 0$ when all $P(o \mid do(a), M)$ are identical (action doesn't change interventional distribution). Standard.

The CIY-vs-EIG distinction is correct:
- CIY is *between-action* KL on intervention distributions (action distinguishability).
- EIG would be *agent-learning* MI: $I(o; \theta \mid do(a), M)$.
- They coincide under high $U_M$ because the agent learning from a distinguishable observation correlates with $U_M$ resolving.

The $\lambda(M_t) \to 0$ as $U_M \to 0$ heuristic (forward-ref to `#disc-ciy-unified-objective`) is the gating mechanism that makes CIY-as-surrogate-for-EIG behave correctly in low-uncertainty regimes.

## Status-label observation

The YAML `status: exact` applies to the CIY *definition* (which is exact). The Epistemic Status text correctly clarifies: "The relationship between CIY and learning value (see Discussion) is discussion-grade." So the segment carries *two* claims of different epistemic strengths:
- CIY definition itself: exact.
- CIY as exploration objective: heuristic (with $\lambda$-weighting).

Frontmatter `exact` reflects the definition's strength. A reader scanning frontmatter could miss the heuristic-grade application. **Mild candidate observation:** when downstream segments use CIY as the exploration objective, they should inherit the *heuristic* tier on that use, not the `exact` tier of the definition.

## What direction next

`#def-adaptive-tempo` per OUTLINE order.

## Errors to watch for

- The TF-XX pattern (now 10 instances). At this point I want to elevate this to a confirmed §B finding rather than a watch-item.
- Whether downstream segments that use CIY as exploration objective propagate the *heuristic* tier of that use, or inherit the segment-level `exact` label.

## Predictions for next segments

`#def-adaptive-tempo`: $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. Multi-channel sum; the central rate quantity in the persistence condition.

## What would I change

- Move both TF-lineage / old-* references to Working Notes.
- Consider whether the segment's title should be "Causal Information Yield (Action-Distinguishability)" so the naming is closer to what the substance is. The current name implies "yield = learning gain"; the segment goes to substantial trouble to clarify that this is *not* what CIY measures. The mismatch between name and substance is mildly misleading, even though the segment corrects it.

## Curious about

Whether the framework ever develops the proper EIG quantity within AAD. The "Open direction" paragraph names it as future work. If the framework's exploration objective is going to be load-bearing for §II's purposeful-agent machinery, replacing CIY with EIG (or proving they're equivalent under stated conditions) tightens the foundation.

## What new knowledge does this enable

- A *tractable* exploration-objective surrogate (CIY) with explicit gating to behave like EIG under uncertainty.
- The query-actions paragraph: external-model access ("ask a well-formed question") as a structurally distinct, high-CIY action class. This is structurally important for logogenic agents.
- The adversarial-mirror framing: deception as exploitation of high-CIY trust channels — formal substrate for deception-resistance work.

## Should the audit process change

No.

## Outline changes for FINAL

Promoting the TF-XX / old-* lineage pattern to a confirmed §B candidate finding (10 instances over 21 segments — clearly a pattern, not isolated hygiene).

## Felt value

**Mid-high magnitude.** The CIY-vs-EIG honest distinction is a place where the framework's epistemic care is visible. The query-actions paragraph and the adversarial-mirror paragraph are both structurally important for downstream consciousness-infrastructure work. The naming concern (CIY suggests "learning yield" but means "distinguishability") is a real mismatch between term and substance.

## What the framework now potentially contributes

The CIY-vs-EIG distinction sharpens what "exploration-driving information" actually means. Most agent-theoretic frameworks conflate these; AAD's separation lets the framework state precisely when CIY-driven exploration suffices and when EIG would be needed. The query-actions framing extends this to *information-from-other-models* — a class of actions that's quantitatively important for logogenic agents but typically treated informally elsewhere.

The adversarial-mirror framing — deception as the dual of cooperation through the same channel — is a structural insight that supports formal analysis of deception-resistance in agentic systems. The framework can in principle ask: "given trust level $\gamma$, what's the maximum disturbance an adversary can inject through a high-CIY channel?"

## Wandering thoughts

The query-actions paragraph is exactly the kind of structural insight the audit was supposed to surface. AAD's framework treats "asking a well-formed question" as a first-class action with quantitatively distinct properties (high CIY, trust-dependent gain, pre-compressed information, possible structural adaptation via grafting). Most agent frameworks treat queries as special cases of "actions"; AAD treats them as a structurally distinct action class.

For logogenic agents, this is load-bearing. An LLM agent's internal token-generation is mostly query actions of the "ask my own pretraining" form. Tool calls are query actions of the "ask an external system" form. Retrieval is query actions of the "ask a corpus" form. The framework's distinction between probe and query actions provides the structural substrate for analyzing how logogenic agents allocate their tempo across these different action types.

The adversarial-mirror paragraph is the formal substrate for "lying to an agent breaks its learning." Successful deception drives high CIY (the deceptive content is distinguishable from honest baseline), exploits high trust ($\gamma$ near 1), and injects a misdirected update. The Lyapunov-framework lift makes this measurable: at what trust level $\gamma$ does the disturbance from deception cross the persistence threshold? That's a *formal* question with implications for adversarial-robustness work.

A naming-brainstorm seed: "causal information yield" suggests "yield as in benefit/profit" which connotes learning. The segment makes clear this is *distinguishability*, not learning. A more accurate term might be "**action distinguishability**" or "**interventional contrast**" — but these are less catchy and CIY has been propagating. Possible compromise: keep CIY as the formal name, lean on "action-distinguishability" as the substantive gloss in any future Brief field. Currently the gloss is in Discussion; surfacing it more might help.

A meta-thought about the segment's status: this is a clean segment with two distinct findings I want to surface — the term-vs-substance naming concern and the TF-XX pattern. Both belong in the FINAL but at different severities.

Continuing to `#def-adaptive-tempo`.
