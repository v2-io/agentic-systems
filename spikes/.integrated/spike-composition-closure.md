# Spike: Composition Closure Criterion

**Status:** Exploratory draft **Context:** This addresses the "Minimum unity for meaningful composition" gap in Section III, formalizing the exact mathematical conditions under which a group of agents can be validly treated as a single composite agent.

## 1. The Core Intuition: Coarse-Graining Agency

In statistical mechanics, the Renormalization Group (RG) provides a formal way to coarse-grain a system: zooming out, grouping micro-components into macro-components, and determining if the macro-components still obey the same equations of state.

In AAD, the composition closure criterion is analogous to RG coarse-graining. We have a set of sub-agents $\{A_i\}_{i=1}^N$, each participating in an interconnected AAD loop. We propose a "macro-agent" $A_c$ (the composite). 

$A_c$ is a valid AAD agent *if and only if* the minimal achievable closure defect $\varepsilon^\ast$—when coarse-graining the full closed-loop dynamics over an admissible class of macro-models—satisfies $\varepsilon^\ast \leq \varepsilon_{max}$ for some validity threshold. Coarse-graining first and then running the macro-loop must yield approximately the same reachable-state trajectory as running the micro-loop and then projecting.

## 2. Formal Setup

Let a system consist of $N$ sub-agents interacting in a shared environment $E$.

**The Micro Closed-Loop System:**
The micro-state, micro-observations, and micro-actions are tuples of all sub-agent components, interacting with a true environment state $\Omega_t \in \mathcal S_{env}$:
$X_{micro, t} = \{ (M_{i,t}, G_{i,t}) \}_{i=1}^N \in \mathcal X_{micro}$ $o_{micro, t} = \{ o_{i,t} \}_{i=1}^N \in \mathcal O_{micro}$ $a_{micro, t} = \{ a_{i,t} \}_{i=1}^N \in \mathcal A_{micro}$

The micro-dynamics form a coupled action-observation loop:
$X_{micro, t} \xrightarrow{\pi_{micro}} a_{micro, t} \xrightarrow{E} (\Omega_{t+1}, o_{micro, t+1}) \xrightarrow{f_{micro}} X_{micro, t+1}$
*(Note: $E$ represents the shared environment transition and observation generation, which couples the agents. $f_{micro}$ is the joint state update.)*

**The Macro Projections and Dynamics:**
We constrain our search to an *admissible class* of projections $\Lambda \in \mathcal P_{adm}$ mapping micro to macro, and an *admissible class* of macro-dynamics $(\pi_c, E_c, f_c) \in \mathcal M_{adm}$:
- $\Lambda_x : \mathcal X_{micro} \to \mathcal X_c = (M_c, G_c)$
- $\Lambda_o : \mathcal O_{micro} \to \mathcal O_c$
- $\Lambda_a : \mathcal A_{micro} \to \mathcal A_c$
- $\Lambda_\Omega : \mathcal S_{env} \to \mathcal S_{env, c}$

The macro closed-loop system is:
$X_{c, t} \xrightarrow{\pi_c} a_{c, t} \xrightarrow{E_c} (\Omega_{c, t+1}, o_{c, t+1}) \xrightarrow{f_c} X_{c, t+1}$

*Without admissibility constraints, closure is trivial (e.g., curve-fitting arbitrary $E_c$ or $f_c$). Admissibility forces the macro-components to retain the structural properties of an AAD agent.*

## 3. Approximate Composition Closure

Rather than a single step, closure must hold over a dynamical horizon. Let $\mathcal D_{micro}$ be the distribution of reachable trajectories generated entirely by the true micro-system interacting with environment $E$ over horizon $H$.

We decompose closure failure into component expected errors averaged over the horizon indices $t \in [1, H]$ for trajectories drawn from $\mathcal D_{micro}$, measuring how well the macro-functions approximate the projected micro-dynamics evaluated at true micro-states:

1. **State Update Closure Error ($\varepsilon_x$):** 
   $\mathbb E_{\tau \sim \mathcal D_{micro}} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_x\big(f_{micro}(X_{micro, t}, o_{micro, t+1})\big) - f_c\big(\Lambda_x(X_{micro, t}), \Lambda_o(o_{micro, t+1})\big) \big\Vert_{\mathcal{X}} \Big]$
2. **Action Closure Error ($\varepsilon_a$):** 
   $\mathbb E_{\tau \sim \mathcal D_{micro}} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_a\big(\pi_{micro}(X_{micro, t})\big) - \pi_c\big(\Lambda_x(X_{micro, t})\big) \big\Vert_{\mathcal{A}} \Big]$
3. **Observation/Environment Closure Error ($\varepsilon_o$):** 
   $\mathbb E_{\tau \sim \mathcal D_{micro}} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_o\big(E_{obs}(\Omega_t, a_{micro, t})\big) - E_{c, obs}\big(\Lambda_\Omega(\Omega_t), \Lambda_a(a_{micro, t})\big) \big\Vert_{\mathcal{O}} \Big]$

*(Note: $E_{obs}$ and $E_{c, obs}$ denote the observation-generating components of the environment transitions. Small component-wise errors guarantee bounded trajectory divergence only if the admissible macro-dynamics $\mathcal M_{adm}$ satisfy appropriate Lipschitz stability conditions. We assume $\mathcal M_{adm}$ is restricted to stable AAD models).*

