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

The certificate admits three strictly-ordered strengths, all on the one object:

| Rung | Condition | Equivalent to | Certificate is |
|---|---|---|---|
| R0 | one-point (C), some $\mathcal M$, local | $A=-J$ Hurwitz + remainder dominated | converse-Lyapunov $\mathcal M$ (exists; generally not forced) |
| R1 | incremental (two-point) $\mathcal M$-strong-monotonicity on $\mathcal B_R$ | global $\mathcal M$-strong-monotone (cocoercive class) | curvature-like $\mathcal M$ (potential sub-case) |
| R2 | R1 with $\mathcal M$ *forced* by a uniqueness theorem on an AAT-internal axiom | natural-gradient in the Čencov-unique Fisher metric | Fisher metric (Čencov-forced) |

R0 ⟸ R1 ⟸ R2 strictly. R0 is the *widest* rung — it reaches the plant-Lyapunov cases (linear-Hurwitz-non-symmetric, PID) where no potential exists; R1 is the cocoercive/proximal class where a variational structure is available; R2 is the uniqueness-theorem-forced statistical case. The widest rung is not a weakness: it is exactly the reach the narrower rungs cannot give. (R2's forcing is established in #disc-additive-coordinate-forcing; R1's cocoercive class in #result-contraction-template.)

## Derivation

**(1 ⟹ 3, 2).** $A=-J$ Hurwitz. By the Lyapunov theorem (Lyapunov 1892; Khalil, *Nonlinear Systems* 3rd ed., Thm 4.6), for every $Q\succ0$ the equation $A^\top\mathcal M+\mathcal M A=-Q$ has a unique solution $\mathcal M\succ0$. Substituting $A=-J$ gives $\mathcal M J+J^\top\mathcal M=Q\succ0$ (clause 3). For the rate: $Q\succeq\lambda_{\min}(Q)\,I\succeq\dfrac{\lambda_{\min}(Q)}{\lambda_{\max}(\mathcal M)}\,\mathcal M$, so (C) holds at the linear level with $\kappa=\dfrac{\lambda_{\min}(Q)}{2\,\lambda_{\max}(\mathcal M)}\gt0$ (clause 2).

**(2 ⟹ 1).** Suppose $\mathcal M\succ0$, $\kappa\gt0$, $\mathcal M J+J^\top\mathcal M\succeq2\kappa\mathcal M$. Take $V(e)=e^\top\mathcal M e$ (valid Lyapunov candidate, $\mathcal M\succ0$). Along $\dot e=-Je$: $\dot V=-e^\top(\mathcal M J+J^\top\mathcal M)e\le-2\kappa\,e^\top\mathcal M e=-2\kappa V\lt0$ for $e\neq0$. Hence $\lVert e(t)\rVert_{\mathcal M}\le e^{-\kappa t}\lVert e(0)\rVert_{\mathcal M}$ and $A=-J$ is Hurwitz.

**(3 ⟺ 2)** is the rate-extraction argument (3 gives 2 with the displayed $\kappa$; 2 is the special case $Q=\mathcal M J+J^\top\mathcal M$).

**Local nonlinear extension.** With $F(e)=Je+r(e)$, $\lVert r(e)\rVert=o(\lVert e\rVert)$, (C) holds on $\mathcal B_R(e^\ast)$ iff the linearization is exponentially stable *and* the second-order remainder is dominated on the ball ($\lVert r(e)\rVert_{\mathcal M}\le c\lVert e\rVert_{\mathcal M}^2$ with $cR\lt\kappa$). This is the standard Lyapunov indirect method (Khalil Thm 4.7); the remainder-domination radius is exactly the contraction-template Tier-2 degradation radius ( #result-contraction-template), not new machinery.

## Epistemic Status

*Exact* at the linearized level (the equivalence is the standard Lyapunov theorem, recognized and applied — not a fresh derivation), and *exact with the standard second-order remainder condition* locally. The constituent theorem is classical; what is contributed here is the recognition that AAT's one-point sector condition (A2'/(T2)) in a free choice of inner product is *exactly* the converse-Lyapunov certificate, which makes the framework's organizing slogan a theorem rather than a heuristic.

*Scope honesty.* Linearized/local — this is the level at which AAT's persistence results already operate (sector conditions, contraction templates, the bridge lemma all linearize about the equilibrium), so it is not a weakening relative to the rest of the theory, but it is a genuine scope statement and is not papered over: there is **no** claim that one-point operator-sector is equivalent to *global* exponential stability (it is not, in general — the global statement requires the incremental rung R1, the cocoercive class). The disturbance-to-ultimate-bound step that turns "contracts" into "stays within a bounded ball under disturbance" is proved separately in #deriv-sector-condition and #result-sector-persistence-template; this result supplies the contraction half of the slogan, those supply the exceeds-the-drift half.

Max attainable: *exact* (it is the Lyapunov theorem, in scope). Novelty posture is *recognition*, not new mathematics.

## Discussion

**This is the segment-level home of the contraction-over-drift organizing principle.** The slogan *an adaptive system is an operator whose contraction rate exceeds its target's drift rate* had, until now, no segment to point to — it was carried as a framing heuristic. The equivalence above is its formal content: the "contraction" half is clause 2 ⟺ clause 1 (a certificate exists iff the dynamics is exponentially stable); the "exceeds the drift" half is the ultimate-bound argument of #result-sector-persistence-template, which takes the certificate's $\kappa$ and the disturbance rate and returns the bounded-error guarantee. A reader can now cite the principle to a result, not to a slogan.

**Why the equivalence matters beyond tidiness.** It is what licenses the cross-sectional reading in #disc-stability-certificate: because "a certificate exists" is the same statement as "the agent can keep up," every structural question about AAT's reach becomes a question about this one object — does a certificate exist here (scope), is it forced to a unique form (forced identity), where does it degenerate (the boundary), does it survive coarse-graining (composition). Without the equivalence those would be four loosely-related observations; with it they are four questions about one mathematical object.

**The certificate is not the Lyapunov function.** $V(e)=e^\top\mathcal M e$ is the Lyapunov function; $\mathcal M$ is the certificate. The distinction is load-bearing downstream: the framework's representational freedom (choice of coordinate / metric) acts on $\mathcal M$, and what that freedom can and cannot do to $\mathcal M$ — change its conditioning but not its inertia — is the content of the boundary facet ( #disc-identifiability-floor, the Sylvester mechanism). Naming $\mathcal M$ as the object, rather than $V$, is what makes that downstream statement expressible.

## Findings

### The Contraction-Over-Drift Principle, Grounded

**Brief:** Picture an agent trying to stay on a target that keeps drifting. Ask one question: is there a way of measuring "how far off am I" — a measuring-stick — such that *every* correction the agent makes provably shrinks that measure? This result says: such a measuring-stick exists exactly when the agent is, in the ordinary control-theory sense, exponentially stable. The two are not analogous, they are the *same fact* (the Lyapunov theorem) — which is why the long-standing slogan "an adaptive system is one whose contraction outpaces its target's drift" is a theorem and not a vibe. A thoughtful non-specialist can carry the whole thing away from the picture: *the measuring-stick exists* = *the agent can keep up*; everything else AAT says about reach, blind spots, and composition is downstream questions about that one stick.

**Impact:** Discharges the long-standing "organizing slogan not yet surfaced at segment level" status by giving the contraction-over-drift principle an exact, citable home. Supplies the anchor that licenses the certificate-cone cross-sectional reading ( #disc-stability-certificate): the equivalence is what turns "four loosely-related structural observations" into "four questions about one object." Cleanly separates the exact mathematical core (this result) from the discussion-grade organizing recognition (the spine), so each is housed at its true epistemic tier rather than the exact equivalence being buried as a derived-tag inside a discussion-grade segment. Names the certificate (not the Lyapunov function) as the object, which is the precondition for the boundary-facet's Sylvester statement being expressible downstream.

**Novelty Claim:** *Claim recognition* that AAT's one-point sector condition under a free choice of inner product is exactly the converse-Lyapunov certificate, making the framework's contraction-over-drift organizing principle the Lyapunov-theorem equivalence rather than a heuristic. The theorem is classical (Lyapunov 1892); the contribution is the identification that the framework's A2'/(T2) machinery *is* this object, and the consequent segment-level grounding of the organizing slogan.

**Related Work:**
- Lyapunov, A. M. (1892), *The General Problem of the Stability of Motion* (Engl. transl. 1992, Taylor & Francis); Khalil, H. K. (2002), *Nonlinear Systems* 3rd ed., Thm 4.6 (Lyapunov equation), Thm 4.7 (indirect method) (found 2026-05-14) — *formal antecedent* — the equivalence and the local extension are this theorem applied; the contribution is the recognition, not the proof.
- #deriv-sector-condition, #result-sector-persistence-template (adjacent) — supply the disturbance-to-ultimate-bound half of the slogan; this result supplies the contraction half.

**Search Log:**
- 2026-05-14 (*targeted*): The equivalence is the textbook Lyapunov theorem; no search needed for the theorem itself. The search target was whether the *recognition* "AAT's one-point sector condition in a free inner product = the converse-Lyapunov certificate, hence the contraction-over-drift slogan is this equivalence" appears articulated elsewhere as a framework-grounding move. Not found at this depth; expected to remain *recognition*-tier (the theorem is universal; the framework-grounding identification is the contribution).

## Working Notes

- **Provenance.** Split out of #disc-stability-certificate 2026-05-14 (it had been a `*[Derived]*`-tagged block) so the exact equivalence is housed at its true tier (`status: exact`) rather than inside a `discussion-grade` segment. Landed in the 2026-05-14 operator-family-unification cycle; see CHANGELOG 2026-05-14. The full proof and the R0/R1/R2 ladder are in the Derivation above; the originating spike is absorbed archaeology, not a live reference.
- **Provisional slug.** `result-certificate-existence`. Subject-noun = "certificate existence" (the result establishes when a certificate exists). Route through the naming pipeline if a better name surfaces.
- **Organizing-principle linkage.** This segment is the intended segment-level home for the PROPOSALS Bundle-1 organizing-principle slogan ("contraction-over-drift"); the PROPOSALS entry should point here once Joseph confirms the propagation step. Bundle-1 not auto-rewritten.
