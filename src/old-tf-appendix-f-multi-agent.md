# Appendix F: Multi-Agent Coupling, Strategic Interaction, and Distributed Adaptation

**Epistemic status**: This appendix is exploratory. The model extension (Section F.1) is a *formulation* — a representational choice extending TFT's single-agent framework. The communication gain (F.2) is a *hypothesis* — an extension of TF-06's uncertainty ratio to social channels that is structurally motivated but not derived. The distributed tempo and persistence conditions (F.3) are *derived* from the model extension, conditional on the communication gain hypothesis. The topology analysis (F.4) and game-theoretic integration (F.5) are *discussion* — qualitative consequences and connection points with existing theory, not formal results. Throughout, the single-agent TFT results are assumed; this appendix adds a coupling layer.

## Motivation

TFT's core theory treats a single agent coupled to an environment. But many of the most important adaptive systems involve *multiple* agents whose feedback loops interact: organizations, teams, adversarial competitors, multi-agent AI systems, immune networks, scientific communities, ecosystems. TF-08 and TF-11 already address the two-agent adversarial case. This appendix extends the framework to $N$ agents with cooperative, adversarial, and mixed coupling.

The extension principle: **each agent runs a local TFT loop; inter-agent interaction enters as additional observation and disturbance channels.** This preserves all single-agent results and adds a coupling layer.

---

## F.1 Model Extension: $N$ Coupled TFT Loops

### Local State

For agents $i = 1, \ldots, N$, each maintains its own TFT state:

- $M_i$: local model (TF-03)
- $\delta_i$: local mismatch (TF-05)
- $\eta_i^*$, $\mathcal{T}_i$, $\alpha_i$, $R_i$: local gain, tempo, sector bound, model class capacity (TF-06, TF-11, App. A)

### Coupled Update

*[Formulation (multi-agent-update)]*
$$M_i^+ = M_i^- + \eta_i \, g_i(\delta_i) + \sum_{j \in \mathcal{N}(i)} w_{ji} \, \eta_{ji} \, h_{ji}(M_j^-, M_i^-)$$

where:
- **First term**: standard self-update from direct observation (single-agent TFT, unchanged).
- **Second term**: model transfer from neighbors $\mathcal{N}(i)$ — a weighted sum of corrections based on model differences.
- $w_{ji} \in [0, 1]$: trust weight that agent $i$ assigns to agent $j$.
- $\eta_{ji}$: communication-channel gain (how much $i$ updates from $j$'s signal; defined in F.2).
- $h_{ji}(M_j^-, M_i^-)$: the communication transform — maps the difference (or message) between $j$'s model and $i$'s model into an update direction for $i$. This is the social analog of TF-06's mismatch transform $g$.

**What counts as "communication."** The second term is general: it covers explicit message exchange (language, data transfer), observation of another agent's actions (social learning, imitation), access to another agent's outputs (ensemble aggregation, consulting an expert), and even indirect signals (market prices, published results). In each case, agent $j$'s model has already compressed information about the shared environment; the communication channel transfers some of that compression to $i$.

**Relation to query actions (TF-08).** Query actions are the *mechanism* by which the communication term is activated: agent $i$ chooses to ask, observe, or consult agent $j$. The CIY of a query action now depends on the communication gain $\eta_{ji}$ and the expected model difference $h_{ji}$. High-CIY queries target agents whose models are likely to differ informatively from the querying agent's own model.

## F.2 Communication Gain

The optimal gain for incorporating agent $j$'s signal extends TF-06's uncertainty ratio:

*[Hypothesis (communication-gain)]*
$$\eta_{ji}^* = \frac{U_{M_i}}{U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji}}$$

where:
- $U_{M_i}$: agent $i$'s model uncertainty (same as TF-06)
- $U_{o,ji}$: **communication channel noise** — latency, ambiguity, compression loss, bandwidth limitations of the channel between $j$ and $i$
- $U_{\text{src},j}$: **source quality uncertainty** — $i$'s uncertainty about $j$'s model calibration and domain competence. Low when $j$ has demonstrated reliable predictions; high when $j$'s track record is unknown or poor
- $U_{\text{align},ji}$: **alignment uncertainty** — $i$'s uncertainty about whether $j$'s communications are optimized to improve $i$'s model or to serve $j$'s potentially conflicting objectives. Zero for fully aligned teammates; high for competitors or unknown agents; potentially very high for adversaries

