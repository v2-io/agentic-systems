# Spike Track: Class Coercion via Wrapping

**Status**: open — initial brief
**Date opened**: 2026-05-09
**Conversation provenance**: Discussion in the temporal-nesting-RG spike track surfaced that Parts III/IV (logogenic agents and ELIs) construct AAD-shaped systems around Class-3 components (LLMs). Joseph asked whether this is a *general* construction — whether Class-2 / Class-3 components can be *constructively* wrapped into Class-1 composites. The hypothesis: this construction is general, gives a constructive form-preservation result, and clarifies the structural relationship between Parts I/II and Parts III/IV.

**Purpose of the spike**. Discover whether the construction actually works as a load-bearing AAD result, and if so, what conditions it requires, what costs it pays, and what existing AAD machinery it strengthens. The aim is theory-strengthening and truth-discovery — *does this hold and what does it actually say?* — not output-shape optimization. Paper-sized findings may naturally fall out (testable bounds on LLM systems, in particular) but they are downstream consequences of theory holding up, not the goal of the work.

**Why this matters for ASF specifically**.
1. Parts III/IV currently sit as a "different problem domain" requiring "coupled formulation from the start" (per CLAUDE.md). Formalizing the wrapping construction would make Parts III/IV a *derived* application of the AAD core rather than a parallel research thread — strengthening the theory's coherence.
2. The form-preservation framing from `spikes/temporal-nesting-rg/99-verdict.md` is currently *descriptive* — when does the form survive coarse-graining? A constructive-form-preservation result would strengthen the framing's load-bearing content.
3. `#hyp-directed-separation-under-composition` is currently a hypothesis. The wrapping construction is a candidate *constructive procedure* for making directed separation hold under composition — which would promote the hypothesis if it goes through.
4. The κ-as-scalar framing was identified as a category error in CLAUDE.md, but the leakage analysis (Sub-spike C) may rehabilitate a wrapper-level residual-coupling rate that *is* meaningful. Worth checking.

