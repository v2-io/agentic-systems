# §1 cluster — R0-loss derivation (strengthen-first attempt #1)

*Strengthen-first pass on the R0-loss claim from `01-cluster-synthesis.md`. The synthesis proposed R0-loss as a structurally distinct rung in `#result-certificate-existence`'s certificate-strength ladder, characterized by $\mathcal M \succ 0$ with $\kappa = 0$. The conservative move is recognition-tier landing. This file attempts the proof that R0-loss is a genuinely distinct rung — and surfaces what does and does not survive AAT-internally.*

## Setup: the AAT-internal frame

Carry over AAT's `#result-certificate-existence` setup: agent error dynamics $\dot e = -F(e)$ near equilibrium $e^\ast$, $F(e^\ast)=0$, Jacobian $J = DF(e^\ast)$. At the linearized level the dynamics are $\dot e = -Je$ (with $A := -J$). A **stability certificate** is $\mathcal M \succ 0$ symmetric with
$$\mathcal M J + J^\top \mathcal M \succeq 2\kappa \mathcal M.\tag{C}$$

The current R0 rung packs **two conditions** into one: existence of $\mathcal M \succ 0$ *and* $\kappa \gt 0$. The synthesis's R0-loss proposal isolates the second by allowing $\kappa = 0$. The question this file tests: does that isolation pick out a structurally distinct dynamic regime, or does it collapse to either R0-strict (degenerate boundary case) or to the M1 identifiability floor (rank collapse)?

## Result 1 (structural distinctness): R0-loss is neither R0-strict nor M1

**Claim (R0-loss-distinctness).** The conditions "$\exists \mathcal M\succ 0: \mathcal M J + J^\top \mathcal M \succeq 0$ with the supremum-$\kappa$ achieving zero" and "$\exists \mathcal M\succ 0, \kappa \gt 0: \mathcal M J + J^\top \mathcal M \succeq 2\kappa \mathcal M$" (R0-strict) and "no certificate exists ($\mathcal M$ would have to drop rank)" (the M1 boundary) are **three mutually exclusive AND collectively exhaustive partitions of the certificate-cone Interior boundary** for linear systems $A = -J \in \mathbb R^{n\times n}$.

**Proof.** Recall the Lyapunov equation $A^\top \mathcal M + \mathcal M A = -Q$ (clause 3 of `#result-certificate-existence`). The complete classification of $A$ by spectral location of its eigenvalues:

- **Case (i): $A$ Hurwitz.** Every eigenvalue has $\mathrm{Re}\lambda \lt 0$. For every $Q \succ 0$ a unique $\mathcal M \succ 0$ solves the Lyapunov equation; the certificate exists with strict $\kappa \gt 0$ as derived in `#result-certificate-existence`. This is **R0-strict**.
- **Case (ii): $A$ has an eigenvalue with $\mathrm{Re}\lambda \gt 0$.** Then no $\mathcal M \succ 0$ can satisfy $\mathcal M J + J^\top \mathcal M \succeq 0$ at all: if such $\mathcal M$ existed, the same Lyapunov-function argument as in the (2 ⟹ 1) derivation of `#result-certificate-existence` would force $\dot V \le 0$ along all trajectories, contradicting the existence of an unstable mode. **No certificate exists** — this is the "no R0" regime entirely outside the ladder.
- **Case (iii): $A$ has all eigenvalues with $\mathrm{Re}\lambda \le 0$, at least one with $\mathrm{Re}\lambda = 0$, and the eigenvalues on the imaginary axis are semisimple (their algebraic multiplicity equals their geometric multiplicity).** Then a positive-definite $\mathcal M$ exists satisfying $\mathcal M J + J^\top \mathcal M \succeq 0$ but $\kappa = 0$ is the supremum. The dynamics are **Lyapunov-stable but not asymptotically stable**: trajectories starting in any $\mathcal M$-ball stay in that ball forever; trajectories on the imaginary-axis modes orbit perpetually. This is **R0-loss**.
- **Case (iv): $A$ has all eigenvalues with $\mathrm{Re}\lambda \le 0$, at least one with $\mathrm{Re}\lambda = 0$, and at least one imaginary-axis eigenvalue is *not* semisimple** (i.e., a Jordan block of size $\ge 2$ at an imaginary eigenvalue). Then no $\mathcal M \succ 0$ satisfies $\mathcal M J + J^\top \mathcal M \succeq 0$: the non-semisimple Jordan block produces polynomially-growing modes ($e \sim t \cdot v$ along the generalized eigenvector), which would violate $\dot V \le 0$ for any quadratic $V$. **No certificate exists** — this is part of the M1 boundary in the sense that the certificate's existence fails, though the underlying mechanism (Jordan-block defect) differs from Fisher-rank-collapse.

