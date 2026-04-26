---
slug: deriv-causal-ib-lmi
type: derivation
status: conditional
depends:
  - deriv-causal-ib-exploration
  - form-information-bottleneck
  - def-pearl-causal-hierarchy
  - result-persistence-condition
  - deriv-fisher-whitened-update-rule
  - def-adaptive-tempo
stage: draft
---

# Derivation: Linear Matrix Inequality Form of the Causal-IB Survival Bound

In `#deriv-causal-ib-exploration`, the survival-imperative exploration drive was derived in scalar form: bound $\mathbb E_\pi[U_o(a)] \le U_o^{\max}$ to keep the agent's mismatch within survivable bounds. The scalar bound admits a "blank wall" attack — actions that minimize $U_o$ in a subspace orthogonal to the drift (e.g., observing a constant signal uncorrelated with the environmental drift) satisfy the survival math without probing the drifting coordinates, and the agent's prediction in those subspaces diverges unboundedly. This segment lifts the survival constraint to a Linear Matrix Inequality on the Fisher Information Matrix, replacing the scalar shadow price with a positive-semidefinite matrix Lagrange multiplier $\Lambda$ that distinguishes by direction, not just by magnitude.

## Formal Expression

### Multidimensional mismatch dynamics

*[Definition (multidim-mismatch)]*

The mismatch state $\delta_t \in \mathbb R^n$ evolves under linear-Gaussian dynamics with action-dependent observation noise:

$$\delta_{t+1} = (I - K_t H)\delta_t + w_t - K_t v_t(a_t)$$

where $w_t \sim \mathcal N(0, Q_\rho)$ is the environmental drift, $v_t \sim \mathcal N(0, R_o(a_t))$ is the observation noise for action $a_t$, and the optimal Kalman gain is $K_t = P_t H^T(H P_t H^T + R_o(a_t))^{-1}$ with $P_t$ the agent's prior uncertainty covariance.

The steady-state mismatch covariance $\Sigma_\delta$ satisfies the discrete-time algebraic Riccati equation. *Survival* requires the spectral bound

$$\lambda_{\max}(\Sigma_\delta) \lt R^2$$

— the matrix lift of the scalar bound $R^\ast \lt R$ from `#result-persistence-condition`.

### Fisher Information Matrix as matrix CIY

*[Definition (matrix-ciy)]*

For the linear-Gaussian observation model, the action-conditional Fisher Information Matrix is

$$\mathcal I_o(a) = H^T R_o(a)^{-1} H.$$

Where the scalar formulation in `#disc-ciy-unified-objective` defined CIY as a surrogate satisfying $\text{CIY}(a) \propto 1/U_o(a)$, the multidimensional formulation identifies CIY directly with the action-conditional FIM. The CIY-$U_o$ surrogate-mapping layer of approximation in the scalar derivation is removed at this layer; the residual CIY-vs-EIG concern (FIM equals EIG-rate only under Gaussian-linear conditions) persists as before.

The information-form Kalman update is additive in the FIM:

$$P_{t+1\mid t+1}^{-1} = P_{t+1\mid t}^{-1} + \mathcal I_o(a_t),$$

where $P_{t+1\mid t} = A P_t A^T + Q_w$ is the prediction step that absorbs process noise. The simplification $P_{t+1}^{-1} = P_t^{-1} + \mathcal I_o(a_t)$ used in some passes refers to the information-update step alone; the full step adds the prediction contribution. The two coincide once the analysis is in steady state.

### LMI survival constraint

*[Derived (lmi-survival)]*

The discrete-time algebraic Riccati equation admits a stabilizing steady-state solution with $\lambda_{\max}(\Sigma_\delta) \lt R^2$ if and only if the action policy $\pi$ provides Fisher information that dominates the unstabilizable modes of the system drift. Specifically, the policy must satisfy the Linear Matrix Inequality

$$\mathbb E_{a \sim \pi}[\mathcal I_o(a)] \succeq \mathcal I_{\min}(Q_\rho, A, R^2)$$

where $\mathcal I_{\min}$ is the symmetric positive-definite lower bound on the FIM required to keep the steady-state covariance's largest eigenvalue below $R^2$. The closed form for $\mathcal I_{\min}$ as a function of $(Q_\rho, A, R^2)$ is given by the steady-state DARE condition — standard control-theory machinery (Boyd, Ghaoui, Feron & Balakrishnan 1994 Ch. 3–5; Anderson & Moore 1979). AAD's contribution at this layer is the framing: $\mathcal I_{\min}$ enters as the *survival-imperative* Fisher-information floor, not as a controller-design parameter.

### Tensor Lagrangian

*[Derived (tensor-lagrangian)]*

The agent maximizes pragmatic value under the LMI constraint:

$$\max_\pi\, \mathbb E_\pi[Q_O(a)] \quad \text{s.t.} \quad \mathbb E_\pi[\mathcal I_o(a)] \succeq \mathcal I_{\min}.$$

