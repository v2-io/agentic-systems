# Strategic Tempo and Cognitive Cost of Strategy

**Status**: Spike. Addresses two --GAP-- entries in `01-aad-core/OUTLINE.md` Section II: (1) "Rate of useful $\Sigma_t$ revision (adaptive tempo for strategy)" and (2) "Complexity cost of maintaining $\Sigma_t$ (IB/MDL for DAGs)."

**Date**: 2026-04-02

**Discipline**: Every step is labeled. Part 1 (strategic tempo) is largely derivable from existing machinery — the four verified cases in #strategic-dynamics-derivation already contain the essential structure. Part 2 (cognitive cost) is more speculative — the IB/MDL extension to strategy DAGs requires new formalization choices.

**Dependencies**: #adaptive-tempo, #strategy-persistence-schema, #strategic-dynamics-derivation, #edge-update-via-gain, #edge-update-causal-validity, #chain-confidence-decay, #information-bottleneck, #deliberation-cost, #explicit-strategy-condition, #credit-assignment-boundary.

---

## Part 1: Strategic Tempo ($\mathcal{T}_\Sigma$)

### 1.1 Definition

Epistemic tempo ( #adaptive-tempo) is:

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$$

the rate of useful information acquisition across observation channels. The agent's total corrective capacity for $M_t$ — the product of how fast observations arrive and how much each one corrects the model.

Strategic tempo should be the analogous quantity for $\Sigma_t$: the rate at which the agent's strategy improves through execution evidence.

*[Definition (strategic-tempo)]*

$$\mathcal{T}_\Sigma = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij}$$