**Normalization requirement.** All four uncertainty terms must be expressed in a **common predictive-dispersion scale** before summation — the same units as $U_{M_i}$ (variance of the predictive distribution over the observed quantity; see TF-06). In practice: $U_{o,ji}$ is the variance of the channel noise added to $j$'s signal; $U_{\text{src},j}$ is the expected additional prediction variance attributable to $j$'s model miscalibration; $U_{\text{align},ji}$ is the expected additional prediction variance attributable to strategic distortion. When these are hard to estimate directly, a conservative approximation is to set $U_{\text{src}} + U_{\text{align}}$ to the empirical variance of $j$'s past prediction residuals as observed by $i$, minus the known channel noise $U_{o,ji}$.

**Additivity as heuristic.** The additive denominator treats all uncertainty sources as independent, zero-mean noise — a structural heuristic, not a strict variance derivation. This is appropriate for $U_{o,ji}$ (channel noise) and $U_{\text{src},j}$ (miscalibration), which are typically unstructured. For $U_{\text{align},ji}$ (deception), additivity is conservative: it correctly drives $\eta_{ji}^*$ toward zero when alignment uncertainty is high. But it misses the adversary's *actual* strategy, which is to make $U_{\text{align},ji}$ *appear* low — presenting as a trustworthy source so that $i$ assigns high $\eta_{ji}^*$ to a poisoned signal. The additive model captures the *defender's* response to detected misalignment; it does not model the *attacker's* optimization over the defender's trust dynamics. See F.5 for where game theory enters.

### Interpretation

When all additional uncertainty terms are zero (perfect channel, perfectly calibrated and fully aligned source): $\eta_{ji}^* \to U_{M_i}/(U_{M_i} + 0) = 1$. Agent $i$ trusts $j$ completely and updates fully.

When any term is large (noisy channel, unreliable or misaligned source): $\eta_{ji}^* \to 0$. Agent $i$ effectively ignores $j$'s signal.

The denominator sums are *not* all equivalent in nature:
- $U_{o,ji}$ is a property of the *channel* — potentially improvable by infrastructure
- $U_{\text{src},j}$ is a property of the *source* — improvable by $j$ improving its own model, or estimable by $i$ through calibration tracking
- $U_{\text{align},ji}$ is a property of the *relationship* — the game-theoretic variable (F.5)

### Connection to Existing TFT

When $j$ is the environment itself (direct observation): the communication gain reduces to TF-06's standard gain $\eta_i^* = U_{M_i}/(U_{M_i} + U_{o_i})$, with $U_{\text{src}} = U_{\text{align}} = 0$ (the environment is neither calibrated nor strategic).

When $j$ is an adversary engaged in deception (TF-08): $U_{\text{align},ji}$ is high, driving $\eta_{ji}^*$ toward zero if $i$ correctly estimates $j$'s adversarial intent. The adversary's strategy is to make $U_{\text{align},ji}$ *appear* low (feigning alignment) so that $i$ assigns high $\eta_{ji}^*$ to deceptive signals. This is precisely the trust-exploitation dynamic described in TF-08's adversarial mirror section.

### Trust Calibration as a Meta-Model

