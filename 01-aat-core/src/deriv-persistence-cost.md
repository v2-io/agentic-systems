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

AAT's persistence machinery establishes that under the sector condition, the estimation error stays bounded. It does not quantify the *sustained rate of effort* an agent must expend to hold that bound. Two agents with identical persistence guarantees can face very different demands — a Kalman filter tracking a slowly drifting process and one tracking a fast one are both persistent; one is nearly dormant, the other running hot. Under Model S with a Gaussian Ornstein–Uhlenbeck signal, any causal estimator that holds the per-component mean-square estimation error at $D$ must take in information about the signal at a rate of at least $n(\sigma_{\text{env}}^2/(2D) - \lambda_s)$ nats per unit time. That is the sequential (causal) rate-distortion function of the signal. The Kalman–Bucy filter meets it with equality, and its rate is $nK/2$, half its own correction gain per component. For the Kalman-optimal agent the price of persistence is therefore $n\alpha/2$ nats per unit time, and the observation channel must have capacity at least $\mathcal{T}/2$ per dimension. Every linear corrector on the same channel takes in that same rate, $nK/2$, whatever its gain; a mis-tuned one pays it for a larger error, and the bound evaluated at its error is slack.

The bound is *filter-agnostic*: it holds for any causal estimator under the stated scope, and it is stated in the error the agent actually achieves. It is also *substrate-agnostic*: Landauer's principle converts it to a thermodynamic dissipation floor in any physical realization (Still et al. 2012). The channel-capacity floor matters in three regimes where observation bandwidth is scarce: biological systems with finite neural channel capacity, bandwidth-constrained distributed systems over noisy or low-bandwidth links, and context-window-limited language models where effective information rate per unit of cognition is bounded by context size and token throughput. Survival, in this framework, is not a state achieved once — it is a *sustained burn rate* of information, and the channel that supports it is part of what keeps the agent in scope.

## Formal Expression

### Setup

