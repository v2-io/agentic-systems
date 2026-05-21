---
spike: strategic-composition-class-3-attempt
file: 03-DYNAMIC-REGIME-AXIS
parent: 00-FRAMING.md
prior: 01-STRENGTHEN-ATTEMPTS, 02-REFRAME-INSIGHT
purpose: formalize the dynamic-regime axis surfaced as "missing" in §7; push the math forward and outward to see where it meets current theory; assess maturity in 04-MATURITY-CHECK.md
---

# §§A–H. The dynamic-regime axis — formalization, derivations, mappings

The §7 reframe surfaced the axis: what strategic composition genuinely shifts is *dynamic regime* (contraction → equilibrium → cyclic-distributional), not *architectural class*. The axis was not a new discovery — it lives implicitly across `#deriv-strategic-composition`'s $\alpha'/\beta'$ partition, `#form-composition-closure`'s contraction presupposition, `#disc-separability-pattern`'s Contraction ladder, `#scope-composite-agent`'s scope-route disjunction, and several others. This file does four things:

- **(§A–B)** Formal definition of the axis and its tiers.
- **(§C–D)** Genuine derivable content — what is derivable about the axis that is not just nomenclature, including the transition operators and a small new no-go that falls out.
- **(§E–F)** Mapping to existing AAT machinery (the ten or so segments where the axis already lives implicitly) and cross-axis interactions with architectural class.
- **(§G–H)** Implications, open questions, and the reduction questions left unsettled.

`04-MATURITY-CHECK.md` then assesses whether the work is mature enough to leave the spike and land somewhere in canon — segment, meta-segment, sub-section, or further-spike-needed.

## §A. Formal definition

**Setup.** Given a composite agent $(X^c, \pi^c)$ satisfying `#scope-composite-agent` (any route C-i through C-iv), with sub-agents indexed $i \in \{1, \ldots, N\}$ and joint state $X^c = (M_t^c, G_t^c)$ aggregating the sub-state tuples $(M_t^{(1)}, \ldots, M_t^{(N)})$ and $(G_t^{(1)}, \ldots, G_t^{(N)})$. Let the joint best-response vector field be

$$F(\pi^c;\, M^c, \{O^{(i)}\}) \;=\; \big(F_1, \ldots, F_N\big), \qquad F_i = \nabla_{\pi^{(i)}} O^{(i)}(\pi^c, M^c)$$

with $\pi^c = (\pi^{(1)}, \ldots, \pi^{(N)})$ the joint policy and $\dot{\pi}^{(i)} = F_i$ the per-agent best-response flow. Where $\pi^{(i)}$ is discrete or set-valued, replace flow with the inclusion $\pi_{t+1}^{(i)} \in \mathrm{BR}_i(\pi_t^{(-i)})$.

**Definition (dynamic regime of a composite).** The dynamic regime $\mathcal R(X^c)$ is the structural type of the fixed-point set of $F$ together with the strongest Lyapunov-class certificate the joint dynamics admit relative to that set. The framework names four tiers, ordered by progressive weakening of the certificate. The R3 tier is the population-scale entry; the first three cover finite-$N$ composites.

The dynamic regime is *structural* — determined by the game structure and the sub-agent objectives, not by the dynamics' realization. Two composites can have different *trajectories* (different initial conditions, different noise paths) but the same dynamic regime; the regime is what the structure of $F$ *admits*, not what any particular run does.

## §B. The four tiers

### B.0 Tier R0 — Contraction-regime

The joint dynamics admit a unique attracting fixed point $X^\ast \in \mathcal X^c$ and a Lyapunov function $V: \mathcal X^c \to \mathbb R_{\geq 0}$ with $V(X^\ast) = 0$, $V(X) \gt 0$ for $X \neq X^\ast$, such that

$$\frac{d}{dt}\, V(X_t^c - X^\ast) \;\leq\; -\alpha_{\text{joint}} \cdot d(X_t^c,\, X^\ast)^2 \qquad \forall\, X_t^c \in \mathcal B(X^\ast)$$

for some basin $\mathcal B(X^\ast)$ and contraction rate $\alpha_{\text{joint}} \gt 0$. Macro-state $G^c_\ast \in \mathcal X^c$ is a *state-variable*.

**Entry conditions.** Scope routes C-i (shared composite objective), C-ii (hierarchical derivation), or C-iii (mutual-benefit alignment) under matched-Tier sub-agents per `#deriv-critical-mass-composition`. The classical AAT machinery applies: `#result-sector-persistence-template`, `#form-composition-closure` bridge lemma, `#der-team-persistence`, `#der-tempo-composition`.

**Sub-tiers (`#disc-separability-pattern` Contraction ladder).** Tier 1: strong monotonicity, bridge lemma applies with derived $\varepsilon^\ast$. Tier 2: local convexity, basin-restricted bridge. Tier 3: neither, domain-specific verification.