The four-case partition is exhaustive (every real matrix sits in exactly one) and mutually exclusive. R0-loss occupies a strict slice — Case (iii) — that is disjoint from R0-strict (Case (i)) and from no-certificate regimes (Cases (ii), (iv)). $\square$

**Reading.** R0-loss is **not** "R0-strict with $\kappa$ tending to zero" — it is the marginal-stability regime that R0-strict cannot reach (R0-strict's $\kappa \gt 0$ is strict by *definition*; the limit $\kappa \to 0^+$ from inside R0-strict does not land in R0-loss but on its closure boundary). R0-loss is **not** the M1 boundary either: M1 (per `#disc-identifiability-floor`) is about $\mathcal M$ becoming rank-deficient (a Sylvester-inertia-preserved boundary of the PSD cone of certificates); R0-loss has $\mathcal M$ remaining $\succ 0$, with the rank drop happening on a different object — the *Hermitian part* $\mathcal M J + J^\top \mathcal M$, which is allowed to touch $0$ in some directions while $\mathcal M$ itself stays interior. The two are distinct facets that happen to abut at the *combined* boundary where both $\mathcal M$ drops rank *and* $\mathcal M J + J^\top \mathcal M$ does — but R0-loss as a regime is genuinely interior to the certificate cone.

**Status.** *Exact* for linear systems on $\mathbb R^n$. The semisimple-imaginary-eigenvalues condition is the standard center-manifold prerequisite for marginal stability; see e.g. Khalil *Nonlinear Systems* 3rd ed., Theorem 4.5.

## Result 2 (Helmholtz characterization): pure R0-loss linearization is purely $A$-component

This connects the synthesis's "Helmholtz $S+A$" claim (from Letcher 2019 Lemma 1) to the R0-loss derivation, AAT-internally rather than as analogy. **A scope-honesty distinction is required**: "pure R0-loss" (the linearization is conservative on the *entire* state space) is sharper than "general R0-loss" (the chain-recurrent set is *some* invariant subspace, with strict contraction on the complementary subspace).

**Claim (Helmholtz-pure-R0-loss).** For a linear system $\dot e = -J e$ with $\mathcal M = I$, the conditions

(i) $J$ admits the certificate $\mathcal M = I$ with supremum-$\kappa = 0$, and the marginal-stability regime (Case (iii)) is "full": every eigenvalue of $-J$ is on the imaginary axis (semisimple), so the chain-recurrent set is all of $\mathbb R^n$;

(ii) the symmetric part $S := \tfrac{1}{2}(J + J^\top)$ vanishes: $S \equiv 0$, equivalently $J$ is purely antisymmetric;

(iii) $V(e) = \tfrac{1}{2}\Vert e\Vert^2$ is *exactly* conserved along trajectories of $\dot e = -J e$ for all initial $e$

are **equivalent**.

**Proof.** (ii ⟹ iii). $\dot V = e^\top \dot e = -e^\top J e = -\tfrac{1}{2} e^\top (J + J^\top) e = -e^\top S e$. If $S = 0$, $\dot V \equiv 0$, so $V$ is conserved. (iii ⟹ ii). $\dot V \equiv 0$ for all $e$ ⟹ $e^\top S e \equiv 0$ for all $e$, which (by polarization for symmetric $S$) forces $S \equiv 0$. (ii ⟹ i). With $\mathcal M = I$ and $S = 0$: $\mathcal M J + J^\top \mathcal M = J + J^\top = 2S = 0$, so the certificate inequality holds with $\kappa = 0$ exactly, no $\kappa \gt 0$ is attainable, and *every* eigenvalue of $J$ (hence $-J$) is purely imaginary (antisymmetric real matrices have purely imaginary spectrum, and are diagonalizable over $\mathbb C$ — hence semisimple). (i ⟹ ii). $S$ is symmetric PSD (because $\mathcal M J + J^\top \mathcal M = 2S \succeq 0$ at $\mathcal M = I$). The "full" Case (iii) hypothesis says every eigenvalue of $-J$ is on the imaginary axis. The skew-Hermitian decomposition $-J = -S + (-A_{\mathrm{anti}})$ where $A_{\mathrm{anti}} = (J - J^\top)/2$ shows that $-J$'s real part (in the matrix-decomposition sense, equal to $-S$) controls the *real* parts of its eigenvalues via the Bendixson localization theorem: $\mathrm{Re}(\lambda(-J)) \in [\lambda_{\min}(-S), \lambda_{\max}(-S)] = [-\lambda_{\max}(S), -\lambda_{\min}(S)]$. For all eigenvalues to have $\mathrm{Re} = 0$, we need $\lambda_{\max}(S) = \lambda_{\min}(S) = 0$, i.e., $S = 0$. $\square$

**Reading.** Letcher 2019's Lemma 1 ($J = S + A$ uniquely with $S$ symmetric, $A$ antisymmetric) and Definition 2 (Hamiltonian game = $S \equiv 0$, $J = A$ purely antisymmetric) are *exactly* the AAT-internal characterization of **pure** R0-loss in the Euclidean metric ($\mathcal M = I$). The "Hamiltonian game" of Letcher is the *fully* R0-loss agent in AAT vocabulary. The "potential game" of Letcher (Definition 2, $A \equiv 0$, $J = S$) is the *fully* R0-strict-with-gradient-flow case in AAT vocabulary — which sits inside R0-strict but is the strictly-narrower potential-flow sub-case (R0-strict admits non-gradient flows too: a Hurwitz $J$ with $J + J^\top \succ 0$ but $J \neq J^\top$, e.g., the *spiral* contraction in 2D).

**The mixed case** (general R0-loss). When $S \succeq 0$ but $S \neq 0$ and $S$ has nontrivial kernel, the dynamics splits: along $\ker(S)$ the dynamics is conservative ($V$ unchanged); along $S$'s positive-eigenspace the dynamics strictly contracts. This corresponds to Conley's *partial* decomposition: the chain-recurrent set is a proper invariant subspace (the $\ker(S)$-direction's orbit), the complement is strongly-gradient-like, and the agent overall is in a *mixed* R0-strict-plus-R0-loss state. The supremum-$\kappa = 0$ because of the conservative subspace; the asymptotic dynamics converge to the conservative subspace and then cycle there forever. This mixed case is exactly what Conley's Fundamental Theorem (1978 §8.1) constructs: the strongly-gradient-like quotient flow + the chain-recurrent subflow, both present in the same dynamics, decomposed canonically.

**Status.** *Exact* for the linear/linearized setting with $\mathcal M = I$, **pure R0-loss case**. The general-$\mathcal M$ version replaces "$S = 0$" with "the $\mathcal M$-symmetric part of $J$ vanishes," where the $\mathcal M$-symmetric part is $S_\mathcal M := \tfrac{1}{2}\mathcal M^{-1}(\mathcal M J + J^\top \mathcal M)$ and the $\mathcal M$-antisymmetric part is $A_\mathcal M := \tfrac{1}{2}\mathcal M^{-1}(\mathcal M J - J^\top \mathcal M)$. The decomposition $J = S_\mathcal M + A_\mathcal M$ is unique and reduces to the standard Helmholtz at $\mathcal M = I$. Joseph's note (Letcher Lemma 1 is "preserved by *orthogonal* change-of-coordinates") is the $\mathcal M = I$ case; for general $\mathcal M$ the preserving group is the $\mathcal M$-orthogonal group, and the decomposition is canonical relative to that group rather than to the Euclidean inner product.

**Scope honesty.** Letcher's Lemma 1 is the unconditional algebraic fact that *any* matrix decomposes as symmetric + antisymmetric. The AAT-internal content above is the *equivalence* of $S = 0$ with full-state marginal stability in the Lyapunov inequality at $\kappa = 0$ — that is the work this result does. The mixed case (partial $S$) is **not** Hamiltonian in Letcher's sense; it is the proper mixture covered by Conley's universal decomposition. The "Helmholtz" name is appropriate (it is the matrix-level shadow of the vector-calculus Helmholtz decomposition into gradient + curl-free parts), but the AAT-internal claim does not require importing the vector-calculus theorem — it follows from the matrix-symmetric/antisymmetric split plus the standard Lyapunov derivative computation plus Bendixson's spectral-localization theorem.

## Result 3 (Conley anchoring): R0-loss agents have chain-recurrent linearizations

This connects the synthesis's "Conley chain-recurrent decomposition" claim (from Conley 1978 §8.1) to the R0-loss derivation, AAT-internally.

**Claim (Conley-R0-loss).** A linear flow $\dot e = -J e$ on a compact invariant set $K \subset \mathbb R^n$ (e.g., $K$ a level set $\{V(e) \le c\}$ of the conserved $V$) is **chain recurrent on $K$** (in Conley's sense; chain-recurrent set $= K$) if and only if $J$ is purely antisymmetric — i.e., the dynamics are in R0-loss with $\mathcal M = I$.

**Proof sketch.** (⟸) If $J$ is purely antisymmetric, $V = \tfrac{1}{2}\Vert e\Vert^2$ is conserved (Result 2.iii). The flow restricted to each level set $\{V = c\}$ (a sphere $S^{n-1}_{\sqrt{2c}}$) is volume-preserving by Liouville's formula ($\mathrm{tr}(-J) = 0$ for antisymmetric $J$) on the level set. On a compact manifold, every volume-preserving flow is chain recurrent (this is essentially Poincaré recurrence — every point is recurrent in the chain sense). Hence the chain-recurrent set on $K$ is all of $K$. (⟹) If $K$ equals the chain-recurrent set and $K$ contains a nontrivial neighborhood of $e^\ast$, then there can be no Lyapunov function strictly decreasing on any open subset of $K$ (else the points there would not be chain-recurrent — they would flow toward the strict decrease). So no $V$ with $\dot V \lt 0$ on a neighborhood exists, which forces $\dot V \equiv 0$ in any candidate quadratic Lyapunov function, which by Result 2 forces $S = 0$. $\square$

**Reading.** Conley 1978's Fundamental Theorem (every flow on a compact space decomposes uniquely into a chain-recurrent subflow + strongly-gradient-like quotient — §8.1, statement) is the *universal* version of the same R0-strict-vs-R0-loss decomposition AAT has been carrying instance-by-instance. Conley's chain-recurrent set is the R0-loss region of the dynamics; the strongly-gradient-like quotient is the R0-strict region. The decomposition is **always available** on compact spaces and is unique. This is the universality the synthesis flagged: R0-strict and R0-loss are not two arbitrary regimes picked out for AAT's convenience — they are the two pieces of Conley's universal decomposition, AAT-localized at the linearization.

The Omidshafiei 2019 Theorem 2.4.11 ("every flow on a compact metric space has a complete Lyapunov function") restates the same universality. The complete Lyapunov function is the AAT-internal certificate, strictly decreasing on the R0-strict region (Conley's "outside the chain-recurrent set") and constant on each R0-loss component (Conley's "chain components"). This is the same object AAT calls $V(e) = e^\top \mathcal M e$ — restricted to the chain-recurrent component, $V$ is constant ($\dot V = 0$ on that component) which is exactly $\kappa = 0$ there.

**Status.** *Exact* for linear flows on compact invariant sets, conditional on Liouville's formula for divergence-free flows + Poincaré recurrence (Theorem 18 in CPT 2021, classical). The compactness condition is essential — without it (e.g., a half-line of equilibria escaping to infinity), chain recurrence can fail in degenerate ways. AAT's natural compact-invariant-set choice is the level set of the certificate, which exists exactly when the certificate is bounded-level-set (a standard auxiliary condition).

## Result 4 (CPT bridge): a finitely-lossless agent has R0-loss-class storage geometry

This is where the synthesis's bridge from CPT 2021's lossless passivity to AAT's R0-loss needs to be carefully drawn — and where the conservative half of the analysis lives.

**The state-space mismatch.** CPT 2021's storage function $L(\mathbf{q})$ acts on **cumulative payoffs** $\mathbf{q}$, not on **errors** $e = x - x^\ast$ in the strategy space. The CPT FTRL dynamic is

$$\dot{\mathbf{q}} = \mathbf{p}, \qquad \mathbf{x} = f(\mathbf{q}) = \nabla h^\ast(\mathbf{q})$$

with state $\mathbf{q}$ and storage $L(\mathbf{q}) = h^\ast(\mathbf{q}) - \langle \mathbf{q}, \mathbf{x}^\ast \rangle + h(\mathbf{x}^\ast)$. This $L$ is convex (it is a convex conjugate plus an affine term) and bounded below by zero (CPT Theorem 7 proof) — but it is **not** a positive-definite quadratic in $\mathbf{q} - \mathbf{q}^\ast$. There is no AAT-style metric $\mathcal M$ such that $L(\mathbf{q}) = (\mathbf{q} - \mathbf{q}^\ast)^\top \mathcal M (\mathbf{q} - \mathbf{q}^\ast)$; for the replicator dynamic specifically, $L$ is the (shifted) KL divergence between $\mathbf{x}^\ast$ and $\nabla h^\ast(\mathbf{q})$, which is convex but not quadratic.

**What the bridge gives.** At the AAT-natural state — error in **strategy space**, $e = \mathbf{x} - \mathbf{x}^\ast$, linearized about the Nash $\mathbf{x}^\ast$ — the dynamics of FTRL+game become $\dot e = J_{\mathrm{eff}} e + (\text{nonlinear})$ for some effective Jacobian $J_{\mathrm{eff}}$. The CPT result Theorem 19 says the *joint* DGS (learning operator + game operator) is finitely lossless, hence Poincaré recurrent. Translating to the linearization at $\mathbf{x}^\ast$: the joint Jacobian $J_{\mathrm{eff}}$ has eigenvalues on the imaginary axis (else the trajectory would either decay or grow, contradicting recurrence). By Result 1 Case (iii), this is precisely R0-loss.

**The bridge claim, AAT-internal version.** A DGS satisfying CPT's hypotheses (convex-combination FTRL coupled with a graphical-constant-sum game with fully-mixed Nash) has its linearization at the Nash equilibrium in the R0-loss regime (Case (iii) of Result 1): all eigenvalues of $J_{\mathrm{eff}}$ have $\mathrm{Re}\lambda = 0$ and are semisimple.

**Where this falls short of a strengthening of the synthesis.** The synthesis claimed CPT's storage function $L$ is "structurally identical to" AAT's Lyapunov $V = e^\top \mathcal M e$. **This is false as a sharp claim.** What is true is *weaker but still substantive*: the *existence* of any conserved (or non-increasing) bounded-below function $L$ along the joint dynamics implies marginal stability of the linearization at any equilibrium it accumulates near, which is R0-loss in AAT vocabulary. The specific *form* of $L$ — quadratic in $e$ for AAT, convex-conjugate of regularizer for FTRL — differs. The connection is at the *qualitative* level of "an agent with a finitely-passive storage function has R0-loss linearization at Nash," not at the *quantitative* level of "the storage function is the certificate."

This is the **strengthening shape that survives**: instead of $L = V$ as claimed in the synthesis, the relationship is "$L$ bounded-below + nonincreasing ⟹ $J_{\mathrm{eff}}$ has Case-(iii) spectrum ⟹ R0-loss." The two storage functions live on different state spaces; their *informational content* about the linearization at equilibrium agrees.

**Status.** *Exact at the linearization* for the qualitative bridge ("finitely-lossless ⟹ R0-loss linearization at any accumulation equilibrium"). *Refuted as stated in the synthesis* for the quantitative bridge ($L$ as $V$ at the certificate level). The corrected version is honest and still useful — but the synthesis's claim (3) under "Mechanics" ("AAT's one-point sector condition ... is structurally identical to CPT's passivity inequality") needs to be downgraded to the qualitative-bridge form.

## Result 5 (composition behaviour): R0-loss × R0-loss is R0-loss, but R0-loss × R0-strict is R0-strict

This tests the **closure question** the synthesis flagged for L5: what happens when we compose certificate regimes?

**Claim (composition table).** For two independent linear subsystems $\dot e_1 = -J_1 e_1$, $\dot e_2 = -J_2 e_2$ with joint state $e = (e_1, e_2)$ and joint Jacobian $J = \mathrm{diag}(J_1, J_2)$:

| $J_1$ regime | $J_2$ regime | Joint regime |
|---|---|---|
| R0-strict | R0-strict | R0-strict |
| R0-strict | R0-loss | R0-strict-projected-out, R0-loss on the surviving $e_2$ axis |
| R0-loss | R0-loss | R0-loss |
| R0-strict | (no certificate) | (no certificate) |
| R0-loss | (no certificate) | (no certificate) |

**Proof sketch.** Take $\mathcal M = \mathrm{diag}(\mathcal M_1, \mathcal M_2)$. Then $\mathcal M J + J^\top \mathcal M = \mathrm{diag}(\mathcal M_1 J_1 + J_1^\top \mathcal M_1,\; \mathcal M_2 J_2 + J_2^\top \mathcal M_2)$. The block-diagonal Hermitian-part is $\succeq 0$ iff each block is, and the supremum-$\kappa$ for the joint is $\min(\kappa_1, \kappa_2)$. Hence:
- strict + strict ⟹ joint $\kappa = \min(\kappa_1, \kappa_2) \gt 0$ ⟹ R0-strict;
- strict + loss ⟹ joint $\kappa = 0$ (the loss component drags it down), but the surviving strict component is still contracting; the joint regime is R0-loss in the union sense — the loss subspace is invariant and conservative, the strict subspace decays exponentially toward equilibrium *within* the loss subspace's level set;
- loss + loss ⟹ joint $\kappa = 0$ with conservative dynamics on both, R0-loss;
- no-certificate + anything ⟹ the joint Jacobian has a Case-(ii) or Case-(iv) eigenvalue ⟹ no joint certificate.

**Reading.** R0-strict is **not** closed under decoupled composition in the sense that adding an R0-loss component to an R0-strict agent gives R0-loss in the joint regime. This matters for AAT's `#form-composition-closure`: composing a contracting agent with a marginally-stable agent (even with no interaction) gives a marginally-stable composite. The contraction guarantee survives only on the contracting subspace; the joint persistence claim drops to ultimate-boundedness on the loss subspace's level set.

For *coupled* composition the analysis becomes harder: CPT Theorem 19 (the synthesis's central CPT result) says that FIC of two lossless operators is lossless via $L_1 + L_2$ — i.e., R0-loss × R0-loss is R0-loss under feedback-interconnection. But the question of whether R0-strict × R0-loss under FIC is R0-strict (the strict factor "wins") or R0-loss (the loss factor "wins") is **not** answered by the synthesis or by CPT — and the answer depends on the interconnection structure. CPT Theorem 2 (Fox-Shamma) covers passive + passive (both possibly strict, possibly lossless) → passive, but the *rate* depends on the coupling.

**Where this leaves the closure question.** R0-loss has well-defined closure behaviour for the **decoupled** case (table above) but the **coupled** case requires the passivity-composition machinery of CPT/Fox-Shamma and is regime-dependent. R0-loss is **not** an absorbing state in general (strict + loss can stay strict if the coupling channel is designed to dissipate the loss component — this is essentially what SGA does, per Letcher 2019: it projects out the antisymmetric component).

**Status.** *Exact* for decoupled composition. *Open* for general coupled composition; partial under CPT-style passivity machinery imported wholesale.

## What survives, what doesn't (strengthen-first verdict for pass #1)

**Result 1 (structural distinctness):** exact, AAT-internal, lands at R0-loss as a genuinely distinct rung — the marginal-stability slice of the certificate cone interior that R0-strict cannot reach by limit and that M1 (rank collapse of $\mathcal M$) is disjoint from.

**Result 2 (Helmholtz characterization):** exact, AAT-internal, makes Letcher's $S=0$ Hamiltonian-game characterization the exact AAT-linearization image of R0-loss.

**Result 3 (Conley anchoring):** exact (modulo standard compactness), AAT-internal, identifies R0-loss with the chain-recurrent component of Conley's Fundamental-Theorem decomposition. This is the universality the synthesis wanted: R0-strict + R0-loss are not invented categories — they are Conley's two pieces of the universal flow decomposition, at AAT's linearization.

**Result 4 (CPT bridge):** *partial.* The qualitative bridge ("finitely-lossless storage ⟹ R0-loss linearization") is exact. The quantitative bridge claimed in the synthesis ("CPT's $L$ is AAT's certificate $V$") is **refuted** at sharp form: the two storage functions live on different state spaces and have different functional forms; only the qualitative content carries over. **This is the soft-landing the synthesis would have committed to had we not done this pass — and it is correctly weaker than the synthesis claimed.**

**Result 5 (composition):** *partial.* Decoupled composition table is exact; coupled composition requires CPT/Fox-Shamma passivity-composition imported wholesale and the rate depends on the interconnection.

## Where R0-loss can land at `status: exact`

Results 1+2+3 jointly land R0-loss as an **exact rung** in `#result-certificate-existence`'s ladder under the precise statement:

> **R0-loss (exact, linearized).** For an agent with linearization $\dot e = -J e$ on $\mathbb R^n$, a stability certificate $\mathcal M \succ 0$ exists with $\mathcal M J + J^\top \mathcal M \succeq 0$ and supremum-$\kappa = 0$ if and only if every eigenvalue of $-J$ has nonpositive real part, at least one has zero real part, and the imaginary-axis eigenvalues are semisimple (no defective Jordan blocks). The dynamics in this regime are Lyapunov-stable but not asymptotically stable, with $V(e) = e^\top \mathcal M e$ conserved on the imaginary-axis-eigenvector subspace. In the **pure** sub-case $\mathcal M = I$ and *all* eigenvalues of $-J$ on the imaginary axis, the regime coincides exactly with $J$ being antisymmetric (Letcher 2019 Lemma 1, Definition 2), and the dynamics restricted to each level set of $V$ are chain-recurrent in Conley's sense (Conley 1978 §8.1). The **mixed** sub-case (some imaginary eigenvalues + some strict-stable ones) corresponds to Conley's universal decomposition into a chain-recurrent subflow (on the imaginary-eigenspace) and a strongly-gradient-like quotient (on the strict-stable complement).

**Strength ladder, extended:**

| Rung | Condition | Equivalent to | Certificate is |
|---|---|---|---|
| **R0-loss** | $\mathcal M J + J^\top \mathcal M \succeq 0$, $\sup \kappa = 0$, some $\mathcal M\succ 0$ | $A=-J$ has imaginary-axis spectrum (semisimple); other eigenvalues if any are strict-stable | conserved on the chain-recurrent subspace + strict-Lyapunov on its strongly-gradient-like complement |
| R0-strict | (C), $\kappa \gt 0$, some $\mathcal M$, local | $A=-J$ Hurwitz + remainder dominated | converse-Lyapunov $\mathcal M$ |
| R1 | incremental (two-point) $\mathcal M$-strong-monotonicity on $\mathcal B_R$ | global $\mathcal M$-strong-monotone (cocoercive class) | curvature-like $\mathcal M$ (potential sub-case) |
| R2 | R1 with $\mathcal M$ forced by uniqueness | natural-gradient in Čencov-unique Fisher | Fisher metric |

The ordering is now **R0-loss ⟸ R0-strict ⟸ R1 ⟸ R2**, with R0-loss the *weakest* rung (existence of certificate without asymptotic decay) and R0-strict adding the contraction rate. The L0-rung in the synthesis's "Possibility ladder" naming should be read as "no rung at all" — the no-certificate regime where the agent is not even Lyapunov-stable.

## What this does NOT do

- Does not lift `#der-adversarial-destabilization`'s Effects-Spiral from discussion-grade. That is strengthen-first pass #2, in `03-effects-spiral-attempt.md`.
- Does not resolve the L4/L5 questions of cross-row unification or fifth-facet status. Those go in `04-fifth-facet-test.md` and `05-cross-row-check.md`.
- Does not modify any canonical segment in `01-aat-core/src/`. The math here lives in the spike; the segment-level landing plan is in `99-verdict.md`.
- The derivation is at the **linearized level** throughout, matching `#result-certificate-existence`'s scope. The nonlinear / center-manifold extension (whether nonlinear dynamics with Case-(iii) linearization are actually Lyapunov-stable as opposed to having quartic-or-higher instabilities on the center manifold) is the standard nonlinear-stability open question (Khalil §4.3); not in AAT's claim and not in this derivation either.
