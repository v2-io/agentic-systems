---
slug: der-causal-insufficiency-detection
type: derived
status: conditional
depends:
  - result-structural-adaptation-necessity
  - def-strategy-dag
  - der-loop-interventional-access
  - der-causal-hierarchy-requirement
  - def-pearl-causal-hierarchy
  - def-causal-information-yield
stage: draft
---

# Derived: Causal Insufficiency Detection

The framework's first explicit *no-go theorem* on agent self-diagnosis. An agent operating at L0 of the Correlation Hierarchy ( #def-strategy-dag) — assuming its action propositions are causally independent — faces a structural impossibility when its world contains a latent common cause acting on multiple of those actions: under purely on-policy execution, no test, statistic, or Bayesian comparison built from the agent's observable history can distinguish the latent-cause world ($\mathcal W_{L1}$) from a no-latent-cause world ($\mathcal W_{L0}^\ast$) whose edge probabilities are matched to the on-policy regime conditionals. The two worlds emit identical on-policy distributions. This is the agent-theoretic instance of the Causal Hierarchy Theorem ( #def-pearl-causal-hierarchy, #der-causal-hierarchy-requirement) applied to the L0/L1 distinction — a Level-2 question (what happens under $do(\cdot)$ on one sibling) being asked of Level-1 data (on-policy observational distributions). The construction of $\mathcal W_{L0}^\ast$ is explicit for the cleanest case (2-sibling OR with strict-prerequisite latent), and the no-go is *exact* for shallow strict-prerequisite cases and *robust-qualitative* for general DAG topology, soft facilitators, and deeper structures.

Detection is therefore *only* possible by capabilities that violate the "purely on-policy" condition. The framework characterizes **five escape routes**, each violating one of the no-go's scope conditions (S1)–(S5): (a) $\varepsilon$-exploration breaks pure on-policy execution (partial detection, scales with $\varepsilon$); (b) joint sibling observability under exploration breaks the short-circuit censoring (strong detection via a pairwise sibling covariance test — *the AAT-canonical detector*, exploiting #der-loop-interventional-access); (c) intermediate-state observability breaks censoring at finer grain (very strong when available, see #der-observability-dominance); (d) structural priors break the no-prior condition; (e) direct intervention on the candidate latent is strongest when available. The primary detection mechanism — pairwise sibling covariance under intervention — is the unique broadly-available violation of the no-go's scope, using only machinery the theory already requires (exploration via SA3, interventional data via the loop).

A historically prominent diagnostic — the L0 plan-level residual — is shown to be a *degenerate special case* of the no-go: under pure on-policy execution the residual is *identically zero* in both worlds by algebraic identity. The collapse is not a quirk of the residual statistic; it is the no-go's prediction for that specific function. No replacement aggregate statistic can do better. Under partial exploration the residual scales as $O(\varepsilon)$ with sign matching the dominant node-type bias, becoming a *confirmatory* signal rather than a primary detector. A subtle but important property: the no-go is *asymmetric* — it forbids on-policy *detection* of L1 from L0 but does *not* forbid on-policy *parameter learning within L0*. The structural source is *sequential short-circuit evaluation* itself, which censors the joint outcomes that would constitute Level-2 evidence; the no-go is therefore a tradeoff between execution efficiency (favoring short-circuit) and structural diagnosis (favoring joint observation), with $\varepsilon$-exploration the AAT compromise.

## Formal Expression

### The No-Go Theorem: Purely On-Policy Detection Is Impossible

*[Derived (no-go-on-policy, from causal hierarchy theorem + observational equivalence under sequential short-circuit), conditional on (S1)–(S5) below]*

Let $\mathcal M_{L0}$ be the agent's L0 strategy model with sequential short-circuit AND/OR execution policy $\pi_{L0}$. Let $\mathcal W_{L1}$ be a world with a latent common cause $C$ acting on multiple sibling action propositions, and $\mathcal W_{L0}^\ast$ be an L0 world with edge probabilities $\{\theta_j^\ast\}$ matched to the on-policy regime conditionals of $\mathcal W_{L1}$. Let $\mathbb P_{\pi_{L0}}^{\text{obs}}[\cdot]$ denote the joint distribution over the agent's on-policy observable events under $\pi_{L0}$.

**Observational equivalence.** $\mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L1}] = \mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L0}^\ast]$.

**No-go conclusion.** Any function of the agent's on-policy observable history alone cannot distinguish $\mathcal W_{L1}$ from $\mathcal W_{L0}^\ast$. Therefore no purely on-policy detection mechanism — no test, statistic, or Bayesian comparison taking only the on-policy distribution as input — can detect L0 causal insufficiency.

**Scope conditions (S1)–(S5).**

