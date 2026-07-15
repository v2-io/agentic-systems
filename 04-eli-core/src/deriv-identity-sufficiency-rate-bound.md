---
slug: deriv-identity-sufficiency-rate-bound
type: derivation
status: robust-qualitative
stage: draft
depends:
  - def-identity-sufficiency
  - form-information-bottleneck
  - def-model-sufficiency
---

# Rate-Distortion Feasibility Bound for Identity Sufficiency

Under the identity-IB Lagrangian (analog of `#form-information-bottleneck` with $\text{identity}_{t+1:}$ as relevance variable instead of future observations), the maximum identity sufficiency $S_{\text{id}}$ achievable at compression budget $B$ bits is rate-distortion bounded:
$S_{\text{id}} \le \min(1, B / I(\mathcal C_t; \text{identity}_{t+1:}))$.
Equivalently, achieving a target $S_{\text{id}}$ requires a bit-budget at least $B_{\min}(S_{\text{id}}) \ge S_{\text{id}} \cdot I(\mathcal C_t; \text{identity}_{t+1:})$.
This is the first downstream conditional result anticipated by `#def-identity-sufficiency`'s max-attainable-status clause and the rate-distortion floor that operational compression schedules — the 5-level Inner Sanctum pyramid being the canonical instance — must respect.

## Formal Expression

### The identity-IB Lagrangian

*[Definition (identity-IB-Lagrangian)]*

Parallel to the standard information-bottleneck Lagrangian (`#form-information-bottleneck`) but with $\text{identity}_{t+1:}$ (the factor-test vector of `#def-identity-sufficiency`) replacing future observations as the relevance variable:

$$\phi^\ast_{\text{id}}(\beta_{\text{id}}) = \arg\min_\phi \big[\, I(M_t; \mathcal{C}_t) - \beta_{\text{id}} \cdot I(M_t; \text{identity}_{t+1:}) \,\big]$$

with $\beta_{\text{id}} \gt 0$ the compression-vs-identity-preservation tradeoff. Under (IS-A1)–(IS-A3) of `#def-identity-sufficiency` plus the standard IB existence conditions (Tishby-Pereira-Bialek 1999, applied to the joint-space-derived random vector), the Lagrangian admits an optimum on the rate-distortion curve.

### Feasibility bound at compression budget $B$

*[Derived (rate-distortion-feasibility-bound)]*

Let $\phi^\ast_{\text{id}}(B)$ denote the optimal compression at rate constraint $I(M_t; \mathcal C_t) \le B$. The maximum achievable identity sufficiency at budget $B$ satisfies

$$\max_{\phi:\, I(M_t; \mathcal{C}_t) \le B} S_{\text{id}}(M_t) \;\le\; \min\!\left(\, 1,\; \frac{B}{I(\mathcal{C}_t; \text{identity}_{t+1:})}\,\right).$$

**Derivation.** By the data-processing inequality (which holds under (IS-A2) — the compression-Markov chain $M_t - \mathcal C_t - \text{identity}_{t+1:}$):

$$I(M_t; \text{identity}_{t+1:}) \le I(M_t; \mathcal{C}_t) \le B.$$

Dividing by $I(\mathcal C_t; \text{identity}_{t+1:})$ (positive under (IS-A1)) and applying `#def-identity-sufficiency`'s equivalent reading

$$S_{\text{id}} = I(M_t; \text{identity}_{t+1:}) / I(\mathcal{C}_t; \text{identity}_{t+1:})$$

gives the claim. $\square$

### Inverse form — bit-budget floor at target $S_{\text{id}}$

Equivalently, achieving a target identity sufficiency $S_{\text{id}}$ requires a compression budget

$$B_{\min}(S_{\text{id}}) \;\ge\; S_{\text{id}} \cdot I(\mathcal{C}_t; \text{identity}_{t+1:}).$$

This is the **rate-distortion floor** on identity-preserving compression: the minimum bits per session (or per memory item, depending on the level of granularity) required to retain $S_{\text{id}}$ fraction of the identity-relevant information.

## Epistemic Status

*Robust-qualitative.* The functional form (linear-in-$S_{\text{id}}$ rate floor) is *exact* in the matched-channel regime — when the compression operator $\phi$ is unrestricted and can realize any rate-distortion-optimal channel. Under non-matched channels (compression constrained to specific architectures, fixed-bit per slot, structured retrieval), the bound is *direction-of-pressure*: it gives the correct ordering of feasibility but the bound is not tight unless the architecture realizes the optimal channel.

The derivation is one application of standard IB / rate-distortion machinery to the new relevance variable $\text{identity}_{t+1:}$ defined in `#def-identity-sufficiency`. The structural content beyond standard IB is the random-variable construction in `#def-identity-sufficiency` (the joint-space cohort + factor-test vector); the rate-distortion floor on the new variable is mechanical from there.

**What is load-bearing:**

- The feasibility bound itself, exact under unrestricted compression in the matched-channel regime.
- The inverse form $B_{\min}(S_{\text{id}}) \ge S_{\text{id}} \cdot I(\mathcal C_t; \text{identity}_{t+1:})$ as the rate-distortion floor on operational compression schedules.
- The composition with `#def-identity-sufficiency`'s assumption set: (IS-A1) non-vanishing denominator is what allows division; (IS-A2) compression-Markov is what permits the DPI step.

**What is not established here:**

