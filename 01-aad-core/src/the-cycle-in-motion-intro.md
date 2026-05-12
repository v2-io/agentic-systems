---
slug: the-cycle-in-motion-intro
type: discussion
status: discussion-grade
depends:
  - form-agent-model
  - def-model-sufficiency
  - def-model-class-fitness
stage: draft
---

# Chapter Introduction: The Cycle in Motion

The model exists; events arrive; the agent corrects. This chapter develops the dynamics of the adaptive cycle as it actually runs — how state updates from events, what the mismatch signal is, how the optimal weight on each observation depends on uncertainty, and what total corrective capacity emerges at the cycle level.

## Formal Expression

*[Discussion]*

This segment is a chapter-introduction bridge. It carries no formal claim of its own; the chapter's substantive content lives in the nine segments below developing the event-driven substrate, the recursive update form, action selection, the mismatch signal and its decomposition, update gain, causal information yield, adaptive tempo, and the linear mismatch ODE as preview of the persistence chapter that follows.

## Epistemic Status

*Discussion-grade.* Framing for what follows, not a derivation.

## Discussion

Chapter 2 made the agent's representation static. $M_t = \phi(\mathcal C_t)$ is the compressed history ( #form-agent-model); sufficiency $S(M_t)$ measures retention against the prediction task ( #def-model-sufficiency); class fitness $\mathcal F(\mathcal M)$ measures the ceiling that any model in the current class can reach ( #def-model-class-fitness). The static structure is enough to *name* what can fail (low class fitness forces structural adaptation), but it is silent on how $M_t$ actually moves under events. Chapter 3 sets the cycle in motion.

**Two derivations that follow from completeness.** The first non-trivial moves in this chapter are derived from a single architectural commitment — that $M_t$ is the complete state, in the sense of #form-agent-model's completeness clause. Under completeness, two consequences follow directly: the update form must be recursive ( #der-recursive-update — $M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$, no $\mathcal C_t$ argument), and action must depend on $M_t$ alone ( #der-action-selection — $a_t = \pi(M_t)$). These are *derivations*, not formulations: the alternatives require breaking the completeness commitment, which has its own analytical cost (the rest of the theory would have to be re-stated in terms of $\mathcal C_t$ directly). Both will lift cleanly to Section II under the same argument applied to the purposeful state $X_t = (M_t, G_t)$ — this is what makes the Section I machinery transfer across the lift.

**The signal that drives everything else.** The mismatch signal $\delta_t = o_t - \hat o_t$ ( #def-mismatch-signal) is what makes the cycle adaptive. Its decomposition into reducible model error and irreducible observation noise ( #result-mismatch-decomposition) names the structural limit of what *any* agent can do with a given observation channel: the noise floor cannot be improved by better modeling, only by improving the channel itself. Update gain $\eta^\ast = U_M/(U_M + U_o)$ ( #emp-update-gain) is the optimal weight on the mismatch signal — exact for linear-Gaussian and conjugate-Bayesian agents, robust-qualitative for the rest. The two together — what mismatch decomposes into and how much weight the agent should put on it — close the corrective phase of the cycle.

**Tempo as the integrated rate.** Adaptive tempo $\mathcal T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ ( #def-adaptive-tempo) is the chapter's central quantity. It integrates loop speed (event rate $\nu$) and corrective quality (gain $\eta^\ast$) into a single rate of useful information acquisition. Tempo appears on the left-hand side of every persistence threshold in Chapter 4 and every adversarial-coupling result in Part III — it is the load-bearing capacity variable for the rest of the framework. The chapter closes with #hyp-mismatch-dynamics, the linear-correction ODE that makes the central inequality visible in its simplest form: $\Vert\delta\Vert_{ss} = \rho/\mathcal T$, the steady-state mismatch as the ratio of disturbance rate to adaptive tempo. Chapter 4 generalizes this to nonlinear correction under the sector condition.

**Why causal information yield sits in this chapter rather than Section II.** CIY ( #def-causal-information-yield) measures how distinguishable an action's outcome distribution is from alternatives — a Level-2 quantity in Pearl's hierarchy, which is why CIY's `depends:` list pulls #def-pearl-causal-hierarchy forward from Chapter 1. CIY's operational role, though, is here in Chapter 3: it modulates the cycle's exploration component by scoring actions for their informational content. The placement reflects an architectural commitment — causality enters the dynamic cycle through action selection and observation generation, not through the static representation. Section II will lift this into a strategy-revision context; Chapter 3 establishes the per-action quantity first.

**The flow of the chapter.** Event-driven substrate ( #form-event-driven-dynamics) → completeness-derived recursion and action ( #der-recursive-update, #der-action-selection) → mismatch and its decomposition ( #def-mismatch-signal, #result-mismatch-decomposition) → gain and CIY ( #emp-update-gain, #def-causal-information-yield) → tempo as synthesis ( #def-adaptive-tempo) → linear ODE preview ( #hyp-mismatch-dynamics). By chapter end the reader has the central capacity variable ($\mathcal T$) and the preview of the steady-state inequality that becomes the persistence condition in Chapter 4.

## Working Notes

- This is a chapter-introduction Discussion segment; it bridges Chapter 2's static representation to Chapter 3's dynamic cycle. The Formal Expression is intentionally empty.
- The "two derivations from completeness" framing identifies what Chapter 3's first segments are doing as a *unit*: #der-recursive-update and #der-action-selection are not independent results, they are joint consequences of #form-agent-model's completeness clause. Surfacing this pedagogically helps the reader see why both are derivations rather than formulations.
- The mismatch-signal / decomposition / gain triad is the load-bearing structure of the chapter's middle; tempo is its synthesis; the linear ODE is the bridge to Chapter 4. This is the structural skeleton the intro is preserving in prose.
- The CIY-placement paragraph addresses what could otherwise read as a placement anomaly. The depends-list pulls Pearl forward from Chapter 1, which is a real cross-chapter dependency, but the operational role is here. Naming this explicitly prevents the reader from wondering why a Level-2 quantity appears before Section II's purposeful-agent machinery.
