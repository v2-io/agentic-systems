---
slug: schema-strategy-persistence
type: proposed-schema
status: sketch
depends:
  - result-sector-condition-stability
  - result-sector-persistence-template
  - def-strategic-calibration
  - def-strategy-dag
stage: draft
---

# Proposed-schema: Strategy Persistence Schema

The sector-persistence template ( #result-sector-persistence-template) proves bounded state for any system with a state variable, a correction function satisfying the sector condition, and bounded disturbance. The template is domain-agnostic — it applies to any state variable meeting its preconditions (T1)–(T3). This schema is the strategic-layer instantiation: if strategic update dynamics satisfy the template's preconditions, strategy persistence follows as a direct instance. A key additional requirement — absent from the epistemic instantiation but load-bearing here — is **experience discounting**, because the strategic sector parameter $\alpha_\Sigma$ decays monotonically with experience and requires an explicit forgetting mechanism to remain bounded below.

## Formal Expression

*[Proposed Schema (strategy-persistence-schema, from sector-persistence-template)]*

**If** strategic update dynamics satisfy the template preconditions (T1)–(T3) of #result-sector-persistence-template for $\xi = \delta_\Sigma$ (a strategic mismatch state), together with:

- **(SA1)** Zero correction at zero strategic mismatch (the template's (T1)): when the mismatch state is zero, no revision occurs
- **(SA2')** Local sector condition on strategic correction (the template's (T2) for $\xi = \delta_\Sigma$): the correction function points inward with baseline efficiency $\alpha_\Sigma$ within a strategic reserve $R_\Sigma$
- **(SA3)** Sufficient exploration (OR-nodes only): the action selection policy allocates correction capacity to all OR alternatives at a rate exceeding the strategic disturbance-to-reserve ratio
- Bounded strategic disturbance at rate $\rho_\Sigma$ (the template's (T3)): the rate at which the environment invalidates causal links is bounded

**Then** $\Sigma_t$ persists iff:

$$\alpha_\Sigma \gt \frac{\rho_\Sigma}{R_\Sigma}$$

directly by the template's Model D result. Here $\alpha_\Sigma$ is the strategic correction rate, $\rho_\Sigma$ is the strategic disturbance rate, and $R_\Sigma$ is the strategic reserve (tolerance for strategic mismatch before performance degrades catastrophically). The Model S instantiation replaces $\rho_\Sigma$ with $\sigma_\Sigma$ and gives $\alpha_\Sigma \gt n\sigma_\Sigma^2/(2R_\Sigma^2)$ under the same template.

### Forgetting as Prerequisite

*[Formulation (forgetting-prerequisite)]*

The schema form above is an **instantaneous persistence check at the current experience level**, not a trajectory guarantee. For Beta-Bernoulli edge updates (the canonical verified case; see #deriv-edge-credence-dynamics Props B.1–B.6), the sector parameter has the form:

$$\alpha_\Sigma = \frac{1}{n+1}$$

where $n$ is the edge's accumulated experience (pseudo-count). Without a forgetting mechanism, $n$ grows monotonically with each observation, so $\alpha_\Sigma \to 0$ for every edge asymptotically. For any fixed $(\rho_\Sigma, R_\Sigma)$ with $\rho_\Sigma \gt 0$, every agent eventually violates the threshold. The structural identity with #result-persistence-condition — where $\alpha$ can be stationary — holds for the strategic case only under an explicit forgetting mechanism.

**Exponential forgetting.** Replace the raw Beta-Bernoulli update with a discounted update: at each step, shrink the pseudo-counts by a factor $\lambda \in (0,1)$:

$$\alpha_k \mapsto \lambda\,\alpha_k + y_k, \qquad \beta_k \mapsto \lambda\,\beta_k + (1-y_k)$$

The effective sample size stabilizes at $n_{\text{eff}} \approx 1/(1-\lambda)$, giving steady-state sector parameter:

$$\alpha_\Sigma^{\text{ss}} \approx 1 - \lambda$$

**The forgetting prerequisite.** Combining with the schema's persistence form:

$$(1 - \lambda) \gt \frac{\rho_\Sigma}{R_\Sigma} \quad\Longleftrightarrow\quad \lambda \lt 1 - \frac{\rho_\Sigma}{R_\Sigma}$$

This is a **prerequisite of the schema's trajectory guarantee, not a tunable heuristic**. An agent without forgetting has no long-run strategic persistence regardless of its initial $\alpha_\Sigma$. The forgetting rate $(1-\lambda)$ must exceed the disturbance-to-reserve ratio, or the instantaneous persistence check — no matter how comfortably it holds at any given time — eventually fails as experience accumulates.

The strategic analog of #result-persistence-condition's linear operational form is therefore:

$$(1 - \lambda) \gt \frac{\rho_\Sigma}{R_\Sigma}$$

playing the role that $\mathcal{T} \gt \rho / \lVert\delta_{\text{critical}}\rVert$ plays for the epistemic case. The forgetting rate $(1-\lambda)$ is the strategic analog of adaptive tempo: faster forgetting means faster tracking but noisier estimates; slower forgetting means stable estimates but slower tracking. The optimal $\lambda$ balances bias and variance for the specific $\rho_\Sigma$ the environment presents.

**Which mismatch state?** The schema applies to any mismatch state for which conditions (SA1)-(SA3) can be verified. Two candidates exist:

- **Strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$: the scalar difference between the agent's strategy-plan-confidence score and the independence-model plan value at true edge parameters. This is the mismatch for which persistence IS proved (Props B.1-B.5 in #deriv-edge-credence-dynamics). It is computable from status propagation without credit assignment. **Scope:** $\delta_s$ operates at L0 of the Correlation Hierarchy ( #def-strategy-dag) — it tracks calibration within the independence model. For L1 (augmented DAG), the same persistence result applies to the augmented graph's $\hat P_\Sigma$. The gap between L0's $\Phi$ and actual plan success under correlated failure is a model-class limitation, not an estimation error.
- **Strategic-calibration residual** $\delta_{\text{strategic}}$: the per-edge value-increment residual aggregation defined in #def-strategic-calibration. This is the mismatch the orient cascade ( #der-orient-cascade) uses for edge-level revision. Persistence of $\delta_{\text{strategic}}$ remains **open** and requires the credit-assignment machinery in #disc-credit-assignment-boundary.

The verified instances below all use per-edge credence error $\boldsymbol\delta_c = (\hat p_k - \theta_k)$ or the plan-level surrogate $\delta_s$. They do not verify the schema for $\delta_{\text{strategic}}$ directly.

## Epistemic Status

*Sketch, with verified instances.* This is a **result schema**, not a proven result in the general case. The mathematical template (sector conditions → bounded mismatch) is derived ( #deriv-sector-condition). What was missing was instantiation — showing that specific strategic update dynamics satisfy the template's preconditions. Four cases have now been verified (full derivations in #deriv-edge-credence-dynamics):

1. **Single edge, Beta-Bernoulli** ($A \to G$): Sector condition satisfied globally with $\alpha_\Sigma = 1/(n+1)$. The bound is tight (expected correction is exactly linear). (A1) satisfied. Persistence condition: $1/(n+1) \gt \rho_\Sigma / R_\Sigma$.

2. **Two-edge chain, observable intermediate** ($A \to B \to G$, $B$ observable): Sector condition satisfied globally with $\alpha_\Sigma = \min(1/(n_1+1), \theta_1/(n_2+1))$ — a weakest-link result. Correction function is diagonal (no cross-edge coupling). (A1) satisfied. The $\theta_1$ factor in edge 2's rate is the evidence-starvation effect.

3. **Two-edge chain, unobservable intermediate** ($A \to B \to G$, $B$ not observable): Per-edge sector condition **fails** — the marginal Bayesian update violates (A1) with bias $O(1/n)$. But plan-level tracking (treating $\hat{\Phi} = p_1 p_2$ as a single Beta) recovers the sector condition with $\alpha_{\Sigma,\text{plan}} = 1/(n_\Phi + 1)$, at the cost of per-edge diagnostic resolution.

4. **Two-arm OR-node, $\varepsilon$-greedy** ($A_1, A_2 \to G$, $G$ is OR): Sector condition satisfied with $\alpha_\Sigma = \min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$ — an **exploration-gated** weakest-link, not depth-gated as in AND chains. (SA3) required: minimum exploration rate $\varepsilon \gt \rho_\Sigma(n_{\max}+1)/R_\Sigma$. Pure greedy ($\varepsilon = 0$) **fails** the sector condition. With optimal equal-rate allocation, $\alpha_\Sigma = 1/(n_1 + n_2 + 2)$ — the correction capacity is split across alternatives.

The schema is no longer purely hypothetical. The sector parameter for strategic dynamics is the edge update gain $\eta_{\text{edge}}$ — the same quantity that governs epistemic persistence. The structural parallel between epistemic and strategic persistence is not an analogy but a mathematical identity at the sector-framework level.

## Discussion

**What's needed to promote this from schema to result.**

1. **Strategic mismatch state**: partially resolved. Prop B.5 in #deriv-edge-credence-dynamics shows the sector condition transfers from per-edge credence error to **strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$ — the scalar difference between the agent's strategy-plan-confidence score and the independence-model plan value at true edge parameters (note: $\Phi$ is NOT actual plan success probability under correlated failure — see #def-strategy-dag edge-independence caveat). For linear correction (Beta-Bernoulli), the transfer is exact ($\alpha_s = \alpha_c$); for nonlinear correction, $\alpha_s \geq \alpha_c / \kappa(\mathbf{J})^2$. **However**, $\delta_s$ is distinct from the **strategic-calibration residual** $\delta_{\text{strategic}}$ defined in #def-strategic-calibration, which is an $L^2$ aggregation of per-edge value-increment residuals requiring credit assignment to compute. Persistence of $\delta_s$ (plan-level tracking) is proved; persistence of $\delta_{\text{strategic}}$ (per-edge diagnostics) remains open and requires the credit-assignment machinery in #disc-credit-assignment-boundary.

2. ~~**Strategic correction function**: needs to satisfy the sector condition.~~ **Resolved** for Beta-Bernoulli edges. Props B.1-B.4 in #deriv-edge-credence-dynamics verify the sector condition for four topologies (single edge, two-edge AND observable/unobservable, two-arm OR).

3. **Strategic disturbance**: The rate at which the environment invalidates causal links in $\Sigma_t$. **Still open** as a formalized quantity — currently a domain parameter ($\rho_\Sigma$), analogous to how $\rho$ for epistemic disturbance is a domain parameter in #result-persistence-condition.

4. ~~**Sector condition verification**: the critical mathematical step.~~ **Resolved** for four topologies. See #deriv-edge-credence-dynamics.

5. ~~**Credit assignment / signal function**: needed for edge updates.~~ **Characterized at the theory level.** #disc-credit-assignment-boundary shows persistence does not require credit assignment (Prop B.5), establishes directional fidelity as the minimal requirement, and provides a gradient-based default signal function. The specific update algorithm is domain engineering, not theory — the same way the gain *estimator* is domain engineering while the gain *principle* ($\eta^\ast = U_M/(U_M + U_o)$) is theory. Caveat: the default gradient signal inherits $\hat P_\Sigma$'s overestimation bias under correlated failures ( #def-strategy-dag, #disc-credit-assignment-boundary).

6. **Time-varying $\alpha_\Sigma$**: this is where the strategic case genuinely differs from the epistemic one. For Beta-Bernoulli edges, $\alpha_\Sigma = 1/(n+1)$ decays monotonically with experience, so the sector-persistence template's constant-$\alpha$ precondition cannot hold asymptotically under any raw Bayesian update. The resolution is the **forgetting prerequisite** promoted into the Formal Expression above: exponential forgetting with $(1-\lambda) \gt \rho_\Sigma / R_\Sigma$ stabilizes $\alpha_\Sigma$ at $1-\lambda$ and converts the schema's instantaneous check into a trajectory guarantee. This is structural, not heuristic — without forgetting, the schema's form holds only until the agent accumulates enough experience to cross below threshold.

**The structural parallel is genuine, but conditional on forgetting.** This schema extends *structural persistence* (see Persistence in `LEXICON.md`) from the epistemic substate to the strategy substate — asking whether the strategy correction machinery can outpace the rate at which the environment invalidates the agent's causal theory. It inherits the same limitation: structural persistence of $\Sigma_t$ does not address operational persistence (how close $\lVert\delta_{\text{strategic}}\rVert$ is to $R_\Sigma$) or continuity persistence (whether the agent's strategic identity coheres through time). The persistence condition for $M_t$ ( #result-persistence-condition) says: adaptive tempo must exceed the ratio of disturbance to critical mismatch. If the same mathematics applies to $\Sigma_t$, then strategy persistence requires strategic tempo to exceed the ratio of strategic disturbance to critical strategic mismatch. The strategic analog of "the environment changes faster than the agent can learn" is "the world invalidates plans faster than the agent can revise them." Both lead to the same catastrophic outcome: the system cannot maintain bounded mismatch and begins to degrade.

**What this would buy the theory.** If promoted to a result, strategy persistence would:
- Provide a formal criterion for "when does a strategy remain viable?"
- Connect strategic failure modes to the same mathematical framework as epistemic failure modes
- Enable quantitative comparison: is the bottleneck epistemic persistence (model can't keep up with reality changes) or strategic persistence (plans can't keep up with requirement changes)?
- Ground the organizational intuition that plans need to be revised faster than the situation changes

## Findings

### The Forgetting Prerequisite for Strategic Persistence

**Brief:** With infinite memory, standard Bayesian updating guarantees eventual strategic failure. The sector parameter for Beta-Bernoulli edge updates is $\alpha_\Sigma = 1/(n+1)$, which decays monotonically as experience $n$ accumulates. For any positive disturbance rate, the persistence threshold $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$ is eventually violated regardless of the agent's initial calibration. Exponential forgetting with discount factor $\lambda$ stabilizes the effective sample size at $1/(1-\lambda)$, giving steady-state $\alpha_\Sigma \approx 1-\lambda$. The forgetting prerequisite — $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ — converts the schema's instantaneous persistence check into a trajectory guarantee. Forgetting is therefore a structural prerequisite, not a tunable heuristic: the rate at which the agent discounts old evidence must exceed the rate at which the environment invalidates plans.

**Impact:** Translates an organizational platitude ("stay adaptive") into a quantitative survival inequality with explicit failure mode. Identifies a structural calcification process common to all long-running adaptive systems whose update mechanism accumulates evidence: institutional rigidity, RL value-function staleness, scientific-paradigm lock-in, and the loss-of-edge phenomenon in incumbent firms all instantiate the same dynamic. The threshold is sharp — no amount of prior learning protects against an environment that invalidates plans faster than the agent forgets. For long-lived AI agents this mandates explicit memory-pruning mechanisms; the design choice is not whether to forget but at what rate. The structural identity with `#result-persistence-condition` (where $\alpha$ can be stationary) is recovered for the strategic case *only* under explicit forgetting, which is itself a non-obvious finding about the asymmetry between epistemic and strategic dynamics.

**Novelty Claim:** *Claim differentiation* on Bayesian update dynamics with experience discounting. The Beta-Bernoulli decay $\alpha = 1/(n+1)$ is elementary and the forgetting-factor remedy is standard adaptive-control / online-learning practice. The AAD-distinctive contribution is the connection from these standard mechanics to a *survival inequality with environment-side parameters* (disturbance rate, reserve), making forgetting a structural prerequisite of strategic persistence rather than a hyperparameter. The threshold $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ is the strategic analog of the linear operational form of the persistence condition, with $(1-\lambda)$ playing the role of adaptive tempo.

**Related Work:**

| ASF Concern | Prior-art Language | Relationship / Positioning |
|---|---|---|
| Exponential forgetting / discounted least squares | Ljung 1987 *System Identification: Theory for the User*, MIT Press (published 1987, found pre-2026) | *formal antecedent* — supplies the discounted-update mechanism; AAD adopts it directly and connects it to a survival threshold |
| Plasticity/stability tradeoff in continual learning | Kirkpatrick et al. 2017 *Overcoming Catastrophic Forgetting in Neural Networks*, PNAS 114(13) (published 2017, found pre-2026) | *conceptual precursor* — frames the same tradeoff at the network-weight level; does not connect to a Lyapunov-style survival inequality with environment parameters |
| Drift detection in streaming learning | Gama et al. 2014 *A Survey on Concept Drift Adaptation*, ACM Computing Surveys 46(4) (published 2014, found pre-2026) | *conceptual precursor* — recognizes the need to track changing distributions; does not formalize "forgetting rate must exceed disturbance-to-reserve ratio" as a structural prerequisite |
| Requisite variety as cybernetic principle | Ashby 1956 *An Introduction to Cybernetics* §11; Conant & Ashby 1970 (published 1956/1970, found pre-2026) | *conceptual precursor* — the regulator's variety must match the disturbance's variety; AAD's forgetting prerequisite is a quantitative time-domain analog applied to the strategic substate |
| Organizational "core rigidities" / competency traps | Leonard-Barton 1992 *Strategic Management Journal* 13:111; Levitt & March 1988 *Annual Review of Sociology* 14:319 (published 1988/1992, found pre-2026) | *conceptual precursor* — qualitative recognition that accumulated competence becomes liability under environmental change; AAD supplies the structural threshold |

**Search Log:**
- 2026-04 (*intuition-only* on the survival-inequality framing): the Beta-Bernoulli $1/(n+1)$ decay is elementary, the forgetting-factor remedy is standard, and the qualitative organizational-calcification intuition is well-established. The unsearched claim is whether the framing as a *structural survival prerequisite* — with environment-side $\rho_\Sigma/R_\Sigma$ on the right-hand side — has been formalized elsewhere as a threshold rather than a hyperparameter. Targeted future search candidates: bounded-rationality with memory cost (Genewein, Leibfried, Grau-Moya, Braun 2015 *Frontiers in Robotics and AI*), regret analysis of forgetting-factor estimators in adaptive control (Anderson-Moore line), organizational-learning literature on competency traps and "core rigidities" connected to environmental volatility metrics. Pre-search expectation: the constituent moves are individually well-precedented; the integrated framing as a Lyapunov-style survival prerequisite for the *strategic* substate, with the structural identity to the epistemic persistence condition under forgetting, is plausibly AAD-distinctive but not yet verified under nominally-comprehensive search.

## Working Notes

- **Done.** Five cases verified: single-edge AND, two-edge AND (observable and unobservable intermediate), two-arm OR ($\varepsilon$-greedy), and mixed AND/OR with common-cause node (L1 augmented DAG). Full derivations in #deriv-edge-credence-dynamics (Props B.1–B.6). Key findings: AND-node persistence is depth-gated (evidence starvation); OR-node persistence is exploration-gated (action selection policy); L1 augmented DAGs exhibit three-way gating (condition testing × starvation × exploration). All satisfy the schema's form ($\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$). B.6 is the first mixed AND/OR case and confirms L1 results transfer from L0 with correct construction. The next step is deeper mixed topologies and multiple common causes.
- **Strategic tempo now formalized.** #def-strategic-tempo defines $\mathcal T_\Sigma = \sum_{(i,j)} \nu_{ij} \cdot \eta_{\text{edge},ij}$ and verifies consistency with all four cases. The relationship to the schema's sector parameter: $\alpha_\Sigma \leq \mathcal T_\Sigma / \lvert E\rvert$ (persistence is bottleneck-limited, not throughput-limited). #form-strategy-complexity-cost provides the IB/MDL framework for strategy compression and derives max useful depth $d^\ast$.
- The strategic disturbance $\rho_\Sigma$ is qualitatively different from epistemic disturbance $\rho$. Epistemic disturbance is about the environment changing (physical state evolves). Strategic disturbance is about the agent's causal theory becoming invalid (the intervention-outcome mapping shifts). These can be correlated (a changing environment invalidates both model and strategy) but they're not the same quantity.
- The stochastic treatment (from track-b simulations) suggests $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$ rather than $\rho_\Sigma / \mathcal T_\Sigma$ for the steady-state strategic mismatch. If this carries over from the epistemic domain, the persistence threshold is different in the stochastic case. Whether strategic disturbance is better modeled as deterministic or stochastic drift is domain-dependent.
- The forgetting prerequisite transforms an organizational platitude ("stay adaptive") into a quantitative constraint: the rate at which an agent discounts old evidence must exceed the rate at which its environment invalidates plans. Institutional examples where this fails — long-running successful firms whose accumulated $n$ suppresses gain below the threshold set by a shifting competitive landscape — are the strategic analog of model-rigidity death spirals. The threshold is precisely $(1-\lambda) = \rho_\Sigma / R_\Sigma$, marking the point at which no amount of prior learning protects against a sufficiently volatile environment.
- **Cross-reference to NeurIPS Paper 2.** The forgetting prerequisite is sharpened in NeurIPS 2026 Paper 2 ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §App-D / `aux-decay-class`) into a **structural-class theorem on gain-decay updates**: define $\mathcal{A}_{\text{decay}}$ = the class of update mechanisms whose effective gain decays to zero with accumulated experience (count-accumulating Bayesian without forgetting; observation-aggregating without restart; Robbins-Monro / vanishing-step-size gradient methods). Every member of $\mathcal{A}_{\text{decay}}$ universally violates the persistence threshold for any positive disturbance rate. Finite-gain mechanisms (constant-step stochastic approximation, sliding windows, bounded memory, block restart) face *bidirectional* thresholds — both the forgetting prerequisite (lower bound on plasticity) and an upper bound from noise blow-up. This lifts the segment's per-mechanism claim to a class-level no-go: gain-decay mechanisms are structurally disqualified regardless of tuning. See `msc/neurips-back-integration-2026-05-08.md` §1 Paper 2 entry 4.
