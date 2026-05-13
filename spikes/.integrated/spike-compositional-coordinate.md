---
slug: spike-compositional-coordinate
type: spike
status: exploratory
date: 2026-04-22
---

# Spike: Is There a Composition-Layer Coordinate-Forcing Theorem?

**Charter.** `#additive-coordinate-forcing` has the honest 1-anchor-plus-2-theorem characterization at three single-agent layers (chain / divergence / update). All three instances are single-agent quantities. Is there a **fourth theorem** at Section III's composition layer — a *compositional coordinate* forced by a Cauchy functional equation on an AAD-internally-motivated additivity axiom, parallel to the three existing instances?

**Speculative by design.** The spike attempts the improbable first (four candidate axioms) and retreats to a structured failure characterization if none lands as a primary instance. All failed attempts are recorded as evidence about what the meta-pattern can and cannot stretch to.

**Outcome (preview).** None of the four candidate axioms clears the bar set by the three existing instances. Two candidates (log-viability, log-identifiability-shortfall) are already classified as *adjacent family members* in their parent spikes — the spike here confirms that classification. A third candidate (persistence-cost-rate) is *not even adjacent* — it yields linear-in-$\alpha$ rather than log-in-$\alpha$ and exits the pattern entirely. The fourth and most serious candidate (**log-closure-deficit across a composition tower**) reaches a partial derivation: the closure-defect $\varepsilon^\ast$ *does* compose multiplicatively under sequential coarse-graining, and its logarithm *is* additive along a composition tower. But the additivity is a **mathematical consequence** of the sub-multiplicativity of operator norms under the sector-persistence-template bridge-lemma form — *not* a theorem conditional on an AAD-internally-motivated additivity axiom independently grounded. The honest landing is: **the composition layer does admit an additive-decomposition structure (log-closure-deficit), but it is anchor-style (mathematical consequence of template machinery), not theorem-style (forced by an AAD-internal axiom via Cauchy FE).** That is a fourth *anchor*, not a fourth theorem — or, more cautiously, an adjacent family member in the direction of `#der-chain-confidence-decay`'s anchor. The three-part meta-architecture's Section III symmetry is achieved, but at the anchor layer, not the theorem layer.

**Secondary outcome.** The spike's failure structure is itself informative. The obstruction is consistent across all four candidates: composition-layer quantities do not have a natural chain-rule-like **independence structure** at the agent level, because composition is defined by **coupling** (shared environment, shared objective, teleological unity). The very property that makes composition interesting — coupling — is what prevents the "products of independent factors" shape that enables Cauchy-FE forcing. This is not accidental; it is structural. The honest meta-architectural conclusion: **`#additive-coordinate-forcing` is architecturally a single-agent family**, with chain/divergence/update indexing three layers of a *single* agent's internal machinery. Composition lives in a different structural family — *monotonicity under composition*, specifically the bridge-lemma shape — and future work should develop that family rather than forcing compositional results into the additive-coordinate-forcing shape.

---

## §1 — The Precise Question

Each instance of `#additive-coordinate-forcing` has a specific shape. Before attacking the composition layer, pin the shape down:

**The shape.** A quantity $\Psi$ (a coordinate on some object) satisfies:

1. **Multiplicative structure under independence.** $\Psi$ is a coordinate on a space where compound objects (made of "independent factors" in some AAD-motivated sense) have multiplicative representations on a *prior* coordinate. Chain: $P(E_1, \ldots, E_n) = \prod_i P(E_i \mid E_{\lt i})$. Divergence: $Q_{XY}(a, b) = Q_X(a)Q_{Y\mid X}(b \mid a)$. Update: $p_{\text{post}}/(1-p_{\text{post}}) = [p_{\text{prior}}/(1-p_{\text{prior}})] \cdot [P(y\mid H_1)/P(y\mid H_0)]$.

2. **AAD-internally-motivated additivity axiom.** An axiom — not a theorem, not a mathematical identity — that AAD commits to on structural grounds, asserting that $\Psi$ (the *target* coordinate) decomposes additively when the prior coordinate has the multiplicative structure. Chain: the probability chain rule is the anchor — a mathematical identity, so the "axiom" is trivially satisfied. Divergence: chain-rule additivity axiom. Update: evidential-additivity axiom. The last two are AAD-internal commitments, not theorems, but each is motivated as the "level-appropriate analog" of the chain-rule identity.

3. **Cauchy functional equation derivation.** The additivity axiom applied on the multiplicative structure forces a functional equation of the form $\Psi(x\cdot y) = \Psi(x) + \Psi(y)$ or $f(rs) = f(r) + r f(s) + g(r)$ (for divergences). Under smoothness / monotonicity, the solution class is logarithmic.

4. **The forced coordinate is logarithmic** (up to positive affine scaling; Aczél 1966 §2.1).

5. **AAD-internal motivation chain.** Each theorem-level instance explicitly cites `#der-chain-confidence-decay` as the anchor motivating its axiom. The three layers are interlocked.

**For a fourth composition-layer instance to land as a primary theorem**, it must:

- **(I)** Identify a compositional quantity $\Psi_{\text{comp}}$ whose prior coordinate has multiplicative structure under "independent sub-agents" (or equivalently: sequential / hierarchical / symmetric composition).
- **(II)** Identify an AAD-internally-motivated additivity axiom on $\Psi_{\text{comp}}$, with the axiom grounded as a compositional analog of the chain-rule identity (or the divergence / update analogs).
- **(III)** Derive the logarithmic-coordinate forcing via Cauchy FE under smoothness.
- **(IV)** Explicitly cite `#der-chain-confidence-decay` (or the chain of analogs) as the anchor motivating the axiom.

