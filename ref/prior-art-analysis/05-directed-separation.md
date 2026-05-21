# Prior-Art Analysis: Directed Separation and Architectural Coupling

> [!note]
> **Refreshed 2026-05-21** with memo-integration light-touch. The substantive content of this analysis was already aligned with the AAT segments (`#der-directed-separation`, `#der-class-coercion-via-wrapping`, `#der-class-coercion-in-composition`, and the logogenic specialization in `03-llm-core/src/der-logogenic-as-wrapping.md`); changes here clarify the **three-class** (not two-class) taxonomy and add memo-cited prior art.

**Target Claim:**
Agent architectures can be formally categorized by **Directed Separation** — the degree to which epistemic updating (beliefs, state estimation) is causally independent of teleological processing (goals, action selection). The framework distinguishes **three classes** (post-2026-05-09 GUC vocabulary):
- **Class 1 (Separated)** — epistemic update is goal-blind by construction (Kalman + LQR; POMDP belief-state filters).
- **Class 2 (Partial)** — bounded coupling: within-agent processing is Separated, but composite-level structures acquire intrinsic across-agent coupling through environment + cross-agent observation (the canonical strategic-composition outcome under goal divergence, per `#deriv-strategic-composition`).
- **Class 3 (Coupled)** — full entanglement: goal-conditioning is causally upstream of observation processing (Active Inference, LLMs at the substrate level).

Class 3 systems can be **coerced** toward Class 1 by enclosing them in an external scaffold with structurally typed query channels (`#der-class-coercion-via-wrapping`). Three regimes of decreasing strictness: **W₁ (strict wrapping)** with separate goal-blind and goal-conditioned component calls per cycle — directed separation holds *structurally* with leakage $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ bounded by pretraining-distribution mutual information; **W₂ (partial wrapping)** with one goal-conditioned call per cycle and structurally typed parsed response — directed separation holds *behaviorally* with no structural leakage bound, only the component's compliance-with-prompted-instruction-to-separate; **W₀ (no wrapping)** — raw Class 3 substrate. The W₀/W₁/W₂ hierarchy refines the Class 1 cell into **Class-1-by-structure** (W₁ or natively goal-blind) vs **Class-1-by-behavior** (W₂). Class coercion is paid in two places: more component calls per macro-step (Brooks's-Law tempo cost — derived in `#der-class-coercion-in-composition`) and a residual leakage rate $\kappa$ bounded structurally (W₁) or behaviorally (W₂).

---

## 1. State of the Field & Scientific Precedence

The Undermind search reveals a profound and explicit scientific precedence for AAT's structural dichotomy between separated and entangled architectures. This taxonomy maps cleanly onto the historical fault line between classical stochastic control (separated) and modern enactive/variational frameworks (coupled).

### Pillar 1: Class 1 Separated Architectures (The Separation Principle)
The mathematical bedrock for AAT's "Class 1" architecture is the **Separation Principle of Stochastic Control**, dating back to Wonham (1968) and Witsenhausen (1971). The Separation Theorem formally proves that for Linear-Quadratic-Gaussian (LQG) systems, optimal control can be factorized into two strictly independent modules: a state estimator (Kalman filter) that is completely blind to the control policy, and a deterministic controller (LQR) that acts on the estimator's output. In AI, this birthed the "sense-model-plan-act" pipeline, where belief updating is structurally separated from goal pursuit.

### Pillar 2: Class 3 Coupled Architectures (Dual Effect & Active Inference)
The concept that goals and observation processing become fundamentally entangled—AAT's "Class 3"—has two major precedents. 
1. **Dual Effect in Control Theory:** Bar-Shalom and Tse (1974) introduced the concept of the "dual effect," describing scenarios where an agent's control actions not only affect the system state but also alter the *quality of future information/observations*. When the dual effect is present, the separation principle breaks down, and estimation and control become intrinsically coupled.
2. **Active Inference:** Friston (2010, 2012) and the Active Inference community provide the modern formalization of entangled perception. In active inference, both action selection and belief updating are driven by the exact same objective: minimizing variational free energy. Crucially, goals (rewards) are absorbed into the agent's prior beliefs about its preferred states. Perception is no longer goal-blind; it is inherently biased by what the agent wants to achieve.

Baltieri and Buckley (2018, 2020) explicitly map this terrain, noting that the modularity of the "classical sandwich" of cognitive science perfectly mirrors the control-theoretic separation principle, whereas Active Inference provides a mathematically rigorous nonmodular (coupled) alternative. 

