---
slug: der-class-coercion-in-composition
type: derived
status: conditional
depends:
  - der-class-coercion-via-wrapping
  - form-composition-closure
  - deriv-sector-condition
  - result-sector-persistence-template
  - der-tempo-composition
stage: draft
---

# Derived: Class Coercion in Composition

Under the wrapper construction of `#der-class-coercion-via-wrapping`, the wrapped system $W$ is a valid AAT composite agent: it satisfies (A1)–(A4) of `#form-composition-closure`, inherits the sector-persistence template from `#result-sector-persistence-template`, and incurs a tempo cost in the Brooks's-Law form of `#der-tempo-composition`. This segment establishes those composition-level consequences. The directed-separation guarantee that motivates the construction is established in the prerequisite segment.

## Formal Expression

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

## Epistemic Status

*Conditional* on the wrapper-design constraints (D-A2), (D-A3), (D-A4), and on the prerequisite directed-separation result of `#der-class-coercion-via-wrapping`. The proof is direct verification using inheritance from `#deriv-sector-condition` and `#def-adaptive-tempo`; both are standard. (D-A4) is automatic for Tier-1 belief-update maps; for Tier-2/3 belief-update maps the wrapper inherits the tier-restricted scope from `#deriv-sector-condition` and `#form-composition-closure`'s bridge-lemma classification.

Max attainable: derived under stated conditions. The composition-level claim is parametrized by the belief-update map's tier; Tier-1 cases inherit cleanly, Tier-2/3 cases inherit under additional restrictions.

## Discussion

### Coercion-distance vs. tracking-distance

The closure-defect $\varepsilon^\ast$ in `#form-composition-closure` is read as a *fidelity* measure: how well the macro-system tracks the projected micro-system. In the wrapping construction, the wrapper deliberately changes the underlying component's behavior to enforce separation — the wrapper *should* differ from the unwrapped component in the goal-conditioning direction. Two distinct quantities are involved:

- $\varepsilon^\ast_{\text{track}}$ — the standard fidelity quantity from `#form-composition-closure`. Used in the bridge lemma to bound trajectory error.
- $\varepsilon^\ast_{\text{coerce}}$ — the wrapping-specific quantity measuring behavioral divergence between the wrapped system and the unwrapped component. Higher means more aggressive coercion.

For wrapper analyses: the persistence-template inheritance (above) uses $\varepsilon^\ast_{\text{track}}$. Cost-of-class-coercion analyses use $\varepsilon^\ast_{\text{coerce}}$. The leakage analysis from `#der-class-coercion-via-wrapping` uses $\kappa$ — a KL-divergence on response distributions, distinct from both trajectory-error quantities. Conflating them propagates downstream confusion.

### Form-preservation reading

Read in form-preservation language, (A1)–(A4) of `#form-composition-closure` are the requirement that AAT's form survive coarse-graining: macro must itself be AAT. The wrapping construction is the *constructive* version — when the underlying component doesn't preserve form on its own (Class 2 (Partial) or Class 3 (Coupled)), the wrapper enforces form-preservation at the macro level by structural commitment of the type signatures (from `#der-class-coercion-via-wrapping`) plus the wrapper-design constraints here. The closure-defect $\varepsilon^\ast_{\text{track}}$ then plays the role of distance from the form-preserved fixed point in the constructive setup.

## Findings

### Wrapper as Valid AAT Composite Agent with Brooks's-Law Tempo Cost

**Brief:** Once you've wrapped a coupled component to get directed separation (the structural rule from `#der-class-coercion-via-wrapping`), is the wrapped system actually a valid AAT agent that AAT's machinery applies to? The answer is yes, under reasonable design constraints on the wrapper's prediction map, gain interpretation, and sector behavior. This means the wrapped system inherits the persistence-condition machinery — the wrapper's own version of "can the agent keep up with disturbance" applies, with disturbance now decomposing into the external environment's drift plus the underlying component's response variance. There's a cost, and it's Brooks's Law in tempo coordinates: every additional component call per cycle (needed to maintain separate belief and goal stores) divides the macro-update rate. The wrapped system runs slower than the component would running alone, by a structurally determined factor.

**Impact:** Closes the loop on whether the wrapping construction yields a *usable* AAT agent: yes, the wrapper inherits `#result-sector-persistence-template` and `#der-tempo-composition` at the wrapper level. Makes the tempo cost of class coercion explicit and quantifiable — it's a Brooks's-Law instance, the same general form that governs all AAT compositions, not a special-case tax. Provides the basis for analyzing logogenic-substrate wrappers (e.g., PROPRIUM's auxilia hierarchy, agentic-tft's CONTEXTUALIZE-CHOOSE phase separation) as valid composite agents with computable persistence and tempo characteristics.

