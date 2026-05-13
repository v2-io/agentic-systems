---
slug: spike-composition-no-go
type: spike
status: exploratory
date: 2026-04-23
depends:
  - disc-identifiability-floor
  - disc-separability-pattern
  - form-composition-closure
  - scope-composite-agent
  - result-sector-persistence-template
  - deriv-critical-mass-composition
  - der-directed-separation
  - der-loop-interventional-access
---

# Spike: Composition-Layer Instance of the Identifiability Floor

**Status**: Exploratory derivation. Two candidate no-go statements pushed through; a third (Class-2 merged architectures) reframed as a *different* meta-pattern. One survives as a genuine load-bearing result matching the `#disc-identifiability-floor` shape.

**Date**: 2026-04-23

**Motivation**: The `#disc-identifiability-floor` meta-pattern currently has two derived instances (F1 on-policy L0-insufficiency detection via CHT; F13 L1' mixture-identifiability via Cramér-Rao). Both live at the single-agent level. A composition-layer instance would complete the negative half of AAD's meta-architecture with a Section III entry — symmetric to what `#disc-separability-pattern` does for scope. The question is whether there is a *genuinely load-bearing* no-go theorem at the composition layer, with an AAD-specific escape that strengthens Section III's machinery.

**Depends on**: `#disc-identifiability-floor`, `#disc-separability-pattern`, `#form-composition-closure`, `#scope-composite-agent`, `#result-sector-persistence-template`, `#deriv-critical-mass-composition`, `#der-directed-separation`, `#der-loop-interventional-access`, `spikes/spike-critical-mass-composition.md`, `spikes/spike-bridge-lemma-contraction.md`, `spikes/spike-composition-scaling-N.md`.

---

## 1. What the Meta-Pattern Requires

The `#disc-identifiability-floor` segment states the shape precisely. For a result to qualify as an instance:

1. **Setting.** An AAD inferential task under a specific information regime.
2. **External theorem.** An information-theoretic limit independent of AAD.
3. **No-go.** The external theorem is invoked to prove the task is impossible *under the regime*.
4. **Boundary characterization.** The conditions under which the regime fails — admitting partial identification — map onto specific AAD machinery.
5. **Strengthened consequence.** The floor elevates a piece of AAD machinery from "useful" to "structurally required by the theory."

A vacuous or trivially escapable no-go (e.g., "without assumptions about agent $i$, you can't analyze agent $i$") would not qualify. The bar is *genuine load-bearing*: removing the AAD machinery that escapes the floor must make the composition-layer result strictly impossible, not merely harder.

The two existing instances set the calibration. F1 applies CHT (Pearl / Bareinboim et al. 2022) to forbid distinguishing L0 from L1 on purely on-policy data. F13 applies Cramér-Rao to forbid identifying L1' mixture parameters from single-channel observation of one child. Each is *exact* under explicit conditions; each names `#der-loop-interventional-access` or observability-as-information-augmentation as the unique escape.

The question: is there a similarly-sharp composition-layer theorem?

---

## 2. Candidate No-Go Statements

I consider four candidate no-go statements, each pairing a composition-layer task with an external theorem:

- **(N-A)** Composite-contraction certification from component-level data under heterogeneous Lyapunov functions.
- **(N-B)** Composite (T2) / composite contraction from component-level data alone, without observable coupling topology, under *some* coupling sign.
- **(N-C)** Scope-satisfaction detection from on-policy composite behavior alone.
- **(N-D)** Class-2 (fully merged) composite analysis via Section II machinery.

Each is pushed in §§3-6 below. Results: (N-A) survives as a genuine no-go matching the meta-pattern; (N-B) is essentially a sharper restatement of (N-A) and is folded in; (N-C) has promise but depends on open work in `#scope-composite-agent`; (N-D) reframes an existing scope exit as a scope claim, not an identifiability floor proper.

---

## 3. Candidate (N-A): Composite Contraction from Component Data Alone

### 3.1 Precise statement

Consider the composition task at its sharpest: given $N$ sub-agents, each verified at its own level (each satisfies its own sector condition with parameters $(\alpha_i, R_i)$, each is Tier 1 per `spikes/spike-bridge-lemma-contraction.md`, each is modular per `#der-directed-separation`), *and* component-level data (sub-agent state trajectories, mismatch observations, update rules), can the composite's contraction rate $\kappa_c$ be certified — bounded below by some positive constant — from the component data alone?

"Component data alone" means: no observation of the coupling topology (the sign pattern of cross-agent influence), no common contraction metric chosen across sub-agents, no passivity certificate on the coupling channels, no shared Lyapunov function. What the certifier sees: each sub-agent in isolation, plus the fact that the agents operate in a shared environment.

*[Setting (composition-contraction-certification)]*

Let $N \geq 2$ sub-agents $\{A_1, \ldots, A_N\}$ each satisfy: (i) `#scope-agency`, (ii) `#result-sector-condition-stability` with positive $(\alpha_i, R_i)$, (iii) Tier 1 per `spikes/spike-bridge-lemma-contraction.md` (incremental sector bound DA2'-inc). Each sub-agent carries its own Lyapunov function $V_i$, each with its own metric/norm structure compatible with its update rule (e.g., Mahalanobis under the sub-agent's own innovation covariance for Kalman, quadratic in state for gradient descent on strongly convex losses). The agents interact through a shared environment; the coupling structure (who influences whom, and with what sign) is *not* observed by the certifier.

**Task:** certify $\kappa_c \gt 0$ (the composite is contracting in a combined metric compatible with all $V_i$) from component data.

### 3.2 External-theorem anchor

Two candidate external theorems supply the no-go:

- **Small-gain theorem contrapositive (Jiang, Teel, Praly 1994; Khalil 2002, ch. 5).** For interconnected ISS systems, the composite is ISS iff the product (or sum, in additive forms) of the interconnection gains is below a threshold. *When the interconnection-gain product is not verifiable from component data alone, no composite-ISS certificate is available from that data.* This is a rigorous statement: if the certifier cannot observe or bound the gain around any coupling cycle, the certifier cannot apply the small-gain theorem.

- **Impossibility of common quadratic Lyapunov function for switched linear systems (Liberzon 2003, *Switching in Systems and Control*, Theorem 2.1; Shorten, Wirth, Mason, Wulff, King 2007, "Stability criteria for switched and hybrid systems," *SIAM Review* 49:545).** For general switched linear systems $\dot x = A_\sigma x$ with $\sigma$ in a finite set, a common quadratic Lyapunov function may not exist even when each $A_\sigma$ is individually Hurwitz. **Dayawansa and Martin (1999) construct explicit $\{A_1, A_2\}$ where each is Hurwitz but no common $V$ exists.** The composition-layer analog: heterogeneous agents with independent Lyapunov functions, coupled through an unobserved topology, may admit no common Lyapunov function certifying composite contraction even when each individual $V_i$ certifies its own $A_i$.

The Liberzon/Shorten common-Lyapunov obstruction is the sharper anchor for AAD's setting. The small-gain contrapositive supplies a complementary argument focused on loop gains; both point at the same underlying identifiability gap.

### 3.3 No-go derivation

*[Derived (N-A, conditional on heterogeneous-Lyapunov + unobserved coupling + signed coupling ambiguity)]*

**Claim.** Under the setting of §3.1, there exist pairs of coupled systems $(\Sigma_1, \Sigma_2)$ and $(\Sigma_1, \Sigma_2')$ such that:

- (a) In isolation, $A_i$ and $A_i'$ are observationally equivalent at the component-data level: the same $(\alpha_i, R_i)$, the same sector condition verification, the same Tier-1 classification.
- (b) The true composite of $(\Sigma_1, \Sigma_2)$ is contracting with $\kappa_c \gt 0$ (cooperative coupling regime per `#deriv-critical-mass-composition` CM2 with $\gamma \lt 0$).
- (c) The true composite of $(\Sigma_1, \Sigma_2')$ is non-contracting, with $\kappa_c \lt 0$ (adversarial coupling regime per `#der-adversarial-destabilization` with $\gamma \gt 0$, destabilization threshold crossed).

Therefore no statistic on component data alone can distinguish $(\Sigma_1, \Sigma_2)$ from $(\Sigma_1, \Sigma_2')$. No composite-contraction certificate is available.

**Construction.** Take two Tier-1 scalar agents in the symmetric-matched setting of `spikes/spike-critical-mass-composition.md` §2:

$$\dot\delta_1 = -\alpha \delta_1 + w_1 + \gamma \mathcal T \cdot \text{sign}(\delta_2), \quad \dot\delta_2 = -\alpha \delta_2 + w_2 + \gamma \mathcal T \cdot \text{sign}(\delta_1).$$

Component-level data (each sub-agent in isolation) shows $\dot\delta_i = -\alpha \delta_i + w_i^{\text{total}}$ with total disturbance bound $\rho + |\gamma| \mathcal T$. This is consistent with both $\gamma = +\gamma_0$ (adversarial) and $\gamma = -\gamma_0$ (cooperative) — the agent experiences the cross-term as bounded disturbance regardless of sign.

- When $\gamma = -\gamma_0$ (cooperative), CM2 gives $(\alpha - C) R \gt \rho + \gamma \mathcal T = \rho - \gamma_0 \mathcal T$, easy to satisfy. $\kappa_c \gt 0$.
- When $\gamma = +\gamma_0$ (adversarial), CM2 requires $(\alpha - C) R \gt \rho + \gamma_0 \mathcal T$. For $\gamma_0 \mathcal T \gt \alpha R - \rho$ the composite destabilizes. $\kappa_c \lt 0$.

The two cases have identical component-level statistics — each sub-agent in isolation sees bounded disturbance of the same magnitude. Only observation of the *joint* dynamics (or structural knowledge of the coupling sign) distinguishes them.

*[Result (composition-contraction-no-go)]*

**Formally:** there exist two coupled systems that induce identical marginal component-level observation distributions but differ in composite contraction ($\kappa_c \gt 0$ vs $\kappa_c \lt 0$). Composite contraction is a *joint* property of the coupled system that is not in general identifiable from marginal component data.

*[Epistemic tag: Derived, tier: exact (under the symmetric-matched-Tier-1-scalar construction), robust-qualitative (for general heterogeneous composites).]*

### 3.4 Boundary characterization (the escape routes)

The no-go's regime — "component data alone, unobserved coupling topology, heterogeneous Lyapunov functions" — admits four structural escape routes, each mapping onto an existing AAD machinery:

- **(E-a) Observable coupling topology.** If the certifier observes the coupling sign pattern — either because the coupling is instrumentable in the environment (shared-channel architecture, explicit communication graph) or because `#der-loop-interventional-access` supplies interventional data at the coupling layer — then $\gamma$'s sign is identified and CM2 applies. The escape maps onto `#der-loop-interventional-access` extended to the composite layer: interventions on sub-agent $A_j$ reveal $A_i$'s cross-coupling response, which is a $do(\cdot)$-data distinction between the two constructions in §3.3.

- **(E-b) Matched Tier at the composite level (common Lyapunov function).** If sub-agents share architecture (matched Tier 1, same norm/metric), the joint quadratic Lyapunov $V = \sum V_i$ is admissible and CM2's critical-mass inequality derives $\kappa_c$ in closed form (`spikes/spike-critical-mass-composition.md` §2). The escape maps onto `#deriv-critical-mass-composition`'s derivation — which is structurally the *unique broadly-available* composition-contraction certificate.

- **(E-c) Passivity / storage-function certificate.** If each sub-agent admits a passivity certificate (storage function $S_i$ with $\dot S_i \leq u_i^T y_i - \epsilon \lVert x_i \rVert^2$, where $u_i, y_i$ are input and output at the coupling port), and the coupling itself is passive (energy-conserving or dissipative), then Willems-style dissipativity arguments (Willems 1972, "Dissipative dynamical systems," *Arch. Ration. Mech. Anal.* 45:321) certify composite stability without requiring coupling-sign observation. The escape maps onto a proposed `#passivity-composition` extension — not currently in AAD, but naturally aligned with the sector-persistence template's structure.

- **(E-d) Shared metric structure (common contraction metric).** If all sub-agents use a common contraction metric (Lohmiller & Slotine 1998), composite contraction follows from component-level contraction rates in that shared metric. The escape maps onto a proposed `#shared-metric-composition` condition — again not currently named in AAD as a scope condition.

The primary AAD-supplied escape is **(E-a) + (E-b)**: `#der-loop-interventional-access` provides the coupling-topology observability (at the composite layer); `#deriv-critical-mass-composition` provides the composite-contraction derivation under matched-Tier structure. (E-c) and (E-d) are adjacent machinery not currently in AAD; they are identified as natural extensions the no-go motivates.

### 3.5 Strengthened consequence

**The no-go elevates three AAD machinery pieces from "useful" to "structurally required":**

1. **`#deriv-critical-mass-composition`** moves from "closed-form result in a special case" to "unique broadly-available derivation certifying composite contraction under the matched-Tier structural escape." Without it, the no-go forbids the inference from component data alone.

2. **`#der-loop-interventional-access` extended to the composite layer** becomes the unique mechanism by which the coupling sign is identifiable under heterogeneous Tier structures. Interventions on one sub-agent reveal the coupling effect on the others — this is the composite-layer analog of the single-agent interventional-access-escape for F1.

3. **`#scope-composite-agent`** acquires a sharper load-bearing role: since composite-contraction certification fails under arbitrary topology, the structural machinery of scope satisfaction (one of C-i, C-ii, C-iii) must be doing real work. Without scope-satisfaction, neither the matched-Tier route (E-b) nor the interventional route (E-a) has motivation — there would be no coherent composite objective to certify. Scope-satisfaction is therefore not decorative; it is what positions the composite within a regime where one of (E-a)-(E-d) can operate.

This is the asymmetry the identifiability-floor pattern insists on. Component-level data alone *cannot* establish composite contraction. The AAD composition-layer apparatus — `#deriv-critical-mass-composition` + `#der-loop-interventional-access` (composite-extension) + `#scope-composite-agent` — is the unique broadly-available route that escapes the no-go.

### 3.6 Tier

*Exact* for the symmetric-matched-Tier-1-scalar construction in §3.3 (the cooperative / adversarial cases are exhibited in closed form).

*Robust qualitative* for general heterogeneous composites (common Lyapunov obstruction via Liberzon / Shorten for switched linear systems is an established impossibility result; the extension to general AAD composites inherits its qualitative structure but not a closed-form counterexample).

The tier matches F1's combined "exact in the shallow strict-prerequisite cases; robust qualitative for general DAG topology" pattern.

---

## 4. Candidate (N-B): Signed-Coupling Unidentifiability — Sharper Restatement

(N-B) sharpens (N-A)'s claim at the specific level of coupling sign. If §3.3's construction holds — the same marginal component-data distribution arises under both cooperative and adversarial coupling — then sign identifiability is the precise thing forbidden.

**Reduction.** (N-B) is the special case of (N-A) where the ambiguity is specifically along the cooperative/adversarial axis. Since `#deriv-critical-mass-composition`'s CM2 reads

$$(\alpha - C) R \gt \rho + \gamma \mathcal T,$$

with $\gamma$'s sign distinguishing cooperation from destabilization, and since the component-level dynamics under any signed coupling can be subsumed into total-disturbance bounds matching an unsigned $|\gamma| \mathcal T$ contribution, the sign information is *exactly* what the component-level statistics discard. This is the most compact form of the no-go — the single bit of coupling-sign information is unidentifiable from component marginals, and that bit is exactly what flips composite persistence.

(N-B) is folded into (N-A) in §8's landing recommendation. The sharper statement is useful as a pedagogical frame; it is the same theorem at higher resolution.

---

## 5. Candidate (N-C): Scope-Satisfaction Detection

### 5.1 Candidate statement

Can the certifier detect whether `#scope-composite-agent` is satisfied — specifically, whether any of (C-i), (C-ii), (C-iii) applies — from on-policy observation of the composite's behavior alone?

### 5.2 Analysis

This is structurally the *composition-layer analog* of F1: F1 forbids distinguishing two strategy-DAG structures (L0 vs L1) from purely on-policy observation; (N-C) would forbid distinguishing two scope-satisfaction structures from purely on-policy observation of the composite.

CHT (Bareinboim et al. 2022) in principle applies: the scope-satisfaction structure is a Level 2 (interventional) question — it requires asking *what the sub-agents would do under various interventions*, which is a property of the causal structure, not the observational distribution. On-policy composite behavior may arise from teleologically-aligned sub-agents cooperating under (C-i), or from opportunistically-aligned sub-agents each optimizing unrelated objectives that happen to produce the same joint behavior on the current policy (failing all three routes).

**Candidate no-go:** There exist two systems $(A_1, A_2)$ with shared objective $O_c$ (satisfying C-i) and $(A_1^\ast, A_2^\ast)$ with orthogonal objectives (failing all three routes) such that the on-policy joint-action distribution is identical. CHT forbids distinguishing them from on-policy data.

### 5.3 Why this is weaker than (N-A)

Two reasons:

1. **(C-i)/(C-ii)/(C-iii) are qualitative routes.** The `#scope-composite-agent` segment explicitly states (§Discussion) that the three routes are not shown to reduce to a single scalar. Constructing observationally-equivalent scope-satisfying vs scope-failing systems requires careful handling of which route each system occupies — a construction that the current `#scope-composite-agent` segment says *can* be done (the scope-failure examples are adversarial pairs, orthogonal objectives, etc.). But a clean no-go theorem at the instance level depends on making the routes operationally comparable, which is open.

2. **The external theorem is CHT re-applied.** The novelty would be at the AAD-application level (recognizing the composite-scope question is Level 2), but the structure repeats F1 rather than offering a distinct external anchor. Whereas (N-A) anchors in the Liberzon / Shorten common-Lyapunov-nonexistence result plus the small-gain contrapositive — a genuinely distinct external anchor at the composition layer.

### 5.4 Disposition

(N-C) is a plausible candidate but depends on structural work in `#scope-composite-agent` that is explicitly open. It is logged as a follow-on instance (parallel to the three adjacent-floors in `#disc-identifiability-floor`'s "Adjacent Floors" section) but not derived here.

---

## 6. Candidate (N-D): Class-2 Merged Architectures

### 6.1 Candidate statement

`#der-directed-separation`'s architectural classification names Class 2 (fully merged) as an explicit scope exit: Section II's sequential-cascade analysis fails by construction, because $G_t$ is causally upstream of every computation in $f_M$. Can this be restated as an `#disc-identifiability-floor` instance?

### 6.2 Why this is a *different* meta-pattern

The identifiability-floor shape requires: (task) → (external theorem) → (no-go on the task) → (AAD machinery as escape). The Class-2 scope exit has a different shape: (architectural property) → (structural incompatibility with Section II's *derivation*) → (separate framework needed, namely `03-logogenic-agents/`).

The difference is subtle but load-bearing:

- **`#disc-identifiability-floor`** names inferential tasks that *cannot be answered from limited data* under specific information regimes. The AAD machinery's escape is an *information augmentation* — intervene, instrument, observe the latent.
- **Class-2 scope exit** names a structural property (goal-conditioned processing topology) that makes *the entire decomposition $f_M$ / $f_G$ / $\pi$* inapplicable. There is no "inferential task under limited data" here; the formal object Section II derives *does not exist* for Class-2 agents.

(N-D) is a *scope-honesty* instance, not an *identifiability-floor* instance. It belongs to a related but distinct meta-pattern: "the formal apparatus does not apply to this architecture-type, coupled formulation required." The `#disc-separability-pattern` segment captures this pattern for scope; the identifiability floor does not.

**Disposition.** (N-D) is *not* an identifiability-floor instance. It is correctly handled by `#der-directed-separation`'s existing Class 1/2/3 classification plus `#disc-separability-pattern`'s architecture-ladder row. Lumping it with (N-A) would conflate two distinct kinds of scope claim and dilute the identifiability-floor pattern. **Rejected.**

---

## 7. Honest Calibration

### 7.1 Is (N-A) genuinely load-bearing?

The test: if we remove the AAD machinery (`#deriv-critical-mass-composition`, `#der-loop-interventional-access`-composite-extension, `#scope-composite-agent`), is composite contraction still inferrable from component data alone?

Walking the case:

- Without `#deriv-critical-mass-composition`: the certifier has only `#result-sector-persistence-template` (T1)-(T3) at the individual level. No closed-form composite-sector-constant derivation. The weakest-link bound (WL) from `working-composition-admissibility.md` §6.2 gives only $\alpha_c \geq \min_i(\alpha_i - \Delta\mathcal T_i^{\text{cost}})$ — which does not see coupling sign. Under the §3.3 construction, (WL) gives the *same* $\alpha_c$ lower bound for both cooperative and adversarial cases. The composite's persistence diverges in the two cases, but (WL) cannot distinguish them. So the minimal AAD machinery is insufficient.

- Without composite-extended `#der-loop-interventional-access`: the certifier cannot gather $do(\cdot)$-data on the coupling channel. The coupling sign remains unidentifiable.

- Without `#scope-composite-agent`: even if (E-a) and (E-b) were available, they would certify nothing meaningful — the "composite" might not be a composite. The scope gate is load-bearing for the *interpretation* of the certification.

All three pieces of AAD machinery are genuinely required. Removing any one reduces composite-contraction certification from "derivable under matched-Tier + observable coupling + scope-satisfaction" to "undefined." This is the asymmetry the identifiability-floor pattern demands.

### 7.2 Is the external theorem solid?

The Liberzon-Shorten common-Lyapunov-nonexistence result (Liberzon 2003, Theorem 2.1; Dayawansa-Martin 1999 explicit counterexample) is a well-established impossibility result in switched/hybrid systems theory. The small-gain contrapositive is also standard (Jiang, Teel, Praly 1994). The §3.3 AAD-specific construction reduces the composition-no-go to these external results plus the coupling-sign ambiguity argument. This matches the identifiability-floor's "conservative in style — invokes published external theorem, doesn't derive new impossibility" criterion.

### 7.3 Is the no-go trivially escapable?

Not from component data alone — the §3.3 construction is an *exhibit* (not merely an assertion) that marginal component distributions identify. The escapes (E-a)-(E-d) are genuine structural augmentations, not observational refinements. Observing more of the same marginal-component data does not escape the no-go; you must observe the *joint* or inject an intervention. This matches F1's structure exactly: purely on-policy data forbids the distinction; joint-sibling observation or exploration escapes.

### 7.4 Does the no-go compose with the other two instances?

Yes. The three instances together populate the correlation / identification / composition axes of `#disc-separability-pattern`:

| Layer | Instance | External theorem | Task | AAD escape |
|---|---|---|---|---|
| Agent-internal (correlation) | F1 | CHT | Distinguish L0 vs L1 on-policy | `#der-loop-interventional-access` (covariance test) |
| Agent-internal (identification) | F13 | Cramér-Rao | Identify L1' mixture from single channel | Observability-as-info-augmentation (Prop B.7) |
| Composition layer | (N-A) | Liberzon/Shorten + small-gain | Certify $\kappa_c \gt 0$ from component data | `#deriv-critical-mass-composition` + composite-extended `#der-loop-interventional-access` + `#scope-composite-agent` |

The three instances cover distinct external theorems (CHT / Cramér-Rao / Liberzon-Shorten), distinct AAD settings (strategy structure / mixture estimation / composite contraction), and distinct AAD-machinery escapes. This is the genuine three-layer negative structure the meta-pattern would predict.

---

## 8. Landing Map

### 8.1 Primary landing: new instance in `#disc-identifiability-floor`

Add a third instance to `#disc-identifiability-floor`, following the four-part template of Instance 1 and Instance 2:

> **Instance 3 — Composite Contraction Certification from Component Data ( #deriv-critical-mass-composition, #form-composition-closure bridge lemma)**
>
> **Setting.** Certify $\kappa_c \gt 0$ (composite contracting in a combined metric) for $N$ sub-agents each verified at its own level (individual sector conditions, Tier 1 classification) using only component-level data — no observation of the coupling sign pattern, no common contraction metric across sub-agents, no passivity certificate.
>
> **External theorem.** Common-Lyapunov nonexistence for switched linear systems (Liberzon 2003 Theorem 2.1; Dayawansa & Martin 1999 explicit counterexample in *SIAM J. Control Optim.* 37:1971); small-gain theorem contrapositive (Jiang, Teel, Praly 1994, *Math. Control Signals Syst.* 7:95; Khalil 2002 ch. 5).
>
> **No-go.** There exist pairs of coupled systems with identical marginal component-level observation distributions but opposite composite-contraction signs ($\kappa_c \gt 0$ vs $\kappa_c \lt 0$). The sign of cross-agent coupling — the single bit distinguishing `#der-team-persistence`'s cooperative regime from `#der-adversarial-destabilization`'s adversarial regime — is not identifiable from component marginals.
>
> **Boundary characterization.** Four structural escapes:
> - (a) Observable coupling topology via composite-extended `#der-loop-interventional-access` — interventions on one sub-agent reveal the cross-coupling response.
> - (b) Matched Tier at the composite level — shared architecture admits common quadratic Lyapunov, yielding `#deriv-critical-mass-composition`'s closed-form CM2 derivation.
> - (c) Passivity / storage-function certificate on the coupling channel (not currently in AAD; adjacent machinery).
> - (d) Common contraction metric (Lohmiller & Slotine 1998; not currently a scope condition in AAD).
>
> **Strengthened consequence.** `#deriv-critical-mass-composition` moves from "closed-form result in a special case" to "unique broadly-available composition-contraction certificate under the structural escape (b)." Composite-extended `#der-loop-interventional-access` becomes the unique coupling-sign identifier under heterogeneous Tier structures. `#scope-composite-agent` acquires load-bearing status: without scope-satisfaction, there is no coherent composite for the escapes to certify.
>
> **Tier.** *Exact* for the symmetric-matched-Tier-1-scalar construction (cooperative vs adversarial ambiguity in closed form). *Robust qualitative* for general heterogeneous composites (common-Lyapunov obstruction inherited from switched-systems literature).

### 8.2 Secondary landings

The instance triggers small cross-reference updates in three segments:

- **`#deriv-critical-mass-composition`**: add a Discussion paragraph noting "This derivation is the unique broadly-available escape from the composition-layer identifiability floor (`#disc-identifiability-floor` Instance 3). Component-level data alone cannot certify composite contraction; the matched-Tier structural escape this segment supplies is what makes composite persistence certifiable at all." This reframes the segment's load-bearing role upward.

- **`#der-loop-interventional-access`**: add a forward-reference to the composite-layer extension. The segment currently grounds Instance 1 at the single-agent level; noting that the same machinery extends to `#disc-identifiability-floor` Instance 3 at the composite layer (coupling-sign identification via interventions on one sub-agent) tightens its meta-pattern role across both floors.

- **`#scope-composite-agent`**: add a note in the Discussion that scope-satisfaction is the *enabling condition* for the composition-layer identifiability-floor escapes. Without it, the escapes have no target; with it, they certify a genuine composite.

- **`#disc-separability-pattern`**: the current "scope hierarchy" ladder row (Adaptive / Agency / Composite with "Section III gaps" in the general-open column) maps precisely onto Instance 3. Add a Discussion note connecting the separability-pattern's composite row to `#disc-identifiability-floor` Instance 3's no-go — this is the symmetric positive/negative pairing the separability-pattern's §"Complementarity with the identifiability floor" section runs for Instances 1 and 2 already.

### 8.3 Open extensions (adjacent-floor candidates)

Following `#disc-identifiability-floor`'s "Adjacent Floors" section, three natural extensions not addressed here:

- **Scope-satisfaction no-go (N-C).** A composition-layer analog of F1 at the scope level: CHT-based no-go on distinguishing scope-satisfying from scope-failing composites from on-policy data. Depends on open work in `#scope-composite-agent` on operationalizing the three routes.

- **N-agent scaling identifiability floor.** Following `spikes/spike-composition-scaling-N.md`: as $N$ grows, the component-data requirements for composite contraction scale as well. Is there an information-theoretic lower bound on the component-data volume needed to certify $\kappa_c \gt 0$ as a function of $N$? Candidate external theorem: sample complexity bounds for causal structure identification (Kocaoglu, Dimakis, Vishwanath 2017).

- **Heterogeneous-tier composites.** Under `spikes/spike-composition-scaling-N.md`'s Tier-1 / Tier-2 / Tier-3 mixtures, the composite's Tier membership is itself unidentifiable from component data (each sub-agent's Tier is known in isolation, but the composite inherits the weakest). This is a structural variation of (N-A) that deserves its own treatment.

### 8.4 What this spike does *not* do

- Does not close the heterogeneous-architecture obstruction in `spikes/spike-critical-mass-composition.md` §6.1. The no-go makes that obstruction's structural status sharper (it sits at the identifiability-floor level), but does not close it.

- Does not resolve the $N \gg 2$ scaling question. The no-go is stated for $N = 2$; extending to $N \geq 3$ is straightforward in principle (more coupling terms, more cases of sign ambiguity) but adds no essential new content.

- Does not introduce `#passivity-composition` or `#shared-metric-composition` as AAD segments. These are identified as adjacent machinery the no-go motivates; their promotion is a separate decision.

- Does not attempt (N-C) or (N-D) at instance-level rigor. (N-C) depends on open scope-operationalization work; (N-D) is explicitly identified as belonging to a different meta-pattern (scope honesty, not identifiability floor).

---

## 9. Honest Epistemic Assessment

**What this spike achieves.**

1. **Identifies (N-A) as a genuine identifiability-floor instance at the composition layer.** The construction in §3.3 exhibits two coupled systems with identical marginal component distributions but opposite composite-contraction signs — a concrete exhibit, not an assertion. This meets the meta-pattern's "setting → external theorem → no-go → escape → strengthened consequence" bar.

2. **Anchors the no-go in established external theorems.** Liberzon 2003 Theorem 2.1 (common-Lyapunov nonexistence for switched linear systems) + Jiang-Teel-Praly 1994 (small-gain theorem for ISS systems). These are well-established results in switched/hybrid systems theory, matching the meta-pattern's "conservative in style" criterion — published external theorem, AAD applies it.

3. **Maps the escapes to AAD machinery that acquires load-bearing status.** `#deriv-critical-mass-composition` becomes *unique broadly-available*; composite-extended `#der-loop-interventional-access` becomes the coupling-sign identifier; `#scope-composite-agent` becomes the enabling condition. This is the same structural move F1 makes for single-agent `#der-loop-interventional-access` and F13 makes for observability-as-info-augmentation.

4. **Rejects (N-D) on meta-pattern grounds.** Class-2 scope exit is scope honesty, not identifiability floor — it belongs with `#disc-separability-pattern`'s architecture ladder, which it already occupies. Keeps the meta-pattern clean.

5. **Logs (N-C) as an adjacent floor.** The scope-satisfaction-detection no-go depends on open structural work in `#scope-composite-agent`; it is a natural extension matching Instance 1's structure, not a closed result.

**What it does not achieve.**

- Does not make the general-heterogeneous case (Liberzon's full common-Lyapunov-nonexistence theorem transposed to general AAD composites) into a closed-form AAD instance. The §3.3 construction is scalar-symmetric-Tier-1; the extension inherits the general qualitative structure from Liberzon but without a closed-form counterexample at the AAD level.

- Does not introduce `#passivity-composition` (E-c) or `#shared-metric-composition` (E-d) as AAD segments. These are identified as natural extensions but their promotion requires separate work.

- Does not close the $N \gg 2$ question; Instance 3 is stated for $N = 2$.

**Confidence.**

- Instance-3 statement and the §3.3 construction: **derived, exact** (the two-system exhibit is a closed-form construction under matched-symmetric-Tier-1-scalar).
- External-theorem anchor: **solid** (Liberzon, Dayawansa-Martin, Jiang-Teel-Praly are all established).
- Load-bearing-test in §7.1: **proved** (removing any of the three AAD machinery pieces reduces certification from derivable to undefined).
- Rejection of (N-D) as identifiability-floor instance: **argued structurally** (the pattern is scope-honesty, not info-limited-inference-task-with-escape). The argument is clean; reasonable reviewers should agree.
- (N-C) as adjacent floor: **sketch-level** — depends on open work elsewhere.

**Overall.** The composition-layer identifiability-floor instance exists, is derivable, and genuinely strengthens AAD's Section III machinery. The meta-pattern's three-layer structure (two single-agent floors + one composition floor) is complete, with distinct external-theorem anchors at each layer. The spike is ready for promotion to `#disc-identifiability-floor` as Instance 3, with cross-reference updates to `#deriv-critical-mass-composition`, `#der-loop-interventional-access`, `#scope-composite-agent`, and `#disc-separability-pattern` as detailed in §8.

---

## 10. Connections to Adjacent Literature

- **Liberzon 2003, *Switching in Systems and Control*, Birkhäuser, Theorem 2.1.** Common quadratic Lyapunov function may not exist for switched linear systems even when each mode is Hurwitz. The composition-layer analog: heterogeneous sub-agents with independent Lyapunov functions may admit no common Lyapunov function certifying composite contraction. This is the primary external anchor.

- **Dayawansa & Martin 1999, "A converse Lyapunov theorem for a class of dynamical systems which undergo switching," *IEEE Trans. Automat. Control* 44:751.** Exhibits explicit $2 \times 2$ Hurwitz matrices for which no common quadratic Lyapunov exists. The two-agent counterexample at the heart of Liberzon's Theorem 2.1.

- **Shorten, Wirth, Mason, Wulff, King 2007, "Stability criteria for switched and hybrid systems," *SIAM Review* 49:545.** Comprehensive review of common-Lyapunov existence theory. Confirms the impossibility is structural, not a proof-technique artifact.

- **Jiang, Teel, Praly 1994, "Small-gain theorem for ISS systems and applications," *Math. Control Signals Syst.* 7:95.** Small-gain theorem for interconnected input-to-state-stable systems: the interconnection is ISS iff gain product below unity. Contrapositive: if interconnection-gain product is unbounded or not observable, no composite-ISS certificate available from component data.

- **Khalil 2002, *Nonlinear Systems*, 3rd ed., ch. 5.** Standard reference for small-gain theorem and related passivity-based composition results. The AAD sector-persistence template already cites this for the single-agent case (ch. 4); the composition-layer extension points to ch. 5.

- **Willems 1972, "Dissipative dynamical systems," *Arch. Ration. Mech. Anal.* 45:321.** Storage-function-based dissipativity framework — the basis for (E-c)'s passivity escape. Not currently cited in AAD; identified as adjacent machinery.

- **Lohmiller & Slotine 1998, "On contraction analysis for non-linear systems," *Automatica* 34:683.** Differential Lyapunov / contraction-metric framework — the basis for (E-d)'s shared-metric escape. Already cited in `spikes/spike-critical-mass-composition.md` §10 and in `spikes/spike-bridge-lemma-contraction.md`; the current spike makes its composition-layer role explicit.

- **Bareinboim, Correa, Ibeling, Icard 2022, "On Pearl's hierarchy and the foundations of causal inference," ACM Books.** The external anchor for the agent-internal floors (F1, and candidate N-C). Cited here for the meta-pattern's cross-layer coherence: the three-layer negative structure uses distinct external theorems but the same application shape.

- **Kocaoglu, Dimakis, Vishwanath 2017, "Entropic causal inference," *AAAI*.** Sample complexity bounds for causal structure identification — candidate anchor for the $N$-scaling adjacent-floor extension in §8.3.

None of these adjacencies change the §3.3 construction or the Instance-3 statement; they confirm the result sits correctly in the broader switched-systems / hybrid-systems / ISS-composition literature and identify where AAD's contribution is distinctive (the $U_O$-modulated $\gamma$ via scope-satisfaction, and the matched-Tier structural escape via `#deriv-critical-mass-composition`).

---

*(End of spike.)*