The Lagrangian for a matrix-inequality-constrained problem uses a positive-semidefinite matrix Lagrange multiplier $\Lambda \succeq 0$:

$$\mathcal L(\pi, \Lambda) = \mathbb E_\pi[Q_O(a)] + \text{Tr}\!\left( \Lambda \cdot \left( \mathbb E_\pi[\mathcal I_o(a)] - \mathcal I_{\min} \right) \right).$$

KKT conditions are primal feasibility ($\mathbb E_\pi[\mathcal I_o(a)] \succeq \mathcal I_{\min}$), dual feasibility ($\Lambda \succeq 0$), and complementary slackness ($\text{Tr}(\Lambda \cdot (\mathbb E_\pi[\mathcal I_o(a)] - \mathcal I_{\min})) = 0$). The optimal action selection rule is

$$a_t \in \arg\max_a \left[\, Q_O(a) + \text{Tr}\!\left(\Lambda \cdot \mathcal I_o(a)\right) \,\right].$$

The trace inner-product $\text{Tr}(\Lambda \cdot \mathcal I_o(a))$ is the **matrix exploration bonus** — the multidimensional analog of $\lambda_{\text{surv}} \cdot \text{CIY}(a)$ from the scalar derivation.

### Resolution of the blank-wall attack

*[Derived (blank-wall-resolution)]*

By complementary slackness, $\Lambda$ has support only in eigendirections where the LMI constraint binds — i.e., directions where the agent's accumulated FIM sits at the threshold $\mathcal I_{\min}$. In non-drifting eigendirections of $Q_\rho$, $\mathcal I_{\min}$ contributes zero (no information needed there to survive), so $\Lambda$ has zero weight in those directions.

For a blank-wall action — high $\mathcal I_o(a)$ in a non-drifting eigendirection — the trace product $\text{Tr}(\Lambda \cdot \mathcal I_o(a))$ evaluates to zero: the action's FIM eigenvalues lie outside $\Lambda$'s support. The agent receives no exploration bonus for the blank-wall action, even though the action would satisfy the scalar magnitude bound. **The matrix Lagrangian distinguishes by direction, not just by magnitude**, mathematically forbidding the trivial-exploration solutions that the scalar form admitted.

### Scalar reduction

*[Derived (scalar-recovery)]*

In the 1D case, $H$ and $R_o(a)$ are scalars, $\mathcal I_o(a) = R_o(a)^{-1}$, and the LMI degenerates to the scalar inequality $\mathbb E_\pi[R_o(a)^{-1}] \geq \mathcal I_{\min}$ which, with $\mathcal I_{\min}^{-1} = U_o^{\max}$, recovers the scalar survival constraint of `#deriv-causal-ib-exploration`. The matrix multiplier $\Lambda$ collapses to a scalar shadow price coinciding with $\lambda_{\text{surv}}$, and the matrix exploration bonus reduces to $\lambda_{\text{surv}} \cdot \text{CIY}(a)$. The multidimensional derivation is structurally consistent with — and properly subsumes — the scalar one.

### Tragedy of the Confident Agent — matrix form

*[Derived (matrix-confidence-tragedy)]*

As the agent's prior covariance $P_t$ shrinks in a particular eigendirection $v$, the agent's confidence in that direction grows. If $v$ also has support in $Q_\rho$ (a drifting eigendirection), the survival LMI requires $\mathcal I_{\min}$ to grow along $v$ to compensate — a confident agent in a drifting direction must source information specifically along that direction, because its low $P_t$ in $v$ means its update gain is small there and slow to absorb new information. By complementary slackness, the matrix shadow price $\Lambda$ develops a large principal eigenvalue along $v$, forcing the agent to choose actions whose $\mathcal I_o(a)$ has large support on $v$. The qualitative tragedy survives the lift: confident agents in drifting worlds are mathematically forced to probe the drifting eigendirections specifically, not just to minimize scalar noise.

## Epistemic Status

*Derived (conditional).* The structural derivation is exact under named conditions:

1. **Riccati stabilizability.** The discrete-time algebraic Riccati equation admits a stabilizing steady-state solution. Standard machinery: Boyd, Ghaoui, Feron & Balakrishnan 1994 §3–5 and Anderson & Moore 1979.
2. **Linear-Gaussian observation model.** The observation $o = Hx + v$ with $v \sim \mathcal N(0, R_o(a))$. Non-Gaussian or nonlinear models require local linearization or extended-Kalman treatment.
3. **Information-form Kalman in steady state.** The $\mathcal I_o$-additivity used in the FIM update reflects the information-update step alone; the prediction step's $A P_t A^T + Q_w$ contribution is absorbed into the steady-state Riccati analysis. Transient regimes admit the constraint shape but with $\mathcal I_{\min}$ a function of the transient covariance.
4. **DARE-imported $\mathcal I_{\min}$.** The closed-form expression for $\mathcal I_{\min}(Q_\rho, A, R^2)$ via the DARE is theorem-imported standard control theory. AAD's contribution is the framing — $\mathcal I_{\min}$ enters as the survival-imperative FIM floor, with $\Lambda$ as the directional exploration-bonus shadow price — not the DARE solution itself.

