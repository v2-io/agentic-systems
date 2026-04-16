---
slug: causal-information-yield
type: definition
status: exact
depends:
  - pearl-causal-hierarchy
  - action-selection
  - mismatch-signal
stage: deps-verified
---

# Definition: Causal Information Yield

Actions don't merely select among outcomes — they produce characteristically different outcome distributions depending on the causal structure. Causal information yield (CIY) quantifies the **action-distinguishability** of an action: how different its outcome distribution is from what alternative actions would produce.

## Formal Expression

*[Definition (causal-information-yield)]*

The **canonical CIY** of action $a$ given model state $M$:

$$\text{CIY}(a;\, M) = \mathbb{E}_{a' \sim q(\cdot \mid M)}\!\left[D_{\mathrm{KL}}\!\left(P(o \mid do(a), M) \,\Vert\, P(o \mid do(a'), M)\right)\right]$$

where $q(\cdot \mid M)$ is a reference distribution over comparator actions (uniform, policy-induced, or task-specific). This measures how strongly the action changes the interventional distribution of outcomes relative to alternatives.

$\text{CIY} \geq 0$ by construction (expectation of KL divergences). $\text{CIY} = 0$ for a passive observer or an agent whose actions don't affect outcome distributions. $\text{CIY} \gt 0$ when actions causally alter what is observed — exactly what distinguishes Level 2 from Level 1 epistemic access ( #pearl-causal-hierarchy).

## Epistemic Status

The CIY *definition* is well-grounded in causal inference theory. The quantity itself is standard — an expected KL divergence under the do-calculus. The interpretive claim — that CIY measures action-distinguishability rather than expected information gain — is exact (it follows from the definition). The relationship between CIY and learning value (see Discussion) is discussion-grade: the $\lambda$-weighted approximation to EIG is heuristic, not derived.

## Discussion

**CIY measures distinguishability, not learning value.** CIY as defined is the expected KL divergence between outcome distributions — how different the outcomes of $a$ are from the outcomes of typical alternatives. This is **action-distinguishability**, not **expected information gain** (EIG). The distinction matters: an action can have high CIY even when the agent already knows the outcome distributions perfectly (the distributions ARE different, but the agent learns nothing new by confirming what it already knows). High CIY is *necessary* for learning (indistinguishable actions can't teach anything) but not *sufficient* (distinguishable actions only teach when the agent is uncertain about the distinction).

The two quantities approximately coincide when $U_M$ is high — when the agent doesn't know the outcome distributions, high-CIY actions also have high EIG because observing a characteristically different outcome updates the agent's beliefs about the causal structure. They diverge when $U_M$ is low — a confident agent gains nothing from taking a distinguishable action it already understands.

The $\lambda(M_t)$ weighting in the unified policy objective ( #ciy-unified-objective) partially compensates: when $U_M$ is low, $\lambda \to 0$, suppressing the CIY term regardless of its magnitude. This makes the exploration term behave more like EIG — suppressing exploration when the agent is already certain. The compensation is heuristic (the $\lambda$ form is not derived). For the current theory, CIY serves as a tractable surrogate for EIG, with the $\lambda$ weighting providing the uncertainty-gating that makes the surrogate reasonable.

**Open direction: proper EIG within ACT.** Replacing CIY with a proper expected information gain quantity — $\text{EIG}(a; M) = I(o; \theta \mid do(a), M)$ where $\theta$ parameterizes the model — would be a stronger foundation for the exploration term, particularly in domains where the agent must decide between actions that are all highly distinguishable but differ in what they teach. Under certain scopes (intervention-rich domains with well-parameterized models), the EIG formulation might yield sharper exploration strategies — preferring actions that resolve the *most uncertain* causal links rather than the most distinguishable ones. Whether this yields operationally significant improvements over the $\lambda$-weighted CIY surrogate is an empirical question. The CIY formulation has the advantage of being computable from the agent's current model alone (it doesn't require reasoning about model uncertainty); EIG requires a meta-model of what the agent doesn't know.

**Dependence on the reference distribution $q$.** The quantitative CIY value depends on the choice of $q$, which is a significant degree of freedom. A uniform $q$ treats all alternatives equally; a policy-induced $q$ emphasizes alternatives the agent would consider. ACT adopts the policy-induced $q$ as default: $q(\cdot \mid M) = \pi(\cdot \mid M)$, yielding CIY as "how different is this action's outcome from what I'd typically see?" CIY values are not comparable across different $q$ choices.

**Query actions: accessing external models.** A qualitatively distinct class of actions: querying another agent's model. When a reliable source exists (expert, database, documentation, well-trained LLM), "ask a well-formed question" can yield information equivalent to thousands of probe-observe cycles. The source's model has already performed the compression work ( #information-bottleneck) — the response transfers the *output* of compression rather than requiring the agent to reconstruct it.

Key properties of query actions:
- **Information density**: Single well-targeted query can carry CIY orders of magnitude higher than individual environment probes
- **Trust-dependent gain**: Update from query depends on the agent's model of the source's reliability and alignment, not on observation channel noise ( #communication-gain)
- **Pre-compressed information**: Responses arrive already compressed in the source's representational framework, introducing a translation cost when frameworks don't align
- **Structural adaptation via external models**: Encountering another agent's model can trigger structural change ( #structural-adaptation-necessity) — incorporating external representational structure rather than building it de novo ("grafting")

When high-CIY query channels are available, the unified policy objective ( #ciy-unified-objective) favors query actions over direct probes, particularly when $U_M$ is high, a trusted source exists, query cost is low, and the needed information is about *structure* rather than the agent's specific situation.

**The adversarial mirror: deception and model corruption.** The same channel that enables cooperative knowledge transfer can be exploited to degrade the opponent's model. A deceptive response yields positive CIY in the strict information-theoretic sense, but the content drives model-reality mismatch *upward*. The update gain $\eta^\ast$ for the victim depends on trust; successful deception exploits high trust to inject a large, misdirected update. In the Lyapunov framework ( #sector-condition-stability), this is adversarial disturbance injected through the observation channel, with coupling coefficient $\gamma_A$ determined by the victim's trust level and exposure. See #communication-gain for the formal treatment of trust-dependent gain, and #adversarial-destabilization for the Lyapunov formalization. Distributed tempo, topology analysis, and game-theoretic integration are Section III content not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`).

**(Descended from TF-08.)**