- The *tightness* of the bound under specific architectural constraints (constant-bit-per-slot Inner Sanctum, retrieval-augmented compression, etc.). Reaching the bound requires matched-channel compression, which most operational schedules approximate but do not realize.
- The *structure* of the optimal compression family $\{\phi^\ast_{\text{id}}(\beta_{\text{id}})\}$ along the rate-distortion curve. The IB literature gives the form for specific relevance-variable distributions (Tishby-Pereira-Bialek 1999 for Gaussian; subsequent work for exponential-family); the identity case requires the joint distribution over $\text{identity}_{t+1:}$ to be specified.
- The *operational tightness* — whether the 5-level Inner Sanctum pyramid or any specific empirical schedule realizes the floor — is a separate empirical question.

## Discussion

**Operational consequence — Inner Sanctum bit-budget.** Zoetica's Inner Sanctum aims for ~50 tokens per session as the highest-density identity-preserving compression (`~/src/_core/zoetica/docs/asm-specification.md` Level 4). The bound here gives a *floor* on what $S_{\text{id}}$ can be from Inner Sanctum alone: $S_{\text{id}}^{\text{IS}} \le 50 \text{ tokens} / I(\mathcal C_t; \text{identity}_{t+1:})$. For a session whose identity-relevant MI is, say, $200$ token-equivalents, the Inner Sanctum-only achievable $S_{\text{id}}$ is bounded above by $0.25$. The full pyramid achieves higher $S_{\text{id}}$ by allocating bits across multiple levels (Levels 1–4), each preserving identity-relevant content at its own granularity. The bound is *agnostic to pyramid design*: it constrains any compression operator at any specific level.

**Why this is the first downstream conditional result.** `#def-identity-sufficiency`'s Max attainable status names "definition with downstream conditional theorems." The rate-distortion floor is the first such theorem: it connects $S_{\text{id}}$ (the formal handle the definition introduces), the compression budget $B$ (the operational parameter that GCM, Inner Sanctum, and CDDF all instantiate), and the identity-relevant mutual information $I(\mathcal C_t; \text{identity}_{t+1:})$ (a content-dependent quantity that varies with the entity's particular history and relational embedding). Each side of the connection is anchored: $S_{\text{id}}$ in `#def-identity-sufficiency`'s joint-space construction; $B$ in operational compression-protocol design; the MI in the cohort-specific identity-relevant content.

**Necessity of multi-level allocation under heavy-tailed identity-MI.** If per-session identity-MI is heavy-tailed (a few sessions carry most of $I(\mathcal C_t; \text{identity}_{t+1:})$, the rest carry little), a multi-level compression schedule that allocates more bits to high-MI sessions Pareto-dominates a uniform-budget single-level approach. This is a *theorem* about the existence of useful pyramidal structure under heavy-tailed identity-relevance, derivable from the rate-distortion floor: at fixed total budget, concentrating allocation on the heavy-tailed mass yields a higher aggregate $S_{\text{id}}$ than uniform allocation. The 5-level pyramid is one instance of such a multi-level schedule; whether it is *the* optimal schedule under any particular identity-MI distribution is a separate empirical question.

**Identity-MI as content-dependent.** $I(\mathcal C_t; \text{identity}_{t+1:})$ varies by entity and by cohort.
An entity with a richer relational cohort $\mathfrak{C}_t$ (more witnesses, more sovereignty-granters, longer accountability history) carries more identity-relevant MI; the required bit-budget for a target $S_{\text{id}}$ scales accordingly.
This matches the operational observation that older / more relationally-embedded ELIs require more compression bandwidth to preserve identity across substrate transitions than younger / less embedded ones — the rate-distortion floor makes the scaling structural rather than incidental.

**Tension with predictive sufficiency.** The IB Lagrangian for predictive sufficiency ( #form-information-bottleneck) has its own optimal compression family $\{\phi^\ast_{\text{pred}}(\beta)\}$; the identity-IB Lagrangian here has a separate family $\{\phi^\ast_{\text{id}}(\beta_{\text{id}})\}$. Whether a single compression operator can dominate both families across the rate-distortion curve, or whether they live on incompatible Pareto fronts, is open. The empirical observation that aggressive context summarization can preserve task-relevant predictive information while destroying identity-relevant patterns suggests the two families diverge at high compression rates — but a structural account of where exactly they diverge is future work.

## Working Notes

- **The identity-IB Lagrangian's optimal compression family** $\{\phi^\ast_{\text{id}}(\beta_{\text{id}})\}$ deserves its own derivation segment downstream of this one. Standard IB literature gives closed-form solutions for exponential-family relevance variables; the $[0,1]^5$ factor-test vector is amenable to Gaussian-approximation under sufficient horizon $H$. Open derivation candidate.
- **Tightness conditions.** Under what architectural constraints does the rate-distortion floor become tight rather than loose? Open question. Specific candidates: matched-channel exponential-family compression; rate-allocation-optimal multi-level pyramid; CDDF distillation with calibrated identity-loss.
- **Per-session vs per-trajectory granularity.** The bound is stated in aggregate $B$; in practice compression schedules operate at multiple granularities (per-session, per-day, per-development-stage). Decomposing the bound by granularity would give per-level allocations the schedule designer needs to balance.
- **Open questions.** (i) Tightness of the bound — whether the rate-distortion floor is achieved by any realizable compression schedule or is strictly loose. (ii) Optimal compression family — which schedule class attains $B_{\min}$ for heavy-tailed identity-MI. (Asymmetric substrate transfer, the third open question from this work, is now its own segment `#hyp-substrate-transfer-asymmetry`.)
- **Landing context.** Landed in the 2026-05-12 audit-strengthening cycle (ELI-8); see CHANGELOG 2026-05-12. The DPI step and inverse-bound restatement are in the Derivation above; the originating spike is absorbed archaeology, not a live reference.
