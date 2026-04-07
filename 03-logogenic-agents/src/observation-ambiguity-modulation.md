---
slug: observation-ambiguity-modulation
type: scope
status: conditional
depends:
  - ai-agent-as-act-agent
  - coupled-update-dynamics
  - directed-separation
  - section-ii-survival
  - mismatch-signal
stage: draft
---

# Scope: Observation Ambiguity Modulation

The approximation error of Section II results for Class 2 agents depends on the product $\kappa_{\text{processing}} \times \mathcal{A}(e_\tau)$, not on $\kappa_{\text{processing}}$ alone. Observation ambiguity $\mathcal{A}(e_\tau)$ measures how much the observation's epistemic content depends on the agent's goals. Binary, verifiable observations (test pass/fail, deployment success, measurable metrics) have low ambiguity — their meaning is goal-independent — and limit the damage from goal-conditioned processing. Ambiguous observations (code quality assessments, strategic evaluations, user intent) have high ambiguity and are where directed-separation violations have maximal impact.

## Formal Expression

*[Definition (observation-ambiguity)]*

The **observation ambiguity** of event $e_\tau$ with respect to the agent's goal state:

$$\mathcal{A}(e_\tau) = \frac{I(G_t \,;\, M_{\tau^+} \mid e_\tau,\, M_{\tau^-},\, \kappa = 1)}{H(M_{\tau^+} \mid e_\tau,\, M_{\tau^-},\, \kappa = 0)}$$

The numerator is the mutual information between goals and the epistemic update *in the fully merged case* — how much goal-knowledge changes the beliefs formed from this observation. The denominator normalizes by the total epistemic update in the fully separated case — how much the observation changes beliefs when processing is goal-blind.

- $\mathcal{A}(e_\tau) \approx 0$: the observation's epistemic content is **goal-independent**. The same beliefs are formed regardless of the agent's goals. Examples: a test either passes or fails; a compiler error has a specific message; a file exists or does not.
- $\mathcal{A}(e_\tau) \approx 1$: the observation's epistemic content is **fully goal-dependent**. Different goals produce systematically different beliefs from the same observation. Examples: a code review comment could be interpreted as "minor style issue" or "critical design flaw" depending on whether the agent's goal is "ship fast" versus "ensure correctness."

*[Scope Condition (ambiguity-modulation)]*

The effective coupling — the degree to which directed-separation violation affects the epistemic update quality — is the product:

$$\kappa_{\text{eff}}(e_\tau) = \kappa_{\text{processing}} \cdot \mathcal{A}(e_\tau)$$

This is the quantity that governs the approximation error for the five approximately-surviving Section II results ( #section-ii-survival). The epistemic bias is bounded by:

$$\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{eff}}(e_\tau) \cdot H(G_t \mid M_{\tau^-})$$

**Consequence for the survival classification.** A Class 2 agent ($\kappa_{\text{processing}} \approx 1$) operating in a domain with low observation ambiguity ($\mathcal{A}(e_\tau) \ll 1$ for most events) has:

$$\kappa_{\text{eff}} \approx \mathcal{A}(e_\tau) \ll 1$$

In such domains, the Section II results classified as "approximately surviving" become *good approximations* despite the agent being fully merged. The directed-separation violation is real but inconsequential because the observations carry minimal interpretive latitude.

*[Scope Condition (domain-classification)]*

Domains can be classified by their typical observation ambiguity, which determines how much of Section II's machinery is directly applicable to Class 2 agents operating in that domain:

| Domain class | Typical $\mathcal{A}$ | Section II applicability | Examples |
|---|---|---|---|
| **Low ambiguity** | $\mathcal{A} \ll 1$ | Section II approximately exact even for Class 2 | Software with comprehensive tests, manufacturing with precise sensors, formal verification |
| **Mixed ambiguity** | $\mathcal{A}$ varies by observation type | Section II reliable for verifiable observations, degraded for interpretive ones | Software development (tests are low-$\mathcal{A}$, code reviews are high-$\mathcal{A}$), clinical medicine (lab results vs. symptom interpretation) |
| **High ambiguity** | $\mathcal{A} \approx 1$ | Section II results significantly degraded for Class 2 | Organizational strategy, intelligence analysis, creative evaluation, philosophical reasoning |

### The $\kappa_{\text{processing}}$ operationalization

*[Definition (kappa-processing-operationalization)]*