The signal is $n$-dimensional with independent Ornstein–Uhlenbeck components, $dx_i = -\lambda_s x_i\,dt + \sigma_{\text{env}}\,dW_i$, observed through $dy_i = x_i\,dt + \sigma_\nu\,dV_i$. Here $\sigma_{\text{env}}$ is the signal's own diffusion (environmental change) and $\sigma_\nu$ the channel-noise intensity. The agent's estimate $\hat x$ is causal: it depends only on observations up to the present. The persistence state is the estimation error $\delta = x - \hat x$ ( #def-mismatch-signal), with per-component steady-state mean square $D$. Under Prop A.1S ( #deriv-sector-condition) its value for a linear corrector with gain $\alpha$ includes the channel noise the correction feeds back: $D = (\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2(\lambda_s + \alpha))$ ( #deriv-sector-condition, Setup). The error contracts at rate $\lambda_s + \alpha$, the signal's own decay plus the gain; for the random-walk signal $\lambda_s = 0$ this is the sector rate of #der-gain-sector-bridge, and for $\lambda_s \gt 0$ the gain is the part of the contraction the agent supplies. Here $\sigma_{\text{env}}$ and $\sigma_\nu$ are the environmental and channel-noise intensities of #deriv-sector-condition's Setup, whose total disturbance $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$ is not used in this segment.

### Persistence Information Rate (main theorem)

*[Derived (persistence-information-rate, from the sequential rate-distortion function)]*

**Proposition.** Any causal estimator that holds the per-component steady-state mean-square estimation error at $D \leq \sigma_{\text{env}}^2/(2\lambda_s)$ must take in information about the signal at a sustained rate

$$\boxed{\;\dot R \;\geq\; n\left(\frac{\sigma_{\text{env}}^2}{2D} - \lambda_s\right) \text{ nats per unit time}\;}$$

**Derivation.** For a scalar Gauss–Markov source $x_{k+1} = a x_k + w_k$, $w_k \sim \mathcal N(0, W)$, the sequential rate-distortion function — the least directed information from source to reproduction per step for any causal scheme meeting mean-square error $D$ at each step — is $\tfrac12 \log(a^2 + W/D)$ when that is positive, and is attained by a linear-Gaussian sensor followed by a Kalman filter (Tanaka, Kim, Parrilo & Mitter 2017, "Semidefinite programming approach to Gaussian sequential rate-distortion trade-offs," *IEEE Trans. Autom. Control* 62(4):1896–1910, doi:10.1109/TAC.2016.2601148, eq. (28); the sequential rate-distortion function is Tatikonda's, Tatikonda, Sahai & Mitter 2004, *IEEE Trans. Autom. Control* 49(9):1549–1561). Sample the OU component at step $\Delta$: $a = e^{-\lambda_s\Delta}$ and $W = \sigma_{\text{env}}^2(1 - e^{-2\lambda_s\Delta})/(2\lambda_s)$, so $a^2 + W/D = 1 - 2\lambda_s\Delta + \sigma_{\text{env}}^2\Delta/D + O(\Delta^2)$. The rate per step is $\tfrac12(\sigma_{\text{env}}^2/D - 2\lambda_s)\Delta + O(\Delta^2)$, and per unit time, as $\Delta \to 0$, $\sigma_{\text{env}}^2/(2D) - \lambda_s$. Independent components add. $\square$

The continuous-time statement is this limit of the exact discrete-time result; the Kalman–Bucy closed form below meets it exactly, which is an independent check. A non-causal reproduction (one that may look ahead) is held only to the classical rate-distortion function, which for OU at high resolution is $2\sigma_{\text{env}}^2/(\pi^2 D)$ by reverse water-filling (Berger 1970, "Information rates of Wiener processes," *IEEE Trans. Inf. Theory* 16(2):134–139, for the Wiener process). That bound is lower and is not met by any filter. An agent acts in real time, so the sequential function is the one that binds.

### Kalman–Bucy Meets the Bound

*[Derived (Kalman-tight, Duncan 1970; Mitter & Newton 2005)]*

By Duncan's theorem (Duncan 1970, "On the calculation of mutual information," *SIAM J. Appl. Math.* 19(1):215–220), the rate at which the observations supply information about the signal to the optimal filter is $\dot I = \tfrac12\operatorname{tr}(H^T \Sigma_o^{-1} H P_{ss})$; per component, $\dot I = P/(2\sigma_\nu^2)$ (the same identity is the information-supply rate of Mitter & Newton 2005, *J. Stat. Phys.* 118:145–176). The steady-state Riccati equation $\sigma_{\text{env}}^2 - 2\lambda_s P - P^2/\sigma_\nu^2 = 0$ gives

$$\frac{P}{2\sigma_\nu^2} = \frac{\sigma_{\text{env}}^2}{2P} - \lambda_s$$

So the Kalman–Bucy filter, at its own error $D = P$, takes in information at exactly the sequential rate-distortion bound, for every $\lambda_s$. **The bound is achieved.** In terms of its correction gain $K = P/\sigma_\nu^2$ (the error contracts at $\lambda_s + K$; for $\lambda_s = 0$ the gain is the sector constant of #der-gain-sector-bridge, scalar Kalman), its rate is

$$\dot I = \frac{K}{2} = \frac{\alpha}{2} \text{ per component}$$

In the drift-dominated limit $\lambda_s \to 0$, $P = \sigma_{\text{env}}\sigma_\nu$ and $K = \sigma_{\text{env}}/\sigma_\nu$.

**The intake is fixed by the channel; the error decides how much of it is used.** For a linear corrector $d\hat x = -(\lambda_s + \alpha)\hat x\,dt + \alpha\,dy$ the path of $\hat x$ determines the path of $y$ ($dy = (d\hat x + (\lambda_s + \alpha)\hat x\,dt)/\alpha$), so $I(x; \hat x) = I(x; y)$, and by Duncan's theorem the observation path carries information about the signal at the rate $P/(2\sigma_\nu^2) = K/2$ per component, where $P$ is the *optimal* filter's error, whatever gain the filter actually runs. Every linear corrector on the channel takes in $nK/2$. A mis-tuned one holds a larger error: for $\lambda_s \to 0$, $D(\alpha) = (\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha) \gt P = \sigma_{\text{env}}\sigma_\nu$ for every $\alpha \neq K$, on either side of $K$. The bound evaluated at that error, $n\sigma_{\text{env}}^2/(2D(\alpha)) = n\alpha\sigma_{\text{env}}^2/(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)$, is then strictly below $nK/2$ and is slack: it is the least any causal estimator would need for that error, not what this one pays. So $n\alpha/2$ is the price *and* the intake only for the Kalman-optimal agent; for any other gain the intake is $nK/2$ and the floor at its error is lower. Holding a target $D$ with a gain $\alpha \neq K$ requires a more informative channel than the floor at $D$ demands, which is the efficiency cost #impl-strategy-dynamics names. In the noiseless-channel limit ($\sigma_\nu \to 0$), holding $D = \sigma_{\text{env}}^2/(2\alpha)$ requires $n\alpha$.

### Channel-Capacity Prerequisite

*[Derived (channel-capacity-floor, from main theorem + Shannon capacity)]*

By Shannon's channel coding theorem (Cover & Thomas 2006 §7.7), an observation channel of capacity $C_{\text{channel}}$ supports no information rate above $C_{\text{channel}}$. Holding the estimation error at $D$ therefore requires

$$C_{\text{channel}} \;\geq\; n\left(\frac{\sigma_{\text{env}}^2}{2D} - \lambda_s\right)$$

For the Kalman-optimal agent, with linear correction and $\alpha = \mathcal{T}$ ( #def-adaptive-tempo, #der-gain-sector-bridge):

$$\boxed{\;C_{\text{channel}} \;\geq\; \mathcal{T} / 2 \text{ nats/time per dimension}\;}$$

**Persistence demands observation-channel capacity.** For the optimal agent the floor is half the adaptive tempo. In general it is fixed by the error the agent must hold. This is a first-class persistence diagnostic beside the correction-rate inequality. It binds in capacity-constrained settings — bandwidth-limited distributed systems, biological neurons, context-window-limited LLMs — where the tempo framework alone underestimates the difficulty of holding a bounded error.

### Rejected Candidate Cost Metrics

The information-rate bound is not the only candidate for a cost-of-persistence quantity. Three alternatives fail structurally. Recording them here keeps the scope-honesty visible.

*[Observation (gain-magnitude-tautological)]* $\mathbb{E}[\lVert K(t)\rVert]$ as a cost metric: in the linear Kalman case $K_{ss} = \alpha$ (sub-scope $\alpha$ per #der-gain-sector-bridge), so "gain magnitude" equals the sector constant itself. Any bound of shape $\mathbb{E}[\lVert K\rVert] \geq f(\alpha, \ldots)$ becomes tautological. Rejected as fundamental cost metric — it recapitulates $\alpha$.

*[Observation (control-effort-filter-specific)]* $\mathbb{E}[\lVert u(t)\rVert^2]$ (per-unit-time control-effort integral): filter-specific. Different filters achieving the same steady-state variance $P_{ss}$ have different control-effort integrals. The Kalman filter is minimum-effort among linear filters (optimal-control interpretation of the Riccati equation); nonlinear filters can trade effort vs variance differently. A filter-agnostic bound cannot be stated in this quantity — it is not invariant under the equivalence class of filters meeting the persistence condition.

*[Observation (Lyapunov-dissipation-conservation)]*
$\mathbb{E}[\alpha\lVert\delta\rVert^2]_{ss}$ (Lyapunov dissipation rate) at steady state equals half the total disturbance power injected into the estimation error, $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/2$ for linear correction — a non-equilibrium-steady-state balance (dissipation balances injection). It does not distinguish a well-adapted agent from a poorly adapted one at a given $\alpha$, so it cannot serve as a cost metric.

The Shannon information rate above is the one that closes. The structural reason: it is filter-agnostic (it depends only on the signal's second-order statistics and the error held), universal (every causal estimator is lower-bounded), met with equality by the optimal filter, and has a clean thermodynamic interpretation (Still et al. 2012, "Thermodynamics of Prediction", *Phys. Rev. Lett.* 109:120604: nonpredictive information retained equals dissipation during interaction).

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Persistence information rate $\dot R \geq n(\sigma_{\text{env}}^2/(2D) - \lambda_s)$ | Sequential RDF of a Gauss–Markov source (Tanaka et al. 2017 eq. (28)), continuous-time limit | Derived (conditional on Gaussian-OU signal, causal estimation; continuous time as the limit of the discrete result) |
| Kalman–Bucy meets the bound; its rate is $nK/2$ | Duncan 1970 + steady-state Riccati identity | Derived (linear-Gaussian, every $\lambda_s$) |
| Price $n\alpha/2$ | The two rows above with $\alpha = K$ | Derived for the Kalman-optimal agent; for other gains the intake is $nK/2$ (Duncan; the filter's path determines the observation path) and the floor at the error held is lower and slack |
| Channel-capacity prerequisite $C \geq \mathcal{T}/2$ | Main theorem + Shannon channel-capacity theorem (Cover-Thomas 2006 §7.7) + $\alpha = \mathcal{T}$ identification | Derived for the Kalman-optimal agent; general form $C \geq n(\sigma_{\text{env}}^2/(2D) - \lambda_s)$ |
| Gain-magnitude as cost metric | $\mathbb{E}[\lVert K\rVert] \approx \alpha$ in sub-scope $\alpha$ | Rejected as fundamental (tautological) |
| Control-effort integral as cost metric | Filter-specific; depends on optimality class | Rejected as universal (filter-dependent) |
| Lyapunov dissipation rate | Balance with total injected disturbance power at steady state | Not a cost metric |
| Non-Gaussian signal extension | Different RDF form (Berger 1971 Ch. 4) | Open — the $1/D$ scaling of the rate is expected to persist qualitatively; prefactors change |
| Model D (bounded disturbance) analog | Requires adversarial / minimax information argument (Csiszár-Körner 2011 Ch. 11) | Open |
| Transient-regime rate | Bound is steady-state; transient rates during structural adaptation much higher | Open |
| Sub-scope $\beta$ transfer | The bound holds for any causal estimator; tightness not guaranteed | Conditional (holds as lower bound; tightness requires the optimal linear-Gaussian filter) |

## Epistemic Status

*Conditional.* Max attainable: *exact* in the linear-Gaussian case; *robust qualitative* for general stationary Gaussian signals; *heuristic* for non-Gaussian.

The theorem rests on three named conditions: (i) a Gaussian Ornstein–Uhlenbeck signal with independent components; (ii) causal estimation, which every acting agent satisfies; (iii) steady state. The discrete-time sequential rate-distortion function is exact (Tanaka et al. 2017); the continuous-time bound is its $\Delta \to 0$ limit, taken here term by term rather than by a limit theorem, and is met exactly by the Kalman–Bucy closed form. That match was also checked numerically: for three parameter sets the discrete per-step bound divided by $\Delta$ converges to the Kalman–Bucy rate $P/(2\sigma_\nu^2)$ as $\Delta \to 0$. Under Model D (bounded disturbance) the argument requires worst-case channel-capacity machinery (Csiszár-Körner 2011 Ch. 11) and gives a different expression.

**Sub-scope transfer.** The bound is stated in the error achieved, so it holds for any causal estimator, in sub-scope $\alpha$ or $\beta$. The $n\alpha/2$ form uses $\alpha = K$ and so belongs to the optimal linear-Gaussian agent; for other agents the error they hold sets the floor, which is what they would need at least, while what a linear corrector on a Gaussian channel actually takes in is $nK/2$ regardless of its gain.

**Confidence in correctness.** The sequential rate-distortion function of a Gauss–Markov source is a published closed form, and Duncan's theorem is classical. The composition is short enough to check by hand, and both closed forms agree. The contribution is the AAT reading: holding the persistence bound is a sustained information demand, met with equality by the optimal filter at half its correction gain, and the channel capacity that supplies it is a persistence prerequisite.

**What this does not establish.**

- Upper bounds on persistence cost (how much rate a specific filter consumes; the bound is a lower limit).
- Optimal filter design for minimum information throughput.
- Non-Gaussian signal cost bounds (qualitative scaling expected; quantitative forms open).
- Cost under Model D adversarial disturbance.
- Cost for composite agents beyond simple additivity.
- The stability upper bound on plasticity that #form-consolidation-dynamics references — that involves the consolidation cadence, not the online information rate.

## Discussion

**The $\alpha/2$ per-dimension Landauer analog.** The theorem has a clean thermodynamic reading per Still et al. 2012: each nat of information about the signal costs at least $k_BT$ of dissipation (Landauer 1961, in its per-nat form $k_BT$/nat, equivalently $k_BT\ln 2$ per bit). Combined, the Kalman-optimal agent persisting at sector constant $\alpha$ in $n$ dimensions takes in $n\alpha/2$ nats/time and so dissipates at least $\tfrac{1}{2} n\alpha\, k_BT$ per unit time in any physical substrate. AAT does not commit to a specific substrate, but the bound is substrate-agnostic: it constrains any filter implementation via the rate-distortion function (information-theoretic) and, when physical, any computational realization via Landauer (thermodynamic).

**Why channel capacity matters as a first-class quantity.** AAT's #result-persistence-condition and #def-adaptive-tempo frame persistence as a correction-rate vs disturbance-rate inequality. This theorem adds a *lower* constraint: the observation channels must supply the information rate the error requires — $\mathcal{T}/2$ nats/time per dimension for the optimal agent — or persistence fails regardless of correction-function design. The constraint is binding wherever observation bandwidth is scarce. Three domains where the capacity floor is more binding than the tempo bound:

- *Biological systems*: neural channel capacity is finite; this bound gives a quantitative minimum on sensory bandwidth for a given adaptive rate.
- *Bandwidth-constrained distributed systems*: agents operating over noisy or low-bandwidth links face channel capacity directly as a hard constraint.
- *Context-window-limited LLMs*: the effective information rate per unit of cognition is bounded by context size and token-throughput; this theorem predicts a minimum tempo achievable at a given context budget.

In each, knowing that $\mathcal{T}/2$ is the floor for the optimal agent converts an opaque "just needs more capacity" observation into a specific dimensional requirement.

**Connection to AAT's meta-architecture.** The result composes with AAT's three meta-segments.

- *#disc-separability-pattern (positive half)*: the bound sits in structured-repair along the identification-regime ladder — derived from an external theorem, met with equality in the linear-Gaussian case, holding as an inequality elsewhere.
- *#disc-identifiability-floor (negative half)*: this is the positive-dual of the floor pattern. Where the floor says "AAT cannot distinguish X without information augmentation" (external no-go + AAT escape), this result says "holding the error at $D$ requires at least $n(\sigma_{\text{env}}^2/(2D) - \lambda_s)$ nats/time of information supply" (external lower bound + AAT bridge through the persistence bound). The two patterns are duals: external-theorem-forbids vs external-theorem-lower-bounds.
- *#disc-additive-coordinate-forcing (constructive half)*: the bound is linear in $1/D$ (and in $\alpha$ for the optimal agent), not logarithmic. It sits *outside* the three-layer logarithmic-coordinate family (chain / divergence / update). No Cauchy-FE argument forces the coordinate here. This is a useful non-example: AAT's additive-coordinate-forcing pattern is not universal; specific results live on different coordinates.

**Relationship to #result-sector-persistence-template.** The template enumerates instantiations (epistemic mismatch; strategic mismatch; sub-agent mismatch; composite trajectory error; composite mismatch; target-agent mismatch). Each has its own state variable $\xi$, sector constant $\alpha$, and disturbance statistics. The persistence cost bound *specializes* for each instantiation in which the state is an estimation error of a Gauss–Markov signal: the rate is fixed by the error held, and by $n\alpha/2$ when the corrector is the optimal one. A compact template-cost bound could land as a subsection of #result-sector-persistence-template so the instances inherit it by substitution. That move is flagged in Working Notes as an optional consolidation.

**The relationship to Mitter-Newton's thermodynamic reading.** Mitter & Newton (2005) showed the Kalman-Bucy filter operates as a Maxwellian demon: it returns signal energy to the heat bath without entropy increase, but only because new information is continually supplied at rate $\dot I$. This supply rate *is* what persistence costs — the filter holds a bounded estimation error by paying, information-theoretically, for new observations at a rate matched to the environment's innovation rate. The theorem makes this quantitative: the rate equals the least any causal estimator could pay for the same error, and it is half the filter's correction gain.

## Working Notes

- **Template-cost subsection.** A compact parametric statement — "under (T1)–(T3) with Model S and a Gauss–Markov signal with per-component parameters $(\lambda_\xi, \sigma_\xi^2)$, holding per-component mean-square $\xi$ at $D$ requires $\dot R \geq n(\sigma_\xi^2/(2D) - \lambda_\xi)$ nats/time, with equality for the optimal linear-Gaussian corrector" — would let each of #result-sector-persistence-template's instances inherit the cost bound by substitution. It applies only to instances whose state is the estimation error of a signal observed through a channel; check that per instance before substituting.
- **Model D adversarial analog.** Rate-distortion is inherently stochastic; Model D's bounded-disturbance version of the theorem requires minimax / worst-case channel capacity (Csiszár-Körner 2011 Ch. 11). Candidate follow-up spike. Expected form: similar $\propto \alpha$ scaling, different prefactor.
- **Non-Gaussian signals.** For heavy-tailed or power-law signals the RDF has a different exact form (Berger 1971 Ch. 4). The qualitative scaling $\dot R_{\min} \propto \sigma_{\text{env}}^2/D$ (with $D$ the mean-square error) is expected to persist; quantitative extensions are per-family.
- **Misspecification cost.** When $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ per #def-model-class-fitness, achievable distortion is bounded away from zero by an additional floor.  
  The rate bound is stated in the error held, so a floor $D_{\text{floor}}$ caps the rate that can usefully be spent: no information rate buys an error below $D_{\text{floor}}$. Connects to #disc-identifiability-floor's "Misspecification-cost quantification" open extension.
- **Composite persistence cost.** For a composite agent, the information-rate bound's scaling under composition is not trivial. Candidate: $\dot R_{c,\min} \leq \sum_i \dot R_{i,\min}$ due to coordination overhead eating capacity. Cost-analog of #der-tempo-composition's sub-additivity + #der-team-persistence's cooperative-coupling reduction. Open.
- **Observation-channel capacity as notation.** Currently AAT uses $U_o$ (observation uncertainty) as a noise parameter. Lifting Shannon channel capacity $C^{(k)}$ of channel $k$ into NOTATION.md and relating it to $U_o$ (via the channel-capacity-from-noise standard transform) would make the capacity-floor condition a first-class persistence diagnostic. This is the biggest architectural opening from this theorem and worth a follow-up scoping decision.
- **Connection to #schema-strategy-persistence.** The strategy-edge persistence condition has its own disturbance statistics $\rho_\Sigma$ and sector constant $\alpha_\Sigma$. Specializing this theorem to strategy edges would give the information rate required to track edge invalidation; the $n_\Sigma\alpha_\Sigma/2$ form holds only if the edge corrector is the optimal one for its disturbance. If $\alpha_\Sigma = 1/(n+1)$ with experience discounting, the gain falls with accumulated $n$ — which connects to the stability-induced myopia result in the pending spike G.
- **Not forced by a Cauchy-FE axiom.** Unlike the three primary instances of #disc-additive-coordinate-forcing (chain, divergence, update), the linear-in-$\alpha$ coordinate of this bound is not forced by an AAT-internal additivity axiom. It is a direct consequence of Gaussian-RDF's specific functional form. This places the result *outside* the three-layer family — a useful non-example that shows the additive-coordinate-forcing pattern is not universal.
- **Landauer-coefficient correction (2026-05-30).** The Discussion's thermodynamic-floor coefficient previously read $n\alpha k_BT/(2\ln 2) \approx 0.35\, n\alpha\, k_BT$; that mixed the bit and nat conventions — a spurious $1/\ln 2$ factor multiplying a nats rate under a per-nat $k_BT$ Landauer constant. Since $\dot R$ is in nats and the intended constant is $k_BT$/nat, the floor is $\tfrac{1}{2}\, n\alpha\, k_BT$/time. Corrected here and in the quoting segment #impl-persistence-and-limits. Surfaced by AUDIT-WORKING-526815 (gold-lift sweep).

### Incidental audit gold (lift 2026-05-31)

Orthogonal pedagogical / generative material from the de-novo auditors' working dirs (per `de-novo-audit-instructions.md` §7.15), deduplicated and lightly attributed. Felt-value here was uniformly "monumental / breathtaking" — the segment is where information theory, control theory, and thermodynamics meet. Certified-track items off-ramped at the end.

#### 1. Candidate Brief prose / pre-prose

- **"Ignorance is cheap; epistemology is expensive."** Synchronizing your model with a drifting reality has a hard minimum energy cost: a perfectly efficient agent doing nothing but observing a changing environment still drains its battery (Gemini, AUDIT-WORKING-829314).
- **Survival as a sustained burn rate.** "Survival is not just a state you achieve; it is a sustained burn rate of Shannon information — you must continuously consume $\dot R$ nats/time just to stay alive." The threshold says whether persistence is *possible*; this says what it *costs* (Gemini, AUDIT-WORKING-193847).

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

- **Dimension bookkeeping.** The bound is derived per component and summed over $n$ independent components; there is no $n$ inside the per-component rate.
- **Landauer coefficient $0.35\to0.5$ (RESOLVED — see WN above).** 471203 quoted the thermodynamic floor as $\approx 0.35\,n\alpha\,k_BT$; corrected to $\tfrac12 n\alpha\,k_BT$ per the 2026-05-30 Landauer-coefficient note above.
