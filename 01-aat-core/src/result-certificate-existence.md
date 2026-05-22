---
slug: result-certificate-existence
type: result
status: exact
depends:
  - deriv-sector-condition
  - result-sector-persistence-template
stage: draft
---

# Result: Certificate Existence — Operator-Sector in Some Metric Is Exponential Stability

The framework's central anchoring identity: **a stability certificate exists for an agent exactly when the agent is exponentially stable about its target**, at the linearized level. The organizing slogan — *an adaptive system is an operator whose contraction rate exceeds its target's drift rate* — is *not a heuristic* but this equivalence (the standard Lyapunov theorem), with the certificate $\mathcal{M}$ as its witness.

A **stability certificate** is a symmetric positive-definite metric $\mathcal{M}$ for which AAT's one-point sector condition holds in the $\mathcal{M}$-inner-product on a ball around the equilibrium. At the linearized level, the existence of such a certificate is *equivalent* to the system matrix being Hurwitz (exponentially stable) by the Lyapunov equation — three clauses, all the same statement: $A=-J$ Hurwitz; some $(\mathcal{M},\kappa)$ with $\mathcal{M}J + J^\top\mathcal{M} \succeq 2\kappa\mathcal{M}$; for every $Q\succ 0$ a unique $\mathcal{M}$ solving $A^\top\mathcal{M} + \mathcal{M}A = -Q$. The certificate is *not unique*: it is whatever positive-definite metric makes the dynamics contract. The result holds at the linearized level (with a standard second-order remainder condition for the local nonlinear extension); the global statement requires the incremental rung R1 (cocoercive class) — a genuine scope statement, named here so the parenthetical "linearized/local" is not buried.

