# L3 — The identifiability-floor is the certificate boundary; Sylvester's law is the no-go

**Leg under test (00-brief L3).** Is M1 `#disc-identifiability-floor` *exactly* the boundary / rank-collapse of the L1 stability-certificate — and if so, is there a *named mechanism* for why no inner-product change escapes it? This is where the spike either finds the unifying truth or the sharp no-go. It finds **both, and they are the same statement.**

## The object L1 handed us

From `01-L1`: the unifying object is the equilibrium **certificate operator** $\mathcal M$ — the converse-Lyapunov metric, which in the statistical sub-case *is* the Fisher information $G$, in the Kalman case is $(P^-)^{-1}$, in the gradient case is the loss Hessian $\nabla^2 L$, in the Lyapunov-plant case is the plant Lyapunov metric. Operator-sector $\iff \mathcal M \succ 0$ on the scope ball — the **interior of the PSD cone** $\mathbb S^n_{\succ 0}$. The freedom AAD has is the *choice of $\mathcal M$* (the metric / coordinate); that is the only degree of freedom in "operator-sector in *some* inner product."

The candidate identification: **the identifiability-floor is $\partial\mathbb S^n_{\succeq 0}$ — the certificate dropping rank (a zero eigenvalue appears).** Test it against all four M1 instances; then ask whether the metric-freedom can ever escape the boundary.

## The no-go mechanism, stated first (then verified per instance)

> **Sylvester's law of inertia.** For any symmetric $\mathcal M$ and any invertible $S$, the congruence $S^\top \mathcal M S$ has the **same inertia** (numbers of positive, negative, zero eigenvalues) as $\mathcal M$ (Sylvester 1852; Horn & Johnson, *Matrix Analysis* 2nd ed., Thm 4.5.8).

Every "change of inner product / reparameterization" available to AAD acts on the certificate by congruence: reparameterizing the model $\theta\mapsto\varphi$ transforms Fisher information by $G_\varphi = S^\top G_\theta S$ with $S=\partial\theta/\partial\varphi$ invertible (Lehmann & Casella, *Theory of Point Estimation* 2nd ed., §2.5, Fisher-information reparameterization formula); changing the operator-sector metric $\mathcal M\mapsto T^\top\mathcal M T$ is a congruence by construction. **Therefore: if the certificate is rank-deficient in one admissible coordinate, it is rank-deficient in *every* admissible coordinate.** The metric-freedom — the *entire* degree of freedom that "operator-sector in some inner product" has, and the *entire* content of M3's coordinate-forcing — **cannot move a point off $\partial\mathbb S^n_{\succeq0}$**, because congruence preserves the kernel's dimension.

That is the spike's central finding. Operator-sector lives in the cone interior; the identifiability-floor *is* the cone boundary; and the boundary is **invariant under the only freedom either pattern has**. They are not "different axes" — they are the interior and the boundary of *one* object, held apart by an inertia invariant. Now verify the identification per M1 instance.

## Instance-by-instance verification

### M1-i — Cramér–Rao rank-1 (L1' unobservable common cause) — CLEAN

