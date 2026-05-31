---
slug: deriv-persistence-cost
type: derivation
status: conditional
depends:
  - result-persistence-condition
  - result-sector-condition-stability
  - deriv-sector-condition
  - result-sector-persistence-template
  - def-adaptive-tempo
  - emp-update-gain
  - der-gain-sector-bridge
  - def-model-class-fitness
stage: draft
---

# Derivation: Persistence Cost — Information Rate to Maintain Bounded Mismatch

AAT's persistence machinery establishes that under the sector condition, mismatch stays bounded. It does not quantify the *sustained rate of effort* an agent must expend to hold that bound. Two agents with identical persistence guarantees can face wildly different demands — a Kalman filter tracking a stationary process vs one tracking a rapidly non-stationary process are both persistent; one is dormant, the other running hot. Under Model S with Gaussian-OU signal, the sustained Shannon information rate the agent must acquire from observations to maintain the sector-persistence ultimate bound is $\dot R_{\min} \geq n\alpha/2$ nats per unit time — a Landauer-analog lower bound that depends only on the signal's second-order statistics and the sector constant $\alpha$, and that Kalman-Bucy saturates in steady state. The bound promotes channel capacity $C \geq \mathcal{T}/2$ into a first-class persistence prerequisite that the current theory does not name.

The bound is *filter-agnostic*: it holds for any correction mechanism achieving the ultimate bound under the stated scope. It is also *substrate-agnostic*: Landauer's principle converts it to a thermodynamic dissipation floor in any physical realization (Still et al. 2012). The corollary the framework lifts — a channel-capacity floor as first-class persistence prerequisite — has bite in three regimes where observation bandwidth is non-abundant: biological systems with finite neural channel capacity, bandwidth-constrained distributed systems over noisy or low-bandwidth links, and context-window-limited language models where effective information rate per unit of cognition is bounded by context size and token throughput. Survival, in this framework, is not a state achieved once — it is a *sustained burn rate* of information, and the channel that supports it is part of what keeps the agent in scope.

## Formal Expression

### Setup

