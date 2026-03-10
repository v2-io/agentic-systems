---
slug: update-gain
type: empirical
status: exact (for Kalman/conjugate systems), structural heuristic (for general RL/organizational systems)
depends:
  - mismatch-signal
  - observation-function
---

# Update Gain (Uncertainty Ratio Principle)

The optimal weight an agent assigns to new observations when updating its model balances its current model uncertainty against the observation channel's noise. High model uncertainty demands high gain (trusting the new observation); high observation noise demands low gain (trusting the prior model).

## Formal Expression

*[Empirical Claim (uncertainty-ratio-principle)]*

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where:
- $\eta^*$ is the optimal update gain (the proportion of mismatch used to correct the model).
- $U_M$ is the agent's internal model uncertainty (predictive variance or entropy).
- $U_o$ is the irreducible observation noise of the channel.

The update rule structurally takes the form:
$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$
where $\delta_t$ is the mismatch (#mismatch-signal) and $g(\cdot)$ is a correction mapping.

## Epistemic Status

This principle is *exact* for linear-Gaussian systems (where it is the Kalman gain) and conjugate Bayesian systems. For general adaptive systems (RL agents, organizational learning, biological adaptation), it is a *robust structural heuristic*. It identifies the functional dependencies that any optimal adaptation process must approximate, even if the precise variance ratio doesn't strictly hold or isn't explicitly computed by the agent.

## Discussion

**The Epistemic Pivot.** Gain determines *epistrophe* — the degree to which the agent turns toward reality to correct its internal model. 
- When $U_M \gg U_o$, the model is highly uncertain (e.g., initialized recently, or following a structural adaptation #structural-adaptation-necessity). The agent should set $\eta^* \to 1$, treating the observation as ground truth.
- When $U_M \ll U_o$, the model is confident and the channel is noisy. The agent should set $\eta^* \to 0$, interpreting the mismatch primarily as sensor noise rather than a structural error in the model.

**Gain Collapse and Confirmation Bias.** A critical failure mode occurs when an agent improperly estimates $U_M \to 0$ (spurious confidence) or $U_o \to \infty$ (spurious distrust of sensors). In both cases, $\eta^* \to 0$, and the agent stops learning. Mismatches are ignored, resulting in confirmation bias or a decoupled reality model.

**Beyond Scalar Gains.** In multi-dimensional systems, $U_M$ and $U_o$ are covariance matrices, and the optimal gain is a matrix (as in the Kalman filter). In multi-agent settings (#400 multi-agent-scope), the $U_o$ term expands to include channel noise, source calibration uncertainty, and alignment/deception uncertainty.

**Connection to Adaptive Tempo.** The update gain is one half of the agent's adaptive tempo (#adaptive-tempo): updating frequently (high $\nu$) is useless if the updates themselves extract no information (low $\eta^*$). The gain measures the *quality* of the update cycle.