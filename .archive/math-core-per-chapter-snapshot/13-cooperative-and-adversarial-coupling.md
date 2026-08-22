# Cooperative and Adversarial Coupling


## Derived: Team Persistence

- **Slug**: `der-team-persistence`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `result-persistence-condition`, `result-sector-condition-stability`, `result-sector-persistence-template`, `hyp-communication-gain`, `def-adaptive-tempo`

Teams persist where individuals cannot through two physically distinct cooperative mechanisms: communication (allies share observations that improve correction) and action (allies act in the shared environment to reduce disturbance at its source). These mechanisms enter the persistence condition at different points — tempo and disturbance respectively — and a given cooperative interaction contributes through one mechanism or the other, not both.

This segment instantiates the sector-persistence template ( #result-sector-persistence-template) at the multi-agent level with state variable $\xi = \delta_i$ (sub-agent $i$'s mismatch) and a decomposed effective disturbance $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$ that accounts for adversarial and cooperative coupling. The template supplies the Lyapunov machinery; this segment's distinctive content is the disturbance decomposition and the corresponding tempo extension.

### Distributed Tempo

*[Definition (distributed-tempo)]*

Agent $i$'s effective tempo includes contributions from both direct observation and communication from allies:

$$\mathcal{T}_i = \underbrace{\sum_k \nu_i^{(k)} \eta_i^{(k)*}}_{\text{direct observation tempo}} + \underbrace{\sum_{j \in \mathcal{N}(i)} \nu_{ji}^{\text{comm}} \, \eta_{ji}^*}_{\text{communication tempo}}$$

where $\nu_{ji}^{\text{comm}}$ is the rate of communication events from agent $j$ to agent $i$, and $\eta_{ji}^\ast$ is the communication gain ( #hyp-communication-gain). Faster team adaptation comes not only from faster individual sensing but from faster, more reliable knowledge transfer.

**Channel independence caveat.** Both sums are additive, inheriting the channel-independence assumption from #def-adaptive-tempo: each channel and each communication source contributes non-redundant correction capacity. When allies report correlated information (overlapping observations, shared intelligence sources, redundant status reports), the communication tempo overcounts. The additive formula is an upper bound; the redundancy penalty depends on the mutual information between communication sources. See #def-adaptive-tempo for the single-agent version of this caveat.

### Cooperative-Adversarial Disturbance Decomposition

*[Formulation (disturbance-decomposition)]*

The disturbance rate experienced by agent $i$ decomposes into environment, adversarial, and cooperative components:

$$\rho_i = \rho_{i,\text{env}} + \sum_{j \in \mathcal{A}_i} \gamma_{j \to i}^{\text{adv}} \, \mathcal{T}_j - \sum_{j \in \mathcal{C}_i} \gamma_{j \to i}^{\text{coop}} \, \mathcal{T}_j$$

where $\mathcal A_i$ is the set of agents adversarially coupled to $i$, $\mathcal C_i$ is the set cooperatively coupled, and the $\gamma$ coefficients capture coupling effectiveness (as in #der-adversarial-destabilization).

**The cooperative term is negative — but through action, not communication.** Allies reduce agent $i$'s effective disturbance by *acting in the shared environment* to prevent or mitigate disturbance at its source. Examples: an ally stabilizes a shared resource, neutralizes a threat before it reaches $i$, or absorbs environmental variation through their own actions. The mechanism is causal coupling through the shared environment, not information transfer.

**Separation from communication tempo.** The communication tempo term (above) captures allies *telling* agent $i$ things that improve its correction. The cooperative disturbance term captures allies *doing* things that reduce the disturbance $i$ faces. These are physically distinct: communication improves $i$'s correction function (better $\alpha_i$, higher $\mathcal{T}_i$); cooperative action reduces the disturbance $\rho_i$ that $i$ must correct against. A single cooperative event contributes through one channel or the other. An ally's message about a threat enters through communication tempo; an ally's action that eliminates the threat enters through disturbance reduction. Counting a single event in both terms would double-count the benefit and make the persistence threshold systematically optimistic.

**Effective disturbance rate.** The decomposition can yield $\rho_i \lt 0$ when cooperative coupling dominates both environment disturbance and adversarial coupling. The sector-condition analysis ( #result-sector-condition-stability) assumes non-negative disturbance (GA-2). Define:

*[Definition (effective-disturbance)]*

$$\rho_i^{\text{eff}} = \max(\rho_i, \, 0)$$

When $\rho_i^{\text{eff}} = 0$, the agent's cooperative network fully absorbs all disturbance — the persistence condition is trivially satisfied and mismatch decays to zero. This is an idealized limit; in practice, $\rho_i^{\text{eff}} \gt 0$ because cooperative coupling is imperfect and environment disturbance is never fully preempted. All downstream uses of $\rho_i$ in the persistence and reserve conditions should be read as $\rho_i^{\text{eff}}$.

### Team Persistence Condition

*[Derived (team-persistence, from sector-condition-stability, persistence-condition)]*

Applying the sector-condition framework ( #result-sector-condition-stability) with $\rho_i^{\text{eff}}$, agent $i$ persists iff:

$$\frac{\rho_i^{\text{eff}}}{\alpha_i} \lt R_i$$

Substituting the decomposition (the $\max(\cdot, 0)$ in $\rho_i^{\text{eff}}$ is omitted to expose the three levers; the condition is trivially satisfied when the numerator is non-positive):

$$\frac{\rho_{i,\text{env}} + \sum_j \gamma_{j \to i}^{\text{adv}} \mathcal{T}_j - \sum_j \gamma_{j \to i}^{\text{coop}} \mathcal{T}_j}{\alpha_i} \lt R_i$$

This reveals three distinct levers for team persistence:

1. **Increase $\alpha_i$** (individual correction efficiency) — better models, better gain calibration, including communication-improved tempo from allies ( #hyp-communication-gain)
2. **Increase cooperative disturbance reduction** ($\gamma^{\text{coop}} \mathcal T_j$) — more effective allied action in the shared environment: stabilizing shared resources, preempting threats, absorbing environmental variation. This is the action-based mechanism distinguished above, not the communication channel.
3. **Reduce adversarial coupling** ($\gamma^{\text{adv}} \mathcal T_j$) — better deception detection, reduced exposure to adversarial actions

### Coordination Overhead Threshold

*[Discussion — Coordination Threshold]*

Communication channels have costs: time to compose and parse messages, bandwidth limitations, synchronization requirements. These costs reduce the agent's effective tempo by diverting capacity from direct adaptation. Let $\Delta \mathcal T_i^{\text{cost}}(j)$ represent the tempo-equivalent coordination cost of maintaining the channel with $j$ — the reduction in $i$'s direct observation tempo caused by the overhead, in units of $[t^{-1}]$.

The net benefit of adding agent $j$ to $i$'s communication network is positive only when:

$$\nu_{ji}^{\text{comm}} \, \eta_{ji}^* \gt \Delta \mathcal{T}_i^{\text{cost}}(j)$$

Both sides have units $[t^{-1}]$: the LHS is communication tempo gained, the RHS is direct-adaptation tempo lost to coordination overhead. This implies a natural team-size limit: adding members increases communication tempo with diminishing returns (as $U_{\text{src}}$ and $U_o$ accumulate across diverse sources) while coordination costs grow, potentially superlinearly. The optimal team size occurs where the marginal communication tempo equals the marginal coordination cost.

---



## Derived: Adversarial Destabilization

- **Slug**: `der-adversarial-destabilization`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `result-sector-condition-stability`, `deriv-sector-condition`, `result-sector-persistence-template`, `def-adaptive-tempo`

When two agents are coupled such that one's praxis contributes to the other's disturbance rate, the faster agent can generate aporia in the target faster than the target's epistrophe can resolve it — driving the target outside its invariant region and causing the correction mechanism to break down entirely.

This segment is the sector-persistence template ( #result-sector-persistence-template) applied with coupling-amplified disturbance: $\rho_B = \rho_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model D) or $\sigma_B = \sigma_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model S). The destabilization threshold is the **negation** of the template's persistence condition for agent $B$: destabilization occurs precisely when the coupling-amplified disturbance violates $\alpha_B R_B \gt \rho_B$. Persistence and destabilization are the same inequality viewed in opposite directions. The superlinear adversarial scaling ( #result-adversarial-tempo-advantage) follows from the template's $1/\alpha$ (Model D) versus $1/\sqrt{\alpha}$ (Model S) scaling, not from separate derivation.

*[Derived (adversarial-destabilization, from sector-persistence-template)]*

**Setup.** Both agents satisfy the single-agent sector-persistence template ( #result-sector-persistence-template) with parameters $(\alpha_A, R_A)$ and $(\alpha_B, R_B)$. Coupling amplifies $B$'s effective disturbance rate by $\gamma_A \cdot \mathcal{T}_A$; destabilization is the negation of the template's persistence condition $\alpha_B R_B \gt \rho_B^{\text{eff}}$ for $B$. See #result-adversarial-exponent-regimes for regime taxonomy.

### Model D: deterministic drift coupling

*[Assumption (Coupling Model D)]* $\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$. The template's Model D conclusion $R_B^\ast = \rho_B/\alpha_B$ applied with the coupling model yields $B$'s destabilization threshold $R_B^\ast \gt R_B$:

$$\boxed{\;\mathcal{T}_A \;\gt\; \frac{\alpha_B R_B - \rho_{B,\text{base}}}{\gamma_A}\;} \quad \text{(Model D)}$$

Denote $\Delta\rho_B^\ast = \alpha_B R_B - \rho_{B,\text{base}}$, $B$'s adaptive reserve — the template's reserve quantity applied with the baseline disturbance. $\square$

### Model S: stochastic noise coupling

*[Assumption (Coupling Model S)]* $\sigma_B = \sigma_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$ — the adversary's tempo increases unpredictability, not systematic direction. The template's Model S conclusion $R_B^\ast = \sigma_B \sqrt{n/(2\alpha_B)}$ (scalar $n = 1$) applied with the coupling yields the destabilization threshold:

$$\boxed{\;\mathcal{T}_A \;\gt\; \frac{R_B \sqrt{2\alpha_B} - \sigma_{B,\text{base}}}{\gamma_A}\;} \quad \text{(Model S)}$$

**Scaling difference.** The Model D threshold is linear in $\alpha_B$; the Model S threshold is linear in $\sqrt{\alpha_B}$ — the same $1/\alpha$ versus $1/\sqrt{\alpha}$ split the template gives for the two disturbance models, propagated through the destabilization negation. This is the direct origin of the $b = 2$ versus $b = 3/2$ exponent distinction in #result-adversarial-exponent-regimes, not a separate derivation. $\square$

### Unified view

Symmetrically, $B$ destabilizes $A$ when the analogous threshold on $\mathcal T_B$ is exceeded, using whichever model describes $A$'s disturbance. The adversarial outcome depends on whether either agent can push the other past its stability limit.

**Regime selection in practice.** Model D fits situations where adversarial action produces persistent positional shifts (military maneuvering, API changes propagating through dependents, doctrinal initiative). Model S fits situations where adversarial action produces unpredictable perturbations around a stationary level (feints, randomized probing, market volatility). Mixed cases are handled by decomposing the disturbance into drift and noise components and applying both bounds additively.

**Interpretation.** "Getting inside the opponent's OODA loop" has a precise Lyapunov characterization: Agent $A$ destabilizes Agent $B$ when $A$'s praxis, multiplied by coupling effectiveness, generates aporia in $B$ faster than $B$'s epistrophe can resolve it — specifically, when $A$'s tempo times coupling exceeds $B$'s adaptive reserve $\Delta\rho^\ast_B$. This captures:

- **Asymmetric coupling** ($\gamma_A \neq \gamma_B$): an agent with lower tempo but higher coupling effectiveness can still win.
- **Finite reserves**: an agent with very high $\mathcal{T}$ but operating near its model-class limit ($\Delta\rho^\ast$ small) is vulnerable despite high tempo.
- **Structural collapse**: when $R^\ast_B \gt R_B$, the failure mode is not merely "large mismatch" but "correction mechanism breakdown" — connecting to #result-structural-adaptation-necessity.

### Corollary: The Effects Spiral

When Agent $B$ is driven past its stability boundary ($R^\ast_B \gt R_B$), and $B$'s degrading model causes $B$'s actions to become erratic in a way that increases $A$'s coupling effectiveness ($\gamma_A$ increases with $\Vert\delta_B\Vert$), the result is a positive-feedback Lyapunov instability:

*[Discussion — Mechanism Schematic]*

$$\Vert\delta_B\Vert \uparrow \;\Rightarrow\; B\text{'s actions become erratic} \;\Rightarrow\; \gamma_A \uparrow \;\Rightarrow\; \rho_B \uparrow \;\Rightarrow\; \Vert\delta_B\Vert \uparrow$$

With $\gamma_A$ now an increasing function of $\Vert\delta_B\Vert$, the disturbance term in $B$'s dynamics grows superlinearly. $\dot{V}_B \gt 0$ and increasing — mismatch accelerates away from the stability region. The spiral terminates only when $B$ undergoes structural adaptation ( #result-structural-adaptation-necessity — changing the model class) or ceases to function as an adaptive agent entirely.

---



## Derived: Interaction-Channel Classification (Recipient-Side)

- **Slug**: `der-interaction-channel-classification`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-observation-function`, `def-mismatch-signal`, `result-mismatch-decomposition`, `emp-update-gain`, `def-adaptive-tempo`, `def-model-class-fitness`, `result-structural-adaptation-necessity`, `result-persistence-condition`, `result-sector-persistence-template`, `der-adversarial-destabilization`, `der-directed-separation`, `disc-credit-assignment-boundary`

The same signal from agent $A$ lands on recipient $B$ as one of four qualitatively different things — informative update, magnitude-shock, structural-shock, or ambient noise — determined by three independent boundary conditions stated entirely in $B$'s existing AAT quantities. The emitter-side collapse of this variation into a scalar $\gamma_A \mathcal T_A$ loses information that is load-bearing: the recipient's repair path depends on which regime the event falls into, and "more tempo" vs "different model class" address structurally different failure modes.

### Setup and Notation

Two purposeful agents $A$ and $B$ coupled through a shared environment. $A$'s praxis produces an event $e_\tau^A$ that enters $B$'s observation channel. On $B$'s side the event is processed by the standard AAT machinery: $h_B$ maps the $A$-induced environment state to observation $o_\tau^B$ ( #def-observation-function); mismatch is $\delta_\tau^B = o_\tau^B - \hat o_\tau^B$; update absorbs $\delta_\tau^B$ with gain $\eta_B^\ast = U_{M,B}/(U_{M,B} + U_{o,B})$ ( #emp-update-gain).

Two event-level quantities enter the classification and must not be conflated:

- $\lVert e_\tau^A\rVert_B$ — the **magnitude** of the event in $B$'s observation space (how large a perturbation it produces in $\delta_\tau^B$ on arrival).
- $\mathcal I(e_\tau^A)$ — the **information content** of the event conditional on $B$'s prior, formally $I(e_\tau^A; \Omega \mid M_{B,\tau^-})$ per NOTATION.md's event-information quantity. A large-magnitude already-predicted event has large $\lVert e\rVert$ but small $\mathcal I$; a tiny-magnitude structurally novel event has small $\lVert e\rVert$ but large $\mathcal I$.

Let $\mathcal F(\mathcal M_B)$ denote $B$'s model-class fitness ( #def-model-class-fitness), and $\mathcal I_{\max}(\mathcal M_B)$ the maximum per-event information content representable within the class (see Working Notes for the cleaner sufficient-statistics-span formulation).

### Classification Boundaries

*[Definition (regime-boundaries)]*

Event $e_\tau^A$ arriving at $B$ falls into one of four regimes, determined by three independent boundary conditions:

**Regime I (Informative update)** when all three hold:

$$\text{(I-a)} \quad \lVert e_\tau^A\rVert_B \leq R_B \qquad \text{(within sector-condition region)}$$

$$\text{(I-b)} \quad \mathcal I(e_\tau^A) \leq \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B) \qquad \text{(representable within model class)}$$

$$\text{(I-c)} \quad \mathcal I(e_\tau^A) \cdot \nu^{(k)} \geq U_{o,B}^{(k)} \cdot c_\text{floor} \qquad \text{(above observability floor)}$$

where $k$ is the arrival channel, $\nu^{(k)}$ its event rate, and $c_\text{floor}$ a detection-theory constant controlling the false-alarm tolerance.

**Regime II-a (Magnitude-shock destabilization)** when (I-a) fails:

$$\lVert e_\tau^A\rVert_B \gt R_B$$

The event exits $B$'s sector-condition region on arrival. $B$'s correction function does not point inward strongly enough to discharge the mismatch before the next event; under sustained rate $\nu \gtrsim \alpha_B$, destabilization proceeds per #der-adversarial-destabilization.

**Regime II-b (Structural-shock destabilization)** when (I-a) holds but (I-b) fails:

$$\lVert e_\tau^A\rVert_B \leq R_B, \qquad \mathcal I(e_\tau^A) \gt \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B)$$

The event's information content exceeds what $B$'s model class can represent. By #result-structural-adaptation-necessity, parametric update within $\mathcal M_B$ cannot close the mismatch; residuals retain systematic structure. Repair requires structural adaptation (a different model class), not more bandwidth.

**Regime III (Ambient noise / slow erosion)** when (I-a) and (I-b) hold but (I-c) fails:

$$\lVert e_\tau^A\rVert_B \leq R_B, \qquad \mathcal I(e_\tau^A) \leq \mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B), \qquad \mathcal I(e_\tau^A) \cdot \nu^{(k)} \lt U_{o,B}^{(k)} \cdot c_\text{floor}$$

The event is representable and within capacity but its information content sits below the observability floor. It contributes to $\delta_B$'s variance (enters Model S as part of $\sigma_{w,B}^2$) without triggering a usable update; $B$'s adaptive reserve $\Delta\rho_B^\ast$ slowly drains.

### Three Independent Boundaries

The three boundary conditions are structurally independent, each stated in quantities AAT already carries:

| Boundary | AAT quantities | Failure mode |
|---|---|---|
| (I-a) / (II-a): sector-region | $\lVert e\rVert_B$, $R_B$ (from #def-model-class-fitness / #result-sector-persistence-template) | *magnitude* — more capacity cures |
| (I-b) / (II-b): model-class | $\mathcal I(e)$, $\mathcal F(\mathcal M_B)$, $\mathcal I_{\max}(\mathcal M_B)$ | *class* — structural adaptation cures |
| (I-c) / (III): observability | $\mathcal I(e)$, $\nu^{(k)}_B$, $U_{o,B}^{(k)}$ (from #obs-gated-tempo-advantage) | *rate* — lower observation noise or higher event rate cures |

No new ad-hoc thresholds are introduced. $\mathcal I_{\max}(\mathcal M_B)$ is the only new symbol; see Working Notes for its cleaner sufficient-statistics-span formulation.

### Regime-Typed Disturbance Decomposition

*[Derived (regime-typed-rho-eff, from regime-boundaries + sector-persistence-template)]*

Under a stream of events $\{e_\tau^A\}$, $B$'s **regime-typed effective disturbance** rate decomposes into regime-typed contributions:

$$\rho_B^{\text{eff}} = \underbrace{\sum_{e \in \text{II-a}} \lVert e\rVert_B \cdot \nu_e}_{\text{magnitude disturbance}} \;+\; \underbrace{\text{floor}(\mathcal M_B) \cdot \sum_{e \in \text{II-b}} \nu_e}_{\text{structural mismatch floor}} \;+\; \underbrace{\sum_{e \in \text{III}} \sigma_e^2 \cdot \nu_e}_{\text{ambient variance}} \;-\; \underbrace{\sum_{e \in \text{I}} \iota_B(e)\,\mathcal I(e) \cdot \nu_e}_{\text{informative correction}}$$

The Regime-I term is **negative**: informative events reduce $B$'s effective disturbance rate, not increase it. This generalizes #der-team-persistence's cooperative-action term $-\gamma^{\text{coop}}\mathcal T_j$: a cooperative event is precisely a Regime-I event from an aligned emitter, and the sign flip in the emitter-side decomposition falls out of the regime assignment on the recipient side. Adversarial events land in Regimes II-a/II-b; ambient-noise events in Regime III.

The emitter-side formulation $\gamma_A \mathcal T_A \to \rho_B^{\text{eff}}$ compresses the regime-typed sum into a single scalar, losing (i) the sign of cooperative coupling, (ii) the magnitude vs structural distinction in destabilization, and (iii) the observability-floor loss to Regime III.

### Structured Derivation — Kalman-over-Kalman

*[Derivation (Kalman-over-Kalman, from regime-boundaries + update-gain)]*

For a concrete check, take $B$ as a Kalman filter on a scalar linear-Gaussian state with model class $\mathcal M_B = \{\theta \in [\theta_{\min}, \theta_{\max}]\}$, process noise $q$, observation noise $r$, sector parameter $\alpha_B = \eta_B^\ast = P_{\text{pred}}/(P_{\text{pred}} + r)$. $B$'s sector-region radius is $R_B = \sqrt{q/(1-\theta_{\max}^2)}$ (stationary standard deviation at the class edge).

$A$'s emitted perturbation $\xi_A$ enters $B$'s innovation as $\delta_\tau^B = \xi_A + \varepsilon_\tau + (\omega_\tau - \hat\omega_\tau)$. Four canonical distributions for $\xi_A$ partition the classification:

**Case 1 — Small-variance Gaussian $\xi_A \sim \mathcal N(0, s^2)$, $s^2 \ll r$ (expected Regime III).** $\mathcal I(\xi_A) \approx s^2/(2r \ln 2)$ nats — small. (I-a) holds ($s \ll R_B$); (I-b) holds (Gaussian-within-Gaussian); (I-c) fails because $\mathcal I(\xi_A) \lt U_{o,B} \cdot c_\text{floor}$. Result: Regime III. Derived consequence — the contribution to $\rho_B^{\text{eff}}$ is through $\sigma_{w,B}^2$; adaptive reserve drains by $\sum_e \eta_B^{\ast 2} s_e^2 \cdot \nu_e$.

**Case 2 — Moderate Gaussian $\xi_A \sim \mathcal N(\mu, s^2)$, $\mu \ll R_B$, $s^2 \sim r$ (expected Regime I).** $\mathcal I(\xi_A) = \tfrac{1}{2}\log(1 + (s^2 + \mu^2)/r)$ — substantial. All three (I-a)/(I-b)/(I-c) hold. Result: Regime I. Standard Kalman update; $M_B$ refines; Regime-I term contributes negatively to $\rho_B^{\text{eff}}$.

**Case 3 — Binary kick $\xi_A \in \{\pm\Delta\}$ with $\Delta \gt R_B$ (expected Regime II-a).** (I-a) fails by construction. The Kalman update $\hat x^+ = \hat x^- + \eta^\ast \Delta$ undershoots by $(1-\eta^\ast)\Delta$ per event. If events arrive at rate $\nu \gtrsim \alpha_B$, lag accumulates and $\alpha_B R_B \gt \rho_B^{\text{eff}}$ is violated. Result: Regime II-a — destabilization per #der-adversarial-destabilization. Notice: the signal is *within* the model class (Gaussian handles $\pm\Delta$ mathematically), but correction cannot discharge it fast enough.

**Case 4 — Heavy-tailed $\xi_A$ with $\mathbb E[\xi_A^2] \sim r$ but kurtosis $\kappa \to \infty$ (expected Regime II-b).** Mean contribution is fine; the problem is the distribution shape. The Kalman filter — Gaussian-optimal — mis-gains: too aggressive for small events, too conservative for genuine large ones. The per-event KL gap $D_{\text{KL}}(P_\text{true} \Vert P_{\mathcal M_B}) \gt 0$ for any heavy-tailed $P_\text{true}$ against Gaussian. By #def-model-class-fitness, $\mathcal F(\mathcal M_B) \lt 1 - \varepsilon$ with $\varepsilon$ lower-bounded by the KL gap; by #result-structural-adaptation-necessity, no parametric update within $\mathcal M_B$ closes the mismatch. Result: Regime II-b — residuals retain non-Gaussian structure (visible in kurtosis tests); repair requires expanding the model class (e.g., Student-$t$ observation model), not more Kalman tuning.

Each case lands where the classification predicts. The derivation transfers to any recipient architecture in which the underlying AAT quantities are well-defined — this is the scope inherited from #result-sector-persistence-template + #def-model-class-fitness + #def-adaptive-tempo.

### Recovery of Emitter-Side Results

*[Derived (emitter-side-recovery)]*

Each existing emitter-side result is a restriction of the four-regime decomposition:

- **#der-adversarial-destabilization** is Regime II-a integrated over a tempo-proportional event stream. The magnitude-shock sub-regime corresponds directly; the structural-shock II-b subcase is implicit in that segment, collapsed into "adaptive reserve exceeded" but here made explicit.
- **#result-adversarial-tempo-advantage** — superlinear tempo scaling follows from the sector-persistence template's $1/\alpha$ (Model D) vs $1/\sqrt\alpha$ (Model S) applied to Regime II events. The $b$-exponent drops toward zero in the high-$U_{o,B}$ limit because the fraction of $A$'s events landing in Regime II drops (more fall into Regime III).
- **#obs-gated-tempo-advantage** is the recipient-side expression of boundary (I-c): high $U_{o,B}$ pushes events into Regime III where they add to variance without contributing to destabilization.
- **#hyp-symbiogenic-composition** corresponds to asymmetric classification: host's signals to endosymbiont contain high-$\mathcal I$ structure the endosymbiont's class cannot initially represent (Regime II-b for the endosymbiont, forcing structural adaptation toward the host's class); endosymbiont's signals to the host land in Regime I (host absorbs endosymbiont's accumulated structure). Consolidation is the fixed-point where both streams are Regime I.
- **Cooperative signaling** (in #der-team-persistence) — Regime-I events from aligned emitters contribute negatively to $\rho_B^{\text{eff}}$ via the cooperative-action term. The communication-tempo $\nu_{ji}^{\text{comm}} \cdot \eta_{ji}^\ast$ is the rate of Regime-I events times the recipient's informative gain.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Three independent boundaries (sector-region / model-class / observability) | Import from #def-model-class-fitness + #result-sector-persistence-template + #obs-gated-tempo-advantage | Formulation choice (three-way partition; coarser / finer alternatives possible) |
| Four-regime partition (I / II-a / II-b / III) | The three boundaries yield four boundary-state combinations; only four are non-degenerate | Derived from the boundary structure |
| (I-a) / (II-a) boundary at $R_B$ | #result-sector-persistence-template's sector-region radius | Derived |
| (I-b) / (II-b) boundary at $\mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}$ | #def-model-class-fitness + class-capacity normalization | Formulation (the $\mathcal I_{\max}$ normalization is heuristic; sufficient-statistics-span form is cleaner — see Working Notes) |
| (I-c) / (III) boundary at $U_{o,B} \cdot c_\text{floor}$ | #obs-gated-tempo-advantage + detection-theory threshold | Formulation ($c_\text{floor}$ is a detection-power parameter) |
| Regime-typed $\rho_B^{\text{eff}}$ decomposition with negative Regime-I term | Aggregation over event stream using regime classification | Derived (the sign of the Regime-I term is structural, not a choice) |
| Kalman-over-Kalman four-case derivation | Direct application of Kalman gain + sector + KL-gap + SNR analyses | Proved (for the stated case) |
| Recovery of #der-adversarial-destabilization, #hyp-symbiogenic-composition, #obs-gated-tempo-advantage, #der-team-persistence as restrictions | Each emitter-side result is exhibited as a per-regime special case | Derived |
| Non-Gaussian Case 4 derivation (heavy-tailed → II-b via KL gap) | Informal argument grounded in robust-filtering literature (Huber, Masreliez) | Discussion-grade (rigorous version requires per-family KL computation) |
| Class 2 (Partial) approximation with $\kappa_{\text{processing}}$ degradation | Transfer from Class 1 (Separated) with goal-blind-update failure | Formulation (qualitative); exact form requires spelling out the goal-contamination coupling |

---



## Result: Adversarial Tempo Advantage

- **Slug**: `result-adversarial-tempo-advantage`
- **Type**: result
- **Status**: conditional
- **Stage**: draft
- **Depends**: `hyp-mismatch-dynamics`, `der-adversarial-destabilization`, `result-persistence-condition`

Under adversarial coupling where one agent's actions contribute to the other's disturbance rate, the steady-state mismatch ratio scales superlinearly with the tempo ratio.

*[Derived (adversarial-tempo-advantage, from sector-persistence-template + adversarial-destabilization coupling model)]*

**Setup.** Two agents $A, B$ with adaptive tempos $\mathcal T_A, \mathcal T_B$, each instantiating #result-sector-persistence-template with linear correction ($\alpha = \mathcal{T}$). The adversarial coupling of #der-adversarial-destabilization enters each agent's effective disturbance:

$$\rho_A^{\text{eff}} = \rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B, \qquad \rho_B^{\text{eff}} = \rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

with $\gamma_A, \gamma_B \gt 0$ coupling effectivenesses and $\rho_{\text{base}}$ the shared background rate (asymmetric $\rho_{\text{base}}$ generalizes straightforwardly).

### Model D: Deterministic coupling, $b = 2$

*[Result (adversarial-tempo-advantage, Model D)]*

The template's Model D conclusion $\lVert\delta\rVert_{ss} = \rho^{\text{eff}}/\mathcal{T}$ (linear case, $\alpha = \mathcal{T}$) applied to both agents and ratioed:

$$\frac{\lVert\delta_B\rVert_{ss}}{\lVert\delta_A\rVert_{ss}} = \frac{(\rho_{\text{base}} + \gamma_A \mathcal{T}_A)\,\mathcal{T}_A}{(\rho_{\text{base}} + \gamma_B \mathcal{T}_B)\,\mathcal{T}_B}$$

In the coupling-dominant limit ($\gamma \mathcal{T} \gg \rho_{\text{base}}$) with symmetric coupling ($\gamma_A = \gamma_B$):

$$\frac{\lVert\delta_B\rVert_{ss}}{\lVert\delta_A\rVert_{ss}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

The exponent is $b = 2$: a **squared** tempo advantage. A 2:1 tempo ratio yields a 4:1 mismatch ratio. The faster agent both (a) corrects its own mismatch faster and (b) generates disturbance for the opponent faster — the two effects compound rather than add. $\square$

### Model S: Stochastic coupling, $b = 3/2$

*[Derived (stochastic-tempo-advantage, from sector-persistence-template Model S + coupling)]*

Under Model S the coupling enters the noise scale: $\sigma_B^{\text{eff}} = \sigma_{\text{base}} + \gamma_A \mathcal T_A$. Adversary tempo increases unpredictability, not systematic direction. The template's Model S steady state $\lVert\delta\rVert_{\text{rms}} = \sigma/\sqrt{2\mathcal{T}}$ (linear $\alpha = \mathcal{T}$, scalar $n = 1$) applied to both agents:

$$\frac{\lVert\delta_B\rVert_{\text{rms}}}{\lVert\delta_A\rVert_{\text{rms}}} = \frac{(\sigma_{\text{base}} + \gamma_A \mathcal{T}_A)\sqrt{\mathcal{T}_A}}{(\sigma_{\text{base}} + \gamma_B \mathcal{T}_B)\sqrt{\mathcal{T}_B}}$$

In the coupling-dominant, symmetric limit:

$$\frac{\lVert\delta_B\rVert_{\text{rms}}}{\lVert\delta_A\rVert_{\text{rms}}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^{3/2}$$

The exponent is $b = 3/2$. $\square$

**Why 3/2, not 2.** The half-power difference between the template's Model D ($1/\alpha$) and Model S ($1/\sqrt{\alpha}$) scalings propagates through the ratio. Numerator contributes $\mathcal T_A^1$ from the coupling; denominator contributes $\mathcal T_B^{1/2}$ from noise averaging; combined with the $A$-side $1/\mathcal T_A^{1/2}$ gives $\mathcal T_A^{3/2}/\mathcal T_B^{3/2}$.

### Summary of Regime-Dependent Exponents

| Regime | Coupling type | Dominance | Exponent $b$ | Source |
|:---|:---|:---|:---:|:---|
| 1 | Deterministic drift (Model D) | Coupling-dominant | $2$ | Derived above |
| 2 | Stochastic noise (Model S) | Coupling-dominant | $3/2$ | Derived above |
| 3 | Either | Non-coupling-dominant | $\to 1$ (det.) or $\to 1/2$ (stoch.) | Asymptotic limit |

**Regime 3 (non-coupling-dominant).** When $\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$ (or $\sigma_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$), the base disturbance dominates and the coupling terms become a perturbation. The mismatch ratio degrades toward $\mathcal T_A / \mathcal T_B$ (linear, $b = 1$) for Model D, or toward $(\mathcal T_A / \mathcal T_B)^{1/2}$ for Model S.

The simulation validation across all three regimes is in #result-adversarial-exponent-regimes.

---
