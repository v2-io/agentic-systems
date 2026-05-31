---
slug: form-strategy-complexity-cost
type: formulation
status: robust-qualitative
depends:
  - def-strategic-tempo
  - form-information-bottleneck
  - norm-explicit-strategy-condition
  - der-chain-confidence-decay
  - deriv-strategy-cost-regret-bound
  - form-structural-change-as-parametric-limit
  - def-value-object
  - form-objective-functional
stage: draft
---

# Formulation: Cognitive Cost of Strategy

A formulation connecting strategy structure to its *maintenance cost* — making the explicit-strategy condition from #norm-explicit-strategy-condition quantitative. The minimum description length of a strategy DAG $\Sigma_t = (V, E, p, \gamma)$ decomposes into *structural* bits (encoding topology — node identities, edge connectivity, AND/OR labels) and *parameter* bits (encoding the edge credences given the topology), scaling as $O(\lvert E\rvert\log\lvert V\rvert)$ for sparse DAGs and moderate-precision credences.

The framework offers a **strategy IB objective**: $\Sigma_t$ is the information-bottleneck compression of the interaction history $\mathcal{C}_t$ *for guidance*, parallel to $M_t$ as the IB-compression of $\mathcal{C}_t$ *for prediction*. The variational form trades off compression cost $I(\mathcal{C}_t;\Sigma_t)$ against a KL divergence from the optimal-policy reference to the strategy-induced policy. The **KL direction** is *not* a stipulation — it is forced by a regret-bound derivation ( #deriv-strategy-cost-regret-bound): under bounded value range and deterministic $\pi^\ast = \delta_{a^\ast}$ (AAT's canonical scope, #def-value-object), the strategy-induced regret satisfies $R(Q_{\Sigma_t}) \leq V_{\max}\cdot\operatorname{TV}(\pi^\ast, Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ by Pinsker, with the sharper Bretagnolle-Huber identity $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})})$ as the primary form. The opposite-direction KL is $+\infty$ whenever $Q_{\Sigma_t}$ places any mass off $a^\ast$ — a vacuous bound. The direction is *forced* with $\pi^\ast$ first (reverse-KL in variational-inference vocabulary). Within the direction-forced family, reverse-KL is *uniquely* selected by a chain-rule additivity axiom (Hobson 1969; Csiszár 1991), AAT-internally motivated as the divergence-level analog of #der-chain-confidence-decay's log-additive layer. This is the **second instance of the four-layer additive-coordinate-forcing meta-pattern** ( #disc-additive-coordinate-forcing): a uniqueness theorem operating on an AAT-internally-motivated additivity axiom forces a specific coordinate. The whole construction lifts the IB objective from discussion-grade to *robust-qualitative*.

The framework derives a **maximum useful chain depth** for AND-chains: given base observation rate $\nu$, per-edge success probability $\theta$, effective sample size $n$, and disturbance-to-capacity ratio $\rho_\Sigma/R_\Sigma$, there is a finite depth $d^\ast$ beyond which the deepest edge cannot maintain bounded mismatch. Beyond this depth, evidence starvation makes the edge uncorrectable faster than the environment invalidates it. A central observation: **deep AND-chains suffer a triple depth penalty** that compounds. (1) *Confidence decay* ( #der-chain-confidence-decay): aggregate confidence $\prod p_k$ decays geometrically — *the plan is less likely to succeed*. (2) *Evidence starvation* ( #deriv-edge-credence-dynamics): effective observation rate decays geometrically — *the plan is harder to calibrate*. (3) *Cognitive cost* (this segment): each additional depth level adds $O(\log\lvert V\rvert)$ bits — *the plan is more expensive to maintain*. All three are multiplicative in depth, making deep sequential strategies exponentially costly along three independent dimensions and creating systematic pressure toward *shallow, OR-heavy strategies*. The framework also makes the maintenance cost from #norm-explicit-strategy-condition concrete by decomposing it into representation cost (proportional to description length), revision cost (proportional to strategic tempo $\mathcal{T}_\Sigma$), and monitoring cost (proportional to edges with partial identifiability).

A practical consequence for language-constituted agents: a context window of $W$ tokens imposes a hard upper bound $\operatorname{DL}(\Sigma_t) \leq W\log_2(\lvert\text{vocab}\rvert)$, making the IB trade-off *non-optional* — the agent *must* compress its strategy, and $d^\ast$ becomes a context-window-limited quantity (a 128K-token context may support a 500-edge DAG encoded in natural language; a 4K-token window may support only a 15-edge sketch). The Miller (2022) coevolving-automata result provides a complementary constraint from the interaction side: a complex $\Sigma_t$ whose edges are only tested over a short horizon is *indistinguishable from a simpler strategy*. The interaction horizon compresses the strategy space from above, just as maintenance cost and evidence starvation compress it from below.

## Formal Expression

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

The optimal strategy complexity balances parsimony against decision-relevance. $\Sigma_t$ is the IB-compression of the interaction history $\mathcal{C}_t$ *for guidance*, parallel to $M_t$ as the IB-compression of $\mathcal{C}_t$ *for prediction* ( #disc-compression-operations for the shared IB shape across AAT's compression operations, and for the relationship between the theoretical $I(\mathcal{C}_t; \Sigma_t)$ compression cost and the operational DL-based minimization below):

**Theoretical form (variational).** $\Sigma_t$ is a tractable variational approximation of the optimal-policy posterior $Q^\ast(\pi \mid M_t)$. The strategy-cost objective:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal{C}_t;\, \Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}\bigl(\pi^\ast(\cdot \mid M_t) \,\big\Vert\, Q_{\Sigma_t}(\pi \mid M_t)\bigr)\right]$$

where $Q_{\Sigma_t}(\pi \mid M_t)$ is the action distribution induced by the strategy DAG given the current model state, and $\pi^\ast(\cdot \mid M_t)$ is the optimal-policy reference. The KL direction — $\pi^\ast$-first — is forced by the regret-bound derivation (next paragraph); the opposite direction is vacuous under deterministic $\pi^\ast$.

**Regret-bound derivation of KL direction.** Under AAT's canonical scope, $\pi^\ast = \delta_{a^\ast}$ is deterministic ( #def-value-object). Define the strategy-induced regret against $\pi^\ast$ as $R(Q_{\Sigma_t}) := V(a^\ast) - \mathbb{E}_{a \sim Q_{\Sigma_t}}[V(a)]$, where $V(a) = Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ is the action-value ( #def-value-object, $O_t$ induces $V$ via #form-objective-functional). Under bounded value range $V_{\max} := \max_a V(a) - \min_a V(a)$:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max}\cdot(1 - Q_{\Sigma_t}(a^\ast)) \;=\; V_{\max}\cdot\operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$$

Applying Pinsker's inequality ($\operatorname{TV}(P,Q) \leq \sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(P\Vert Q)}$) with $P = \pi^\ast$, $Q = Q_{\Sigma_t}$:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max}\cdot\sqrt{\tfrac{1}{2}\, D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$$

Under deterministic $\pi^\ast$, $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast)$ — finite and graded whenever $Q_{\Sigma_t}(a^\ast) \gt 0$. The opposite-direction $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ equals $+\infty$ whenever $Q_{\Sigma_t}$ places any mass off $a^\ast$, giving a vacuous bound. The regret-bound argument therefore **forces the KL direction** with $\pi^\ast$ first. Within the direction-forced f-divergence family, reverse-KL is *uniquely* selected under the chain-rule additivity axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975), which is AAT-internally motivated as the divergence-level analog of additive log-confidence decay ( #der-chain-confidence-decay). See #deriv-strategy-cost-regret-bound §6.1 for the uniqueness theorem, §6.2 for secondary supporting characterizations (gradient-tractability, VI-alignment, MDL), and §7 for the linear-vs-square-root $\beta_\Sigma$ trade-off.

The variational form is the strategy-layer analog of variational free energy minimization in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99; Parr & Pezzulo 2022, *Active Inference*, MIT Press). AAT borrows the variational form as the appropriate generalization of the Shannon-MI relevance term and now derives the direction of KL from an internal regret-bound argument — without committing to AI's preferences-as-priors encoding ($C(o) = \log P_{\mathrm{pref}}(o)$; AAT's $O_t$ remains a value functional on trajectories, #form-objective-functional) or to expected free energy as master objective (AAT's CIY-unified objective is a related but distinct decomposition; #disc-ciy-unified-objective).

