---
slug: spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24
type: spike
status: draft
date: 2026-04-24
---

# Spike: Fenchel-Bregman Reframe of `#additive-coordinate-forcing`

**Charter.** The IB-purity spike's Path 7 (`msc/spike-ib-purity-strategy-cost-strengthening-2026-04-24.md` §7) produced a structural observation that may require reframing `#additive-coordinate-forcing`: the divergence-layer instance (reverse-KL) and the update-layer instance (log-odds) are not independent Cauchy-FE forcings but Fenchel-dual aspects of one exponential-family commitment. This spike verifies Path 7's claim, analyzes whether the Čencov/metric layer sits inside or outside the Fenchel structure, analyzes the chain-layer anchor's relationship, and compares three candidate reframes with explicit tradeoffs.

**Posture.** Strengthen-first, not soften-first. "Adopt Path 7's reframe" and "keep the current framing" are both easy defaults. The harder question is what the *accurate* structural description is once Path 7's observation is on the table.

**Outcome in one sentence.** Path 7's Fenchel-duality observation is **verified, mathematically correct, and incomplete in a specific way**: the divergence ↔ update duality it names is real, but the Čencov/metric layer is *also* inside the same Legendre-Fenchel geometry (Fisher = Hessian of log-partition = Bregman-Riemannian limit of reverse-KL), *and* the chain-layer anchor is the restriction of the same geometry to product exponential families. The honest structural description is therefore **not** "1-anchor + 1-Fenchel-pair + 1-Čencov-instance" (the naive Path-7 reframe, under-unified) nor "1-anchor + 3-theorem" (the current framing, over-separated) — it is **one geometric commitment (the exponential-family / Legendre-Fenchel structure on categorical distributions) manifesting at four operational layers under independently-motivated AAD axioms that all happen to be simultaneously satisfied by that geometry**. Reframe (A) — the unified exponential-family reframe — is the accurate description; reframes (B) and (C) either under-unify (keep separations that are illusory) or over-separate (erect boundaries the geometry does not respect). The recommendation is **reframe (A) with sharp preservation of the axiom-independence story** — the axioms are not redundant; they are *independently-motivated constraints that all happen to be simultaneously satisfied by the exponential-family geometry*, and *that convergence is itself the meta-pattern's substance*.

---

## §1 — Verifying Path 7's Fenchel-Bregman computation

### §1.1 The claim to verify

Path 7 states: on the probability simplex $\Delta^{n-1} = \{Q \in \mathbb{R}^n : Q_a \geq 0, \sum_a Q_a = 1\}$, the negative-entropy potential $\phi(Q) = \sum_a Q(a) \log Q(a)$ is strictly convex and Legendre; its Fenchel conjugate is the log-partition function $\phi^*(\eta) = \log \sum_a e^{\eta_a}$; the primal-dual correspondence is $Q(a) = e^{\eta_a} / \sum_{a'} e^{\eta_{a'}}$ (softmax); the Bregman divergence induced by $\phi$ on the primal side is reverse-KL: $B_\phi(P, Q) = D_{\mathrm{KL}}(P \Vert Q)$; and on the dual side, the analogous Bregman divergence $B_{\phi^*}(\eta, \eta')$ is also a "reverse-KL-at-dual-coordinates" object.

### §1.2 Direct verification

*[Derived, status: exact]* **(FB-1) Legendre property of negative entropy on the simplex.** On the *relative interior* of $\Delta^{n-1}$ (i.e., $Q \in \Delta^{n-1}$ with $Q_a \gt 0$ for all $a$), $\phi(Q) = \sum_a Q_a \log Q_a$ is strictly convex (Hessian $\nabla^2 \phi = \operatorname{diag}(1/Q_a)$ is strictly PD on the tangent space $\{v : \sum_a v_a = 0\}$), is of Legendre type (steep: $\lVert \nabla \phi \rVert \to \infty$ at the boundary, where any $Q_a \to 0$), and is essentially smooth on the relative interior (Rockafellar 1970 *Convex Analysis* §26.1, Definition of Legendre function).

**(FB-2) Fenchel conjugate.** The Fenchel conjugate is
$$\phi^*(\eta) \;=\; \sup_{Q \in \Delta^{n-1}} \bigl[\langle \eta, Q\rangle - \phi(Q)\bigr]$$

The simplex constraint $\sum_a Q_a = 1$ is enforced via Lagrange multiplier $\mu$. Stationarity gives $\eta_a - \log Q_a - 1 - \mu = 0$, whence $Q_a = e^{\eta_a - 1 - \mu}$. Normalization $\sum_a Q_a = 1$ forces $\mu = \log \sum_a e^{\eta_a} - 1$ and $Q_a = e^{\eta_a} / \sum_{a'} e^{\eta_{a'}}$ (softmax). Substituting:
$$\phi^*(\eta) \;=\; \log \sum_a e^{\eta_a} - 1 \cdot 1 \;=\; \log \sum_a e^{\eta_a} - 1$$

Dropping the constant $-1$ (which is absorbed into the affine gauge freedom $\eta_a \mapsto \eta_a + c$), we recover $\phi^*(\eta) = \log \sum_a e^{\eta_a}$: the **log-partition function** of the categorical exponential family in natural parameters $\eta$.

**(FB-3) Primal-dual correspondence.** By (FB-2), $Q = \nabla \phi^*(\eta)$ yields the softmax $Q_a = e^{\eta_a} / \sum_{a'} e^{\eta_{a'}}$; and $\eta = \nabla \phi(Q) = \log Q + \mathbf{1}$, modulo the $\mathbf{1}$ that lives in the constraint-normal direction. The coordinate $\eta_a - \eta_b = \log(Q_a / Q_b)$ is the **log-odds ratio** — the coordinate of `#edge-update-natural-parameter` generalized to the categorical case.

**(FB-4) Bregman divergence on the primal.** The Bregman divergence induced by $\phi$ is
$$B_\phi(P, Q) \;=\; \phi(P) - \phi(Q) - \langle \nabla\phi(Q), P - Q \rangle$$

Computing: $\phi(P) - \phi(Q) = \sum_a [P_a \log P_a - Q_a \log Q_a]$. The inner-product term, using $\nabla\phi(Q)_a = \log Q_a + 1$, is $\sum_a (\log Q_a + 1)(P_a - Q_a) = \sum_a (\log Q_a)(P_a - Q_a) + \sum_a (P_a - Q_a)$. The second sum is zero (both $P$ and $Q$ are probability vectors). Therefore:
$$B_\phi(P, Q) \;=\; \sum_a P_a \log P_a - \sum_a Q_a \log Q_a - \sum_a (\log Q_a)(P_a - Q_a)$$
$$=\; \sum_a P_a \log P_a - \sum_a P_a \log Q_a \;=\; \sum_a P_a \log \frac{P_a}{Q_a} \;=\; D_{\mathrm{KL}}(P \Vert Q)$$

So $B_\phi(P, Q) = D_{\mathrm{KL}}(P \Vert Q)$ — **reverse-KL is the Bregman divergence of the negative-entropy potential**, confirming Path 7's claim.

**(FB-5) Bregman divergence on the dual.** By Fenchel duality, the dual Bregman divergence is
$$B_{\phi^*}(\eta, \eta') \;=\; B_\phi(\nabla\phi^*(\eta), \nabla\phi^*(\eta'))$$

which, in the exponential-family case, gives a log-partition form: $B_{\phi^*}(\eta, \eta') = \phi^*(\eta) - \phi^*(\eta') - \langle Q(\eta'), \eta - \eta'\rangle$ where $Q(\eta)$ is the softmax. This is the "cumulant-generating Bregman divergence" standard in exponential-family estimation theory (Amari-Nagaoka 2000 §3.5; Nielsen-Garcia 2009 *Statistical exponential families: A digest with flash cards*). It equals the KL divergence between the corresponding exponential-family distributions evaluated at the two parameter points: $B_{\phi^*}(\eta, \eta') = D_{\mathrm{KL}}(Q(\eta) \Vert Q(\eta'))$ *[Derived, status: exact; Amari-Nagaoka 2000 §3.5 Eq. (3.77) and Proposition 3.9]*.

This is the same reverse-KL object, parameterized by $\eta$ rather than by $Q$ — the two are the same geometric quantity in different coordinates.

### §1.3 Verdict on Path 7's claim

