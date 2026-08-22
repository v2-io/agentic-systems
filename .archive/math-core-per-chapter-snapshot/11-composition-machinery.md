# Composition Machinery


## Formulation: Composition Closure Criterion

- **Slug**: `form-composition-closure`
- **Type**: formulation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `post-composition-consistency`, `scope-composite-agent`, `scope-multi-agent`, `def-agent-environment`, `form-event-driven-dynamics`, `result-sector-condition-stability`, `deriv-sector-condition`, `result-sector-persistence-template`, `result-persistence-condition`

We define a group of interacting agents as a valid composite macro-agent when its closed-loop dynamics approximately commute with coarse-graining — that is, when projecting micro-states to macro-states and then running macro-dynamics yields approximately the same result as running micro-dynamics and then projecting.

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

Aggregation is part of the projection specification — common choices are mean/sum (linear systems), first/last (event-rate projections), or task-specific sufficient statistics. When $K_c = 1$ the windows collapse, $\Lambda_o, \Lambda_a$ reduce to pointwise maps, and micro- and macro-tempos coincide (synchronous-update composites). When $K_c \gg 1$ the composite operates on the quasi-steady-state output of its sub-agents, the regime that #der-temporal-nesting asserts as the natural one for composition. $K_c$ is part of the problem specification; it does not appear in (A1)-(A4) or (P1)-(P3) below, but it determines at what granularity closure is measured.

Let $\mathcal D_{\text{micro}}$ be the distribution of reachable trajectories generated entirely by the true micro-system over horizon $H$, and let $o_{\text{micro}, (m-1)K_c : m K_c}$ denote the window of $K_c$ micro-observations $(o_{\text{micro}, (m-1)K_c + 1}, \ldots, o_{\text{micro}, m K_c})$ between macro-boundaries $m-1$ and $m$ (similarly for actions).

*[Definition (Composition Closure)]* We define the minimal achievable closure defect $\varepsilon^\ast$ over the admissible classes as:

$$ \varepsilon^\ast = \inf_{\Lambda \in \mathcal P_{\text{adm}},\, (\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}} \big\lVert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\rVert $$

where the expected component errors evaluated over true micro-trajectories $\tau \sim \mathcal D_{\text{micro}}$, measured **per macro-step**, are:

- $\varepsilon_x = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_x\big(X_{\text{micro},\, m K_c}\big) - f_c\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c}),\; \Lambda_o(o_{\text{micro},\, (m-1)K_c : m K_c})\big) \big\rVert_{\mathcal{X}} \Big]$
- $\varepsilon_a = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_a\big(a_{\text{micro},\, (m-1)K_c : m K_c}\big) - \pi_c\big(\Lambda_x(X_{\text{micro},\, (m-1)K_c})\big) \big\rVert_{\mathcal{A}} \Big]$
- $\varepsilon_o = \mathbb E_\tau \Big[ \frac{1}{M_H} \sum_{m=1}^{M_H} \big\lVert \Lambda_o\big(E_{\text{obs}}(\Omega,\, a_{\text{micro}})\big\vert_{(m-1)K_c : m K_c}\big) - E_{c,\text{obs}}\big(\Lambda_\Omega(\Omega_{(m-1)K_c}),\; \pi_c(\Lambda_x(X_{\text{micro},\, (m-1)K_c}))\big) \big\rVert_{\mathcal{O}} \Big]$

where $M_H = \lfloor H/K_c \rfloor$ is the number of macro-steps in horizon $H$, and $E_{\text{obs}}(\Omega, a_{\text{micro}})\big\vert_{(m-1)K_c : m K_c}$ denotes the window of micro-observations the environment produces across the macro-step.

**Units.** $\varepsilon_x, \varepsilon_a, \varepsilon_o$ carry units of distance — per-macro-step norm errors. Multiplied by the macro-update rate $\nu_c$ (units $[\text{time}^{-1}]$), they yield the disturbance-rate units $[\text{distance}]\cdot[\text{time}^{-1}]$ demanded by the sector-persistence template's $\rho_\xi$ ( #result-sector-persistence-template) and by the dimensional accounting in #der-tempo-composition. The previous per-micro-step formulation conflated $\varepsilon^\ast$'s granularity with $\nu_c$'s — the macro-step formulation resolves the unit inconsistency.

**$K_c = 1$ special case.** When micro and macro update in lockstep, $M_H = H$, the observation/action windows collapse, and the formulas reduce to the synchronous form. This is the regime of tightly-coupled groups (distributed algorithms running in phase, ensemble filters where every member steps per tick) and is where the two-Kalman worked example below operates.