### B.1 Tier R1 — Equilibrium-regime ($\alpha'$)

The joint dynamics admit a fixed-point set $\mathcal E = \{X^\ast_j\}_{j \in J}$ with $\lvert J \rvert \geq 1$ where each $X^\ast_j$ is a Nash equilibrium. Lyapunov-on-deviation holds locally near each equilibrium under either of two structural conditions:

**Potential-game (Monderer-Shapley 1996).** A scalar potential $\Phi: \mathcal X^c \to \mathbb R$ exists such that each sub-agent's unilateral improvement matches the potential's unilateral improvement. The potential is the joint Lyapunov; the sector-persistence template transfers with state variable $\xi = \pi^c - \pi^c_\ast$ and sector constant $\alpha_{\text{joint}}$ equal to the smallest eigenvalue of $\nabla^2 \Phi(\pi^c_\ast)$.

**Monotone-game (Rosen 1965).** The Jacobian of the joint pseudo-gradient field is negative-definite on the joint strategy space (diagonally strictly concave). No scalar potential need exist; a weighted-norm Lyapunov on the joint Jacobian's symmetric part substitutes. Convergence rate $\alpha_{\text{joint}}$ is the smallest eigenvalue of the symmetric part of $\nabla F(\pi^c_\ast)$.

**Macro-state.** Fixed-point object $\mathcal E$ — either a single Nash $X^\ast$ if unique, or the equilibrium set if multiple. Not a state-variable. Composite belief content at rational expectations encodes $\mathcal E$ structurally (the bidirectional map $\mathcal E \leftrightarrow M^c_\ast$ of §3 in `01-STRENGTHEN-ATTEMPTS.md`).

**Entry conditions.** Scope route C-iv with potential or monotone structure. `#deriv-strategic-composition` Cournot is the canonical worked instantiation.

### B.2 Tier R2 — Cyclic-distributional-regime ($\beta'$)

The joint dynamics admit *no* fixed point in pure-strategy space (cyclic games — rock-paper-scissors, matching pennies), or admit fixed points that are not local attractors (saddle-point Nash in zero-sum games where best-response orbits the equilibrium rather than approaching it). No-regret dynamics drive the empirical joint distribution to the coarse correlated equilibrium set (Hart-Mas-Colell 2000):

$$\frac{1}{T} \sum_{t=1}^T \mathbb{1}\{\pi^c_t \in \mathrm{CCE}\} \;\to\; 1 \qquad \text{at rate } O(1/\sqrt T)$$

**Macro-state.** Distributional object — a measure $\mu \in \Delta(\mathcal X^c)$ supported on the CCE set. Not a state-variable, not a fixed-point object on $\mathcal X^c$; only a fixed-point object on $\Delta(\mathcal X^c)$.

**Entry conditions.** Scope route C-iv without potential or monotone structure. Mixed-Nash games where best-response orbits but no-regret converges in distribution.

**Honest scope.** AAT in R2 predicts only set-convergence of empirical play to CCE; it cannot predict short-run trajectory, per-sub-agent mismatch convergence, or equilibrium selection. This is the framework's $\beta'$ scope limit honestly stated — and it is a *regime limit*, not an architectural limit.

### B.3 Tier R3 — Mean-field-equilibrium-regime

For $N \to \infty$, each agent interacts with the *distribution* of other agents' strategies rather than with named others. The macro-state becomes a distributional fixed point in measure space; the dynamics may contract to this fixed point under explicit conditions (Lasry-Lions 2007, Huang-Malhamé-Caines 2006).

**Why R3 is distinct from R2.** R2's macro-state is a distribution-on-strategies arising as the *empirical* distribution of finite-$N$ play; the fixed-point structure lives in the joint pure-strategy space and is a saddle-point or cycle. R3's macro-state is a distribution-on-population-strategies arising as the *thermodynamic limit*; the fixed-point structure is in the measure space directly and can be a genuine attractor under contracting MFG dynamics.

R3 is the only tier where macro-state type (Axis C from §7.2) genuinely diverges from dynamic regime in a way the framework's existing $\alpha'/\beta'$ does not capture. R3 is also the population-scope gap that Section III currently flags (per `#deriv-strategic-composition` Working Notes "Mean-field extension").

**Entry conditions.** Population scope ($N \to \infty$). Currently a Section III gap; AAT machinery for R3 is not yet developed.

### B.4 The four-tier ladder

