# §1 cluster — L5 fifth-facet test

*Tests the synthesis's L5 claim (line 93): the strict-vs-loss boundary as the structurally distinct sub-facet of the Interior — refining `#disc-stability-certificate`'s four-facet structure into something like five-facet, with the strict-loss boundary landing in the spine itself. Test: applies the spine's own "new facet or new object?" criterion (line 84 of disc-stability-certificate) to the candidate.*

## The spine's own test

From `disc-stability-certificate.md` line 84 (verbatim):

> The recurring *accumulation-type confound* — asking about a per-step residue in the vocabulary of its accumulation, which dissolved the $\varepsilon^\ast(N)$ poly-vs-exponential question and recurred across the framework — run through this segment's own test ("is a candidate organizing pattern a new facet, or a genuinely new object?") returns **neither**: it is a new *reading* of an existing facet (the temporal/representation dual of the Interior), so the cone gains no sixth facet and the framework no fifth independent meta-segment.

So the spine has already worked one case through this test (the accumulation-typing pattern) and returned **neither** — a new *reading*, not a new facet. The test asks: does the candidate (here: the strict-vs-loss split) introduce a structurally new piece of the cone, or is it a re-reading of an existing facet?

## The candidate restated

Per §02 of this spike, the Interior facet of `#disc-stability-certificate` decomposes into:
- **R0-strict sub-region**: $\mathcal M \succ 0$ with $\kappa \gt 0$, the standard contraction case
- **R0-loss sub-region**: $\mathcal M \succ 0$ with $\kappa = 0$, the marginal-stability/conservative case (chain-recurrent / Hamiltonian / lossless)
- **strict/loss boundary**: the subset of the cone where the supremum-$\kappa$ transitions from positive to zero

The synthesis's L5 candidate is the **boundary** between strict and loss as a fifth facet — peer to the four established facets (Interior, Scope of existence, Forced identity, Boundary, Projection behaviour).

## Three tests for facet-status

I'll apply three tests to gauge whether this is a facet or a sub-region:

### Test (i) — Structural invariance under the framework's representational freedom

Each of the four established facets has an invariance property under the framework's representational freedom (coordinate / metric change):

- **Interior** (R0-strict region): invariant under congruence ($\mathcal M \succ 0$ stays $\succ 0$).
- **Boundary M1** (rank-deficient $\mathcal M$): invariant under congruence (Sylvester's law of inertia).
- **Scope-of-existence M2**: invariant under the agent's representational restriction (the separability pattern is structural, not metric-dependent).
- **Forced-identity M3**: characterized by the *failure* of an invariance (when Helmholtz fails, the certificate is matched not forced).
- **Projection behaviour**: invariant under coarse-graining algebra (Schur complement).

What about the strict/loss boundary? It is the locus where the supremum-$\kappa$ over admissible $\mathcal M$ transitions from $\gt 0$ to $= 0$. **Is this invariant under congruence?**

Yes — under a congruence $\mathcal M \mapsto P^\top \mathcal M P$, the inequality $\mathcal M J + J^\top \mathcal M \succeq 2\kappa \mathcal M$ transforms to $(P^\top \mathcal M P) J + J^\top (P^\top \mathcal M P) \succeq 2\kappa (P^\top \mathcal M P)$ which, after pre/post-multiplication by $P^{-T}$ and $P^{-1}$, is the same inequality on the transformed Jacobian $\tilde J = P^{-1} J P$ with the same $\kappa$. So $\sup \kappa$ is invariant under congruence — and the strict/loss boundary is therefore the locus of *Jacobians* (modulo congruence) with $\sup \kappa = 0$, which is a congruence-invariant condition.

But — the four established facets are facets of the *cone of certificates* (PSD cone in $\mathbb S^n$), with the dynamics' $J$ as a parameter. The strict/loss boundary is naturally read as a property of the *Jacobian* (whether $J$'s spectrum is on the imaginary axis or strictly in the open left half plane), with the certificate $\mathcal M$ as a witness. This is a different *type* of object than the existing facets — the existing facets parametrize regions of the PSD cone for fixed dynamics; the strict/loss boundary parametrizes regions of dynamics for which certificates exist.

**Test (i) verdict: ambiguous.** The strict/loss boundary is congruence-invariant (a good sign for facet-status), but lives on the *Jacobian-side* of the cone structure, while the established facets live on the *certificate-side*. This is a mismatch.

### Test (ii) — Failure mode plurality

The three established failure modes (M1, M2, M3 — Sylvester / separability / Helmholtz) are *mutually invariant* (line 62 of `disc-stability-certificate.md`): "Each obstruction is untouched by the others' freedoms: a metric change does not fix non-invariance; projection does not fix non-symmetry; rank-augmentation does not fix a memory kernel."

Does the strict/loss boundary survive this mutual-invariance test against M1/M2/M3?

