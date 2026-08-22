# TF-00: Notation and Conventions

This document defines all symbols used in Temporal Feedback Theory, serving as a single authoritative reference. When a symbol appears in any TF document, its meaning is as defined here unless explicitly noted otherwise.

## Equation Tag Semantics

Displayed equations in TF documents are prefixed with inline tags `*[ ... ]*` to indicate epistemic status at equation level.

- `Definition`: Introduces a quantity, object, or notation.
- `Formulation`: Representational or modeling choice.
- `Derived`: Logical consequence of prior assumptions/definitions.
- `Hypothesis`: Assumed dynamic/relationship not proved in TFT.
- `Empirical Claim`: Generalization supported by domain evidence, not fully derived.
- `Discussion`: Conceptual or normative expression used for interpretation/design.
- `Derived (Conditional on ...)`: Derived result that depends on explicitly named assumptions.

## The Adaptive Loop

The adaptive feedback loop at the heart of TFT unfolds in five phases, named from Greek philosophical vocabulary for precision and to mark TFT as a logogenic theory.

| Phase | Greek | Sense | TFT Step |
|-------|-------|-------|----------|
| **Prolepsis** (πρόληψις) | Anticipation | Stoic preconception through which experience is interpreted | Model generates prediction: $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ |
| **Aisthesis** (αἴσθησις) | Perception | Raw sensory contact between agent and world | Observation arrives: $o_t$ |
| **Aporia** (ἀπορία) | Perplexity | Recognizing that reality differs from expectation | Mismatch signal: $\delta_t = o_t - \hat o_t$ |
| **Epistrophe** (ἐπιστροφή) | Turning-toward | The model turns toward reality, proportionally | Gain-weighted update: $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ |
| **Praxis** (πρᾶξις) | Informed action | Action arising from understanding, not mere motion | Action selection: $a_t = \pi(M_t)$ |

The loop is: Prolepsis → Aisthesis → Aporia → Epistrophe → Praxis → (Prolepsis). The terms carry their own weight and do not require an acronym.

## Primitives (TF-01)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\Omega$ | State space | Environment state (unobservable totality) | TF-01 |
| $\Omega_t$ | State | Environment state at time $t$ | TF-01 |
| $\mathcal{O}$ | Set | Observation space | TF-01 |
| $\mathcal{A}$ | Set | Action space | TF-01 |
| $o_t$ | $\in \mathcal{O}$ | Observation at time $t$ | TF-01 |
| $a_t$ | $\in \mathcal{A}$ | Action at time $t$ | TF-01 |
| $h$ | Function | Observation function: $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$. Action-dependence is optional; when absent, reduces to $h(\Omega_t, \varepsilon_t)$ | TF-01 |
| $T$ | Distribution | Transition: $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ | TF-01 |
| $\varepsilon_t$ | Random variable | Observation noise | TF-01 |
| $H(\cdot)$ | Functional | Shannon entropy | Standard |
| $I(\cdot; \cdot)$ | Functional | Mutual information | Standard |

## Temporal Structure (TF-02)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\mathcal C_t$ | Sequence | Interaction history (*chronica*): $(o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$. The singular, non-forkable causal record of the agent's experience. | TF-02 |
| $do(\cdot)$ | Operator | Pearl's intervention operator (Level 2) | TF-02 |
| $\text{CIY}(a)$ | Scalar $\geq 0$ | Canonical causal information yield of action $a$, defined from interventional outcome distributions. | TF-08 |
| $\text{CIY}_{\text{proxy}}(a)$ | Scalar (sign-indefinite) | Observational proxy for CIY based on MI difference; useful diagnostically but requires assumptions for causal interpretation. | TF-08 |

