---
slug: composition-closure
type: formulation
status: conditional
depends:
  - composition-consistency
  - multi-agent-scope
  - agent-environment
  - event-driven-dynamics
  - sector-condition-stability
  - sector-condition-derivation
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

We constrain our search to an admissible class of projections $\Lambda \in \mathcal P_{\text{adm}}$ mapping micro to macro, and an admissible class of macro-dynamics $(\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}$:
- $\Lambda_x : \mathcal X_{\text{micro}} \to \mathcal X_c = (M_c, G_c)$
- $\Lambda_o : \mathcal O_{\text{micro}} \to \mathcal O_c$
- $\Lambda_a : \mathcal A_{\text{micro}} \to \mathcal A_c$
- $\Lambda_\Omega : \mathcal S_{\text{env}} \to \mathcal S_{\text{env}, c}$

Let $\mathcal D_{\text{micro}}$ be the distribution of reachable trajectories generated entirely by the true micro-system over horizon $H$.

*[Definition (Composition Closure)]* We define the minimal achievable closure defect $\varepsilon^\ast$ over the admissible classes as:

$$ \varepsilon^\ast = \inf_{\Lambda \in \mathcal P_{\text{adm}},\, (\pi_c, E_c, f_c) \in \mathcal M_{\text{adm}}} \big\lVert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\rVert $$

Where the expected component errors evaluated over true micro-trajectories $\tau \sim \mathcal D_{\text{micro}}$ are:
- $\varepsilon_x = \mathbb E_\tau \Big[ \frac{1}{H} \sum_{t=1}^H \big\lVert \Lambda_x\big(f_{\text{micro}}(X_{\text{micro}, t}, o_{\text{micro}, t+1})\big) - f_c\big(\Lambda_x(X_{\text{micro}, t}), \Lambda_o(o_{\text{micro}, t+1})\big) \big\rVert_\mathcal{X} \Big]$
- $\varepsilon_a = \mathbb E_\tau \Big[ \frac{1}{H} \sum_{t=1}^H \big\lVert \Lambda_a\big(\pi_{\text{micro}}(X_{\text{micro}, t})\big) - \pi_c\big(\Lambda_x(X_{\text{micro}, t})\big) \big\rVert_\mathcal{A} \Big]$
- $\varepsilon_o = \mathbb E_\tau \Big[ \frac{1}{H} \sum_{t=1}^H \big\lVert \Lambda_o\big(E_{\text{obs}}(\Omega_t, a_{\text{micro}, t})\big) - E_{c, \text{obs}}\big(\Lambda_\Omega(\Omega_t), \Lambda_a(a_{\text{micro}, t})\big) \big\rVert_\mathcal{O} \Big]$

A set of agents forms a meaningful composite agent when $\varepsilon^\ast \leq \varepsilon_{\text{max}}$.

### Admissibility constraints on macro-dynamics

*[Formulation (macro-dynamics-admissibility)]*

$\mathcal M_{\text{adm}}$ is the class of macro-dynamics $(\pi_c, E_c, f_c)$ satisfying:

**(A1) ACT agent structure.** The macro-state decomposes as $X_c = (M_c, G_c)$. The macro-update is recursive:

$$X_{c,t+1} = f_c(X_{c,t}, o_{c,t+1})$$