**$K_c \gg 1$ case.** When the composite lives at a strictly slower timescale than its sub-agents (the regime #der-temporal-nesting asserts as natural), only micro-states at macro-boundaries enter $\varepsilon_x$, and macro-observations aggregate $K_c$ micro-observations. The closure defect then measures how well the macro-dynamics predicts the *next* macro-state from the *previous* macro-state and the aggregated micro-observation window — not any intermediate micro-state. Timescale abstraction is recovered: the composite's description need not — and under $K_c \gg 1$ should not — track the micro-trajectory between macro-boundaries.

The closure-defect framework applies to sets that satisfy #scope-composite-agent — i.e., that form composites via at least one of the three alignment routes (shared objective, hierarchical derivation, mutual benefit). Given scope-satisfaction, a set forms a *meaningful* composite agent — distinguished from a multi-agent system whose low-$\varepsilon^\ast$ projection is a happenstance of the environment rather than a reflection of composite coherence — when $\varepsilon^\ast \leq \varepsilon_{\text{max}}$. Without scope-satisfaction, the $\varepsilon^\ast$ infimum is still well-defined as a projection property, but the resulting "composite" has ill-defined purposeful substate $G_c = (O_c, \Sigma_c)$ and composition-level machinery (team persistence, composite tempo) does not apply.

### Admissibility constraints on macro-dynamics

*[Formulation (macro-dynamics-admissibility)]*

$\mathcal M_{\text{adm}}$ is the class of macro-dynamics $(\pi_c, E_c, f_c)$ satisfying:

**(A1) AAT agent structure.** The macro-state decomposes as $X_c = (M_c, G_c)$. The macro-update is recursive at macro-time $m$:

$$X_{c,m+1} = f_c(X_{c,m}, o_{c,m+1})$$

The macro-policy is state-dependent: $a_{c,m} = \pi_c(X_{c,m})$. This ensures the macro-agent has the same structural components as a single AAT agent ( #def-agent-environment, #der-recursive-update, #der-action-selection).

**(A2) Macro-mismatch.** A mismatch signal is well-defined:

$$\delta_{c,m} = o_{c,m} - \hat{o}_{c,m}(M_c, a_{c,m-1})$$

where $\hat o_{c,m}$ is the macro-model's prediction of the next macro-observation. This ensures the macro-agent can detect prediction errors — the foundation of adaptation ( #def-mismatch-signal).

**(A3) Macro-tempo.** The macro-update has well-defined adaptive tempo:

$$\mathcal T_c = \sum_k \nu_c^{(k)} \cdot \eta_c^{(k)\ast}$$

where $k$ indexes the macro-agent's observation channels, $\nu_c^{(k)}$ is the event rate, and $\eta_c^{(k)\ast}$ is the optimal gain ( #def-adaptive-tempo, #emp-update-gain). This ensures the persistence condition is formulable at the macro level.

**(A4) Bounded macro-correction.** The macro-correction function satisfies the sector condition ( #result-sector-condition-stability):

$$\delta_c^T F_c(\mathcal T_c, \delta_c) \geq \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert \delta_c \rVert \leq R_c$$

with $\alpha_c \gt 0$ (positive correction rate) and $R_c \gt 0$ (finite reserve). This ensures the macro-agent's corrections work — they reduce mismatch rather than amplifying it, within the macro-model's capacity.

**What (A1)-(A4) prevent.** Without these constraints, the infimum over $\mathcal M_{\text{adm}}$ is trivially zero (any dynamical system can curve-fit micro-trajectories over a finite horizon). The constraints force the macro-dynamics to be a genuine AAT agent — with decomposed state, prediction errors, adaptive tempo, and stable correction — not an arbitrary function approximator. $\varepsilon^\ast$ then measures the irreducible cost of representing multiple agents as one AAT agent.

**What (A1)-(A4) do NOT require.** Directed separation ( #der-directed-separation) is not part of the admissibility constraints. It is an additional structural property that some composites have and others don't ( #hyp-directed-separation-under-composition). Results that depend on directed separation declare it as an additional assumption. Similarly, strategy structure ($G_c = (O_c, \Sigma_c)$ with a DAG) is not required — simpler goal representations are admissible.

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

**Independence from (A1)-(A4).** The macro-dynamics admissibility (A1)-(A4) partially constrains the projection — (A1) requires $\Lambda_x$ to preserve the $M_c / G_c$ decomposition, and (A4) implicitly requires regularity through the sector condition. But (A1)-(A4) do not specify how much predictive information the projection must retain. A macro-agent with a very coarse projection can satisfy (A1)-(A4) while being a poor representation of the micro-system. The information-preservation condition (P1) fills this gap. See `spikes/spike-projection-admissibility.md` §5 for the full independence analysis.

### Bridge lemma: closure defect to trajectory error

*[Derived (bridge-lemma, from sector-persistence-template + A4 + contraction assumption)]*

The bridge lemma is the sector-persistence template ( #result-sector-persistence-template) applied with state variable $\xi = e_m = X_{c,m} - \Lambda_x(X_{\text{micro},\, m K_c})$ (trajectory error at macro-boundaries, between macro-evolved state and projected micro-state) and effective disturbance rate $\rho_\xi = \varepsilon^\ast \nu_c$ (closure defect per macro-step, multiplied by macro-update rate). The units are consistent by construction of the macro-step formulation above: $\varepsilon^\ast$ is per-macro-step (distance) and $\nu_c$ is macro-step rate ($[\text{time}^{-1}]$), so $\rho_\xi$ has the disturbance-rate units the template requires. The template yields directly:

$$\limsup_{m \to \infty} \lVert e_m \rVert \leq \frac{\varepsilon^\ast \nu_c}{\alpha_c}$$

This bound fits within the composite's sector-condition region iff $\varepsilon^\ast \lt \alpha_c R_c / \nu_c$, which is the persistence condition applied to the closure-error rate: if it fails, the macro-description diverges from micro-reality.

**What the bridge lemma adds beyond the template.** The template's precondition (T2) is the one-point sector bound. For the trajectory-error instantiation, the bound propagation requires a *strictly stronger* condition: the macro-update map $f_c(\cdot, o)$ must be contracting in its state argument (**incremental sector bound**, DA2'-inc — strong monotonicity of $F_c$), not merely one-point sector-bounded at each state. The per-step contraction factor is $\lambda = 1 - \alpha_c/\nu_c \lt 1$ (automatic when $\alpha_c \lt \nu_c$, true for any realistic agent that doesn't fully correct in a single step). This stronger condition is where the tier structure enters; see Epistemic Status for the Tier 1/2/3 taxonomy.

**The sector condition (A4) does double duty — conditionally.** (A4) ensures the macro-agent corrects external mismatch (single-agent persistence) AND — under the incremental sector bound — that the macro-description tracks micro-reality (this bridge). Both are instances of the same template applied to different state variables with different effective disturbance rates.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Closure-defect quantity $\varepsilon^\ast$ as infimum over admissible classes | Definition built from (A1)-(A4), (P1)-(P3), and $K_c$ | Formulation choice |
| Three-component decomposition into $\varepsilon_x, \varepsilon_a, \varepsilon_o$ | Match to the three arrows of the action-observation loop (state, action, observation) | Formulation choice |
| Per-macro-step formulation; $\varepsilon^\ast$ has units of distance-per-macro-step | 2026-04-22 temporal coarse-graining repair (Finding A); forced by dimensional consistency with $\rho_\xi = \varepsilon^\ast \nu_c$ in #result-sector-persistence-template and #der-tempo-composition | Derived (dimensional consistency) |
| Timescale ratio $K_c \geq 1$ as independent problem-specification parameter | Application-specific; $K_c = 1$ (synchronous) and $K_c \gg 1$ ( #der-temporal-nesting regime) both admissible | Formulation choice |
| (A1) Macro AAT structure $X_c = (M_c, G_c)$ with recursive update | Import from #def-agent-environment + #der-recursive-update + #der-action-selection | Formulation choice (requirement) |
| (A2) Well-defined macro-mismatch | Import from #def-mismatch-signal | Formulation choice (requirement) |
| (A3) Well-defined macro-tempo | Import from #def-adaptive-tempo + #emp-update-gain | Formulation choice (requirement) |
| (A4) Sector-bounded macro-correction | Import from #result-sector-condition-stability | Formulation choice (requirement) |
| (A1)-(A4) as a requirement *set* render the infimum non-trivial (exclude curve-fitting macro-dynamics) | Consequence of restricting $\mathcal M_{\text{adm}}$ to genuine AAT agents | Derived (under the chosen requirement set) |
| (P1) Information-preservation constraint | IB Lagrangian-dual with source $X_{\text{micro}}$, relevance $o_{\text{micro}, t+1}$; formally connects to #disc-compression-operations | Formulation choice (requirement) |
| (P2) Lipschitz continuity of $\Lambda$ | Required for bridge-lemma trajectory-error bound (without it, bounded $\varepsilon^\ast$ does not imply bounded trajectory error) | Formulation choice (requirement) |
| (P3) Strict dimensionality reduction | Rules out identity projection (which trivially achieves $\varepsilon^\ast = 0$ but is not abstraction) | Formulation choice (requirement) |
| (P1)-(P3) independent of (A1)-(A4) | Spike analysis (`spikes/spike-projection-admissibility.md` §5) — (A1) and (A4) constrain $\Lambda_x$ partially but do not fix information-preservation level | Derived |
| Bridge lemma: $\limsup \lVert e_m \rVert \leq \varepsilon^\ast \nu_c / \alpha_c$ | Sector-persistence template ( #result-sector-persistence-template) applied with state $\xi = e_m$, disturbance rate $\rho_\xi = \varepsilon^\ast \nu_c$ | Derived (conditional on incremental sector bound DA2'a-inc) |
| Persistence-as-closure-boundedness condition $\varepsilon^\ast \lt \alpha_c R_c / \nu_c$ | Sector-condition region fits the asymptotic error ball | Derived (under A4 + DA2'a-inc) |
| Incremental sector bound (DA2'a-inc) is strictly stronger than (A4)'s one-point sector bound | Counterexample exhibited (oscillatory globally-inward, locally non-monotone corrections); `spikes/spike-bridge-lemma-contraction.md` §4.1 | Proved |
| Three-tier agent classification (Tier 1 / 2 / 3) for bridge-lemma applicability | Taxonomy induced by whether DA2'a-inc holds globally (T1), locally (T2), or must be verified per-domain (T3) | Formulation choice (classification) |
| Tier 1: bridge lemma derived for Bayesian updaters on exponential families, gradient descent on strongly convex losses, linear correction with positive-definite gain-observation product | Standard monotone-operator / Kalman analysis; `spikes/spike-bridge-lemma-contraction.md` | Derived (conditional on DA2'a-inc + linear prediction, i.e., C2) |
| Tier 2: local contraction with factor degraded by $\kappa(D\hat o)^2$ | Extended-Kalman / locally-convex analysis | Derived (local) |
| Tier 3: contraction must be verified per-domain | No general result available for non-convex / discontinuous / non-mismatch-driven components | Discussion-grade |
| Composite (A4) from sub-agent properties: $\alpha_c \geq \min_i(\alpha_i - \Delta \mathcal T_i^{\text{cost}})$, $R_c \leq \min_i R_i$ | Weakest-link bound; `msc/working-composition-admissibility.md` §6.2 | Derived (conditional on bounded coordination cost per #der-team-persistence) |
| Composite critical-mass inequality $(\alpha - C)R \gt \rho + \gamma\mathcal T$ (symmetric-matched-Tier-1) — sign-sensitive refinement of the weakest-link bound; recovers #der-team-persistence (cooperative) and #der-adversarial-destabilization (adversarial) as signed special cases | #deriv-critical-mass-composition | Derived (conditional on Tier 1 + matched-symmetric + Model D + coupling model C1/C2) |
| Composite persistence as (contraction) ∧ (scope-satisfaction): $\kappa_c(U_O) \gt 0 \wedge$ #scope-composite-agent | #deriv-critical-mass-composition (CM4); $U_O$ enters multiplicatively on $\gamma$ plus scope-gate, not additively | Derived (with (UO-mult) discussion-grade) |
| Asymmetric-limit connection to #hyp-symbiogenic-composition (S-3) autonomy reduction | #deriv-critical-mass-composition §asymmetric-limit; weighted Lyapunov $V_\mu$ with $\mu \to 0$ | Sketch (S-2 function transfer not yet formalized; promotable when #hyp-symbiogenic-composition closes (S-2)) |
| Meta-machine exact composition ($\varepsilon^\ast = 0$) for finite-state Moore machines | Miller 2022 §3.3; product automaton is the micro-dynamics by construction | Derived (external theorem) |
| Two-Kalman instantiation: $\varepsilon^\ast = 0$ at all $\rho_{\text{corr}}$ for the means-only projection at steady state | Analytic steady-state calculation; `spikes/spike-composition-correlated-kalman.md` | Proved (closed form) |
| $\varepsilon_x$ depends on both sub-agent unity *and* update-rule heterogeneity ($\Delta K$) | Heterogeneous-gain Kalman case; #result-unity-closure-mapping | Derived (specific closed form for the two-Kalman case) |
| Mahalanobis norm as natural choice for estimation-type agents | Two-Kalman verification; Kalman gain minimizes expected squared Mahalanobis distance | Formulation choice (canonical for estimation; general-domain norm specification open) |
| $N$-agent scaling of $\varepsilon^\ast$ | The "polynomial vs. exponential" framing is mis-typed (a per-step residue asked an accumulation question); `spikes/spike-composition-scaling-N.md`, CHANGELOG 2026-05-19 | Re-typed / resolved: $\varepsilon^\ast(N)$ is dimension-free-zero in the benign linear-Gaussian-stationary regime (all $N$, all coupling), graph-Laplacian-bounded with **no exponential regime** under compression (the consensus operator `#deriv-critical-mass-composition` already names), and order-incompatibility-invariant ($\leq\lvert S\rvert\log 2$, $N$-free) for strategy-DAG composition. No exponential regime exists. Full statement: the next two rows + Discussion |
| Computability of (P1) for nonlinear / non-Gaussian systems | Requires Monte Carlo or variational bounds; closed-form only for linear-Gaussian | Open |
| Principled setting of the $\epsilon_I$ threshold | No formal criterion currently; candidate tying to team size and coupling structure | Open |
| Strategy-DAG projection under $\Lambda_x$ | Causal-$\tau$-abstraction frame; #def-strategy-dag §"Composing heterogeneous strategy DAGs" (topology / SCC-condensation), #result-unity-closure-mapping (fixed-topology credence instance); CHANGELOG 2026-05-19 | Resolved (*conditional*; one named sub-open Q1): the right object is a causal-$\tau$-abstraction; exact $\Sigma_c$ iff shared sub-orders jointly acyclic + AND/OR-compatible, else the minimal admissible $\Sigma_c$ is the SCC-condensation with defect $\sum_{\lvert C\rvert\gt1}\mathrm{TC}(C)\leq\lvert S\rvert\log 2$ — **bounded by shared-plan size, $N$-free**. Beckers–Eberhardt–Halpern $(\tau,\epsilon)$-abstraction $\Rightarrow$ bounded $\varepsilon_\Sigma$ (the *frame*, not term-for-term; the high-level distance remains AAT's to choose). Q1 (constant-tightness for non-deterministic intra-SCC coupling) is a named sub-open, not a reopening |
| Mori-Zwanzig zero-lag bound $\varepsilon^\ast \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}}$ | Koopman/MZ projection (stationary coordinate-compatible case) | Derived (conditional on stationarity) |
| Full-kernel MZ bound on $\varepsilon^\ast$ | Type mismatch (trajectory-accumulation vs. per-step) | Refuted at the $\varepsilon^\ast$-level; natural home is the bridge-lemma trajectory-error bound |

The dividing line: (A1)-(A4) and (P1)-(P3) are *formulation choices of the requirement set* — alternative requirement sets are possible (e.g., entropy-preservation instead of MI-preservation; contraction bound in place of Lipschitz), and this one is chosen for parsimony, direct import from prior AAT segments, and downstream tractability. The *consequences* that follow under this requirement set — the non-triviality of the infimum, the bridge-lemma bound, the weakest-link composite-(A4) derivation, the two-Kalman $\varepsilon^\ast = 0$ result — are Derived, with bridge-lemma-level results carrying the additional DA2'a-inc condition (which is proved strictly stronger than (A4) alone). The Tier 1/2/3 classification is itself a formulation, but the per-tier results are derived under tier-specific conditions. The genuinely-open questions are now the computability / principled-setting questions for (P1) and $\epsilon_I$. The $N$-agent-scaling and strategy-DAG-projection rows are **resolved** (re-typed; the "poly-vs-exp" / "domain-specific-unresolved" framings were mis-typed — see the two rows above and CHANGELOG 2026-05-19); the prior claim that $N$-scaling "decides whether very large teams are representable as single AAT agents at all" is **withdrawn** — it was the dissolved mis-frame, not a live open question. There is no exponential-in-$N$ regime.

---



## Derived: Composite Tempo Inequality

- **Slug**: `der-tempo-composition`
- **Type**: derived
- **Status**: sketch
- **Stage**: draft
- **Depends**: `form-composition-closure`, `result-sector-persistence-template`, `def-adaptive-tempo`

The adaptive tempo of a composite agent is bounded from above by the sum of its sub-agents' tempos. The gap between aggregate potential and realized composite tempo is the coordination overhead — tempo consumed by internal reconciliation rather than external mismatch correction.

This segment instantiates the sector-persistence template ( #result-sector-persistence-template) at the composite level with state variable $\xi = \delta_c$ (composite mismatch) and a decomposed effective disturbance $\rho_{\text{eff}} = \rho_{\text{ext}} + \varepsilon^\ast \nu_c$ — external environment plus closure-defect contribution from #form-composition-closure's bridge lemma. The template supplies the Lyapunov machinery; this segment's distinctive content is the tempo-equivalent form of the coordination overhead lower bound $C_{\text{coord}} \geq \varepsilon^\ast \nu_c$.

Let $\mathcal T_i$ be the adaptive tempo of sub-agent $i$ within a composite group of $N$ agents. Let $\mathcal T_c$ be the adaptive tempo of the composite macro-agent $A_c$ defined by an admissible coarse-graining $\Lambda$.

*[Derived (Sub-additive Tempo, sketch)]* For any composite agent $A_c$ with minimal closure defect $\varepsilon^\ast \geq 0$, the composite tempo is bounded by the sum of individual tempos:
$$ \mathcal{T}_c \leq \sum_{i=1}^N \mathcal{T}_i $$

*[Definition (Coordination Overhead)]* We define the **coordination overhead penalty** $C_{\text{coord}}$ as the difference between aggregate potential and realized macro-tempo:
$$ C_{\text{coord}} := \Big( \sum_{i=1}^N \mathcal{T}_i \Big) - \mathcal{T}_c $$

---



## Hypothesis: Directed Separation Under Composition

- **Slug**: `hyp-directed-separation-under-composition`
- **Type**: hypothesis
- **Status**: conditional
- **Stage**: draft
- **Depends**: `der-directed-separation`, `scope-multi-agent`, `form-composition-closure`

When individual agents satisfy directed separation ( #der-directed-separation), does the composite macro-agent also satisfy it? The answer depends on whether the composite's internal information routing — which observations reach which sub-agents — is itself goal-dependent. Two cases arise, corresponding to the first two classes in #der-directed-separation's architectural classification.

*[Hypothesis (directed-separation-under-composition, extending directed-separation to composites)]*

Consider $N$ agents $A_1, \ldots, A_N$, each satisfying directed separation individually: $M_{i,\tau^+} = f_M^{(i)}(M_{i,\tau^-}, e_{i,\tau})$ with no $G_t^{(i)}$ argument.

**The question.** Directed separation is about **processing**, not **selection** ( #der-directed-separation, scope condition). A single agent's goals affect which events it seeks (through $\pi$), but $f_M$ processes whatever event arrives without reference to $G_t$. At the composite level, the analogous question is: does the composite's routing structure $R_t$ ( #scope-multi-agent) depend on the composite's goals $G_t^c$?

Note: sub-agents' goal-driven actions shape the environment, which other sub-agents observe. This is NOT a violation of directed separation — it is the same mechanism directed separation explicitly allows at the single-agent level: goals influence events through action, but processing of realized events is goal-blind. Agent $B$ observing environmental changes caused by $A$'s goal-driven behavior is $B$ processing a realized event goal-blindly. The observations carry information about $A$'s goals, but that is a property of the event's content, not a failure of goal-blind processing. Similarly, individual messages reflecting individual agents' goals is action through policy, not a routing-structure dependence on $G_t^c$.

### Case 1: Goal-blind routing

*[Hypothesis (Case 1)]*

If the routing structure satisfies $R_t \perp G_t^c$ ( #scope-multi-agent, goal-blind routing) — neither the communication topology $\mathcal N_t$ nor the protocol $c_t^{(j \to i)}$ depends on the composite's goals — then:

- Each sub-agent processes observations goal-blindly (individual directed separation)
- The routing is goal-blind (by construction)
- Therefore $f_M^c$ is $G_t^c$-independent

Directed separation **survives** at the composite level. Examples: military command structures with doctrinal communication protocols, software teams with defined code-review processes, multi-agent AI systems with protocol-specified message passing.

### Case 2: Goal-dependent routing

*[Hypothesis (Case 2)]*

If $R_t$ depends on $G_t^c$ — either the topology $\mathcal N_t$ changes (different reporting chains activated depending on the mission) or the protocol $c_t^{(j \to i)}$ changes (different intelligence products shared depending on the objective) — then the composite's effective observation function has a goal argument:

$$o_c = h^c(\Omega, a_{\text{micro}}, G_t^c, \xi)$$

Even if each sub-agent's $f_M^{(i)}$ processes $o_i$ goal-blindly, the **set of observations reaching each sub-agent** depends on $G_t^c$ through the routing function. Directed separation **fails** at the composite level. The composite is analogous to a Class 3 (Coupled) architecture: goal content shapes the information pathway, not through individual interpretation but through collective routing.

---



## Derived: Class Coercion via Wrapping

- **Slug**: `der-class-coercion-via-wrapping`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `der-directed-separation`, `def-agent-environment`

A Class 2 (Partial) or Class 3 (Coupled) component (one whose forward pass entangles belief-update and goal-conditioning) can be embedded inside an external scaffold whose state $X_W = (M_W, G_W)$ is updated by structurally distinct query channels: **goal-blind queries** to the component update $M_W$; **goal-conditioned queries** update $G_W$. Under stated conditions on the component, directed separation holds at the wrapper level by construction, and the composite system is Class 1 (Separated) — even though the underlying component is not. This is the constructive direction of `#hyp-directed-separation-under-composition` for the wrapper-around-component special case: a procedure for *making* directed separation hold when the underlying component does not provide it.

This segment establishes the directed-separation claim. The companion segment `#der-class-coercion-in-composition` establishes that the wrapped system is also a valid AAT composite agent (satisfying (A1)–(A4) of `#form-composition-closure`) and inherits the sector-persistence and tempo-composition machinery at the wrapper level.

### Setup

Let $A : \mathcal I_A \to \mathcal O_A$ be a primitive component, treated by the wrapper as a black-box oracle: the wrapper issues queries (inputs) and consumes responses (outputs), without access to $A$'s internal state. $\mathcal Q_A \subseteq \mathcal I_A$ is the set of admissible queries.

A **wrapper** $W$ over $A$ has state $X_W = (M_W, G_W) \in \mathcal X_M \times \mathcal X_G$ with $\mathcal X_G = \mathcal X_O \times \mathcal X_\Sigma$ per `#def-strategy-dimension`. The wrapper interacts with an environment via observations $o_W \in \mathcal O_W$ and actions $a_W \in \mathcal A_W$.

*[Definition (wrapper-update-maps)]* The wrapper's update at macro-step $m$ uses four type-signed components:

- **Belief-side query selector:** $q_M : \mathcal X_M \times \mathcal O_W \to \mathcal Q_A$. The wrapper chooses the query for $M_W$ updates from belief and observation only — *no $G_W$ argument*.
- **Strategy-side query selector:** $q_G : \mathcal X_M \times \mathcal X_G \to \mathcal Q_A$. May depend on $G_W$.
- **Belief-update map:** $f_M : \mathcal X_M \times \mathcal O_W \times \mathcal Q_A \times \mathcal O_A \to \mathcal X_M$. Updates $M_W$ from prior belief, observation, the query made, and the component's response. *No $G_W$ argument.*
- **Strategy-update map:** $f_G : \mathcal X_G \times \mathcal X_M \times \mathcal Q_A \times \mathcal O_A \to \mathcal X_G$. May depend on $G_W$.

The external policy $\pi_W : \mathcal X_W \to \mathcal A_W$ selects the wrapper's external action.

A macro-step proceeds: construct $q_M(M_W, o_W)$ → query $A$ → apply $f_M$; construct $q_G(M_W', G_W)$ → query $A$ → apply $f_G$; emit $\pi_W(X_W')$. The wrapper makes $K \geq 2$ component calls per macro-step in this minimal form (more in richer wrapper designs).

### Conditions

*[Conditions (component-admissibility)]* The theorem applies under three conditions on the component $A$:

**(C1) Goal-blind admissibility.** $\mathcal Q_A$ contains queries whose specification can be constructed from $(M_W, o_W)$ alone — i.e., a non-trivial $q_M$ exists. Components partition into three classes:
- **Class A (goal-blind by design).** $A$'s interface is goal-blind by construction — POMDP belief-state filters, world models, sensory pipelines, retrieval systems, calculators. (C1) holds trivially.
- **Class B (admit a goal-blind query mode).** $A$ supports goal-conditioned queries but also goal-blind ones. Large language models in summarization or fact-extraction modes; hybrid RL agents with separable value/policy; multi-modal models. (C1) holds operationally — the wrapper *chooses* to use the goal-blind mode.
- **Class C (fundamentally goal-conditioned).** $A$'s only operating mode requires goal-conditioning. Pure end-to-end goal-conditioned policy networks. (C1) fails; the construction does not apply.

**(C2) Stationary component conditional.** $A$'s output distribution conditional on input is fixed during the wrapper's operation: $P(A(\cdot) \mid q)$ does not depend on prior queries or on side information beyond $q$. Adaptation-during-deployment systems are out of scope.

**(C3) No implicit goal-inference.** $A$'s response to a goal-blind query does not depend on $G_W$ via inference from query patterns:

$$P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M) \quad \forall\, q_M, G_W$$

For pretrained components (notably LLMs), (C3) holds *exactly* only when query content is statistically independent of $G_W$ in the pretraining distribution. The approximate form weakens (C3) to a leakage bound (Theorem 2 below).

### Theorem 1: Directed separation at the wrapper level (exact form)

*[Derived (directed-separation-at-wrapper-exact, from C1+C2+C3)]*

Under (C1)–(C3), directed separation holds *exactly* at the wrapper level:

$$P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1},\ G_{W,m}) = P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1})$$

Therefore $W$ is a Class 1 (Separated) architecture per `#der-directed-separation`.

*Proof.* Identify all paths from $G_{W,m}$ to $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1})$. The update is

$$M_{W,m+1} = f_M\big(M_{W,m},\, o_{W,m+1},\, q_M(M_{W,m}, o_{W,m+1}),\, A(q_M(M_{W,m}, o_{W,m+1}))\big)$$

$f_M$ has no $G_W$ argument by type signature (D-pathway-1 closed). $q_M$ has no $G_W$ argument by type signature (D-pathway-2 closed). The remaining pathway is $A(q_M)$ depending on $G_W$ given $q_M$. Under (C3), $P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$ — the response is conditionally independent of $G_W$ given $q_M$. Since $q_M$ is itself a deterministic function of $(M_{W,m}, o_{W,m+1})$, conditioning on $(M_{W,m}, o_{W,m+1})$ determines $q_M$, and the integrand $P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, q_M, A(q_M)) \cdot P(A(q_M) \mid q_M, G_W)$ no longer depends on $G_W$. The conditional distribution of $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1}, G_{W,m})$ equals that given $(M_{W,m}, o_{W,m+1})$. ∎

### Theorem 2: Directed separation (approximate form, C3 weakened to leakage bound)

*[Derived (directed-separation-at-wrapper-approximate, from C1+C2+leakage-bound)]*

If (C3) is replaced by a KL-leakage bound

$$D_\text{KL}\big(P(A(q_M) \mid q_M, G_W)\, \big\Vert\, P(A(q_M) \mid q_M)\big) \le \kappa \quad \forall\, q_M, G_W$$

then the wrapper-level KL-divergence on $M_W$ updates is bounded by the same $\kappa$:

$$D_\text{KL}\big(P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, G_{W,m})\, \big\Vert\, P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1})\big) \le \kappa$$

