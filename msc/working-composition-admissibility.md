# Working Notes: Composition Closure Admissibility

**Status**: Active brainstorming and early formalization. This is the exploration space for what $\mathcal{M}_{adm}$ should contain — the most important open problem in Section III's formal foundations.

**Date**: 2026-04-01

**The problem**: composition-closure defines $\varepsilon^*$ as an infimum over admissible classes $\mathcal{P}_{adm}$ (projections) and $\mathcal{M}_{adm}$ (macro-dynamics). Without constraints on $\mathcal{M}_{adm}$, the infimum is trivially zero (curve-fit anything). The admissibility constraints must prevent trivial closure while not being so strict that no composite qualifies. They are currently "placeholders" (composition-closure Working Notes). This document explores what they should be.

---

## 1. The Question, Decomposed

$\mathcal{M}_{adm}$ constrains what kind of object $(\pi_c, E_c, f_c)$ the macro-dynamics can be. Three sub-questions:

**(Q1) What structural form must the macro-dynamics have?** Must $(\pi_c, E_c, f_c)$ decompose into the same components as a single AAD agent? Or can it be any dynamical system that happens to predict the micro-behavior?

**(Q2) What properties must the macro-quantities satisfy?** Must the macro-state decompose as $(M_c, G_c)$? Must the macro-update be recursive? Must directed separation hold? Each AAD result depends on specific properties — which are required?

**(Q3) What regularity conditions are needed for the bridge from bounded $\varepsilon^*$ to bounded trajectory error?** (The bridge lemma issue.) Even if $\varepsilon^*$ is small, compounding errors can make trajectory predictions diverge. What prevents this?

---

## 2. Wide Brainstorm

### 2.1 Analogies from Other Fields

**Statistical mechanics → thermodynamics.** A thermodynamic description is admissible when the system has well-defined intensive variables (temperature, pressure) and equations of state relating them. Not every microscopic system has a useful thermodynamic description — those near equilibrium do; far-from-equilibrium systems require kinetic theory. The analog: not every group of agents has a useful macro-agent description. Those with fast internal coordination (near "coordination equilibrium") do. The admissibility is: the macro-state has well-defined AAD state variables and update dynamics.

What makes this interesting: thermodynamics doesn't require knowing the microscopic dynamics. It requires the MACROSCOPIC variables to satisfy certain relationships (laws of thermodynamics). Similarly, $\mathcal{M}_{adm}$ might not need to reference the micro-dynamics at all — it might only constrain the macro-dynamics' own structure.

**Renormalization group (RG).** The RG asks: what theories are fixed points of coarse-graining? The effective Hamiltonian after coarse-graining must live in the same function space as the original. AAD's analog: the macro-dynamics must live in the same "function space" as individual AAD agents — same structural components, same update logic, same relationship between tempo and persistence. The admissibility is: coarse-graining maps AAD agents to AAD agents.

What makes this sharp: the RG framework says the admissible class is determined by what SURVIVES coarse-graining. Properties that are destroyed by projection are not part of the admissible class. This suggests: $\mathcal{M}_{adm}$ should require exactly those AAD properties that survive projection from micro to macro, and not require properties that are destroyed.

**Control theory → model reduction.** Balanced truncation preserves the Hankel singular values — the modes that are simultaneously most controllable and most observable. The admissibility is: the reduced model preserves these modes. AAD analog: $\Lambda$ should preserve the most observable and most actionable aspects of the micro-state. Admissibility requires the macro-model to have good observability (macro-observations are informative about macro-state) and good controllability (macro-actions affect macro-state).

**Software architecture → interface contracts.** A module is valid when its public API (interface) is a sufficient specification for clients. The internal implementation can be anything. Analog: the macro-agent's "API" — how it responds to observations and produces actions — must satisfy AAD's structural contracts. The internal micro-dynamics are implementation details.

This maps to a behavioral admissibility: don't constrain the macro-agent's internals, constrain its input-output behavior. A macro-agent is admissible if its behavior (observation → action mapping over time) is indistinguishable from SOME AAD agent with well-defined tempo, mismatch, gain, etc.

**Coase's theory of the firm.** A firm's boundary is where internal coordination becomes cheaper than market transactions. The admissibility analog: a composite boundary is where internal coordination costs are low enough that the macro-description is simpler than tracking all micro-agents individually. Admissibility is: the macro-description is actually a simplification (lower description length than the micro-description), not a complication.

This is a minimum description length (MDL) perspective: the macro-dynamics should be a compressed description of the micro-dynamics that retains predictive power. If $(\pi_c, E_c, f_c)$ is as complex as the full micro-system, it's not a useful abstraction.

**Biology → levels of organization.** An organism is a valid "agent" because cells coordinate fast enough relative to environmental challenges. But the admissibility isn't just speed — it's also about the organism having genuine emergent properties (perception, motor control, homeostasis) that can't be reduced to any single cell. The admissibility might include: the macro-agent has capabilities (tempo, persistence, strategic depth) that genuinely emerge from composition, not just re-label micro-quantities.

