---
slug: coupled-diagnostic-framework
type: result
status: conditional
depends:
  - coupled-update-dynamics
  - section-ii-survival
  - satisfaction-gap
  - control-regret
  - strategic-calibration
  - orient-cascade
  - observation-ambiguity-modulation
stage: draft
---

# Result: Coupled Diagnostic Framework

Even though the Class 2 agent's update does not decompose into sequential epistemic-then-strategic processing, the diagnostic quantities — satisfaction gap, control regret, and strategic calibration — can be computed *after* each coupled update. The orient cascade's sequential ordering, which is derived for Class 1 agents, becomes a normative decomposition procedure: the analyst (or the agent itself, in a reflective step) extracts diagnostic quantities from the coupled output and applies the 2x2 diagnostic table.

## Formal Expression

*[Derived (coupled-diagnostic, from post-hoc decomposability of diagnostic quantities)]*

### The coupled resolution process

The orient cascade for Class 1 agents ( #orient-cascade):

$$\delta_{\text{epistemic}} \to \delta_{\text{sat}} \to \delta_{\text{regret}} \to \delta_{\text{strategic}} \to O_t \text{ revision}$$

is replaced, for Class 2 agents, by:

**Step 1. Coupled update.**

$$X^{(\text{post})} = f_{\text{LLM}}(\text{prompt}(X^{(\text{pre})}, e_\tau))$$

The forward pass simultaneously updates beliefs and strategic assessments. There is no internal sequential cascade. The output $X^{(\text{post})} = (M^{(\text{post})}, G^{(\text{post})})$ is the post-update state, where the decomposition into $M$ and $G$ components is analytical, not architectural.

**Step 2. Post-hoc diagnostic extraction.**

From $X^{(\text{post})}$, compute:

$$\delta_{\text{sat}}^{(\text{post})} = V_{O_t}^{\min} - A_O(M^{(\text{post})};\, \Pi, N_h)$$

$$\delta_{\text{regret}}^{(\text{post})} = A_O(M^{(\text{post})};\, \Pi, N_h) - V_O(M^{(\text{post})}, \pi_{\text{current}};\, N_h)$$

These quantities are well-defined ( #satisfaction-gap, #control-regret survive exactly for Class 2 agents per #section-ii-survival). They are computed from the *post-update* state, which is goal-conditioned — $M^{(\text{post})}$ reflects the goals in the prompt. The definitions are exact; the diagnostic values incorporate whatever biases goal-conditioning introduced into $M^{(\text{post})}$.

**Step 3. Apply the 2x2 diagnostic table.**

| | $\delta_{\text{regret}} \approx 0$ | $\delta_{\text{regret}} \gg 0$ |
|---|---|---|
| $\delta_{\text{sat}} \leq 0$ | **Success**: goal attainable, policy near-optimal | **Strategy problem**: goal attainable, policy poor $\to$ revise $\Sigma_t$ |
| $\delta_{\text{sat}} \gt 0$ | **Capability limit**: best available policy insufficient | **Both**: strategy weak AND goal hard $\to$ revise $\Sigma_t$ first |

The table is identical to the Class 1 version ( #orient-cascade). What differs is the *provenance* of the inputs: for Class 1, the inputs come from a sequential cascade with guaranteed ordering; for Class 2, they come from a post-hoc decomposition of a coupled update.

**Step 4. Conditional follow-up.**

- If the diagnostic indicates **strategy revision** ($\delta_{\text{regret}} \gg 0$): initiate a second coupled update with attention directed to strategic alternatives. For an LLM agent, this means a follow-up reasoning step or prompt that explicitly requests strategy evaluation.
- If the diagnostic indicates **objective revision** ($\delta_{\text{sat}} \gt 0$ persisting across $\Sigma_t$ revision attempts): flag for explicit deliberation. The normative ordering — "do not revise $O_t$ until you have verified that $\Sigma_t$ improvement cannot close the gap" — is enforced as a design constraint, not derived from information dependency.

### Provenance of the diagnostic ordering

*[Discussion (ordering-as-design-principle)]*

For Class 1 agents, the cascade ordering is *derived*: you cannot evaluate strategy quality with an out-of-date reality model, because $M_t$ appears in the formulas for $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$. The information dependency forces the ordering.

For Class 2 agents, the logical dependency still holds — $\delta_{\text{sat}}$ still depends on $M_t$, and computing it from a stale $M_t$ is still meaningless. But the agent's processing does not enforce the dependency: the forward pass may evaluate strategic implications before adequately processing the epistemic content of the observation. The ordering transitions from a *derived consequence* to a *normative design pattern*:

$$\text{Class 1: ordering is forced by architecture} \qquad \text{Class 2: ordering is enforced by design}$$

The mechanisms for enforcement in Class 2 agents:
- **Structured reasoning templates** that separate epistemic update from strategic evaluation ("First, what did I learn? Then, what does it mean for my plan?")
- **Multi-step agent loops** where separate prompts handle observation processing and strategy evaluation
- **System-level monitoring** that detects when the agent's reasoning trace violates the cascade ordering

### Accuracy of post-hoc diagnostics

*[Derived (diagnostic-accuracy, conditional on observation-ambiguity-modulation)]*

The post-hoc diagnostics are computed from a goal-conditioned $M^{(\text{post})}$. Their accuracy relative to the "clean" (goal-blind) diagnostics depends on the epistemic bias $\Delta M_{\text{bias}}$ ( #section-ii-survival):

$$\lvert\delta_{\text{sat}}^{(\text{coupled})} - \delta_{\text{sat}}^{(\text{clean})}\rvert \leq L_A \cdot \lVert\Delta M_{\text{bias}}\rVert$$

$$\lvert\delta_{\text{regret}}^{(\text{coupled})} - \delta_{\text{regret}}^{(\text{clean})}\rvert \leq 2 L_A \cdot \lVert\Delta M_{\text{bias}}\rVert$$

where $L_A$ is the Lipschitz constant of the attainability function $A_O(\cdot; \Pi, N_h)$ with respect to $M_t$ (the factor of 2 for regret arises because it depends on both $A_O$ and $V_O$, each contributing $L_A$ sensitivity). The error is bounded by the epistemic bias, which in turn is bounded by $O(\kappa \cdot \text{ambiguity})$ per #observation-ambiguity-modulation.

**Consequence:** For low-ambiguity observations (test pass/fail, deployment success/failure, measurable metrics), the post-hoc diagnostics are accurate even for fully merged agents ($\kappa \approx 1$), because the epistemic bias from goal-conditioning is small when the observation's meaning is unambiguous. For high-ambiguity observations (code quality assessments, strategic evaluations, user feedback interpretation), the diagnostics may be systematically biased.

## Epistemic Status

*Conditional.* The post-hoc decomposability of diagnostic quantities is exact — $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ are well-defined mathematical objects computable from any $(M_t, G_t)$ regardless of how the state was produced. This is inherited from their survival classification in #section-ii-survival. The accuracy bounds are conditional on: (1) the Lipschitz regularity of $A_O$ with respect to $M_t$ (plausible for smooth value functions but not guaranteed in general), and (2) the epistemic bias structure from #section-ii-survival. The ordering-as-design-principle claim is discussion-grade — it is a normative recommendation, not a derived result.

Max attainable: conditional. The accuracy bounds require the Lipschitz constant $L_A$, which is domain-dependent and not computed by the theory.

## Discussion

**The diagnostic framework as the bridge.** This segment is the practical bridge between ACT's Section II machinery and logogenic agent engineering. The message: you can still use the 2x2 diagnostic table, the satisfaction gap, and control regret. What you lose is the guarantee that these quantities were computed in the right order from unbiased inputs. What you must add is: (a) an enforcement mechanism for the cascade ordering, and (b) awareness that the diagnostics may be biased by goal-conditioning, with bias proportional to observation ambiguity.

**Strategic calibration under coupling.** The edge residual ( #strategic-calibration) in the coupled formulation becomes:

$$r_{ij}^{(\text{coupled})} = \mathbb{E}[\Delta V_O \mid \text{edge traversed}, X_t] - \Delta V_O^{\text{observed}}$$

The conditioning on $X_t$ (rather than $M_t$ alone) means the residual measures calibration of the coupled $(M_t, \Sigma_t)$ system. It cannot cleanly separate "the causal model is wrong" from "the beliefs are biased by goals." The aggregate $\delta_{\text{strategic}}$ remains meaningful as a measure of "how well is the strategy working?" but the diagnostic power for *localizing* the source of miscalibration is degraded.

**Iterative refinement.** The coupled diagnostic framework naturally supports iterative refinement: after the initial coupled update and diagnostic extraction, the agent can re-process the situation with attention to specific diagnostic findings. Each iteration is a new coupled update with the diagnostic results as additional context. This iterative process converges toward the same endpoint as the sequential cascade — the difference is that convergence is empirical (dependent on the agent's reasoning quality) rather than guaranteed (by the cascade's information-dependency ordering). Formal convergence conditions for this iterative process are open.

## Working Notes

- The Lipschitz constant $L_A$ for the attainability function deserves characterization, at least for common objective types. For constraint-satisfaction objectives with smooth feasibility boundaries, $L_A$ should be computable. For utility-maximizing objectives, $L_A$ depends on the curvature of the value landscape around $M_t$.
- The "enforcement mechanisms" for cascade ordering (structured templates, multi-step loops, monitoring) are engineering prescriptions, not theory. The theory's contribution is identifying *what* must be enforced (the ordering) and *why* (information dependency), not *how* (that is architecture-specific).
- The iterative refinement process (repeated coupled updates with diagnostic feedback) resembles a fixed-point iteration. Its convergence properties — existence, uniqueness, rate — are open and would strengthen the result significantly. The coupled update may have multiple fixed points (the agent converges to different belief-strategy pairs depending on initialization); uniqueness conditions are needed for predictive power.
