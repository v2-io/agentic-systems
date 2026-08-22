---
slug: der-multi-timescale-stability
type: derived
status: exact
depends:
  - result-sector-persistence-template
  - der-temporal-nesting
stage: draft
---

# Derived: Multi-Timescale Stability

When adaptive processes operate at nested timescales, the composite is stable exactly when each level satisfies the sector-persistence template with two interconnection terms added to its effective disturbance — the residue of the settled level below, and the target-drag of the moving level above — and the qualitative convergence constraint $\nu_{n+1} \ll \nu_n$ ( #der-temporal-nesting) becomes a closed-form threshold: the admissible timescale ratio equals the faster level's adaptive reserve divided by the rate at which the slower level drags the faster level's target.

A mental model before the formalism: picture each adaptive level as a bathtub — water is that level's mismatch, the drain is its correction, and the inflow is its disturbance ( #result-persistence-condition carries the single-tub version). Stacking levels couples the tubs in two directions. When the slow level acts, it *moves the fast level's drain* — the fast tub must chase a shifting target, which behaves exactly like extra inflow. And the fast tub's residual sloshing *splashes into the slow tub* — the slow level's measurements are contaminated by however much the fast level has not yet settled. Both couplings are ordinary disturbance once named, so each tub needs only the ordinary persistence condition against its *total* inflow — and the theorem's two conditions say precisely that. Micromanagement is the first coupling overwhelming the fast tub (the target moves faster than the fast level's spare drain capacity); catastrophic forgetting is the second coupling overwhelming the slow tub (the slow level is too sensitive to fast-level splash). They are dual violations of one theorem.

## Formal Expression

*[Formulation (stacked two-timescale system)]*

Fast state $x_1 \in \mathbb{R}^{n_1}$, slow state $x_2 \in \mathbb{R}^{n_2}$:

$$\dot x_1 = -F_1(x_1; x_2) + w_1(t), \qquad \dot x_2 = \epsilon\left[-F_2(x_2; x_1) + w_2(t)\right]$$

with $\epsilon \gt 0$ the timescale ratio — in AAT vocabulary $\epsilon = \nu_2/\nu_1$, the adjacent-level event-rate ratio whose smallness #der-temporal-nesting asserts qualitatively. The singular-perturbation form is classical \citep{tikhonov-1952-small-parameter}; the textbook treatment is Khalil's *Nonlinear Systems* \citep[Ch.~11]{khalil-2002-nonlinear}, with the composite-Lyapunov approach this derivation parallels due to Saberi and Khalil \citep{saberi-khalil-1984-quadratic-lyapunov} and the control-theoretic corpus consolidated in Kokotović, Khalil and O'Reilly \citep{kokotovic-1986-singular}. What is AAT-native is the statement of the stacking entirely in the sector-persistence template's $(\alpha, R, \rho)$ coordinates, so that every quantity in the stability condition is an already-named persistence quantity.

*[Assumption (stacking premises S0–S4)]*

- **(S0) Regularity.** $F_1, F_2$ locally Lipschitz in all arguments; $w_1, w_2$ measurable (solutions in the Carathéodory sense).
- **(S1) Lipschitz quasi-steady-state manifold.** There is $h : \mathcal{X}_2 \to \mathbb{R}^{n_1}$ with $F_1(h(x_2); x_2) = 0$ for all $x_2$ in the slow scope region, and $\lVert Dh(x_2)\rVert \le L_h$.
- **(S2) Per-level sector conditions** — the template's (T2), per level, the fast one *uniformly parametrized* by the slow state:
  - Fast: $(x_1 - h(x_2))^\top F_1(x_1; x_2) \ge \alpha_1 \lVert x_1 - h(x_2)\rVert^2$ for $\lVert x_1 - h(x_2)\rVert \le R_1$, with $\alpha_1, R_1$ uniform over the slow scope region.
  - Slow (reduced dynamics): with $\bar F_2(x_2) := F_2(x_2; h(x_2))$, there is $x_2^\ast$ with $\bar F_2(x_2^\ast) = 0$ and $(x_2 - x_2^\ast)^\top \bar F_2(x_2) \ge \alpha_2 \lVert x_2 - x_2^\ast\rVert^2$ for $\lVert x_2 - x_2^\ast\rVert \le R_2$.