**Depends on / cites**: `#hyp-directed-separation-under-composition`, `#der-directed-separation` (the descriptive classification), `#form-composition-closure` (admissibility (A1)–(A4)), `#der-tempo-composition` (Brooks's-Law form), `#result-sector-persistence-template`, the Parts III/IV component (`03-logogenic-agents/`, `04-eli/`), the PROPRIUM ontology and architecture (`~/src/firmatum/PROPRIUM-ONTOLOGY.md`, `PROPRIUM-ARCHITECTURE.md`), `~/src/shoshin/` (PROPRIUM operational instance), the agentic-tft document family (`ref/agentic-tft/`), `spikes/temporal-nesting-rg/99-verdict.md` for the form-preservation framing context.

---

## 1. The construction

The structure of the wrapper is the same in every instance, varying only in which queries the underlying component supports and how the wrapper aggregates them.

### 1.1 Setup

Let $A : \mathcal{I}_A \to \mathcal{O}_A$ be a primitive component — a function from inputs to outputs that the wrapper treats as a black-box oracle. Let $\mathcal{Q}_A \subseteq \mathcal{I}_A$ be the set of admissible queries the wrapper can issue.

A **wrapper** $W$ over $A$ is an AAD-shaped composite agent with explicit external state $X_W = (M_W, G_W)$ where $M_W \in \mathcal{X}_M$ is the wrapper's belief state and $G_W = (O_W, \Sigma_W) \in \mathcal{X}_G$ is its purposeful sub-state. The wrapper's update is:

$$f_W(X_W, o_W) = (\, f_M(M_W, o_W;\, q_M(M_W, o_W);\, A(q_M)),\; f_G(G_W, M_W;\, q_G(M_W, G_W);\, A(q_G))\, )$$

Reading the type signatures:

- $q_M : \mathcal{X}_M \times \mathcal{O}_W \to \mathcal{Q}_A$ — a **goal-blind query selector**: the wrapper chooses what to ask the component about, based on $M_W$ and the current observation, *but not on $G_W$*. This is the structural commitment that gets directed separation back at the wrapper level.
- $q_G : \mathcal{X}_M \times \mathcal{X}_G \to \mathcal{Q}_A$ — a **goal-conditioned query selector**: for strategy updates, the wrapper is allowed to consult the component goal-conditionally (this is what (A1) requires for $\Sigma_W$ updates).
- $f_M : \mathcal{X}_M \times \mathcal{O}_W \times \mathcal{Q}_A \times \mathcal{O}_A \to \mathcal{X}_M$ — the belief-update map, a function of $M_W$, observation, the query made, and the component's response. **Crucially, no $G_W$ argument.**
- $f_G : \mathcal{X}_G \times \mathcal{X}_M \times \mathcal{Q}_A \times \mathcal{O}_A \to \mathcal{X}_G$ — the strategy-update map, allowed to use $G_W$ and goal-conditioned queries.

The external policy is $\pi_W : \mathcal{X}_W \to \mathcal{A}_W$, selecting external actions on the environment.

### 1.2 The directed-separation claim

**Claim (Wrapper-Level Directed Separation).** Under conditions C1–C3 below, $\dot M_W$ is independent of $G_W$ — directed separation holds at the wrapper level *exactly*.

The intuition is structural: $f_M$'s type signature has no $G_W$ argument; $q_M$'s type signature has no $G_W$ argument; therefore the only path by which $G_W$ could influence $M_W$ is through $A$'s response to a query whose input doesn't carry $G_W$. If $A$ does not infer goal-information from query patterns, that path is closed.

**Conditions:**
- (C1) **Admissibility.** $\mathcal{Q}_A$ contains queries whose specification depends only on $M_W$ and $o_W$ (the wrapper can construct goal-blind inputs). Sub-spike B characterizes the failure modes here (some components don't admit goal-blind queries; e.g., end-to-end policies with no observable belief channel).
- (C2) **Determinism (or fixed conditional).** $A$'s output distribution conditional on input is fixed: $A$ does not adapt during deployment in ways that depend on goal information seen elsewhere in the trajectory.
- (C3) **No goal-inference leakage.** $A$ does not infer goal information from query patterns and inject it back into outputs. This is the strong leakage absence condition. Sub-spike C characterizes the residual when this fails.

When (C1)–(C3) hold *exactly*, the wrapper is Class-1 by construction. When (C3) holds *approximately*, the wrapper is *almost-Class-1* with leakage bounded by a residual coupling rate $\kappa_W$.

### 1.3 Why this works

The wrapper is a coarse-graining of the component: many component calls per macro-step, with the wrapper imposing structural separation between calls that update $M_W$ and calls that update $G_W$. The temporal-nesting-RG spike (`spikes/temporal-nesting-rg/`) established that AAD's form is preserved under coarse-graining (form-preservation is the framing's core claim). Class coercion via wrapping is the *constructive* version: instead of asking "when is form preserved?" we ask "how do we *make* the form be preserved?" The answer is: build a scaffold whose structural separation enforces what the underlying component fails to provide.

The construction does not reduce the underlying component's expressiveness — $A$ can still be invoked goal-conditionally for $G_W$ updates. What it does is *factor the component's role* into goal-blind queries (which feed $M_W$) and goal-conditioned queries (which feed $G_W$). The factorization is structurally enforced by the wrapper's type signatures.

## 2. The tempo cost: Brooks's-Law instance

The wrapper makes $K \geq 1$ component calls per macro-step (one for $M_W$ update, one for $G_W$ update, possibly multiple for retrieval / planning). If the component's nominal call rate is $\nu_A$, the wrapper-level update rate is $\nu_W = \nu_A / K$. By `#der-tempo-composition`:

$$\mathcal{T}_W \leq \mathcal{T}_A - C_\text{coord}^\text{wrap}$$

where $C_\text{coord}^\text{wrap}$ is the coordination overhead specific to the wrapping construction. **The cost of class coercion is paid as tempo.** This is exactly the Brooks's-Law form: adding internal-state-management overhead reduces the realized external tempo even though the underlying component's compute rate is unchanged.

Sub-spike E quantifies this for canonical wrapper architectures and produces testable predictions.

## 3. Coercion-$\varepsilon^*$ vs. fidelity-$\varepsilon^*$

The bridge lemma in `#form-composition-closure` reads $\varepsilon^*$ as a *fidelity* measure: how well does the macro-system track the micro-system? In the wrapping construction, this reading inverts: the wrapper *deliberately* changes the component's behavior to enforce directed separation. We *want* the macro-system to *not* track the micro-system in the goal-conditioning direction.

This requires disambiguation. Sub-spike D works out the right framing. Tentative names:

- $\varepsilon^*_\text{track}$ — the standard bridge-lemma quantity. Measures macro-tracks-micro fidelity. Lower is better; $\varepsilon^* = 0$ means the macro is a perfect compression of the micro.
- $\varepsilon^*_\text{coerce}$ — the wrapping-specific quantity. Measures macro-coerces-micro distance. Higher means the wrapper has more aggressively forced the underlying component into a different (Class-1-shaped) behavior. Lower means the wrapper changes little.

Both have valid bridge-lemma forms; they measure different things. Confusion would be costly in segment-level work, so the disambiguation matters.

## 4. Theorem candidate (preliminary form)

**Theorem (Class Coercion via Wrapping).** Let $A$ be a Class-2 or Class-3 component satisfying admissibility conditions (C1)–(C3) of §1.2. Then there exists a wrapper $W$ over $A$ such that:

1. $W$ satisfies (A1)–(A4) of `#form-composition-closure` at the wrapper level.
2. Directed separation holds at the wrapper level: $\dot M_W \perp G_W$.
3. $W$ is therefore Class-1 in the architecture classification of `#der-directed-separation`.
4. The tempo cost is bounded by $C_\text{coord}^\text{wrap}$ in the form of `#der-tempo-composition`, with explicit dependence on the number of component calls per macro-step.
5. Coercion-$\varepsilon^*$ is bounded by a quantity that depends on the wrapper's structural choices (which queries it issues, how it aggregates).

**Approximate version.** When (C3) is replaced by a leakage bound $\kappa$, directed separation holds approximately at the wrapper level with leakage rate $\le \kappa$, and the wrapper is *almost-Class-1* in the classification.

**Universality claim.** Together with admissibility conditions (C1) for component types, this gives an effective universality statement: AAD applies to all components admitting goal-blind queries, with the cost of class compliance paid in tempo and a measurable coercion distance.

This is the load-bearing claim. Sub-spike A formalizes and proves what can be proved; sub-spikes B–H probe the conditions, costs, and instances.

## 5. Sub-spike enumeration

Each sub-spike is described, with its expected output file. Italicized entries are flagged for delegation to Opus sub-agents.

### A. Theorem statement and proof attempt
Goal: formalize the construction; state the theorem under the cleanest set of conditions; prove what can be proved; identify what reduces to wrapper-design constraints rather than theorem content.
- (A1)–(A4) verification at wrapper level — should be by construction once $f_M, f_G, \pi_W$ are typed correctly.
- (A4) — the sector condition for $f_M$ — is a wrapper-design constraint, not automatic. Document.
- Connection to `#hyp-directed-separation-under-composition`: this strengthens that hypothesis from "when does directed separation hold?" to "constructive procedure for making it hold."

Output: `01-theorem-statement.md`.

### B. Component admissibility characterization
Goal: classify components by whether they admit (C1) — goal-blind queries.
- LLMs: yes, with leakage caveats.
- Pure end-to-end policy networks (no observable belief channel): no.
- RL agents with explicit value functions: probably yes; depends on what the value function exposes.
- Specialized expert systems / databases: yes by design.
- Other agentic primitives (planners, classifiers, retrieval systems): case-by-case.

Output: `02-admissibility.md`.

### C. Leakage characterization (when C3 fails)
Goal: bound the residual coupling $\kappa_W$ when goal-blind queries leak goal-information through component pretraining.
- For LLMs: the mutual information between query distribution and goal distribution gives an upper bound on goal-information surviving in goal-blind responses.
- The bound is a function of context-window content, query selection policy $q_M$, and pretraining dataset goal-content.
- Connect to "almost-Class-1" / partial-Class-2 in `#der-directed-separation`.
- Test: when does $\kappa_W = 0$ exactly? (Probably: when $A$ is a deterministic function of input syntax with no learned world-model component, e.g., a calculator or syntactic parser. Most useful components have $\kappa_W > 0$.)

Output: `03-leakage.md`.

### D. Coercion-$\varepsilon^*$ vs. fidelity-$\varepsilon^*$ disambiguation
Goal: clean separation of the two quantities and their bridge-lemma forms. Avoid downstream confusion.
- Define each carefully.
- Prove (or note) that they admit independent bounds.
- Identify which AAD results (persistence, tempo, etc.) use which quantity.

Output: `04-epsilon-semantics.md`.

### E. Tempo cost accounting
Goal: compute $C_\text{coord}^\text{wrap}$ for canonical wrapper architectures; produce testable predictions.
- ReAct-style wrapper: $K$ scratchpad steps per macro-step.
- PROPRIUM-style wrapper: full nine-component scaffold; $K$ depends on which components are touched.
- Reflexion-style wrapper: $K$ self-evaluation calls per macro-step.
- Connect to `#der-tempo-composition` Brooks's-Law form.
- Output specific empirical predictions: predicted slowdown vs. measured slowdown on benchmark task suites.

Output: `05-tempo-cost.md`.

### F. *Empirical instance survey* (delegate)
Goal: catalog wrapping moves in known scaffolded-LLM frameworks. Categorize by what kind of (M, G) scaffold they implement; identify which are full Class-1 wrappers vs. partial wrappers vs. something else entirely.
- PROPRIUM (canonical for ASF). Read the actual ontology + architecture documents.
- BabyAGI, AutoGPT, ReAct, Reflexion, Voyager, MemGPT, Reflexion, ReST.
- Anthropic's Constitutional AI, RLHF (these are *different* moves — shape the component vs. wrap it; worth differentiating).

Output: `06-empirical-instances.md`. Sub-agent.

### G. Quantitative bounds and what they would predict
Goal: as a *consequence* of the theorem and the leakage and tempo accounting, derive concrete bounds that the theory would predict. Useful both as truth-checks (bounds that match observed behavior support the theory; bounds that don't are diagnostic) and as honest extension surfaces.
- Tempo: predicted slowdown as function of wrapper depth $K$.
- Leakage: predicted $\kappa_W$ as function of context-window goal-content; the prediction can in principle be checked by mutual-information estimators on actual responses.
- Failure modes: predicted behavior when admissibility fails; predicted behavior when leakage exceeds critical thresholds.
- Control / persistence: predicted persistence-condition transfer from component to wrapper level.

Output: `07-quantitative-bounds.md`.

### H. Connection to Parts III/IV (logogenic agents, ELIs)
Goal: show that PROPRIUM is a canonical instance; identify where Parts III/IV constrain or strengthen the general theorem.
- ELI-specific persistence requirements (morally weighted persistence) may go beyond bare class coercion.
- The (M, G) scaffold in PROPRIUM has more structure than the minimum; document what's load-bearing for ELI vs. what's elaboration.

Output: `08-parts-3-4-connection.md`.

### I. *Prior-art differentiation* (delegate)
Goal: clearly differentiate from adjacent constructions in the literature.
- RGM (Friston 2025): parametric scale-invariance vs. architectural scaffolding.
- MDP-homomorphism (Ravindran-Barto, Abel, etc.): compresses an existing modular system vs. constructs modularity around a non-modular core.
- HTN / options / MAXQ: decomposes a goal vs. creates goal/belief separation.
- Constitutional AI / RLHF: shapes the component (changes its weights) vs. wraps it (uses it as a black-box).
- Tool-using LLM frameworks (ReAct, Toolformer): practical instances; AAD provides the theoretical framing.
- LangChain / LangGraph / Inspect: software frameworks for these constructions; cite as engineering instances.
- Categorical / structured active inference (Smithe 2024, Capucci, etc.): compositional structure for nested abstractions; differentiate by the wrapper's *constructive* aspect.

Output: `09-prior-art-differentiation.md`. Sub-agent.

### Synthesis (`99-verdict.md`)
Goal: integrate all sub-spike results; recommend what becomes new AAD segment(s); recommend paper-extraction shape.

## 6. Where this lands in AAD if it goes through

If the theorem holds under the conditions stated:

- **New segment** (probably appendix or new derivation in `01-aat-core/src/`): `#der-class-coercion-via-wrapping` or `#result-class-coercion`. Statement, proof, conditions, costs.
- **Strengthen** `#hyp-directed-separation-under-composition` from descriptive to constructive.
- **New segment** for the leakage characterization: `#meas-wrapper-leakage` or similar. Empirical-claim status; bounds derivable from measurement when relevant.
- **Discussion-level integration** in `#der-tempo-composition` connecting Brooks's-Law form to the wrapper construction.
- **Cross-component reference** in `03-logogenic-agents/` and `04-eli/` segments: PROPRIUM as canonical instance of the general construction; results in those parts inherit the wrapper-level (A1)–(A4) and persistence template.
- **Resolves a known scope-statement** in CLAUDE.md ("Directed separation violated by goal-conditioned agents (LLMs) — handled as architectural scope (Class 2 exit), not approximation"). The wrapping construction promotes this from "scope exit" to "constructive route through" — Class 3 isn't a fundamental obstruction; it's a primitive-component class that can be wrapped at a measurable cost.

## 7. Risks and honest caveats

- **The strong-leakage-absence condition (C3) may not hold for any real LLM.** All pretrained models carry implicit goal-correlations from training data. The "approximate Class-1" version may be the best one can do for any real instance. The theorem statement must be honest about this — the *exact* version may be a structural ideal that no operational system reaches.
- **The construction may be expensive in tempo.** If $K$ is very large, the wrapper-level tempo may be too slow to be useful for most tasks. The theorem says class coercion is *possible*; the cost question is whether the result is *useful*. Both belong in the honest accounting.
- **The wrapping construction changes the component's behavior intentionally.** Reasonable people may disagree about whether the resulting agent is "the same" as the underlying component "in some meaningful sense." This is partly a philosophical question and partly a question about what we want from AAD-compliant systems. Take a position; don't paper over it.
- **"Universality of AAD" is a strong claim that needs to be hedged.** The construction works for components admitting goal-blind queries; it doesn't apply to components where this is structurally impossible. The honest statement is "AAD applies to all *admissible* components," not "AAD applies to all components."
- **The (O, Σ) recursion thread from `spikes/temporal-nesting-rg/03-rg-0c-strategy-recursion.md`** found that recursive sub-objectives are degenerate / typed-options-MAXQ. Make sure the wrapping construction doesn't quietly rely on the (O, Σ) recursion that was deferred.

## 8. Working agreements

- **Math lives in segments, not spikes.** Successful theorems land as appendix segments under `01-aat-core/src/`. This directory is the reasoning trail.
- **Honest epistemic labels.** Each result tagged with its tier. Failed proof attempts documented as failures, not deleted.
- **Strengthen before softening** (per project convention). When a condition fails, attempt to derive a stronger result first; only then narrow scope.
- **Cite generously.** Per AAD's prior-art-integration discipline, adopt names and frameworks from prior work (RGM form-preservation, MDP-homomorphism bridge bounds, scaffolded-LLM frameworks). AAD's contribution is the synthesis.
- **Self-contained for handoff.** Future-me or future-agent should be able to pick up cold from any file in this directory.

---

## 9. File index

- `00-brief.md` — this file
- `01-theorem-statement.md` — sub-spike A (in progress)
- `02-admissibility.md` — sub-spike B (pending)
- `03-leakage.md` — sub-spike C (pending)
- `04-epsilon-semantics.md` — sub-spike D (pending)
- `05-tempo-cost.md` — sub-spike E (pending)
- `06-empirical-instances.md` — sub-spike F (delegated)
- `07-quantitative-bounds.md` — sub-spike G (pending)
- `08-parts-3-4-connection.md` — sub-spike H (pending)
- `09-prior-art-differentiation.md` — sub-spike I (delegated)
- `99-verdict.md` — synthesis (final)
