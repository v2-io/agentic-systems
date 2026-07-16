---
slug: def-strategic-tempo
type: definition
status: conditional
depends:
  - def-adaptive-tempo
  - hyp-edge-update-via-gain
  - def-strategy-dag
  - scope-edge-update-causal-validity
  - deriv-edge-credence-dynamics
stage: draft
---

# Definition: Strategic Tempo

The strategic analog of #def-adaptive-tempo. **Strategic tempo** $\mathcal T_\Sigma$ is the effective rate at which an agent acquires useful revisions to its strategy $\Sigma_t$ — the sum of per-edge correction capacities across the strategy DAG, with each edge's contribution weighted by an *identifiability coefficient* $\iota_{ij}$ that captures whether the evidence stream genuinely identifies the edge's causal effect. The structural parallel with epistemic tempo is exact: edge observation rate $\nu_{ij}$ times per-edge update gain $\eta_{\text{edge},ij}$ times identifiability coefficient $\iota_{ij}$, summed over edges. The $\iota$ factor is where edge-causal-validity ( #scope-edge-update-causal-validity) enters the operational machinery of strategy revision: *an agent cannot improve the parts of its strategy that it cannot test interventionally.* Regime-A (intervention-rich) edges contribute full tempo at their observation rate; Regime-C (observation-only) edges contribute essentially nothing regardless of how fast the agent acts or how many observations it makes.

A *key structural difference* from epistemic tempo: edge rates are **endogenous**. Epistemic-tempo channel rates $\nu^{(k)}$ are largely exogenous — the environment generates observations at its own pace. Strategic-tempo edge rates $\nu_{ij}$ depend on the agent's *action policy* (which edges get tested) and on *upstream success* (downstream edges are tested only when upstream edges fire). This endogeneity is the source of the structural differences between epistemic and strategic persistence. The framework decomposes strategic tempo by topology. **AND-chains are depth-gated**: each edge at depth $k$ is tested at the upstream-success-attenuated rate $\nu_k = \nu\prod_{j\lt k}\theta_j$. For a uniform chain ($\theta_k = \theta$), total strategic tempo $\mathcal T_\Sigma$ converges to $\nu/((n+1)(1-\theta))$ as $d \to \infty$ — total strategic tempo is bounded even for arbitrarily deep chains, but the marginal contribution of each new edge decays geometrically. The deep edges are *evidence-starved*. **OR-nodes are exploration-gated**: under $\varepsilon$-greedy, the rate allocated to the greedy arm gets nearly all the action budget while exploratory arms get only $\varepsilon/m$. Pure greedy makes non-greedy arms *permanently uncorrectable*.

**Per-edge persistence** inherits the same weakest-link structure as per-dimension epistemic persistence ( #result-per-dimension-persistence): for $\Sigma_t$ to persist, every edge must maintain bounded mismatch — $\forall (i,j) \in E:\;\nu_{ij} \cdot \iota_{ij} \cdot \eta_{\text{edge},ij} \gt \rho_{\Sigma,ij}/R_{\Sigma,ij}$. The aggregate $\mathcal T_\Sigma$ is at most the sum and at least the minimum across edges; exceeding total disturbance is *necessary but not sufficient*. *Persistence is bottleneck-limited by the weakest edge, not governed by the aggregate.* Scalar $\mathcal T_\Sigma$ overestimates effective strategic adaptation for the same reason scalar $\mathcal{T}$ overestimates epistemic adaptation — it averages over heterogeneous correction capacities. A practical consequence: given a fixed action budget, the topology that maximizes strategic tempo is *shallow and OR-heavy* (more edges directly observable, no attenuation); the topology that minimizes it is *deep AND-chains*. As observations accumulate per edge, $\eta_{\text{edge},ij}$ shrinks (diminishing returns), so $\mathcal T_\Sigma$ *declines over time even in a static environment*.

## Formal Expression

*[Definition (strategic-tempo)]*

$$\mathcal{T}_\Sigma = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij} \cdot \iota_{ij}$$

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

