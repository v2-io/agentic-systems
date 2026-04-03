---
slug: edge-update-via-gain
type: hypothesis
status: discussion-grade
depends:
  - strategy-dag
  - update-gain
  - mismatch-signal
stage: draft
---

# Hypothesis: Edge Update via Gain

The uncertainty-ratio gain principle ( #update-gain) extends from epistemic updates to strategy-edge updates: edge credences revise in proportion to the ratio of edge uncertainty to observation noise. This gives a principled, conservative update rule that avoids overreacting to single observations.

## Formal Expression

*[Hypothesis (edge-update-via-gain)]*

Edge credences update via:

$$p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot \left(\text{signal}(o_t, i, j) - p_{ij}^{\text{old}}\right)$$

where:
- $\text{signal}(o_t, i, j) \in [0, 1]$: evidential content of observation $o_t$ about the causal link $i \to j$
- $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$: update gain

with:
- $U_{\text{edge}}$: uncertainty about this specific causal link. If $p_{ij} \sim \text{Beta}(\alpha_{ij}, \beta_{ij})$: $U_{\text{edge}} = \text{Var}[\text{Beta}] = \alpha\beta / ((\alpha + \beta)^2(\alpha + \beta + 1))$
- $U_{\text{obs}}$: observation noise on the channel confirming this link. $U_{\text{obs}} \propto 1/\sigma_j$ (inverse of observability of node $j$)

**Beta-Bernoulli equivalence.** For binary observations (success/failure of step $j$):
- Observe success: $\alpha_{ij} \to \alpha_{ij} + 1$
- Observe failure: $\beta_{ij} \to \beta_{ij} + 1$
- Point estimate: $p_{ij} = \alpha / (\alpha + \beta)$

This is the standard Bayesian update for a Bernoulli process — the gain principle reduces to conjugate updating in the binary case.

## Epistemic Status

*Hypothesis.* The extension of the gain principle from $M_t$ to $\Sigma_t$ edges is structurally motivated: the same uncertainty-ratio logic applies wherever an agent updates a belief in response to noisy evidence. The update *form* is validated for Beta-Bernoulli edges across four topologies (#strategic-dynamics-derivation, Props B.1-B.4). The signal function — how to compute $\text{signal}(o_t, i, j)$ — is now characterized at the theory level:

- **Theory-level resolution.** #credit-assignment-boundary shows that persistence does not require per-edge credit assignment (Prop B.5), that any signal function with directional fidelity suffices for persistence (Level 1), and that exact attribution is #P-hard in general (Level 3). The gradient-based candidate $\text{signal}_k = p_k + J_k \cdot (y_G - \hat P_\Sigma) / \lVert\mathbf{J}\rVert^2$ satisfies directional fidelity for monotone DAGs and is computable in $O(\lvert V\rvert + \lvert E\rvert)$.
- **What remains domain-specific.** The choice among signal function implementations (gradient attribution, proportional blame, belief propagation, exact Bayesian) depends on the domain's observability structure and computational budget. This is engineering, analogous to how the gain *principle* ($\eta^\ast = U_M/(U_M + U_o)$) is theory while the gain *estimator* (Kalman, TD-learning, intuition) is engineering.
- **Remaining open questions.** (1) Continuous outcomes with multi-parent nodes — signal function candidates exist but are not verified. (2) Interaction with $M_t$ updates �� edge updates use observations already processed for $M_t$; whether this creates statistical dependencies that bias edge updates is not analyzed. (3) The gradient candidate inherits $\hat P_\Sigma$'s overestimation bias under correlated failures ( #strategy-dag) — see #credit-assignment-boundary Working Notes.

## Discussion

**Connection to #observability-dominance.** When $\sigma_j \approx 0$: $U_{\text{obs}} \to \infty$, $\eta_{\text{edge}} \to 0$. The edge is frozen at its prior. Unobservable links cannot be updated — this is the mechanism that makes unobservable paths epistemically dead.

**Connection to #strategic-calibration.** The edge update rule is the correction function that the strategic calibration residual calls for: persistently positive $r_{ij}$ (predicted value increment exceeds observed) should reduce $p_{ij}$; persistently negative $r_{ij}$ should increase it. The gain principle provides the update magnitude — how much to adjust given the evidence strength.

**Conservative by design.** The uncertainty ratio ensures the agent doesn't overreact to single observations: a well-established edge ($\alpha + \beta$ large, $U_{\text{edge}}$ small) requires strong evidence to revise; a newly hypothesized edge ($\alpha + \beta$ small, $U_{\text{edge}}$ large) is easily moved by evidence. This mirrors the epistemic gain's behavior for $M_t$ — the agent trusts accumulated experience over individual observations.

## Working Notes

- The signal function is characterized at the theory level (#credit-assignment-boundary) but remains domain-specific in implementation. The gradient-based candidate is the theory's default Level 1 scheme; domains with richer observability can do better (Level 2-3). For continuous outcomes with multiple contributing edges, even the gradient candidate requires further validation.
- **Partial progress on the signal function** (from #strategic-dynamics-derivation (Props B.2-B.3)). For observable binary outcomes in a chain $A \to B \to G$: when $B$ is observable, the signal function is trivial — $\text{signal}(o_t, A, B) = y_B$ and $\text{signal}(o_t, B, G) = y_G$ (given $y_B = 1$), with no signal when the upstream edge fails. When $B$ is unobservable, the proportional-blame signal $q_k = P(\text{edge } k \text{ caused failure} \mid y_G = 0)$ turns out to be exactly the marginal Bayesian point estimate — not a heuristic. This is a genuine result: the "obvious" blame-assignment heuristic is the optimal marginal update for the posterior mean. However, the marginal point-estimate update is biased at truth (violates A1 with $O(1/n)$ bias), so the signal function is correct as a Bayesian computation but produces a biased correction when used in the factored point-estimate representation. The signal function question remains open for continuous outcomes, multi-parent nodes, and general DAG topologies.
- The Beta-Bernoulli model assumes edge outcomes are i.i.d. Bernoulli draws. This is adequate for many settings but misses: (a) time-varying edge reliability ($p_{ij}$ drifting), (b) context-dependent reliability ($p_{ij}$ varies with environmental conditions), (c) correlated edge outcomes. Extending to time-varying priors (discounting old evidence) would connect to the mismatch dynamics framework.