**Novelty Claim:** *Claim integration* of the AAT sector-Lyapunov persistence template, Brooks's-Law tempo accounting, and the form-composition-closure (A1)–(A4) discipline, applied to the wrapper-around-component construction. The composition-level inheritance is straightforward given the persistence-template and tempo-composition machinery; the contribution is establishing that the wrapped system is in the right shape for those results to apply, and naming the Brooks's-Law form of the coercion cost.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Predictive-loss bounds under coarse-graining of MDPs | Ravindran-Barto 2004, "An algebraic approach to abstraction in reinforcement learning"; Taylor, Precup, Panangaden 2008, "Bounding performance loss in approximate MDP homomorphisms," NeurIPS; Abel, Hershkowitz, Littman 2016, "Near optimal behavior via approximate state abstraction," ICML; Subramanian, Sinha, Seraj, Mahajan 2020, "Approximate information state for approximate planning," arXiv:2010.08843; Congeduti, Mey, Oliehoek 2020, "Loss bounds for approximate influence-based abstraction," arXiv:2011.01788 | *adjacent literature* — control-theoretic predictive-loss bounds. AAT connects to this cluster via `#form-composition-closure`'s bridge lemma at the wrapper level. |
| Compositional structure for nested agents | Smithe 2024, "Structured Active Inference," arXiv:2406.07577; Capucci, Gavranović, Hedges, Rischel 2022, "Towards foundations of categorical cybernetics," ACT 2021 | *adjacent literature* — categorical / lens framing of compositional agents. The wrapper construction is consistent with the lens framing; an alternative reading in categorical-systems-theory terms is available. |
| Form-preservation under coarse-graining | Friston 2019 *J. Theor. Biol.*, "On Markov blankets and hierarchical self-organisation"; Friston, Heins, Verbelen, Da Costa et al. 2025 *Front. Network Physiology*, "From pixels to planning: scale-free active inference" | *adjacent literature* — Friston's framing of the renormalization group as form-conservation under coarse-graining. The wrapping construction reads as a constructive form-preservation move. |
| IB-Lagrangian semigroup composition | Mehta, Schwab 2014, "An exact mapping between the Variational Renormalization Group and Deep Learning," arXiv:1410.3831; Kline, Palmer 2022, "Gaussian Information Bottleneck and the Non-Perturbative Renormalization Group," PMC8967309 | *adjacent literature* — IB-as-RG. The wrapper's (P1) information-preservation condition (from `#form-composition-closure`) is IB-shaped; the semigroup composition rule is the closest analog of "AAT form preserved under iterated wrapping." |
| Singular-perturbation as unified RG | Chen, Goldenfeld, Oono 1996, "Renormalization group and singular perturbations," *Phys. Rev. E* 54:376; Chiba 2009, SIAM J. Appl. Dyn. Syst. 8:1066 | *formal antecedent* — RG framework subsumes singular perturbation theory. The $K_c \gg 1$ timescale-separation regime in `#form-composition-closure` invokes this for free. |

**Search Log:**

- 2026-05-09 (*targeted*): Search across MDP-homomorphism / hierarchical-control / categorical-systems-theory / FEP-RG / IB-RG / singular-perturbation-RG threads. Verdict: **substantial overlap** with the MDP-homomorphism and categorical-cybernetics lines as the closest formal prior art for composition under coarse-graining. AAT's contribution is the specific Brooks's-Law tempo form and the persistence-template inheritance pattern.

## Working Notes

- **Detailed tempo accounting for canonical wrapper architectures.** $C_\text{coord}^\text{wrap}$ for ReAct-shape, Reflexion-shape, PROPRIUM-shape wrappers is an empirically-relevant computation deferred from this segment's promotion. The general bound (Brooks's-Law form via `#der-tempo-composition`) is established here; specific architectural breakdowns are follow-on.
- **Connection to ELI-specific structure in `04-eli-core/`.** Most ELI-specific content (sovereignty axes, accountability infrastructure, identity factors, substrate-independence) is *added structure* beyond what the composition-level inheritance provides — this segment establishes the wrapper as a valid composite agent; ELI work is what happens on top of that substrate.
- **Segment split provenance (2026-05-11).** This segment was bifurcated from a combined "class coercion" derivation. The prerequisite segment `#der-class-coercion-via-wrapping` carries the directed-separation claim (Claim A: wrapper is Class 1 (Separated) by construction); this segment carries the composition-level claim (Claim B: wrapper is a valid AAT composite agent with persistence-template inheritance and Brooks's-Law tempo cost). The split reflects FORMAT.md Gate 1 discipline: each segment's depends list reflects exactly what its claim actually requires.
