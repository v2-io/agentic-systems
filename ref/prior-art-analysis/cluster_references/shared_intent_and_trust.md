# Cluster Reference: Shared Intent, Trust, and Bandwidth

**Overview:** Frames communication as the Information Bottleneck compression of purpose, deriving Auftragstaktik bandwidth priorities and trust-weighted update gains to avoid catastrophic effects spirals.

---

## Canonical Source Segments

### Source: `def-shared-intent.md`

```yaml
---
slug: def-shared-intent
type: definition
status: discussion-grade
depends:
  - def-unity-dimensions
  - form-information-bottleneck
  - form-objective-functional
stage: draft
---
```


# Definition: Shared Intent

When sub-agents within a composite must coordinate, they face a communication problem: transmitting the full objective $O_t$ and strategy $\Sigma_t$ is expensive (high bandwidth, high latency), but acting without any shared purpose wastes coordination potential. The Information Bottleneck ( #form-information-bottleneck) applied to inter-agent communication predicts an optimal compression: transmit enough of $G_t$ to align behavior, not more.

## Formal Expression

*[Definition (shared-intent)]*

Let $G_t^{\text{full}}$ be the source agent's complete purposeful state $(O_t, \Sigma_t)$. Let $G_t^{\text{shared}}$ be the compressed representation communicated to partners. The shared intent is the IB-optimal compression:

$$G_t^{\text{shared}} = \arg\min_{G_s} \left[ I(G_t^{\text{full}}; G_s) - \beta \cdot I(G_s; a_t^{\text{coordinated}}) \right]$$

where $a_t^{\text{coordinated}}$ is the jointly optimal action and $\beta$ controls the complexity-relevance tradeoff. At high $\beta$, the agent communicates more detail (approaching full model sharing). At low $\beta$, communication is minimal (approaching independent action).

The shared intent is the *minimal sufficient statistic* of the sender's purposeful state for predicting the jointly optimal coordination behavior.

## Epistemic Status

*Discussion-grade.* Max attainable: conditional (conditional on the IB framework being appropriate for inter-agent communication). The application of IB to inter-agent communication is structurally motivated — IB compresses optimally given a relevance criterion, and coordination relevance is the natural criterion — but the specific formulation assumes: (1) the sender knows the jointly optimal action (which requires knowing other agents' states), (2) the compression is lossless in the IB sense (real communication introduces noise, delay, and misinterpretation), (3) the $\beta$ parameter is fixed rather than dynamically adjusted. These are strong assumptions. The qualitative prediction (communicate purpose before plans before models) is more robust than the specific IB formulation.

## Discussion

**What gets compressed out.** The IB compression preferentially preserves:
1. Terminal objectives (what the agent is trying to achieve) — these are compact and change slowly
2. High-level strategy (which approach, not which specific steps) — moderate size, moderate change rate
3. Strategic details (specific edge credences in $\Sigma_t$) — large, change fast, low coordination value

**Connection to cognitive cost of $\Sigma_t$.** For agents with bounded communication capacity (bandwidth-limited channels, finite context windows), the DAG must be summarized for transmission. A 500-node strategy DAG cannot be shared in full; the IB compression identifies which structural features of the DAG matter for coordination.

**Organizational communication patterns.** Commander's intent in military doctrine is an empirical instantiation: the commander communicates *what* to achieve and *why*, not *how*. This is IB-optimal if objectives change slowly (low $\nu_O$) and strategies change fast (high $\nu_\Sigma$) — communicating objectives gives a long shelf life per bit transmitted.

## Working Notes
- The IB formulation assumes a single relevance variable ($a_t^{\text{coordinated}}$). In practice, coordination relevance is multi-dimensional: shared intent needs to support action coordination, conflict resolution, resource allocation, and adaptive replanning. A richer relevance variable might be needed.
- How does shared intent interact with 100% context turnover? An AI agent starting a new session needs to reconstruct $G_t^{\text{shared}}$ from persistent storage. The compression from full $G_t$ to shared intent is also useful for $M_t$ preservation ( #disc-m-preservation) — store the compressed version, not the full state.


---

### Source: `hyp-auftragstaktik-principle.md`

```yaml
---
slug: hyp-auftragstaktik-principle
type: hypothesis
status: discussion-grade
depends:
  - def-shared-intent
  - def-unity-dimensions
  - def-adaptive-tempo
stage: draft
---
```


# Hypothesis: Auftragstaktik Principle

For a composite agent with limited communication bandwidth, the optimal allocation prioritizes sharing objectives over strategies over models. This captures the structural insight of Auftragstaktik (mission-type tactics): investing communication bandwidth in shared purpose (teleological unity) while accepting lower epistemic and strategic unity, granting sub-agents autonomy to adapt locally. The model predicts the same priority ordering that military doctrine discovered empirically; whether the mechanism (IB-optimal bandwidth allocation) is the actual reason Auftragstaktik works is an open question.

## Formal Expression

*[Hypothesis (auftragstaktik-principle)]*

Let a composite agent's total inter-agent communication bandwidth be $B = B_O + B_\Sigma + B_M$, allocated across objective sharing ($B_O$), strategy coordination ($B_\Sigma$), and model synchronization ($B_M$).

The hypothesis: the allocation that maximizes composite tempo $\mathcal{T}_c$ (or equivalently, minimizes coordination overhead $C_{\text{coord}}$) prioritizes:

$$B_O \gt B_\Sigma \gt B_M$$

when:
- Objectives change slowly relative to strategies: $\nu_O \ll \nu_\Sigma$
- Strategies change slowly relative to models: $\nu_\Sigma \ll \nu_M$
- Sub-agents have sufficient local adaptive capacity: each $\mathcal{T}_i \gt \rho_i^{\text{local}} / \Vert\delta_{\text{critical}}^i\Vert$

The priority ordering follows from the IB framework ( #def-shared-intent): the bits with the longest shelf life and highest coordination value per bit should be transmitted first. Objectives change slowly and enable autonomous coordination (sub-agents who share objectives can independently choose compatible strategies). Models change fast and provide diminishing coordination value (two agents with the same model but different objectives still conflict).

## Epistemic Status

*Discussion-grade.* Max attainable: empirical. The priority ordering is a qualitative prediction grounded in the IB framework and supported by extensive military-organizational evidence (Bungay's analysis of Clausewitz, Wehrmacht doctrine, modern mission command). But it is not derived — the IB optimization would need to be solved explicitly with realistic cost functions to confirm the ordering, and the conditions under which the ordering reverses (e.g., when model synchronization is critical because the situation is genuinely ambiguous) are not characterized. The empirical evidence is strong but comes primarily from one domain (military command); generalization to software teams, AI agent swarms, and other settings is plausible but unverified.

## Discussion

**When the ordering reverses.** The prioritization $B_O \gt B_\Sigma \gt B_M$ assumes sub-agents can independently construct adequate local models. When the environment is genuinely ambiguous and local observations are insufficient (fog of war, novel codebase, unprecedented market conditions), model synchronization may be worth more than objective sharing — sub-agents who share the same wrong model at least err consistently, which is sometimes better than each having a different wrong model.

**Bungay's evidence.** In *The Art of Action*, Bungay documents that organizations consistently fail by inverting this priority: they over-invest in controlling *how* subordinates act (strategy sharing, $B_\Sigma$) rather than ensuring subordinates understand *why* (objective sharing, $B_O$). The result: subordinates who follow instructions precisely but cannot adapt when conditions change, because they lack the teleological context to improvise intelligently.

**The software team instantiation.** A well-functioning development team has:
- High $B_O$: clear product goals, understood by all (sprint goals, feature objectives)
- Moderate $B_\Sigma$: architectural decisions shared, implementation details autonomous
- Low $B_M$: each developer builds their own mental model of the code they touch; full codebase understanding is neither expected nor efficient

When this inverts (micromanagement of implementation details, unclear product goals), team tempo drops — consistent with the Auftragstaktik prediction.

**Connection to Conway's Law.** Conway's Law (system structure mirrors communication structure) is a consequence: when $B_\Sigma$ is low and $B_O$ is high, sub-agents coordinate through shared objectives rather than explicit action coordination, producing systems whose boundaries reflect objective decomposition rather than communication channels.

## Working Notes
- The formal IB derivation of the priority ordering would need: (1) a model of how each unity dimension contributes to composite tempo, (2) the rate of change of each shared quantity ($\nu_O$, $\nu_\Sigma$, $\nu_M$), (3) the communication cost per bit for each type. The qualitative argument is that objectives are compact and slow-changing (high bits-per-cost, long shelf life), while models are large and fast-changing (low bits-per-cost, short shelf life). Formalizing this is tractable but has not been done.
- The principle may need qualification for AI agent teams where model synchronization is cheap (shared vector databases, persistent memory) but objective alignment is hard (prompt engineering, RLHF). The cost structure differs from human organizations.


---

### Source: `hyp-communication-gain.md`

```yaml
---
slug: hyp-communication-gain
type: hypothesis
status: discussion-grade
depends:
  - emp-update-gain
  - scope-multi-agent
stage: draft
---
```


# Hypothesis: Communication Gain

When an agent incorporates information from another agent (rather than from direct observation), the optimal update gain extends the uncertainty ratio with additional terms for source quality and teleological-unity uncertainty.

## Formal Expression

*[Hypothesis (communication-gain)]*

$$\eta_{ji}^* = \frac{U_{M_i}}{U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji}}$$

where:
- $U_{M_i}$: agent $i$'s model uncertainty (same as #emp-update-gain)
- $U_{o,ji}$: **communication channel noise** — latency, ambiguity, compression loss, bandwidth limitations of the channel between $j$ and $i$
- $U_{\text{src},j}$: **source quality uncertainty** — $i$'s uncertainty about $j$'s model calibration and domain competence
- $U_{\text{align},ji}$: **teleological-unity uncertainty** — $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives

When all additional terms are zero (perfect channel, calibrated and aligned source): $\eta_{ji}^\ast \to 1$ (full trust). When any term is large: $\eta_{ji}^\ast \to 0$ (ignore the signal).

**Connection to single-agent case.** When $j$ is the environment (direct observation): $U_{\text{src}} = U_{\text{align}} = 0$, recovering #emp-update-gain's standard form $\eta^\ast = U_M / (U_M + U_o)$.

## Epistemic Status

*Hypothesis.* The additive denominator treats all uncertainty sources as independent, zero-mean noise — a structural heuristic, not a strict variance derivation. This is appropriate for $U_{o,ji}$ (channel noise) and $U_{\text{src},j}$ (miscalibration), which are typically unstructured. For $U_{\text{align},ji}$ (deception), additivity is conservative: it correctly drives $\eta_{ji}^\ast$ toward zero when teleological-unity uncertainty is high, but misses the adversary's *actual* strategy — presenting as trustworthy to exploit high $\eta_{ji}^\ast$. The additive model captures the *defender's* response to detected misalignment; it does not model the *attacker's* optimization over the defender's trust dynamics.

All four uncertainty terms must be expressed in a **common predictive-dispersion scale** before summation — the same units as $U_{M_i}$ (variance of the predictive distribution over the observed quantity). When hard to estimate directly, a conservative approximation: set $U_{\text{src}} + U_{\text{align}}$ to the empirical variance of $j$'s past prediction residuals as observed by $i$, minus the known channel noise $U_{o,ji}$.

## Discussion

**The denominator terms have different natures.** $U_{o,ji}$ is a property of the *channel* — improvable by infrastructure. $U_{\text{src},j}$ is a property of the *source* — improvable by $j$ improving its model, or estimable by $i$ through calibration tracking. $U_{\text{align},ji}$ is a property of the *relationship* — the game-theoretic variable.

**Trust calibration as a meta-model.** Agent $i$'s estimates of $U_{\text{src},j}$ and $U_{\text{align},ji}$ constitute a **trust meta-model** — a model of models. This meta-model is itself subject to AAT's full apparatus: it has mismatch (trust prediction errors), should be updated with appropriate gain (not overreacting to single disagreements), and can be structurally inadequate ( #result-structural-adaptation-necessity — the agent's trust model class may not capture the actual reliability structure of its sources).

**Risk-asymmetric trust.** The Bayesian posterior on source reliability gives the best *estimate*, but the *decision* about how much to trust should be risk-weighted. Trusting a deceptive agent (HILP — high impact, low probability) can cause catastrophic model corruption ( #der-adversarial-destabilization, effects spiral). Mild miscalibration toward a reliable source (LIHP) causes small ongoing inefficiency. For high-stakes interactions, use a conservative quantile of the trust posterior rather than the mean — require more evidence before granting high trust.

**Trust transitivity.** When agent $i$ has no direct experience with agent $k$, but trusted intermediary $j$ provides an assessment, the transitive trust question arises. A Bayesian mixture model discounts the recommendation by the intermediary's own reliability:

$$P_i(\theta_k \mid s_j) \propto \left[r_{ji} \cdot P(s_j \mid \theta_k) + (1 - r_{ji}) \cdot P_0(s_j)\right] \cdot P_i(\theta_k)$$

where $r_{ji}$ is $i$'s reliability estimate of $j$ and $\theta_k$ is $k$'s true alignment. When $r_{ji} \to 0$, the posterior collapses to the prior (no update); when $r_{ji} \to 1$, the full informative likelihood applies. This model gives a principled three-phase trust formation: prior → transitive update → direct experience (which eventually swamps the prior).

## Working Notes

- The communication gain enters the distributed tempo: $\mathcal{T}_i = \sum_k \nu_i^{(k)} \eta_i^{(k)\ast} + \sum_{j} \nu_{ji}^{\text{comm}} \eta_{ji}^\ast$. This is the formal basis for #der-team-persistence — teams persist where individuals cannot because cooperative communication adds to each agent's effective tempo.
- Coordination overhead limits team size: adding members increases communication tempo with diminishing returns while coordination costs grow. The optimal team size occurs where marginal communication tempo equals marginal coordination cost. This connects to organizational theory (span of control, communication overhead).
- The adversary's strategy (making $U_{\text{align}}$ *appear* low) creates a meta-game on trust estimation. This is where game theory enters — the trust calibration itself is strategic. AAT provides the state variables (mismatch, gain, tempo, reserve); game theory provides the equilibrium analysis.
- Open: when multiple intermediaries provide corroborating recommendations about $k$, correlation matters. If all got their information from the same source, corroboration is illusory.
- Consider eventually **splitting $U_{\text{src},j}$ from $U_{\text{align},ji}$** into separate treatment tracks, not just separate denominator terms. Source calibration uncertainty is an *estimation* problem (estimable, improvable, converges with data). Alignment uncertainty is a *strategic* problem (the adversary optimizes *over* the defender's trust policy, not independently of it). The additive heuristic correctly drives $\eta_{ji}^\ast$ toward zero in both cases, but a richer model would separate the estimation problem (how good is this source?) from the trust-policy problem (how much should I trust, given that the source knows my trust policy?). The latter requires game-theoretic treatment — AAT provides the state variables; the equilibrium analysis is external.


---

### Source: `impl-unity-communication.md`

```yaml
---
slug: impl-unity-communication
type: discussion
status: discussion-grade
depends:
  - def-unity-dimensions
  - result-unity-closure-mapping
  - def-shared-intent
  - hyp-auftragstaktik-principle
  - hyp-communication-gain
  - form-composition-closure
  - emp-update-gain
stage: draft
---
```


# Additional Implications & Discussion

The chapter sits between Ch.2's composition machinery (closure defect, bridge lemma, wrapping construction) and Ch.4's cooperative-vs-adversarial coupling, and its job is to give *unity* a quantitative content rather than leaving it as a verbal property of composites that work. Unity decomposes into named axes that parametrize a rate-distortion curve for closure defect; shared intent decomposes into an IB-optimal compression of the sender's purposeful state; communication gain decomposes the Bayesian update for inter-agent channels into source-noise, source-competence, and source-alignment terms. None of the three segments carries a `## Findings` section, so the implications segment is their canonical catalog home — but the work is mostly synthesis: surfacing what the chapter delivers as a chapter, what's hypothesis-grade rather than derived, and what bridges into Ch.4 and the rest of Part III.

## Unity dimensions and the rate-distortion content of "well-coordinated"

`#def-unity-dimensions` decomposes unity into a *content axis* (four dimensions — $U_M$, $U_O$, $U_\Sigma$, $U_{\text{obs}}$ — measuring sub-agent agreement on models, objectives, strategies, and observations respectively) and a *structural axis* ($U_f$, update-rule homogeneity). The implications-side payoff comes from `#result-unity-closure-mapping`: unity dimensions are not point-valued predictors of composite quality; they parametrize *rate-distortion curves* for closure-defect components. The achievable closure-defect component $\varepsilon_d$ under projection of macro-dimension $k_d$ is monotone decreasing in both the relevant content unity $U_d$ and the structural unity $U_f$ — higher unity along either axis lowers achievable closure defect at a given compression. Closed forms hold in the linear-Gaussian case; structural monotonicity survives more broadly.

The two-axis structure is not aesthetic — it is *forced* by the heterogeneous-Kalman case. Two agents can have identical content unity (same models, same objectives, same observations) and still produce composite closure defect if their update *machinery* differs ($K_1 \neq K_2$ in the Kalman case, or $\eta_1^\ast \neq \eta_2^\ast$ in the gain-principle case). The structural-unity term picks this up; the content axes alone would miss it. The framework's prediction is concrete: composite agents with high content unity but low structural unity will show closure-defect signatures the content-only analysis cannot diagnose, and the remedy is *update-rule homogenization* (synchronizing how sub-agents update, not just what they believe). For multi-agent ML systems, this is the underlying mechanism behind the empirical pattern that an ensemble of identically-trained models behaves differently from an ensemble whose members were trained with different optimizers or schedules — same content, different structural unity, different composite behavior.

The composition with Ch.2's closure-defect framework is the implication that anchors Part III's coordination story. Unity's rate-distortion content is *what makes the bridge lemma actionable*: the lemma converts predictive closure defect into trajectory error, and unity tells the composite-design practitioner *which dimensions to invest in* to reduce $\varepsilon^\ast$. Investing in $U_O$ (objective alignment) reduces $\varepsilon_a$ multiplicatively; investing in $U_\Sigma$ (strategy coordination) reduces it further through $f_1$; investing in $U_f$ (update homogeneity) reduces all components simultaneously. The closed-form predictions are linear-Gaussian; the structural pattern (unity dimensions monotone in closure defect, two-axis structure load-bearing) survives more broadly as robust-qualitative.

## Shared intent and the Auftragstaktik bandwidth allocation

`#def-shared-intent` formalizes commander's-intent / mission-command doctrine as an Information Bottleneck compression: the optimal inter-agent communication transmits enough of the sender's purposeful state $G_t = (O_t, \Sigma_t)$ to align coordination behavior, not more. The minimal sufficient statistic for predicting jointly optimal coordination is what gets transmitted; everything below that bar is discarded as IB-suboptimal at a given complexity-relevance tradeoff parameter $\beta$.

The implications-side payoff is what `#hyp-auftragstaktik-principle` extracts from this: under named regime conditions (objectives change slowly relative to strategies which change slowly relative to models; sub-agents have sufficient local adaptive capacity), the IB-optimal bandwidth allocation prioritizes $B_O \gt B_\Sigma \gt B_M$ — invest in objective sharing, then strategy coordination, then model synchronization, in that order. The framework's prediction is the priority ordering Auftragstaktik discovered empirically in 19th-century Prussian military doctrine (Moltke, Clausewitz) and that Bungay 2011 documents organizations consistently *fail* by inverting (micromanaging *how* subordinates act rather than ensuring they understand *why*). The mechanism the framework proposes — bits with longer shelf life and higher coordination value per bit transmitted first — is hypothesis-grade rather than derived, and the segment carries that honestly. What the IB framework predicts and what military doctrine empirically converged on agree at the *qualitative* level; whether the underlying mechanism is in fact IB-optimal bandwidth allocation is open.

What this buys for AAT's composition machinery is a quantitative reading of the cost in Ch.2's tempo-composition inequality. The closure defect $\varepsilon^\ast \nu_c$ that enters the composite's effective disturbance has a *bandwidth signature*: maintaining $\varepsilon^\ast$ small requires the composite to spend inter-agent bandwidth on the dimensions that close the closure defect. The Auftragstaktik prediction is that this spending is *front-loaded* in the priority ordering — most of the closure-defect reduction comes from a small bandwidth investment in objective sharing, with strategy and model investment delivering diminishing returns. For software teams the picture is concrete: well-functioning teams have high $B_O$ (clear product goals understood by all), moderate $B_\Sigma$ (architectural decisions shared, implementation autonomous), low $B_M$ (each developer builds their own mental model of the code they touch). When this inverts — micromanagement of implementation details, unclear product goals — team tempo drops, consistent with the framework's prediction.

The cross-domain transfer follows naturally and the segment surfaces it: Conway's Law (system structure mirrors communication structure) is a consequence rather than a separate observation. When $B_\Sigma$ is low and $B_O$ is high, sub-agents coordinate through shared objectives rather than explicit action coordination, producing systems whose boundaries reflect objective decomposition rather than communication channels. The framework's contribution is the structural argument — Conway's Law follows from IB-optimal bandwidth allocation under the regime conditions — rather than the empirical observation, which long predates AAT.

The honest scope statement worth surfacing: when the regime conditions fail, the priority ordering reverses. The prioritization assumes sub-agents can independently construct adequate local models; when the environment is genuinely ambiguous and local observations are insufficient (fog of war, novel codebase, unprecedented market conditions), model synchronization may be worth more than objective sharing — sub-agents who share the same wrong model at least err consistently, which is sometimes better than each having a different wrong model. The framework's prediction is that high-ambiguity regimes shift the IB-optimal allocation toward $B_M$, and the priority inversion is observable.

## Trust as inverse effective noise — the communication-gain decomposition

`#hyp-communication-gain` extends the single-agent uncertainty ratio from `#emp-update-gain` ($\eta^\ast = U_M/(U_M+U_o)$) to inter-agent channels by adding two new noise sources to the denominator: $U_{\text{src},j}$ (source-competence uncertainty, $i$'s uncertainty about $j$'s model calibration) and $U_{\text{align},ji}$ (teleological-unity uncertainty, $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives). The implication is that *trust formalizes as the inverse of effective noise on the inter-agent channel*: $\eta_{ji}^\ast \to 1$ when source-noise, source-competence, and source-alignment uncertainties are all small; $\eta_{ji}^\ast \to 0$ when any is large. The single-agent case is recovered when $j$ is the environment: $U_{\text{src}} = U_{\text{align}} = 0$, and the standard $\eta^\ast$ form returns.

The structural payoff is that *trust calibration is itself an AAT process*. Agent $i$'s estimates of $U_{\text{src},j}$ and $U_{\text{align},ji}$ constitute a *trust meta-model* — a model of models — which is subject to the framework's full apparatus: mismatch (trust prediction errors), gain (not overreacting to single disagreements), and structural inadequacy (`#result-structural-adaptation-necessity` applied at the meta-level — the agent's trust-model class may not capture the actual reliability structure of its sources). This is the segment's quietest claim and one of the framework's more reach-y consequences: relationships between agents are AAT processes operating on agent-pair-indexed quantities, with structure mirroring the agent-environment loop one level up. For AI-agent practitioners this prescribes a specific architectural pattern: trust assessments should be Bayesian-update-style with explicit calibration tracking, not threshold-based or static.

The decomposition also names a sharp distinction between the three uncertainty terms that downstream segments rely on. $U_{o,ji}$ is a property of the *channel* — improvable by infrastructure. $U_{\text{src},j}$ is a property of the *source* — improvable by $j$ improving its model, or estimable by $i$ through calibration tracking. $U_{\text{align},ji}$ is a property of the *relationship* — the game-theoretic variable, and the one that becomes load-bearing in Ch.4's cooperative-vs-adversarial coupling and Ch.5's strategic composition. The signed-coupling structure of those chapters is what determines $U_{\text{align},ji}$: cooperative coupling ($\gamma \lt 0$, from `#deriv-critical-mass-composition`) corresponds to $U_{\text{align},ji} \to 0$ (aligned objectives, trust calibrates to high $\eta_{ji}^\ast$); adversarial coupling ($\gamma \gt 0$) corresponds to $U_{\text{align},ji}$ large (misaligned objectives, trust calibrates to low $\eta_{ji}^\ast$). The communication-gain decomposition here is what makes the signed-coupling structure of Ch.4 *operational* at the trust-meta-model level.

The risk-asymmetric trust discussion in the segment is worth surfacing as an implications-flavored point in its own right: the Bayesian posterior on source reliability gives the best *estimate*, but the *decision* about how much to trust should be risk-weighted. Trusting a deceptive agent (high impact, low probability) can cause catastrophic model corruption via `#der-adversarial-destabilization`'s effects spiral; mild miscalibration toward a reliable source (low impact, high probability) causes small ongoing inefficiency. For high-stakes interactions, the framework prescribes a conservative quantile of the trust posterior rather than the mean — require more evidence before granting high trust. This is the AAT-internal grounding for the empirical pattern that high-trust relationships build slowly and break quickly: the structural reason is that the decision-side risk-asymmetry favors slow accumulation and fast erosion.

## Composition with the framework's other machinery

The chapter's three findings compose with the rest of Part III in a way worth surfacing as a unifying point. Ch.2's closure defect $\varepsilon^\ast$ acquires its rate-distortion content from this chapter's `#result-unity-closure-mapping`; Ch.2's coordination overhead $C_{\text{coord}} \geq \varepsilon^\ast \nu_c$ in `#der-tempo-composition`'s tempo composition acquires its bandwidth signature from this chapter's Auftragstaktik prediction. Ch.4's signed coupling $\gamma$ acquires its trust-meta-model interpretation from this chapter's $U_{\text{align},ji}$; Ch.5's strategic composition under partially-opposing objectives acquires its $U_{\text{align},ji}$ dynamics from how `#hyp-communication-gain`'s trust calibration responds to observed coupling sign. The chapter is the *bandwidth and trust layer* between Ch.2's composition machinery and Ch.4/Ch.5's coupling dynamics — and the framework's posture is that all four chapters are operating on the same composite-agent persistence machinery, with each chapter supplying a different parametric content (machinery, bandwidth/trust, coupling sign, equilibrium).

Two cross-domain transfers worth noting before leaving the chapter. *Multi-agent AI safety*: the trust-calibration apparatus prescribes that agent-to-agent communication should be filtered through Bayesian-update-style assessment with explicit calibration tracking. Multi-agent systems that rely on flat trust models (one threshold, applied uniformly to all interlocutors) systematically miscalibrate the way `#hyp-communication-gain` predicts — they trust unreliable sources too much in low-stakes regimes and too little in high-stakes regimes, because the structural decomposition into channel / source / alignment noise is collapsed. *Human-AI teaming*: the same apparatus predicts which dimensions of teaming matter. Shared intent first (high-bandwidth objective alignment); strategy coordination next (architectural decisions shared, implementation autonomous); model synchronization last (the AI agent doesn't need the human's full mental model and vice versa). The framework's contribution against the empirical-design literature on human-AI teaming is that the priority ordering is structural, not contingent.

## Working Notes

- This segment is a chapter-end discussion grouping findings from `#def-unity-dimensions`, `#result-unity-closure-mapping`, `#def-shared-intent`, `#hyp-auftragstaktik-principle`, and `#hyp-communication-gain`. The cross-segment composition with Ch.2's machinery in §4 leans on `#form-composition-closure` and `#der-tempo-composition`; the forward bridges into Ch.4 lean on `#der-team-persistence`, `#der-adversarial-destabilization`, and `#deriv-strategic-composition`.
- **Cross-reference vs canonical-home policy.** None of this chapter's five source segments carry `## Findings` sections. This implications segment is the canonical catalog home for #22 (Shared Intent / Auftragstaktik via IB), #47 (Rate-Distortion Mapping of Team Unity), and #51 (Trust Formalization via Communication Gain), and treats each in full. The treatment is honest about the hypothesis-grade nature of #22 and #51 — both are structurally motivated but not derived — and about the linear-Gaussian-specific closed forms for #47 with structural monotonicity surviving more broadly.
- **Cross-segment finding — bandwidth-and-trust as the layer between Ch.2 and Ch.4.** The unifying point in §4 is itself a cross-segment finding without a single segment home: the framework's composition story is operating on a single composite-persistence machinery across Ch.2 (machinery), Ch.3 (bandwidth and trust), Ch.4 (coupling sign), and Ch.5 (equilibrium). Each chapter supplies a different parametric content. This synthesis is what the implications-segment series at chapter-end can do that the individual segments cannot.
- **Hypothesis-grade content honest scoping.** Three of the chapter's findings sit at hypothesis-grade epistemic strength — #22 (Auftragstaktik priority ordering is qualitatively predicted but the IB-optimal-allocation mechanism is not derived in closed form), #51 (the additive denominator for communication gain treats uncertainty sources as independent, which is structural rather than derived), and parts of #47 (the rate-distortion mapping has closed-form predictions only in the linear-Gaussian case; structural monotonicity survives more broadly as robust-qualitative). The implications segment reflects this honestly rather than over-claiming theorem-grade status.
- **No identifiability-floor instance lands in this chapter.** The chapter's findings are about *machinery* (unity dimensions, shared intent compression, trust calibration) rather than about identifiability boundaries. The four formal identifiability-floor instances are now all surfaced in the implications series (Instance 1 in Ch.4-strategy-dynamics, Instance 2 in Ch.3-strategy-structure, Instance 3 in Ch.2-composition-machinery, Instance 4 in Ch.5-orient-cascade). Instance 5 (Mehra non-identifiability) remains candidate.
- **Connection to NeurIPS submissions.** The chapter's findings are AAT-internal; their cross-references in current submissions are scope and structural-argument links rather than theorem-grade adoption. The Auftragstaktik prediction could land in a future multi-agent-AI-safety submission if the regime conditions can be operationalized as testable conditions on a real multi-agent system.


---

