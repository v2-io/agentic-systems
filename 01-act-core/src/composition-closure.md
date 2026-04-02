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

### Bridge lemma: closure defect to trajectory error

*[Derived (bridge-lemma, from sector-condition-derivation + A4)]*

If the macro-dynamics satisfy (A4), then bounded closure defect implies bounded trajectory error.

**Setup.** Let $\tilde X_{c,t} = \Lambda_x(X_{\text{micro},t})$ be the projected micro-state ("true" macro-state) and $X_{c,t}$ be the macro-state evolved by macro-dynamics. Define trajectory error $e_t = X_{c,t} - \tilde X_{c,t}$.

**Per-step error evolution.** At step $t$, decompose the next-step error:

$$e_{t+1} = \underbrace{f_c(\tilde X_{c,t} + e_t, o_{c,t+1}) - f_c(\tilde X_{c,t}, o_{c,t+1})}_{\text{propagation of accumulated error}} + \underbrace{f_c(\tilde X_{c,t}, o_{c,t+1}) - \tilde X_{c,t+1}}_{\text{new closure error } \leq \varepsilon_x}$$

The first term measures how the macro-update propagates existing error. By (A4), the macro-correction is contracting: it reduces the mismatch component of the state. In discrete time, the sector condition with correction rate $\alpha_c$ and event rate $\nu_c$ gives a per-step contraction factor:

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

The closure defect $\varepsilon^\ast$ is well-defined given (A1)-(A4) and specified norms. The admissibility constraints (A1)-(A4) are a *formulation choice* — they specify what "ACT-shaped macro-dynamics" means by requiring the components that ACT's results depend on. Other admissibility specifications are possible (behavioral equivalence, information-theoretic measures); this one is motivated by making the persistence machinery and the bridge lemma available at the macro level.

The bridge lemma is *derived* under the contraction assumption ($\lambda = 1 - \alpha_c / \nu_c \lt 1$, i.e., the macro-agent doesn't fully correct in one step — always true for realistic systems). The discrete-time argument uses a standard linear recurrence, not continuous-time Lyapunov, so the continuous/discrete gap is closed. The remaining assumption is that the sector condition on the correction function implies contraction of the full update map $f_c(\cdot, o)$ in its state argument — which holds when the correction dominates the state update (the correction is the primary mechanism by which the state changes in response to itself, as opposed to new information from $o$). This is the normal regime for adaptive agents; it can fail during structural adaptation when the state changes discontinuously.

The norm choices ($\lVert\cdot\rVert_\mathcal{X}$, $\lVert\cdot\rVert_\mathcal{A}$, $\lVert\cdot\rVert_\mathcal{O}$, and the combination norm) remain load-bearing and unspecified. Domain-specific instantiation will require choosing these.

## Discussion

This criterion replaces intuitive questions about "where the boundary of an agent is" with a functional test: does a macroscopic ACT description preserve the underlying micro-dynamics well enough to remain predictive and capable? The core requirement is an **approximate dynamical homomorphism** — the macro-dynamics approximately commute with the projection.

**Relationship to #composition-consistency.** The Section I postulate requires that ACT's machinery be scale-invariant — predictions at different levels of description must be compatible. This segment operationalizes "compatible" as "bounded closure defect under admissible coarse-graining." The admissibility constraints ensure the macro-description is genuinely ACT-shaped, so the same persistence condition, the same tempo framework, and the same mismatch dynamics apply at the macro level with macro-level parameters.

**The sector condition does double duty.** (A4) ensures the macro-agent's corrections work (structural persistence), AND it ensures the macro-description tracks micro-reality (bridge lemma). Both uses address *structural persistence* in the sense of `LEXICON.md` — the capacity of the correction machinery, not the current operating point or the composite's identity through time. This is the central insight: an ACT agent that is structurally persistent in its own right also persists as a faithful representation of its constituents, because both require the same thing — contracting correction dynamics under bounded perturbation.

**Deriving composite (A4) from sub-agent properties.** If each sub-agent satisfies the sector condition with parameters $(\alpha_i, R_i)$, and coordination costs are bounded by $\Delta\mathcal T_i^{\text{cost}}$ per agent ( #team-persistence), then the composite satisfies (A4) with:

$$\alpha_c \geq \min_i (\alpha_i - \Delta\mathcal T_i^{\text{cost}})$$

$$R_c \leq \min_i R_i$$

This is a weakest-link bound (conservative but clean). Cooperative coupling ( #team-persistence) can improve $\alpha_c$ beyond this bound by reducing effective disturbance. The key implication: (A4) is *verifiable* from micro-level properties — compute each sub-agent's sector-condition parameters, estimate coordination costs, and check whether the composite has positive correction rate. No need to compute $f_c$ directly. See `msc/working-composition-admissibility.md` §6.2 for the derivation.

**Connection to team-persistence.** #team-persistence derives persistence conditions for sub-agents in a cooperative-adversarial network. This segment provides the macro-level complement: the conditions under which the composite itself is a valid ACT agent. Together they close the loop: sub-agents persist individually (team-persistence) AND the composite is a meaningful macro-agent (composition closure with admissibility).

## Working Notes

- The norm choices ($\lVert\cdot\rVert_\mathcal{X}$, $\lVert\cdot\rVert_\mathcal{A}$, $\lVert\cdot\rVert_\mathcal{O}$, and the combination norm on the tuple) are load-bearing but unspecified. Domain-specific instantiation will require choosing these. For a software team, the natural norms might be task-weighted; for a military unit, they might be objective-weighted.
- The $\mathcal P_{\text{adm}}$ question (projection admissibility) is not addressed by (A1)-(A4), which constrain the macro-dynamics. Projection admissibility — what projections $\Lambda$ are allowed — is an independent question. An information-preservation approach ($\Lambda$ must retain predictive mutual information) is promising but not yet formalized.
- The bridge lemma's discrete-time formalization needs the contraction mapping theorem for one-step update maps under persistent perturbation. This is standard in discrete Lyapunov theory (Elaydi 2005) and should be a straightforward translation of the continuous-time sketch.
- The weakest-link structure ($\alpha_c = \min_i \alpha_i^{\text{eff}}$) is conservative. In practice, strong sub-agents may compensate for weak ones through cooperative coupling. A tighter bound would account for cross-agent compensation, likely through the cooperative disturbance reduction terms in #team-persistence.
- **A richer toy case** is needed: two purposeful agents (Section II) with strategy DAGs, cooperative communication, and a shared objective. This would exercise (A1) fully (including the $G_c$ component) and test whether the admissibility constraints are tight enough to be useful without being so tight they exclude interesting composites.
- The approach is an approximate dynamical homomorphism condition, a standard tool in dynamical systems and model reduction (cf. Mori-Zwanzig projection, balanced truncation). The specific contribution is applying it to ACT's closed-loop agent structure with sector-condition-based stability guarantees.
