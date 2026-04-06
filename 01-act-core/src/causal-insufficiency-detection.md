---
slug: causal-insufficiency-detection
type: derived
status: conditional
depends:
  - structural-adaptation-necessity
  - strategy-dag
  - loop-interventional-access
  - causal-information-yield
stage: draft
---

# Derived: Causal Insufficiency Detection

An agent operating at L0 of the Correlation Hierarchy ( #strategy-dag) can detect that its strategy DAG is causally insufficient — that latent common causes exist — from the structure of its own residuals after parametric convergence. The agent's interventions can further localize the common cause to specific sibling groups. This is #structural-adaptation-necessity applied to the strategy layer, with the independence model as the model class and the ±ρ bias formula as the diagnostic signal.

## Formal Expression

### The Detection Principle

*[Derived (from structural-adaptation-necessity + ±ρ bias formula)]*

After edge credences converge ($\hat p_k \approx \theta_k$, low gain), the plan-confidence error $\delta_s \approx 0$ — the agent is well-calibrated within the independence model. The agent also observes actual plan outcomes $y_G \in \{0, 1\}$. The **L0 residual** — the gap between the independence-model reference value and actual success — converges to:

$$\Phi^{L0} - \bar{y}_G \;\longrightarrow\; \begin{cases} +\rho & \text{OR-heavy strategies (overestimation)} \\ -\rho & \text{AND-heavy strategies (underestimation)} \end{cases}$$

where $\rho$ aggregates the latent covariance structure and $\bar{y}_G$ is the empirical success rate.

**Detection criterion.** A persistently nonzero L0 residual after edge-credence convergence is diagnostic of causal insufficiency:

$$\lvert\Phi^{L0} - \bar{y}_G\rvert \gt \epsilon \quad \text{after } n_k \gg 1 \;\forall\; k \quad\implies\quad \text{DAG is causally insufficient}$$

The sign diagnoses the dominant bias: positive means OR-node overestimation (illusory redundancy), negative means AND-node underestimation (unrecognized synergy).

This is not a new principle — it is #structural-adaptation-necessity's diagnostic criterion ("persistent irreducible mismatch after parametric convergence is diagnostic of model class inadequacy") instantiated for the strategy layer with the independence model as the model class and $\rho$ as the irreducible mismatch.

### Interventional Localization

*[Derived (from loop-interventional-access + independence test)]*

The agent can identify *where* the latent common cause acts by testing for pairwise covariance among sibling edges under the same parent.

Under L0 (independence), sibling outcomes are uncorrelated:

$$H_0: \text{Cov}(Y_{A_i}, Y_{A_j}) = 0 \quad \forall\; i \neq j \;\text{siblings under the same parent}$$

Under causal insufficiency (latent common cause), sibling outcomes are positively correlated:

$$H_1: \exists\; i \neq j \;\text{with}\; \text{Cov}(Y_{A_i}, Y_{A_j}) \gt 0$$

The agent generates test data through the standard exploration mechanism (SA3 — $\varepsilon$-greedy or similar). On trials where both siblings are observable — the agent tries one and can also observe the other's outcome, or tries them in rapid succession before the environment state changes — it accumulates the empirical covariance:

$$\hat\rho_{ij} = \frac{1}{N}\sum_t (Y_{A_i,t} - \bar{Y}_{A_i})(Y_{A_j,t} - \bar{Y}_{A_j})$$

A significantly positive $\hat\rho_{ij}$ localizes the latent common cause: $A_i$ and $A_j$ share a dependency not represented in the DAG.

The feedback loop ( #loop-interventional-access) is what makes this possible: the agent's actions are genuine interventions, so the $(A_i, Y_i)$ pairs are interventional data. The covariance test is a causal independence test conducted on interventional data — it detects common causes that would be confounded in purely observational data.

### From Detection to L1 Construction

Once the agent detects $\hat\rho_{ij} \gt 0$ between siblings $A_i$ and $A_j$, it knows a latent common cause exists but not its identity. The construction process:

1. **Hypothesize** a common-cause node $C$ that explains the correlation.
2. **Estimate** $\theta_C$ from the pattern of joint outcomes. The joint failure rate $P(A_i\text{ fails}, A_j\text{ fails})$ exceeds $(1-\theta_i)(1-\theta_j)$ by $\rho_{ij}$; the excess localizes the common cause's frequency.
3. **Restructure** the DAG: factor $C$ above the correlated siblings ( #strategy-dag, L1 construction principle).
4. **Re-estimate** conditional edge credences $\theta_{k|C}$ from the data, conditioned on the inferred $C$ state.

This is structural adaptation ( #structural-adaptation-necessity) at the strategy level: the agent changes its model class from L0 to L1, adding representational capacity for a pattern the L0 model cannot express. The cost is the standard cost of structural change: temporary performance degradation while the new credences converge, and increased graph complexity.

### Diagnostic CIY

*[Discussion (diagnostic-ciy)]*

Which actions are most informative for detecting latent common causes? An action that tests multiple potentially-correlated edges simultaneously has high causal information yield for the independence hypothesis ( #causal-information-yield). The explore-exploit tradeoff extends with a third axis:

- **Exploit**: pursue the current best plan
- **Explore**: test unknown edges for their individual success rates
- **Diagnose**: test known edges for their joint correlation structure

Diagnosis is a form of internal exploration — the agent probes its own model's structural assumptions rather than learning new parameter values. A chess engine exploring futures is deliberation about state; an agent testing whether two alternatives share a common failure mode is deliberation about model structure. The information value of diagnostic actions is highest when:

- Edge credences have converged (the agent knows the marginals but not the joint structure)
- The L0 residual is persistently nonzero (there is evidence of model inadequacy but the source is unknown)
- Multiple siblings are jointly observable (the covariance test has data)

## Epistemic Status

*Conditional on strategy-layer instantiation of structural-adaptation-necessity.* The detection principle is a direct application of #structural-adaptation-necessity's diagnostic criterion: persistent mismatch after parametric convergence → model class inadequacy. The instantiation to the independence model (L0 → L1 transition) is exact: the ±ρ formula provides the quantitative signal, and the sign diagnoses the node-type-specific bias direction. The interventional localization is standard hypothesis testing applied to interventional data from the feedback loop.

The "from detection to construction" pipeline is discussion-grade: the detection signal is precise, but the specific procedures for estimating $\theta_C$ and $\theta_{k|C}$ from correlated outcome data are domain engineering. The diagnostic CIY discussion is ungrounded — it identifies the right question (which actions are most informative for structural detection) but does not derive the answer.

### What Cannot Be Detected

Interventions cannot detect common causes that:

- **Affect only one edge**: idiosyncratic factors are not common causes. They appear as noise in individual edge credences.
- **Are too rare to produce observable joint failures**: a common cause with $\theta_C \approx 1$ (almost always active) rarely reveals itself. The agent needs enough failure events to estimate the covariance.
- **Correlate edges that are never jointly observable**: if the agent can never observe both $A_i$ and $A_j$ in the same environment state (mutually exclusive with long horizons), the joint outcome data is unavailable.
- **Introduce negative correlation**: the formulation assumes positive correlation from shared enabling factors. Negative correlation (competing for a shared resource) requires a different model and produces the opposite bias pattern.

These limitations parallel the information-theoretic underdetermination in #credit-assignment-boundary: detection requires data, and the data must have the right structure.

## Discussion

**The detection-construction cycle.** The full cycle — L0 operation → detect persistent bias → localize common cause → construct L1 → re-converge — is a concrete instance of the structural adaptation cycle described in #structural-adaptation-necessity. The agent starts with a simpler model class (L0), operates until the model class's limitations become empirically visible, then transitions to a richer model class (L1) at the cost of temporary uncertainty. The ±ρ formula makes the detection criterion quantitative rather than qualitative: the agent knows *how much* bias to expect if a common cause of a given strength exists, and can set detection thresholds accordingly.

**Connection to the orient cascade.** The detection signal enters the orient cascade ( #orient-cascade) at step 1 (epistemic update): the agent observes that its plan-level predictions are systematically wrong. This feeds into step 4 (strategic calibration): the per-edge credences are accurate but the plan-level combination is wrong — a structural problem, not a parametric one. The cascade's response is step 5-equivalent: structural revision of $\Sigma_t$ (adding the common-cause node), which is objective-preserving strategy restructuring.

**Domain instantiations.** The detection mechanism applies concretely in:
- **Software deployment**: two services sharing infrastructure fail together more often than independent failure rates predict → add infrastructure-health node
- **Military operations**: two concurrent operations fail together under adverse weather → add weather-condition node
- **Investment**: two positions lose value together during market stress → add market-regime node
- **Organizational strategy**: two initiatives stall together during leadership transitions → add organizational-stability node
