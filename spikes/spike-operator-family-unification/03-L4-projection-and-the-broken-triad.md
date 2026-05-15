# L4 — Projection, the certificate's two defects, and the broken integrability triad

**Leg under test (00-brief L4 + the synthesis hypothesis).** Does the certificate survive projection? Is the Mori–Zwanzig memory kernel the certificate's projection-defect? And — the seductive one — do **Helmholtz (non-gradient residue) ≅ Sylvester (rank-deficiency) ≅ Mori–Zwanzig (memory kernel)** coincide as "three faces of one failure-of-integrability," making the operator-family meta-segment a single spine?

The brief flagged the triad as *hypothesis, to be verified not asserted*. **Verification breaks it.** That break is the honest load-bearing result of this leg, and it is stronger than the triad would have been.

## The projection setup

Micro-dynamics $\dot x=-Jx$, $A=-J$ Hurwitz, certificate $\mathcal M\succ0$ with $\mathcal M J+J^\top\mathcal M = Q\succ0$ (L1). Idempotent projection $P=P^2$ onto the resolved/macro subspace, $\mathcal Q=I-P$. Partition in a basis adapted to $P$ (block 1 = resolved, block 2 = eliminated):

$$\mathcal M=\begin{pmatrix}\mathcal M_{11}&\mathcal M_{12}\\\mathcal M_{21}&\mathcal M_{22}\end{pmatrix}\succ0,\qquad J=\begin{pmatrix}J_{11}&J_{12}\\J_{21}&J_{22}\end{pmatrix}.$$

The C1 predecessor parked Λ as "not an endomorphism, doesn't fit." In the certificate frame the right object is **not** the surjection onto the quotient but the idempotent $P$ on the full space — an endomorphism. So the C1 category problem dissolves *at the certificate level*. The question becomes sharp: does $\mathcal M$, and the dynamic guarantee it gives, survive restriction to $\operatorname{range}P$?

## Two distinct things were being conflated; separate them

**(a) The certificate-as-metric survives projection — Schur, PD-preserving.** The natural restricted metric is the Schur complement $\widehat{\mathcal M}=\mathcal M/\mathcal M_{22}=\mathcal M_{11}-\mathcal M_{12}\mathcal M_{22}^{-1}\mathcal M_{21}$. Since $\mathcal M\succ0$, its Schur complement is $\succ0$ (Horn & Johnson, *Matrix Analysis* 2nd ed., Thm 7.7.7 / Boyd–Vandenberghe §A.5.5). **So a positive-definite certificate, restricted to the resolved subspace, is still positive-definite. The static object survives projection unconditionally.**

**(b) The *dynamic certification* does NOT survive — and the defect is the Mori–Zwanzig memory term, a Schur/commutator quantity.** The exact reduced dynamics for $Px$ is **not** the Markov truncation $\dot{x}_{\rm res}=-P J P\,x_{\rm res}$; by Mori–Zwanzig (Mori 1965; Zwanzig 1961; Chorin–Hald–Kupferman 2002) it carries a memory convolution with kernel built from the orthogonal propagator $e^{-\mathcal Q J \mathcal Q\,t}$ and a noise term. The question "does $\widehat{\mathcal M}$ certify the *closed macro-flow*?" requires the Lyapunov relation for the **effective** generator, not the truncated one. Writing the truncated relation:

$$\widehat{\mathcal M}\,(PJP)+(PJP)^\top\widehat{\mathcal M}\;=\;\underbrace{(\text{compression of }Q)}_{\succ0\ \text{part}}\;-\;\underbrace{\mathcal C}_{\text{memory/commutator defect}},$$

where $\mathcal C$ is exactly the bilinear contribution of the eliminated-block coupling $J_{12},J_{21}$ through the orthogonal dynamics — the static (zero-lag) part of the MZ memory kernel. The micro relation $\mathcal M J+J^\top\mathcal M=Q\succ0$ does **not** imply the truncated relation is $\succ0$, precisely because $\mathcal C\neq0$ whenever $P$ is not $J$-invariant ($J_{21}\neq0$ or $J_{12}\neq0$). This recovers, in the certificate frame, the prior `spike-mori-zwanzig-composition` result: the **zero-lag kernel bound $\varepsilon^\ast\ge\lVert\mathcal Q_\Lambda U P_\Lambda\rVert_{\rm op}$ closes** (it is $\lVert\mathcal C\rVert$), while the **trajectory bound $\varepsilon^\ast\ge C\lVert K\rVert$ does not** (per-step vs. accumulation type mismatch — exactly the gap between the static $\mathcal C$ and the full memory convolution).

> **L4 result (proved/structural).** The certificate has **two separable defects under projection**: the *metric* survives as a PD form (Schur complement, unconditional), but the *dynamic guarantee* degrades by the Mori–Zwanzig memory commutator $\mathcal C$, and $\varepsilon^\ast = \lVert\mathcal C\rVert$ (zero-lag) is the closure defect. $\varepsilon^\ast=0$ iff $P$ is $J$-invariant (the eliminated subspace does not feed back) — the exact composition-closure condition. **The composition floor (Liberzon, L3 M1-iii) is this same defect read as "no common certificate": two interior certificates whose projection-coupled composite has $\mathcal C$ large enough to push the truncated relation out of $\succ0$.**

## The triad is broken — and that is the finding