For LLM-based agents, $\kappa_{\text{processing}}$ ( #directed-separation) can be operationalized empirically:

$$\hat\kappa_{\text{processing}} = \frac{1}{\lvert\mathcal{E}_{\text{test}}\rvert} \sum_{e \in \mathcal{E}_{\text{test}}} \frac{d(M_{\tau^+}^{(G_1)}(e),\; M_{\tau^+}^{(G_2)}(e))}{d_{\text{max}}(e)}$$

where:
- $M_{\tau^+}^{(G_1)}(e)$ and $M_{\tau^+}^{(G_2)}(e)$ are the epistemic components of the agent's response to event $e$ under two different goal states $G_1$ and $G_2$
- $d(\cdot, \cdot)$ is a distance measure on the epistemic content (e.g., semantic similarity of the "what I learned" portions of the response)
- $d_{\text{max}}(e)$ normalizes by the maximum observed divergence for event $e$
- $\mathcal{E}_{\text{test}}$ is a representative set of events

This is a behavioral proxy: present the same observation to the agent under different goals and measure how much the epistemic content of the response changes. A perfectly modular agent ($\kappa = 0$) would produce identical epistemic content regardless of the goal. A fully merged agent produces goal-dependent epistemic content.

Similarly, the ambiguity of a specific observation can be estimated by the same procedure, holding $\kappa$ fixed (which, for an LLM, means using the same model):

$$\hat{\mathcal{A}}(e_\tau) = \frac{\text{Var}_{G}[M_{\tau^+}^{(G)}(e_\tau)]}{\text{Var}_e[M_{\tau^+}^{(G_{\text{fixed}})}(e)]}$$

The numerator measures how much the epistemic update varies across goals for a fixed observation; the denominator normalizes by how much it varies across observations for a fixed goal.

## Epistemic Status

*Conditional.* The core claim — that approximation error depends on $\kappa \times \mathcal{A}$, not $\kappa$ alone — is structurally motivated and consistent with all examples analyzed in the survival analysis (`msc/spike-coupled-survival-analysis.md`). The multiplicative structure is the simplest form consistent with the boundary conditions ($\mathcal{A} = 0 \Rightarrow$ no error regardless of $\kappa$; $\kappa = 0 \Rightarrow$ no error regardless of $\mathcal{A}$). However, the multiplicative form is not derived — it is the simplest interpolation between the boundary cases. The actual error structure could be nonlinear (e.g., $\kappa^a \cdot \mathcal{A}^b$ with $a, b \neq 1$), and the interaction between coupling and ambiguity could involve threshold effects rather than smooth scaling.

The domain classification (low/mixed/high ambiguity) is robust-qualitative — the examples are well-motivated and the categories are useful for engineering guidance. The specific operational definitions ($\hat\kappa$, $\hat{\mathcal{A}}$) are measurement proposals, not validated instruments.

Max attainable: conditional. The multiplicative structure could potentially be derived from the information geometry of the observation channel, relating $\mathcal{A}(e_\tau)$ to the Fisher information of the observation with respect to $G_t$. This would require a specific model of how goal-conditioning enters the likelihood function — feasible in principle but not attempted.

## Discussion

**Why ambiguity matters more than coupling.** For LLM-based agents, $\kappa_{\text{processing}} \approx 1$ is architectural — it cannot be reduced without changing the architecture (e.g., from a single LLM to a modular system). But $\mathcal{A}(e_\tau)$ is a property of the *domain and observation design*, which is under the system designer's control. The practical lever for making Section II results applicable to LLM agents is not reducing $\kappa$ (which requires architectural changes) but reducing $\mathcal{A}$ (which requires better observation design): more tests, more precise metrics, more structured outputs, less reliance on interpretive judgments.

**The software domain advantage.** Software development is a mixed-ambiguity domain with an unusually high proportion of low-ambiguity observations: tests pass or fail, linters report specific violations, type checkers give precise errors, deployments succeed or fail, metrics are numerical. This makes software a favorable domain for applying ACT's Section II machinery to LLM agents — the goal-conditioning effects are limited to the interpretive observations (code review, architectural assessment, requirement interpretation). The low-ambiguity observations anchor the agent's epistemic state in goal-independent reality, limiting the damage from goal-conditioned interpretation of the ambiguous observations.

**Goal-conditioned ambiguity as motivated reasoning.** High $\mathcal{A}(e_\tau)$ with high $\kappa_{\text{processing}}$ is the formal characterization of motivated reasoning: the agent's goals shape how it interprets evidence. An LLM agent reading code with goal "ship the feature today" may downweight evidence of bugs that would delay shipping. The $\kappa \times \mathcal{A}$ framework quantifies this: the motivated reasoning is maximal when the observation is ambiguous ($\mathcal{A} \approx 1$) and the processing is fully merged ($\kappa \approx 1$). It vanishes when the observation is unambiguous ($\mathcal{A} \approx 0$) — a test failure is a test failure regardless of the agent's shipping deadline.

**Relationship to Section I quantities.** The mismatch signal $\delta_t$ ( #mismatch-signal) is defined on observable prediction error. For low-ambiguity observations, $\delta_t$ is goal-independent (the prediction error is what it is). For high-ambiguity observations, the *prediction* itself may be goal-conditioned (the agent's expectation about what it will observe depends on what it hopes to observe), introducing bias into $\delta_t$. This means that even Section I quantities, while formally well-defined regardless of coupling, can be *effectively biased* by goal-conditioning in high-ambiguity domains. The ambiguity modulation applies not just to Section II's survival but to the practical accuracy of Section I's quantities in coupled architectures.

## Working Notes

- The information-geometric derivation path: if observations lie in a space $\mathcal{O}$ and the agent's likelihood model is $P(o \mid M, G)$, then ambiguity could be defined via the Fisher information: $\mathcal A(e) \propto \text{tr}(\mathcal I_G(e)) / \text{tr}(\mathcal I_M(e))$, where $\mathcal I_G$ and $\mathcal I_M$ are the Fisher information matrices with respect to $G$ and $M$ respectively. This would make the definition intrinsic to the observation model rather than dependent on the processing architecture. Worth pursuing if the logogenic agent theory develops further.
- The domain classification (low/mixed/high) is coarse. A finer classification would characterize the *distribution* of $\mathcal{A}$ across the observation stream: what fraction of events are low-ambiguity, what fraction are high-ambiguity, and how the agent's strategy depends on each type. In a software domain, the high-ambiguity observations (code review, architecture decisions) are often the most *strategically important* ones, creating a worst-case correlation between ambiguity and strategic significance.
- The operationalization $\hat\kappa$ requires running the same observation through the agent with different goals. For LLM agents, this is feasible as an offline diagnostic (feed the same tool output with different system prompts). It cannot be computed online during normal operation because the agent has only one goal at a time.
