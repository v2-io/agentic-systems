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

— the optimal update gain weighted by the ratio of model uncertainty to total uncertainty. When the agent is highly uncertain about its model ($U_M$ large), gain approaches 1: trust the observation, you have little else to go on. When the agent is confident and the channel is noisy ($U_o$ large), gain approaches 0: trust your model, the observation isn't telling you much. For linear-Gaussian agents this is exactly the Kalman gain; for the rest of AAT's scope it is a robust qualitative result — any rational adaptive process must approximate this functional form, whether or not it explicitly computes the variance ratio.

Multiply gain by the rate at which observations arrive ($\nu$, the event rate), sum across the agent's channels, and you have adaptive tempo:

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$$

Tempo is the rate at which the agent turns observations into useful corrections — speed times quality. It is the chapter's central object and the load-bearing capacity variable for the rest of the framework. Every persistence threshold in Chapter 4 will have tempo on the left-hand side, and every adversarial-coupling result in Part III will depend on tempo ratios.

The chapter closes with the linear-correction ODE as a heuristic preview. Under linear correction and bounded environmental disturbance, the steady-state mismatch is

$$\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$$

a ratio: how fast the world is changing, divided by how fast the agent corrects. Mismatch stays bounded when the agent corrects faster than reality drifts. This is the persistence condition in its simplest form; Chapter 4 generalizes it to nonlinear correction under the sector condition, where the result has the same shape.

