---
slug: deriv-edge-update-natural-parameter
type: derivation
status: conditional
depends:
  - def-strategy-dag
  - hyp-edge-update-via-gain
  - der-chain-confidence-decay
  - deriv-strategy-cost-regret-bound
stage: draft
---

# Derivation: Log-Odds as the Unique Additive-Evidence Parameterization for Edge Credences

The log-odds coordinate $\lambda_{ij} = \log(p_{ij} / (1 - p_{ij}))$ is the unique parameterization (up to positive affine transformation) on which independent Bernoulli evidence updates edge credences additively, under an evidential-additivity axiom motivated as the update-level analog of #der-chain-confidence-decay's chain-level additive log-confidence decomposition. This segment states the uniqueness theorem, derives it, and explains how it positions log-odds as the natural parameterization for AAD's continuous-gradient edge-update machinery.

## Formal Expression

### Setup

Let $p \in (0, 1)$ denote a scalar Bernoulli credence (the probability that a proposition is true) and let $\psi : (0, 1) \to \mathbb{R}$ be a smooth, strictly monotone reparameterization. Consider a sequence of independent Bernoulli observations $y_1, \ldots, y_n \in \{0, 1\}$ drawn from a channel with likelihood ratio $P(y \mid H_1) / P(y \mid H_0)$.

**Evidential-additivity axiom.** The posterior update, applied to a single observation $y$, takes the form

*[Assumption (evidential-additivity axiom)]*

$$\psi(p_{\text{post}}) = \psi(p_{\text{prior}}) + g(y)$$

for some function $g : \{0, 1\} \to \mathbb{R}$ that depends only on the observation $y$ — not on $p_{\text{prior}}$ nor on observation history.

### Theorem

*[Derived (evidential-additivity uniqueness of log-odds, conditional on the axiom above)]*

**Theorem.** The functional equation above admits solutions if and only if

$$\psi(p) = c \cdot \log\!\frac{p}{1 - p} + d$$

for constants $c \gt 0$ and $d \in \mathbb{R}$, with $g(y) = c \cdot \ell(y)$ where $\ell(y) = \log[P(y \mid H_1) / P(y \mid H_0)]$ is the log-likelihood ratio.

### Derivation

*[Derived (Proof Step: Bayesian form of the update)]*

By Bayes' theorem applied to binary hypotheses,

$$\frac{p_{\text{post}}}{1 - p_{\text{post}}} = \frac{p_{\text{prior}}}{1 - p_{\text{prior}}} \cdot \frac{P(y \mid H_1)}{P(y \mid H_0)}$$

Taking the logarithm of both sides and writing $h(p) := \log(p / (1 - p))$,

$$h(p_{\text{post}}) = h(p_{\text{prior}}) + \ell(y)$$

So $\psi = h$ trivially satisfies the axiom with $g = \ell$.

*[Derived (Proof Step: uniqueness by Cauchy functional equation)]*

Suppose $\psi$ is any smooth, strictly monotone reparameterization satisfying the axiom. Since the Bayesian mapping $p_{\text{prior}} \mapsto p_{\text{post}}$ is fully determined by $y$ through the likelihood ratio, the difference $\psi(p_{\text{post}}) - \psi(p_{\text{prior}})$ depends only on $y$, and by the axiom must equal $g(y)$.

Change variables via $\lambda = h(p) = \log(p/(1-p))$ and define $\Psi(\lambda) := \psi(\sigma(\lambda))$ where $\sigma(\lambda) = 1 / (1 + e^{-\lambda})$ is the logistic sigmoid. The axiom becomes

$$\Psi(\lambda + \ell(y)) - \Psi(\lambda) = g(y) \quad \text{for all } \lambda \in \mathbb{R},\, y \in \{0, 1\}$$

Extending to continuous-valued evidence (or considering mixtures of Bernoulli channels with varying likelihood ratios, which span all of $\mathbb{R}$ in the $\ell$-value space), the identity

$$\Psi(\lambda + \ell) - \Psi(\lambda) = G(\ell) \quad \text{for all } \lambda, \ell \in \mathbb{R}$$

holds for a function $G$ independent of $\lambda$. This is the Cauchy functional equation (translation-additivity). Combined with the smoothness assumption on $\psi$, the unique solution class is $\Psi(\lambda) = c \cdot \lambda + d$ for constants $c$ and $d$ (Aczél 1966, *Lectures on Functional Equations and Their Applications*, §2.1).

*[Derived (Proof Step: determining the constants)]*

