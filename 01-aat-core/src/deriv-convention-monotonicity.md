---
slug: deriv-convention-monotonicity
type: derivation
status: exact
depends:
  - def-value-object
stage: draft
---

# Derivation: Convention Monotonicity — the Receding-Horizon Rung

The convention hierarchy ( #def-value-object) orders three continuation conventions by their best-achievable value: $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$, for fixed model $M_t$, fixed policy class $\Pi$, fixed evaluated horizon $N_h$. This appendix carries the derivation of the two rungs, which differ in character. The **right rung** $A_O^{\text{RH}} \leq A_O^{\text{B}}$ is exact and unconditional — a one-line supremum-over-a-larger-set argument. The **left rung** $A_O^{(1)} \leq A_O^{\text{RH}}$ is *false in general*: an unguarded receding-horizon replanner over a window $N_r \lt N_h$ optimizes a *truncated* objective whose preference order can invert relative to the full evaluated objective, and it can then underperform the frozen current policy. The left rung holds **exactly** when the replanning objective is an *order-consistent surrogate* for the full-horizon objective; three structurally-checkable conditions each force this. The negative half is the standard receding-horizon / model-predictive-control fact that a short-horizon controller without a terminal cost or terminal constraint is not guaranteed to be monotone (or stabilizing); the positive half is rollout / one-step policy improvement and the control-Lyapunov terminal-cost construction.

## Formal Expression

Fix $M_t$, policy class $\Pi$, and evaluated horizon $N_h$. Recall the static-evaluation forms ( #def-value-object): $A_O^{(1)}$ scores the best first action under continuation $\pi_{\text{current}}$; $A_O^{\text{RH}}$ scores it under the receding-horizon continuation $\pi_{\text{RH}}$ with replanning window $N_r$; $A_O^{\text{B}}$ scores it under the Bellman-optimal continuation $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$. Stage values accrue over the evaluated horizon and $V_O$ is their expectation.

### The right rung is unconditional

*[Derived (convention-monotonicity-right-rung, from def-value-object)]*

$$A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h) \;\leq\; A_O^{\text{B}}(M_t;\, \Pi, N_h).$$

By definition $\pi^\ast$ maximizes $V_O(M_t, \cdot; N_h)$ over $\Pi$. The receding-horizon continuation $\pi_{\text{RH}}$ is drawn from $\Pi$, so $V_O(M_t, \pi_{\text{RH}}; N_h) \leq V_O(M_t, \pi^\ast; N_h)$. Taking the supremum over the first action preserves the inequality (the supremum of a function over a set is at least its value at any member). No condition on $N_r$ is needed. $\square$

### The left rung is conditional

*[Derived (Conditional on order-consistency of the replanning objective)]*

$$A_O^{(1)}(M_t;\, \Pi, N_h) \;\leq\; A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h)$$

holds exactly when the receding-horizon replanning objective is an **order-consistent surrogate** for the full-horizon objective: for every reachable state, the action $\pi_{\text{RH}}$ commits has full-$N_h$-horizon value at least that of the action $\pi_{\text{current}}$ would take. Under order-consistency, $\pi_{\text{RH}}$ weakly dominates $\pi_{\text{current}}$ pointwise on the full objective, so $V_O(M_t, \pi_{\text{RH}}; N_h) \geq V_O(M_t, \pi_{\text{current}}; N_h)$ at every reachable state; taking the supremum over the first action gives the rung. The naive justification — "$\pi_{\text{RH}} \succeq \pi_{\text{current}}$ because C2 optimizes where C1 holds fixed" — fails without order-consistency: C2 with window $N_r \lt N_h$ optimizes the *truncated* $N_r$-step objective, and "optimal for the truncated objective" does not imply "$\succeq \pi_{\text{current}}$ on the full objective."

Three named conditions each force order-consistency and are therefore each sufficient:

