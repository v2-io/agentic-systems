---
spike: variational-a2prime
date: 2026-04-22
status: ready-for-review
posture: strengthen-first
related_spikes:
  - spike-a2-prime-strengthening.md
  - spike-active-inference-vs-aad.md
  - spike-f20-kl-direction-strengthening.md
  - spike-adaptive-gain-dynamics.md
target_segments:
  - sector-condition-derivation.md
  - gain-sector-bridge.md
  - sector-persistence-template.md
  - cognitive-cost-strategy.md  # = strategy-complexity-cost
---

# Spike: Variational A2' — Approximate Directional Fidelity Under a KL Bound

**Gap addressed.** Variational / approximate-inference agents currently sit in A2' sub-scope β (assumed). The earlier A2' strengthening spike (`spikes/spike-a2-prime-strengthening.md`, Path 4) ruled this out of sub-scope α because "approximation error can rotate the correction." Gemini's audit flagged the resulting opacity: a large agent class (modern ML, VAE-based agents, many contemporary AI systems, active inference in practice) is left with A2' as an empirical claim rather than a derived guarantee.

**Question.** Under a quantitative control on the approximation error — specifically a KL bound on the variational posterior against the true posterior — does B1 (directional fidelity) recover with an *ε-quantified* degradation, yielding an *approximate-α* sub-scope with explicit persistence bounds?

**Posture.** Strengthen first: attempt the improbable derivations (natural-gradient VI recovering α fully; mean-field VI recovering ε-fidelity via Pinsker). Soften only where necessary (non-amortized VI with uncontrolled ε).

## 1. Setup

### 1.1 The agent

Let $z$ be a latent state (the hidden parameter on which mismatch depends), $x$ the observable (the data / event stream). The agent maintains a variational posterior $q_\phi(z \mid x)$ parametrized by $\phi$, approximating the true posterior $p(z \mid x)$. The agent's correction rule is *variational inference*:

*[Definition (Variational Update)]*

$$\phi_t = \arg\min_\phi \mathrm{KL}(q_\phi(z \mid x_{1:t}) \,\Vert\, p(z \mid x_{1:t})) \qquad \text{(idealized)}$$

In practice the agent runs a finite-step optimizer (natural-gradient, amortized inference network, coordinate ascent in mean-field) that returns some $q_\phi$ achieving $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$ for a controllable $\varepsilon$.

### 1.2 The mismatch signal under a variational posterior

The variational posterior induces a *predicted* observation distribution
$$\hat p(o_{t+1} \mid x_{1:t}) = \mathbb E_{z \sim q_\phi}[p(o_{t+1} \mid z, a_t)]$$
and the mismatch signal is $\delta_t = o_{t+1} - \hat o_{t+1}$ where $\hat o_{t+1} = \mathbb E_{\hat p}[o_{t+1}]$.

Under the *true* posterior $p(z \mid x_{1:t})$ the agent would produce $\hat o^\ast_{t+1}$; under the variational posterior it produces $\hat o_{t+1}$. The **variational-induced bias** in the predicted observation is
$$b_\varepsilon := \hat o_{t+1} - \hat o^\ast_{t+1} = \mathbb E_{q_\phi}[o_{t+1} \mid \cdot] - \mathbb E_{p}[o_{t+1} \mid \cdot]$$

This is the object that "rotates the correction" in spike-a2-prime's Path 4.

### 1.3 Target: ε-fidelity B1

Recall B1 from `#der-gain-sector-bridge`:
$$\delta^T H g(\delta) \geq c_{\min} \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R$$

The target is to derive a *relaxed* form under $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$:

*[Target Formulation (ε-fidelity B1)]*

$$\delta^T H g_\varepsilon(\delta) \geq (c_{\min} - g(\varepsilon)) \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R$$

where $g_\varepsilon$ is the correction induced by the variational posterior and $g(\varepsilon) \to 0$ as $\varepsilon \to 0$. The working question is: what is the explicit form of the degradation $g(\varepsilon)$?

## 2. Propagating the KL bound through the correction function

### 2.1 Pinsker's inequality in TV