**Definition (Composition Closure):** We define the **minimal achievable closure defect** $\varepsilon^\ast$ over the admissible classes:
$\varepsilon^\ast = \inf_{\Lambda \in \mathcal P_{adm}, (\pi_c, E_c, f_c) \in \mathcal M_{adm}} \big\Vert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\Vert$

A set of agents $\{A_i\}$ forms a meaningful composite agent $A_c$ if $\varepsilon^\ast \leq \varepsilon_{max}$. 
*(Note: We refer to $\varepsilon^\ast$ operationally as "compositional entropy." It is an evocative label for the aggregate closure defect—an irreducible loss of capability due to being multiple—though its strict information-theoretic form depends on the specific norms chosen.)*

## 4. The Tempo Inequality: $\mathcal T_c \leq \sum \mathcal T_i$

The most powerful consequence of this formalization is the relationship between the aggregate capability of the composite agent and the sum of its parts. 

Let $\mathcal T_i$ be the adaptive tempo of sub-agent $i$. Let $\mathcal T_c$ be the adaptive tempo of the valid composite agent.

**Theorem Sketch (Sub-additive Tempo):** 
For any composite agent $A_c$ with minimal closure defect $\varepsilon^\ast \geq 0$, the composite tempo is bounded by the sum of individual tempos:

$\mathcal T_c \leq \sum_{i=1}^N \mathcal T_i$

We can formally define the **coordination overhead penalty** as the difference:
$C_{\text{coord}}(\varepsilon^\ast) := \Big( \sum_{i=1}^N \mathcal T_i \Big) - \mathcal T_c$

### Proof Intuition:
1. **Tempo is a rate of mismatch correction** ($\nu \cdot \eta^\ast_{\text{eff}}$). 
2. In the best case ($\varepsilon^\ast = 0$), every "tick" of an individual's AAD loop contributes directly to the macro AAD loop without friction. Thus $\mathcal T_c = \sum \mathcal T_i$ and $C_{\text{coord}} = 0$.
3. When $\varepsilon^\ast \gt 0$, closure fails partially. Sub-agents spend a fraction of their individual tempo correcting *internal* mismatches generated by other sub-agents (e.g., Alice changes an API, Bob must spend tempo updating $M_{Bob}$ to understand it), or taking actions that counteract each other.
4. The macro-agent $A_c$ does not gain adaptive advantage against the *external* environment from these internal reconciliation cycles. These cycles are consumed by $C_{\text{coord}}(\varepsilon^\ast)$.

### Equality Conditions ($\mathcal T_c = \sum \mathcal T_i$):
Strict equality implies $C_{\text{coord}} = 0$, requiring (as sufficient conditions):
1. **Orthogonal Routing:** The information dependency DAG exactly matches organizational boundaries (no costly cross-talk).
2. **Perfect Shared Intent:** No tempo is lost to internal negotiation or conflicting pursuit of $O_t$.
3. **No Net Macro-Information Loss:** Observations may be redundant, but they do not result in wasted tempo after fusion, nor is critical macro-information lost during coordination.

## 5. Connections to the Rest of AAD

*   **Persistence Threshold ( #der-team-persistence):** $\varepsilon^\ast$ is a closure error, not a persistence condition itself. However, it mediates persistence. A composite agent survives if its aggregate tempo overcomes the external environment change rate: $\mathcal T_c \gt \rho_{ext} / \Vert\delta_{crit}\Vert$. Because $\mathcal T_c = \sum \mathcal T_i - C_{\text{coord}}(\varepsilon^\ast)$, high closure defect drains tempo, which can push the macro-agent below the persistence threshold, causing it to disintegrate as a coherent entity.
*   **Unity Dimensions as Predictors:** The previously defined qualitative unity dimensions serve as predictors or bounds for the component closure errors. High Epistemic Unity ($U_M$) predicts low $\varepsilon_M$. High Teleological Unity ($U_O$) strongly predicts low $\varepsilon_G$. High Strategic Unity ($U_\Sigma$) strongly predicts low $\varepsilon_a$. Finally, high Perceptual Unity (shared observation functions/routing) strongly predicts low $\varepsilon_o$.
*   **Information Bottleneck ( #def-shared-intent):** The projection function $\Lambda_x$ can be analyzed or chosen via an Information Bottleneck objective. It compresses micro-states into a macro-state, where the $\beta$ parameter dictates how much micro-variance is discarded as irrelevant to the macro-dynamics.
*   **Software Teams (Section IV):** Brooks's Law / Conway's Law are domain consequences of the closure criterion. If code modularity forces $\Lambda_x$ to blend highly coupled states across team boundaries, $\varepsilon^\ast$ spikes, $C_{\text{coord}}$ dominates, and adding developers ($\sum \mathcal T_i$) fails to increase—or even decreases—overall team tempo $\mathcal T_c$.

## 6. Next Steps for Canonicalization
1. Formalize the exact mathematical structure of the admissible classes $\mathcal P_{adm}$ and $\mathcal M_{adm}$.
2. Formalize the map connecting the unity dimensions ($U$) to the closure error bounds ($\varepsilon^\ast$).
3. Detail the specific functional form of $C_{\text{coord}}(\varepsilon^\ast)$ and derive its monotonic relationship with closure defect.
4. Provide the formal bridge lemma connecting expected component closure errors to bounded trajectory rollout divergence over horizon $H$.