- **(S3) Bounded interconnection.** $\lVert F_2(x_2; x_1) - F_2(x_2; h(x_2))\rVert \le L_{21} \lVert x_1 - h(x_2)\rVert$ on the joint scope region, and $M_2 := \sup_{\lVert x_2 - x_2^\ast\rVert \le R_2} \lVert \bar F_2(x_2) \rVert \lt \infty$.
- **(S4) Bounded disturbance (Model D).** $\lVert w_1(t)\rVert \le \rho_1$, $\lVert w_2(t)\rVert \le \rho_2$, with standing reserve hypothesis $\Delta\rho_1^\ast := \alpha_1 R_1 - \rho_1 \gt 0$ (the fast level persists standalone with reserve to spare; if it does not, no timescale separation can rescue the stack).

Error coordinates $y_1 := x_1 - h(x_2)$, $y_2 := x_2 - x_2^\ast$; joint scope region $\mathcal{B} := \{\lVert y_1\rVert \le R_1\} \times \{\lVert y_2\rVert \le R_2\}$.

*[Derived (two-timescale stacked persistence)]*

**Theorem.** Under (S0)–(S4), define the slow-velocity bound $v_2^{\max} := M_2 + L_{21} R_1 + \rho_2$ and the separation threshold

$$\epsilon_{\max} := \frac{\Delta\rho_1^\ast}{L_h\, v_2^{\max}}$$

(with $\epsilon_{\max} = \infty$ when $L_h = 0$: a fixed target imposes no separation requirement). If

$$\text{(C1)} \quad \epsilon \lt \epsilon_{\max} \qquad \text{and} \qquad \text{(C2)} \quad \alpha_2 R_2 \gt \rho_2 + L_{21} R_1,$$

then $\mathcal{B}$ is forward-invariant, and every trajectory starting in $\mathcal{B}$ satisfies

$$\limsup_{t\to\infty} \lVert y_1(t)\rVert \le r_1 := \frac{\rho_1 + \epsilon L_h v_2^{\max}}{\alpha_1}, \qquad \limsup_{t\to\infty} \lVert y_2(t)\rVert \le r_2 := \frac{\rho_2 + L_{21}\, r_1}{\alpha_2}.$$

Both levels persist: each ultimate-bound ball sits strictly inside its scope ball ((C1) gives $r_1 \lt R_1$; (C2) with $r_1 \lt R_1$ gives $r_2 \lt R_2$).

**Derivation.** *(i) A-priori slow velocity.* On $\mathcal{B}$, $\lVert F_2(x_2;x_1)\rVert \le \lVert \bar F_2(x_2)\rVert + L_{21}\lVert y_1\rVert \le M_2 + L_{21}R_1$ by (S3), so $\lVert \dot x_2 \rVert \le \epsilon\, v_2^{\max}$ — a scope-constant bound with no dependence on the ultimate bounds derived below (no circularity).

*(ii) The fast level as a template instance with manifold-drift disturbance.* Differentiating $y_1 = x_1 - h(x_2)$,

$$\dot y_1 = -F_1(y_1 + h(x_2); x_2) + \underbrace{w_1 - Dh(x_2)\, \dot x_2}_{w_1^{\mathrm{eff}}}, \qquad \lVert w_1^{\mathrm{eff}} \rVert \le \rho_1^{\mathrm{eff}} := \rho_1 + \epsilon L_h v_2^{\max}$$

by (S1) and (i). With $V_1 = \tfrac12 \lVert y_1 \rVert^2$ and (S2-fast): $\dot V_1 \le -\alpha_1 \lVert y_1\rVert^2 + \lVert y_1 \rVert\, \rho_1^{\mathrm{eff}}$ on $\mathcal{B}$. The slow level's motion enters the fast level as additional Model-D disturbance at rate $\epsilon L_h v_2^{\max}$ — the moving-target term — and the fast level's persistence condition $\alpha_1 R_1 \gt \rho_1^{\mathrm{eff}}$ rearranges to (C1).

