# Simulation Variant: Causal-IB Exploration vs Survival
**Date:** 2026-04-25
**Related Segment:** `#deriv-causal-ib-exploration`
**Code:** `variant_causal_ib.py`

## Setup
This simulation tests the hypothesis that purely pragmatic exploitation (maximizing $Q_O$) is a fatal strategy in volatile environments if exploitation generates highly ambiguous observations (high $U_o$).

An AAD agent is placed in an environment with drift rate $\rho = 0.5$ and structural capacity $R = 4.0$. At each step, it chooses between:
- **Exploit:** Yields reward if mismatch is low, but generates extremely noisy observations ($U_o = 100.0$, low Causal Information Yield).
- **Explore:** Yields zero reward, but generates crisp, unambiguous observations ($U_o = 0.01$, high CIY).

The agent uses the unified objective from `#disc-ciy-unified-objective`, testing various weightings ($\lambda$) for the CIY term:
1. **Greedy (Constant $\lambda=0$):** Pure exploitation.
2. **Constant $\lambda \gt 0$:** Heuristic exploration bonuses.
3. **Uncertainty-Scaled:** $\lambda \propto U_M$.
4. **Lyapunov-Bounded:** The exact Lagrange multiplier derived in `#deriv-causal-ib-exploration`: $\lambda \propto \frac{U_M}{R - R^\ast}$.

## Results
(500 episodes, 200 steps per episode)

| Strategy                  | Survival Rate   | Mean Reward    |
|---------------------------|-----------------|----------------|
| `constant_0.0` (Greedy)   | 0.00%           | 2.20           |
| `constant_0.005`          | 100.00%         | 0.00           |
| `uncertainty_scaled_0.01` | 100.00%         | 0.00           |
| `lyapunov_bounded_0.001`  | 100.00%         | 92.08          |

## Interpretation
1. **Exploitation is Fatal Without Information:** The greedy strategy (`constant_0.0`) failed 100% of the time. By continuously choosing high-noise exploitation actions, its update gain $\eta^\ast$ collapsed. With low gain, it could not correct the environmental drift $\rho = 0.5$, and its true mismatch rapidly crossed the fatal capacity bound $R=4.0$. It achieved an average reward of only 2.20 before dying.
2. **Heuristics Over-Explore:** The heuristic exploration strategies (`constant_0.005`, `uncertainty_scaled`) survived perfectly, but achieved **zero reward**. They over-explored, prioritizing the crisp CIY observations at the expense of ever actually exploiting the low-mismatch states they achieved.
3. **Lyapunov-Bounded Lambda is Optimal:** The derived Lagrange multiplier strategy (`lyapunov_bounded`) perfectly balanced the two. It exploited as much as physically possible while safely within the persistence basin ($R^\ast \ll R$), earning a massive mean reward of 92.08. When environmental drift or sensor noise pushed $R^\ast \to R$, the multiplier $\lambda$ automatically spiked, forcing the agent to take a high-CIY exploration action just long enough to drop its uncertainty $U_M$ and recover stability, before returning to exploitation. 

This empirically validates the derivation in `#deriv-causal-ib-exploration`: the exploration weight $\lambda$ is not an arbitrary hyperparameter, but the exact restoring force of the Lyapunov survival constraint.