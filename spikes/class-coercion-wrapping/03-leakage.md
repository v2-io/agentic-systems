# Sub-Spike C: Leakage Characterization

**Status**: derivation. Hierarchy of three wrapping regimes; structural-vs-behavioral leakage bound; honest scope on what cannot currently be bounded.
**Date**: 2026-05-09
**Depends on**: `01-theorem-statement.md` (especially condition C3 and the approximate Theorem 2). Informed by `06-empirical-instances.md` finding that PROPRIUM/shoshin is *partial-wrapping*, not strict wrapping.

---

## 1. The condition restated and its failure modes

**(C3) No implicit goal-inference.** $A$'s response to a goal-blind query $q_M$ does not depend on $G_W$ via inference from query patterns:

$$P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$$

The empirical-instances survey (`06-empirical-instances.md`) reveals that the brief's strict wrapping move — issuing structurally separate goal-blind queries — is rare in practice. Most "agentic LLM" frameworks (PROPRIUM/shoshin included) issue one goal-conditioned call per macro-step and parse its response into typed update slots. This produces a *different* construction with different leakage characteristics. The leakage analysis must distinguish these regimes.

## 2. The wrapping-regime hierarchy

Three regimes, in order of decreasing structural commitment to directed separation:

### 2.1 Regime W₁ — Strict wrapping (the brief's construction)

The wrapper issues *separate* goal-blind queries $q_M$ for $f_M$ and goal-conditioned queries $q_G$ for $f_G$. The goal-blind query's input does not contain $G_W$.

Empirical instances: rare. Generative Agents (Park et al. 2023) approximates this with a structurally goal-blind observation→memory step. PROPRIUM's auxilia hierarchy *could* implement this if auxilia handled $f_M$ updates with cheap-substrate goal-blind calls — but the documented architecture does not require this and shoshin does not implement it.

### 2.2 Regime W₂ — Partial wrapping / output-structuring (the dominant pattern)

The wrapper issues *one* goal-conditioned query carrying the full $(M_W, G_W)$ context, and parses the response into separate $M_W$-update fields and $G_W$-update fields. Structural separation lives at the *write boundary* (typed update fields) but not at the *query boundary* (one goal-conditioned input).

Empirical instances: PROPRIUM/shoshin (per `06-empirical-instances.md`), ReAct, Reflexion, BabyAGI, AutoGPT, MemGPT, most LangChain/LangGraph patterns.

### 2.3 Regime W₀ — No wrapping (raw component use)

The wrapper does not even structurally separate updates at the write boundary. The component's response is consumed directly into a flat state. This is the Class-3 baseline.

## 3. Leakage in each regime

### 3.1 Regime W₁ leakage — structural

In strict wrapping, $G_W$ does not enter $q_M$ as an input. The only path by which the response $A(q_M)$ can depend on $G_W$ is through *implicit inference* — $A$ recognizing query patterns that statistically correlate with goal-content in its pretraining distribution.

**Bound (W₁).** The KL leakage in Regime W₁ is bounded above by the statistical correlation between query content and goal-content in $A$'s pretraining distribution:

$$\kappa_\text{W₁} = \mathbb{E}_{q_M}\big[\, D_\text{KL}\big(P(A(q_M) \mid q_M, G_W)\, \big\Vert\, P(A(q_M) \mid q_M)\big)\, \big]$$

This is bounded above by the conditional mutual information $I(A(q_M); G_W \mid q_M)$ in the joint pretraining + deployment distribution. For LLMs:

$$\kappa_\text{W₁} \le I(A(q_M); G_W \mid q_M)$$

with equality when the worst-case $G_W$ distribution is realized.

The bound is *informative*: it's a quantity about the component's pretraining, separate from the wrapper's design. Two components with the same query interface but different pretraining distributions will have different $\kappa_\text{W₁}$. This makes leakage a *measurable property of the component*.

For component classes with low pretraining-induced goal-content (purely syntactic systems, calculators, untrained-on-goals models): $\kappa_\text{W₁} \approx 0$. For LLMs trained on goal-rich data (instruction-following, RLHF): $\kappa_\text{W₁}$ is potentially substantial but in principle measurable via mutual-information estimators.

The wrapper can further reduce $\kappa_\text{W₁}$ by restricting query content — querying only on observation-grounded sensorimotor extracts rather than higher-level descriptions reduces $I(q_M; G_W)$ which upper-bounds $I(A(q_M); G_W \mid q_M)$.

### 3.2 Regime W₂ leakage — behavioral

In partial wrapping / output-structuring, $G_W$ enters the query as input. The component sees the full goal-conditioning context and is *asked* (via prompting structure) to produce separated outputs. Leakage now depends on whether the component *honors* the requested separation in its outputs — a behavioral property, not a structural one.