*[Standard (Pinsker's inequality; Tsybakov 2009, Lemma 2.5)]*

For any probability measures $P, Q$,
$$\operatorname{TV}(P, Q) \leq \sqrt{\tfrac{1}{2} \mathrm{KL}(P \Vert Q)} \leq \sqrt{\tfrac{1}{2}\varepsilon}$$
when $\mathrm{KL}(P \Vert Q) \leq \varepsilon$.

### 2.2 Predicted-observation bias bound

Let $V_o := \sup_{z,a}\lVert\mathbb E[o_{t+1} \mid z, a]\rVert_\infty \lt \infty$ be the bound on the per-$z$ conditional mean (assumed finite; this is the "bounded value range" analog in observation space).

*[Derived (variational bias bound)]*

$$\lVert b_\varepsilon \rVert = \lVert \mathbb E_{q_\phi}[o \mid \cdot] - \mathbb E_p[o \mid \cdot]\rVert \leq 2 V_o \operatorname{TV}(q_\phi, p) \leq V_o \sqrt{2\varepsilon}$$

The variational bias scales as $O(\sqrt{\varepsilon})$, not $O(\varepsilon)$ — Pinsker's inequality is the binding constraint.

**Where the square root comes from.** The dual form $\operatorname{TV}(P, Q) = \tfrac{1}{2}\sup_{\lVert f\rVert_\infty \leq 1}|\mathbb E_P f - \mathbb E_Q f|$ gives the factor of 2; the Pinsker bound trades TV for $\sqrt{\mathrm{KL}}$ because TV is $L^1$-scale and KL is $L^2$-scale in divergence geometry (Csiszár 1967). Any linear functional of the posterior (expected value, mean observation, action-selection integral) inherits the $\sqrt{\varepsilon}$ scaling.

### 2.3 Effective correction under the variational posterior

Under the variational posterior, the correction is
$$g_\varepsilon(\delta) = g^\ast(\delta) + e_\varepsilon(\delta)$$
where $g^\ast$ is the correction under the true posterior and $e_\varepsilon$ is the approximation-induced perturbation. By §2.2, $\lVert e_\varepsilon(\delta)\rVert \leq L_g V_o \sqrt{2\varepsilon}$ where $L_g$ is the Lipschitz constant of the correction-from-posterior map (bounded under standard smoothness assumptions on $p(o \mid z)$).

Substituting into the inner product:
$$\delta^T H g_\varepsilon(\delta) = \delta^T H g^\ast(\delta) + \delta^T H e_\varepsilon(\delta)$$

The first term satisfies B1 (the true-posterior update is in sub-scope α by Bayesian coherence — `#der-gain-sector-bridge` §6.1). The second term is bounded by Cauchy-Schwarz:
$$\delta^T H e_\varepsilon(\delta) \geq -\lVert\delta\rVert \cdot \lVert H\rVert_{\mathrm{op}} \cdot L_g V_o \sqrt{2\varepsilon}$$

Let $C_H := \lVert H\rVert_{\mathrm{op}} \cdot L_g V_o$. Then:

*[Derived (ε-fidelity B1; Pinsker + Cauchy-Schwarz)]*

$$\delta^T H g_\varepsilon(\delta) \geq c_{\min}\lVert\delta\rVert^2 - C_H \sqrt{2\varepsilon} \lVert\delta\rVert$$

### 2.4 The degradation function g(ε)

Factor out $\lVert\delta\rVert$ to align with the sector-quadratic form. For $\lVert\delta\rVert \geq \delta_0 := C_H\sqrt{2\varepsilon}/c_{\min}$ (a lower mismatch floor below which the variational bias dominates the contraction):

$$\delta^T H g_\varepsilon(\delta) \geq \left(c_{\min} - \frac{C_H\sqrt{2\varepsilon}}{\lVert\delta\rVert}\right)\lVert\delta\rVert^2$$

The effective sector constant is
$$c_\varepsilon(\lVert\delta\rVert) = c_{\min} - \frac{C_H\sqrt{2\varepsilon}}{\lVert\delta\rVert}$$

which is $\lVert\delta\rVert$-dependent — variational contraction degrades as mismatch shrinks toward the approximation-induced floor.

**Two regime formulations.**

*Regime A — Large-mismatch sector.* For $\lVert\delta\rVert \geq 2\delta_0$: $c_\varepsilon \geq c_{\min}/2 =: c_\varepsilon^{\mathrm{lb}}$. The sector condition holds uniformly with a degraded constant.

*Regime B — Approximation-dominated floor.* For $\lVert\delta\rVert \lt \delta_0$: the bound goes negative; the agent cannot reliably contract. The variational approximation has left the agent with a residual mismatch radius $\delta_0 = O(\sqrt{\varepsilon})$.

**This is the explicit degradation function:** $g(\varepsilon) \to 0$ as $\sqrt{\varepsilon} \to 0$, scaling as **$O(\sqrt{\varepsilon})$** (Pinsker-dominated), not $O(\varepsilon)$. The $\sqrt{\varepsilon}$ rate is **tight** in general — the Pinsker bound is achieved by the two-point distribution, and the linear-functional lift is tight for extreme observation configurations.

## 3. Sector-persistence template instantiation (ε-Regime A)

Under Regime A — trajectories with $\lVert\delta\rVert \geq 2\delta_0$ — the ε-fidelity B1 gives A2' with sector constant $\alpha_\varepsilon = \eta^\ast \cdot c_\varepsilon^{\mathrm{lb}} = \eta^\ast c_{\min}/2$. The template's (T1)–(T3) hold on the *restricted region* $\mathcal B_R \setminus \mathcal B_{2\delta_0}$, which is an annulus.

### 3.1 Stopped ultimate bound

**Model D (bounded disturbance).** Apply `#result-sector-persistence-template` with stopping time $\tau := \inf\{t : \lVert\delta(t)\rVert \leq 2\delta_0 \text{ or } \lVert\delta(t)\rVert \geq R\}$. On $[0, \tau)$, the template proves
$$\lVert\delta(t)\rVert \leq \max\{\lVert\delta(0)\rVert e^{-\alpha_\varepsilon t}, \rho/\alpha_\varepsilon + 2\delta_0\}$$

Two cases:

- *If $\rho/\alpha_\varepsilon + 2\delta_0 \lt R$*: the agent persists to a radius $R^\ast_\varepsilon = \rho/\alpha_\varepsilon + 2\delta_0$. The variational-approximation floor $2\delta_0$ *adds* to the deterministic-disturbance floor.
- *If $\rho/\alpha_\varepsilon + 2\delta_0 \geq R$*: the variational approximation is too coarse for the environment — structural adaptation is needed (#result-structural-adaptation-necessity).

**Model S (stochastic disturbance).** Prop A.1S via stopping-time localization at $\tau$ (Khasminskii 2012 ch. 5; exactly the technique used in the A2' strengthening spike Path 5):

*[Derived (variational Model-S ultimate bound)]*

$$\mathbb E[\lVert\delta(t \wedge \tau)\rVert^2] \leq \lVert\delta(0)\rVert^2 e^{-2\alpha_\varepsilon t} + \frac{n\sigma_w^2}{2\alpha_\varepsilon} + (2\delta_0)^2$$

The RMS ultimate bound is
$$R^\ast_{S,\varepsilon} = \sqrt{\frac{n\sigma_w^2}{2\alpha_\varepsilon} + 4\delta_0^2} \leq \sigma_w\sqrt{\frac{n}{\alpha_\varepsilon}} + 2\delta_0$$

### 3.2 Ultimate-bound scaling

The variational floor contributes $O(\sqrt{\varepsilon})$ to the ultimate bound (since $\delta_0 \propto \sqrt{\varepsilon}$). The sector-constant degradation contributes at most a factor of 2 (from $c_{\min}$ to $c_{\min}/2$). The overall statement:

*[Result (variational persistence degradation)]*

Under $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$, the ultimate-bound radius degrades by an additive $O(\sqrt\varepsilon)$ term plus at most a factor-of-2 multiplicative hit on the sector constant. The system is $O(\sqrt\varepsilon)$-persistent relative to its exact-Bayesian counterpart.

This is the promised ε-A2' result with quantified degradation.

## 4. Mean-field VI as the workhorse case

Factorized $q_\phi(z) = \prod_i q_i(z_i)$. The KL bound has a known variational form:
$$\mathrm{KL}(q \Vert p) = \sum_i \mathrm{KL}(q_i \Vert p_i^{\text{marg}}) + I_p(z_1; \ldots; z_n) \leq \varepsilon$$
where $I_p$ is the multi-information of the true posterior across the factorization (Cover & Thomas 2006, §2.5; also Wainwright & Jordan 2008, §3.4 in the mean-field section).

**Two sources of variational error.**

1. *Per-factor approximation* $\sum_i \mathrm{KL}(q_i \Vert p_i^{\text{marg}})$ — the agent's per-dimension posterior misses the true marginal. Controllable by flexible families.
2. *Structural mismatch* $I_p(z_1; \ldots; z_n)$ — the true posterior has cross-factor dependencies the factorized $q$ cannot represent. *Irreducible* within the mean-field family.

The second is the failure mode Wainwright & Jordan 2008 (§2.3 and §5, on mean-field's optimization landscape) name as the *mean-field mode-missing* phenomenon: mean-field VI is mode-seeking, and factorization forces collapse to a single mode when $p$ is multimodal.

### 4.1 Mode-missing and B1 failure

If the true posterior is bimodal with modes $z_1^\ast, z_2^\ast$ yielding *opposite-sign* predicted observations, mean-field VI converges to one mode (picked by initialization / optimization path). The variational predicted observation is systematically biased by up to $V_o$ — not small, not bounded by $\sqrt{\varepsilon}$, because $\varepsilon$ in this case is the *intrinsic* floor $I_p(z_1; z_2)$, which can be large even with optimal per-factor $q_i$.

**Verdict for mean-field VI.** The ε-B1 derivation works *when the true posterior is approximately factorized* — $I_p$ small and thus $\varepsilon$ small. When the true posterior is strongly coupled, mean-field VI is in sub-scope β honestly — the $\sqrt\varepsilon$ bound is correct but $\varepsilon$ itself is irreducibly large, so the derivation yields no useful persistence guarantee.

This is the honest scope boundary for mean-field VI: the machinery promotes cleanly *within the approximately-factorized regime*, fails honestly *outside*.

## 5. Natural-gradient VI: recovers full sub-scope α

Natural-gradient VI (Amari 1998; Hoffman et al. 2013 "Stochastic Variational Inference"; Khan & Lin 2017 "Conjugate-Computation Variational Inference"; Khan & Nielsen 2018 "Fast yet simple natural-gradient descent") replaces the Euclidean gradient on $\phi$ with the *Fisher-corrected* gradient:
$$\phi_{t+1} = \phi_t - \eta_\phi \cdot F_\phi^{-1} \nabla_\phi \mathcal L(\phi_t)$$
where $F_\phi$ is the Fisher information matrix of $q_\phi$ and $\mathcal L$ is the variational objective (negative ELBO).

### 5.1 Why natural-gradient is (near-)α

**Claim.** For exponential-family variational posteriors with natural-gradient updates, B1 holds *structurally*, not only ε-approximately.

**Argument.** Natural-gradient descent on the ELBO equals coordinate-free mirror descent under the Fisher metric (Raskutti & Mukherjee 2015, "The information geometry of mirror descent"). For exponential-family $q$ in natural parameters, the Fisher information matrix is the Hessian of the log-partition function; natural-gradient VI reduces to *exact Bayesian updating in the natural-parameter space* (Khan & Lin 2017, §3–4 deriving CVI as conjugate-family stochastic Bayes).

This places natural-gradient VI (with exponential-family $q$) in the existing sub-scope α row "Exponential families in natural parameters" of `#der-gain-sector-bridge`: $\alpha = \eta \cdot \lambda_{\min}(\text{Fisher})$, B1 holds by Fisher-PD construction, A2' derived.

### 5.2 Where natural-gradient still degrades

When $q_\phi$ is *not* exponential-family (neural-network variational families, normalizing flows, mixture variational posteriors), the Fisher-gradient equivalence breaks. Natural-gradient remains efficient but loses the exact Bayesian equivalence. These agents fall into the ε-B1 framework of §2–3 with degradation determined by the *family's expressivity gap* against the true posterior.

**Summary.** Natural-gradient VI with exponential-family posteriors is sub-scope α (exact). Natural-gradient VI with flexible-family posteriors is ε-B1 sub-scope ($\alpha'$; see §9.1) with $\sqrt\varepsilon$ degradation.

## 6. Amortized VI (VAE-style)

Amortized VI uses a recognition network $q_\phi(z \mid x)$ shared across observations (Kingma & Welling 2013, "Auto-Encoding Variational Bayes"; Rezende et al. 2014). Two additional error sources beyond fixed-parameter VI:

1. *Amortization gap* (Cremer, Li & Duvenaud 2018, "Inference Suboptimality in VAEs"): for each $x$, $q_\phi(z \mid x)$ is suboptimal compared to the best factorized $q_x^\ast(z)$ one could fit per-example. Bounded by network expressivity.
2. *Encoder generalization error*: the network is trained on a finite dataset and faces generalization error on new $x$.

Total KL bound:
$$\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon_{\text{fam}} + \varepsilon_{\text{amort}} + \varepsilon_{\text{gen}}$$

**Composition.** The three error sources compose *additively* in KL, so the Pinsker-induced TV and observation bias scale as $\sqrt{\varepsilon_{\text{fam}} + \varepsilon_{\text{amort}} + \varepsilon_{\text{gen}}}$. Each additional source is a positive contribution to the effective floor $\delta_0 = C_H\sqrt{2(\varepsilon_{\text{fam}}+\varepsilon_{\text{amort}}+\varepsilon_{\text{gen}})}/c_{\min}$.

**Verdict.** Amortized VI degrades linearly in the number of error sources (in KL) and square-root linearly (in $\delta_0$-contribution). Not catastrophic composition, but the composition is *additive* in $\varepsilon$, which means amortized-VI agents accumulate persistence floor proportional to the number of approximation layers. The floor is controllable by (a) wider networks (reduces $\varepsilon_{\text{fam}}$ and $\varepsilon_{\text{amort}}$), (b) more training data (reduces $\varepsilon_{\text{gen}}$), (c) flow / IAF encoders (reduces $\varepsilon_{\text{fam}}$).

This gives a principled way to *budget* approximation errors across the VAE stack against the agent's persistence target: given desired ultimate bound $R^\ast$, solve $2\delta_0 \leq R^\ast/2$ for the total KL budget, then allocate across $\varepsilon_{\text{fam}}, \varepsilon_{\text{amort}}, \varepsilon_{\text{gen}}$.

## 7. Relation to active inference

Active inference (Friston et al. 2017; Da Costa et al. 2020; Parr & Pezzulo 2022) does variational Bayesian inference on a generative model with discrete-state or continuous-state posteriors. The core object is the variational posterior $Q(s)$ over hidden states.

**Implication of §§2–3 for active-inference agents.** Under a KL-bound $\mathrm{KL}(Q \Vert P(s \mid o)) \leq \varepsilon$ on the variational posterior against the true posterior:

- Active inference agents *with exponential-family generative models and natural-gradient message passing* (the standard discrete-state case in Da Costa et al. 2020 with A/B/C/D matrices and log-partition-function-based updates) inherit AAD sub-scope α via §5 — A2' is derived.
- Active inference agents with *mean-field variational posteriors and structured (non-factorized) generative models* face the mean-field mode-missing failure of §4 — ε-A2' with $\varepsilon$ potentially irreducibly large under strong cross-state dependence.
- *Sophisticated inference* (Friston, Da Costa, Hafner, Hesp & Parr 2021) adds recursive EFE depth; the recursion composes approximation errors like §6's amortized-VI composition.

**Positioning.** This gives active-inference agents a *conditional* AAD A2' guarantee — derived in the natural-gradient / exp-family subcase, ε-degraded otherwise. It does *not* commit AAD to active inference as master framework (per `spikes/spike-active-inference-vs-aad.md` §I action 5; V-strong G-BP2 remains deferred). The positioning is: AAD can *certify* active-inference agents' persistence under explicit approximation bounds, which is a sharper statement than active inference's own FEP-flow stability argument (narrow-validity per Aguilera et al. 2022).

This is a strengthening of AAD's relationship to active inference without adopting it: *AAD's sector-Lyapunov apparatus supplies the persistence guarantee that the FEP-flow argument underdelivers*.

## 8. Honest failure modes

The ε-A2' derivation works under §§2–6 assumptions. It **fails** in:

1. **Uncontrolled $\varepsilon$.** Non-amortized VI in production where the agent does not track its own KL gap. If the variational optimization has not converged (or convergence is not monitored), $\varepsilon$ is unknown and no persistence guarantee is available. **Scope.** ε-A2' applies only when the agent can bound $\varepsilon$ — e.g., via ELBO monitoring, IWAE bounds (Burda et al. 2015), or held-out log-likelihood diagnostics. Agents that do not monitor $\varepsilon$ remain in sub-scope β.

2. **Mode-missing on strongly multimodal posteriors.** Mean-field VI on posteriors with multiple well-separated modes gives irreducible $\varepsilon$ (the factorization cannot represent cross-mode structure). The $\sqrt{\varepsilon}$ bound is correct but useless — $\varepsilon$ is not small. **Scope.** ε-A2' applies under approximately-factorized true posteriors; outside this, the agent is honestly sub-scope β regardless of per-factor optimization quality. Diagnostic: true posterior's multi-information $I_p(z_1; \ldots; z_n)$ as prerequisite check.

3. **Degenerate posteriors (exploding variance).** If $p(z \mid x)$ has infinite or near-infinite variance (heavy-tailed likelihoods, unidentified parameters), the predicted-observation map is not Lipschitz in $z$ and $L_g$ is unbounded. The TV-to-observation-bias step fails. **Scope.** ε-A2' requires the observation model $p(o \mid z, a)$ to be Lipschitz with bounded $L_g$. This is automatic for Gaussian-emission models, fails for Cauchy-emission or non-integrable-likelihood models.

4. **Non-exponential-family *and* non-amortized *and* uncontrolled *and* multimodal.** The worst case where every safeguard fails. Many state-of-the-art deep generative models (diffusion posteriors at test time, energy-based models with uncontrolled MCMC) sit in this regime. **Scope.** These agents remain strictly sub-scope β. No amount of KL-bound machinery rescues them.

5. **Variational-posterior support mismatch.** If $q_\phi$ has support not contained in $p$'s support, $\mathrm{KL}(q_\phi \Vert p) = +\infty$ identically, and the bound is vacuous. **Scope.** ε-A2' requires $\operatorname{supp}(q_\phi) \subseteq \operatorname{supp}(p)$. This is usually satisfied by construction in exp-family VI; it can fail for adversarial variational families (WAE, etc.) where the support is chosen by the agent.

The scope of ε-A2' is therefore: **VI agents with controllable-and-monitored KL, Lipschitz observation models, and supports nested in the true posterior**. This is a large and important class — modern ML agents, Bayesian neural networks under BBVI with monitoring, active-inference agents with exp-family generative models, VAEs with well-trained encoders on in-distribution data — but not universal.

## 9. Landing map

### 9.1 Recommended: sub-scope α' as explicit ε-indexed extension of α

**Proposal.** Extend the A2' sub-scope partition in `#deriv-sector-condition` and `#der-gain-sector-bridge` from **{α, β}** to **{α, α', β}**:

- **α** — B1 structural, A2' derived (unchanged): Bayesian/Kalman, exponential-family natural parameters, gradient on strongly convex loss, L2-regularized convex, linear PD $KH$.
- **α' (new)** — ε-B1 with quantified degradation, ε-A2' derived with $\sqrt\varepsilon$-scaling floor: variational inference under §8 scope constraints (controllable-KL, Lipschitz observation, nested support). Sector constant $\alpha_\varepsilon = \eta^\ast c_{\min}(1 - O(\sqrt\varepsilon))$ (Regime A) with additive floor $2\delta_0 = O(\sqrt\varepsilon)$ in the ultimate bound.
- **β** — A2' assumed per-agent (scope-narrowed): PID, rule-based, human-judgment, severely misspecified, non-convex-beyond-basin, per-step SGD, *non-amortized-and-uncontrolled VI*, *multimodal-strongly-coupled mean-field VI*, *non-Lipschitz observation models*.

This is a scope-narrowing of β (moving the well-controlled-VI subset out of β into α') plus a new tiering.

### 9.2 Mechanical edits

**New appendix segment: `#deriv-variational-sector-condition`** (proposed slug). Type `derivation`, status `exact` for §§2–3, `robust-qualitative` for §§4–6 application cases.

Content (summarizing this spike):

1. Setup (§1 of the spike).
2. Pinsker propagation and ε-B1 derivation (§2).
3. Sector-persistence template instantiation under ε-B1 (§3), including both Model D and Model S ultimate-bound formulas.
4. Workhorse cases: mean-field (§4), natural-gradient (§5), amortized (§6).
5. Active-inference positioning (§7), cross-referencing `spikes/spike-active-inference-vs-aad.md`.
6. Scope statement (§8 failure modes) — what ε-A2' does *not* cover.
7. Derivation-audit table per O-BP14 convention.

**Touches to existing segments.**

- **`#deriv-sector-condition`**:
  - Extend the sub-scope paragraph from α/β to α/α'/β; add a sentence pointing to `#deriv-variational-sector-condition` for the ε-derivation.
  - Update the O-BP14 derivation-table row for A2' to reflect the three-way split.
- **`#der-gain-sector-bridge`**:
  - Add α' to the "Verified Instances" table with: *Update class = Variational (controlled-KL, Lipschitz obs); Bridge status = ε-Derived; Sector parameter $\alpha = \eta^\ast c_{\min}(1-O(\sqrt\varepsilon))$; Valid region = $\mathcal B_R \setminus \mathcal B_{2\delta_0}$*.
  - Update failure-mode FM-5 ("Variational / approximate posteriors — B1 not guaranteed by optimality") with cross-reference to `#deriv-variational-sector-condition` — the failure is now structured, not unstructured.
- **`#result-sector-persistence-template`**:
  - Add a row to the instantiations table for "variational-inference agent" with effective disturbance $\rho_\xi + \alpha_\varepsilon \cdot 2\delta_0$ (additive floor as effective disturbance) and region $\mathcal B_R \setminus \mathcal B_{2\delta_0}$.
  - Add brief Epistemic Status note: "The sub-scope α' variational case inherits the template with an additive floor; see `#deriv-variational-sector-condition`."
- **`#form-strategy-complexity-cost`** (the G-BP2 V-medium segment, slug `strategy-complexity-cost`):
  - Working Notes addition: the $\pi^\ast$-first reverse-KL form has a natural persistence interpretation — under KL-bound $\varepsilon$ on $Q_{\Sigma_t}$ against $\pi^\ast$, the strategy-induced regret is $O(\sqrt\varepsilon)$ and enters the agent's effective disturbance via `#deriv-variational-sector-condition`. This connects the strategy-cost KL direction (forced by §6.1 of `#deriv-strategy-cost-regret-bound`) to the strategic-mismatch ultimate bound.
- **`#spike-active-inference-vs-aad.md` §I action 5** (V-strong G-BP2 deferral): this spike *does not* force the V-strong move; it supplies the conditional AAD→AI persistence guarantee while leaving V-strong adoption deferred per the spike's guidance.

### 9.3 Stage impact

- `#deriv-variational-sector-condition`: new segment, stage `draft`.
- `#deriv-sector-condition`: was `draft`, remains `draft` (substantive sub-scope extension).
- `#der-gain-sector-bridge`: was `draft`, remains `draft` (new table row + failure-mode update).
- `#result-sector-persistence-template`: was `draft`, remains `draft` (new instantiation row).
- `#form-strategy-complexity-cost`: was `draft`, remains `draft` (Working Notes addition).

### 9.4 Cross-cutting connections

- **`#additive-coordinate-forcing`** (2026-04-23 meta-segment): variational persistence sits outside the meta-pattern — no logarithmic coordinate is *forced*; the Pinsker $\sqrt\varepsilon$ is a bound, not a coordinate transform. Classify as *outside* the meta-pattern's three-layer structure. This is informative: it shows the meta-pattern's scope boundary (the pattern is about coordinate-forcing via Cauchy-FE, not about approximation-quantification via Pinsker).
- **`#disc-identifiability-floor`**: ε-A2' is a *positive* result, the opposite structural pattern from identifiability-floor's external-no-go results. No direct floor-instance.
- **`#disc-separability-pattern`**: ε-A2' introduces a new *ladder* position — between "separable core" (sub-scope α, clean derivation) and "general open" (sub-scope β, per-agent verification), ε-A2' is the *structured-repair* row for the VI agent class. This strengthens `#disc-separability-pattern`'s three-part characterization by populating the structured-repair half of the contraction ladder.

## 10. Epistemic assessment

**What is proved (exact, §§2–3).** Given $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$, Lipschitz $L_g$, bounded $V_o$, and B1 for the true-posterior correction: ε-B1 holds with $\sqrt\varepsilon$-scaling degradation, and the sector-persistence template applies on $\mathcal B_R \setminus \mathcal B_{2\delta_0}$ with ultimate-bound degradation $O(\sqrt\varepsilon)$. This is standard Pinsker + Cauchy-Schwarz + stopping-time localization — the mathematics is textbook; the contribution is the application to AAD's A2' sub-scope.

**What is robust-qualitative (§§4–6).** The workhorse cases — mean-field, natural-gradient, amortized — inherit the §§2–3 machinery under their respective assumptions. The mean-field honest scope boundary (approximately-factorized posteriors), natural-gradient's recovery to full α for exp-family, and the amortized-VI additive-KL composition are all standard variational-inference observations promoted into AAD's scope language.

**What is discussion-grade (§7).** Active-inference positioning. The conditional AAD A2' for active-inference agents under exp-family + natural-gradient is proved; the broader positioning ("AAD supplies the persistence guarantee AI's FEP-flow underdelivers") is a strategic observation, not a theorem.

**What is open (§8).** Uncontrolled-$\varepsilon$ agents (scale of modern practice: unclear), degenerate-posterior agents (rare but important edge cases), and the measure of how much of "modern ML agents" actually satisfies the §8 scope — this is an empirical question the spike does not answer.

**Max attainable.** *Exact* for the core §§2–3 derivation. *Robust-qualitative* for §§4–6. The spike does not promise to move variational-inference agents into sub-scope α (the true-posterior case); it promises sub-scope α' — a third tier with quantified $\sqrt\varepsilon$-degradation — which is strictly stronger than β (assumed) and strictly weaker than α (derived without approximation).

**Honesty about the Pinsker rate.** The $\sqrt\varepsilon$ rate is *tight* in general (Pinsker is tight for two-point distributions; the linear-functional lift achieves the bound under extreme observation configurations). The rate can be *improved to $\varepsilon$* in special cases (tight log-Sobolev inequalities, transportation-cost inequalities under $T_2$-Talagrand; Bobkov & Götze 1999). The spike does not chase these — they are domain-specific and the $\sqrt\varepsilon$ bound suffices for the sub-scope α' characterization.

**What this spike does NOT do.** It does not resolve the V-strong G-BP2 active-inference-master-framework question. It does not replace the β sub-scope — it *narrows* β by moving the controlled-VI case out. It does not extend to per-step stochastic-gradient VI (BBVI with one sample per step) without additional machinery (per-step SGD enters via effective disturbance in Prop A.1S, same as it does for classical SGD). It does not handle non-KL divergence approximations (Rényi-VI, $\chi^2$-VI, $\alpha$-divergence VI — each would need its own information-theoretic inequality).

**Why this is worth landing.** The biggest gap in A2' coverage was a large and growing agent class (modern ML) sitting in β as "assumed per-agent." The ε-A2' derivation moves the *controlled* subset into a derived tier with explicit $\sqrt\varepsilon$ bounds — this is strictly more informative than β for any agent that monitors its own approximation error. For the uncontrolled subset, the spike *also* sharpens β by naming exactly what goes wrong (uncontrolled $\varepsilon$, mode-missing, non-Lipschitz, unnested support), converting "variational approximations are outside scope" into four named failure modes each with a structural remediation path.

## 11. References

- Amari, S. (1998). Natural gradient works efficiently in learning. *Neural Computation* 10(2):251–276.
- Bobkov, S. & Götze, F. (1999). Exponential integrability and transportation cost related to logarithmic Sobolev inequalities. *J. Funct. Anal.* 163:1–28.
- Blei, D. M., Kucukelbir, A. & McAuliffe, J. D. (2017). Variational inference: A review for statisticians. *JASA* 112(518):859–877.
- Burda, Y., Grosse, R. & Salakhutdinov, R. (2015). Importance weighted autoencoders. arXiv:1509.00519.
- Cover, T. & Thomas, J. (2006). *Elements of Information Theory* (2nd ed.). Wiley. §2.5 (multi-information).
- Cremer, C., Li, X. & Duvenaud, D. (2018). Inference suboptimality in variational autoencoders. *ICML*.
- Csiszár, I. (1967). Information-type measures of difference of probability distributions and indirect observations. *Studia Sci. Math. Hungar.* 2:299–318. (Pinsker-type inequalities.)
- Da Costa, L., Parr, T., Sajid, N., Veselic, S., Neacsu, V. & Friston, K. (2020). Active inference on discrete state-spaces. *J. Math. Psych.* 99:102447.
- Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P. & Pezzulo, G. (2017). Active inference: a process theory. *Neural Computation* 29(1):1–49.
- Friston, K., Da Costa, L., Hafner, D., Hesp, C. & Parr, T. (2021). Sophisticated inference. *Neural Computation* 33(3):713–763.
- Hoffman, M., Blei, D., Wang, C. & Paisley, J. (2013). Stochastic variational inference. *JMLR* 14:1303–1347.
- Khan, M. E. & Lin, W. (2017). Conjugate-computation variational inference: Converting variational inference in non-conjugate models to inferences in conjugate models. *AISTATS*.
- Khan, M. E. & Nielsen, D. (2018). Fast yet simple natural-gradient descent for variational inference in complex models. *arXiv:1807.04489*.
- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Ch. 4, 9.
- Khasminskii, R. (2012). *Stochastic Stability of Differential Equations* (2nd ed.). Springer. Ch. 5 (stopping-time localization).
- Kingma, D. & Welling, M. (2013). Auto-encoding variational Bayes. arXiv:1312.6114.
- Raskutti, G. & Mukherjee, S. (2015). The information geometry of mirror descent. *IEEE Trans. Inf. Theory* 61(3):1451–1457.
- Rezende, D. J., Mohamed, S. & Wierstra, D. (2014). Stochastic backpropagation and approximate inference in deep generative models. *ICML*.
- Tsybakov, A. B. (2009). *Introduction to Nonparametric Estimation*. Springer. Lemma 2.5 (Pinsker).
- Wainwright, M. & Jordan, M. (2008). Graphical models, exponential families, and variational inference. *Found. Trends Mach. Learn.* 1(1–2):1–305. §§2.3, 3.4, 5 (mean-field VI).
- Aguilera, M., Millidge, B., Tschantz, A. & Buckley, C. L. (2022). How particular is the physics of the free energy principle? *Phys. Life Rev.* 40:24–50. (FEP-flow narrow-validity cite.)
- AAD segments cited: `#deriv-sector-condition`, `#der-gain-sector-bridge`, `#result-sector-persistence-template`, `#form-strategy-complexity-cost`, `#deriv-strategy-cost-regret-bound`, `#additive-coordinate-forcing`, `#disc-identifiability-floor`, `#disc-separability-pattern`, `#result-structural-adaptation-necessity`.
