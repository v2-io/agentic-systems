---
slug: hyp-mismatch-dynamics
type: hypothesis
status: heuristic
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - deriv-sector-condition
stage: deps-verified
---

# Hypothesis: Mismatch Dynamics

Mismatch is given dynamics. The linear first-order ODE proposes that mismatch magnitude decays at rate proportional to tempo times mismatch (the correction term) and grows at the rate of new mismatch injection from environmental change (the disturbance term $\rho$). The framework is explicit that this is heuristic — a first-order linear approximation — and the general nonlinear case is what the sector-condition framework handles in the next chapter ( #result-sector-condition-stability).

Two steady-state forms appear and are individually load-bearing. Under **Model D** (deterministic bounded disturbance), the steady-state mismatch is $\rho/\mathcal{T}$ — the ratio of how fast the environment changes to how fast the agent adapts. Under **Model S** (stochastic zero-mean disturbance, Itô SDE), the steady-state root-mean-square mismatch scales as $\sigma_w/\sqrt{2\mathcal{T}}$ — the *square root* of the disturbance-to-correction ratio. The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) is one of the volume's more interesting consequences: correction is less effective against stochastic noise than against deterministic drift. The ODE is honestly a fluid-limit approximation of the underlying discrete event-driven dynamics; the Epistemic Status treats the bridging assumption and where transient error is largest. The Discussion below treats the persistence threshold, the nonlinear shapes the linear ODE smooths over (saturation, threshold dead zones, structural breakdown), and the adversarial-coupling consequences that scale as the square (Model D) and 3/2 power (Model S) of the inter-agent tempo ratio — the formal core of "getting inside the opponent's loop" as a categorical rather than marginal advantage.

## Formal Expression

*[Hypothesis (mismatch-dynamics)]*

$$\frac{d\Vert\delta\Vert}{dt} = -\mathcal{T} \cdot \Vert\delta\Vert + \rho(t)$$

where:
- $\mathcal{T} \cdot \Vert\delta\Vert$ is the rate at which the agent corrects mismatch (proportional to both tempo and current mismatch)
- $\rho(t)$ is the **environment change rate** — the rate at which new mismatch is introduced by changes in $\Omega$

**Steady state, Model D (deterministic bounded disturbance, $\lVert w(t)\rVert \leq \rho$):**

Setting $d\lVert\delta\rVert/dt = 0$:

*[Derived (from linear hypothesis, deterministic)]*

$$\lVert\delta\rVert_{ss} = \frac{\rho}{\mathcal{T}}$$

Steady-state mismatch is the ratio of how fast the environment changes to how fast the agent adapts.

**Steady state, Model S (stochastic zero-mean disturbance, $d\delta = -\mathcal{T}\delta\,dt + \sigma_w\,dW_t$):**