$$\alpha_\Sigma \leq \frac{\mathcal{T}_\Sigma}{\lvert E\rvert} \leq \mathcal{T}_\Sigma$$

(minimum $\leq$ average $\leq$ sum). Consequently, $\mathcal T_\Sigma \gt \lvert E\rvert \cdot \rho_\Sigma / R_\Sigma$ is *necessary* for persistence but not sufficient --- the persistence condition is bottleneck-limited by the weakest edge, not governed by the aggregate.

## Epistemic Status

The definition itself is axiomatic --- it names a quantity by analogy with #def-adaptive-tempo. The consistency verification with the four cases from #deriv-edge-credence-dynamics is *derived* (conditional on Beta-Bernoulli dynamics). The AND-chain geometric attenuation is *derived* (conditional on independent edge outcomes). The OR-node exploration gating and identifiability adjustment are *hypotheses* in the general DAG case, though verified for the specific topologies above. The bottleneck-limited persistence observation is *derived* from #result-per-dimension-persistence's result applied to the strategy substate. The additive form also inherits the noise-correlation scope derived in #deriv-tempo-additivity: the edge-wise sum is exact when the edges' evidence-noise is cross-edge independent, and the deviation under correlated evidence (e.g., one observation informing several edges, or a shared attribution error contaminating a path) is *signed* — a common evidence source overcounts, while structurally anti-correlated evidence errors can make the sum an undercount. The per-edge topology conditions named above are independence assumptions of this kind.

Max attainable: conditional. Currently conditional because the general DAG case (mixed AND/OR topologies, correlated edges) has not been verified.

## Discussion

**Connection to #result-per-dimension-persistence.** The per-edge persistence condition inherits the same structure as the per-dimension epistemic result: the weak edge is the bottleneck. Scalar $\mathcal T_\Sigma$ overestimates effective strategic adaptation for the same reason scalar $\mathcal{T}$ overestimates epistemic adaptation --- it averages over heterogeneous correction capacities. A topology-specific corollary *[Discussion]*: per-edge persistence (every edge calibrated) and plan-level persistence (the plan's value estimate tracks reality) can diverge in a *stationary* environment only at OR-nodes — a starved exploratory arm drifts uncalibrated while the greedy arm carries the plan value — whereas AND-structures cannot exhibit the divergence, since every edge on the conjunctive path enters the plan value and an uncalibrated edge shows up there directly.

**Three-way tradeoff.** Strategic tempo competes with both epistemic tempo and exploitation for the agent's finite action capacity. Each action that tests a strategy edge (improving $\mathcal T_\Sigma$) is an action not spent gathering epistemic information (improving $\mathcal{T}$) or pursuing the current best action (exploitation). The allocation is addressed in #disc-exploit-explore-deliberate — the extended deliberation threshold is derived, but the broader three-way framing is discussion-grade. Deliberation (internal computation) supplements $\mathcal T_\Sigma$ via an internal channel distinct from action-generated evidence.

**Software as Regime A.** In software development, tests are genuine interventions with attributable outcomes ($\iota_{ij} \approx 1$). This makes software agents naturally high-$\mathcal T_\Sigma$ --- a structural advantage identified but not yet formalized in the TST domain ( `02-tst-core/`).

## Working Notes

