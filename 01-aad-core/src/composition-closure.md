---
slug: composition-closure
type: formulation
status: conditional
depends:
  - postulate-composition-consistency
  - scope-composite-agent
  - multi-agent-scope
  - agent-environment
  - event-driven-dynamics
  - sector-condition-stability
  - sector-condition-derivation
  - sector-persistence-template
  - persistence-condition
stage: draft
---

# Formulation: Composition Closure Criterion

We define a group of interacting agents as a valid composite macro-agent when its closed-loop dynamics approximately commute with coarse-graining — that is, when projecting micro-states to macro-states and then running macro-dynamics yields approximately the same result as running micro-dynamics and then projecting.

## Formal Expression

Let a system consist of $N$ sub-agents interacting in a shared environment with state space $\mathcal S_{\text{env}}$. The micro-state, micro-observations, and micro-actions are:

$$X_{\text{micro}, t} = \{ (M_{i,t}, G_{i,t}) \}_{i=1}^N \in \mathcal X_{\text{micro}}$$

$$o_{\text{micro}, t} = \{ o_{i,t} \}_{i=1}^N \in \mathcal O_{\text{micro}}$$

$$a_{\text{micro}, t} = \{ a_{i,t} \}_{i=1}^N \in \mathcal A_{\text{micro}}$$

The coupled micro-dynamics form an action-observation loop:

$$X_{\text{micro}, t} \xrightarrow{\pi_{\text{micro}}} a_{\text{micro}, t} \xrightarrow{E} (\Omega_{t+1}, o_{\text{micro}, t+1}) \xrightarrow{f_{\text{micro}}} X_{\text{micro}, t+1}$$

We constrain our search to an admissible class of projections $\Lambda \in \mathcal P_{\text{adm}}$ mapping micro to macro, an admissible class of macro-dynamics $(\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}$, and a **timescale ratio** $K_c \geq 1$: the number of micro-timesteps per macro-step. Micro-time is indexed by $t \in \{0, \ldots, H\}$; macro-time by $m \in \{0, \ldots, \lfloor H/K_c \rfloor\}$ with macro-step $m$ corresponding to micro-timestep $t = m K_c$. The projection components then have type signatures:

- $\Lambda_x : \mathcal X_{\text{micro}} \to \mathcal X_c = (M_c, G_c)$ — pointwise, evaluated at macro-boundaries.
- $\Lambda_\Omega : \mathcal S_{\text{env}} \to \mathcal S_{\text{env}, c}$ — pointwise, evaluated at macro-boundaries.
- $\Lambda_o : \mathcal O_{\text{micro}}^{K_c} \to \mathcal O_c$ — aggregates the window of $K_c$ micro-observations between successive macro-boundaries.
- $\Lambda_a : \mathcal A_{\text{micro}}^{K_c} \to \mathcal A_c$ — aggregates the window of $K_c$ micro-actions similarly (used on the observation-comparison side; the macro-policy $\pi_c$ emits one macro-action per macro-step).

Aggregation is part of the projection specification — common choices are mean/sum (linear systems), first/last (event-rate projections), or task-specific sufficient statistics. When $K_c = 1$ the windows collapse, $\Lambda_o, \Lambda_a$ reduce to pointwise maps, and micro- and macro-tempos coincide (synchronous-update composites). When $K_c \gg 1$ the composite operates on the quasi-steady-state output of its sub-agents, the regime that #temporal-nesting asserts as the natural one for composition. $K_c$ is part of the problem specification; it does not appear in (A1)-(A4) or (P1)-(P3) below, but it determines at what granularity closure is measured.

Let $\mathcal D_{\text{micro}}$ be the distribution of reachable trajectories generated entirely by the true micro-system over horizon $H$, and let $o_{\text{micro}, (m-1)K_c : m K_c}$ denote the window of $K_c$ micro-observations $(o_{\text{micro}, (m-1)K_c + 1}, \ldots, o_{\text{micro}, m K_c})$ between macro-boundaries $m-1$ and $m$ (similarly for actions).

*[Definition (Composition Closure)]* We define the minimal achievable closure defect $\varepsilon^\ast$ over the admissible classes as:

$$ \varepsilon^\ast = \inf_{\Lambda \in \mathcal P_{\text{adm}},\, (\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}} \big\lVert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\rVert $$

where the expected component errors evaluated over true micro-trajectories $\tau \sim \mathcal D_{\text{micro}}$, measured **per macro-step**, are:

- $\varepsilon_x = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_x\big(X_{\text{micro},\, m K_c}\big) - f_c\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c}),\; \Lambda_o(o_{\text{micro},\, (m-1)K_c : m K_c})\big) \big\rVert_\mathcal{X} \Big]$
- $\varepsilon_a = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_a\big(a_{\text{micro},\, (m-1)K_c : m K_c}\big) - \pi_c\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c})\big) \big\rVert_\mathcal{A} \Big]$
- $\varepsilon_o = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_o\big(E_{\text{obs}}(\Omega,\, a_{\text{micro}})\big\vert_{(m-1)K_c : m K_c}\big) - E_{c,\text{obs}}\big(\Lambda_\Omega(\Omega_{(m-1)K_c}),\; \pi_c(\Lambda_x(X_{\text{micro},\, (m-1)K_c}))\big) \big\rVert_\mathcal{O} \Big]$

where $M_H = \lfloor H/K_c \rfloor$ is the number of macro-steps in horizon $H$, and $E_{\text{obs}}(\Omega, a_{\text{micro}})\big\vert_{(m-1)K_c : m K_c}$ denotes the window of micro-observations the environment produces across the macro-step.

**Units.** $\varepsilon_x, \varepsilon_a, \varepsilon_o$ carry units of distance — per-macro-step norm errors. Multiplied by the macro-update rate $\nu_c$ (units $[\text{time}^{-1}]$), they yield the disturbance-rate units $[\text{distance}]\cdot[\text{time}^{-1}]$ demanded by the sector-persistence template's $\rho_\xi$ ( #sector-persistence-template) and by the dimensional accounting in #tempo-composition. The previous per-micro-step formulation conflated $\varepsilon^\ast$'s granularity with $\nu_c$'s — the macro-step formulation resolves the unit inconsistency.