The brief's hypothesis: Helmholtz (dynamics) ≅ Sylvester (identifiability) ≅ Mori–Zwanzig (composition), one failure-of-integrability. Verify each pairwise identity:

- **Helmholtz vs. the floor.** A non-gradient field ($J=DF(0)$ non-symmetric ⟹ no potential $\Phi$) is the Helmholtz/Hodge obstruction. **But L1 proved a non-symmetric Hurwitz $J$ still has a Lyapunov certificate $\mathcal M\succ0$ — it is *not* on the floor.** So the non-gradient residue does **not** cause loss of the certificate. Helmholtz is therefore **not** a face of M1. It is a face of **M3** — it is exactly *why* the certificate is "matched, not forced" outside the potential cases (jacobian-b1 §6.4/§7.3): non-symmetry ⟹ no $\Phi$ ⟹ Čencov/(SOC) cannot force the metric ⟹ Lyapunov-existence (converse-Lyapunov) is all you get. Helmholtz lives on the *forcing* axis, not the *existence* axis. **Identity 1 of the triad: FALSE.**
- **Sylvester vs. Mori–Zwanzig.** Sylvester's law (L3): congruence preserves inertia; metric-freedom cannot cross $\partial\mathbb S^n_{\succeq0}$ — an **invertible**-transformation invariant. The MZ defect (this file): projection $P$ is **non-invertible** (rank $P<n$); the defect is a Schur-complement *plus memory-commutator* quantity, not an inertia statement (indeed the Schur complement of PD is PD — inertia is *not* what fails; the *dynamic* relation is). Sylvester is about what the **metric freedom** cannot do; Mori–Zwanzig is about what **dimension reduction** does. Different group acting (congruence $GL_n$ vs. idempotent projection), different invariant (inertia vs. $J$-invariance of $\operatorname{range}P$). **Identity 2 of the triad: FALSE.**

So the seductive "one integrability obstruction, three faces" is **not true**. The honest structure:

> **The single object is real (the certificate cone $\mathbb S^n$); the failures are irreducibly three distinct, named theorems:**
> - **M3 / forcing failure = Helmholtz–Hodge:** the field is non-gradient ⟹ no potential ⟹ the certificate is matched (converse-Lyapunov existence), not forced (Čencov). Invariant: symmetry of $DF$.
> - **M1 / existence failure = Sylvester's law of inertia:** the certificate drops rank; congruence (the entire metric-freedom) preserves the kernel ⟹ no coordinate escapes the floor; only rank-augmentation (new information) exits. Invariant: inertia under $GL_n$ congruence.
> - **Composition failure = Mori–Zwanzig / Schur:** projection preserves the metric (Schur, PD) but not the dynamic guarantee; $\varepsilon^\ast=\lVert\mathcal C\rVert$, zero iff $\operatorname{range}P$ is $J$-invariant. Invariant: $J$-invariance of the resolved subspace under non-invertible $P$.
>
> Each obstruction is invariant under the *others'* degrees of freedom (metric change doesn't fix non-invariance; projection doesn't fix non-symmetry; rank-augmentation doesn't fix a memory kernel). **That mutual invariance is the proof that the three are irreducible — they cannot be folded into one mechanism.**

## Why the broken triad is the stronger result

Had the triad held, the operator-family meta-segment would be a single spine — elegant but, on the evidence, false. The verified structure is more useful to every future agent: it says **do not attempt to unify M1, composition-closure, and M3-forcing into one obstruction** — they are Sylvester, Mori–Zwanzig/Schur, and Helmholtz respectively, and the proof of their distinctness is that each is invariant under the others' freedoms. The unification that *is* real — one certificate cone with interior (operator-sector), boundary (M1), forced-vs-matched identity (M3), scope-of-existence (M2), and a projection-defect (composition) — is exactly **completion-state 2 (succeed-at-claim), not state 1**. The spike reached a true unification at the object level and a *plural, sharply-named* no-go at the failure level. The plurality is the content: it is why AAD has four meta-patterns and not one, stated as a theorem rather than an intuition.

## Epistemic status ledger (this leg)

| Claim | Tier |
|---|---|
| Certificate-as-metric survives projection (Schur complement of PD is PD) | Exact (proved; Horn–Johnson Thm 7.7.7) |
| Dynamic certification degrades by the MZ memory commutator $\mathcal C$; $\varepsilon^\ast=\lVert\mathcal C\rVert$ zero-lag; $=0$ iff $\operatorname{range}P$ is $J$-invariant | Derived (structural; recovers prior `spike-mori-zwanzig-composition` zero-lag-closes / trajectory-doesn't result in the certificate frame) |
| Composition floor (Liberzon, L3 M1-iii) = this defect read as "no common certificate" | Derived (robust-qualitative; identification exact, Liberzon cited) |
| Triad identity Helmholtz ≅ Sylvester: **FALSE** (non-symmetric Hurwitz has a certificate; L1) | Exact (proved by the L1 counterexample) |
| Triad identity Sylvester ≅ Mori–Zwanzig: **FALSE** (congruence/$GL_n$-invariant vs. non-invertible-projection-invariant; Schur of PD is PD so inertia is not what fails) | Exact (proved; different group, different invariant) |
| The three failures are irreducible (each invariant under the others' freedoms) | Derived (robust-qualitative; the per-pair invariance is exact, the "exactly three" is the synthesis claim) |