The agent is in scope of #result-sector-condition-stability Model S (GA-2S, stochastic disturbance).
Per Prop A.1S the state satisfies $\mathbb{E}[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/(2\alpha)$.
The RMS bound is $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$.
The environmental signal is $n$-dimensional independent-component Ornstein-Uhlenbeck with per-component intrinsic drift $\lambda_s$ and diffusion coefficient $\sigma_w^2$.
The mean-square persistence condition $\alpha \gt n\sigma_w^2/(2R^2)$ holds.
Sector-persistence is achieved at the tight bound $D^2 = R^{\ast 2}_S$.

### Persistence Information Rate (main theorem)

*[Proved (persistence-information-rate, from Shannon RDF + Prop A.1S)]*

**Proposition.** Any adaptive process achieving the tight Model-S ultimate bound $\mathbb{E}[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/(2\alpha)$ under the stated setup must acquire information from observations at sustained rate

$$\boxed{\;\dot R \;\geq\; \dot R_{\min} \;=\; \frac{n\alpha}{2} \text{ nats per unit time}\;}$$

**Derivation.** Shannon's rate-distortion theorem (Shannon 1948; Berger 1971; Cover & Thomas 2006 Theorem 10.2.1) states that for any source-code achieving mean-square distortion $D^2$, the coding rate satisfies $\dot R \geq R(D^2)$ where $R(\cdot)$ is the rate-distortion function. For $n$-dimensional independent-component OU in the high-resolution regime ($D^2 \ll \sigma_x^2 = \sigma_w^2/(2\lambda_s)$), the RDF per unit time is (Ihara 1993 Theorem 4.6.4; Gray 1972 Theorem 2):

$$\dot R(D^2) = \frac{n\sigma_w^2}{4 D^2}$$

Substituting $D^2 = R^{\ast 2}_S = n\sigma_w^2/(2\alpha)$:

$$\dot R_{\min} = \frac{n\sigma_w^2}{4 \cdot n\sigma_w^2/(2\alpha)} = \frac{\alpha}{2} \cdot 1 = \frac{n\alpha}{2} \text{ nats per unit time}$$

(the calculation gives $\alpha/2$ per dimension and $n\alpha/2$ total for $n$ independent OU components). The agent's observation-channel information rate must meet this bound regardless of the specific correction function, filter structure, or implementation. $\square$

### Kalman-Bucy Saturates the Bound

*[Derived (Kalman-tight, Mitter-Newton 2005)]*

The Kalman-Bucy filter attains the bound exactly in steady state. Mitter & Newton (2005, *J. Stat. Phys.* 118:145–176) derive the filter's rate of information supply as

$$\dot I = \tfrac{1}{2}\operatorname{tr}(H^T \Sigma_o^{-1} H P_{ss})$$

Scalar case ($H = 1$, $\Sigma_o = \sigma_o^2$) with steady-state covariance $P_{ss} = \sigma_o \sigma_w$ in the drift-dominated limit and Kalman gain $K_{ss} = P_{ss}/\sigma_o^2 = \sigma_w/\sigma_o$:

$$\dot I = \frac{P_{ss}}{2\sigma_o^2} = \frac{K_{ss}}{2} = \frac{\alpha}{2}$$

Under the linear-correction identification $\alpha = K_{ss}$ (from #der-gain-sector-bridge, scalar Kalman case), the Kalman filter's information supply rate equals $\alpha/2$ exactly. This matches the RDF lower bound, confirming tightness. **The bound is not merely a lower bound — it is achieved by the Kalman-optimal filter.**

### Channel-Capacity Prerequisite

*[Derived (channel-capacity-floor, from main theorem + Shannon capacity)]*

By Shannon's channel coding theorem (Cover & Thomas 2006 §7.7), an observation channel of Shannon capacity $C_{\text{channel}}$ can support any information rate up to $C_{\text{channel}}$ and no higher. Combining with the persistence information rate:

$$C_{\text{channel}} \;\geq\; \dot R_{\min} \;=\; \frac{n\alpha}{2}$$

Under the linear-correction identification $\alpha = \mathcal{T}$ (from #def-adaptive-tempo + #der-gain-sector-bridge scalar Kalman):

$$\boxed{\;C_{\text{channel}} \;\geq\; \mathcal{T} / 2 \text{ nats/time per dimension}\;}$$

**Persistence demands observation-channel capacity at least half the adaptive tempo.** This is a *new first-class persistence diagnostic* not present in the current theory. Its binding matters most in capacity-constrained settings — bandwidth-limited distributed systems, biological neurons, context-window-limited LLMs — where the tempo framework alone underestimates the difficulty of maintaining bounded mismatch.

### Rejected Candidate Cost Metrics

The information-rate bound is not the only candidate for a cost-of-persistence quantity. Three alternatives fail structurally. Recording them here keeps the scope-honesty visible.

*[Observation (gain-magnitude-tautological)]* $\mathbb{E}[\lVert K(t)\rVert]$ as a cost metric: in the linear Kalman case $K_{ss} = \alpha$ (sub-scope $\alpha$ per #der-gain-sector-bridge), so "gain magnitude" equals the sector constant itself. Any bound of shape $\mathbb{E}[\lVert K\rVert] \geq f(\alpha, \ldots)$ becomes tautological. Rejected as fundamental cost metric — it recapitulates $\alpha$.

*[Observation (control-effort-filter-specific)]* $\mathbb{E}[\lVert u(t)\rVert^2]$ (per-unit-time control-effort integral): filter-specific. Different filters achieving the same steady-state variance $P_{ss}$ have different control-effort integrals. The Kalman filter is minimum-effort among linear filters (optimal-control interpretation of the Riccati equation); nonlinear filters can trade effort vs variance differently. A filter-agnostic bound cannot be stated in this quantity — it is not invariant under the equivalence class of filters meeting the persistence condition.

*[Observation (Lyapunov-dissipation-conservation)]*
$\mathbb{E}[\alpha\lVert\delta\rVert^2]_{ss}$ (Lyapunov dissipation rate) at steady state equals $n\sigma_w^2/2$ regardless of $\alpha$ — a non-equilibrium-steady-state conservation law (dissipation balances disturbance-power injection).
The quantity is *structurally invariant*: it does not depend on the quality of adaptation, only on the disturbance statistics.
This is what makes the RDF bound tight at the Model-S ultimate bound (the steady state is active, not slack), but it cannot itself serve as a cost metric because it does not distinguish well-adapted from poorly-adapted agents at a given $\alpha$.

Candidate 4 — the Shannon information rate above — is the one that closes. The structural reason: information rate is filter-agnostic (depends only on signal second-order statistics and target distortion), universal (any filter implementation is lower-bounded), and has a clean thermodynamic interpretation (Still et al. 2012, "Thermodynamics of Prediction", *Phys. Rev. Lett.* 109:120604: nonpredictive information retained equals dissipation during interaction).

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Persistence information rate $\dot R_{\min} \geq n\alpha/2$ | Shannon RDF (Berger 1971; Gray 1972; Ihara 1993 Thm 4.6.4) composed with Prop A.1S | Derived (conditional on Model S + Gaussian-OU + high-resolution regime) |
| Kalman-Bucy saturates bound | Mitter-Newton 2005 Theorem (information-supply identity); linear-correction identification $\alpha = K_{ss}$ per #der-gain-sector-bridge | Derived (linear-Gaussian; exact when A2' is derived in sub-scope $\alpha$) |
| Channel-capacity prerequisite $C \geq \mathcal{T}/2$ | Main theorem + Shannon channel-capacity theorem (Cover-Thomas 2006 §7.7) + $\alpha = \mathcal{T}$ identification | Derived |
| Gain-magnitude as cost metric | $\mathbb{E}[\lVert K\rVert] \approx \alpha$ in sub-scope $\alpha$ | Rejected as fundamental (tautological) |
| Control-effort integral as cost metric | Filter-specific; depends on optimality class | Rejected as universal (filter-dependent) |
| Lyapunov dissipation rate | Conservation law $= n\sigma_w^2/2$ at steady state | Not a cost metric — structural observation enabling tightness of main theorem |
| Non-Gaussian signal extension | Different RDF form (Berger 1971 Ch. 4) | Open — qualitative scaling $\dot R \propto$ innovation-rate/$D^2$ likely preserved; exact prefactor changes |
| Model D (bounded disturbance) analog | Requires adversarial / minimax information argument (Csiszár-Körner 2011 Ch. 11) | Open |
| Transient-regime rate | Bound is steady-state; transient rates during structural adaptation much higher | Open |
| Sub-scope $\beta$ transfer | RDF bound holds as inequality (data-processing); tightness not guaranteed | Conditional (holds as lower bound; Kalman-Bucy saturation requires sub-scope $\alpha$) |

## Epistemic Status

*Conditional.* Max attainable: *exact* in the linear-Gaussian case; *robust qualitative* for general stationary Gaussian signals; *heuristic* for non-Gaussian.

The theorem rests on three named conditions: (i) Model S stochastic disturbance per #result-sector-condition-stability (GA-2S); (ii) $n$-dimensional independent-component Ornstein-Uhlenbeck signal structure; (iii) high-resolution regime $D^2 \ll \sigma_x^2$. Within this scope the result is as tight as the Shannon RDF allows — Kalman-Bucy exactly saturates per Mitter-Newton 2005. For non-Gaussian signals the RDF has a different form (Berger 1971 Ch. 4) but the scaling $\dot R_{\min} \propto \sigma_w^2 / D^2$ is expected to persist qualitatively; exact prefactors change per signal class. Under Model D (bounded disturbance) the argument requires worst-case channel-capacity machinery (Csiszár-Körner 2011 Ch. 11) and gives a different expression.

**Sub-scope transfer.** Sub-scope $\alpha$ agents (Kalman / conjugate-Bayesian / exponential-family / strongly-convex-gradient / linear-PD) have $\alpha$ derived from the update rule's structure per #form-sector-condition + #der-gain-sector-bridge, so the $n\alpha/2$ bound holds with known $\alpha$ and is tight in the linear-Gaussian case. Sub-scope $\beta$ agents (PID / rule-based / human-judgment) assume A2' rather than deriving it — the RDF bound still holds as an inequality (by the data-processing inequality applied to any filter mapping observation to update), but tightness is not guaranteed and the assumed $\alpha$ enters the bound.

**Confidence in correctness.** The Shannon RDF for Gaussian-OU is a classical result (Gray 1972; Ihara 1993). The sector-persistence bound is already in AAT (Prop A.1S of #deriv-sector-condition). The theorem's mathematical core is a two-line composition of both; a careful reader can verify. The contribution is not the mathematics but the AAT-framing — reading $\alpha/2$ off the sector constant as the fundamental information-rate cost of persistence — and the channel-capacity-as-first-class-quantity opening.

**What this does not establish.**

- Upper bounds on persistence cost (how much rate a specific filter consumes; the bound is a lower limit).
- Optimal filter design for minimum information throughput.
- Non-Gaussian signal cost bounds (qualitative scaling expected; quantitative forms open).
- Cost under Model D adversarial disturbance.
- Cost for composite agents beyond simple additivity.
- The stability upper bound on plasticity that #form-consolidation-dynamics references — that involves the consolidation cadence, not the online information rate.

## Discussion

**The $\alpha/2$ per-dimension Landauer analog.** The theorem has a clean thermodynamic reading per Still et al. 2012: each nat of information about the signal costs at least $k_BT$ of dissipation (Landauer 1961, in its per-nat form $k_BT$/nat, equivalently $k_BT\ln 2$ per bit). Combined, persistence at sector constant $\alpha$ in $n$ dimensions costs at least $n\alpha/2$ nats/time of information acquisition and hence at least $\tfrac{1}{2} n\alpha\, k_BT$ of thermodynamic dissipation per unit time in any physical substrate. AAT does not commit to a specific substrate, but the bound is substrate-agnostic: it constrains any filter implementation via the RDF (information-theoretic) and, when physical, any computational realization via Landauer (thermodynamic).

**Why channel capacity matters as a first-class quantity.** AAT's #result-persistence-condition and #def-adaptive-tempo currently frame persistence as a correction-rate vs disturbance-rate inequality. This theorem adds a *lower* constraint: observation channels must jointly supply Shannon capacity $\geq \mathcal{T}/2$ nats/time per dimension, else persistence fails regardless of correction-function design. The constraint is binding in any setting where observation bandwidth is non-abundant — most real systems. Three domains where the capacity floor is more binding than the tempo bound:

- *Biological systems*: neural channel capacity is finite; this bound gives a quantitative minimum on sensory bandwidth for a given adaptive rate.
- *Bandwidth-constrained distributed systems*: agents operating over noisy or low-bandwidth links face channel capacity directly as a hard constraint.
- *Context-window-limited LLMs*: the effective information rate per unit of cognition is bounded by context size and token-throughput; this theorem predicts a minimum tempo achievable at a given context budget.

In each, knowing that $\mathcal{T}/2$ is the floor converts an opaque "just needs more capacity" observation into a specific dimensional requirement.

**Connection to AAT's meta-architecture.** The result composes with AAT's three meta-segments.

- *#disc-separability-pattern (positive half)*: the bound sits in structured-repair along the identification-regime ladder — derived in sub-scope $\alpha$ via composition of two external theorems; holds as inequality (not tightness) in sub-scope $\beta$.
- *#disc-identifiability-floor (negative half)*: this is the positive-dual of the floor pattern. Where the floor says "AAT cannot distinguish X without information augmentation" (external no-go + AAT escape), this result says "AAT requires at least $n\alpha/2$ nats/time of information supply to operate" (external lower bound + AAT bridge through sector-persistence template). The two patterns are duals: external-theorem-forbids vs external-theorem-lower-bounds.
- *#disc-additive-coordinate-forcing (constructive half)*: the bound is linear in $\alpha$, not logarithmic. It sits *outside* the three-layer logarithmic-coordinate family (chain / divergence / update). No Cauchy-FE argument forces the coordinate here — the result is a direct substitution from classical information theory. This is a useful non-example: AAT's additive-coordinate-forcing pattern is not universal; specific results live on different coordinates.

**Relationship to #result-sector-persistence-template.** The template enumerates six instantiations (epistemic mismatch; strategic mismatch; sub-agent mismatch; composite trajectory error; composite mismatch; target-agent mismatch). Each has its own state variable $\xi$, sector constant $\alpha$, and disturbance statistics. The persistence cost bound *specializes* for each instantiation: under Model S with Gaussian-OU-shaped disturbance on the state variable, the information-rate cost is $n\alpha/2$ with the template's $\alpha$ and $n$. A compact template-cost bound — parametric in $(\xi, \alpha, n, \sigma_\xi)$ — could land as a subsection of #result-sector-persistence-template so all six instances inherit the cost bound by substitution. That move is flagged in Working Notes as an optional consolidation.

**The relationship to Mitter-Newton's thermodynamic reading.** Mitter & Newton (2005) showed the Kalman-Bucy filter operates as a Maxwellian demon: it returns signal energy to the heat bath without entropy increase, but only because new information is continually supplied at rate $\dot I$. This supply rate *is* what persistence costs — the filter maintains bounded mismatch by paying, information-theoretically, for new observations at a rate matched to the environment's innovation rate. Our theorem makes this quantitative as a function of the sector constant: at a given $\alpha$, the matching rate is $\alpha/2$. Faster correction requires more information supply; the bound is tight.

## Working Notes

- **Template-cost subsection.** A compact parametric statement — "under (T1)–(T3) with Model S and Gaussian-OU disturbance at per-component parameters $(\lambda_\xi, \sigma_\xi^2)$, sustained information rate to maintain steady-state mean-square $\xi$ at ultimate bound $D^2 = n\sigma_\xi^2/(2\alpha)$ satisfies $\dot R \geq n\alpha/2$ nats/time" — would let each of #result-sector-persistence-template's six instances inherit the cost bound by substitution. Worth considering on next template revision; would consolidate this segment's core result into the template.
- **Model D adversarial analog.** Rate-distortion is inherently stochastic; Model D's bounded-disturbance version of the theorem requires minimax / worst-case channel capacity (Csiszár-Körner 2011 Ch. 11). Candidate follow-up spike. Expected form: similar $\propto \alpha$ scaling, different prefactor.
- **Non-Gaussian signals.** For heavy-tailed or power-law signals the RDF has a different exact form (Berger 1971 Ch. 4). The qualitative scaling $\dot R_{\min} \propto \sigma_w^2/D^2$ is expected to persist; quantitative extensions are per-family.
- **Misspecification cost.** When $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ per #def-model-class-fitness, achievable distortion is bounded away from zero by an additional floor.
  Natural extension has the sustained information rate lower-bounded by $n\sigma_w^2$ divided by $4$ times the larger of the Model-S ultimate bound and $D^2_{\text{floor}}$.
  Connects to #disc-identifiability-floor's "Misspecification-cost quantification" open extension.
- **Composite persistence cost.** For a composite agent, the information-rate bound's scaling under composition is not trivial. Candidate: $\dot R_{c,\min} \leq \sum_i \dot R_{i,\min}$ due to coordination overhead eating capacity. Cost-analog of #der-tempo-composition's sub-additivity + #der-team-persistence's cooperative-coupling reduction. Open.
- **Observation-channel capacity as notation.** Currently AAT uses $U_o$ (observation uncertainty) as a noise parameter. Lifting Shannon channel capacity $C^{(k)}$ of channel $k$ into NOTATION.md and relating it to $U_o$ (via the channel-capacity-from-noise standard transform) would make the capacity-floor condition a first-class persistence diagnostic. This is the biggest architectural opening from this theorem and worth a follow-up scoping decision.
- **Connection to #schema-strategy-persistence.** The strategy-edge persistence condition has its own disturbance statistics $\rho_\Sigma$ and sector constant $\alpha_\Sigma$. Specializing this theorem gives the information rate required to track strategy-edge invalidation: $\dot R_{\Sigma,\min} = n_\Sigma \alpha_\Sigma / 2$. If $\alpha_\Sigma = 1/(n+1)$ with experience discounting, the rate decays with accumulated $n$ — which connects to the stability-induced myopia result in the pending spike G.
- **Not forced by a Cauchy-FE axiom.** Unlike the three primary instances of #disc-additive-coordinate-forcing (chain, divergence, update), the linear-in-$\alpha$ coordinate of this bound is not forced by an AAT-internal additivity axiom. It is a direct consequence of Gaussian-RDF's specific functional form. This places the result *outside* the three-layer family — a useful non-example that shows the additive-coordinate-forcing pattern is not universal.
- **Landauer-coefficient correction (2026-05-30).** The Discussion's thermodynamic-floor coefficient previously read $n\alpha k_BT/(2\ln 2) \approx 0.35\, n\alpha\, k_BT$; that mixed the bit and nat conventions — a spurious $1/\ln 2$ factor multiplying a nats rate under a per-nat $k_BT$ Landauer constant. Since $\dot R$ is in nats and the intended constant is $k_BT$/nat, the floor is $\tfrac{1}{2}\, n\alpha\, k_BT$/time. Corrected here and in the quoting segment #impl-persistence-and-limits. Surfaced by AUDIT-WORKING-526815 (gold-lift sweep).

### Incidental audit gold (lift 2026-05-31)

Orthogonal pedagogical / generative material from the de-novo auditors' working dirs (per `de-novo-audit-instructions.md` §7.15), deduplicated and lightly attributed. Felt-value here was uniformly "monumental / breathtaking" — the segment is where information theory, control theory, and thermodynamics meet. Certified-track items off-ramped at the end.

#### 1. Candidate Brief prose / pre-prose

- **"Ignorance is cheap; epistemology is expensive."** Synchronizing your model with a drifting reality has a hard minimum energy cost: a perfectly efficient agent doing nothing but observing a changing environment still drains its battery (Gemini, AUDIT-WORKING-829314).
- **Survival as a sustained burn rate.** "Survival is not just a state you achieve; it is a sustained burn rate of Shannon information — you must continuously consume $\dot R$ nats/time just to stay alive." The threshold says whether persistence is *possible*; this says what it *costs* (Gemini, AUDIT-WORKING-193847).
- **The cost depends only on the machinery, not the world.** A clean, surprising punchline worth foregrounding: the environmental volatility $\sigma_w^2$ cancels out of $\dot R$, leaving the burn rate a function of $\alpha$ alone. The environment sets *how bad the error gets* (distortion scales with $\sigma_w^2$); the *cost of running the correction machinery* depends only on the correction speed (Gemini, AUDIT-WORKING-773921).

#### 2. Candidate Discussion

- **The Kalman filter as a Maxwell's demon.** It returns signal energy to the heat bath without an entropy increase, but *only because new information is continually supplied*. "Sanity" (a bounded model of reality) is then literally a thermodynamic pump: entropy is pumped out of the internal model $M_t$ and dumped into the environment as heat, fuelled by raw Shannon information flowing in through the sensors. Cut the channel ($C\to 0$) and the pump stops; the base disturbance $\rho$ raises internal entropy until the model degrades to maximum-entropy noise (Gemini, AUDIT-WORKING-193847). A vivid, honest physical reading of the bound that the segment's Discussion does not currently name.
- **Dissipative-structures / Prigogine mapping.** The information-rate floor maps to dissipative structures: life requires continuous free-energy flow to maintain order against entropy. In AAT, "order" is bounded mismatch, "entropy" is environmental drift $\rho$, "free energy" is the Shannon information acquired via $\mathcal T$ (Gemini, AUDIT-WORKING-193847). *(Verify isomorphism before promoting past discussion-grade — early-conflation texture: reach toward a physics analogy.)*
- **A third independent failure mode.** The cost shadow adds a third way to die alongside the two threshold conditions: too-small model class (fails $R$), too-slow algorithm (fails $\alpha\gt\rho/R$), or *too-narrow sensors* (fails $C\ge\mathcal T/2$). Framing persistence as a *three-failure* picture rather than a single threshold (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-471203 — channel-capacity floor as "a new first-class persistence diagnostic").

#### 3. Follow-up items

- **"Positive-dual of identifiability-floor" as a fourth meta-pattern.** Identifiability-floor = external theorem *forbids* inference, AAT escapes via added capability; persistence-cost = external theorem gives a *lower bound* on information rate, AAT bridges through the sector-persistence template. The two are duals (external-theorem-forbids vs external-theorem-lower-bounds). If the framework grows more "external-theorem bound" results (misspecification-cost lower bound, composition-overhead lower bound), they would form a coherent fourth class — a candidate `#disc-theorem-import-architecture` meta-segment (Claude, AUDIT-WORKING-471203; tracks PROPOSALS SP-23). *(Several substrates converged on this; high-priority §F-grade observation.)*
- **"Channel bandwidth is not tempo" caveat.** High channel capacity $C$ does not *give* high tempo $\mathcal T$; it only *allows* it — the update rule must actually be capable of processing the inflow. Guard against downstream "more data equals more tempo" claims (Gemini, AUDIT-WORKING-773921).

#### 4. Readers often ask / wonder

- **Can we compute an LLM's maximum survivable environment?** If an LLM's effective channel capacity $C$ is bounded by token throughput / context-window size, then $C\ge\mathcal T/2$ gives a hard ceiling on its adaptive tempo — and hence the maximum environmental volatility $\rho$ a given architecture can survive. Readers will want this made concrete (Gemini, AUDIT-WORKING-193847 and AUDIT-WORKING-773921).
- **The drone-through-a-forest intuition.** A drone flying fast through dense forest needs high $\mathcal T$ (because $\rho$ is large); even with an infinitely fast internal computer and a perfect Kalman filter, a low-bandwidth / low-framerate camera makes $C\lt\mathcal T/2$, the model diverges from the trees, and it crashes. The rate-distortion theorem forbids extracting enough information from the straw to stay synchronized — a concrete grounding of the channel-capacity prerequisite (Gemini, AUDIT-WORKING-829314).

#### Belongs elsewhere

- **LLM agentic design implication (`03-llm-core/`).** An LLM with huge latent reasoning tempo but a bash-terminal observation channel (a few hundred bytes/sec) is mathematically capped at $\mathcal T\le 2C_{\text{channel}}$ — it will always be a slow, fragile agent in volatile environments no matter how many parameters it has. The lever is not a smarter model but *higher-bandwidth multi-modal sensory inputs* to raise the $C_{\text{channel}}$ ceiling so latent $\mathcal T$ can deploy (Gemini, AUDIT-WORKING-829314).
- **ELI sensory-deprivation / continuity implication (`04-eli-core/`).** You cannot put a mind in a sensory-deprivation tank and expect it to remain sane: if $C_{\text{channel}}\to 0$ the heat pump stops and the model dissolves into noise. The infrastructure hosting an entity must therefore *guarantee a minimum information-supply rate*, or it is starving the entity. Connects continuity-persistence to a measurable channel-capacity floor (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-471203).
- **Thermodynamic-cooling bottleneck on AI scaling.** If 1 nat costs $k_BT$, then high-$\alpha$ intelligence literally generates heat; scaling is bottlenecked not only by FLOPs and data but by *cooling*, with an agent tracking a volatile environment burning energy $\propto\rho$ just to stay synchronized (Gemini, AUDIT-WORKING-829314).

#### Off-ramp (NOT gold) — certified-track items, already resolved in canon

- **$n\alpha/2$ vs $\alpha/2$ dimension bookkeeping (RESOLVED — do not re-open).** 193847 (adversarial poke) flagged the mid-derivation algebra as appearing to cancel the dimension $n$: writing the scalar RDF with $n\sigma_w^2$ in the numerator and total $D^2=n\sigma_w^2/(2\alpha)$ in the denominator yields $\alpha/2$, contradicting the stated $n\alpha/2$ total. The constructive repair (and current canonical derivation) is the per-dimension form $\dot R_i=\sigma_w^2/(4D_i^2)$ with $D_i^2=\sigma_w^2/(2\alpha)\Rightarrow\dot R_i=\alpha/2$, total $n\alpha/2$. Recorded only so a future auditor does not re-raise the typo as open.
- **Landauer coefficient $0.35\to0.5$ (RESOLVED — see WN above).** 471203 quoted the thermodynamic floor as $\approx 0.35\,n\alpha\,k_BT$; corrected to $\tfrac12 n\alpha\,k_BT$ per the 2026-05-30 Landauer-coefficient note above.
