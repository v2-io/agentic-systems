---
slug: edge-update-natural-parameter
type: derivation
status: conditional
depends:
  - strategy-dag
  - edge-update-via-gain
  - chain-confidence-decay
  - strategy-cost-regret-bound
stage: draft
---

# Derivation: Log-Odds as the Unique Additive-Evidence Parameterization for Edge Credences

The log-odds coordinate $\lambda_{ij} = \log(p_{ij} / (1 - p_{ij}))$ is the unique parameterization (up to positive affine transformation) on which independent Bernoulli evidence updates edge credences additively, under an evidential-additivity axiom motivated as the update-level analog of #chain-confidence-decay's chain-level additive log-confidence decomposition. This segment states the uniqueness theorem, derives it, and explains how it positions log-odds as the natural parameterization for AAD's continuous-gradient edge-update machinery.

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
| **Chain level** | Confidence along a causal chain | $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ | #chain-confidence-decay |
| **Divergence level** | Mismatch between optimal and strategy policies | $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ decomposes additively across DAG layers along the optimal trajectory | #strategy-cost-regret-bound §6.1 |
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

These consequences are why the continuous-gradient edge-update machinery in #credit-assignment-boundary is well-posed globally in log-odds but exhibits the Finding 2 mechanical break (unbounded updates pushing credences outside $[0, 1]$) when stated directly in probability space.

### Scope Condition

*[Scope (evidential-additivity scope)]*

The evidential-additivity axiom applies to agent classes that treat observations as independent Bernoulli likelihood evidence — the Bayesian-coherent sub-scope of AAD. Non-Bayesian agents (PID controllers, rule-based systems, human judgment per #update-gain) do not invoke likelihood-ratio accumulation and are outside the axiom's scope. This matches the sub-scope $\alpha$ / sub-scope $\beta$ partition in #gain-sector-bridge (see also `msc/spike-a2-prime-strengthening.md`): the uniqueness applies within sub-scope $\alpha$, where B1 (directional fidelity) is already derived from Bayesian coherence.

For multinomial / categorical edge credences with $K \gt 2$ outcomes, the analog is softmax / canonical exponential-family parameters: the softmax natural parameters $\eta_k = \log \pi_k$ (up to a reference-class shift) satisfy the same evidential-additivity axiom. The Bernoulli case ($K = 2$) collapses to log-odds.

## Epistemic Status

*Derived (conditional on the evidential-additivity axiom).* The uniqueness theorem is a standard functional-equation result (Cauchy functional equation with smoothness; Aczél 1966 §2.1). The AAD-internal motivation of the axiom is structural: it is the update-level analog of #chain-confidence-decay's chain-level additive log-confidence decomposition and #strategy-cost-regret-bound §6.1's divergence-level chain-rule additivity. Without the axiom, the selection of log-odds weakens to canonical-not-unique on convergent grounds (exponential-family naturalness, Fisher-information / natural-gradient canonicity, domain-well-posedness of the continuous gradient).

**Max attainable:** *exact* for the Cauchy functional equation step (standard); *derived-conditional* for the overall uniqueness claim because the axiom, though AAD-internally motivated, is itself a commitment rather than a consequence of prior AAD commitments. The axiom's status is parallel to the chain-rule additivity axiom in #strategy-cost-regret-bound §6.1 — both are AAD-internally motivated as the "right level" instances of a single additive-decomposition principle.

**Not uniqueness in the unconditional sense.** The theorem states that *if* credence updates live on a single additive coordinate whose increment depends only on the observation, *then* that coordinate is log-odds up to positive affine. It does not rule out non-additive update schemes, nor schemes that live on multiple coordinates (e.g., Beta-Bernoulli with sufficient statistics $(\alpha, \beta)$ rather than a single credence coordinate). The Beta-Bernoulli presentation is *equivalent* in content to the log-odds presentation under a change of coordinates; the uniqueness is about what single-coordinate additive form is possible.

## Discussion

**Why this matters for G-BP1.** The scoping spike `msc/spike-gbp1-logit-scoping.md` examined whether log-odds reparameterization (G-BP1 in `msc/architectural-proposals-2026-04-22.md`) is *uniquely correct* or merely canonical. Paths A (exponential-family canonical), C (Fisher / natural-gradient), and D (sector-condition preservation) supply convergent grounds but no uniqueness theorem. Path B (this segment) gives the uniqueness result conditional on the evidential-additivity axiom. The axiom is AAD-internally motivated, so the result is genuine strengthening — not "log-odds happens to work" but "log-odds is forced by the update-level analog of a principle AAD already relies on at chain and divergence levels."

**Why this matters for Finding 2.** The mechanical break in #credit-assignment-boundary's default signal function (unbounded gradient updates pushing credences outside $[0, 1]$ when $\lVert \mathbf{J} \rVert^2 \to 0$; see `msc/pending-findings-2026-04-22.md` §Finding 2) is a presentation artifact of the probability-space coordinate. In log-odds, the domain is $\mathbb{R}$ and the update is well-posed globally. The fix is not "clip the update" but "present the update in its native additive coordinate."

**Relationship to Bayesian conjugate analysis.** The Beta-Bernoulli conjugate update produces posterior hyperparameters $(\alpha + y, \beta + 1 - y)$ that are additive in the sufficient statistics, giving the point estimate $\hat p = \alpha / (\alpha + \beta)$ that updates *non-additively* in probability space. The content is the same — the log-odds coordinate makes the additivity manifest at the level of credence itself, while Beta-Bernoulli shows the same additivity at the level of sufficient statistics. The two are dual presentations of the same exponential-family structure.

**Non-uniqueness outside the Bayesian sub-scope.** For non-Bayesian agents in sub-scope $\beta$ of #gain-sector-bridge (PID controllers, rule-based systems, human judgment), the evidential-additivity axiom does not apply. Such agents may update credences via coordinate-free heuristics (proportional blame, threshold rules) that do not decompose into likelihood-ratio addition. The uniqueness of log-odds is therefore scope-conditional, not universal.

**Path B's role in the overall pattern.** The segment makes visible that AAD is committed to three consistent additive-decomposition moves — chain, divergence, update — each forcing a logarithmic coordinate in its own layer. Future additive-decomposition structures in AAD (e.g., any novel decomposition along trajectories, across channels, or between agents) should be examined for whether the same logarithmic-coordinate forcing applies. If yes, log-odds / natural-parameter / reverse-KL-style results compose cleanly. If no, the new layer is a genuine departure requiring its own analysis. The pattern is catalogued at the meta-pattern level in #additive-coordinate-forcing, including the 1-anchor-plus-2-theorem characterization (the chain layer is a mathematical identity; divergence and update are theorems conditional on AAD-internally-motivated axioms) and the adjacent-family classification (Lyapunov quadratic and IB Lagrangian share the additive shape but not the AAD-internal forcing structure).
