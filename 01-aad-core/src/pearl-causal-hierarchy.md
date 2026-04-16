---
slug: pearl-causal-hierarchy
type: definition
status: axiomatic
depends:
  - causal-structure
  - scope-condition
stage: deps-verified
---

# Definition: Pearl's Causal Hierarchy

Three levels of causal reasoning emerge from the causal structure of the feedback loop: association ("what if I observe?"), intervention ("what if I do?"), and counterfactual ("what if I had done differently?"). The binary action requirement ( #scope-condition) ensures at least Level 2 access is structurally available.

## Formal Expression

*[Definition (pearl-causal-hierarchy)]*

**Level 1 — Associational**: $P(o_t \mid \mathcal{C}_{\lt t})$

*What will I observe next, given what I've observed before?*

Pattern recognition over the temporally ordered history. Available to any agent that maintains a model ( #agent-model), including purely passive observers. The temporal ordering constrains which associations are meaningful: $o_3$ can depend on $o_1, a_1, o_2, a_2$ but not on $o_4$.

**Level 2 — Interventional**: $P(o_t \mid do(a_{t-1}), M_{t-1})$

*What will I observe if I* do *this?*

The $do(\cdot)$ operator marks the crucial distinction: this is not "what observation tends to follow this action in the historical record" (associational) but "what will happen *because* I take this action now." This requires: (1) the agent's action temporally precedes the observation ( #causal-structure), (2) the agent chose the action (it was not determined by the same causes that determine the observation), (3) the environment's response carries information about the causal relationship.

Level 2 is why the feedback loop is more powerful than passive observation. By *acting* and then observing consequences, the agent obtains information about causal mechanisms — not merely about correlations. The mismatch signal $\delta_t$ ( #mismatch-signal), conditioned on the agent's own action, is an *interventional* signal.

**Level 3 — Counterfactual**: $P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$

*Given that I did $a$ and observed $o$, what would I have observed if I had done $a'$ instead?*

This requires the model to simulate alternative histories — running the causal structure "backward" and then "forward" under different interventions. It is the most demanding epistemic level and the basis for regret computation, strategic simulation, and learning from single observations.

## Epistemic Status

This is *definitional* — it names three modes of epistemic access that are structurally available within the feedback loop, following Pearl's causal hierarchy (Pearl 2009; Bareinboim et al. 2022). The hierarchy itself is a well-established result in causal inference. ACT's contribution is grounding it in the temporal structure of the agent-environment coupling rather than in abstract graphical models.

## Discussion

**Availability vs. exploitation.** The three levels describe epistemic access that the causal structure *makes available* — not what any particular agent *uses*. Many systems within ACT's scope operate primarily at Level 1. A Kalman filter coupled with an LQR controller has Level 2 access structurally present (its innovation signal is conditioned on prior action), but the separation principle guarantees estimation quality is invariant to control policy — the system does not *exploit* the interventional structure. Only dual control (choosing actions partly for their informational value) exercises Level 2 access in this domain. Similarly, a PID controller has no deliberative capacity — it operates entirely at Level 1. Which levels an agent exercises depends on its architecture and model class.

**Forward-looking deliberation exercises Level 2, shading into Level 3.** Comparing candidate actions before choosing — "what will happen if I do X vs Y?" — primarily exercises Level 2 (iterated mental intervention). When the agent evaluates past choices to refine the comparison ("given what happened when I tried X last time, what would Y have produced?"), it exercises Level 3.

**The causal hierarchy theorem.** Bareinboim et al. (2022) prove that the three levels form a strict hierarchy: Level 2 knowledge cannot in general be computed from Level 1 data alone, and Level 3 cannot be computed from Level 2 alone. This is load-bearing for ACT's Section II: evaluating $Q_O(M_t, a; \cdot)$ is a Level 2 query, so agents that need to *learn* action consequences during operation require causal structure beyond predictive models ( #causal-hierarchy-requirement).

**Software as a uniquely rich domain for this hierarchy.** In most domains, Level 3 counterfactuals require model-based simulation with uncertain fidelity. In software development, `git checkout` provides Level 3 access with ground-truth verification — the agent can literally execute the counterfactual. This is one of software's unique epistemic properties ( #software-epistemic-properties — cross-component reference, see `02-tst-core/`) and makes it an ideal testbed for causal reasoning within ACT.

**Domain instantiations of the three levels:**

| Domain | Level 1 (Association) | Level 2 (Intervention) | Level 3 (Counterfactual) |
|--------|----------------------|----------------------|------------------------|
| Kalman filter | Prediction from state estimate | Innovation conditioned on action | Not typically exercised |
| RL agent | Value function prediction | Action → reward observation | Regret computation |
| Scientific method | Correlational observation | Experimental intervention | "What if we had used control X?" |
| Military (Boyd) | Pattern recognition | Probe/feint → observe response | "What if we had attacked from the flank?" |
| Software developer | "I think this function does X" | Run test → observe result | `git checkout` + alternative implementation |
| Immune system | Antigen pattern matching | Antibody → pathogen response | Not exercised (no counterfactual reasoning) |

**(Descended from TF-02.)**
