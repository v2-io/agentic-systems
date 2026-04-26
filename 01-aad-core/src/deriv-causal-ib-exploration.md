---
slug: deriv-causal-ib-exploration
type: derivation
status: conditional
depends:
  - disc-ciy-unified-objective
  - form-information-bottleneck
  - def-pearl-causal-hierarchy
  - result-persistence-condition
  - def-mismatch-signal
stage: draft
---

# Derivation: The Survival-Imperative Exploration Drive

The unified policy objective in `#disc-ciy-unified-objective` combines pragmatic value $Q_O$ with an epistemic exploration term (Causal Information Yield, CIY) weighted by $\lambda_{\text{info}} \propto U_M$. The logic is intuitive: explore when uncertain. 

However, AAD's underlying Lyapunov dynamics ( `#result-persistence-condition`) force a *second, structurally distinct* exploration drive: the **Survival Imperative**. This segment derives that an agent must actively seek low-noise (high CIY) observations not just to learn, but to physically survive environmental drift when its model is *confident*.

## The Persistence-Bounded Objective

The agent's primary goal is to maximize pragmatic value:
$$\max_{\pi} \mathbb{E}_{a \sim \pi} [Q_O(a)]$$

The agent is subject to the structural persistence condition ($\alpha R \gt \rho^{\text{eff}}$), meaning it only survives if its steady-state mismatch $R^\ast \lt R$. 
Under Model D dynamics, $R^\ast = \rho^{\text{eff}} / (\eta^\ast c_{\min})$. 
Using the optimal update gain $\eta^\ast = \frac{U_M}{U_M + U_o}$, we can rewrite the survival constraint exactly:
$$\frac{U_M}{U_M + U_o} \gt \frac{\rho^{\text{eff}}}{R c_{\min}}$$

Solving for $U_o$, we find the maximum observation noise the agent can tolerate without destabilizing:
$$U_o^{\max} = U_M \left( \frac{R c_{\min}}{\rho^{\text{eff}}} - 1 \right)$$

This creates a strict constraint on the agent's action selection:
$$\mathbb{E}_{a \sim \pi} [U_o(a)] \le U_o^{\max}(M_t)$$

## The Tragedy of the Confident Agent

Notice the proportionality: $U_o^{\max} \propto U_M$. 

As $U_M \to 0$ (the agent becomes highly confident), $U_o^{\max} \to 0$. The survival constraint becomes infinitely tight. 

If the environment is drifting ($\rho^{\text{eff}} \gt 0$), a confident agent inherently ignores noisy observations ($\eta^\ast \to 0$). To survive the drift, the agent *must* force an update. The only way to penetrate its own stubbornness is to generate an observation so pristine (low $U_o$) that the agent is forced to correct its course. Thus, a confident agent in a drifting world is *forced* to explore (seek low $U_o$) simply to survive. 

Conversely, an uncertain agent (high $U_M$) has a loose constraint (large $U_o^{\max}$). It updates easily ($\eta^\ast \to 1$), so it can safely exploit noisy states without fear of structural collapse.

## Deriving the Survival Lagrange Multiplier $\lambda_{\text{surv}}$

*[Derivation (survival-exploration)]*

Formulating the KKT Lagrangian for this constrained optimization:
$$\mathcal{L} = \mathbb{E}[Q_O(a)] - \lambda' \cdot (\mathbb{E}[U_o(a)] - U_o^{\max})$$

The shadow price $\lambda'$ scales as $1 / (U_o^{\max} - \mathbb{E}[U_o])$. At the boundary, $\lambda' \propto 1/U_o^{\max}$, yielding:
$$\lambda' \propto \frac{\rho^{\text{eff}}}{(R c_{\min} - \rho^{\text{eff}}) \cdot U_M}$$

To align this with the CIY objective, we invoke the structural assumption that Causal Information Yield is inversely proportional to observation ambiguity: $\text{CIY}(a) \propto 1/U_o(a)$. 
Transforming the Lagrangian penalty from $U_o$ to $1/U_o$ (which introduces a non-linear mapping of the multiplier, operating-point dependent), the equivalent survival weight on CIY becomes:
$$\lambda_{\text{surv}}(M_t) \propto \frac{\rho^{\text{eff}}}{(R c_{\min} - \rho^{\text{eff}}) \cdot U_M}$$

## Epistemic Status