**$K_c = 1$ special case.** When micro and macro update in lockstep, $M_H = H$, the observation/action windows collapse, and the formulas reduce to the synchronous form. This is the regime of tightly-coupled groups (distributed algorithms running in phase, ensemble filters where every member steps per tick) and is where the two-Kalman worked example below operates.

**$K_c \gg 1$ case.** When the composite lives at a strictly slower timescale than its sub-agents (the regime #temporal-nesting asserts as natural), only micro-states at macro-boundaries enter $\varepsilon_x$, and macro-observations aggregate $K_c$ micro-observations. The closure defect then measures how well the macro-dynamics predicts the *next* macro-state from the *previous* macro-state and the aggregated micro-observation window — not any intermediate micro-state. Timescale abstraction is recovered: the composite's description need not — and under $K_c \gg 1$ should not — track the micro-trajectory between macro-boundaries.

The closure-defect framework applies to sets that satisfy #scope-composite-agent — i.e., that form composites via at least one of the three alignment routes (shared objective, hierarchical derivation, mutual benefit). Given scope-satisfaction, a set forms a *meaningful* composite agent — distinguished from a multi-agent system whose low-$\varepsilon^\ast$ projection is a happenstance of the environment rather than a reflection of composite coherence — when $\varepsilon^\ast \leq \varepsilon_{\text{max}}$. Without scope-satisfaction, the $\varepsilon^\ast$ infimum is still well-defined as a projection property, but the resulting "composite" has ill-defined purposeful substate $G_c = (O_c, \Sigma_c)$ and composition-level machinery (team persistence, composite tempo) does not apply.

### Admissibility constraints on macro-dynamics

*[Formulation (macro-dynamics-admissibility)]*

$\mathcal M_{\text{adm}}$ is the class of macro-dynamics $(\pi_c, E_c, f_c)$ satisfying:

**(A1) AAD agent structure.** The macro-state decomposes as $X_c = (M_c, G_c)$. The macro-update is recursive at macro-time $m$:

$$X_{c,m+1} = f_c(X_{c,m}, o_{c,m+1})$$

The macro-policy is state-dependent: $a_{c,m} = \pi_c(X_{c,m})$. This ensures the macro-agent has the same structural components as a single AAD agent ( #agent-environment, #recursive-update, #action-selection).

**(A2) Macro-mismatch.** A mismatch signal is well-defined:

$$\delta_{c,m} = o_{c,m} - \hat{o}_{c,m}(M_c, a_{c,m-1})$$

where $\hat o_{c,m}$ is the macro-model's prediction of the next macro-observation. This ensures the macro-agent can detect prediction errors — the foundation of adaptation ( #mismatch-signal).

**(A3) Macro-tempo.** The macro-update has well-defined adaptive tempo:

$$\mathcal T_c = \sum_k \nu_c^{(k)} \cdot \eta_c^{(k)\ast}$$

where $k$ indexes the macro-agent's observation channels, $\nu_c^{(k)}$ is the event rate, and $\eta_c^{(k)\ast}$ is the optimal gain ( #adaptive-tempo, #update-gain). This ensures the persistence condition is formulable at the macro level.

**(A4) Bounded macro-correction.** The macro-correction function satisfies the sector condition ( #sector-condition-stability):

$$\delta_c^T F_c(\mathcal T_c, \delta_c) \geq \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert \delta_c \rVert \leq R_c$$

with $\alpha_c \gt 0$ (positive correction rate) and $R_c \gt 0$ (finite reserve). This ensures the macro-agent's corrections work — they reduce mismatch rather than amplifying it, within the macro-model's capacity.

**What (A1)-(A4) prevent.** Without these constraints, the infimum over $\mathcal M_{\text{adm}}$ is trivially zero (any dynamical system can curve-fit micro-trajectories over a finite horizon). The constraints force the macro-dynamics to be a genuine AAD agent — with decomposed state, prediction errors, adaptive tempo, and stable correction — not an arbitrary function approximator. $\varepsilon^\ast$ then measures the irreducible cost of representing multiple agents as one AAD agent.

**What (A1)-(A4) do NOT require.** Directed separation ( #directed-separation) is not part of the admissibility constraints. It is an additional structural property that some composites have and others don't ( #directed-separation-under-composition). Results that depend on directed separation declare it as an additional assumption. Similarly, strategy structure ($G_c = (O_c, \Sigma_c)$ with a DAG) is not required — simpler goal representations are admissible.

### Admissibility constraints on projections

*[Definition (projection-admissibility, proposed from spike)]*

The admissible class of projections $\mathcal P_{\text{adm}}(\epsilon_I, L)$ consists of projections $\Lambda = (\Lambda_x, \Lambda_o, \Lambda_a, \Lambda_\Omega)$ satisfying three conditions:

**(P1) Information preservation.** The projection retains at least a fraction $(1 - \epsilon_I)$ of the predictive mutual information, evaluated across a macro-step:

$$I\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c});\; \Lambda_o(o_{\text{micro},\, (m-1)K_c : m K_c}) \mid \Lambda_a(a_{\text{micro},\, (m-1)K_c : m K_c})\big) \geq (1 - \epsilon_I) \cdot I\big(X_{\text{micro},\, (m-1)K_c};\; o_{\text{micro},\, (m-1)K_c : m K_c} \mid a_{\text{micro},\, (m-1)K_c : m K_c}\big)$$

The left side is the predictive information the macro-state has about the next macro-observation (aggregated over the $K_c$-window), conditioned on the macro-action. The right side is the micro-state's predictive information about the *same* macro-observation, conditioned on the same aggregated actions — both sides share a common target so the ratio is well-defined. The parameter $\epsilon_I \in [0, 1)$ controls how much predictive power may be sacrificed by projection. This is the information bottleneck (Tishby et al. 1999) applied to the projection map. When $K_c = 1$, the windows collapse to singletons and (P1) reduces to the per-micro-step form previously stated.

**(P2) Lipschitz continuity.** Each component of $\Lambda$ is Lipschitz-continuous with constant $L$:

$$\lVert \Lambda_x(X) - \Lambda_x(X') \rVert_{\mathcal X_c} \leq L \cdot \lVert X - X' \rVert_{\mathcal X_{\text{micro}}} \quad \forall\, X, X' \in \mathcal X_{\text{micro}}$$

(and analogously for $\Lambda_o, \Lambda_a, \Lambda_\Omega$, each with its own Lipschitz constant). Without Lipschitz regularity, bounded closure defect does not imply bounded trajectory error — the bridge lemma requires this or something equivalent. When the projection is $L$-Lipschitz, the trajectory error bound becomes $L \cdot \varepsilon^\ast / \alpha_c$.

**(P3) Dimensionality reduction.** The macro-state space has strictly lower dimension than the micro-state space:

$$\dim(\mathcal X_c) \lt \dim(\mathcal X_{\text{micro}})$$

This prevents the trivial identity projection, which achieves $\varepsilon^\ast = 0$ but is not a genuine abstraction.

**Why three conditions.** No single condition suffices alone. (P1) prevents degenerate projections (a constant map $\Lambda_x = c$ has zero mutual information). (P2) prevents pathological projections (discontinuous maps that amplify micro-errors into unbounded macro-errors). (P3) prevents trivial projections (the identity map satisfies (P1) and (P2) but achieves nothing). Together they constrain $\mathcal P_{\text{adm}}$ to projections that are informative, regular, and genuinely reductive.

**The $(\epsilon_I, L)$ parameters are part of the problem specification, not derived quantities.** The natural choice for many applications is $L = 1$ (non-expansive projection) and $\epsilon_I$ chosen as the minimum information loss compatible with genuine dimensionality reduction.

**Independence from (A1)-(A4).** The macro-dynamics admissibility (A1)-(A4) partially constrains the projection — (A1) requires $\Lambda_x$ to preserve the $M_c / G_c$ decomposition, and (A4) implicitly requires regularity through the sector condition. But (A1)-(A4) do not specify how much predictive information the projection must retain. A macro-agent with a very coarse projection can satisfy (A1)-(A4) while being a poor representation of the micro-system. The information-preservation condition (P1) fills this gap. See `msc/spike-projection-admissibility.md` §5 for the full independence analysis.

### Bridge lemma: closure defect to trajectory error

*[Derived (bridge-lemma, from sector-persistence-template + A4 + contraction assumption)]*

The bridge lemma is the sector-persistence template ( #sector-persistence-template) applied with state variable $\xi = e_m = X_{c,m} - \Lambda_x(X_{\text{micro},\, m K_c})$ (trajectory error at macro-boundaries, between macro-evolved state and projected micro-state) and effective disturbance rate $\rho_\xi = \varepsilon^\ast \nu_c$ (closure defect per macro-step, multiplied by macro-update rate). The units are consistent by construction of the macro-step formulation above: $\varepsilon^\ast$ is per-macro-step (distance) and $\nu_c$ is macro-step rate ($[\text{time}^{-1}]$), so $\rho_\xi$ has the disturbance-rate units the template requires. The template yields directly:

$$\limsup_{m \to \infty} \lVert e_m \rVert \leq \frac{\varepsilon^\ast \nu_c}{\alpha_c}$$

This bound fits within the composite's sector-condition region iff $\varepsilon^\ast \lt \alpha_c R_c / \nu_c$, which is the persistence condition applied to the closure-error rate: if it fails, the macro-description diverges from micro-reality.

**What the bridge lemma adds beyond the template.** The template's precondition (T2) is the one-point sector bound. For the trajectory-error instantiation, the bound propagation requires a *strictly stronger* condition: the macro-update map $f_c(\cdot, o)$ must be contracting in its state argument (**incremental sector bound**, DA2'-inc — strong monotonicity of $F_c$), not merely one-point sector-bounded at each state. The per-step contraction factor is $\lambda = 1 - \alpha_c/\nu_c \lt 1$ (automatic when $\alpha_c \lt \nu_c$, true for any realistic agent that doesn't fully correct in a single step). This stronger condition is where the tier structure enters; see Epistemic Status for the Tier 1/2/3 taxonomy.

**The sector condition (A4) does double duty — conditionally.** (A4) ensures the macro-agent corrects external mismatch (single-agent persistence) AND — under the incremental sector bound — that the macro-description tracks micro-reality (this bridge). Both are instances of the same template applied to different state variables with different effective disturbance rates.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Closure-defect quantity $\varepsilon^\ast$ as infimum over admissible classes | Definition built from (A1)-(A4), (P1)-(P3), and $K_c$ | Formulation choice |
| Three-component decomposition into $\varepsilon_x, \varepsilon_a, \varepsilon_o$ | Match to the three arrows of the action-observation loop (state, action, observation) | Formulation choice |
| Per-macro-step formulation; $\varepsilon^\ast$ has units of distance-per-macro-step | 2026-04-22 temporal coarse-graining repair (Finding A); forced by dimensional consistency with $\rho_\xi = \varepsilon^\ast \nu_c$ in #sector-persistence-template and #tempo-composition | Derived (dimensional consistency) |
| Timescale ratio $K_c \geq 1$ as independent problem-specification parameter | Application-specific; $K_c = 1$ (synchronous) and $K_c \gg 1$ ( #temporal-nesting regime) both admissible | Formulation choice |
| (A1) Macro AAD structure $X_c = (M_c, G_c)$ with recursive update | Import from #agent-environment + #recursive-update + #action-selection | Formulation choice (requirement) |
| (A2) Well-defined macro-mismatch | Import from #mismatch-signal | Formulation choice (requirement) |
| (A3) Well-defined macro-tempo | Import from #adaptive-tempo + #update-gain | Formulation choice (requirement) |
| (A4) Sector-bounded macro-correction | Import from #sector-condition-stability | Formulation choice (requirement) |
| (A1)-(A4) as a requirement *set* render the infimum non-trivial (exclude curve-fitting macro-dynamics) | Consequence of restricting $\mathcal M_{\text{adm}}$ to genuine AAD agents | Derived (under the chosen requirement set) |
| (P1) Information-preservation constraint | IB Lagrangian-dual with source $X_{\text{micro}}$, relevance $o_{\text{micro}, t+1}$; formally connects to #compression-operations | Formulation choice (requirement) |
| (P2) Lipschitz continuity of $\Lambda$ | Required for bridge-lemma trajectory-error bound (without it, bounded $\varepsilon^\ast$ does not imply bounded trajectory error) | Formulation choice (requirement) |
| (P3) Strict dimensionality reduction | Rules out identity projection (which trivially achieves $\varepsilon^\ast = 0$ but is not abstraction) | Formulation choice (requirement) |
| (P1)-(P3) independent of (A1)-(A4) | Spike analysis (`msc/spike-projection-admissibility.md` §5) — (A1) and (A4) constrain $\Lambda_x$ partially but do not fix information-preservation level | Derived |
| Bridge lemma: $\limsup \lVert e_m \rVert \leq \varepsilon^\ast \nu_c / \alpha_c$ | Sector-persistence template ( #sector-persistence-template) applied with state $\xi = e_m$, disturbance rate $\rho_\xi = \varepsilon^\ast \nu_c$ | Derived (conditional on incremental sector bound DA2'a-inc) |
| Persistence-as-closure-boundedness condition $\varepsilon^\ast \lt \alpha_c R_c / \nu_c$ | Sector-condition region fits the asymptotic error ball | Derived (under A4 + DA2'a-inc) |
| Incremental sector bound (DA2'a-inc) is strictly stronger than (A4)'s one-point sector bound | Counterexample exhibited (oscillatory globally-inward, locally non-monotone corrections); `msc/spike-bridge-lemma-contraction.md` §4.1 | Proved |
| Three-tier agent classification (Tier 1 / 2 / 3) for bridge-lemma applicability | Taxonomy induced by whether DA2'a-inc holds globally (T1), locally (T2), or must be verified per-domain (T3) | Formulation choice (classification) |
| Tier 1: bridge lemma derived for Bayesian updaters on exponential families, gradient descent on strongly convex losses, linear correction with positive-definite gain-observation product | Standard monotone-operator / Kalman analysis; `msc/spike-bridge-lemma-contraction.md` | Derived (conditional on DA2'a-inc + linear prediction, i.e., C2) |
| Tier 2: local contraction with factor degraded by $\kappa(D\hat o)^2$ | Extended-Kalman / locally-convex analysis | Derived (local) |
| Tier 3: contraction must be verified per-domain | No general result available for non-convex / discontinuous / non-mismatch-driven components | Discussion-grade |
| Composite (A4) from sub-agent properties: $\alpha_c \geq \min_i(\alpha_i - \Delta \mathcal T_i^{\text{cost}})$, $R_c \leq \min_i R_i$ | Weakest-link bound; `msc/working-composition-admissibility.md` §6.2 | Derived (conditional on bounded coordination cost per #team-persistence) |
| Composite critical-mass inequality $(\alpha - C)R \gt \rho + \gamma\mathcal T$ (symmetric-matched-Tier-1) — sign-sensitive refinement of the weakest-link bound; recovers #team-persistence (cooperative) and #adversarial-destabilization (adversarial) as signed special cases | #critical-mass-composition | Derived (conditional on Tier 1 + matched-symmetric + Model D + coupling model C1/C2) |
| Composite persistence as (contraction) ∧ (scope-satisfaction): $\kappa_c(U_O) \gt 0 \wedge$ #scope-composite-agent | #critical-mass-composition (CM4); $U_O$ enters multiplicatively on $\gamma$ plus scope-gate, not additively | Derived (with (UO-mult) discussion-grade) |
| Asymmetric-limit connection to #symbiogenic-composition (S-3) autonomy reduction | #critical-mass-composition §asymmetric-limit; weighted Lyapunov $V_\mu$ with $\mu \to 0$ | Sketch (S-2 function transfer not yet formalized; promotable when #symbiogenic-composition closes (S-2)) |
| Meta-machine exact composition ($\varepsilon^\ast = 0$) for finite-state Moore machines | Miller 2022 §3.3; product automaton is the micro-dynamics by construction | Derived (external theorem) |
| Two-Kalman instantiation: $\varepsilon^\ast = 0$ at all $\rho_{\text{corr}}$ for the means-only projection at steady state | Analytic steady-state calculation; `msc/spike-composition-correlated-kalman.md` | Proved (closed form) |
| $\varepsilon_x$ depends on both sub-agent unity *and* update-rule heterogeneity ($\Delta K$) | Heterogeneous-gain Kalman case; #unity-closure-mapping | Derived (specific closed form for the two-Kalman case) |
| Mahalanobis norm as natural choice for estimation-type agents | Two-Kalman verification; Kalman gain minimizes expected squared Mahalanobis distance | Formulation choice (canonical for estimation; general-domain norm specification open) |
| $N$-agent scaling of $\varepsilon^\ast$ (polynomial vs. exponential in team size) | Coupling-structure dependent; `msc/spike-composition-scaling-N.md` | Open |
| Computability of (P1) for nonlinear / non-Gaussian systems | Requires Monte Carlo or variational bounds; closed-form only for linear-Gaussian | Open |
| Principled setting of the $\epsilon_I$ threshold | No formal criterion currently; candidate tying to team size and coupling structure | Open |
| Strategy-DAG projection under $\Lambda_x$ | Domain-specific; not resolved by (P1)-(P3) | Open |
| Mori-Zwanzig zero-lag bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ | Koopman/MZ projection (stationary coordinate-compatible case) | Derived (conditional on stationarity) |
| Full-kernel MZ bound on $\varepsilon^\ast$ | Type mismatch (trajectory-accumulation vs. per-step) | Refuted at the $\varepsilon^\ast$-level; natural home is the bridge-lemma trajectory-error bound |

The dividing line: (A1)-(A4) and (P1)-(P3) are *formulation choices of the requirement set* — alternative requirement sets are possible (e.g., entropy-preservation instead of MI-preservation; contraction bound in place of Lipschitz), and this one is chosen for parsimony, direct import from prior AAD segments, and downstream tractability. The *consequences* that follow under this requirement set — the non-triviality of the infimum, the bridge-lemma bound, the weakest-link composite-(A4) derivation, the two-Kalman $\varepsilon^\ast = 0$ result — are Derived, with bridge-lemma-level results carrying the additional DA2'a-inc condition (which is proved strictly stronger than (A4) alone). The Tier 1/2/3 classification is itself a formulation, but the per-tier results are derived under tier-specific conditions. Two classes of genuinely open questions remain: the computability / principled-setting questions for (P1) and $\epsilon_I$, and the $N$-agent scaling of $\varepsilon^\ast$ — the latter decides whether very large teams are representable as single AAD agents at all.

## Epistemic Status

*Conditional.* Max attainable: conditional (formulation choice).

The closure defect $\varepsilon^\ast$ is well-defined given (A1)-(A4), (P1)-(P3), the timescale ratio $K_c$, and specified norms. The macro-dynamics admissibility (A1)-(A4) and the projection admissibility (P1)-(P3) are independent formulation choices — (A1)-(A4) specify what "AAD-shaped macro-dynamics" means; (P1)-(P3) specify what "informative, regular, genuinely reductive projections" means. Both are needed for $\varepsilon^\ast$ to be an infimum over a non-trivial, non-degenerate class. The timescale ratio $K_c \geq 1$ is a third, independent piece of problem specification: it sets the granularity at which closure is measured and the type signatures of $\Lambda_o, \Lambda_a$. $K_c$ does not constrain the macro-dynamics class and is not derived — it is chosen from the timescale separation of the application (per #temporal-nesting). Both $K_c = 1$ (tightly-coupled composites) and $K_c \gg 1$ (hierarchically composed composites on their own timescale) are admissible. The projection admissibility conditions have a proposed definition with one exact instantiation (two-Kalman case at $K_c = 1$, `msc/spike-projection-admissibility.md`); general-case computability of (P1) and the dependence of $\varepsilon^\ast$ on $K_c$ for a fixed application remain open.

The bridge lemma is *conditional* — not fully derived from (A4) alone. The precise additional condition is the **incremental sector bound** (DA2'a-inc): the correction function $F_d$ must be *strongly monotone* ($\langle \delta - \delta', F_d(\delta) - F_d(\delta') \rangle \geq c_{\min} \lVert \delta - \delta' \rVert^2$ for all pairs), not just satisfy the one-point sector bound. This is strictly stronger than (A4) — a counterexample exists: oscillatory corrections that are globally inward-pointing but locally non-monotone (`msc/spike-bridge-lemma-contraction.md`, §4.1). Three tiers of agents result:

- **Tier 1 (contraction proved):** Kalman filters, exponential-family Bayesian updaters, gradient descent on strongly convex losses, all linear corrections with positive definite gain-observation product. For these agents the bridge lemma is *derived* from (A4) + DA2'a-inc + linear prediction (C2), with contraction factor $\lambda_{\text{eff}}$ from #discrete-sector-condition.
- **Tier 2 (local contraction):** Extended Kalman, locally convex gradients, nonlinear prediction models. Contraction holds locally with factor degraded by $\kappa(D\hat{o})^2$.
- **Tier 3 (independent verification):** Non-convex optimization, discontinuous/rule-based corrections, agents with non-mismatch-driven state components. Contraction must be verified per-domain.

The discrete-time recurrence argument itself is standard (Elaydi 2005); the contribution is identifying the incremental sector bound as the precise condition that bridges sector-bounded correction to full-update-map contraction. Full derivation: `msc/spike-bridge-lemma-contraction.md`.

The norm choices ($\lVert\cdot\rVert_\mathcal{X}$, $\lVert\cdot\rVert_\mathcal{A}$, $\lVert\cdot\rVert_\mathcal{O}$, and the combination norm) are load-bearing. For estimation-type agents, the Mahalanobis norm (weighted by inverse prediction-error covariance) is the natural choice — verified exactly in the two-Kalman case. For general domains, norm specification remains open.

## Discussion

This criterion replaces intuitive questions about "where the boundary of an agent is" with a functional test: does a macroscopic AAD description preserve the underlying micro-dynamics well enough to remain predictive and capable? The core requirement is an **approximate dynamical homomorphism** — the macro-dynamics approximately commute with the projection.

**Relationship to #postulate-composition-consistency.** The Section I postulate requires that AAD's machinery be scale-invariant — predictions at different levels of description must be compatible. This segment operationalizes "compatible" as "bounded closure defect under admissible coarse-graining." The admissibility constraints ensure the macro-description is genuinely AAD-shaped, so the same persistence condition, the same tempo framework, and the same mismatch dynamics apply at the macro level with macro-level parameters.

**Topology-indexed composition closures (via #contraction-template).** `#contraction-template` lifts the bridge-lemma's DA2'-inc condition into the contraction-metric framework of Lohmiller & Slotine 1998. Under its (CT1)–(CT3) preconditions, three topology-indexed closure results apply:

- **Parallel composition** preserves contraction under blockdiag metric at rate $\min(\lambda_1, \lambda_2)$ — recovers this segment's weakest-link bound.
- **Cascade composition** ($\dot x_1 = f_1(x_1)$, $\dot x_2 = f_2(x_1, x_2)$) preserves contraction under lower-triangular weighted metric at rate bounded by $\min(\lambda_1, \lambda_2)$ up to coupling-gain adjustment (Slotine 2003 Thm 2). Handles hierarchical agent structures.
- **Negative feedback with bounded loop gain** (Slotine 2003 Thm 3) gives the heterogeneous critical-mass inequality $(\lambda_1 - C_1)(\lambda_2 - C_2) > k_{12} k_{21}/4$ via (CM2-M) in #contraction-template — extending #critical-mass-composition's matched-symmetric (CM2) to heterogeneous sub-agents with different architectures and coupling strengths.

The Tier 1/2/3 bridge-lemma taxonomy of this segment maps cleanly to Tier 1M/2M/3M under #contraction-template (globally metric-contracting / locally metric-contracting / no globally valid metric). The observation that (CT2) at $M = I$ is *equivalent* to DA2'-inc means this segment has been carrying the Jacobian-level Euclidean contraction condition at the composite level all along; #contraction-template surfaces this at the single-agent level and adds the compositional theorems that generalize this segment's closure content beyond the matched-symmetric case.

**DA2'-inc ≡ (CT2) at $M = I$ — structural-transparency equivalence.** *[Derived, status: exact.]* For $C^1$ correction functions $F$ on convex domains, the following three conditions are equivalent (standard monotone-operator theory; Rockafellar & Wets 1998 *Variational Analysis* Corollary 12.4; Nesterov 2004 *Introductory Lectures on Convex Optimization* §2.1.3 Theorem 2.1.9 — strong monotonicity ⇔ symmetric-part of Jacobian uniformly positive-definite):

(a) DA2'-inc (strong monotonicity): $(\delta - \delta')^\top (F(\delta) - F(\delta')) \geq c \lVert \delta - \delta'\rVert^2$ for all $\delta, \delta'$.

(b) Jacobian-symmetric-part PD: $(\partial F/\partial\delta)_{\mathrm{sym}} \succeq c I$ pointwise on the domain.

(c) (CT2) at $M = I$ with $\lambda = c$: $-\partial F/\partial\delta - (\partial F/\partial\delta)^\top \preceq -2\lambda I$.

*Derivation.* (a) → (b): take $\delta' \to \delta$ along direction $v$, divide by $\lVert \delta - \delta'\rVert^2$, take the limit. (b) → (a): integrate $v^\top(\partial F/\partial\delta)_{\mathrm{sym}} v \geq c \lVert v\rVert^2$ along the segment from $\delta'$ to $\delta$. (b) ↔ (c): direct algebraic identity.

**Implication for AAD-internal derivability.** Under this equivalence, the Euclidean sub-scope metric-α₁ cases of `#contraction-template` (Kalman-scalar, Euclidean strongly-convex-gradient, L2-regularized, linear-PD-symmetric) are AAD-internally derived from the DA2'-inc commitment already carried at the composite level — no new axiom required. What the (CT2)-at-$M=I$ framing adds is *visibility*: the Jacobian-level condition was implicit under the DA2'-inc name; surfacing the equivalence converts the Euclidean sub-scope from "theorem-imported from Lohmiller-Slotine" to "AAD-internally derived via a standard monotone-operator identity." This is structural transparency, not new content. Non-Euclidean metric-α₂ cases (Fisher, Hessian, Lyapunov-metric) remain separately treated in `#contraction-template` — the equivalence is specific to $M = I$.

**The sector condition does double duty — conditionally.** (A4) ensures the macro-agent's corrections work (structural persistence), AND — given the additional contraction assumption (see Epistemic Status) — it ensures the macro-description tracks micro-reality (bridge lemma). Both uses address *structural persistence* in the sense of `LEXICON.md` — the capacity of the correction machinery, not the current operating point or the composite's identity through time. The central insight is that structural persistence of the composite and faithfulness to its constituents are related through the same mechanism — contracting correction dynamics under bounded perturbation — but the bridge from sector-bounded correction to full-update-map contraction requires an assumption beyond (A4) that has been verified for estimation-type agents (Kalman) and remains open for general agents. When this assumption holds, the composite that persists in its own right also persists as a faithful representation of its constituents.

**Deriving composite (A4) from sub-agent properties.** If each sub-agent satisfies the sector condition with parameters $(\alpha_i, R_i)$, and coordination costs are bounded by $\Delta\mathcal T_i^{\text{cost}}$ per agent ( #team-persistence), then the composite satisfies (A4) with:

$$\alpha_c \geq \min_i (\alpha_i - \Delta\mathcal T_i^{\text{cost}})$$

$$R_c \leq \min_i R_i$$

This is a weakest-link bound (conservative but clean). Cooperative coupling ( #team-persistence) can improve $\alpha_c$ beyond this bound by reducing effective disturbance. The key implication: (A4) is *verifiable* from micro-level properties — compute each sub-agent's sector-condition parameters, estimate coordination costs, and check whether the composite has positive correction rate. No need to compute $f_c$ directly. See `msc/working-composition-admissibility.md` §6.2 for the derivation.

**Sign-sensitive refinement (derived).** The sign-blind weakest-link bound is subsumed by #critical-mass-composition's closed-form inequality $(\alpha - C)R \gt \rho + \gamma\mathcal T$ (CM2) in the matched-symmetric-Tier-1 case, where the right-hand side makes the effective disturbance explicit and the sign of the coupling $\gamma$ (cooperative $\gamma \lt 0$ vs adversarial $\gamma \gt 0$) enters directly. (CM2) can yield composite persistence even when the weakest-link bound alone fails — when cooperative coupling reduces $\rho + \gamma\mathcal T$ below what the raw $\alpha - C$ margin would permit. #team-persistence (cooperative) and #adversarial-destabilization (adversarial) are recovered as signed special cases. The honest composite-persistence statement is the conjunction of contraction (CM3) **and** scope-satisfaction ( #scope-composite-agent) — (CM4) — making explicit that composite persistence can fail in two qualitatively different ways: the composite fails to contract, or the composite was never a composite. The asymmetric-parameter limit $\alpha_2 \to 0$ via weighted Lyapunov $V_\mu$ formalizes #symbiogenic-composition's (S-3) autonomy-reduction mechanism as a smooth deformation of (CM4), not a discontinuous regime change.

**Connection to team-persistence.** #team-persistence derives persistence conditions for sub-agents in a cooperative-adversarial network. This segment provides the macro-level complement: the conditions under which the composite itself is a valid AAD agent. Together they close the loop: sub-agents persist individually (team-persistence) AND the composite is a meaningful macro-agent (composition closure with admissibility).

**Meta-machine: exact composition for finite automata (Miller 2022).** When agents are finite-state automata (Moore machines), composition is *exact*: two machines with state sets $S_1$, $S_2$ interacting through their output/input channels form a **meta-machine** (Miller 2022, *Ex Machina*, §3.3) — itself a Moore machine with state set $S_1 \times S_2$, deterministic transitions (each machine's output determines the other's input), and a single starting state from the constituent starting states. The closure defect $\varepsilon^\ast = 0$ trivially, because the product automaton *is* the micro-dynamics — there is no approximation. The meta-machine always falls into a cycle (finite states with deterministic transitions must eventually revisit a state), so two interacting automata produce an eventually-periodic joint behavior. The composition-closure framework becomes interesting when we ask for a *compressed* macro-description: can a smaller automaton (fewer than $\lvert S_1\rvert \times \lvert S_2\rvert$ states) approximate the meta-machine? This is where $\varepsilon^\ast \gt 0$ and the admissibility constraints become non-trivial — (P3) requires genuine dimensionality reduction, and (P1) asks how much predictive information the compression preserves. Machine minimization (the theorem that every automaton has a unique minimized equivalent; Hopcroft et al. 2006) is a natural candidate for the optimal projection: the minimized meta-machine has the fewest states that reproduce the full joint behavior, achieving $\varepsilon^\ast = 0$ with (P3) satisfied whenever the minimized machine is smaller than the product. See #worked-example-cam (planned) for the full instantiation.

**Two-Kalman instantiation.** The simplest nontrivial worked case: two Kalman filters tracking correlated scalar random walks with correlation $\rho_{\text{corr}}$, no communication. This case sits at $K_c = 1$ — both sub-agents and the composite step together — so the macro-step formulation reduces to the pointwise form; the $\Lambda_o$ aggregation is the identity. The natural projection keeps the state estimates and discards the covariance states (means-only projection, dimension 2 from micro-dimension 4). At steady state, the closure defect is exactly $\varepsilon^\ast = 0$ for **all** values of $\rho_{\text{corr}}$ — the means-only projection perfectly represents the micro-dynamics because the Kalman gains converge to constants and the discarded covariance state carries no information. The "cost of independence" (the estimation performance lost by not exploiting cross-correlations) is a **performance gap** $\Delta_{\text{perf}} \approx 2\rho_{\text{corr}}^2 q^2 r / (S^\ast)^2$ (quadratic in $\rho_{\text{corr}}$ for small correlations), not a closure defect — it measures suboptimality relative to a joint filter, not failure to track the micro-dynamics. The composition-closure framework diagnoses representability ("is this group a coherent AAD agent?"), not optimality ("is this group as good as a centralized agent?"). See `msc/spike-composition-correlated-kalman.md` for the full derivation, (A1)-(A4) verification, and the first genuine $\varepsilon^\ast \gt 0$ case (purposeful agents with Beta-Bernoulli strategy updates). All three (P1)-(P3) conditions are verified exactly: $\epsilon_I = 0$ (no information loss at steady state, since the discarded covariance state is constant), $L = 1$ (the projection is a coordinate map), and $\dim(\mathcal X_c) = 2 \lt 4 = \dim(\mathcal X_{\text{micro}})$.

**Norm specification for estimation-type agents.** The two-Kalman case identifies the Mahalanobis norm as the natural choice for agents whose primary function is state estimation. The state norm weights by the inverse prediction-error covariance: $\lVert X_c - X_c' \rVert^2 = (\hat\omega_c - \hat\omega_c')^T (P_{\text{pred}}^\ast)^{-1} (\hat\omega_c - \hat\omega_c')$. The observation norm weights by the inverse innovation covariance $S^{-1} = (P_{\text{pred}}^\ast + R)^{-1}$. The general principle: norms should weight by inverse uncertainty, so that differences in well-estimated components count more than differences in poorly-estimated ones. This is the norm the Kalman filter implicitly uses — the Kalman gain minimizes the expected squared Mahalanobis distance from truth. For domains without a natural covariance structure (discrete states, non-Gaussian models), the Euclidean norm remains the default. See `msc/spike-projection-admissibility.md` §4 for derivation and §4.5 for the general-case pattern.

## Working Notes

- **Resolved: $\mathcal P_{\text{adm}}$ now has a proposed definition.** (P1)-(P3) above. Confirmed independent of (A1)-(A4) — the macro-dynamics admissibility partially constrains projections but does not specify information-preservation level. See `msc/spike-projection-admissibility.md` §5 for the analysis.
- **Resolved (2026-04-22): temporal coarse-graining gap.** The previous formulation summed $\varepsilon_x, \varepsilon_a, \varepsilon_o$ over micro-timesteps ($t=1, \ldots, H$), forcing synchronous micro-and-macro cadence. This contradicted #temporal-nesting (composites naturally update on slower timescales, $\nu_{\text{level }n+1} \ll \nu_{\text{level }n}$) and conflicted with #tempo-composition's dimensional accounting, which treats $\varepsilon^\ast$ as a per-macro-step quantity and $\nu_c$ as the macro-update rate. Introducing the timescale ratio $K_c \geq 1$ and reformulating the defects per macro-step fixes both issues: $\Lambda_o, \Lambda_a$ become window-aware (aggregating $K_c$ micro-observations/actions), the sum runs over macro-steps $m$, and $\varepsilon^\ast \nu_c$ has consistent rate units by construction. $K_c = 1$ recovers the previous formula; $K_c \gg 1$ enables the timescale abstraction that was always part of the composition theory's intent. The bridge lemma and the sector-persistence-template instantiation are unchanged in substance — the template's state variable is now $e_m$ at macro-boundaries rather than $e_t$ at micro-timesteps, but the Lyapunov argument is identical. Option 3 of `msc/pending-findings-2026-04-21.md` Finding A; Option 2 (full Mori-Zwanzig equilibrium-residual form) remains a possible future refinement if one wants an explicit singular-perturbation framing.
- **Resolved: norm choices for estimation-type agents.** The Mahalanobis norm (inverse-covariance-weighted) is the natural choice for Kalman-type agents, verified exactly in the two-Kalman case. The general principle (weight by inverse uncertainty) extends to other estimation frameworks. For non-estimation agents (discrete states, non-Gaussian), norms remain domain-specific.
- **Open: computing (P1) for nonlinear/non-Gaussian systems.** The information-preservation condition requires conditional mutual information over the joint distribution of micro-states, observations, and actions. Tractable for linear-Gaussian systems (closed-form); requires Monte Carlo estimation or variational bounds for general systems.
- **Open: the right value of $\epsilon_I$.** The information-preservation threshold is a free parameter. Too small ($\epsilon_I \to 0$) excludes useful projections; too large ($\epsilon_I \to 1$) admits degenerate ones. A natural candidate: $\epsilon_I$ comparable to the fractional information loss from adding one agent to the composite — tying it to team size and coupling structure. Formalizing this is open.
- **Open: $N$-agent scaling of $\varepsilon^\ast$.** Whether the closure defect scales polynomially or exponentially with $N$ depends on coupling structure. Tree-structured coupling (hierarchical organizations) may allow efficient dimensionality reduction; fully-connected coupling may not. This is the formal analog of the claim that very large teams cannot be treated as single agents.
- **Partial: Mori-Zwanzig connection.** Under stationarity and coordinate-compatibility assumptions on the micro-dynamics, the Koopman-operator framing lifts $\Lambda_x$ to a Hilbert-space projection $P_\Lambda$ with $Q_\Lambda = I - P_\Lambda$. The MZ-optimal Markovian macro-dynamics is $f_c^{\text{MZ}} = P_\Lambda U P_\Lambda$ (the conditional expectation given the macro-state), providing a concrete benchmark against which admissibility constraints can be measured. When $f_c^{\text{MZ}} \notin \mathcal M_{\text{adm}}$, the per-step bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ holds — a zero-lag memory-kernel bound. The bridge-lemma contraction on $f_c$ in state space corresponds to spectral gap of $Q_\Lambda U$ in observable space (distinct quantities but related). *What does not close*: the full-kernel bound $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\ell^1}$ (sum-of-lags) is a type mismatch — $\varepsilon^\ast$ is per-step; $\lVert K \rVert_{\ell^1}$ is trajectory-accumulation. Natural home for the full-kernel norm is the bridge lemma's trajectory-error bound, not $\varepsilon^\ast$ directly. *Hard obstruction*: MZ's stationarity assumption fails for purposeful agents with non-stationary auxiliary state (Beta-Bernoulli with diverging $n$) — exactly the cases where $\varepsilon^\ast \gt 0$ genuinely. Extending to these requires innovation-frame reformulation, not yet developed.
- **(P1) as IB Lagrangian-dual — resolved.** (P1) is the Lagrangian-dual of a standard IB constraint with source $X_{\text{micro}}$, compressed representation $\Lambda_x(X_{\text{micro}})$, relevance variable $o_{\text{micro},t+1} \mid a_{\text{micro},t}$, and $\beta(\epsilon_I)$ the rate-distortion multiplier. See #compression-operations for the derivation and for the shared IB shape across AAD's four compression operations ($M_t$, $\Sigma_t$, shared intent, $\Lambda$). (P2) Lipschitz continuity remains a separate analytic admissibility condition. (P3) dimensional reduction remains separate in the Gaussian case (the IB-optimal $T$ at any finite $\beta$ typically uses full support; categorical dimensional reduction is harder than any rate constraint). The "all admissibility is IB" slogan overclaims; the accurate slogan is "(P1) is IB; (P2) and (P3) compose with it as separate conditions." Cross-instance unification is shape-sharing (U-medium), not a reduction to a single master problem (U-strong) — cross-instance theorems do not follow from the shared IB shape alone.
- **Two independent drivers of $\varepsilon_x$.** The non-degenerate Kalman case (heterogeneous gains $K_1^\ast \neq K_2^\ast$ with projection $\Lambda_x(\hat\omega_1, \hat\omega_2) = (\hat\omega_1 + \hat\omega_2)/\sqrt 2$) shows $\varepsilon_x$ depends on *both* sub-agent unity (process correlation, captured by $U_M$) *and* update-rule heterogeneity ($\Delta K = K_1^\ast - K_2^\ast$). $\Delta K = 0$ gives $\varepsilon_x = 0$ at every correlation; $\Delta K \neq 0$ gives $\varepsilon_x \gt 0$ even at perfect correlation. The closed form is $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2/S_+]$ where $S_\pm$ are innovation variances in the $\pm$ rotation and $C_{+-}$ their cross-covariance. Heterogeneity is not captured by the four unity dimensions in #unity-dimensions as currently defined; this is a gap in that segment, not in this one — the closure defect correctly registers both drivers. See #unity-closure-mapping for the full analysis.
- **Open: strategy DAG projection.** How individual strategy DAGs compose under $\Lambda_x$ (union, abstracted DAG, or no macro-strategy) is deeply domain-specific and not resolved by (P1)-(P3). The information-preservation condition provides a functional test but not a specific mechanism.
- ~~The bridge lemma's contraction assumption — proving it from (A4) alone.~~ **CHARACTERIZED 2026-04-06** (`msc/spike-bridge-lemma-contraction.md`). The contraction assumption cannot be proved from (A4) alone. The precise additional condition is the **incremental sector bound** (DA2'a-inc): the correction function $F_d$ must be *strongly monotone* ($\langle \delta - \delta', F_d(\delta) - F_d(\delta') \rangle \geq c_{\min} \lVert \delta - \delta' \rVert^2$), not just satisfy the one-point sector bound. Strong monotonicity is strictly stronger than the one-point sector bound (counterexample: oscillatory corrections that are globally inward-pointing but locally non-monotone). Three agent tiers emerge: **Tier 1** (contraction proved — all Bayesian updaters on exponential families, all gradient agents on strongly convex losses, all linear corrections with positive definite gain-observation product); **Tier 2** (local contraction — nonlinear prediction models, with factor degraded by $\kappa(D\hat{o})^2$); **Tier 3** (independent verification required — non-convex optimization, discontinuous rules, agents with non-mismatch-driven state components). For Tier 1 agents, the bridge lemma is promoted from "conditional" to "derived (conditional on DA2'-inc + linear prediction)." The contraction factor equals $\lambda_{\text{eff}}$ from #discrete-sector-condition.
- The weakest-link structure ($\alpha_c = \min_i \alpha_i^{\text{eff}}$) is conservative. In practice, strong sub-agents may compensate for weak ones through cooperative coupling. A tighter bound would account for cross-agent compensation, likely through the cooperative disturbance reduction terms in #team-persistence.
- **A richer toy case** is needed: two purposeful agents (Section II) with strategy DAGs, cooperative communication, and a shared objective. This would exercise (A1) fully (including the $G_c$ component) and test whether the admissibility constraints are tight enough to be useful without being so tight they exclude interesting composites.
- The approach is an approximate dynamical homomorphism condition, a standard tool in dynamical systems and model reduction (cf. Mori-Zwanzig projection, balanced truncation). The specific contribution is applying it to AAD's closed-loop agent structure with sector-condition-based stability guarantees.