## The Model (TF-03, Formulation)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $M_t$ | $\in \mathcal{M}$ | Model state at time $t$ | TF-03 |
| $\mathcal{M}$ | Set | Model space (the class of representable models) | TF-03 |
| $\phi$ | Function | Compression: $M_t = \phi(\mathcal C_t)$ | TF-03 |
| $f$ | Function | Recursive update: $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$; serial special case $M_t = f(M_{t-1}, o_t, a_{t-1})$ | TF-02 |
| $S(M_t)$ | $\in [0, 1]$ | Model sufficiency — theoretical ideal (full future, all actions) | TF-10 |
| $S_\Pi(M_t)$ | $\in [0, 1]$ | Model sufficiency — operational form (finite horizon $N_h$, policy class $\Pi$). The measured object. | TF-10 |
| $\mathcal{F}(\mathcal{M})$ | $\in [0, 1]$ | Model class fitness: $\sup_{M \in \mathcal{M}} S(M)$. Implicitly depends on environment dynamics $(T, h)$; see TF-10 note | TF-10 |
| $\beta$ | Scalar $\gt 0$ | Information bottleneck trade-off parameter | TF-03 |

## Event-Driven Dynamics (TF-04)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $e$ | Event | An atomic observation or action-completion event | TF-04 |
| $\tau$ | $\in \mathbb R_{\geq 0}$ | Continuous timestamp of an event | TF-04 |
| $\mathcal{E}$ | Sequence | Event stream: $\{(e_i, \tau_i)\}$ | TF-04 |
| $\nu^{(k)}$ | Rate (Hz) | Event rate on channel $k$ | TF-04 |
| $M_{\tau^-}$, $M_{\tau^+}$ | $\in \mathcal{M}$ | Model state just before / after event at $\tau$ | TF-04 |
| $\mathcal{I}(e_\tau)$ | Scalar $\geq 0$ | Event information content: $I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$ | TF-04 |
| $U_o^{(k)}$ | Scalar $\gt 0$ | Observation uncertainty on channel $k$ | TF-04 |
| $\nu_{\text{eff}}$ | Rate ($t^{-1}$) | Effective adaptation rate: $\sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. Identical to $\mathcal{T}$ (TF-11). | TF-04 |

## Mismatch Signal (TF-05)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\hat o_t$ | $\in \mathcal{O}$ | Predicted observation: $\mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$ | TF-05 |
| $\delta_t$ | $\in \mathcal{O}$ | Mismatch signal (prediction error): $o_t - \hat o_t$. Primary definition; used in mismatch dynamics (TF-11, App. A) | TF-05 |
| $\tilde{\delta}_t$ | $\in T_M\mathcal{M}$ | Score-function mismatch: $-\nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$. Information-theoretic generalization for non-vector $\mathcal{O}$ or probabilistic models | TF-05 |

## Update Gain (TF-06)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\eta$ | Scalar, vector, or matrix | Update gain (general) | TF-06 |
| $\eta^\ast$ | Same | Optimal update gain | TF-06 |
| $\eta^{(k)\ast}$ | Same | Optimal gain on channel $k$ | TF-06 |
| $U_M$ | Scalar $\gt 0$ | Model uncertainty: $\text{Var}_{M_{t-1}}[\hat o_t \mid a_{t-1}]$ or appropriate dispersion measure (see TF-06 for general definition) | TF-06 |
| $U_o$ | Scalar $\gt 0$ | Observation uncertainty: $\text{Var}[\varepsilon_t]$ or channel-specific $U_o^{(k)}$ (see TF-06 for general definition) | TF-06 |
| $g$ | Function | Mismatch transform: maps mismatch to update direction. $g: \mathcal{O} \to T_M\mathcal{M}$ for prediction errors $\delta_t$; $g: T_M\mathcal{M} \to T_M\mathcal{M}$ for score-function mismatches $\tilde{\delta}_t$ | TF-06 |

## Action Selection (TF-07)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\pi$ | Function or distribution | Policy: $a_t = \pi(M_t)$ or $a_t \sim \pi(\cdot \mid M_t)$ | TF-07 |
| Action fluency | Characterized via deliberation gain | Degree to which effective action flows from $M_t$ without deliberation. High fluency $\Leftrightarrow$ $\Delta\eta^\ast(\Delta\tau) \approx 0$ for all $\Delta\tau$ (TF-09). Distinct from model sufficiency $S(M_t)$. | TF-07 |
| $\lambda(M_t)$ | Scalar $\geq 0$ | Exploration-exploitation balance weight | TF-08 |