The wrapper is *almost-Class-1 (Separated)* with leakage rate $\le \kappa$. *Proof.* The wrapper-level $M_W$ update is a deterministic function of the component response given the wrapper's other inputs; the data-processing inequality propagates the KL bound from response distribution to wrapper-state distribution. ∎

### Wrapping regime hierarchy

The construction supports three regimes, distinguished by where structural separation lives:

| Regime | Construction | Leakage bound | Leakage source |
|---|---|---|---|
| **W₀** (no wrapping) | Raw Class 2 (Partial) or Class 3 (Coupled) component | $\kappa_{W_0}$ at the component's maximum goal-conditioning sensitivity | No constraint |
| **W₂** (partial wrapping) | One goal-conditioned call per macro-step; structurally typed parsed response routes updates to $M_W$ vs. $G_W$ slots | $\kappa_{W_2}$ bounded *behaviorally* — by the component's compliance with the prompted instruction-to-separate; **no structural bound** | Component's instruction-following fidelity |
| **W₁** (strict wrapping) | Theorem 1 / 2 — separate $q_M$ and $q_G$ calls per macro-step | $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ — bounded *structurally* by mutual information in the pretraining distribution | Pretraining-induced query-content / goal-content correlation |

W₁ admits a structural bound from (C3) or its weakening; W₂ admits only a behavioral bound from the component's compliance fidelity. The two are different in kind — structural bounds are derivable from query content; behavioral bounds depend on the component's training and prompt-following. The same KL-form bound of Theorem 2 covers both regimes; what changes is *what determines* $\kappa$.

