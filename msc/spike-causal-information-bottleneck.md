# Spike: The Causal Information Bottleneck (Causal-IB) for AAD Exploration

**Status.** Exploratory research spike.
**Date.** 2026-04-25.
**Pressure Point.** In `#disc-ciy-unified-objective`, the agent's action selection is defined as a heuristic combination of value exploitation ($Q_O$) and Causal Information Yield (CIY) for exploration, weighted by a tuning parameter $\lambda(M_t)$:
$$a_t = \arg\max_a \left[ Q_O(a; M_t) + \lambda(M_t) \cdot \text{CIY}_q(a; M_t) \right]$$
The segment acknowledges this is "Discussion-grade (heuristic)" because it lacks a rigorous first-principles derivation tying the specific tradeoff $\lambda$ to the agent's underlying epistemic bounds. This spike attempts to derive this exact objective function (and explicitly define $\lambda$) using the **Causal Information Bottleneck (Causal-IB)**.

## 1. The Standard IB formulation (Background)

Per `#form-information-bottleneck`, the standard IB objective for the epistemic state $M_t$ compressing the chronica $\mathcal{C}_t$ to predict future observations $O_{future}$ is:
$$ \min_{P(M_t \mid \mathcal{C}_t)} \mathcal{L}_{\text{IB}} = I(M_t; \mathcal{C}_t) - \beta \cdot I(M_t; O_{future} \mid a_{future}) $$

This defines the *optimal representation* $M_t$. However, it doesn't strictly tell us how to *act* ($a_t$) to acquire the best $\mathcal{C}_{t+1}$ to form the best $M_{t+1}$. 

## 2. The Interventional Requirement

To select an action $a_t$ for exploration, we don't just want a $\mathcal{C}_{t+1}$ that predicts what *will* happen (associational). We want a $\mathcal{C}_{t+1}$ that helps the agent predict what *would* happen under various interventions (causal). 

Following Wieczorek & Roth (2017) and AAD's `#def-pearl-causal-hierarchy`, we need $M_t$ to preserve information about the interventional distribution $P(o \mid do(a))$. 

Let $\Omega$ be the true environment state, and let $O_a$ be the counterfactual observation under intervention $do(a)$.

## 3. Deriving the Unified Objective from Causal-IB

Suppose the agent seeks an action policy $\pi(a \mid M_t)$ that balances two things:
1. **Pragmatic Utility:** Maximizing expected value $Q_O(a)$.
2. **Epistemic Utility (Causal-IB):** Maximizing the flow of *causal information* into $M_{t+1}$. 

Let's formulate the agent's objective as maximizing a Free Energy functional that includes both the instrumental value and the Causal-IB constraint on the transition $\mathcal{C}_t \xrightarrow{a_t} \mathcal{C}_{t+1}$.

*(Drafting the math...)*

Let $I_{\text{causal}}(M_t; O \mid do(A))$ denote the interventional mutual information. 

If the agent takes action $a_t$, it observes $o_{t+1}$, updating $M_t \to M_{t+1}$. The expected *gain* in causal predictive power is exactly the Expected Information Gain (EIG) over the interventional parameters of the environment.

As noted in `#def-causal-information-yield`, CIY is a computationally tractable surrogate for EIG:
$$\text{CIY}(a; M_t) = \mathbb{E}_{a' \sim q} \left[ D_{\text{KL}}(P(o \mid do(a), M_t) \Vert P(o \mid do(a'), M_t)) \right]$$

If we frame the agent's policy $\pi$ as the solution to a regularized optimization problem:
$$ \max_{\pi} \mathbb{E}_{a \sim \pi} [Q_O(a)] - \frac{1}{\beta_{explore}} D_{\text{KL}}(\pi \Vert \pi_{\text{prior}}) $$
where $\pi_{\text{prior}}$ is an exploration prior. If we define the "value" of an action purely epistemically as its CIY, then the prior $\pi_{\text{prior}} \propto \exp(\text{CIY})$.

Substituting this back in gives us an objective that looks exactly like the heuristic:
$$ \mathbb{E}[Q_O(a)] + \frac{1}{\beta_{explore}} \text{CIY}(a) $$
Thus, $\lambda = 1/\beta_{explore}$. 

## 4. Grounding $\lambda$ in the Persistence Condition

Can we define $\beta_{explore}$ strictly in terms of AAD quantities? 

In IB, $\beta$ is the Lagrange multiplier bounding the representation complexity. In AAD, representation complexity is bounded by $R$ (capacity) and $\alpha$ (efficiency) from `#result-persistence-condition`.

If the agent's uncertainty $U_M$ is high, it is near the boundary of its persistence sector ($R^\ast \approx R$). To avoid destabilization, it *must* increase its update gain $\eta^\ast$. To make high update gain effective, it *must* generate observations with high causal identifiability. 

Therefore, $\lambda(M_t)$ should scale directly with the proximity to the persistence boundary:
$$ \lambda(M_t) \propto \frac{\rho^{\text{eff}}}{\alpha R - \rho^{\text{eff}}} \cdot U_M $$