**Bound (W₂).** The KL leakage in Regime W₂ has no structural upper bound. It is bounded only by the component's *compliance fidelity* — how well it honors the prompted instruction to produce goal-blind belief-update content despite having $G_W$ in input.

$$\kappa_\text{W₂} \le \kappa_\text{compliance}(A, q_M\text{-prompt})$$

where $\kappa_\text{compliance}$ is an empirical property of the component-prompt pair, not a derivable theoretical bound.

For well-instructed LLMs, $\kappa_\text{compliance}$ may be small in practice. For adversarial inputs or LLMs that don't follow the instruction reliably, $\kappa_\text{compliance}$ can approach maximum leakage.

**This is the central honest finding for partial wrapping.** Without a structural commitment to goal-blindness at the query boundary, the leakage is bounded only by behavioral / training-time properties of the component, not by the wrapper's design. **Partial wrapping does not derive directed-separation by structure; it relies on the component's compliance.**

### 3.3 Regime W₀ leakage — full Class-3

No wrapping, no separation. $\kappa_\text{W₀}$ is at the component's maximum goal-conditioning sensitivity — there's no constraint on how much the component's output depends on $G_W$. This is the Class-3 baseline.

## 4. The structural-vs-behavioral distinction

§3 surfaces a distinction worth naming explicitly:

- **Structural separation** (W₁): leakage is bounded by *what cannot be inferred* from a query that doesn't contain $G_W$. Bound is a statistical property of the component, derivable in principle from pretraining-distribution analysis.
- **Behavioral separation** (W₂): leakage is bounded by *what the component chooses to do* with $G_W$ when it has it. Bound is a behavioral property, derivable only empirically.

The two are different in kind, not just in degree. Structural separation gives a directed-separation guarantee that the wrapper can prove from its construction. Behavioral separation gives a directed-separation *expectation* that depends on the component's training and prompt-following fidelity.

This distinction matters for the directed-separation classification in `#der-directed-separation`. The class taxonomy should arguably distinguish:

- **Class 1 by structure** (W₁ or natively goal-blind) — exact directed separation by construction.
- **Class 1 by behavior** (W₂ with reliable component) — expected directed separation, no structural guarantee.
- **Class 2** — partial, mixed.
- **Class 3** (W₀ or non-admissible) — directed separation fails.

## 5. The Park / agentic-tft cognitive-loop-spec construction

The empirical survey (`06-empirical-instances.md` §1.4) flagged that the agentic-tft cognitive-loop-spec separates CONTEXTUALIZE (belief-side update) from CHOOSE (strategy-side update) in time, with prediction and surprise computed against the current $M_W$ *before* $G_W$ enters consideration. If implemented faithfully, this is closer to W₁ than W₂.

Specifically: if the CONTEXTUALIZE phase makes a goal-blind query (e.g., "what is the surprise of this observation given my current world model?") and the CHOOSE phase makes a goal-conditioned query (e.g., "given this world-model update and my current goals, what should I do?"), then the construction *is* strict wrapping — at the cost of two LLM calls per cycle instead of one.

The cognitive-loop-spec is the natural integration target for the strict wrapping move — it specifies the structure already; the leakage analysis here would clarify the bound that follows.

## 6. Bounds in usable terms

Three quantities matter for empirical measurement:

**$\kappa_\text{W₁}$** — leakage in strict wrapping. Bounded by $I(A(q_M); G_W \mid q_M)$. For a fixed component, this is a function of the wrapper's choice of $q_M$ — narrower queries (less context) reduce the bound; richer queries increase it. Measurable in principle by:

1. Constructing a goal-blind query template.
2. Sampling multiple $G_W$ values consistent with the wrapper's history.
3. Running the component on the same query under each $G_W$ and measuring the divergence between response distributions.