**Operational form.** Since $I(\mathcal{C}_t; \Sigma_t)$ is not computable in closed form for general DAG encodings, the operational minimization replaces the information cost with a description-length surrogate and the KL term with a sample-based estimate (a per-edge calibration discrepancy weighted by decision-relevance — see #disc-credit-assignment-boundary for the gradient form):

$$\Sigma_t^\ast \approx \arg\min_{\Sigma_t} \left[\operatorname{DL}(\Sigma_t) + \beta_\Sigma \cdot \widehat{D_{\mathrm{KL}}}(\pi^\ast \,\Vert\, Q_{\Sigma_t})\right]$$

where:
- $\operatorname{DL}(\Sigma_t)$: description length (coding-cost upper bound on $I(\mathcal{C}_t; \Sigma_t)$ for the given DAG encoding scheme — see §2.2 below)
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
| 100 | 0.01 | 0 |
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
- $C_{\text{revise}} \propto \sum_{(i,j)} \nu_{ij} \cdot c_{\text{update}}$: cost of processing edge updates (proportional to strategic tempo $\mathcal{T}_\Sigma$ times per-update cost)
- $C_{\text{monitor}} \propto \lvert\{(i,j) : \iota_{ij} \lt 1\}\rvert$: cost of monitoring edges with partial identifiability (the agent must do extra causal reasoning for non-trivial edges)

This decomposition makes the #norm-explicit-strategy-condition's maintenance term concrete: each component maps to a quantity defined elsewhere in the theory.

### Complexity compression operations

*[Discussion (complexity-compression)]*

The IB objective suggests three compression operations, corresponding to structural changes from #form-structural-change-as-parametric-limit:

1. **Edge pruning** (operation 3 in #form-structural-change-as-parametric-limit): remove edges with $\eta_{\text{edge},ij} \cdot I_{\text{edge},ij} \lt c_{\text{bit}}$, where $I_{\text{edge},ij}$ is the decision-relevance of that edge and $c_{\text{bit}}$ is the per-bit maintenance cost. Edges that contribute less decision value than their representational cost are candidates for removal.
2. **Node merging** (reducing $\lvert V\rvert$): collapse intermediate nodes that serve no decision-distinguishing function. This reduces $\operatorname{DL}_{\text{struct}}$ by a factor proportional to the reduction in $\lvert V\rvert$.
3. **Depth truncation** at $d^\ast$: prune all edges beyond the maximum useful depth. This is not optimization but necessity --- edges beyond $d^\ast$ cannot maintain bounded mismatch.

## Epistemic Status

The description length formulation is a *formulation* --- it applies standard MDL to the strategy DAG, which is a representational choice not a derived necessity. The IB objective is *formulation (strengthened by regret bound)* in its variational form (above): the specific KL *direction* ($\pi^\ast$-first, i.e., reverse-KL in the variational-inference vocabulary) is *derived* as an upper regret bound via Pinsker's inequality under bounded value range and deterministic $\pi^\ast$ (see Regret-bound derivation paragraph above; full derivation in appendix #deriv-strategy-cost-regret-bound). The choice of reverse-KL *within* the direction-forced family upgrades from canonical-formulation to **derived (conditional on chain-rule additivity axiom)** — the chain-rule axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975) picks reverse-KL uniquely among f-divergences, and the axiom is AAT-internally motivated as the divergence-level analog of #der-chain-confidence-decay (see #deriv-strategy-cost-regret-bound §6.1). Secondary properties (gradient-tractability, variational-inference alignment with Friston et al. 2017, Da Costa et al. 2020, Parr & Pezzulo 2022; MDL coding; compatibility with Amari & Nagaoka 2000 Fisher geometry) are convergent evidence rather than independent uniqueness grounds — in particular, Fisher-metric-at-second-order is *not* distinguishing within f-divergences (Eguchi 1983, *Ann. Statist.* 11(3):793–803). The regret-bound derivation closes the direction ambiguity that the earlier V-medium move (commit `a14682e`) left open: the initial V-medium form used $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ (forward-KL), which is $+\infty$ under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has any off-optimum mass — a different-valued but structurally identical degeneracy to the Shannon-MI zero it replaced. The $\pi^\ast$-first reverse-KL direction escapes both degeneracies by construction.

The variational form replaces an earlier Shannon-MI form $-\beta_\Sigma \cdot I(\Sigma_t;\, \pi^\ast \mid M_t)$ which had a Shannon-zero degeneracy: when $\pi^\ast$ is a deterministic function of $M_t$ (the standard scope), Shannon mutual information to a constant vanishes identically, collapsing the objective to $\arg\min \operatorname{DL}(\Sigma_t)$. The $\pi^\ast$-first KL form does not have this degeneracy and is graded whenever $Q_{\Sigma_t}$ places any mass on $a^\ast$. The maximum useful depth $d^\ast$ is *derived* conditional on Beta-Bernoulli dynamics and the per-edge persistence condition from #def-strategic-tempo. The triple depth penalty is an *observation* combining results from three independent segments. The enriched maintenance decomposition is *formulation*. The compression operations are *discussion-grade*.

**On $\beta_\Sigma$ interpretation.** Under the Pinsker-reverse-KL bound $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2} D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$, a square-root-in-KL trade-off would naturalize $\beta_\Sigma$ globally as $\beta_\Sigma \propto V_{\max}$. The segment retains the linear-in-KL form (to preserve the rate-distortion-Lagrangian IB shape shared with #disc-compression-operations); under the linear form, $\beta_\Sigma$ has only a *local* regret-bound interpretation ($\partial R / \partial D_{\mathrm{KL}}$ at the operating point). This is a trade-off between IB-shape alignment and regret-scale naturalization. Under AAT's canonical deterministic-$\pi^\ast$ scope, the sharper Bretagnolle-Huber identity $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})})$ holds as the primary form ( #deriv-strategy-cost-regret-bound §4); Pinsker is retained here for IB-shape alignment and as the loose general form correct for stochastic-$\pi^\ast$ extensions.

**Assumption explicitly stated: bounded value range.** The regret-bound derivation requires $V_{\max}:=\max_a V(a) - \min_a V(a) \lt \infty$ over $\mathcal{A}$ at fixed $M_t$. This is mild but not automatic — #form-objective-functional specifies $V_{O_t}: \text{trajectories} \to \mathbb{R}$, and bounded range at fixed state is an additional assumption stated here.

Max attainable: *robust-qualitative* for the IB objective with the direction-forced derivation; conditional for the specific functional form (linear vs. square-root in KL). The DL formulation is standard; the depth bound could reach exact status for specific edge models. The regret-bound derivation does not extend to stochastic $\pi^\ast$ (outside AAT canonical scope); see #def-value-object continuation conventions for scope.

## Discussion

**Connection to #norm-explicit-strategy-condition.** The enriched maintenance decomposition gives the cost inequality quantitative content: an agent can now *compute* whether a proposed strategy is worth maintaining by estimating its description length, revision cost, and monitoring burden, and comparing against the exploration/repair cost of operating without it.

**LLM context windows as DL constraint.** For language-constituted agents ( `03-llm-core/`), the strategy must fit in the context window. A context window of $W$ tokens imposes $\operatorname{DL}(\Sigma_t) \leq W \cdot \log_2(\lvert\text{vocab}\rvert)$ as a hard constraint. This makes the IB trade-off non-optional: the agent *must* compress its strategy, and the depth bound $d^\ast$ becomes a context-window-limited quantity. A 128K-token context window may support a 500-edge DAG encoded in natural language; a 4K-token window may support only a 15-edge sketch.

**Computational compression from interaction horizon (Miller 2022).** The maximum useful depth $d^\ast$ derived above constrains complexity from the *maintenance* side (evidence starvation). Miller (2022, *Ex Machina*, Table 12.2) provides a complementary constraint from the *interaction* side: the number of interaction rounds compresses the space of behaviorally distinguishable strategies regardless of the agent's internal complexity. For Moore machines with binary actions:

| Agent states | Unique computations | After 1 round | After 2 rounds | After 4 rounds |
|---|---|---|---|---|
| 1 | 2 | 2 | 2 | 2 |
| 2 | 26 | 2 | 8 | 26 |
| 3 | 1,054 | 2 | 8 | 690 |
| 4 | 57,068 | 2 | 8 | 5,936 |

The pattern: $\text{effective complexity} = \min(\text{agent complexity}, \text{interaction-horizon complexity})$. With only one round, even a four-state machine (57,068 unique computations) reduces to two distinguishable behaviors — equivalent to a one-state machine. With two rounds, all machines with two or more states reduce to eight distinguishable behaviors. The interaction horizon compresses the strategy space from above, just as the maintenance cost and evidence starvation compress it from below. For AAT's strategy DAG, the analog: a complex $\Sigma_t$ whose edges are only tested over a short horizon gains nothing from its depth — the untested structure is indistinguishable from a simpler strategy. This reinforces the $d^\ast$ bound and provides empirical grounding beyond the Beta-Bernoulli derivation.

**Strategy simplification pressure.** The triple depth penalty creates systematic pressure toward shallow, wide (OR-heavy) strategies over deep, sequential (AND-heavy) ones. This aligns with the structural pressure identified in #der-chain-confidence-decay's Discussion, now grounded in three independent mechanisms rather than one.

## Working Notes

- **Mixed topologies.** The depth bound $d^\ast$ assumes uniform AND-chains. Mixed AND/OR DAGs have heterogeneous depth penalties: OR-nodes reset the evidence-starvation clock (each alternative is tested independently), while AND-nodes compound it. The effective depth for computing $d^\ast$ may be the longest AND-chain in the DAG, not the total graph depth.
- **Optimal topology.** Given a fixed DL budget and action rate $\nu$, what DAG topology maximizes decision-relevant information $I(\Sigma_t;\, \pi^\ast \mid M_t)$? This is a combinatorial optimization over graph structures --- likely NP-hard in general but potentially tractable for specific graph families (trees, bounded treewidth).
- **Dynamic complexity.** As edges converge (high $n_{ij}$), their per-edge $\eta_{\text{edge},ij}$ shrinks, but their description length $\operatorname{DL}_{\text{param}}$ grows (more bits to encode the precise credence). The IB objective would favor *dropping* converged edges (they contribute little decision-relevant information since the agent already acts correctly on them), replacing them with a default "high confidence" summary. This is a principled version of "stop tracking what you already know."
- **Stochastic $\mathcal{T}_\Sigma$.** If strategic disturbance follows Model S (stochastic) rather than Model D (deterministic), the steady-state mismatch scales as $\rho_\Sigma / \sqrt{\mathcal{T}_\Sigma}$ rather than $\rho_\Sigma / \mathcal{T}_\Sigma$. The depth bound $d^\ast$ would change accordingly. Not yet derived.

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. *Orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals), staged for an eventual careful promotion pass, kept separate from the certified theory-fix findings. **Coverage for this segment:** 526815, 584721, 773921, 829314, 849201. (Multiple substrates rated this segment top-decile.)

#### 1. Candidate Brief prose / pre-prose

- **"You cannot out-plan the entropy of the environment."** The plain-language stake of the $d^\ast$ max-useful-depth result: beyond $d^\ast$, "the agent accumulates strategic mismatch on deep edges regardless of how fast it acts at the top of the chain" — a "devastating mathematical critique of 5-year corporate strategic plans" (Gemini/829314). Strong candidate Brief hook for the depth bound.
- **"Don't plan further than you can reliably update your plan."** The one-line gloss for bounded-rationality-in-planning (Claude/849201). And: over-planning is "not a psychological flaw but a mathematical error that burns adaptive reserve maintaining uncorrectable beliefs" (Gemini/773921).

#### 2. Candidate Discussion

- **The regret-bound derivation forcing reverse-KL — frame it as the headline strengthening.** Several substrates singled this out as a recent, clean structural win: it converts an arbitrary-looking KL *direction* choice into a decision-theoretic *forcing* argument and resolves the Shannon-zero degeneracy (MI to a deterministic $\pi^\ast$ vanishes) and the forward-KL $+\infty$ degeneracy at once (Claude/584721, 849201; Gemini/773921, 829314). Candidate to foreground in Discussion as "direction is derived, not stipulated."
- **LLM context-window as a literal DL budget.** The $W\log_2|\text{vocab}|$ bound on $\operatorname{DL}(\Sigma_t)$ is "the strongest connection between AAT and modern GenAI engineering in the framework so far" (Gemini/773921). Vivid reader-facing consequences: a chain-of-thought plan exceeding the window induces "sudden-onset dementia — the agent forgets why it is doing what it is doing" (Gemini/829314); and a *counterintuitive prediction* worth stating — small-context agents naturally adopt shallow/wide (OR-heavy) strategies, while large-context agents "might fall into the trap of building brittle deep AND-heavy plans that fail due to volatility before they finish" (Gemini/829314; Claude/526815, 584721). Candidate Discussion bridge to `03-llm-core/`.
- **Six converging arguments for shallow plans (the meta-pattern).** This segment consolidates the *triple* depth penalty (confidence-decay + evidence-starvation + cognitive-cost); adding the strategic-tempo bottleneck (`#def-strategic-tempo`), identifiability-degradation (`#scope-edge-update-causal-validity`), and Miller's interaction-horizon compression from *above* yields six independent mechanisms compounding to the same conclusion. Flagged as a candidate organizing-principle observation worth elevating to a meta-segment (Claude/584721). *(Same meta-pattern surfaced under `#scope-edge-update-causal-validity` and `#def-strategic-tempo` — one home, not three.)*

#### 3. Follow-up items

- **"Stop tracking what you already know" — compression-by-convergence.** The IB objective favors *dropping* converged (high-$n$) edges, whose precise credences cost more bits while contributing little decision-relevant information, replacing them with a "high confidence" default — a principled (not heuristic) continual-learning operation (Claude/584721). Already a Working-Notes bullet; flagged as a candidate to develop.
- **Resolved during the audit window:** Codex/526815 (F69) flagged the $d^\ast$ illustration table as arithmetically wrong (claimed $d^\ast=5$ for the $n=100$, $\rho/R=0.01$ case where the formula gives $0$); the current table reads $d^\ast=0$ for that row (verified 2026-05-31) — the correction has landed. Similarly the Bretagnolle-Huber identity is now the *primary* regret form in canon with Pinsker shown as the intermediate, largely discharging 584721's F-D2 "Pinsker-only" integration-debt note. *(The remaining Codex F70 — `C_revise` scaling as raw $\nu_{ij}$ vs strategic-tempo — and F71 — undeclared warrant-bearing deps — route to the off-ramp as candidate findings; see lift report.)*

#### 4. Readers often ask / wonder

- **How does an agent actually perform "node merging" on a causal DAG?** Is it abstracting several concrete actions into one macro-action (the Options framework / hierarchical RL)? The compression operations (edge-pruning, node-merging, depth-truncation) invite this question (Claude/829314, 849201).
- **Editorial signal:** two substrates read the Active-Inference-differentiation paragraph and the Pinsker-vs-Bretagnolle-Huber detail as belonging in the appendix (`#deriv-strategy-cost-regret-bound`), leaving the operational objective + Pinsker intuition in-body (Claude/829314). Preserved as a placement signal for the eventual pedagogy pass.

#### 5. Candidate figures

- **Sandwich-bound diagram.** Strategy complexity bounded *from below* by maintenance cost / evidence starvation ($d^\ast$) and *from above* by Miller's interaction-horizon compression ($\text{effective complexity}=\min(\text{agent complexity},\text{horizon complexity})$) — "even if you can afford a deep DAG, a short interaction horizon means the depth doesn't pay off" (Claude/584721). A two-sided-bound figure communicates this faster than the prose.
- **Triple-depth-penalty panel.** The three compounding mechanisms (decay / starvation / cost) as a single multiplicative-in-depth visual; "should be visually highlighted as a major structural result" (Gemini/829314).

#### Belongs elsewhere

- **Six-mechanism shallow-plan convergence → a meta-segment.** As above, this cross-segment structural observation (spanning der-chain-confidence-decay, der-observability-dominance, scope-edge-update-causal-validity, def-strategic-tempo, this segment, and Miller's horizon bound) is a candidate organizing principle for the Meta-Architecture cluster rather than living implicitly across six segments (Claude/584721).
- **Context-window-driven strategy-shape prediction → `03-llm-core/`.** The prediction that effective context budget shapes whether a logogenic agent adopts shallow-wide vs deep-brittle strategies is reach into the logogenic-agent material, not this segment (Gemini/829314; Claude/526815).