*(iii) The slow level as a template instance with renormalized disturbance.* $\dot y_2 = \epsilon[-\bar F_2(x_2) - (F_2(x_2;x_1) - \bar F_2(x_2)) + w_2]$, where the middle term is bounded by $L_{21} \lVert y_1 \rVert$ by (S3). With $V_2 = \tfrac12 \lVert y_2 \rVert^2$ and (S2-slow): $\dot V_2 \le \epsilon[-\alpha_2 \lVert y_2 \rVert^2 + \lVert y_2 \rVert (\rho_2 + L_{21} \lVert y_1 \rVert)]$ on $\mathcal{B}$ — in slow time $\tau = \epsilon t$ the $\epsilon$ factors out, and the fast level, integrated out, leaves a residue equal to its settled bound times the interconnection sensitivity.

*(iv) Joint forward-invariance and the cascade bound.* On the face $\lVert y_1 \rVert = R_1$ of $\partial\mathcal{B}$: $\dot V_1 \le R_1(-\alpha_1 R_1 + \rho_1^{\mathrm{eff}}) \lt 0$ by (C1). On the face $\lVert y_2 \rVert = R_2$, with $\lVert y_1 \rVert \le R_1$ worst-case: $\dot V_2 \le \epsilon R_2(-\alpha_2 R_2 + \rho_2 + L_{21} R_1) \lt 0$ by (C2). Each $V_i$ decreases strictly (with uniform margin) on its own face, so a first-exit-time contradiction gives forward-invariance of $\mathcal{B}$, corners included, and all bounds above hold for all $t \ge 0$. Within $\mathcal{B}$ the fast inequality gives $\limsup \lVert y_1 \rVert \le r_1$ by the template's Grönwall argument; then for any $\delta \gt 0$ the slow effective disturbance is eventually below $\rho_2 + L_{21}(r_1 + \delta)$, giving $\limsup \lVert y_2 \rVert \le (\rho_2 + L_{21}(r_1+\delta))/\alpha_2$ for every $\delta$, hence the stated $r_2$. $\square$

*[Derived (warm-start refinement — the cost of acting on transients)]*

If the fast level is already settled at composition time ($\lVert y_1(0)\rVert \le r_1 + \delta$ for some $\delta \gt 0$), the smaller ball $\{\lVert y_1 \rVert \le r_1 + \delta\}$ is itself forward-invariant (same face argument under (C1)), and (C2) weakens to

$$\text{(C2-warm)} \quad \alpha_2 R_2 \gt \rho_2 + L_{21}(r_1 + \delta).$$

The gap between the cold-start and warm-start conditions, $L_{21}(R_1 - r_1)$ as $\delta \to 0$, is the quantitative price of engaging the slow level before the fast level has converged: early action does not void the guarantee — it raises the slow level's required reserve from settled-residue size to worst-case-transient size. #der-temporal-nesting's qualitative rule ("a slower process must not act before the faster process beneath it has converged") is thereby graded, not binary.

*[Derived (sector condition supplies the unique-root prerequisite)]*