**Path 7's Fenchel-duality claim is verified and correct.** The identifications

- *$\phi(Q) = \sum_a Q_a \log Q_a$ is the primal potential*,
- *$\phi^*(\eta) = \log \sum_a e^{\eta_a}$ is its Fenchel conjugate (log-partition)*,
- *$Q \leftrightarrow \eta$ via $Q = \operatorname{softmax}(\eta)$ and $\eta_a - \eta_b = \log(Q_a / Q_b)$ (log-odds ratio)*,
- *$B_\phi(P, Q) = D_{\mathrm{KL}}(P \Vert Q)$ (reverse-KL on primal)*,
- *$B_{\phi^*}(\eta, \eta') = D_{\mathrm{KL}}(Q(\eta) \Vert Q(\eta'))$ (reverse-KL on dual)*

are a complete, textbook-standard Legendre-Fenchel correspondence (Rockafellar 1970 §26; Amari-Nagaoka 2000 §3.5; Bauschke-Combettes 2017 *Convex Analysis and Monotone Operator Theory* §13). The divergence-layer coordinate (reverse-KL on $\Delta^{n-1}$) and the update-layer coordinate (log-odds on $\mathbb{R}^n/\mathbf{1}$) are **two sides of one Legendre-Fenchel pair**, not two independent objects.

### §1.4 "Same commitment" or "two constraints simultaneously satisfied"?

The deeper question Path 7 raises: are the divergence-layer chain-rule-additivity axiom (Hobson 1969 / Csiszár 1991) and the update-layer evidential-additivity axiom (Aczél 1966) **manifestations of one underlying commitment**, or **two genuinely different constraints that happen to produce Fenchel-dual coordinates**?

*[Derived, status: robust-qualitative]* **The two axioms are not the same constraint.** They are distinct statements about distinct objects:

- The divergence-layer axiom constrains a bivariate object $D : \mathcal{P}(\mathcal{A}) \times \mathcal{P}(\mathcal{A}) \to \mathbb{R}_{\geq 0}$, requiring chain-rule decomposition $D(P_{XY} \Vert Q_{XY}) = D(P_X \Vert Q_X) + \mathbb{E}_{P_X}[D(P_{Y\mid X} \Vert Q_{Y\mid X})]$.
- The update-layer axiom constrains a univariate coordinate function $\psi : (0,1) \to \mathbb{R}$, requiring additive evidence accumulation $\psi(p_{\text{post}}) - \psi(p_{\text{prior}}) = g(y)$.

These have different inputs, different outputs, and different logical forms (bivariate symmetry constraint vs. univariate functional equation). They are not translations of each other.

**But the exponential-family geometry simultaneously satisfies both.** On the categorical exponential family:

- The chain-rule-additivity axiom is satisfied by reverse-KL because reverse-KL is the Bregman divergence of a potential whose Hessian factorizes along conditional-independence structure (Amari-Nagaoka 2000 §3.7 on statistical-manifold product structure).
- The evidential-additivity axiom is satisfied by log-odds because log-odds is the natural parameter of a Bernoulli exponential family, and natural parameters accumulate likelihood-ratios additively (standard).

Both facts fall out of the same geometric structure but via different mechanical derivations. The Fenchel correspondence is what *relates* them: the divergence coordinate on the primal and the update coordinate on the dual *are* the two sides of one Legendre transform, even though the axioms motivating each are independent.

**The structural claim, precisely stated.** *[Derived, status: robust-qualitative]* The divergence-layer and update-layer axioms are **independent**; but their *simultaneous satisfaction by a single geometric object* — the categorical exponential family with negative-entropy potential — is **not coincidental**: it reflects that the exponential-family structure is the geometric object that the entire surrounding apparatus (DAG factorization, regret bound, Bayesian coherence, AND/OR scope) has *already committed to*. The axioms are "probing" different surfaces of the same object.

This is what Path 7's §7 named as "Fenchel-dual aspects of one exponential-family commitment." The phrase is **accurate** as a geometric description of the two coordinates but **underspecified** as a description of the axiomatic structure: the axioms remain independent; what unifies is the geometric object they jointly pick out.

---

## §2 — Does the Čencov / metric layer sit inside or outside the Fenchel structure?

### §2.1 The classical identity: Fisher = Hessian of log-partition

*[Derived, status: exact; Amari-Nagaoka 2000 §3.5 Theorem 3.5]* For an exponential family $p(x; \eta) = \exp(\eta^T T(x) - A(\eta))$ with log-partition $A(\eta)$ (= $\phi^*(\eta)$ in the notation of §1), the Fisher information matrix is:
$$\mathbf{I}(\eta) \;=\; \nabla^2_\eta A(\eta) \;=\; \operatorname{Cov}_{p(\cdot;\eta)}[T(X)]$$

For the categorical case with $\eta \in \mathbb{R}^n$ modulo $\mathbf{1}$: $\mathbf{I}(\eta) = \operatorname{diag}(Q(\eta)) - Q(\eta) Q(\eta)^T$, which is the Hessian of $\phi^*(\eta) = \log \sum_a e^{\eta_a}$ on the tangent space $\{v : \sum_a v_a = 0\}$.

**This is a Fenchel-side identity.** The Fisher metric is literally $\nabla^2 \phi^*$ — the second derivative of the dual potential of the same Legendre-Fenchel pair that generates reverse-KL and log-odds. By the standard Taylor expansion of a Bregman divergence (Amari-Nagaoka 2000 §3.5 Eq. 3.77; Eguchi 1983 §2):
$$B_{\phi^*}(\eta + \varepsilon v, \eta) \;=\; \tfrac{1}{2} v^T \mathbf{I}(\eta) v + O(\varepsilon^3)$$

The Fisher metric *is* the infinitesimal form of the dual Bregman divergence — the second-order expansion of reverse-KL at $P = Q$ (Eguchi 1983 Proposition 3.1).

### §2.2 Čencov's theorem is not the only route to the Fisher metric

Čencov 1982 forces the Fisher metric under **Markov-morphism invariance** (= parameterization-invariance under sufficient-statistic coarse-graining). This is a *different* axiomatic route than Legendre-Fenchel: Čencov's axiom is about statistical manifolds in full generality (including non-exponential families), not specifically about exponential families.

*[Observation, status: robust-qualitative]* **On categorical (or any exponential-family) manifolds, the Fisher metric forced by Čencov-invariance and the Fisher metric derived from $\nabla^2 \phi^*$ are the same metric** (up to a global scale; Ay-Jost-Lê-Schwachhöfer 2017 *Information Geometry*, Theorem 5.1). Two independently-motivated structural commitments converge on one object:

- *Route 1 (Čencov).* Statistical-manifold-level invariance under coarse-graining → Fisher metric uniquely forced (up to scale).
- *Route 2 (Fenchel-Bregman).* Legendre structure on the exponential family with negative-entropy potential → Fisher metric = $\nabla^2 \phi^*$.

On exponential-family statistical manifolds, these two routes produce the *same* metric. Outside of exponential families (e.g., curved families, non-parametric models), only Čencov's route applies — Legendre-Fenchel duality there does not straightforwardly reduce to Fisher-metric.

### §2.3 Does the Čencov layer sit inside the Fenchel structure?

**For the AAD-specific use case — where the Fisher-metric instance is applied to `#gain-sector-bridge` exponential-family-in-natural-parameters and matrix-Kalman cases (see `#gain-sector-bridge` "Fisher-metric cases under parameterization-invariance") — yes**. Both of those instances live on exponential families (Kalman is the Gaussian exponential family; Kalman-natural-parameters lives in precision coordinates, which are exponential-family natural parameters). On those manifolds, the Fisher metric is $\nabla^2 \phi^*$, and the Čencov axiom's conclusion coincides with the Fenchel-Bregman derivation's conclusion.

**For general statistical manifolds — no, not necessarily.** If AAD were to invoke the Fisher metric on a *curved* statistical family (one not representable as an exponential family), Čencov's theorem still gives the Fisher metric, but it does not arise as the Hessian of a single convex dual potential. The Legendre-Fenchel picture decomposes — it applies only to *exponential-family sub-manifolds* in general.