### Pillar 3: Blankets and Metaphysics (Friston vs. Pearl Blankets)
A critical conceptual anchor for AAT's architectural framing is provided by Bruineberg et al. (2021) in *"The Emperor’s New Markov Blankets"*. They distinguish between **Pearl blankets** (used instrumentally as an epistemic tool for conditional independence in Bayesian networks) and **Friston blankets** (used metaphysically to define the causal boundary of an agent). This maps tightly to AAT's focus on whether "perception-action coupling" is just an epistemic reality or a structural/architectural mandate.

### Pillar 4: Class Coercion and Scaffolding
The prior art for "Class Coercion" — wrapping an entangled system in a separated scaffold — has two strands:
- **Hybrid Deliberative/Reactive architectures.** Gat (1992) *Integrating planning and reacting in a heterogeneous asynchronous architecture for controlling real-world mobile robots*; Simmons (1994) *Structured control for autonomous robots*; Au (2004) on planner wrappers with external-query management — these involve orchestrating reactive (entangled) layers beneath deliberative (separated) planners. AAT's contribution here is not the wrapping move itself but the *theorem-shaped* wrapper-level directed-separation guarantee plus the explicit leakage bound and tempo tax.
- **Cognitive-architecture lineage.** Georgeff (1998) BDI; Newell (1990) Soar; Anderson (2007) ACT-R; Sun (2016) CLARION — multi-component agent designs with separated belief/goal/action state for 40+ years. The W₁ wrapping move is essentially the per-cycle commitment that cognitive architectures make at the system level.
- **Information-constrained control (closest formal cost-side ancestor).** Tanaka, Esfahani & Mitter (2015) *LQG Control With Minimum Directed Information*; Fox & Tishby (2016) *Minimum-information LQG control* — explicit price for modular structure via directed-information or rate constraints. These are the nearest formal ancestors of AAT's wrapper-level leakage; they price information / bandwidth but do not derive a specifically epistemic-vs-teleological contamination measure.
- **Modern LLM agent scaffolding (W₂ in practice).** Yao et al. (2022) *ReAct*; Shinn et al. (2023) *Reflexion*; Park et al. (2023) *Generative Agents*; Packer et al. (2023) *MemGPT*; Wang et al. (2023) *Voyager*. Most practical scaffolds are W₂ (partial wrapping / output-structuring); *Generative Agents* is the closest empirical instance of W₁ (a structurally goal-blind observation→memory step).

---

## 2. Key Anchor Papers Identified

1. **Baltieri, M., & Buckley, C. (2018). The modularity of action and perception revisited using control theory and active inference.**
   *Significance:* Explicitly draws the connection between cognitive modularity and the control-theoretic Separation Principle, contrasting it with the nonmodular structure of active inference.
2. **Bar-Shalom, Y., & Tse, E. (1974). Dual effect, certainty equivalence, and separation in stochastic control.**
   *Significance:* Formalizes when separation breaks down due to control actions affecting state uncertainty (the "dual effect"), forcing estimation and control to couple.
3. **Bruineberg, J., et al. (2021). The Emperor’s New Markov Blankets.**
   *Significance:* Provides the exact philosophical framing for distinguishing epistemic boundaries (Pearl) from architectural/metaphysical boundaries (Friston) in perception-action loops.
4. **Witsenhausen, H. (1971). Separation of estimation and control for discrete time systems.**
   *Significance:* A foundational text establishing the mathematical conditions under which belief-updating and action-selection can be structurally decoupled.

---

## 3. Conclusion on Novelty & Overlap

AAT's "Directed Separation" taxonomy is highly grounded, serving as a unifying nomenclature for a dichotomy that has existed in disparate fields for 50 years. 

**Where AAT actually contributes:**

1. **Three-class taxonomy (architectural novelty).** Class 1 (Separated) / Class 2 (Partial) / Class 3 (Coupled) is a real refinement over the usual binary modular-vs-entangled contrast. The Class 2 (Partial) class is load-bearing: many practical systems are not clean Kalman-filter stacks and not pure end-to-end entanglement either — they have mixed routing, shared infrastructure, distribution-dependent leakage, or composition-induced across-agent coupling (the canonical strategic-composition case in `#deriv-strategic-composition`). The criterion itself is structural — *are goals causally upstream of epistemic processing?* — which is sharper than codebase modularity or designer intent and closer to a real architectural invariant.