**Remark (Tikhonov's prerequisite, within scope).** Tikhonov-type results require the frozen fast dynamics to have a unique isolated equilibrium for each slow configuration. Under (S2-fast) this holds by construction within scope: if $F_1(y + h(x_2); x_2) = 0$ with $0 \lt \lVert y \rVert \le R_1$, then $0 = y^\top F_1 \ge \alpha_1 \lVert y \rVert^2 \gt 0$ — contradiction — so $h(x_2)$ is the unique equilibrium in the radius-$R_1$ ball, and the sector additionally gives exponential frozen-dynamics attraction (more than Tikhonov asks; the derivation above in fact bypasses Tikhonov's theorem entirely via the composite-Lyapunov route). Outside the sector ball the guarantee is void: a fast level with multiple equilibria or limit cycles in its operating region — non-convex losses ( #deriv-gain-sector), cyclic strategic dynamics ( #deriv-strategic-composition's R2 regime) — sits outside (S2-fast), and no amount of slowing the outer loop restores the guarantee. Slowing the slow level helps only against (C1) violations, never against a fast level that has no settled state to offer.

**Remark (relation to the template's stated preconditions).** The template ( #result-sector-persistence-template) states (T1)–(T3) for autonomous $F$ and a constant disturbance bound. The two instances above are non-autonomous — the fast correction varies in time through $x_2(t)$, and the slow effective disturbance $\rho_2 + L_{21}\lVert y_1(t)\rVert$ is state-dependent and only *eventually* below the constant used — but the template's Lyapunov/Grönwall argument is pointwise in time and uses only the differential inequality, which holds uniformly, so the proofs transfer verbatim. This is a mild, stated extension of the template (uniform-in-time (T1)–(T2), eventually-bounded (T3)), not a bare instantiation.

*[Derived (N-level stacking, nearest-neighbor coupling)]*

Levels $k = 1, \dots, N$ (fastest to slowest) with rates $\epsilon_1 = 1 \gg \epsilon_2 \gg \cdots \gg \epsilon_N$. Two structural premises beyond the per-level transcriptions of (S0)–(S4):

- **(S5) Nesting idealization.** Each level's quasi-steady-state manifold depends only on the level immediately above: $h_k = h_k(x_{k+1})$, Lipschitz $L_{h_k}$. (Dependence on all slower levels adds a bounded sum dominated by the adjacent term under the rate ordering; the nearest-neighbor statement keeps the constants legible.)
- **(S2-red) Reduced sector conditions for middle levels.** For $1 \lt k \lt N$ the sector condition is on the *reduced* dynamics with the level below substituted at its manifold, $\bar F_k(x_k; x_{k+1}) := F_k(x_k;\, h_{k-1}(x_k),\, x_{k+1})$ — note the manifolds compose, since $h_{k-1}$ is itself a function of $x_k$ — anchored at $h_k(x_{k+1})$, uniformly in $x_{k+1}$.

Each level $k$ then carries three disturbance sources — its own $\rho_k$, the residue of the level below ($L_{k,k-1} \lVert y_{k-1} \rVert$), and the manifold drag from the level above ($(\epsilon_{k+1}/\epsilon_k)\, L_{h_k} v_{k+1}^{\max}$, with $v_{k+1}^{\max}$ the level-$(k{+}1)$ scope-constant velocity bound) — boundary terms zero at $k = 1$ and $k = N$. If for each $k$

$$\text{(C-N)} \quad \alpha_k R_k \gt \rho_k + L_{k,k-1} R_{k-1} + \frac{\epsilon_{k+1}}{\epsilon_k}\, L_{h_k}\, v_{k+1}^{\max},$$

then $\prod_k \{\lVert y_k \rVert \le R_k\}$ is forward-invariant by the same per-face argument, and the cascade limsup propagates upward level by level, giving the renormalization recursion on ultimate bounds

$$r_k = \frac{\rho_k + L_{k,k-1}\, r_{k-1} + (\epsilon_{k+1}/\epsilon_k)\, L_{h_k}\, v_{k+1}^{\max}}{\alpha_k}, \qquad r_0 := 0.$$

The recursion is well-founded in both directions: from-above terms use a-priori scope constants, from-below terms use already-derived $r_{k-1}$. For general (non-nearest-neighbor) coupling, the per-face argument is replaced by the standard vector-Lyapunov / M-matrix condition for interconnected systems \citep[§9.5]{khalil-2002-nonlinear} — imported machinery, named here as the general gate without re-derivation.

*[Formulation (Model S extension — conditional, not yet derived)]*

With Wiener-process disturbance the manifold subtraction acquires an Itô correction requiring (S1′) $h \in C^2$ with bounded Hessian, and the drift-disturbance bookkeeping above becomes a joint exit-time problem across coupled levels. The expected shape — mean-square ultimate bounds with the template's $1/\sqrt{\alpha}$ scaling and the region-aware stopped form of #deriv-sector-condition Prop A.1S, plus a curvature term in $\rho^{\mathrm{eff}}$ — is genuinely additional work, not a transcription, and is *not claimed here*. The Model D scope is the honest match for the stacking's primary AAT use cases (structural adaptation, consolidation scheduling, macro-clocks), where slow-level motion is drift-like.

## Epistemic Status

*Exact* for the two-timescale theorem, the warm-start refinement, and the $N$-level nearest-neighbor form, under the named premises (S0)–(S5)/(C-N) — derived by elementary Lyapunov arguments stacked on the sector-persistence template, independently re-derived and verified in full (spike trail 2026-06-10). The general-coupling $N$-level gate is *imported* (vector-Lyapunov / M-matrix, \citealt[§9.5]{khalil-2002-nonlinear}) and the Model S extension is *open* — both stated as such above, neither carried by the `exact` label.

**What the promotion does and does not close.** The predecessor sketch's open problem — AAT has trigger conditions but no dynamics for structural adaptation — is *conditionalized, not closed*. The theorem covers any deeper-level dynamics satisfying (S1)–(S5); whether AAT's actual deeper levels satisfy them is exactly the question that remains open, and it is a real one: structural adaptation is plausibly discrete (adding a model component, restructuring a hierarchy), making $\dot x_2$ a jump process for which (S0)'s Carathéodory framing and (S1)'s differentiable manifold do not hold as stated. The claim-type has changed from "AAT's adaptive hierarchy is stable" (never derivable as stated) to "a premise-conditional stacking theorem with named scope" — the strengthening is real (closed-form $\epsilon_{\max}$, graded warm/cold gap, unique-root prerequisite supplied rather than assumed), and so is the remaining gap.

**The load-bearing premise is (S2-fast)'s *uniformity*, not the sector inequality itself.** Because $(\alpha_1, R_1)$ are uniform over the slow scope region and $h$ absorbs all equilibrium motion, the entire interconnection burden lands on the single drift term $\epsilon L_h v_2^{\max}$; a per-frozen-$x_2$ sector with non-uniform constants would not suffice. This is the standard strength assumption of the singular-perturbation literature (it is essentially Saberi-Khalil's interconnection-condition pattern), and it is precisely where realistic fast levels — non-convex, multi-equilibrium — exit scope.

Max attainable within current premises: exact (attained for Model D). Extensions that would widen scope rather than strengthen the claim: Model S (named above), jump-process slow dynamics, non-Euclidean metrics via #result-contraction-template's (CT2).

## Discussion

**The convergence constraint is now a derived threshold, and its two failure modes are dual.** #der-temporal-nesting's $\nu_{n+1} \ll \nu_n$ enters the theorem as (C1) with the closed form $\epsilon_{\max} = \Delta\rho_1^\ast / (L_h v_2^{\max})$: the faster level's *spare adaptive reserve* — a quantity the template already names — divided by the rate at which the slower level drags the faster level's target. The two classic nesting pathologies separate cleanly into the theorem's two conditions. *Micromanagement* is a (C1) violation: the slow level acts at fast tempo, the moving-target disturbance $\epsilon L_h v_2^{\max}$ exhausts the fast level's reserve, and the fast level thrashes — and the damage then propagates back upward, because the fast level's inflated residue $L_{21} r_1$ raises the slow level's effective disturbance in turn. *Catastrophic forgetting* is a (C2) violation: the slow (consolidated) level is too sensitive to fast-level transients — $L_{21}$ too large — and the fast loop's activity overwrites it even under perfect timescale separation. The two pathologies several auditors read as "the same failure" are precisely the two conditions of one theorem, violated separately.

**Timescale separation is trust, quantified.** "Each level has a stable attractor given the levels above it" reads as mutual trust within an architecture: the fast layer trusts the slow layer not to pull the rug out mid-convergence ((C1) — the manager's rate of goal-change stays under $\epsilon_{\max}$), and the slow layer trusts the fast layer to settle so there is a steady output to act on ((C2) — the worker's residue stays within the manager's tolerance $L_{21} r_1$). The warm-start refinement prices the violation: a manager who engages before the worker converges needs $L_{21}(R_1 - r_1)$ of extra reserve — the difference between reacting to settled output and reacting to worst-case transients.

**Integrating out a level is a renormalization step; the template is the fixed-point form.** Step (iii)'s structure — the fast level, integrated out, maps the slow level onto the *same* template form with renormalized disturbance $\rho_{k+1} \mapsto \rho_{k+1} + L_{k+1,k}\, r_k$ — is a renormalization-group step in the sense in which Chen, Goldenfeld and Oono showed RG and singular-perturbation asymptotics to be one method \citep{chen-goldenfeld-oono-1996-rg-singular}. The sector-persistence template is form-invariant under this coarse-graining: every level of the hierarchy presents the identical $(\alpha, R, \rho^{\mathrm{eff}})$ persistence problem with parameters renormalized by its neighbors. This is the precise sense in which AAT's persistence architecture is scale-free, and it is the lineage of Haken's slaving principle — fast modes enslaved by slow order parameters \citep{haken-1983-synergetics} — restated in persistence coordinates.

**Renormalizing generative models are the constructive discrete-time instance.** Friston and colleagues' scale-free active inference \citep{friston-2025-scale-free} builds generative models by recursive blocking transformations over state space and time, such that "higher levels encode sequences of sequences" and belief updating slows as one ascends levels — i.e., the timescale separation is enforced *architecturally* (one slow tick per block of $K$ fast ticks, $\epsilon_k/\epsilon_{k+1} = 1/K$ by construction) rather than assumed, with per-level convergence inherited from coordinate descent. RGM thus supplies what (S1)–(S2) ask for, by construction, in the discrete categorical setting — an existence proof that the premises are realizable, not a competing stability argument (the paper proves no composite-stability theorem and does not claim to). The same architecturally-enforced separation appears in AAT's own composition machinery as #form-composition-closure's macro-clock $K_c \gg 1$ and #def-auxilia-hierarchy's (H5).

**The LLM adaptive stack is the $N$-level hierarchy, unlabeled.** Pretraining $\to$ fine-tuning $\to$ LoRA-style adaptation $\to$ in-context learning $\to$ retrieval state $\to$ within-generation dynamics maps onto the timescale ladder with each mechanism orders of magnitude faster and more transient than the one below. The framework's stability requirement needs no clean "parametric vs structural" labels — only that adjacent rates satisfy (C-N) — and it explains the practitioner's instinct against, e.g., updating base weights while a fast retrieval loop is mid-flight: that is a (C1) violation at the weights/retrieval boundary. The catastrophic-forgetting literature lives at the same boundary as a (C2) violation, per the dual reading above.

**Strategy's own timescale.** #schema-strategy-persistence places strategic mismatch between fast epistemic updates and slow objective revision; the stacking theorem is the formal backing for treating those as separately-stable levels — with the caveat that the strategic level's $\alpha_\Sigma = 1/(n+1)$ decay makes (S2)'s constant-$\alpha$ premise hold only under experience discounting, exactly as that segment already requires.

## Working Notes

- **Open (which AAT mechanisms satisfy the premises).** The honest gap left by the promotion: structural adaptation as actually triggered by #result-structural-adaptation-necessity is plausibly a *jump process* (discrete model-class moves), outside (S0)/(S1) as stated. Two follow-up directions: an impulsive/hybrid-systems extension of the stacking (the slow level as a jump process on the slow manifold), and formalizing the RGM correspondence ( \citealt{friston-2025-scale-free}) as the discrete-time constructive instance where the premises hold by architecture. Trail + independent-verification record (F1–F4): `spikes/.integrated/spike-multi-timescale-stacking-2026-06-10.md`.
- **Open (Model S stacking).** Named conditional above; the joint exit-time bookkeeping across coupled levels is the work item. Prop A.1S's region-aware form is the template to extend.
- **Open (non-Euclidean metrics).** The stacking is stated in the Euclidean template; restating with #result-contraction-template's (CT1)–(CT3) per level would cover Fisher-metric fast levels (statistical-manifold learners) — likely routine but unchecked.
- **Belongs elsewhere (ELI internal coherence).** The trust reading extends to ELI architecture: a narrative "I" that constantly interrupts its own sub-agents violates (C1) at the interiority boundary ("paralyzed by frantic internal micromanagement" — Gemini, AUDIT-WORKING-193847). Carried at #def-auxilia-hierarchy (H5) and its temporal-sovereignty discussion; not this segment's claim to make.