The result *specializes* in different sub-cases of the framework to four familiar metrics: Fisher information for Bayesian agents (Čencov-forced under R2); inverse-prior-covariance for Kalman agents; loss Hessian for gradient agents; plant-selected Lyapunov metric for linear-Hurwitz or PID agents. *These are not four separate stories — they are one object under four certificates*. The unification is structural: the same Lyapunov equivalence underlies all four, with the specialization determined by the agent class. The framework treats this segment as the **spine** of three meta-patterns: separability ( `#disc-separability-pattern` — *scope-of-existence* of a certificate), additive coordinate forcing ( `#disc-additive-coordinate-forcing` — when the certificate is *forced* to a unique form), and identifiability floors ( `#disc-identifiability-floor` — where the certificate's *boundary* lives via the Sylvester mechanism). Naming $\mathcal M$ as the object — rather than $V(e) = e^\top \mathcal M e$, the Lyapunov function — is what makes those downstream statements expressible.

## Formal Expression

### The object

*[Definition (stability-certificate)]*

For an agent with error dynamics $\dot e=-F(e)$ about an equilibrium $e^\ast$ ($F(e^\ast)=0$, $F\in C^1$ near $e^\ast$, Jacobian $J:=DF(e^\ast)$), a **stability certificate** is a symmetric positive-definite $\mathcal M$ for which the one-point sector condition holds in the $\mathcal M$-inner-product on a ball $\mathcal B_R(e^\ast)$:

$$\langle F(e),\,e-e^\ast\rangle_{\mathcal M}\;\ge\;\kappa\,\lVert e-e^\ast\rVert_{\mathcal M}^2,\qquad \kappa\gt0. \tag{C}$$

The certificate is not unique: it is whatever positive-definite form makes the dynamics contract. In the recurring sub-cases it specializes — to the Fisher information for Bayesian agents, to $(P^-)^{-1}$ for Kalman agents, to the loss Hessian for gradient agents, and to a plant-selected Lyapunov metric for linear-Hurwitz or PID agents. These are not four separate stories; they are one object under four certificates.

### The equivalence

*[Result (certificate-existence), exact at the linearized level]*

At the linearized level (C) reads $\mathcal M J+J^\top\mathcal M\succeq 2\kappa\mathcal M\succ0$, a strict Lyapunov inequality for the system matrix $A=-J$. The following are equivalent:

1. $A=-J$ is Hurwitz — the linearized error dynamics $\dot e=-Je$ is exponentially stable;
2. there exist $\mathcal M\succ0$ and $\kappa\gt0$ with $\mathcal M J+J^\top\mathcal M\succeq2\kappa\mathcal M$ — a one-point sector condition (a stability certificate) in *some* inner product;
3. for every $Q\succ0$ there exists a unique $\mathcal M\succ0$ with $\mathcal M J+J^\top\mathcal M=Q$.

So "operator-sector in *some* inner product" and "the equilibrium is exponentially stable" are **the same statement**, with the certificate $\mathcal M$ as the converse-Lyapunov witness — an equivalence, not an analogy.

### The certificate-strength ladder

*[Derived (ordering of conditions; exact)]*

The certificate admits four strictly-ordered strengths, all on the one object:

| Rung | Condition | Equivalent to | Certificate is |
|---|---|---|---|
| **R0-loss** | some $\mathcal M\succ 0$, $\mathcal M J + J^\top \mathcal M \succeq 0$, $\sup\kappa = 0$ | $A=-J$ has only nonpositive-real-part eigenvalues, at least one on the imaginary axis (semisimple) | conserved on the chain-recurrent subspace + strict-Lyapunov on its strongly-gradient-like complement |
| **R0-strict** | one-point (C), some $\mathcal M$ with $\kappa\gt 0$, local | $A=-J$ Hurwitz + remainder dominated | converse-Lyapunov $\mathcal M$ (exists; generally not forced) |
| R1 | incremental (two-point) $\mathcal M$-strong-monotonicity on $\mathcal B_R$ | global $\mathcal M$-strong-monotone (cocoercive class) | curvature-like $\mathcal M$ (potential sub-case) |
| R2 | R1 with $\mathcal M$ *forced* by a uniqueness theorem on an AAT-internal axiom | natural-gradient in the Čencov-unique Fisher metric | Fisher metric (Čencov-forced) |

R0-loss ⟸ R0-strict ⟸ R1 ⟸ R2 strictly. R0-loss is the *widest* rung — a certificate exists but $\sup\kappa = 0$: the dynamics is Lyapunov-stable, not asymptotically stable, with $V(e)=e^\top\mathcal M e$ conserved on an imaginary-axis-eigenvector subspace and strict contraction on its strongly-gradient-like complement (Conley's universal decomposition; pure-case Helmholtz $S/A$ characterization derived below). R0-strict is the contraction rung with $\kappa\gt 0$ strict, reaching the plant-Lyapunov cases (linear-Hurwitz-non-symmetric, PID) where no potential exists. R1 is the cocoercive/proximal class where a variational structure is available; R2 is the uniqueness-theorem-forced statistical case. The widest rung is not a weakness: it is exactly the reach the narrower rungs cannot give. (R0-loss's pure-case characterization and Conley anchoring are in the Derivation below; R2's forcing is established in #disc-additive-coordinate-forcing; R1's cocoercive class in #result-contraction-template.)

## Derivation

**(1 ⟹ 3, 2).** $A=-J$ Hurwitz. By the Lyapunov theorem (Lyapunov 1892; Khalil, *Nonlinear Systems* 3rd ed., Thm 4.6), for every $Q\succ0$ the equation $A^\top\mathcal M+\mathcal M A=-Q$ has a unique solution $\mathcal M\succ0$. Substituting $A=-J$ gives $\mathcal M J+J^\top\mathcal M=Q\succ0$ (clause 3). For the rate: $Q\succeq\lambda_{\min}(Q)\,I\succeq\dfrac{\lambda_{\min}(Q)}{\lambda_{\max}(\mathcal M)}\,\mathcal M$, so (C) holds at the linear level with $\kappa=\dfrac{\lambda_{\min}(Q)}{2\,\lambda_{\max}(\mathcal M)}\gt0$ (clause 2).

**(2 ⟹ 1).** Suppose $\mathcal M\succ0$, $\kappa\gt0$, $\mathcal M J+J^\top\mathcal M\succeq2\kappa\mathcal M$. Take $V(e)=e^\top\mathcal M e$ (valid Lyapunov candidate, $\mathcal M\succ0$). Along $\dot e=-Je$: $\dot V=-e^\top(\mathcal M J+J^\top\mathcal M)e\le-2\kappa\,e^\top\mathcal M e=-2\kappa V\lt0$ for $e\neq0$. Hence $\lVert e(t)\rVert_{\mathcal M}\le e^{-\kappa t}\lVert e(0)\rVert_{\mathcal M}$ and $A=-J$ is Hurwitz.

**(3 ⟺ 2)** is the rate-extraction argument (3 gives 2 with the displayed $\kappa$; 2 is the special case $Q=\mathcal M J+J^\top\mathcal M$).

**Local nonlinear extension.** With $F(e)=Je+r(e)$, $\lVert r(e)\rVert=o(\lVert e\rVert)$, (C) holds on $\mathcal B_R(e^\ast)$ iff the linearization is exponentially stable *and* the second-order remainder is dominated on the ball ($\lVert r(e)\rVert_{\mathcal M}\le c\lVert e\rVert_{\mathcal M}^2$ with $cR\lt\kappa$). This is the standard Lyapunov indirect method (Khalil Thm 4.7); the remainder-domination radius is exactly the contraction-template Tier-2 degradation radius ( #result-contraction-template), not new machinery.

### R0-loss: certificate without contraction

*[Derived (R0-loss-distinctness; exact at the linearized level for the pure case, exact-via-Conley for the mixed case)]*

When $A=-J$ is non-Hurwitz but admits *some* $\mathcal M\succ 0$ with $\mathcal M J + J^\top \mathcal M \succeq 0$ at $\sup\kappa = 0$, the Lyapunov inequality holds non-strictly and the dynamics is Lyapunov-stable but not asymptotically stable. The complete spectral classification of $A$ partitions the linear-system space into four cases:

- **(i) $A$ Hurwitz** — R0-strict (above).
- **(ii) $A$ has an eigenvalue with $\mathrm{Re}\lambda\gt 0$** — no certificate exists: a $\mathcal M\succ 0$ satisfying $\mathcal M J + J^\top \mathcal M \succeq 0$ would force $\dot V \le 0$ along all trajectories, contradicting the unstable mode. *Outside the ladder.*
- **(iii) $A$ has all eigenvalues with $\mathrm{Re}\lambda \le 0$, at least one on the imaginary axis, imaginary-axis eigenvalues semisimple** — R0-loss. A certificate $\mathcal M\succ 0$ exists; trajectories along the imaginary-axis-eigenvector subspace orbit perpetually (conserving $V = e^\top \mathcal M e$ on each level set), and trajectories on the strict-stable complement decay exponentially toward that subspace.
- **(iv) defective Jordan block at an imaginary eigenvalue** — no certificate exists: polynomial growth on the generalized eigenvector ($e \sim t\cdot v$) violates $\dot V \le 0$ for any quadratic $V$. *Outside the ladder.*

R0-loss occupies the strict slice (iii), disjoint from R0-strict (i) and from the no-certificate regimes (ii), (iv). The four-case partition is exhaustive (every real matrix sits in exactly one) and mutually exclusive. R0-loss is *not* "R0-strict with $\kappa$ tending to zero" — R0-strict's $\kappa\gt 0$ is strict by definition; the limit $\kappa\to 0^+$ does not land in R0-loss but on its closure boundary. R0-loss is also distinct from the identifiability-floor boundary of $\mathbb S^n_{\succeq 0}$ ( #disc-identifiability-floor's Sylvester mechanism): the floor has $\mathcal M$ dropping rank, while R0-loss has $\mathcal M$ remaining $\succ 0$ with the rank drop on the *Hermitian part* $\mathcal M J + J^\top \mathcal M$ instead.

**Pure case — Helmholtz $S/A$ as canonical sufficient route.** Taking $\mathcal M = I$, $S:=\tfrac{1}{2}(J + J^\top)$, $A_{\mathrm{anti}}:=\tfrac{1}{2}(J - J^\top)$. The conditions

(ii) $S \equiv 0$ ($J$ is purely antisymmetric);

(iii) $V(e) = \tfrac{1}{2}\lVert e\rVert^2$ is exactly conserved along $\dot e = -Je$ for all initial $e$

are equivalent — (ii ⟹ iii) by direct calculation $\dot V = -e^\top S e \equiv 0$ when $S = 0$, and (iii ⟹ ii) by polarization for symmetric $S$. Either implies case (iii) of the spectral partition above: real antisymmetric $J$ has purely-imaginary spectrum (its characteristic polynomial is even, forcing eigenvalues in $\pm i\omega$ pairs) and is diagonalizable over $\mathbb C$ (hence semisimple).

**The converse — case (iii) implying antisymmetry at $\mathcal M = I$ — does not hold.** A non-antisymmetric $J$ can sit in case (iii) too: $J = \begin{pmatrix} 1 & -2 \\ 2 & -1 \end{pmatrix}$ has $S = \mathrm{diag}(1,-1)$ at $\mathcal M = I$ (so $\mathcal M J + J^\top \mathcal M = 2S$ is indefinite, failing the certificate condition there) but eigenvalues $\pm i\sqrt 3$ (pure imaginary, semisimple). For such a $J$ the R0-loss certificate exists by the spectral partition but requires $\mathcal M \neq I$; finding the explicit metric (via similarity to real Jordan form, or the center-manifold construction below) is what the partition guarantees but does not provide constructively. **The full characterization of R0-loss is the four-case spectral partition above; the Helmholtz $S/A$ route at $\mathcal M = I$ is the canonical *sufficient* construction for the antisymmetric sub-class — the structural framing for the Letcher 2019 Hamiltonian-game vocabulary — not a necessary condition for R0-loss generally.** Bendixson's localization $\mathrm{Re}(\lambda(-J)) \in [-\lambda_{\max}(S), -\lambda_{\min}(S)]$ gives a *containment* interval that here is $[-1, 1]$ — wide enough to permit purely-imaginary eigenvalues without forcing $S = 0$.

Letcher-Balduzzi et al. 2019 Lemma 1 (uniqueness of the $S + A$ decomposition) and Definition 2 (Hamiltonian game = $S \equiv 0$) name this sufficient route in game-mechanics vocabulary; AAT's content is the recognition that the antisymmetric sub-class is the cleanest specific construction, with the R0-loss regime itself broader. The general-$\mathcal M$ extension replaces $S$ with $S_\mathcal M := \tfrac{1}{2}\mathcal M^{-1}(\mathcal M J + J^\top \mathcal M)$; an $\mathcal M$ rendering $S_\mathcal M \succeq 0$ exists for every case-(iii) $J$ by the partition.

**Mixed case — Conley anchoring.** At a chosen certificate $\mathcal M$ rendering $S_\mathcal M \succeq 0$ with nontrivial kernel — some imaginary-axis eigenvalues plus some strict-stable ones — the dynamics splits canonically: along $\ker(S_\mathcal M)$, $V$ is conserved (the chain-recurrent component); along $S_\mathcal M$'s positive-eigenspace, $V$ decays strictly (the strongly-gradient-like component). This is Conley 1978's universal decomposition (Fundamental Theorem of Dynamical Systems, §8.1): every flow on a compact invariant set decomposes uniquely into a chain-recurrent subflow plus a strongly-gradient-like quotient. AAT's R0-loss localizes this universality at the linearization. On the chain-recurrent component (the restricted operator is $\mathcal M$-antisymmetric on $\ker(S_\mathcal M)$ and hence trace-free in the $\mathcal M$-orthonormal basis), $V$ restricted to each level set $\{V = c\}$ is volume-preserving by Liouville, hence chain-recurrent in Conley's sense (Poincaré recurrence). The explicit construction of $\mathcal M$ in the mixed case follows from center-manifold machinery (Carr 1981 §2); the qualitative shape — chain-recurrent subspace + strongly-gradient-like complement — is universal, while the explicit metric is standard but not derived here.

## Epistemic Status

*Exact* at the linearized level (the equivalence is the standard Lyapunov theorem, recognized and applied — not a fresh derivation), and *exact with the standard second-order remainder condition* locally. The constituent theorem is classical; what is contributed here is the recognition that AAT's one-point sector condition (A2'/(T2)) in a free choice of inner product is *exactly* the converse-Lyapunov certificate, which makes the framework's organizing slogan a theorem rather than a heuristic.

*Scope honesty.* Linearized/local — this is the level at which AAT's persistence results already operate (sector conditions, contraction templates, the bridge lemma all linearize about the equilibrium), so it is not a weakening relative to the rest of the theory, but it is a genuine scope statement and is not papered over: there is **no** claim that one-point operator-sector is equivalent to *global* exponential stability (it is not, in general — the global statement requires the incremental rung R1, the cocoercive class). The disturbance-to-ultimate-bound step that turns "contracts" into "stays within a bounded ball under disturbance" is proved separately in #deriv-sector-condition and #result-sector-persistence-template; this result supplies the contraction half of the slogan, those supply the exceeds-the-drift half.

*R0-loss scope.* The R0-loss rung's pure case (Helmholtz $S \equiv 0$ characterization; all eigenvalues on the imaginary axis, semisimple) is *exact* at the linearized level — the equivalence $S \equiv 0 \Leftrightarrow$ full-state marginal stability at $\kappa = 0$ follows from polarization plus Bendixson's localization. The mixed case (chain-recurrent subspace + strongly-gradient-like complement) is *exact-via-Conley* — Conley 1978 §8.1's universal decomposition supplies the qualitative shape; the explicit $\mathcal M$ construction in mixed cases is center-manifold-level work (Carr 1981 §2) sketched above rather than derived. The non-Hurwitz scope question — whether nonlinear systems with Case-(iii) linearization are actually Lyapunov-stable rather than displaying quartic-or-higher instabilities on the center manifold — is the standard nonlinear-stability open problem (Khalil §4.3), not within the linearized claim made here.

Max attainable: *exact* (it is the Lyapunov theorem, in scope; R0-loss extends via Letcher 2019 / Conley 1978, recognized and applied — not fresh derivations). Novelty posture is *recognition*, not new mathematics.

## Discussion

**This is the segment-level home of the contraction-over-drift organizing principle.** The slogan *an adaptive system is an operator whose contraction rate exceeds its target's drift rate* had, until now, no segment to point to — it was carried as a framing heuristic. The equivalence above is its formal content: the "contraction" half is clause 2 ⟺ clause 1 (a certificate exists iff the dynamics is exponentially stable); the "exceeds the drift" half is the ultimate-bound argument of #result-sector-persistence-template, which takes the certificate's $\kappa$ and the disturbance rate and returns the bounded-error guarantee. A reader can now cite the principle to a result, not to a slogan.

**Why the equivalence matters beyond tidiness.** It is what licenses the cross-sectional reading in #disc-stability-certificate: because "a certificate exists" is the same statement as "the agent can keep up," every structural question about AAT's reach becomes a question about this one object — does a certificate exist here (scope), is it forced to a unique form (forced identity), where does it degenerate (the boundary), does it survive coarse-graining (composition). Without the equivalence those would be four loosely-related observations; with it they are four questions about one mathematical object.

**The certificate is not the Lyapunov function.** $V(e)=e^\top\mathcal M e$ is the Lyapunov function; $\mathcal M$ is the certificate. The distinction is load-bearing downstream: the framework's representational freedom (choice of coordinate / metric) acts on $\mathcal M$, and what that freedom can and cannot do to $\mathcal M$ — change its conditioning but not its inertia — is the content of the boundary facet ( #disc-identifiability-floor, the Sylvester mechanism). Naming $\mathcal M$ as the object, rather than $V$, is what makes that downstream statement expressible.

**R0-loss as the linearization-fingerprint of saddle-Nash composite regimes.** Pure R0-loss at the single-agent linearization level is the spectral fingerprint of `#disc-dynamic-regime-axis`'s **R2 cyclic-distributional-regime** at the joint Jacobian linearized about saddle-only Nash equilibria: the joint best-response field's symmetric part vanishes there (no potential structure), and the antisymmetric part supplies the imaginary-axis spectrum. FTRL × graphical-constant-sum games with fully-mixed Nash (Cheung-Piliouras-Tao 2021 Theorem 19: lossless DGS + Poincaré recurrence on bounded level sets) is the worked composite instance. The R-letter overlap with the dynamic-regime axis is layer-honest, not collision: this segment's R0-loss/R0-strict/R1/R2 lives at the single-agent linearized error space $\mathbb R^n$ (the agent's own certificate over its own error coordinate); the dynamic-regime axis's R0/R1/R2/R3 lives at the composite joint-strategy space $\mathcal X^c$ (the joint-dynamics fixed-point structure of a composite of sub-agents). Same letters, different objects, different layers — composing across layers is exactly what the bridge sentence above does, and is the structural content of the layering rather than a coincidence to be hidden.