- **2026-07-16 — OR/AND calibration-vs-performance divergence gloss added to Discussion** (bulk-64 closeout; provenance: `spikes/.integrated/spike-or-node-strategic-dynamics.md` §4, whose substantive results were verified landed — this was its one unlanded discussion-grade observation).
- **2026-07-16 — noise-correlation scope made explicit (ripple from #deriv-tempo-additivity).** The Epistemic Status now names the cross-edge evidence-noise independence condition and its signed deviation. Nothing in the body claimed the overcount-only reading, so no claim was deleted — this closes the "same scope, unaudited" flag from the 2026-07-15 spike.
- **Mixed AND/OR DAGs.** The structural decomposition treats AND-chains and OR-nodes separately. Real strategy DAGs interleave both. How the geometric attenuation (AND) and exploration gating (OR) interact in mixed topologies is unverified. The per-edge persistence condition sidesteps this by treating each edge independently, but the *aggregate* behavior of $\mathcal T_\Sigma$ in mixed DAGs may exhibit interference effects (e.g., evidence starvation in an AND-chain feeding into an OR-node's greedy arm).
- **Optimal topology.** Given a fixed action budget $\nu$, what DAG topology maximizes $\mathcal T_\Sigma$? Shallow OR-heavy structures maximize tempo (more edges are directly observable, no attenuation). Deep AND-chains minimize tempo. This may yield a principled argument for preferring flat, option-rich strategies over deep sequential plans --- complementing the confidence-decay argument in #der-chain-confidence-decay.
- **Dynamic complexity.** As $n_{ij}$ grows (more observations per edge), $\eta_{\text{edge},ij}$ shrinks (diminishing returns). Strategic tempo declines over time even in a static environment --- the agent's corrections become smaller as edges converge. This is the correct qualitative behavior (converged edges need less correction) but means $\mathcal T_\Sigma$ is not a fixed property of the agent-environment pair.
- **Cross-reference to NeurIPS Paper 2.** The strategic-tempo aggregator is **bottleneck-not-sum** in NeurIPS 2026 Paper 2 ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §5 Lemma 4.2 / `#lem-forgetting`): $\mathcal T_\Sigma^{\text{bn,ss}} := \min_{(i,j) \in E} \nu_{ij} \cdot \iota_{ij} \cdot (1 - \lambda_{ij})$. Adversarial disturbance concentrates on the slowest-forgetting / weakest-attribution / slowest-revisited element — the same weakest-link pattern as `#result-per-dimension-persistence` at strategic-tempo level. This segment's $\mathcal T_\Sigma = \sum_{(i,j)} \nu_{ij} \cdot \eta_{\text{edge},ij}$ is the throughput aggregation; the bottleneck form is the persistence-relevant aggregation. The two are compatible: throughput-sum bounds the budget of corrective work the agent can allocate; bottleneck-min bounds the rate at which the worst element survives adversarial concentration. See `spikes/neurips-back-integration-2026-05-08.md` §1 Paper 2 entry 8.

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. *Orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals), staged for an eventual careful promotion pass, kept separate from the certified theory-fix findings. **Coverage for this segment:** 471203, 526815, 584721, 773921, 829314.

#### 1. Candidate Brief prose / pre-prose

- **Endogenous vs. exogenous observation rates — "why learning a strategy is harder than learning a world model."** Independently flagged as the segment's deepest point: epistemic observation rates are *exogenous* (the world happens to you), but strategic edge rates are *endogenous* — you only get to test a downstream edge if you succeed at the upstream ones (Claude/584721, 829314; Codex/526815). One auditor called it "the deepest architectural insight in Part II" and the source of the $M_t$/$\Sigma_t$ persistence differences. Strong candidate Brief framing.
- **"The shape determines the physics of how the plan learns."** A wide/OR-heavy DAG learns its paths in parallel (tempo scales with the exploration budget); a deep/AND-chain has *bounded total tempo* no matter how fast the early steps run. Candidate one-line Brief hook (Gemini/829314).

#### 2. Candidate Discussion