## 5. Formal Derivation

Let the persistence basin boundary be $R^\ast = \frac{\rho}{\eta^\ast c_{\min}}$ (Model D) or $R^\ast = \frac{\sigma_w}{\sqrt{2\eta^\ast c_{\min}}}$ (Model S). Let $R$ be the structural capacity of the agent.

The agent's viability margin is $\Delta R = R - R^\ast$. If $\Delta R \le 0$, the agent loses persistence (destabilizes). 

As uncertainty $U_M$ increases, $\eta^\ast = \frac{U_M}{U_M + U_o}$ approaches 1. However, if the agent only exploits, it collects data with high observation ambiguity $U_o$, suppressing $\eta^\ast$ and driving $R^\ast$ dangerously close to $R$.

To maximize $\eta^\ast$, the agent must minimize $U_o$. Actions that minimize $U_o$ (producing unambiguous observations) are, by definition, causal interventions with high Causal Information Yield (CIY).

Therefore, the objective of the agent is a constrained optimization problem:
$$ \max_{\pi} \mathbb{E}_{a \sim \pi} [Q_O(a)] $$
$$ \text{subject to } \mathbb{E}_{a \sim \pi} [U_o(a)] \le U_o^{\text{max}}(M_t) $$
where $U_o^{\text{max}}$ is the maximum allowable observation noise that keeps $R^\ast \lt R$. 

Using the KKT conditions, the Lagrangian is:
$$ \mathcal{L} = \mathbb{E}[Q_O(a)] - \lambda \cdot (\mathbb{E}[U_o(a)] - U_o^{\text{max}}) $$

Since $\text{CIY}(a) \propto 1/U_o(a)$, maximizing $-\lambda U_o(a)$ is structurally equivalent to maximizing $+\lambda' \text{CIY}(a)$. 

The optimal Lagrange multiplier $\lambda'$ must scale with the strictness of the constraint. As $R^\ast \to R$ (the agent approaches the brink of destabilization), the constraint becomes infinitely stiff, and $\lambda' \to \infty$. 

Using a first-order Taylor expansion around the stability boundary, the penalty weight $\lambda$ scales proportionally to the inverse margin:
$$ \lambda(M_t) \propto \frac{1}{R - R^\ast} \cdot U_M $$
Since $R^\ast \propto \rho / \alpha$, this yields the exact scaling proposed:
$$ \lambda(M_t) \propto \frac{\rho^{\text{eff}}}{\alpha R - \rho^{\text{eff}}} \cdot U_M $$

## 6. Conclusion
The heuristic tuning parameter $\lambda(M_t)$ in `#disc-ciy-unified-objective` is not arbitrary. It is the exact Lagrange multiplier enforcing the AAD Lyapunov persistence condition ($\alpha R \gt \rho$) on the agent's action policy. As the agent's environment becomes more volatile ($\rho \uparrow$) or its uncertainty grows ($U_M \uparrow$), the persistence constraint forces the agent to abandon pragmatic exploitation ($Q_O$) and prioritize pure interventional exploration (CIY). 

This derivation bridges the pragmatic-epistemic gap without requiring the Active Inference "preferences-as-priors" assumption. It relies purely on the physics of Lyapunov stability.

## 7. Adversarial Critique & Structural Repair (2026-04-25)

**Adversarial Critique:** The derivation proves that survival requires bounding scalar observation noise $U_o$, which forces $\lambda \to \infty$ near the boundary. However, CIY is a property of a *specific action*. If an agent finds *one* safe, low-noise action that is completely orthogonal to the environment's drift (e.g., staring at a blank wall), the scalar math says it can take that action forever to minimize $U_o$ and survive. But staring at a wall teaches the agent nothing about the drifting environment! The scalar reduction collapses the dimensionality of the action space, allowing trivial, non-exploratory solutions to satisfy the math.

**Forward-Pass Repair:** The critique is valid and exposes a weakness in scalarizing multivariate dynamics. The constraint $\mathbb{E}_\pi [U_o(a)] \le U_o^{\max}$ must be formulated over the *information matrix*, not a scalar trace. Staring at a wall reduces variance in an orthogonal direction to the environmental drift. The true Lyapunov constraint must require that the observation matrix spans the specific eigenspace where the disturbance $\rho$ is acting. 
*Fix:* This requires upgrading the KKT Lagrangian from a scalar inequality to a Linear Matrix Inequality (LMI) involving the Fisher Information Matrix. This LMI will mathematically force the agent to choose actions that actively probe the specific dimensions that are drifting, forbidding "blank wall" exploitation.

**Promotion Plan:** 
- The scalar version was already promoted to `01-aad-core/src/deriv-causal-ib-exploration.md` as a first-order derivation.
- To fully formalize the LMI repair, a future update to `#deriv-causal-ib-exploration` should introduce the Fisher Information Matrix constraint. This will also likely require an update to `#def-adaptive-tempo` to handle tensor-valued correction rates properly.

*(End of spike.)*