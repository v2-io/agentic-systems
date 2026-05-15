# L1 — The stability certificate: operator-sector ⟺ Hurwitz Jacobian

**Leg under test (00-brief L1).** Is one-point operator-sector "in *some* inner product" an *exact equivalence* with the linearized equilibrium being exponentially stable (Jacobian Hurwitz), via the converse-Lyapunov theorem — or only a typographic analogy? This is the O-BP10 keystone. The C1 predecessor asserted the operator-sector / monotone-operator correspondence via Rockafellar/Bauschke-Combettes but did not pin the equivalence; this file pins it and marks exactly where it is iff, where it is one-directional, and where the one-point-vs-incremental gap bites.

## Setup and conventions

Continuous-time error dynamics around an equilibrium, $F(0)=0$:

$$\dot e = -F(e), \qquad e \in \mathbb R^n, \quad F \in C^1 \text{ near } 0.$$

Linearization: $\dot e = -J e + r(e)$, $J := DF(0)$, $\lVert r(e)\rVert = o(\lVert e\rVert)$. Write the *system matrix* $A := -J$. Equilibrium $e=0$ is exponentially stable for the linearization iff $A$ is Hurwitz (spectrum in the open left half-plane), equivalently $\operatorname{Re}\lambda(J) > 0$ for every eigenvalue $\lambda(J)$.