## Deliberation Cost (TF-09)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\Delta\tau$ | Duration $\geq 0$ | Deliberation duration | TF-09 |
| $\Delta\eta^\ast(\Delta\tau)$ | Scalar $\geq 0$ | Gain improvement from deliberation of duration $\Delta\tau$ | TF-09 |
| $\rho_{\text{delib}}$ | Rate (surprise/time) | Local mismatch drift rate during deliberation pauses (Assumption 9.0) | TF-09 |

## Structural Adaptation (TF-10)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\Phi$ | Function | Structural update: $\mathcal M_{t+1} = \Phi(\mathcal M_t, \text{performance history})$ | TF-10 |

## Adaptive Tempo and Dynamics (TF-11)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $\mathcal{T}$ | Rate ($t^{-1}$) | Adaptive tempo: $\sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ | TF-11 |
| $\rho(t)$ | Rate (surprise/time) | Environment change rate (rate of new mismatch introduction) | TF-11 |
| $\Vert\delta\Vert_{ss}$ | Scalar $\geq 0$ | Steady-state mismatch: $\rho / \mathcal{T}$ | TF-11 |

## Lyapunov Analysis (Appendix A)

| Symbol | Type | Meaning | Defined in |
|--------|------|---------|------------|
| $F(\mathcal{T}, \delta)$ | Function | Correction function (general nonlinear) | App. A |
| $w(t)$ | Vector | Disturbance (new mismatch), $\Vertw(t)\Vert \leq \rho$ | App. A |
| $\alpha$ | Scalar $\gt 0$ | Lower sector bound of correction function | App. A |
| $R$ | Scalar $\gt 0$ | Radius of sector-condition region (model class capacity) | App. A |
| $R^\ast$ | Scalar $\gt 0$ | Ultimately bounded mismatch radius: $\rho/\alpha$ | App. A |
| $\Delta\rho^\ast$ | Scalar $\geq 0$ | Adaptive reserve: $\alpha R - \rho$ | App. A |
| $\gamma_A$ | Scalar $\gt 0$ | Coupling effectiveness of $A$'s actions on $B$'s disturbance | App. A |
| $V(\delta)$ | Scalar $\geq 0$ | Lyapunov function: $\frac{1}{2}\Vert\delta\Vert^2$ | App. A |

## Conventions

**Subscript $t$**: Discrete time index when events arrive uniformly on a single channel. Also used as continuous macroscopic time in the mismatch dynamics ODEs (TF-11, Appendix A), where the differential equations abstract over the microscopic event-driven updates at timestamps $\tau$ (TF-04). Context disambiguates: $M_t = f(M_{t-1}, o_t, a_{t-1})$ is discrete; $d\Vert\delta\Vert/dt$ is continuous.

**Subscript $\tau$**: Continuous timestamp of an individual event. Used in the event-driven formulation (TF-04) for microscopic update dynamics.

**Superscript $(k)$**: Channel index. Distinguishes observation or action channels with distinct rates and noise characteristics.

**Calligraphic letters** ($\mathcal{M}$, $\mathcal{O}$, $\mathcal{A}$, $\mathcal{E}$, $\mathcal{C}$, $\mathcal{T}$, $\mathcal{I}$): Sets, spaces, or aggregate quantities. The interaction history uses $\mathcal{C}$ (for *chronica*) rather than $\mathcal{H}$ to avoid collision with $H(\cdot)$ (Shannon entropy) in speech and handwriting. Exceptions: $\mathcal{T}$ is a scalar rate, not a set — the calligraphic distinguishes adaptive tempo from temperature or other common uses of $T$. $\mathcal{I}(e_\tau)$ is a scalar (event information content) — the calligraphic distinguishes it from the mutual information functional $I(\cdot;\cdot)$.

**$\Vert \cdot \Vert$**: Norm (Euclidean or information-theoretic) of a vector. Used for mismatch magnitude throughout.

**$\lvert \cdot \rvert$**: Cardinality of a set (e.g., $|\mathcal{A}|$). Not used for mismatch magnitude — use $\Vert\cdot\Vert$ instead.

