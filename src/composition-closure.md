---
slug: composition-closure
type: formulation
status: conditional
depends:
  - composition-consistency
  - multi-agent-scope
  - agent-environment
  - event-driven-dynamics
---

# Formulation: Composition Closure Criterion

We define a group of interacting agents as a valid composite macro-agent when its closed-loop dynamics approximately commute with coarse-graining — that is, when projecting micro-states to macro-states and then running macro-dynamics yields approximately the same result as running micro-dynamics and then projecting.

## Formal Expression

Let a system consist of $N$ sub-agents interacting in a shared environment with state space $\mathcal S_{env}$. The micro-state, micro-observations, and micro-actions are:

$$X_{micro, t} = \{ (M_{i,t}, G_{i,t}) \}_{i=1}^N \in \mathcal X_{micro}$$

$$o_{micro, t} = \{ o_{i,t} \}_{i=1}^N \in \mathcal O_{micro}$$

$$a_{micro, t} = \{ a_{i,t} \}_{i=1}^N \in \mathcal A_{micro}$$

The coupled micro-dynamics form an action-observation loop:

$$X_{micro, t} \xrightarrow{\pi_{micro}} a_{micro, t} \xrightarrow{E} (\Omega_{t+1}, o_{micro, t+1}) \xrightarrow{f_{micro}} X_{micro, t+1}$$

We constrain our search to an admissible class of projections $\Lambda \in \mathcal P_{adm}$ mapping micro to macro, and an admissible class of macro-dynamics $(\pi_c, E_c, f_c) \in \mathcal M_{adm}$:
- $\Lambda_x : \mathcal X_{micro} \to \mathcal X_c = (M_c, G_c)$
- $\Lambda_o : \mathcal O_{micro} \to \mathcal O_c$
- $\Lambda_a : \mathcal A_{micro} \to \mathcal A_c$
- $\Lambda_\Omega : \mathcal S_{env} \to \mathcal S_{env, c}$

Let $\mathcal D_{micro}$ be the distribution of reachable trajectories generated entirely by the true micro-system over horizon $H$.

*[Definition (Composition Closure)]* We define the minimal achievable closure defect $\varepsilon^\ast$ over the admissible classes as:
$$ \varepsilon^* = \inf_{\Lambda \in \mathcal{P}_{adm}, (\pi_c, E_c, f_c) \in \mathcal{M}_{adm}} \big\Vert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\Vert $$

Where the expected component errors evaluated over true micro-trajectories $\tau \sim \mathcal D_{micro}$ are:
- $\varepsilon_x = \mathbb E_{\tau} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_x\big(f_{micro}(X_{micro, t}, o_{micro, t+1})\big) - f_c\big(\Lambda_x(X_{micro, t}), \Lambda_o(o_{micro, t+1})\big) \big\Vert_{\mathcal{X}} \Big]$
- $\varepsilon_a = \mathbb E_{\tau} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_a\big(\pi_{micro}(X_{micro, t})\big) - \pi_c\big(\Lambda_x(X_{micro, t})\big) \big\Vert_{\mathcal{A}} \Big]$
- $\varepsilon_o = \mathbb E_{\tau} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_o\big(E_{obs}(\Omega_t, a_{micro, t})\big) - E_{c, obs}\big(\Lambda_\Omega(\Omega_t), \Lambda_a(a_{micro, t})\big) \big\Vert_{\mathcal{O}} \Big]$

A set of agents forms a meaningful composite agent when $\varepsilon^\ast \leq \varepsilon_{max}$.

## Epistemic Status

*Conditional.* Max attainable: conditional (formulation choice). The mathematical definition of $\varepsilon^\ast$ is well-formed — given specified norms and admissibility constraints, it's a well-defined infimum. The formulation is conditional on two under-specified components: (1) the admissibility constraints ($\mathcal P_{adm}$ and $\mathcal M_{adm}$) that prevent trivial closure by requiring the macro-agent to satisfy ACT's structural requirements, and (2) the norm choices for states, actions, and observations, which are load-bearing — different norms yield different $\varepsilon^\ast$ values. The criterion itself is a *formulation choice*: approximate dynamical homomorphism is one way to operationalize the scale invariance required by #composition-consistency, but not the only possible one.

## Discussion

This criterion replaces intuitive questions about "where the boundary of an agent is" with a functional test: does a macroscopic ACT description preserve the underlying micro-dynamics well enough to remain predictive and capable? The core requirement is an **approximate dynamical homomorphism** — the macro-dynamics approximately commute with the projection.

Without admissibility constraints on $\mathcal P_{adm}$ and $\mathcal M_{adm}$, closure would be trivial (e.g., arbitrarily curve-fitting an open-loop model). By forcing the macro-components to retain the structure of an ACT agent, the minimal closure defect $\varepsilon^\ast$ quantifies the irreducible cost of being multiple. High qualitative unity (shared models, shared objectives) strongly predicts a low $\varepsilon^\ast$.

**Relationship to #composition-consistency.** The Section I postulate requires that ACT's machinery be scale-invariant — predictions at different levels of description must be compatible. This segment operationalizes "compatible" as "bounded closure defect under admissible coarse-graining." Other operationalizations are possible (e.g., behavioral equivalence, information-theoretic measures), making this a formulation choice rather than a derived consequence.

## Working Notes
- The admissibility constraints are the hard part and currently serve as placeholders. What exactly must the macro-agent satisfy? Recursive update? Directed separation? The full scope condition? Specifying $\mathcal M_{adm}$ is where the real content will live.
- The norm choices ($\Vert\cdot\Vert_{\mathcal{X}}$, $\Vert\cdot\Vert_{\mathcal{A}}$, $\Vert\cdot\Vert_{\mathcal{O}}$, and the combination norm on the tuple) are load-bearing but unspecified. Domain-specific instantiation will require choosing these.
- Bridge lemma needed: small expected component-wise errors guarantee bounded trajectory divergence only if the admissible macro-dynamics $\mathcal M_{adm}$ satisfy appropriate Lipschitz stability conditions. Without this, bounded $\varepsilon^\ast$ doesn't formally guarantee bounded trajectory error.
- The approach is an approximate dynamical homomorphism condition, a standard tool in dynamical systems and model reduction (cf. Mori-Zwanzig projection, balanced truncation). The specific contribution is applying it to ACT's closed-loop agent structure.
