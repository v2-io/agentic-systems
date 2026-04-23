---
spike: kl-to-state-distance-template-extraction-2026-04-24
date: 2026-04-24
status: architectural — template extraction proposal with recommendation; client survey complete; two primary clients + one adjacent family member; narrow-template (Option B) recommended over unified-template (Option A) and no-extraction (Option C)
trigger: Two independent strengthening-first spikes on 2026-04-24 (`spike-bias-bound-constant-C-strengthening-2026-04-24.md` M4; `spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md` parallel-machinery observation) identified Pinsker / Otto-Villani / Bakry-Émery / Lipschitz-posterior machinery in use at multiple points in AAD. The observation: AAD is quietly carrying a shared "KL-to-state-distance" apparatus whose role parallels how `#sector-persistence-template` factors out Lyapunov sector-bound machinery across six AAD results. The extraction question is architectural, not mathematical.
posture: Strengthen-first. Investigate what the right abstraction actually is before defaulting to "yes extract" or "no keep independent." Check the too-narrow move, the adjacent-family move, and the (PI)/Čencov path. Do not rank by effort.
relates_to:
  - variational-sector-condition
  - sector-persistence-template
  - additive-coordinate-forcing
  - agent-identity
  - discussion-identifiability-floor
  - discussion-separability-pattern
  - contraction-template
  - gain-sector-bridge
  - fisher-whitened-update-rule
  - strategy-cost-regret-bound
  - msc/spike-bias-bound-constant-C-strengthening-2026-04-24.md
  - msc/spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md
  - msc/naming-brainstorm-2026-04-24.md
---

# Spike: KL-to-State-Distance Template Extraction

## Headline (up front)

**Is the shared machinery real, and should it be factored out as a template?**

**The shared machinery is real but narrower than M4's briefing suggests. Recommendation: Option B (narrow template on the Otto-Villani / Lipschitz-posterior track only), with `#variational-sector-condition` positioned as an adjacent family member sharing Pinsker's inequality but not the template's full shape.** The unified-template move (Option A) collapses two structurally different outputs (scalar sector-constant degradation vs. vector state-displacement) under one abstraction that trades compression for honest differentiation — it saves one citation chain but hides the structural distinction the reader needs. The no-extraction move (Option C) leaves a load-bearing shared-theorem apparatus un-named while AAD acquires a second primary instance in the Bias-Bound-Derivation spike. Option B captures the genuine shared machinery (Pinsker→Otto-Villani→Lipschitz-posterior cascade in W₂ on state space) with explicit T1/T2/T3 precondition tiering and accommodates `#bias-bound-derivation` as the first primary client and future KL→posterior-displacement clients as future primary clients, while leaving Pinsker+Cauchy-Schwarz→scalar-sector-degradation (`#variational-sector-condition`) to its own segment.

**Summary of the comparison.** Both client segments perform KL-to-something conversion using Pinsker as the base inequality, and both have an $O(\sqrt\varepsilon)$ baseline with $O(\varepsilon)$ refinement under LSI/T2. But the template-worthy apparatus is the *cascade* that converts a KL bound on one distribution into a W₂ bound on a pushforward distribution via an explicit Lipschitz-posterior step, giving a state-space displacement bound. `#variational-sector-condition` does not have the pushforward step — it propagates a TV bound through a correction function via Cauchy-Schwarz to degrade a scalar constant, not to bound a state displacement. The Pinsker inequality itself is shared; the cascade after Pinsker is not.

**Candidate name after the communal-imagination test: `#posterior-displacement-template`** (or, if the stronger geometric framing is preferred, `#transport-posterior-template`). The former is flatter and describes the output quantity that downstream segments cite; the latter surfaces the machinery. Both pass the six-months-later test better than `#kl-to-state-distance-template` (too long, too descriptive, no handle) or `#concentration-template` (wrong cross-reference — "concentration" in ML means tail bounds, not state-displacement bounds).

---

## §1. The question explicitly

Two independent 2026-04-24 spikes observed what looks like the same apparatus used at two points in AAD:

**Client A — `#variational-sector-condition`.** Input: a KL bound $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$ on the variational approximation. Machinery: Pinsker's inequality gives $\lVert q_\phi - p\rVert_{TV} \leq \sqrt{\varepsilon/2}$, then Cauchy-Schwarz propagates this TV bound through a correction function $K\hat P$ to bound the *scalar sector constant degradation*:

$$c_\varepsilon(\lVert\delta\rVert) = c_{\min} - C_H\sqrt{2\varepsilon}/\lVert\delta\rVert$$

Output: a state-dependent sector constant that is weakened uniformly on a radius-$2\delta_0$ ball around target ($\delta_0 = O(\sqrt\varepsilon)$), with Regime-A/B decomposition for the sector-persistence template. The "state distance" here is the radius $\delta_0$ at which the sector bound fails to hold, not a bound on distance between two distributions.

**Client B — Proposed `#bias-bound-derivation`.** Input: a conditional mutual information bound $I(G; \Omega_\tau \vert e_\tau, M_{\tau^-})$ interpretable as an expected KL divergence from goal-conditional posterior to goal-marginalized posterior. Machinery: (i) chain-rule identity $\mathbb E_G[\mathrm{KL}(P_{\Omega\vert e,M,G}\Vert P_{\Omega\vert e,M})] = I$, (ii) Pinsker → TV bound on the observation distribution, (iii) Otto-Villani under LSI → W₂ bound on the observation distribution, (iv) Lipschitz-posterior stability (Stuart 2010) → W₂ bound on the posterior distribution over $M$:

$$\mathbb E[W_2^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})] \leq \frac{2 L_{\text{post}}^2}{\rho_{\text{LSI}}} \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \vert e_\tau, M_{\tau^-})$$

Output: a W₂ bound on the pushforward posterior distribution over $M$, which translates to a bound on the displacement of the coupled vs. decoupled post-update state *as a distribution on $M$*.

**The observation.** Both segments: (a) start from a KL-style information-theoretic bound; (b) use Pinsker as the base inequality; (c) sharpen from $\sqrt\varepsilon$ to $\varepsilon$ when log-Sobolev / Talagrand T2 is available; (d) apply the result within an AAD-internal machinery (sector-condition for A; Class-2 bias for B). The spike's M4 note read: *"the same machinery — a KL-to-state-distance template analogous to how `#sector-persistence-template` was extracted from multiple sector-persistence-flavored results."*