`#disc-identifiability-floor` Instance 2 (the L1' single-channel refutation, `#deriv-edge-credence-dynamics`): under an unobservable common cause, the Fisher information matrix for the edge parameters is **rank-1** (Fisher rank-deficiency). In the spine frame the Fisher information *is* the certificate $\mathcal M$ (statistical sub-case, `01-L1` and jacobian-b1 §6.2). Rank-1 Fisher $\iff \mathcal M$ has an $(n{-}1)$-dimensional kernel $\iff$ the point sits on $\partial\mathbb S^n_{\succeq0}$ with corank $n{-}1$. The Cramér–Rao bound (variance $\ge \mathcal M^{-1}$) is *literally* "the certificate must be invertible to bound the estimator"; on the floor $\mathcal M^{-1}$ does not exist along the kernel — unbounded variance, no consistent estimator. **And the irreducibility is exactly Sylvester:** the prior spike-finding-13 / spike-rho-factorization work showed "no reparameterization removes the rank-1 degeneracy" *by direct computation*; here that computation is recognized as a special case of Sylvester's law of inertia — congruence preserves the corank. **Status: exact (proved); the identification is tight and the no-go mechanism is named (Sylvester).**

### M1-ii — Bareinboim Causal Hierarchy Theorem (on-policy L0-insufficiency) — CLEAN, and it unifies the escape routes

`#disc-identifiability-floor` Instance 1 / `#der-causal-insufficiency-detection`: under purely on-policy execution no mechanism distinguishes L0-insufficient from L0-sufficient with matched regime conditionals (Bareinboim CHT). In the certificate frame: the relevant object is the information operator for the *causal* parameter under the *observational regime*. On-policy data carries no variation along the intervention coordinate, so the score has no component there — the causal-parameter block of the information operator is **rank-deficient by construction of the regime**. This is again $\mathcal M$ on $\partial\mathbb S^n_{\succeq0}$, the kernel being precisely the causal direction the CHT says is unidentified.

The payoff is the **escape routes unify**: `#der-loop-interventional-access`'s result (the feedback loop *generates* Level-2 data) is, in this frame, **rank-augmentation** — interventional data adds a new score component with support along the previously-null causal direction, so $\mathcal M \to \mathcal M + \Delta$ with $\Delta$ supported on the old kernel, lifting the point off the boundary into the interior. The no-go ("you cannot get there from observational data alone") is exactly **Sylvester again**: observational reparameterization is congruence, congruence preserves the kernel, so *within the observational regime* no coordinate choice identifies the causal parameter; only rank-augmentation (a genuinely larger data operator, not a reweighting) escapes. **This is a genuine unification: M1's "floor + named escape routes" structure = "$\partial$ of the cone + rank-augmentation is the only exit; reweighting (Sylvester) is not." Status: exact for the structural claim; the CHT itself is cited (Bareinboim et al. 2022), not re-derived.**

### M1-iii — Liberzon common-Lyapunov-nonexistence (composition floor) — CLEAN, and it is the L4 bridge

`#disc-identifiability-floor` Instance 3 (`spike-composition-no-go`, Liberzon 2003 + Dayawansa–Martin 1999): two subsystems with stable marginals but no common Lyapunov function; the composite can be unstable. In the certificate frame this is *literally* a certificate statement: each marginal has its own certificate $\mathcal M_1,\mathcal M_2 \succ0$ (each is in the interior, separately), but **no single $\mathcal M$ certifies the composite** — the composite's reachable certificate set fails to intersect the cone interior. The §3.3 closed-form counterexample (two coupled systems, identical marginal distributions, opposite composite-contraction sign) is exactly "two interior points whose composition lands on/over the boundary." **This is the certificate's non-preservation under composition — the same object as M1-i/ii, now at the composite layer — and it is precisely the L4 question (does the certificate survive projection/composition?). M1 and the composition no-go are the *same boundary* seen at agent vs. composite scope.** Status: exact for the identification; Liberzon/Dayawansa–Martin cited.

### M1-iv — Čencov (the forcing theorem) is the bridge between M1 and M3 — CLEAN

Čencov 1982 (Markov-invariant metric uniqueness) is M3's forcing theorem (jacobian-b1 §7.2 Angle 3: the *only* angle that clears the additive-coordinate-forcing uniqueness discipline, statistical scope). In the spine frame Čencov says: *when the certificate is forced, it is forced to be the Fisher information* — the very operator whose rank-collapse is M1-i. So M3 ("which $\mathcal M$ is forced") and M1 ("where the forced $\mathcal M$ degenerates") are **two facts about one operator**: Čencov forces $\mathcal M=$ Fisher (M3); Fisher rank-collapse is the floor (M1). They are not separate axes — they are "the certificate's identity" and "the certificate's boundary," and Čencov is what ties the identity to the very object whose boundary M1 names. **Status: exact for the structural bridge; Čencov cited.**

## The unifying truth and the sharp no-go are the same statement

Both completion targets are hit, and they coincide:

> **Unifying truth (succeed-at-claim, strong form).** AAD's cross-sectional structure is the geometry of *one* object — the equilibrium certificate operator $\mathcal M$ on the PSD cone $\mathbb S^n$:
> - **operator-sector** = $\mathcal M\succ0$ on the scope ball = cone *interior*;
> - **M2 separability** = the region where $\mathcal M\succ0$ (the certificate-exists scope; "where" the framework applies);
> - **M3 additive-coordinate-forcing** = *which* $\mathcal M$ — Čencov forces $\mathcal M=$ Fisher uniquely in statistical scope, matched elsewhere ("which coordinate");
> - **M1 identifiability-floor** = $\mathcal M\in\partial\mathbb S^n_{\succeq0}$ (rank-collapse); escape = rank-augmentation only ("what cannot be reached, and the only way out");
> - **composition** = whether a *common* $\mathcal M$ survives projection (Liberzon; the L4 Mori–Zwanzig residue is the certificate's projection-defect).
>
> The four meta-patterns are the **interior / scope-of-existence / forced-identity / boundary** of one cone, plus its **behaviour under projection**. This is exactly the M3-pattern self-description ("layer-specific manifestations of a single geometric object") raised to the whole framework.

> **Sharp no-go (the load-bearing core).** Operator-sector and the identifiability-floor are **provably not unifiable into a single interior statement, and the obstruction is named: Sylvester's law of inertia.** The entire freedom of "operator-sector in *some* inner product" and the entire content of M3 coordinate-forcing act on $\mathcal M$ by *congruence*; congruence preserves inertia; therefore a rank-deficient certificate is rank-deficient in **every** admissible coordinate. The floor is the cone boundary; the metric-freedom is a congruence orbit; **congruence orbits do not cross $\partial\mathbb S^n_{\succeq0}$.** You cannot reweight off the floor — you can only rank-augment (add genuinely new information: interventional data, a side channel, a witness), which is *not* a metric change. This is *why* M1 is a distinct, irreducible meta-pattern and not a corner of operator-sector: not "they are different concerns" (the soft answer) but "they are the interior and boundary of one cone, separated by an inertia invariant that is exactly the framework's only degree of freedom" (the sharp answer).

This *sharpens* the C1 predecessor's honest-but-soft "the identifiability-floor structure is orthogonal to operator-sector." It is not orthogonal — it is the **boundary** of the very cone operator-sector is the interior of, and the orthogonality intuition was the shadow of the inertia invariant. "Orthogonal axes" → "interior vs. boundary of one cone, held apart by Sylvester." That is the revealing no-go Joseph asked the spike to push to.

## Epistemic status ledger

| Claim | Tier |
|---|---|
| Operator-sector (one-point, in some metric) ⟺ Hurwitz certificate exists (L1-lin) | Exact (proved; Lyapunov theorem) |
| Certificate = Fisher (statistical) / $(P^-)^{-1}$ (Kalman) / Hessian (gradient) / Lyapunov-metric (plant) | Exact in each sub-case (cited: jacobian-b1 §6.2; standard) |
| M1-i Cramér–Rao rank-1 = certificate corank ≥1; irreducibility = Sylvester | Exact (proved; Sylvester's law) |
| M1-ii Bareinboim CHT = causal-block rank-deficiency under observational regime; escape = rank-augmentation; reweighting-no-go = Sylvester | Exact for structural identification; CHT cited not re-derived |
| M1-iii Liberzon = no common certificate under composition (the L4 bridge) | Exact for identification; Liberzon/D–M cited |
| M1-iv Čencov ties M3's forced identity to the very operator M1's boundary names | Exact for the bridge; Čencov cited |
| Four meta-patterns = interior / scope / forced-identity / boundary + projection-behaviour of one cone | Derived (robust-qualitative): the identification is exact per-instance; "all of AAD" is the synthesis claim and is as strong as the four instances jointly |
| Sylvester's law is the named obstruction to unifying M1 into operator-sector | Exact (proved) — **the spike's load-bearing no-go** |

## Open seam handed to L4

M1-iii (Liberzon) already showed the composition floor *is* the certificate's non-preservation under composition. L4 must close: is the Mori–Zwanzig memory kernel $Q_\Lambda U P_\Lambda$ exactly the certificate's *projection*-defect — i.e., is "projected dynamics not Hurwitz though micro is" the same boundary, seen under $\Lambda$? If yes, the integrability triad closes: **non-gradient residue (Helmholtz, dynamics side) ≅ rank-deficiency (Sylvester, identifiability side) ≅ memory kernel (Mori–Zwanzig, composition side)** — three faces of one failure-of-integrability, and the operator-family meta-segment is the spine that names it.