- **Bounded total tempo of deep chains → "waterfall is mathematically dead."** The geometric series $\sum_{k=1}^{d}\theta^{k-1}\to 1/(1-\theta)$ proves a deep AND-chain's *total* learning capacity asymptotically plateaus while the marginal tempo of deep edges decays to zero — "deep plans literally cannot learn fast enough to survive a volatile environment." Worked instance: a 20-step sequential plan starves its late steps of evidence; a startup exploring 5 verticals in parallel calibrates all five (Gemini/829314; Claude/584721, 471203). Candidate Discussion centerpiece.
- **The evolutionary reading.** Instincts are shallow OR-heavy DAGs ("if hot, pull hand away OR yell"); complex human planning is deep AND-heavy and "incredibly fragile, requiring massive cultural scaffolding (forced observability, artificially lowered $\rho$ via institutions) to survive its own mathematical evidence starvation — we build society to lower $\rho$ so our deep AND-chains don't collapse before they finish" (Gemini/829314). Candidate Discussion analogy; isomorphism would need checking before promotion past discussion-grade.
- **Endogenous tempo is *why* "do-what-you-know" organizations fail.** Because edge rates $\nu_{ij}$ are endogenous, an agent that always exploits and never tests alternatives drives $\nu$ on its exploratory edges $\to 0$, so $\mathcal T_\Sigma$ for those edges collapses to the greedy branch only — the agent "starves its strategic learning capacity" and (combining with `#der-causal-insufficiency-detection`) cannot even detect its L0 insufficiency (Claude/451729). Candidate Discussion line tying the endogenous-rate property to a concrete organizational failure.
- **Five converging arguments for shallow plans.** This segment's strategic-tempo bottleneck is the *fifth* independent pressure toward shallow strategy DAGs, joining chain-confidence-decay, evidence-starvation, identifiability-degradation, and cognitive cost. Candidate to surface as a cross-segment structural observation (Claude/584721). *(Same meta-pattern flagged under `#scope-edge-update-causal-validity` as the "quadruple ceiling" — this is the fifth leg; consider a single meta-segment home.)*

#### 3. Follow-up items

- **Dynamic complexity / gain-collapse warning.** $\mathcal T_\Sigma$ declines over time even in a *static* environment because $\eta_{\text{edge}}=1/(n+1)$ shrinks as $n$ grows — so a long-running agent eventually has insufficient strategic-correction capacity for any non-stationarity unless a $\rho$-spike re-inflates $\eta$. Connects to the gain-collapse / stability-induced-myopia / detection-latency-blowup pathology cluster; candidate to develop (Claude/584721; Gemini/829314). Already partly a Working-Notes item.
- **Candidate "tempo-maximizing topology" theorem (off-ramp-adjacent).** One auditor sketched that under a fixed action budget $\nu$ and fixed edge count, the tempo-maximizing topology is the shallowest OR-tree: AND-chain tempo converges to $\nu/((n+1)(1-\theta))$ while flat-OR (full exploration) gives $\nu/(n+1)$, so OR-flat beats an AND-chain for depth $\gt 1/(1-\theta)$ (e.g. depth $\gt 10$ at $\theta=0.9$); the Working-Notes "shallow OR-heavy maximizes tempo" line may be promotable to a derived statement (Claude/451729). *If* this firms up it is a candidate derivation (strengthen-first), not a framing bullet — flagged for the off-ramp.
- *(Codex/526815 F66/F67/F68 route to the off-ramp — see lift report — as candidate findings: the headline defines $\mathcal T_\Sigma$ as a *sum* but the persistence-relevant quantity is the bottleneck/min; "Regime-C edges contribute essentially nothing" overstates — observational evidence still improves *associational* prediction; the $\mathcal T_\Sigma \gt \vert E\vert\rho/R$ necessary bound assumes homogeneous per-edge thresholds and should sum $\sum_e \rho_e/R_e$ in the heterogeneous case.)*

#### 4. Readers often ask / wonder

- **How does the agent allocate a finite action budget across exploit / epistemic-explore / strategic-explore (deliberate)?** Several substrates reached forward to `#disc-exploit-explore-deliberate` for the three-way (or four-way, with "diagnose") allocation rule (Claude/584721, 829314).

#### 5. Candidate figures

- **Throughput-sum vs. bottleneck-min, same edges.** Two simultaneous summaries over the same DAG edges: a throughput *sum* (looks healthy) and a bottleneck *minimum* (the one untested or weakly-identifiable edge that actually fails the per-edge persistence condition). Makes the sum-vs-min distinction visible at a glance (Codex/526815) — pedagogy + the F66 guardrail in one figure.

#### Belongs elsewhere

- *(none surfaced beyond the shared "shallow-plans meta-pattern" pointer noted under Discussion)*