**The specific question.** Is this one template instantiated twice, or two different machineries sharing their first step? And: are there other implicit clients in AAD that the template would absorb?

---

## §2. Template extraction in template form — explicit comparison

The precision question is: *can one template-statement capture both clients, with parameterization choosing between them, and does that template do useful work?* Write each client explicitly in template form and check.

### §2.1 Client A in template form

| Template slot | Client A filling |
|---|---|
| **Input** | KL bound $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$ |
| **Output type** | Scalar: sector constant $c_\varepsilon(\lVert\delta\rVert)$ |
| **Intermediate step 1** | Pinsker → $\lVert q_\phi - p\rVert_{TV} \leq \sqrt{\varepsilon/2}$ |
| **Intermediate step 2** | Cauchy-Schwarz: $(K\hat P - P^\ast)^T (\hat P - P^\ast) \geq (c_{\min} - C_H\sqrt{2\varepsilon}/\lVert\delta\rVert) \lVert\delta\rVert^2$ |
| **Lipschitz / regularity assumption** | Observation-model Lipschitz constant $C_H$; nested-support on variational family |
| **Output interpretation** | State-dependent sector constant; feeds into `#sector-persistence-template` Regime-A/B |
| **Tightening path (T1→T2)** | Otto-Villani / T2-Talagrand: improves scalar from $O(\sqrt\varepsilon)$ to $O(\varepsilon)$ degradation |

### §2.2 Client B in template form

| Template slot | Client B filling |
|---|---|
| **Input** | Conditional mutual information $I(G; \Omega \vert e, M)$ = expected KL divergence |
| **Output type** | Distance in measure space: $W_2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})$ on distributions over $\mathcal M$ |
| **Intermediate step 1** | Pinsker → TV bound on $P_{\Omega\vert e,M,G}$ vs $P_{\Omega\vert e,M}$ |
| **Intermediate step 2** | Otto-Villani under LSI → $W_2^2(P_{\Omega\vert e,M,G}, P_{\Omega\vert e,M}) \leq (2/\rho_{\text{LSI}})\cdot\mathrm{KL}$ |
| **Intermediate step 3** | Lipschitz-posterior stability (Stuart 2010): $W_2(P_{M\vert e,G}, P_{M\vert e}) \leq L_{\text{post}} \cdot W_2(P_{\Omega\vert e,G}, P_{\Omega\vert e})$ |
| **Lipschitz / regularity assumption** | (i) LSI constant $\rho_{\text{LSI}}$ on observation distribution; (ii) Lipschitz-posterior stability constant $L_{\text{post}}$ |
| **Output interpretation** | W₂ bound on state-space pushforward; explicit constant $C^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ |
| **Tightening path (T1→T2)** | Already at $O(\varepsilon)$ under LSI; Bakry-Émery gives LSI constant explicitly under Ricci-positive curvature |

### §2.3 The structural difference

Both clients use Pinsker as Step 1. But **Steps 2–3 differ fundamentally**:

- Client A's Step 2 is *Cauchy-Schwarz applied to a correction function* — it converts a TV bound on a distribution into a degradation of a scalar inner-product constant by estimating how far the correction direction can rotate. The output is a scalar modifier on the sector-condition constant.

- Client B's Steps 2–3 are *Otto-Villani then Lipschitz-posterior* — a cascade that converts a KL bound on one distribution into a W₂ bound on a pushforward distribution. The output is a distance (in Wasserstein-2) between two probability distributions on state space.

The outputs occupy different objects. Client A's output is a real number (the sector constant's value at norm $\lVert\delta\rVert$); Client B's output is a distance between measures. Client A's intermediate machinery is *regularity propagation through a correction-operator inner product*; Client B's intermediate machinery is *coupling-based transport distance propagation through a Bayesian inverse problem*.

**The honest read.** Pinsker is shared. Everything after Pinsker is different. The apparatus described in Client B — Pinsker → Otto-Villani-under-LSI → Lipschitz-posterior → W₂ on state-pushforward — is a coherent three-step cascade with load-bearing joint structure (the Otto-Villani step and the Lipschitz-posterior step fit together to produce a W₂-bound on state-space distributions; neither step alone would). Client A has only the first step (Pinsker) in common with that cascade.

**Implication for template extraction.** If we abstract around "any segment that uses Pinsker's inequality to propagate a KL bound," the template becomes *Pinsker itself* — a textbook result (Tsybakov 2009 §2.4; Cover-Thomas 2006 §11.6) that does not need an AAD-internal meta-segment. If we abstract around "the specific cascade Pinsker → Otto-Villani → Lipschitz-posterior → W₂ on posterior pushforward," the template is substantive and has Client B as its primary current instance — but Client A is an adjacent family member, not an instance.

---

## §3. Complete client survey

Beyond the two flagged clients, where else in `01-aad-core/src/` does similar machinery appear?

### §3.1 Actual Pinsker-using segments (grep-identified)

Eleven segments match against `Pinsker|KL.*TV|TV.*KL|log-Sobolev|Talagrand|Otto-Villani|Bakry|Wasserstein|W_2|Fisher-Rao|Čencov`. Sorted by role:

| Segment | Machinery | Template fit? |
|---|---|---|
| `#variational-sector-condition` | Pinsker + Cauchy-Schwarz → scalar sector-constant degradation | **Adjacent family member** (§2.3) |
| `#strategy-cost-regret-bound` | Pinsker + bounded value range → **regret** bound, not state-distance | No — different output (regret, not state-distance) |
| `#strategy-complexity-cost` | Same as above, cited from `#strategy-cost-regret-bound` | No — same reason |
| `#compression-operations` | Cites the Pinsker → regret bound in Discussion | No — same reason |
| `#ciy-unified-objective` | Cites the Pinsker → regret bound in Discussion | No — same reason |
| `#exploit-explore-deliberate` | Cites the Pinsker → regret bound in Discussion | No — same reason |
| `#detection-latency` | "Pinsker-type linearization" on linearized Bernoulli likelihood for mismatch-signal magnitude | No — different shape (residual-magnitude on sufficient-statistic accumulation, not KL→displacement) |
| `#fisher-whitened-update-rule` | (PI)+Čencov → Fisher metric; no KL→state-distance | No — uses (PI)/Čencov at the metric layer, not the transport layer |
| `#gain-sector-bridge` | Fisher-metric cases under (PI)+Čencov | No — same as above |
| `#contraction-template` | (CT2) Jacobian-level conditions, Fisher-metric lift under (PI)+Čencov | No — same as above |
| `#additive-coordinate-forcing` | Meta-segment naming the (PI)+Čencov family | No — meta-pattern on the metric/coordinate layer |
| *Proposed* `#bias-bound-derivation` | Pinsker → Otto-Villani under LSI → Lipschitz-posterior → W₂ on state pushforward | **Primary instance** (§2.2) |