Strict monotonicity of $\psi$ forces $c \ne 0$. Taking $\psi$ to have the same monotonicity sense as $p \mapsto p$ (credence increasing with $\psi$), we need $c \gt 0$. Thus $\psi(p) = c \cdot h(p) + d = c \cdot \log(p / (1 - p)) + d$, and $g(y) = c \cdot \ell(y)$.

This completes the proof. $\square$

### Three-Layer Parallel

*[Discussion (three-layer additive decomposition)]*

The evidential-additivity axiom is the update-level instance of an additive-decomposition principle that AAD has already committed to at two prior layers:

| Layer | Quantity decomposed | Decomposition form | Source |
|---|---|---|---|
| **Chain level** | Confidence along a causal chain | $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ | #der-chain-confidence-decay |
| **Divergence level** | Mismatch between optimal and strategy policies | $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ decomposes additively across DAG layers along the optimal trajectory | #deriv-strategy-cost-regret-bound §6.1 |
| **Update level** | Credence evolution under independent evidence | $\psi(p_{\text{post}}) - \psi(p_{\text{prior}}) = g(y_1) + \cdots + g(y_n)$ for $n$ observations, with $\psi =$ log-odds | This segment |

Each layer forces a logarithmic coordinate through essentially the same structural move: products of independent factors become sums on a log scale. At the chain level, $p^n \to n \log p$; at the divergence level, $\prod Q \to \sum \log Q$; at the update level, $\prod \text{LR} \to \sum \log \text{LR}$. The three are the same transform applied to different quantities.

### Interpretation for the Edge-Update Machinery

*[Discussion (operational consequence)]*

For edge credence $p_{ij}$ with log-odds $\lambda_{ij} = \log(p_{ij} / (1 - p_{ij}))$, the Bayesian update under independent Bernoulli evidence is

$$\lambda_{ij}^{\text{post}} = \lambda_{ij}^{\text{prior}} + \ell(y)$$

where $\ell(y)$ is the per-observation log-likelihood ratio.

**Two operational consequences that follow from the uniqueness theorem:**

1. **Domain unboundedness.** The log-odds coordinate has domain $\mathbb{R}$, not $[0, 1]$. Additive updates cannot escape the domain, regardless of update magnitude. The probability-space presentation $p_{ij} \in [0, 1]$ is the projected image of the log-odds coordinate, obtained via $p_{ij} = \sigma(\lambda_{ij})$ at the readout interface.

2. **Invariance under the chain of causal reasoning.** Because the log-odds coordinate is the unique additive evidence coordinate, evidence accumulated along one edge in a strategy DAG can be composed with evidence accumulated along another edge by addition in the log-odds vector space, provided the evidence is conditionally independent. The Beta-Bernoulli moment-parameter form $\hat p = \alpha / (\alpha + \beta)$ is the projected image, where $\alpha, \beta$ are the cumulative sufficient statistics in exponential-family form.

These consequences are why the continuous-gradient edge-update machinery in #disc-credit-assignment-boundary is well-posed globally in log-odds but exhibits the Finding 2 mechanical break (unbounded updates pushing credences outside $[0, 1]$) when stated directly in probability space.

### Scope Condition

*[Scope (evidential-additivity scope)]*