**Scalar reduction of gain and tempo.** When $\eta^\ast$ appears as a scalar in the mismatch dynamics (TF-11, Appendix A), it represents the effective correction fraction along the current mismatch direction: $\eta^\ast_{\text{eff}} = \delta^T K \delta / \Vert\delta\Vert^2$ where $K$ is the full gain operator. The scalar adaptive tempo $\mathcal{T} = \nu \cdot \eta^\ast_{\text{eff}}$ is the correction rate along this direction. The sector condition parameter $\alpha$ in Appendix A corresponds to the worst-case scalar projection: $\alpha = \inf_{\delta \neq 0} \delta^T F(\mathcal{T}, \delta) / \Vert\delta\Vert^2$. The full anisotropic treatment would require a tempo tensor (TF-11 Open Question #4); the scalar reduction is valid when correction dynamics are approximately isotropic or when $\rho$ is roughly uniform across mismatch dimensions.

## Units (Informal)

The theory is stated in natural (dimensionless information-theoretic) units where possible:

- $\eta^\ast$: Dimensionless ratio in $[0, 1]$
- $\nu^{(k)}$: Events per unit time (Hz)
- $\mathcal{T}$: Inverse time ($t^{-1}$). Informally: "effective correction rate."
- $\rho$: Mismatch per unit time ([surprise] $\cdot t^{-1}$). Rate at which new mismatch is introduced.
- $S(M_t)$: Dimensionless ratio in $[0, 1]$

**Dimensional analysis of the mismatch ODE.** In $d\Vert\delta\Vert/dt = -\mathcal{T}\Vert\delta\Vert + \rho$: the LHS has units [surprise $\cdot t^{-1}$]; the term $\mathcal{T}\Vert\delta\Vert$ has units $[t^{-1}] \cdot [\text{surprise}] = [\text{surprise} \cdot t^{-1}]$; and $\rho$ has units $[\text{surprise} \cdot t^{-1}]$. All terms are consistent. Note that $\mathcal{T}$ and $\rho$ have *different* units — they are not directly comparable. The **persistence condition** is $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$, which is dimensionally consistent ($[t^{-1}] \gt [\text{surprise} \cdot t^{-1}] / [\text{surprise}]$). When $\Vert\delta_{\text{critical}}\Vert$ is normalized to 1, this reduces to the shorthand "$\mathcal{T} \gt \rho$" — but this notation is only valid under that normalization. All formal statements in TFT use the full form; the shorthand appears only after explicit definition (TF-11).

## Global Assumptions

Load-bearing assumptions that appear locally in individual documents but are referenced by multiple downstream results. Each is identified here for cross-referencing.

| ID | Assumption | Where introduced | Used by |
|----|-----------|-----------------|---------|
| GA-1 | **Fresh noise.** $\varepsilon_t$ is conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$. | TF-01 (implicit), TF-05 (proof of Prop 5.1) | Prop 5.1, mismatch decomposition |
| GA-2 | **Bounded disturbance.** $\Vertw(t)\Vert \leq \rho$ for finite $\rho$. | TF-11, App. A (Prop A.1) | Props A.1–A.3, persistence threshold |
| GA-3 | **Sector condition.** $\delta^T F(\mathcal{T}, \delta) \geq \alpha\Vert\delta\Vert^2$ for $\Vert\delta\Vert \leq R$. | App. A (A2') | Props A.1–A.3 |
| GA-4 | **Local deliberation drift.** Mismatch accumulates at rate $\rho_{\text{delib}}$ during inaction. | TF-09 (Assumption 9.0) | Prop 9.1 |
| GA-5 | **Fluid limit.** Event rate $\nu$ is high relative to dynamics timescale ($\eta^\ast \ll 1$). | TF-11 (bridging note) | Mismatch ODE, steady-state formula |

These are the theory's main load-bearing assumptions beyond the scope definition (TF-01) and formulation choices (TF-03, TF-04). GA-1 through GA-3 are the most foundational; GA-4 and GA-5 are local to specific results.

## Dependency Structure

The theory's documents form a directed dependency graph. Each document depends on the axioms and definitions established before it; cross-links indicate where later documents reference earlier material beyond the primary chain.

### Primary Chain

```
TF-01 (Scope) → TF-02 (Causal Structure) → TF-03 (Model) → TF-04 (Dynamics)
    → TF-05 (Mismatch) → TF-06 (Update Gain) → TF-07 (Action Selection)
    → TF-08 (Exploration-Exploitation) → TF-09 (Deliberation Cost)
    → TF-10 (Structural Adaptation) → TF-11 (Tempo)
    → Appendix A (Lyapunov Stability)
    → Appendix B (Estimation Procedures)
    → Appendices C, D (Worked Examples)
```

**Note on TF-08.** TF-08 is hypothesis + discussion — it contains no formal propositions but houses the CIY (causal information yield) machinery and provides the conceptual bridge between action selection (TF-07) and adversarial dynamics (TF-11, Appendix A). Downstream documents that reference CIY in policy objectives or adversarial coupling depend on it conceptually, though the formal results (Propositions 9.1, 11.1, A.1–A.3) do not require it.

### Key Cross-Links

- TF-05 → TF-01 + TF-03 (Prop 5.1 derives mismatch from scope + model formulation)
- TF-07 → TF-02 (epistemic levels from causal axiom ground deliberation)
- TF-08 → TF-02 (CIY definitions build on causal axiom's epistemic levels)
- TF-09 → TF-06 + Assumption 9.0 (local deliberation drift; TF-11 later provides global consistency)
- TF-10 → TF-03 (structural adaptation changes model class from model formulation)
- TF-10 → TF-09 (structural change cost as massive deliberation cost)
- TF-11 → TF-06 (adaptive tempo = rate × gain)
- Appendix A → TF-11 (generalizes linear dynamics to nonlinear Lyapunov)
- Appendix B → TF-06 + TF-09 + TF-11 + App. A (estimation procedures)
- Appendix C → TF-01 through App. A (Kalman worked example — exact mapping)
- Appendix D → TF-01 through TF-11 (RL worked example — approximate mapping)
- Appendix F → TF-06 + TF-08 + TF-11 + App. A (multi-agent coupling, strategic interaction)

## Formal Results Index

The theory contains formal propositions (stated with explicit assumptions and proof sketches) alongside discussion-grade claims (argued qualitatively or by analogy). This index distinguishes them.

### Propositions *(stated and proved/sketched under explicit assumptions)*

| Result | Location | Depends on | Status | Robustness |
|--------|----------|------------|--------|------------|
| Prop 5.1: Mismatch Inevitability | TF-05 | TF-01, TF-03 | Proved (sketch) | **Robust** — requires only scope + model |
| Prop 9.1: Deliberation Threshold | TF-09 | TF-07, TF-06, Asm 9.0 | Proved (sketch) | **Conditional** — on local drift assumption |
| Prop 10.1: Structural Adaptation Necessity | TF-10 | TF-03, TF-05, TF-10 ($S$, $\mathcal{F}$ defs) | Proved (sketch) | **Robust** — pure information-theoretic |
| Prop 11.1: Persistence Threshold | TF-11 | TF-06, TF-04 | Proved (linear); generalized by A.1 | **Linear-dependent** — qualitative result robust (A.1) |
| Cor. 11.2: Squared Tempo Advantage | TF-11 | Linear ODE + linear coupling | Derived | **Linear-dependent** — first-order heuristic |
| Prop A.1: Bounded Mismatch | App. A | Sector condition | Proved | **Robust** — general nonlinear |
| Prop A.2: Adaptive Reserve | App. A | A.1 | Proved (corollary) | **Robust** — general nonlinear |
| Prop A.3: Adversarial Destabilization | App. A | A.1, coupling model | Proved | **Robust** (with decoupling caveat) |
| Cor. A.3.1: Effects Spiral | App. A | A.3 | Proved (corollary) | **Robust** — positive feedback mechanism |

**Robustness key**: **Robust** = holds under general nonlinear dynamics or pure information-theoretic assumptions. **Linear-dependent** = derived from the linear mismatch dynamics hypothesis; qualitative conclusion may survive but quantitative form is approximate. **Conditional** = depends on explicitly named local assumptions.

### Discussion-Grade Claims *(argued but not formally derived)*

| Claim | Location | Nature |
|-------|----------|--------|
| Uncertainty ratio principle ($\eta^\ast = U_M/(U_M + U_o)$) | TF-06 | Empirical; exact in Kalman/conjugate Bayes, structural elsewhere |
| Unified policy objective ($\pi^\ast = \arg\max[\text{value} + \lambda \cdot \text{CIY}]$) | TF-08 | Structural analogy with active inference; $\lambda$ not derived |
| Speed-quality substitutability | TF-11 | Follows from $\mathcal{T} = \nu \cdot \eta^\ast$; qualitative implication |
| Action fluency concept | TF-07 | Characterized via deliberation gain ($\Delta\eta^\ast \approx 0 \Rightarrow$ high fluency) |
| Non-forkability of causal trajectories | App. G | Conceptual argument from sufficiency + temporal ordering |

### Claim Registry *(epistemic tier of every major claim)*

This table classifies every substantive claim in TFT by its epistemic strength, from strongest to weakest. Use it to calibrate trust: **exact** claims are mathematically validated; **robust qualitative** claims survive across assumptions; **heuristic** claims are useful approximations whose quantitative form may not hold.

| Claim | Tier | Notes |
|-------|------|-------|
| Mismatch inevitability (Prop 5.1) | **Exact** | Follows from scope + model; the decomposition is a mathematical identity under GA-1 |
| Structural adaptation necessity (Prop 10.1) | **Exact** | Information-theoretic; holds whenever $\mathcal{F}(\mathcal{M}) \lt 1$ |
| Bounded mismatch under sector condition (Prop A.1) | **Exact** | Standard Lyapunov; proved under GA-2, GA-3 |
| Adaptive reserve (Prop A.2) | **Exact** | Corollary of A.1 |
| Adversarial destabilization threshold (Prop A.3) | **Exact** | Under decoupled analysis; full coupled dynamics are richer |
| Persistence threshold — qualitative | **Robust qualitative** | Any monotone correction function has a capacity limit (App A) |
| Temporal nesting convergence constraint | **Robust qualitative** | Standard singular perturbation reasoning |
| Recursive model update from causal structure | **Robust qualitative** | Follows from temporal axiom (TF-02, physical) + partial observability (TF-01, scope) + state completeness (TF-03, definitional). General form: $\dot{M} = g(M, u)$; event-driven special case: $f(M_{\tau^-}, e_\tau)$ |
| Gain form $\eta^\ast = U_M/(U_M + U_o)$ — structural ratio | **Robust qualitative** | Optimal gain is *higher* when model is uncertain relative to observation; universal across domains |
| Gain form $\eta^\ast = U_M/(U_M + U_o)$ — scalar expression | **Exact** in Kalman/conjugate Bayes; **heuristic** elsewhere | Scalar expression is exact when $U_M$, $U_o$ are well-defined scalars; structural ratio holds more broadly |
| Steady-state mismatch $\Vert\delta\Vert_{ss} = \rho/\mathcal{T}$ | **Heuristic** | Depends on linear ODE hypothesis; useful first-order approximation |
| Squared tempo advantage (Cor. 11.2) | **Heuristic** | Depends on linear ODE + linear coupling; striking but first-order |
| Speed-quality substitutability | **Heuristic** | Follows from multiplicative $\mathcal{T} = \nu \cdot \eta^\ast$; may not hold under nonlinear dynamics |
| Unified policy objective (value + $\lambda$ CIY) | **Heuristic** | Structural form is convergent with active inference / IDS; $\lambda$ is not derived |
| Action fluency via $\Delta\eta^\ast \approx 0$ | **Robust qualitative** | Characterization is clean but "fluency" is not a formal proposition |
| Communication gain (Appendix F) | **Heuristic** | Extends uncertainty ratio to social channels; untested |
| Team persistence via cooperative $\rho$ | **Heuristic** | Follows from the multi-agent model extension; untested |