## Findings

### The Contraction-Over-Drift Principle, Grounded

**Brief:** Picture an agent trying to stay on a target that keeps drifting. Ask one question: is there a way of measuring "how far off am I" — a measuring-stick — such that *every* correction the agent makes provably shrinks that measure? This result says: such a measuring-stick exists exactly when the agent is, in the ordinary control-theory sense, exponentially stable. The two are not analogous, they are the *same fact* (the Lyapunov theorem) — which is why the long-standing slogan "an adaptive system is one whose contraction outpaces its target's drift" is a theorem and not a vibe. A thoughtful non-specialist can carry the whole thing away from the picture: *the measuring-stick exists* = *the agent can keep up*; everything else AAT says about reach, blind spots, and composition is downstream questions about that one stick.

**Impact:** Discharges the long-standing "organizing slogan not yet surfaced at segment level" status by giving the contraction-over-drift principle an exact, citable home. Supplies the anchor that licenses the certificate-cone cross-sectional reading ( #disc-stability-certificate): the equivalence is what turns "four loosely-related structural observations" into "four questions about one object." Cleanly separates the exact mathematical core (this result) from the discussion-grade organizing recognition (the spine), so each is housed at its true epistemic tier rather than the exact equivalence being buried as a derived-tag inside a discussion-grade segment. Names the certificate (not the Lyapunov function) as the object, which is the precondition for the boundary-facet's Sylvester statement being expressible downstream.

**Novelty Claim:** *Claim recognition* that AAT's one-point sector condition under a free choice of inner product is exactly the converse-Lyapunov certificate, making the framework's contraction-over-drift organizing principle the Lyapunov-theorem equivalence rather than a heuristic. The theorem is classical (Lyapunov 1892); the contribution is the identification that the framework's A2'/(T2) machinery *is* this object, and the consequent segment-level grounding of the organizing slogan.

**Related Work:**
- Lyapunov, A. M. (1892), *The General Problem of the Stability of Motion* (Engl. transl. 1992, Taylor & Francis); Khalil, H. K. (2002), *Nonlinear Systems* 3rd ed., Thm 4.6 (Lyapunov equation), Thm 4.7 (indirect method) (found 2026-05-14) — *formal antecedent* — the equivalence and the local extension are this theorem applied; the contribution is the recognition, not the proof.
- Conley, C. (1978), *Isolated Invariant Sets and the Morse Index*, CBMS Regional Conf. Ser. Math. 38, AMS — Fundamental Theorem of Dynamical Systems, §8.1 (found 2026-05-22) — *formal antecedent* — the universal decomposition of any flow on a compact invariant set into a chain-recurrent subflow plus a strongly-gradient-like quotient. R0-loss's mixed case is this universality localized at the linearization. The constituent theorem is classical; the contribution is recognizing that the R0-strict / R0-loss distinction is exactly Conley's two pieces of the universal decomposition.
- Letcher, A., Balduzzi, D., Racanière, S., Martens, J., Foerster, J., Tuyls, K. & Graepel, T. (2019), "Differentiable Game Mechanics," *JMLR* 20:1–40 (found 2026-05-22) — *formal antecedent* — Lemma 1 (uniqueness of the symmetric+antisymmetric decomposition $J = S + A$) and Definition 2 (Hamiltonian game = $J$ purely antisymmetric) supply the pure-R0-loss characterization. Letcher's "Hamiltonian game" is the *fully* R0-loss agent in AAT's linearization vocabulary; "potential game" is the strict sub-case of R0-strict where $J = J^\top$.
- Cheung, Y. K., Piliouras, G. & Tao, Y. (2021), "Online Optimization in Games via Control Theory: Connecting Regret, Passivity and Poincaré Recurrence," *arXiv:2106.04748* (found 2026-05-22) — *formal antecedent (worked composite instance)* — Theorem 19 (FTRL × graphical-constant-sum-with-fully-mixed-Nash is lossless DGS, with Poincaré recurrence on bounded level sets) provides the worked composite instance of R0-loss at the joint Jacobian's saddle-only-Nash linearization. The qualitative bridge "finitely-lossless storage ⟹ R0-loss linearization at any accumulation equilibrium" survives; the quantitative bridge ($L$ as $V$) does not (different state spaces, different functional forms; see also #def-control-regret Discussion on the qualitative-only diagnostic).
- #deriv-sector-condition, #result-sector-persistence-template (adjacent) — supply the disturbance-to-ultimate-bound half of the slogan; this result supplies the contraction half.

**Search Log:**
- 2026-05-14 (*targeted*): The equivalence is the textbook Lyapunov theorem; no search needed for the theorem itself. The search target was whether the *recognition* "AAT's one-point sector condition in a free inner product = the converse-Lyapunov certificate, hence the contraction-over-drift slogan is this equivalence" appears articulated elsewhere as a framework-grounding move. Not found at this depth; expected to remain *recognition*-tier (the theorem is universal; the framework-grounding identification is the contribution).
- 2026-05-22 (*absorbed*, Track CR Phase 3): R0-loss rung extension absorbed via §1 enrichment cluster spike (`spikes/spike-enrichment-cluster1-2026-05-21/02-r0-loss-derivation.md`) plus integration-reconciliation verdict (`spikes/spike-integration-reconciliation-2026-05-22/99-verdict.md` §5 Phase 3). The constituent prior art (Conley 1978; Letcher 2019; Cheung-Piliouras-Tao 2021) was verified in the §1 cluster's domain; no separate Pillar / Undermind search was conducted for the rung-extension itself — the rung is the AAT-internal recognition that these textbook results jointly classify a fourth ladder rung disjoint from R0-strict and from the Sylvester-floor regime.

## Working Notes

- **Provenance.** Split out of #disc-stability-certificate 2026-05-14 (it had been a `*[Derived]*`-tagged block) so the exact equivalence is housed at its true tier (`status: exact`) rather than inside a `discussion-grade` segment. Landed in the 2026-05-14 operator-family-unification cycle; see CHANGELOG 2026-05-14. The full proof and the R0-loss / R0-strict / R1 / R2 ladder are in the Derivation above; the originating spike is absorbed archaeology, not a live reference.
- **R0-loss landing (2026-05-22).** Extension landed via Track CR Phase 3 per `spikes/spike-integration-reconciliation-2026-05-22/99-verdict.md` §5 Phase 3 and `spikes/spike-enrichment-cluster1-2026-05-21/02-r0-loss-derivation.md` (the §1 cluster's derivation work). The prior `R0` rung was renamed to `R0-strict` for naming-consistency with the Helmholtz $S$-positive vs $S$-zero split; R0-loss was added as the new widest rung; the Discussion gained a cross-layer bridge sentence locating R0-loss as the linearization-fingerprint of #disc-dynamic-regime-axis R2 cyclic-distributional composite regimes. The mid-case explicit $\mathcal M$ construction (center-manifold-level, Carr 1981 §2) is sketched in the Derivation but not derived in detail here — readers needing the explicit construction work through the center-manifold mechanics standard in nonlinear stability theory. Cross-canon rename sweep also touches #disc-stability-certificate (ladder reference in the anchor) and #result-contraction-template (ladder summary in Discussion), plus the OUTLINE.md table entry.
- **Provisional slug.** `result-certificate-existence`. Subject-noun = "certificate existence" (the result establishes when a certificate exists). Route through the naming pipeline if a better name surfaces.
- **Organizing-principle linkage.** This segment is the intended segment-level home for the PROPOSALS Bundle-1 organizing-principle slogan ("contraction-over-drift"); the PROPOSALS entry should point here once Joseph confirms the propagation step. Bundle-1 not auto-rewritten.
