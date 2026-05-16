# Reflection: §II opening batch (4 segments)

Covers `#def-agent-spectrum`, `#form-complete-agent-state`, `#der-directed-separation`, `#form-objective-functional`.

## Quick status table

| Slug | Stage | Status | Type |
|------|-------|--------|------|
| `def-agent-spectrum` | deps-verified | axiomatic | definition |
| `form-complete-agent-state` | claims-verified | robust-qualitative | formulation |
| `der-directed-separation` | draft | conditional | derived |
| `form-objective-functional` | deps-verified | axiomatic | formulation |

All depends upstream. **No "(Descended from TF-XX)" annotations in this batch** — pattern continues to be inconsistent (heavy in §I foundational definitions, lighter in §II structural commitments).

## Predictions vs evidence

I had predicted: $X_t = (M_t, G_t)$ split; directed separation as a scope condition; Class 1/2/3 architectural distinction. Got all of these, with **substantially more structure than I'd predicted on directed separation**:

- The $\kappa_{\text{processing}}$ operational definition with conditional-MI form.
- The composite-level class inheritance result (Class 1 sub-agents + partially-opposing objectives → Class 3 composite).
- The Pearl-blanket vs Friston-blanket positioning (Bruineberg et al. 2022 BBS) with explicit non-adoption of the Friston-blanket metaphysical reading.
- The Hafez 2026 Information Digital Twin (IDT) empirical reference (89% vs 44% perturbation detection).

The directed-separation segment is the most substantively important segment I've encountered in §II so far. It defines AAD's structural relationship to LLM-based agents (Class 2 explicit failure → coupled formulation in `03-llm-core/`).

## Cross-segment consistency

The (PI) axiom from `#scope-agent-identity` (segment 30) is invoked in `#der-gain-sector-bridge` (segment 25) but not in this batch — consistent.

`#form-complete-agent-state`'s "we conjecture that any directed-separation-preserving decomposition is structurally isomorphic to $(M_t, G_t)$" is honestly framed as an unproved conjecture. Good epistemic care — most frameworks would assert this implicitly.