### §3.2 The regret-bound cluster is a separate template-worthy group

The five regret-bound-citing segments (`#strategy-cost-regret-bound`, `#strategy-complexity-cost`, `#compression-operations`, `#ciy-unified-objective`, `#exploit-explore-deliberate`) share the machinery *Pinsker → regret bound under bounded value range*, which has a different output space (regret, not state-distance) and a different intermediate step (bounded value range giving the inner product $\mathbb E_Q[V(a^\ast) - V(a)]$ a $V_{\max}$-Lipschitz bound). This machinery *is* a shared apparatus — but it is already named in `#strategy-cost-regret-bound`, which is positioned as a derivation segment whose result is cited by the other four. The cross-citation structure already does the work that a template-extraction would do for this cluster. No further factoring is indicated.

The Pinsker-machinery in the regret cluster is structurally *different* from the KL→state-distance machinery in Clients A and B: the regret cluster uses Pinsker to bound a *functional* ($R = \mathbb E_Q[V(\pi^\ast) - V(\pi)]$) which is bilinear in the distribution; the KL→state-distance cascade uses Pinsker to bound a *distance* in the measure space. Different linear-functional vs. metric-space outputs.

### §3.3 No implicit clients

No segment in the survey uses an informal "small KL implies small state-distance" claim without naming the specific inequality. The Fisher-Rao / (PI) track is structurally separate: those segments use Čencov's theorem to force the *metric*, not Pinsker's inequality to bound a state-distance.

**Implication.** The template-extraction decision is about Client B (primary) and Client A (adjacent). There is no third or fourth implicit client to pull in.

### §3.4 Forward-looking potential clients

Three places where KL→state-distance machinery *could plausibly* appear in future AAD work:

1. **Composition-scope-condition robustness.** If `#scope-composite-agent` ever needs a "small-KL-between-sub-agent-models implies small-composite-displacement" argument (e.g., under Class-3 partially-separated agents where the composite state-update is a pushforward of sub-agent updates), Otto-Villani+Lipschitz-posterior would be the right machinery.

2. **Causal-IB extension (open per `#discussion-identifiability-floor`).** If causal-IB lands as a future appendix, it likely needs KL→W₂ bounds on the post-intervention distribution as a function of intervention-information budget.

3. **Misspecification cost (open per `#discussion-identifiability-floor`).** The expected floor is "degradation rate from misspecification is bounded below by an information-theoretic quantity" — a Pinsker-to-state-distance cascade applies naturally.