The matrix-CIY mapping ($\mathcal I_o(a)$ as multidimensional CIY) is more rigorous than the scalar version: where the scalar formulation needed CIY $\propto 1/U_o$ as an assumed structural mapping, the matrix formulation directly identifies CIY with the action-conditional FIM, removing one of the two layers of approximation in `#disc-ciy-unified-objective`. The CIY-vs-EIG surrogate concern remains: FIM is the EIG-rate for Gaussian linear models but diverges from EIG under non-Gaussian or non-local conditions.

## Discussion

**Connection to AAD's existing matrix-form machinery.** The LMI repair sits naturally within several existing AAD components rather than being imported from outside:

- `#deriv-fisher-whitened-update-rule` derives Fisher-information-based credit assignment as AAD-internal under the (PI) parameterization-invariance axiom + Čencov 1982 uniqueness. The FIM appearing in the LMI is the same Fisher metric, used here for survival rather than for credit assignment — two roles for one geometric object.
- `#disc-additive-coordinate-forcing` lists Čencov-invariance as the 4th primary instance of the meta-pattern. The LMI's reliance on the FIM sits cleanly within that meta-pattern: the Fisher metric is forced by AAD-internal axioms, not adopted ad hoc.
- `#result-contraction-template` carries matrix-form sector machinery (Lohmiller-Slotine metric formulation) for Section III composition. The LMI's discrete-time Riccati is the control-theoretic analog of the contraction-metric framework — both are matrix-form sector conditions on multivariate dynamics.
- `#def-adaptive-tempo` will need a tensor extension to $\mathcal T$ for full alignment with this segment's directional structure; the LMI gives an explicit demand for tensor-valued adaptive rates.

**Two parallel exploration drives — matrix lift.** The scalar dual-drive distinction in `#disc-ciy-unified-objective` ($\lambda_{\text{info}} \propto U_M$ epistemic vs $\lambda_{\text{surv}} \propto 1/U_M$ Lyapunov-survival) generalizes to two matrix-valued drives that compose additively:

- $\Lambda_{\text{info}}$: epistemic information-gain matrix scaled by $P_t$. Dominates eigendirections where $P_t$ is large (high uncertainty in some direction) — agent explores to learn that direction.
- $\Lambda_{\text{surv}}$: Lyapunov survival-imperative matrix derived above, with eigenvalue support where the LMI constraint binds. Dominates when $P_t$ is small along a drifting eigendirection — agent explores to track the drift it's about to lose grip on.

The agent's total exploration shadow price is $\Lambda_{\text{info}} + \Lambda_{\text{surv}}$, with the relative direction-by-direction weights set by where the agent sits in $(P_t, Q_\rho)$ space.

**Connection to Active Inference.** Same dark-room sidestep as the scalar version: the matrix-form survival imperative is forced by Lyapunov bounds, not preferences-as-priors. The matrix lift sharpens the argument by ruling out the non-exploratory "blank wall" trivial solutions that the scalar form admitted.

**Empirical signature.** A 2D drift environment with separable drifting/non-drifting subspaces is the simplest test: a scalar-Lagrangian agent succumbs to blank-wall traps; an LMI agent — with $\Lambda$ developing weight specifically in the drifting direction — must select actions whose $\mathcal I_o$ aligns with the drift. The directional discrimination is empirically visible in the agent's action-selection histogram across the two subspaces.

## Working Notes

- **Tensor adaptive tempo.** `#def-adaptive-tempo` is currently scalar; the LMI repair requires tensor-valued $\mathcal T$ tracking per-direction rates for full alignment with this segment and with `#deriv-fisher-whitened-update-rule` and `#deriv-adaptive-gain-dynamics`. Queued in TODO.
- **Worked 2D example.** A concrete 2D drift environment showing $\text{Tr}(\Lambda \mathcal I_o)$ distinguishing wall-channel from drift-channel actions would sharpen the blank-wall resolution. Queued.
- **2D simulation.** Generalization of `msc/track-b-nonlinear-sims/variants/variant_causal_ib.py` to 2D with separable drifting/non-drifting subspaces would empirically validate the matrix Lagrangian's directional discrimination. Queued.
- **EIG vs FIM gap.** For non-Gaussian or non-local observation models, FIM diverges from EIG. The CIY-vs-EIG concern in `#disc-ciy-unified-objective` Epistemic Status persists; the matrix lift removes the CIY-$U_o$ surrogate but not the CIY-EIG surrogate.
- **Reasoning trail.** `msc/spike-causal-ib-lmi-repair.md` records the spike that surfaced the LMI repair from the scalar segment's blank-wall critique.