where:
- $(i,j)$ ranges over all edges in the strategy DAG $\Sigma_t$
- $\nu_{ij}$ is the effective rate at which edge $(i,j)$ receives execution evidence (trials per unit time)
- $\eta_{\text{edge},ij}$ is the edge update gain ( #edge-update-via-gain): $\eta_{\text{edge},ij} = 1/(n_{ij} + 1)$ for Beta-Bernoulli edges

**The key difference from epistemic tempo.** Epistemic tempo sums over observation *channels* — the agent's sensory interfaces with the environment. Strategic tempo sums over *edges* — the agent's causal beliefs about action-outcome links. The indexing is different because the objects being corrected are different. For $M_t$, the agent corrects a compressed state via observation channels. For $\Sigma_t$, the agent corrects edge credences via execution outcomes.

**Effective edge rate $\nu_{ij}$ is not exogenous.** For epistemic tempo, channel rates $\nu^{(k)}$ are largely exogenous — they depend on the environment's event-generating process and the agent's sensor placement. For strategic tempo, edge rates depend on: (a) the agent's action-selection policy (which edges get tested), (b) upstream success (downstream edges in AND-chains are tested only when all upstream edges succeed), and (c) the environment's event rate. This endogeneity is a fundamental difference — strategic tempo is partly under the agent's control.

### 1.2 Consistency with the Four Verified Cases

The definition must be consistent with the $\alpha_\Sigma$ values derived in #strategic-dynamics-derivation (Props B.1–B.4). In each case, the sector parameter $\alpha_\Sigma$ is a minimum over per-edge correction rates. The strategic tempo, as a sum, is a different quantity — it measures total correction capacity across all edges, while $\alpha_\Sigma$ measures the weakest-link correction rate. But the relationship between them is precise.

**Case B.1: Single edge ($A \to G$).** One edge, tested every trial. $\nu_{AG} = \nu$ (the base action rate). $\eta_{\text{edge}} = 1/(n+1)$.

$$\mathcal{T}_\Sigma = \nu \cdot \frac{1}{n+1}$$

The sector parameter is $\alpha_\Sigma = 1/(n+1)$. The tempo-persistence relationship: the persistence condition $\alpha_\Sigma \gt \rho_\Sigma / R_\Sigma$ becomes $\mathcal{T}_\Sigma / \nu \gt \rho_\Sigma / R_\Sigma$, i.e., $\mathcal{T}_\Sigma \gt \nu \rho_\Sigma / R_\Sigma$. For normalized action rate $\nu = 1$, strategic tempo is exactly the sector parameter.

**Case B.2: Two-edge AND-chain, observable intermediate ($A \to B \to G$).** Edge 1 is tested every trial: $\nu_1 = \nu$. Edge 2 is tested only when edge 1 succeeds: $\nu_2 = \nu \theta_1$.

$$\mathcal{T}_\Sigma = \nu \cdot \frac{1}{n_1+1} + \nu\theta_1 \cdot \frac{1}{n_2+1}$$

*[Derived (strategic tempo, two-edge AND observable)]*

This is the *total* correction capacity. The sector parameter — the weakest link — is:

$$\alpha_\Sigma = \min\!\left(\frac{1}{n_1+1},\; \frac{\theta_1}{n_2+1}\right)$$

The relationship: $\mathcal{T}_\Sigma / \nu = 1/(n_1+1) + \theta_1/(n_2+1) \geq 2\alpha_\Sigma$, with equality when the two per-edge rates are equal. **Strategic tempo is an aggregate; the persistence condition depends on the bottleneck.** This parallels the scalar-vs-vector tempo warning in #adaptive-tempo: scalar tempo overestimates capacity along the weak dimension.

The evidence-starvation effect appears directly in $\nu_2 = \nu\theta_1$ — the downstream edge's effective rate is attenuated by the upstream success probability. This is not an artifact of the sector analysis but a property of the tempo itself.

**Case B.3: Two-edge AND-chain, unobservable intermediate.** Per-edge rates are the same as B.2, but per-edge updates violate SA1 (bias $O(1/n)$ at truth). At the plan level, $\mathcal{T}_{\Sigma,\text{plan}} = \nu / (n_\Phi + 1)$ — only one effective "edge" (the composite).

**Case B.4: Two-arm OR-node, $\varepsilon$-greedy.** Edge 1 (greedy): $\nu_1 = \nu(1-\varepsilon)$. Edge 2 (non-greedy): $\nu_2 = \nu\varepsilon$.

$$\mathcal{T}_\Sigma = \nu(1-\varepsilon) \cdot \frac{1}{n_1+1} + \nu\varepsilon \cdot \frac{1}{n_2+1}$$

*[Derived (strategic tempo, two-arm OR $\varepsilon$-greedy)]*

The sector parameter is $\alpha_\Sigma = \min((1-\varepsilon)/(n_1+1),\; \varepsilon/(n_2+1))$. The tempo-to-sector relationship is the same: total tempo sums per-edge contributions; the persistence bottleneck is the minimum. With optimal exploration ($\varepsilon^\ast = (n_1+1)/(n_1+n_2+2)$), the two terms equalize: $\alpha_\Sigma^\ast = 1/(n_1+n_2+2)$ and $\mathcal{T}_\Sigma^\ast = 2\nu/(n_1+n_2+2)$.

### 1.3 Decomposition by Structure

Epistemic tempo decomposes by observation channels — each channel contributes independently to the total corrective capacity (under the channel independence assumption, see #adaptive-tempo). Strategic tempo decomposes by edges, but the decomposition reveals *structural* patterns:

**AND-chains: depth-gated evidence starvation.**

*[Derived (depth-$d$ chain strategic tempo)]*

For a chain of depth $d$ with all intermediates observable:

$$\mathcal{T}_\Sigma = \nu \sum_{k=1}^{d} \frac{\prod_{j=1}^{k-1}\theta_j}{n_k + 1}$$

Edge $k$'s contribution to tempo is attenuated by $\prod_{j \lt k}\theta_j$ — the probability that all upstream edges succeed and edge $k$ is tested. For a uniform chain ($\theta_j = \theta$, $n_k = n$ for all $k$):

$$\mathcal{T}_\Sigma = \frac{\nu}{n+1} \sum_{k=1}^{d} \theta^{k-1} = \frac{\nu}{n+1} \cdot \frac{1 - \theta^d}{1 - \theta}$$

This converges to $\nu / ((n+1)(1-\theta))$ as $d \to \infty$ — the total strategic tempo is bounded even for arbitrarily deep chains, because downstream edges contribute geometrically less. The *marginal* tempo contribution of adding edge $k$ to the chain is $\nu\theta^{k-1}/(n_k+1)$, which decays exponentially with depth.

**OR-nodes: exploration-gated allocation.**

For a $k$-arm OR-node with $\varepsilon$-uniform exploration:

$$\mathcal{T}_\Sigma = \nu\!\left[\frac{1-\varepsilon}{n_{\text{greedy}}+1} + \frac{\varepsilon}{k-1}\sum_{j \neq \text{greedy}}\frac{1}{n_j+1}\right]$$

Strategic tempo at OR-nodes is an allocation problem: the agent distributes its trial rate $\nu$ among alternatives. Exploration rate $\varepsilon$ controls the distribution. Pure greedy ($\varepsilon = 0$) concentrates all tempo on one arm, yielding zero tempo on the others.

**Mixed AND/OR DAGs: the general decomposition.**

*[Hypothesis (general DAG strategic tempo)]*

For a general AND/OR DAG with edge set $E$ and action policy $\pi$:

$$\mathcal{T}_\Sigma = \sum_{(i,j) \in E} \nu_{ij}(\pi, \boldsymbol{\theta}) \cdot \eta_{\text{edge},ij}$$

where $\nu_{ij}(\pi, \boldsymbol{\theta})$ is the effective trial rate for edge $(i,j)$ under policy $\pi$ and true edge probabilities $\boldsymbol{\theta}$. For AND-chains, $\nu_{ij}$ is attenuated by upstream success probabilities. For OR-children, $\nu_{ij}$ is determined by the action-selection policy. The general computation requires propagating both the trial rate (from root to leaves, or leaves to root depending on DAG orientation) and the selection policy through the DAG.

The hypothesis is that this general form is well-defined and consistent with the four verified cases. Verification for mixed topologies is open — it would be the natural next step in the #strategic-dynamics-derivation program.

### 1.4 Strategic Tempo Under the Three Causal Regimes

From #edge-update-causal-validity, edge updates have different causal validity across three regimes. Strategic tempo inherits this structure through the identifiability-adjusted gain:

$$\eta_{\text{edge},ij}^{\text{adj}} = \eta_{\text{edge},ij} \cdot \iota_{ij}$$

where $\iota_{ij} \in [0,1]$ is the identifiability coefficient.

*[Hypothesis (regime-adjusted strategic tempo)]*

$$\mathcal{T}_\Sigma^{\text{eff}} = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij} \cdot \iota_{ij}$$

| Regime | $\iota_{ij}$ | Effect on $\mathcal{T}_\Sigma$ |
|--------|-------------|-------------------------------|
| **A: Intervention-rich** | $\approx 1$ (leaf edges, clean attribution) | Full strategic tempo. $\mathcal{T}_\Sigma^{\text{eff}} \approx \mathcal{T}_\Sigma$. |
| **B: Partial intervention** | $\in (0,1)$ (concurrent actions, self-selection) | Reduced tempo. Updates carry optimistic bias. |
| **C: Observation-only** | $\approx 0$ (no intervention, confounded) | Near-zero strategic tempo for affected edges. Edges frozen at prior. |

**The regime decomposition is additive.** If some edges are in Regime A and others in Regime C, the total effective strategic tempo is dominated by the Regime A edges — the Regime C edges contribute nothing. This gives a precise meaning to "the agent cannot improve the parts of its strategy that it cannot test interventionally."

**Strategic tempo in software (Regime A).** In software development, the agent runs a specific test ($do(i)$ = run test, observe pass/fail). C1-C3 from #edge-update-causal-validity are all satisfied. Leaf-originating edges have $\iota \approx 1$. Software agents in Regime A have maximal strategic tempo for their action rate and DAG structure. This is one reason why software development can sustain deep, explicit strategies — the full strategic tempo machinery is available.

### 1.5 The Persistence Condition in Terms of $\mathcal{T}_\Sigma$

The persistence condition from #strategy-persistence-schema is $\alpha_\Sigma \gt \rho_\Sigma / R_\Sigma$. The sector parameter $\alpha_\Sigma$ is the weakest-link per-edge correction rate (a minimum), while $\mathcal{T}_\Sigma$ is the total correction rate (a sum). The relationship between the two, for $\lvert E\rvert$ edges:

*[Derived (tempo-persistence relationship)]*

$$\alpha_\Sigma \leq \frac{\mathcal{T}_\Sigma}{\lvert E\rvert} \leq \mathcal{T}_\Sigma$$

The left inequality holds because the minimum is at most the average. The right holds because the average is at most the sum. Therefore $\mathcal{T}_\Sigma \gt \lvert E\rvert \cdot \rho_\Sigma / R_\Sigma$ is a *necessary* condition for persistence (if all edges persist, the total tempo must exceed this threshold), but not sufficient — a high total $\mathcal{T}_\Sigma$ does not guarantee persistence if one edge is starved. When edges have approximately equal correction rates ($\alpha_\Sigma \approx \mathcal{T}_\Sigma / \lvert E\rvert$), the bound is tight and the necessary condition becomes approximately sufficient.

**The persistence condition is bottleneck-limited, not throughput-limited.** A high total $\mathcal{T}_\Sigma$ does not guarantee persistence if one edge is starved. This parallels #per-dimension-persistence's insight about epistemic persistence: the weak dimension is the bottleneck. For strategic persistence, the "weak edge" — the one with lowest $\nu_{ij} \cdot \eta_{\text{edge},ij}$ — determines whether the strategy survives.

The natural formulation of strategic persistence is therefore *per-edge*:

$$\forall\, (i,j) \in E: \quad \nu_{ij} \cdot \eta_{\text{edge},ij} \gt \frac{\rho_{\Sigma,ij}}{R_{\Sigma,ij}}$$

where $\rho_{\Sigma,ij}$ is the per-edge disturbance rate and $R_{\Sigma,ij}$ is the per-edge reserve. This is the vector generalization of #per-dimension-persistence applied to strategy edges.

### 1.6 Epistemic Status (Part 1)

**Strategic tempo definition** (Section 1.1): *Definition.* A naming of the quantity that characterizes the agent's total strategic corrective capacity. Max attainable: axiomatic (it is a definition). The definition is well-motivated by the structural parallel with epistemic tempo and consistent with the four verified cases.

**Consistency with verified cases** (Section 1.2): *Derived.* Each computation follows directly from the per-edge rates already established in #strategic-dynamics-derivation. The tempo-to-sector-parameter relationship is algebraic.

**Structural decomposition** (Section 1.3): *Derived (AND-chain), Hypothesis (general DAG).* The depth-$d$ chain tempo is derived from the evidence-starvation rates already in Props B.2 and the depth-$d$ generalization. The general DAG form is hypothesized — consistent with the four cases but not verified for mixed topologies.

**Regime adjustment** (Section 1.4): *Hypothesis.* The identifiability-adjusted tempo inherits the identifiability coefficient from #edge-update-causal-validity, which is itself a hypothesis.

**Persistence relation** (Section 1.5): *Derived.* The bounds relating $\mathcal{T}_\Sigma$ to $\alpha_\Sigma$ are algebraic (min-sum inequalities).

---

## Part 2: Cognitive Cost of Strategy (IB/MDL for DAGs)

### 2.1 The Problem

The epistemic side of AAD has a principled framework for model compression: the information bottleneck ( #information-bottleneck) balances retained history against predictive power, with the trade-off $\beta$ depending on environment volatility. The deliberation-cost analysis ( #deliberation-cost) captures the temporal cost of thinking versus acting.

But neither addresses the *ongoing* cognitive cost of maintaining a strategy DAG. A strategy DAG with $\lvert V\rvert$ nodes and $\lvert E\rvert$ edges, each carrying a Beta credence, must be:
- **Stored** in the agent's representational capacity
- **Propagated** to compute plan confidence via AND/OR rules
- **Updated** via execution evidence on each tested edge
- **Monitored** for structural changes (pruning dead edges, grafting new ones)

These are real costs. An agent with finite representational capacity (bounded context window, limited working memory, constrained computational budget) cannot maintain an arbitrarily complex strategy. The question is: what is the principled trade-off between strategy complexity and planning utility?

### 2.2 Strategy Description Length

*[Formulation (strategy-description-length)]*

The description length of a strategy DAG $\Sigma_t$ decomposes into structural and parametric components:

$$\text{DL}(\Sigma_t) = \text{DL}_{\text{struct}}(G) + \text{DL}_{\text{param}}(\boldsymbol{p} \mid G)$$

**Structural component.** The graph $G = (V, E, \gamma)$ with node types (action leaf, condition leaf, internal) and combination rules $\gamma(v) \in \{\text{AND}, \text{OR}\}$:

$$\text{DL}_{\text{struct}}(G) = \log\binom{\lvert V\rvert^2}{\lvert E\rvert} + \lvert V\rvert\!\cdot\!\log 3 + \lvert V_{\text{internal}}\rvert\!\cdot\!\log 2$$

where the first term counts the edge-selection cost (which of the possible edges are present), the second counts node-type assignments, and the third counts AND/OR assignments. This is the standard MDL graph-encoding cost, up to constant factors.

**Parametric component.** Each edge $(i,j)$ carries a Beta credence $\text{Beta}(\alpha_{ij}, \beta_{ij})$. Under the MDL convention, the parametric cost per edge is approximately half a parameter (one degree of freedom in Beta, since $p_{ij} = \alpha_{ij}/(\alpha_{ij}+\beta_{ij})$ and $n_{ij} = \alpha_{ij} + \beta_{ij}$):

$$\text{DL}_{\text{param}}(\boldsymbol{p} \mid G) \approx \frac{\lvert E\rvert}{2}\log n_{\text{eff}}$$

where $n_{\text{eff}}$ is the effective sample size. As the agent accumulates evidence, the parametric cost grows logarithmically — well-evidenced edges have tighter credence intervals, requiring more bits to specify.

**Total cost scaling.** The dominant term is structural: $O(\lvert E\rvert \log \lvert V\rvert)$. Strategy complexity scales primarily with the number of edges (the causal claims the agent makes), not with the precision of those claims.

### 2.3 The Information Bottleneck for Strategy

The epistemic IB objective ( #information-bottleneck) is:

$$\phi^\ast = \arg\min_\phi \left[I(M_t;\, \mathcal{C}_t) - \beta \cdot I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})\right]$$

balancing compression cost against predictive power. The strategic analog:

*[Formulation (strategy-IB-objective)]*

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\text{DL}(\Sigma_t) - \beta_\Sigma \cdot I(\Sigma_t;\, \pi^\ast \mid M_t)\right]$$