**AAD-specific scope observation.** The AAD commitment to the Fisher-metric instance is currently scoped to exponential-family-in-natural-parameters and matrix-Kalman cases (per `#gain-sector-bridge`). On this scope, the Fenchel-Bregman and Čencov derivations agree. **So within AAD's current Fisher-metric scope, Čencov sits inside the Fenchel structure**; but this fact is partly a consequence of AAD having chosen to apply the Fisher-metric instance only where exponential-family structure is present. A future generalization (e.g., applying (PI) to a non-exponential statistical family) would break the coincidence.

*[Claim, status: robust-qualitative]* **The Čencov layer's coincidence with the Fenchel structure on AAD's current scope is not accidental, but it is also not forced by the AAD axiomatic system alone.** It is forced by the conjunction of (a) the (PI) parameterization-invariance axiom, (b) Čencov's theorem, AND (c) AAD's independent commitment to exponential-family scope in `#gain-sector-bridge`. Remove any of the three and the coincidence weakens — in particular, if (PI) were adopted but the Fisher-metric instance applied to curved non-exponential families, Čencov's derivation would still apply, but the Fenchel-Bregman derivation would not.

### §2.4 What this implies for the meta-pattern

The Fenchel-Bregman reframe encompasses the Čencov/metric layer **on AAD's current scope**, but it does so via a *scope coincidence*, not a structural identity at the axiomatic level. The clean statement:

- **On exponential-family statistical manifolds** (AAD's current Fisher-metric scope): Čencov's Fisher metric = $\nabla^2 \phi^*$ = the infinitesimal form of reverse-KL. The metric layer is inside the Fenchel-Bregman geometry.
- **In full generality**: Čencov's Fisher metric is forced by Markov-morphism invariance regardless of whether a convex dual potential exists. The metric layer is *structurally broader* than the Fenchel-Bregman geometry, even if they coincide on the sub-scope AAD cares about.

This is load-bearing for the reframe question: whether the Čencov layer is "inside" or "outside" the Fenchel structure depends on whether AAD ever intends to apply the Fisher-metric instance beyond its current exponential-family scope. If not (the pragmatic stance), Čencov sits inside. If yes (the structurally-permissive stance), Čencov sits partially outside.

---

## §3 — The chain-layer anchor and the Fenchel structure

### §3.1 What the chain-layer anchor does

`#chain-confidence-decay` states the log-of-product identity $\log P(E_1, \ldots, E_n) = \sum_i \log P(E_i \mid E_{\lt i})$, which is a mathematical identity obtained by applying log to the probability chain rule. The segment positions this as:
- A mathematical identity, not an AAD axiom.
- The anchor for the divergence- and update-layer uniqueness theorems, because both theorems' axioms are positioned as "the divergence-level analog" and "the update-level analog" of the chain-layer identity's additive log-confidence decomposition.
- A Section II structural-pressure result (long plans are fragile because log-confidence accumulates negative terms).

### §3.2 Does the chain-layer connect to the Fenchel structure?

*[Derived, status: robust-qualitative]* **The chain-layer identity is a statement about product exponential families, and can be recast as a statement about the additivity of Bregman-divergence contributions along a factorization.** Consider:

$$-\log P(E_1, \ldots, E_n) \;=\; \sum_i \bigl[-\log P(E_i \mid E_{\lt i})\bigr]$$

Each term $-\log P(E_i \mid E_{\lt i})$ is the reverse-KL from $\delta_{E_i}$ (point mass on the realized outcome) to the predictive distribution $P(\cdot \mid E_{\lt i})$ — i.e., the negative log-likelihood, which is the Bregman divergence (reverse-KL) evaluated at a specific trajectory. The chain rule then states:

$$B_{\phi^{\otimes n}}\bigl(\delta_{E_1:n}, P_{1:n}\bigr) \;=\; \sum_i \mathbb{E}_{E_{\lt i}}\bigl[B_\phi(\delta_{E_i}, P(\cdot \mid E_{\lt i}))\bigr]$$

where $\phi^{\otimes n}$ is the negative-entropy potential on the product simplex $(\Delta^{n-1})^{\otimes n}$, and the equality uses the **additivity of Bregman divergences across independent exponential-family factors** (standard; Cover-Thomas 2006 §2.5 for the KL case; Amari-Nagaoka 2000 Proposition 3.10 for the Bregman-general case).

This shows that the chain-layer identity is **the Bregman-divergence version of the product-form factorization on exponential families**. It is the restriction of the Fenchel-Bregman geometry to product families.

### §3.3 But the chain-layer identity holds for *any* probability distribution

The probability chain rule $\log P(E_1, \ldots, E_n) = \sum_i \log P(E_i \mid E_{\lt i})$ is **not specific to exponential families**. It holds for any joint distribution — this is why `#chain-confidence-decay` is a mathematical identity rather than a derived result. The Fenchel-Bregman reading of §3.2 is *one* way to see the identity through an exponential-family lens, but the identity itself is more general.

*[Observation, status: exact]* **The chain-layer identity is consistent with the Fenchel-Bregman geometry on exponential families, but it is not a consequence of that geometry — it is a broader fact that happens to restrict cleanly to exponential families.** The same remark applies as for the Čencov layer (§2.3): on the exponential-family sub-scope, the chain layer and the Fenchel geometry are consistent; in full generality, the chain layer is structurally broader.

### §3.4 The anchor's role under the reframe

Under the current `#additive-coordinate-forcing` framing, the chain-layer identity is the *motivational anchor* for the divergence and update layers — their AAD-internal additivity axioms are stated as analogs of the chain-layer identity. Under the Fenchel-reframe, there are two possible readings:

1. **Anchor preserved as motivation.** The chain-layer identity still motivates the divergence-layer and update-layer axioms as "analogs of a commitment AAD already relies on"; the Fenchel-Bregman duality is a *separate* observation about how the resulting coordinates relate geometrically. The anchor and the geometric unification are orthogonal observations.

2. **Anchor absorbed into the geometry.** The chain-layer identity, the divergence-layer axiom, and the update-layer axiom are all independently-motivated ways of saying "the surrounding apparatus lives on the exponential-family geometry." The chain layer's logarithmic coordinate is forced by the probability chain rule; the divergence layer's reverse-KL coordinate is forced by chain-rule-additivity + Cauchy-FE; the update layer's log-odds coordinate is forced by evidential-additivity + Cauchy-FE. All three axioms are independently motivated and all three converge on the exponential-family structure because that is the geometric object AAD's architecture has already committed to.

**Reading (1) preserves the motivational story intact; reading (2) dissolves it into a geometric convergence.** The question is whether the *motivational cross-cites* among the three axioms are load-bearing or merely rhetorical.

*[Claim, status: robust-qualitative]* **Reading (1) is structurally more honest.** The three axioms have different logical forms (§1.4) and are independently-justifiable: chain-rule-additivity in divergence (Hobson 1969 axiom on bivariate objects) and evidential-additivity in update (Aczél 1966 axiom on univariate functions) are distinct formal constraints. Their common structural content — "additivity along a factorization" — is real but abstract; the *specific* axioms are independently-motivated. Pretending the axioms are redundant because they have geometric convergence collapses the motivation-structure in a way that loses information.

**The correct statement**: the chain-layer identity is the motivational anchor *under AAD's axiom-structure*; the Fenchel-Bregman geometry is what emerges when the three axioms all land on the same underlying object. Both readings of the anchor are correct from different vantage points, but the reframe should preserve the motivational anchor structure while naming the geometric convergence as an additional observation.

---

## §4 — What counts as "independent forcing" for the meta-pattern?

### §4.1 The question sharpened

The current `#additive-coordinate-forcing` treats each of the four instances as an independent application of Cauchy-FE / Čencov-invariance on an AAD-internally-motivated axiom. Path 7's observation asks: if the divergence-layer and update-layer coordinates are Fenchel-dual (i.e., two sides of one Legendre transform), is the current framing *overcounting* independent instances?

*[Observation, status: robust-qualitative]* There are two senses of "independent" to disambiguate:

- **Independent axiomatic motivation.** Do the axioms for the four layers have distinct logical forms, such that one cannot be derived from another? *Yes — this is established in §1.4 and §2.2.* Chain-rule additivity, evidential additivity, and parameterization-invariance are logically distinct constraints. The current framing is correct at this level.

- **Independent geometric content.** Do the forced coordinates lie in geometrically distinct spaces, or are they dual/equivalent aspects of one space? *No — the forced coordinates are related by Legendre-Fenchel duality (divergence-layer and update-layer) and by second-order expansion / infinitesimal form (metric-layer).* The current framing is **overcounting** at this level.

### §4.2 The "multiple paths to the same point" reading

A common pattern in mathematics: multiple independently-motivated axiomatic systems converge on the same object. Examples:

- The real numbers can be constructed via Dedekind cuts, Cauchy sequences, or axiomatically via the least-upper-bound property. These are independent constructions; they all pick out the same object.
- The exponential function can be defined via its ODE, via its power series, via its functional equation, or via its limit form. Four independent routes to the same object.
- The Fisher metric can be derived via Čencov-invariance, via Hessian of log-partition, via Rao's distance, via fisher-information-in-likelihood-ratios. Four independent routes to the same metric.

In each case, the *convergence* is load-bearing: that multiple independently-motivated routes pick out the same object is stronger evidence that the object is structurally right than any single route would be.

*[Claim, status: robust-qualitative]* **AAD's situation is of this kind.** Chain-rule-additivity + Cauchy-FE, evidential-additivity + Cauchy-FE, and parameterization-invariance + Čencov are three independently-motivated axiomatic routes that all converge on (sub-surfaces of) the exponential-family geometry on categorical distributions. The convergence is the meta-pattern's substance, not a byproduct to be compressed away.

The meta-pattern's value is therefore not "we independently force the same coordinate four times" (overcounted — there are not four independent coordinates; there are four independently-motivated axiomatic routes to one geometric object). The meta-pattern's value is also not "we have one exponential-family commitment that shows up in four places" (undercounted — the axioms are logically independent, not re-statements of a single commitment).

The meta-pattern's value is: **a cluster of independently-motivated AAD-internal axioms all converge on a single geometric object (the exponential-family structure on categorical distributions and its Legendre-Fenchel geometry), and this convergence is itself the meta-pattern — it shows that AAD's architecture has quietly committed to this geometry via multiple independent surface constraints**.

### §4.3 Implications for counting

Under this reading, the questions "how many instances are there?" and "how many axioms are there?" have different answers:

- **Number of independent axioms: 3 (plus 1 anchor).** Chain-rule-additivity, evidential-additivity, parameterization-invariance (+ the chain-layer mathematical identity as the motivational anchor).
- **Number of geometrically distinct coordinates: 1 family of related coordinates on one space.** The exponential-family geometry on categorical distributions, manifesting as (primal) softmax / $Q$, (dual) log-odds / $\eta$, (quadratic form) Fisher metric, and (integrated) reverse-KL Bregman divergence. These are not four separate coordinates; they are four aspects of one geometric object.
- **Number of AAD-segment instances that fall under the pattern: 4.** `#chain-confidence-decay`, `#strategy-cost-regret-bound` §6.1, `#edge-update-natural-parameter`, and the `#gain-sector-bridge` Fisher-metric cases.

The current framing conflates these three counts. The reframe disambiguates them: **3 axioms + 1 anchor → converging on 1 geometric object → expressed across 4 AAD-segment instances.**

---

## §5 — The adjacent family members under the reframe

### §5.1 Lyapunov quadratic

The Lyapunov quadratic $V(\delta) = \tfrac{1}{2}\lVert\delta\rVert^2$ is the Bregman divergence of the Euclidean potential $\phi(\delta) = \tfrac{1}{2}\lVert\delta\rVert^2$:
$$B_\phi(\delta, \delta') \;=\; \phi(\delta) - \phi(\delta') - \langle \nabla\phi(\delta'), \delta - \delta'\rangle \;=\; \tfrac{1}{2}\lVert\delta - \delta'\rVert^2$$

which is Fenchel-**self-dual** (the Euclidean potential is its own Fenchel conjugate up to a sign). This is the Bregman divergence on $\mathbb{R}^n$ with the Euclidean inner product.

*[Observation, status: exact]* **Under the Fenchel-Bregman reframe, the Lyapunov quadratic is a Bregman divergence with a different convex potential (Euclidean $\lVert\cdot\rVert^2$ instead of negative-entropy).** It is structurally in the same family — both are Bregman divergences on finite-dimensional convex domains — but it lives on a different convex potential.

**Is this a primary instance?** The Lyapunov potential is *chosen* (the sector condition A2' is matched to this coordinate; the converse-Lyapunov theorem guarantees existence but not equality to the Euclidean norm — see `#additive-coordinate-forcing`'s Lyapunov adjacent-family discussion). So under AAD's current commitments, the Lyapunov quadratic is an adjacent-family Bregman divergence, not a *forced* coordinate.

**Under (PI) + the Fisher-metric instance of `#gain-sector-bridge`, the matrix-Kalman case's natural Lyapunov $V(\delta) = \tfrac{1}{2}\delta^T P^{-1} \delta$ becomes the Bregman divergence of the Fisher potential.** On this scope, the Lyapunov potential is forced (by (PI) + Čencov) to be the Fisher metric, and the Bregman structure aligns with the divergence-layer geometry. Outside of this scope (scalar sector conditions in non-statistical-manifold contexts), the Lyapunov potential remains chosen.

*[Claim, status: robust-qualitative]* **Under the reframe, the Lyapunov quadratic is promoted from "adjacent family with coordinate matched rather than forced" to "Bregman divergence on Euclidean potential" (parallel to reverse-KL being the Bregman divergence on negative-entropy potential).** It still does not qualify as a *primary instance* of additive-coordinate-forcing because its axiom (converse-Lyapunov existence) is structurally different from the four primary instances (the converse-Lyapunov theorem establishes *some* Lyapunov function exists — it does not uniquely force one). But its Bregman-structure relationship to the other instances is now visible.

### §5.2 IB Lagrangian

The IB Lagrangian $I(X;T) - \beta I(T;Y)$ is an additive Lagrangian form using mutual informations. Mutual information on exponential families is a Bregman-divergence-related object (specifically, $I(X;T) = \mathbb{E}_X[D_{\mathrm{KL}}(P(T\mid X) \Vert P(T))]$, which is a reverse-KL instance on the exponential-family geometry).

*[Observation, status: robust-qualitative]* **Under the reframe, IB is an application of the Fenchel-Bregman geometry (since mutual information is expectation-of-reverse-KL, and reverse-KL is the Bregman divergence of negative-entropy).** The IB Lagrangian sits inside the same geometric family as the primary instances.

**Is IB promoted to a primary instance under the reframe?** The current segment's reason for adjacency is that IB is *adopted* from Tishby-Pereira-Bialek 1999 as an applied external theorem, not *re-derived* under AAD-internal motivation. The Fenchel-Bregman reframe does not change that — the geometric structure IB operates on is now known to coincide with the structure underlying the divergence / update / metric primary instances, but the AAD commitment to IB is still "adopt" rather than "internally-force."

*[Claim, status: robust-qualitative]* **Under the reframe, IB is still an adjacent family member, but its adjacency is now visible as "same geometric object, different axiomatic route (Tishby-Pereira-Bialek 1999's information-theoretic capacity axiom rather than AAD-internal motivation)."** The reframe sharpens the classification: all adjacent family members (Lyapunov, IB) are on the same Bregman-geometry family as the primary instances; they differ from the primary instances in their axiomatic provenance (chosen / imported), not in their geometric structure.

### §5.3 The (AV) variance-additive case

The variance-additive candidate (from `msc/spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24.md` precursor — the ρ-factorization spike in the 2026-04-23 brainstorm cycle) is a candidate fourth instance that was *not* promoted because the ρ-factorization is natively variance-additive, not log-multiplicative. Under the Fenchel-Bregman lens: variance-additive structure corresponds to Bregman divergence on **squared-norm potentials** (Euclidean or Mahalanobis), not negative-entropy potentials. So the variance-additive case would be a Bregman-type instance, but on a *different* potential family than the exponential-family / negative-entropy geometry underlying the primary instances.

*[Observation, status: robust-qualitative]* **The (AV) variance-additive case is Bregman-type but geometrically distinct.** The reframe clarifies that there is not one universal Bregman-divergence structure in AAD; there is the exponential-family / negative-entropy sub-family (which the four primary instances share) and the Euclidean / squared-norm sub-family (which Lyapunov and (AV) share). Whether (AV) qualifies as a primary instance would depend on whether AAD has an internally-motivated axiom that forces the squared-norm potential (the variance-additive precondition, if internally justified). This was the obstruction the 2026-04-23 brainstorm cycle identified — ρ-factorization is natively variance-additive in `#team-persistence`'s structure, which is *Euclidean*-Bregman rather than *entropic*-Bregman. The reframe gives a principled language for why (AV) is a different *kind* of potential than the primary four.

---

## §6 — Three candidate reframes

### §6.1 Reframe (A): Full exponential-family-geometry unification

**Thesis.** Restate the meta-pattern as: *AAD has committed to the exponential-family geometry on categorical distributions (with negative-entropy potential and log-partition dual) as its underlying geometric object, via a cluster of four independently-motivated AAD-internal axioms/identities that all happen to be simultaneously satisfied by that geometry*. The four manifestations — logarithmic chain coordinate (anchor); reverse-KL divergence; log-odds update coordinate; Fisher metric — are the four layer-specific surfaces of one geometric commitment.

**Structure.**
- 1 geometric object (exponential-family structure on categorical distributions)
- 3 AAD-internal axioms (chain-rule additivity, evidential additivity, parameterization-invariance) + 1 mathematical-identity anchor (probability chain rule + log)
- 4 AAD-segment manifestations at chain / divergence / update / metric layers

**Presentation flavor.** "When AAD needs a coordinate at a particular layer, its surrounding apparatus forces an axiom that picks the exponential-family coordinate at that layer. The four layers are different operational aspects of one geometric object; the four axioms are independently-motivated constraints that the geometric object satisfies simultaneously."

**Merits.**
- **Unification.** Names a structural convergence that is mathematically real (Fenchel-Bregman, Fisher-as-Hessian, Bregman-additivity under factorization are textbook identities).
- **Clarifies adjacent cases.** Lyapunov quadratic sits on Euclidean-Bregman, different potential family; IB sits on same geometric family, different axiomatic provenance; (AV) sits on a third potential family. Clean typology.
- **Strengthens the "beauty / concision / fundamentality" virtues** CLAUDE.md treats as first-class. One geometric object with multiple manifestations is a stronger and more beautiful description than four parallel theorem-level instances.
- **Aligns with Amari-Nagaoka 2000's standard information-geometry framing.** The reframe brings AAD into line with the standard mathematical framework that already treats divergence / natural parameter / Fisher metric as three aspects of one exponential-family structure.

**Risks / costs.**
- **Risk of appearing to over-unify.** The axioms *are* logically independent; the reframe must not suggest they are reducible to one axiom. The "convergence of independent axioms" framing (§4.2) is the correct form, not "one underlying axiom in disguise."
- **Risk of losing the motivational anchor structure.** The three theorem-level axioms are positioned as "analogs of the chain-layer identity." Under the unification reframe, the motivational cross-cites might be read as decorative rather than load-bearing. Guarding against this: the reframe must preserve the axiom-independence story — the axioms are motivated by being analogs of the chain anchor *and* they converge on the exponential-family geometry; both observations are true.
- **Risk of re-scoping the meta-pattern.** The current framing covers *any* AAD layer where a coordinate is forced by a uniqueness-theorem argument on an AAD-internal axiom. The exponential-family reframe narrows the meta-pattern to *the specific exponential-family geometry*. If a future AAD segment forces a coordinate via a different uniqueness-theorem on a different geometry (e.g., Dempster-Shafer belief functions; min-plus semiring; non-commutative probability), the reframe would not straightforwardly accommodate it. This is a real cost — the current framing's breadth would narrow.
- **Reader-approachability cost.** Exponential-family geometry is more technical than Cauchy-FE. Readers who understand "functional equation forces a coordinate" will have to learn Legendre-Fenchel duality to understand the reframe.

### §6.2 Reframe (B): Separation-is-real (keep current framing + add Fenchel-duality as Discussion observation)

**Thesis.** The three theorem-level axioms (chain-rule additivity, evidential additivity, parameterization-invariance) are *genuinely independent* structural commitments that *happen to be simultaneously satisfied* by the exponential-family geometry. The convergence is notable but does not justify merging the four instances into one. The current 1-anchor-plus-3-theorem framing is correct; the Fenchel-Bregman duality is a Discussion-level observation about how the forced coordinates relate geometrically, not a reframe of the meta-pattern's structure.

**Structure.** Unchanged from current: 4 primary instances, 2 adjacent family members, explicit 1-anchor-3-theorem characterization.

**Addition.** A Discussion paragraph in `#additive-coordinate-forcing` noting that the divergence-layer and update-layer coordinates are Fenchel-dual via the negative-entropy potential; that the metric-layer Fisher metric is the infinitesimal form of the dual Bregman divergence; and that the chain-layer identity restricts cleanly to the exponential-family product structure. Framed as "additional structural observation," not as a replacement of the primary-instances count.

**Merits.**
- **Preserves the axiom-independence story cleanly.** Each axiom stands alone; the meta-pattern is "AAD's architecture quietly forces four structurally-distinct axioms that each force a coordinate via a uniqueness theorem." The independence of the axioms is the substance.
- **Preserves breadth.** The meta-pattern remains flexible for future instances that might use different uniqueness-theorem machineries on different geometries (Dempster-Shafer, min-plus, etc.).
- **Minimal segment churn.** Current framing is retained; one Discussion paragraph is added.

**Risks / costs.**
- **Under-describes the structural convergence.** The Fenchel-Bregman duality is more than a "nice observation" — it is a mathematical identity (§1-§3) that relates the forced coordinates. Treating it as a Discussion-level aside undersells its structural significance.
- **Leaves the reader asking the obvious question.** If a reader notices that reverse-KL's Bregman divergence and log-odds' natural parameter are Fenchel-dual, they will expect the meta-segment to state this explicitly and position the duality structurally. A Discussion-paragraph acknowledgment is enough to be correct but not enough to be illuminating.
- **Does not clarify adjacent-family structure.** Under (B), Lyapunov remains "adjacent because coordinate is matched rather than forced"; IB remains "adjacent because imported rather than re-derived." The reframe (A) adds a second, more structural dimension — what convex potential does the case's Bregman divergence sit on — that the current framing does not.

### §6.3 Reframe (C): Hybrid (anchor + Fenchel-dual pair + Čencov as three structurally distinct)

**Thesis.** The chain-layer anchor, the Fenchel-dual divergence ↔ update pair, and the Čencov metric layer are three structurally distinct things. The anchor is a probability identity; the Fenchel-pair is a geometric duality on exponential families; the Čencov instance is a statistical-manifold invariance commitment that coincides with the Fenchel geometry on AAD's current scope but is not reducible to it in general.

**Structure.**
- Chain-layer anchor: 1 (probability identity, not geometric)
- Fenchel-dual pair (divergence + update): 1 (two aspects of exponential-family Legendre-Fenchel structure)
- Čencov metric layer: 1 (statistical-manifold invariance, broader in general; coincides with Fenchel-pair on AAD's current scope)

Total: 3 structurally distinct instances (not 4 parallel ones; not 1 unified geometric object).

**Merits.**
- **Intermediate between (A) and (B).** Captures the Fenchel duality in the structure of the pattern itself (not just as a Discussion aside), while preserving the Čencov / chain distinctions that (A) compresses.
- **Clean statement of the relationships.** Three categories of structural content, each with its own geometric character:
  - Chain-layer: probability identity (not specific to exponential families)
  - Fenchel-pair: exponential-family Legendre-Fenchel structure
  - Čencov: statistical-manifold invariance (broader in general)
- **Preserves the axiom-independence story.** The Fenchel-pair is still composed of two axioms (chain-rule additivity + evidential additivity); the Čencov instance has its own (parameterization-invariance).

**Risks / costs.**
- **Slightly more complex than (A) or (B).** The three-category typology is less clean than either "one geometric object" (A) or "four parallel instances" (B).
- **Invites a quibble about the chain-layer.** §3 showed that the chain-layer identity *can* be read as a Bregman-divergence statement on product exponential families. Reframe (C) treats it as geometrically separate; a reader could argue it should be folded into the Fenchel category. The defense is §3.3: the chain-layer identity holds for any joint distribution, not just exponential families; its relationship to Fenchel is one-way (restriction, not identity).
- **Requires justifying the Čencov-as-separate-from-Fenchel claim.** On AAD's current scope the two coincide; (C) preserves the separation based on Čencov's applicability outside exponential families. This is honest but requires careful explanation of the scope distinction.

### §6.4 Comparison table

| Criterion | (A) Full unification | (B) Separation-is-real | (C) Hybrid |
|---|---|---|---|
| Geometric accuracy on AAD's current scope | High (correctly names the convergence) | Low-medium (acknowledges but doesn't structure the convergence) | High (explicit about the Fenchel-pair + the Čencov-scope coincidence) |
| Preserves axiom-independence story | High if carefully stated; risk of compression | High (primary virtue) | High |
| Preserves motivational anchor structure | Medium-high (anchor role preserved in the convergence framing, but diluted) | High | High |
| Flexibility for future non-exponential-family instances | Low (the reframe is specific to exponential-family geometry) | High | Medium-high (explicit that Čencov is broader than Fenchel in general) |
| Reader approachability | Lower (requires Legendre-Fenchel) | Higher (Cauchy-FE is more familiar) | Medium |
| Clarity on adjacent-family structure | High (Bregman-divergence sub-families clearly distinguished) | Low (adjacent-family classification is axiomatic-provenance-based only) | Medium-high (Fenchel-pair + Lyapunov-as-different-potential explicit) |
| Segment churn to implement | High (rewrite meta-segment) | Low (one Discussion paragraph) | Medium (re-partition the primary-instance table) |
| Match to standard information geometry | High (Amari-Nagaoka 2000 standard) | Low (AAD-specific framing) | Medium (Amari-Nagaoka on Fenchel-pair; Čencov-distinct on metric layer) |

---

## §7 — Recommendation

**Recommended reframe: a modified (A) / (C) hybrid.**

The accurate structural description is **reframe (A) with explicit preservation of the axiom-independence story**, positioned as follows:

### §7.1 The reframe statement

> AAD's architecture has quietly committed to the **exponential-family geometry on categorical distributions** — the Legendre-Fenchel structure where the primal potential is negative entropy, the dual potential is log-partition, the primal coordinate is $Q$ (softmax image), the dual coordinate is log-odds / natural parameters, the associated Bregman divergence is reverse-KL, and the infinitesimal form of the Bregman divergence is the Fisher metric.
>
> This commitment manifests at four operational layers of the theory — chain, divergence, update, and metric — via **independently-motivated AAD-internal axioms** (the probability chain rule / chain-rule additivity / evidential additivity / parameterization-invariance) that all happen to be simultaneously satisfied by the exponential-family geometry. The convergence is not coincidence: it reflects that AAD's surrounding apparatus (DAG factorization, Bayesian coherence, regret-bound decision theory, and the singular-trajectory scope) has committed to this geometry through multiple independent surface constraints.
>
> The meta-pattern's structure is therefore:
> - **One geometric object**: the exponential-family Legendre-Fenchel structure on categorical distributions.
> - **Four independently-motivated AAD-internal axioms / identities** (chain-rule identity anchor + three theorem-level axioms).
> - **Four AAD-segment manifestations** at chain / divergence / update / metric layers — where the forced coordinate is the layer-specific surface of the one geometric object (logarithmic; reverse-KL; log-odds; Fisher).
>
> The convergence across independent axioms is itself the meta-pattern's substance — not a byproduct to be compressed into a single axiom.

### §7.2 Why this framing is the honest one

**Against over-unification.** The axioms are logically independent (§1.4, §2.2). Treating them as re-statements of one underlying commitment would lose the information that three *independent* structural requirements all converge on the same geometry — and that convergence is the pattern's real content.

**Against under-structuring.** The geometric convergence is real and mathematically tight (§1-§3 verifications). Treating it as a Discussion-level aside misses the architecture's self-consistency. A reader familiar with Amari-Nagaoka information geometry will immediately see the Legendre-Fenchel structure; the meta-segment should make that visibility load-bearing.

**On reader approachability.** Reframe (A) requires introducing the Legendre-Fenchel structure. The current segment already cites Aczél 1966 and Čencov 1982; adding Amari-Nagaoka 2000 and Bregman 1967 is a small additional bibliographic commitment. The upside — a structurally unified description that connects AAD's four layer-specific instances to standard information geometry — is worth the technical cost.

**On preserving motivational anchor structure.** The chain-layer identity remains the motivational anchor for the three theorem-level axioms (each axiom is still stated as "the $X$-level analog of the chain-layer additive-decomposition"). The Fenchel-Bregman reframe does not erase this; it adds an additional observation: the *reason* the three analog axioms all succeed is that they all probe the same underlying exponential-family geometry.

### §7.3 Concrete segment-level deliverables

If this reframe is adopted, the concrete changes to `#additive-coordinate-forcing` are:

1. **Revise the section structure.** Replace "1-anchor-plus-3-theorem" with "one-geometric-object-across-four-layers" as the primary framing. Preserve the axiom-independence substructure within the new framing (i.e., the four layers are still described by independent axioms, but now explicitly related through their common geometric object).

2. **Add a new section: "The underlying geometric object."** State the Legendre-Fenchel structure directly: negative-entropy potential on $\Delta^{n-1}$, log-partition Fenchel conjugate on natural-parameter space, softmax primal-dual correspondence, reverse-KL Bregman divergence, Fisher metric as Hessian of dual potential. Cite Amari-Nagaoka 2000 §3.5, Bregman 1967, Rockafellar 1970, Bauschke-Combettes 2017.

3. **Recast the four-instance table.** Replace "four parallel Cauchy-FE / Čencov instances" with "four layer-specific manifestations of the same geometry." Columns: Layer / AAD-internal axiom / Uniqueness mechanism (Cauchy-FE or Čencov-invariance) / Forced coordinate / Relation to the exponential-family geometry (e.g., "primal point"; "Bregman divergence on primal"; "natural coordinate on dual"; "Hessian of dual potential").

4. **Revise the adjacent-family discussion.** Reclassify Lyapunov quadratic as "Bregman divergence on Euclidean potential" (different convex potential, not different family). Reclassify IB as "application of the negative-entropy / reverse-KL Bregman geometry, imported axiomatic provenance rather than AAD-internally-motivated axiom." Note the (AV) variance-additive case as "Bregman-type but on a squared-norm potential" — a distinct potential sub-family.

5. **Update the Čencov-Fenchel relationship.** Explicitly state that on AAD's current Fisher-metric scope (exponential-family-in-natural-parameters and matrix-Kalman cases), the Čencov-derived Fisher metric coincides with the Hessian of the dual potential. Note the scope dependency: outside exponential families, Čencov applies but Fenchel-Bregman does not straightforwardly.

6. **Update the complementarity-with-#identifiability-floor-and-#separability-pattern section.** The three meta-segments retain their cross-sectional roles. The exponential-family reframe sharpens #additive-coordinate-forcing's "constructive" role: when AAD forces a coordinate, it forces a surface of the exponential-family geometry — not a generic logarithmic coordinate, but the specific log-coordinate-of-exponential-family.

7. **Preserve the motivational anchor.** Keep the paragraphs where the theorem-level axioms are stated as analogs of the chain-layer identity — these are still correct and still load-bearing. Add: "The reason the three analog axioms all succeed is that they all probe one geometric object; the chain-layer identity is the motivational anchor *and* the geometric object is the structural target." Both observations are true.

**Segment churn estimate.** Medium — the meta-segment rewrites substantially but the four instance-segments (`#chain-confidence-decay`, `#strategy-cost-regret-bound`, `#edge-update-natural-parameter`, `#gain-sector-bridge` Fisher-metric cases) need at most one paragraph of Discussion addition each pointing to the unified geometric picture. The structural substrate of each instance segment is unchanged.

**Effort-time note.** Per CLAUDE.md, "Effort, time, and 'risk-of-getting-stuck' are *false constraints* in this work." The recommendation stands on structural honesty, not estimated effort. Even if the recommended reframe were to require full meta-segment rewrite + four instance-segment Discussion additions, that is the correct work if the reframe is the honest description.

---

## §8 — Implications for the "Instance 4" traffic jam

The task briefing flagged a "4-candidate 'Instance 4' traffic jam": multiple candidates (ρ-factorization / architecture / constant-C / Čencov-Fisher-metric) vying for the fourth primary instance slot. The Fenchel-Bregman reframe affects this routing question.

### §8.1 Candidate analysis under the reframe

**Čencov / Fisher-metric (current resident).**
- Under current framing: fourth primary instance via (PI) + Čencov 1982.
- Under reframe (A): the metric-layer manifestation of the exponential-family geometry; already inside the unified geometric structure on AAD's current scope.
- **Verdict under reframe:** stays as a manifestation of the single geometric object. The "four primary instances" count becomes "four layer-specific manifestations of one geometry."

**ρ-factorization / variance-additive (AV).**
- Current status: not a primary instance (ρ-factorization's native additive structure is variance-additive, not log-additive).
- Under reframe (A): Bregman-type on a *different* convex potential family (squared-norm / Euclidean-Mahalanobis), not on negative-entropy. Geometrically distinct from the four manifestations.
- **Verdict under reframe:** (AV) would need to be understood as a *separate* meta-pattern candidate on a different geometric object (squared-norm Bregman rather than negative-entropy Bregman). It does not qualify as a fifth manifestation of the same geometry; it would be the first manifestation of a second, potentially-parallel meta-pattern. If pursued, it opens a structural comparison: "AAD has committed to two distinct Bregman geometries — entropic (categorical distributions) and Euclidean-like (variance-additive statistics)." Whether this second geometry warrants its own meta-segment or sits as a distinct structural observation is a separate scoping question.

**Architecture / coupling (Gemini's "coupling-as-primary-geometric-variable" thesis).**
- Current status: not a formal primary-instance candidate. Hypothesized in Gemini's 2026-04-23 audit as a deeper unification.
- Under reframe (A): coupling lives in a different geometric space (inter-agent couplings on the architecture DAG, not probability distributions on actions). It is not obviously a Bregman / Legendre-Fenchel object in the same sense. Potentially a separate meta-observation about composition geometry.
- **Verdict under reframe:** does not qualify as a primary instance under either current framing or (A). If pursued, it would be a separate meta-pattern about composition-architecture geometry, not an extension of additive-coordinate-forcing.

**Constant-C (from the critical-mass composition closed form, `#critical-mass-composition`).**
- Current status: not a primary instance (the $C$ constant in $(\alpha - C)R \gt \rho + \gamma\mathcal{T}$ is a contraction-rate parameter, not a coordinate).
- Under reframe (A): does not live on the exponential-family geometry; is a sector-condition / Lyapunov-contraction object. Adjacent family at best (Lyapunov quadratic).
- **Verdict under reframe:** does not qualify. Stays outside the meta-pattern.

### §8.2 Net implication

The reframe (A) **resolves the traffic jam by geometric typing**: candidates that live on the exponential-family geometry (Čencov-Fisher) are manifestations of the pattern; candidates that live on other Bregman geometries (AV) are candidates for a *parallel* meta-pattern on a different geometric object, not extensions of this one; candidates that are not Bregman-type (coupling architecture; constant-C Lyapunov contraction rates) are outside the pattern entirely.

Under reframe (A), the meta-pattern's primary-instance count is stable at **four layer-specific manifestations of one geometric object**. Future candidates that appear to fit the pattern should be asked: *does this candidate live on the exponential-family Legendre-Fenchel geometry?* If yes, it is a further manifestation of the same object (which at four layers — chain / divergence / update / metric — is already fully covered; a fifth layer would have to be a structurally distinct coordinate on the same geometry). If no, it is either an adjacent family member (different Bregman geometry) or outside the pattern entirely.

**This is a valuable side-effect of the reframe.** The current framing provides no principled way to adjudicate candidate fifth instances (each would need its own axiom-check). The reframe (A) supplies a principled filter: *does the candidate's coordinate arise from the Legendre-Fenchel / exponential-family geometry?* If yes, check which of the four layer-surfaces it corresponds to; if no, route it to a separate meta-pattern candidate.

---

## §9 — Honest caveats on what this spike does and does not establish

### §9.1 What this spike establishes (with epistemic labels)

- *[Derived, status: exact]* **Path 7's Fenchel-duality computation is correct** (§1). Reverse-KL is the Bregman divergence of negative-entropy on the simplex; log-odds is the Fenchel-dual natural coordinate; the correspondence is textbook Legendre-Fenchel.
- *[Derived, status: exact]* **Fisher metric = Hessian of log-partition** on exponential families (§2.1). The Čencov-derived Fisher metric coincides with $\nabla^2 \phi^*$ on AAD's current Fisher-metric scope.
- *[Derived, status: robust-qualitative]* **The divergence-layer and update-layer axioms are logically independent** despite producing Fenchel-dual coordinates (§1.4).
- *[Derived, status: robust-qualitative]* **The Čencov-axiom and the Fenchel-Bregman derivation give the same Fisher metric on exponential-family manifolds but are independent in full generality** (§2.3).
- *[Derived, status: robust-qualitative]* **The chain-layer identity holds broadly (any probability distribution), not just on exponential families** (§3.3); its Fenchel-Bregman reading is a restriction, not an equivalence.
- *[Observation, status: robust-qualitative]* **The meta-pattern's honest description is "multiple independently-motivated AAD-internal axioms converge on one exponential-family geometric object"** — this is neither full unification (axioms are independent) nor full separation (geometric object is shared) (§4.2).

### §9.2 What this spike does not establish

- **Whether the reframe (A) is worth the segment-churn cost.** I have recommended it on structural-honesty grounds, but the final call is Joseph's — this is a framing decision with architectural-proposal weight, not a bug-fix.
- **Whether all citations are correctly attributed at the granularity needed for segment promotion.** I relied on Amari-Nagaoka 2000 §3.5 for several specific claims (primal-dual Bregman, Fisher-as-Hessian, Proposition 3.10 on product-structure additivity). If the reframe is adopted, a PDF-verification pass on these attributions would be needed before segment-level landing. The reference is in `ref/` as `amari-cichocki-2010-info-geom-divergence.pdf` and related materials, but the specific theorem-number claims above should be checked against Amari-Nagaoka 2000 directly, not against the 2010 Amari-Cichocki paper (which is a different text).
- **Whether the (AV) variance-additive candidate warrants a second, parallel meta-pattern.** Flagged in §8.1 as a separate scoping question for a future cycle.
- **Whether the reframe dilutes the distinctiveness of AAD's contribution.** The reframe brings AAD closer to standard information geometry; a reader might read it as "AAD is just rediscovering Amari-Nagaoka's framework." The correct defense: AAD's contribution is showing that *its independently-motivated axioms, each grounded in its own AAD-internal architectural commitment, all converge on this geometry*. The geometry itself is standard; the convergence of axioms is AAD-specific. This defense is coherent but requires the meta-segment to state it clearly.
- **Full scope analysis outside categorical distributions.** The reframe is stated for categorical exponential families. For Gaussian families (Kalman), the Fenchel-Bregman picture also applies (with Mahalanobis-norm Bregman on the mean-covariance manifold); this spike has not worked through the Gaussian case in detail. The `#gain-sector-bridge` matrix-Kalman row is expected to fit but has not been explicitly verified here.

### §9.3 What I did not attempt

- **Deriving the three axioms from a single deeper commitment.** If such a derivation existed, the reframe would move from "axioms converge on one object" to "one axiom forces one object with multiple surface expressions." This would be a strictly stronger claim and I did not pursue it. The candidate deeper commitment would be something like "AAD's probabilistic architecture commits to exponential-family representability"; whether this is derivable from existing AAD commitments or would need to be added as a new axiom is a separate spike. The conservative reading — axioms are independent and happen to converge — is the one defended here.
- **Connecting to the monotone-operator-theory lineage** (Rockafellar / Bauschke-Combettes) invoked in `#sector-persistence-template`. Bregman divergences sit inside monotone-operator theory (convex-analytic duality is a special case of monotone-operator duality); the three meta-segments (`#additive-coordinate-forcing`, `#identifiability-floor`, `#separability-pattern`) plus `#sector-persistence-template` might all share a deeper convex-analytic common substrate. This is speculative and not pursued in this spike.

---

## §10 — References invoked

**Legendre-Fenchel / Bregman divergence foundations:**
- Rockafellar, R. T. 1970. *Convex Analysis.* Princeton University Press (§26 Legendre functions; §12 Fenchel conjugacy).
- Bauschke, H. & Combettes, P. 2017. *Convex Analysis and Monotone Operator Theory in Hilbert Spaces.* Springer, 2nd ed. (§13 on Bregman distances).
- Bregman, L. M. 1967. "The relaxation method of finding the common point of convex sets and its application to the solution of problems in convex programming." *USSR Comp. Math. and Math. Physics* 7(3):200–217.

**Information geometry (standard framework for the reframe):**
- Amari, S. & Nagaoka, H. 2000. *Methods of Information Geometry.* AMS / Oxford University Press. (§3.5 for dual potentials and Fisher-as-Hessian; Theorem 3.5; Eq. 3.77; Proposition 3.9 and 3.10 for product-family additivity; §3.7 for statistical-manifold product structure.)
- Amari, S. 2009. "α-divergence is unique, belonging to both f-divergence and Bregman divergence classes." *IEEE Trans. Info. Theory* 55(11):4925–4931.
- Ay, N., Jost, J., Lê, H. V. & Schwachhöfer, L. 2017. *Information Geometry.* Springer (Theorem 5.1 on Čencov's theorem in the exponential-family case).
- Eguchi, S. 1983. "Second order efficiency of minimum contrast estimators in a curved exponential family." *Annals of Statistics* 11(3):793–803 (§2 on f-divergence → Fisher-metric-at-second-order).

**Čencov / invariance route:**
- Čencov, N. N. 1982. *Statistical Decision Rules and Optimal Inference.* Translations of Mathematical Monographs 53. AMS.
- Morozova, E. & Chentsov, N. 1991. "Markov invariant geometry on state manifolds." *Itogi Nauki i Tekhniki* (trans. in *J. Sov. Math.* 56(5):2648–2669).

**Cauchy functional equation / axiomatic uniqueness (existing AAD references):**
- Aczél, J. 1966. *Lectures on Functional Equations and Their Applications.* Academic Press (§2.1 on the Cauchy functional equation).
- Aczél, J. & Daróczy, Z. 1975. *On Measures of Information and Their Characterizations.* Academic Press.
- Hobson, A. 1969. "A new theorem of information theory." *J. Stat. Phys.* 1(3):383–391.
- Csiszár, I. 1991. "Why least squares and maximum entropy? An axiomatic approach to inference for linear inverse problems." *Annals of Statistics* 19(4):2032–2066.
- Shore, J. E. & Johnson, R. W. 1980. "Axiomatic derivation of the principle of maximum entropy and the principle of minimum cross-entropy." *IEEE Trans. Info. Theory* 26(1):26–37.

**Direct AAD segment dependencies:**
- `#additive-coordinate-forcing` (the meta-segment under reframe)
- `#chain-confidence-decay` (anchor)
- `#strategy-cost-regret-bound` (divergence-layer instance)
- `#edge-update-natural-parameter` (update-layer instance)
- `#agent-identity` (where (PI) is anchored)
- `#gain-sector-bridge` (Fisher-metric cases)
- `#identifiability-floor`, `#separability-pattern` (the sister meta-segments)
- `msc/spike-ib-purity-strategy-cost-strengthening-2026-04-24.md` (Path 7 source)
- `msc/spike-reverse-kl-uniqueness.md` (prior divergence-layer uniqueness spike)
- `msc/spike-jacobian-b1-strengthening.md` (prior metric-layer spike)

---

## Working Notes

- **On the conservative vs. aggressive unification framings.** The spike lands on a modified (A) framing that preserves axiom independence while naming the geometric convergence. A more aggressive framing would attempt to derive the three axioms from a single deeper AAD commitment (e.g., "exponential-family representability of the surrounding apparatus"). I judged that move to be speculative — whether such a deeper commitment can be identified from existing AAD segments is not clear from the current state. If a future spike does find such a derivation, the reframe would strengthen further to "one axiom → one object → four layer-surfaces."

- **On the Gaussian case.** The `#gain-sector-bridge` Fisher-metric row includes both exponential-family-in-natural-parameters (which is clearly the exponential-family Fenchel-Bregman structure) and matrix-Kalman (Gaussian). The Gaussian case also fits: on the Gaussian exponential family, the Fenchel-dual potential is the log-partition of the Gaussian family, the Bregman divergence is Gaussian KL, and the Fisher metric is the Hessian of the log-partition. A short Gaussian-case walkthrough would strengthen §2's scope analysis. Not done in this spike; flagged for potential follow-up.

- **On non-categorical, non-Gaussian statistical manifolds.** The reframe's strongest form applies to exponential-family manifolds. For curved families or non-parametric models, the Čencov route still produces a Fisher metric, but the Legendre-Fenchel structure does not apply in the same way. If AAD ever extends to curved families (e.g., for non-exponential-family logogenic-agent applications), the reframe would need a "curved-family extension" treatment. Out of scope here.

- **On the "independently-motivated" language.** The phrase "independently-motivated AAD-internal axioms" is load-bearing in the reframe. "Independently-motivated" means each axiom has its own AAD-internal justification (chain-rule additivity is motivated by `#chain-confidence-decay`-analog reasoning, etc.); it does NOT mean the axioms are orthogonal or uncorrelated. They are independent as logical statements but they co-vary: each is motivated by adjacent AAD commitments, which in turn are reinforced by one another across the architecture. The reframe should preserve this double meaning — axiomatically independent, architecturally correlated.

- **On the effort question.** Per CLAUDE.md strengthen-before-soften, effort/time is not an input to the recommendation. If the reframe is structurally more honest, the work to land it is the right work. This spike does not attempt to estimate the effort; it attempts to name the honest structure.

- **On the 4-candidate Instance-4 traffic jam.** §8 argues that the reframe resolves the jam by geometric typing — different candidates live on different Bregman geometries (exponential-family / Euclidean-squared-norm / coupling-architecture / not-Bregman) and so belong to different meta-patterns or no meta-pattern. The Čencov/Fisher-metric candidate (currently resident) stays, but as a layer-specific manifestation of the unified geometric object rather than a parallel fourth instance. The ρ-factorization / (AV) candidate, if pursued, opens a second parallel meta-pattern on squared-norm Bregman rather than fitting as an extension of this one.

- **On the second parallel meta-pattern possibility.** If (AV) is promoted (requires resolving the 2026-04-23 brainstorm cycle's obstruction), AAD would carry *two* Bregman-geometry meta-patterns: entropic (on categorical distributions, this segment's topic) and squared-norm (on variance-additive statistics, including Lyapunov quadratic and variance-additive composition). Whether these should be unified as "AAD's architecture commits to Bregman geometries with axiom-appropriate convex potentials" or kept separate is another scoping question for a future cycle. I have not pursued it.

- **On the convex-potentials-in-AAD-overall observation.** The reframe surfaces a broader observation: AAD uses three distinct convex potentials across its architecture — negative-entropy on categorical distributions (this meta-pattern), squared-norm on state-space (Lyapunov sector), and log-partition on exponential-family natural parameters (the dual of negative-entropy, which is the same potential pair as the first). A unified picture might emerge if AAD explicitly categorizes its Bregman-type structures. Speculative; not pursued.

- **On reviewing the axioms for redundancy one more time.** The axiom-independence claim (§1.4, §2.2) is important. I verified: chain-rule additivity operates on bivariate objects $D(P \Vert Q)$; evidential additivity operates on univariate coordinates $\psi(p)$; parameterization-invariance operates on the theory's predictions under coordinate change. These have different logical types (bivariate vs. univariate vs. meta-theoretic). I did not find a way to reduce them to a single axiom — each specifies a different structural requirement. The convergence on exponential-family geometry is therefore genuine structural convergence across independent constraints, not redundancy.

- **On the "strengthen before softening" posture applied here.** The obvious softening move would be: "Path 7 shows the divergence and update instances are dual; narrow the meta-segment to 1-anchor + 1-pair + 1-Čencov = 3 instances." The strengthening move — which is what this spike attempted — is to ask whether the structure is *even more* unified than Path 7 names (and whether less unified than Path 7 names). The answer in both directions: Path 7 is correctly identifying a real structural observation, but the structure is more than a pair-duality and less than a full reduction-to-one-axiom. The honest description is convergence-of-independent-axioms-on-one-geometric-object (reframe A with axiom-independence preserved). This is structurally *stronger* than the current 1-anchor-3-theorem framing (it names more structure) but *preserves* the axiom-independence story (it does not claim the axioms collapse to one). It is the strengthening the "strengthen-first" posture calls for.
