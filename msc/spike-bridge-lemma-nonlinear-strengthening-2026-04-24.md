---
spike: bridge-lemma-nonlinear-strengthening-2026-04-24
date: 2026-04-24
status: exploratory — substantive partial strengthening via hybrid-dissipativity + Jacobian-iISS + passivity-composition landing; honest negative on non-smooth and adversarial halves
trigger: External reviewer (Gemini) flagged the Sector-Lyapunov Bridge Lemma (sector-bounded correction ⇒ contraction of the full update map) as verified only for linear-Kalman agents; general nonlinear case stands as unproven assumption. Strengthen-first spike examining whether the pressure point is dissolved, partially addressed, or still biting after the 2026-04-23 `#contraction-template` landing.
posture: Strengthen-first. Try three non-obvious routes before retreating to softening. Effort / time / "risk of getting stuck" are not ranked.
relates_to:
  - sector-persistence-template
  - contraction-template
  - composition-closure
  - critical-mass-composition
  - scope-composite-agent
  - gain-sector-bridge
  - sector-condition-derivation
  - adaptive-gain-dynamics
  - discussion-identifiability-floor
  - discussion-separability-pattern
  - additive-coordinate-forcing
  - agent-identity
  - msc/spike-bridge-lemma-contraction.md
  - msc/spike-contraction-metric-generalization.md
  - msc/spike-gain-sector-bridge-nonlinear.md
  - msc/spike-jacobian-b1-strengthening.md
  - msc/spike-passivity-composition.md
  - msc/spike-operator-sector-unification.md
  - msc/spike-update-operator-sector.md
  - msc/spike-a2-prime-strengthening.md
---

# Spike: Bridge-Lemma Nonlinear Strengthening — Does the Pressure Point Still Bite?

## Headline (up front)

**Is the Gemini pressure point dissolved, partially addressed, or still biting?**

**Partially addressed. It still bites, but the locus has moved.** The 2026-04-23 `#contraction-template` landing substantially closed the *cooperative nonlinear* half of the gap by providing explicit Jacobian-level / metric-contraction conditions (CT2) under which sector-bounded correction does imply full-update-map contraction, with topology-indexed closure (parallel / cascade / negative-feedback / (CM2-M)) for composition. Under the (PI) axiom in `#agent-identity` and the Čencov uniqueness theorem, two of five metric-α₂ classes (information-metric Kalman, Fisher-metric exponential families) lift to AAD-internally derived. Three metric-α₂ classes (Hessian / Lyapunov-linear-Hurwitz / Lyapunov-PID-bounded-plant) remain theorem-imported from Lohmiller-Slotine 1998 with honest labeling.

What this spike adds, beyond that prior landing:

1. **A promotable strengthening via Angle 2 (DA2'-inc ≡ (CT2) at $M=I$) that is under-advertised in current segments.** `#composition-closure`'s DA2'-inc condition *is* (CT2) at $M=I$ for $C^1$ correction maps on convex domains (Rockafellar-Wets 1998 Cor 12.4). Euclidean sub-scope metric-α₁ lifts to AAD-internally derived under the composition-scope condition *without* requiring heredity as a new axiom — the equivalence is a standard identity, already implicit in AAD's existing bridge-lemma commitment. This is a structural-transparency lift worth landing in `#composition-closure` / `#contraction-template`.

2. **Passivity / dissipativity route (L1b): promotion-ready but not yet landed.** `msc/spike-passivity-composition.md` established that the Kalman + PID-on-positive-real-plant composite — the canonical heterogeneous case currently reachable under `#critical-mass-composition` only via the weakest-link bound — is $\mathcal L_2$-stable under Willems-dissipativity with *heterogeneous storage-function shapes* (Mahalanobis + plant-storage). Under `#directed-separation`'s Class 1/2/3, **passivity closure maps cleanly onto the architectural classification**: Class 1 has clean ports (heterogeneous-composition closes); Class 3 has leaky ports (ε-error); Class 2 fails (no separable ports). This gives Section III a port-structure reading of the architecture taxonomy that is currently not visible in segments.

3. **Incremental-input-to-state-stability (iISS) / Jacobian-iISS (L2a) closes the global nonlinear-prediction gap for Tier 2 under a named Lipschitz condition.** The Tier 2 local result from `msc/spike-bridge-lemma-contraction.md` §5.3 extends to a global result under incremental ISS (Angeli 2002 / Jiang-Teel-Praly 1994 / Sontag 1989) whenever the prediction Jacobian's condition number is uniformly bounded *in a specific metric*. The scope-shift from "local-only for Tier 2" to "global-under-uniform-Jacobian-conditioning for Tier 2M" is a genuine lift for extended-Kalman, particle-filter-in-low-variance, and Bayesian-under-non-conjugate-likelihood classes.

4. **A sharp no-go result for non-smooth / rule-based agents (N1).** No Lipschitz-based sector-to-contraction bridge is possible for non-$C^1$ correction functions without additional structure (switched-systems dwell-time, Filippov solutions, impulsive-dissipative framework). **This is a structural barrier, not a gap.** The honest landing is a `type:scope` move in `#sector-condition-derivation`: sub-scope β's "rule-based / discontinuous" entry is out-of-scope for contraction-based bridge-lemma analysis, period. The `#discussion-identifiability-floor` structure absorbs the non-contractibility via regime-C identifiability collapse when the rule's state-space depends on regime structure.

5. **A sharp negative for the ADVERSARIAL half (N2).** Contraction metrics cannot handle strategic / game-theoretic equilibria (saddle points of dynamics even under Nash uniqueness). Three independent obstructions (Slotine-theorem applicability, passivity universality-property, contraction-metric attractor requirement) give a *convergent* no-go: no scalar sector-bound on single-agent correction can imply composite contraction in the adversarial regime without additional equilibrium-theoretic machinery. `#adversarial-destabilization` + `#strategic-composition` (under (C-iv) scope route) are the right tools; the bridge lemma does not extend there and cannot be forced to.

**Net:** the pressure point is reframed rather than dissolved. The cooperative nonlinear half has a substantively strengthened answer; the adversarial and non-smooth halves are sharp scope exits. The remaining "genuinely open" territory is (i) global non-Euclidean contraction for Tier 2M under uniformly-bounded prediction-Jacobian conditioning, (ii) passivity-closure in Class 3 (leaky-port composite ε-error quantification), (iii) extension to state-dependent-metric adaptive systems (Pham-Slotine 2007 / `#adaptive-gain-dynamics` (MG-4) cross-coupling).

---

## §1. Honest audit of current state

### 1.1 What Gemini flagged, and what the 2026-04-23 landing already did

Gemini's finding, restated: the **Sector-Lyapunov Bridge Lemma** asserts that a local sector condition on the correction function implies contraction of the full update map; it is proved for linear Kalman (`msc/spike-composition-correlated-kalman.md`, `msc/spike-bridge-lemma-contraction.md` §2.3) but for general nonlinear agents it sits as an unproven assumption. Without it, `#composition-closure`'s trajectory-error bound and `#critical-mass-composition`'s (CM2) both degrade from derived results to conditional claims whose conditionality is opaque.

**State at end of 2026-04-23 cycle** (per CLAUDE.md "What's Settled" + `#contraction-template` Discussion):

- `#contraction-template` (Lohmiller-Slotine generalization) landed with preconditions (CT1)–(CT3) + (M0) and Model-D / Model-S ultimate-bound results. The Jacobian-level condition (CT2) with $M=I$ is *equivalent* to `#composition-closure`'s DA2'-inc for $C^1$ $F$ on convex domains (a structural identity, standard in monotone-operator theory). This means **AAD has been carrying the Jacobian-level condition at the composite level all along** under the DA2'-inc name; the spike that produced `#contraction-template` explicitly stated this (§1.2 of `msc/spike-contraction-metric-generalization.md`).
- Monotone-operator lineage (Rockafellar 1970 / Bauschke-Combettes 2017) acknowledged in `#sector-persistence-template` and `#sector-condition-derivation` — AAD's sector condition (T2) is one-point strong monotonicity at the equilibrium; DA2'-inc is full two-point strong monotonicity; Bauschke-Combettes §§22–28 supplies the perturbation / splitting / averaging theorems.
- A2' sub-scope partition refined into metric-α₁ / metric-α₂ / metric-β as the seventh ladder of `#discussion-separability-pattern`. Metric-α₁ (Euclidean): Kalman-scalar, Euclidean strongly-convex-gradient, L2-regularized, linear-PD-symmetric. Metric-α₂ (non-Euclidean): information-metric matrix Kalman, Fisher-metric exp-family, Hessian-metric strongly-convex, Lyapunov-metric linear-Hurwitz-non-symmetric, Lyapunov-metric PID-bounded-plant.
- **(PI) parameterization-invariance axiom** added to `#agent-identity`. Via Čencov 1982 (unique Fisher metric under sufficient-statistic invariance on statistical manifolds), two metric-α₂ classes (information-metric Kalman, Fisher-metric exp-family) lift to AAD-internally derived. This is `#additive-coordinate-forcing`'s fourth primary instance — via the Čencov-uniqueness family rather than the Cauchy-FE family.
- Section III composition under (CM2-M): Slotine 2003 negative-feedback small-gain gives the heterogeneous dyad closed form $(\lambda_1 - C_1)(\lambda_2 - C_2) > k_{12}k_{21}/4$, already folded into `#critical-mass-composition`.

### 1.2 Where the pressure point still bites — precise residual

The 2026-04-23 landing addresses the cooperative / smooth nonlinear half of Gemini's finding substantively. What remains:

- **(R1) Three metric-α₂ classes remain theorem-imported** (Hessian / Lyapunov-linear-Hurwitz / Lyapunov-PID-bounded-plant). No AAD-internal axiom forces these metric choices; the Jacobian-level B1 strengthening spike's §11.3 names heredity-as-axiom as the route but flags adoption as an architectural decision.
- **(R2) Tier 2 under nonlinear prediction is local-only in `msc/spike-bridge-lemma-contraction.md` Prop 5.** The `#contraction-template` lands with "basin-chart" structure for non-convex-within-basin but the extended-Kalman-filter class remains at local-contraction status.
- **(R3) The passivity / dissipativity route is not landed.** `msc/spike-passivity-composition.md` (exploratory, 2026-04-22) identified that Kalman + PID-on-positive-real-plant — exactly the canonical heterogeneous-class composition Gemini's finding highlights — is $\mathcal L_2$-stable under Willems-dissipativity with *no matching-architecture requirement*. This is a strong, clean, textbook result (Khalil 2002 ch. 6 Thm 6.4) that should close part of Gemini's finding structurally. It did not land in a segment.
- **(R4) Non-smooth / rule-based sub-scope-β classes** have no bridge-lemma route at all; this is a genuine structural limit masquerading as an open question.
- **(R5) Adversarial / strategic Section III** (between `#critical-mass-composition` at $\gamma > 0$ and `#strategic-composition` under (C-iv) scope route) is structurally outside contraction-metric scope. This is a known honest-limits statement in `#contraction-template` §Honest failure modes, but the *convergence* of three independent obstructions into a no-go-like conclusion is worth stating sharply.
- **(R6) Identifiability-floor interaction.** `#contraction-template` §5 notes that metric formulation assumes $F$ points in a valid direction — but the coupling between the identifiability-floor axis and the Jacobian-level-contraction axis is not quantitatively stated. A combined result ("contraction holds iff $\iota_k > 0$ uniformly on the observable subspace AND the Jacobian satisfies B1*") is missing.

**Each of (R1)–(R6) is a specific target for strengthening.** The spike's posture: attempt (R1) through (R6) in order, recording outcomes honestly.

---

## §2. Route 1: hybrid-dissipativity via Willems storage functions + Khalil negative-feedback $\mathcal L_2$-stability (for (R3) / (R1) partial lift)

### 2.1 Thesis

If each sub-agent can be assigned a *Willems storage function* $S_i(\xi_i) \geq 0$ satisfying the dissipation inequality $\dot S_i \leq s_i(u_i, y_i)$ for a quadratic supply rate $s_i$, then the composite's dissipativity is *derived* without regard to storage-function shape homogeneity — passivity is preserved under parallel and negative-feedback interconnection, and $\mathcal L_2$-stability follows when one storage function is output-strict and the other input-strict (Khalil 2002 Thm 6.4; Willems 1972; van der Schaft 2017 ch. 5). This closes the heterogeneous-architecture Tier 1 / Tier 2 / Tier 3 composition question on the *cooperative half* of Section III — precisely the case where matched-architecture Lyapunov fails in `#critical-mass-composition` §6.1.

### 2.2 Formal content

Let $\xi_i$ be sub-agent $i$'s state, $u_i$ its input (disturbance + couplings), $y_i$ its output (action / response). A *storage function* $S_i: \mathcal X_i \to \mathbb R_{\geq 0}$ satisfies the **dissipation inequality** (Willems 1972):

$$\dot S_i \leq s_i(u_i, y_i). \tag{D1}$$

A system is **output-strictly passive** if $s_i(u_i, y_i) = u_i^T y_i - \epsilon_i \lVert y_i \rVert^2$ for some $\epsilon_i > 0$; **input-strictly passive** if $s_i = u_i^T y_i - \delta_i \lVert u_i\rVert^2$ for some $\delta_i > 0$. Passivity means $s_i = u_i^T y_i$.

*[Result (heterogeneous-composition-passivity, Khalil 2002 Thm 6.4)]* If $\Sigma_1$ is output-strictly passive with storage $S_1$ and dissipation rate $\epsilon_1$, $\Sigma_2$ is input-strictly passive with storage $S_2$ and dissipation rate $\delta_2$, and they are connected by negative feedback ($u_1 = r - y_2$, $u_2 = y_1$), then the composite with storage $S_c = S_1 + S_2$ is $\mathcal L_2$-stable from external input $r$ to output $y_1$: $\lVert y_1\rVert_{\mathcal L_2} \leq (1/\min(\epsilon_1, \delta_2)) \lVert r\rVert_{\mathcal L_2}$.

**Key observation (from `msc/spike-passivity-composition.md` §3.2).** The theorem does **not** require $S_1$ and $S_2$ to have matching shape. They can live in different coordinate systems, different dimensions, different units. The cross-terms in $\dot S_1 + \dot S_2$ cancel via the negative-feedback identity $u_1 = -y_2, u_2 = y_1$, regardless of storage-function shape.

### 2.3 Storage-function table for AAD sub-scope α/β

From the passivity spike §2 (adapted):

| Agent class | Storage function $S$ | Supply rate $s$ | Passivity status |
|---|---|---|---|
| Linear Kalman | Mahalanobis $\tfrac12 e^T (P^\ast)^{-1} e$ | $s = e^T(K^\ast)^T H w - \alpha_K \lVert e\rVert^2_{P^{-1}}$ | Output-strictly passive (derived) |
| Exp-family Bayesian | Bregman $D_B(\theta^\ast \Vert \theta)$ | Quadratic Fisher-bounded | Output-strictly passive (derived) |
| Gradient-on-strongly-convex | Loss excess $L(\theta) - L(\theta^\ast)$ | $s \leq w^T \nabla L - \eta \mu \lVert \nabla L\rVert^2$ | Output-strictly passive (derived) |
| PID **on positive-real plant** | Plant-storage + $\tfrac12 K_I(\int e)^2 + \tfrac12 K_D e^2$ | Port-dependent, signed | **Passive iff plant is positive-real** (conditional) |
| PID on non-positive-real plant | None generically | — | Not passive (honest limit) |
| Rule-based / discontinuous | None in general | — | Not passive (honest limit) |
| Variational approximate posterior (in basin) | ELBO excess | Local supply rate | ε-passive (conditional on convergence basin) |
| Severely misspecified | None (target-validity failure) | — | Not passive |
| Non-convex beyond basin | None (basin boundary = sector failure) | — | Not passive |

**This table is a specific strengthening.** PID-on-positive-real-plant promotes from sub-scope β to a new conditional sub-scope — **PID + positive-real-plant = dissipativity-derived, not A2'-assumed**. The positive-real-plant class covers mass-spring-damper mechanical systems, thermal systems, electrical circuits with positive impedance, and many chemical-process plants — a large applied class.

### 2.4 Worked composite: Kalman + PID-on-positive-real-plant

From `msc/spike-passivity-composition.md` §4 (adapted):

Plant: $\dot x = -\gamma_p x + u + w_{\text{env}}$, positive-real ($\gamma_p > 0$). Kalman estimates $x$ from noisy observation $o = x + v$, runs steady-state recurrence. PID uses Kalman's $\hat x$ against reference $r$. Composite storage:

$$S_c = \underbrace{\tfrac{1}{2P^\ast} e_K^2}_{\text{Mahalanobis}} + \underbrace{\tfrac{\gamma_p}{2} e_c^2 + \tfrac{K_I}{2} x_I^2 + \tfrac{K_D}{2} (\dot e_c)^2}_{\text{PID-plus-plant}}$$

Cross-terms cancel via the Kalman-output-becomes-PID-input negative-feedback identity. Composite dissipation rate is a heterogeneous minimum of $\alpha_K$ (Mahalanobis) and $\alpha_{\text{PID}}$ (plant-weighted). **Composite is $\mathcal L_2$-stable. Storage-function shapes are heterogeneous. This is a direct strengthening over `#critical-mass-composition`'s weakest-link bound for this composite.**

### 2.5 Connection to `#directed-separation` architectural classification

A structural reading that is not currently in any segment:

- **Class 1 (modular):** Ports are clean. Sub-agents have well-defined input (observation) and output (action) with separable state-update. Heterogeneous passivity closure applies directly — this is precisely the class for which the negative-feedback interconnection identity goes through cleanly.
- **Class 2 (fully merged, e.g., LLM):** No port decomposition. Observation and action entangled in the same attention / state-update operation. The negative-feedback interconnection identity *cannot be stated*, let alone used. **Passivity composition fails here structurally — not because the agents are unstable, but because the port structure doesn't exist.**
- **Class 3 (partially modular):** Leaky ports. Storage-function inequality holds up to an ε-error of magnitude $O(\kappa)$ (the modularity coefficient from `#directed-separation`). Composite is $\mathcal L_2$-stable with degraded margin proportional to $\kappa$.

**This gives `#directed-separation`'s Class 1/2/3 a *composition-theoretic* reading** complementing its modularity and identifiability readings. It is a structural-transparency move, not a new result — but it is the clearest statement of why `#directed-separation` is architectural-not-parametric at the composition level.

### 2.6 Epistemic status, route 1

*Tier: derived.* All content within existing mathematical machinery:
- Storage-function machinery: Willems 1972, standard.
- Heterogeneous passivity composition: Khalil 2002 Thm 6.1, 6.2, 6.4, standard.
- Kalman as output-strictly passive: standard estimation theory (Anderson-Moore 1979 ch. 4).
- PID-on-positive-real: KYP lemma / Lur'e-Postnikov (Khalil ch. 6 Thm 6.3), standard.

**Promotion status: promotable.** The passivity spike from 2026-04-22 is complete content; its content has not been landed in segments. This spike's route-1 conclusion is the same as the passivity spike's §9.1 substantive move — `#dissipativity-template` as a new appendix segment, OR extensions to `#sector-persistence-template` + `#critical-mass-composition` + `#directed-separation` with passivity-composition paragraphs. **The only novel addition in this spike is the Class 1/2/3 port-structure reading (§2.5).**

**Honest limit of route 1.** Passivity covers *cooperative-and-neutral* multi-agent composition. It does *not* cover:
- Adversarial regimes (strategic opponent can drive passive port against its own structure; §5.2 of this spike).
- Non-smooth / rule-based (no storage function; §5.1).
- Non-positive-real plants (PID composition closure fails).

---

## §3. Route 2: DA2'-inc ≡ (CT2) at $M = I$ — the AAD-already-had-it lift (strengthening for (R1) Euclidean cases)

### 3.1 Thesis

The Jacobian-level condition (CT2) at $M = I$ is *identically* the same object as `#composition-closure`'s DA2'-inc for $C^1$ correction functions on convex domains. This is a standard lemma (Rockafellar-Wets 1998 Cor 12.4; Nesterov 2004 §2.1.3 — strong monotonicity of $F$ ⇔ symmetric-part of Jacobian uniformly PD). **AAD has been carrying the Jacobian-level Euclidean contraction condition at the composite level since DA2'-inc was introduced** — stating it explicitly at the agent level via (CT2) is *making implicit commitments visible*, not adding new content. This lifts Euclidean sub-scope metric-α₁ from "derived conditional on theorem-import from Lohmiller-Slotine" to "derived AAD-internally" without any new axiomatic commitment.

### 3.2 Formal content

*[Result (DA2'-inc-and-CT2-equivalence), status: exact]*

For $C^1$ $F: \mathcal D \to \mathbb R^n$ on convex $\mathcal D$:

(a) DA2'-inc: $(\delta - \delta')^T (F(\delta) - F(\delta')) \geq c \lVert \delta - \delta' \rVert^2$ for all $\delta, \delta' \in \mathcal D$.

(b) Jacobian-symmetric-part-PD: $(\partial F/\partial\delta)_{\text{sym}} \succeq c I$ pointwise on $\mathcal D$.

(c) (CT2) at $M = I$ with $\lambda = c$: $-\partial F/\partial\delta - (\partial F/\partial\delta)^T \preceq -2\lambda I$, equivalently $(\partial F/\partial\delta)_{\text{sym}} \succeq \lambda I$.

**(a) ⇔ (b) ⇔ (c)** for $C^1$ $F$ on convex $\mathcal D$.

*Derivation.* (a) → (b): take $\delta' \to \delta$ along any direction $v$, divide by $\lVert \delta - \delta' \rVert^2$, take the limit. (b) → (a): integrate along the segment from $\delta'$ to $\delta$; the integrand $v^T (\partial F/\partial\delta)_{\text{sym}} v \geq c \lVert v\rVert^2$ by (b). (b) ↔ (c): direct algebraic identity. $\square$

**This is standard monotone-operator theory** (Rockafellar-Wets 1998 Cor 12.4). It is restated here because its AAD application has not been surfaced in segments.

### 3.3 Why this is a lift rather than a restatement

Before this observation, `#contraction-template`'s derivation of (CT2) for Euclidean cases runs through Lohmiller-Slotine 1998 (a theorem-import). `#composition-closure`'s DA2'-inc was a *separately-posited condition* for Tier 1 — the segment states DA2'-inc is proved for Kalman, exp-family, strongly-convex-gradient, and linear-PD without explicitly identifying it as the Jacobian-level form of the Euclidean contraction condition.

Under the equivalence:
- DA2'-inc at the agent level = B1*-inc (Jacobian-level incremental B1) = (CT2) at $M = I$.
- AAD's commitment to DA2'-inc at the composite level (for Tier 1) is *already* a commitment to the Jacobian-level Euclidean contraction condition at the composite level.
- The lift is: stating this explicitly at the agent level moves the Euclidean metric-α₁ derivation from theorem-import to AAD-internal, because the condition was already there under a different name.

**Structural-transparency lift, not a new derivation.** The mathematical content is unchanged; the *naming* changes, and under the naming change the derivation route is clearer: AAD commits to (CT2)-at-$M=I$ at the composite level via DA2'-inc; the equivalence §3.2 makes this the same as (CT2)-at-$M=I$ at the agent level under $C^1$; agent-level B1* is the natural predecessor for this via §3.1 integration-at-zero. The tier structure collapses to: **(CT2) at $M = I$ = Euclidean metric-α₁ agent-level = DA2'-inc composite-level.** No new axiom required.

### 3.4 What this does NOT lift

The observation lifts *Euclidean* metric-α₁ only. The non-Euclidean metric-α₂ cases (Fisher for statistical, Hessian / Lyapunov-metric for non-statistical) are not subsumed — they require a specific *choice* of metric that (CT2) at $M = I$ does not force.

The (PI) axiom + Čencov route (Angle 3 of `msc/spike-jacobian-b1-strengthening.md`) is the separate strengthening for statistical metric-α₂. The three non-statistical metric-α₂ classes (Hessian / Lyapunov-linear-Hurwitz / Lyapunov-PID-bounded-plant) remain theorem-imported — no route closes them AAD-internally.

### 3.5 Epistemic status, route 2

*Tier: exact.* The equivalence §3.2 is standard Rockafellar-Wets 1998 Cor 12.4 / Nesterov 2004 §2.1.3. The lift is via recognizing that AAD's existing DA2'-inc commitment was Jacobian-level-Euclidean all along.

**Promotion status: promotable (structural transparency).** Not a new mathematical result; a naming / labeling alignment that removes the theorem-import status for Euclidean metric-α₁. Should land as:

- `#composition-closure` Discussion: add a paragraph stating the equivalence (DA2'-inc ≡ (CT2) at $M = I$ for $C^1$ $F$ on convex domains) with citation to Rockafellar-Wets 1998. Cross-reference `#contraction-template`.
- `#contraction-template` Epistemic Status: classify Euclidean metric-α₁ as "AAD-internally derived via DA2'-inc equivalence" rather than theorem-imported.
- `#gain-sector-bridge` (optional): add a brief "Incremental / Jacobian-level form (B1*)" paragraph in Formal Expression, noting that under $C^1$ smoothness B1 has an incremental form B1*-inc equivalent to DA2'-inc at the agent level. Flag as derived-under-sub-scope-α.

---

## §4. Route 3: Incremental ISS / Jacobian-iISS for Tier 2 global lift (strengthening for (R2))

### 4.1 Thesis

The Tier 2 local-contraction result (extended Kalman, particle-filter-in-low-variance, Bayesian-under-non-conjugate-likelihood) in `msc/spike-bridge-lemma-contraction.md` Prop 5 can be lifted from local to global under **incremental input-to-state stability (iISS)** in a metric adapted to the prediction Jacobian's *uniform* conditioning bound. The result uses Angeli 2002 / Jiang-Teel-Praly 1994 / Sontag 1989 iISS apparatus, which for $C^1$ systems reduces to a *differential iISS-Lyapunov* condition structurally parallel to (CT2).

### 4.2 Formal content

**Incremental ISS (Angeli 2002):** a system $\dot x = f(x, u)$ is iISS if for every pair of trajectories $x_1(t), x_2(t)$ starting at different initial conditions and driven by inputs $u_1(t), u_2(t)$, there exist class-$\mathcal{KL}$ $\beta$ and class-$\mathcal K$ $\gamma$ such that

$$\lVert x_1(t) - x_2(t) \rVert \leq \beta(\lVert x_1(0) - x_2(0) \rVert, t) + \gamma(\lVert u_1 - u_2 \rVert_\infty). \tag{iISS}$$

For $C^1$ systems, iISS has a *differential* characterization: there exists a Riemannian metric $M(x)$ and class-$\mathcal K$ $\gamma$ such that the variational dynamics $\dot{\delta x} = \partial f/\partial x \cdot \delta x + \partial f/\partial u \cdot \delta u$ satisfy

$$\frac{d}{dt} \lVert \delta x \rVert_M^2 \leq -2\lambda \lVert \delta x\rVert_M^2 + c \lVert \delta u\rVert^2. \tag{iISS-diff}$$

This is precisely (CT2) with an added input-gain term — the contraction-template with exogenous input.

**Application to AAD.** Consider the full-update map $f_c(X, o)$ for a nonlinear-prediction agent. The state-difference dynamics (`msc/spike-bridge-lemma-contraction.md` §2.2):

$$f_c(X, o) - f_c(X', o) = (X - X') + \eta[g(o - \hat o(X)) - g(o - \hat o(X'))]$$

Setting $\delta u = 0$ (same observation) and $\delta x = X - X'$:

$$\Delta f_c = \delta x + \eta[g(\delta)g - g(\delta)']$$

Under:
- **(C1') Incremental sector-Lipschitz on $F_d = Hg$ (DA2'a-inc + DA2'b-inc, strong monotonicity + Lipschitz);**
- **(C2') $C^1$ prediction $\hat o(X)$ with prediction Jacobian $D\hat o(X)$ having *uniformly bounded condition number* $\kappa_h$ on a globally-valid metric $M_h(X)$;**
- **(C3') Bounded gain $\eta < 2c_{\min}/c_{\max}^2$;**

the incremental iISS-Lyapunov condition (iISS-diff) holds *globally* with $M = M_h^{-T}(X) M_h^{-1}(X)$ (pulling the Euclidean contraction back through the prediction Jacobian), contraction rate $\lambda = \eta c_{\min}/\kappa_h^2$, and input gain $c$ proportional to the observation-noise supply rate.

**Proof sketch.** The state-difference-via-innovation map is $H_h(X) \Delta f_c = -\Delta \delta + \eta [F_d(\delta) - F_d(\delta')]$ with $H_h = D\hat o(X)$. Under the *local-constant-$\kappa_h$* assumption, `msc/spike-bridge-lemma-contraction.md` Theorem 2 proves contraction in the $H^T H$-norm with $\lambda_{\text{eff}}^2 = 1 - 2\eta c_{\min} + \eta^2 c_{\max}^2$. The lift to *global* requires the Jacobian conditioning bound $\kappa_h$ to hold uniformly; this is the iISS condition $M_h(X)$ Riemannian on the whole state space. Contraction in $M_h$-norm then gives Euclidean contraction with factor $\kappa_h^2 \lambda_{\text{eff}}$ (same as the local bound but now globally). $\square$

### 4.3 Which AAD classes lift to Tier 2M-global under this condition

- **Extended Kalman filter** with prediction $\hat o(X) = h(X)$ for $C^1$ nonlinear $h$: lifts to Tier 2M-global iff $\lVert Dh \rVert / \lVert Dh^{-1}\rVert$ bounded uniformly — equivalent to the observation operator being a *uniform immersion* on the state space. This is restrictive but checkable in applied cases (EKF for smooth mechanical systems, EKF for logistic regression).
- **Particle filter in low-variance regime:** prediction Jacobian approximated by local mean; bounded-condition-number condition translates to: the filter's local linearization is uniformly well-conditioned. Holds in the low-variance regime by construction.
- **Bayesian update with non-conjugate likelihood:** prediction Jacobian is the derivative of the log-likelihood's gradient with respect to parameter; bounded-condition-number condition = Fisher information has bounded spectrum uniformly. Holds for exp-family-with-bounded-statistics.
- **Gradient-on-locally-convex-loss with sufficient global regularity:** lifts to Tier 2M-global iff the loss function is $C^2$ with Hessian eigenvalues bounded in $[\mu, L]$ *globally* (not just within the basin). This is rare — typically, non-convex losses have multiple basins with different conditioning. The basin-chart structure of `#contraction-template` §3.4 remains the honest scope.

### 4.4 What route 3 does not reach

- **Non-convex losses with multiple basins.** No global metric exists. Basin-chart structure is the honest scope.
- **Agents with discontinuous / switching dynamics.** $C^1$ requirement fails.
- **Adaptive-metric algorithms.** The metric itself changes with state; see `#adaptive-gain-dynamics` (MG-4) coupling-boundedness. If metric-state coupling satisfies (MG-4), route 3 composes; if not, metric-state feedback can destabilize.

### 4.5 Epistemic status, route 3

*Tier: derived, conditional on (C1')–(C3') and uniform $\kappa_h$ in a globally-valid metric $M_h$.* The iISS-differential characterization is standard (Angeli 2002; Sontag 1989). The application to AAD's full-update map is a structured extension of `msc/spike-bridge-lemma-contraction.md` Prop 5 from local to global under the named condition. **Promotion status: promotable as an extension to `#contraction-template` or as a distinct appendix segment `#iISS-contraction` if the global-Tier-2M result warrants separate identity.**

**Honest limit.** This is a conditional lift, not a universal one. The condition (uniform Jacobian conditioning in a globally-valid metric) is non-trivial and often fails for non-convex losses or agents with switching structure. The lift substantively extends Tier 2 from "local only" to "global under named condition"; it does not eliminate the Tier 2 honest-scope boundary.

---

## §5. Honest no-go results

Spike instructions: "Can a no-go theorem be derived — showing that for a specified broader class, no scalar sector bound can imply contraction without additional structure? A sharp negative is as valuable as a positive."

Two such results, one structural (non-smooth dynamics) and one game-theoretic (adversarial regimes).

### 5.1 No-go for non-smooth / rule-based correction functions (N1)

**Claim.** For correction functions $F: \mathcal B_R \to \mathbb R^n$ that are not locally Lipschitz, no scalar sector bound $\delta^T F(\delta) \geq \alpha \lVert \delta\rVert^2$ implies the full-update-map contraction (CP) of the bridge lemma, regardless of how tight $\alpha$ is.

**Derivation.** The bridge-lemma contraction $\lVert f_c(X, o) - f_c(X', o) \rVert \leq \lambda \lVert X - X' \rVert$ requires some form of Lipschitz continuity for the comparison to be well-defined (the update map must not jump arbitrarily between nearby $X, X'$). For discontinuous $F$ (rule-based agents with threshold triggers, state-machine controllers), $f_c$ is discontinuous in $X$, and $\lVert f_c(X, o) - f_c(X', o)\rVert$ can be $\Omega(1)$ for arbitrarily small $\lVert X - X'\rVert$ at rule-firing boundaries. No $\lambda < 1$ exists.

**Counterexample.** Let $F(\delta) = \operatorname{sign}(\delta) \cdot \min(|\delta|, c)$ for $c > 0$ (clipped sign function, a crude rule-based "bang-bang with saturation"). The sector bound $\delta \cdot F(\delta) = |\delta| \cdot \min(|\delta|, c) \geq (c/R) \delta^2$ for $|\delta| \leq R$ (crude, positive). So A2' holds with $\alpha = c/R$. But the update map $f_c(X, o) = X - \eta \operatorname{sign}(X) \cdot \min(|X|, c)$ has a discontinuity at $X = 0$, and $\lim_{X \to 0^+} f_c(X) - \lim_{X \to 0^-} f_c(X) = -2\eta \min(|X|, c) \to 0$ but the derivative at 0 is undefined. More sharply: take $F(\delta) = \alpha \delta$ for $|\delta| < 1$ and $F(\delta) = \alpha \delta + \operatorname{sign}(\delta)\cdot \mathbf 1[|\delta| \geq 1]$ (discontinuous jump at $|\delta| = 1$). Sector bound holds with $\alpha$, but $f_c$ jumps by $\eta$ at $|X| = 1$ — not a contraction.

**Verdict.** Non-smooth $F$ structurally prevents the sector-to-contraction bridge. This is **a Lipschitz floor, not a contraction-theory gap.** No refinement of sector-bound, no weighted Lyapunov, no metric adaptation escapes it without assuming additional structure (dwell-time, Filippov solutions, impulsive-dissipative framework).

**Honest landing.** `#sector-condition-derivation`'s sub-scope β entry "rule-based / discontinuous" is out-of-scope for contraction-based bridge-lemma analysis. The analytical tools for this class are in a different framework (Di Bernardo, Liuzza & Russo 2014 for piecewise-smooth switched systems; Clarke calculus for Lipschitz-nonsmooth; van der Schaft-Schumacher 2000 for hybrid-dissipative). AAD's honest scope exit is explicit: this class is formally out-of-scope for the contraction-template bridge-lemma route, and remains in sub-scope β with A2' as a per-instance modeling assumption.

**Composition with `#discussion-identifiability-floor`.** Rule-based agents with regime-dependent rule firing have *structurally* regime-C identifiability ($\iota_k = 0$ on regime-switching boundaries) — the identifiability-floor Instance 2 (L1' unobservable-$C$) absorbs the non-contractibility when the rule's state dependency is on an unobservable common cause. This is consistent with the `#discussion-identifiability-floor` pattern: structural no-go statements from external theorems (Lipschitz-continuity requirement for contraction; Cramér-Rao floor for identification) strengthen the load-bearing role of AAD's in-scope machinery.

### 5.2 No-go for adversarial / strategic regimes (N2)

**Claim.** For two-agent systems in the adversarial regime of `#critical-mass-composition` ($\gamma > 0$) or the strategic-composite regime of `#strategic-composition` under (C-iv) scope route, no single-agent scalar sector bound implies composite contraction. Three independent obstructions converge.

**Obstruction (i): Slotine-theorem-applicability.** Slotine 2003's compositional theorems (parallel / cascade / negative-feedback small-gain) require each sub-system to be individually contracting *and* for the composition topology to preserve contraction. Adversarial dynamics between two agents each optimizing opposing objectives yield a *saddle-point* equilibrium of the joint best-response dynamics — a fixed point that is attracting in some directions and repelling in others. Contraction analysis requires attracting fixed points; saddle points break the framework directly (Slotine 2003 §III).

**Obstruction (ii): Passivity-universality.** A passive system's dissipation inequality $\dot S \leq s(u, y)$ must hold for *all* inputs $u$, including adversarially chosen ones. A strategic opponent can select $u$ to maximize the recipient's storage-function growth rather than respecting the port structure. The passivity closure (Khalil Thm 6.4) remains true formally — the *supply rate* is bounded — but the adversary can drive arbitrary trajectories via the supply term regardless (`msc/spike-passivity-composition.md` §8.3). Passivity gives *cooperative/neutral* robustness, not adversarial.

**Obstruction (iii): Contraction-metric attractor requirement.** Contraction metrics (Lohmiller-Slotine 1998) prove local exponential stability of an *attractor* of the dynamics. Adversarial gradient-ascent-descent dynamics (fictitious play, no-regret dynamics) converge to Nash equilibria but the convergence is in *average-iterate* sense (Cesàro-mean), not last-iterate. Last-iterate convergence fails for generic non-zero-sum games (Daskalakis et al. 2018). No contraction metric exists for systems whose last iterates do not converge.

**Convergent no-go.** The three obstructions arise from different theorem families (compositional-contraction, dissipativity-universality, differential-Lyapunov attractor theory) but converge on the same conclusion: **no extension of sector-bounded-single-agent analysis covers adversarial multi-agent dynamics without equilibrium-theoretic machinery.**

**Honest landing.** `#strategic-composition` is AAD's right tool for (C-iv)-scope strategic composites; it uses Monderer-Shapley 1996 potential-game machinery or Rosen 1965 monotone-game machinery, *not* contraction analysis. `#adversarial-destabilization` handles asymmetric attacker-target dynamics (not a composite). The contraction-template bridge-lemma does not extend to the adversarial half of Section III *by structural necessity*. This is not a gap to be closed; it is a scope boundary that AAD correctly honors.

**Consequence for Gemini's finding.** The cooperative nonlinear half of Gemini's pressure point has a substantively strengthened answer (via routes 1–3). The adversarial half does not — and cannot — receive the same treatment. This is the *epistemic architecture* (CLAUDE.md §7) working as intended: scope-honesty surfaces where the contraction-apparatus stops applying, rather than pretending the apparatus is universal.

### 5.3 Epistemic status of no-go results

*Tier: exact for N1 (Lipschitz counterexample is constructive); robust qualitative for N2 (three independent obstructions from well-attested theorem families converge).*

**Promotion status: promotable as explicit scope statements.** The N1 no-go should land as a sharper statement in `#sector-condition-derivation`'s sub-scope β discussion: rule-based / discontinuous is *structurally* out-of-scope for contraction-based bridge-lemma analysis. The N2 no-go should land as a note in `#contraction-template` §Honest failure modes: the adversarial half of Section III has three independent obstructions to contraction analysis, naming `#strategic-composition` as the right tool.

---

## §6. Honest remaining open items

After routes 1–3 and no-go results N1, N2:

### 6.1 (R1-residual) Three non-statistical metric-α₂ classes remain theorem-imported

- **Hessian-metric strongly-convex gradient.** Metric = Hessian of loss. Motivated by optimization (Nesterov 2004; Bubeck 2015) but not forced by an AAD-internal axiom. Angle 5 (second-order curvature axiom (SOC)) of `msc/spike-jacobian-b1-strengthening.md` is a candidate but "adjacent family" only, not primary-instance.
- **Lyapunov-metric linear-Hurwitz-non-symmetric.** Metric solves Lyapunov equation $MA + A^T M = -Q$. Selected by plant structure (Hurwitz spectrum), not by AAD-internal commitment.
- **Lyapunov-metric PID-bounded-plant.** Metric solves Lyapunov equation tuned to nominal PID design. Passivity route (§2) gives positive-real-plant closure; metric-Lyapunov route gives Lipschitz-plant closure; the two overlap for strictly-positive-real plants.

**Status:** Open, with honest labeling. The heredity axiom (Angle 1 of Jacobian-B1 spike) is the most ambitious candidate route; its adoption is architectural, not mathematical.

### 6.2 (R2-residual) Tier 2M-global lift requires uniform Jacobian conditioning

Route 3 extends Tier 2 from local to global under the condition that the prediction Jacobian's condition number is bounded uniformly in a globally-valid metric. For systems where this condition fails (non-convex losses with multiple basins; switching-structure-dependent prediction), Tier 2 remains honestly local with basin-chart structure.

**Status:** Partially open. The global lift is clean under the named condition; characterizing which AAD classes generically satisfy the uniform-Jacobian-conditioning condition is a follow-up derivation.

### 6.3 (R3-residual) Passivity in Class 3 with leaky ports — ε-error quantification

§2.5 states that Class 3 (partially modular per `#directed-separation`) composes under passivity with ε-error of magnitude $O(\kappa)$ where $\kappa$ is the modularity coefficient. The ε-error's quantitative form (as a function of $\kappa$, storage-function curvatures, and port-leakage structure) is not derived here.

**Status:** Open. A dedicated spike on Class 3 passivity ε-error quantification would produce a usable bound; this spike does not supply it.

### 6.4 (R6-residual) Identifiability-floor × Jacobian-contraction joint scope

`#contraction-template` §5 notes the orthogonality of the metric axis and the identifiability-floor axis. A joint scope statement — "contraction-with-identification holds iff (CT1)–(CT3) hold AND $\iota_k > 0$ uniformly on the observable subspace" — is implicit in both `#discussion-identifiability-floor` and `#contraction-template` but not stated explicitly as a combined admissibility condition.

**Status:** Open. A joint-scope paragraph in `#contraction-template` or `#discussion-identifiability-floor` would state this explicitly; the content is a composition of existing results, not new.

### 6.5 (R-new) Adaptive-metric coupling with `#adaptive-gain-dynamics`

When the metric $M(\xi, t)$ is itself adapted alongside $\xi$, the metric-state coupling term $\dot M$ in (CT2) can destabilize contraction. `#adaptive-gain-dynamics` (MG-4) coupling-boundedness handles this for gain-state coupling; the metric-state analog is `#adaptive-gain-dynamics`'s augmented-state construction applied to the metric. This composes, but the composition is not stated in `#contraction-template`.

**Status:** Open. A cross-reference between `#contraction-template` and `#adaptive-gain-dynamics` would close the loop; the content is structural, not new.

---

## §7. Recommended segment-level moves (do NOT modify segments in this spike)

The spike instructions: "Recommended segment-level moves (new appendix segment? extension to #contraction-template? new no-go result?) — but do NOT modify segments yourself."

### 7.1 Minimal (structural transparency, no new axioms)

Land the DA2'-inc ≡ (CT2)-at-$M=I$ equivalence (Route 2, §3) and the N1/N2 no-go statements (§5) in existing segments:

- **`#composition-closure` Discussion:** add one paragraph stating that DA2'-inc for $C^1$ $F$ on convex domains is the Jacobian-level Euclidean contraction condition, equivalent to (CT2) at $M = I$ via Rockafellar-Wets 1998 Cor 12.4. Cross-reference `#contraction-template`.
- **`#contraction-template` Epistemic Status:** classify Euclidean metric-α₁ cases as "AAD-internally derived via DA2'-inc equivalence" rather than theorem-imported.
- **`#contraction-template` Honest failure modes:** sharpen the adversarial-half statement to name the three independent obstructions (Slotine-applicability, passivity-universality, contraction-metric-attractor). Cross-reference `#strategic-composition`.
- **`#sector-condition-derivation` sub-scope β discussion:** sharpen the "rule-based / discontinuous" entry — this class is structurally out-of-scope for contraction-based bridge-lemma analysis (Lipschitz floor). Cross-reference the hybrid-dissipative framework (van der Schaft-Schumacher 2000) as the appropriate external apparatus.

**Effort estimate:** Three paragraph-scale edits and one section-scale sharpening. No new segments.

**Promotion status:** Every claim is either standard monotone-operator theory (equivalence §3.2) or a scope-exit statement (N1, N2) derived from well-attested external theorem families.

### 7.2 Moderate (new meta-segment for the dissipativity route)

Land the passivity / dissipativity route (Route 1, §2) as a new appendix segment:

- **`#dissipativity-template`** (new segment, type: result, status: derived): states the Willems storage-function + Khalil negative-feedback $\mathcal L_2$-stability as an AAD appendix. Generalizes `#sector-persistence-template` to the heterogeneous-storage-function regime (quadratic storage ⊂ general Willems storage). Contains the storage-function table for AAD sub-scope α/β agents. Cross-references `#composition-closure` and `#critical-mass-composition` for the heterogeneous-composition closure route.
- **`#critical-mass-composition` Working Notes:** add a note that `#dissipativity-template` supplies the heterogeneous-architecture-composition route missing from §6.1's weakest-link bound for Kalman + PID-on-positive-real-plant.
- **`#directed-separation` Discussion:** add the Class 1/2/3 port-structure reading from §2.5 — Class 1 has clean ports (heterogeneous passivity closure), Class 3 has leaky ports (ε-error composition), Class 2 fails (no port decomposition).

**Effort estimate:** One new appendix segment (≈200 lines) plus two paragraph-scale edits.

**Promotion status:** Everything in `msc/spike-passivity-composition.md` plus the Class 1/2/3 port-structure reading. The passivity spike is itself ready for promotion; this move executes it with the architectural-classification addition.

### 7.3 Strong (dedicated appendix for global Tier-2M iISS)

If the iISS-global Tier 2M lift (Route 3, §4) warrants its own identity, land as a new appendix segment:

- **`#iISS-contraction`** (new segment, type: result, status: derived-conditional): states the incremental ISS extension of `#contraction-template` to Tier 2M-global under uniform Jacobian conditioning. Covers extended Kalman, particle-filter-in-low-variance, Bayesian-under-non-conjugate-likelihood. Cross-references Angeli 2002.

**Effort estimate:** One new appendix segment (~150 lines).

**Promotion status:** The iISS apparatus is standard (Angeli 2002; Sontag 1989; Jiang-Teel-Praly 1994); the application to AAD's full-update map is structural-derivative from `msc/spike-bridge-lemma-contraction.md` Prop 5 lifted from local to global under the named condition.

### 7.4 Recommendation

**Minimal (§7.1) should land first.** It executes the structural-transparency lift that removes one layer of theorem-import for Euclidean metric-α₁ and sharpens the scope statements that are currently soft in `#contraction-template` / `#sector-condition-derivation`. Low axiomatic cost, high architectural clarity.

**Moderate (§7.2) should land second.** It closes the *specific* heterogeneous-composition case Gemini's finding highlighted (Kalman + PID). The Class 1/2/3 port-structure reading (§2.5) gives `#directed-separation` a composition-theoretic lens it currently lacks.

**Strong (§7.3) is optional.** The iISS lift is substantive but more technical and currently has fewer direct applications within AAD's existing case catalog. Landing it would extend Tier 2M cleanly; not landing it keeps basin-chart Tier 2 as honest scope.

---

## §8. Claim-tier table (per AAD convention)

| Claim | Tier | Derivation route |
|---|---|---|
| Current AAD state partially addresses Gemini's pressure point via `#contraction-template` landing | Exact | Direct audit of 2026-04-23 cycle outputs |
| DA2'-inc ≡ (CT2) at $M = I$ for $C^1$ $F$ on convex domains | Exact | Rockafellar-Wets 1998 Cor 12.4; standard |
| Euclidean sub-scope metric-α₁ lifts from theorem-import to AAD-internal via DA2'-inc equivalence | Exact (content) / Robust qualitative (lift-status classification) | §3 |
| Heterogeneous Kalman + PID-on-positive-real-plant composite is $\mathcal L_2$-stable via Willems-dissipativity + Khalil Thm 6.4 | Exact | Khalil 2002 Thm 6.4; standard passivity theory |
| Kalman is output-strictly passive with Mahalanobis storage | Exact | Anderson-Moore 1979 ch. 4 standard |
| PID-on-positive-real-plant is passive with plant-plus-integrator-plus-derivative storage | Exact, conditional on positive-real plant | Khalil 2002 Thm 6.3 standard |
| Class 1/2/3 port-structure reading of `#directed-separation` (§2.5) | Robust qualitative | Novel AAD-structural observation; valid but not theorem |
| Tier 2M-global lift under uniform Jacobian conditioning in a globally-valid metric $M_h$ (Route 3) | Derived, conditional on (C1')–(C3') + uniform $\kappa_h$ | Angeli 2002 iISS-differential + AAD-specific composition |
| N1 no-go: non-Lipschitz $F$ prevents sector-to-contraction bridge | Exact | Constructive counterexample §5.1 |
| N2 no-go: adversarial regime has three independent contraction-apparatus obstructions | Robust qualitative | Convergence of Slotine-theorem + passivity-universality + Daskalakis et al. 2018 |
| Three non-statistical metric-α₂ classes remain theorem-imported without heredity | Robust qualitative | §6.1; no AAD-internal axiom cleanly forces metric choice |
| Adaptive-metric coupling with `#adaptive-gain-dynamics` composes but is not yet stated | Derived | §6.5; composition of existing results |
| Identifiability-floor × Jacobian-contraction joint scope is implicit but not explicit | Derived | §6.4; composition of existing results |

**Max attainable for this spike's content:** exact for Routes 2 / N1; derived-conditional for Routes 1 / 3 / N2.

---

## §9. Relation to CLAUDE.md epistemic-architecture framing

This spike's routes + no-go results compose onto AAD's three-part meta-pattern architecture (CLAUDE.md §7b):

- **`#discussion-separability-pattern` (positive):** Route 2's lift makes the seventh ladder (metric-α₁ / metric-α₂ / metric-β under A2' sub-scope) more explicit. Euclidean metric-α₁ is AAD-internally derived; statistical metric-α₂ is AAD-internally derived under (PI)+Čencov; non-statistical metric-α₂ is theorem-imported; metric-β is structurally out-of-scope (per N1).
- **`#discussion-identifiability-floor` (negative):** The N1 no-go for non-smooth / rule-based adds a *fourth* structural limit — Lipschitz-floor for contraction-based bridge-lemma analysis. This is a different flavor from the three existing instances (CHT for on-policy detection, Cramér-Rao for L1' mixture, Liberzon for composition-layer common Lyapunov); it is a smoothness-requirement floor rather than an information-theoretic floor. Could be considered for an Instance 4 entry under a broader framing of `#discussion-identifiability-floor` as "structural-property floors that AAD machinery doesn't escape."
- **`#additive-coordinate-forcing` (constructive):** No new primary instance from this spike. The (PI)+Čencov instance already landed as the fourth primary in the 2026-04-23 Gap A/B cycle.

The **epistemic-architecture interpretation** of Gemini's pressure point: it is fundamentally a question about the *scope honesty* of the bridge lemma. The pre-2026-04-23 version stated the bridge lemma without making its scope visible at the segment level. The 2026-04-23 `#contraction-template` landing surfaced metric-α₁ / metric-α₂ / metric-β as visible scope. This spike's routes sharpen which specific agent classes sit at which scope tier (storage-function route adds PID-on-positive-real-plant as sub-scope α' conditional on plant property), and the no-gos make the scope boundaries precise (N1 sharpens the sub-scope β smoothness floor; N2 sharpens the cooperative-only boundary). Net: **the pressure point is reframed from "contraction works or doesn't" to "contraction works in a characterized scope, structurally fails outside that scope for named reasons."** This is the scope-honesty-as-architecture mode (CLAUDE.md §7a).

---

## §10. Honest epistemic assessment

### 10.1 What this spike achieves

1. **Audit clarity.** The post-2026-04-23 state partially addresses Gemini's pressure point; three-plus specific residuals (R1–R6) remain. The pressure point has shifted locus: from "linear-Kalman-only" (pre-2026-04-23) to "metric-α₁ AAD-internal + statistical metric-α₂ via (PI) + non-statistical metric-α₂ theorem-imported + adversarial out-of-scope + non-smooth out-of-scope" (post-2026-04-23 + this spike). The shift is a substantive narrowing, not a dissolution.

2. **Route 1 (passivity) as promotion-ready.** `msc/spike-passivity-composition.md` content ready to land as `#dissipativity-template` meta-segment plus Class 1/2/3 port-structure reading of `#directed-separation`. Adds one new AAD sub-scope class (PID-on-positive-real-plant = sub-scope α' conditional on plant property). Closes the canonical Kalman + PID heterogeneous-composition case Gemini's finding highlighted.

3. **Route 2 (DA2'-inc ≡ (CT2)-at-$M=I$ equivalence) as promotion-ready structural transparency.** Euclidean metric-α₁ was already AAD-internal under the DA2'-inc commitment; surfacing the equivalence as an identity removes a theorem-import layer. Low-cost landing in `#composition-closure` + `#contraction-template`.

4. **Route 3 (iISS global lift for Tier 2M) as conditional promotion candidate.** Extended-Kalman, particle-filter-in-low-variance, Bayesian-under-non-conjugate-likelihood lift from local to global under uniform-Jacobian-conditioning. Standard iISS apparatus (Angeli 2002); AAD-specific composition.

5. **N1 no-go (non-smooth / rule-based Lipschitz floor) as sharp scope statement.** Structural-not-gap; the bridge-lemma route cannot extend to discontinuous $F$ without changing framework. Cross-references hybrid-dissipative machinery.

6. **N2 no-go (adversarial / strategic regime) as sharp scope statement.** Three independent obstructions converge; `#strategic-composition` is the right tool for (C-iv) scope composites.

### 10.2 What this spike does not achieve

1. **Does not lift the three non-statistical metric-α₂ classes.** Hessian, Lyapunov-linear-Hurwitz, Lyapunov-PID-bounded-plant stay theorem-imported. Heredity axiom adoption (Angle 1 of Jacobian-B1 spike) remains the most ambitious candidate; this spike does not re-litigate that architectural decision.

2. **Does not quantify Class 3 passivity ε-error.** The port-leakage → $O(\kappa)$ ε-error observation is qualitative; quantitative bound requires dedicated derivation.

3. **Does not close identifiability-floor × Jacobian-contraction joint scope explicitly.** §6.4 observes the orthogonality composes; the explicit joint-scope paragraph is a follow-up landing.

4. **Does not extend to `#adaptive-gain-dynamics` adaptive-metric coupling.** §6.5 observes the composition exists; the detailed statement is a follow-up.

5. **Does not cover the L1' mixture regime under correlated-evidence.** `#fisher-whitened-update-rule` and Prop B.7's five-way gating in `#strategic-dynamics-derivation` handle this structurally; the bridge-lemma apparatus composes with those results but this spike does not trace the composition.

### 10.3 Overall verdict

**The pressure point is partially addressed with honest characterization of the residual.** Gemini's finding — bridge lemma verified only for linear Kalman — was substantively addressed by the 2026-04-23 `#contraction-template` landing; this spike contributes three promotable strengthenings (passivity route for heterogeneous cooperative composition; DA2'-inc equivalence for Euclidean metric-α₁ theorem-import removal; iISS global lift for Tier 2M) and two sharp no-go statements (non-smooth Lipschitz floor; adversarial-regime three-obstruction convergence) that together re-characterize the scope.

The strengthen-first posture succeeds for three of six residuals (R1 Euclidean via Route 2; R3 passivity via Route 1; R2 Tier 2 via Route 3). It honestly records failures for (R1 non-statistical metric-α₂), (R4 non-smooth), (R5 adversarial) — the first because heredity-axiom adoption is architectural (this spike doesn't re-decide), the second two because they are structural limits of the contraction framework, not gaps.

**Net for Gemini's finding.** The cooperative-smooth-nonlinear half of Section III composition has a substantively strengthened bridge-lemma answer after this spike's landings. The non-smooth and adversarial halves have sharp scope exits rather than unresolved gaps. The remaining genuinely-open items (R1-non-statistical, R2-global-conditional, R3-ε-error, R5-adaptive-metric, R6-joint-scope) are characterized as follow-up work rather than indictments of the framework.

**Strongest recommendation.** §7.1 minimal landing should execute first — structural-transparency lift for Route 2 + scope-sharpening for N1/N2 — before any architectural decision about heredity or broader scope moves. This is the "surface scope at the segment level" principle (CLAUDE.md §7a) applied directly to the content this spike reviews.

---

## §11. Working notes / follow-up flags

- **Relation to `#dissipativity-template` candidate.** `msc/spike-passivity-composition.md` §9 recommends this as a substantive landing. This spike concurs and adds the Class 1/2/3 port-structure reading (§2.5) to the content. If `#dissipativity-template` is landed, it should include the port-structure reading.
- **Relation to `#operator-sector-template` candidate.** `msc/spike-operator-sector-unification.md` §10 considers a fourth meta-segment (alongside `#discussion-separability-pattern`, `#discussion-identifiability-floor`, `#additive-coordinate-forcing`) for the operator-sector / monotone-operator lineage. That decision is orthogonal to this spike's recommendations; the operator-sector spike already recommends a "modest landing" (edits to existing segments) rather than a new meta-segment.
- **Heredity axiom decision.** Angle 1 of `msc/spike-jacobian-b1-strengthening.md` remains the most ambitious strengthening; it would lift B1* at the agent level to AAD-internally forced under a stronger-form `#composition-consistency`. This spike does not re-litigate that decision. If heredity is adopted, the three non-statistical metric-α₂ classes promote; until then, they stay theorem-imported.
- **Connection to `#update-gain` / `#adaptive-gain-dynamics`.** The augmented-state construction that `#adaptive-gain-dynamics` uses for gain-state coupling (MG-1)–(MG-4) has a structural analog for metric-state coupling under adaptive-metric algorithms. A cross-reference between `#contraction-template` and `#adaptive-gain-dynamics` would close §6.5.
- **iISS vs dissipativity.** Both apparatuses handle inputs-to-states stability, but via different mathematical routes (Lyapunov-via-trajectory-difference vs storage-function-inequality). For AAD-internal use, iISS is closer to `#contraction-template` (differential Lyapunov); dissipativity is closer to `#dissipativity-template` (storage + supply rate). The two should cohere at landing; this spike treats them in separate routes (§2, §4) without forcing coherence, leaving that to segment-level landing.
- **(PI) axiom limits.** The (PI) axiom lifts the two statistical metric-α₂ classes. Extending it to non-statistical metric-α₂ via a broader invariance principle (e.g., Lie-group invariance under the agent's symmetry group) is speculative and not pursued here.
- **Opus O-BP10 slogan.** "An adaptive system is a projection whose contraction rate exceeds its target's drift rate." The operator-sector restatement in `msc/spike-operator-sector-unification.md` §12 open-questions is: "an adaptive system is an operator whose strong-monotonicity rate exceeds its disturbance rate." This spike's routes give specific strong-monotonicity certificates (DA2'-inc = (CT2)-at-$M=I$ for Euclidean; (PI)+Čencov for Fisher; dissipativity for heterogeneous storage; iISS-differential for Tier 2M-global). The slogan's segment-level surfacing would be a natural complement.

---

## §12. References

**Contraction analysis:**
- Lohmiller, W. & Slotine, J.-J. E. (1998). "On contraction analysis for non-linear systems." *Automatica* 34(6):683–696.
- Slotine, J.-J. E. (2003). "Modular stability tools for distributed computation and control." *Int. J. Adapt. Control Signal Process.* 17(6):397–416.

**Monotone operator theory:**
- Rockafellar, R. T. (1970). *Convex Analysis.* Princeton University Press. §24, §37.
- Rockafellar, R. T. & Wets, R. J.-B. (1998). *Variational Analysis.* Springer. Cor 12.4.
- Bauschke, H. H. & Combettes, P. L. (2017). *Convex Analysis and Monotone Operator Theory in Hilbert Spaces* (2nd ed.). Springer. §§4, 22–28.

**Incremental ISS:**
- Angeli, D. (2002). "A Lyapunov approach to incremental stability properties." *IEEE Trans. Automatic Control* 47(3):410–421.
- Sontag, E. D. (1989). "Smooth stabilization implies coprime factorization." *IEEE Trans. Automatic Control* 34(4):435–443.
- Jiang, Z.-P., Teel, A. R. & Praly, L. (1994). "Small-gain theorem for ISS systems and applications." *Mathematics of Control, Signals and Systems* 7(2):95–120.

**Passivity / dissipativity:**
- Willems, J. C. (1972). "Dissipative dynamical systems part I: general theory." *Arch. Rational Mech. Anal.* 45(5):321–351.
- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Ch. 6.
- van der Schaft, A. (2017). *L2-Gain and Passivity Techniques in Nonlinear Control* (3rd ed.). Springer. Ch. 5.
- Anderson, B. D. O. & Moore, J. B. (1979). *Optimal Filtering.* Prentice Hall. Ch. 4.

**Hybrid / switched systems:**
- van der Schaft, A. J. & Schumacher, J. M. (2000). *An Introduction to Hybrid Dynamical Systems.* Springer.
- Di Bernardo, M., Liuzza, D. & Russo, G. (2014). "Contraction analysis for a class of nondifferentiable systems with applications to stability and network synchronization." *SIAM J. Control Optim.* 52(5):3203–3227.

**Information geometry:**
- Čencov (Chentsov), N. N. (1982). *Statistical Decision Rules and Optimal Inference.* AMS.
- Amari, S. & Nagaoka, H. (2000). *Methods of Information Geometry.* AMS.

**Adversarial / game-theoretic convergence:**
- Daskalakis, C., Ilyas, A., Syrgkanis, V. & Zeng, H. (2018). "Training GANs with optimism." *International Conference on Learning Representations.* [Last-iterate non-convergence for generic non-zero-sum games.]
- Monderer, D. & Shapley, L. S. (1996). "Potential games." *Games and Economic Behavior* 14(1):124–143.
- Rosen, J. B. (1965). "Existence and uniqueness of equilibrium points for concave n-person games." *Econometrica* 33(3):520–534.

**AAD segments referenced:**
`#sector-persistence-template`, `#contraction-template`, `#composition-closure`, `#critical-mass-composition`, `#scope-composite-agent`, `#gain-sector-bridge`, `#sector-condition-derivation`, `#adaptive-gain-dynamics`, `#discussion-identifiability-floor`, `#discussion-separability-pattern`, `#additive-coordinate-forcing`, `#agent-identity`, `#directed-separation`, `#strategic-composition`, `#adversarial-destabilization`, `#update-gain`.

**AAD spike trail:**
- `msc/spike-bridge-lemma-contraction.md` (2026-04-06) — DA2'-inc identification + Tier 1/2/3.
- `msc/spike-contraction-metric-generalization.md` (2026-04-22) — metric-formulation R1 landing for `#contraction-template`.
- `msc/spike-jacobian-b1-strengthening.md` (2026-04-23) — Angles 1 / 2 / 3 / 4 / 5 for AAD-internal B1* strengthening.
- `msc/spike-passivity-composition.md` (2026-04-22) — Willems-dissipativity heterogeneous composition route.
- `msc/spike-operator-sector-unification.md` (2026-04-22) — monotone-operator unification 2-instance-plus-1-consequence.
- `msc/spike-update-operator-sector.md` (2026-04-22) — operator-sector on log-odds credit-assignment iteration.
- `msc/spike-gain-sector-bridge-nonlinear.md` (2026-04-02) — GA-3 ↔ local strong convexity equivalence for gradient agents.
- `msc/spike-a2-prime-strengthening.md` (2026-04-22) — A2' derivability inquiry; three paths attempted.

*(End of spike.)*