**Implication.** Future-client density matters for template cost-benefit. A template that serves Client B + three future clients is more worth extracting than a template that serves only Client B. The three future clients are all KL→state-distance-on-pushforward-distribution (Client B's pattern), *not* Client A's Pinsker+Cauchy-Schwarz→scalar pattern. This argues for Option B (narrow template on Client B's cascade) over Option A (unified template accommodating both).

---

## §4. Three candidate abstractions

### §4.1 Option A — Unified template subsuming both Clients A and B

**Thesis.** Write a single template segment parameterized by output norm choice. The template states: *from a KL bound on an input distribution and precondition tier T1/T2/T3, derive a state-distance bound on an output quantity, with bound scaling $O(\sqrt\varepsilon)$ or $O(\varepsilon)$ depending on tier.*

**Abstraction.** Input: KL bound $\varepsilon$. Output norm: parameterized ($TV$ / $W_2$ / Fisher-Rao / scalar sector-degradation). Tier T1: Pinsker baseline, $O(\sqrt\varepsilon)$. Tier T2: Otto-Villani under LSI, $O(\varepsilon)$. Tier T3: Otto-Villani + Lipschitz-posterior, $O(\varepsilon)$ with explicit constant.

**Client instantiation table under Option A:**

| Client | Output norm | Tier | Rate | Post-Pinsker machinery |
|---|---|---|---|---|
| `#variational-sector-condition` (Client A) | Scalar sector-degradation | T1 | $O(\sqrt\varepsilon)$ | Cauchy-Schwarz |
| *proposed* `#bias-bound-derivation` (Client B) | $W_2$ on state pushforward | T3 | $O(\varepsilon)$ | Otto-Villani + Lipschitz-posterior |

**Honest problems with Option A.**

1. *The output spaces are structurally different.* Client A's output is a scalar that modifies a pre-existing sector bound. Client B's output is a metric-space distance that bounds a new quantity. The template can only unify them by declaring "output quantity is a scalar" at the wrong abstraction level, which discards the structural distinction the reader needs.

2. *The post-Pinsker machinery doesn't fit a single parameterization.* Cauchy-Schwarz (Client A) and Otto-Villani+Lipschitz-posterior (Client B) are not members of a common parametric family. "Parameterize by post-Pinsker step" collapses to "write both independently and call it a template," which fails the template test (a template should do work beyond restating each instance).

3. *Comparison with `#sector-persistence-template`.* That template's six instances share a *common Lyapunov argument* with the same quadratic $V(\xi) = \tfrac12\lVert\xi\rVert^2$, verified (T1)–(T3) across all instances. The client-specific content is *what counts as the state variable, the correction function, and the effective disturbance*. The common derivation is genuinely shared — the template's *body* is the same across instances. Option A's proposed "body" is not shared: Client A's Cauchy-Schwarz bookkeeping and Client B's Otto-Villani/Stuart cascade are different derivations. A template whose body doesn't match across instances is a table of contents, not a theorem.

4. *The naming problem.* No natural name for Option A accurately describes both clients. `#kl-to-state-distance-template` is literal but misleading (Client A's "state distance" is a scalar). `#concentration-template` is wrong (concentration-of-measure is about tail bounds). `#transport-inequality-template` is misleading for Client A (Cauchy-Schwarz isn't a transport inequality). Each naming candidate privileges one client over the other.

**Verdict on Option A.** The unification is superficial. Pinsker is shared; the rest isn't. Extracting Option A would save one literature-citation chain (Pinsker, Cover-Thomas §11.6) across two segments while introducing a template whose body doesn't match across instances.

### §4.2 Option B — Narrow template on Client B's cascade (recommended)

**Thesis.** Write a template segment that abstracts *only* the Pinsker → Otto-Villani → Lipschitz-posterior → W₂ cascade, with Client B (proposed `#bias-bound-derivation`) as its first primary instance and the three forward-looking clients (§3.4) as candidate future instances. Position `#variational-sector-condition` as an adjacent family member in the same spirit as Lyapunov and IB Lagrangian are adjacent to the three Cauchy-FE instances in `#additive-coordinate-forcing`.

**Abstraction.**

- **Input.** A KL divergence bound $\varepsilon = \mathrm{KL}(P \Vert Q)$ between two distributions $P, Q$ on a *base space* $\Omega$ (typically observation space).
- **Precondition tier T1 (baseline).** Unconditional Pinsker: $\lVert P - Q\rVert_{TV} \leq \sqrt{\varepsilon/2}$. Output rate $O(\sqrt\varepsilon)$ on TV.
- **Precondition tier T2 (transport-inequality).** Log-Sobolev inequality on $Q$ with constant $\rho_{\text{LSI}}$: $W_2^2(P, Q) \leq (2/\rho_{\text{LSI}})\varepsilon$. Output rate $O(\varepsilon)$ on $W_2$.
- **Precondition tier T3 (posterior-Lipschitz closure).** Lipschitz-posterior stability (Stuart 2010) with constant $L_{\text{post}}$: $W_2(f_\ast P, f_\ast Q) \leq L_{\text{post}} \cdot W_2(P, Q)$ where $f$ is a Bayesian-posterior pushforward. Output rate $O(\varepsilon)$ on $W_2$ on state-space pushforward.
- **Output.** $\mathbb E[W_2^2(f_\ast P, f_\ast Q)] \leq (2L_{\text{post}}^2/\rho_{\text{LSI}}) \cdot \varepsilon$.

**Client instantiation table under Option B:**

| Client | Status | $P$ | $Q$ | $f$ | Tier | Output |
|---|---|---|---|---|---|---|
| *proposed* `#bias-bound-derivation` | Primary instance | $P_{\Omega\vert e,M,G}$ | $P_{\Omega\vert e,M}$ | Bayesian posterior on $M$ | T3 | $W_2$ on $M$-posterior |
| *forward* causal-IB | Candidate future | Interventional distr. | Observational distr. | Post-intervention pushforward | T3 | W₂ on post-intervention state |
| *forward* misspecification-cost | Candidate future | True model likelihood | Assumed model likelihood | Bayesian posterior on $M$ | T3 | W₂ on $M$-posterior |
| *forward* composition-scope-robustness | Candidate future | Sub-agent model $M_i$ | Nominal sub-agent model | Composite-state pushforward | T3 | W₂ on composite state |

**Four primary/candidate instances suffice to justify the template** — the same density as `#sector-persistence-template` (six instances) and `#contraction-template` (five verified instances + three theorem-imported), both of which are promoted templates in AAD.

**Client A (`#variational-sector-condition`) as adjacent family member.** In the same way that Lyapunov quadratic and IB Lagrangian are documented in `#additive-coordinate-forcing` as *adjacent family members* — sharing the pattern's shape without its forcing structure — `#variational-sector-condition` shares the template's *first step* (Pinsker on a KL bound from a variational approximation) but not its cascade (no Otto-Villani, no Lipschitz-posterior, no W₂ on pushforward; instead Cauchy-Schwarz on the correction inner product). The adjacency is explicit: both use KL divergence as input; both recover $O(\varepsilon)$ under LSI; both serve sector-condition-adjacent purposes. But the template's *body* (Otto-Villani+Lipschitz-posterior cascade) does not transfer to the variational-sector segment; adapting it would require reformulating the variational mismatch $\delta$ as a pushforward distribution, which is not the segment's native construction. The honest positioning: document the adjacency in both segments' Discussion sections; keep both segments' derivations independent.

**Honest problems with Option B.**

1. *Only one primary instance currently exists.* The template would land with one primary client (the proposed `#bias-bound-derivation`) and three candidate future instances. `#sector-persistence-template`'s promotion was justified by six existing instances; a one-instance template is harder to justify. *Response:* `#contraction-template` was similarly promoted with five verified + three theorem-imported instances at landing, not all fully-worked AAD segments. The density test should be "does the template predict structure in future work?" — three forward-looking candidates (§3.4) plus Client B gives four, comparable to existing meta-templates. But honest: Option B depends on the forward-looking instances actually materializing; if causal-IB, misspecification-cost, and composition-scope-robustness all fall away, the template serves one client.

2. *Three of five `#sector-persistence-template` instances are Lyapunov-quadratic; Client B's Otto-Villani cascade is genuinely distinct machinery.* This is a structural strength: if the template predicts a *new* machinery pattern that future clients will instantiate, that's what templates are for.

3. *Option B requires `#bias-bound-derivation` to land first.* Until that segment is in the codebase, the template has zero committed primary instances. *Response:* this is a promotion-ordering concern, not a template-validity concern. Land `#bias-bound-derivation` first, then the template as a second move that factors out its cascade for reuse.

**Verdict on Option B.** Substantive, honest, and aligns with AAD's existing template-extraction pattern (one shared derivation body across multiple instances, explicit T1/T2/T3 preconditions, client-specific instantiation table, adjacent family members documented).

### §4.3 Option C — No extraction; keep segments independent

**Thesis.** The shared content is one inequality (Pinsker) and an optional tightening (LSI→Otto-Villani). Both are textbook. Each client segment cites the inequality directly (Tsybakov 2009; Cover-Thomas 2006; Otto-Villani 2000; Bakry-Émery 1985). No template extraction is warranted.

**Honest problems with Option C.**

1. *Misses the genuine three-step cascade in Client B.* The cascade *Pinsker → Otto-Villani → Lipschitz-posterior → W₂ on pushforward* is not a textbook fact — it is a composition of three separate textbook results that together produce an AAD-relevant state-space bound. If it appears in four places (Client B plus three forward-looking clients) with the same structure, that's a template, and the alternative is three-way citation-chain repetition.

2. *Hides the constant-C discovery from the bias-bound spike.* The bias-bound spike's key result — under (H1)–(H3), $C^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ with explicit geometric interpretation ($L_{\text{post}}$ = prior-likelihood tension, $\rho_{\text{LSI}}$ = observation concentration) — is useful *general-purpose* content that future derivations will want to cite. Factoring it into a template makes it citable; leaving it inline in `#bias-bound-derivation` makes each future client re-derive the cascade.

3. *Prevents naming a structural pattern that is visibly repeating.* If three forward-looking clients materialize, the segment-author for each will independently re-derive the three-step cascade; a template makes the pattern visible and the re-derivations unnecessary.

**Option C response.** These problems are real *if* the forward-looking clients materialize. If they don't (causal-IB, misspecification-cost, composition-scope-robustness all fall away or use different machinery), Option C wins. The decision reduces to: *how confident are we that KL→state-distance-on-pushforward will recur in AAD work?*

**Verdict on Option C.** Honest fallback if Option B's forward-looking clients turn out to not need the cascade. Defensible near-term (one instance doesn't justify a template); weaker mid-term if the forward-looking clients land.

---

## §5. Evaluation matrix

| Dimension | Option A (unified) | Option B (narrow) | Option C (no extraction) |
|---|---|---|---|
| **Mathematical correctness** | Correct but abstraction is superficial (§4.1 pt 3) | Correct; cascade is a composition of three textbook theorems | Trivially correct (inline derivation per client) |
| **Structural honesty** | **Weak.** Declares unified template where body doesn't match | **Strong.** Template body shared across primary + forward-looking instances; `#variational-sector-condition` explicitly adjacent | **Strong.** No overclaim |
| **Value to future segment work** | Low. Future clients instantiating Client B's cascade don't benefit from Client A's Cauchy-Schwarz machinery being in the template | **High.** Each future client gets the (H1)–(H3) preconditions + cascade as a drop-in | Low. Each future client re-derives |
| **Alignment with `#sector-persistence-template` precedent** | Weak. The Lyapunov template has a *single shared derivation body*; Option A's body is two unrelated derivations | **Strong.** Option B matches the extracted-shared-body pattern | Neutral (no template extracted) |
| **Alignment with `#additive-coordinate-forcing` precedent** | Weak. That meta-segment distinguishes primary instances (Cauchy-FE / Čencov) from adjacent family members; Option A blurs this | **Strong.** Option B preserves the primary-instance vs adjacent distinction | Neutral |
| **Promotion cost** | Medium (new segment + cross-references in 2 clients) | Medium (new segment + cross-references in 1 primary + 1 adjacent) | None |
| **Reversibility** | Medium (if template is underused, can be downgraded to lemma) | Medium (same) | High (can always extract later if pattern becomes obvious) |
| **Commits to forward-looking clients** | Yes | Yes | No |

**Aggregate read.** Option B dominates Option A on structural honesty, value to future work, and alignment with existing template precedent. Option B beats Option C *if* the forward-looking clients materialize (three candidates, §3.4); Option C is defensible-near-term *if* they don't. Option C is the honest fallback; Option B is the honest lead.

---

## §6. Recommendation with explicit tradeoffs

**Recommended: Option B — narrow template on the Otto-Villani + Lipschitz-posterior cascade with Client B as primary instance.**

**Conditions under which Option B is the right move:**

1. `#bias-bound-derivation` lands as a segment (currently proposed in `msc/spike-bias-bound-constant-C-strengthening-2026-04-24.md` M1). The template cannot land before its primary instance.
2. At least one of the three forward-looking clients (§3.4) appears credible as work AAD will actually pursue. If all three are permanently shelved, Option C is honest.
3. `#variational-sector-condition` is explicitly re-positioned in its Discussion as *adjacent family member* to the new template, with Pinsker as the shared first step and Cauchy-Schwarz / scalar-sector-degradation / Regime-A/B as the adjacent-specific content. This positioning is mathematically accurate (both use Pinsker; Client A does not use the cascade) and parallels the adjacent-family-member treatment in `#additive-coordinate-forcing` for Lyapunov and IB Lagrangian.

**Conditions under which Option B is *not* the right move:**

- If the three forward-looking clients are unlikely to materialize. Then Client B alone does not justify a template; Option C is honest.
- If Client B's proposed segment `#bias-bound-derivation` is not going to land (e.g., if the Constant-C spike's Track 2 Fisher-Rao route is preferred over Track 1 transport-inequality route). Option B is specifically about Track 1 / the W₂-on-pushforward cascade; if AAD commits to Track 2 only, Option B has no client.