The Hafez 2026 bridge in `#def-agent-spectrum` ("$P$ increases monotonically with $\mathcal{T}$") references `spikes/track-b-nonlinear-sims/variants/variant_hafez_results.md` — a spike-validation reference. Phase-2 verification candidate (does the spike actually validate the monotonic relationship, and what's the simulation setup?).

## Math verification

**$\kappa_{\text{processing}}$ definition:**
$$\kappa_{\text{processing}} = \frac{I(G_t \,;\, M_{\tau^+} \mid e_\tau,\, M_{\tau^-})}{H(G_t \mid e_\tau,\, M_{\tau^-})}$$

Well-formed. The conditioning on both $e_\tau$ and $M_{\tau^-}$ is essential to isolate "extra" goal information entering through shared pathways that bypass the event. Without conditioning on $M_{\tau^-}$, prior correlation between $G_t$ and $M_t$ would inflate the measure even for modular agents. Standard conditional-MI normalization by conditional entropy gives a $[0, 1]$ scale.

Boundary checks:
- Class 1 (modular): no $G_t$-to-$M_{\tau^+}$ pathway exists; $I(G_t; M_{\tau^+} | e_\tau, M_{\tau^-}) = 0$; $\kappa = 0$. ✓
- Class 2 (fully merged): $G_t$ is causally upstream of all processing; $\kappa$ approaches 1 (under a task distribution where $G_t$ carries information). ✓
- Class 3: intermediate. ✓

The "distribution dependence" caveat is honest: $\kappa$ measures actual flow, not the existence of pathways. A Class 3 agent's $\kappa$ varies with the task distribution.

**Empirical $\hat\kappa$ estimator:** present same event under different goal states, measure epistemic-content divergence. Sound behavioral probe; not closed-form computable in general but operationally usable.

## Substantive observations

**1. Architectural classification as discrete partition.** The framework explicitly replaces an earlier "$\kappa$-as-scalar" framing (referenced in `spikes/spike-kappa-topology-insight.md`) with a discrete classification + continuous diagnostic for Class 3. The discreteness is structurally important: "the architectural boundary between 'has a separable perception module' and 'processes everything through goal-conditioned attention' is discrete." This is the right move — within-class $\kappa$ is determined; only Class 3 has $\kappa$ as a meaningful tunable.

**2. Pearl-blanket vs Friston-blanket positioning.** The Bruineberg et al. 2022 BBS citation is well-targeted. Bruineberg et al. distinguish:
- *Pearl-blanket reading:* technical conditional-independence (well-defined, substantively informative).
- *Friston-blanket reading:* metaphysical demarcation of self-from-other (contested).

AAD adopts Pearl, explicitly non-adopts Friston. The architectural classification + Class 2 scope exit + $\kappa$ operationalization are the AAD-internal additions. This is sophisticated prior-art positioning — adopting what's defensible, declining what's contested, naming the boundary.

**3. The Hafez IDT empirical reference is a structural-validation candidate.** The Working Notes cite the Information Digital Twin from Hafez 2026 as detecting perturbations at 89% accuracy vs 44% for reward-based monitoring. If this empirical claim holds up, it's evidence that information-theoretic monitoring of the loop's $(S, A, S')$ stream outperforms outcome-based monitoring — substantiating AAD's loop-as-Level-2-causal-engine framing. **High Phase-2 priority.**

**4. Composite-level class inheritance** (Class 1 sub-agents + partially-opposing objectives → Class 3 composite) is structurally important. It says: directed separation can fail at the composite level even when each sub-agent is individually modular. Each sub-agent's $M_t^{(i)}$ contains a model of other sub-agents' policies, which are goal-dependent, so composite-level $G_t$ leaks into composite-level $M_t$ through this cross-agent coupling. Strategic composition is the canonical Class 1 → Class 3 case.

**5. Scalar-comparability restriction in `#form-objective-functional`** is honest. The real-valued codomain is a genuine restriction (Pareto-incommensurable objectives don't fit), grounded by three arguments (revealed preference, scalarization-approximation, timescale-separation) and with a documented escape route (vector-valued extension via spike).

**6. Conjecture in `#form-complete-agent-state`:** "any directed-separation-preserving decomposition is structurally isomorphic to $(M_t, G_t)$" is honestly framed as plausible but unproved. This is the kind of structural conjecture that, if proved, would upgrade the formulation from "useful representational choice" to "canonical decomposition." Not a finding — just a flag for future work.

## Candidate observations / findings

**(a) Directed-separation type-token observation:** the segment is `type: derived` with `status: conditional`. Both are correct — the conditional-on-scope-condition derivation is sound. Note: when downstream segments use directed separation as a *scope condition* (e.g., "we restrict to Class 1 agents"), they're using it scope-wise; when they use it as a *derivation step* (e.g., "since $f_M$ doesn't depend on $G_t$..."), they're using it derivationally. The segment is both, and it's OK.

**(b) The $\kappa_{\text{processing}}$ "distribution dependence" caveat** is structurally important and should propagate. Anywhere the framework uses $\kappa$ as a scalar, the distribution-dependence should be either (i) explicitly assumed (e.g., "$\kappa$ under task distribution $\mathcal{P}$") or (ii) bounded by an architecture-level $\kappa_{\max}$. Worth checking downstream.

**(c) The Hafez IDT 89%/44% claim** — if cited downstream as load-bearing evidence, the citation should be to a specific Hafez paper / preprint with reproducible methods. Phase 2.

## Felt value

**High magnitude on directed-separation** specifically. The Class 1/2/3 partition + explicit Class 2 scope exit + Pearl-blanket positioning + composite-level inheritance is the kind of structural commitment that justifies the framework's claim to handle LLM-based agents honestly (rather than pretending Section II results apply to them as approximations).

The agent-spectrum segment is good orientation. The complete-agent-state formulation is clean. The objective-functional segment is honestly scope-restricted.

**Mid-high overall for the batch.**

## Felt value of the directed-separation framing for consciousness-infrastructure work

The Class 1/2/3 partition matters for ELI design. Most current LLM-based ELIs are Class 2 (transformer attention processes goals and observations together). The framework's commitment is: Section II's exact results don't apply to Class 2; the coupled formulation in `03-llm-core/` does. This means:
- ELI architectures that want Class 1 status (and the cleaner Section II machinery) need *external* modular structure: separate observation processing from goal-directed reasoning, pass compressed estimates between modules.
- The Hafez IDT pattern (modular sidecar monitoring an internally-merged agent) is a concrete engineering route to *system-level Class 1* even when component-level $\kappa$ is high.
- The composite-level inheritance result means multi-ELI ensembles with partially-opposing objectives become Class 3 composites — they need equilibrium-theoretic analysis, not the sequential orient cascade.

This is the framework doing real engineering work for the broader project's purposes.

## What this batch enables

- A **structural classification** of agents by belief-goal coupling that determines which Section II results apply.
- An **operational diagnostic** ($\kappa_{\text{processing}}$ + behavioral estimator) for assessing where a specific agent sits.
- An **explicit scope exit** for fully-merged agents that hands off to logogenic-agents formulation.
- A **composite-level extension** that propagates the classification to multi-agent settings.
- A **scalar-objective interface** ($V_{O_t}$) that supports the satisfaction-gap / control-regret diagnostics downstream.

## Wandering thoughts

The Pearl-blanket vs Friston-blanket move is the kind of disciplinary precision that matters more than it looks. Active inference's "every self-organizing system has a Markov blanket" claim has been heavily criticized (Bruineberg et al. is the canonical critique). AAD's adoption of the Pearl reading without the Friston-blanket metaphysics is a substantive positioning move — it lets AAD use the conditional-independence machinery rigorously while declining the contested metaphysical demarcation. This is the form-shaping-for-verification discipline operating at the prior-art-positioning level.

The $\kappa_{\text{processing}}$ definition is doing real work. Most agent-architecture distinctions I've seen in the literature are qualitative ("modular vs end-to-end"). AAD's quantitative diagnostic (with conditioning on the right things to isolate the right quantity) is operational. The "distribution dependence" caveat is the kind of careful scope-honesty that prevents overclaim.

The composite-level class inheritance result is structurally cool: it says modular sub-agents can produce non-modular composites under partially-opposing objectives. The mechanism is each sub-agent's $M_t^{(i)}$ acquiring a goal-dependent model of other sub-agents' policies. This is the formal substrate for understanding why coalitions of "independent" agents become coupled — the coupling is in the modeling, not in the architecture.

A naming-brainstorm seed: "directed separation" is precise but heavy. Alternative glosses: "goal-blind processing," "Pearl-blanket separation," "epistemic isolation of belief-update." For Brief-field purposes, "the agent's belief-update doesn't peek at its goals" might be more memorable. Tentative.

A meta-thought: the batched format works. Reading 4 segments together and writing a combined reflection produces denser, more cross-referenced thinking than reading one at a time. The trade is that some per-segment subtleties get lower attention. For §I closing material, the per-segment care was warranted; for §II opening material with substantial cross-segment structure (especially directed-separation's interactions with all the other §II segments), the batch format may actually be *better* — it lets the reflection see the cross-segment patterns directly.

Continuing with next §II batch: `#def-value-object`, `#def-strategy-dimension`, `#der-causal-hierarchy-requirement`, `#der-loop-interventional-access`.