*Derived (conditional).* The derivation of the $U_o^{\max}$ bound and the KKT multiplier $\lambda'$ is exact, conditional on the continuous-time Lyapunov bounds from `#result-sector-condition-stability`. The mapping to $\lambda_{\text{surv}} \cdot \text{CIY}$ is *heuristic*, conditional on the assumed structural relationship $\text{CIY}(a) \propto 1/U_o(a)$ and the non-linear transformation of the shadow price.

## Discussion

**Two Parallel Exploration Drives.** AAD dictates two correlated but distinct motivations for exploration, acting at opposite ends of the uncertainty spectrum:
1. **Epistemic Information Gain ($\lambda_{\text{info}} \propto U_M$):** Explored in `#disc-ciy-unified-objective`. The agent explores to reduce its model uncertainty. Dominates when $U_M$ is high.
2. **Lyapunov Survival Imperative ($\lambda_{\text{surv}} \propto 1/U_M$):** Derived here. The agent explores to force high-fidelity corrections against environmental drift. Dominates when $U_M$ is low.

**Resolving the IB $\beta$ vs $\rho$ conflation.** This derivation clarifies a structural tension in the standard IB formulation (`#form-information-bottleneck`). Standard IB natively discards old information as $\rho$ rises because the joint distribution $P(\mathcal{C}_t, O_{t+1})$ decorrelates. The agent's *representational preference* ($\beta$) does not need to change. However, the agent's *action policy* is tightly coupled to $\rho$. As $\rho$ increases, the survival constraint tightens ($U_o^{\max} \downarrow$), forcing the Lagrange multiplier $\lambda_{\text{surv}}$ to spike. The environment dictates the representation natively; survival dictates the policy.

**Connection to Active Inference.** This derivation completely sidesteps the Active Inference "preferences-as-priors" assumption (the dark room problem). The survival exploration drive exists purely because failing to bound $U_o$ mathematically guarantees structural collapse ($\alpha R \lt \rho^{\text{eff}}$). Exploration is derived as a physical survival imperative, not a psychological preference.

**Honest limit: the scalar formulation admits a "blank wall" attack.** The survival constraint as derived bounds the *scalar* observation-noise expectation $\mathbb{E}_\pi[U_o(a)] \le U_o^{\max}$ — it cares only about the magnitude of $U_o$, not its alignment with the directions in which $\rho^{\text{eff}}$ is acting. Concretely, suppose the environment has a multidimensional state in which only some coordinates are drifting; an agent action that selects an observation channel orthogonal to the drift (a constant signal — the "blank wall") drives $U_o$ to near-zero in that subspace and satisfies the scalar survival condition. The agent's prediction error in the drifting subspace nevertheless grows without bound, because the observations carry no information about the drifting coordinates. The scalar reduction collapses the dimensionality that matters: low $U_o$ guarantees survival only when the low-noise observations actually project onto the drifting eigenspace of $\rho^{\text{eff}}$.

The repair direction upgrades the scalar inequality to a Linear Matrix Inequality on the Fisher Information Matrix: the observation channel must inject sufficient information along every eigendirection of the disturbance, not merely reduce overall noise magnitude. This forbids "blank wall" exploitation by mathematical construction — an action that doesn't probe the drifting coordinates fails the LMI even when its scalar trace is small. The LMI formulation is sketched in `msc/spike-causal-information-bottleneck.md` §7 and likely also requires tensor-valued $\mathcal{T}$ in `#def-adaptive-tempo` to track per-direction adaptive rates. The scalar derivation above remains correct in its scope (1D environments and isotropic-disturbance multidimensional environments where any observation channel suffices), and the qualitative dual-drive picture survives the lift; the LMI generalization is what closes the multidimensional gap.

## Working Notes
- **Empirical validation.** The derivation is validated in `msc/track-b-nonlinear-sims/variants/variant_causal_ib.py` (results: `variant_causal_ib_results.md`). In a highly volatile environment ($\rho = 0.5$) where exploitation produces ambiguous observations ($U_o = 100.0$), a purely greedy agent ($\lambda = 0$) suffers a 0% survival rate because its update gain collapses.
- **LMI generalization queued.** The "blank wall" multidimensional limit named in Discussion is queued in TODO. Spike `msc/spike-causal-information-bottleneck.md` §7 sketches the Linear-Matrix-Inequality on the Fisher Information Matrix that closes the gap; the lift will likely require tensor-valued $\mathcal{T}$ in `#def-adaptive-tempo`. 