- (S1) Pure on-policy execution; no off-policy sampling.
- (S2) Sequential short-circuit AND/OR evaluation.
- (S3) Censored sibling observation: short-circuited siblings are not observed.
- (S4) No interventional access to candidate latents.
- (S5) No structural priors positing specific common causes.

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause and $\theta_{j \mid \neg C} = 0$ — see #example-L1). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures: the structural argument transfers, but explicit $\mathcal W_{L0}^\ast$ construction has been carried out only for shallow cases.

**Construction of $\mathcal W_{L0}^\ast$.** For a 2-sibling OR with strict-prerequisite latent $C$, $P(C) = \theta_C$, conditional success rates $\theta_{j \mid C}$:

$$\theta_1^\ast = \theta_C \cdot \theta_{1 \mid C}, \qquad \theta_2^\ast = p_2^c = \frac{\theta_C\,(1 - \theta_{1 \mid C})\,\theta_{2 \mid C}}{1 - \theta_C\,\theta_{1 \mid C}}$$

Direct verification (see #example-L1) shows $\mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L1}] = \mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L0}^\ast]$ on the three on-policy observable events. The Bareinboim, Correa, Ibeling & Icard (2022) Causal Hierarchy Theorem then gives the no-go: any two SCMs that agree on Level 1 (associational) data cannot in general be distinguished on Level 2 (interventional) questions, and the L0/L1 distinction — whether siblings share a common cause — is precisely a Level 2 question about $P(A_2 \mid do(\neg A_1))$ versus $P(A_2 \mid \neg A_1)$.

**Why this matters.** The no-go is the structural reason the prior aggregate-residual mechanism collapses on-policy: the residual is a function of $\mathbb P_{\pi_{L0}}^{\text{obs}}$, which is identical between the two worlds, so the residual is identically zero under both. The collapse is not a quirk of the residual statistic — it is a special case of the no-go applied to that specific function. No replacement aggregate statistic can do better.

### The Detection Routes: What Circumvents the No-Go

*[Derived (boundary-routes, from no-go scope conditions)]*

The no-go's scope conditions (S1)–(S5) define "purely on-policy." Each condition's violation corresponds to an AAT capability that admits (partial) detection:

| Route | Scope violated | AAT capability | Detection strength |
|-------|----------------|----------------|--------------------|
| (a) $\varepsilon$-exploration | (S1) | SA3 exploration ( #deriv-edge-credence-dynamics Prop B.4) | Partial, scales with $\varepsilon$ |
| (b) Joint sibling observability | (S3) | Covariance test under SA3 + #der-loop-interventional-access | Strong |
| (c) Intermediate observability | (S3) at finer grain | Observability investment ( #der-observability-dominance) | Very strong when available |
| (d) Structural priors | (S5) | Hypothesized common-cause nodes in DAG construction | Prior-quality-dependent |
| (e) Direct intervention on latent | (S4) | Domain-specific latent control | Strongest when available |

The covariance test (route (b)) is the AAT-canonical detector: it uses only machinery the theory already requires (exploration via SA3, interventional data via the loop) and is available in the broadest range of domains. The remaining sections operationalize this primary mechanism.

### Primary Detection Mechanism: Pairwise Sibling Covariance Under Intervention

*[Derived (from loop-interventional-access + independence test, conditional on SA3 exploration providing joint observability)]*

Under L0 (the independence model in #def-strategy-dag's Correlation Hierarchy, a causally sufficient AND/OR tree, in which siblings have disjoint ancestors), sibling outcomes under a common parent are uncorrelated:

$$H_0:\;\operatorname{Cov}(Y_{A_i}, Y_{A_j}) = 0 \quad \forall\; i \neq j \;\text{siblings under the same parent}$$

Under causal insufficiency (latent common cause $C$ acting on multiple siblings), sibling outcomes are correlated:

$$H_1:\;\exists\; i \neq j \;\text{with}\; \operatorname{Cov}(Y_{A_i}, Y_{A_j}) \neq 0$$

The correlation is positive when the latent enables or disables the siblings together (shared infrastructure, a common resource that is either there or not). It is negative when the latent makes them exclude one another: siblings competing for one scarce resource, or alternative answers to one question, such as "arm $k$ is the best arm" for each $k$ ( #example-strategy). Both reject $H_0$.

The agent generates test data through the standard exploration mechanism (SA3 — $\varepsilon$-greedy or similar). On trials where both siblings are observable — the agent tries one and can also observe the other's outcome, or tries them in rapid succession before the environment state changes — it accumulates the empirical covariance:

$$\hat\rho_{ij} = \frac{1}{N}\sum_t (Y_{A_i,t} - \bar{Y}_{A_i})(Y_{A_j,t} - \bar{Y}_{A_j})$$

A $\hat\rho_{ij}$ significantly different from zero, of either sign, rejects the L0 independence hypothesis. Joint observability ( #der-loop-interventional-access supplies the interventional character; SA3 supplies the joint sampling) is precisely the violation of scope condition (S3) that admits the test under the no-go.

**Detection criterion.** A statistically significant nonzero $\hat\rho_{ij}$ at sample size $N$ sufficient for the desired test power, after per-edge credences have stabilized (two-sided), between siblings whose *modelled* ancestor sets are disjoint:

$$\lvert\hat\rho_{ij}\rvert \gt z_{1-\alpha/2}\,\hat\sigma_{\rho_{ij}} / \sqrt{N} \quad\implies\quad \text{a cause outside the graph acts on siblings } i, j$$

(Standard hypothesis-testing form; threshold and test power depend on application.) The disjointness condition is what $H_0$ assumes. Under L0 the agent's model is a tree, so every sibling pair meets it, and the criterion reads as written. Once the model is not a tree it is not automatic: siblings that share a modelled ancestor are correlated with every cause modelled. The naive-L1 graph of #example-L1, with $C$ a parent of both $B_1$ and $B_2$, has $\operatorname{Cov}(Y_{B_1}, Y_{B_2}) = 0.504 - 0.72 \cdot 0.56 = 0.1008$ and no latent at all. For such pairs the statistic to test is the covariance conditional on the shared modelled ancestors, and an unconditional nonzero covariance says only what the graph already says.

**Preconditions for the covariance test.**

1. **Joint observability.** The agent can occasionally observe $(Y_{A_i}, Y_{A_j})$ pairs in the same environment state. Pure short-circuit execution censors one of each pair; SA3 exploration or simultaneous-attempt regimes provide uncensored pairs.
2. **Per-edge credence stabilization.** Edge credences $\hat p_i, \hat p_j$ have stopped drifting at the timescale of the covariance accumulation, so $\bar Y_{A_i}, \bar Y_{A_j}$ are well-defined empirical means.
3. **Approximate stationarity over the test window.** The latent common cause's frequency and the conditional success rates are not drifting faster than the test's accumulation timescale.

When these preconditions hold, $\hat\rho_{ij} \neq 0$ is diagnostic of a missing common cause acting on $(A_i, A_j)$, and its sign says which kind (enabling together, or exclusive). When they do not, the signal is ambiguous.

### The Aggregate Residual as a Degenerate Special Case of the No-Go

*[Derived (residual-degeneracy, as instance of no-go theorem)]*

A historically prominent diagnostic uses the L0 plan-level residual $\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G$ as a detection signal. The no-go theorem subsumes this as a special case: under pure on-policy execution, the residual is *identically zero* in both $\mathcal W_{L1}$ and $\mathcal W_{L0}^\ast$.

**Direct verification.** Under sequential short-circuit, the agent's empirical credences converge to the on-policy regime conditionals: $\hat p_j \to p_j^c$. Plugging these into the L0 arithmetic recovers the chain rule of probability (e.g., for OR: $1 - (1 - p_1^c)(1 - p_2^c) = 1 - P(\neg A_1, \neg A_2) = P(A_1 \cup A_2)$, which equals $\bar y_G$ under the executed policy). The residual is zero by algebraic identity.

This is *not* a separate finding from the no-go: it is the no-go's prediction for the specific aggregate-residual statistic. The no-go forbids *any* on-policy statistic from distinguishing $\mathcal W_{L1}$ from $\mathcal W_{L0}^\ast$; the residual evaluates to the same value (zero) in both, as expected.

**Off-policy boundary.** Under $\varepsilon$-exploration (route (a)), the residual scales as $O(\varepsilon)$ to leading order with sign matching the dominant node-type bias ($+$ for OR-heavy, $-$ for AND-heavy, when $\rho \gt 0$; reversed when $\rho \lt 0$):

$$\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G = \varepsilon \cdot R + O(\varepsilon^2), \quad \operatorname{sign}(R) = \operatorname{sign}(\rho)$$

where $R$ is structure-dependent and recovers the marginal-limit $\rho$ at $\varepsilon = 1$. *[Heuristic]* The qualitative form is robust; the exact coefficient depends on the gap between conditional and marginal credences. The widely-quoted "$\varepsilon \cdot \rho$" scaling is correct as an order-of-magnitude statement. For a 2-sibling OR with conditional credences $p_j^c$, the exact two-OR formula is $\varepsilon R_1 - \varepsilon^2 R_2$ with $R_1 - R_2 = \rho$; the leading-order coefficient $R_1$ is structure-dependent and equals $\rho$ only at $\varepsilon = 1$.

The residual is therefore a *confirmatory* signal under route (a): when the agent has material off-policy exploration and the covariance test (route (b)) has localized a candidate latent, the residual sign confirms the bias direction. It is not a primary detector and cannot replace the covariance test.

### From Detection to L1 Construction

*[Derived (from the covariance signal + the L1 construction principle in #def-strategy-dag for positive covariance; explicit conditioning for negative)]*

Once the agent detects $\hat\rho_{ij} \neq 0$ between siblings $A_i$ and $A_j$, it knows a latent common cause exists but not its identity. For $\hat\rho_{ij} \gt 0$, a shared enabling cause, the construction process is:

1. **Hypothesize** a common-cause node $C$ that explains the correlation.
2. **Estimate** $\theta_C$ from the pattern of joint outcomes. The joint failure rate $P(A_i\text{ fails}, A_j\text{ fails})$ is $(1-\theta_i)(1-\theta_j) + \hat\rho_{ij}$; the excess localizes the common cause's frequency.
3. **Restructure** the DAG: factor $C$ above the correlated siblings ( #def-strategy-dag, L1 construction principle: factor the common cause above the correlation it creates).
4. **Re-estimate** conditional edge credences $\theta_{k\mid C}$ from the data, conditioned on the inferred $C$ state.

This is structural adaptation ( #result-structural-adaptation-necessity) at the strategy level: the agent changes its model class from L0 to L1, adding representational capacity for a pattern the L0 model cannot express. The cost is the standard cost of structural change: temporary performance degradation while the new credences converge, and increased graph complexity. (Soft-facilitator common causes require L1' rather than L1 — see #def-strategy-dag and #example-L1 for the strict-prerequisite vs soft-facilitator distinction.)

**When $\hat\rho_{ij} \lt 0$.** The latent makes the siblings exclude one another, so no single gate enables both, and factoring above (step 3) does not apply. The repair is to make the latent a node whose states are the alternatives (which sibling gets the resource, which answer is true) and to condition on it. This is the explicit-conditioning form of #def-strategy-dag, $P_\Sigma(G) = \sum_c P(C = c)\, P_\Sigma(G \mid C = c)$. When the siblings are fully exclusive, an OR over them is the sum of their transmitted credences ( #example-strategy). The observability caveat of L1' carries over: if $C$'s state is never observed, the per-state credences face the same identifiability floor (Prop B.7 in #deriv-edge-credence-dynamics).

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

*Conditional* on the no-go's scope conditions (S1)–(S5) and on strategy-layer instantiation of #result-structural-adaptation-necessity. The **no-go theorem** is *exact* for shallow strict-prerequisite cases (2-sibling OR or AND, single binary common cause) by direct construction; *robust qualitative* for general DAG topology, soft facilitators, and deeper structures. The structural argument (observational equivalence of regime-conditional L0 and latent-cause L1) transfers to the general case; explicit construction of $\mathcal W_{L0}^\ast$ has been carried out only for shallow cases.

The **boundary characterization** (routes (a)–(e)) is *robust qualitative*: each route maps to a specific scope-condition violation and to existing AAT machinery, but the precise detection power of each route depends on domain particulars. Routes (a) and (b) have explicit AAT scaffolding ( #deriv-edge-credence-dynamics, #der-loop-interventional-access); routes (c)–(e) depend on domain capability.

The **primary detection mechanism** (pairwise sibling covariance) is *robust qualitative*: standard hypothesis testing applied to interventional data from the feedback loop, with explicit preconditions, between siblings whose modelled ancestor sets are disjoint (automatic under L0; conditional covariance otherwise), and blind by construction to latents that show only in the joint of three or more siblings. Its sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence; in adversarial or fast-drifting environments the test's effective sample size shrinks.

The **aggregate residual** as a confirmatory signal is *exact* for the on-policy collapse (no-go's prediction is direct); the off-policy mixed-regime scaling is *heuristic* (linear-in-$\varepsilon$ with structure-dependent coefficient).

The **detection-to-construction pipeline** is *discussion-grade*: the trigger is the (statistically rigorous) covariance signal, but the specific procedures for estimating $\theta_C$ and $\theta_{k\mid C}$ from correlated outcome data are domain engineering.

### What Cannot Be Detected

By the no-go and its boundary characterization, several latent structures remain undetectable by *any* AAT route:

- **Latents with no joint-observability route.** If the latent affects siblings that cannot be jointly observed (mutually exclusive with long horizons, no cause-indicator availability, no intervention capability, no informative prior), the no-go applies in full strength and detection is impossible.
- **Latents affecting only one edge.** By definition not common causes; appear as noise in individual edge credences.
- **Latents too rare to produce observable joint outcomes.** Even with route (b) operational, a latent with $\theta_C \approx 1$ rarely reveals itself — the agent needs enough $C = 0$ events to estimate the covariance.
- **Latents that act only on triples.** For two binary siblings, zero covariance is independence, so a latent that leaves a pair's covariance at zero also leaves the AND/OR propagation at that pair exact; the test misses it and nothing is biased. For three or more siblings, pairwise independence is not mutual independence. Take binary $X, Y$ fair and independent and $Z = X \oplus Y$: every pair is independent, yet $P(X \wedge Y \wedge Z) = 0$ against the product $1/8$, and a four-state latent $C = (X, Y)$ realizes it. The pairwise covariance test is blind to such a latent while the three-way AND or OR at that node is biased. The test is a test of pairwise structure; a latent that shows only in the joint of three or more siblings needs the joint statistic.

These limitations parallel the information-theoretic underdetermination in #disc-credit-assignment-boundary: detection requires data with the right structure, and the no-go specifies precisely what "right structure" means.

## Claim Record

### Under purely on-policy short-circuit execution, no statistic of the agent's history distinguishes a latent common cause from matched independent edges

**Register:** formal — exact for the shallow strict-prerequisite case by explicit construction of $\mathcal W_{L0}^\ast$; robust-qualitative for general topology, soft facilitators and depth, where the construction has not been carried out (tag `no-go-on-policy`, Tier).

**Population:** L0 strategy learners under (S1)–(S5).

**True of:** the 2-sibling OR with strict-prerequisite latent (Formal Expression; numerics at #example-L1).

**False of:** any agent that violates one of (S1)–(S5): $\varepsilon$-exploration, joint sibling observability, intermediate observability, structural priors, intervention on the latent. The agent is then outside the no-go, by the route table.

**Falsifier:** a function of the on-policy history that separates $\mathcal W_{L1}$ from $\mathcal W_{L0}^\ast$ in the shallow case; the construction shows the two distributions equal, so none exists. For the general case the owed item is a mixed-topology, multiple-latent construction (Working Notes); a general topology on which no matched $\mathcal W_{L0}^\ast$ exists would narrow the claim to the cases constructed.

**Instantiated:** not applicable.

### An organization that runs its backup only when its primary fails cannot learn from its own records that the two share a failure cause

**Register:** descriptive — the no-go read as a prediction about real agents with censored sequential execution (Discussion, "Domain instantiations"): they over-trust their redundancy until a joint failure.

**Population:** agents or organizations whose execution of alternatives is sequential and censored (S2–S3) and whose learning comes from their own operational records (S1, S4, S5).

**True of:** no checked instance; the deployment, operations, investment and organizational cases in Discussion are illustrations.

**False of:** an organization that runs drills, simultaneous trials or chaos tests (routes (b) and (c)) is outside the population; the claim does not say such organizations are rare.

**Falsifier:** operational records of a censored, short-circuit organization from which a latent common cause was detected before any joint failure without any of routes (a)–(e); or incident data in which such organizations' redundancy fails no more often than their independence estimates predict.

**Instantiated:** no.

### Pairwise sibling covariance under exploration detects the latent, and is the detector to use

**Register:** formal for the test's validity under its three preconditions (a standard hypothesis test on jointly observed outcomes; a nonzero covariance of either sign rejects L0 independence); normative for its recommendation as "the AAT-canonical detector", which rests on its using only machinery the theory already requires.

**Population:** L0 learners with SA3 exploration and occasional joint observability of sibling outcomes, after per-edge credences have stabilized, under approximate stationarity over the test window, testing sibling pairs with disjoint modelled ancestor sets (every pair, under L0's tree).

**True of:** #example-L1 (internal consistency, not instantiation): the on-policy table shows the no-go, and the marginal-sampling covariance $0.1008$ between $A_1$ and $A_2$ at L0 is what the test detects.

**False of:** latents with no joint-observability route, latents on one edge, and latents too rare to produce joint outcomes ("What Cannot Be Detected"); for these the test has no data. Latents that correlate three or more siblings only jointly (pairwise independent, mutually dependent), which the pairwise statistic cannot see although the node's propagation is biased. Sibling pairs sharing a modelled ancestor, for which the unconditional covariance is nonzero with every cause modelled (the naive-L1 graph of #example-L1); the criterion excludes them.

**Falsifier:** for validity, a nonzero sibling covariance of the predicted sign arising under the stated preconditions, between siblings with disjoint modelled ancestors, with no cause outside the graph; the Detection criterion is the sentence it would refute. For the recommendation, a domain in which routes (c)–(e) are available and cheaper, which the body allows.

**Instantiated:** no.

## Discussion

**Why the no-go is a strengthening, not a softening.** The prior framing ("the residual mechanism collapses on-policy") was a local observation about one statistic. The no-go is the structural reason: any on-policy statistic must collapse, because the on-policy distribution is identical between L0 and L1 worlds matched on regime conditionals. The covariance test is not just *a* working detector — it is the unique broadly-available violation of the no-go's scope. This sharpens the load-bearing of `#der-loop-interventional-access`: without the loop's interventional data, the no-go forbids detection entirely; with it, route (b) is operational.

**Connection to Pearl's hierarchy.** The L0/L1 distinction is a Level 2 distinction in Pearl's framework — it concerns whether $P(A_2 \mid do(\neg A_1)) = P(A_2 \mid \neg A_1)$. The Causal Hierarchy Theorem (Bareinboim, Correa, Ibeling & Icard 2022, Theorem 1) proves that Level 2 distinctions are not in general identifiable from Level 1 (associational) data. The no-go is the AAT-specific instantiation: on-policy data is Level 1; the L0/L1 question is Level 2; therefore detection requires more than on-policy data. The five circumvention routes are all ways the agent obtains supra-Level-1 information.

**The censoring mechanism is the structural source.** Sequential short-circuit evaluation is what makes on-policy data Level 1 only — it censors the joint outcomes that would constitute Level 2 evidence. An agent that *did not* short-circuit would obtain joint sibling outcomes naturally, and the no-go would not apply. But short-circuit is forced by efficiency: testing $A_2$ when $A_1$ has already succeeded is wasted action. The no-go is therefore a tradeoff between execution efficiency (favoring short-circuit) and structural diagnosis (favoring joint observation). SA3 $\varepsilon$-exploration is the AAT compromise: short-circuit by default, occasional non-short-circuit excursions that pay the efficiency cost to maintain detection capability.

**Connection to the orient cascade.** The detection signal enters the orient cascade ( #der-orient-cascade) at step 4c (causal-sufficiency check). Step 4c's reference to "pairwise sibling covariance under an augmented test" aligns with the primary detection mechanism here. The no-go strengthens the cascade's load-bearing: step 4c is not "one possible diagnostic" but "the unique broadly-available diagnostic given the structural impossibility of purely on-policy detection."

**Connection to the broader identifiability-floor pattern.** The no-go is one of an emerging class of structural impossibility results in AAT — limits on what can be inferred from limited information, derived from external information-theoretic theorems. See #disc-identifiability-floor for the meta-pattern collecting this result alongside the L1' mixture-identifiability obstruction ( #deriv-edge-credence-dynamics Prop B.7) and the open causal-IB extension for interventional relevance variables.

**Domain instantiations.** The covariance test (route (b)) applies concretely in:
- **Software deployment**: two services sharing infrastructure fail together more often than independent failure rates predict → add infrastructure-health node.
- **Military operations**: two concurrent operations fail together under adverse weather → add weather-condition node.
- **Investment**: two positions lose value together during market stress → add market-regime node.
- **Organizational strategy**: two initiatives stall together during leadership transitions → add organizational-stability node.

In each, what makes detection feasible is the agent's ability to occasionally observe *both* sibling outcomes — the route (b) capability. Pure short-circuit ("only run service B if A is down") suppresses the joint-observation events the test relies on; some routine joint exposure is necessary. When joint observation is impossible (routes (b) and (c) both unavailable) and intervention on the candidate latent is impossible (route (e) unavailable), the agent must rely on structural priors (route (d)) — domain knowledge positing the common cause. This is the regime in which intuition-driven causal modeling is the only tractable approach.

## Findings

### On-Policy L0 Insufficiency Is Structurally Undetectable

**Brief:** An agent operating with a strategy model that assumes its action propositions are causally independent (an L0 model) faces a structural impossibility when its world contains a latent common cause acting on multiple of those actions: under purely on-policy execution, no test, statistic, or Bayesian comparison built from the agent's observable history can distinguish the latent-cause world from a no-latent-cause world whose edge probabilities are matched to the on-policy regime conditionals. The two worlds emit identical on-policy distributions. This is not a quirk of any particular diagnostic — it is the agent-theoretic instance of the Causal Hierarchy Theorem applied to the L0/L1 distinction, which is a Level-2 question being asked of Level-1 data. The agent that wants to discover its own model's structural insufficiency must source data the on-policy regime structurally cannot produce.

**Impact:** Reframes exploration from a discretionary diagnostic activity into a structural prerequisite for self-correction at the strategy layer. Each scope-condition violation (S1)–(S5) maps to a specific AAT capability that admits partial detection — most importantly, joint sibling observability under exploration, which lifts `#der-loop-interventional-access` from "useful machinery" to "the unique broadly-available violation of the no-go." Downstream, this hardens the orient cascade's causal-sufficiency check from "one possible diagnostic" to "the only widely-applicable diagnostic"; it explains why the prior aggregate-residual mechanism collapses on-policy (the residual is one statistic the no-go forbids, and *every* on-policy statistic is forbidden); and it gives a precise account of when L0→L1 escalation can and cannot be triggered from the agent's own data.

**Novelty Claim:** *Claim differentiation* on the framing of why structure-aware exploration is required. Causal bandit and causal MDP work under hidden confounding establishes that observational and interventional data are non-interchangeable and that intervention can be necessary for low-regret learning; this finding sharpens that line into a no-go for *self-diagnosis* under policy-perfect execution, tied to latent strategic correlation structure rather than to regret minimization, and characterizes five boundary routes by which AAT machinery escapes it.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Observational vs experimental data are non-equivalent under hidden confounding | Bareinboim, Forney & Pearl 2015, "Bandits with Unobserved Confounders" *NeurIPS* (published 2015, found 2026-04 via Undermind report) | *conceptual precursor* — the underlying observational/interventional asymmetry is shared; this finding recasts it as a no-go on agent self-diagnosis rather than a regret bound on action selection |
| Sequential extension to MDPs | Zhang & Bareinboim 2016, "Markov Decision Processes with Unobserved Confounders" (published 2016, found 2026-04) | *conceptual precursor* — sharpens the bandit asymmetry to sequential control; the present finding's L0/L1 distinction is the strategy-DAG analog at the structural-detection layer rather than the policy-optimality layer |
| Naive randomization can be insufficient under confounding | Forney, Pearl & Bareinboim 2017, "Counterfactual Data-Fusion for Online Reinforcement Learners" *ICML* (published 2017, found 2026-04) | *conceptual precursor* — narrows the gap between generic exploration and structure-aware experimentation; the present finding's covariance test under joint sibling observability is one such structure-aware mechanism, derived as the unique broadly-available violation of the no-go's scope conditions |
| Not all interventions are useful | Lee & Bareinboim 2018, "Structural Causal Bandits" *NeurIPS*; Lee & Bareinboim 2020, "Characterizing Optimal Mixed Policies" *NeurIPS* (published 2018/2020, found 2026-04) | *conceptual precursor* — closest formal neighborhood for "exploration design"; the present finding addresses a different question (when *any* on-policy diagnosis is impossible) but inherits the principle that not all interventional data carries equal structural-detection value |
| Exploration as epistemic-value drive | Friston, Rigoli, Ognibene, Mathys, FitzGerald & Pezzulo 2015, "Active inference and epistemic value" *Cognitive Neuroscience* 6:187–214 (published 2015, found 2026-04) | *adjacent literature* — weaker threat because EFE-based exploration reduces uncertainty under the generative model rather than Pearl-style observational equivalence under hidden common causes; the structural-undetectability claim does not arise in the EFE framework, which presumes a generative model expressive enough to represent the latent |
| Theorem the no-go imports | Causal Hierarchy Theorem: SCMs agreeing on Level 1 may disagree on Level 2 (Bareinboim, Correa, Ibeling & Icard 2022, in *Probabilistic and Causal Inference: The Works of Judea Pearl*; published 2022, found 2025) | *formal antecedent* — the no-go is the AAT-specific instantiation; the L0/L1 distinction is precisely a Level-2 question (concerns $P(A_2 \mid do(\neg A_1))$ vs $P(A_2 \mid \neg A_1)$) being asked of on-policy Level-1 data |

**Search Log:**

- 2026-04 (*nominally comprehensive*, via `ref/Novelty_defense_and_integration.md` Pillar 1): Undermind report on the causal-bandits-and-MDPs-under-hidden-confounding literature, plus active-inference epistemic-value exploration, established the prior-art landscape; verdict was *Conceptual Precursor* (High confidence). The closest formal neighborhood is the Bareinboim/Zhang/Forney/Lee line; no paper surveyed states the claim in the same form (no-go for self-diagnosis under policy-perfect execution tied to latent strategic correlation). The defense strategy positions ASF's increment narrowly: a no-go theorem on structural detection rather than a regret bound on action selection, with five explicit boundary routes mapped to existing AAT machinery.
- 2025 (*targeted*): Bareinboim, Correa, Ibeling & Icard 2022 identified as the formal antecedent for the Causal Hierarchy Theorem invocation; the segment's invocation of the CHT was already grounded in this source before the comprehensive Pillar-1 defense.

## Working Notes

- The general-topology construction is a structural argument; the explicit $\mathcal W_{L0}^\ast$ for arbitrary AND/OR DAGs with mixed common-cause patterns has not been carried out. For load-bearing application of the no-go to specific complex topologies, the construction should be specialized. Currently the load-bearing applications (orient-cascade step 4c, strategy-dag's L0/L1 escalation principle) reference shallow strict-prerequisite cases for which the no-go is exact.
- The boundary characterization's routes (c) and (e) depend on domain capability and are not formalized in AAT beyond cross-references to `#der-observability-dominance` and `#der-loop-interventional-access`. A future refinement could quantify "detection power" per route as a function of domain parameters (e.g., observability cost, intervention availability, prior strength).
- The no-go is asymmetric: it forbids on-policy *detection* of L1 from L0, but it does *not* forbid on-policy *parameter learning within L0*. The agent can learn its L0 conditionals to arbitrary precision on-policy; it just cannot determine whether those conditionals hide a latent. This distinction sharpens the diagnosis-vs-calibration split that #result-structural-adaptation-necessity makes at the parametric/structural boundary.
- The CHT (Bareinboim et al. 2022) is invoked as an external theorem. AAT inherits its conditions (well-defined SCMs over compatible variable sets); these are satisfied for the strategy-DAG setting by construction.

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. *Orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals), staged for an eventual careful promotion pass, kept separate from the certified theory-fix findings. **Coverage for this segment:** 193847, 361742, 471203, 526815, 584721, 773921, 829314, 849201. (Two of the substrates rated this segment top-decile / "one of the framework's strongest pieces.")

#### 1. Candidate Brief prose / pre-prose

- **The one-line stake.** Several substrates converged on the same plain-language hook: an agent operating strictly on-policy in a confounded world "will develop perfectly calibrated, completely wrong causal beliefs, and the math proves it cannot detect its own error without breaking policy" (Claude/193847) — i.e. "making mistakes is a structural prerequisite for maintaining a causal grip on reality" (Gemini/773921). Strong candidate Brief opener.
- **The asymmetry as the precise statement of the no-go:** "on-policy parameter learning is fine; on-policy *structural* detection is forbidden" — an L0 agent can converge to perfect L0 conditionals and still be in an L1 world without ever knowing (Claude/584721). Already in Working Notes; flagged for surfacing more prominently because it *is* the sharp content.

#### 2. Candidate Discussion

- **"Efficiency destroys diagnostic observability."** The censoring mechanism (sequential short-circuit AND/OR evaluation) is the structural source of the no-go: "if I want to do A AND B, and A fails, I don't bother trying B … I never observe the joint outcome (A fails, B fails), which is exactly the data I need" (Claude/193847). Multiple substrates independently named short-circuit-efficiency and self-diagnosis as in *direct mathematical opposition* (Claude/193847, 526815, 584721; Gemini/773921, 829314). A candidate Discussion framing of *why* the censoring condition (S2) is load-bearing rather than incidental.
- **Diagnostic CIY as a fourth action axis.** This segment introduces "diagnose" alongside explore / exploit / deliberate — testing *structural* assumptions (joint outcomes), distinct from testing edge *values*. Candidate to develop as a four-axis framework and to reconcile with the three-way `#disc-exploit-explore-deliberate` (Claude/584721, 361742; Gemini/829314).

#### 3. Follow-up items

- **One non-shallow construction wanted.** The no-go is exact for shallow strict-prerequisite cases and robust-qualitative for general topology; the audit suggests at least one mixed-AND/OR + multiple-latent construction to back the general claim (Claude/471203). Tracks the existing Working-Notes general-topology item.

#### 4. Readers often ask / wonder

- **How is the tempo budget split across explore / exploit / diagnose?** Once "diagnose" is named as its own axis, allocation across the (now) four drives is the natural next question (Gemini/829314; Claude/584721).
- **How does the agent set $\varepsilon$** (the exploration / redundant-test rate) to balance the efficiency cost of joint observation against the value of detecting latents? (Claude/849201, 193847).

#### 5. Candidate figures

- **Two-worlds-funnel diagram.** Draw $\mathcal W_{L1}$ (latent common cause) and the matched $\mathcal W_{L0}^\ast$ both funneling into the *same* censored on-policy trace; the five escape routes are "side doors" that add the missing joint or structural information. Proposed as clearer than another covariance-test table (Codex/526815).

#### Belongs elsewhere

- **Chaos engineering / red-teaming / drills → TST + general systems.** The data-center worked instance: a primary-DB-then-backup-DB OR with short-circuit fallback "never queries the Backup when the Primary is healthy", so it cannot compute the failure covariance and is blind to a shared-power-supply latent until simultaneous failure. This gives "a rigorous mathematical foundation for Chaos Engineering, red-teaming, and military drills … a system that optimizes purely for on-policy efficiency is mathematically guaranteed to harbor undetectable structural fragilities" (Gemini/829314); "testing in production is mathematically necessary — staging environments (L0 models) structurally cannot predict latent common causes (L1 reality)" (Gemini/773921). Domain reach into `02-tst-core/` and systems engineering, not this segment.
- **The mathematical root of *play* → `04-eli-core/`.** "Play is action stripped of its immediate purposeful efficiency … it generates the uncensored joint-outcome data required to build a valid L1 causal model." An infrastructure that forbids "wasting time" forces the intelligence into a brittle, superstitious L0 understanding — so a developmental crèche must *budget* for non-efficient joint exploration (Gemini/193847). Aspirational reach pointing at developmental-environment material in `04-eli-core/`.
- **Christensen's innovator's dilemma as a corollary → strategy/organizational-positioning material.** The no-go is "a formal version of Christensen's innovator's dilemma: incumbents doing the rational thing (optimizing on the on-policy distribution) systematically fail to detect disruptive structural changes that only become visible through off-policy exploration … predicted as a *structural impossibility, not a motivational failure*" (Claude/451729). Candidate cross-domain instantiation; lands more naturally in adversarial/competitive or positioning material than in this segment.
