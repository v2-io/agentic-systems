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

Chapter 2 left us with a static picture. $M_t$ is the agent's compressed model of reality; sufficiency measures how much predictive content it retains; class fitness measures the ceiling within a representational class. None of that tells us how $M_t$ *moves* under events. Chapter 3 sets the cycle in motion.

The first two results fall out of a commitment we already made. We chose to call $M_t$ the agent's complete state — anything the agent remembers is in $M_t$, and the only way new information enters is through events. Under that completeness, two things follow immediately. The update from $M_{\tau^-}$ to $M_{\tau^+}$ depends on the prior model and the incoming event, and *nothing else* — the agent doesn't need to (and structurally cannot) re-process its entire history. And the agent's action depends on $M_t$ alone — the action is a function of what the agent currently believes, not directly of the history. Both feel obvious in hindsight; both are *derived*, not chosen.

The cycle's engine is the mismatch signal. The agent predicts an observation, the actual observation arrives, the gap between them is $\delta_t = o_t - \hat o_t$. Mismatch decomposes cleanly into two parts: the agent's model was wrong (reducible by better modeling) and the observation channel is noisy (irreducible — no amount of smarter modeling will eliminate sensor noise). There is a floor on prediction error set by the channel itself, and chasing below it amounts to fitting noise.

Given a mismatch, how much should the agent trust the new observation versus its prior model? The answer has a startlingly simple form:

$$\eta^\ast = \frac{U_M}{U_M + U_o}$$

— the optimal update gain weighted by the ratio of model uncertainty to total uncertainty. When the agent is highly uncertain about its model ($U_M$ large), gain approaches 1: trust the observation, you have little else to go on. When the agent is confident and the channel is noisy ($U_o$ large), gain approaches 0: trust your model, the observation isn't telling you much. For linear-Gaussian agents this is exactly the Kalman gain; for the rest of AAD's scope it is a robust qualitative result — any rational adaptive process must approximate this functional form, whether or not it explicitly computes the variance ratio.

Multiply gain by the rate at which observations arrive ($\nu$, the event rate), sum across the agent's channels, and you have adaptive tempo:

$$\mathcal T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$$

Tempo is the rate at which the agent turns observations into useful corrections — speed times quality. It is the chapter's central object and the load-bearing capacity variable for the rest of the framework. Every persistence threshold in Chapter 4 will have tempo on the left-hand side, and every adversarial-coupling result in Part III will depend on tempo ratios.

The chapter closes with the linear-correction ODE as a heuristic preview. Under linear correction and bounded environmental disturbance, the steady-state mismatch is

$$\Vert\delta\Vert_{ss} = \rho / \mathcal T$$

a ratio: how fast the world is changing, divided by how fast the agent corrects. Mismatch stays bounded when the agent corrects faster than reality drifts. This is the persistence condition in its simplest form; Chapter 4 generalizes it to nonlinear correction under the sector condition, where the result has the same shape.

Causal information yield (CIY, in #def-causal-information-yield) enters the chapter here because action-coupling is where causality first bites. CIY uses Pearl's $do(\cdot)$ notation — an external import (Pearl 2009; Bareinboim, Correa, Ibeling & Icard 2022; AAD's recapitulation lives at #def-pearl-causal-hierarchy in Part II Ch.2, where the framework deploys the hierarchy as machinery rather than referencing it as vocabulary). Its operational role in Chapter 3 is to score actions for their informational value to the cycle; Section II will lift CIY into a strategy-revision context.

The flow of the chapter: event-driven substrate ( #form-event-driven-dynamics) → recursion and action falling out of completeness ( #der-recursive-update, #der-action-selection) → mismatch and its decomposition ( #def-mismatch-signal, #result-mismatch-decomposition) → gain and CIY ( #emp-update-gain, #def-causal-information-yield) → tempo as the synthesis ( #def-adaptive-tempo) → linear ODE preview ( #hyp-mismatch-dynamics). The chapter ends with the central capacity variable and the preview of the persistence inequality that Chapter 4 generalizes.

## Working Notes

- This is a chapter-introduction segment; it bridges Chapter 2's static representation to Chapter 3's dynamic cycle. It carries no formal claim of its own.
- The "two derivations from completeness" framing identifies what Chapter 3's first segments are doing as a unit: #der-recursive-update and #der-action-selection are not independent results, they are joint consequences of #form-agent-model's completeness clause.
- The CIY-placement paragraph used to be apologetic, addressing what looked like a placement anomaly (CIY in Part I Ch.3 depending on the Pearl-hierarchy segment in Part I Ch.1). After the 2026-05-12 relocation of def-pearl-causal-hierarchy to Part II Ch.2 (recapitulation-of-external-result framing), the paragraph is declarative: CIY is in Ch.3 because action-coupling is where causality first bites; the do-notation is externally cited; the AAD recapitulation lives in Part II Ch.2 where the framework deploys the hierarchy operationally.