**Tradeoffs explicit.**

- *Option B over Option A.* Gain: honest differentiation of Client A (adjacent) from Client B (primary). Cost: two separate segments (the template + `#variational-sector-condition`'s adjacent treatment) where Option A would use one. Verdict: the differentiation is *load-bearing* for future readers — conflating a scalar-sector-degradation bound with a W₂-on-pushforward bound is exactly the kind of confusion AAD's scope-honesty posture is supposed to prevent.

- *Option B over Option C.* Gain: factored-out cascade that four future clients can instantiate without re-derivation; named structural pattern that makes the repeat-usage visible. Cost: commits to a template that depends on forward-looking-clients materializing. Verdict: acceptable if those clients are credible; re-evaluate in 6 months if not.

---

## §7. Candidate name — applying the communal-imagination test

The communal-imagination test (per `msc/naming-brainstorm-2026-04-24.md` Observation 3): *could a skilled reader, six months after first encounter, refer to this concept in a conversation without looking it up?* Names that pass in AAD: satisfaction gap, control regret, chronica, orient cascade, identifiability floor, directed separation. Names that fail: additive-coordinate-forcing, separability-pattern.

**Candidates:**

1. **`#kl-to-state-distance-template`** — Descriptive but long (five words, two hyphens). "KL" is a proper-noun-ish abbreviation that doesn't read smoothly in conversation. Fails the test: *"the KL-to-state-distance-template tells us that..."* is not how people talk. **Rejected.**

2. **`#information-displacement-template`** — Shorter, more evocative. "Information displacement" names the input-output shape (information bound in → displacement out). Passes the test: *"by information displacement, the bias bound is..."* reads naturally. Risk: "displacement" has specific meaning in active inference (generative-model displacement) that might confuse; "information" is over-used. **Possible.**

3. **`#concentration-template`** — Shortest. Connects to concentration-of-measure literature (Ledoux 2001). Risk: "concentration" in ML-adjacent literature means *tail bounds* (Hoeffding, Bernstein, Chernoff), not *distance bounds*. Using the name here would create a terminology collision. **Rejected.**

4. **`#transport-inequality-template`** — Names the underlying machinery (Otto-Villani, Talagrand T2). Risk: Pinsker is not a transport inequality (it is an information-theoretic inequality); the template includes Pinsker as T1. Misleading on scope. **Rejected.**

5. **`#posterior-displacement-template`** — Names the *output quantity* (displacement of the Bayesian posterior). Passes the test: *"by the posterior-displacement template, small-KL perturbations of observation produce small-W₂ perturbations of posterior..."* reads naturally. Accurate to Client B's cascade (Bayesian-posterior Lipschitz-stability is the load-bearing third step). Risk: "posterior" might be over-restrictive if a forward-looking client doesn't use Bayesian-posterior pushforward specifically (e.g., causal-IB post-intervention pushforward is not literally a Bayesian posterior). **Leading candidate.**

6. **`#transport-posterior-template`** — Combines the machinery (transport / W₂) with the output quantity (posterior displacement). Passes the test on the second read but feels compound. **Possible.**

**Recommendation.** `#posterior-displacement-template` as first choice — the output quantity is what downstream segments cite, the name reads naturally in conversation, and "posterior displacement" is a semi-standard phrase in Bayesian inverse problems (Stuart 2010 uses "posterior stability" for the Lipschitz constant; "displacement" flips the framing to the bound rather than the stability constant). If the forward-looking clients (causal-IB, misspecification-cost) use non-Bayesian pushforwards, re-evaluate — a more general name like `#transport-posterior-template` or `#information-displacement-template` would cover those cases.

---

## §8. Sketch of the template segment (if Option B is recommended and executed)

**Deliverable form (contingent on `#bias-bound-derivation` landing first).**

```yaml
---
slug: posterior-displacement-template
type: result
status: exact
depends:
  - agent-identity
  - additive-coordinate-forcing
  - bias-bound-derivation
stage: draft
---
```

### Skeleton — formal expression

**Template preconditions.**

Let $(P, Q)$ be two probability distributions on a base space $\Omega$ with $\mathrm{KL}(P \Vert Q) \leq \varepsilon$. Let $f: \Omega \to \mathcal P(\mathcal M)$ be a measurable map producing distributions on state space $\mathcal M$. The template applies when:

**(T1) KL-bound input.** $\mathrm{KL}(P \Vert Q) \leq \varepsilon$ is given (the segment's input; typically derived elsewhere).

**(T2-Pinsker) Baseline transport.** *Always available* (Pinsker's inequality; Tsybakov 2009 §2.4): $\lVert P - Q\rVert_{TV} \leq \sqrt{\varepsilon/2}$.

**(T2-LSI) Transport-inequality tier.** $Q$ satisfies a log-Sobolev inequality with constant $\rho_{\text{LSI}} > 0$ (sufficient: $Q$ strongly-log-concave with constant $K$, by Bakry-Émery 1985 curvature-dimension condition, giving $\rho_{\text{LSI}} \geq K$). Under (T2-LSI), Otto-Villani 2000 Theorem 1 gives $W_2^2(P, Q) \leq (2/\rho_{\text{LSI}}) \mathrm{KL}(P \Vert Q)$.

**(T3) Lipschitz-posterior stability.** The pushforward $f$ is $L_{\text{post}}$-Lipschitz in $W_2$: $W_2(f_\ast P, f_\ast Q) \leq L_{\text{post}} W_2(P, Q)$. Sufficient: $f$ is a Bayesian-posterior map on a well-posed inverse problem with bounded log-likelihood Hessian (Stuart 2010 Theorem 4.6; Hairer-Stuart-Vollmer 2014 for explicit W₂-bounds).

**Template result.**

Under (T1)+(T2-Pinsker): $\lVert f_\ast P - f_\ast Q\rVert_{TV} \leq L_{\text{TV}} \sqrt{\varepsilon/2}$ where $L_{\text{TV}}$ is a TV-Lipschitz constant of $f$ (weaker than W₂-Lipschitz).

Under (T1)+(T2-LSI)+(T3): $W_2^2(f_\ast P, f_\ast Q) \leq (2 L_{\text{post}}^2/\rho_{\text{LSI}}) \varepsilon$. The constant $C^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ is explicit and has geometric interpretation ($L_{\text{post}}$ = prior-likelihood tension; $\rho_{\text{LSI}}$ = observation-distribution concentration).

**Tier summary:**

| Tier | Preconditions | Output | Rate | Constants explicit? |
|---|---|---|---|---|
| T1 | (T1) alone | TV on base space | $O(\sqrt\varepsilon)$ | Universal (Pinsker) |
| T2 | (T1) + (T2-LSI) | W₂ on base space | $O(\varepsilon)$ | Yes, $2/\rho_{\text{LSI}}$ |
| T3 | (T1) + (T2-LSI) + (T3) | W₂ on pushforward | $O(\varepsilon)$ | Yes, $2L_{\text{post}}^2/\rho_{\text{LSI}}$ |

### Skeleton — client-instance table

| Client | $P$ | $Q$ | $f$ | Tier | Output | Locally-verified preconditions |
|---|---|---|---|---|---|---|
| `#bias-bound-derivation` | Goal-conditional obs distribution $P_{\Omega\vert e,M,G}$ | Goal-marginalized $P_{\Omega\vert e,M}$ | Bayesian posterior on $M$ | T3 | $\mathbb E[W_2^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})]$ | (T2-LSI) via Gaussian observation $\rho_{\text{LSI}}=1/\sigma^2$ or Bakry-Émery; (T3) via Stuart 2010 for well-posed inverse problem |
| *candidate* causal-IB | Interventional $P_\tau^{\text{do}}$ | Observational $P_\tau^{\text{obs}}$ | Post-intervention state pushforward | T3 | W₂ on post-intervention state | *Open* |
| *candidate* misspecification-cost | True $P_\theta^\ast$ | Assumed $P_{\hat\theta}$ | Bayesian posterior on $M$ | T3 | W₂ on $M$-posterior under misspecification | *Open* |
| *candidate* composition-scope-robustness | Sub-agent $M_i$ | Nominal sub-agent | Composite-state pushforward | T3 | W₂ on composite state | *Open*; requires composition-scope-condition geometry |

### Skeleton — adjacent family member

**`#variational-sector-condition`** shares (T1) and (T2-Pinsker) but does not use the (T3) posterior-Lipschitz pushforward. Its post-Pinsker machinery is Cauchy-Schwarz propagation through a correction inner product, producing a *scalar sector-constant degradation* rather than a state-space displacement. Documented as adjacent family member in both segments' Discussion.

### Skeleton — external lineage

The cascade's three steps are standard:
- Pinsker's inequality: Tsybakov 2009 §2.4; Cover-Thomas 2006 §11.6.
- Otto-Villani under log-Sobolev: Otto & Villani 2000, *J. Funct. Anal.* 173(2):361–400; Bakry-Émery 1985 for LSI under curvature-dimension.
- Lipschitz-posterior stability: Stuart 2010, *Acta Numerica* 19:451–559; Hairer-Stuart-Vollmer 2014 *SIAM J. Math. Anal.* 46(1):415–451.

AAD's contribution: (i) identifying the cascade as the load-bearing apparatus for KL→state-pushforward-displacement across multiple AAD segments; (ii) the geometric-stiffness interpretation of $2L_{\text{post}}^2/\rho_{\text{LSI}}$ tying prior-likelihood tension to observation concentration; (iii) the connection to `#agent-identity`'s (PI) axiom via the Fisher-Rao special case (cf. `#bias-bound-derivation`'s Track 2).

### Skeleton — Fisher-Rao adjacency

Under the (PI) parameterization-invariance axiom in `#agent-identity` (fourth primary instance of `#additive-coordinate-forcing`), the statistical-manifold sub-case of $\mathcal M$ carries a canonical Fisher-Rao metric. When the base space $\Omega$ and state space $\mathcal M$ are both statistical manifolds, the template's W₂ on pushforward admits a Fisher-Rao specialization: under small-information regime, $\mathbb E\lVert\Delta M\rVert_{FR} \leq \sqrt 2 \cdot \sqrt\varepsilon$ (dimension-free, universal constant). This is Track 2 of `#bias-bound-derivation`; it composes with the template's T3 output when LSI holds simultaneously in W₂ and in Fisher-Rao metric (equivalent for Gaussian observation models; divergent in general).

The Fisher-Rao track is *downstream* of the (PI)/Čencov fourth primary instance, not a new primary instance of `#additive-coordinate-forcing`. Consistent with `#additive-coordinate-forcing`'s principle: the (PI)-adoption is load-bearing; derived W₂ / Fisher-Rao bounds are the (PI) commitment's downstream consequences.

### Skeleton — connection to `#additive-coordinate-forcing`

The template sits *adjacent* to the meta-pattern but is not itself an instance:

- `#additive-coordinate-forcing` is at the *coordinate* layer — it forces what coordinate to use (log / Fisher-metric).
- `#posterior-displacement-template` is at the *bound-propagation* layer — given a KL bound in whatever coordinate the divergence layer selects, propagate it through a pushforward to a state-displacement bound.

The two meta-pieces compose: once the divergence layer selects reverse-KL (per `#edge-update-natural-parameter` / `#strategy-cost-regret-bound`), and the metric layer selects Fisher-Rao (per `#gain-sector-bridge` under (PI)), the template supplies the bound-propagation machinery that converts reverse-KL bounds on observations into W₂ / Fisher-Rao bounds on posteriors. Orthogonal-but-composing.

### Skeleton — Epistemic Status

*Exact.* The template abstracts three textbook inequalities; AAD's contribution is composition + AAD-relevant-client identification. Max attainable: *exact*. The result is as strong as Otto-Villani + Bayesian-posterior-stability theory, which is established.

**Load-bearing.** Pinsker (T1), Otto-Villani under LSI (T2), Lipschitz-posterior stability under well-posed inverse problem (T3) are each standard; the composition is the AAD-specific packaging.

**Not established.**
- Templates under *unbounded* KL: all three tiers assume $\varepsilon < \infty$. Unbounded KL regimes (e.g., support-mismatch) are scope-exits.
- Non-Lipschitz pushforward $f$: (T3) fails for ill-posed inverse problems (lack of Bayesian stability). Scope-exit for those.
- Non-concentrating observation distribution: (T2-LSI) fails for heavy-tailed observations. Scope-exit; T1 is the available fallback.

### Skeleton — Discussion

**Why factor this out.** Three forward-looking clients (causal-IB, misspecification-cost, composition-scope-robustness) and one primary client (`#bias-bound-derivation`) share the same cascade. Factoring it out makes the shared machinery visible, enables citing a single (T1)+(T2)+(T3) precondition bundle, and parallels `#sector-persistence-template`'s treatment of Lyapunov sector-bounds.

**What varies per-client.** (i) Which $P$, $Q$, $f$ apply; (ii) which LSI constant $\rho_{\text{LSI}}$ is available (Gaussian: $1/\sigma^2$; Bakry-Émery: curvature bound); (iii) which Lipschitz constant $L_{\text{post}}$ is available (well-posed inverse problem's stability constant, domain-specific).

**Adjacent vs. primary.** `#variational-sector-condition` uses Pinsker but not the cascade; it is adjacent. This preserves the primary-instance vs adjacent distinction that `#additive-coordinate-forcing` established.

**Regime-A/B decomposition is client-side, not template-side.** The template delivers an expected-value bound $\mathbb E[W_2^2(f_\ast P, f_\ast Q)] \leq C^2 \varepsilon$. Regime-A/B (clean-sector-bound / approximation-dominated-floor) is `#variational-sector-condition`'s specific way of using the bound in conjunction with `#sector-persistence-template` — it is a client-level composition, not a template-level feature. Future primary clients of `#posterior-displacement-template` will develop their own Regime decompositions as the segment's consumption pattern dictates.

---

## §9. Epistemic tier labels

| Claim | Tier | Notes |
|---|---|---|
| Pinsker's inequality T1 | **Exact** | Textbook (Tsybakov 2009) |
| Otto-Villani inequality T2 under LSI | **Exact** | Otto-Villani 2000 Thm 1; Bakry-Émery 1985 |
| Lipschitz-posterior stability T3 | **Conditional** on well-posed inverse problem | Stuart 2010 |
| Template cascade produces $C^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ under (T1)+(T2)+(T3) | **Derived (conditional)** | Direct composition |
| Client A (`#variational-sector-condition`) and Client B (proposed `#bias-bound-derivation`) share machinery | **Robust qualitative** | Pinsker shared; post-Pinsker machinery differs |
| The shared machinery is Pinsker *alone*, not the full cascade | **Derived** | §2.3 explicit comparison |
| Option A (unified template) is a weak abstraction | **Derived (from §4.1)** | Template body doesn't match across Client A and Client B |
| Option B (narrow template) aligns with `#sector-persistence-template` precedent | **Robust qualitative** | Shared-derivation-body pattern preserved |
| Option B has one primary + three forward-looking candidate instances | **Derived** | §3.4 enumeration |
| Option C honest fallback if forward-looking clients don't materialize | **Robust qualitative** | Depends on work not yet committed |
| `#posterior-displacement-template` passes the communal-imagination test | **Heuristic** | Naming judgment, not derivation |
| The template sits at bound-propagation layer, orthogonal to coordinate layer of `#additive-coordinate-forcing` | **Discussion-grade** | Structural positioning claim |

---

## §10. What the spike did not settle

- **Promotion ordering.** `#posterior-displacement-template` cannot land before `#bias-bound-derivation` (the template's one current primary instance). The ordering is: first `#bias-bound-derivation` (per `msc/spike-bias-bound-constant-C-strengthening-2026-04-24.md` M1), then the template extraction as a second move. If the reader wants the template-landing executed in a single session, the `#bias-bound-derivation` segment must be written first.

- **Whether the three forward-looking clients will materialize.** §3.4 names causal-IB, misspecification-cost, composition-scope-robustness as candidates. All three are listed as "Open" in CLAUDE.md §Open and `#discussion-identifiability-floor`'s open extensions. Committing to the template is a bet that at least one of these will be pursued; the bet is reasonable but not settled.

- **Whether `#variational-sector-condition` should reference the template or just cite Pinsker directly.** If Option B lands, the adjacent-family positioning goes in `#variational-sector-condition`'s Discussion (analogous to how Lyapunov is positioned adjacent in `#additive-coordinate-forcing`). If Option C prevails, `#variational-sector-condition` stays unchanged.

- **Non-Bayesian pushforwards.** The template's (T3) posterior-Lipschitz step is stated for Bayesian-posterior pushforwards via Stuart 2010. If a forward-looking client uses a non-Bayesian pushforward (e.g., causal-IB's post-intervention transformation, which is not literally a Bayesian conditioning step), (T3) needs generalization. The abstract Lipschitz-pushforward form holds for any $W_2$-Lipschitz map, so this is a minor rephrasing at the template level; the client-side would supply its specific Lipschitz constant.

- **TST connection.** If `02-tst-core/` segments use KL→state-distance cascades (e.g., model-update bounds from commit evidence), the template would serve as a cross-part bridge. Not surveyed in this spike; `02-tst-core/src/` not checked.

- **The Fisher-Rao track's positioning inside the template.** The (PI)/Čencov Fisher-Rao specialization (Track 2 of `#bias-bound-derivation`) could be a *fourth tier* T4 on top of T3, or a separate adjacent Fisher-Rao track within the template. The sketch (§8) treats it as adjacent; reasonable argument exists for treating it as T4. Defer to the template-authoring session.

- **Name choice finalization.** §7 recommends `#posterior-displacement-template` but flags that `#transport-posterior-template` or `#information-displacement-template` may be preferable if forward-looking clients use non-Bayesian pushforwards. Final name waits for Joseph's input.

---

## §11. One-paragraph summary for the caller

Two primary clients share Pinsker's inequality, but the *cascade after Pinsker* (Otto-Villani under LSI → Lipschitz-posterior → W₂ on state-space pushforward) is present only in the proposed `#bias-bound-derivation`; `#variational-sector-condition` uses Pinsker followed by Cauchy-Schwarz on a correction-operator inner product to produce a scalar sector-constant degradation, not a W₂ distance on a pushforward. The unified-template move (Option A) is structurally weak — it abstracts around output "state distance" but the two clients' outputs occupy different objects (scalar vs. metric-space distance), and the template's body (post-Pinsker derivation) does not transfer between them. The narrow-template move (Option B) — factoring the Pinsker → Otto-Villani → Lipschitz-posterior → W₂ cascade as a three-tier template with `#bias-bound-derivation` as primary client, three forward-looking candidate instances (causal-IB / misspecification-cost / composition-scope-robustness) pending, and `#variational-sector-condition` as an adjacent family member — is the architecturally honest move and aligns with AAD's existing template-extraction precedent (`#sector-persistence-template`, `#contraction-template`). The no-extraction move (Option C) is the honest fallback *if* the forward-looking clients do not materialize; it leaves one primary plus one adjacent client independently carrying the cascade. Recommendation: Option B, named `#posterior-displacement-template`, with execution contingent on `#bias-bound-derivation` landing first. The template sits at AAD's *bound-propagation* layer, orthogonal to `#additive-coordinate-forcing`'s *coordinate-selection* layer; together they compose into the full KL-coordinate-selection → KL-to-state-displacement pipeline that AAD increasingly needs. No segment files were modified; the deliverable is the recommendation plus the template sketch ready for a future segment-authoring session.