The W₀ / W₂ / W₁ distinction refines the Class 1 (Separated) cell of `#der-directed-separation`: within Class 1 (Separated), **Class-1-by-structure** (natively goal-blind components, or W₁ wrapping) has a structurally derivable directed-separation guarantee; **Class-1-by-behavior** (W₂ wrapping) has only an empirically estimable guarantee that depends on the component's instruction-following.

---



## Derived: Class Coercion in Composition

- **Slug**: `der-class-coercion-in-composition`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `der-class-coercion-via-wrapping`, `form-composition-closure`, `deriv-sector-condition`, `result-sector-persistence-template`, `der-tempo-composition`

Under the wrapper construction of `#der-class-coercion-via-wrapping`, the wrapped system $W$ is a valid AAT composite agent: it satisfies (A1)–(A4) of `#form-composition-closure`, inherits the sector-persistence template from `#result-sector-persistence-template`, and incurs a tempo cost in the Brooks's-Law form of `#der-tempo-composition`. This segment establishes those composition-level consequences. The directed-separation guarantee that motivates the construction is established in the prerequisite segment.

### Setup (inherited)

The wrapper structure, the four type-signed update components ($q_M$, $q_G$, $f_M$, $f_G$), the macro-step schedule ($K \geq 2$ component calls per macro-step), and the admissibility conditions (C1)–(C3) on the component $A$ are defined in `#der-class-coercion-via-wrapping`. This segment uses that setup without redefinition.