Causal information yield (CIY, in #def-causal-information-yield) enters the chapter here because action-coupling is where causality first bites. CIY uses Pearl's $do(\cdot)$ notation — an external import (Pearl 2009; Bareinboim, Correa, Ibeling & Icard 2022; AAT's recapitulation lives at #def-pearl-causal-hierarchy in Part II Ch.2, where the framework deploys the hierarchy as machinery rather than referencing it as vocabulary). Its operational role in Chapter 3 is to score actions for their informational value to the cycle; Part II will lift CIY into a strategy-revision context.

The flow of the chapter: event-driven substrate ( #form-event-driven-dynamics) → recursion and action falling out of completeness ( #der-recursive-update, #der-action-selection) → mismatch and its decomposition ( #def-mismatch-signal, #result-mismatch-decomposition) → gain and CIY ( #emp-update-gain, #def-causal-information-yield) → tempo as the synthesis ( #def-adaptive-tempo) → linear ODE preview ( #hyp-mismatch-dynamics). The chapter ends with the central capacity variable and the preview of the persistence inequality that Chapter 4 generalizes.

## Working Notes

- This is a chapter-introduction segment; it bridges Chapter 2's static representation to Chapter 3's dynamic cycle. It carries no formal claim of its own.
- The "two derivations from completeness" framing identifies what Chapter 3's first segments are doing as a unit: #der-recursive-update and #der-action-selection are not independent results, they are joint consequences of #form-agent-model's completeness clause.
- The CIY-placement paragraph used to be apologetic, addressing what looked like a placement anomaly (CIY in Part I Ch.3 depending on the Pearl-hierarchy segment in Part I Ch.1). After the 2026-05-12 relocation of def-pearl-causal-hierarchy to Part II Ch.2 (recapitulation-of-external-result framing), the paragraph is declarative: CIY is in Ch.3 because action-coupling is where causality first bites; the do-notation is externally cited; the AAT recapitulation lives in Part II Ch.2 where the framework deploys the hierarchy operationally.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal material — pedagogical framing, candidate figures, naming, reach — kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** only 4 of the 14 contributing audit dirs reached a digested reflection on this chapter-intro segment (384279, 472913, 526815, 773921); the per-segment dirs that began Section-I reading at the first content segment, and the batched dirs (451729 jumped from `#def-model-class-fitness` straight to `#form-event-driven-dynamics`), produced no intro reflection. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **The tempo-as-speed-times-quality gloss with the HFT counterexample** is the standout pedagogy — a curious reader could re-derive the chapter from it: "high-frequency trading with a garbage model ($\eta \approx 0$) has zero tempo, and slow human deliberation ($\nu$ low) requires very high gain ($\eta \approx 1$) to survive" (Claude, AUDIT-WORKING-773921). Pairs naturally with the steady-state hook "$\lVert\delta\rVert_{ss} = \rho/\mathcal{T}$ — drift divided by correction rate" as the chapter's one-line spine (same source).
- The left-to-right pipeline-with-feedback-loop framing: "event arrival $\to$ model update $\to$ prediction/mismatch $\to$ gain $\to$ tempo $\to$ persistence preview," with a single highlighted *capacity-synthesis point at tempo* (Claude, AUDIT-WORKING-526815). A compact verbal map of the next nine segments.

#### Candidate Discussion

- **The two-layer linear-ODE-as-pedagogy / sector-condition-as-rigor framing** is worth surfacing as the chapter's methodological stance: "the framework is naming where its pedagogy and its rigor diverge. The linear ODE is for reading; the sector condition is for proving" (Codex/Claude, AUDIT-WORKING-384279). The intro already commits to "linear ODE as preview, then generalize via sector condition in Ch.4"; this is a candidate sharpening of *why* that ordering is honest rather than loose.

#### Follow-up items

- **"Derived, not chosen" risks an unconditional reading.** The intro says of `#der-recursive-update` + `#der-action-selection`: "both are *derived*, not chosen" — but `#form-agent-model`'s completeness is itself a *formulation choice*. Two substrates flag that "derived from a formulation choice" is legitimate, but the bare "derived, not chosen" can read as unconditional inevitability; candidate one-clause tightening to "derived *given* the completeness formulation" (Claude, AUDIT-WORKING-472913 — set as a decisive downstream test; Claude, AUDIT-WORKING-526815 — "action as a function of $M_t$ alone may be too strong unless goal/objective state is already in $M_t$, which Part II separates as $G_t$").
- **Lift the Pearl-as-external-import convention upstream.** The intro is the *only* place the convention is articulated; a reader walking OUTLINE order meets $do(\cdot)$ in `scope-agency` before the convention is stated. Candidate: state it in FORMAT.md or at first use, not solely in this Ch.3 intro (Codex/Claude, AUDIT-WORKING-384279).

#### Readers often ask / wonder

- "Where does action-selection's dependence sit — on $M_t$ alone, or on the purposeful state too?" A reader meets "action depends on $M_t$" here and carries the question into Part II's $X_t = (M_t, G_t)$ lift; the intro could preview "complete agent state" rather than "$M_t$ alone" to preempt it (Claude, AUDIT-WORKING-526815).

#### Candidate figures

- **A sequential-process pipeline diagram** (not a static concept map): colored channel lanes $\to$ event stream $\to$ a rate/value bottleneck where $\nu$ and $\eta$ multiply $\to$ tempo, with the feedback loop closed and one node highlighted as the "capacity synthesis" point (Claude, AUDIT-WORKING-526815). Per the locked diagram conventions, this chapter-opening map would be a strong mental-model-first scaffold; reserve the chapter's load-bearing diagram budget for the mismatch/gain/tempo or persistence-preview segment rather than the intro (Claude, AUDIT-WORKING-472913).

#### Belongs elsewhere

- The math-preview verifications ($\eta^\ast = U_M/(U_M+U_o)$, $\mathcal{T} = \sum_k \nu^{(k)}\eta^{(k)\ast}$, $\lVert\delta\rVert_{ss} = \rho/\mathcal{T}$) and the "strong claim to grade downstream" note (the intro's "any rational adaptive process must approximate this functional form" framing of $\eta^\ast$) pertain to the segments that define those quantities (`#emp-update-gain`, `#def-adaptive-tempo`, `#hyp-mismatch-dynamics`), not to this intro (Codex/Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-472913).
