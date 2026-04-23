---
slug: causal-insufficiency-detection
type: derived
status: conditional
depends:
  - structural-adaptation-necessity
  - strategy-dag
  - loop-interventional-access
  - causal-hierarchy-requirement
  - pearl-causal-hierarchy
  - causal-information-yield
stage: draft
---

# Derived: Causal Insufficiency Detection

An agent operating at L0 of the Correlation Hierarchy ( #strategy-dag) faces a structural impossibility: under purely on-policy execution, no detection mechanism can distinguish an L0-insufficient world (latent common causes present) from an L0-sufficient world matched to the on-policy regime conditionals. This is a consequence of the causal hierarchy theorem ( #pearl-causal-hierarchy, #causal-hierarchy-requirement) — observational data does not in general identify interventional structure. Detection is therefore *only* possible by capabilities that violate the "purely on-policy" condition: joint sibling observability under exploration (the canonical AAD route, exploiting #loop-interventional-access), intermediate-state observability, structural priors, or direct intervention on the candidate latent. The pairwise sibling covariance test is the AAD-canonical detector; the L0 plan-level residual is a degenerate special case of the no-go.

## Formal Expression

### The No-Go Theorem: Purely On-Policy Detection Is Impossible

*[Derived (no-go-on-policy, from causal hierarchy theorem + observational equivalence under sequential short-circuit), conditional on (S1)–(S5) below]*

Let $\mathcal{M}_{L0}$ be the agent's L0 strategy model with sequential short-circuit AND/OR execution policy $\pi_{L0}$. Let $\mathcal{W}_{L1}$ be a world with a latent common cause $C$ acting on multiple sibling action propositions, and $\mathcal{W}_{L0}^\ast$ be an L0 world with edge probabilities $\{\theta_j^\ast\}$ matched to the on-policy regime conditionals of $\mathcal{W}_{L1}$. Let $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\cdot]$ denote the joint distribution over the agent's on-policy observable events under $\pi_{L0}$.

**Observational equivalence.** $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L1}] = \mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L0}^\ast]$.

**No-go conclusion.** Any function of the agent's on-policy observable history alone cannot distinguish $\mathcal{W}_{L1}$ from $\mathcal{W}_{L0}^\ast$. Therefore no purely on-policy detection mechanism — no test, statistic, or Bayesian comparison taking only the on-policy distribution as input — can detect L0 causal insufficiency.

**Scope conditions (S1)–(S5).**

- (S1) Pure on-policy execution; no off-policy sampling.
- (S2) Sequential short-circuit AND/OR evaluation.
- (S3) Censored sibling observation: short-circuited siblings are not observed.
- (S4) No interventional access to candidate latents.
- (S5) No structural priors positing specific common causes.

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause and $\theta_{j \mid \neg C} = 0$ — see #worked-example-L1). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures: the structural argument transfers, but explicit $\mathcal{W}_{L0}^\ast$ construction has been carried out only for shallow cases.

**Construction of $\mathcal{W}_{L0}^\ast$.** For a 2-sibling OR with strict-prerequisite latent $C$, $P(C) = \theta_C$, conditional success rates $\theta_{j \mid C}$:

$$\theta_1^\ast = \theta_C \cdot \theta_{1 \mid C}, \qquad \theta_2^\ast = p_2^c = \frac{\theta_C\,(1 - \theta_{1 \mid C})\,\theta_{2 \mid C}}{1 - \theta_C\,\theta_{1 \mid C}}$$

