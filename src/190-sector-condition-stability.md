---
slug: sector-condition-stability
type: theorem
status: exact (under qualitative monotonicity assumptions)
depends:
  - adaptive-tempo
  - mismatch-signal
---

# Sector Condition Stability

An agent's mismatch remains bounded — preventing model breakdown — as long as its correction function points inward (reducing mismatch) and is proportional to the mismatch within bounded limits, and the effective correction strength exceeds the environmental disturbance rate. 

## Formal Expression

Let $\delta(t) \in \mathbb{R}^n$ be the vector of model-reality mismatches.
Let the mismatch dynamics be driven by an unspecific, potentially nonlinear correction function $F$ and an external disturbance rate $w(t)$:
$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

Assume $F$ satisfies the **local sector condition** for $\|\delta\| \leq R$:
*[Assumption (sector-condition)]*
$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \|\delta\|^2$$
where $\alpha > 0$ represents the worst-case correction efficiency within the valid region of radius $R$ (the model class capacity).

Let the disturbance be bounded: $\|w(t)\| \leq \rho$.

*[Theorem (Bounded Mismatch, from Lyapunov analysis)]*
The mismatch $\delta(t)$ is ultimately bounded by $R^* = \rho / \alpha$. The agent persists (avoids divergence) if and only if:
$$\alpha > \frac{\rho}{R}$$

*[Theorem (Adaptive Reserve)]*
The agent's capacity to absorb sudden environmental shocks before its model breaks down (exceeding radius $R$) is the **adaptive reserve**:
$$\Delta\rho^* = \alpha R - \rho$$

## Epistemic Status

These results are *exact mathematically derived consequences* of standard Lyapunov stability theory under the mild qualitative assumptions of bounded disturbances and the sector condition. They explicitly replace the brittle linear ODE hypothesis ($\dot{\delta} = -\mathcal{T}\delta + \rho$) with a rigorous foundation that handles nonlinear thresholding, saturation, and arbitrary correction functions.

## Discussion

**Why the Sector Condition Matters.** The linear ODE approximation assumes that correction scales perfectly linearly with mismatch forever. Real adaptive systems saturate (large errors overwhelm the update mechanism), exhibit thresholding (small errors are ignored), or break down structurally when the model class is exhausted. The sector condition provides a unified mathematical language to say: "As long as the correction pushes the model in the right direction with at least *some* baseline efficiency $\alpha$, the system is stable."

**Generalizing the Persistence Threshold.** In the linear case, $\alpha$ is simply the adaptive tempo $\mathcal{T}$. The general result $\alpha > \rho/R$ proves that the persistence threshold (#persistence-condition) is a deep structural necessity of any bounded-correction system, not an artifact of a specific linear approximation.

**Adversarial Destabilization.** If an adversary $A$ deliberately injects disturbance into agent $B$'s environment (so $\rho_B = \rho_{B,\text{base}} + \gamma_A \mathcal{T}_A$), agent $A$ destabilizes agent $B$ exactly when $A$'s effective disruption exceeds $B$'s adaptive reserve:
$$\gamma_A \mathcal{T}_A > \Delta\rho^*_B$$
This formally defines "getting inside the opponent's loop" as a Lyapunov instability. Once $B$ is pushed past its invariant region $R$, its actions become erratic, often increasing $A$'s coupling effectiveness ($\gamma_A$) in a positive-feedback loop (the *effects spiral*).

**Trigger for Structural Adaptation.** When $\rho / \alpha > R$, the environment introduces disturbance faster than the model class $\mathcal{M}$'s maximum capacity to parameterize corrections. The sector condition fails. This is the dynamical trigger for structural adaptation (#structural-adaptation-necessity), demanding a new model class with a larger valid radius $R'$ or better efficiency $\alpha'$.