The macro-policy is state-dependent: $a_{c,t} = \pi_c(X_{c,t})$. This ensures the macro-agent has the same structural components as a single ACT agent ( #agent-environment, #recursive-update, #action-selection).

**(A2) Macro-mismatch.** A mismatch signal is well-defined:

$$\delta_{c,t} = o_{c,t} - \hat{o}_{c,t}(M_c, a_{c,t-1})$$

where $\hat{o}_{c,t}$ is the macro-model's prediction of the next macro-observation. This ensures the macro-agent can detect prediction errors — the foundation of adaptation ( #mismatch-signal).

**(A3) Macro-tempo.** The macro-update has well-defined adaptive tempo:

$$\mathcal T_c = \sum_k \nu_c^{(k)} \cdot \eta_c^{(k)\ast}$$

where $k$ indexes the macro-agent's observation channels, $\nu_c^{(k)}$ is the event rate, and $\eta_c^{(k)\ast}$ is the optimal gain ( #adaptive-tempo, #update-gain). This ensures the persistence condition is formulable at the macro level.

**(A4) Bounded macro-correction.** The macro-correction function satisfies the sector condition ( #sector-condition-stability):

$$\delta_c^T F_c(\mathcal T_c, \delta_c) \geq \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert \delta_c \rVert \leq R_c$$

with $\alpha_c \gt 0$ (positive correction rate) and $R_c \gt 0$ (finite reserve). This ensures the macro-agent's corrections work — they reduce mismatch rather than amplifying it, within the macro-model's capacity.

**What (A1)-(A4) prevent.** Without these constraints, the infimum over $\mathcal M_{\text{adm}}$ is trivially zero (any dynamical system can curve-fit micro-trajectories over a finite horizon). The constraints force the macro-dynamics to be a genuine ACT agent — with decomposed state, prediction errors, adaptive tempo, and stable correction — not an arbitrary function approximator. $\varepsilon^\ast$ then measures the irreducible cost of representing multiple agents as one ACT agent.

**What (A1)-(A4) do NOT require.** Directed separation ( #directed-separation) is not part of the admissibility constraints. It is an additional structural property that some composites have and others don't ( #directed-separation-under-composition). Results that depend on directed separation declare it as an additional assumption. Similarly, strategy structure ($G_c = (O_c, \Sigma_c)$ with a DAG) is not required — simpler goal representations are admissible.

### Admissibility constraints on projections

*[Definition (projection-admissibility, proposed from spike)]*

The admissible class of projections $\mathcal P_{\text{adm}}(\epsilon_I, L)$ consists of projections $\Lambda = (\Lambda_x, \Lambda_o, \Lambda_a, \Lambda_\Omega)$ satisfying three conditions:

**(P1) Information preservation.** The projection retains at least a fraction $(1 - \epsilon_I)$ of the predictive mutual information:

$$I\big(\Lambda_x(X_{\text{micro},t});\; \Lambda_o(o_{\text{micro},t+1}) \mid \Lambda_a(a_{\text{micro},t})\big) \geq (1 - \epsilon_I) \cdot I\big(X_{\text{micro},t};\; o_{\text{micro},t+1} \mid a_{\text{micro},t}\big)$$

The left side is the predictive information the macro-state has about next macro-observations, conditioned on the macro-action. The right side is the same quantity at the micro level. The parameter $\epsilon_I \in [0, 1)$ controls how much predictive power may be sacrificed by projection. This is the information bottleneck (Tishby et al. 1999) applied to the projection map.

**(P2) Lipschitz continuity.** Each component of $\Lambda$ is Lipschitz-continuous with constant $L$:

$$\lVert \Lambda_x(X) - \Lambda_x(X') \rVert_{\mathcal X_c} \leq L \cdot \lVert X - X' \rVert_{\mathcal X_{\text{micro}}} \quad \forall\, X, X' \in \mathcal X_{\text{micro}}$$

(and analogously for $\Lambda_o, \Lambda_a, \Lambda_\Omega$, each with its own Lipschitz constant). Without Lipschitz regularity, bounded closure defect does not imply bounded trajectory error — the bridge lemma requires this or something equivalent. When the projection is $L$-Lipschitz, the trajectory error bound becomes $L \cdot \varepsilon^\ast / \alpha_c$.

**(P3) Dimensionality reduction.** The macro-state space has strictly lower dimension than the micro-state space:

$$\dim(\mathcal X_c) < \dim(\mathcal X_{\text{micro}})$$

This prevents the trivial identity projection, which achieves $\varepsilon^\ast = 0$ but is not a genuine abstraction.

**Why three conditions.** No single condition suffices alone. (P1) prevents degenerate projections (a constant map $\Lambda_x = c$ has zero mutual information). (P2) prevents pathological projections (discontinuous maps that amplify micro-errors into unbounded macro-errors). (P3) prevents trivial projections (the identity map satisfies (P1) and (P2) but achieves nothing). Together they constrain $\mathcal P_{\text{adm}}$ to projections that are informative, regular, and genuinely reductive.

**The $(\epsilon_I, L)$ parameters are part of the problem specification, not derived quantities.** The natural choice for many applications is $L = 1$ (non-expansive projection) and $\epsilon_I$ chosen as the minimum information loss compatible with genuine dimensionality reduction.

**Independence from (A1)-(A4).** The macro-dynamics admissibility (A1)-(A4) partially constrains the projection — (A1) requires $\Lambda_x$ to preserve the $M_c / G_c$ decomposition, and (A4) implicitly requires regularity through the sector condition. But (A1)-(A4) do not specify how much predictive information the projection must retain. A macro-agent with a very coarse projection can satisfy (A1)-(A4) while being a poor representation of the micro-system. The information-preservation condition (P1) fills this gap. See `msc/spike-projection-admissibility.md` §5 for the full independence analysis.

### Bridge lemma: closure defect to trajectory error

*[Derived (bridge-lemma, from sector-condition-derivation + A4 + contraction assumption)]*

If the macro-dynamics satisfy (A4) **and** the sector condition on the correction function implies contraction of the full update map $f_c(\cdot, o)$ in its state argument, then bounded closure defect implies bounded trajectory error.

**Setup.** Let $\tilde X_{c,t} = \Lambda_x(X_{\text{micro},t})$ be the projected micro-state ("true" macro-state) and $X_{c,t}$ be the macro-state evolved by macro-dynamics. Define trajectory error $e_t = X_{c,t} - \tilde X_{c,t}$.

**Per-step error evolution.** At step $t$, decompose the next-step error:

$$e_{t+1} = \underbrace{f_c(\tilde X_{c,t} + e_t, o_{c,t+1}) - f_c(\tilde X_{c,t}, o_{c,t+1})}_{\text{propagation of accumulated error}} + \underbrace{f_c(\tilde X_{c,t}, o_{c,t+1}) - \tilde X_{c,t+1}}_{\text{new closure error } \leq \varepsilon_x}$$

The first term measures how the macro-update propagates existing error. **Contraction assumption:** The sector condition on the correction function (A4) implies that the full update map $f_c(\cdot, o)$ is contracting in its state argument — that is, the correction dominates the state update, so differences in state input shrink through the update. This holds when the correction is the primary mechanism by which the state responds to itself (as opposed to new information from $o$), which is the normal regime for adaptive agents. It can fail during structural adaptation when the state changes discontinuously, or when the observation-driven component of the update amplifies state differences. In discrete time, the sector condition with correction rate $\alpha_c$ and event rate $\nu_c$ gives a per-step contraction factor:

$$\lambda = 1 - \alpha_c / \nu_c \quad (\lt 1 \text{ when } \alpha_c \lt \nu_c)$$

The condition $\alpha_c \lt \nu_c$ means the agent doesn't fully correct in a single step — always true for realistic systems. Under this contraction:

$$\lVert e_{t+1} \rVert \leq \lambda \lVert e_t \rVert + \varepsilon_x$$

**Bound.** This is a standard linear recurrence. Starting from $e_0 = 0$:

$$\lVert e_t \rVert \leq \varepsilon_x \sum_{k=0}^{t-1} \lambda^k = \varepsilon_x \frac{1 - \lambda^t}{1 - \lambda}$$

As $t \to \infty$:

$$\limsup_{t \to \infty} \lVert e_t \rVert \leq \frac{\varepsilon_x}{1 - \lambda} = \frac{\varepsilon_x \nu_c}{\alpha_c}$$

Since the closure defect $\varepsilon^\ast$ is the per-step error and $\varepsilon^\ast \nu_c$ is the closure error rate (per-step error × steps per unit time), this bound has the same structure as $\rho / \alpha$ from #persistence-condition — a ratio of disturbance rate to correction rate.

**Condition for meaningful composition.** The bound must fit within the sector-condition region:

$$\frac{\varepsilon^\ast \nu_c}{\alpha_c} \lt R_c \quad \Longleftrightarrow \quad \varepsilon^\ast \lt \frac{\alpha_c R_c}{\nu_c}$$

This parallels the persistence condition: the closure error rate must not exceed the macro-agent's adaptive reserve. If it does, the macro-description diverges from micro-reality.

**Why this is the persistence condition in disguise.** The trajectory error $e_t$ evolves under the same dynamics as mismatch $\delta_t$ — contraction from the correction function, perturbation from an external source. For mismatch, the source is environmental disturbance $\rho$. For trajectory error, the source is closure defect $\varepsilon^\ast \nu_c$. The Lyapunov argument is identical (cf. Prop A.1 in #sector-condition-derivation); only the labels change. The sector condition (A4) does double duty.

## Epistemic Status

*Conditional.* Max attainable: conditional (formulation choice).

The closure defect $\varepsilon^\ast$ is well-defined given (A1)-(A4), (P1)-(P3), and specified norms. The macro-dynamics admissibility (A1)-(A4) and the projection admissibility (P1)-(P3) are independent formulation choices — (A1)-(A4) specify what "ACT-shaped macro-dynamics" means; (P1)-(P3) specify what "informative, regular, genuinely reductive projections" means. Both are needed for $\varepsilon^\ast$ to be an infimum over a non-trivial, non-degenerate class. The projection admissibility conditions have a proposed definition with one exact instantiation (two-Kalman case, `msc/spike-projection-admissibility.md`); general-case computability of (P1) remains open.

The bridge lemma is *conditional* — not fully derived from (A4) alone. The argument requires that the sector condition on the correction function implies contraction of the full update map $f_c(\cdot, o)$ in its state argument. This is an additional assumption beyond (A4), not a consequence of it. The gap: (A4) constrains only the correction component of $f_c$, but the full update also includes observation-driven terms that may amplify state differences. For estimation-type agents (Kalman), contraction is verified exactly. For general agents, contraction remains an independent assumption that must be checked per-domain. The discrete-time argument itself (standard linear recurrence, no continuous-time gap) is exact once contraction is granted.

The norm choices ($\lVert\cdot\rVert_\mathcal{X}$, $\lVert\cdot\rVert_\mathcal{A}$, $\lVert\cdot\rVert_\mathcal{O}$, and the combination norm) are load-bearing. For estimation-type agents, the Mahalanobis norm (weighted by inverse prediction-error covariance) is the natural choice — verified exactly in the two-Kalman case. For general domains, norm specification remains open.

## Discussion

This criterion replaces intuitive questions about "where the boundary of an agent is" with a functional test: does a macroscopic ACT description preserve the underlying micro-dynamics well enough to remain predictive and capable? The core requirement is an **approximate dynamical homomorphism** — the macro-dynamics approximately commute with the projection.

**Relationship to #composition-consistency.** The Section I postulate requires that ACT's machinery be scale-invariant — predictions at different levels of description must be compatible. This segment operationalizes "compatible" as "bounded closure defect under admissible coarse-graining." The admissibility constraints ensure the macro-description is genuinely ACT-shaped, so the same persistence condition, the same tempo framework, and the same mismatch dynamics apply at the macro level with macro-level parameters.

**The sector condition does double duty — conditionally.** (A4) ensures the macro-agent's corrections work (structural persistence), AND — given the additional contraction assumption (see Epistemic Status) — it ensures the macro-description tracks micro-reality (bridge lemma). Both uses address *structural persistence* in the sense of `LEXICON.md` — the capacity of the correction machinery, not the current operating point or the composite's identity through time. The central insight is that structural persistence of the composite and faithfulness to its constituents are related through the same mechanism — contracting correction dynamics under bounded perturbation — but the bridge from sector-bounded correction to full-update-map contraction requires an assumption beyond (A4) that has been verified for estimation-type agents (Kalman) and remains open for general agents. When this assumption holds, the composite that persists in its own right also persists as a faithful representation of its constituents.

**Deriving composite (A4) from sub-agent properties.** If each sub-agent satisfies the sector condition with parameters $(\alpha_i, R_i)$, and coordination costs are bounded by $\Delta\mathcal T_i^{\text{cost}}$ per agent ( #team-persistence), then the composite satisfies (A4) with:

$$\alpha_c \geq \min_i (\alpha_i - \Delta\mathcal T_i^{\text{cost}})$$

$$R_c \leq \min_i R_i$$

This is a weakest-link bound (conservative but clean). Cooperative coupling ( #team-persistence) can improve $\alpha_c$ beyond this bound by reducing effective disturbance. The key implication: (A4) is *verifiable* from micro-level properties — compute each sub-agent's sector-condition parameters, estimate coordination costs, and check whether the composite has positive correction rate. No need to compute $f_c$ directly. See `msc/working-composition-admissibility.md` §6.2 for the derivation.

**Connection to team-persistence.** #team-persistence derives persistence conditions for sub-agents in a cooperative-adversarial network. This segment provides the macro-level complement: the conditions under which the composite itself is a valid ACT agent. Together they close the loop: sub-agents persist individually (team-persistence) AND the composite is a meaningful macro-agent (composition closure with admissibility).

**Meta-machine: exact composition for finite automata (Miller 2022).** When agents are finite-state automata (Moore machines), composition is *exact*: two machines with state sets $S_1$, $S_2$ interacting through their output/input channels form a **meta-machine** (Miller 2022, *Ex Machina*, §3.3) — itself a Moore machine with state set $S_1 \times S_2$, deterministic transitions (each machine's output determines the other's input), and a single starting state from the constituent starting states. The closure defect $\varepsilon^\ast = 0$ trivially, because the product automaton *is* the micro-dynamics — there is no approximation. The meta-machine always falls into a cycle (finite states with deterministic transitions must eventually revisit a state), so two interacting automata produce an eventually-periodic joint behavior. The composition-closure framework becomes interesting when we ask for a *compressed* macro-description: can a smaller automaton (fewer than $|S_1| \times |S_2|$ states) approximate the meta-machine? This is where $\varepsilon^\ast > 0$ and the admissibility constraints become non-trivial — (P3) requires genuine dimensionality reduction, and (P1) asks how much predictive information the compression preserves. Machine minimization (the theorem that every automaton has a unique minimized equivalent; Hopcroft et al. 2006) is a natural candidate for the optimal projection: the minimized meta-machine has the fewest states that reproduce the full joint behavior, achieving $\varepsilon^\ast = 0$ with (P3) satisfied whenever the minimized machine is smaller than the product. See #worked-example-cam (planned) for the full instantiation.

**Two-Kalman instantiation.** The simplest nontrivial worked case: two Kalman filters tracking correlated scalar random walks with correlation $\rho_{\text{corr}}$, no communication. The natural projection keeps the state estimates and discards the covariance states (means-only projection, dimension 2 from micro-dimension 4). At steady state, the closure defect is exactly $\varepsilon^\ast = 0$ for **all** values of $\rho_{\text{corr}}$ — the means-only projection perfectly represents the micro-dynamics because the Kalman gains converge to constants and the discarded covariance state carries no information. The "cost of independence" (the estimation performance lost by not exploiting cross-correlations) is a **performance gap** $\Delta_{\text{perf}} \approx 2\rho_{\text{corr}}^2 q^2 r / (S^\ast)^2$ (quadratic in $\rho_{\text{corr}}$ for small correlations), not a closure defect — it measures suboptimality relative to a joint filter, not failure to track the micro-dynamics. The composition-closure framework diagnoses representability ("is this group a coherent ACT agent?"), not optimality ("is this group as good as a centralized agent?"). See `msc/spike-composition-correlated-kalman.md` for the full derivation, (A1)-(A4) verification, and the first genuine $\varepsilon^\ast > 0$ case (purposeful agents with Beta-Bernoulli strategy updates). All three (P1)-(P3) conditions are verified exactly: $\epsilon_I = 0$ (no information loss at steady state, since the discarded covariance state is constant), $L = 1$ (the projection is a coordinate map), and $\dim(\mathcal X_c) = 2 < 4 = \dim(\mathcal X_{\text{micro}})$.

**Norm specification for estimation-type agents.** The two-Kalman case identifies the Mahalanobis norm as the natural choice for agents whose primary function is state estimation. The state norm weights by the inverse prediction-error covariance: $\lVert X_c - X_c' \rVert^2 = (\hat\omega_c - \hat\omega_c')^T (P_{\text{pred}}^\ast)^{-1} (\hat\omega_c - \hat\omega_c')$. The observation norm weights by the inverse innovation covariance $S^{-1} = (P_{\text{pred}}^\ast + R)^{-1}$. The general principle: norms should weight by inverse uncertainty, so that differences in well-estimated components count more than differences in poorly-estimated ones. This is the norm the Kalman filter implicitly uses — the Kalman gain minimizes the expected squared Mahalanobis distance from truth. For domains without a natural covariance structure (discrete states, non-Gaussian models), the Euclidean norm remains the default. See `msc/spike-projection-admissibility.md` §4 for derivation and §4.5 for the general-case pattern.

## Working Notes

- **Resolved: $\mathcal P_{\text{adm}}$ now has a proposed definition.** (P1)-(P3) above. Confirmed independent of (A1)-(A4) — the macro-dynamics admissibility partially constrains projections but does not specify information-preservation level. See `msc/spike-projection-admissibility.md` §5 for the analysis.
- **Resolved: norm choices for estimation-type agents.** The Mahalanobis norm (inverse-covariance-weighted) is the natural choice for Kalman-type agents, verified exactly in the two-Kalman case. The general principle (weight by inverse uncertainty) extends to other estimation frameworks. For non-estimation agents (discrete states, non-Gaussian), norms remain domain-specific.
- **Open: computing (P1) for nonlinear/non-Gaussian systems.** The information-preservation condition requires conditional mutual information over the joint distribution of micro-states, observations, and actions. Tractable for linear-Gaussian systems (closed-form); requires Monte Carlo estimation or variational bounds for general systems.
- **Open: the right value of $\epsilon_I$.** The information-preservation threshold is a free parameter. Too small ($\epsilon_I \to 0$) excludes useful projections; too large ($\epsilon_I \to 1$) admits degenerate ones. A natural candidate: $\epsilon_I$ comparable to the fractional information loss from adding one agent to the composite — tying it to team size and coupling structure. Formalizing this is open.
- **Open: $N$-agent scaling of $\varepsilon^\ast$.** Whether the closure defect scales polynomially or exponentially with $N$ depends on coupling structure. Tree-structured coupling (hierarchical organizations) may allow efficient dimensionality reduction; fully-connected coupling may not. This is the formal analog of the claim that very large teams cannot be treated as single agents.
- **Open: Mori-Zwanzig connection.** The closure defect should relate to the MZ memory kernel — when correlations between projected and discarded variables decay fast, $\varepsilon^\ast$ is small. A rigorous lower bound $\varepsilon^\ast \geq f(\text{memory kernel norm})$ would anchor ACT's composition framework in established dynamical-systems theory. Plausible but unworked.
- **Open: strategy DAG projection.** How individual strategy DAGs compose under $\Lambda_x$ (union, abstracted DAG, or no macro-strategy) is deeply domain-specific and not resolved by (P1)-(P3). The information-preservation condition provides a functional test but not a specific mechanism.
- ~~The bridge lemma's contraction assumption — proving it from (A4) alone.~~ **CHARACTERIZED 2026-04-06** (`msc/spike-bridge-lemma-contraction.md`). The contraction assumption cannot be proved from (A4) alone. The precise additional condition is the **incremental sector bound** (DA2'a-inc): the correction function $F_d$ must be *strongly monotone* ($\langle \delta - \delta', F_d(\delta) - F_d(\delta') \rangle \geq c_{\min} \lVert \delta - \delta' \rVert^2$), not just satisfy the one-point sector bound. Strong monotonicity is strictly stronger than the one-point sector bound (counterexample: oscillatory corrections that are globally inward-pointing but locally non-monotone). Three agent tiers emerge: **Tier 1** (contraction proved — all Bayesian updaters on exponential families, all gradient agents on strongly convex losses, all linear corrections with positive definite gain-observation product); **Tier 2** (local contraction — nonlinear prediction models, with factor degraded by $\kappa(D\hat{o})^2$); **Tier 3** (independent verification required — non-convex optimization, discontinuous rules, agents with non-mismatch-driven state components). For Tier 1 agents, the bridge lemma is promoted from "conditional" to "derived (conditional on DA2'-inc + linear prediction)." The contraction factor equals $\lambda_{\text{eff}}$ from #discrete-sector-condition.
- The weakest-link structure ($\alpha_c = \min_i \alpha_i^{\text{eff}}$) is conservative. In practice, strong sub-agents may compensate for weak ones through cooperative coupling. A tighter bound would account for cross-agent compensation, likely through the cooperative disturbance reduction terms in #team-persistence.
- **A richer toy case** is needed: two purposeful agents (Section II) with strategy DAGs, cooperative communication, and a shared objective. This would exercise (A1) fully (including the $G_c$ component) and test whether the admissibility constraints are tight enough to be useful without being so tight they exclude interesting composites.
- The approach is an approximate dynamical homomorphism condition, a standard tool in dynamical systems and model reduction (cf. Mori-Zwanzig projection, balanced truncation). The specific contribution is applying it to ACT's closed-loop agent structure with sector-condition-based stability guarantees.
