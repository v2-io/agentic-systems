# Appendix E: TFT Core — Minimal Formal Path

**Purpose.** This appendix presents the core theorem chain of Temporal Feedback Theory in condensed form: one scope definition, one axiom (with derived recursive update), one formulation, five propositions, and the key definitions connecting them. No extended discussion, domain instantiations, or open questions. For full development, see the individual TF documents. For notation, see [TF-00](TF-00.md).

---

## 1. Scope (TF-01)

TFT applies to any agent-environment pair where the agent observes, acts, and faces residual uncertainty:

$$\mathcal{S}_{\text{TFT}} = \{(Agent, \Omega) : \mathcal{O} \neq \emptyset, \; |\mathcal{A}| \geq 2, \; H(\Omega_t \mid \mathcal{C}_t) > 0 \}$$

Observations are lossy: $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$. Actions affect the environment: $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$. The binary-action minimum ($|\mathcal{A}| \geq 2$) ensures at least one interventional contrast exists.

## 2. Causal Structure (TF-02, Axiom)

The interaction history $\mathcal{C}_t = (o_1, a_1, \ldots, a_{t-1}, o_t)$ is temporally ordered and irreversible. This ordering grounds three levels of epistemic access (Pearl's causal hierarchy): **associational** ($P(o_t \mid \mathcal{C}_{<t})$), **interventional** ($P(o_t \mid do(a_{t-1}), M_{t-1})$), and **counterfactual** ($P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$).

**Recursive update (derived from TF-02 + TF-01 + TF-03).** The arrow of time (physical), partial observability (scope), and state completeness (modeling commitment) jointly yield the general causal-respecting update $\dot{M} = g(M, u)$. Under TFT's event-driven assumption: $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$. Serial special case: $M_t = f(M_{t-1}, o_t, a_{t-1})$. This is the unique form consistent with the three constraints (uniqueness argument in TF-02).

## 3. The Model (TF-03, Formulation)

Any persisting agent is analyzed as maintaining a **model** $M_t = \phi(\mathcal{C}_t) \in \mathcal{M}$ — a compression of its interaction history.

## 4. Prolepsis → Aisthesis → Aporia: The Mismatch Signal (TF-05, Derived)

The model anticipates (*prolepsis*); reality responds (*aisthesis*). Their difference is the mismatch — *aporia*:

$$\delta_t = o_t - \hat{o}_t, \quad \hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$$

**Proposition 5.1 (Mismatch Inevitability).** For any $(Agent, \Omega) \in \mathcal{S}_{\text{TFT}}$:

$$\mathbb{E}[\|\delta_t\|^2] = \underbrace{\mathbb{E}[\|\hat{o}_t - \bar{o}_t\|^2]}_{\text{model error (reducible)}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{observation noise (irreducible)}} > 0$$

whenever observation noise is non-degenerate or the model's predictive mean is misspecified.

## 5. Epistrophe: The Update Gain (TF-06, Empirical Claim)

The model turns toward reality (*epistrophe*): $M_t = M_{t-1} + \eta(M_{t-1}) \cdot g(\delta_t)$.

**Uncertainty ratio principle.** The optimal gain has the structural form:

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where $U_M = \text{Var}_{M_{t-1}}[\hat{o}_t \mid a_{t-1}]$ (model uncertainty) and $U_o = \text{Var}[\varepsilon_t]$ (observation uncertainty). Exact for Kalman and conjugate Bayesian systems; structural form validated approximately across RL, PID, and organizational adaptation.

## 6. Adaptive Tempo and Persistence (TF-11, Derived + Hypothesis)

**Adaptive tempo** (the effective rate at which the agent reduces mismatch):

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

**Mismatch dynamics** (hypothesis — linear approximation):

$$\frac{d\|\delta\|}{dt} = -\mathcal{T} \cdot \|\delta\| + \rho(t)$$

**Proposition 11.1 (Persistence Threshold).** Steady-state mismatch $\|\delta\|_{ss} = \rho/\mathcal{T}$. The model remains functionally adequate iff:

$$\mathcal{T} > \frac{\rho}{\|\delta_{\text{critical}}\|}$$

**Corollary 11.2 (Squared Tempo Advantage).** Under adversarial coupling with negligible base disturbance, steady-state mismatch ratios scale as:

$$\frac{\|\delta_B\|_{ss}}{\|\delta_A\|_{ss}} = \frac{\gamma_A}{\gamma_B}\left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

## 7. Lyapunov Generalization (Appendix A, Derived)

The linear hypothesis is replaced by a **sector condition**: $\delta^T F(\mathcal{T}, \delta) \geq \alpha\|\delta\|^2$ for $\|\delta\| \leq R$.

**Proposition A.1 (Bounded Mismatch).** Under the sector condition with bounded disturbance $\|w(t)\| \leq \rho$: mismatch is ultimately bounded by $R^* = \rho/\alpha$. The agent persists iff $\alpha > \rho/R$.

**Proposition A.2 (Adaptive Reserve).** The agent can absorb additional disturbance $\Delta\rho^* = \alpha R - \rho$ without mismatch diverging.

**Proposition A.3 (Adversarial Destabilization).** Agent $A$ drives Agent $B$ past its stability boundary when $\gamma_A \cdot \mathcal{T}_A > \Delta\rho^*_B$.

**Corollary A.3.1 (Effects Spiral).** Post-destabilization, $B$'s degrading model increases $A$'s coupling effectiveness, creating a positive-feedback Lyapunov instability.

## 8. Structural Adaptation Trigger (TF-10, Derived)

**Model sufficiency:** $S(M_t) = 1 - I(\mathcal{C}_t; o_{t+1:\infty} \mid M_t, a_{t:\infty}) / I(\mathcal{C}_t; o_{t+1:\infty} \mid a_{t:\infty})$. **Model class fitness:** $\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$.

**Proposition 10.1 (Structural Adaptation Necessity).** If $\mathcal{F}(\mathcal{M}) < 1 - \epsilon$, no parametric adaptation within $\mathcal{M}$ can reduce mismatch below a floor determined by $\epsilon$. Persistent structured residuals after parametric convergence are diagnostic of model class inadequacy.

---

## Dependency Chain

```
TF-01 (scope) → TF-02 (causal structure, recursive update)
    → TF-03 (model, formulation) → TF-05 (mismatch, Prop 5.1)
    → TF-06 (gain, empirical claim) → TF-11 (tempo, Props 11.1 + 11.2)
    → Appendix A (Lyapunov, Props A.1–A.3, Cor. A.3.1)
TF-03 + TF-05 + TF-10 (sufficiency defs) → TF-10 (Prop 10.1)
```

## Robustness Summary

| Result | Robustness |
|--------|------------|
| Prop 5.1 (Mismatch Inevitability) | **Robust** — requires only scope + model |
| Prop 10.1 (Structural Adaptation) | **Robust** — pure information-theoretic |
| Prop 11.1 (Persistence Threshold) | **Linear-dependent** — qualitative result generalized by A.1 |
| Cor. 11.2 (Squared Tempo Advantage) | **Linear-dependent** — first-order heuristic |
| Props A.1–A.3, Cor. A.3.1 | **Robust** — general nonlinear (sector condition) |