where:
- $\text{DL}(\Sigma_t)$: description length (storage and maintenance cost)
- $I(\Sigma_t;\, \pi^\ast \mid M_t)$: the mutual information between the strategy and the optimal policy, given the current model — how much the strategy tells the agent about what to do

**What is the "relevant information" the strategy must preserve?** For the epistemic IB, the relevant information is predictive power — how much the model tells you about future observations given future actions. For the strategy IB, the relevant information is *action guidance* — how much the strategy tells you about the optimal action-value ordering.

*[Discussion (action-guidance as relevant information)]*

The strategy's purpose is to guide action selection. A strategy DAG is useful to the extent that it changes the agent's action choice. Formally, define the **action-guidance information**:

$$I(\Sigma_t;\, \pi^\ast \mid M_t) = H(\pi^\ast \mid M_t) - H(\pi^\ast \mid M_t, \Sigma_t)$$

This is the reduction in uncertainty about the optimal policy that the strategy provides, given the current model. An agent without $\Sigma_t$ selects actions using $M_t$ alone (model-free or purely exploratory); with $\Sigma_t$, the agent narrows the action space to those consistent with its causal plan. The information value of $\Sigma_t$ is this narrowing.

**When is action guidance maximal?** When the action space is large, the environment has structure the model alone does not exploit, and the strategy identifies the few actions worth considering. In a two-action environment, $\Sigma_t$ provides at most 1 bit of guidance. In a 1000-action environment with deep causal structure, $\Sigma_t$ can provide $\approx 10$ bits.