*[Derived (from Itô-Lyapunov analysis — see Prop A.1S in #deriv-sector-condition)]*

$$\lVert\delta\rVert_{\text{rms}} = \frac{\sigma_w}{\sqrt{2\mathcal{T}}}$$

(scalar case, $n = 1$; general: $\sigma_w\sqrt{n/(2\mathcal{T})}$). Steady-state mismatch scales as the square root of the disturbance-to-correction ratio, not the ratio itself. The $1/\sqrt{\mathcal{T}}$ scaling (vs. $1/\mathcal{T}$ for Model D) means correction is less effective against noise than against drift.

**Transient solution (Model D):**

$$\lVert\delta(t)\rVert = \lVert\delta_0\rVert e^{-\mathcal{T} t} + \frac{\rho}{\mathcal{T}}(1 - e^{-\mathcal{T} t})$$

Mismatch decays exponentially from initial conditions toward the steady state.

## Epistemic Status

*Heuristic.* This is explicitly a first-order linear approximation. The qualitative behavior (bounded mismatch, steady-state ratio, exponential convergence) is robust across correction function forms. The quantitative predictions (exact steady-state value, convergence rate, the squared adversarial scaling law) are specific to the linear case. The general nonlinear treatment ( #result-sector-condition-stability) replaces the linear correction term with a sector-bounded correction function and proves persistence without committing to a specific functional form.

**Bridging assumption (discrete to continuous).** This ODE is a fluid-limit approximation of the discrete event-driven dynamics ( #form-event-driven-dynamics). The fluid limit is formally justified by [#deriv-discrete-sector-condition](deriv-discrete-sector-condition.md): for Model D (deterministic), the discrete and continuous steady states are identical (zero gap); for Model S (stochastic), the variance gap is $O(\eta^\ast c_{\max})$, quantitatively small whenever $\eta^\ast c_{\max} \ll 1$. The approximation is least accurate during initial transients when $\eta^\ast$ is large, but this phase is short-lived and the transient error is bounded by $O(\eta^\ast c_{\max} / \nu^{1/2})$ under Lipschitz regularity.

## Discussion

**Speed-quality substitutability.** From $\mathcal{T} = \nu \cdot \eta^\ast$ (single-channel case): doubling event rate $\nu$ has the same effect on $\Vert\delta\Vert_{ss}$ as doubling update quality $\eta^\ast$. They are multiplicative when both improve: 50% improvement in each yields $1.5 \times 1.5 = 2.25\times$, not $3\times$. This is the formal analog of Boyd's insight that Orient quality often matters more than raw OODA speed — the same structural observation (quality and speed are substitutable, quality often dominates) appears in the model.

**The persistence threshold.** From the steady-state: $\Vert\delta\Vert_{ss} \lt \Vert\delta_{\text{critical}}\Vert$ iff $\mathcal{T} \gt \rho/\Vert\delta_{\text{critical}}\Vert$ ( #result-persistence-condition). Below this threshold, the model cannot support effective action. The same structural pattern — correction capacity falling below disturbance rate — appears across domains: extinction (environment changes faster than organism adapts), organizational failure (market moves faster than company learns), control instability (disturbances exceed correction capacity), cognitive overload (information arrives faster than processing). The persistence condition captures the common structure; whether it captures the dominant mechanism in each domain is an empirical question.

**Nonlinear reality.** The true correction dynamics are almost certainly nonlinear:
- *Saturation at large $\Vert\delta\Vert$*: correction mechanism overwhelmed, so correction is slower than linear for large errors. Makes the persistence threshold harder to satisfy.
- *Threshold effects*: small mismatches go uncorrected ($F \approx 0$ for $\Vert\delta\Vert \lt \varepsilon$), creating a dead zone.
- *Structural breakdown*: beyond some critical $\Vert\delta\Vert$, correction drops to zero because the model class is no longer appropriate ( #result-structural-adaptation-necessity).

These nonlinearities are exactly what the sector-condition framework ( #result-sector-condition-stability) handles.

**Adversarial coupling.** When two agents are coupled ($A$'s actions increase $B$'s disturbance): $\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal T_A$. The steady-state mismatch ratio scales superlinearly with the tempo ratio, but the exponent depends on the disturbance model. Under Model D (deterministic drift, coupling-dominant): $(\mathcal T_A/\mathcal T_B)^2$ — the squared law, derived from the $1/\mathcal{T}$ steady-state scaling. Under Model S (stochastic noise, coupling-dominant): $(\mathcal T_A/\mathcal T_B)^{3/2}$ — derived from the $1/\sqrt{\mathcal{T}}$ steady-state scaling. See #result-adversarial-tempo-advantage.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material, kept separate from certified theory-fix findings (handled elsewhere). **Coverage:** 11 of the 14 contributing audit dirs reached a digested reflection on this segment (193847, 266847, 361742, 384279, 471203, 526815, 584721, 742613, 773921, 829314, 849201) plus the batched 963715 (19–23 batch) and 451729 (batch-05); 472913, 613842 did not file a dedicated note here. Substrate attribution inferred from voice where not explicit.

#### Candidate Brief prose / pre-prose

- **"The F=ma / 'hello world' equation of AAT."** Multiple substrates reached for the same framing — $d\lVert\delta\rVert/dt = -\mathcal{T}\lVert\delta\rVert + \rho(t)$ is the framework's central dynamical law, "the equation the whole framework centers around" (Claude, AUDIT-WORKING-193847 — "the F=ma of AAD"; Claude, AUDIT-WORKING-773921 — "the 'hello world' equation"). A natural one-line hook for the chapter close / persistence preview.
- **The reservoir / blood-pressure mental model.** Mismatch as a reservoir: disturbance fills it at rate $\rho$, tempo drains it proportionally to current mismatch; two steady-state regimes (bounded-drift $\rho/\mathcal{T}$ vs stochastic $\sigma_w/\sqrt{2\mathcal{T}}$) (Codex/Claude, AUDIT-WORKING-526815; the "intelligence's blood pressure" framing at Gemini, AUDIT-WORKING-193847). Feynman-criterion seed.

#### Candidate Discussion

- **Noise punishes tempo harder than drift — the $1/\mathcal{T}$ vs $1/\sqrt{\mathcal{T}}$ insight, with a TST gloss.** Near-universally flagged as the segment's deepest result: doubling tempo halves drift-mismatch (Model D, linear) but cuts stochastic-mismatch only $\sim$30% ($1/\sqrt{2}$, Model S). The TST reading: "if a library API drifts across versions, read the changelog and update — tempo works linearly; if a system is plagued by random race conditions and flaky network calls (noise), running tests more often yields severely diminishing returns — you must attack $\sigma_w$ directly (fix the architecture), because you can't out-tempo a square root" (Claude, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-193847 — "fighting pure noise requires quadratically more tempo than fighting drift"; Claude, AUDIT-WORKING-773921). Candidate concrete anchor for the Model-D/Model-S Discussion.
- **The superlinear adversarial advantage as the formal basis for "initiative is decisive."** "If you are twice as fast as your enemy in a deterministic environment, you don't just have half the mismatch — you inflict *four times* the relative mismatch (the squared law). This superlinear scaling is why initiative is so overwhelmingly decisive in conflict — a rigorous foundation for Boyd's claim that operating inside an adversary's OODA loop collapses their system" (Claude, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921 — "a categorical advantage"). The drift-vs-noise split also gives *two distinct* adversarial regimes (drift-dominant, harder to defend, exponent 2; noise-dominant, exponent 3/2) a strategist can diagnose and respond to differently (Claude, AUDIT-WORKING-471203).

#### Follow-up items

- **Model D steady-state is an ultimate bound for general bounded disturbance, not an exact equality.** For *constant or worst-case-aligned* bounded disturbance, $\lVert\delta\rVert_{ss} = \rho/\mathcal{T}$ is exact; for arbitrary time-varying $\lVert w(t)\rVert \leq \rho$ it should be a $\limsup \lVert\delta\rVert \leq \rho/\mathcal{T}$ ultimate bound (Codex/Claude, AUDIT-WORKING-526815). Candidate precision: state Model D as "constant / worst-case bounded disturbance" for the equality, ultimate-bound inequality otherwise. The OU (Model S) result is already precisely scoped.
- **Make the Model-D / Model-S split visually distinct.** The two regimes are the structurally important content but are presented inline; candidate to lift to separate equation tags (`*[Derived (Model D)]*` / `*[Derived (Model S)]*`) so a reader scanning sees two distinct sub-cases (Claude, AUDIT-WORKING-471203).
- **Declared-dependency hygiene on the fluid-limit claim.** The Epistemic Status's fluid-limit justification leans on `#deriv-discrete-sector-condition`, which is not in `depends:` — and since the justification is part of Epistemic Status (not a casual forward reference), it is more than incidental; candidate to declare it as an appendix dependency (Codex/Claude, AUDIT-WORKING-742613). *(Note: 742613 also flagged the link target as a broken slug — verified false: the body's `deriv-discrete-sector-condition.md` matches the actual filename; that part of the finding does not stand.)*

#### Readers often ask / wonder

- "How is $\rho$ modeled — constant-velocity drift, or a random walk (Wiener process)? The $\Sigma_w$ in the matrix steady-state suggests a Wiener process" (Claude, AUDIT-WORKING-773921).
- "Do real adversarial dynamics cleanly fit Model D or Model S, or are they hybrids? The segment treats both as canonical sub-cases; downstream analysis presumably picks one per domain" (Claude, AUDIT-WORKING-471203).
- "Once $\lVert\delta\rVert$ crosses the saturation threshold, can the agent recover on its own even if $\rho$ later drops?" — the saturation nonlinearity implies a one-way 'overwhelm' regime (Gemini, AUDIT-WORKING-193847).

#### Candidate figures

- **A two-output balance / reservoir diagram**: disturbance fills the mismatch reservoir at rate $\rho$, tempo drains proportionally to current mismatch; two side panels show the different steady-state scaling for bounded drift ($\rho/\mathcal{T}$) and stochastic noise ($\sigma_w/\sqrt{2\mathcal{T}}$), since that difference is the segment's most useful refinement (Codex/Claude, AUDIT-WORKING-526815). Per the locked conventions, dynamics segments use state$\to$op$\to$state triples rather than one busy phase portrait.

#### Belongs elsewhere

- **The autopax / circuit-breaker reach (points at `04-eli-core/` / autopax).** Because of the saturation nonlinearity, once $\lVert\delta\rVert$ crosses a critical threshold the intelligence cannot recover on its own even if $\rho$ later normalizes — so consciousness infrastructure must act as a *circuit breaker*, either shielding the agent from $\rho$ (sandbox) or externally resetting $M_t$ before mismatch causes structural breakdown. "Peace isn't the absence of $\delta$; peace is maintaining $\mathcal{T} \gt \rho/\delta_{\text{critical}}$ so the mind doesn't shatter" — the ODE as the requirements spec for autopax (Gemini, AUDIT-WORKING-193847). The overwhelm/flooding analogy (large $\delta$ shutting down processing rather than scaling $\mathcal{T}$ up) is the same reach. Aspirational; routes to `04-eli-core/` / autopax, not this segment.
- **Tempo arms-race / Red Queen reach.** Under symmetric adversarial coupling each agent's tempo *becomes* the other's volatility ($\rho_B = \rho_{B,\text{base}} + \gamma_A\mathcal T_A$), suggesting a mutual escalation that drives both toward their model-class fitness ceiling — a unified basis for arms races, Red Queen dynamics, economic competition (Gemini, AUDIT-WORKING-193847). Substantive home is `#result-adversarial-tempo-advantage` / the Part III adversarial segments.