Agent $i$'s estimates of $U_{\text{src},j}$ and $U_{\text{align},ji}$ constitute a **trust meta-model** — a model of models. This meta-model is itself subject to TFT's full apparatus: it has mismatch (trust prediction errors), should be updated with appropriate gain (not overreacting to single instances of disagreement), and can be structurally inadequate (the agent's trust model class may not capture the actual reliability structure of its sources).

A minimal Bayesian trust update: track per-source calibration by comparing $j$'s past communications to subsequent ground truth. Use the residual statistics to update $U_{\text{src},j}$ and, where detectable, $U_{\text{align},ji}$. This is a concrete instance of TF-10's structural adaptation applied to the trust meta-model.

### Trust Transitivity

When agent $i$ has no direct experience with agent $k$, but intermediary $j$ (whom $i$ does trust) provides an assessment of $k$, the transitive trust question is: what should $i$'s initial trust in $k$ be?

**Bayesian transitive prior.** Model $j$'s recommendation as a mixture signal:

*[Hypothesis (transitive-trust)]*
$$P_i(\theta_k \mid s_j) \propto \left[r_{ji} \cdot P(s_j \mid \theta_k) + (1 - r_{ji}) \cdot P_0(s_j)\right] \cdot P_i(\theta_k)$$

where $\theta_k \in [0, 1]$ represents $k$'s true alignment (probability of honest, calibrated communication), $s_j$ is $j$'s assessment of $k$, and $r_{ji}$ is $i$'s reliability estimate of $j$. With probability $r_{ji}$, the signal is informative (drawn from the true likelihood $P(s_j \mid \theta_k)$); with probability $1 - r_{ji}$, it is uninformative (drawn from a null distribution $P_0$). This naturally discounts the transitive recommendation by the intermediary's own reliability: when $r_{ji} \to 0$, the posterior collapses to the prior (no update); when $r_{ji} \to 1$, the full informative likelihood applies.

**Three-phase trust formation:**
1. *Prior*: $P_i(\theta_k)$ — default trust for unknown agents (could be context-dependent: higher in a cooperative team, lower in an adversarial environment).
2. *Transitive update*: Incorporate $j$'s recommendation via the mixture likelihood above. Multiple intermediaries contribute additively (each with their own $r_{ji}$), and corroborating signals concentrate the posterior faster.
3. *Direct experience*: As $i$ interacts with $k$ directly, each interaction provides a ground-truth observation that updates the posterior normally. After sufficient direct experience, the intermediary-derived prior is swamped.

**Risk-asymmetric trust (HILP/LIHP).** The Bayesian posterior gives the best *estimate* of $\theta_k$. But the *decision* about how much to trust $k$ should be risk-weighted:

- **HILP** (High Impact, Low Probability): Trusting a deceptive agent can cause catastrophic model corruption (Corollary A.3.1's effects spiral), possibly irreversible. The cost of misplaced trust in this regime is disproportionately large.
- **LIHP** (Low Impact, High Probability): Mild miscalibration of trust toward a reliable source causes small ongoing inefficiency — slightly suboptimal gain, minor tempo loss.

The risk-adjusted communication gain replaces the posterior *mean* of $\theta_k$ with a **conservative quantile**:

*[Discussion (risk-adjusted-trust)]*
$$U_{\text{align},ki}^{\text{eff}} = U_{\text{align},ki}^{\text{Bayes}} \cdot \frac{1}{Q_p[\theta_k]}$$

where $Q_p[\theta_k]$ is the $p$-th quantile of the trust posterior (e.g., $p = 0.05$ for a 95%-conservative estimate). When the posterior is concentrated (much direct evidence), $Q_p \approx \mathbb{E}[\theta_k]$ and the risk adjustment is negligible. When the posterior is diffuse (little evidence, relying on transitive trust), $Q_p \ll \mathbb{E}[\theta_k]$ and the effective alignment uncertainty is inflated — requiring *more evidence before granting high trust*.

The severity of the quantile $p$ should scale with the stakes: routine interactions use $p$ near 0.5 (posterior mean, minimal conservatism); high-impact interactions use $p$ near 0.05 or lower. This is equivalent to requiring that the trust posterior concentrate more before allowing high $\eta_{ki}^*$ in high-stakes settings.

**Connection to TF-06 gain dynamics.** This risk adjustment is the trust analog of TF-06's observation that an agent with high $U_M$ (uncertain model) should use a high $\eta^*$ (trust new observations), while an agent with low $U_M$ (confident model) should use a low $\eta^*$ (trust the model). The risk-adjusted trust inverts this for the *alignment* dimension: when stakes are high, treat all transitively-derived trust as carrying higher effective uncertainty, and require more direct evidence before converging.

## F.3 Distributed Tempo and Team Persistence

### Distributed Adaptive Tempo

Agent $i$'s effective tempo now includes contributions from both direct observation and communication:

*[Definition (distributed-tempo)]*
$$\mathcal{T}_i = \underbrace{\sum_k \nu_i^{(k)} \eta_i^{(k)*}}_{\text{direct observation tempo}} + \underbrace{\sum_{j \in \mathcal{N}(i)} \nu_{ji}^{\text{comm}} \, \eta_{ji}^*}_{\text{communication tempo}}$$

where $\nu_{ji}^{\text{comm}}$ is the rate of communication events from $j$ to $i$. Faster team adaptation comes not only from faster individual sensing/action but from faster, more reliable knowledge transfer.

### Cooperative-Adversarial Disturbance Decomposition

The effective disturbance rate for agent $i$ decomposes into environment, adversarial, and cooperative components:

*[Formulation (disturbance-decomposition)]*
$$\rho_i = \rho_{i,\text{env}} + \sum_{j \in \mathcal{A}_i} \gamma_{j \to i}^{\text{adv}} \, \mathcal{T}_j - \sum_{j \in \mathcal{C}_i} \gamma_{j \to i}^{\text{coop}} \, \mathcal{T}_j$$

where $\mathcal{A}_i$ is the set of agents adversarially coupled to $i$, $\mathcal{C}_i$ is the set cooperatively coupled, and the $\gamma$ coefficients capture coupling effectiveness (as in TF-11 and Appendix A).

**The cooperative term is negative.** Allies *reduce* agent $i$'s effective disturbance by sharing information that preemptively corrects mismatch. This is the formal content of why teams can persist in environments where individuals cannot: the cooperative communication tempo offsets environment disturbance that would exceed any single agent's capacity.

**Sign convention.** The decomposition above can yield $\rho_i < 0$ when cooperative coupling dominates both environment disturbance and adversarial coupling. Appendix A's sector-condition analysis (Propositions A.1–A.3) assumes $\rho \geq 0$ (non-negative disturbance bound). For the persistence condition, define the **effective disturbance rate**:

*[Definition (effective-disturbance)]*
$$\rho_i^{\text{eff}} = \max(\rho_i, \, 0)$$

When $\rho_i^{\text{eff}} = 0$, the agent's cooperative network fully absorbs all disturbance — the persistence condition is trivially satisfied and mismatch decays to zero. This is the idealized limit; in practice, $\rho_i^{\text{eff}} > 0$ because cooperative coupling is imperfect and environment disturbance is never fully preempted. All downstream uses of $\rho_i$ in the persistence and reserve conditions should be read as $\rho_i^{\text{eff}}$.

### Team Persistence Condition

Applying Appendix A's sector-condition framework with $\rho_i^{\text{eff}}$, agent $i$ persists iff:

*[Derived (team-persistence)]*
$$\frac{\rho_i^{\text{eff}}}{\alpha_i} < R_i$$

Substituting the decomposition (the $\max(\cdot, 0)$ in $\rho_i^{\text{eff}}$ is omitted here to expose the three levers; the condition is trivially satisfied when the numerator is non-positive):

$$\frac{\rho_{i,\text{env}} + \sum_j \gamma_{j \to i}^{\text{adv}} \mathcal{T}_j - \sum_j \gamma_{j \to i}^{\text{coop}} \mathcal{T}_j}{\alpha_i} < R_i$$

This reveals three distinct levers for team persistence:
1. **Increase $\alpha_i$** (individual correction efficiency) — better models, better gain calibration
2. **Increase cooperative tempo** ($\gamma^{\text{coop}} \mathcal{T}_j$) — more reliable allies, faster communication
3. **Reduce adversarial coupling** ($\gamma^{\text{adv}} \mathcal{T}_j$) — better deception detection, reduced exposure

### Coordination Overhead

Communication channels have costs: time to compose/parse messages, bandwidth limitations, synchronization requirements, meeting overhead. These costs reduce the agent's effective tempo by diverting time and compute from direct adaptation. Let $\Delta \mathcal{T}_i^{\text{cost}}(j)$ represent the **tempo-equivalent coordination cost** of maintaining the communication channel with $j$ — the reduction in $i$'s direct observation tempo caused by the overhead, in units of $[t^{-1}]$.

The net benefit of adding agent $j$ to $i$'s communication network is positive only when the communication tempo gained exceeds the direct-adaptation tempo lost:

*[Discussion — Coordination Threshold]*
$$\nu_{ji}^{\text{comm}} \, \eta_{ji}^* > \Delta \mathcal{T}_i^{\text{cost}}(j)$$

Both sides have units $[t^{-1}]$: the LHS is communication tempo gained, the RHS is direct-adaptation tempo lost to coordination overhead. This implies a natural team-size limit: adding members increases communication tempo with diminishing returns (as $U_{\text{src}}$ and $U_{o}$ accumulate across diverse sources) while coordination costs grow, potentially superlinearly. The optimal team size occurs where the marginal communication tempo equals the marginal coordination cost.

## F.4 Topology-Dependent Analysis

The multi-agent framework instantiates differently depending on the coupling structure.

### Collaborative Peer Network

Agents with roughly equal capability and aligned objectives share information to reduce collective mismatch.

- **Update structure**: Weighted consensus or diffusion — each agent moves its model toward a trust-weighted average of neighbors' models, while also updating from its own observations.
- **Key metric**: *Disagreement energy* — $\sum_{(i,j)} w_{ij} \| M_i - M_j \|^2$. High disagreement with low external mismatch often indicates miscalibrated trust (one agent is right, the other hasn't updated), not model inadequacy. Low disagreement with high mismatch indicates the team is wrong together — a shared structural limitation (TF-10).
- **Failure mode**: *Groupthink* — the network converges on a shared model that is confidently wrong, because internal consensus suppresses the mismatch signals from dissenting agents. In TFT terms: $U_{\text{src},j} \to 0$ for all in-group sources (excessive trust), while $\eta_i^*$ for direct observations is depressed by the confidence of the group model. The remedy is to maintain sensitivity to direct-observation mismatch even when the group is confident — i.e., to never let communication tempo fully substitute for observation tempo.

### Ensemble (Parallel Specialists + Aggregator)

Multiple agents maintain domain-specific models; an aggregator combines them.

- **Update structure**: The aggregator's policy weights experts by their uncertainty *and* historical calibration, not confidence alone. An expert that is confident and wrong should be downweighted; one that is uncertain but well-calibrated should be upweighted.
- **Exploration policy**: The aggregator should allocate queries (attention, resources) to experts whose models are most uncertain about the current situation — the CIY-maximizing strategy at the aggregation level.
- **Structural adaptation trigger**: If all experts fail similarly (correlated residuals), the model class needs expansion — the ensemble's diversity is insufficient. If only some fail, re-route or recalibrate rather than restructure.

### Hierarchical (Strategic → Tactical → Execution)

Agents at different timescales coupled vertically, mapping TF-11's temporal nesting to organizational structure.

- **Update structure**: Upper layers receive *summaries* (quasi-steady-state output) from lower layers and issue *directives* (hyperparameter updates: goals, constraints, priors), not high-frequency control commands.
- **Key constraint**: TF-11's convergence condition ($\nu_{n+1} \ll \nu_n$) applies between organizational levels. When upper-layer intervention frequency approaches lower-layer correction timescale, the result is *command-induced oscillation* — the organizational analog of control-theoretic instability from gain mismatch. This is the formal content of "micromanagement degrades performance."
- **Information asymmetry**: Upper layers have broader context but lower resolution; lower layers have higher resolution but narrower scope. The communication gain $\eta_{ji}^*$ should reflect this: upward communication compresses local detail into aggregate summaries ($U_{o,ji}$ high from compression), while downward communication translates broad directives into local constraints ($U_{\text{align},ji}$ encodes the mapping quality from strategic objectives to tactical actions).

## F.5 Game-Theoretic Integration Points

TFT provides the state variables (mismatch, gain, tempo, reserve) and dynamics (the correction loop). Game theory provides the *strategic analysis*: when agents choose their coupling parameters ($w_{ji}$, $\gamma$, communication content) to optimize their own objectives, what equilibria arise?

### Where Game Theory Is Needed

TFT alone cannot answer:
1. **When is honest communication incentive-compatible?** — Under what conditions does agent $j$ prefer to send signals that reduce $i$'s mismatch rather than increase it? The cheap-talk and signaling-game literature addresses this.
2. **What trust levels are equilibrium?** — In repeated interaction, what $U_{\text{align},ji}$ values are self-consistent? Reputation games and mechanism design provide tools.
3. **How do adversaries optimally allocate disruption?** — An adversary facing multiple targets must choose how to distribute its tempo across opponents. This is a resource-allocation game.

### Decision-Theoretic Integration

Within each agent's loop, decision theory refines the policy:

1. **$\lambda$ as value-of-information price (TF-08).** The exploration weight $\lambda(M_t)$ in the unified policy objective is a decision-theoretic quantity: it prices the expected future value of information against the expected immediate value of exploitation. In environments with known dynamics, $\lambda$ is derivable (Gittins index, information-directed sampling). In general, it is a design parameter whose setting reflects the agent's time horizon and risk preference.

2. **Deliberation stopping (TF-09).** Proposition 9.1's threshold is an optimal-stopping criterion: continue deliberating iff the marginal gain exceeds the marginal cost. This is a classic metareasoning problem from bounded rationality. The extension to multi-agent settings adds a dimension: deliberation may include consulting other agents, whose response time enters the deliberation cost.

3. **Structural adaptation as switching under costs (TF-10).** The decision to change model class is a sequential hypothesis test with switching cost. Decision theory gives the optimal switching rule: change when the expected future mismatch reduction from the new model class exceeds the transition cost (knowledge loss, temporary performance drop, coordination cost). In multi-agent settings, structural change may require *coordinated* switching — adding a consensus or signaling requirement.

### What TFT Contributes to Game Theory

TFT's value for game-theoretic analysis is providing precise, measurable state variables for strategic interaction:

- **Tempo as a strategic resource**: $\mathcal{T}$ is the asset agents compete over or cooperate to increase.
- **Reserve as vulnerability**: $\Delta\rho^*$ is the target adversaries aim to exhaust and allies aim to preserve.
- **Mismatch as the battlefield**: $\|\delta\|$ is what adversaries try to increase in opponents and reduce in themselves.
- **Trust calibration as the meta-game**: the accuracy of $U_{\text{align},ji}$ estimates determines whether the agent can correctly price communication signals.

This gives game theory concrete operands rather than abstract "utilities" — the payoff structure is grounded in measurable adaptive quantities.

## F.6 Operational Quantities

For implementing multi-agent TFT, the following quantities should be tracked per source $j$ as estimated by agent $i$:

| Symbol | Meaning | Estimation |
|--------|---------|------------|
| $r_{ji}$ | Reliability calibration of source $j$ | Running Brier/log-loss score against subsequent ground truth |
| $d_{ji}$ | Communication delay | Direct measurement of message latency |
| $A_{ji}$ | Alignment score | Inferred from agreement on verifiable predictions; domain-specific |
| $\Delta\mathcal{T}_i^{\text{cost}}$ | Tempo-equivalent coordination cost | Direct-adaptation tempo lost to communication overhead $[t^{-1}]$ |
| $V_{\text{disagree}}$ | Network disagreement energy | $\sum_{(i,j)} w_{ij} \|M_i - M_j\|^2$; high with low mismatch → trust miscalibration |

### Practical Control Rules

- High-stakes updates from low-reliability sources should require **cross-source agreement** (quorum) before integration.
- Track per-source calibration over time; auto-adjust $w_{ji}$ based on verified prediction accuracy.
- Separate **query actions for information** from **actions on the world** in policy logs — these have different CIY structures and different cost profiles.
- Trigger structural adaptation only when residual mismatch patterns persist after: (a) trust recalibration, (b) routing changes, (c) communication-channel upgrades.

## F.7 Falsification Predictions

If the multi-agent extension's core claims are wrong, the following observable failures should occur. These are testable in multi-agent simulations (distributed estimation, multi-agent RL, adversarial games) and, with instrumentation, in organizational and team settings.

1. **Adaptive communication gain outperforms fixed trust.** The communication gain hypothesis (F.2) predicts that $\eta_{ji}^* = U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$ should yield lower steady-state mismatch than any fixed trust weight $w_{ji}$ when source reliability varies over time or across contexts. **Falsified if**: in a multi-agent estimation task with heterogeneous and time-varying source reliability, a well-tuned *fixed* trust weight consistently matches or outperforms the adaptive communication gain across a range of drift rates and source-failure scenarios. This would indicate that the additional uncertainty terms ($U_{\text{src}}$, $U_{\text{align}}$) either don't carry usable information or that the overhead of estimating them exceeds their value.

2. **Cooperative communication enables persistence beyond individual capacity.** The team persistence condition (F.3) predicts that agents with $\mathcal{T}_i < \rho_i / R_i$ individually (insufficient solo tempo) can persist when cooperative communication provides enough distributed tempo to close the gap. Specifically: adding a reliable ally with tempo $\mathcal{T}_j$ and cooperative coupling $\gamma_{j \to i}^{\text{coop}}$ should reduce $i$'s effective $\rho_i$ by $\gamma_{j \to i}^{\text{coop}} \mathcal{T}_j$, bringing the persistence condition into range. **Falsified if**: in a controlled setting, adding cooperative communication channels with measured $\gamma^{\text{coop}}$ and $\mathcal{T}_j$ does *not* reduce $i$'s steady-state mismatch by the predicted amount. This would indicate the cooperative $\rho$ decomposition is structurally wrong — cooperation helps through a mechanism not captured by the additive disturbance model.

3. **Risk-adjusted transitive trust outperforms Bayesian mean trust under adversarial contamination.** The HILP/LIHP trust adjustment (F.2) predicts that using a conservative quantile $Q_p[\theta_k]$ rather than the posterior mean $\mathbb{E}[\theta_k]$ for setting $U_{\text{align}}$ should yield better *worst-case* mismatch in environments with occasional deceptive sources, at the cost of slightly worse *average-case* efficiency. **Falsified if**: in a multi-agent setting with a known fraction of adversarial sources, conservative-quantile trust does not improve worst-case mismatch relative to mean trust, or if the average-case efficiency cost is so large that total mismatch is higher. This would indicate that the risk-asymmetric adjustment overcorrects — that the HILP tail risk is already adequately handled by the Bayesian posterior without additional conservatism.

These predictions target the extension's three main hypotheses (communication gain structure, cooperative persistence, risk-adjusted trust). Failures in (1) or (2) would undermine the core multi-agent framework; failure in (3) would indicate the trust transitivity mechanism needs refinement while leaving the broader structure intact.

## F.8 Open Questions

1. **Emergence.** When does the network exhibit qualitatively different adaptive behavior than any individual agent? TFT gives a partial answer: when the network's effective distributed tempo exceeds any individual's, the network can persist in environments where no individual can. But "emergence" in the richer sense — novel model classes or capabilities arising from interaction that no individual agent could discover alone — requires a theory of network-level structural adaptation (TF-10 at the collective level). This is beyond TFT's current scope.

2. **Convergence in consensus dynamics.** The peer-network update rule (F.1's second term) defines a dynamical system over model states. Under what conditions does this converge? Standard consensus theory gives conditions for convergence of scalar averages; convergence of structured models (posterior distributions, value functions, neural network weights) is a harder problem.

3. **Adversarial equilibria.** In the two-agent case (TF-11, Appendix A), the adversarial outcome is determined by tempo ratios and reserves. In $N$-agent networks, coalition formation, asymmetric information, and multi-front competition create richer dynamics. Mapping TFT's framework onto $N$-player game solutions is a substantial extension.

4. **Trust transitivity — remaining questions.** The three-phase model in F.2 (prior → transitive update → direct experience) with risk-asymmetric quantile adjustment provides a starting framework. Open questions remain: (a) How should the null distribution $P_0$ be chosen? A uniform $P_0$ makes the mixture model equivalent to soft discounting; a structured $P_0$ (e.g., biased toward deception) models actively adversarial intermediaries. (b) How should the risk quantile $p$ be calibrated? Ideally from the loss function, but the loss from deception may be hard to estimate *before* it occurs. (c) When multiple intermediaries provide corroborating recommendations, how should correlation be handled? If $j_1$ and $j_2$ both recommend $k$ but both got their information from the same source, the corroboration is illusory. The trust network's dependency structure matters.

5. **Communication as structural adaptation.** A well-formed query to an expert can transfer not just parametric information (reducing $\|\delta\|$) but *structural* information (expanding $\mathcal{M}$). This is the "grafting" mechanism from TF-10: incorporating another agent's representational structure. A theory of *when and how* communication triggers structural vs. parametric adaptation in the receiver is needed.

---

## Summary

| Concept | Single-agent TFT | Multi-agent extension |
|---------|------------------|----------------------|
| Update | $M^+ = M^- + \eta \, g(\delta)$ | + communication term $\sum_j w_{ji} \eta_{ji} h_{ji}(M_j, M_i)$ |
| Gain | $\eta^* = U_M/(U_M + U_o)$ | $\eta_{ji}^* = U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$ |
| Tempo | $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)*}$ | + $\sum_j \nu_{ji}^{\text{comm}} \eta_{ji}^*$ (communication channels) |
| Disturbance | $\rho$ (exogenous or adversarial) | $\rho_i = \rho_{\text{env}} + \gamma^{\text{adv}} \mathcal{T}_j - \gamma^{\text{coop}} \mathcal{T}_j$ |
| Persistence | $\alpha > \rho / R$ | Same, with cooperative $\rho$ reduction |
| New quantities | — | $U_{\text{src}}$, $U_{\text{align}}$, $C^{\text{coord}}$, $V_{\text{disagree}}$ |