The evidential-additivity axiom applies to agent classes that treat observations as independent Bernoulli likelihood evidence — the Bayesian-coherent sub-scope of AAD. Non-Bayesian agents (PID controllers, rule-based systems, human judgment per #emp-update-gain) do not invoke likelihood-ratio accumulation and are outside the axiom's scope. This matches the sub-scope $\alpha$ / sub-scope $\beta$ partition in #der-gain-sector-bridge (see also `spikes/spike-a2-prime-strengthening.md`): the uniqueness applies within sub-scope $\alpha$, where B1 (directional fidelity) is already derived from Bayesian coherence.

For multinomial / categorical edge credences with $K \gt 2$ outcomes, the analog is softmax / canonical exponential-family parameters: the softmax natural parameters $\eta_k = \log \pi_k$ (up to a reference-class shift) satisfy the same evidential-additivity axiom. The Bernoulli case ($K = 2$) collapses to log-odds.

## Epistemic Status

*Derived (conditional on the evidential-additivity axiom).* The uniqueness theorem is a standard functional-equation result (Cauchy functional equation with smoothness; Aczél 1966 §2.1). The AAD-internal motivation of the axiom is structural: it is the update-level analog of #der-chain-confidence-decay's chain-level additive log-confidence decomposition and #deriv-strategy-cost-regret-bound §6.1's divergence-level chain-rule additivity. Without the axiom, the selection of log-odds weakens to canonical-not-unique on convergent grounds (exponential-family naturalness, Fisher-information / natural-gradient canonicity, domain-well-posedness of the continuous gradient).

**Max attainable:** *exact* for the Cauchy functional equation step (standard); *derived-conditional* for the overall uniqueness claim because the axiom, though AAD-internally motivated, is itself a commitment rather than a consequence of prior AAD commitments. The axiom's status is parallel to the chain-rule additivity axiom in #deriv-strategy-cost-regret-bound §6.1 — both are AAD-internally motivated as the "right level" instances of a single additive-decomposition principle.

**Not uniqueness in the unconditional sense.** The theorem states that *if* credence updates live on a single additive coordinate whose increment depends only on the observation, *then* that coordinate is log-odds up to positive affine. It does not rule out non-additive update schemes, nor schemes that live on multiple coordinates (e.g., Beta-Bernoulli with sufficient statistics $(\alpha, \beta)$ rather than a single credence coordinate). The Beta-Bernoulli presentation is *equivalent* in content to the log-odds presentation under a change of coordinates; the uniqueness is about what single-coordinate additive form is possible.

## Discussion

**Why this matters for G-BP1.** The scoping spike `spikes/spike-gbp1-logit-scoping.md` examined whether log-odds reparameterization (G-BP1 in `msc/architectural-proposals-2026-04-22.md`) is *uniquely correct* or merely canonical. Paths A (exponential-family canonical), C (Fisher / natural-gradient), and D (sector-condition preservation) supply convergent grounds but no uniqueness theorem. Path B (this segment) gives the uniqueness result conditional on the evidential-additivity axiom. The axiom is AAD-internally motivated, so the result is genuine strengthening — not "log-odds happens to work" but "log-odds is forced by the update-level analog of a principle AAD already relies on at chain and divergence levels."

**Why this matters for Finding 2.** The mechanical break in #disc-credit-assignment-boundary's default signal function (unbounded gradient updates pushing credences outside $[0, 1]$ when $\lVert \mathbf{J} \rVert^2 \to 0$; see `audits/pending-findings-2026-04-22.md` §Finding 2) is a presentation artifact of the probability-space coordinate. In log-odds, the domain is $\mathbb{R}$ and the update is well-posed globally. The fix is not "clip the update" but "present the update in its native additive coordinate."

**Relationship to Bayesian conjugate analysis.** The Beta-Bernoulli conjugate update produces posterior hyperparameters $(\alpha + y, \beta + 1 - y)$ that are additive in the sufficient statistics, giving the point estimate $\hat p = \alpha / (\alpha + \beta)$ that updates *non-additively* in probability space. The content is the same — the log-odds coordinate makes the additivity manifest at the level of credence itself, while Beta-Bernoulli shows the same additivity at the level of sufficient statistics. The two are dual presentations of the same exponential-family structure.

**Non-uniqueness outside the Bayesian sub-scope.** For non-Bayesian agents in sub-scope $\beta$ of #der-gain-sector-bridge (PID controllers, rule-based systems, human judgment), the evidential-additivity axiom does not apply. Such agents may update credences via coordinate-free heuristics (proportional blame, threshold rules) that do not decompose into likelihood-ratio addition. The uniqueness of log-odds is therefore scope-conditional, not universal.

**Path B's role in the overall pattern.** The segment makes visible that AAD is committed to a family of consistent coordinate-forcing moves at chain, divergence, update, and metric layers, each forcing a specific coordinate via a uniqueness theorem on an AAD-internally-motivated axiom. Future coordinate-forcing structures in AAD (e.g., any novel decomposition along trajectories, across channels, or between agents) should be examined for whether Cauchy-FE on an additivity axiom or Čencov-invariance on a parameterization-invariance axiom applies. If yes, log-odds / natural-parameter / reverse-KL / Fisher-metric-style results compose cleanly. If no, the new layer is a genuine departure requiring its own analysis. The pattern is catalogued at the meta-pattern level in #disc-additive-coordinate-forcing, including the 1-anchor-plus-3-theorem characterization (the chain layer is a mathematical identity; divergence, update, and metric are theorems conditional on AAD-internally-motivated axioms) and the adjacent-family classification (Lyapunov quadratic and IB Lagrangian share the additive shape but not the AAD-internal forcing structure).

**Block-structured evidential additivity under L1' correlated evidence.** When sibling edges share a latent common cause $C$ (L1' correlated evidence per `#def-strategy-dag`'s Correlation Hierarchy), the independent-evidence axiom grounding Path B is literally false. Under *observable* $C$, the likelihood factorizes per-cluster as $P(\mathbf y, c) = P(c)\prod_k P(y_k \mid c)$, and the per-factor Aczél-1966 uniqueness argument applies independently to each factor. The forced coordinate becomes a $(2K+1)$-dimensional vector log-odds (one coordinate for $\theta_C$, two per child edge for $p_{j\mid C}$ and $p_{j\mid \neg C}$), reducing to the scalar log-odds when the cluster is a singleton and no latent is present. This is a **generalization-in-scope** of the theorem above, not a new primary instance of `#disc-additive-coordinate-forcing`: the forcing machinery is unchanged (Cauchy-FE on per-factor additivity); the scope widens to block-factorized likelihoods under observable latents. Under *unobservable* $C$, the soft-EM responsibility-reweighted posterior depends nonlinearly on the prior, so no smooth $\psi$ satisfies the block-additivity axiom — the axiom is structurally inconsistent with Bayesian mixture updates. This is the same scope boundary that `#disc-identifiability-floor` Instance 2 names via the Cramér-Rao Fisher-rank-1 obstruction; two independent analytical routes (Cauchy-FE failure at update layer; Cramér-Rao rank deficiency at observation layer) converge on the same unobservable-$C$ structural floor, strengthening the "structural, not analytical-artifact" reading of Instance 2.

## Findings

### Log-Odds as Uniquely-Forced Edge-Update Coordinate

**Brief:** When updating beliefs about whether something is true, there's a question of "what's the natural number to update?" — the probability itself, or some transformation of it. This result identifies a particular transformation (the log-odds, also used in logistic regression and Bayesian inference broadly) as the *uniquely* natural one for agents updating on independent evidence, in the precise sense that any equivalent representation must be log-odds up to scale. The choice isn't aesthetic; it's forced by what "independent evidence should add up" means mathematically. The uniqueness follows from Cauchy's functional equation operating on an evidential-additivity axiom motivated as the update-level analog of the chain-layer log-additive identity in `#der-chain-confidence-decay`.

**Impact:** Promotes a representational choice that previously had only convergent grounds (exponential-family canonicity, Fisher-information naturalness, sector-condition preservation) to a uniqueness theorem under an explicit AAD-internal axiom, joining the additive-coordinate-forcing meta-pattern (`#disc-additive-coordinate-forcing`) as one of its three theorem-grade instances. The result resolves a mechanical issue in the credit-assignment default signal function (`#disc-credit-assignment-boundary`), where unbounded gradient updates pushing credences outside [0,1] in the probability-space presentation become globally well-posed in the log-odds presentation (domain $\mathbb{R}$). It also positions log-odds as the coordinate against which downstream gain-and-update machinery should be analyzed for sub-scope $\alpha$ (Bayesian-coherent) agents.

**Novelty Claim:** *Claim differentiation* on an already-canonical representational choice (log-odds as the natural Bayesian-update coordinate, well-known from logistic regression / exponential-family / information-geometry traditions) by deriving its uniqueness under an AAD-internally-motivated evidential-additivity axiom. The Cauchy-FE machinery is classical; the AAD-internal axiomatization and the meta-pattern membership are the contribution.

**Related Work:**

- Aczél 1966, *Lectures on Functional Equations and Their Applications* §2.1 — *formal antecedent* — Cauchy-FE uniqueness machinery directly adopted in the derivation; cited inline.
- Cox 1946, "Probability, frequency and reasonable expectation" *Am. J. Phys.* 14:1–13; Jaynes 2003, *Probability Theory: The Logic of Science* — *conceptual precursor* — log-odds and additive-evidence accumulation as the natural form for Bayesian update; folk knowledge in this tradition.
- Amari & Nagaoka 2000, *Methods of Information Geometry* §2 — *formal antecedent* — log-odds as the natural parameter in the Bernoulli exponential family; the canonical-natural-parameter framing.
- Bishop 2006, *Pattern Recognition and Machine Learning* §4.2; Murphy 2012, *Machine Learning: A Probabilistic Perspective* — *adjacent literature* — standard statistical-learning treatments of log-odds and logistic regression; representational standard.

**Search Log:**
- 2026-04 (*intuition-only* on AAD-internal axiomatization angle): no targeted search for prior derivations of log-odds via the specific evidential-additivity axiom (update-level analog of chain-rule additivity) has been conducted. Pre-search expectation: the Cauchy-FE move is classical (Aczél 1966); the log-odds canonical parameter is exponential-family standard; the *AAD-internal axiomatization* (motivating the additivity axiom as the update-level analog of `#der-chain-confidence-decay`) is the contribution being claimed. A targeted search would query the Bayesian-coherence and information-geometry literatures specifically for prior axiomatic derivations of log-odds via Cauchy-FE in agent-update settings.
- 2025 (*targeted*): Aczél 1966 confirmed as the formal antecedent for the Cauchy-FE machinery; cited inline.