Alternatively, to land as a fourth *anchor* (parallel to `#der-chain-confidence-decay`'s role):

- **(I')** Identify a compositional quantity whose log-decomposition is a **mathematical identity** via a probability/algebraic identity — not a theorem conditional on an AAD-internal axiom.

Below I attack five candidates against this bar. The spike charter listed three; I add two more that the existing literature suggests.

---

## §2 — Candidate Axiom #1: Viability Composition

### 2.1 The candidate

From `spikes/spike-internal-external-decomposition.md`, log-viability is defined as

$$\mathcal V = \log \frac{\lVert\delta_{\text{critical}}\rVert}{R^\ast} = \log\lVert\delta_{\text{critical}}\rVert - \log R^\ast$$

with $R^\ast = \rho/\alpha$ (Model D). Persistence is $\mathcal V \gt 0$.

**Candidate composition question.** Under $n$-agent composition via `#form-composition-closure`, is composite log-viability $\mathcal V_c$ additively decomposable over sub-agent log-viabilities $\mathcal V_i$?

### 2.2 Candidate axiom

*[Candidate axiom — viability composition]*

For $n$ independent sub-agents (architecturally modular, teleologically aligned via route C-i of `#scope-composite-agent`, and facing disturbance channels that factor independently), the composite log-viability decomposes additively:

$$\mathcal V_c \;=\; \sum_i \phi_i \mathcal V_i \;+\; \mathcal V_{\text{coupling}}$$

for some weights $\phi_i \geq 0$ and a coupling term.

The hoped-for Cauchy FE argument: the composite viability $V_c = \lVert\delta_{\text{critical},c}\rVert/R_c^\ast$ should relate multiplicatively to the individual viabilities via the sub-additive tempo inequality (`#der-tempo-composition`) and the weakest-link bound on $R$, so $\log V_c$ should be forced additive.

### 2.3 Derivation attempt

From `spikes/spike-critical-mass-composition.md` (CM4), symmetric-matched-Tier-1 dyad gives

$$\kappa_c = (\alpha - C)R - \rho - \gamma(U_O)\mathcal T$$

Persistence is $\kappa_c \gt 0$. The composite ultimate bound is

$$R_c^\ast = \frac{\rho + \gamma\mathcal T}{\alpha - C}$$

So composite log-viability is

$$\mathcal V_c = \log\lVert\delta_{\text{critical},c}\rVert - \log(\rho + \gamma\mathcal T) + \log(\alpha - C)$$

For this to decompose as $\sum \phi_i \mathcal V_i + \mathcal V_{\text{coupling}}$ we'd need:

$$\log(\alpha - C) \;\overset{?}{=}\; \log\alpha_1 + \log\alpha_2 + (\text{correction})$$

$$\log(\rho + \gamma\mathcal T) \;\overset{?}{=}\; \log\rho_1 + \log\rho_2 + (\text{correction})$$

Neither is cleanly additive in the sub-agent log-quantities. $\log(\alpha - C)$ is $\log\alpha + \log(1 - C/\alpha)$, so subtracting $\log\alpha$ leaves a correction term $\log(1 - C/\alpha)$ that depends on the ratio — **not the product — of AAD primitives**. Worse, $\rho + \gamma\mathcal T$ is a *sum*, not a product; its log is the log of a sum, which does not split at all.

**Concrete failure.** Take the symmetric-matched case: $\alpha_1 = \alpha_2 = \alpha$, $\rho_1 = \rho_2 = \rho$, $C = 0$, $\gamma = 0$. Then $\mathcal V_c = \log\lVert\delta_{\text{critical},c}\rVert - \log\rho + \log\alpha$. Comparing to individual $\mathcal V_i = \log\lVert\delta_{\text{critical}}\rVert - \log\rho + \log\alpha$: the two are **equal** (up to $\lVert\delta_{\text{critical},c}\rVert$ vs $\lVert\delta_{\text{critical}}\rVert$, which is a projection-choice artifact). No additive decomposition was extracted — the composite is essentially "one of the agents," not "the sum of the agents."

**Deeper failure.** Even if one wanted to *posit* additive decomposition axiomatically, the underlying disturbance coupling is through a **sum** $\rho + \gamma\mathcal T$, not a product. The Cauchy FE machinery requires multiplicative structure on the prior coordinate. Logging a sum does not give an additive decomposition; it gives a logarithm-of-a-sum, which has no Cauchy-FE uniqueness story.

### 2.4 Verdict

**Candidate 1 fails at step (I) — no multiplicative structure under composition.** Composite viability does not relate multiplicatively to sub-agent viabilities because the mechanisms of composition (coupling via disturbance sum, coordination cost via subtraction) operate **additively in the natural untranslated coordinate**, not multiplicatively. Cauchy FE machinery cannot be applied.

This matches the `spikes/spike-internal-external-decomposition.md` §2's classification of log-viability as an *adjacent family member* of the three anchors — logarithmic by *matching* to the structure of $R^\ast = \rho/\alpha$ (a ratio), not forced by a Cauchy-FE argument on a composition axiom. The spike here confirms the adjacency and adds the finding that **even extending log-viability to the composition layer does not change the classification**: it remains adjacent.

---

## §3 — Candidate Axiom #2: Persistence-Cost Composition

### 3.1 The candidate

From `spikes/spike-persistence-cost.md` §6, the persistence-cost lower bound is

$$\dot R_{\min} \geq \frac{n\alpha}{2}\text{ nats/time}$$

Channel-capacity floor: $C \geq \mathcal T/2$.

**Candidate composition question.** Does composite persistence cost decompose additively over sub-agent costs?

### 3.2 Candidate axiom

*[Candidate axiom — persistence-cost composition]*

For $n$ sub-agents with independent observation channels facing independent disturbance statistics, the composite's minimum sustained information rate $\dot R_{\min,c}$ decomposes as the **sum** of sub-agent minimum rates plus a coordination term:

$$\dot R_{\min,c} \;=\; \sum_i \dot R_{\min,i} \;+\; \dot R_{\text{coord}}$$

Hoped-for Cauchy FE derivation: the composite's rate-distortion function over $n$ independent Gaussian channels decomposes as a sum (standard Shannon result), and the sum is directly additive.

### 3.3 Derivation attempt

Shannon's rate-distortion theorem for $n$ independent Gaussian sources gives

$$R(D^2) = \sum_i R_i(D_i^2)$$

directly — this is a well-known property of independent sources (Cover & Thomas 2006 §10.3.3). So for independent sub-agent channels:

$$\dot R_{\min,c} = \sum_i \dot R_{\min,i}$$

exactly. With `spikes/spike-persistence-cost.md`'s identification $\dot R_{\min,i} = \alpha_i/2$, the composite rate is $\sum_i \alpha_i/2$.

**But this is additivity in the *rate* coordinate, not in a *logarithmic* coordinate.** The sum is additive in nats/time, which is already an additive quantity — the logarithm has already been taken inside Shannon's theorem (via $R = I(X;T)$ mutual information, which is logarithmic by construction). There is no *further* Cauchy-FE uniqueness argument to run; the rate is already on the log-scale coordinate.

**Test against the three-instance pattern.** Chain / divergence / update each start from a *product* structure and derive *sum on log-scale*. Here we start from a sum structure (rate-distortion of independent Gaussians is additive by Cover-Thomas). The "log coordinate" was already taken when we moved from joint distributions to mutual information. There is no Cauchy FE to solve — nothing is being forced to be logarithmic.

**What *is* true:** the persistence-cost rate is **additively composable across independent channels**. This is a useful compositional property, but it is not a Cauchy-FE-forcing theorem; it is a *corollary* of Shannon's theorem that has nothing to do with AAD-internal axioms.

### 3.4 Verdict

**Candidate 2 fails at step (II) — no AAD-internal axiom is being invoked.** The additivity is a standard consequence of Shannon's rate-distortion theorem for independent Gaussian sources, not a theorem conditional on an AAD-internal axiom. The result is clean and useful, but it sits in the same structural position as the IB Lagrangian: *adopted from an external theorem*, not *derived from an AAD-internal axiom*.

Classification: **adjacent family member** in the same sense as IB. The additive decomposition is an adopted-external-theorem, not an AAD-internal Cauchy-FE move.

---

## §4 — Candidate Axiom #3: Log-Identifiability Composition

### 4.1 The candidate

`#disc-identifiability-floor` states structural no-go results from external information-theoretic theorems. Each agent faces an identifiability floor determined by Fisher information: what it *cannot* distinguish with its current observation channel and model class.

**Candidate composition question.** When $n$ agents pool observations (team, crèche, organization), does the composite identifiability-shortfall decompose additively over sub-agent Fisher information contributions?

### 4.2 Candidate axiom

*[Candidate axiom — Fisher information composition]*

For $n$ agents observing independent samples from a shared parameter family $\{P_\theta\}$, the composite Fisher information $I_c(\theta)$ is the **sum** of sub-agent Fisher information:

$$I_c(\theta) = \sum_i I_i(\theta)$$

and therefore log-identifiability-shortfall (where "shortfall" relates to Cramér-Rao) decomposes additively.

Hoped-for Cauchy FE: the Fisher information additivity under independent samples is a theorem (Lehmann & Casella 1998 §2.6); applied on log-scale would give Cauchy-FE forcing.

### 4.3 Derivation attempt

Fisher information additivity: for independent observations $Y_1, \ldots, Y_n$ from parameter family $\{P_\theta\}$,

$$I_{Y_1, \ldots, Y_n}(\theta) = \sum_i I_{Y_i}(\theta)$$

This is a direct consequence of the factorization of joint likelihoods: $\log P(y_1, \ldots, y_n; \theta) = \sum_i \log P(y_i; \theta)$, so the score $\ell'_\theta = \sum_i \ell'_{\theta,i}$ and under independence the variances add.

**Checking against the pattern.** The multiplicative structure is the joint likelihood factorization $P(\mathbf y; \theta) = \prod_i P(y_i; \theta)$. Logarithm: $\log P(\mathbf y; \theta) = \sum_i \log P(y_i; \theta)$. This is **exactly the `#der-chain-confidence-decay` move** — log of a product is a sum of logs, applied to likelihood functions of $\theta$ at multiple independent samples.

**So this is not a new forcing argument — it is an application of `#der-chain-confidence-decay`'s chain-rule identity** to a different object (likelihoods of multiple samples, rather than confidences of multi-step plans). Fisher information is the variance of the score, where the score is the derivative of the log-likelihood; the score's additivity under independence follows from the log's additivity under independence.

**Re-classified.** Fisher information composition is **not** a fourth theorem; it is a **corollary of `#der-chain-confidence-decay`'s anchor identity**, applied to likelihood functions in a compositional setting. The anchor does reach the composition layer — but via its *direct* application (log of a product of likelihoods is a sum of log-likelihoods), not via a new Cauchy-FE theorem conditional on an AAD-internal axiom.

**What the spike charter expected (log-identifiability-shortfall) vs. what's there (Fisher info).** The charter asked about log-identifiability-shortfall combining additively. "Shortfall" would be something like $\log(I_{\text{required}}/I_{\text{available}})$ — which decomposes as $\log I_{\text{required}} - \log I_{\text{available}}$, where each is computed via the Fisher-information additivity above. So the shortfall *does* decompose additively, but this is a direct consequence of the Fisher-additivity and therefore of the chain-rule identity. No new axiom, no new Cauchy FE.

### 4.4 Verdict

**Candidate 3 is a corollary of the chain-layer anchor, not a new theorem.** Fisher-information composition (and hence log-identifiability-shortfall composition) is a direct application of `#der-chain-confidence-decay`'s log-of-product-is-sum-of-logs identity to multi-sample likelihood functions. The result is genuine — it really does give additive composition of identifiability shortfalls — but it sits under the chain layer rather than as a parallel fourth theorem.

Interesting structural observation: **the chain-layer anchor *does* reach Section III**, but as a direct application rather than as a new theorem. In other words, `#der-chain-confidence-decay` already has compositional content that has not been surfaced; that content is "the anchor applies to likelihood factorizations across independent samples, and this gives Fisher-information additivity and identifiability-shortfall composition automatically." This is a candidate Discussion-section addition to `#der-chain-confidence-decay`, not a new segment.

---

## §5 — Candidate Axiom #4: Log-Closure-Deficit Along a Composition Tower

This is the most serious candidate — the one that engages composition machinery directly rather than single-agent quantities-lifted-to-groups.

### 5.1 The candidate

From `#form-composition-closure`: the closure defect $\varepsilon^\ast$ measures how well a coarse-graining projection $\Lambda$ and macro-dynamics $(\pi_c, E_c, f_c)$ approximate the micro-system. For sequential coarse-graining — a **composition tower** of level 0 (atomic) → level 1 (dyads / teams) → level 2 (organizations) → ... → level $L$ — each level has its own closure defect $\varepsilon_\ell^\ast$ against the level-below.

**Candidate composition question.** Under a composition tower with projections $\Lambda_1, \ldots, \Lambda_L$ composing as $\Lambda_L \circ \cdots \circ \Lambda_1$, is there a multiplicative structure on trajectory-error bounds such that a log-closure-deficit coordinate forces additive decomposition via Cauchy FE?

### 5.2 The multiplicative structure

The bridge lemma in `#form-composition-closure` gives

$$\limsup_{m \to \infty} \lVert e_m^{(\ell)}\rVert \leq \frac{\varepsilon_\ell^\ast \nu_c^{(\ell)}}{\alpha_c^{(\ell)}}$$

for the level-$\ell$ trajectory error (where $e_m^{(\ell)}$ is the projection-error at macro-boundary $m$ of level $\ell$). Under sequential composition with an $L$-level tower, the **total** trajectory error between level-0 truth and level-$L$ description can be expressed via a telescoping argument:

$$\lVert e_m^{(0 \to L)}\rVert \leq \sum_\ell \Lambda_\ell^{\text{lip}} \cdot \frac{\varepsilon_\ell^\ast \nu_c^{(\ell)}}{\alpha_c^{(\ell)}}$$

where $\Lambda_\ell^{\text{lip}}$ is the Lipschitz constant of the projection at level $\ell$ (from condition (P2) in `#form-composition-closure`).

**Is there a multiplicative form?** Observe that if each projection is $L$-Lipschitz and the level-$\ell$ bridge lemma requires a contraction factor $\kappa_\ell = \alpha_\ell/\nu_\ell \leq 1$, then **sequential contraction factors multiply**:

$$\prod_{\ell=1}^L \kappa_\ell \leq \prod_{\ell=1}^L \frac{\alpha_\ell}{\nu_\ell}$$

This is the standard telescoping of contraction rates under a composition tower (Lohmiller & Slotine 1998; see also contraction analysis for cascade systems). On log-scale:

$$\log\prod_\ell \kappa_\ell \;=\; \sum_\ell \log \kappa_\ell \;=\; \sum_\ell (\log\alpha_\ell - \log\nu_\ell)$$

**This is an additive decomposition on a log-coordinate.** Let $\mathcal D_\ell := -\log\kappa_\ell = \log(\nu_\ell/\alpha_\ell)$ be the **level-$\ell$ log-contraction-deficit**; then

$$\mathcal D_{\text{tower}} \;=\; \sum_\ell \mathcal D_\ell$$

with the persistence-under-composition condition being $\mathcal D_{\text{tower}} \lt \infty$ and specifically $\sum_\ell \mathcal D_\ell \leq \log(R/\varepsilon^\ast_{\text{target}})$ or similar.

### 5.3 Is this a Cauchy-FE theorem?

**Testing against the pattern.** The multiplicative structure is the product of contraction factors $\prod_\ell \kappa_\ell$. Taking logarithms gives additivity. For this to be a fourth *theorem* in the style of the divergence and update layers, we'd need:

1. An **AAD-internally-motivated additivity axiom** on the log-contraction-deficit.
2. A **Cauchy functional equation** enforced by that axiom.
3. Logarithm as the **unique** coordinate forced.

**What's there.** The log-additivity is a **mathematical identity** via the standard $\log(\prod) = \sum \log$ identity, applied to the sequential-composition contraction factors. This is the **same mathematical identity that anchors `#der-chain-confidence-decay`**, applied to a different object (sequential contraction factors, rather than chain probabilities).

**What's not there.** There is no additional AAD-internal axiom being invoked. The multiplicative structure ($\prod \kappa_\ell$) is a mathematical consequence of the bridge-lemma form (sector-persistence-template with telescoping), not a commitment. Taking the log is a **matching** move — matching the coordinate to the existing multiplicative structure — not a **forcing** move via Cauchy FE on an axiom.

**Is the multiplicative structure itself forced?** Partial. The product-of-contraction-factors form comes from the sector-persistence-template's one-level bridge lemma. If the template form is accepted (and it is, across the six instances catalogued in `#result-sector-persistence-template`), then sequential application produces the product. The product is *derived* from the template; the template is *chosen* as AAD's persistence-analysis shape. So the derivation chain is:

$$\text{sector-persistence-template (chosen shape)} \;\to\; \text{bridge-lemma form (derived, conditional on DA2'-inc)} \;\to\; \text{sequential product structure (derived)} \;\to\; \text{log-additive decomposition (mathematical identity)}$$

Each step is justified, but the overall move is a **chained consequence**, not a Cauchy-FE-on-an-axiom theorem. It lives structurally between "chain-rule identity" (mathematical, no axiom required) and "divergence theorem" (AAD axiom + Cauchy FE).

### 5.4 Closer examination — does a Cauchy-FE-compatible axiom exist?

Push harder. Can one frame an axiom that would promote this to theorem status?

**Candidate axiom: sequential-bridge-lemma additivity.** Posit: for any composition tower, the total log-contraction-deficit decomposes additively over levels, and this decomposition is forced by requiring that the tower's macro-trajectory error bound be expressible as a *single* deficit rather than a coupled system.

Applying the Cauchy FE machinery: let $\Psi$ be any smooth monotone reparameterization of contraction-factor-space such that $\Psi(\kappa_1 \kappa_2) = \Psi(\kappa_1) + \Psi(\kappa_2)$ for independent contraction factors. This is $\Psi(xy) = \Psi(x) + \Psi(y)$ — the classical Cauchy equation on the multiplicative group — forcing $\Psi(x) = c\log x$.

**Good — Cauchy FE applies.** If the additivity axiom is accepted, log is forced.

**But the axiom is a direct restatement of the multiplicative structure.** The chain layer says "probability products factor into sums of log-probabilities" — this is a *mathematical identity* from $\log(xy) = \log x + \log y$. The composition tower axiom above says "contraction factors multiplicatively along a composition tower factor into sums of log-contraction-deficits" — and *this* is also the same mathematical identity. Both rest on $\log$ of a product being a sum of logs.

**What distinguishes the divergence / update theorems?** The divergence-layer axiom says "chain-rule additivity for *f-divergences*" — this is **not** a mathematical identity, because $f$-divergences are a family of quantities and the chain rule holds for only one member of that family (reverse-KL). The axiom commits to a *specific* shape that could have been different; Cauchy FE shows the shape forces a specific functional form.

The update-layer axiom says "evidential additivity for *credence update functions*" — this is **not** a mathematical identity, because credence update functions could in principle be multi-coordinate or non-single-valued. The axiom commits to a specific shape; Cauchy FE shows the shape forces log-odds.

**The composition-tower candidate is closer to the chain layer than to the divergence/update layers.** The "axiom" is not selecting a specific functional form from a family of possibilities — it is restating that contraction factors compose multiplicatively, which is a mathematical consequence of sequential composition. The $\log$ is forced at the same level at which it is forced in `#der-chain-confidence-decay`: *mathematically, no axiom needed*.

### 5.5 Verdict: fourth anchor, not fourth theorem

**Candidate 4 achieves anchor-status but not theorem-status.** The log-contraction-deficit *does* decompose additively along a composition tower (by $\log$ of product = sum of logs), and the decomposition *does* sit at Section III. But it is anchor-style (mathematical consequence of the multiplicative composition structure), not theorem-style (conditional on an AAD-internal axiom whose additivity claim is a *choice* rather than an identity).

Under the charter's step (I'):

- **(I') Identify a compositional quantity whose log-decomposition is a mathematical identity via a probability/algebraic identity** — yes, with $\mathcal D_\ell = \log(\nu_\ell/\alpha_\ell)$ along a composition tower and $\log(\prod \kappa_\ell) = \sum \log\kappa_\ell$.

So Candidate 4 lands as a **fourth anchor**, parallel to `#der-chain-confidence-decay`. This is a legitimate structural finding, but it is *weaker* than a fourth theorem (which is what the charter asked for).

**Honest epistemic status.** The result is under-ripe. The sequential-contraction-product structure is standard in contraction analysis (Lohmiller-Slotine 1998) and has been used implicitly in AAD's bridge-lemma cascading. Naming it as the "composition-layer anchor" in `#additive-coordinate-forcing` would:

- Be honest about its anchor-rather-than-theorem status.
- Surface a genuine compositional move that the meta-segment currently does not capture.
- Risk overstating Section III symmetry (1 anchor at single-agent + 1 anchor at composition = 2 anchors; 2 theorems at single-agent + 0 theorems at composition = asymmetric in a way that might invite further overclaiming).

---

## §6 — Candidate Axiom #5: Shared-Intent Compression Across Channels

Attempted as a last push. Mentioned in `#additive-coordinate-forcing`'s Working Notes as a candidate future layer.

### 6.1 The candidate

`#def-shared-intent` (Section III) defines shared intent as an IB-compressed purpose common across agents in a composite. Communication between agents has costs — communication gain $\eta_{ji}^\ast$ (`#hyp-communication-gain`), channel capacity, coordination overhead $C_{\text{coord}}$.

**Candidate composition question.** Does shared-intent cost aggregate additively across pairwise communication channels, with the log of pairwise trust-weighted confidence forced as the unique additive coordinate?

### 6.2 Attempted derivation

For pairwise communication, let $\eta_{ji}^\ast = U_{M_i}/(U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji})$ be the gain from agent $j$ communicating to agent $i$ (per `#hyp-communication-gain`).

**Candidate axiom:** the total shared-intent communication cost across a composite of $n$ agents decomposes additively over pairwise channels:

$$C_{\text{intent}}^{\text{total}} = \sum_{i \neq j} c_{ji}(\eta_{ji}^\ast)$$

where $c_{ji}$ is the per-channel communication cost as a function of the channel's communication gain.

For this to force a log coordinate via Cauchy FE, we'd need the pairwise gains to compose multiplicatively in some natural way, e.g., $\eta_{ji}^\ast$ along a communication tree composes as a product of edge gains, and the overall "reachability cost" would log-decompose into edge costs.

**Works only on trees.** If the communication structure is a tree (star / hierarchy), then reachability from agent $j$ to agent $i$ along the path $j \to k_1 \to k_2 \to \ldots \to i$ multiplies along edges (each edge's gain is a likelihood-ratio-like factor, and independence across edges gives a product of ratios; cf. `#der-chain-confidence-decay`). Taking the log gives additive decomposition of log-reachability into per-edge log-gains.

**Applied-`#der-chain-confidence-decay` again.** This is another instance of the chain-layer anchor, applied to communication trees rather than causal plans. The multiplicative structure comes from independence-across-edges + likelihood-ratio-structure, which is the same foundation as the chain layer.

**Not a new theorem; recapitulates the chain anchor on a different domain.** The chain anchor reaches the communication-tree composition layer, just as it reaches the likelihood-composition layer (§4).

### 6.3 Verdict

**Candidate 5 is a second application of the chain-layer anchor, to communication trees.** Like Candidate 3 (Fisher-info / identifiability), it extends the chain anchor's reach to a composition setting without inventing a new axiom. The compositional structure is there but derives from chain-layer rather than from an independent Section III commitment.

**Meta-observation.** Candidates 3, 4, and 5 all show that **`#der-chain-confidence-decay` is an anchor whose reach extends beyond the strategy DAG**. Its mathematical identity (log of product is sum of logs) applies wherever:
- Probabilities / likelihoods factor under independence (likelihoods across samples — Candidate 3).
- Contraction factors multiply under sequential composition (composition tower — Candidate 4).
- Gains multiply under tree-structured communication (communication tree — Candidate 5).

The anchor is more productive at the composition layer than the current `#additive-coordinate-forcing` surfaces. This is a **surfacing opportunity** for `#der-chain-confidence-decay`, not a new theorem.

---

## §7 — The Structural Obstruction Against a Fourth Theorem

### 7.1 Pattern across all five candidates

| Candidate | Multiplicative structure? | AAD-internal axiom needed? | Cauchy FE selects from family? | Landing |
|---|---|---|---|---|
| 1. Viability composition | **No** — composition is additive (disturbance sum, cost subtraction) | — | — | Fails at step (I) |
| 2. Persistence-cost composition | Already on log-scale (rate is logarithmic) | No — Shannon's theorem used | No | Adjacent (like IB) |
| 3. Fisher-info / identifiability | Yes (likelihood factorization) | No — follows from chain anchor | No | Corollary of chain anchor |
| 4. Composition-tower contraction | Yes (sequential product) | No — mathematical identity | No | Fourth anchor |
| 5. Shared-intent / communication trees | Yes (tree product) | No — follows from chain anchor | No | Corollary of chain anchor |

None of the five achieves theorem-status parallel to divergence and update.

### 7.2 Why — the structural reason

The divergence layer forces log via Cauchy FE on the **chain-rule axiom for f-divergences**. This axiom is substantive because $f$-divergences are a *family* of candidate functional forms, and the axiom selects one. The Cauchy FE derivation rules out $\chi^2$, Rényi, Hellinger, etc., and leaves only reverse-KL.

The update layer forces log-odds via Cauchy FE on the **evidential-additivity axiom for credence updates**. This axiom is substantive because credence updates are a *family* of candidate reparameterizations, and the axiom selects one. The Cauchy FE derivation rules out probability-additive, inverse-additive, etc., and leaves only log-odds.

**For a fourth theorem, we'd need a composition-layer family of candidate functional forms, with an AAD-internal axiom that selects one.** But composition-layer quantities do not present as a family of candidate reparameterizations. They present as:
- **Sums** (disturbance coupling, coordination cost) — no multiplicative structure to transform.
- **Products** (contraction factors, likelihoods, gains along trees) — already resolved by the chain anchor's mathematical identity.
- **Adopted external theorems** (Shannon rate-distortion over independent channels) — adopted, not AAD-forced.

**The structural reason is that composition is not a family of functional-form choices.** Composition is defined by *coupling* structure — shared environment, shared objective, teleological unity. The act of composition is choosing a *coupling pattern* (which agents share what), not choosing a *functional form* for how to encode the composition. The Cauchy-FE-forcing machinery operates on functional-form choices; composition choices live in a different space (graph structures, tiering, tier-specific contraction verification).

### 7.3 What this means for the meta-pattern

`#additive-coordinate-forcing` is architecturally a **single-agent family**: chain / divergence / update index three layers of a *single* agent's internal machinery. Extending the pattern to composition requires either:

**Option A. Accept that the composition layer adds a fourth anchor, not a fourth theorem.** The log-contraction-deficit additivity along a composition tower is a legitimate compositional anchor. This extends `#additive-coordinate-forcing` with asymmetric structure (2 anchors + 2 theorems), honest about the difference.

**Option B. Accept that the composition layer is not in `#additive-coordinate-forcing`'s structural family at all.** Composition admits its own structural family — **monotonicity under composition** (which is the bridge-lemma shape plus tier-specific conditions on when contraction survives composition). This family deserves its own meta-segment, parallel to the three meta-segments but at the composition layer: `#bridge-lemma-family` or `#composition-monotonicity-pattern`.

**Option C. Surface `#der-chain-confidence-decay`'s composition-layer corollaries at the segment level, without promoting them to meta-pattern.** The chain anchor reaches Fisher-info composition, composition-tower contraction, and communication-tree gains. Each is a useful corollary; none is a fourth theorem; and `#der-chain-confidence-decay` already has segment-level real estate for these applications.

### 7.4 Recommendation on which option

I recommend a *conjunction* of Option A (lightly) and Option C (substantively), with Option B as a follow-on for Section III:

**Option C (substantive)**: add a Discussion note to `#der-chain-confidence-decay` naming the anchor's three-fold reach into composition-layer applications (likelihoods / composition towers / communication trees). This surfaces the existing structure without reorganizing `#additive-coordinate-forcing`.

**Option A (light)**: add a Working Notes entry to `#additive-coordinate-forcing` documenting that the composition-tower log-contraction-deficit is anchor-style (not theorem-style), with this spike as the reference. This honestly acknowledges the Section III symmetry question without overclaiming a fourth instance.

**Option B (deferred)**: capture for future work that composition *does* have its own structural family — *monotonicity under composition* — organized around the bridge-lemma form, the Tier 1/2/3 classification, and the critical-mass inequality (CM4 from `spikes/spike-critical-mass-composition.md`). This family is not isomorphic to `#additive-coordinate-forcing`; forcing it into that shape would overclaim. Developing it as its own meta-pattern is a genuine follow-on spike.

---

## §8 — Relation to SOC Speculation (`spikes/spike-soc-composition.md`)

The SOC-speculation spike conjectured an RG-style fixed-point argument on composition — self-similarity under coarse-graining producing power-law tails and an "optimal-at-critical" conjecture. Does this interact with the spike's candidates?

**Candidate 4 interaction.** The composition-tower structure with sequential contraction $\prod_\ell \kappa_\ell$ is precisely the setup in which RG-style fixed-points would appear. If the tower were self-similar ($\alpha_\ell$, $\nu_\ell$ invariant under level), the product $\prod_\ell \kappa_\ell$ would exhibit a critical point at $\kappa_\ell = 1$ (the persistence threshold), and approaching criticality from above would show power-law slowdown.

**But the RG-fixed-point argument is structurally different from the Cauchy-FE argument.** RG operates on **parameter flow** under coarse-graining: does $(\alpha, \rho, R, \gamma)$ at one scale map (under a coarse-graining projection) into $(\alpha', \rho', R', \gamma')$ at the next scale, with a fixed point of the flow? The Cauchy-FE argument operates on **coordinate forcing** for a single quantity, not on parameter flow.

**They are complementary, not competing.** RG-speculation asks: how do AAD parameters flow under coarse-graining? Cauchy-FE-at-composition asks: how does a single compositional quantity decompose across levels? Both are structural questions about Section III, addressing different aspects. The RG-speculation is currently parked (`spikes/spike-soc-composition.md`); this spike does not activate it.

---

## §9 — Honest Epistemic Assessment

### 9.1 What this spike achieves

1. **Negative characterization.** Four candidate composition-layer axioms (viability, persistence-cost, Fisher-info, composition-tower, shared-intent) do not land as fourth-theorem instances parallel to divergence and update.

2. **Structural reason.** Composition is a coupling-pattern choice, not a functional-form choice; Cauchy-FE machinery operates on functional-form families. The machinery is architecturally single-agent.

3. **Anchor-layer composition finding.** The log-contraction-deficit along a composition tower is additively decomposable, but as a mathematical consequence of $\log(\prod) = \sum\log$, not as a theorem conditional on an AAD-internal axiom. This is a fourth anchor (parallel to `#der-chain-confidence-decay`), not a fourth theorem.

4. **Chain anchor reaches Section III.** The chain-layer anchor has unsurfaced reach: Fisher-info additivity across samples, contraction-factor additivity across towers, and gain additivity across communication trees all follow from it directly. These are corollaries of `#der-chain-confidence-decay`, not new theorems.

5. **Identification of the natural Section III structural family.** Composition's own family is **monotonicity under composition** (bridge-lemma form, Tier 1/2/3, critical-mass inequality (CM4)) — parallel to but not reducible to `#additive-coordinate-forcing`.

### 9.2 What this spike does not achieve

1. **No fourth-theorem promotion.** The spike does not land a fourth instance of `#additive-coordinate-forcing` at theorem-level. The three-theorem structure (divergence / update at theorem-level; chain at anchor-level) is confirmed.

2. **No full derivation of Option A's anchor extension.** Candidate 4's anchor-status is stated but not formally derived — the spike describes the log-decomposition of sequential contraction factors and notes that AAD's bridge-lemma machinery produces this naturally, but does not produce a segment-ready derivation.

3. **No exploration of Option B in depth.** The identification of "monotonicity under composition" as Section III's own structural family is named but not developed as a meta-segment. That's a follow-on spike.

### 9.3 Epistemic tier of the findings

- **Negative characterization (Candidates 1–5 do not achieve theorem-status).** **Exact** for Candidates 1 and 2 (multiplicative structure absent / Shannon's theorem adopted directly). **Exact** for Candidates 3 and 5 (direct consequences of the chain anchor's identity). **Robust qualitative** for Candidate 4 (the anchor classification is clear; the formal derivation needs another round to be segment-ready).

- **Anchor-layer composition finding.** **Robust qualitative.** The form is clean; the segment-ready derivation is one pass away.

- **Chain-anchor composition-layer corollaries.** **Exact.** Fisher-info additivity from likelihood factorization, contraction-tower additivity from sequential-product contraction, communication-tree additivity from tree-structured multiplication.

- **Meta-architectural finding (composition is a different family, not `#additive-coordinate-forcing`).** **Robust qualitative.** Structurally motivated; the formal derivation of "composition is coupling-pattern-choice, not functional-form-choice" is at the discussion-grade level.

### 9.4 Confidence

- **High confidence** that no fourth theorem parallel to divergence/update lands in the composition layer, given the structural reason in §7.2.

- **Medium-high confidence** that Candidate 4 (log-contraction-deficit along composition tower) is the right fourth-anchor candidate, and that it is anchor-level rather than theorem-level.

- **Medium confidence** that composition's own structural family is "monotonicity under composition" as sketched. This is the follow-on-spike territory.

- **Low confidence** on whether Option A (light anchor extension) or Option B (deferred follow-on) is the right priority. Both are honest; the prioritization is a framing question.

---

## §10 — Recommendations for Landing

### 10.1 `#additive-coordinate-forcing` Working Notes addition

Add a working note:

> **Composition-layer candidate (anchor-style, not theorem-style).** The log-contraction-deficit $\mathcal D_\ell = \log(\nu_\ell/\alpha_\ell)$ along a composition tower decomposes additively, $\mathcal D_{\text{tower}} = \sum_\ell \mathcal D_\ell$, via $\log$ of product-of-contraction-factors $\prod_\ell \kappa_\ell$. The decomposition is anchor-style (mathematical identity via sequential-composition telescoping) rather than theorem-style (no AAD-internal additivity axiom selecting among functional forms). If promoted, it would extend the pattern to "2-anchor-plus-2-theorem" at the cost of asymmetric structure (three layers are single-agent, one is compositional). Promoted only if the Section III symmetry is considered desirable over the architectural honesty that the pattern is structurally single-agent. See `spikes/spike-compositional-coordinate.md` §5 for the full analysis.

### 10.2 `#der-chain-confidence-decay` Discussion addition

Add a Discussion paragraph:

> **The anchor reaches Section III directly.** The log-of-product-is-sum-of-logs identity extends beyond the strategy DAG: (a) across independent likelihood samples, it gives Fisher-information additivity and log-identifiability-shortfall composition (Cramér-Rao-based, `#disc-identifiability-floor` Instance 2); (b) along a composition tower of Tier 1 sub-agents, it gives additive decomposition of log-contraction-deficit $\mathcal D_{\text{tower}} = \sum_\ell \log(\nu_\ell/\alpha_\ell)$ (`#form-composition-closure` bridge-lemma-in-sequence); (c) along communication trees with multiplicative trust-weighted gains, it gives additive decomposition of log-reachability per pairwise channel (`#hyp-communication-gain`). These are direct corollaries of the chain-layer identity, not new theorems. The anchor's reach is wider than the strategy-DAG context in which it is currently derived.

### 10.3 Follow-on spike: composition's own structural family

Mark as an open follow-on in `spikes/INDEX.md`:

> **Composition monotonicity pattern (follow-on from `spike-compositional-coordinate.md`).** `#additive-coordinate-forcing` is architecturally single-agent. Composition admits its own structural family — *monotonicity under composition* — organized around the bridge-lemma form, the Tier 1/2/3 contraction classification, and the critical-mass inequality (CM4). This family is parallel to but not reducible to `#additive-coordinate-forcing`. Candidate meta-segment: `#composition-monotonicity-pattern` or `#bridge-lemma-family`. Scope: names the three-part shape (atomic contraction / tier-gated transfer / critical-mass threshold) across composition-tower, tempo-composition, team-persistence, adversarial-destabilization, composition-closure. Status: parked pending independent motivation.

### 10.4 What not to do

- **Do not promote Candidate 4 to a fourth theorem.** It is anchor-level, and the 1-anchor-plus-2-theorem characterization's epistemic cleanliness depends on not collapsing the distinction.
- **Do not add Candidate 1 (viability), 2 (persistence-cost), 3 (Fisher-info), or 5 (communication-tree) as primary instances.** All are either adjacent family members (1, 2) or corollaries of the chain anchor (3, 5).
- **Do not reframe `#additive-coordinate-forcing` as "single-agent plus composition"** at this point — the pattern's cleanliness depends on its current architectural scope. Consider this reframing only if Option B (independent composition-monotonicity meta-segment) matures.

---

## §11 — Summary

**Question.** Is there an AAD-internally-motivated additivity axiom that forces a *composition coordinate* — a fourth theorem in the `#additive-coordinate-forcing` family living at Section III?

**Answer.** No, at theorem-level. Maybe, at anchor-level (Candidate 4: log-contraction-deficit along composition tower).

**Structural reason.** Cauchy-FE-on-AAD-axiom forcing operates on **functional-form families** (f-divergences, credence reparameterizations). Composition-layer quantities present as **coupling-pattern choices**, not functional-form families. The pattern is architecturally single-agent.

**Valuable findings from failure branches.**

1. The chain-layer anchor (`#der-chain-confidence-decay`) has unsurfaced reach into Section III via Fisher-info composition, composition-tower contraction, and communication-tree gains. Surfacing this in the segment is a cheap concrete improvement.

2. The log-contraction-deficit along a composition tower gives an anchor-level composition-layer instance of the pattern, if a fourth anchor is wanted. It is honest to position this as anchor, not theorem.

3. Composition admits its own structural family — **monotonicity under composition** — parallel to `#additive-coordinate-forcing`. Developing this as its own meta-segment is the genuine Section III completion.

**Recommendations.**

- Add Candidate-4 anchor finding to `#additive-coordinate-forcing` Working Notes (light).
- Surface the chain-anchor's Section III reach in `#der-chain-confidence-decay` Discussion (substantive).
- Mark composition-monotonicity meta-segment as follow-on spike (deferred).

**Epistemic honesty.** The spike's biggest-ticket goal (a fourth Cauchy-FE theorem at composition) did not land. The failure structure is clean and informative. The honest findings (anchor-layer composition, chain-anchor reach, monotonicity family) are genuine contributions at lower epistemic tiers than "fourth theorem" would have been.

---

*End of spike.*
