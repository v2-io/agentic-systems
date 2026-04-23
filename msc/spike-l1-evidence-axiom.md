---
status: draft-spike
date: 2026-04-22
author: opus-1m
topic: block-structured evidential-additivity axiom under correlated failures (L1'/L2)
relates_to:
  - edge-update-natural-parameter
  - additive-coordinate-forcing
  - credit-assignment-boundary
  - discussion-identifiability-floor
  - discussion-separability-pattern
  - strategy-dag (Correlation Hierarchy)
  - strategic-dynamics-derivation (Prop B.7)
  - strategy-cost-regret-bound (§6.1)
---

# Spike: Block-Structured Evidential-Additivity Axiom Under Correlated Failures

## Problem statement

The #edge-update-natural-parameter segment derives log-odds as the unique additive-evidence parameterization (up to positive affine) under the *evidential-additivity axiom*:

$$\psi(p_{\text{post}}) = \psi(p_{\text{prior}}) + g(y)$$

where $g$ depends only on the observation $y$, and the underlying Bernoulli channel has likelihood ratio $P(y \mid H_1)/P(y \mid H_0)$ treated as *independent* across updates. When the edge credences $\{p_{ij}\}$ sit on a DAG with causally-insufficient topology — that is, when sibling edges share a latent common cause $C$ (L1' regime in #strategy-dag) — the observations $(y_j, y_k)$ generated along two sibling edges $(\cdot, j)$ and $(\cdot, k)$ are *not* independent. The Bayesian update is not the concatenation of two per-edge Bernoulli updates; it is a coupled mixture update.

The independent-evidence axiom is literally false in L1'. If the log-odds coordinate's uniqueness rests on that axiom, what happens structurally when the axiom fails? Two possible outcomes shape the landing:

- **Positive.** An AAD-internally-motivated block-structured additivity axiom (evidence decomposes additively *across* correlation clusters, with some within-cluster coupling) admits a Cauchy-FE-style uniqueness derivation. The forced coordinate becomes *vector-valued* log-odds on a quotient graph — one coordinate per cluster. This would be a genuine third theorem in #additive-coordinate-forcing, matching its 1-anchor-plus-2-theorem shape at a new layer.
- **Negative.** The axiom is ambiguous between multiple forms, or each form forces a different coordinate, or the relevant axiom is not AAD-internally motivated (it has to be imported from Bayesian-network sufficient-statistic theory or exponential-family naturality). Then the result is a new *instance of the identifiability floor* — name the external theorem (Cauchy-FE on what axiom? Markov-invariance from Čencov? the Aczél-Daróczy system?), name what cannot be forced without importing more than AAD motivates internally, and name the unique escape (observability of $C$ per Prop B.7 — already on the books).

Either outcome is useful. The spike attempts the positive branch with honest accounting; the negative-result branch is structured as the fallback.

This matters for #credit-assignment-boundary, where the default signal function is stated in log-odds. If L1'/L2 pushes the correct coordinate to vector-valued log-odds on the quotient graph, the signal function's native coordinate is richer than "log-odds per edge" — it is log-odds on clusters with a within-cluster correlation parameter. The #credit-assignment-boundary segment currently lands L1 at "gradient signal still has directional fidelity on average; principled fix is L1 augmentation" — a working-notes-grade fix. A principled L1' signal function would close that gap.

## Map of the spike

- §1 — State the independent-evidence axiom again carefully; identify exactly where L1' breaks it.
- §2 — Define block-structured additivity and run the Cauchy-FE argument. Positive result: vector-valued log-odds on the quotient graph, scalar log-odds per cluster, matching reduction for singletons.
- §3 — Within-cluster correlation parameter $\rho$: does it interpolate smoothly between L0 (independent) and a fully-coupled regime? What functional equation governs it?
- §4 — Relation to Hobson / Csiszár / Shore-Johnson on the divergence side. The sister reverse-KL theorem rests on chain-rule additivity; does a block-wise chain rule hold?
- §5 — Negative-result branch. What breaks in the positive-result derivation if pushed naively? Shore-Johnson's system-independence axiom is the clearest friction point; this is where the negative branch is strongest.
- §6 — Does block-additivity motivate AAD-internally? Parallel to the independent-evidence axiom's chain-layer analog.
- §7 — Lift attempt to L2 (non-latent-common-cause correlation structure).
- §8 — Candidate landing — new appendix segment, extension of #edge-update-natural-parameter, or new #discussion-identifiability-floor instance.
- §9 — Epistemic assessment per tier.

## §1 — Where the independent-evidence axiom breaks

### §1.1 Restatement of the axiom and what it assumes

From #edge-update-natural-parameter, the independent-evidence axiom states:

*[Assumption (evidential-additivity)]*

$$\psi(p_{\text{post}}) = \psi(p_{\text{prior}}) + g(y)$$

with $g: \{0,1\} \to \mathbb{R}$ depending only on the observation $y$ — not on $p_{\text{prior}}$ nor on observation history. The underlying generative model is: each Bernoulli observation is generated independently from a channel with fixed likelihood ratio, and the posterior is the Bayesian update against this channel.

The axiom has three implicit commitments:

(I1) **Single-coordinate sufficiency.** Posterior belief over the edge is summarized by a single scalar $\psi(p)$. The posterior is NOT a richer object (e.g., a Beta distribution tracking both mean and uncertainty, or a joint distribution over $(p_{ij}, p_{ik})$).

(I2) **Likelihood factorization.** For two observations $y_1, y_2$: $P(y_1, y_2 \mid H) = P(y_1 \mid H) P(y_2 \mid H)$. Under this factorization the log-likelihood-ratio is additive: $\ell(y_1, y_2) = \ell(y_1) + \ell(y_2)$. This is *observation-level* independence; conditional on the hypothesis, observations are iid.

(I3) **Per-edge locality.** The update to edge $(i,j)$ depends only on observations associated with that edge, not on observations associated with sibling edges $(i,k)$. This is a *parameter-level* independence: even if observations on two channels tell the agent something about both edges, the single-edge axiom treats them as if they informed only the edge they were collected on.

### §1.2 What L1' breaks

Under L1' with binary common cause $C$ and soft-facilitator children $j, k$ sharing $C$:

- The per-child likelihood $P(y_j = 1)$ is the mixture $\mu_j = \theta_C \theta_{j\mid C} + (1-\theta_C)\theta_{j\mid \neg C}$. Under the three-parameter vector $\phi_j = (\theta_C, \theta_{j\mid C}, \theta_{j\mid \neg C})$ this *is* still a single Bernoulli channel on $y_j$.
- But observations $y_j$ and $y_k$ are marginally *coupled* — they are independent conditional on $C$ but not marginally. $P(y_j, y_k) \neq P(y_j)P(y_k)$ in general. Specifically, $P(y_j = 1, y_k = 1) = \theta_C \theta_{j\mid C}\theta_{k\mid C} + (1-\theta_C)\theta_{j\mid\neg C}\theta_{k\mid\neg C}$ which differs from $\mu_j \mu_k$ by $\theta_C(1-\theta_C)(\theta_{j\mid C} - \theta_{j\mid\neg C})(\theta_{k\mid C} - \theta_{k\mid\neg C}) = \theta_C(1-\theta_C)\Delta_j\Delta_k$ — the separability gaps multiplied by the $C$-Bernoulli variance. This is the familiar latent-factor positive correlation when $\Delta_j, \Delta_k$ have the same sign.

Relative to the three axiom commitments:

- (I1) fails if we try to summarize the joint posterior over $(p_{ij}, p_{ik})$ by a scalar per edge. The correlation is a separate degree of freedom.
- (I2) fails at the observation level whenever $\Delta_j \neq 0$ and $\Delta_k \neq 0$ and they have the same sign (positive correlation) or opposite (negative correlation). Specifically, $\ell(y_j, y_k) \neq \ell(y_j) + \ell(y_k)$ in the mixture model.
- (I3) fails because observation $y_j$ updates not only $\hat p_j$ but also — through the $C$ channel — $\hat\theta_C$, which in turn updates $\hat p_k = \theta_C p_{k\mid C} + (1-\theta_C)p_{k\mid\neg C}$. Information flows between siblings via $C$.

So all three implicit commitments of the independent-evidence axiom fail in L1'. The question is whether a weaker axiom that respects block structure forces a unique coordinate in the same way.

### §1.3 The quotient-graph idea

The natural weakening. If we partition edges into *correlation clusters* $C_1, \ldots, C_m$ under an equivalence relation "shares a latent common cause with," then:

- Within a cluster, the observations are coupled via the shared latent.
- Between clusters (by construction of the partition — clusters are maximal sets sharing latents), observations *are* independent.

Evidence *across clusters* should still be additive (each cluster's posterior is independent of the others). What the cluster-level coordinate looks like, and what within-cluster coordinates survive, are the two quantities to derive.

This is the partition structure underlying **block-additivity**: additivity at the level of blocks (clusters), with within-block structure encoding the shared-latent coupling.

## §2 — Block-additive axiom and the Cauchy-FE argument

### §2.1 Statement

Let the edges $E = \{(i,j)\}$ of the strategy DAG be partitioned into $m$ disjoint blocks $\mathcal{C}_1, \ldots, \mathcal{C}_m$ under a "shares a latent common cause with" equivalence relation. Let $\mathbf{p}_\alpha = (p_{ij})_{(i,j) \in \mathcal{C}_\alpha} \in (0,1)^{|\mathcal{C}_\alpha|}$ denote the block-$\alpha$ credence vector. Posit: there exists a smooth coordinate $\Psi_\alpha: (0,1)^{|\mathcal{C}_\alpha|} \to \mathbb{R}^{k_\alpha}$ (with $k_\alpha$ to be determined) such that

*[Assumption (block-additivity axiom)]*

$$\Psi_\alpha(\mathbf{p}_\alpha^{\text{post}}) = \Psi_\alpha(\mathbf{p}_\alpha^{\text{prior}}) + G_\alpha(\mathbf{y}_\alpha)$$

where $G_\alpha : \mathcal{Y}_\alpha \to \mathbb{R}^{k_\alpha}$ depends only on the observations $\mathbf{y}_\alpha$ collected *within* cluster $\alpha$. The coordinate $\Psi = (\Psi_1, \ldots, \Psi_m) : (0,1)^{|E|} \to \mathbb{R}^{\sum_\alpha k_\alpha}$ summarizes the block-structured posterior on a fixed-dimensional state; $G = (G_1, \ldots, G_m)$ depends on observations only (not on prior state). Different clusters' coordinates evolve additively and independently under their respective observations.

Two sub-questions:

(Q1) Is the block-additive axiom AAD-internally motivated, or imported?
(Q2) What is the functional-equation consequence — is the coordinate $\Psi$ uniquely forced, and is it logarithmic?

### §2.2 Step 1 — Inter-cluster structure

Fix $\alpha \neq \beta$. Consider a sequence of observations in which the first $n$ observations lie in cluster $\alpha$ and the next $n'$ lie in cluster $\beta$. Because the clusters share no latents (by construction of the partition), the $\alpha$-observations update only $\Psi_\alpha$ and the $\beta$-observations update only $\Psi_\beta$:

$$\Psi_\alpha(\mathbf{p}_\alpha^{n+n'}) = \Psi_\alpha(\mathbf{p}_\alpha^{0}) + \sum_{t=1}^n G_\alpha(\mathbf{y}_\alpha^{(t)})$$

$$\Psi_\beta(\mathbf{p}_\beta^{n+n'}) = \Psi_\beta(\mathbf{p}_\beta^{0}) + \sum_{t=n+1}^{n+n'} G_\beta(\mathbf{y}_\beta^{(t)})$$

This is not a constraint — it is a restatement of the block-additivity axiom for each cluster in isolation. The interesting constraint comes from within-cluster structure.

### §2.3 Step 2 — Within-cluster: reducing to the mixture Fisher structure

Focus on one cluster $\alpha$ with $K$ children sharing a single binary latent $C$. Parameters of the block: $\phi = (\theta_C, \theta_{1\mid C}, \theta_{1\mid\neg C}, \theta_{2\mid C}, \theta_{2\mid\neg C}, \ldots, \theta_{K\mid C}, \theta_{K\mid\neg C})$. This is a $2K+1$-dimensional parameter space. Observations: $\mathbf{y}_\alpha = (y_1, \ldots, y_K)$ per trial; if $C$ is observable per trial, we additionally have $c \in \{0,1\}$.

**Case A — $C$ observable per trial.** The likelihood factorizes:

$$P(\mathbf{y}_\alpha, c \mid \phi) = P(c \mid \theta_C) \cdot \prod_{k=1}^K P(y_k \mid c, \theta_{k\mid c})$$

This is a product of $K+1$ independent Bernoulli likelihoods (one for $c$, then one for each $y_k$ conditioned on the observed $c$). The Bayesian update becomes:

$$\log\frac{\theta_C^{\text{post}}}{1-\theta_C^{\text{post}}} = \log\frac{\theta_C^{\text{prior}}}{1-\theta_C^{\text{prior}}} + \ell_C(c)$$

$$\log\frac{\theta_{k\mid 1}^{\text{post}}}{1-\theta_{k\mid 1}^{\text{post}}} = \log\frac{\theta_{k\mid 1}^{\text{prior}}}{1-\theta_{k\mid 1}^{\text{prior}}} + \mathbb{1}[c=1] \cdot \ell_{k\mid 1}(y_k)$$

(and symmetrically for $\theta_{k\mid 0}$ using $\mathbb{1}[c=0]$). This is $2K+1$ independent scalar log-odds coordinates, each updating additively by its own log-likelihood ratio. The Aczél uniqueness theorem (one coordinate at a time) forces each component to be log-odds up to positive affine. Composition: the block coordinate $\Psi_\alpha$ is forced to be

$$\Psi_\alpha(\phi) = \bigl(\lambda_C,\; \lambda_{1\mid 0}, \lambda_{1\mid 1},\; \ldots,\; \lambda_{K\mid 0}, \lambda_{K\mid 1}\bigr) \in \mathbb{R}^{2K+1}$$

with $k_\alpha = 2K+1$ and each $\lambda = \log(\theta/(1-\theta))$.

*[Derived (Conditional on block-additivity axiom under observable $C$; product-of-independent-Bernoullis factorization)]* Under observable $C$, block-additivity forces the coordinate $\Psi_\alpha$ to be the $(2K+1)$-dimensional log-odds vector on the *conditional* parameters.

*Key observation.* The block coordinate is NOT one log-odds per edge ($K$-dimensional) and is NOT one log-odds per cluster (1-dimensional). It is $(2K+1)$-dimensional — one per *conditional* regime, with the $C$-parameter's log-odds as a shared coordinate. The per-edge marginal credence $\hat p_k = \theta_C\theta_{k\mid 1} + (1-\theta_C)\theta_{k\mid 0}$ is a *derived* quantity (a non-log-linear combination of the block coordinates); it is not itself additive under block observations.

This is consistent with the #strategic-dynamics-derivation Prop B.7 state representation, which uses $(\theta_C, \{\theta_{k\mid C}\}, \{\theta_{k\mid \neg C}\})$ as the joint state — an affine image of the log-odds vector under each component's sigmoid-exp.

**Case B — $C$ unobservable.** The likelihood does NOT factorize across $C$:

$$P(\mathbf{y}_\alpha \mid \phi) = \sum_{c \in \{0,1\}} P(c \mid \theta_C) \prod_{k=1}^K P(y_k \mid c, \theta_{k\mid c})$$

This is a *mixture* over $c$, not a product. The log-likelihood is:

$$\log P(\mathbf{y}_\alpha \mid \phi) = \log\Bigl[ \theta_C \prod_k \theta_{k\mid 1}^{y_k}(1-\theta_{k\mid 1})^{1-y_k} + (1-\theta_C)\prod_k \theta_{k\mid 0}^{y_k}(1-\theta_{k\mid 0})^{1-y_k}\Bigr]$$

The score function of this log-likelihood does not decompose into a sum of per-parameter pieces. Specifically, the score for $\theta_C$, $\theta_{k\mid 1}$, and $\theta_{k\mid 0}$ all depend nonlinearly on the whole observation vector through the posterior $P(c \mid \mathbf{y}_\alpha, \phi)$ (the soft-EM responsibility).

Consequence: if we impose block-additivity $\Psi_\alpha(\phi^{\text{post}}) = \Psi_\alpha(\phi^{\text{prior}}) + G_\alpha(\mathbf{y}_\alpha)$ with $G_\alpha$ depending only on the observation $\mathbf{y}_\alpha$ — then the functional equation has no solution in the generic case for any $k_\alpha \geq 1$, because the posterior $\phi^{\text{post}}$ depends on the *prior* $\phi^{\text{prior}}$ nonlinearly via the responsibility weights. That is:

$$\phi^{\text{post}}_{k\mid 1} = \phi^{\text{prior}}_{k\mid 1} + \frac{r(y_k, \mathbf{y}_{-k}, \phi^{\text{prior}})}{n_{k\mid 1}+1}(y_k - \phi^{\text{prior}}_{k\mid 1})$$

where $r$ is the soft-EM responsibility, which depends on $\phi^{\text{prior}}$ itself. So $\Psi_\alpha(\phi^{\text{post}}) - \Psi_\alpha(\phi^{\text{prior}})$ is *not* a function of observations alone — it is a function of observations AND prior.

**Result.** Under unobservable $C$, the block-additivity axiom is *inconsistent* (no $\Psi_\alpha$ satisfies it for the true Bayesian update), not merely weaker. This is not "multiple coordinates compatible with the axiom"; it is "no coordinate compatible with the axiom because the true Bayesian update on the mixture does not have the axiomatic form."

*[Derived (No-go: block-additivity fails under unobservable $C$, from the nonlinear responsibility dependence of the mixture posterior)]*

This is a structural result: it explains why the Cauchy-FE argument cannot give us a log-odds coordinate in the unobservable-$C$ regime, matching the Cramér-Rao refutation in Prop B.7 from a different direction. It generalizes: whenever a posterior update depends on the prior nonlinearly through a mixture responsibility (or any non-sufficient statistic), the additivity axiom $\Psi_{\text{post}} = \Psi_{\text{prior}} + G(\text{observation})$ is inconsistent with the true Bayes rule.

### §2.4 Step 3 — Reduction to singletons

When a cluster $\alpha$ is a singleton (one child, no latent — i.e., the edge is independent of all other edges), the block structure collapses: $K=1$, no $C$, $k_\alpha = 1$, and the coordinate reduces to a single scalar log-odds per edge. This matches #edge-update-natural-parameter's univariate result exactly.

The reduction also makes the dimension formula $k_\alpha = 2K+1$ interpretable. A cluster with $K=1$ (single child with a latent) has $k_\alpha = 3$ (the two conditional credences plus $\theta_C$), one more coordinate than the naive per-edge count of 1. The "extra" coordinate is the latent — and it's there whether or not the edge has siblings in the cluster, as long as the posterior depends on $C$ at all. This foreshadows §5's negative-result branch: the block dimension tracks the *parameter* count of the joint model, not the *edge* count.

### §2.5 Summary of §2

| Regime | $\Psi_\alpha$ dim | Forced shape | Method |
|---|---|---|---|
| Independent (singleton cluster) | 1 per edge | scalar log-odds | #edge-update-natural-parameter |
| L1' with observable $C$ | $2K+1$ per cluster | log-odds on conditional regimes | §2.3 Case A (product factorization + Aczél per coordinate) |
| L1' with unobservable $C$ | — | no solution | §2.3 Case B (nonlinear responsibility kills the axiom) |

So the positive result holds in observable-$C$: the coordinate IS forced, and it IS logarithmic — just higher-dimensional than the naive "log-odds per edge" would suggest. The negative result holds in unobservable-$C$: the axiom is *inconsistent*, structurally parallel to the Cramér-Rao floor from the Fisher-information side.

The positive case requires observable $C$ — which is the same structural precondition that Prop B.7 requires. The two results (this section's block-Cauchy-FE and Prop B.7's sector transfer) share a scope boundary.

## §3 — Within-cluster correlation parameter ρ

### §3.1 The interpolation question

The user's Angle 3 conjecture: within-cluster, a correlation parameter $\rho$ interpolates between L0 ($\rho = 0$, per-edge scalar log-odds) and a fully-coupled regime ($\rho = 1$, one log-odds per cluster).

Under the Case A analysis above, this is structurally misleading. The observable-$C$ coordinate is NOT one log-odds per cluster (that would be 1-dimensional); it is $(2K+1)$-dimensional. The coordinate doesn't "interpolate" between $K$-dimensional (L0) and 1-dimensional (fully coupled) — it gets *larger* under correlation, not smaller.

Why? Because the block structure retains full information about each conditional regime. The shared latent doesn't reduce the degrees of freedom; it adds one (the latent's own credence) while leaving the conditional credences as distinct coordinates.

### §3.2 A parameterization where $\rho$ is meaningful

The one natural correlation parameter on $(K=2, \text{observable } C)$ is $\text{Cov}(y_j, y_k) = \theta_C(1-\theta_C)\Delta_j\Delta_k$ where $\Delta_j = \theta_{j\mid 1} - \theta_{j\mid 0}$. The coupling strength between siblings is $|\Delta_j \Delta_k|$: separability gaps product. This is a *derived* quantity from the block coordinates, not a free parameter.

- $\Delta_j \to 0$: sibling $j$ becomes conditionally independent of $C$ (trivial block; reduces to L0 on that sibling).
- $|\Delta_j|\uparrow 1$: $j$ is strongly coupled to $C$.

Under $\Delta_j \to 0$, the block coordinate's $\theta_{j\mid 1}$ and $\theta_{j\mid 0}$ components collapse to a single value — effectively reducing $k_\alpha$ by 1 (the degenerate direction). So the $\rho$-interpolation corresponds to the degenerate/nondegenerate boundary of the mixture, *not* a continuous dimension reduction.

**Refutation of the conjecture.** The structural answer in §2 leaves no room for $\rho$ as a smooth interpolator on the coordinate's dimension. Either the block has $K$ independent edges ($k_\alpha = K$, each its own log-odds) or it has a shared latent with $K$ children ($k_\alpha = 2K+1$ under observable $C$, no consistent coordinate under unobservable $C$). The jump from $K$ to $2K+1$ is *discrete*: adding a latent adds the latent's credence plus one extra conditional credence per child.

*[Derived (no-go for $\rho$-continuous interpolation of the forced-coordinate dimension, from the block-Cauchy-FE structure)]*

This is a genuinely non-obvious result. The intuition that "correlation strength smoothly parameterizes the coordinate" is wrong; the coordinate is piecewise-constant in dimension with discrete jumps at each addition of a shared latent.

### §3.3 What $\rho$ DOES parameterize

$\rho$ interpolates the *Fisher information* of the marginal channel. Under unobservable $C$, the per-trial Fisher matrix has rank 1 with leading eigenvalue proportional to $|\Delta_j|^2$ (the separability-gap energy); see Prop B.7's rank-1 factorization $\mathcal{F} = uu^T/(\mu_j(1-\mu_j))$ with $u = (\Delta_j, \theta_C, 1-\theta_C)$. The identifiable direction has curvature $|\Delta_j|^2$; the null directions (the indeterminacy manifold) have zero curvature.

So $\rho$ (specifically $|\Delta_j|$) parameterizes *how much of the $(2K+1)$-dimensional block is identifiable from marginals*:
- $|\Delta_j| \to 0$: zero identifiability on any of the conditional parameters (Cramér-Rao bound is infinite everywhere).
- $|\Delta_j| \to 1$: one direction is identifiable; $2K$ remain in the Cramér-Rao null space.

Under any finite $|\Delta_j|$, only the marginal $\mu_j$ is identifiable from single-channel observations; the $2K$ conditional coordinates are underdetermined.

**Read.** $\rho$ is not a coordinate-dimension interpolator; it is a Fisher-rank-identifiability scaling parameter for the marginal channel. The block coordinate is $(2K+1)$-dimensional in the Bayesian/axiomatic sense; what changes with $\rho$ is the Fisher-information floor on how much of that coordinate can be estimated from a given channel.

### §3.4 Connection to the identifiability-floor pattern

This §3.3 read places $\rho$ inside the identifiability-floor structure of Instance 2. The Cauchy-FE axiomatic analysis (this spike's §2) and the Fisher-information analysis (Prop B.7) both live at the same block coordinate $\mathbb{R}^{2K+1}$; the Cauchy-FE view tells you what the coordinate *is*, and the Fisher view tells you how much of it is *estimable*. The $\rho$-parameter governs the Fisher-information story, not the Cauchy-FE story.

## §4 — Relation to Hobson / Csiszár / Shore-Johnson

### §4.1 The chain-rule analog question

The divergence-layer companion theorem in #strategy-cost-regret-bound §6.1 rests on the chain-rule additivity axiom:

$$D_f(P_{XY}\Vert Q_{XY}) = D_f(P_X\Vert Q_X) + \mathbb{E}_{P_X}[D_f(P_{Y\mid X}\Vert Q_{Y\mid X})]$$

Forcing $f(t) = c\cdot t\log t$ (reverse-KL up to scaling) via Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980.

The evidential-additivity axiom is the update-layer analog. What's the block-additivity analog on the divergence side?

**Candidate.** For a cluster-partitioned joint distribution $P = \prod_\alpha P_\alpha$ (joint factored over clusters — "inter-cluster" independence by construction), a divergence should decompose:

$$D_f(P\Vert Q) = \sum_\alpha D_f(P_\alpha \Vert Q_\alpha)$$

when $Q$ also factors across clusters. This is the *product* or *system-independence* axiom (Shore-Johnson 1980 Axiom II, p.28) — distinct from the chain-rule axiom but closely related. For independent subsystems, the cross-entropy sums.

Shore-Johnson Axiom II states: "If a system has a density $P$ that can be factored as the product of independent subsystem densities, the principle of minimum cross-entropy should reproduce the subsystem densities when applied to each subsystem separately."

**Status of this axiom.** Shore-Johnson 1980 prove that Axiom II (along with three others) uniquely characterizes Kullback-Leibler cross-entropy as the minimum-cross-entropy update principle. So there IS a divergence-layer analog: the system-independence axiom is the block-additivity axiom stated at the level of distributions rather than credences. It forces reverse-KL as the unique divergence up to scaling, same answer as the chain-rule axiom (the two are logically connected but formally distinct).

### §4.2 Shore-Johnson subset-independence as the block-axiom analog

Shore-Johnson's Axiom III (subset independence, p.28 of the IEEE Info. Theory paper) is actually the closer analog. It states: "If information about one subset is combined with information about another, non-overlapping subset, the resulting conditional probability density function should be the same as if the information had been considered separately."

This is exactly block-additivity at the distribution level: non-overlapping subsets (= our clusters) combine additively in the cross-entropy. Shore-Johnson prove that KL is the unique choice under Axioms I–IV (uniqueness, invariance, system-independence, subset-independence).

### §4.3 Does the block-additivity axiom for credences Case-A-force log-odds via the same route?

The observable-$C$ case decomposes the block likelihood as a product of $2K+1$ independent Bernoullis. Under a product-of-independent-Bernoullis, the Shore-Johnson derivation of KL applies *per coordinate*, and by the Aczél 1966 functional-equation argument the update-layer log-odds is forced per coordinate. These are two different theorems living on the same product structure:

- **Shore-Johnson / Hobson / Csiszár** force the *divergence* between the joint distribution and its target to be KL.
- **Aczél's Cauchy-FE** argument forces the *credence coordinate* on which evidence adds up to be log-odds.

Under the product structure, these coincide: reverse-KL on the product distribution equals the sum of per-factor reverse-KLs, and each factor's log-odds is the natural parameter of that factor's Bernoulli. So Case A is doubly-covered: the positive result can be derived either from the block-wise evidential-additivity axiom (per-coordinate Aczél) or from the Shore-Johnson subset-independence axiom applied at the distribution level.

**The parallel is deep.** At both the update and divergence layers, the positive result in the factorizable regime is:

| Layer | Axiom | Forced coordinate |
|---|---|---|
| Divergence, independent | Chain-rule or system-independence | reverse-KL |
| Divergence, block (observable $C$) | Subset independence on cluster-factorized $P$, $Q$ | reverse-KL per cluster factor, additively |
| Update, independent | Evidential additivity | log-odds per edge |
| Update, block (observable $C$) | Block evidential additivity on cluster-factorized likelihood | $(2K+1)$-dim log-odds per cluster |

So the block-additivity version of the update axiom recovers the same logarithmic coordinate, just at higher dimension. **And** the Shore-Johnson-style divergence-layer version also recovers KL, same coordinate.

### §4.4 Does a chain-rule analog hold block-wise?

The chain rule $D_f(P_{XY}\Vert Q_{XY}) = D_f(P_X\Vert Q_X) + \mathbb{E}_{P_X}[D_f(P_{Y\mid X}\Vert Q_{Y\mid X})]$ generalizes to any conditional decomposition. For the block structure under observable $C$:

$$D_{\mathrm{KL}}(P_{\mathbf y, c}^\ast \Vert Q_{\mathbf y, c}^\Sigma) = D_{\mathrm{KL}}(P_c^\ast \Vert Q_c^\Sigma) + \mathbb{E}_{c\sim P^\ast}\Bigl[D_{\mathrm{KL}}(P_{\mathbf y \mid c}^\ast \Vert Q_{\mathbf y \mid c}^\Sigma)\Bigr]$$

and the inner term further decomposes by per-child conditional independence:

$$= D_{\mathrm{KL}}(P_c^\ast \Vert Q_c^\Sigma) + \mathbb{E}_c\Bigl[\sum_k D_{\mathrm{KL}}(P_{y_k \mid c}^\ast \Vert Q_{y_k \mid c}^\Sigma)\Bigr]$$

This is block-wise chain rule: the divergence decomposes into the latent-level divergence plus the expected per-child conditional divergence. Under observable $C$, the chain-rule axiom applies directly. Under unobservable $C$, the chain decomposition fails — the joint marginal $P(\mathbf{y})$ cannot be factored through the unobserved latent $C$ without introducing an integrated term that is not a per-observation divergence.

This matches §2.3 Case B: under unobservable $C$, the structural decomposition fails on both the update side (no additive coordinate) and the divergence side (no chain-rule factorization through $C$).

### §4.5 Under unobservable $C$ — Shore-Johnson friction

Shore-Johnson's subset-independence axiom is satisfied when subsets truly are independent (i.e., the joint factors). Under the marginal mixture $P(\mathbf{y}) = \sum_c P(c)\prod_k P(y_k\mid c)$ with $C$ unobservable, the marginal $P(\mathbf{y})$ does *not* factor across $k$ — children are correlated through the unobserved latent. So Shore-Johnson's subset-independence axiom is false for the marginal distribution.

If we posit block-additivity at the *observation* level (subset independence of the children as observed) in the unobservable-$C$ regime, the axiom is imposing a constraint that contradicts the underlying generative model. Either:

- (a) the axiom is accepted, and the agent's divergence calculation is inconsistent with Bayesian updates (the agent is using KL on an assumed-factorized distribution that doesn't actually factor — this is an approximation, not a derivation); or
- (b) the axiom is rejected, and we leave the unobservable-$C$ regime outside the Shore-Johnson uniqueness result.

Option (b) is the honest posture. It matches the Cramér-Rao refutation in Prop B.7: under unobservable $C$, there is no Bayesian-coherent way to treat the block as factorized; the mixture identifiability obstruction is structural.

### §4.6 Summary of §4

- **Observable $C$.** Block-additivity (at update or divergence layer) works via factorization, forces log-odds at the update level and reverse-KL at the divergence level, each $(2K+1)$-dimensional per cluster.
- **Unobservable $C$.** The axioms fail. The update-level axiom is inconsistent (§2.3 Case B); the divergence-level subset-independence axiom is false for the marginal (§4.5). Both sides refuse the factorization. This converges on the identifiability-floor reading.

## §5 — Negative-result branch

The strongest negative-result formulation. Even in the observable-$C$ case where positive results hold, the block-additivity axiom has a subtle failure mode worth naming.

### §5.1 What "AAD-internally motivated" requires

Per #additive-coordinate-forcing's 1-anchor-plus-2-theorem characterization: an axiom is AAD-internally motivated if it is an analog (at a new layer) of #chain-confidence-decay's chain-rule identity. The existing axioms:

- **Chain-rule additivity** (divergence layer): analog of "log-confidence decomposes additively along the DAG" (#chain-confidence-decay) at the divergence level.
- **Evidential additivity** (update layer): analog of the same chain-layer identity, at the update level.

Both are motivated because the chain layer is a mathematical identity via the probability chain rule, and the two theorem-layer axioms apply the *same* decomposition to a new quantity (divergence, credence).

**Block-additivity.** Does the block axiom have an analogous AAD-internal motivation? Candidates:

- (C1) "Confidence along a cluster decomposes additively into per-member contributions." This is FALSE for clusters with shared latents — the whole point of L1' is that cluster-members are NOT independent, so their confidences do NOT decompose additively (they decompose multiplicatively conditional on the latent, not per-member additively). So (C1) is NOT the analog.
- (C2) "Across clusters, confidence decomposes additively (clusters are independent by construction)." This is TRUE and IS the analog. The chain rule operates on causally-independent factors; the block axiom operates on correlation-partition-independent factors. Both say "independent pieces contribute additively on the log scale."
- (C3) "Within a cluster, given the latent, confidence decomposes additively." This is also TRUE conditionally. The chain rule on a fixed observed $C$-realization gives per-child additivity.

The (C2) motivation is AAD-internal and solid: given the DAG structure, the correlation partition is a structural feature, and independence across clusters follows from the partition's construction. (C3) is also AAD-internal: AAD's DAG factorization is exactly "conditional-independence-along-the-DAG," and conditional on the latent, per-child independence holds.

So the block-additivity axiom under observable $C$ is AAD-internally motivated at both the inter-cluster (C2) and intra-cluster (C3) levels. This justifies calling the result a "genuine third theorem" if we land it.

### §5.2 Where the motivation fails

Under *unobservable* $C$, the motivation (C3) is vacuous: we cannot condition on $C$ because we never observe it. The axiom becomes "confidence decomposes additively across children" — which is FALSE given the latent coupling. The AAD-internal motivation relies on either observing $C$ or on the chain rule operating in a conditional-independent decomposition that the agent can evaluate.

**The negative-result branch's crisp form.** The block-additivity axiom has AAD-internal motivation in the observable-$C$ regime only. In the unobservable-$C$ regime, there is no AAD-internal axiom that forces a unique coordinate. The positive result is scope-restricted.

This exactly parallels the scope restriction on the axiom in #edge-update-natural-parameter: the evidential-additivity axiom is stated for Bayesian-coherent sub-scope $\alpha$ (per #gain-sector-bridge), with non-Bayesian agents in sub-scope $\beta$ outside the uniqueness. Block-additivity under observable $C$ is a Bayesian-coherent extension; under unobservable $C$, the Bayesian posterior itself does not admit the additive form.

### §5.3 What is the unique escape from the unobservable-$C$ regime?

Three routes, recapitulating Prop B.7's repair routes:

- (R1) **Augment $C$-observability.** Move the cluster from unobservable-$C$ regime to observable-$C$ regime. This is an *information-augmentation* move — the same escape named by #discussion-identifiability-floor Instance 2.
- (R2) **Multi-child joint observation.** Observe $K \geq 2$ children jointly under the same $C$-realization. The joint Fisher matrix reaches rank $2K+1$ (Prop B.7 Repair (ii)); this is structurally equivalent to observing $C$ indirectly through its multi-child fingerprint. Still relies on observability of the joint structure at the trial level.
- (R3) **Plan-level fallback.** Track only the marginal $\hat\mu_j$, losing per-conditional diagnostics. This is L0-on-marginals; the block collapses to a product of independent marginal channels, and each channel's log-odds is forced by the standard Aczél result.

All three routes escape the unobservable-$C$ regime by either adding information (R1, R2) or projecting to a lower-dimensional space (R3) where the independent-evidence axiom applies without block structure.

### §5.4 The negative-result shape

The negative-result branch, stated as an #discussion-identifiability-floor instance candidate:

- **Setting.** Force a unique additive-evidence coordinate on an L1' cluster with unobservable common cause, using a block-additivity axiom analogous to #edge-update-natural-parameter's evidential-additivity axiom.
- **External theorem.** Cauchy's functional equation requires the domain transformations to commute with addition — i.e., the posterior update $\phi^{\text{post}}(\phi^{\text{prior}}, \mathbf{y})$ must have the form $\phi^{\text{post}} = T(\phi^{\text{prior}} + U(\mathbf{y}))$ for some $T$ and $U$. The mixture-posterior responsibility-reweighting update does not have this form.
- **No-go.** No smooth coordinate $\Psi_\alpha$ satisfies the block-additivity axiom for the true Bayesian update under unobservable $C$.
- **Boundary characterization.** Three escapes: $C$-augmentation, joint multi-child observation, plan-level marginal fallback. Each transforms the problem to a regime where the axiom holds.
- **Strengthened consequence.** Observability of the latent is structurally required — not merely convenient — for axiomatic uniqueness of the credence coordinate. This strengthens the same load-bearing claim as Prop B.7's Cramér-Rao floor: observability-of-$C$ as information-augmentation.

This *converges* with Instance 2 of #discussion-identifiability-floor rather than creating a fourth instance. Both obstructions have the same scope boundary (observable vs unobservable $C$), same repair routes, and same strengthened consequence (observability-of-$C$ as load-bearing). The contribution of this spike's negative branch is to show that the structural obstruction appears at *two independent layers* (Cauchy-FE uniqueness at the coordinate level; Cramér-Rao floor at the Fisher-information level) — strengthening the robustness of the floor.

## §6 — AAD-internal motivation check

### §6.1 Is block-additivity under observable $C$ a genuine third theorem in #additive-coordinate-forcing?

The 1-anchor-plus-2-theorem characterization requires:

- The chain-layer identity (#chain-confidence-decay) as anchor.
- Axiom-conditional theorems at other layers, motivated internally as analogs.

The two existing theorems are at the *divergence* layer and the *update* layer. Both are single-scalar results per coordinate (reverse-KL as a scalar, log-odds as a scalar). The block version would be at the *cluster* layer — a vector-valued coordinate on a block factor.

**Arguments for "genuine third theorem."**

- (P1) The observable-$C$ block axiom is AAD-internally motivated at both inter-cluster (C2) and intra-cluster (C3) levels (see §5.1). The motivation is the same chain-rule identity applied to a block-wise conditional factorization.
- (P2) The forced coordinate is logarithmic ($(2K+1)$-dimensional log-odds vector), matching the pattern's logarithmic-coordinate shape.
- (P3) The reduction to singleton clusters recovers #edge-update-natural-parameter exactly. So the block version is a *generalization*, not a parallel theorem.

**Arguments against.**

- (A1) The block version is *derived from* #edge-update-natural-parameter by per-coordinate application in a factored likelihood. It's not independent of the existing theorem; it's a consequence of applying it per-coordinate under a factorization. A "third theorem" should introduce new content, not just recapitulate the existing theorem on a larger factor space.
- (A2) The axiom (block-additivity) is arguably just "evidential additivity applied to each factor of a block-factorized likelihood," not a genuinely new axiom.
- (A3) The dimension bump from $K$ to $2K+1$ under a shared latent is information about the *model* (the mixture has one extra parameter per block for the latent's own credence), not information about the *coordinate* in a new sense. The Cauchy-FE argument still forces each scalar coordinate to be log-odds; nothing new at the functional-equation level.

**Honest read.** The block version is NOT a genuine third theorem in the #additive-coordinate-forcing pattern. It is an *extension* of #edge-update-natural-parameter to block-factorized likelihoods — a generalization of the existing theorem's scope, not a new uniqueness result at a new layer.

The landing for this spike should therefore be: extend #edge-update-natural-parameter with a block-structure generalization, rather than create a new segment. The extension clarifies what happens under L1'/L2 and names the observable-$C$ vs unobservable-$C$ scope boundary.

### §6.2 Does Case B (unobservable $C$) give a new identifiability-floor instance?

Case B shows that the block-additivity axiom is inconsistent with Bayesian updating under unobservable $C$. This is a structural no-go; does it warrant a standalone entry in #discussion-identifiability-floor, parallel to Instances 1 (CHT) and 2 (Cramér-Rao)?

**Candidate characterization for a new instance:**

- **Setting.** Force an additive-evidence coordinate on an L1' cluster under unobservable common cause.
- **External theorem.** Cauchy's functional equation has no smooth solution for a posterior update whose dependence on the prior is not translation-commuting.
- **No-go.** No axiomatic Cauchy-FE derivation forces a unique log-odds coordinate for the block under unobservable $C$.
- **Repair routes.** Same three as Prop B.7: $C$-augmentation, multi-child joint observation, plan-level marginal.
- **Strengthened consequence.** Observability-of-$C$ is required for Cauchy-FE-style coordinate uniqueness, not just for Cramér-Rao-style Fisher identifiability.

**Honest read.** This is NOT a new floor instance because the repair routes and strengthened consequence are identical to Instance 2. It is a *second-layer confirmation* of Instance 2 — the same observability-of-$C$ scope boundary obstructs both the Fisher-information story (Instance 2) and the Cauchy-FE coordinate story (this spike). The value is strengthening Instance 2 by showing it obstructs at two independent structural layers.

Better landing: a note added to #discussion-identifiability-floor Instance 2 observing the dual obstruction at the Cauchy-FE layer, strengthening the "this is structural, not a defect of one analytical route" reading. Not a new instance.

### §6.3 The spike's honest takeaways

- (T1) **Positive result is not a new theorem.** Observable-$C$ block-additivity is a per-coordinate application of #edge-update-natural-parameter under block factorization. Worth noting as an extension; not a third theorem in #additive-coordinate-forcing.
- (T2) **Negative result is not a new floor.** Unobservable-$C$ Cauchy-FE obstruction confirms Instance 2 of #discussion-identifiability-floor at a second structural layer. Worth noting as a dual-obstruction strengthening; not a new instance.
- (T3) **The two structural layers converge on the same scope boundary.** Both the Cauchy-FE uniqueness (this spike) and the Cramér-Rao identifiability (Prop B.7) agree: observable $C$ → structurally clean; unobservable $C$ → structurally obstructed. The convergence matters because it shows the scope boundary is not an artifact of one choice of analytical tool.
- (T4) **Within-cluster $\rho$ conjecture is refuted as stated.** $\rho$ does not interpolate the coordinate's dimension; it interpolates the Fisher identifiability of the marginal channel. The coordinate dimension is piecewise-constant ($K$ under no latent; $2K+1$ under latent) with a discrete jump.

## §7 — Ladder-up attempt to L2

### §7.1 What L2 adds

The Correlation Hierarchy (#strategy-dag) describes L2 as "full joint failure distribution over edges" — arbitrary correlation structure without the latent-common-cause scaffolding. Specifying a full joint over $m$ binary edges requires $2^m - 1$ parameters; bounded-cognition constraints (#strategy-complexity-cost) forbid this in general.

What's in L2 but not L1'?

- Non-latent correlation. E.g., direct causal coupling between siblings without an intermediate variable. $Y_j \to Y_k$ directly (Y_j affects Y_k, not via a common cause).
- Chain-correlated structure. Y_1 → Y_2 → Y_3 where the correlations propagate along a chain, not a star.
- Higher-order interactions. Triplet correlations beyond what pairwise latent-common-cause can produce.

The block-additivity axiom as stated in §2 presumed the correlation structure was *latent-common-cause mediated*. In L2, that's not guaranteed.

### §7.2 Does block-additivity still force log-odds in L2?

For a general joint distribution $P(\mathbf{y})$ on $m$ binary edges, the natural parameter space of the joint is the log-probabilities of the $2^m$ cell values (or equivalently, the exponential-family canonical parameters). Under independent Bernoulli assumption, this collapses to $m$ log-odds parameters. Under arbitrary L2 correlation, we need all $2^m - 1$ interaction parameters (main effects + pairwise + higher).

The exponential-family natural parameterization of $P(\mathbf{y})$ on $m$ binary variables is the log-linear model:

$$\log P(\mathbf{y}) = \sum_{S \subseteq [m], S \neq \emptyset} \lambda_S \prod_{k \in S} y_k - A(\lambda)$$

with $2^m - 1$ parameters $\lambda_S$ (one per non-empty subset) and log-partition $A(\lambda)$. This is the Ising-like parameterization.

**Does the block-additivity axiom force this coordinate under L2?** Under iid observations of the joint $\mathbf{y}^{(t)}$, the Bayesian update in the natural-parameter coordinate IS additive:

$$\lambda_S^{\text{post}} = \lambda_S^{\text{prior}} + \ell_S(\mathbf{y}^{(t)})$$

for each subset $S$, with $\ell_S$ the log-likelihood contribution of the $S$-interaction feature. This follows from the exponential-family conjugate structure: the log of a product-of-exponential-family is a sum of natural parameters.

So: under joint observations and the Ising-like natural parameterization, the $(2^m - 1)$-dimensional coordinate is forced to be log-linear (the generalization of log-odds), and block-additivity holds trivially because the coordinate is already at the natural-parameter level.

**What this buys.** A clean generalization: at any correlation level (L0 / L1' / L2), if the agent observes the joint vector $\mathbf{y}$ at each trial and updates the joint posterior, the forced coordinate is the log-linear natural parameterization. The dimension is $m$ at L0 (only main effects), $m + c$ at L1' (main + $c$ interactions induced by latents), and up to $2^m - 1$ at full L2.

**What this costs.** Exponential parameter growth. The $2^m - 1$ cost IS the reason L2 is intractable for #strategy-dag; the present analysis only shows that *if* the agent chose to represent the full joint, the natural coordinate is log-linear. The intractability is at the representation level, not the coordinate level.

### §7.3 Where L2 block-additivity fails

When the agent's *observation* doesn't include the full joint — only partial marginals, or only summary statistics — the block-additivity axiom fails similarly to the unobservable-$C$ case:

- Partial-marginal observation: the posterior update on the full joint depends nonlinearly on the prior through the marginalization; same mixture-posterior obstruction.
- Summary-statistic observation: Fisher information is rank-limited (not full $2^m - 1$); Cramér-Rao obstruction.

So L2 admits the positive result (log-linear coordinate forced) iff the agent observes the full joint — which is structurally equivalent to "no latents are unobservable" in the generalized sense.

### §7.4 Scope map

| Regime | Observation | Coordinate | Forced by |
|---|---|---|---|
| L0 | Per-edge Bernoulli | $m$-dim log-odds | Aczél per coordinate |
| L1' with observable $C$ | $\mathbf{y} \cup \{c\}$ per trial | $(2K+1)$-dim log-odds (per cluster) | Aczél per factor |
| L1' with unobservable $C$ | $\mathbf{y}$ only | — | Case B inconsistency |
| L2 with full-joint observation | $\mathbf{y}$ full vector | $(2^m - 1)$-dim log-linear | Aczél per subset |
| L2 with partial observation | Subsets of $\mathbf{y}$ | — | Partial-marginal inconsistency |

The pattern: additive-coordinate forcing works whenever the observation is informationally sufficient for the joint posterior to admit a translation-commuting form. Fails whenever the observation induces mixture-responsibility or marginalization nonlinearity.

## §8 — Candidate landing

### §8.1 Landing recommendation

Based on §6's honest takeaways:

**Primary landing — extension of #edge-update-natural-parameter.** Add a new subsection to #edge-update-natural-parameter titled "Block Structure and Correlated Evidence" with:

- Statement of the block-additivity axiom under observable $C$.
- §2.3 Case A: log-odds forced per factor in the $(2K+1)$-dim block coordinate, reducing to singleton Aczél.
- §2.3 Case B: structural failure of the axiom under unobservable $C$ (dual obstruction to Prop B.7's Cramér-Rao floor).
- §7.2: L2 extension under full-joint observation (log-linear coordinate).
- Scope map as a table (§7.4).

The extension clarifies what the log-odds coordinate becomes under correlated evidence — which is important because #credit-assignment-boundary's default signal function is stated in log-odds and should be updated to reflect the higher-dimensional block coordinate under L1'.

**Secondary landing — note added to #discussion-identifiability-floor Instance 2.** One paragraph noting that the unobservable-$C$ obstruction appears at a second structural layer (Cauchy-FE coordinate uniqueness) in addition to the Cramér-Rao Fisher-information layer. Strengthens the "structural, not analytical-artifact" reading of the floor.

**Tertiary landing — update to #additive-coordinate-forcing.** Add a Working Note entry under "Candidate future layers" noting that the block-evidence case was investigated and determined to be an extension of #edge-update-natural-parameter under factorization, not a new layer in the 1-anchor-plus-2-theorem pattern. Updates the meta-segment's honest accounting of which Cauchy-FE instances live independently vs as generalizations.

**Quaternary landing — note in #credit-assignment-boundary.** Observe that the default signal function's log-odds presentation, stated per edge, generalizes to a block coordinate under observable $C$ per the §2.3 Case A extension. The practical consequence: under L1' with observable $C$, the signal function should update $(2K+1)$ coordinates per cluster (one per conditional regime plus the latent), not $K$ marginal coordinates. This would be a first-class repair of the "gradient signal operates at L0; principled fix is L1 augmentation" working-notes-grade gap currently in #credit-assignment-boundary's correlated-failure interaction.

### §8.2 What the landing does NOT do

- Does not promote any new theorem to #additive-coordinate-forcing's primary instances. The spike found the block result is an extension, not a third primary theorem.
- Does not create a new #discussion-identifiability-floor instance. The dual obstruction strengthens Instance 2 but does not introduce a structurally new obstruction.
- Does not replace Prop B.7's Cramér-Rao analysis. The two (Cauchy-FE and Cramér-Rao) are independent routes to the same scope boundary, both of which are useful to have on the record.

### §8.3 Minimal vs full landing

**Minimal landing.** Just add the observable-$C$ extension and the scope table to #edge-update-natural-parameter; mention the Case B obstruction briefly. Cross-link to Prop B.7 for the Cramér-Rao-side derivation. One medium-sized subsection.

**Full landing.** All four landings (primary + secondary + tertiary + quaternary) as separate edits across four segments. Full landing also includes: (i) explicit L2 log-linear extension in the new subsection with worked example (2-edge Ising), (ii) formal statement of the dual-obstruction convergence between Cauchy-FE and Cramér-Rao, (iii) update to #credit-assignment-boundary's default signal function for block regimes.

Recommend **minimal landing first**, with full landing deferred unless the #credit-assignment-boundary generalization (quaternary) is picked up as an active work item. The #credit-assignment-boundary update would be the single highest-value follow-on because it closes a working-notes-grade gap.

### §8.4 Alternative landing — park the spike

If reviewers judge the extension not worth the segment disruption, park as archaeological:

- §2.3 Case A positive result is *known* in the Bayesian-network literature (exponential-family conjugate updates on factorized likelihoods; standard). AAD's contribution would only be the explicit observation that block-additivity is the update-layer axiom under which the result lives, and the scope boundary at unobservable $C$.
- §2.3 Case B negative result is *equivalent* to Prop B.7's Cramér-Rao refutation from a different angle. Value is in convergence; novelty is minimal.

The park-decision would retain the spike for the record, noting that (a) log-odds generalizes cleanly to blocks under observable $C$ via per-factor Aczél; (b) the unobservable-$C$ floor is confirmed at the Cauchy-FE layer; (c) $\rho$-interpolation conjecture refuted as stated.

### §8.5 Recommended decision

Land minimal (single subsection extension of #edge-update-natural-parameter + brief cross-refs in #discussion-identifiability-floor and #additive-coordinate-forcing). Promote quaternary landing (#credit-assignment-boundary update) when the block-coordinate signal function becomes a needed improvement (triggered by new L1' applications, or by L2 spikes). The minimal landing is low-disruption and closes the "what happens to log-odds under L1'" question that this spike raised.

## §9 — Epistemic assessment

### §9.1 Tier-labeled content summary

| Content | Tier | Justification |
|---|---|---|
| §2.3 Case A: block coordinate is $(2K+1)$-dim log-odds under observable $C$ | **Exact** (conditional on block-additivity axiom under observable $C$) | Per-factor Aczél applied to product-of-Bernoullis likelihood; standard Cauchy-FE argument |
| §2.3 Case B: block-additivity axiom inconsistent under unobservable $C$ | **Exact** (conditional on soft-EM responsibility-reweighting Bayesian update) | Translation-commuting form contradicted by responsibility dependence on prior |
| §3.2 Refutation of $\rho$-interpolation conjecture as stated | **Robust qualitative** | The dimension jump from $K$ to $2K+1$ is discrete, not continuous in any natural correlation parameter |
| §3.3 $\rho$ parameterizes Fisher identifiability, not coordinate dimension | **Robust qualitative** | Specific form at $\rho=\Delta_j\Delta_k$ is exact; the broader identifiability-vs-coordinate distinction is a structural observation |
| §4.5 Shore-Johnson subset-independence fails for unobservable-$C$ marginals | **Exact** | Direct check: the mixture does not factor across children |
| §6.1 Block-additivity is an extension of #edge-update-natural-parameter, not a third theorem | **Robust qualitative** | Judgment call; depends on how "new theorem" is defined; honest accounting favors extension |
| §6.2 Unobservable-$C$ Cauchy-FE obstruction confirms Instance 2, not new instance | **Robust qualitative** | Same scope boundary, same repair routes, same strengthened consequence as Instance 2 |
| §7.2 L2 log-linear coordinate forced under full-joint observation | **Exact** (conditional on exponential-family structure) | Standard exponential-family conjugate-update result |
| §7.4 Scope map (L0/L1'/L2 × full/partial observation) | **Robust qualitative** | The pattern is correct; the mapping of unobservable-$C$ and partial-marginal into the same "Fisher-obstructed" column is structural |

### §9.2 What is solid

- (S1) The observable-$C$ block coordinate is $(2K+1)$-dimensional log-odds per cluster. This is a direct per-factor application of the existing Aczél theorem on a factorized likelihood. No new mathematical content; clean extension.
- (S2) The unobservable-$C$ axiom inconsistency. The responsibility-reweighted update on a mixture cannot be expressed as $\Psi_{\text{post}} = \Psi_{\text{prior}} + G(\mathbf{y})$; this is a structural property of mixture posteriors, not a quirk of one formulation.
- (S3) Convergence with Prop B.7 at the scope boundary. Observable $C$ → structurally clean (Cauchy-FE works, Cramér-Rao identifiable); unobservable $C$ → structurally obstructed (Cauchy-FE inconsistent, Cramér-Rao rank-deficient). Both boundary agreements are exact.
- (S4) $\rho$ does NOT interpolate coordinate dimension. The dimension is piecewise-constant with a discrete jump at latent-addition; the $\rho$ parameter governs Fisher-information identifiability of the marginal channel, not the coordinate dimension itself.

### §9.3 What is fragile

- (F1) The "not a third theorem" judgment (§6.1) is a framing call. Reasonable reviewers could argue that a block-axiom uniqueness theorem with a different motivation structure (cluster-factorization AAD-internal motivation vs chain-rule AAD-internal motivation) is genuinely new. The honest read leans extension, but the call is contestable.
- (F2) The "not a new floor instance" judgment (§6.2) is similarly a framing call. The dual obstruction strengthens Instance 2; whether that's a standalone floor or a reinforcement of an existing floor depends on taste. The honest read leans reinforcement.
- (F3) The L2 extension (§7.2) is sketchy. The log-linear coordinate under full-joint observation is standard exponential-family theory, but AAD hasn't systematically treated full-joint observation as a practical regime; the $2^m - 1$ cost makes it mostly aspirational. The extension is formally correct but practically bounded.
- (F4) The quaternary landing (§8.1) — updating #credit-assignment-boundary's default signal function to operate on the block coordinate — has non-trivial downstream effects that weren't worked through here. Specifically: what does the gradient $\mathbf{J}$ look like on a block coordinate? What is the analog of $\iota_k$ (identifiability coefficient) under a $(2K+1)$-dim coordinate? These are not answered in this spike.

### §9.4 What is open

- (O1) The full-joint observation regime (§7) is a theoretical scope not developed elsewhere in AAD. If the agent observed the full joint vector at every trial, many of the L2 obstructions would lift. Whether this is a meaningful practical scope or purely formal is a separate question; the spike didn't investigate.
- (O2) The "second-layer confirmation" of Instance 2 (§5.4, §6.2) — does the dual Cauchy-FE + Cramér-Rao obstruction point to a deeper unifying obstruction? Is there a single axiomatic statement from which both follow? This is a deep research question that could seed a future spike. Speculative angle: both obstructions arise from *non-translation-commuting posterior updates*; both Cauchy-FE and Cramér-Rao are sensitive to the failure of this property, at different structural layers.
- (O3) The block-coordinate signal function for #credit-assignment-boundary. Specifically: how does the $\mathbf{J}$-Jacobian generalize to operate on a $(2K+1)$-dim coordinate? What is the corresponding $\iota$ coefficient? How does directional fidelity (B1) look on the block coordinate? These are concrete, work-through-able questions that the quaternary landing opens.

### §9.5 Spike's honest bottom line

The spike set out to test whether a block-structured evidential-additivity axiom forces a unique coordinate analogous to #edge-update-natural-parameter's Aczél result. The answer is:

- **Yes, under observable $C$** — with the coordinate being $(2K+1)$-dimensional log-odds per cluster, derived as a per-factor application of the existing Aczél theorem on the factored likelihood. Not a new theorem; a clean extension.
- **No, under unobservable $C$** — with the axiom being *inconsistent* with Bayesian updating, not merely weaker. This confirms #discussion-identifiability-floor Instance 2 at a second structural layer, strengthening but not creating a new instance.
- **No, $\rho$ does not interpolate the coordinate dimension** — it parameterizes marginal-channel Fisher identifiability instead. The coordinate dimension is piecewise-constant.
- **No, block-additivity is not a third theorem in #additive-coordinate-forcing** — it is an extension of the update-layer theorem under factorization, not a new layer.

The clean version of this result is a small extension to #edge-update-natural-parameter (scope clarified under L1'/L2) and a cross-reference paragraph in #discussion-identifiability-floor noting the dual-obstruction convergence. The $\rho$-refutation is a valuable honest correction of the likely intuition; it is worth preserving in the spike for that reason. The open follow-on is the #credit-assignment-boundary block-coordinate signal function; this spike doesn't resolve it but frames it concretely.

The spike's value is not a new theorem — it is honest scope clarification of an existing one. That kind of "strengthening before softening" work is valuable for the epistemic architecture (per Opus's "honesty as architectural principle" observation) even when the headline is "no new theorem here." The convergence with the identifiability-floor pattern is the takeaway most worth preserving.

## Working notes

- The full-joint-observation angle (§7) could support a follow-on spike on "when does an agent have access to joint observation structure, and what does that buy?" This is tangent to Prop B.7's Repair (ii) and may be tractable under high-identifiability-calibration-laboratory settings (e.g., software, where intermediate states are observable by construction per TST).
- The dual-obstruction observation (Cauchy-FE + Cramér-Rao both obstructed at unobservable $C$) invites a deeper unification: is there a single axiomatic obstruction from which both follow? This would promote the identifiability-floor pattern from "external theorems applied to AAD settings" to "a unified obstruction theory within AAD itself." Speculative; outside this spike's scope.
- The §5.3 R2 (multi-child joint observation) route is the under-explored repair in Prop B.7. The spike's analysis shows it's equivalent to raising the Fisher matrix to rank $2K+1$, which IS full rank on the $(2K+1)$-dim block coordinate. So multi-child joint observation is structurally equivalent to observing $C$ indirectly through its multi-child fingerprint. Whether this can be formalized as "observing a sufficient statistic of $C$" (vs observing $C$ directly) is a mild open question — probably yes under standard sufficient-statistic theory (Fisher 1922; Koopman-Pitman-Darmois).
- The Shore-Johnson subset-independence axiom (§4.5) is the divergence-layer analog of block-additivity at the observation level. Under observable $C$, it gives the same result as the Aczél per-factor derivation; under unobservable $C$, the axiom is false for the marginal (children aren't independent marginals). This convergence between the update-layer and divergence-layer stories is the strongest evidence that block-additivity under observable $C$ is a real structural feature, not an accidental alignment.
- If the minimal landing is executed, the Case B obstruction should be stated precisely enough that future spikes on (a) variational-approximation posteriors, (b) mean-field EM, (c) score-matching updates can check whether those families evade the obstruction. Almost certainly they do NOT — variational updates typically don't admit a translation-commuting form either — but that's worth checking explicitly.
- Historical cross-check: the correspondence between "posterior update has form $T(\phi + U(y))$" and "exponential-family conjugate" is a classical result. Our §2.3 Case B is effectively "mixture models are not exponential families in the natural sense" — a textbook fact. The contribution is making it visible at the Cauchy-FE / additive-coordinate layer of AAD, where it hadn't been stated.