The **one-point operator-sector condition in metric $M \succ 0$** (continuous form, the AAD A2'/(T2) condition lifted to a weighted inner product $\langle x,y\rangle_M = x^\top M y$):

$$\langle F(e), e\rangle_M \;\ge\; \kappa\, \lVert e\rVert_M^2 \qquad \text{on } \mathcal B_R, \qquad \kappa>0. \tag{OS-1}$$

To leading order $F(e)=Je+o(\lVert e\rVert)$, so (OS-1) at the linear level is $e^\top M J e \ge \kappa\, e^\top M e$ for all $e$, i.e.

$$M J + J^\top M \;\succeq\; 2\kappa M \;\succ\;0. \tag{OS-1-lin}$$

This is *precisely* a strict Lyapunov inequality for $A=-J$: writing it as $A^\top M + M A = -(MJ+J^\top M) \preceq -2\kappa M \prec 0$.

## The equivalence (linear level) — VERIFIED, exact iff

> **Proposition L1-lin.** For $J \in \mathbb R^{n\times n}$, the following are equivalent:
> 1. $A=-J$ is Hurwitz (the linearized error dynamics $\dot e=-Je$ is exponentially stable);
> 2. there exist $M\succ 0$ and $\kappa>0$ such that $MJ+J^\top M \succeq 2\kappa M$ — i.e., the dynamics satisfies a one-point operator-sector condition (OS-1-lin) in the $M$-inner-product with rate $\kappa$;
> 3. there exist $M\succ 0$ and $Q\succ 0$ with $MJ+J^\top M = Q$.

**Proof.**
(1 ⟹ 3, 2). $A$ Hurwitz. By the Lyapunov theorem (Lyapunov 1892; Khalil 2002, *Nonlinear Systems* 3rd ed., Thm 4.6), for every $Q\succ 0$ the equation $A^\top M + M A = -Q$ has a unique solution $M\succ 0$. Substituting $A=-J$: $-(J^\top M + M J) = -Q$, i.e. $MJ+J^\top M = Q \succ 0$ (gives 3). For the rate: $Q \succeq \lambda_{\min}(Q)\,I \succeq \dfrac{\lambda_{\min}(Q)}{\lambda_{\max}(M)}\,M$, so (OS-1-lin) holds with $\kappa = \dfrac{\lambda_{\min}(Q)}{2\,\lambda_{\max}(M)}>0$ (gives 2).

(2 ⟹ 1). Suppose $M\succ 0$, $\kappa>0$, $MJ+J^\top M\succeq 2\kappa M$. Take $V(e)=e^\top M e$, a valid Lyapunov candidate ($M\succ0$). Along $\dot e=-Je$: $\dot V = -e^\top(MJ+J^\top M)e \le -2\kappa\,e^\top M e = -2\kappa V < 0$ for $e\neq0$. Hence $V$ is a strict Lyapunov function and $A=-J$ is Hurwitz (in fact $\lVert e(t)\rVert_M \le e^{-\kappa t}\lVert e(0)\rVert_M$).

(3 ⟺ 2) is the rate-extraction argument already given (3 gives 2 with $\kappa=\lambda_{\min}(Q)/2\lambda_{\max}(M)$; 2 is a special case of 3 with $Q=MJ+J^\top M$). $\;\square$

**Epistemic status: exact (proved).** This is the standard Lyapunov equivalence; the only content added here is the *reading* — clause 2 is exactly the AAD one-point operator-sector condition in a weighted inner product. So at the linearized level the O-BP10 keystone is **not an analogy: it is an equivalence.** "An adaptive system is an operator whose [strong-monotonicity / contraction] rate exceeds its disturbance rate" is, modulo the disturbance-vs-rate ultimate-bound step (proved separately in `#deriv-sector-condition` Prop A.1 / the persistence template), the Lyapunov characterization of exponential stability, with the metric $M$ as the certificate.

## Why this is the *widest* unifying object (and the Lyapunov counterexample is not a counterexample to *this*)

The brief flagged that jacobian-b1 §6.4 falsified the naive "potential $\Phi$ is the unifying object" hypothesis: the linear-Hurwitz-non-symmetric case is operator-sector in a Lyapunov metric but is **not** a gradient field — no $\Phi$. Proposition L1-lin shows why that is *consistent with*, not destructive of, the stability-certificate spine: the certificate $M$ from the Lyapunov equation **always exists when $A$ is Hurwitz**, regardless of whether $J$ is symmetric / a gradient. A non-normal Hurwitz $J$ (e.g. $J=\begin{psmallmatrix}1&-10\\0&1\end{psmallmatrix}$, eigenvalues $1,1$ so $\operatorname{Re}\lambda(J)>0$, $A=-J$ Hurwitz) has *no* potential but *does* have a unique Lyapunov $M\succ0$ — the operator-sector condition holds in the $M$-inner-product even though it fails in the Euclidean one. So:

> **The unifying object is the equilibrium Jacobian's stability certificate $M$ (the converse-Lyapunov metric), which exists exactly on the Hurwitz set — strictly wider than the potential/gradient class and strictly wider than the Euclidean-operator-sector class.** Potential structure ($\nabla^2\Phi$, the (SOC) axiom) is the *sub-case where the certificate is the objective's curvature*; Euclidean operator-sector is the *sub-case where the certificate is $M=I$*. The C1 four "instances" and the jacobian-b1 five metric cases are not a list — they are points on one set (Hurwitz), distinguished by *which certificate the metric is* (identity / Lyapunov-plant / Hessian / Fisher / information).

This is the spine. It survives the Lyapunov counterexample because the counterexample is a counterexample to "*potential* is the object," not to "*the certificate* is the object." Verification did its job: the false leg (potential-unification) is dead; the surviving leg (certificate-unification) is *proved* at the linear level.

## The one-point-vs-incremental gap — handled honestly, and it is a *ladder*, not a defect

The C1 spike (§3.2) correctly worried that one-point operator-sector is strictly weaker than incremental (two-point) strong monotonicity. Proposition L1-lin is about the **one-point** form and it is *exactly* the Hurwitz characterization. The incremental form

$$\langle F(x)-F(y),\,x-y\rangle_M \ge \kappa\lVert x-y\rVert_M^2 \quad \forall x,y\in\mathcal B_R \tag{OS-inc}$$

is **strictly stronger** and is **not** equivalent to Hurwitz. (OS-inc) is global $M$-strong-monotonicity of $F$ on the ball; combined with Lipschitz it is the Baillon–Haddad cocoercive class (Bauschke–Combettes 2017 §18, §22). Cocoercivity ⟹ the field is (a metric image of) a *monotone* operator with the splitting/proximal closure properties — this is the class where a potential-like variational structure is available. So the honest hierarchy is a **certificate-strength ladder**, all on a single object:

| Rung | Condition | Equivalent to | AAD label | Certificate is |
|---|---|---|---|---|
| R0 | $\exists M\succ0$: one-point OS at $e^*$, local | $A=-J$ Hurwitz + 2nd-order remainder dominated on $\mathcal B_R$ | A2'/(T2) one-point; sub-scope α∪(Lyapunov-β) | converse-Lyapunov $M$ (exists, generally not forced) |
| R1 | $\exists M\succ0$: (OS-inc) on $\mathcal B_R$ | $F$ globally $M$-strongly-monotone on ball | DA2'-inc; cocoercive class | curvature-like $M$ (potential sub-case) |
| R2 | (OS-inc) with $M$ *forced* by an AAD-internal uniqueness theorem | $F$ natural-gradient in the Čencov-unique Fisher metric | M3 statistical instance | Fisher metric (Čencov-forced) |

R0 ⟸ R1 ⟸ R2 strictly. **The C1 "one-point is weaker" is reframed: one-point (R0) is not a weakness — it is the *widest rung*, the one that reaches the Lyapunov-plant β-cases the incremental form (R1) and the forced form (R2) cannot. The ladder itself is a meta-structural fact: the operator-family meta-pattern, if it is a spine, is this ladder.** This is consistent with jacobian-b1 §7.3's "(L2) mixed lift with layered structure" verdict — that file found the *layering*; this file names what it is layering: rungs of the stability certificate.

## Nonlinear / local statement (the honest L1)

> **L1 (local equivalence, the honest form).** One-point operator-sector (OS-1) in *some* inner product $M\succ0$ on a ball $\mathcal B_R$ around $e^*$ holds **iff** (i) the linearization is exponentially stable ($A=-J$ Hurwitz; equivalently the converse-Lyapunov $M$ exists, Prop L1-lin) **and** (ii) the second-order remainder is dominated on $\mathcal B_R$: $\lVert r(e)\rVert_M \le c\lVert e\rVert_M^2$ with $cR < \kappa$ so the linear contraction is not overturned inside the ball. Condition (ii) is *exactly* the C1 §8(b) Tier-2 "$\kappa(D\hat o)^2$ degradation" radius condition — it is not new machinery, it is the Lyapunov indirect method (Khalil Thm 4.7) read in the operator-sector metric.

**Epistemic status: exact (proved at linear level via Prop L1-lin; the nonlinear local extension is the standard Lyapunov indirect method, cited not re-derived).** No analogy remains in L1. The keystone holds.

## What L1 settles, and what it hands to L3

- **Settled:** O-BP10 is an equivalence, not an analogy — at the (linearized, local) level that AAD's persistence results already operate at. The "operator-sector in some metric" object *is* "equilibrium exponentially stable," with the metric as the converse-Lyapunov certificate. The four C1 instances and five jacobian-b1 metric cases are one set (Hurwitz) under different certificates. The one-point/incremental gap is a *rung ladder* on that one object, not competing definitions.
- **Handed to L3:** Prop L1-lin's certificate $M$ exists **iff $A$ Hurwitz**. The Lyapunov equation $A^\top M+MA=-Q$ becomes **singular exactly when $A$ has an eigenvalue on the imaginary axis** (Re $\lambda(J)=0$). That boundary is the candidate identifiability-floor. L3 tests whether AAD's actual M1 instances (Bareinboim CHT, Cramér–Rao rank-1, Liberzon common-Lyapunov-nonexistence, Čencov) are *exactly* certificate-boundary / certificate-rank-collapse events — i.e., whether M1 is the boundary of the very set L1 characterizes. If yes, M1 and operator-sector are dual the way a domain and its boundary are dual: provably *not* unifiable into one interior statement, and that non-unifiability is the sharp no-go.
- **Handed to L4:** the certificate is an *endomorphism-level* object (a metric on the micro-space), so the C1 "Λ is not an endomorphism" category problem does not arise at the certificate level. L4 tests whether the certificate survives projection — i.e., whether the Mori–Zwanzig memory kernel is exactly "the projected dynamics' Jacobian is not Hurwitz even though the micro one is," the projection-side certificate-failure.