Direct verification (see #worked-example-L1) shows $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L1}] = \mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L0}^\ast]$ on the three on-policy observable events. The Bareinboim, Correa, Ibeling & Icard (2022) Causal Hierarchy Theorem then gives the no-go: any two SCMs that agree on Level 1 (associational) data cannot in general be distinguished on Level 2 (interventional) questions, and the L0/L1 distinction — whether siblings share a common cause — is precisely a Level 2 question about $P(A_2 \mid do(\neg A_1))$ versus $P(A_2 \mid \neg A_1)$.

**Why this matters.** The no-go is the structural reason the prior aggregate-residual mechanism collapses on-policy: the residual is a function of $\mathbb{P}_{\pi_{L0}}^{\text{obs}}$, which is identical between the two worlds, so the residual is identically zero under both. The collapse is not a quirk of the residual statistic — it is a special case of the no-go applied to that specific function. No replacement aggregate statistic can do better.

### The Detection Routes: What Circumvents the No-Go

*[Derived (boundary-routes, from no-go scope conditions)]*

The no-go's scope conditions (S1)–(S5) define "purely on-policy." Each condition's violation corresponds to an AAD capability that admits (partial) detection:

| Route | Scope violated | AAD capability | Detection strength |
|-------|----------------|----------------|--------------------|
| (a) ε-exploration | (S1) | SA3 exploration ( #strategic-dynamics-derivation Prop B.4) | Partial, scales with ε |
| (b) Joint sibling observability | (S3) | Covariance test under SA3 + #loop-interventional-access | Strong |
| (c) Intermediate observability | (S3) at finer grain | Observability investment ( #observability-dominance) | Very strong when available |
| (d) Structural priors | (S5) | Hypothesized common-cause nodes in DAG construction | Prior-quality-dependent |
| (e) Direct intervention on latent | (S4) | Domain-specific latent control | Strongest when available |

The covariance test (route (b)) is the AAD-canonical detector: it uses only machinery the theory already requires (exploration via SA3, interventional data via the loop) and is available in the broadest range of domains. The remaining sections operationalize this primary mechanism.

### Primary Detection Mechanism: Pairwise Sibling Covariance Under Intervention

*[Derived (from loop-interventional-access + independence test, conditional on SA3 exploration providing joint observability)]*

Under L0 (the independence model in #strategy-dag's Correlation Hierarchy), sibling outcomes under a common parent are uncorrelated:

$$H_0:\;\operatorname{Cov}(Y_{A_i}, Y_{A_j}) = 0 \quad \forall\; i \neq j \;\text{siblings under the same parent}$$

Under causal insufficiency (latent common cause $C$ acting on multiple siblings), sibling outcomes are positively correlated:

$$H_1:\;\exists\; i \neq j \;\text{with}\; \operatorname{Cov}(Y_{A_i}, Y_{A_j}) \gt 0$$

The agent generates test data through the standard exploration mechanism (SA3 — $\varepsilon$-greedy or similar). On trials where both siblings are observable — the agent tries one and can also observe the other's outcome, or tries them in rapid succession before the environment state changes — it accumulates the empirical covariance:

$$\hat\rho_{ij} = \frac{1}{N}\sum_t (Y_{A_i,t} - \bar{Y}_{A_i})(Y_{A_j,t} - \bar{Y}_{A_j})$$

A significantly positive $\hat\rho_{ij}$ rejects the L0 independence hypothesis. Joint observability ( #loop-interventional-access supplies the interventional character; SA3 supplies the joint sampling) is precisely the violation of scope condition (S3) that admits the test under the no-go.

**Detection criterion.** A statistically significant positive $\hat\rho_{ij}$ at sample size $N$ sufficient for the desired test power, after per-edge credences have stabilized:

$$\hat\rho_{ij} \gt z_{1-\alpha}\,\hat\sigma_{\rho_{ij}} / \sqrt{N} \quad\implies\quad \text{DAG is causally insufficient between siblings } i, j$$

(Standard hypothesis-testing form; threshold and test power depend on application.)

**Preconditions for the covariance test.**

1. **Joint observability.** The agent can occasionally observe $(Y_{A_i}, Y_{A_j})$ pairs in the same environment state. Pure short-circuit execution censors one of each pair; SA3 exploration or simultaneous-attempt regimes provide uncensored pairs.
2. **Per-edge credence stabilization.** Edge credences $\hat p_i, \hat p_j$ have stopped drifting at the timescale of the covariance accumulation, so $\bar Y_{A_i}, \bar Y_{A_j}$ are well-defined empirical means.
3. **Approximate stationarity over the test window.** The latent common cause's frequency and the conditional success rates are not drifting faster than the test's accumulation timescale.

When these preconditions hold, $\hat\rho_{ij} \gt 0$ is diagnostic of a missing common cause acting on $(A_i, A_j)$. When they do not, the signal is ambiguous.

### The Aggregate Residual as a Degenerate Special Case of the No-Go

*[Derived (residual-degeneracy, as instance of no-go theorem)]*

A historically prominent diagnostic uses the L0 plan-level residual $\Phi^{L0}(\hat{\boldsymbol p}) - \bar{y}_G$ as a detection signal. The no-go theorem subsumes this as a special case: under pure on-policy execution, the residual is *identically zero* in both $\mathcal{W}_{L1}$ and $\mathcal{W}_{L0}^\ast$.

**Direct verification.** Under sequential short-circuit, the agent's empirical credences converge to the on-policy regime conditionals: $\hat p_j \to p_j^c$. Plugging these into the L0 arithmetic recovers the chain rule of probability (e.g., for OR: $1 - (1 - p_1^c)(1 - p_2^c) = 1 - P(\neg A_1, \neg A_2) = P(A_1 \cup A_2)$, which equals $\bar y_G$ under the executed policy). The residual is zero by algebraic identity.

This is *not* a separate finding from the no-go: it is the no-go's prediction for the specific aggregate-residual statistic. The no-go forbids *any* on-policy statistic from distinguishing $\mathcal{W}_{L1}$ from $\mathcal{W}_{L0}^\ast$; the residual evaluates to the same value (zero) in both, as expected.

**Off-policy boundary.** Under ε-exploration (route (a)), the residual scales as $O(\varepsilon)$ to leading order with sign matching the dominant node-type bias ($+$ for OR-heavy, $-$ for AND-heavy):

$$\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G = \varepsilon \cdot R + O(\varepsilon^2), \quad \operatorname{sign}(R) = \operatorname{sign}(\rho)$$

where $R$ is structure-dependent and recovers the marginal-limit $\rho$ at $\varepsilon = 1$. *[Heuristic]* The qualitative form is robust; the exact coefficient depends on the gap between conditional and marginal credences. The widely-quoted "$\varepsilon \cdot \rho$" scaling is correct as an order-of-magnitude statement. For a 2-sibling OR with conditional credences $p_j^c$, the exact two-OR formula is $\varepsilon R_1 - \varepsilon^2 R_2$ with $R_1 - R_2 = \rho$; the leading-order coefficient $R_1$ is structure-dependent and equals $\rho$ only at $\varepsilon = 1$.

The residual is therefore a *confirmatory* signal under route (a): when the agent has material off-policy exploration and the covariance test (route (b)) has localized a candidate latent, the residual sign confirms the bias direction. It is not a primary detector and cannot replace the covariance test.

### From Detection to L1 Construction

*[Derived (from positive covariance signal + L1 construction principle in #strategy-dag)]*

Once the agent detects $\hat\rho_{ij} \gt 0$ between siblings $A_i$ and $A_j$, it knows a latent common cause exists but not its identity. The construction process:

1. **Hypothesize** a common-cause node $C$ that explains the correlation.
2. **Estimate** $\theta_C$ from the pattern of joint outcomes. The joint failure rate $P(A_i\text{ fails}, A_j\text{ fails})$ exceeds $(1-\theta_i)(1-\theta_j)$ by $\hat\rho_{ij}$; the excess localizes the common cause's frequency.
3. **Restructure** the DAG: factor $C$ above the correlated siblings ( #strategy-dag, L1 construction principle: factor the common cause above the correlation it creates).
4. **Re-estimate** conditional edge credences $\theta_{k\mid C}$ from the data, conditioned on the inferred $C$ state.

This is structural adaptation ( #structural-adaptation-necessity) at the strategy level: the agent changes its model class from L0 to L1, adding representational capacity for a pattern the L0 model cannot express. The cost is the standard cost of structural change: temporary performance degradation while the new credences converge, and increased graph complexity. (Soft-facilitator common causes require L1' rather than L1 — see #strategy-dag and #worked-example-L1 for the strict-prerequisite vs soft-facilitator distinction.)

### Diagnostic CIY

*[Discussion (diagnostic-ciy)]*

Which actions are most informative for detecting latent common causes? Under the no-go, only actions that violate one of (S1)–(S5) yield detection signal. The explore-exploit tradeoff extends with a third axis tied to the boundary characterization:

- **Exploit**: pursue the current best plan (no scope violation; no detection signal).
- **Explore**: test unknown edges for individual success rates (route (a); partial detection).
- **Diagnose**: test known edges for joint correlation structure (route (b); strong detection).

Diagnosis is a form of internal exploration — the agent probes its own model's structural assumptions by violating (S3) deliberately, generating joint sibling outcomes that the no-go forbids the agent to obtain on-policy. The information value of diagnostic actions is highest when:

- Edge credences have converged (the agent has good marginals/conditionals but unknown joint structure).
- Joint outcomes for sibling pairs are observable in the same environment state (the covariance test has data — route (b) is operational).
- The agent has sufficient off-policy budget that the secondary residual signal corroborates (route (a) is also operational).

## Epistemic Status

*Conditional* on the no-go's scope conditions (S1)–(S5) and on strategy-layer instantiation of #structural-adaptation-necessity. The **no-go theorem** is *exact* for shallow strict-prerequisite cases (2-sibling OR or AND, single binary common cause) by direct construction; *robust qualitative* for general DAG topology, soft facilitators, and deeper structures. The structural argument (observational equivalence of regime-conditional L0 and latent-cause L1) transfers to the general case; explicit construction of $\mathcal{W}_{L0}^\ast$ has been carried out only for shallow cases.

The **boundary characterization** (routes (a)–(e)) is *robust qualitative*: each route maps to a specific scope-condition violation and to existing AAD machinery, but the precise detection power of each route depends on domain particulars. Routes (a) and (b) have explicit AAD scaffolding ( #strategic-dynamics-derivation, #loop-interventional-access); routes (c)–(e) depend on domain capability.

The **primary detection mechanism** (pairwise sibling covariance) is *robust qualitative*: standard hypothesis testing applied to interventional data from the feedback loop, with explicit preconditions. Its sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence; in adversarial or fast-drifting environments the test's effective sample size shrinks.

The **aggregate residual** as a confirmatory signal is *exact* for the on-policy collapse (no-go's prediction is direct); the off-policy mixed-regime scaling is *heuristic* (linear-in-$\varepsilon$ with structure-dependent coefficient).

The **detection-to-construction pipeline** is *discussion-grade*: the trigger is the (statistically rigorous) covariance signal, but the specific procedures for estimating $\theta_C$ and $\theta_{k\mid C}$ from correlated outcome data are domain engineering.

### What Cannot Be Detected

By the no-go and its boundary characterization, several latent structures remain undetectable by *any* AAD route:

- **Latents with no joint-observability route.** If the latent affects siblings that cannot be jointly observed (mutually exclusive with long horizons, no cause-indicator availability, no intervention capability, no informative prior), the no-go applies in full strength and detection is impossible.
- **Latents affecting only one edge.** By definition not common causes; appear as noise in individual edge credences.
- **Latents too rare to produce observable joint outcomes.** Even with route (b) operational, a latent with $\theta_C \approx 1$ rarely reveals itself — the agent needs enough $C = 0$ events to estimate the covariance.
- **Negatively-correlating latents.** The formulation assumes positive correlation from shared enabling factors. Negative correlation (competing for a shared resource) produces the opposite bias pattern and requires a different model.

These limitations parallel the information-theoretic underdetermination in #credit-assignment-boundary: detection requires data with the right structure, and the no-go specifies precisely what "right structure" means.

## Discussion

**Why the no-go is a strengthening, not a softening.** The prior framing ("the residual mechanism collapses on-policy") was a local observation about one statistic. The no-go is the structural reason: any on-policy statistic must collapse, because the on-policy distribution is identical between L0 and L1 worlds matched on regime conditionals. The covariance test is not just *a* working detector — it is the unique broadly-available violation of the no-go's scope. This sharpens the load-bearing of `#loop-interventional-access`: without the loop's interventional data, the no-go forbids detection entirely; with it, route (b) is operational.

**Connection to Pearl's hierarchy.** The L0/L1 distinction is a Level 2 distinction in Pearl's framework — it concerns whether $P(A_2 \mid do(\neg A_1)) = P(A_2 \mid \neg A_1)$. The Causal Hierarchy Theorem (Bareinboim, Correa, Ibeling & Icard 2022, Theorem 1) proves that Level 2 distinctions are not in general identifiable from Level 1 (associational) data. The no-go is the AAD-specific instantiation: on-policy data is Level 1; the L0/L1 question is Level 2; therefore detection requires more than on-policy data. The five circumvention routes are all ways the agent obtains supra-Level-1 information.

**The censoring mechanism is the structural source.** Sequential short-circuit evaluation is what makes on-policy data Level 1 only — it censors the joint outcomes that would constitute Level 2 evidence. An agent that *did not* short-circuit would obtain joint sibling outcomes naturally, and the no-go would not apply. But short-circuit is forced by efficiency: testing $A_2$ when $A_1$ has already succeeded is wasted action. The no-go is therefore a tradeoff between execution efficiency (favoring short-circuit) and structural diagnosis (favoring joint observation). SA3 ε-exploration is the AAD compromise: short-circuit by default, occasional non-short-circuit excursions that pay the efficiency cost to maintain detection capability.

**Connection to the orient cascade.** The detection signal enters the orient cascade ( #orient-cascade) at step 4c (causal-sufficiency check). Step 4c's reference to "pairwise sibling covariance under an augmented test" aligns with the primary detection mechanism here. The no-go strengthens the cascade's load-bearing: step 4c is not "one possible diagnostic" but "the unique broadly-available diagnostic given the structural impossibility of purely on-policy detection."

**Connection to the broader identifiability-floor pattern.** The no-go is one of an emerging class of structural impossibility results in AAD — limits on what can be inferred from limited information, derived from external information-theoretic theorems. See #discussion-identifiability-floor for the meta-pattern collecting this result alongside the L1' mixture-identifiability obstruction ( #strategic-dynamics-derivation Prop B.7) and the open causal-IB extension for interventional relevance variables.

**Domain instantiations.** The covariance test (route (b)) applies concretely in:
- **Software deployment**: two services sharing infrastructure fail together more often than independent failure rates predict → add infrastructure-health node.
- **Military operations**: two concurrent operations fail together under adverse weather → add weather-condition node.
- **Investment**: two positions lose value together during market stress → add market-regime node.
- **Organizational strategy**: two initiatives stall together during leadership transitions → add organizational-stability node.

In each, what makes detection feasible is the agent's ability to occasionally observe *both* sibling outcomes — the route (b) capability. Pure short-circuit ("only run service B if A is down") suppresses the joint-observation events the test relies on; some routine joint exposure is necessary. When joint observation is impossible (routes (b) and (c) both unavailable) and intervention on the candidate latent is impossible (route (e) unavailable), the agent must rely on structural priors (route (d)) — domain knowledge positing the common cause. This is the regime in which intuition-driven causal modeling is the only tractable approach.

## Working Notes

- The general-topology construction is a structural argument; the explicit $\mathcal{W}_{L0}^\ast$ for arbitrary AND/OR DAGs with mixed common-cause patterns has not been carried out. For load-bearing application of the no-go to specific complex topologies, the construction should be specialized. Currently the load-bearing applications (orient-cascade step 4c, strategy-dag's L0/L1 escalation principle) reference shallow strict-prerequisite cases for which the no-go is exact.
- The boundary characterization's routes (c) and (e) depend on domain capability and are not formalized in AAD beyond cross-references to `#observability-dominance` and `#loop-interventional-access`. A future refinement could quantify "detection power" per route as a function of domain parameters (e.g., observability cost, intervention availability, prior strength).
- The no-go is asymmetric: it forbids on-policy *detection* of L1 from L0, but it does *not* forbid on-policy *parameter learning within L0*. The agent can learn its L0 conditionals to arbitrary precision on-policy; it just cannot determine whether those conditionals hide a latent. This distinction sharpens the diagnosis-vs-calibration split that #structural-adaptation-necessity makes at the parametric/structural boundary.
- The CHT (Bareinboim et al. 2022) is invoked as an external theorem. AAD inherits its conditions (well-defined SCMs over compatible variable sets); these are satisfied for the strategy-DAG setting by construction.