**(RH-1) Horizon alignment: $N_r \geq N_h$.** The replanning window covers the whole evaluated horizon, so C2's per-step optimization *is* full-horizon optimization from each reached state. By Bellman's principle of optimality the receding-horizon continuation then equals the optimal continuation, giving $A_O^{\text{RH}} = A_O^{\text{B}} \geq A_O^{(1)}$. This condition is degenerate by design: when $N_r \geq N_h$ the C2/C3 distinction collapses on the evaluated horizon, so it serves as a boundary marker, not as the operative condition for genuine $N_r \lt N_h$ replanning.

**(RH-2) Value-compared (improvement-checked) replanning — the operative condition.** C2 commits the replanned action only if its full-horizon value is at least that of continuing $\pi_{\text{current}}$; otherwise it keeps $\pi_{\text{current}}$. At each reachable state $s$ with $k$ steps remaining,

$$\pi_{\text{RH}}(s) \;:=\; \arg\max_{a \in \{a_{\text{replan}}(s),\; \pi_{\text{current}}(s)\}} \Big[\, r(s, a) + V_O\big(s'(s,a),\, \pi_{\text{current}};\, k-1\big) \,\Big],$$

i.e., each candidate first action is scored by *rollout under the base policy $\pi_{\text{current}}$* over the remaining full horizon. By construction $\pi_{\text{RH}}$ weakly dominates $\pi_{\text{current}}$ pointwise on the full objective, so $A_O^{(1)} \leq A_O^{\text{RH}}$. This is one-step policy improvement (rollout with base policy $\pi_{\text{current}}$), whose defining property is that the improved policy never underperforms its base policy. It is the natural AAT reading of C2 for strategy revision, since the orient cascade's purpose at step 4 ( #der-orient-cascade) is *improvement over the current strategy*: the monotonicity then follows from the improvement guard rather than from replanning per se.

**(RH-3) Terminal-cost / cost-to-go consistency — the general condition.** Equip the $N_r$-step replanning objective with a terminal value function $V_f$ at the truncation boundary satisfying both

$$V_f(s) \;\leq\; \max_{a} \big[\, r(s,a) + V_f(s') \,\big] \qquad \text{(control-Lyapunov / value-underestimator decrease inequality)},$$

$$V_f(s) \;\leq\; V_O\big(s,\, \pi_{\text{current}};\, \text{remaining horizon}\big) \qquad \text{(terminal cost lower-bounds the baseline tail)}.$$

The first inequality is the standard terminal-cost ingredient that makes the truncated-with-terminal-cost optimization a valid surrogate for the full-horizon objective. The second ensures the surrogate never undervalues the baseline tail, so the replanner never trades the baseline away for a truncation artifact. Together they force order-consistency, giving $A_O^{(1)} \leq A_O^{\text{RH}}$. Conditions (RH-1) and (RH-2) are special cases: (RH-1) is $V_f \equiv$ optimal tail with $N_r = N_h$; (RH-2) is $V_f = V_O(\cdot,\, \pi_{\text{current}};\, \cdot)$, the baseline cost-to-go itself.

### The counterexample

Absent any order-consistency condition the left rung fails. A deterministic two-state, two-action, two-step instance suffices. Evaluate continuations from a post-first-action state $x$ with evaluated horizon $N_h = 2$ continuation steps and replanning window $N_r = 1$; stage rewards lie on transitions and $V_O$ is their sum.

- At $x$, two admissible actions: $g$ ("greedy") gives immediate value $+1$ and transitions to a dead state $D$ (value $0$ thereafter); $p$ ("patient") gives immediate value $0$ and transitions to a high-value state $H$.
- At $H$: value $+10$ per step. At $D$: value $0$.
- $\pi_{\text{current}}$ is "patient at $x$" (action $p$).

Then:

- **C1 (frozen $\pi_{\text{current}}$):** $0$ at step 1 via $p$, then $+10$ at step 2 in $H$, so $A_O^{(1)} = 10$.
- **C2 ($N_r = 1$ replanning):** the one-step lookahead at $x$ prefers $g$ ($+1 \gt 0$), lands in $D$, collects $0$ at step 2, so $A_O^{\text{RH}} = 1$.
- **C3 (Bellman over $N_h = 2$):** picks $p$, value $10$, so $A_O^{\text{B}} = 10$.

Hence $A_O^{(1)} = 10 \gt A_O^{\text{RH}} = 1$: the left rung is violated, while the right rung ($1 \leq 10$) holds as derived. The myopic window optimizes a truncated objective whose order is *inverted* relative to the full objective — $+1$ now beats $+0$ now within the window, but $+0$ now then $+10$ later beats $+1$ now then $0$ later on the full horizon. This is precisely the situation C2 is reaching for ("a goal unattainable under frozen continuation may be reachable with replanning") and shows the reaching cuts both ways unless the replanning objective is order-consistent with the evaluated objective. The control case $N_r = N_h$ restores the rung (then $A_O^{\text{RH}} = A_O^{\text{B}} = 10$, condition (RH-1)); the value-compared guard (RH-2) and a baseline-lower-bounding terminal cost (RH-3) each likewise restore it to value $10$.

### Corollary orderings

The corollary $\delta$-orderings inherit the same split. With $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$ ( #def-satisfaction-gap) and $\delta_{\text{regret}}$ a difference of $A_O$ values ( #def-control-regret):

$$\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \qquad \text{and} \qquad \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}} \qquad \text{(unconditional, from the right rung)};$$

$$\delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)} \qquad \text{and} \qquad \delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \qquad \text{(conditional on order-consistency, RH-1/2/3)}.$$

## Epistemic Status

*Exact.* The right rung is exact and unconditional (supremum over a larger set). The left rung is exact under any one of the order-consistency conditions (RH-1), (RH-2), (RH-3) — each a closed-form sufficient condition — and the two-state counterexample is an exact demonstration that no unconditional left rung exists for genuine $N_r \lt N_h$ replanning. The failure is structural: it is objective-mismatch between the truncated $N_r$-step replanning objective and the evaluated $N_h$-horizon objective, not a pathology of a contrived instance. The conditions are standard receding-horizon results — (RH-1) is Bellman's principle of optimality; (RH-2) is rollout / one-step policy improvement; (RH-3) is the control-Lyapunov terminal-cost construction — applied to AAT's value-object setting; the elementary derivations above are self-contained and do not depend on any external citation. The corollary $\delta$-orderings inherit the unconditional/conditional split exactly.

## Discussion

**Why the left rung is the interesting one.** The hierarchy is usually read as "more planning is weakly better," and the right rung makes that precise for the step from receding-horizon to Bellman. The left rung — from frozen continuation to receding-horizon — is where the reading breaks: replanning is *not* automatically an improvement over standing pat. The reason is that a finite replanning window optimizes a different objective than the one the value is scored against, and a short window can be actively misled by near-term value. The standard remedy in receding-horizon control is exactly (RH-2)/(RH-3): guard the replanned action against the baseline, or carry a terminal cost that keeps the truncated objective honest about the tail. AAT's C2-for-strategy-revision reading inherits this: the orient cascade escalates to C2 *to improve on* $\pi_{\text{current}}$, and the improvement guard (RH-2) is what makes "escalate to C2" a monotone move rather than a gamble.

**Relation to the diagnostic direction.** The split does not disturb the C1-default diagnostic logic ( #def-value-object). C1 remains the most conservative diagnostic, and the locally-stuck-vs-genuinely-infeasible reading is unaffected: it rests on the C1/C3 endpoints and the right rung, not on the conditional left rung. What the split adds is a caution for deployments that escalate to C2 — unguarded short-horizon replanning is not guaranteed to dominate the frozen baseline, so a C2 diagnostic should use a window covering the horizon, a value-compared guard, or a control-Lyapunov terminal cost.

## Findings

### Convention monotonicity is a one-sided guarantee

**Claim.** Status: exact. In the convention hierarchy, the receding-horizon-to-Bellman rung ($A_O^{\text{RH}} \leq A_O^{\text{B}}$) is unconditional, but the one-step-to-receding-horizon rung ($A_O^{(1)} \leq A_O^{\text{RH}}$) is false in general and holds exactly under order-consistency of the replanning objective — forced by any of (RH-1) horizon alignment, (RH-2) a value-compared/rollout guard, or (RH-3) a baseline-lower-bounding control-Lyapunov terminal cost. A two-state, two-action, two-step counterexample exhibits an unguarded short-horizon replanner underperforming the frozen current policy.

**Brief.** More planning is not automatically better. Looking one move ahead and grabbing the action that looks best *right now* can be worse than just sticking with your current plan — the classic short-sighted trap (take the quick $+1$ into a dead end, miss the $+0$-now-then-$+10$-later path). It becomes reliably better only if you check the replanned move against simply continuing as you were (or carry an honest estimate of the long-run value past your planning window). Solving the whole problem optimally is always at least as good as the limited replanner — that direction never fails.

**Impact.** Sharpens the convention-hierarchy monotonicity ( #def-value-object) from an unconditional claim into a one-sided guarantee plus a named-condition characterization of the other side — a more useful and more honest statement, and a caution for any deployment that escalates to receding-horizon (C2) diagnostics: guard the replanning objective or the monotone-improvement reading does not hold.

**Antecedents.** *Formal antecedent.* Rollout / one-step policy improvement and limited-lookahead policies (Bertsekas, *Rollout, Policy Iteration, and Distributed Reinforcement Learning*, 2020; *Dynamic Programming and Optimal Control*, Vol. I) supply (RH-2); terminal-cost/terminal-set ingredients for receding-horizon stability (Rawlings, Mayne & Diehl, *Model Predictive Control: Theory, Computation, and Design*, 2nd ed., 2017, Ch. 2; Grüne & Pannek, *Nonlinear Model Predictive Control*, 2nd ed., 2017, Chs. 5–6) supply (RH-3). The non-monotonicity of unguarded short-horizon model-predictive control is the well-known phenomenon these ingredients exist to prevent.

**Related work.** Bertsekas (2020), *Rollout, Policy Iteration, and Distributed Reinforcement Learning* — formal antecedent; supplies the (RH-2) one-step-improvement guarantee that rollout never underperforms its base policy. Rawlings, Mayne & Diehl (2017), *Model Predictive Control*, 2nd ed. — formal antecedent; terminal-cost ingredients (RH-3) and the non-monotonicity of MPC without them. Grüne & Pannek (2017), *Nonlinear Model Predictive Control*, 2nd ed. — formal antecedent; stability without terminal constraints and the role of the prediction horizon. Status of all three: `intuition-only` pending a `relata` citation pass — the math here is elementary and self-contained, so the citations orient rather than back the derivation.

## Working Notes

- The reproducibility scripts for the counterexample and the two strengthenings live with the originating spike: `spikes/spike-value-object-convention-monotonicity-2026-05-30/sim-rh-counterexample.py` (the no-go counterexample and the $N_r = N_h$ control) and `sim-rh-strengthening.py` (the RH-2 value-compared guard and the RH-3 baseline-lower-bounding terminal cost, each restoring the rung on the same instance).
- External citations for (RH-1/2/3) are `intuition-only` until a `relata` pass lands them; the derivations are elementary dynamic programming and do not depend on the citation.
- **Documented dead-end (so a future agent does not re-attempt it):** there is no way to recover the unconditional left rung $A_O^{(1)} \leq A_O^{\text{RH}}$ for genuine $N_r \lt N_h$ replanning without an order-consistency condition. The failure is structural objective-mismatch and the two-state counterexample is minimal. The strengthening *is* the (RH-1/2/3) characterization; do not re-derive the rung as unconditional.
