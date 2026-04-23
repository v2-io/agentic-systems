# Spike: Neutral Drift & Endogenous Coupling — Strengthening Attempt

**Date**: 2026-04-24
**Status**: Exploratory strengthening spike. Prompted by Gemini's reiteration of the "neutral drift / endogenous $\gamma$" gap (after reading `msc/spike-neutral-drift-lyapunov.md` and prior snapshot of Section III).
**Prior art in-project**: `msc/spike-neutral-drift-lyapunov.md` (the original framing of the gap); `msc/spike-miller-act-bridge.md`; `msc/spike-kappa-hb-operationalization.md`; `msc/spike-kappa-topology-insight.md`.
**Segments most relevant to this spike** (post-2026-04-23 state, which is AFTER Gemini's snapshot): `#agent-opacity` (new), `#interaction-channel-classification` (new), `#critical-mass-composition` (new), `#agent-identity` with (PI), `#discussion-identifiability-floor` (including Instance 3 composition-layer), `#loop-interventional-access`, `#agent-spectrum`, `#multi-agent-scope`.

**Brief for the reader:** the gap alleged is that AAD's Lyapunov-persistence machinery uses only behavioral observables $(\alpha, \rho, R)$, so two architecturally different agents with identical behavioral signatures in the current regime are formally indistinguishable — AAD is "blind to neutral drift." Coupling coefficients $\gamma$ are treated as exogenous, blocking a model of niche creation. This spike attempts to *strengthen* rather than soften: derive what AAD can see, name the precise observability conditions under which it cannot, and propose segment-level moves.

---

## 0. Scope audit: what changed since the alleged gap was framed

The allegation rests on a snapshot that predates the 2026-04-23 cycle. Three recent additions bear directly on it:

- **`#agent-opacity`** introduced $H_b^{A\mid B}(t, \tau)$: observer-indexed, horizon-indexed, trajectory-indexed entropy of agent $A$'s future action given $B$'s filtration. This is a *non-$(\alpha, \rho, R)$* behavioral observable.
- **`#interaction-channel-classification`** decomposed recipient-side coupling into four regimes (Informative I / Magnitude-shock II-a / Structural-shock II-b / Ambient III) with boundaries in $(\lVert e\rVert, R, \mathcal I, \mathcal F(\mathcal M), \mathcal I_{\max}, U_o, \nu, c_{\text{floor}})$. Eight quantities, not three.
- **`#discussion-identifiability-floor` Instance 3** (composition-layer, Liberzon 2003): proved a structural no-go — the single bit of coupling sign distinguishing cooperative from adversarial regimes is *unidentifiable from component marginal observation distributions*. Four escapes named: (a) composite-extended loop interventional access; (b) matched-Tier-at-composite; (c) passivity / storage certificate; (d) common contraction metric.

The existence of Instance 3 is the most important pre-existing result for this spike: **AAD has already formalized one version of the gap** (unidentifiable sign of $\gamma$ from marginals), has already named the structural conditions under which identification is recovered, and has already tied those conditions to specific AAD machinery. The question this spike asks is whether the remainder of the "neutral drift" gap — structural variation *within* a contraction-sign class, and the emergence of $\gamma$ itself — admits similar treatment.

The honest accounting at segment level after 2026-04-23:

| Gemini-framed gap | AAD state post-2026-04-23 |
|---|---|
| "State space uses only $(\alpha, \rho, R)$" | Segments carry additional first-class behavioral observables: $H_b$ (`#agent-opacity`), the four-regime tuple (`#interaction-channel-classification`), higher-moment structure (kurtosis diagnostic in `#interaction-channel-classification` Case 4), per-edge opacity $H_b^{e\mid B}$. $(\alpha, \rho, R)$ is the sector-condition triple, not the state space. |
| "Agents with identical $(\alpha, \rho, R)$ are indistinguishable" | FALSE *if* $H_b$ or fluctuation-structure or recipient-regime-distribution is observable; TRUE if all we observe is ultimate-bound statistics on $\lVert\delta\rVert$. The gap was framed too strongly. |
| "Coupling coefficients $\gamma$ are exogenous" | TRUE at `#critical-mass-composition`'s promoted closed form; $\gamma$ enters as formulation (C1). Derivation of $\gamma$ from interaction statistics is not promoted. |
| "AAD cannot model neutral drift" | Partial: neutral drift in the *strict* sense (variation across a behavioral-equivalence class with identical observables at every accessible observer/horizon) is provably invisible by construction, but this is a real no-go. Neutral drift in the *loose* sense (variation in implementation that differs on *some* observer or *some* higher moment) is visible under the 2026-04-23 additions. |
| "AAD cannot model niche creation" | TRUE at formal segment level; `#multi-agent-scope` permits population-level observables but does not carry population-level dynamics. This is an honest gap. |

---

## 1. Strengthening attempt A: Endogenize $\gamma$ from covariance structure

### A.1 The proposal

Treat $\gamma_{ij}$ not as a formulation choice but as a functional of the joint $(\delta_i, \delta_j)$ trajectory. Specifically, under the `#critical-mass-composition` (C1) coupling model $\rho_i^{\text{eff}} = \rho + \gamma \mathcal T_j$, test whether $\gamma$ is recoverable from the Wiener-filter / Granger-causal structure on the composite trajectory $(\delta_1, \delta_2)$.

### A.2 What works: the matched-symmetric-Tier-1 case

*[Claim-tier: derived; exact within the stated construction.]*

Under `#critical-mass-composition`'s (C1)+(C2) and matched-symmetric-Tier-1 (Kalman / exp-family / gradient-strongly-convex / linear-PD), the sub-agent Model D / Model S dynamics are linear in $\delta$ up to the bounded disturbance. In Model S with shared noise covariance $\sigma_w^2$, the steady-state cross-covariance

$$C_{12} := \lim_{t \to \infty} \mathbb E[\delta_1(t)\,\delta_2(t)^\top]$$

satisfies a Lyapunov equation whose solution (Kalman-over-Kalman steady state, directly analogous to the derivation in `#interaction-channel-classification`'s Case 2) yields

$$C_{12} = -\frac{\gamma \mathcal T}{2(\alpha - C)} \cdot \sigma_w^2\,I + O(\gamma^2)$$

*[Derived, conditional on Tier-1 matched symmetric Model S; linearization valid for $\gamma\mathcal T \ll (\alpha - C)R$ i.e. the persistence-margin regime.]*

This is a **sign-preserving scalar** in $\gamma$. Under the bounded-disturbance Model D variant, a parallel derivation using the signed input-to-state-gain matrix yields the same sign.

**Strengthening consequence (candidate).** In the matched-symmetric-Tier-1 + persistence-margin scope, $\gamma$ is identifiable from steady-state cross-covariance up to a normalization from $\sigma_w^2$ (which is itself empirically estimable from each sub-agent's autocovariance). Endogenization succeeds *in this sub-scope*.

### A.3 Where this fails: heterogeneous coupling pattern

*[Claim-tier: robust qualitative; exact counterexample exists.]*

The endogenization above recovers the *scalar* $\gamma$ in the matched-symmetric-Tier-1 construction. It does not survive the full generality of what `#critical-mass-composition` left open:

- **Nonlinear coupling** $\gamma = \gamma(\delta_j)$: the steady-state cross-covariance becomes a functional of the disturbance distribution, not a scalar; recovering the functional requires either high-moment data or explicit perturbation experiments.
- **State-dependent direction** (the "effects-spiral" territory of `#adversarial-destabilization`): no stationary cross-covariance in general; need trajectory-level analysis.
- **Common-latent-driver confound**: a shared disturbance $w$ entering both agents produces cross-covariance *without* coupling. This is exactly `#discussion-identifiability-floor` Instance 2's single-channel mixture problem lifted to the coupling layer — unobservable common cause is unidentifiable from marginals-plus-cross-covariance. Only (a) loop-interventional access on $A$ while observing $B$'s response or (b) instrumenting the latent ("structural priors positing common causes" in Instance 1's route (d) language) escapes it.

The **sign** of $\gamma$ from Instance 3 is recovered in the matched-symmetric-Tier-1 case, but Instance 3's no-go was about exactly this regime's boundary: under *pure marginal* component observation, the sign is invisible. Instance 3 does not forbid recovery from *joint* observation — it forbids recovery from marginal observation. The endogenization above uses *joint* observation (the cross-covariance), so it does not violate Instance 3; it *operationalizes* Instance 3's escape (b) matched-Tier-at-composite.

### A.4 Outcome of A

**Partial strengthening.** $\gamma$ is recoverable as a dynamical variable from cross-covariance in the matched-symmetric-Tier-1 scope under joint observation of the composite trajectory; this operationalizes Instance 3's escape (b) quantitatively rather than qualitatively. For heterogeneous coupling or unobservable common drivers, endogenization meets Instance 3's no-go and requires the loop-interventional-access escape (a).

**What this does not give.** A coupled dynamical system on $(x_i, \gamma_{ij})$ where $\gamma$ itself has a derivation — only an estimator. Going further (a dynamic $\dot\gamma$) requires the niche-creation story in §8 below.

---

## 2. Strengthening attempt B: $H_b$ as the missing state-space dimension

### B.1 The proposal

Two agents with identical $(\alpha, \rho, R)$ but different internals *must* differ on some observable if they are to be called different agents. The `#agent-opacity` $H_b^{A\mid B}$ is indexed by observer, horizon, and trajectory; the equivalence class induced by "identical across all $(B, \tau, \mathcal C)$" is strictly finer than the equivalence class induced by "identical $(\alpha, \rho, R)$." Therefore $H_b$ supplies the structural observable the Gemini gap claimed was absent.

### B.2 What this gets

*[Claim-tier: robust qualitative at segment level; exact as a trivial consequence of information theory when interpreted carefully.]*

Formally, two agents $A$ and $A'$ on the same trajectory $\mathcal C$ with action sequences $\{a_t\}, \{a_t'\}$ that differ on *any* event ($\exists t: a_t \neq a_t'$) satisfy $H_b^{A\mid B}(t^\ast, \tau) \neq H_b^{A'\mid B}(t^\ast, \tau)$ for *some* observer $B$ whose filtration $\mathcal F_B^{t^\ast}$ is fine enough to witness $a_{t^\ast}$. This is a tautology: if actions ever differ, the conditional entropies of actions-given-filtration differ at some filtration.

The *nontrivial* version is: how much does $H_b^{A\mid B}$ discriminate within the $(\alpha, \rho, R)$-equivalence class for *coarse* observers (realistic $B$ with limited filtrations)? Here the answer is empirical and depends on the observer's instrumentation — the honest statement is the `#agent-opacity` segment's observer-indexing commitment.

### B.3 Where the strengthening is genuine

The `#agent-opacity` segment's four-fold indexing — observer, time, horizon, trajectory — gives a structure that the $(\alpha, \rho, R)$ triple lacks: **a pair of agents with identical $(\alpha, \rho, R)$ at the present operating point can differ in $H_b^{A\mid B}$ at future horizons, at finer observers, or at specific points on the trajectory.** The sector condition's equivalence class is a snapshot at the *current disturbance regime and current sector region*; $H_b$ is horizon-indexed, so it sees regime-change *futures* that the sector condition collapses.

**This is the sharpest AAD-native answer to the neutral-drift framing**: the sector condition's equivalence class is defined only on the current $(\alpha, \rho, R)$-scope; horizon-indexed $H_b$ separates agents that differ *on the regime-change that has not yet happened*. Miller's Phases 2–3 (neutral invasion, neutral drift) become visible as $H_b^{A\mid B}(t, \tau_{\text{future}})$ divergence at horizons $\tau$ extending past the scope region where $(\alpha, \rho, R)$ are defined.

*[Claim-tier: robust qualitative. The horizon-indexing move is definitionally available; whether $H_b$ is practically estimable at horizons where the current regime's predictions don't transfer is an empirical question about observer instrumentation.]*

### B.4 The limit

$H_b$ indexes over observers. If *every* observer is restricted to the current-regime filtration — no out-of-regime probing, no interventional access at the boundary — $H_b$ at future horizons is dominated by the observer's prior, not by the agent's internals. The "behavioral equivalence class under Phase 1 regime" still has the original ambiguity; it is only when an out-of-regime observer is admitted (or when the regime naturally shifts via Phases 4–5) that $H_b$ discriminates.

This is a real scope limit: $H_b$ is not magic. It discriminates over the class of observers AAD admits; the class of observers AAD admits is not unbounded.

### B.5 Outcome of B

**Moderate strengthening.** The `#agent-opacity` segment supplies the "missing state-space dimension" the gap alleged was absent — but only under (i) admitting horizon-indexed observation and (ii) admitting observers whose filtrations extend beyond the current-regime boundary. Both (i) and (ii) are structurally available in the `#agent-opacity` formalism; neither is automatic.

**Segment-level implication.** `#agent-opacity`'s "Future meta-segment candidate" note in Discussion mentions a possible fourth `#discussion-identifiability-floor` instance. The natural formal anchor is Fano's inequality at the observer-side prediction task: for observers whose $H_b^{A\mid B}(t, \tau) \geq H_{\text{threshold}}$, there exists a lower bound on prediction-error probability. The neutral-drift-invisibility result then becomes: "under Phase-1-regime-restricted observers, $H_b$ is insufficient to distinguish a drift variant from the incumbent; out-of-regime observation or intervention is required." This would be a genuine fourth instance.

---

## 3. Strengthening attempt C: Fluctuation / higher-order observables

### C.1 The proposal

If two agents have identical $\alpha$ and $R$ but differ in *how* they achieve the sector bound, they should differ in the covariance structure of their mismatch trajectory. The fluctuation-dissipation theorem relates stationary fluctuation statistics to response functions: two systems with identical mean response can differ at second-moment. Green-Kubo relations recover transport coefficients from equilibrium fluctuations.

### C.2 What AAD already has

*[Claim-tier: exact for the stated construction; robust qualitative in transfer.]*

The `#interaction-channel-classification` Case 4 derivation demonstrates exactly this move: two events with identical mean magnitude but different kurtosis land in different regimes (II-a vs II-b) because the Kalman recipient's class-fitness $\mathcal F(\mathcal M_B)$ responds differently to the distribution *shape*. The KL gap $D_{\text{KL}}(P_{\text{true}} \Vert P_{\mathcal M_B}) > 0$ for heavy-tailed inputs against Gaussian, visible in kurtosis tests on the residual stream — this *is* a higher-moment observable.

`#sector-condition-derivation` §270 similarly uses second-moment bounds (steady-state $\mathbb E\lVert\delta\rVert^2$) in Prop A.1S for the stochastic Model S. The template's stopping-time localization in Khasminskii 2012 relies on second-moment control.

In the sector-condition *derivation*, moments beyond second are treated as bounded-in-tail (GA-2S finite second moment is explicit; higher moments are not load-bearing at the Lyapunov level). But in the *diagnostic* side of the theory (classification, model-class-fitness, residual diagnostics), higher moments already appear.

### C.3 The Fluctuation-Dissipation analog

*[Claim-tier: robust qualitative; the specific FDT form is heuristic because AAD is not in thermodynamic equilibrium.]*

For a Tier-1 agent in Model S with sector constant $\alpha$ and isotropic noise $\sigma_w^2 I$, the steady-state autocovariance of $\delta$ satisfies

$$C_{\delta\delta}(\tau) := \mathbb E[\delta(t)\,\delta(t+\tau)^\top] = \frac{\sigma_w^2}{2\alpha}\,e^{-\alpha\tau}\,I + O(\text{nonlinear})$$

*[Derived for linear Model S Ornstein-Uhlenbeck; this is precisely the calculation underlying `#persistence-cost`'s $\dot R \geq n\alpha/2$ nats/time.]*

The response function — how $\delta$ changes under a unit perturbation of $w$ — in the linear Gaussian case equals $C_{\delta\delta}(\tau)/\sigma_w^2$, recovering an FDT-analog. Two Tier-1 agents with identical $\alpha$ will have identical $C_{\delta\delta}(\tau)$ at all lags in the linear case; they are then genuinely indistinguishable from autocovariance-only data. **Fluctuation statistics add nothing over $(\alpha, R, \sigma_w^2)$ in the linear case.**

But in the *nonlinear* case — which is the generic case AAD's $\beta$ sub-scope covers — two agents with matched $(\alpha, R)$ can have different lag-structure at second order and beyond. The higher-order spectral moments (bispectrum, trispectrum) carry architectural information the covariance does not.

### C.4 Where this fails

*[Claim-tier: heuristic. The neutral-drift specifically-targeted variant construction deserves care.]*

The Miller neutral-drift scenario posits a variant $\nu$ whose correction function $F_\nu$ satisfies the same sector bound *in the current disturbance regime*. If the disturbance regime is linear-Gaussian and the variants are also linear in that regime, they produce identical autocovariance. A determined adversary constructing "perfectly camouflaged" neutral drift would match *all* moments in the current regime, leaving out-of-regime probing as the only distinguisher.

But the honest biological/social neutral-drift scenarios do not work like this. Drift variants typically have some observable higher-moment signature (different response latency, different saturation, different noise injection pattern) that a sufficiently careful observer can see. The stronger statement is therefore:

**Hypothesis.** *Generic* neutral drift (not adversarially constructed) preserves $(\alpha, R)$ at leading order but breaks matching at some finite moment of $\delta$'s stationary distribution or finite-lag structure. Under non-degenerate genericity, $\sup_k \lvert C^{(k)}_\delta - C^{(k)}_{\delta,\text{incumbent}}\rvert > 0$ for some moment order $k$.

*Falsification criterion:* a biological or engineered system where a confirmed neutral-drift variant passes all finite-moment and all-lag tests against the incumbent. I know of no such case; the hypothesis is testable.

### C.5 Outcome of C

**Partial strengthening with named limit.** Fluctuation structure gives a genuine non-$\alpha$-non-$R$ observable in the nonlinear and higher-moment regimes AAD's $\beta$ sub-scope covers. In the linear-Gaussian regime (AAD's $\alpha_1$ sub-scope, Kalman / exp-family), fluctuation structure collapses to $(\alpha, R, \sigma_w^2)$ and neutral drift is invisible from this direction. The strengthened claim: **neutral drift that is undetectable from fluctuation statistics is necessarily confined to the agent's linear-Gaussian sub-scope; in the generic non-linear sub-scope, higher-moment observables discriminate.**

**Segment-level implication.** This content would naturally live in `#sector-persistence-template`'s Discussion as a note on *what the template bounds*: $\alpha R$ is a bound on the ultimate mean deviation; higher-moment structure is diagnostic of architecture beyond the template. Alternatively a new appendix `#fluctuation-diagnostics` could make the point at segment level; lightest landing is probably the template Discussion addition.

---

## 4. Strengthening attempt D: Information-geometric trajectory distance

### D.1 The proposal

On the manifold of agent types (parameterized update rules), two behaviorally-equivalent agents under the current regime define points on an equivalence class. The Fisher-Rao distance between their trajectory distributions $\mathbb P_A, \mathbb P_{A'}$ — under perturbation, under alternative observers — should be zero for truly equivalent agents and positive for neutral-drift variants.

### D.2 Existing AAD anchoring

The 2026-04-23 cycle landed (PI) — parameterization-invariance — in `#agent-identity` and Čencov's uniqueness theorem as the fourth primary instance of `#additive-coordinate-forcing`. The Fisher information metric is therefore the unique (up to affine) AAD-natural metric on statistical-manifold sub-cases of $M_t$. The construction this spike needs is available.

*[Claim-tier: derived for linear-Gaussian and exp-family sub-scope; robust qualitative in transfer.]*

Let $\Theta$ parameterize the agent's class (update rule + correction function). Two agents $\theta, \theta'$ generate trajectory distributions $\mathbb P_{\theta}, \mathbb P_{\theta'}$ over $\{\delta_t\}$. The Fisher-Rao distance

$$d_{\text{FR}}(\theta, \theta') = \inf_{\gamma: \theta \to \theta'} \int_0^1 \sqrt{\dot\gamma^\top \mathcal I(\gamma(s))\,\dot\gamma}\,ds$$

is zero iff $\mathbb P_\theta = \mathbb P_{\theta'}$ almost surely. Two agents with identical $(\alpha, \rho, R, \sigma_w^2)$ and identical higher-moment structure *do* generate identical $\mathbb P$ and have $d_{\text{FR}} = 0$; they are then genuinely the same agent under the chosen observable.

The interesting move is: under what observation channel is $d_{\text{FR}}$ zero? If the observation channel is restricted (only $(\alpha, R)$ summary statistics visible), the *effective* Fisher-Rao distance over the channel is strictly zero for a non-trivial equivalence class. If the channel is expanded (all trajectory moments visible), the distance separates agents at all moment orders where they differ.

### D.3 Why this is nearly tautological

$d_{\text{FR}} = 0$ iff $\mathbb P_\theta = \mathbb P_{\theta'}$ over the chosen sigma-algebra. For "neutral drift" to make sense, the equivalence class must be defined relative to a specific observation channel $\Sigma$ — otherwise we're just claiming that agents with identical output distributions are identical, which is trivial.

The non-trivial statement is: **the equivalence class under Fisher-Rao distance over channel $\Sigma$ is exactly the set of agents indistinguishable from channel $\Sigma$.** This is a scope condition on the observer, not on the theory. AAD does not decide what channel the observer has access to — it gives the metric conditional on the channel.

### D.4 Outcome of D

**Tautological strengthening; non-trivial reframe.** Fisher-Rao gives AAD the correct metric for measuring neutral drift *once the observation channel is fixed*. The neutral-drift problem is then precisely the problem of *which observation channel* an observer has. This dovetails with `#agent-opacity`'s observer-indexing: neutral drift is invisibility under the observer's filtration, and filtration-expansion (adding horizon, moments, or interventions) is the only escape.

**Segment-level implication.** The Čencov / Fisher-Rao apparatus is already in AAD via `#additive-coordinate-forcing` Instance 4; the *observer-conditioned* form of neutral-drift identification is implicit. Surfacing it could happen as an `#agent-opacity` Discussion extension or (more cleanly) as a new Discussion paragraph in `#discussion-identifiability-floor` where the structural-drift-invisibility theme would then sit alongside Instance 3's coupling-sign invisibility.

---

## 5. Strengthening attempt E: Interventional distinguishability via `#loop-interventional-access`

### E.1 The proposal

Pearl's Level 2 distinguishes distributions that agree under observation but disagree under intervention. `#loop-interventional-access` provides Level-2 data by construction: the agent's action causes its next observation. Two agents with identical behavior under observation can be distinguished by their response to perturbation.

### E.2 Sketch derivation

*[Claim-tier: robust qualitative; exact in specific instantiations.]*

Consider two agents $A, A'$ with identical $(\alpha, \rho, R)$, both in the persistence regime under disturbance $w$. Inject a perturbation $\Delta w$ that stays within $A$'s sector region but probes a different direction than $A$ has sampled. If $A$ and $A'$ are genuinely the same, $\delta_A$ and $\delta_{A'}$ respond identically. If their correction functions differ (even within the same sector class), the responses diverge.

This is `#loop-interventional-access` applied at the *probing-agent* layer rather than the agent-under-study layer. An observer running interventional probes against the candidate agent generates do-data per Pearl's hierarchy. The response is a Level-2 signature of the agent's architecture that is strictly finer than the Level-1 behavior in the unperturbed regime.

**Instance 3 of `#discussion-identifiability-floor`** already names this escape at the composition layer: "Observable coupling topology via composite-extended `#loop-interventional-access` — interventions on sub-agent $A_j$ reveal $A_i$'s cross-coupling response." The agent-level version is the same move: interventions on $A$'s input reveal $A$'s correction-function response-to-intervention, which neutral-drift variants will differ on.

### E.3 The observation-only counterexample

Instance 1 of `#discussion-identifiability-floor` is instructive: on-policy data cannot distinguish L0 and L1. The Miller neutral-drift variant is precisely the L1/L1' version at the *correction-function* layer — a latent structural distinction invisible under observation but visible under the right intervention. The theorem form: **under observation-only access (Level 1 in the Pearl hierarchy), the equivalence class of architecturally-different-behaviorally-identical agents is nonempty; under loop-interventional access, the equivalence class collapses to the architecture class.**

This is the same pattern Instance 1 and Instance 2 already follow. The structural form:

- *Setting*: distinguish two agents with identical observable behavior in the current regime.
- *External theorem*: Causal Hierarchy Theorem (Bareinboim et al. 2022) — Level 2 distinctions unidentifiable from Level 1 data.
- *No-go*: observationally equivalent agents cannot be distinguished from on-policy data.
- *Boundary characterization*: loop-interventional access escapes; out-of-regime perturbation escapes; higher-moment observation escapes in the non-linear sub-scope.
- *Strengthened consequence*: `#loop-interventional-access` becomes load-bearing for neutral-drift detection, not just for Level-2 causal reasoning.

### E.4 Outcome of E

**Strong strengthening.** Neutral-drift detection reduces to a Pearl-Level-2 task, which AAD has already equipped itself for via `#loop-interventional-access`. The alleged gap becomes a known identifiability-floor instance, with AAD machinery as unique broadly-available escape.

**This is the headline strengthening of the spike.** Combined with E's connection to the composition-layer no-go (Instance 3), the two form a natural *pair* of identifiability floors — one at the single-agent architecture layer, one at the composition layer. The single-agent version would be a candidate fourth `#discussion-identifiability-floor` instance.

*[Claim-tier: The pattern match is robust qualitative; formalizing the single-agent neutral-drift floor to the standard of Instances 1-3 (explicit external theorem, specific no-go construction, four structural escapes) is scope for a follow-up spike. The pattern shape is established, but the tight Instance-N derivation is not yet produced.]*

---

## 6. Strengthening attempt F: Interaction-channel classification as emitter filter-signature

### F.1 The proposal

The brief asks: does `#interaction-channel-classification`'s four-regime recipient-side decomposition also classify $B$'s *internal response* to equivalent inputs, flagging drift-equivalent agents as having different "filter signatures"?

### F.2 What the segment already does

Yes, effectively. The segment's Kalman-over-Kalman derivation explicitly tests whether a given input — canonically $\xi_A \sim \mathcal N(0, s^2)$, $\xi_A = \pm\Delta$, heavy-tailed, or moderate-Gaussian — lands in Regime I / II-a / II-b / III *given the recipient's architecture*. Two recipients with identical $(\alpha, \rho, R)$ but different correction-function internals can assign the same input to different regimes, *because the four boundary conditions use more than $(\alpha, \rho, R)$*:

- (I-a) uses $R_B$ alone, but
- (I-b) uses $\mathcal F(\mathcal M_B) \cdot \mathcal I_{\max}(\mathcal M_B)$ — class-specific, not captured by $\alpha$ or $R$.
- (I-c) uses $U_{o,B}^{(k)} \cdot c_{\text{floor}}$ — observation-noise-specific.

Two agents with identical mean-deviation bound $R$ but different $\mathcal M_B$ (e.g. Gaussian vs. Student-$t$ observation model) classify the same heavy-tailed input differently (Regime II-b for Gaussian, Regime I for Student-$t$). **The regime assignment is an architectural fingerprint, not a $(\alpha, R)$ consequence.**

### F.3 What this means for the drift gap

Given a stream of inputs, the *distribution over regimes* is a high-dimensional signature that discriminates within the $(\alpha, R)$ equivalence class. A pair of recipients $(B, B')$ with matched $(\alpha, R)$ but different $\mathcal M$ assign the same input stream to different regime-frequencies; their regime-distribution histograms separate.

*[Claim-tier: derived from the segment's Kalman-over-Kalman four-case analysis; robust qualitative for general Tier-1; heuristic for $\beta$ sub-scope.]*

This is an *observable behavioral* signature — no internal access required, no interventional probing required. The observer needs only to classify incoming events against the recipient's observed response.

### F.4 Limits

Regime classification requires the observer to have *its own* model of the recipient, which is precisely the observer-indexed filtration in `#agent-opacity`. Without such a model, the observer sees only the response and cannot assign a regime. So this strengthening is parasitic on `#agent-opacity`'s observer-filtration machinery — not a separate escape.

### F.5 Outcome of F

**Confirmation-as-strengthening.** The `#interaction-channel-classification` machinery already does the work the brief asked about. The regime-distribution histogram over a representative input stream *is* a filter-signature discriminating within the $(\alpha, R)$ equivalence class. This would be worth surfacing more explicitly at the Discussion level, possibly with a note in `#agent-opacity` cross-referencing the regime-distribution as a specific form of $H_b$-related observable.

---

## 7. Strengthening attempt G: Population-level layer on top of singular-trajectory scope

### G.1 The brief's challenge

Can population variables be introduced as a compatible secondary layer (meta-machine; Miller) without violating `#agent-identity`'s singular-trajectory scope?

### G.2 What `#agent-identity` actually says

The segment's scope commitment is load-bearing *for predictions about the token agent's dynamics*. It does not forbid a meta-theory in which tokens are distributed and the distribution has its own dynamics — it says AAD's formal apparatus does not presently cover that. The "What the scope excludes" list includes "Agents conceived as type/equivalence-class entities" as out-of-scope without the additional machinery.

So the permissibility question is: can a population-level layer be *added* without contradicting the single-trajectory commitment at the token level? Yes, structurally. Each token agent retains its $\mathcal C_t$; the population is a collection indexed by agents, with its own state variables (composition vector, niche-occupation measure) and its own dynamics (birth, death, variant introduction).

### G.3 What the addition would look like

*[Claim-tier: sketch; structurally motivated, rigor pending.]*

Define population state $P_t = \{(A_i, \mathcal C_t^{(i)})\}_i$. Each agent is its own AAD agent. The population aggregate supports two kinds of variables:

- **Ensemble averages of AAD quantities**: $\bar\alpha = \mathbb E_i[\alpha_i]$, $\text{Var}(\alpha) = \text{Var}_i[\alpha_i]$, the architecture-distribution $\mu_t$ over agent types.
- **Population dynamics**: birth/death rates, replication mechanism, variant-introduction rate, selection pressure driven by the aggregate outcome.

The population's dynamics are *compatible with* but *not derivable from* the agent-level AAD machinery. Compatible because each agent's per-token dynamics are unchanged; not derivable because the population transition kernel introduces new objects (variation operator, selection kernel) AAD does not supply.

### G.4 Where this connects to the drift gap

Miller's Phases 2–3 (neutral invasion, neutral drift) are population-level phenomena by construction. Endogenous $\gamma$ emerging from population composition — the Phase 4 niche-creation move — requires population-level variables. Specifically, a dyadic $\gamma_{ij}(P_t)$ that depends on who is in the population beyond the dyad.

At the population layer, Phase 4's niche emergence can be modeled as a bifurcation in $\gamma_{ij}$ as a function of the variant's population fraction — a hypothesis that would be testable (and, under adversarial / evolutionary dynamics, often is). This is a genuinely new result, not AAD-native; but it is *compatible* with AAD rather than requiring a revision of the token-level commitments.

### G.5 The scope-honest framing

The correct segment-level move is to state: *AAD's token-level machinery does not forbid a population-level layer; such a layer, with its own state variables and dynamics, would compose compatibly if each instantiated agent remains on its singular trajectory; specific population dynamics (variant introduction, selection, niche creation) are out of AAD's current formal scope and are the natural subject of a future Section-III extension or a companion component.* This matches the existing scope-honesty posture.

### G.6 Outcome of G

**Permissive strengthening with an explicit scope-gate.** Population layer is admissible, is compatible with singular-trajectory scope, and is the natural home for Phase 4 niche-creation dynamics. AAD does not need to reject the population layer — it needs to state that the population layer is a compatible but not currently formalized extension. This is a segment-level addition to `#agent-identity` or `#multi-agent-scope`, not a theorem.

---

## 8. Putting the pieces together: the no-go version

### 8.1 Theorem sketch (candidate fourth `#discussion-identifiability-floor` instance)

*[Claim-tier: sketch — pattern is established (five-element shape matches Instances 1–3); specific external-theorem anchoring and the four escape routes still need tightening to reach Instance-form.]*

**Setting.** Two agents $A, A'$ on the same regime-restricted trajectory, with identical behavioral summaries $(\alpha, R)$ in that regime. Question: can $A$ and $A'$ be distinguished?

**External theorem.** Bareinboim et al. 2022 CHT at the agent-internal layer (agents are SCMs over their state spaces; two SCMs agreeing on Level-1 data can disagree on Level-2). Alternative anchor: Cramér-Rao at the fluctuation-structure layer (in the linear-Gaussian sub-scope, moments beyond second do not add information, and two agents matched at second-order are Fisher-Rao-equivalent over the restricted channel).

**No-go.** Under on-policy, in-regime, $(\alpha, R)$-summary-only observation, the equivalence class of architecturally-distinct-behaviorally-identical agents is non-trivial. Specifically in the linear-Gaussian sub-scope, it is a finite-dimensional manifold of Jordan-form-preserving architectural variations.

**Boundary characterization (four escapes — tentative):**

- (a) **Loop-interventional access** (§5): perturbation probes distinguish within the on-policy equivalence class. Strongest in sub-scope $\alpha_1$ where the interventional response is computable from the agent's update rule.
- (b) **Horizon-extended or out-of-regime observation** via horizon-indexed $H_b$ (§2, §B.3). Requires observers whose filtration extends past the current-regime scope.
- (c) **Higher-moment observation** (§3): nonlinear sub-scope agents differ at moments beyond second; the escape transfers across the $\alpha_1 \to \alpha_2 \to \beta$ ladder with decreasing information.
- (d) **Architecture-instrumented observation**: direct observation of the update rule or internal state (breaks the black-box scope).

**Strengthened consequences.**
- `#loop-interventional-access` becomes the unique broadly-available escape at the agent-internal layer (matching its role at Instance 1's causal-sufficiency layer and Instance 3's composition layer — a three-layer chain).
- `#agent-opacity`'s horizon-indexing and `#interaction-channel-classification`'s regime-histogram become structurally required diagnostic instruments, not optional ones.
- The Lyapunov template `#sector-persistence-template` acquires explicit "this is a bound on ultimate-deviation statistics; architectural discrimination requires additional information channels per #discussion-identifiability-floor Instance N" as a Discussion note.

### 8.2 Why this is a genuine fourth instance

The three existing instances target different layers:
- Instance 1: causal structure layer (L0 vs L1 detection).
- Instance 2: mixture parameter layer (L1' soft-facilitator identification).
- Instance 3: composition layer (coupling sign from component marginals).

A fourth instance at the architecture-within-behavior-class layer would be a natural sibling — neither coincident with nor redundant against the three. It would close the pattern at a layer currently implicit in the theory.

### 8.3 What the spike does NOT yet have

- A crisp closed-form no-go construction at the level of Instance 1's "on-policy observation of L0 ≡ on-policy observation of L1 for edge probabilities matched to regime conditionals" or Instance 3's "symmetric-matched-Tier-1 scalar coupled systems with $\gamma = \pm\gamma_0$ indistinguishable from component marginals." The linear-Gaussian sub-scope version of this — two Kalman filters with different state-space realizations but identical innovation-sequence spectrum — is standard (Kalman canonical form ambiguity), but the tie to neutral drift needs laying out.
- An explicit citation to a single external theorem that does the heavy lifting. CHT (Bareinboim) is one candidate; Kalman canonical-form non-uniqueness (Kalman 1963 / Ho-Kalman 1966) is another and arguably sharper for the linear-Gaussian case. The honest framing may be dual-anchor (two external theorems at two sub-scopes) rather than single.
- The four escape routes need tightening — in particular, (b) horizon-extended observation needs to show it does *not* collapse into (a) loop-interventional access (i.e., that passive observation at extended horizons genuinely escapes, without requiring intervention).

These are explicit to-dos for a follow-up promotion-directed spike.

---

## 9. Honest accounting of what this spike did and did not do

### 9.1 What was genuinely strengthened

1. **§1 / Attempt A**: Endogenization of $\gamma$ in the matched-symmetric-Tier-1 + persistence-margin scope via cross-covariance, operationalizing Instance 3's escape (b) quantitatively. *Derived, exact in scope.*
2. **§2 / Attempt B**: $H_b$'s horizon-indexing separates Miller's Phase 2–3 drift variants from the incumbent under out-of-regime horizon observation. *Robust qualitative with explicit scope limit.*
3. **§5 / Attempt E**: Reduction of neutral-drift detection to a Pearl-Level-2 task, with `#loop-interventional-access` as unique broadly-available escape. *Robust qualitative; pattern-match solid; formal Instance-N tightening deferred to follow-up.*
4. **§6 / Attempt F**: Confirmation that `#interaction-channel-classification`'s regime-histogram already provides a filter-signature separating architectural variants within $(\alpha, R)$-equivalence. *Derived from the segment's existing machinery.*
5. **§7 / Attempt G**: Population-layer compatibility with `#agent-identity`'s singular-trajectory scope; identification of niche-creation as the natural Phase 4 extension target. *Scope-level, permissive with explicit exit.*
6. **§8 / Synthesis**: Candidate fourth `#discussion-identifiability-floor` instance articulated at pattern level, matching the five-element shape of Instances 1–3.

### 9.2 What was not strengthened

- **Neutral drift adversarially constructed to match all finite moments and all interventional responses in the current regime is genuinely invisible.** This is a real no-go, not a softening: no theory grounded in finite observation can see it. The correct response is to name it as a scope limit, not to claim to cover it.
- **Endogenous $\gamma$ as a derived dynamical variable (not merely estimable from cross-covariance)**: this is not produced in this spike. The step from "cross-covariance gives a sign-preserving scalar estimator of $\gamma$" to "$\gamma$ has its own governing equation" requires population-layer machinery (§7) that is out of token-level AAD's current scope. This is an honest open.
- **Phase 4 niche-creation as an AAD-derived result**: requires population-layer dynamics, which AAD does not have. The compatibility result in §7 says nothing stronger than "this can be added without contradiction."

### 9.3 What the gap looked like vs. what it actually is

The Gemini-framed gap ("AAD cannot see this agent at all") was overclaimed given the 2026-04-23 state. The honest characterization is:

- At the single-agent layer in the linear-Gaussian sub-scope under on-policy observation and bounded horizon: **yes, neutral drift is invisible** — this is provably so and matches what Instance 1 says at the causal layer.
- Under extended observation (horizon, moments, regime, intervention): **discriminable via existing AAD machinery** — this is the Instance-pattern result.
- Adversarial-construction neutral drift matching all accessible channels: **provably invisible, by construction** — honest scope limit.
- Phase 4 niche creation (endogenous $\gamma$ from population composition): **compatible extension, not currently formalized** — honest open at the population-layer.

This is a more accurate picture than either the original spike's "structurally blind" framing or an overclaiming "AAD sees everything" posture.

---

## 10. Recommended segment-level moves (Joseph-facing, not executed)

Ordered by what carries the most theoretical consequence, not by effort.

### 10.1 Fourth `#discussion-identifiability-floor` instance (SP-3 candidate)

*Segment*: `#discussion-identifiability-floor`, as new Instance 4.

*Content*: Architecture-within-behavior-class no-go at the agent-internal layer. Setting: distinguish behaviorally-equivalent agents. External theorem: CHT at the agent-as-SCM layer (linear-Gaussian Kalman canonical-form non-uniqueness as the tight sub-scope anchor). No-go: on-policy in-regime observation cannot distinguish. Four escapes: loop-interventional access; horizon-extended observation; higher-moment observation; architecture instrumentation. Strengthened consequence: `#loop-interventional-access` gets a *third* load-bearing role (after Instance 1's causal-sufficiency and Instance 3's composition).

*Effort estimate*: the pattern-match is clear; the formal Instance-N derivation (closed-form no-go construction matched to an external theorem) is a non-trivial spike. Natural follow-up from this one.

*Load-bearing*: High. A three-instance-chain of `#loop-interventional-access` dependency (agent-internal / causal-structure / composition) would be a strong theoretical pattern.

### 10.2 Extend `#agent-opacity` Discussion with observer-filtration scope note

*Segment*: `#agent-opacity`, Discussion section or a new "Scope of observer-filtration" subsection.

*Content*: $H_b$'s discrimination within $(\alpha, R)$-equivalence is real but parasitic on the observer's filtration; neutral drift undetectable under Phase-1-regime-restricted observers is exactly what $H_b$ cannot see with that filtration. Out-of-regime observation, horizon extension, or interventional probing is required. Cross-reference to `#discussion-identifiability-floor` Instance 4 (once landed) and to `#loop-interventional-access`.

*Effort estimate*: One paragraph plus cross-reference. Low.

*Load-bearing*: Moderate. Makes the scope honesty of `#agent-opacity` visible; aligns with the "scope-honesty-as-architecture" posture.

### 10.3 Fluctuation-structure note in `#sector-persistence-template` Discussion

*Segment*: `#sector-persistence-template`.

*Content*: the template bounds first-moment / second-moment ultimate deviation; architectural discrimination within an $(\alpha, R, \sigma_w^2)$-equivalence class requires higher-moment observables (skewness / kurtosis / spectral moments beyond second), which the nonlinear sub-scope generically supplies. Reference to `#interaction-channel-classification` Case 4 as worked instance; forward-reference to `#discussion-identifiability-floor` Instance 4.

*Effort estimate*: One paragraph. Low.

*Load-bearing*: Low-moderate. Clarifies what the template bounds and what it does not.

### 10.4 `#critical-mass-composition` addendum on $\gamma$-estimation from cross-covariance

*Segment*: `#critical-mass-composition`, possibly in the derivation-audit table or a short Discussion subsection.

*Content*: In the matched-symmetric-Tier-1 + persistence-margin scope, $\gamma$ is *estimable* from joint $(\delta_1, \delta_2)$ cross-covariance via the steady-state Lyapunov equation (sign-preserving scalar, up to $\sigma_w^2$ normalization). This *operationalizes* Instance 3 escape (b) matched-Tier-at-composite — the escape from the composition-layer identifiability floor is not only structurally admissible but delivers a concrete joint-data estimator for $\gamma$. Explicit note that estimation is distinct from derivation (*endogenization-as-estimator*, not *endogenization-as-dynamical-variable*).

*Effort estimate*: Moderate. The derivation is standard Lyapunov algebra; the segment placement and framing are the main work.

*Load-bearing*: Moderate. Tightens Instance 3's escape (b) from structural-admissibility to quantitatively-operational.

### 10.5 Population-layer scope extension in `#agent-identity`

*Segment*: `#agent-identity`, Discussion section.

*Content*: Explicit statement that singular-trajectory scope at the token level is compatible with a meta-theoretic population layer in which tokens are instances with their own dynamics; such a layer is out of AAD's current formal scope and is the natural home for phenomena (Phase 4 niche creation, selection dynamics, variant introduction) that require population-level state. This is already implicit in the existing "What the scope excludes" list; the strengthening move is to make it explicit that the exclusion is a deferred extension, not a rejection.

*Effort estimate*: One paragraph. Low.

*Load-bearing*: Low at the theoretical core; moderate for `03-logogenic-agents/` framing, where population-layer dynamics will become directly relevant.

### 10.6 Do NOT: new segment on "latent structural diversity"

The original `msc/spike-neutral-drift-lyapunov.md` proposed a new AAD concept "latent structural diversity" for correction-architecture variation invisible under current conditions. After the 2026-04-23 cycle, this concept is **not needed as a new segment** — it is fully expressible using `#agent-opacity`'s horizon-indexing combined with `#discussion-identifiability-floor` Instance 4 (candidate). Creating a separate "latent structural diversity" segment would violate the "prior art integration" convention (adopt/compose existing segments rather than invent NIH concepts).

---

## 11. Open questions for the follow-up spike

1. **Single-agent fourth-instance closed form.** The cleanest no-go construction: two Kalman filters with identical innovation-sequence spectra but different state-space realizations (Kalman-Ho canonical form ambiguity). This is classical and citable; lift to the AAD form and check whether the four escape routes compose cleanly. The sharp question: is the horizon-extended-observation escape (b) genuinely distinct from the interventional escape (a), or does horizon-extension in closed-loop dynamics eventually require action-generated data? I suspect they overlap in practice; the formal question is whether passive observation at long horizons under the agent's *original* policy is Level-1 or Level-2 data.

2. **Endogenous-$\gamma$ dynamics as a follow-up to §A.** The cross-covariance estimator is one-shot; the dynamics $\dot\gamma = f(P_t, \delta, \ldots)$ requires either a population layer or a slow-fast decomposition within a single-agent-with-slow-coupling-variable formulation. The latter is a candidate next spike — take $\gamma$ as a slow state variable on its own time scale, check whether AAD's `#adaptive-gain-dynamics` machinery (meta-gain conditions MG-1–MG-4) transfers.

3. **Fluctuation-FDT anchoring in nonequilibrium regimes.** The FDT analog in §3 is cleanest in Ornstein-Uhlenbeck steady state. AAD's $\beta$ sub-scope includes agents far from this regime. Whether a nonequilibrium-FDT (Crooks, Jarzynski) form applies at the rigor level of the existing sector-persistence template is not obvious; heuristic use in Discussion is safe, derivation-layer claims are not.

4. **Mechanism-design as fifth-instance candidate.** `#discussion-identifiability-floor` Working Notes already flags Gibbard-Satterthwaite / Myerson-Satterthwaite / Arrow as candidate fourth instance. The interaction with the architecture-within-behavior-class instance identified here needs coordination — whether these are parallel fourth-instance candidates, or one subsumes the other, or they target genuinely different layers, deserves explicit treatment before either is promoted.

5. **Interaction with `#discussion-separability-pattern`.** The fourth-instance candidate in §8 naturally pairs with a separability-pattern-like positive-scope ladder: *architecture-observable-core* (sub-scope $\alpha_1$ with horizon-extended observation) / *architecture-semi-observable* ($\alpha_1/\alpha_2$ with intervention or moment-observation) / *architecture-unobservable* ($\beta$ with adversarial matching). Another ladder candidate for `#discussion-separability-pattern` (which currently has seven).

---

*Follow-up spike candidates:* (a) closed-form single-agent Instance 4 with Kalman-Ho canonical-form anchoring (§8 + §11.1); (b) slow-fast endogenous-$\gamma$ dynamics via `#adaptive-gain-dynamics` meta-gain transfer (§11.2); (c) mechanism-design vs. architecture-within-behavior-class instance coordination (§11.4). Each is independent of the others; each could run in parallel.

*The primary segment-level move this spike recommends is §10.1 (fourth `#discussion-identifiability-floor` instance).* Everything else is smaller addenda or scope notes that land naturally alongside §10.1 or stand on their own.