This is operationally feasible for any component with stochastic outputs. For deterministic components, the divergence is either 0 or 1 (response either depends on $G_W$ or doesn't); intermediate values require ensemble or temperature.

**$\kappa_\text{W₂}$** — leakage in partial wrapping. Has no structural bound. Empirically measurable but not predictable from theory. Equivalent to "how well does the LLM follow the structural-separation instruction in its prompt."

**$\Delta\kappa = \kappa_\text{W₂} - \kappa_\text{W₁}$** — the leakage gap from foregoing strict wrapping. This is the operational cost of partial wrapping in directed-separation terms. Could be small for well-instructed LLMs, large for adversarial settings.

The honest theoretical result: $\kappa_\text{W₁}$ is bounded; $\kappa_\text{W₂}$ is not. Whether $\Delta\kappa$ is small or large in practice is empirical and depends on the component.

## 7. Sources of leakage in pretrained components (W₁ contributions)

Even in strict wrapping, pretrained components can carry implicit goal-correlations. Identifiable sources:

(a) **Statistical co-occurrence of observation-content and goal-content in pretraining data.** If pretraining data systematically pairs certain observation-types with certain goals, the component will infer goals from observations even without explicit prompting. Hard to characterize without auditing the pretraining distribution.

(b) **RLHF / instruction-following training that biases responses toward "useful" content.** Models trained to be helpful infer "what's wanted here?" from query content and bias responses accordingly. This is goal-inference even when the goal isn't in the input.

(c) **In-context retrieval / few-shot examples.** If the wrapper includes few-shot examples in $q_M$, the example content can leak goal-information if examples were selected goal-conditionally.

(d) **System prompt contamination.** Many LLM deployments include a system prompt that may carry goal-content (e.g., "you are a helpful assistant for [goal-domain]"). This contaminates "goal-blind" queries unless the system prompt is itself goal-blind.

For minimum-leakage strict wrapping: use a base / un-RLHF'd LLM, no system prompt, no few-shot examples, queries restricted to observation-content. This is structurally cleanest but operationally constrained.

## 8. Connection to Theorem 2

`01-theorem-statement.md` Theorem 2 stated the approximate-form bound

$$D_\text{KL}\big(P(M_{W,m+1} \mid \ldots, G_{W,m})\, \big\Vert\, P(M_{W,m+1} \mid \ldots)\big) \le \kappa$$

via the data-processing inequality. With this sub-spike's analysis:

- Theorem 2 with $\kappa = \kappa_\text{W₁}$: structural directed-separation bound for strict wrapping.
- Theorem 2 with $\kappa = \kappa_\text{W₂}$: behavioral directed-separation bound for partial wrapping. The bound exists but is not derivable from structure.
- Regime W₀: Theorem 2 doesn't apply — there's no goal-blind query or goal-blind update channel to bound.

The "almost-Class-1 with leakage rate $\kappa$" framing of Theorem 2 covers W₁ and W₂; their distinction is *what determines $\kappa$* — structure for W₁, behavior for W₂.

## 9. Honest scope

**What this sub-spike does:**
- Distinguishes structural vs. behavioral directed-separation regimes.
- Provides the bound $\kappa_\text{W₁} \le I(A(q_M); G_W \mid q_M)$ for strict wrapping.
- Names the operational consequence: partial wrapping has no structural leakage bound; it relies on the component's behavioral compliance.
- Identifies measurable quantities: $\kappa_\text{W₁}$, $\kappa_\text{W₂}$, $\Delta\kappa$.

**What this sub-spike does *not* do:**
- Compute $\kappa_\text{W₁}$ for any specific component. The mutual-information estimation is empirical work; this sub-spike provides the bound, not the measurement.
- Provide a structural bound for $\kappa_\text{W₂}$ (none exists; this is the honest finding).
- Address adversarial settings where the component is actively trying to leak goal-information.
- Address temporal accumulation of leakage across many macro-steps.

The W₁ / W₂ distinction is the central content. It explains why the strict wrapping move has theoretical value (structural bound) even when practical instances overwhelmingly use partial wrapping (no structural bound). For Parts III/IV, this means: PROPRIUM-as-implemented is W₂, with leakage rate that depends on the underlying LLM's compliance fidelity. PROPRIUM *could* move to W₁ via the auxilia hierarchy (per `06-empirical-instances.md` §1.3 item 5), at the cost of more LLM calls per cycle. The strengthening would gain a structural directed-separation bound that PROPRIUM-as-implemented lacks.

## 10. Open questions

- Is the $\kappa_\text{W₁}$ bound tight? §6's measurement procedure gives an empirical handle, but the theoretical worst-case (over $G_W$ distributions) may be loose for the actual deployment distribution. Worth investigating.
- Can $\kappa_\text{W₂}$ be bounded under additional assumptions on the component (e.g., "the component honestly attempts to follow structural-separation instructions")? Possibly, with a behavioral-compliance axiom — but this would be a hypothesis rather than a derived bound.
- Does compositional wrapping (wrapping a wrapped component) compose the leakage rates additively, multiplicatively, or in some other way? Unclear; relevant if the wrapping construction is iterated (e.g., a meta-wrapper around a wrapper around a component).
- Does the W₁/W₂ distinction affect the persistence template's bounds? Through Theorem 1's (A4)-inheritance: probably yes, with $\rho_W$ bounded above by component-noise + leakage-induced effective disturbance. Worth working out in sub-spike G.

---

## File index

- This file: `03-leakage.md`
- Brief: `00-brief.md`
- Theorem statement (depended on): `01-theorem-statement.md`
- Admissibility: `02-admissibility.md`
- Empirical instances (cited): `06-empirical-instances.md`
- ε* semantics (next): `04-epsilon-semantics.md`