| Tier | Fixed-point structure | Lyapunov certificate | Macro-state type | Convergence rate | Scope route |
|---|---|---|---|---|---|
| **R0** Contraction | Unique attracting $X^\ast \in \mathcal X^c$ | Joint Lyapunov $V$, global or basin-restricted | State-variable $X^\ast$ | Exponential at $\alpha_{\text{joint}}$ | C-i / C-ii / C-iii |
| **R1** Equilibrium ($\alpha'$) | Fixed-point set $\mathcal E \subset \mathcal X^c$, locally attracting | Potential $\Phi$ (Monderer-Shapley) or weighted-norm (Rosen) | Fixed-point object $\mathcal E$ | Exponential near $\mathcal E$ at $\alpha_{\text{joint}}^{(j)}$ | C-iv + potential/monotone |
| **R2** Cyclic-distributional ($\beta'$) | No pure-strategy fixed point, or saddle-only | None on $\mathcal X^c$; no-regret-with-doubling on $\Delta(\mathcal X^c)$ | Distributional object $\mu \in \Delta(\mathcal X^c)$ | Polynomial $O(1/\sqrt T)$ | C-iv without potential/monotone |
| **R3** Mean-field equilibrium | Distributional fixed point in measure space | MFG-specific (Lasry-Lions monotonicity) | Distribution-on-population $\rho \in \mathcal P(\mathcal A)$ | MFG-specific, often exponential | Population-scope gap |

The tiers are ordered by progressively weaker Lyapunov certificate; each weakening corresponds to a structural simplification *lost* from the regime above. This is the same shape as the seven existing ladders in `#disc-separability-pattern`: separable core (R0 contraction) / structured repair (R1 equilibrium with augmented Lyapunov) / general open (R2 cyclic; R3 mean-field as a separate frontier).

## §C. Derivable content — what the axis actually buys

The axis is not just classification. Four derivable contents fall out once it is stated formally; one is a small new no-go.

### C.1 Macro-state-type / regime correspondence (a structural identity for finite $N$)

**Claim.** For finite-$N$ composites (tiers R0/R1/R2), the macro-state type is *structurally identified* by the dynamic regime:

$$\mathcal R(X^c) = \text{R0} \Leftrightarrow G^c_\ast \in \mathcal X^c \text{ (state-variable)}$$

$$\mathcal R(X^c) = \text{R1} \Leftrightarrow G^c_\ast = \mathcal E \subset \mathcal X^c \text{ (fixed-point object)}$$

$$\mathcal R(X^c) = \text{R2} \Leftrightarrow G^c_\ast = \mu \in \Delta(\mathcal X^c) \text{ (distributional object)}$$

*Proof sketch.* Each direction is by the entry-condition definitions in §B. R0 demands unique attracting fixed point in $\mathcal X^c$, which gives a state-variable. R1 demands a fixed-point set under Lyapunov-on-deviation, which is a fixed-point object (singleton if unique, set if multi). R2 demands no pure-strategy fixed point plus no-regret CCE convergence, which gives a distributional object. The converse direction follows from the macro-state type forcing the available Lyapunov machinery — state-variable admits scalar Lyapunov (R0), fixed-point set admits potential or weighted-norm Lyapunov (R1), distributional macro-state admits only doubling-trick CCE convergence (R2). ∎

**Why this matters.** The identity says Axes B and C of §7.2 *collapse for finite $N$*. R3 breaks the identity — mean-field-equilibrium has distributional macro-state with contracting dynamics, distinct from R2's polynomial CCE convergence. The two axes are genuinely distinct (as §7.6 (O1) flagged) and the breaking case is exactly the population-scope frontier the framework currently flags as gap.

This is the cleanest formal content of the dynamic-regime axis: it is the axis that unifies fixed-point structure, Lyapunov certificate, and macro-state type into a single classification for finite-$N$ composites, with the mean-field limit as the explicit boundary case.

### C.2 Convergence rate as regime invariant

The rate $\alpha_{\text{joint}}$ (R0 / R1) or $O(1/\sqrt T)$ rate (R2) is determined by the regime *up to* a sub-tier-dependent constant. Specifically:

- R0: $\alpha_{\text{joint}}$ inherits from `#deriv-critical-mass-composition`'s closed-form for matched-Tier dyad; depends on sub-agent $\alpha^{(i)}$ and coupling $\gamma$.
- R1 potential: $\alpha_{\text{joint}}^{(j)} = \lambda_{\min}(\nabla^2 \Phi(X^\ast_j))$ — smallest eigenvalue of potential Hessian at $X^\ast_j$.
- R1 monotone: $\alpha_{\text{joint}}^{(j)} = \lambda_{\min}\!\left(\tfrac{1}{2}(\nabla F + \nabla F^\top)(X^\ast_j)\right)$ — smallest eigenvalue of symmetric part of joint Jacobian evaluated at $X^\ast_j$.
- R2: $O(1/\sqrt T)$ with constant determined by sub-agent regret bounds; no per-equilibrium decomposition.

**Why this matters.** Sub-tier diagnostics within each regime are structural (eigenvalue-of-Hessian, eigenvalue-of-symmetric-Jacobian) and computable from the game structure. The regime-level rate-class (exponential / polynomial) is a regime invariant — exponential in R0/R1, polynomial in R2 — without sub-tier dependence.

### C.3 Regime-transition map and a derived no-go

Five non-trivial transitions between adjacent tiers, each with its own structural mechanism:

| Direction | Mechanism | Reversibility |
|---|---|---|
| R1 → R0 | Sub-agent objectives align (scope-route shift C-iv → C-i/ii/iii); or hierarchical derivation collapses partially-opposing objectives to common parent | *Conditional* — requires structural commitment, not just dynamical adjustment |
| R0 → R1 | Sub-agent objectives diverge (scope-route shift C-i/ii/iii → C-iv); or mechanism design fails to maintain alignment | *Default-direction* — divergence is the entropy direction |
| R2 → R1 | Game structure augmented with potential or monotone properties (mechanism design, institutional shaping, payoff curvature modification) | *Conditional* — requires structural augmentation, costly to acquire |
| R1 → R2 | Potential/monotone structure destroyed (adversarial entry, mechanism manipulation, mis-coordinated multi-agent dynamics introducing cycles) | *Default-direction* under adversarial pressure |
| Anywhere → R3 | Population scale-up ($N \to \infty$); finite-$N$ dynamics enter the mean-field thermodynamic limit | *Limit operation*, not a transition between finite-$N$ regimes |

**A derived no-go falls out:** *the transitions are asymmetric in cost*. Self-driven *descent* (R0 → R1, R1 → R2) is the default under generic perturbation of the objective structure — alignment is fragile, potential-structure is fragile, both can be destroyed by local perturbations. Self-driven *ascent* (R1 → R0, R2 → R1) requires explicit structural commitment that costs more than the descent did to acquire. Symbiogenic absorption (`#hyp-symbiogenic-composition`) is the structural mechanism for R1 → R0 ascent; mechanism design under explicit potential-game constraints is the mechanism for R2 → R1 ascent.

This is an *energy-asymmetry* on the dynamic-regime axis — descent is downhill, ascent is uphill, and the asymmetry is structural rather than parametric. Adversaries exploit it as the modularity-state version exploits the modularity descent.

**The no-go shape, precisely.** For a strategic composite at R1 with $\mathcal E = \{X^\ast_j\}$ multi-equilibria, **no purely-dynamical move converts the composite to R0 with state-variable macro-state $X^\ast$ unique-attracting**. The conversion requires either:

- (a) Scope-route alignment: shifting to C-i/ii/iii by re-aligning $\{O^{(i)}\}$ structurally — a commitment that costs out-of-band negotiation or mechanism design.
- (b) Hierarchical derivation: imposing a parent objective $O^c$ from which the $\{O^{(i)}\}$ are derivable — a structural decomposition the sub-agents must accept.

This no-go is the *positive* dual of `#disc-identifiability-floor` Instance 3 (composite contraction certification from component-marginals is structurally impossible) — the floor instance says you can't identify $\alpha_c \gt 0$ in R0 from sub-agent marginals; this no-go says you can't move from R1 to R0 without structural augmentation. Both have the same essential shape: the composite carries irreducible information about its regime that no purely-component-level move can settle.

### C.4 The Lyapunov-machinery transfer

The persistence template `#result-sector-persistence-template` lifts cleanly across R0 → R1, with the Lyapunov function changing form at each tier:

$$\text{R0: } V_{\text{R0}}(X^c) = \lVert X^c - X^\ast \rVert^2 \qquad \dot V_{\text{R0}} \leq -\alpha_{\text{joint}} V_{\text{R0}}$$

$$\text{R1 potential: } V_{\text{R1},\Phi}(\pi^c) = \Phi(\pi^c) - \Phi(\pi^c_\ast) \qquad \dot V_{\text{R1},\Phi} = \sum_i \langle \nabla_{\pi^{(i)}}\Phi,\, \dot\pi^{(i)}\rangle \geq \alpha_{\text{joint}} \lVert \nabla \Phi \rVert^2$$

$$\text{R1 monotone: } V_{\text{R1},F}(\pi^c) = \tfrac{1}{2}(\pi^c - \pi^c_\ast)^\top P\, (\pi^c - \pi^c_\ast) \quad \dot V_{\text{R1},F} \leq -\alpha_{\text{joint}} V_{\text{R1},F}$$

with $P$ the weighted-norm matrix solving the Lyapunov equation for the linearized $\nabla F$ at $\pi^c_\ast$.

**At R2, the Lyapunov form fails.** No state-space Lyapunov exists; the dynamics orbit equilibria rather than converge to them. The doubling-trick (Hart-Mas-Colell 2000) gives a *regret bound* — cumulative regret is $O(\sqrt T)$ — which translates to empirical-distribution convergence to CCE at $O(1/\sqrt T)$ rate. This is convergence of the *distribution*, not of trajectories.

The Lyapunov-transfer arc R0 → R1 → R2 is the existing $\alpha/\beta'$ partition of `#deriv-strategic-composition` lifted into a regime-tiering vocabulary; the contribution is making the *transfer* explicit as a regime-axis property rather than scattered across segments.

## §D. The contraction-regime sub-tier — what changes when you lift contraction from R0 to R1

The R0 → R1 lift is the move the framework already calls "contraction-to-equilibrium hand-off" in `#impl-strategic-composition`. Made formal under the regime axis:

**What stays.** Lyapunov machinery, exponential convergence rate near equilibrium, state-space (rather than distributional) macro-state.

**What changes.**

- Lyapunov function shifts from $\lVert X^c - X^\ast \rVert^2$ to $\Phi(\pi^c) - \Phi(\pi^c_\ast)$ (potential) or weighted-norm $(\pi^c - \pi^c_\ast)^\top P (\pi^c - \pi^c_\ast)$ (monotone). The Lyapunov is no longer the squared distance from the shared target; it is the potential (or weighted-norm deviation from Nash).
- Macro-state shifts from state-variable $X^\ast$ (the shared target the composite attracts toward) to fixed-point object $\mathcal E$ (the equilibrium set the dynamics converge to). The macro-state type-change is the formal version of `#scope-composite-agent`'s "*the composite's macro-state is defined relative to the equilibrium structure $\mathcal E$ rather than relative to a shared target state.*"
- Per-equilibrium basins replace the global basin. Each $X^\ast_j \in \mathcal E$ has its own basin $\mathcal B(X^\ast_j)$; trajectories from different initial conditions converge to different equilibria. Equilibrium selection becomes a sub-tier diagnostic that R0 does not face.
- Sector constant $\alpha_{\text{joint}}$ lives at the joint potential's curvature (Monderer-Shapley) or joint Jacobian's symmetric part (Rosen) at each equilibrium — *not* at any individual sub-agent's $\alpha$. The composite-level sector constant decouples from the sub-agent-level sector constants. (The current `#deriv-strategic-composition` makes this point at "the composite-level sector constant lives at the *joint potential's curvature*"; the regime axis names this as the R0 → R1 transition's formal content.)

**What is *new* at R1 that has no R0 analog.**

- Equilibrium-selection ambiguity. R0 has unique attractor; R1 may have multiple equilibria with distinct basins. The selection question is a regime-tier-specific open question (`#deriv-strategic-composition` Honest Limits).
- Saddle-point Nash. R1 may have equilibria that are *not* locally attracting under best-response (the boundary case before R2). Whether the equilibrium-regime tier includes saddle-Nash games is a sub-tier question; the framework's R1 definition above requires *Lyapunov-on-deviation* locally, which excludes saddle-only Nash games. Saddle-only games are R2.
- Mechanism design as regime-shaping. An external designer can shape $\{O^{(i)}\}$ to make the strategic interaction a potential or monotone game — i.e., to bring R2 down to R1 by structural augmentation. Mechanism-design impossibility theorems (Gibbard-Satterthwaite, Arrow, Myerson-Satterthwaite) say *which augmentations are impossible* under stated constraints. This is the dynamic-regime axis instance of the identifiability-floor pattern (per `#deriv-strategic-composition` mechanism-design cross-references and §C.3 above).

## §E. Operational diagnostics — how to determine a composite's regime

Three diagnostic questions sequentially decide the regime:

**(D1) Are sub-agent objectives aligned?**

- Yes (shared / derivable / mutual-benefit): **R0** under matched-Tier; otherwise check `#deriv-critical-mass-composition` conditions.
- No (partially-opposing): proceed to (D2).

**(D2) Does the game admit a potential or monotone structure?**

- Potential ($\exists\, \Phi$ s.t. unilateral improvement matches): **R1 potential** (Monderer-Shapley).
- Monotone (joint Jacobian symmetric part is negative-definite on strategy space): **R1 monotone** (Rosen).
- Neither but pure-strategy Nash exists and is locally attractor: **R1 general** (variational-inequality scope, possibly sub-R1 — depends on whether the local attractor admits any Lyapunov certificate).
- No pure-strategy Nash, or only saddle-Nash: proceed to (D3).

**(D3) Does no-regret learning converge in distribution to CCE?**

- Yes (Hart-Mas-Colell 2000 conditions: regret-minimization, bounded payoffs): **R2** with empirical-distribution macro-state on CCE support.
- No (pathological game; e.g., unbounded payoffs, non-compact strategy space): scope-out of finite-$N$ machinery; check R3 entry.

**(D4) Population scale-up?**

- $N$ very large with population-distribution interaction: **R3** if MFG conditions hold; scope-out otherwise.

Each step is structurally checkable from the game definition $(\{A^{(i)}\}, \{O^{(i)}\})$. The regime determination does not require running the dynamics — it is a property of the structure. This is what distinguishes the regime axis from a *behavioral* classification of dynamics — the regime is *structural*, like architectural class.

## §F. Mapping to existing AAT machinery

The axis lives implicitly across ten segments (and likely more). The mapping below names each, what it does in the axis vocabulary, and whether it requires changes once the axis is surfaced.

| Existing segment / construct | Axis-vocabulary content | Change required after axis lands? |
|---|---|---|
| `#scope-composite-agent` routes C-i/ii/iii | Entry conditions for R0 | None (existing definition aligns) |
| `#scope-composite-agent` route C-iv | Entry condition for R1 + R2 | Add regime-tier annotation distinguishing potential/monotone (R1) from general (R2); cross-reference `#deriv-strategic-composition` sub-scope $\alpha'/\beta'$ |
| `#form-composition-closure` contraction presupposition | R0 machinery | Make the R0-presupposition explicit in the segment scope statement |
| `#result-sector-persistence-template` | R0 sector constant + persistence | Lift the Lyapunov-machinery transfer to R1 explicitly (currently lives in `#deriv-strategic-composition` as A2'-analog) |
| `#deriv-critical-mass-composition` matched-Tier closed form | R0 sub-tier specialization | None (matched-Tier dyad is a Tier-1 instance of R0 in the Contraction ladder) |
| `#der-team-persistence` cooperative limit | R0 limiting case | None |
| `#deriv-strategic-composition` sub-scope $\alpha'$ | R1 with potential/monotone Lyapunov transfer | The segment is the canonical R1 machinery; surface the axis-tier vocabulary alongside the sub-scope vocabulary |
| `#deriv-strategic-composition` sub-scope $\beta'$ | R2 with CCE convergence only | Same — surface axis-tier vocabulary alongside |
| `#impl-strategic-composition` "contraction-to-equilibrium hand-off" | R0 → R1 transition | Re-derive the hand-off in regime-axis vocabulary; replace "Class 3 (Coupled) composite" language with regime-axis language per `99-VERDICT.md` (C7) |
| `#disc-separability-pattern` Contraction ladder (row 4) | R0 sub-tier classification | Either re-cast as "R0 sub-tier" or add an eighth row for the full dynamic-regime axis |
| `#hyp-symbiogenic-composition` | R1 → R0 transition mechanism | Make the regime-ascent vocabulary explicit |
| `#der-adversarial-destabilization` | R0 or R1 target under exogenous adversarial parameter | Distinguish target-regime cases; the asymmetric adversary may force regime descent on the target |
| `#scope-composite-agent` Working Notes "common scalar across routes" | Implicit question — does $U_O$ collapse all routes? | Resolved in negative: R0 / R1 / R2 are structurally distinct, no scalar reduces them; the routes correspond to regime-tier entry conditions, not to a continuous spectrum |

**Observation.** The axis is *already present in the framework as a load-bearing organizing structure* — every one of the ten+ segments above is operating on the axis without naming it. Surfacing the axis as a formal construct does two things: (a) consolidates ten implicit usages into one explicit definition; (b) makes the cross-segment consistency checkable. It is reorganization more than derivation, with a small amount of derivation around the §C content (the macro-state-type identity, the regime-transition no-go, the Lyapunov-machinery transfer made explicit).

## §G. Cross-axis interactions

Three axes coexist in the framework after this surfacing:

- **Axis A — Architectural class.** Processing topology — Class 1 / 2 / 3. Determined by sub-agent class + routing + shared-substrate-with-$G^c$-allocation.
- **Axis B — Dynamic regime.** Joint-dynamics fixed-point structure + Lyapunov certificate — R0 / R1 / R2 / R3. Determined by objective alignment + game structure + population scale.
- **Axis C — Macro-state type.** Type-theoretic shape of $G^c_\ast$ — state-variable / fixed-point-object / distributional. For finite $N$, identified by Axis B per §C.1; for $N \to \infty$ (R3) the identity can break.

**Axes A and B are independent.** The full cross-product is meaningful:

| | R0 contraction | R1 equilibrium | R2 cyclic-distributional | R3 mean-field |
|---|---|---|---|---|
| **Class 1 Separated** | Kalman+LQR team with shared target | Cournot duopoly (distinct hardware) | Rock-paper-scissors players on distinct hardware | Mean-field finance / population biology with modular individual agents |
| **Class 2 Partial** | Biological cortex in coordinated task | Hybrid AI-biological with partial coupling, strategic | Hybrid with mixed pathways in cyclic game | (population-scale partial-architecture; speculative) |
| **Class 3 Coupled** | Multi-LLM shared substrate, aligned objective (wrapping construction available) | Multi-LLM shared substrate, strategic (wrapping construction available) | Multi-LLM shared substrate, cyclic interaction | Multi-LLM population at scale |

All twelve cells are operationally meaningful. The wrapping construction (`#der-class-coercion-via-wrapping`) operates on **Axis A only** — it converts Class 3 → Class 1 architecturally at structural-leakage cost. It does **not** change Axis B regime. A wrapped strategic composite is still in R1; the wrapping recovers architectural Class 1 but not regime R0. This is the cross-axis content the previous framing was missing.

**Symmetrically, alignment work operates on Axis B only.** Re-aligning objectives moves the composite from R1 to R0 on Axis B; it does not change architectural class on Axis A. Symbiogenic absorption (`#hyp-symbiogenic-composition`) is the structural mechanism for the R1 → R0 transition; per `#impl-strategic-composition` it is also the mechanism by which `#deriv-critical-mass-composition`'s machinery covers the regime-ascent direction.

**Two adversarial pressures act on different axes.** `#disc-adversarial-coupling-pressure` describes adversaries driving the target *Axis A* toward Class 3 (couples target's belief and goal processing). A separate adversarial pressure — call it *strategic divergence pressure* — drives the target *Axis B* toward R1 or R2 (introduces objective divergence by introducing a competitor; introduces cyclic structure by mechanism manipulation). The two are structurally distinct adversarial moves with distinct defenses (architectural scaffolding for Axis A; mechanism-design commitment for Axis B).

**For the queued `#disc-modularity-state-dynamics` meta-segment:** the three-operation modularity-state picture (truthification / strategic self-coupling / adversarial coupling pressure) operates on Axis A. A parallel three-operation dynamic-regime picture would be: alignment-strengthening (R1 → R0; self-driven-ascending — `#hyp-symbiogenic-composition`'s mechanism), strategic-divergence-acquisition (R0 → R1; self-driven-descending — joining a competitive market; entering a negotiation), adversarial-divergence-pressure (R0 → R1 or R1 → R2; externally-driven-descending — adversary introducing goal-divergence into a previously-aligned team). The parallel structure across the two axes is itself a finding worth surfacing — both axes have a three-operation modularity-like dynamics.

## §H. Implications

**(H1) Modular safety architectures fail under goal divergence (re-derived on stronger ground).** The previous `#impl-strategic-composition` claim attributed the failure to architectural-class change. The regime-axis re-derivation: modular safety constructions designed for contraction-regime composites (R0) carry guarantees that depend on the unique-attracting fixed point and the global Lyapunov contraction. Under goal divergence, the composite transitions to R1 (equilibrium-regime); the unique-attracting fixed point becomes a *set* of equilibria with per-basin dynamics; saddle-point Nash equilibria break Lyapunov contraction; multi-equilibria break uniqueness. Modular safety guarantees designed for R0 do not transfer to R1. Under further loss of potential/monotone structure (e.g., adversarial entry making the interaction cyclic), the composite transitions to R2; no Lyapunov certificate exists on state-space; only distributional CCE convergence. Modular safety guarantees designed for R0 *certainly* do not transfer to R2.

The argument is constructive — given a modular safety architecture with guarantee $G_{\text{safety}}$ over R0 trajectories, you can identify exactly which step of the guarantee derivation breaks under R0 → R1 transition (the unique-attractor step) and under R1 → R2 transition (the Lyapunov-on-deviation step). The empirical instantiations (constitutional AI red-teaming, mesa-optimizer formation) map onto these specific breakpoints.

**(H2) The wrapping construction is regime-independent.** `#der-class-coercion-via-wrapping` operates on Axis A; it does not move the composite up or down the Axis B regime ladder. Wrapped multi-LLM strategic composites are R1 architecturally-Class-1; they have all of R1's failure modes (multi-equilibria, saddle-Nash, equilibrium selection ambiguity) regardless of the wrapping. This is operationally important for `03-llm-core/` work: wrapping recovers Section II machinery applicability, but does *not* recover Section III contraction-regime composition machinery if the underlying interaction is strategic.

**(H3) Mechanism design as regime-shaping.** The mechanism-design impossibility theorems (Gibbard-Satterthwaite, Arrow, Myerson-Satterthwaite) are the structural floors on what *external designers* can achieve in the regime-ascent direction (R2 → R1 or R1 → R0 via designer intervention). They are candidate adjacent-floor instances for `#disc-identifiability-floor` per `#deriv-strategic-composition` Discussion; the regime-axis re-reading makes the candidacy structural — mechanism-design impossibility is the regime-ascent-impossibility instance, just as composite-contraction-certification is the regime-identification-impossibility instance.

**(H4) Convergence rates as regime-tier diagnostic.** R0/R1 give exponential convergence; R2 gives polynomial. A composite whose joint dynamics show polynomial rather than exponential convergence is in R2 or saddle-only R1; this is operationally diagnosable from observation alone. Combined with the structural diagnostics (§E), this gives both *structural* and *behavioral* regime identification.

**(H5) Identifiability floor for regime.** From component-only data (sub-agent marginals), is the composite's regime in general identifiable? The same shape as `#disc-identifiability-floor` Instance 3 applies — the coupling-sign bit that distinguishes cooperative from adversarial regimes is unidentifiable from component marginals (Liberzon 2003). For the regime axis, this generalizes: the *game-structure bit* (alignment vs strategic) and the *potential-existence bit* (R1 vs R2) are jointly unidentifiable from component marginals without observation of the composite-level coupling topology. A candidate Identifiability-floor Instance 6 — regime-identification from component marginals — falls out as a derived no-go.

## §I. Open questions and reduction questions

**(Q1) Sub-tier structure within each regime.** Each regime has its own internal classification (R0 has the Contraction ladder Tier 1/2/3; R1 has potential / monotone / general; R2 has CCE-convergence-rate sub-classification; R3 has MFG-uniqueness sub-classification). Whether these sub-classifications can be unified across regimes — i.e., whether there is a meta-classification "*structural-augmentation strength required for Lyapunov certificate*" that lives on a single axis across R0/R1/R2 — is open. Plausible candidate: the Lyapunov-certificate-strength axis (full-state-space Lyapunov / local-on-deviation Lyapunov / distributional-on-empirical Lyapunov / no Lyapunov).

**(Q2) R3 — what does mean-field equilibrium actually require?** R3 is the population-scope frontier. Its formalization for AAT awaits Section III population-dynamics machinery; the current spike has only sketched the entry condition (population-distribution interaction at $N \to \infty$). The MFG literature (Lasry-Lions 2007, Huang-Malhamé-Caines 2006) supplies the external machinery; AAT's contribution would be the framework-internal coordinate (Mean-field-tempo? Population-coupling-density?) under which the machinery operates.

**(Q3) Composition of regimes — composite-of-composites.** What is the regime of a composite-of-composites? Two coordinated R0 teams meeting in a strategic interaction — is the macro-macro composite R1 (with each team as a sub-agent)? Two R1 strategic composites embedded in a larger R0 cooperative meta-composite — is the meta-composite R0? The regime axis under nested composition is open. Plausible conjecture: regime takes the *highest* tier among nested levels (in the descent direction), since any descent at any level forces the meta-composite to inherit the looser Lyapunov certificate.

**(Q4) Identifiability-floor for regime — full derivation.** The §H.5 candidate floor instance (regime-identification from component marginals) is sketched but not derived. A full derivation would identify which bits of regime-membership are identifiable from component data and which are not (the coupling-sign bit per Liberzon 2003 is the known floor; the regime-augmentation bit may be a new floor instance).

**(Q5) Reduction questions to existing meta-segments.**

- Does the regime axis reduce to a row in `#disc-separability-pattern` (8th row, Dynamic-regime ladder: R0 separable core / R1 structured repair / R2 + R3 general open)? Or does it warrant peer-meta-segment status? §H.5 suggests it has its own identifiability-floor instance (candidate Instance 6), which is the structural pattern that distinguishes a peer-meta-segment from a row-in-the-ladder (each peer-meta-segment is associated with at least one floor instance per the `#disc-separability-pattern` ↔ `#disc-identifiability-floor` complementarity).
- Does the regime axis reduce to a sub-pattern of the queued `#disc-modularity-state-dynamics`? §G's parallel three-operation structure across Axes A and B suggests *not* — they are parallel patterns, not one nested in the other. The modularity-state-dynamics meta-segment would treat Axis A; a dynamic-regime-dynamics meta-segment would treat Axis B; a higher-order meta-segment (if one is warranted) would treat their parallelism.

**(Q6) Whether Axis C (macro-state type) deserves its own status.** §C.1's identity says Axes B and C collapse for finite $N$. R3 breaks the identity. Whether Axis C deserves to be tracked separately or is fully derivable from Axis B + population-scope is open — depends on how the R3 work develops.

---

`04-MATURITY-CHECK.md` now assesses whether what is on the page is ready to leave the spike and land somewhere in canon. The axis is genuinely there in the framework's substance; the question is whether the surfacing is mature enough.