### 2.2 Structural Approaches

**Approach A: Require the scope condition + recursive update.**

Minimal: the macro-agent satisfies the scope condition (observations, binary choice, residual uncertainty) and has recursive update structure ($X_{c,t+1} = f_c(X_{c,t}, o_{c,t+1})$).

This prevents: open-loop models (no recursive update), memoryless models (no state), and non-agent systems (no observation or action).

This doesn't prevent: macro-dynamics that are technically recursive but have no meaningful decomposition into epistemic and purposeful substates. A lookup table mapping macro-observations to macro-actions is recursive but not an AAD agent in any meaningful sense.

**Approach B: Require $(M_c, G_c)$ decomposition + mismatch signal.**

The macro-state decomposes as $X_c = (M_c, G_c)$, and a well-defined mismatch signal $\delta_c = o_{c,t} - \hat{o}_{c,t}(M_c, a_{c,t})$ exists. This ensures the macro-agent has a reality model that makes predictions and a way to detect when predictions fail.

This prevents: macro-dynamics without a meaningful model (pure reactive systems), and ensures the persistence condition machinery applies at the macro level.

Doesn't address: whether $M_c$ and $G_c$ interact correctly (directed separation, orient cascade).

**Approach C: Tiered admissibility.**

$\mathcal{M}_{adm}$ is parameterized by a level $\ell$:

| Level | Requirements | Enables |
|-------|------------|---------|
| 0 | Scope condition | Identifying composites as agents |
| 1 | + Recursive update, $(M_c, G_c)$ decomposition, mismatch signal | Persistence condition, mismatch dynamics |
| 2 | + Directed separation ($f_{M_c}$ goal-blind) | Orient cascade, sequential update |
| 3 | + Strategy DAG structure in $G_c$ | Edge updates, strategic calibration |

Different Section III results require different admissibility levels. The tempo inequality needs Level 1. Directed separation under composition needs Level 2. Strategy-edge vulnerability needs Level 3.

**Advantage**: honest about what each result requires, doesn't over-constrain.
**Disadvantage**: complicates the formalism. Every result needs to state its admissibility level.

**Approach D: Information-preservation admissibility.**

The projection $\Lambda$ and macro-dynamics $(\pi_c, E_c, f_c)$ must jointly preserve enough predictive information:

$$I(\Lambda_x(X_{micro,t}); \Lambda_o(o_{micro, t+1}) \mid \Lambda_a(a_{micro,t})) \geq (1 - \epsilon) \cdot I(X_{micro,t}; o_{micro,t+1} \mid a_{micro,t})$$

The macro-state must retain at least $(1-\epsilon)$ of the predictive mutual information that the micro-state has about next observations. This is the information bottleneck applied to the projection.

**Advantage**: principled, connects to IB framework, domain-agnostic.
**Disadvantage**: doesn't guarantee AAD-structure at the macro level. A neural network could satisfy this without having decomposed state, mismatch signals, etc.

**Approach E: Behavioral equivalence.**

The macro-agent's externally observable behavior (actions given observation history) must be $\epsilon$-close to the behavior produced by some well-formed AAD agent with known tempo, mismatch, and gain:

$$\sup_{\text{obs histories}} \lVert \pi_c(\Lambda_x(X_{micro})) - \pi_{AAD}(M_{AAD}, G_{AAD}) \rVert \leq \epsilon$$

for some AAD agent $(M_{AAD}, G_{AAD}, \pi_{AAD})$ with well-defined quantities.

**Advantage**: doesn't constrain internals, only requires that the external behavior is consistent with AAD.
**Disadvantage**: existential quantifier — hard to verify. How do you show such an AAD agent exists?

### 2.3 The Bridge Lemma Perspective

The composition-closure Working Notes flag: "small expected component-wise errors guarantee bounded trajectory divergence only if the admissible macro-dynamics satisfy appropriate Lipschitz stability conditions."

This suggests a different angle on admissibility: $\mathcal{M}_{adm}$ should be the class of macro-dynamics for which bounded closure defect implies bounded trajectory error. The admissibility isn't about AAD structure at all — it's about stability.

The key condition: the macro-dynamics must be Lipschitz continuous in the macro-state:

$$\lVert f_c(X_c, o_c) - f_c(X_c', o_c) \rVert \leq L \cdot \lVert X_c - X_c' \rVert$$

With Lipschitz constant $L$, a per-step error of $\varepsilon$ produces at most $\varepsilon \cdot (L^H - 1)/(L - 1)$ trajectory divergence over horizon $H$.

Connection to AAD: the sector condition from the persistence framework (δᵀF ≥ α‖δ‖² for ‖δ‖ ≤ R) IS a Lipschitz-like condition on the correction function. If the macro-dynamics satisfy the sector condition, they satisfy the Lipschitz requirement. So: **macro-dynamics in the persistence regime automatically satisfy the bridge lemma requirement.**

This is promising. It means: if we require $\mathcal{M}_{adm}$ to satisfy the sector condition, we get both AAD-structure (persistence condition applies) and trajectory-error boundedness (bridge lemma holds) in one requirement.

---

## 3. Promising Directions

### 3.1 Direction: Structural + Stability

Combine the minimal structural requirements with the stability requirement:

**$\mathcal{M}_{adm}$ requires:**

1. **Structural form**: $(\pi_c, f_c, E_c)$ decomposes as an AAD agent — state $X_c = (M_c, G_c)$, recursive update $X_{c,t+1} = f_c(X_{c,t}, o_{c,t+1})$, state-dependent policy $a_{c,t} = \pi_c(X_{c,t})$.

2. **Mismatch well-defined**: A mismatch signal $\delta_{c,t}$ exists that compares macro-predictions to macro-observations.

3. **Correction satisfies sector condition**: The macro-update function, viewed as a correction mechanism for $\delta_{c,t}$, satisfies:

$$\delta_c^T f_c(\delta_c) \geq \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert \delta_c \rVert \leq R_c$$

with finite $\alpha_c > 0$ and $R_c > 0$.

**What this buys:**
- (1) ensures AAD structure at the macro level
- (2) ensures the persistence machinery applies
- (3) ensures bounded trajectory error (bridge lemma) AND gives the macro-agent a well-defined adaptive reserve

**What this costs:**
- Verifying the sector condition for specific composites requires knowing the macro-correction function, which is defined through $\Lambda$ and the micro-dynamics. This is circular unless there's a way to verify the sector condition from micro-level properties.

**The circularity-breaking insight**: if each sub-agent satisfies its own sector condition (which it does, by the persistence framework), and the coordination structure doesn't destroy stability (bounded coordination overhead), then the composite should satisfy a composite sector condition. The $\alpha_c$ and $R_c$ of the composite are determined by the sub-agents' individual parameters plus coordination quality.

This connects directly to #team-persistence, which already derives the composite persistence condition from individual conditions plus coordination. If team-persistence is correct, the sector condition at the composite level follows.

### 3.2 Direction: RG-Fixed-Point Approach

Define $\mathcal{M}_{adm}$ as the class of dynamics that are "AAD-shaped" in the following sense:

An AAD agent is characterized by a tuple $(\mathcal{T}, \rho, \delta_{\text{crit}}, R, \alpha)$ — tempo, disturbance, critical mismatch, reserve, correction rate. These are the "slow variables" that survive coarse-graining (like temperature and pressure survive the micro-to-thermodynamic projection).

$\mathcal{M}_{adm}$ = the class of macro-dynamics for which these five quantities are well-defined and satisfy the persistence condition:

$$\alpha_c > \rho_c / R_c$$

**The RG connection**: the projection $\Lambda$ maps micro-quantities to macro-quantities. The admissibility is: the macro-quantities satisfy the same dynamical law (persistence condition) as the micro-quantities. This is a fixed-point condition — AAD is invariant under coarse-graining within the admissible class.

**What this buys**: a clean mathematical statement of what composition-consistency actually requires. The theory is scale-invariant in the strong sense: the same persistence condition holds at every level, with level-specific parameters.

**What this costs**: verifying that the macro-quantities are well-defined requires computing them, which requires knowing $\Lambda$ — bringing back the optimization problem. But the statement of what's required is clear even if the verification is hard.

### 3.3 Direction: Minimal + Pragmatic

Don't try to specify $\mathcal{M}_{adm}$ completely. Instead:

1. State the minimal structural requirements (Approach A: scope condition + recursive update + $(M_c, G_c)$ decomposition).
2. Add requirements AS NEEDED by specific results — each Section III segment declares what additional admissibility it assumes.
3. Leave the question of WHETHER a specific composite satisfies admissibility as a domain-specific empirical question.

This is the most honest approach. It acknowledges that we don't yet know the full list of required properties, and it doesn't pretend otherwise. The theory develops the CONSEQUENCES of admissibility (what follows if the macro-agent has these properties) while leaving the VERIFICATION of admissibility as future work.

**What this buys**: progress without false precision. Section III results can be stated and proved conditional on their specific admissibility requirements.

**What this costs**: the composition-closure criterion remains formally incomplete — $\varepsilon^*$ is well-defined given admissibility constraints, but the constraints themselves are a menu rather than a specification.

---

## 4. Working a Direction: Structural + Stability

This seems most promising. Let me try to make it precise.

### 4.1 Formal statement

$\mathcal{M}_{adm}$ is the class of macro-dynamics $(\pi_c, E_c, f_c)$ satisfying:

**(A1) AAD agent structure.** The macro-state decomposes as $X_c = (M_c, G_c) \in \mathcal{X}_c$. The macro-update is recursive: $X_{c,t+1} = f_c(X_{c,t}, o_{c,t+1})$. The macro-policy is state-dependent: $a_{c,t} = \pi_c(X_{c,t})$.

**(A2) Macro-mismatch.** A mismatch signal is well-defined:

$$\delta_{c,t} = o_{c,t} - \hat{o}_{c,t}(M_c, a_{c,t-1})$$

where $\hat{o}_{c,t}$ is the macro-model's prediction of the next macro-observation given the current macro-model and previous macro-action.

**(A3) Macro-tempo.** The macro-update has well-defined adaptive tempo:

$$\mathcal{T}_c = \sum_k \nu_c^{(k)} \cdot \eta_c^{(k)*}$$

where $k$ indexes the macro-agent's observation channels (which are the projected micro-channels), $\nu_c^{(k)}$ is the event rate, and $\eta_c^{(k)*}$ is the optimal gain.

**(A4) Bounded macro-correction.** The macro-correction function (how $M_c$ responds to $\delta_c$) satisfies the sector condition:

$$\delta_c^T f_c^{(M)}(\delta_c) \geq \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert \delta_c \rVert \leq R_c$$

with $\alpha_c > 0$ (positive correction rate) and $R_c > 0$ (finite reserve).

### 4.2 What each requirement prevents

**(A1)** prevents: open-loop models, memoryless models, models without the epistemic/purposeful decomposition. Ensures the persistence condition, orient cascade, and strategy machinery CAN apply (whether they DO apply depends on additional conditions like directed separation).

**(A2)** prevents: macro-dynamics without a reality-testing mechanism. Ensures the macro-agent can detect when its predictions fail — the foundation of adaptation.

**(A3)** prevents: macro-dynamics whose adaptation rate is undefined. Ensures the persistence condition IS applicable — you can ask "is the macro-agent adapting fast enough?"

**(A4)** prevents: macro-dynamics with unbounded or wrong-direction corrections (positive feedback in the correction loop). Ensures the bridge from bounded closure defect to bounded trajectory error. And, critically, it ensures the macro-agent is in the persistence regime — its corrections work.

### 4.3 What's NOT required

Directed separation is NOT required by $\mathcal{M}_{adm}$. It's an additional structural property that some composites have (Case 1 from #directed-separation-under-composition) and others don't (Case 2). Results that depend on directed separation declare it as an additional assumption.

Strategy structure (DAG) is NOT required. The macro-agent may have $G_c = (O_c, \Sigma_c)$ with a full strategy DAG, or $G_c$ may be a simpler goal representation. Strategy-dependent results assume strategy structure.

### 4.4 Deriving composite (A4) from micro-level properties

The critical step: can we verify that a composite satisfies (A4) from the sub-agents' properties without computing the macro-correction function directly?

**Conjecture**: If each sub-agent $A_i$ satisfies its own sector condition with parameters $(\alpha_i, R_i)$, and the coordination structure has bounded overhead $C_{\text{coord}}$, then the composite satisfies (A4) with:

$$\alpha_c \geq \min_i \alpha_i - C_{\text{coord}} / R_c$$

$$R_c \leq \min_i R_i$$

(The composite's correction rate is the weakest sub-agent's rate minus coordination cost; the composite's reserve is the smallest individual reserve.)

This is rough — the actual relationship depends on whether sub-agents' mismatch dimensions are orthogonal or coupled, and on the coordination structure. But it shows the shape: the composite's stability properties derive from individual properties plus coordination quality.

If this can be tightened, it would close the loop: admissibility constraints → verifiable from micro-level properties → $\varepsilon^*$ well-defined → bridge lemma holds → bounded trajectory error.

### 4.5 Connection to existing segments

- **team-persistence** already has a composite persistence condition. Does it implicitly assume (A1)-(A4)? If so, making this explicit strengthens that segment.
- **tempo-composition** gives $\mathcal{T}_c \leq \sum \mathcal{T}_i$. This is (A3) instantiated — the macro-tempo exists and is bounded by the sum of individual tempos.
- **composition-consistency**'s timescale condition ($\tau_{\text{eq}} \ll \tau_{\text{ext}}$) is a sufficient condition for (A4) — fast internal coordination implies the composite is in a stable correction regime.

---

## 5. Open Questions

1. **Is (A4) too strong?** The sector condition requires the macro-correction to be well-behaved. But some composites might be useful macro-descriptions even when the correction is imperfect (e.g., an organization that adapts slowly but predictably). Should $\mathcal{M}_{adm}$ allow "slow but stable" composites?

2. **The norm question.** (A2) and (A4) use norms on $\delta_c$ and $X_c$. These norms are load-bearing (different norms give different $\alpha_c$ and $R_c$). Should the norms be part of $\mathcal{M}_{adm}$ or left as domain-specific choices? The composition-closure segment already flags this.

3. **Does (A1) prevent useful non-decomposable macro-agents?** Some composites might be best described by a macro-state that doesn't cleanly decompose into $(M_c, G_c)$ — e.g., a composite where epistemic and purposeful states are entangled at the macro level (Case 2 composites with goal-dependent routing). Requiring decomposition might exclude them. But these are exactly the composites that need the coupled formulation, so excluding them from Section III's separated analysis is correct.

4. **Empirical validation.** Can (A1)-(A4) be checked for real composites? For a software team: (A1) is plausible (the team has a shared model and shared goals), (A2) is measurable (compare team predictions to outcomes), (A3) is estimable (count observation channels and estimate gain), (A4) is the hard one — does the team actually correct in the sector-condition sense? Empirical work would need to instantiate the norms and parameters.

5. **What about $\mathcal{P}_{adm}$?** This document focuses on $\mathcal{M}_{adm}$ (what the macro-dynamics must look like). The projection admissibility $\mathcal{P}_{adm}$ (what projections are allowed) is equally important but less developed. The information-preservation direction (Approach D, §2.2) is the most promising for $\mathcal{P}_{adm}$: the projection must retain enough predictive information.

---

## 6. Worked Results

### 6.1 The Bridge Lemma (Step 1)

**Claim**: If the macro-dynamics satisfy the sector condition (A4), then bounded closure defect implies bounded trajectory error.

**Setup.** Let $\tilde{X}_{c,t} = \Lambda_x(X_{micro,t})$ be the "true" macro-state (projected from micro-dynamics), and $X_{c,t}$ be the macro-state evolved by macro-dynamics. Define trajectory error:

$$e_t = X_{c,t} - \tilde{X}_{c,t}$$

The per-step closure defect provides: starting from $X_{c,t} = \tilde{X}_{c,t}$ (no accumulated error), one step of macro-dynamics introduces error at most $\varepsilon_x$.

**Key observation.** The trajectory error $e_t$ evolves under the SAME dynamical system that governs mismatch — the macro-correction function acts to reduce divergence, while the closure defect acts as a persistent perturbation. This is structurally identical to Prop A.1 (bounded mismatch) from #sector-condition-derivation, with:

| Mismatch problem (A.1) | Bridge problem |
|---|---|
| State: $\delta_t$ (model-reality mismatch) | State: $e_t$ (trajectory divergence) |
| Correction: $F(\mathcal{T}_c, \delta)$ | Correction: contraction of $f_c$ |
| Disturbance: $w(t)$, $\lVert w \rVert \leq \rho$ | Disturbance: closure defect, $\lVert \varepsilon_x \rVert \leq \varepsilon^\ast$ |
| Bound: $R^\ast = \rho / \alpha$ | Bound: $R_e^\ast = \varepsilon^\ast / \alpha_c$ |

**Sketch of proof.** Define Lyapunov candidate $V(e) = \frac{1}{2}\lVert e \rVert^2$. Along trajectories:

$$\dot{V} \leq -\alpha_c \lVert e \rVert^2 + \varepsilon^\ast \lVert e \rVert = -\lVert e \rVert (\alpha_c \lVert e \rVert - \varepsilon^\ast)$$

This is negative whenever $\lVert e \rVert > \varepsilon^\ast / \alpha_c$. Therefore:

$$\limsup_{t \to \infty} \lVert e_t \rVert \leq \frac{\varepsilon^\ast}{\alpha_c}$$

provided $\varepsilon^\ast / \alpha_c < R_c$ (the error stays within the sector-condition region).

**Result (Bridge Lemma).** Under (A4), bounded closure defect $\varepsilon^\ast$ implies bounded trajectory error with the same structure as the persistence condition:

$$\lVert e_t \rVert \leq \frac{\varepsilon^\ast}{\alpha_c} \quad \text{(ultimately)}$$

The condition for the bridge to hold: $\varepsilon^\ast < \alpha_c R_c$. That is: the closure defect must be within the macro-agent's adaptive reserve. If the closure defect exceeds the reserve, the macro-description diverges from the micro-reality — the composite "isn't really a single agent" in a precise dynamical sense.

**Epistemic status update:** The continuous-time sketch above has been superseded by a discrete-time derivation in `01-aad-core/src/composition-closure.md`. The discrete version uses a standard linear recurrence ($\lVert e_{t+1} \rVert \leq \lambda \lVert e_t \rVert + \varepsilon_x$) with contraction factor $\lambda = 1 - \alpha_c / \nu_c$, giving the bound $\varepsilon_x \nu_c / \alpha_c$. The remaining assumption: the sector condition on the correction function implies contraction of the full update map in its state argument. This holds when correction dominates the state update — the normal regime for adaptive agents, excluding structural adaptation events.

**What this buys.** If correct, (A4) simultaneously ensures:
1. Macro-agent persistence (the standard result from #sector-condition-stability)
2. Bounded trajectory divergence from micro-reality (the bridge lemma)
3. The trajectory bound $\varepsilon^\ast / \alpha_c$ is interpretable: it's the ratio of closure defect to correction efficiency, the same structure as $\rho / \alpha$ for mismatch

**The surprise.** The bridge lemma is not a separate mathematical structure — it IS the persistence condition, applied to a different state variable (trajectory error instead of model-reality mismatch). The sector condition does double duty. This was not obvious in advance but is clean in retrospect: any system with contracting dynamics and bounded perturbation has bounded error, regardless of what the "error" measures.

### 6.2 Composite Sector Condition (Step 2)

**Claim**: If each sub-agent satisfies its own sector condition, the composite satisfies a composite sector condition under certain coordination assumptions.

**Setup.** $N$ sub-agents, each with mismatch $\delta_i \in \mathbb{R}^{n_i}$, correction function $F_i$ satisfying:

$$\delta_i^T F_i(\mathcal{T}_i, \delta_i) \geq \alpha_i \lVert \delta_i \rVert^2 \quad \text{for } \lVert \delta_i \rVert \leq R_i$$

Define composite mismatch as the concatenated vector: $\delta_c = (\delta_1, \ldots, \delta_N) \in \mathbb{R}^{\sum n_i}$, with $\lVert \delta_c \rVert^2 = \sum_i \lVert \delta_i \rVert^2$.

**Case 1: No inter-agent coupling (orthogonal dynamics).**

Each agent's correction operates independently: $F_c(\delta_c) = (F_1(\delta_1), \ldots, F_N(\delta_N))$.

$$\delta_c^T F_c(\delta_c) = \sum_i \delta_i^T F_i(\delta_i) \geq \sum_i \alpha_i \lVert \delta_i \rVert^2 \geq (\min_i \alpha_i) \lVert \delta_c \rVert^2$$

So: $\alpha_c = \min_i \alpha_i$, $R_c = \min_i R_i$. The composite sector condition holds trivially. The weakest sub-agent determines the composite's correction rate; the smallest reserve determines the composite's reserve.

**Case 2: Cooperative coupling (from team-persistence).**

Each agent receives cooperative corrections from allies. From #team-persistence's disturbance decomposition:

$$\rho_i^{\text{eff}} = \rho_{i,\text{env}} - \sum_{j \in \mathcal{C}_i} \gamma_{j \to i}^{\text{coop}} \mathcal{T}_j$$

The cooperative terms REDUCE effective disturbance. This is equivalent to increasing effective $\alpha_i$:

$$\alpha_i^{\text{eff}} = \alpha_i + \frac{\sum_j \gamma_{j \to i}^{\text{coop}} \mathcal{T}_j}{\lVert \delta_i \rVert}$$

Wait — this doesn't work dimensionally. The cooperative term is a disturbance reduction, not a correction-rate increase. Let me reconsider.

The right way: cooperative communication enters as reduced disturbance, not increased correction. The composite sector condition relates to whether the composite's TOTAL dynamics (correction minus disturbance) are stable. From the persistence condition:

$$\text{Agent } i \text{ persists iff } \alpha_i > \rho_i^{\text{eff}} / R_i$$

The composite persists iff ALL agents persist (the weakest link). So:

$$\text{Composite persists iff } \min_i \left(\alpha_i - \rho_i^{\text{eff}} / R_i\right) > 0$$

This is equivalent to: the composite's effective persistence margin is:

$$\Delta\alpha_c = \min_i \left(\alpha_i - \frac{\rho_i^{\text{eff}}}{R_i}\right) > 0$$

**Case 3: Coordination overhead.**

Coordination costs reduce each agent's effective correction rate. If agent $i$ spends $\Delta\mathcal{T}_i^{\text{cost}}$ of its tempo on coordination (from #team-persistence), its effective correction rate decreases:

$$\alpha_i^{\text{eff}} = \alpha_i - \Delta\mathcal{T}_i^{\text{cost}}$$

(In the linear case, $\alpha = \mathcal{T}$, so reducing tempo by the coordination cost directly reduces $\alpha$.)

The composite sector condition becomes:

$$\alpha_c = \min_i (\alpha_i - \Delta\mathcal{T}_i^{\text{cost}})$$

And the composite persistence condition:

$$\alpha_c > \frac{\max_i \rho_i^{\text{eff}}}{R_c}$$

**Synthesis.** The composite sector condition holds with:

$$\alpha_c = \min_i \left(\alpha_i - \Delta\mathcal{T}_i^{\text{cost}}\right)$$
$$R_c = \min_i R_i$$

provided all sub-agents are in the persistence regime ($\alpha_i > \rho_i^{\text{eff}} / R_i + \Delta\mathcal{T}_i^{\text{cost}}$ for all $i$).

**Epistemic status: sketch.** Case 1 (orthogonal) is clean — the proof is straightforward. Case 2 (cooperative) works through the disturbance decomposition from team-persistence. Case 3 (coordination overhead) is a heuristic: treating coordination cost as a reduction in $\alpha$ is first-order correct but may miss nonlinear interactions between coordination and correction. The weakest-link structure ($\min_i$) is conservative — it's possible that strong sub-agents compensate for weak ones — but it's the right structure for worst-case bounds.

**What this buys.** Admissibility (A4) is VERIFIABLE from micro-level properties: compute each sub-agent's $(\alpha_i, R_i)$, estimate coordination costs $\Delta\mathcal{T}_i^{\text{cost}}$, and check whether the composite $\alpha_c > 0$. No need to compute the macro-correction function directly.

### 6.3 Team-Persistence Cross-Check (Step 3)

team-persistence assumes, for each sub-agent $i$:
- **(A1)** Implicitly: the distributed tempo definition assumes $X_i = (M_i, G_i)$ with recursive update. ✓
- **(A2)** Implicitly: the persistence condition uses $\rho_i^{\text{eff}}$, which requires mismatch signals for each agent. ✓
- **(A3)** Explicitly: the distributed tempo formula defines $\mathcal{T}_i$. ✓
- **(A4)** Explicitly: the persistence condition applies the sector-condition framework. ✓

team-persistence does NOT derive (A1)-(A4) for the COMPOSITE macro-agent. It derives persistence conditions from the sub-agents' perspective: each sub-agent persists given the cooperative/adversarial network. The macro-agent level — whether the composite AS A WHOLE satisfies AAD's structural requirements — is not addressed.

The gap between team-persistence and what we need:
- team-persistence: "each sub-agent persists in the team context" (micro-level persistence)
- Composition admissibility: "the macro-agent satisfies AAD's structural requirements" (macro-level structure)

These are RELATED but DIFFERENT. Micro-level persistence is NECESSARY for macro-level admissibility (if sub-agents diverge, the composite can't be a valid macro-agent). But it's not SUFFICIENT — the macro-dynamics must also have AAD structure (decomposed state, mismatch signal, tempo, sector condition on the correction function).

The composite sector condition derived in §6.2 provides the bridge: IF each sub-agent satisfies its sector condition AND coordination costs are bounded, THEN the composite has a well-defined correction rate $\alpha_c$ and reserve $R_c$ — satisfying (A4) at the macro level.

### 6.4 Toy Case: Two Linear Agents (Step 4)

**Setup.** Two agents, linear dynamics, orthogonal observation channels, no communication.

Agent 1: $\dot{\delta}_1 = -\alpha_1 \delta_1 + w_1(t)$, $\lVert w_1 \rVert \leq \rho_1$
Agent 2: $\dot{\delta}_2 = -\alpha_2 \delta_2 + w_2(t)$, $\lVert w_2 \rVert \leq \rho_2$

**Trivial projection** ($\Lambda$ = identity): $\delta_c = (\delta_1, \delta_2)$, macro-dynamics identical to micro-dynamics. $\varepsilon^\ast = 0$. All admissibility conditions trivially satisfied. Uninteresting but confirms the framework.

**Averaging projection**: $\delta_c = (\delta_1 + \delta_2)/2$. The true dynamics of $\delta_c$:

$$\dot{\delta}_c = -\frac{\alpha_1 \delta_1 + \alpha_2 \delta_2}{2} + \frac{w_1 + w_2}{2}$$

**Sub-case: $\alpha_1 = \alpha_2 = \alpha$.** Then $\dot{\delta}_c = -\alpha \delta_c + w_c$, where $\lVert w_c \rVert \leq (\rho_1 + \rho_2)/2$. The macro-dynamics are exactly AAD-shaped. $\varepsilon^\ast = 0$ (no closure defect). $\alpha_c = \alpha$, $\rho_c = (\rho_1 + \rho_2)/2$.

The composite persistence condition: $\alpha > (\rho_1 + \rho_2)/(2R)$. Compare to individual: $\alpha > \rho_i / R_i$. If agents face similar disturbance ($\rho_1 \approx \rho_2 \approx \rho$), the composite threshold is $\alpha > \rho / R$ — same as individual. No advantage from composition when channels are independent and rates are equal. This is expected: without communication, the agents don't help each other.

**Sub-case: $\alpha_1 \neq \alpha_2$.** The best linear macro-dynamics: $\dot{\delta}_c = -\alpha_c \delta_c + w_c$. The optimal $\alpha_c$ minimizes the closure defect:

$$\varepsilon_x = \left\lVert \frac{\alpha_1 \delta_1 + \alpha_2 \delta_2}{2} - \alpha_c \frac{\delta_1 + \delta_2}{2} \right\rVert = \frac{\lvert \alpha_1 - \alpha_2 \rvert}{2} \cdot \frac{\lvert \delta_1 - \delta_2 \rvert}{2}$$

This is minimized by $\alpha_c = (\alpha_1 + \alpha_2)/2$, giving residual closure defect proportional to $\lvert \alpha_1 - \alpha_2 \rvert \cdot \lvert \delta_1 - \delta_2 \rvert / 4$.

**Interpretation.** The closure defect is small when:
- Agents have similar correction rates ($\alpha_1 \approx \alpha_2$): the average captures both well
- Agents have similar mismatch ($\delta_1 \approx \delta_2$): the averaging projection doesn't lose information

The defect is large when agents are DIFFERENT — different correction rates, different mismatch states. This is intuitive: averaging is a poor summary of a heterogeneous group.

**Applying the bridge lemma.** With $\alpha_c = (\alpha_1 + \alpha_2)/2$ and $\varepsilon^\ast \propto \lvert \alpha_1 - \alpha_2 \rvert$:

$$\lVert e_t \rVert \leq \frac{\varepsilon^\ast}{\alpha_c} \propto \frac{\lvert \alpha_1 - \alpha_2 \rvert}{(\alpha_1 + \alpha_2)/2}$$

The trajectory error is proportional to the RELATIVE difference in correction rates. For agents with similar $\alpha$, the error is small. For very different agents, the averaging projection is poor — the macro-description doesn't faithfully represent either agent.

**Verification of (A1)-(A4):**
- (A1): $X_c = \delta_c$ (degenerate — no $G_c$ in this toy case, which is a Section I setting). ✓ modulo the $G$ component being vacuous.
- (A2): $\delta_c$ is the mismatch signal for the averaged state. ✓
- (A3): $\mathcal{T}_c = (\alpha_1 + \alpha_2)/2$ (in the linear case, $\alpha = \mathcal{T}$). ✓
- (A4): Sector condition holds with $\alpha_c = (\alpha_1 + \alpha_2)/2$. ✓

The toy case confirms: the framework works, the bridge lemma gives the right bounds, and the admissibility conditions are verifiable. The interesting case (heterogeneous agents, non-trivial projection) shows closure defect proportional to agent heterogeneity — a sensible result.

---

## 7. Updated Assessment

The "Structural + Stability" direction (§4) is stronger than I expected:

1. **The bridge lemma falls out of the sector condition for free.** The same Lyapunov argument that proves persistence proves trajectory-error boundedness. This is not two theorems — it's one theorem applied to two different state variables.

2. **Composite (A4) derives from individual sector conditions.** The weakest-link structure ($\alpha_c = \min_i \alpha_i^{\text{eff}}$) is conservative but clean, and the cooperative/adversarial terms from team-persistence integrate naturally.

3. **The toy case confirms the framework works** with computable quantities and interpretable results.

**What's still shaky:**
- The proof sketch for the bridge lemma needs the discrete-time/continuous-time gap closed. The continuous-time argument is clean; the discrete-time version needs the Lyapunov decrease condition adapted to one-step maps.
- The composite sector condition in the cooperative case goes through team-persistence's disturbance decomposition, which is itself a formulation choice (additive, sign-separated cooperative/adversarial terms). If the decomposition is wrong, the composite derivation inherits the error.
- The toy case doesn't exercise the $G_c$ component (it's a Section I setting, not Section II). A richer toy case with purposeful agents would be needed to test (A1) fully.

**Recommended next actions:**
1. Formalize the bridge lemma for discrete-time systems (one-step contraction → bounded error under persistent perturbation). This is standard in discrete Lyapunov theory and should be a straightforward translation.
2. Write (A1)-(A4) into composition-closure as a proposed specification for $\mathcal{M}_{adm}$.
3. Compute a richer toy case: two purposeful agents (Section II) with directed-separation, shared environment, cooperative communication. Verify (A1)-(A4) and compute $\varepsilon^\ast$.

## 8. Remaining Open Questions (updated from §5)

1. ~~Can we prove the bridge lemma under (A4)?~~ **Yes, in sketch form.** The sector condition implies contraction; closure defect is bounded perturbation; trajectory error is ultimately bounded at $\varepsilon^\ast / \alpha_c$.

2. ~~Can we derive composite (A4) from individual sector conditions?~~ **Yes, for the orthogonal case (clean) and cooperative case (via team-persistence).** The weakest-link structure is $\alpha_c = \min_i (\alpha_i - \Delta\mathcal{T}_i^{\text{cost}})$.

3. ~~Does team-persistence assume (A1)-(A4)?~~ **Yes, implicitly on sub-agents. No, it doesn't derive (A1)-(A4) on the composite macro-agent.** The gap is bridgeable through §6.2.

4. The $\mathcal{P}_{adm}$ question (projection admissibility) remains open. The information-preservation approach (§2.2, Approach D) is promising but hasn't been worked.

5. The norm choices remain unspecified and load-bearing. The toy case uses Euclidean norm; real applications will need domain-specific norms.