### Wrapper-design constraints

For (A2)–(A4) of `#form-composition-closure` to hold at the wrapper level, the wrapper's update structure must satisfy three additional constraints:

*[Conditions (wrapper-design)]*

**(D-A2)** The wrapper commits to a prediction map $\hat o_W : \mathcal X_M \times \mathcal A_W \to \mathcal O_W$ so that macro-mismatch $\delta_W = o_W - \hat o_W$ is well-defined.

**(D-A3)** $f_M$ supports a gain interpretation per `#def-adaptive-tempo`. Holds for Tier-1 belief-update maps — Bayesian on exponential families, gradient on strongly convex losses, linear-PD with bounded gain. Tier-2/3 cases inherit the corresponding tier-restricted scope from `#deriv-sector-condition`.

**(D-A4)** $f_M$ satisfies the sector condition with positive correction rate. Automatic for Tier-1 belief-update maps via `#deriv-sector-condition` Prop A.1 and `#der-gain-sector-bridge`.

(A1) of `#form-composition-closure` holds by construction — $X_W = (M_W, G_W)$ has the AAT form because the wrapper *builds it in*.

### Theorem: Wrapper as valid AAT composite agent

*[Derived (wrapper-as-composite, from (D-A2)+(D-A3)+(D-A4))]*