**When is action guidance minimal?** When $M_t$ alone is sufficient for near-optimal action selection (the value function is simple enough to compute directly), or when $\Sigma_t$ is so inaccurate that it misdirects more than it helps. The latter connects to #strategic-calibration: a miscalibrated strategy has negative net guidance.

### 2.4 The Complexity-Depth Trade-off

Chain confidence decay ( #chain-confidence-decay) and evidence starvation ( #strategic-dynamics-derivation, Prop B.2) impose independent penalties on deep strategies. Combined with the cognitive cost of maintaining edges, these yield an information-theoretic upper bound on useful DAG depth.

*[Derived (useful depth bound, heuristic)]*

Consider a uniform AND-chain of depth $d$ with per-edge confidence $p$ and per-edge experience $n$. Three depth-dependent costs:

1. **Confidence decay** ( #chain-confidence-decay): Plan confidence $P(\text{chain}) = p^d$. The information content of the plan's confidence assessment: $-d\log p$ bits (log-confidence grows linearly).

2. **Evidence starvation** (Section 1.3 above): Strategic tempo for the deepest edge: $\nu_{d} \cdot \eta_d = \nu p^{d-1}/(n+1)$. The deepest edge's correction rate decays exponentially.

3. **Cognitive cost** (Section 2.2): Description length of a depth-$d$ chain: $\text{DL} \approx d\log d + (d/2)\log n$ (the $d\log d$ from structure, $(d/2)\log n$ from parameters).

The marginal benefit of adding edge $d+1$ to the chain is the additional confidence resolution — the ability to distinguish the plan's success probability at the resolution of $p^{d+1}$ rather than $p^d$. This marginal benefit is $\log(1/p)$ bits — constant in $d$.

The marginal cost has three components, all growing with $d$:
- Marginal confidence loss: constant ($\log(1/p)$ bits)
- Marginal evidence starvation: the new edge's correction rate is $\nu p^d / (n+1)$, exponentially decreasing
- Marginal cognitive cost: $\approx \log d$ bits for the structural cost

**The depth bound.** Adding an edge is net-beneficial when the marginal planning benefit exceeds the marginal cost. The binding constraint is evidence starvation: beyond depth $d^\ast$ where $\nu p^{d^\ast - 1}/(n+1) \lt \rho_\Sigma / R_\Sigma$, the new edge cannot be calibrated — its credence drifts away from truth faster than evidence corrects it. This gives:

*[Derived (maximum useful chain depth, conditional on Beta-Bernoulli)]*

$$d^\ast = 1 + \left\lfloor\frac{\log\!\left(\frac{R_\Sigma}{\rho_\Sigma(n+1)}\right)}{\log(1/p)}\right\rfloor$$

Beyond $d^\ast$, additional edges are epistemically unlearnable — they fail the per-edge persistence condition regardless of the agent's action rate. This is a *hard* bound from the learning dynamics, independent of the agent's cognitive capacity. The cognitive cost adds a softer bound on top: even edges within the learnable range may not be worth maintaining if their marginal description cost exceeds their marginal planning value.

**Quantitative illustration** (uniform chain, $p = 0.8$, $\nu = 1$):

| $n$ | $\rho_\Sigma/R_\Sigma$ | $d^\ast$ |
|-----|----------------------|----------|
| 10 | 0.01 | 10 |
| 10 | 0.1 | 0 |
| 100 | 0.01 | 5 |
| 100 | 0.1 | 0 |

Note: $d^\ast = 0$ means no edges are learnable at that disturbance rate — the first edge already fails the per-edge persistence condition ($1/(n+1) < \rho_\Sigma / R_\Sigma$). High experience ($n$) and high disturbance ($\rho_\Sigma$) both reduce useful depth. This is the gain-collapse effect from #strategic-dynamics-derivation applied to the depth dimension: deep edges have both lower gain (from $1/(n+1)$) and lower trial rates (from $p^{d-1}$), making them the first to lose their persistence battle.

### 2.5 The Enriched Explicit Strategy Condition

The explicit strategy condition ( #explicit-strategy-condition) states that planning beats exploring when:

$$C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$$

Section 2.2 gives content to $C_{\text{maintain}}$ — the ongoing cost of keeping $\Sigma_t$ in representational capacity:

*[Formulation (enriched strategy condition)]*

$$C_{\text{plan}} + C_{\text{DL}}(\Sigma_t) + C_{\text{update}}(\Sigma_t) + C_{\text{monitor}}(\Sigma_t) \lt C_{\text{explore}} + C_{\text{repair}}$$

where:
- $C_{\text{DL}}(\Sigma_t) \propto \text{DL}(\Sigma_t)$: storage cost, proportional to description length
- $C_{\text{update}}(\Sigma_t) \propto \lvert E\rvert \cdot \bar\nu$: per-cycle update cost, proportional to edge count times mean trial rate (each evidence event triggers an edge update)
- $C_{\text{monitor}}(\Sigma_t) \propto \lvert V\rvert$: structural monitoring cost, checking whether nodes should be pruned or added (see #structural-change-as-parametric-limit)

**The complexity ceiling.** The enriched condition implies an upper bound on strategy complexity. For a given domain ($C_{\text{explore}}$, $C_{\text{repair}}$ fixed), increasing $\Sigma_t$ complexity eventually makes the left side exceed the right:

$$\lvert E\rvert^\ast : \quad C_{\text{plan}} + C_{\text{DL}}(\lvert E\rvert^\ast) + C_{\text{update}}(\lvert E\rvert^\ast) = C_{\text{explore}} + C_{\text{repair}}$$

Beyond $\lvert E\rvert^\ast$ edges, the agent should simplify its strategy — drop low-value edges, collapse unobservable chains to plan-level aggregates (as in Prop B.3), or prune alternatives at OR-nodes. The "how detailed should my plan be?" question from #explicit-strategy-condition's working notes now has a formal answer: detailed enough that the planning benefit exceeds the maintenance cost, and no more.

### 2.6 Strategy Compression: the IB Trade-off in Practice

The IB trade-off $\beta_\Sigma$ for strategy compression depends on the same factors as the epistemic IB trade-off $\beta$, plus strategy-specific considerations:

**High $\beta_\Sigma$ (retain detail) when:**
- Actions are expensive/irreversible — planning mistakes are costly, so high-resolution strategy pays
- The environment is causally complex — many edges carry distinct, non-redundant information about action-outcome links
- The strategy DAG has been well-evidenced — maintenance cost is low relative to planning value (many edges are near the true value, requiring only monitoring, not active revision)

**Low $\beta_\Sigma$ (compress aggressively) when:**
- Actions are cheap/reversible — trial-and-error is affordable
- The environment is volatile ($\rho_\Sigma$ high) — detailed causal models go stale quickly, wasting maintenance effort
- The agent has limited representational capacity — LLM context windows, human working memory, organizational communication bandwidth
- Many edges are in Regime C — unidentifiable edges provide no strategic tempo, so maintaining them is pure cost

*[Discussion (compression operations)]*

Concrete compression operations for strategy DAGs:

1. **Edge pruning**: remove edges with credence near 0 (causal link disconfirmed) or near 1 (link confirmed, no longer informative). Reduces $\lvert E\rvert$.

2. **Chain collapse**: replace an AND-chain $A \to B \to G$ with a single aggregate edge $A \to G$ carrying credence $\hat\Phi = p_1 p_2$. This is exactly the plan-level tracking from Prop B.3 — it sacrifices per-edge diagnostics for lower description length. Justified when the intermediate $B$ is unobservable.

3. **Alternative pruning**: at an OR-node with many arms, drop arms that are dominated (lower credence than the best, and exploration cost exceeds expected information gain). Reduces breadth.

4. **Abstraction**: replace a detailed sub-DAG with a single representative node. The sub-DAG's internal structure is "compiled" into a single credence. This is the strategy analog of model abstraction in the epistemic IB.

Each operation reduces $\text{DL}(\Sigma_t)$ at the cost of $I(\Sigma_t;\, \pi^\ast \mid M_t)$ — action guidance. The IB framework says: compress until the marginal description-length saving equals $\beta_\Sigma$ times the marginal action-guidance loss.

### 2.7 Connection to Chain Confidence Decay

Chain confidence decay ( #chain-confidence-decay) provides a planning-side constraint on strategy depth: longer chains have lower aggregate confidence, providing less useful discrimination for action selection. The cognitive-cost analysis provides an independent constraint on the learning side.

*[Discussion (double depth penalty, extended)]*

#chain-confidence-decay identifies a double depth penalty: confidence decay (propagation) and evidence starvation (learning). The cognitive cost adds a *third* penalty:

1. **Confidence decay**: deeper chains have lower plan confidence, reducing the *signal* available for action selection
2. **Evidence starvation**: deeper edges learn more slowly, reducing the *calibration* of that signal
3. **Cognitive cost**: deeper chains have higher description length, consuming more representational capacity

These three penalties compound:
- An agent with a deep, poorly calibrated strategy (penalties 1 + 2) that also has limited capacity (penalty 3) faces a triple bind
- The optimal depth $d^\ast$ is the minimum over three independent constraints: the evidence-starvation bound (Section 2.4), the confidence-discrimination bound (when $p^d$ falls below the action-selection threshold), and the cognitive-capacity bound (when $\text{DL}(d)$ exceeds the agent's budget)

In practice, evidence starvation is likely the binding constraint for deep AND-chains in volatile environments, while cognitive cost is the binding constraint for broad OR-nodes in capacity-limited agents.

### 2.8 Epistemic Status (Part 2)

**Strategy description length** (Section 2.2): *Formulation.* The MDL decomposition into structural and parametric components is standard information-theoretic machinery applied to DAGs. It is a representational choice, not a derived result. Alternative encodings (e.g., Kolmogorov complexity, or prequential MDL) would give different constants but the same scaling.

**Strategy IB objective** (Section 2.3): *Formulation, discussion-grade.* The extension of the IB framework from models to strategies is structurally motivated — both face a compression-utility trade-off. But the "relevant information" for strategy ($I(\Sigma_t;\, \pi^\ast \mid M_t)$) involves the optimal policy, which is generally unknown. This makes the formulation analytically useful but computationally intractable as stated. The epistemic IB has the same issue (the relevant information involves future observations). Max attainable: formulation (there is no unique "right" way to define the trade-off; this is a useful one).

**Useful depth bound** (Section 2.4): *Derived, conditional on Beta-Bernoulli and uniform chain.* The evidence-starvation bound on $d^\ast$ follows directly from the per-edge persistence condition. The specific formula is conditional on the uniform-chain assumption; the qualitative result (there exists a maximum useful depth, determined by the persistence condition) is robust.

**Enriched strategy condition** (Section 2.5): *Formulation.* The decomposition of $C_{\text{maintain}}$ into storage, update, and monitoring costs is a design framework, not a derivation. It gives content to the previously informal $C_{\text{maintain}}$ term.

**Compression operations** (Section 2.6): *Discussion-grade.* The operations (pruning, collapse, abstraction) are motivated by the IB framework but their optimality conditions are not derived.

---

## Summary: What Promotes to Segments

### Candidate segment: `strategic-tempo`

**Type**: Definition. **Status**: Axiomatic.

**Formal Expression**: $\mathcal{T}_\Sigma = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij}$

**Content**: Definition, consistency verification with the four cases, structural decomposition (depth-gated for AND, exploration-gated for OR), regime adjustment. The per-edge persistence formulation.

**Dependencies**: #adaptive-tempo, #edge-update-via-gain, #strategic-dynamics-derivation, #edge-update-causal-validity.

**What's derived vs hypothesized**: The definition is a naming. Consistency with Props B.1-B.4 is derived. The general DAG form and regime adjustment are hypothesized.

### Candidate segment: `strategy-complexity-cost`

**Type**: Formulation. **Status**: Discussion-grade.

**Formal Expression**: $\text{DL}(\Sigma_t) = \text{DL}_{\text{struct}}(G) + \text{DL}_{\text{param}}(\boldsymbol{p} \mid G)$ and the strategy IB objective.

**Content**: Description length, the IB trade-off for strategy, the enriched explicit-strategy condition, compression operations, the useful-depth bound.

**Dependencies**: #information-bottleneck, #explicit-strategy-condition, #chain-confidence-decay, #strategic-dynamics-derivation, #structural-change-as-parametric-limit.

**What's derived vs hypothesized**: The description length decomposition is standard. The IB objective is a formulation. The depth bound is derived (conditional on Beta-Bernoulli). The compression operations are discussion-grade.

---

## Open Questions

1. **Mixed AND/OR DAGs.** The strategic tempo decomposition is verified for pure AND-chains and pure OR-nodes. Mixed topologies may reveal interaction effects between evidence starvation and exploration gating. A spike testing specific mixed cases (e.g., an AND-chain feeding an OR-node) would settle this.

2. **Optimal strategy topology.** Given a fixed cognitive budget $\text{DL}_{\max}$, what DAG structure maximizes strategic tempo? The analysis suggests: broad, shallow DAGs with many OR-alternatives (each getting some exploration) dominate deep AND-chains (which starve downstream edges). But this depends on the domain's causal structure — if the real causal chain is deep, a shallow strategy misses genuine causal links.

3. **Dynamic complexity.** An agent should vary its strategy complexity over time: start simple (low $\text{DL}$, broad exploration), elaborate as evidence accumulates (grow the DAG), and re-simplify when the environment changes (prune stale edges). The IB trade-off $\beta_\Sigma$ should increase with evidence and decrease with volatility. Formalizing this dynamics is open.

4. **Connection to the three-way tradeoff.** The third --GAP-- in Section II is "Three-way exploit/explore/deliberate allocation with $\Sigma_t$." Strategic tempo provides the missing quantity for that allocation: the agent should allocate trials to maximize the minimum per-edge $\nu_{ij} \cdot \eta_{\text{edge},ij}$ (for persistence), or to maximize total $\mathcal{T}_\Sigma$ (for throughput), or to balance between them. This connects to the exploit/explore tradeoff ( #ciy-unified-objective) extended with a "deliberate = revise $\Sigma_t$" mode.

5. **Stochastic strategic tempo.** The working notes in #strategy-persistence-schema mention $\rho_\Sigma / \sqrt{\mathcal{T}_\Sigma}$ rather than $\rho_\Sigma / \mathcal{T}_\Sigma$ for stochastic steady-state strategic mismatch. If the stochastic treatment carries over, the persistence condition becomes $\mathcal{T}_\Sigma \gt (\rho_\Sigma / R_\Sigma)^2$ — qualitatively different from the deterministic case. Clarifying which regime applies (deterministic drift vs stochastic noise) is domain-dependent and open.

6. **Cognitive cost for LLM agents.** For logogenic agents ( `03-logogenic-agents/`), the representational capacity constraint is the context window. Strategy $\text{DL}(\Sigma_t)$ must fit within the context budget alongside $M_t$ and the task description. This gives a concrete version of the complexity ceiling: $\text{DL}(\Sigma_t) \lt C_{\text{context}} - \text{DL}(M_t) - \text{DL}(\text{task})$. The IB trade-off $\beta_\Sigma$ is directly calibrated by what fits in the window.