2. **Wrapper-level directed-separation theorem (theorem-grade math).** `#der-class-coercion-via-wrapping` proves: under (C1) goal-blind admissibility, (C2) stationary component conditional, and (C3) no implicit goal-inference, **directed separation holds *exactly* at the wrapper level** (Theorem 1, by conditional-independence argument over the wrapper's type signatures). Under (C3) weakened to a KL-leakage bound $\kappa$, **the wrapper-level KL on $M_W$ updates is bounded by the same $\kappa$** (Theorem 2, by the data-processing inequality). Both are Nash-style: new theorems derived using standard conditional-independence and DPI machinery in an AAT-internal axiomatic setting. The wrapper move appears materially stronger than the older hybrid-architecture literature (Gat, Simmons, Au), which shows layered control and planner wrappers but does not derive wrapper-level conditional-independence theorems.

3. **W₀/W₁/W₂ regime hierarchy + Class-1-by-structure vs Class-1-by-behavior distinction (architectural novelty).** Explicitly distinguishing structurally-derivable separation guarantees (W₁) from empirically-estimable ones (W₂) is genuinely useful and not standard in the AI-scaffolding literature. The structural bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ is theorem-grade content; the behavioral bound for W₂ depends on the component's instruction-following fidelity and has no structural upper bound. Practitioners need this distinction to know what guarantee they actually have.

4. **Composition-level consequences (theorem-grade math, with Brooks's-Law tempo cost).** `#der-class-coercion-in-composition` shows the wrapped system is a valid AAT composite agent (verifies (A1)–(A4) of `#form-composition-closure`), inherits the sector-persistence template at the wrapper level, and pays a Brooks's-Law tempo cost: $\nu_W \le \nu_A / K$ where $K \ge 2$ is the component calls per macro-step. The cost of class coercion is *paid in tempo*, in the same Brooks's-Law form that governs all AAT compositions — not a special-case tax but a general structural form.

5. **Logogenic-substrate specialization (`03-llm-core/`).** `#der-logogenic-as-wrapping` specializes the class-coercion theorem to LLMs (Class-B components in the admissibility partition) and identifies PROPRIUM-as-implemented as W₂ with the auxilia hierarchy as the candidate W₁ realization. This is the connecting bridge from AAT-core to AAT's primary applied domain (logogenic agents).

**AAT-native methodological inventions on this row:**
- The Class 1/2/3 taxonomy itself.
- The W₀/W₁/W₂ wrapping-regime hierarchy.
- The Class A/B/C component-admissibility partition (goal-blind by design / admits goal-blind mode / fundamentally goal-conditioned).
- The Class-1-by-structure vs Class-1-by-behavior distinction.
- Conditions (C1)/(C2)/(C3) and their weakening to KL-leakage bound.

**Where AAT does *not* claim novelty:**
- The Separation Principle for LQG (Wonham 1968, Witsenhausen 1971).
- The dual-effect concept (Bar-Shalom & Tse 1974).
- Active inference / variational free energy (Friston 2010, 2012).
- Pearl vs Friston blanket distinction (Bruineberg et al. 2021).
- Hybrid deliberative/reactive architectures (Gat, Simmons, Au, Arkin).
- The data-processing inequality (classical information theory).

**Epistemic status of the load-bearing segments.** `#der-directed-separation` is `status: conditional` (the architectural classification depends on the kappa_processing scope); `#der-class-coercion-via-wrapping` is `status: conditional` on (C1)/(C2)/(C3); `#der-class-coercion-in-composition` is `status: conditional` on the wrapper-design constraints (D-A2)/(D-A3)/(D-A4). Theorems are exact under stated conditions; the realistic LLM regime is Theorem 2 (approximate form) with $\kappa$ characterized empirically.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **High.** Wrapper-level directed-separation theorem (Theorem 1, exact form), KL-leakage bound theorem (Theorem 2, via DPI), Brooks's-Law tempo cost derivation, composite-class-inheritance result. Multiple theorem-grade derivations.
- *Arch Novelty:* **High.** Class 1/2/3 taxonomy, W₀/W₁/W₂ regime hierarchy, Class A/B/C admissibility partition, Class-1-by-structure-vs-behavior distinction.
- *Synth Novelty:* **High.** Unifies separation-principle ancestry with modern coupled-architecture frameworks (active inference) under one classification + bridges to LLM scaffolding practice.
- *Appl Novelty:* **High.** Direct application to LLM-agent engineering: PROPRIUM-as-W₂ characterization, auxilia-as-W₁ realization, ReAct/Reflexion/MemGPT/Voyager classified within the regime hierarchy.
- *Impact:* **High.** This is one of AAT's flagship contributions — the entire AI industry is building wrapper architectures around LLMs without a structural theory of what guarantees the wrapping provides. AAT's leakage bound + tempo cost give the wrapping practice a structural mathematical reading.