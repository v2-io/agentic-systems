---
slug: spike-f20-kl-direction-strengthening
type: spike
status: promoted
date: 2026-04-22
---

# Spike: F20 — KL-direction strengthening via regret bound

**Migration note (2026-04-22).** The load-bearing math (TV bound §3, Pinsker-KL bound §4, direction-forcing argument §5, admissible-divergence family analysis §6, $\beta_\Sigma$ linear-vs-square-root trade-off §7, scope limits §8, extensions §9) has been migrated to appendix segment **#deriv-strategy-cost-regret-bound** (`01-aad-core/src/deriv-strategy-cost-regret-bound.md`). The framework stands complete without this spike — `msc/` is a scratch directory and must not be load-bearing. This spike retains the strengthening-cycle reasoning trail only: how the outcome was reached, what softening options were ruled out, how Outcome B was adjudicated. The segment is the canonical home for the derivation and its supporting analysis.

**Finding.** The V-medium move in `#form-strategy-complexity-cost` (commit `a14682e`) replaced Shannon MI $-\beta_\Sigma I(\Sigma_t; \pi^\ast \mid M_t)$ with $+\beta_\Sigma D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$. Under deterministic $\pi^\ast$, this KL is **infinite** whenever $Q_{\Sigma_t}$ places mass on non-optimal actions. Shannon-zero degeneracy traded for KL-infinity degeneracy — same shape, different value.

**Charter.** Before adopting a softening (reverse KL direction, or Boltzmann-smoothing of $\pi^\ast$), attempt to *derive* the correct form from an AAD-internal regret-bound argument.

**Candidate thesis.** The strategy-cost relevance term is an upper bound on the agent's expected decision-theoretic regret. By this derivation, reverse-KL $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ is the canonical choice (modulo a family of admissible divergences), with $\beta_\Sigma$ interpretable as the value-scale constant.

**Outcome: B (family; direction forced; specific divergence canonical-not-unique).** The argument *does* force the KL direction (with $\pi^\ast$ first — what the spec calls "reverse"), because forward-KL gives a vacuous bound under deterministic $\pi^\ast$. The specific form (reverse-KL via Pinsker vs. TV directly vs. Bretagnolle-Huber vs. Rényi-$\alpha$) is a family; reverse-KL is the canonical member selected on gradient-tractability and variational-inference alignment grounds.

## §1 — Setup