- **Vs M1 (Sylvester rank-collapse):** the strict/loss boundary has $\mathcal M \succ 0$; M1 has $\mathcal M$ rank-deficient. These are disjoint (Result 1 Case (iii) vs M1 boundary). Not invariant — but **disjoint** (a stronger separation).
- **Vs M2 (Scope of existence):** strict/loss is interior to the certificate cone; M2 is about whether the cone has any certificate at all. Disjoint via different mechanism.
- **Vs M3 (Forced identity):** strict/loss is about *rate* ($\kappa$); M3 is about *which $\mathcal M$*. These are **orthogonal coordinates**: an agent can be R0-strict with matched-not-forced $\mathcal M$ (e.g., linear-Hurwitz non-symmetric — the running example in `#result-certificate-existence`); an agent can be R0-loss with $\mathcal M$ forced ($\mathcal M = I$ on antisymmetric $J$ is canonical). The strict/loss split and the forced/matched split are independent. **Mutually orthogonal.**

So the strict/loss split satisfies the mutual-invariance test against M3 (orthogonality) and is disjoint from M1/M2 (no overlap). This is a *good* sign for facet-status — it doesn't collapse to an existing facet.

**Test (ii) verdict: positive for facet-status.** The strict/loss split is genuinely distinct from M1/M2/M3.

### Test (iii) — Constructive-impossibility-posture instance

`#disc-constructive-impossibility-posture` establishes the five-instance pattern for the M1 boundary (per `#disc-stability-certificate` line 82, M1 is the boundary facet that grounds the constructive-impossibility posture). If the strict/loss boundary is a peer facet, it should support its own constructive-impossibility-posture instance: name the floor, name the unique broadly-available escape, treat the no-go as load-bearing apparatus.

**Constructive-impossibility-posture instance for R0-loss:**

- **The floor.** The R0-loss boundary $\kappa = 0$: agents whose linearization is purely imaginary-eigenvalue (semisimple) cannot achieve $\kappa \gt 0$ on any positive-definite metric. Equivalently: agents whose Jacobian has $S \equiv 0$ in the Helmholtz decomposition (Hamiltonian games per Letcher 2019) cannot be strictly contracting under any quadratic Lyapunov function. The agent cannot leave the chain-recurrent component of its dynamics by any pure choice of representation.
- **The unique broadly-available escape.** **Symplectic Gradient Adjustment** (SGA, Letcher 2019 §3) — augment the agent's update with $\lambda A^\top \xi$ so the modified dynamics gains a strict-positive symmetric part. This is the only widely-applicable method in the literature for projecting an R0-loss agent onto the R0-strict regime; it works because $A^\top \xi = \nabla \mathcal H$ for the Hamiltonian $\mathcal H = \tfrac{1}{2}\Vert\xi\Vert^2$, and gradient descent on $\mathcal H$ strictly decreases it. Alternative paths exist (changing the agent class entirely; adding external dissipation) but SGA is the unique pure-algorithmic broadly-available escape per the cluster literature.
- **The no-go as load-bearing apparatus.** Without R0-loss as a named regime, the "Hamiltonian agent cannot contract" no-go has no place to live in AAT — it would be a property of specific examples (zero-sum games, matching pennies) rather than a structural fact. Naming R0-loss makes the no-go citable: any agent whose dynamics live in the chain-recurrent set of its linearization cannot achieve persistence-as-exponential-decay; it can only achieve persistence-as-bounded-recurrence. SGA-style augmentation becomes the unique structurally-named escape; without it, the agent is stuck at R0-loss permanently.

**Test (iii) verdict: positive for facet-status, with a worked constructive-impossibility-posture instance.** The strict/loss boundary supports the full pattern: floor + unique escape + structural no-go. It is not just a sub-region of the Interior — it admits the same constructive-impossibility-posture treatment that grounds M1's facet-status.

## Synthesis of the three tests

Test (i): ambiguous — congruence-invariant but lives on the Jacobian side, not the cone side.

Test (ii): positive — orthogonal to M3, disjoint from M1/M2.

Test (iii): positive — supports a full constructive-impossibility-posture instance (R0-loss floor + SGA-as-unique-escape + structural no-go).

**Net verdict on L5: the strict/loss split is *structurally facet-worthy*, but its placement is more subtle than a peer fifth facet.** Test (i)'s mismatch matters: the four established facets parametrize regions of the certificate cone for fixed dynamics; the strict/loss split parametrizes regions of *dynamics* for which certificates exist with given rate. These are dual perspectives.

## The cleanest version of L5

The cleanest version of L5 is **not** to add a fifth peer facet to the four, but to recognize that the **Interior facet has a 2-component structural decomposition** that lifts it from a featureless cone-interior into the Helmholtz-decomposed pair (R0-strict / R0-loss). The L5 candidate becomes:

> **Refinement of the Interior facet of `#disc-stability-certificate`.** The Interior is not a single region of the cone; it is the *Helmholtz-decomposed* region where the certificate inequality holds in $\succeq$ form. The Helmholtz decomposition of the linearized certificate's Hermitian part $\mathcal M J + J^\top \mathcal M = 2(S_\mathcal M + A_\mathcal M)\mathcal M$ (with $S_\mathcal M$ symmetric, $A_\mathcal M$ antisymmetric in the $\mathcal M$-inner-product) gives two natural sub-regions:
>
> - **R0-strict** — $S_\mathcal M \succ 0$ dominates; the certificate strictly contracts; AAT's current Interior.
> - **R0-loss** — $S_\mathcal M = 0$ (pure $A_\mathcal M$); the certificate is conserved; the chain-recurrent sub-region per Conley 1978, the Hamiltonian-game regime per Letcher 2019, the lossless-passivity regime per CPT 2021.
>
> Together, R0-strict ∪ R0-loss = certificate-cone Interior, with their *boundary* (the surface where $\kappa$ transitions from positive to zero) being the surface where strict-passivity transitions to lossless-passivity in CPT's vocabulary. Each sub-region admits its own constructive-impossibility-posture instance: R0-strict's is the M1 boundary (rank-collapse no-go, observability-augmentation escape); R0-loss's is the SGA no-go (Hamiltonian-game no-contraction floor, SGA-as-symplectic-augmentation escape).

This is a **refinement-of-an-existing-facet**, not a new facet — answering the spine's own "new facet or new object?" test with **a new internal structure on an existing facet**, which matches the form of the spine's prior worked-example answer (the accumulation-typing pattern, which returned the same form: new reading of an existing facet rather than a new facet).

## Comparison with the spine's accumulation-typing precedent

The spine's accumulation-typing answer (`disc-stability-certificate.md` line 84) was:

> *neither — a new reading of an existing facet (the temporal/representation dual of the Interior)*

The analogous R0-loss answer would be:

> *a 2-component internal structure on an existing facet — the Helmholtz decomposition of the Interior*

Both refine the Interior facet, in different ways. The accumulation-typing read it through the *temporal* axis; the Helmholtz/R0-loss read it through the *spectral* axis ($S$-vs-$A$). The two readings are **compatible** — they refine different coordinates of the same facet.

## What the spine gains from L5-as-Interior-refinement

1. The Interior facet's table row in `disc-stability-certificate.md` line 42–48 expands: not just "$\mathcal M \succ 0$ on the scope ball: the contraction holds" but "$\mathcal M \succ 0$ with Helmholtz $S+A$ decomposition: $S \succ 0$ gives R0-strict (contraction); $S = 0$ gives R0-loss (conservation/recurrence)".
2. The strength-ladder in `#result-certificate-existence` adds R0-loss at the bottom (weakest rung).
3. Conley 1978 + Letcher 2019 + CPT 2021 + Candogan 2010 + Omidshafiei 2019 + Papadimitriou-Piliouras 2018 + Balduzzi 2018 become a coordinated citation cluster for the R0-loss sub-region, with each contributing one verified-prior-art piece.
4. The spine's own line 70 honest-edge ("Whether exactly three obstructions exhaust the failure modes is not proved") is **not** modified by this — R0-loss is not a failure mode; it is a non-failing-but-non-contracting interior sub-region. The three obstructions (M1/M2/M3) remain the failure modes; the spine's plurality-of-obstructions analysis is preserved.

## What L5 does NOT do

- It does not displace the four established facets.
- It does not add a fifth peer facet.
- It does not modify the three-obstruction failure-mode analysis.
- It does not force `#disc-stability-certificate`'s OUTLINE preamble change.

It refines the Interior facet's internal structure, which is a smaller-commitment landing than the synthesis's L5 framing (which suggested a fifth facet of peer status) but is also more *honest to the spine's own test*: the new structure is genuinely on an existing facet rather than being a new facet alongside.

## L5 verdict

**L5 partially justified — at the refinement-of-Interior-facet form, not at the new-fifth-facet form.** The strict/loss split is structurally significant (passes tests (ii) and (iii) of facet-status), but it sits *inside* the Interior facet as a Helmholtz $S/A$ decomposition of the cone interior, rather than alongside the four facets as a new peer.

The cleanest landing:
1. In `#result-certificate-existence`: add R0-loss to the strength ladder (per §02).
2. In `#disc-stability-certificate`: refine the Interior facet row of the four-facet table to name the $S/A$ decomposition, add a Discussion paragraph naming R0-strict / R0-loss as the two sub-regions, cite Conley/Letcher/CPT.
3. The four-facet structure stays four. The honesty-edge on line 70 stays unmodified. The accumulation-typing precedent at line 84 gains a parallel Helmholtz-typing paragraph.

Joseph's call on whether to write up the Helmholtz refinement as a Discussion paragraph inside `#disc-stability-certificate` *or* as its own small `disc-helmholtz-interior` segment is a presentational question (a single segment cross-references many facets; a new segment carries more weight but creates more cross-link maintenance). My recommendation given the spine's own precedent: keep the refinement as Discussion inside `#disc-stability-certificate`, matching how the accumulation-typing precedent was handled.
