# Strategy Dynamics


## Definition: Strategic Calibration

- **Slug**: `def-strategic-calibration`
- **Type**: definition
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `def-strategy-dag`, `def-value-object`

The strategic calibration residual measures whether the strategy's causal model is correct: are the edges in $\Sigma_t$ accurate predictors of how much value each step actually produces? This is the fine-grained diagnostic that localizes control regret to specific parts of the strategy.

*[Definition (strategic-calibration)]*

For each edge $(i, j)$ in $\Sigma_t$ with credence $p_{ij}$, the **edge residual**:

$$r_{ij} = \mathbb{E}[\Delta V_O \mid \text{edge } (i,j) \text{ traversed},\, M_t] - \Delta V_O^{\text{observed}}$$

where $\Delta V_O$ is the change in $V_O(M_t, \pi;\, N_h)$ attributable to completing step $j$ — as predicted by $\Sigma_t$ versus as observed.

The **strategic calibration residual** aggregates across active edges:

$$\delta_{\text{strategic}} = \left(\sum_{(i,j) \in \text{active}} w_{ij} \cdot r_{ij}^2 \right)^{1/2}$$

where $w_{ij}$ weights edges by importance (e.g., criticality to the current plan's critical path).

**Conditioning.** The edge residual $r_{ij}$ is meaningful only when:
- The edge was actually traversed (the agent attempted the step)
- $M_t$ is adequate (so the observed $\Delta V_O$ is meaningful, not noise)
- The agent followed $\Sigma_t$'s prescription for step $j$ (execution fidelity — otherwise the residual conflates bad plan with bad execution)

Without the execution fidelity condition, a positive residual could mean "the plan is wrong" or "the agent didn't follow the plan." These require different corrections ($\Sigma_t$ revision vs. execution improvement).

---



## Derived: Causal Insufficiency Detection

- **Slug**: `der-causal-insufficiency-detection`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `result-structural-adaptation-necessity`, `def-strategy-dag`, `der-loop-interventional-access`, `der-causal-hierarchy-requirement`, `def-pearl-causal-hierarchy`, `def-causal-information-yield`

An agent operating at L0 of the Correlation Hierarchy ( #def-strategy-dag) faces a structural impossibility: under purely on-policy execution, no detection mechanism can distinguish an L0-insufficient world (latent common causes present) from an L0-sufficient world matched to the on-policy regime conditionals. This is a consequence of the causal hierarchy theorem ( #def-pearl-causal-hierarchy, #der-causal-hierarchy-requirement) — observational data does not in general identify interventional structure. Detection is therefore *only* possible by capabilities that violate the "purely on-policy" condition: joint sibling observability under exploration (the canonical AAT route, exploiting #der-loop-interventional-access), intermediate-state observability, structural priors, or direct intervention on the candidate latent. The pairwise sibling covariance test is the AAT-canonical detector; the L0 plan-level residual is a degenerate special case of the no-go.

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

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause and $\theta_{j \mid \neg C} = 0$ — see #example-L1). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures: the structural argument transfers, but explicit $\mathcal{W}_{L0}^\ast$ construction has been carried out only for shallow cases.

**Construction of $\mathcal{W}_{L0}^\ast$.** For a 2-sibling OR with strict-prerequisite latent $C$, $P(C) = \theta_C$, conditional success rates $\theta_{j \mid C}$:

$$\theta_1^\ast = \theta_C \cdot \theta_{1 \mid C}, \qquad \theta_2^\ast = p_2^c = \frac{\theta_C\,(1 - \theta_{1 \mid C})\,\theta_{2 \mid C}}{1 - \theta_C\,\theta_{1 \mid C}}$$

Direct verification (see #example-L1) shows $\mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L1}] = \mathbb{P}_{\pi_{L0}}^{\text{obs}}[\mathcal{W}_{L0}^\ast]$ on the three on-policy observable events. The Bareinboim, Correa, Ibeling & Icard (2022) Causal Hierarchy Theorem then gives the no-go: any two SCMs that agree on Level 1 (associational) data cannot in general be distinguished on Level 2 (interventional) questions, and the L0/L1 distinction — whether siblings share a common cause — is precisely a Level 2 question about $P(A_2 \mid do(\neg A_1))$ versus $P(A_2 \mid \neg A_1)$.

**Why this matters.** The no-go is the structural reason the prior aggregate-residual mechanism collapses on-policy: the residual is a function of $\mathbb{P}_{\pi_{L0}}^{\text{obs}}$, which is identical between the two worlds, so the residual is identically zero under both. The collapse is not a quirk of the residual statistic — it is a special case of the no-go applied to that specific function. No replacement aggregate statistic can do better.

### The Detection Routes: What Circumvents the No-Go

*[Derived (boundary-routes, from no-go scope conditions)]*

The no-go's scope conditions (S1)–(S5) define "purely on-policy." Each condition's violation corresponds to an AAT capability that admits (partial) detection:

| Route | Scope violated | AAT capability | Detection strength |
|-------|----------------|----------------|--------------------|
| (a) ε-exploration | (S1) | SA3 exploration ( #deriv-edge-credence-dynamics Prop B.4) | Partial, scales with ε |
| (b) Joint sibling observability | (S3) | Covariance test under SA3 + #der-loop-interventional-access | Strong |
| (c) Intermediate observability | (S3) at finer grain | Observability investment ( #der-observability-dominance) | Very strong when available |
| (d) Structural priors | (S5) | Hypothesized common-cause nodes in DAG construction | Prior-quality-dependent |
| (e) Direct intervention on latent | (S4) | Domain-specific latent control | Strongest when available |

The covariance test (route (b)) is the AAT-canonical detector: it uses only machinery the theory already requires (exploration via SA3, interventional data via the loop) and is available in the broadest range of domains. The remaining sections operationalize this primary mechanism.

### Primary Detection Mechanism: Pairwise Sibling Covariance Under Intervention

*[Derived (from loop-interventional-access + independence test, conditional on SA3 exploration providing joint observability)]*

Under L0 (the independence model in #def-strategy-dag's Correlation Hierarchy), sibling outcomes under a common parent are uncorrelated:

$$H_0:\;\operatorname{Cov}(Y_{A_i}, Y_{A_j}) = 0 \quad \forall\; i \neq j \;\text{siblings under the same parent}$$

Under causal insufficiency (latent common cause $C$ acting on multiple siblings), sibling outcomes are positively correlated:

$$H_1:\;\exists\; i \neq j \;\text{with}\; \operatorname{Cov}(Y_{A_i}, Y_{A_j}) \gt 0$$

The agent generates test data through the standard exploration mechanism (SA3 — $\varepsilon$-greedy or similar). On trials where both siblings are observable — the agent tries one and can also observe the other's outcome, or tries them in rapid succession before the environment state changes — it accumulates the empirical covariance:

$$\hat\rho_{ij} = \frac{1}{N}\sum_t (Y_{A_i,t} - \bar{Y}_{A_i})(Y_{A_j,t} - \bar{Y}_{A_j})$$

A significantly positive $\hat\rho_{ij}$ rejects the L0 independence hypothesis. Joint observability ( #der-loop-interventional-access supplies the interventional character; SA3 supplies the joint sampling) is precisely the violation of scope condition (S3) that admits the test under the no-go.

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

*[Derived (from positive covariance signal + L1 construction principle in #def-strategy-dag)]*

Once the agent detects $\hat\rho_{ij} \gt 0$ between siblings $A_i$ and $A_j$, it knows a latent common cause exists but not its identity. The construction process:

1. **Hypothesize** a common-cause node $C$ that explains the correlation.
2. **Estimate** $\theta_C$ from the pattern of joint outcomes. The joint failure rate $P(A_i\text{ fails}, A_j\text{ fails})$ exceeds $(1-\theta_i)(1-\theta_j)$ by $\hat\rho_{ij}$; the excess localizes the common cause's frequency.
3. **Restructure** the DAG: factor $C$ above the correlated siblings ( #def-strategy-dag, L1 construction principle: factor the common cause above the correlation it creates).
4. **Re-estimate** conditional edge credences $\theta_{k\mid C}$ from the data, conditioned on the inferred $C$ state.

This is structural adaptation ( #result-structural-adaptation-necessity) at the strategy level: the agent changes its model class from L0 to L1, adding representational capacity for a pattern the L0 model cannot express. The cost is the standard cost of structural change: temporary performance degradation while the new credences converge, and increased graph complexity. (Soft-facilitator common causes require L1' rather than L1 — see #def-strategy-dag and #example-L1 for the strict-prerequisite vs soft-facilitator distinction.)

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

---



## Derived: Observability Dominance

- **Slug**: `der-observability-dominance`
- **Type**: derived
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `def-strategy-dag`, `emp-update-gain`

Unobservable strategy edges cannot be updated — the gain principle drives their update rate to zero. This means the agent's effective strategy is limited to the parts it can observe, regardless of the nominal confidence in unobservable paths. Observability dominates nominal confidence in determining which strategies are epistemically alive.

*[Derived (observability-dominance, from update-gain + strategy-dag)]*

For a path $P$ through $\Sigma_t$, the **path observability**:

$$\text{obs}(P) = \min_{v \in P} \sigma_v$$

where $\sigma_v$ is the observability of node $v$ — how well the agent can determine whether $v$ has been achieved. The weakest link determines the path's observability.

**Observability-adjusted confidence:**

$$\text{conf}_{\text{obs}}(P) = \text{conf}(P) \cdot \text{obs}(P)$$

When $\sigma_v \approx 0$ for any node $v$ on the path: by #emp-update-gain, $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}}) \to 0$ as $U_{\text{obs}} \to \infty$. The edges connecting to $v$ are **frozen at their prior** — the agent cannot update them regardless of what happens. The path is epistemically dead.

---



## Hypothesis: Edge Update via Gain

- **Slug**: `hyp-edge-update-via-gain`
- **Type**: hypothesis
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `def-strategy-dag`, `emp-update-gain`, `def-mismatch-signal`, `der-chain-confidence-decay`

The uncertainty-ratio gain principle ( #emp-update-gain) extends from epistemic updates to strategy-edge updates: edge credences revise in proportion to the ratio of edge uncertainty to observation noise, modulated by the identifiability of the causal link ( #scope-edge-update-causal-validity). This gives a principled, conservative update rule that avoids overreacting to single observations and degrades gracefully when causal identification is weak.

*[Hypothesis (edge-update-via-gain)]*

Edge credences update via:

$$p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot \left(\text{signal}(o_t, i, j) - p_{ij}^{\text{old}}\right)$$

where:
- $\text{signal}(o_t, i, j) \in [0, 1]$: evidential content of observation $o_t$ about the causal link $i \to j$
- $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$: update gain

with:
- $U_{\text{edge}}$: uncertainty about this specific causal link. If $p_{ij} \sim \text{Beta}(\alpha_{ij}, \beta_{ij})$: $U_{\text{edge}} = \text{Var}[\text{Beta}] = \alpha\beta / ((\alpha + \beta)^2(\alpha + \beta + 1))$
- $U_{\text{obs}}$: observation noise on the channel confirming this link. $U_{\text{obs}} \propto 1/\sigma_j$ (inverse of observability of node $j$)

**Beta-Bernoulli instantiation.** For binary observations (success/failure of step $j$):
- Observe success: $\alpha_{ij} \to \alpha_{ij} + 1$
- Observe failure: $\beta_{ij} \to \beta_{ij} + 1$
- Point estimate: $p_{ij} = \alpha / (\alpha + \beta)$
- Effective gain: $\eta_{\text{edge}} = 1/(n+1)$ where $n = \alpha + \beta$

This is the standard Bayesian conjugate update, yielding $\Delta\hat p = (y - \hat p)/(n+1)$. The gain $1/(n+1)$ is the exact conjugate update rate — not a literal substitution into $\eta = U_{\text{edge}}/(U_{\text{edge}} + U_{\text{obs}})$, which is a structural principle (conservative updating proportional to relative uncertainty), not a universal algebraic formula. The Beta-Bernoulli gain satisfies the same principle: it decreases as posterior certainty increases, trusting accumulated evidence over individual observations. But the algebraic derivation is conjugate analysis, not Kalman-style variance ratios, because the Bernoulli observation model has different noise structure than the Gaussian case where the variance-ratio formula is exact. The sector-condition analysis in #deriv-edge-credence-dynamics (Props B.1-B.4) uses the exact Beta-Bernoulli gain $1/(n+1)$ directly.

**Parallel log-odds presentation.** The same update is natively additive in the log-odds coordinate $\lambda_{ij} = \log(p_{ij}/(1 - p_{ij}))$:

$$\lambda_{ij}^{\text{new}} = \lambda_{ij}^{\text{old}} + \ell(y)$$

where $\ell(y) = \log[P(y \mid \text{edge true})/P(y \mid \text{edge false})]$ is the per-observation log-likelihood ratio. The log-odds coordinate is the unique (up to positive affine transformation) parameterization on which Bayesian independent-evidence accumulation is additive — forced by the evidential-additivity axiom derived in #deriv-edge-update-natural-parameter, which is the update-level analog of #der-chain-confidence-decay's chain-level additive log-confidence decomposition. The moment-parameter (probability-space) form $\Delta\hat p = (y - \hat p)/(n+1)$ is the projected image of the log-odds additive update under the sigmoid readout $p = \sigma(\lambda)$; the two coordinates carry equivalent content.

The log-odds presentation matters for #disc-credit-assignment-boundary's default signal function, where continuous-gradient updates can break the $[0, 1]$ domain in probability-space presentation but are well-posed globally on $\lambda \in \mathbb{R}$. For the per-edge Beta-Bernoulli derivation of Props B.1–B.4 in #deriv-edge-credence-dynamics, the moment-parameter form is retained because algebraic tightness (the gain $1/(n+1)$ is exact in probability space) is pedagogically cleaner; the sector-parameter content is Fisher-equivalent in either coordinate.

---



## Scope: Causal Validity of Edge Updates

- **Slug**: `scope-edge-update-causal-validity`
- **Type**: scope
- **Status**: conditional
- **Stage**: deps-verified
- **Depends**: `hyp-edge-update-via-gain`, `def-causal-information-yield`, `der-loop-interventional-access`, `def-strategic-calibration`, `def-strategy-dag`

The gain-based edge update ( #hyp-edge-update-via-gain) revises edge credences $p_{ij}$ --- causal efficacy estimates whose identification strength varies with the data regime ( #def-strategy-dag). This segment scopes where the update yields credences that approximate the interventional quantity $P(j \mid do(i), M_t)$, where it yields partially identified estimates, and where it yields associational proxies.

*[Scope Condition (edge-update-causal-validity)]*

### Where the agent has direct intervention

By #def-strategy-dag, leaf action nodes are propositions about the agent's own actions: "action $a$ succeeds at $\tau_v$." When the agent executes an action leaf, it performs a genuine $do(\cdot)$ operation. The edge from that leaf to its child carries credence $p_{ij} = \text{Cr}(j \text{ advances} \mid do(i), M_t)$, and the execution-observation pair $(do(i), o_j)$ is interventional data for that edge.

However, interventional data does not automatically yield clean causal identification. By #der-loop-interventional-access, the loop provides data *generated under intervention* — but between the intervention and a usable causal estimate stand coverage, within-step confounding, delay, and partial observability. The following conditions determine when the interventional data is strong enough for valid edge revision:

**(C1) The parent is an action leaf under the agent's control.** The agent directly executed the action. This makes the data interventional in character — the agent chose the action, the environment responded. For condition leaves (observable states the agent doesn't control) and internal nodes (propositional combinations achieved indirectly), $do(i)$ is not directly available. See "Indirect edges" below for the weaker identification available at those positions.

**(C2) The outcome is attributable.** The agent can distinguish whether $j$ advanced specifically because of $do(i)$, or for other concurrent reasons. This is the credit-assignment problem identified in #def-strategic-calibration. It is trivially satisfied for single-parent nodes (one possible cause) and for well-isolated interventions. It is violated when multiple parent edges of $j$ fire concurrently.

**(C3) Execution conditions vary.** The agent does not systematically execute $i$ only under conditions that independently favor $j$'s success. If it does, the observed success rate carries selection bias: $P(j \mid \text{chose to execute } i) \neq P(j \mid do(i))$ because the decision to execute correlates with favorable conditions. This is mitigated when the agent varies execution contexts across episodes, or when external factors (CI pipelines, scheduled operations) force execution regardless of conditions.

C1 establishes that the data is interventional. C2 and C3 determine whether the interventional signal can be cleanly extracted. All three are satisfied simultaneously in Regime A domains; they degrade together in Regime B and C domains.

### Three regimes

These conditions partition domains into admissibility regimes, paralleling #scope-ciy-observational-proxy:

| Regime | C1 | C2 | C3 | Causal validity of leaf-edge updates |
|--------|----|----|----|----|
| **A: Intervention-rich** | Agent controls leaf actions | Good isolation (one action at a time) | Conditions vary (CI, diverse contexts) | **Strong.** Updates approximate interventional. |
| **B: Partial intervention** | Agent acts but with coordination constraints | Concurrent actions blur attribution | Self-selection likely | **Moderate.** Updates carry optimistic bias. |
| **C: Observation-only** | Agent did not act (condition leaves, passive monitoring) | Attribution impossible | Confounding dominant | **Weak.** Updates reflect association, not causation. |

### Indirect edges

For edges between non-leaf nodes, or edges whose parent is a condition node, the agent does not directly intervene on the parent. Instead, the agent's interventions at the leaves propagate upward through the DAG. The edge $(i, j)$ where $i$ is an internal node receives *indirect* interventional evidence: the agent intervened on leaves below $i$, observed that $i$ was (or wasn't) achieved, and then observed whether $j$ advanced.

This indirect evidence is weaker for two reasons:
1. **Compounding attribution**: the agent must attribute $j$'s outcome to edge $(i, j)$ after already attributing $i$'s achievement to the leaf-level interventions. Each attribution step introduces uncertainty.
2. **Confounding from below**: $i$'s achievement depends on multiple leaf actions and condition states. Even if each leaf intervention is clean, their combined effect on $i$ may be confounded.

The identification strength for indirect edges decreases with depth in the DAG — deeper edges are farther from the agent's direct interventions and have more confounding pathways.

### Identifiability-adjusted gain

*[Hypothesis (identifiability-coefficient)]*

The update gain should be adjusted by the agent's confidence in causal attribution:

$$\eta_{\text{edge}}^{\text{adj}} = \eta_{\text{edge}} \cdot \iota_{ij}$$

where $\iota_{ij} \in [0, 1]$ is the **identifiability coefficient** — the agent's estimate of how cleanly the observed outcome can be attributed to edge $(i, j)$ specifically.

- $\iota_{ij} = 1$: clean attribution (leaf-originating edge, single parent, isolated execution in Regime A).
- $\iota_{ij} \approx 0$: no attribution possible (deep internal edge, many concurrent causes, Regime C).

For leaf-originating edges in Regime A: $\iota_{ij} \approx 1$. For internal edges at depth $d$: $\iota_{ij}$ decreases with $d$ (each level of indirect inference degrades attribution). The precise functional form is domain-dependent.

This unifies two sources of frozen edges:
1. Low **observability** ($\sigma_v \approx 0$ from #der-observability-dominance): the node's outcome is hard to *measure*.
2. Low **identifiability** ($\iota_{ij} \approx 0$): the outcome is measurable but can't be *attributed* to this edge.

Both drive $\eta_{\text{edge}} \to 0$ and produce the same effect: the edge is frozen at its prior.

---



## Discussion: Credit Assignment Boundary

- **Slug**: `disc-credit-assignment-boundary`
- **Type**: discussion
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `def-strategy-dag`, `hyp-edge-update-via-gain`, `deriv-edge-update-natural-parameter`, `def-strategic-calibration`, `der-observability-dominance`, `der-gain-sector-bridge`, `deriv-edge-credence-dynamics`

The strategy-revision loop requires assigning credit for observed outcomes to specific edges in the strategy DAG — decomposing "the plan partially worked" into "step 3 failed, step 5 was irrelevant, step 1 succeeded." This is AAT's version of RL's temporal credit assignment problem. This segment characterizes the boundary between tractable and intractable cases, states what the theory requires of any credit-assignment scheme, and identifies what the theory can guarantee without solving the problem at all.

### The Credit Assignment Problem for Strategy DAGs

*[Discussion (credit-assignment-problem)]*

Given strategy DAG $\Sigma_t = (V, E, p, \gamma)$, an observed outcome at the root (and possibly at some intermediate nodes), produce per-edge signals $\text{signal}(o_t, i, j)$ for each edge $(i,j) \in E$ such that the edge update

$$p_{ij}^{\text{new}} = p_{ij} + \eta_{\text{edge}} \cdot (\text{signal}(o_t, i, j) - p_{ij})$$

drives credences toward truth. The problem is trivial when all intermediates are observable (each edge updates from its own observation) and genuinely hard when intermediates are unobservable and the DAG has shared structure.

### Default Signal Function (Gradient-Based Attribution, Regime-Aware)

*[Formulation (gradient-signal-function)]*

Any edge-update signal function decomposes along three independent axes: *what happened* at the child node, *whether that outcome is attributable* to the specific edge being updated, and *how causal* the evidence is:

$$\text{signal}(o_t, i, j) = f\bigl(\text{outcome}(o_t, j),\; \text{attribution}(o_t, i, j),\; \text{regime}(i, j)\bigr)$$

The outcome component answers "what was observed at $j$?" The attribution component answers "can we credit that outcome to edge $(i,j)$ specifically, or did other parents contribute?" The regime component answers "how causal is the evidence — is it interventional (Regime A), partially identified (Regime B), or observational (Regime C)?" This decomposition is derived from the regime-indexed edge semantics of #def-strategy-dag and #scope-edge-update-causal-validity: the same signal pipeline must carry the regime distinction through to the update.

AAT's default implementation, analogous to $\eta^\ast = U_M/(U_M + U_o)$ being the default gain. The update is stated in the log-odds coordinate $\lambda_k = \log(p_k/(1-p_k))$ — the unique additive-evidence coordinate forced by the evidential-additivity axiom ( #deriv-edge-update-natural-parameter). The probability-space form is the projected image via $p_k = \sigma(\lambda_k)$ at the readout interface:

$$\lambda_k^{\text{new}} = \lambda_k + \eta_{\text{edge}} \cdot \iota_k \cdot \frac{J_k \cdot (y_G - \hat P_\Sigma)}{\lVert\mathbf{J}\rVert^2}, \qquad p_k^{\text{new}} = \sigma(\lambda_k^{\text{new}})$$

where:
- $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$ is the plan-value gradient (computable from status propagation in $O(\lvert V\rvert + \lvert E\rvert)$) — supplying the *attribution* component
- $(y_G - \hat P_\Sigma)$ is the plan-level residual — the *outcome* component
- $\iota_k \in [0, 1]$ is the edge's identifiability coefficient ( #scope-edge-update-causal-validity) — the *regime* modulation, scaling the correction by the fraction of evidence that genuinely identifies this edge's causal effect
- $\eta_{\text{edge}}$ is the edge-level update gain ( #hyp-edge-update-via-gain); for Beta-Bernoulli the moment-parameter form recovers $\eta_{\text{edge}} = 1/(n_k+1)$ under the sufficient-statistic correspondence

For Regime-A edges ($\iota_k \approx 1$), the log-odds update recovers the pure gradient-based form $\Delta\lambda_k = \eta_{\text{edge}} \cdot J_k(y_G - \hat P_\Sigma)/\lVert\mathbf{J}\rVert^2$. For Regime-C edges ($\iota_k \approx 0$), the update is essentially zero — no meaningful update is made because no meaningful causal evidence is available. Regime-B edges receive proportionally reduced updates that honestly reflect the weaker identification.

**Why log-odds rather than probability-space.** In probability space, the same update written as $\text{signal}_k - p_k$ can push $p_k^{\text{new}}$ outside $[0, 1]$ when $\lVert\mathbf{J}\rVert^2$ is small — a mechanical break of the $[0, 1]$ probability domain. The log-odds coordinate has domain $\mathbb{R}$, so additive updates never escape the domain; the sigmoid projection at the readout interface guarantees $p_k^{\text{new}} \in (0, 1)$ by construction. The log-odds coordinate is the unique (up to positive affine transformation) parameterization on which Bayesian independent-evidence accumulation is additive ( #deriv-edge-update-natural-parameter); this makes it the natural presentation for any continuous-gradient update rule that aims to preserve Bayesian coherence. The probability-space presentation remains useful for interpretation but is the projected image, not the native update coordinate.

**Properties:**
- **Domain closure (no mechanical break):** Updates live on $\lambda_k \in \mathbb{R}$, so no update magnitude can push credence outside the valid probability domain. The sigmoid projection $p_k = \sigma(\lambda_k) \in (0, 1)$ at the readout interface guarantees $[0, 1]$ boundedness by construction — not by clipping. The historical probability-space presentation required a normalization constant and could diverge when $\lVert\mathbf{J}\rVert^2 \to 0$; the log-odds presentation eliminates this failure mode.
- **Directional fidelity (B1):** For $\iota_k \gt 0$, satisfies $\mathbb{E}[\Delta\lambda_k] \propto \iota_k \cdot J_k(\Phi - \hat P_\Sigma) \propto \iota_k \cdot J_k \cdot \delta_s$. Since $J_k \geq 0$ for monotone AND/OR DAGs and $\iota_k \geq 0$ by definition, the expected log-odds update pushes each edge's credence toward truth whenever evidence is available to push it. The probability-space image inherits directional fidelity through the monotonic sigmoid.
- **Sector parameter:** $\alpha_s = \iota_k \cdot \eta_{\text{edge}}$ for componentwise corrections (regime-adjusted Prop B.5b); $\alpha_s = \iota_k \cdot \eta_{\text{edge}} / \kappa(\mathbf{J})^2$ for coupled corrections. Regime-C edges have $\alpha_s \approx 0$, making them effectively frozen — consistent with #der-observability-dominance's treatment of unobservable edges. The sector parameter is Fisher-equivalent across coordinates (see Epistemic Status); the probability-space and log-odds-space statements of Props B.1–B.7 carry the same content.
- **Computational cost:** $O(\lvert V\rvert + \lvert E\rvert)$ — the same forward pass that computes $\hat P_\Sigma$ also yields $\mathbf{J}$. The $\iota$ factors are per-edge domain parameters, not computed from the DAG structure. The sigmoid projection is $O(\lvert E\rvert)$ per update step.
- **Relationship to RL:** This is the AAT analog of REINFORCE with a causal-identification weighting — the Jacobian $\mathbf{J}$ is the score function, $(y_G - \hat P_\Sigma)$ is the advantage, and $\iota_k$ is the causal-validity discount on each edge's update.

**Correlated-failure interaction (L0 vs L1).** The gradient signal operates at L0 of the Correlation Hierarchy ( #def-strategy-dag). When the DAG is causally insufficient (the dominant real-world case), the residual $(y_G - \hat P_\Sigma)$ decomposes into per-edge miscalibration *plus* omitted correlation structure. $\hat P_\Sigma$ systematically overestimates success, making the residual systematically negative on failure. The gradient signal then attributes to individual edges what is actually causal insufficiency (missing common-cause nodes). The signal retains directional fidelity *on average* (it pushes edges downward when the plan is overconfident, which is the correct direction), but the per-edge attribution is contaminated. The principled fix is L1: add common-cause nodes to restore causal sufficiency, then apply gradient attribution to the augmented DAG. In the augmented DAG, the residual correctly decomposes into per-edge miscalibration because the correlation structure is explicitly represented.

Domains with richer observation structure can do better (Thompson sampling, full belief propagation, domain-specific attribution). The gradient-based signal is the *concrete Level 1 default* — the minimum viable credit-assignment scheme that satisfies the theory's requirements.

### What the Theory Can Guarantee Without Solving Credit Assignment

Three results hold independently of any specific credit-assignment scheme:

**1. Persistence is credit-assignment-free.** Proposition B.5 in #deriv-edge-credence-dynamics shows that the sector condition transfers from per-edge credence space to **strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$ via the Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$. The Jacobian is computable from status propagation in $O(\lvert V\rvert + \lvert E\rvert)$ — no outcome decomposition required. The persistence guarantee (whether the strategy's plan-level self-assessment can be maintained) does not depend on the agent's ability to attribute outcomes to edges. **Note:** this proves persistence of $\delta_s$ (strategy-plan-confidence error), not of $\delta_{\text{strategic}}$ (the per-edge calibration residual from #def-strategic-calibration). Extending persistence to $\delta_{\text{strategic}}$ requires solving the credit-assignment problem — that is the gap this segment characterizes.

**2. The diagnostic framework is plan-level.** The satisfaction gap ( #def-satisfaction-gap), control regret ( #def-control-regret), and the orient cascade ordering ( #der-orient-cascade) operate on aggregate value, not per-edge quantities. They tell the agent *whether* the strategy is failing (and whether the failure is feasibility vs. optimality vs. calibration), without requiring per-edge attribution.

**3. Observability-dominance identifies the tractable edges.** #der-observability-dominance determines which edges have nonzero observability — only these can receive informative signals. Edges with zero observability are frozen regardless of the credit-assignment scheme. The tractable boundary is the observable subgraph of $\Sigma_t$.

### The Tractable Cases

*[Discussion (tractable-credit-assignment)]*

Credit assignment is solved (exact, polynomial-time) when:

| Condition | Why tractable | Update rule |
|---|---|---|
| **All intermediates observable** | Each edge has its own observation; updates decouple | Beta-Bernoulli per edge (Prop B.2) |
| **Binary outcomes, independent edges, linear chain** | Marginal Bayesian update = proportional blame | Prop B.3 (with plan-level fallback for unobservable) |
| **Tree DAG, observable leaves** | No shared descendants; message passing is exact | Belief propagation (standard) |

### The Intractable Cases: Three Independent Barriers

*[Discussion (intractable-credit-assignment)]*

Exact per-edge attribution in general AND/OR DAGs with partial observability faces three independent barriers:

**1. Computational intractability (\#P-hardness).** The "contribution of edge $k$ to the observed outcome" has the form of a Shapley value over a cooperative game defined by the AND/OR propagation. Since AND/OR DAGs can represent any monotone Boolean function (including weighted threshold functions), and Shapley value computation for weighted voting games is \#P-complete (Deng and Papadimitriou, 1994), exact attribution is \#P-hard. *Caveat:* the reduction is to *exact* computation; approximate Shapley values are computable in polynomial time with sampling.

**2. Information-theoretic underdetermination.** When intermediates are unobservable, per-edge attribution is *underdetermined*, not just hard. The identifiable subspace has dimension bounded by the number of observable nodes:

$$\dim(\mathcal{I}(\mathcal{V}_{\text{obs}})) \leq \lvert\mathcal{V}_{\text{obs}}\rvert$$

When $\lvert\mathcal V_{\text{obs}}\rvert \lt \lvert E\rvert$ (fewer observable nodes than edges), some directions in $\boldsymbol\theta$-space are fundamentally unresolvable from the available data. Any attribution in the unidentifiable directions relies on prior beliefs, not evidence.

**3. The posterior correlation barrier.** Even for approximately identifiable cases, any factored representation (independent Beta posteriors per edge) necessarily discards the correlation introduced by failure at multi-parent nodes. The exact posterior complexity grows exponentially with the number of observed failures. The factored representation is an approximation by construction — coupled corrections are inherent to the problem, not an artifact of a bad algorithm.

### The Design Requirement

*[Discussion (credit-assignment-design-requirement)]*

The theory does not prescribe a specific credit-assignment scheme. It states what any scheme must satisfy for the persistence guarantees to hold:

**Minimal requirement (from #der-gain-sector-bridge):** The per-edge signal function must have **directional fidelity** — the expected update for each edge must point toward the true credence:

$$\mathbb{E}[(\text{signal}(o_t, i, j) - p_{ij}) \cdot (p_{ij} - \theta_{ij})] \leq 0$$

(the expected correction is non-positively correlated with the current error). This is the per-component version of condition B1 from the bridge theorem. Any signal function satisfying this produces sector-satisfying corrections that transfer losslessly to value space (Prop B.5b, componentwise case).

**Sufficient condition for persistence:** Per-component directional fidelity + bounded gain ($\eta_{\text{edge}} \gt 0$). The theory guarantees persistence when these hold, regardless of how the signals are computed.

**What's NOT required:** Exact attribution, unbiased estimation, minimum-variance estimation, or optimality of any kind. The persistence guarantee is robust to approximation — a sloppy but directionally correct signal function still produces bounded strategic mismatch. The *quality* of the approximation affects the *tightness* of the persistence bound (how close $R^\ast_\Sigma$ is to zero), not whether persistence holds at all.

### The Hierarchy of Credit Assignment Quality

| Level | Requirement | What it buys | Cost |
|---|---|---|---|
| **0** (none) | Plan-level tracking only | Persistence guarantee (Prop B.5) | No per-edge diagnostics |
| **1** (directional) | Directional fidelity per edge | Persistence + rough per-edge diagnostics | Gradient computation $O(\lvert V\rvert + \lvert E\rvert)$ |
| **2** (approximate) | Proportional blame / expectation propagation | Persistence + per-edge diagnostics (with bias) | Factor-graph inference |
| **3** (exact) | Full Bayesian posterior | Persistence + optimal per-edge calibration | \#P-hard (general case) |

AAT's formal guarantees require only Level 0. Practical agents need at least Level 1 for adaptive behavior — and the default signal function (above) provides a concrete Level 1 scheme. Level 2 is the sweet spot for most applications. Useful Level 2 factor-graph approximations include: exact Belief Propagation (BP) on tree or polytree cases, loopy BP or max-sum for MAP-style diagnosis, Expectation Propagation (EP) for approximate marginals, and structured variational methods only where common-cause structure is explicitly modeled. Level 3 is a mathematical ideal that is computationally unattainable in the general case.

---



## Formulation: Structural Change as Parametric Limit

- **Slug**: `form-structural-change-as-parametric-limit`
- **Type**: formulation
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `def-strategy-dag`, `result-structural-adaptation-necessity`

In the probabilistic DAG, "structural" changes to $\Sigma_t$ are continuous operations on edge weights and node sets — not a separate mechanism. Pruning is a credence dropping below threshold; **strategic grafting** is a new causal hypothesis initialized at a prior. This dissolves the sharp line between parametric update (adjusting weights) and structural change (adding/removing edges). *(The unqualified term "grafting" — familiar from horticulture, graph rewriting, and decision-tree learning — is sanctioned in-segment shorthand for "strategic grafting" once the canonical compound has been introduced.)*

*[Formulation (structural-change-as-parametric-limit)]*

The six operations on $\Sigma_t$, ordered from most to least frequent:

| Operation | What changes | Trigger |
|-----------|-------------|---------|
| Reweighting | Edge credence $p_{ij}$ | New observation about the link ( #hyp-edge-update-via-gain) |
| $\gamma$ reclassification | Node combination type AND↔OR | Strong structural evidence that combination semantics changed |
| Pruning | Remove failed branch ($p_{ij} \to \approx 0$) | Credence drops below viability threshold |
| Strategic grafting | Add new branch ($0 \to p_{ij}$) | Discovery of a new possible path (initialized at prior) |
| Objective revision | Change terminal nodes | Feasibility failure or opportunity ( #def-satisfaction-gap) |
| Full restructure | Replace entire $\Sigma_t$ | Catastrophic failure ( #result-structural-adaptation-necessity) |

A healthy agent does continuous strategic maintenance (reweight, occasionally prune and graft) and rarely reaches catastrophic restructuring. Full restructure is the strategic analog of #result-structural-adaptation-necessity's model-class change — the rare, expensive event when the entire representational structure must be replaced.

---



## Definition: Strategic Tempo

- **Slug**: `def-strategic-tempo`
- **Type**: definition
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-adaptive-tempo`, `hyp-edge-update-via-gain`, `def-strategy-dag`, `scope-edge-update-causal-validity`, `deriv-edge-credence-dynamics`

The effective rate at which an agent acquires useful revisions to its strategy $\Sigma_t$ --- the sum of per-edge correction capacities across the strategy DAG, weighted by each edge's causal identifiability.

*[Definition (strategic-tempo)]*

$$\mathcal T_\Sigma = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij} \cdot \iota_{ij}$$

where:
- $(i,j)$ indexes the edges of the strategy DAG ( #def-strategy-dag)
- $\nu_{ij}$ is the effective observation rate for edge $(i,j)$ --- how often the agent obtains evidence about the causal link $i \to j$
- $\eta_{\text{edge},ij}$ is the per-edge update gain ( #hyp-edge-update-via-gain)
- $\iota_{ij} \in [0, 1]$ is the identifiability coefficient ( #scope-edge-update-causal-validity): the fraction of the evidence stream that genuinely identifies the edge's causal effect

**Regime contributions.** The identifiability coefficient captures the regime distinction from #scope-edge-update-causal-validity:

| Regime | $\iota_{ij}$ | Contribution to $\mathcal T_\Sigma$ | Example domain |
|---|---|---|---|
| **A** Intervention-rich | $\approx 1$ | Full: $\nu_{ij} \cdot \eta_{\text{edge},ij}$ | Software tests, laboratory experiments |
| **B** Partial intervention | $\in (0, 1)$ | Reduced proportionally | Organizational actions with concurrent effects |
| **C** Observation-only | $\approx 0$ | Near-zero: edges contribute negligibly | Passive monitoring, intelligence analysis |

**An agent cannot improve the parts of its strategy that it cannot test interventionally.** This is the operational content of the $\iota$ factor: Regime-C edges contribute essentially nothing to $\mathcal T_\Sigma$ regardless of how fast the agent acts or how many observations it makes. Regime-A edges yield full strategic tempo at their observation rate. The $\iota$ factor is where edge-causal-validity ( #scope-edge-update-causal-validity) enters the operational machinery of strategy revision.

**Parallel with epistemic tempo.** The definition mirrors #def-adaptive-tempo's $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$, replacing observation channels with strategy edges and adding the $\iota$ modulation for causal identifiability. The structural parallel is exact for Regime-A edges (where $\iota = 1$ recovers the direct rate-times-gain form); in mixed regimes, $\iota$ carries the additional content distinguishing interventional evidence from associational proxy.

**Key difference: endogenous edge rates.** Epistemic tempo's channel rates $\nu^{(k)}$ are largely exogenous --- the environment generates observations at its own pace. Strategic tempo's edge rates $\nu_{ij}$ are *endogenous*: they depend on the agent's action policy (which edges get tested) and on upstream success (downstream edges are tested only when upstream edges fire). This endogeneity is the source of the structural differences between epistemic and strategic persistence.

### Consistency verification

The definition is consistent with the four verified topologies from #deriv-edge-credence-dynamics:

**Case B.1 (single edge $A \to G$).** One edge, $\nu = \nu_{AG}$, $\eta_{\text{edge}} = 1/(n+1)$. $\mathcal T_\Sigma = \nu_{AG}/(n+1)$. The sector parameter $\alpha_\Sigma = 1/(n+1)$ is the per-observation correction quality; $\mathcal T_\Sigma = \nu \cdot \alpha_\Sigma$, matching the epistemic tempo pattern exactly.

**Case B.2 (two-edge AND chain, $A \to B \to G$, $B$ observable).** Two edges. Edge 1 is tested at rate $\nu_1 = \nu$ (every execution). Edge 2 is tested only when edge 1 succeeds: $\nu_2 = \nu \cdot \theta_1$. The bottleneck edge has $\alpha_\Sigma = \min(1/(n_1+1),\; \theta_1/(n_2+1))$. $\mathcal T_\Sigma = \nu/(n_1+1) + \nu\theta_1/(n_2+1)$, consistent with depth-gated attenuation.

**Case B.3 (two-edge AND chain, $B$ unobservable).** Per-edge tempo is ill-defined (the marginal point estimate is biased). Plan-level tempo is well-defined: $\mathcal T_{\Sigma,\text{plan}} = \nu/(n_\Phi + 1)$, treating $\hat\Phi = p_1 p_2$ as a single tracked quantity.

**Case B.4 (two-arm OR node, $\varepsilon$-greedy).** Edge 1 tested at rate $\nu_1 = \nu(1-\varepsilon)$, edge 2 at rate $\nu_2 = \nu\varepsilon$. $\mathcal T_\Sigma = \nu(1-\varepsilon)/(n_1+1) + \nu\varepsilon/(n_2+1)$. Action selection directly controls the rate allocation --- exploration-gated, not depth-gated.

### Structural decomposition

**AND-chains: depth-gated (geometric attenuation).** In a chain of depth $d$ with edge success probabilities $\theta_k$, the effective observation rate for edge $k$ is:

*[Derived (Conditional on independent edges)]*

$$\nu_k = \nu \cdot \prod_{j \lt k} \theta_j$$

Each additional depth level attenuates by a factor $\theta_k \lt 1$. For a uniform chain ($\theta_k = \theta$, $n_k = n$ for all $k$):

$$\mathcal{T}_\Sigma = \frac{\nu}{n+1} \sum_{k=1}^{d} \theta^{k-1} = \frac{\nu}{n+1} \cdot \frac{1 - \theta^d}{1 - \theta}$$

This converges to $\nu / ((n+1)(1-\theta))$ as $d \to \infty$ --- total strategic tempo is bounded even for arbitrarily deep chains. The marginal tempo contribution of edge $k$ decays as $\theta^{k-1}$, falling below any fixed threshold at depth $d^\ast$ ( #form-strategy-complexity-cost). Deep AND-chains have low $\mathcal T_\Sigma$ at their leaves regardless of how fast the agent acts --- the evidence-starvation effect identified in #deriv-edge-credence-dynamics.

**OR-nodes: exploration-gated.** At an OR-node with $m$ alternatives under $\varepsilon$-exploration, the rate allocated to alternative $l$ is:

*[Definition (OR-node rate allocation)]*

$$\nu_l = \begin{cases} \nu(1 - \varepsilon + \varepsilon/m) & l = l^\ast \text{ (greedy arm)} \\ \nu \cdot \varepsilon/m & l \neq l^\ast \text{ (exploratory arms)} \end{cases}$$

The bottleneck is the least-explored alternative. Pure greedy ($\varepsilon = 0$) gives $\nu_l = 0$ for non-greedy arms, making those edges permanently uncorrectable.

### Per-edge persistence

*[Derived (from persistence-condition applied per edge)]*

For $\Sigma_t$ to persist, every edge must maintain bounded mismatch. The bottleneck condition is:

$$\forall (i,j) \in E: \quad \nu_{ij} \cdot \iota_{ij} \cdot \eta_{\text{edge},ij} \gt \frac{\rho_{\Sigma,ij}}{R_{\Sigma,ij}}$$

This is the per-edge analog of #result-per-dimension-persistence's per-dimension condition for $M_t$. The aggregate relationship between $\mathcal T_\Sigma$ and the average correction rate $\alpha_\Sigma$ is:

$$\alpha_\Sigma \leq \frac{\mathcal T_\Sigma}{\lvert E\rvert} \leq \mathcal T_\Sigma$$

(minimum $\leq$ average $\leq$ sum). Consequently, $\mathcal T_\Sigma \gt \lvert E\rvert \cdot \rho_\Sigma / R_\Sigma$ is *necessary* for persistence but not sufficient --- the persistence condition is bottleneck-limited by the weakest edge, not governed by the aggregate.

---



## Formulation: Cognitive Cost of Strategy

- **Slug**: `form-strategy-complexity-cost`
- **Type**: formulation
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `def-strategic-tempo`, `form-information-bottleneck`, `norm-explicit-strategy-condition`, `der-chain-confidence-decay`, `deriv-strategy-cost-regret-bound`, `form-structural-change-as-parametric-limit`, `def-value-object`, `form-objective-functional`

The complexity cost of maintaining an explicit strategy $\Sigma_t$, formulated via minimum description length and the information bottleneck principle --- connecting DAG structure to the maintenance term $C_{\text{maintain}}$ in the explicit strategy condition ( #norm-explicit-strategy-condition).

### Strategy description length

*[Formulation (strategy-description-length)]*

The minimum description length of a strategy DAG $\Sigma_t = (V, E, p, \gamma)$ ( #def-strategy-dag) decomposes as:

$$\operatorname{DL}(\Sigma_t) = \operatorname{DL}_{\text{struct}}(G) + \operatorname{DL}_{\text{param}}(p \mid G)$$

where:
- $\operatorname{DL}_{\text{struct}}(G)$: bits to encode the DAG topology --- node identities, edge connectivity, AND/OR labels $\gamma$. Scales as $O(\lvert E\rvert \log \lvert V\rvert)$ for sparse DAGs.
- $\operatorname{DL}_{\text{param}}(p \mid G)$: bits to encode the edge credences given the topology. For Beta-distributed credences, each edge requires $O(\log n_{ij})$ bits where $n_{ij} = \alpha_{ij} + \beta_{ij}$ is the effective sample size.

The total scales as $O(\lvert E\rvert \log \lvert V\rvert)$ for moderate-precision credences, growing linearly in the number of edges and logarithmically in the number of nodes.

### Strategy IB objective

*[Formulation (strategy-IB-objective; KL-direction strengthened by regret bound — see Epistemic Status)]*

The optimal strategy complexity balances parsimony against decision-relevance. $\Sigma_t$ is the IB-compression of the interaction history $\mathcal C_t$ *for guidance*, parallel to $M_t$ as the IB-compression of $\mathcal C_t$ *for prediction* ( #disc-compression-operations for the shared IB shape across AAT's compression operations, and for the relationship between the theoretical $I(\mathcal C_t; \Sigma_t)$ compression cost and the operational DL-based minimization below):

**Theoretical form (variational).** $\Sigma_t$ is a tractable variational approximation of the optimal-policy posterior $Q^\ast(\pi \mid M_t)$. The strategy-cost objective:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}\bigl(\pi^\ast(\cdot \mid M_t) \,\big\Vert\, Q_{\Sigma_t}(\pi \mid M_t)\bigr)\right]$$

where $Q_{\Sigma_t}(\pi \mid M_t)$ is the action distribution induced by the strategy DAG given the current model state, and $\pi^\ast(\cdot \mid M_t)$ is the optimal-policy reference. The KL direction — $\pi^\ast$-first — is forced by the regret-bound derivation (next paragraph); the opposite direction is vacuous under deterministic $\pi^\ast$.

**Regret-bound derivation of KL direction.** Under AAT's canonical scope, $\pi^\ast = \delta_{a^\ast}$ is deterministic ( #def-value-object). Define the strategy-induced regret against $\pi^\ast$ as $R(Q_{\Sigma_t}) := V(a^\ast) - \mathbb{E}_{a \sim Q_{\Sigma_t}}[V(a)]$, where $V(a) = Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ is the action-value ( #def-value-object, $O_t$ induces $V$ via #form-objective-functional). Under bounded value range $V_{\max} := \max_a V(a) - \min_a V(a)$:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max}\cdot(1 - Q_{\Sigma_t}(a^\ast)) \;=\; V_{\max}\cdot\operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$$

Applying Pinsker's inequality ($\operatorname{TV}(P,Q) \leq \sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(P\Vert Q)}$) with $P = \pi^\ast$, $Q = Q_{\Sigma_t}$:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max}\cdot\sqrt{\tfrac{1}{2}\, D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$$

Under deterministic $\pi^\ast$, $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast)$ — finite and graded whenever $Q_{\Sigma_t}(a^\ast) \gt 0$. The opposite-direction $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ equals $+\infty$ whenever $Q_{\Sigma_t}$ places any mass off $a^\ast$, giving a vacuous bound. The regret-bound argument therefore **forces the KL direction** with $\pi^\ast$ first. Within the direction-forced f-divergence family, reverse-KL is *uniquely* selected under the chain-rule additivity axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975), which is AAT-internally motivated as the divergence-level analog of additive log-confidence decay ( #der-chain-confidence-decay). See #deriv-strategy-cost-regret-bound §6.1 for the uniqueness theorem, §6.2 for secondary supporting characterizations (gradient-tractability, VI-alignment, MDL), and §7 for the linear-vs-square-root $\beta_\Sigma$ trade-off.

The variational form is the strategy-layer analog of variational free energy minimization in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99; Parr & Pezzulo 2022, *Active Inference*, MIT Press). AAT borrows the variational form as the appropriate generalization of the Shannon-MI relevance term and now derives the direction of KL from an internal regret-bound argument — without committing to AI's preferences-as-priors encoding ($C(o) = \log P_{\mathrm{pref}}(o)$; AAT's $O_t$ remains a value functional on trajectories, #form-objective-functional) or to expected free energy as master objective (AAT's CIY-unified objective is a related but distinct decomposition; #disc-ciy-unified-objective).

**Operational form.** Since $I(\mathcal C_t; \Sigma_t)$ is not computable in closed form for general DAG encodings, the operational minimization replaces the information cost with a description-length surrogate and the KL term with a sample-based estimate (a per-edge calibration discrepancy weighted by decision-relevance — see #disc-credit-assignment-boundary for the gradient form):

$$\Sigma_t^\ast \approx \arg\min_{\Sigma_t} \left[\operatorname{DL}(\Sigma_t) + \beta_\Sigma \cdot \widehat{D_{\mathrm{KL}}}(\pi^\ast \,\Vert\, Q_{\Sigma_t})\right]$$

where:
- $\operatorname{DL}(\Sigma_t)$: description length (coding-cost upper bound on $I(\mathcal C_t; \Sigma_t)$ for the given DAG encoding scheme — see §2.2 below)
- $\widehat{D_{\mathrm{KL}}}(\pi^\ast \,\Vert\, Q_{\Sigma_t})$: sample-based estimate of the KL divergence from the optimal-policy reference to the strategy-induced policy
- $\beta_\Sigma \gt 0$: trade-off parameter — cognitive cost per decision-relevant bit (the $\Sigma_t$ instance of the shared $\beta$ framework in #disc-compression-operations); under the regret-bound derivation, $\beta_\Sigma$ has a *local* interpretation as $V_{\max}/(2\sqrt{2 D_{\mathrm{KL}}})$ via the Pinsker form (the linear-KL form is the IB-shape instance; the square-root form is the tighter regret-scale form — see Epistemic Status and the spike for the trade-off)

The two forms agree in the limit where the DAG encoding is rate-distortion optimal and the policy posterior is sample-recoverable; the operational form is the one an agent actually runs. The theoretical form places the objective on the same variational frontier as $M_t$, shared intent, and composition projection, with the $\pi^\ast$-first KL-form relevance term resolving the Shannon-zero degeneracy under deterministic $\pi^\ast$ *and* the forward-KL infinity degeneracy that the opposite direction would introduce.

When $\beta_\Sigma$ is low (high maintenance cost relative to decision value), the agent prefers simple strategies. When $\beta_\Sigma$ is high (strategy is cheap to maintain relative to its decision value), the agent can afford complex plans. The explicit strategy condition ( #norm-explicit-strategy-condition) is the binary threshold: $\beta_\Sigma$ large enough that *any* $\Sigma_t$ is worth maintaining.

### Maximum useful chain depth

*[Derived (Conditional on Beta-Bernoulli, per-edge persistence)]*

From #def-strategic-tempo's per-edge persistence condition, an AND-chain of depth $d$ with per-edge observation rate $\nu$, true success probability $\theta$ per edge, and effective sample size $n$ per edge persists only if the deepest edge satisfies:

$$\nu \cdot \theta^{d-1} \cdot \frac{1}{n+1} \gt \frac{\rho_\Sigma}{R_\Sigma}$$

Solving for the maximum depth at which persistence is achievable:

$$d^\ast = 1 + \left\lfloor \frac{\log\bigl(\frac{\nu}{(n+1)\rho_\Sigma / R_\Sigma}\bigr)}{\log(1/\theta)} \right\rfloor$$

When $\nu / ((n+1)\rho_\Sigma / R_\Sigma) \leq 1$, even $d = 1$ fails --- the agent cannot maintain a single edge under these conditions.

**Interpretation.** Beyond depth $d^\ast$, evidence starvation makes edges uncorrectable faster than the environment invalidates them. The agent accumulates strategic mismatch on deep edges regardless of how fast it acts at the top of the chain.

**Quantitative illustration** ($\theta = 0.8$, $\nu = 1$):

| $n$ | $\rho_\Sigma / R_\Sigma$ | $d^\ast$ |
|-----|--------------------------|----------|
| 10 | 0.01 | 10 |
| 10 | 0.1 | 0 |
| 100 | 0.01 | 5 |
| 100 | 0.1 | 0 |

High evidence requirements ($n$ large) and volatile environments ($\rho_\Sigma / R_\Sigma$ large) severely limit useful chain depth.

### Triple depth penalty

Deep AND-chains suffer three independent penalties that compound:

1. **Confidence decay** ( #der-chain-confidence-decay): aggregate confidence $\prod p_k$ decays geometrically with depth. The plan is *less likely to succeed*.
2. **Evidence starvation** ( #deriv-edge-credence-dynamics): effective observation rate $\nu_k = \nu \cdot \prod_{j \lt k}\theta_j$ decays geometrically. The plan is *harder to calibrate*.
3. **Cognitive cost** (this segment): each additional depth level adds $O(\log \lvert V\rvert)$ bits to description length. The plan is *more expensive to maintain*.

All three are multiplicative in depth, making deep sequential strategies exponentially costly along three independent dimensions.

### Enriched explicit strategy condition

*[Formulation (enriched-strategy-condition)]*

The maintenance cost $C_{\text{maintain}}$ from #norm-explicit-strategy-condition decomposes as:

$$C_{\text{maintain}} = C_{\text{represent}} + C_{\text{revise}} + C_{\text{monitor}}$$

where:
- $C_{\text{represent}} \propto \operatorname{DL}(\Sigma_t)$: cognitive cost of holding the strategy in working memory (proportional to description length)
- $C_{\text{revise}} \propto \sum_{(i,j)} \nu_{ij} \cdot c_{\text{update}}$: cost of processing edge updates (proportional to strategic tempo $\mathcal T_\Sigma$ times per-update cost)
- $C_{\text{monitor}} \propto \lvert\{(i,j) : \iota_{ij} \lt 1\}\rvert$: cost of monitoring edges with partial identifiability (the agent must do extra causal reasoning for non-trivial edges)

This decomposition makes the #norm-explicit-strategy-condition's maintenance term concrete: each component maps to a quantity defined elsewhere in the theory.

### Complexity compression operations

*[Discussion (complexity-compression)]*

The IB objective suggests three compression operations, corresponding to structural changes from #form-structural-change-as-parametric-limit:

1. **Edge pruning** (operation 3 in #form-structural-change-as-parametric-limit): remove edges with $\eta_{\text{edge},ij} \cdot I_{\text{edge},ij} \lt c_{\text{bit}}$, where $I_{\text{edge},ij}$ is the decision-relevance of that edge and $c_{\text{bit}}$ is the per-bit maintenance cost. Edges that contribute less decision value than their representational cost are candidates for removal.
2. **Node merging** (reducing $\lvert V\rvert$): collapse intermediate nodes that serve no decision-distinguishing function. This reduces $\operatorname{DL}_{\text{struct}}$ by a factor proportional to the reduction in $\lvert V\rvert$.
3. **Depth truncation** at $d^\ast$: prune all edges beyond the maximum useful depth. This is not optimization but necessity --- edges beyond $d^\ast$ cannot maintain bounded mismatch.

---



## Proposed-schema: Strategy Persistence Schema

- **Slug**: `schema-strategy-persistence`
- **Type**: proposed-schema
- **Status**: conditional
- **Stage**: draft
- **Depends**: `result-sector-condition-stability`, `result-sector-persistence-template`, `def-strategic-calibration`, `def-strategy-dag`

The sector-persistence template ( #result-sector-persistence-template) proves bounded state for any system with a state variable, a correction function satisfying the sector condition, and bounded disturbance. The template is domain-agnostic — it applies to any state variable meeting its preconditions (T1)–(T3). This schema is the strategic-layer instantiation: if strategic update dynamics satisfy the template's preconditions, strategy persistence follows as a direct instance. A key additional requirement — absent from the epistemic instantiation but load-bearing here — is **experience discounting**, because the strategic sector parameter $\alpha_\Sigma$ decays monotonically with experience and requires an explicit forgetting mechanism to remain bounded below.

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

The effective sample size stabilizes at $n_{\text{eff}} = 1/(1-\lambda)$, and substituting into Prop B.1's $\alpha_\Sigma = 1/(n+1)$ gives the exact steady-state sector parameter:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}} + 1} = \frac{1-\lambda}{2-\lambda}$$

For slow forgetting ($\lambda \to 1$, the regime where the prerequisite is most likely to bind), the leading-order expansion gives the simpler form $\alpha_\Sigma^{\text{ss}} \approx 1-\lambda$ — which agrees with the forgetting rate itself. Outside the high-$\lambda$ regime the approximation deteriorates: at $\lambda = 0.5$, the exact form gives $\alpha_\Sigma^{\text{ss}} = 1/3$ while the linear approximation gives $1/2$ (≈ 50% overestimate); at $\lambda = 0.9$, exact $\alpha_\Sigma^{\text{ss}} = 1/11$ versus approximation $1/10$ (≈ 10% overestimate).

**The forgetting prerequisite.** Combining with the schema's persistence form $\alpha_\Sigma > \rho_\Sigma/R_\Sigma$:

$$\frac{1-\lambda}{2-\lambda} \;\gt\; \frac{\rho_\Sigma}{R_\Sigma} \quad\Longleftrightarrow\quad \lambda \;\lt\; \frac{R_\Sigma - 2\rho_\Sigma}{R_\Sigma - \rho_\Sigma}$$

(valid when $\rho_\Sigma \lt R_\Sigma/2$; for $\rho_\Sigma \ge R_\Sigma/2$ no $\lambda$ satisfies the prerequisite and the schema's trajectory guarantee fails for any forgetting rate). The hard ceiling at $\rho_\Sigma = R_\Sigma/2$ and the algebraic content of the steady-state form are derived self-contained in #deriv-strategic-persistence-hard-ceiling — a $\lambda$-independent structural cap on the schema's reachable persistence region under any exponential-forgetting design.

This is a **prerequisite of the schema's trajectory guarantee, not a tunable heuristic**. An agent without forgetting has no long-run strategic persistence regardless of its initial $\alpha_\Sigma$. The steady-state sector parameter must exceed the disturbance-to-reserve ratio, or the instantaneous persistence check — no matter how comfortably it holds at any given time — eventually fails as experience accumulates.

In the slow-forgetting regime the threshold simplifies to the linear-form analog of #result-persistence-condition:

$$(1 - \lambda) \;\gt\; \frac{\rho_\Sigma}{R_\Sigma} \qquad (\text{slow-forgetting limit, } \lambda \to 1)$$

playing the role that $\mathcal{T} \gt \rho / \lVert\delta_{\text{critical}}\rVert$ plays for the epistemic case. The forgetting rate $(1-\lambda)$ is the strategic analog of adaptive tempo: faster forgetting means faster tracking but noisier estimates; slower forgetting means stable estimates but slower tracking. The optimal $\lambda$ balances bias and variance for the specific $\rho_\Sigma$ the environment presents. Outside the slow-forgetting regime, the exact form $(1-\lambda)/(2-\lambda) \gt \rho_\Sigma/R_\Sigma$ is the operating threshold and the simpler linear form is unsafe (it permits $\lambda$ values that violate the actual prerequisite).

**Which mismatch state?** The schema applies to any mismatch state for which conditions (SA1)-(SA3) can be verified. Two candidates exist:

- **Strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$: the scalar difference between the agent's strategy-plan-confidence score and the independence-model plan value at true edge parameters. This is the mismatch for which persistence IS proved (Props B.1-B.5 in #deriv-edge-credence-dynamics). It is computable from status propagation without credit assignment. **Scope:** $\delta_s$ operates at L0 of the Correlation Hierarchy ( #def-strategy-dag) — it tracks calibration within the independence model. For L1 (augmented DAG), the same persistence result applies to the augmented graph's $\hat P_\Sigma$. The gap between L0's $\Phi$ and actual plan success under correlated failure is a model-class limitation, not an estimation error.
- **Strategic-calibration residual** $\delta_{\text{strategic}}$: the per-edge value-increment residual aggregation defined in #def-strategic-calibration. This is the mismatch the orient cascade ( #der-orient-cascade) uses for edge-level revision. Persistence of $\delta_{\text{strategic}}$ remains **open** and requires the credit-assignment machinery in #disc-credit-assignment-boundary.

The verified instances below all use per-edge credence error $\boldsymbol\delta_c = (\hat p_k - \theta_k)$ or the plan-level surrogate $\delta_s$. They do not verify the schema for $\delta_{\text{strategic}}$ directly.

---



## Formulation: Consolidation Dynamics

- **Slug**: `form-consolidation-dynamics`
- **Type**: formulation
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `der-recursive-update`, `deriv-recursive-update`, `form-event-driven-dynamics`, `der-temporal-nesting`, `form-information-bottleneck`, `disc-compression-operations`, `result-structural-adaptation-necessity`, `schema-strategy-persistence`, `form-structural-change-as-parametric-limit`

Consolidation is a regime of the between-event dynamics $g_M$ of #der-recursive-update in which the agent applies Markov updates driven by replayed or internally-generated pseudo-events, with objective of reducing the rate-distortion gap to the IB-optimal compression $\phi^\ast(\mathcal C_t)$. It is not a new adaptive primitive — the recursive-update form $f(M_{\tau^-}, e_\tau)$ is preserved — but it is a distinct operating regime with its own scope condition, its own objective, and its own failure modes, each of which the theory currently names only implicitly or in a parenthetical. Naming the regime makes the stability-plasticity window visible as an AAT-expressible failure boundary and supplies the architectural primitive that logogenic agents (`03-llm-core/`) require under context-turnover.

### Regime definition

*[Formulation (consolidation-regime, specializes #der-recursive-update)]*

Let the agent's between-event dynamics be $g_M(M_\tau)$ per #deriv-recursive-update (Corollary: Between-events dynamics, $dM/d\tau = g(M_\tau)$). **Consolidation** is the regime of $g_M$ in which the agent applies updates $M_{\tau^+} = f(M_{\tau^-}, e_\tau^{\text{replay}})$ where $e_\tau^{\text{replay}}$ is a pseudo-event synthesized from $M_{\tau^-}$ itself — a sample drawn from the agent's retained trace (replay buffer, hippocampal reinstatement, a remembered episode, an earlier paragraph re-read). The recursive-update form is preserved; what distinguishes consolidation is the *objective* these updates optimize:

$$\text{consolidation objective: } \min_{M_\tau} \mathcal J_{\text{IB}}(M_\tau) \;:=\; I(M_\tau; \mathcal C_t) - \beta I(M_\tau; o_{t+1:\infty} \mid a_{t:\infty})$$

— the #form-information-bottleneck Lagrangian evaluated against the agent's accumulated chronica $\mathcal C_t$. By contrast, online update's objective (per #emp-update-gain) is one-step predictive mismatch minimization at the current event; it has no representation of $\mathcal J_{\text{IB}}$.

Under C3 (state completeness, per #deriv-recursive-update), $\mathcal I(e_\tau^{\text{replay}} \mid M_{\tau^-}) = 0$: the pseudo-event carries no new external information. Yet the update still does work — it *redistributes* existing information across the factorization structure of $M_\tau$. The distinguishing content is not the information brought in (zero, by construction) but the rate-distortion gap closed (nonzero, when the agent has not yet reached $\phi^\ast$).

### Scope condition — timescale separation

*[Scope (timescale-separation)]*

Let $\nu_{\text{online}}$ be the rate of external events ( #form-event-driven-dynamics) and $\nu_{\text{consol}}$ the rate of consolidation updates. The consolidation regime is well-defined only when

$$\nu_{\text{consol}} \ll \nu_{\text{online}}$$

— the convergence constraint of #der-temporal-nesting applied to an additional intermediate timescale between parametric update (fast) and structural adaptation (slow). Violating this constraint makes consolidation act on online transients rather than settled state, producing the same oscillation failures #der-temporal-nesting warns about.

### Necessity condition

*[Derived (consolidation-necessity, conditional)]*

Consolidation is necessary — online-only cannot reach the IB optimum — when *both* of the following hold:

**(N1) Sub-state factorization.** $M_t$ factors into sub-states $M_t^{\text{fast}}$ and $M_t^{\text{slow}}$ with divergent compression-prediction trade-offs. $M_t^{\text{fast}}$ favors high-capacity sparse representation; $M_t^{\text{slow}}$ favors distributed compressed representation. The two sub-states capture cross-episode regularities versus verbatim traces respectively — the Complementary Learning Systems factorization (McClelland, McNaughton & O'Reilly 1995; Kumaran, Hassabis & McClelland 2016).

**(N2) Bounded per-event budget.** The per-event processing budget $B_{\text{online}}$ is strictly less than the integration cost $B_{\text{consol-needed}}$ for updating $M_t^{\text{slow}}$ against cross-episode regularities. Online updates can move at most $B_{\text{online}}$ bits of model-state change per event; updating $M_t^{\text{slow}}$ to represent a cross-episode pattern requires comparison against a distribution of prior episodes, which exceeds $B_{\text{online}}$.

When (N1) *or* (N2) fails, consolidation is a *luxury*: online update with sufficient per-event budget or without sub-state factorization can reach $\phi^\ast$ in the limit. Kalman filters with persistent covariance, conjugate-Bayesian agents with full posterior, and linear-Gaussian systems with online Riccati updates all satisfy neither (N1) nor (N2) and have no consolidation need. When (N1) *and* (N2) both hold, consolidation is a *necessity*: no online-only policy reaches $\phi^\ast$ under the joint constraint.

### Stability-plasticity feasibility window

*[Derived (stability-plasticity-window, conditional)]*

#schema-strategy-persistence derives the *plasticity lower bound* on forgetting rate $\lambda$:

$$(1 - \lambda) \;\gt\; \rho_\Sigma / R_\Sigma \qquad \text{(plasticity lower bound, from \#schema-strategy-persistence)}$$

— forgetting fast enough to track non-stationarity. This segment's complement is a *stability upper bound*:

$$(1 - \lambda) \;\lt\; \phi(\nu_{\text{consol}}, \text{consolidation-budget}) \qquad \text{(stability upper bound, see Working Notes for derivation sketch)}$$

— forgetting slow enough to let consolidation integrate cross-episode patterns before they are discarded. Between these bounds is the **feasibility window** for $\lambda$. Empty window — rapid non-stationarity with slow consolidation cadence — is the catastrophic-forgetting regime (French 1999; Kirkpatrick et al. 2017): no $\lambda$ satisfies both constraints and the agent's long-run IB objective is strictly worse than a slower-environment or faster-consolidation counterpart.

The upper bound's exact form depends on the consolidation mechanism and is not derived here — it is a candidate derivation flagged in Working Notes. What is derived: the window's *existence* as a structural object (plasticity must satisfy both bounds) and the catastrophic-forgetting regime as its empty-window limit.

### Structural-adaptation enablement

*[Derived (structural-adaptation-requires-consolidation, conditional)]*

Under (N1)+(N2), structural adaptation (per #result-structural-adaptation-necessity) cannot be executed online. Parametric update has a hard timescale constraint — mismatch decays at rate $\mathcal T$; delayed updates accumulate mismatch at rate $\rho$. Structural adaptation tolerates much larger delay because the slow process operates on what $R_\Sigma$ or $R$ are *measuring tolerance against* — the model class itself. Consolidation provides the operating regime where structural operations (decomposition-and-recombination, expansion, compression, grafting per #form-structural-change-as-parametric-limit) become executable: the per-event budget is irrelevant when updates are offline, and interleaved replay supports stability-preserving structural change.

Pure online structural adaptation is the luxury case where per-event budget equals or exceeds integration cost for structural-class operations — this is where Bayesian nonparametric agents with unlimited compute sit. All finite-budget agents require consolidation for quality-preserving structural change.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Consolidation as regime of $g_M$ with replayed/pseudo-event driver | Specialization of #der-recursive-update's Discussion (consolidation listed as an example) | Formulation choice (the "regime" framing; could alternatively be presented as a distinct adaptive primitive with its own update form) |
| IB-gap reduction as consolidation's objective | Identification with #form-information-bottleneck's Lagrangian against $\mathcal C_t$ | Derived (given IB acceptance; the alternative — online-update-only optimization — leaves the gap un-reducible under (N1)+(N2)) |
| Scope condition $\nu_{\text{consol}} \ll \nu_{\text{online}}$ | Direct application of #der-temporal-nesting convergence constraint | Derived |
| Necessity condition (N1)+(N2) | Structural argument: under (N1), cross-episode information cannot enter one event; under (N2), online budget insufficient for cross-episode integration | Derived (qualitatively; the quantitative version requires specifying $B_{\text{online}}$ and $B_{\text{consol-needed}}$ per architecture) |
| Stability-plasticity window existence | #schema-strategy-persistence's lower bound + this segment's upper bound (form open) | Derived (existence); upper-bound functional form open |
| Catastrophic-forgetting regime = empty window | Direct from both-bounds-unsatisfiable | Derived |
| Structural adaptation requires consolidation under (N1)+(N2) | #result-structural-adaptation-necessity's per-step timescale + consolidation's offline budget | Derived (qualitatively) |
| CLS factorization (hippocampal fast / neocortical slow) as canonical (N1) instance | McClelland-McNaughton-O'Reilly 1995; Kumaran-Hassabis-McClelland 2016 | External theorem (CLS literature) |
| Quantitative online-only no-go under (N1)+(N2) | Rate-distortion argument sketched but not rigorously derived here | Sketch (candidate #disc-identifiability-floor Instance 3) |

---