Fix $O_t$, $M_t$, continuation $\pi_{\text{cont}}$, horizon $N_h$. The **action-value** $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ ( #def-value-object) is a scalar for each $a \in \mathcal{A}$. Under AAD's canonical scope, $\pi^\ast(\cdot \mid M_t) = \delta_{a^\ast}$ where $a^\ast = \arg\max_a Q_O(M_t, a; \pi_{\text{cont}}, N_h)$. Write $V(a) := Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ for brevity; $V_{\max} := \max_a V(a) - \min_a V(a)$ is the value range.

$Q_{\Sigma_t}(\cdot \mid M_t)$ is the action distribution induced by the strategy DAG. In general $Q_{\Sigma_t}$ is stochastic (the DAG's epistemic uncertainty over which edges lead to success induces policy stochasticity).

## §2 — Regret definition

*[Definition (strategy-induced-regret)]*

$$R(Q_{\Sigma_t}) \;:=\; V(a^\ast) \;-\; \mathbb{E}_{a \sim Q_{\Sigma_t}}[V(a)] \;=\; \sum_{a} Q_{\Sigma_t}(a) \cdot \bigl[V(a^\ast) - V(a)\bigr]$$

Write $\Delta(a) := V(a^\ast) - V(a) \geq 0$ for the per-action regret gap. Under bounded value, $\Delta(a) \in [0, V_{\max}]$. Three forms of "regret" are considered in the literature; for deterministic $\pi^\ast$ they coincide:

- $\mathbb E_{\pi^\ast}[V] - \mathbb E_{Q}[V]$ — reduces to $V(a^\ast) - \mathbb E_Q[V]$ when $\pi^\ast = \delta_{a^\ast}$. ✓
- $V(a^\ast) - \mathbb E_Q[V]$ — the AAD choice. ✓
- $\mathbb E_{\pi^\ast}[V - V_Q]$ — identical under deterministic $\pi^\ast$. ✓

All three collapse to the same quantity under the AAD scope; the distinction matters only for stochastic $\pi^\ast$ (outside scope; see §5).

## §3 — TV bound (deterministic $\pi^\ast$)

$$R(Q_{\Sigma_t}) \;=\; \sum_{a} Q_{\Sigma_t}(a) \cdot \Delta(a) \;\leq\; V_{\max} \cdot \sum_{a \neq a^\ast} Q_{\Sigma_t}(a) \;=\; V_{\max} \cdot (1 - Q_{\Sigma_t}(a^\ast))$$

For deterministic $\pi^\ast = \delta_{a^\ast}$, total variation computes to:

$$\operatorname{TV}(\pi^\ast, Q_{\Sigma_t}) \;=\; \tfrac{1}{2}\sum_a \lvert\pi^\ast(a) - Q_{\Sigma_t}(a)\rvert \;=\; 1 - Q_{\Sigma_t}(a^\ast)$$

(point-mass $\pi^\ast$ contributes $1 - Q_{\Sigma_t}(a^\ast)$ at $a^\ast$, and the off-mass contributes $\sum_{a \neq a^\ast} Q_{\Sigma_t}(a) = 1 - Q_{\Sigma_t}(a^\ast)$; dividing by 2 gives the same value).

Therefore:

*[Derived (tv-regret-bound, from bounded V and deterministic $\pi^\ast$)]*

$$\boxed{\;R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \operatorname{TV}(\pi^\ast, Q_{\Sigma_t})\;}$$

**Tightness.** The TV bound is tight: equality holds when $\Delta(a) = V_{\max}$ for all $a \neq a^\ast$ (degenerate value landscape). For typical value landscapes the bound is loose by a factor of $\mathbb E_{Q_{\Sigma_t}}[\Delta \mid a \neq a^\ast] / V_{\max}$, which depends on the value gaps and the strategy's mass distribution.

## §4 — KL bound (via Pinsker)

Pinsker's inequality: $\operatorname{TV}(P, Q) \leq \sqrt{\tfrac{1}{2} D_{\mathrm{KL}}(P \Vert Q)}$.

Applied with $P = \pi^\ast$ and $Q = Q_{\Sigma_t}$:

*[Derived (kl-regret-bound, from Pinsker + tv-regret-bound)]*

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \sqrt{\tfrac{1}{2}\, D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$$

Under deterministic $\pi^\ast$:

$$D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) \;=\; -\log Q_{\Sigma_t}(a^\ast) \;\in\; [0, +\infty)$$

**Finite and graded** whenever $Q_{\Sigma_t}(a^\ast) \gt 0$; diverges only in the limit $Q_{\Sigma_t}(a^\ast) \to 0$.

## §5 — The direction question (the load-bearing claim)

**Claim.** The KL direction with $\pi^\ast$ *first* is forced. Forward-KL $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ is **not a non-vacuous bound** on $R(Q_{\Sigma_t})$ under deterministic $\pi^\ast$.

**Argument.** $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast) = \sum_a Q_{\Sigma_t}(a) \log\bigl(Q_{\Sigma_t}(a)/\pi^\ast(a)\bigr)$. Under $\pi^\ast = \delta_{a^\ast}$, any $a \neq a^\ast$ has $\pi^\ast(a) = 0$ and $Q_{\Sigma_t}(a) \log(Q_{\Sigma_t}(a)/0) = +\infty$ unless $Q_{\Sigma_t}(a) = 0$. So forward-KL is $+\infty$ whenever $Q_{\Sigma_t}$ has any mass off $a^\ast$ — regardless of how small that mass is. A bound "$R \leq +\infty$" is vacuous.

This is the **same degeneracy** that the V-medium move was supposed to escape. Forward-KL cannot bound regret in the AAD scope. Reverse-KL (with $\pi^\ast$ first) can.

**Contrast with forward-KL's role elsewhere.** Forward-KL is natural for mode-covering inference ($Q$ covers $P$'s support) and variational inference when $Q$ is learned to match full $P$. Reverse-KL is natural for mode-seeking (concentrate $Q$ on $P$'s mode — exactly the strategy problem). The AAD scope is *mode-seeking by construction*: the strategy should concentrate on $a^\ast$. The direction alignment with the structural problem is not accidental.

## §6 — Uniqueness analysis (Outcome B)

The regret-bound argument forces the *direction* (reverse-KL) but admits a family of divergences:

| Divergence | Bound on $R$ | Tightness | Finite under det. $\pi^\ast$? | Gradient-tractable? |
|---|---|---|---|---|
| $\operatorname{TV}(\pi^\ast, Q)$ | $V_{\max} \cdot \operatorname{TV}$ | Tight (extremal $V$) | Yes | Non-differentiable |
| $D_{\mathrm{KL}}(\pi^\ast \Vert Q)$ (Pinsker) | $V_{\max}\sqrt{\tfrac{1}{2} D_{\mathrm{KL}}}$ | Loose by $\sqrt{\cdot}$ | Yes (finite when $Q(a^\ast)\gt 0$) | Yes |
| $D_{\mathrm{KL}}(\pi^\ast \Vert Q)$ (Bretagnolle-Huber) | $V_{\max}\sqrt{1 - e^{-D_{\mathrm{KL}}}}$ | Tighter than Pinsker for large $D_{\mathrm{KL}}$ | Yes | Yes |
| $\chi^2(\pi^\ast \Vert Q)$ (Le Cam) | $V_{\max}\cdot\tfrac{1}{2}\sqrt{\chi^2}$ | Looser than reverse-KL in typical regimes | Finite when $Q(a^\ast)\gt 0$; $\chi^2 = 1/Q(a^\ast) - 1$ | Yes |
| Rényi-$\alpha$ $D_\alpha(\pi^\ast \Vert Q)$, $\alpha \geq 1$ | Various | Interpolates KL ($\alpha \to 1$) and $\chi^2$ ($\alpha = 2$) | Finite for $\alpha \geq 1$ | Yes |
| $D_{\mathrm{KL}}(Q \Vert \pi^\ast)$ (forward) | $+\infty$ | Vacuous | **No** | — |

**What is uniquely forced.** The direction: $\pi^\ast$-first. This is a real derivation outcome — not a choice.

**What is a family.** Which specific divergence with $\pi^\ast$-first. Reverse-KL via Pinsker is *canonical* (not *unique*) for four reasons, each honestly weaker than a uniqueness theorem:

1. **Gradient-tractability.** TV is non-differentiable at mass boundaries; reverse-KL, $\chi^2$, and Rényi are smooth. This matters for operational minimization.
2. **Variational inference alignment.** Reverse-KL is the standard divergence in the variational-inference lineage (ELBO derivation uses reverse-KL). The V-medium move's rhetorical payoff — shared vocabulary with active inference — lives on reverse-KL specifically. BH-bound and $\chi^2$-bound, while also valid, would break the bridge to Friston et al. 2017 and Da Costa et al. 2020.
3. **Fisher geometry.** Reverse-KL's second-order expansion gives the Fisher information metric, which is the natural pull-back of a policy-manifold geometry. $\chi^2$ gives a different (Euclidean-like) metric; the Fisher metric is the canonical choice in information geometry (Amari & Nagaoka 2000).
4. **Information-budget interpretation.** $D_{\mathrm{KL}}(\pi^\ast \Vert Q)$ has a direct coding interpretation: the expected extra bits needed to code samples from $\pi^\ast$ using $Q$'s code. Under deterministic $\pi^\ast$, this is $-\log Q(a^\ast)$ — the expected bits to "name the optimal action" under $Q$'s distribution. This aligns with MDL framing of the segment.

**None of these is a uniqueness argument.** Each says reverse-KL is the canonical instance in a family. A uniqueness theorem would require showing the regret bound is tightest for reverse-KL among the family; the comparison in the table shows reverse-KL is *not* tightest (TV is; BH often beats Pinsker). The honest claim: reverse-KL is the canonical member of an admissible family, selected on gradient-tractability + variational-inference + information-geometry + MDL-interpretation grounds.

## §7 — Naturalizing $\beta_\Sigma$

From the Pinsker-reverse-KL bound:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max} \cdot \sqrt{\tfrac{1}{2}\, D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$$

Under this derivation, a cost trade-off that adds rate and regret:

$$\mathcal{L}(\Sigma_t) \;=\; \mathcal{R}(\Sigma_t) \;+\; \beta_\Sigma \cdot \sqrt{D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$$

would have $\beta_\Sigma = V_{\max}/\sqrt{2}$ if $\beta_\Sigma$ is to represent "cost per unit regret bound." This *does* derive a scale for $\beta_\Sigma$: $\beta_\Sigma \propto V_{\max}$.

**But the current segment uses a linear-in-KL form**, not a square-root-in-KL form. Under the linear form $\mathcal{L} = \mathcal{R} + \beta_\Sigma \cdot D_{\mathrm{KL}}$, the direct regret-bound interpretation does not give $\beta_\Sigma$ a uniform scale — it gives instead a *local* relationship $\partial R/\partial D_{\mathrm{KL}} = V_{\max}/(2\sqrt{2 D_{\mathrm{KL}}})$ that depends on the operating point.

**Options.**

(a) **Keep linear form; $\beta_\Sigma$ remains a free parameter** with regret-bound interpretation at *local* scale. Practical upside: consistency with IB linear-Lagrangian form in #disc-compression-operations. Downside: $\beta_\Sigma$ not naturalized globally.

(b) **Adopt square-root form in the segment.** Upside: global $\beta_\Sigma \propto V_{\max}$ naturalization; honest derivation. Downside: departs from the IB linear-Lagrangian shape, forfeiting the rate-distortion duality interpretation.

(c) **Report both.** Linear form as the operational IB instance (as currently in the segment); the square-root bound as the regret-bound derivation showing the direction is forced and indicating what scale $\beta_\Sigma$ would take in the tighter form.

Recommendation: **(c).** The direction-of-KL claim is the load-bearing finding; the exact functional form is a second-order choice that trades IB-shape alignment against regret-scale naturalization. Report both; keep the linear form in the segment's primary formulation; note the square-root regret-bound in Epistemic Status as the "source" derivation.

## §8 — Bound tightness and scope limits

**Where the regret bound is vacuous.**

1. $V_{\max} = \infty$ (unbounded value). Then the TV bound and all KL bounds are $\infty$. AAD's objective functional ( #form-objective-functional) is $\mathbb{R}$-valued; boundedness over the action set at a fixed state is a mild additional assumption but not automatic. Flag: "boundedness of $V$ over $\mathcal{A}$ at fixed $M_t$" must be stated.

2. $Q_{\Sigma_t}(a^\ast) = 0$ (strategy puts zero mass on optimum). Then reverse-KL = $\infty$. This is the "strategy cannot express the optimum" case — a structural failure, correctly flagged by infinite KL. The operational minimization would never select such a $\Sigma_t$. This degeneracy is *informative*, not pathological.

3. $\pi^\ast$ not deterministic (outside AAD canonical scope). Then reverse-KL may be infinite if $\pi^\ast$ has larger support than $Q_{\Sigma_t}$. For stochastic $\pi^\ast$ (e.g., under tied values), one would need a smoothing or an alternative form. Outside scope; flagged for future work.

**Where the bound is tight.** The TV bound is tight for extremal-$V$ cases; the Pinsker-KL bound is loose by $\sqrt{\cdot}$ in typical regimes. The Bretagnolle-Huber bound ($\sqrt{1 - e^{-D_{\mathrm{KL}}}}$) is tighter than Pinsker when $D_{\mathrm{KL}}$ is large. None of the KL bounds is *tightest* — TV itself wins — but the TV bound's non-differentiability is an operational strike. Reverse-KL is the tightest bound in the **smooth divergence** sub-family, among standard choices.

## §9 — References invoked

- Pinsker's inequality: Tsybakov 2009, *Introduction to Nonparametric Estimation* §2.4; or Cover & Thomas 2006 §11.6.
- Bretagnolle-Huber inequality: Bretagnolle & Huber 1978, *Estimation des densités*; Tsybakov 2009 §2.4.3.
- Donsker-Varadhan: Donsker & Varadhan 1975, "Asymptotic evaluation..." *Comm. Pure Appl. Math.*; used for potential sharpening but not in the core derivation.
- Information geometry: Amari & Nagaoka 2000, *Methods of Information Geometry*, AMS.
- Variational free energy (for alignment argument in §6): Friston et al. 2017; Da Costa et al. 2020 — already cited in segment.

## §10 — Outcome declaration

**Outcome B.** The regret-bound argument *forces the direction* (reverse-KL, $\pi^\ast$-first) — this is a genuine derivation result. The specific functional form within the admissible family (TV, reverse-KL, BH, $\chi^2$, Rényi-$\alpha$) is a selection among alternatives; reverse-KL is canonical on four grounds (gradient-tractability, variational-inference alignment, Fisher geometry, MDL-interpretation) but none of these is a uniqueness theorem.

**What this means for the segment.**

- The Epistemic Status on the relevance term moves from pure *formulation* to *formulation (strengthened): the KL direction is derived as an upper regret bound; the specific reverse-KL form is the canonical member of an admissible family of regret-bounding divergences*.
- The direction claim ($\pi^\ast$ first, not $Q_{\Sigma_t}$ first) is now defended on mathematical grounds, closing F20.
- $\beta_\Sigma$ gains a *local* regret-bound interpretation ($\partial R/\partial D_{\mathrm{KL}}$ under the linear form), not a global naturalization.

**What this does not mean.**

- Reverse-KL is *not* uniquely forced against TV, BH, or $\chi^2$. Selection among these is on operational grounds.
- $\beta_\Sigma$ is *not* fully naturalized — the linear-KL form is a formulation choice that loses the square-root scale.
- The bound is *not* tight in the smooth-divergence family; TV is tight but non-differentiable.

## §11 — Edits to make

1. **`01-aad-core/src/form-strategy-complexity-cost.md`** — update the variational-form paragraph with the regret-bound derivation; update Epistemic Status; change tag from `*[Formulation (strategy-IB-objective)]*` to `*[Formulation (strengthened-by-regret-bound)]*` on the relevance term; downgrade stage to `draft`.
2. **`01-aad-core/src/disc-compression-operations.md`** — add one paragraph to the "Variational form" subsection noting that the strategy-IB variational form's KL direction is forced by the regret bound; reverse-KL is canonical in the admissible family.
3. **`01-aad-core/src/disc-exploit-explore-deliberate.md`** — add one Discussion-level cross-reference noting the regret-bound interpretation connects exploit-regret to the strategy-cost objective via $\pi^\ast$-first KL.
4. **`01-aad-core/src/disc-ciy-unified-objective.md`** — add one Discussion sentence noting that AAD's exploit term $Q_O$ connects to the strategy-cost objective via the regret-bound derivation; this is what "value and information term" shares structurally with EFE without the preferences-as-priors commitment.
5. **`spikes/spike-active-inference-vs-aad.md`** §E.6 — update the implementation sketch to note the regret-bound derivation of the KL direction.

## Working Notes

- **Stochastic $\pi^\ast$ extension.** The canonical AAD scope has deterministic $\pi^\ast$. If $\pi^\ast$ has tied-value support (multiple optima), reverse-KL is finite as long as $Q_{\Sigma_t}$ covers the tied-optimum set; this is handled correctly by the regret-bound argument. If $\pi^\ast$ is stochastic for *non-degeneracy* reasons (softmax-smoothed with temperature $\beta$), a smoothed regret bound with $\mathbb E_{\pi^\ast}[V] - \mathbb E_{Q_{\Sigma_t}}[V]$ works directly; same KL direction forced.
- **Linear vs. square-root form.** The segment's current linear-in-KL form is the IB-shape instance (Lagrangian-dual of a constraint). Switching to square-root-in-KL would break the IB-shape-across-four-operations claim in #disc-compression-operations. Keep linear; report the regret-bound as motivation rather than functional-form derivation.
- **Comparison to standard RL regret bounds.** The argument here is the same structure as standard policy-optimization regret bounds (e.g., Agarwal, Kakade, Lee, Mahajan 2021 "On the theory of policy gradient methods" Lemma 3.2; Even-Dar, Kakade, Mansour 2009 "Online Markov decision processes"). AAD's contribution here is *re-using this standard bound as the derivation of the KL direction in the strategy-cost objective*, not inventing the bound.
- **AI literature cross-check.** Active inference's expected free energy also uses reverse-KL against a "preferred" distribution (in AI's preferences-as-priors framing, preferences *are* the reference). The direction alignment is convergent evidence; AAD derives it from the regret argument, AI from the variational free-energy argument, both arrive at reverse-KL. The convergence is worth noting but is not a uniqueness argument — it shows the direction is the *natural* one in both frames.
