---
slug: satisfaction-gap
type: definition
status: exact
depends:
  - value-object
  - objective-functional
stage: claims-verified
---

# Definition: Satisfaction Gap

The satisfaction gap measures whether the agent's objective is achievable: the distance between what the objective requires and what the best available policy can deliver. It answers "is this goal feasible given what I know and what I can do?"

## Formal Expression

*[Definition (objective-attainability)]*

$$A_O(M_t;\, \Pi, N_h) = \sup_{\pi \in \Pi} V_O(M_t, \pi;\, N_h)$$

The **objective attainability** — the best achievable value given current beliefs $M_t$, available policy class $\Pi$, and horizon $N_h$.

*[Definition (satisfaction-gap)]*

$$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t;\, \Pi, N_h)$$

where $V_{O_t}^{\min}$ is the minimum trajectory value that counts as "objective met" — a threshold set by the objective itself (for constraints: all satisfied; for utility: a minimum acceptable level).

- $\delta_{\text{sat}} \gt 0$: The objective is **unmet** under the best available policy, current model, and horizon.
- $\delta_{\text{sat}} \leq 0$: The objective is **attainable** in principle.

**Disambiguation.** $\delta_{\text{sat}} \gt 0$ does NOT automatically mean the goal is wrong. It means the goal is unmet given $(M_t, \Pi, N_h)$. The positive signal has multiple possible causes:

| Cause | Fix | How to distinguish |
|---|---|---|
| Goal is genuinely infeasible | Revise $O_t$ | Persists across $M_t$, $\Pi$, $N_h$ improvements |
| Policy class too narrow | Expand $\Pi$ (structural adaptation of $\Sigma_t$) | $\delta_{\text{sat}}$ decreases when richer policies are tried |
| Horizon too short | Extend $N_h$ | $\delta_{\text{sat}}$ decreases with longer planning horizon |
| Model is wrong about feasibility | Improve $M_t$ (reduce $\delta_{\text{epistemic}}$) | $\delta_{\text{sat}}$ changes when $M_t$ is corrected |
| Objectives jointly infeasible | Revise $O_t$ or relax constraints | Individual terminal satisfaction gaps are zero but AND-node fails; cross-terminal tradeoff is required |

Objective revision is the **last resort**, not the first response to unmet goals. The orient cascade ( #orient-cascade) formalizes this ordering.

## Epistemic Status

*Exact as a definition — convention-relative as a diagnostic.* The satisfaction gap is a mathematical definition — the difference between a threshold and a supremum over a function class. The definition is precise; the *computation* of $A_O$ is generally intractable (it requires optimization over a policy class), but the quantity is well-defined. However, the *value* of $\delta_{\text{sat}}$ depends on three external parameters: the continuation convention ($\pi_{\text{cont}}$), the horizon ($N_h$), and the scalarization of the objective ($V_{O_t}$). These are not derived by ACT — they are choices the analyst makes. The satisfaction gap is therefore an intrinsic architectural diagnostic *given* a measurement convention, not an absolute property of the agent.

**Convention dependence.** $A_O$ inherits the continuation convention from the value object ( #value-object). Under the canonical default ($\pi_{\text{cont}} = \pi_{\text{current}}$), $A_O = \sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$ is the **best first-action attainability** — the supremum is over the first action only, with continuation fixed at $\pi_{\text{current}}$. This is a *one-step-improvement* quantity, not a full-policy optimum. Under the Bellman convention ($\pi_{\text{cont}} = \pi^\ast$), $A_O$ becomes the full-policy optimal value — a stronger but harder-to-compute quantity. The distinction matters: $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$ mean different things under different conventions, and analyses using different conventions should not be compared directly. ACT adopts the one-step improvement convention as the canonical default; all diagnostics are comparable across analyses of the same agent only when computed under the same convention.

## Discussion

**Why two gap measures, not one.** An earlier formulation used a single $\delta_{\text{objective}}$ for goal-related mismatch. This conflates two distinct situations: "the goal is too hard" and "the strategy is too weak." When the agent is optimally pursuing an infeasible goal, $\delta_{\text{objective}}$ is large but there's no strategy to improve — the problem is the goal, not the plan. The satisfaction gap ($\delta_{\text{sat}}$) and control regret ( #control-regret) separate these cases, enabling the right corrective action.

**The disambiguation table is load-bearing.** Without it, an agent facing $\delta_{\text{sat}} \gt 0$ might immediately revise its objective when the real problem is an inadequate model or a too-narrow policy class. The table encodes the diagnostic procedure: check $M_t$ adequacy first (maybe the goal IS feasible but the model doesn't know it), then check $\Pi$ and $N_h$, and only then consider revising $O_t$.

**Dependence on $M_t$.** $A_O$ is computed from $M_t$, not from the true environment state $\Omega_t$. The agent's assessment of attainability could be wrong — an achievable goal might look unachievable with a bad model, or vice versa. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's attainability assessment closer to reality. This is why the orient cascade puts epistemic update before attainability evaluation.

## Working Notes

- $V_{O_t}^{\min}$ (the satisfaction threshold) is a property of the objective, not of the agent. For constraint-satisfaction objectives, it's natural (all constraints met = satisfied). For utility-maximizing objectives, it's less obvious — what counts as "good enough"? This threshold may need to be explicitly modeled as part of $O_t$.
- The supremum in $A_O$ is over $\Pi$, the available policy class. For agents with explicit $\Sigma_t$, $\Pi$ corresponds to the set of strategies representable in the agent's DAG formalism. Expanding $\Pi$ (structural adaptation of $\Sigma_t$ — adding nodes, edges, or changing $\gamma$ assignments) is the purposeful analog of #structural-adaptation-necessity.
