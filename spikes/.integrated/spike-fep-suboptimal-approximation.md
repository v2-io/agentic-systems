# Spike: The Free Energy Principle as a Sub-Optimal Approximation

**Status.** Exploratory research spike.
**Date.** 2026-04-25.
**Pressure Point.** The Agentic Systems Framework (AAT) frequently contrasts itself with Active Inference and the Free Energy Principle (FEP) (e.g., `#disc-ciy-unified-objective`, `#def-satisfaction-gap`). The core claim is that AAT's strict separation of Pragmatic Value ($Q_O$) and Epistemic Exploration (CIY) avoids FEP's "dark room problem" (encoding preferences as priors). 

This spike attempts to formally mathematically derive Friston's Expected Free Energy (EFE) directly from the AAT Lagrangian. By showing exactly which mathematical constraints must be incorrectly forced onto AAT to recover EFE, we can definitively prove that Active Inference is a mathematically sub-optimal projection of AAT.

## 1. The AAT Baseline

From the Causal-IB LMI derivation (`#deriv-causal-ib-exploration` / `spike-causal-ib-lmi-repair`), the optimal AAT action policy maximizes the Lagrangian:
$$ \mathcal{L}_{\text{AAT}}(a) = \mathbb{E}[Q_O(a)] + \text{Tr}\left( \Lambda \cdot \mathcal{I}_o(a) \right) $$
Where:
- $Q_O(a)$ is the expected pragmatic value of the action (based on the value functional $O_t$).
- $\mathcal{I}_o(a)$ is the interventional Fisher Information Matrix (measuring causal information yield).
- $\Lambda \succeq 0$ is the matrix Lagrange multiplier enforcing the Lyapunov survival bound ($\lambda_{\max}(\Sigma_\delta) < R^2$).

Crucially, $\Lambda$ only has non-zero eigenvalues in the specific state-space directions where environmental disturbance ($\rho$) is pushing the agent near its capacity limit $R$.

## 2. The Active Inference Baseline

In Active Inference, an agent acts to minimize Expected Free Energy $G(\pi)$ over future trajectories. The standard decomposition of EFE (e.g., Parr & Pezzulo 2022) is:
$$ -G(\pi) = \underbrace{\mathbb{E}_{Q(o \mid \pi)} [\log P_{\text{pref}}(o)]}_{\text{Pragmatic Value}} + \underbrace{\mathbb{E}_{Q(s \mid \pi)} [H(o \mid s) - H(o \mid s, \pi)]}_{\text{Epistemic Value (EIG)}} $$

To minimize Free Energy, the agent maximizes the sum of:
1. The expected log-probability of achieving its preferred sensory states.
2. The Expected Information Gain (EIG) about hidden states (resolving uncertainty).

## 3. Deriving EFE from AAT (The Three Fatal Assumptions)

We can recover the exact EFE functional from the AAT Lagrangian, but *only* if we force the AAT agent to adopt three highly restrictive, sub-optimal structural assumptions:

### Assumption 1: The "Dark Room" Collapse (Teleological Degeneracy)
AAT defines $O_t$ as a functional over arbitrary state trajectories. To recover EFE, we must force the agent to encode its goals exclusively as a static prior probability distribution over immediate sensory observations:
$$ Q_O(a) \equiv \mathbb{E}_{P(o \mid do(a))} [\log P_{\text{pref}}(o)] $$
*Why this is sub-optimal:* This forces the agent's purposeful state ($G_t$) into the same mathematical coordinate space as its epistemic state ($M_t$). This creates the Dark Room problem: the agent cannot mathematically distinguish between "I achieved my goal" and "I lowered my expectations to match reality." AAT's `#def-satisfaction-gap` proves this distinction is diagnostically vital.

### Assumption 2: Uniformly Catastrophic Volatility (Resource Waste)
In AAT, the exploration drive is targeted: the trace product $\text{Tr}(\Lambda \cdot \mathcal{I}_o)$ only rewards information gathering in dimensions where survival is threatened. 
To recover EFE, we must assume the environment's drift covariance $Q_\rho$ is perfectly isotropic and infinite in all directions, meaning the agent is constantly on the brink of death from every possible angle. Under this assumption, the shadow price matrix becomes a scalar identity matrix: $\Lambda \to \lambda I$.
The trace product collapses:
$$ \text{Tr}(\lambda I \cdot \mathcal{I}_o) = \lambda \cdot \text{Tr}(\mathcal{I}_o) \propto \text{Total Information Gain} $$
*Why this is sub-optimal:* EFE forces the agent to maximize *all* information gain (EIG) indiscriminately. An AAT agent knows that gathering information about safe, stable dimensions is a waste of tempo ($\mathcal{T}$). EFE agents over-explore irrelevant state spaces.

### Assumption 3: Causal Blindness (Level 1 $\equiv$ Level 2)
EFE computes Epistemic Value using standard Shannon mutual information based on the agent's generative model (Pearl Level 1: Associational). AAT computes Causal Information Yield (CIY) using the interventional Fisher Information Matrix (Pearl Level 2: Interventional).
To recover EFE, we must assume that the agent's actions perfectly screen off all back-door confounders, meaning $P(o \mid a) \equiv P(o \mid do(a))$. 
*Why this is sub-optimal:* As proven in `#der-causal-insufficiency-detection`, this assumption is false for any complex strategy DAG with latent common causes. An EFE agent will confidently execute actions that are merely correlated with good outcomes, while an AAT agent will specifically seek interventions that isolate the causal mechanism.

## 4. Conditional Objective Comparison

*[Candidate Formulation]*

If we apply these three constraints to the AAT Lagrangian, we recover a form resembling negative Expected Free Energy:
$$ \mathcal{L}_{\text{AAT}}^{\text{constrained}}(a) = \mathbb{E}[\log P_{\text{pref}}(o)] + \lambda \cdot \text{EIG}(a) \equiv -G(a) $$

**Candidate Hypothesis (FEP Objective Mapping):** Active Inference's Expected Free Energy (EFE) minimization can be mathematically recovered from AAT's survival Lagrangian under specific structural restrictions: (1) preferences encoded as priors, (2) uniform/scalar epistemic pricing, and (3) associational rather than interventional dynamics.

While claiming EFE is "strictly suboptimal" is an overreach—since advanced active-inference variants can include epistemic value and richer generative models—this mapping clarifies exactly *which* architectural constraints separate default AAT from default FEP.

## 5. Conclusion and Recommended Moves

This spike refines AAT's positioning against Active Inference, moving from a philosophical critique to a specific set of testable structural restrictions required to map one objective to the other.

**Recommended Moves:**
- Keep this spike as a post-causal-IB positioning note.
- Do not promote as a "dominance theorem". The best landing would be a small discussion addendum in `#disc-ciy-unified-objective` noting that EFE-like objectives are recovered under specific restrictions (preferences-as-priors, scalar epistemic price).
- Wait for the causal-IB LMI work to settle before any formal integration.

*(End of spike.)*