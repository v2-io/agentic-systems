---
slug: the-reality-model-intro
type: discussion
status: discussion-grade
depends:
  - def-chronica
  - scope-adaptive-system
  - def-agent-environment
stage: draft
---

# Chapter Introduction: The Reality Model

Having named the objects of the agent–environment coupling and bounded what AAT applies to, we turn to what the agent maintains internally: a compressed model of reality, with measurable adequacy against the chronica it was constructed from.

An agent navigating uncertainty cannot see the world directly. Whatever it knows about reality, it built from its history of partial observations — the chronica $\mathcal{C}_t$. Carrying that history around in raw form is infeasible at any scale that matters; finite agents compress, and we want to talk about what they end up with. So we commit to writing the agent's state as $M_t = \phi(\mathcal{C}_t)$ — a function of history, condensed into something the agent can work with. Every downstream result in AAT — gain, tempo, persistence, structural adaptation — operates on this $M_t$.

The first useful question to ask of a given compression is how good it is. Sufficiency $S(M_t)$ measures the fraction of the chronica's predictive content that survives: $S = 1$ means the agent has lost nothing by compressing; $S \lt 1$ means it has lost something it might have used. The optimal compression for a given purpose — keep what predicts the future, discard what doesn't — is what Tishby's information bottleneck characterizes, and we adopt that framing directly.

The deeper question is what the agent *could* hold in the best case. There is a ceiling — the highest sufficiency any model in the agent's current representational class can reach. Call it $\mathcal{F}(\mathcal{M})$, model-class fitness. When fitness is high, the agent can keep improving by tuning within the class. When fitness is low, no amount of better tuning helps. The agent is using the wrong *kind* of model for its world, and the remedy is not a better instance of the same model — it is a different class entirely.

That last point is the seed of one of the framework's central results. Class fitness is named statically here, where the model is treated as a frozen object. Chapter 4 will use it to derive *structural adaptation necessity*: when the class is inadequate, the agent must change classes, not parameters, because the mismatch floor that parametric updates cannot get below is set by this ceiling. The trigger lives in this chapter; the consequence unfolds in Chapter 4.

The four segments that follow develop this in order. #form-agent-model commits to the compressed-state representation and the completeness assumption — anything not in $M_t$ is lost to the agent, by construction. #form-information-bottleneck applies Tishby's framework to characterize optimal compression for an agent whose target is future observations. #def-model-sufficiency turns "how much was retained" into a measurable ratio. #def-model-class-fitness lifts the question from a specific model to the best the whole class can reach.

## Working Notes

- This is a chapter-introduction segment; its job is to bridge Chapter 1's ontology/scope/causal-structure setup to Chapter 2's representation choice and frame what follows. It carries no formal claim of its own.
- The "ceiling that's low means you need a different class" framing is the centerpiece; the structural-adaptation result that grows from it is the load-bearing connection to Chapter 4. Other framings considered (IB Lagrangian as opening, sufficiency as opening) bury the lede.
- The depends list is light by design — this is a bridge segment, not a derivation, so it does not carry the structural load that a depends entry would normally signal.