Under (D-A2)–(D-A4) and the directed-separation conditions of `#der-class-coercion-via-wrapping`, the wrapper $W$ satisfies (A1)–(A4) of `#form-composition-closure` and therefore qualifies as an AAT composite agent.

*Proof.* (A1) by construction of the type signatures; the wrapper's state is $X_W = (M_W, G_W)$ in the AAT shape. (A2) under (D-A2): the prediction map closes the mismatch definition. (A3) under (D-A3): Tier-1 belief-update maps inherit gain interpretation via `#deriv-sector-condition` Prop A.1, with the Tier-2/3 lifts deferring to the tier-restricted scope from `#form-composition-closure`'s bridge-lemma classification. (A4) under (D-A4): the sector condition transfers from the (Tier-1) belief-update map to the wrapper level via `#der-gain-sector-bridge`. ∎

### Inheritance of the persistence template

Under (D-A4), the wrapper inherits `#result-sector-persistence-template` at the wrapper level: persistence holds when $\alpha_W R_W \gt \rho_W$. The wrapper-level effective disturbance has two contributions: external environmental disturbance $\rho_\text{ext}$ acting through $o_W$, and internal disturbance from the component's response variance, $\rho_\text{int}$, bounded by the variance of $A$'s responses to goal-blind queries. Total: $\rho_W = \rho_\text{ext} + \rho_\text{int}$. Persistence at the wrapper level requires $\alpha_W R_W \gt \rho_\text{ext} + \rho_\text{int}$.

### Tempo cost — Brooks's-Law instance

The wrapper makes $K \geq 2$ component calls per macro-step (more in richer wrapper designs). If the component's nominal call rate is $\nu_A$, the wrapper-level macro-update rate is $\nu_W = \nu_A / K$. By `#der-tempo-composition`,

$$\mathcal T_W \leq \mathcal T_A^\text{nominal} - C_\text{coord}^\text{wrap}$$

where $C_\text{coord}^\text{wrap}$ is the coordination overhead specific to the wrapping construction — the tempo consumed by maintaining the wrapper's $(M_W, G_W)$ state separately from the component's internal state. This is the cost of class coercion paid in tempo: the same Brooks's-Law form whose general statement is in `#der-tempo-composition`. Adding state-management infrastructure reduces realized external tempo even when the underlying component's compute rate is unchanged.

---
