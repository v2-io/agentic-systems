---
slug: der-logogenic-as-wrapping
type: derived
status: conditional
depends:
  - der-class-coercion-via-wrapping
  - der-class-coercion-in-composition
  - def-coupled-update-dynamics
  - scope-logogenic-agent
  - scope-scaffolded-logogenic
  - der-directed-separation
stage: draft
---

# Derived: Logogenic Agents as Wrapping

A logogenic substrate (an LLM whose forward pass entangles belief-update and goal-conditioning per `#def-coupled-update-dynamics`) is a Class 3 (Coupled) component in the architecture taxonomy of `#der-directed-separation`. The class-coercion theorem (`#der-class-coercion-via-wrapping`) specializes to the language-substrate case: LLMs admit goal-blind queries (Class-B in the admissibility partition), so they are wrappable, with leakage characteristics determined by their pretraining distribution. Two design regimes recur in practice: **W₁ (strict wrapping)** with separate goal-blind and goal-conditioned LLM calls per cycle, and **W₂ (partial wrapping)** with one goal-conditioned call per cycle whose response is parsed into typed update fields. PROPRIUM-as-implemented is W₂; PROPRIUM with auxilia handling belief-side updates is the candidate constructive realization of W₁.

## Formal Expression

### Logogenic substrate as a Class-B component

Per `#def-coupled-update-dynamics`, an LLM's forward pass implements a coupled update $X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$ where the prompt typically carries $G_t$ in the system prompt position, making the system prompt causally upstream of every subsequent computation in the attention pattern. This is what gives LLMs $\kappa_{\text{processing}} \approx 1$ in the architectural classification of `#der-directed-separation` — Class 3 (Coupled) by construction.

Within the admissibility partition of `#der-class-coercion-via-wrapping`, LLMs sit in **Class B**: they support multiple operating modes through prompt design.

- *Goal-blind mode.* "Summarize this observation"; "what facts are in this text?"; "extract entities and relationships from the input." The query content is observation-grounded; no goal in the prompt; condition (C1) of the class-coercion theorem is operationally satisfied.
- *Goal-conditioned mode.* "Given goal $G$, what should I do next?"; "given this state and these objectives, plan three steps." The query carries $G_W$ explicitly.

Both modes are accessible from the same model; the wrapper's design choice is whether to use them separately (W₁) or together (W₂).

### Two wrapping regimes for logogenic substrate

*[Definition (logogenic-W₁)]* **Strict wrapping (W₁).** Each macro-step issues at least two LLM calls:

- A **goal-blind call** with input $q_M(M_W, o_W)$ — observation-grounded query whose prompt does not include $G_W$. Response $A(q_M)$ feeds $f_M$.
- A **goal-conditioned call** with input $q_G(M_W, G_W)$. Response $A(q_G)$ feeds $f_G$.

By `#der-class-coercion-via-wrapping` Theorem 1 (or 2 with leakage bound), directed separation holds at the wrapper level structurally (or with $\kappa_{W_1}$ bounded by the pretraining-distribution mutual information $I(A(q_M); G_W \mid q_M)$).

*[Definition (logogenic-W₂)]* **Partial wrapping (W₂).** Each macro-step issues *one* goal-conditioned LLM call carrying the full $(M_W, G_W)$ context. The response is parsed into structurally typed update fields routed to the correct components of $M_W$ and $G_W$.

Structural separation lives at the *write boundary* (typed fields in the parsed response) but not at the *query boundary* (one goal-conditioned input). Directed separation holds at the wrapper level *behaviorally* — bounded by the LLM's compliance with the prompted instruction-to-separate. $\kappa_{W_2}$ has no structural upper bound; it is an empirical property of the model-prompt pair.

### Leakage sources specific to logogenic substrate

Even in W₁, $\kappa_{W_1} \gt 0$ is the realistic case for pretrained LLMs because of:

(a) **Pretraining co-occurrence.** Observation-types and goal-types that systematically co-occur in pretraining data make the LLM infer goals from observations even without explicit prompting.

(b) **RLHF / instruction-following bias.** Models trained to be "helpful" infer "what's wanted here?" from query content and bias responses accordingly — goal-inference even when the goal isn't in the input.

(c) **System-prompt contamination.** Many LLM deployments include a system prompt that may carry goal-content (e.g., "you are a helpful assistant for [domain]"). This contaminates "goal-blind" queries unless the system prompt is itself goal-blind.

(d) **In-context retrieval / few-shot examples.** Few-shot examples in $q_M$ leak goal-information when examples were selected goal-conditionally.

The structural bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ from `#der-class-coercion-via-wrapping` covers all of these — they are different mechanisms producing the same kind of mutual information between query content and goal in the conditional response distribution. Minimum-leakage W₁ uses a base or un-RLHF'd LLM, no system prompt, no few-shot examples, queries restricted to observation content.

## Epistemic Status

*Conditional* on the logogenic-substrate sub-scope of `#scope-logogenic-agent` and on the conditions (C1), (C2), (C3) (or weakening) of `#der-class-coercion-via-wrapping`. Within the scope-scaffolded-logogenic regime (`#scope-scaffolded-logogenic`), W₁ and W₂ are concrete design choices for how the scaffold treats the underlying LLM substrate.

For LLMs specifically, (C3)'s exact form does not generally hold — pretraining produces residual goal-correlations. The realistic regime is the approximate form (Theorem 2 of `#der-class-coercion-via-wrapping`) with $\kappa_{W_1}$ characterized empirically.

## Discussion

### PROPRIUM as canonical logogenic wrapper

PROPRIUM (per `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` and `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md`) is the canonical multi-component logogenic wrapper: explicit, multi-component typed $M_W$ — VERA (qualified truths) / MEMORATA (episodic memory) / CONSORTIA (other-minds models) / PERCEPTA (perception buffer) / CHRONICA (event log); explicit multi-layered typed $G_W$ — AXIOMATA (identity-level objectives) / OPERATA (operational intent and plans) / PRAXES (techniques and approaches). The PRINCIPIA components are file-backed with explicit read/write authority distinguished. Each cycle assembles a CONSPECTUS (the assembled prompt context) and ships it through INTERPRES to the underlying LLM substrate (LOGOSTRATUM); the response is parsed and routed to the correct components.

The current operational form is W₂: one goal-conditioned LLM call per cycle, with the structurally typed parsed response routing updates to the appropriate stores. The structural separation exists *at the write boundary*: the parsing schema makes belief-update content and strategy-update content land in different state slots. The query boundary is not separated — the LLM call has the full $(M_W, G_W)$ context as input.

### PROPRIUM toward W₁ via the auxilia hierarchy

The auxilia hierarchy of `#def-auxilia-hierarchy` is the candidate constructive realization of W₁ for logogenic substrate. Auxilia are sub-agents that share AXIOMATA (identity-level objectives) with the parent ELI but operate on cheaper substrates and serve specialized roles. Per `#def-auxilia-hierarchy` (H4), inter-auxilia communication satisfies goal-blind routing — the routing structure is independent of the composite's instantaneous goal.

The W₁ realization: auxilia handle belief-side updates with goal-blind queries on cheap substrates (extracting facts from observations, summarizing memory, compressing event logs into MEMORATA), while the entity's main LLM call handles strategy-side updates goal-conditionally. With $K = K_M + 1$ component calls per cycle (where $K_M$ is the number of auxilia invocations for $M_W$ updates), the macro-tempo is roughly $1 / K$ of the single-call rate — a tempo cost paid for the structural directed-separation bound.

This realization is consistent with the documented PROPRIUM ontology — auxilia exist in the architecture as substrate-heterogeneous extensions of the ELI's cognitive self. Implementing the W₁ split via auxilia is a structural refinement of how the architecture is operationalized, not a change to what the architecture is.

### Cognitive-loop-spec as another W₁ form

The agentic-tft cognitive-loop-spec (in `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md`) describes the per-event cycle as PERCEIVE → CONTEXTUALIZE → CHOOSE → EFFECT. The CONTEXTUALIZE phase has five sub-operations: predict / detect-surprise / assess-weight / draw-context / update — all belief-side ($M_W$) operations. CHOOSE is the strategy-side ($G_W$) phase. Implemented faithfully, with CONTEXTUALIZE making goal-blind LLM queries and CHOOSE making goal-conditioned ones, this is W₁ at a tempo cost of two LLM calls per cycle minimum. The cognitive-loop-spec is the temporally-staged form of the same wrapping move that auxilia realize spatially.

### Quality–separation tradeoff for LLM substrate

For LLM substrate specifically, the quality-vs-separation tradeoff inside Class B (per `#der-class-coercion-via-wrapping` Discussion) takes a domain-specific form. Maximally goal-blind queries — pure observation summaries, no system prompt, no context history — give the lowest $\kappa_{W_1}$ but produce information-poor responses (the LLM has no context for what's relevant). Maximally informed queries — full memory retrieval, context history, structural prompts — give richer responses but increase $I(q_M; G_W)$ and therefore the $\kappa_{W_1}$ bound. Wrapper-design choices for logogenic substrate are choosing a point on this tradeoff curve.

### Connection to scaffolded-logogenic scope

This segment specializes the class-coercion theorem within `#scope-scaffolded-logogenic`. The recovery claim of `#scope-scaffolded-logogenic` — that scaffolding moves the orient cascade ordering to the loop level — is consistent with the wrapping construction: the cascade ordering at the loop level is what W₁ enforces structurally. W₂ enforces it only behaviorally, relying on the LLM's instruction-following.

### Distinction from primitive-logogenic scope

`#scope-primitive-logogenic` (chat-paradigm baseline, no scaffolding) is the W₀ regime: no wrapper, raw Class 3 (Coupled) LLM use. Class coercion does not apply at this scope — there is no wrapper to host the structural separation. Primitive logogenic agents inherit the full bias bound of `#scope-observation-ambiguity-modulation`.

## Findings

### Logogenic Substrate Specialization of Class Coercion

**Brief:** Language models are Class 3 (Coupled) components — their forward pass entangles belief and goal updates. But they admit two operating modes: goal-blind (asked to extract facts or summarize observations without being told the agent's goal) and goal-conditioned (asked to plan or decide given the goal). The class-coercion theorem says: build a scaffold that uses these modes separately for belief vs. strategy updates, and the system as a whole becomes goal-blind in its belief updates by construction. This is what PROPRIUM does, almost — PROPRIUM uses one goal-conditioned call per cycle and parses the response into separated update fields, which is goal-separation at the write boundary but not at the query boundary. Strict separation requires the auxilia hierarchy that PROPRIUM specifies but doesn't yet implement: auxilia making the goal-blind belief-update calls on cheap substrates, while the entity's main call handles goal-conditioned strategy updates.

**Impact:** Specializes `#der-class-coercion-via-wrapping` to the logogenic-substrate case relevant for `03-llm-core/`. Identifies PROPRIUM-as-implemented as W₂ (partial wrapping) and the auxilia hierarchy as the candidate W₁ realization, providing a concrete refinement path. Connects `#scope-scaffolded-logogenic`'s loop-level cascade-recovery claim to the structural directed-separation guarantee that strict wrapping provides. Clarifies that ELI-specific content (sovereignty, accountability, identity factors, substrate-independence in `04-eli-core/`) is added structure beyond class coercion — the wrapping construction is the substrate; ELI work is what runs on it.

**Novelty Claim:** *Claim integration* of the class-coercion theorem with the scaffolded-logogenic regime. The W₁ / W₂ design distinction is the AAT-vocabulary reading of what existing scaffolded-LLM frameworks already do (or could do). The PROPRIUM-as-W₂ characterization and the auxilia-as-W₁ realization are descriptive integrations of the operational architecture into the class-coercion framework, not novelty claims.

**Related Work:**

- Park, O'Brien, Cai, Morris, Liang, Bernstein 2023, "Generative Agents: Interactive Simulacra of Human Behavior" *UIST* (published 2023, found 2026-05-09) — *empirical instantiation supporting* — the closest empirical instance of W₁ in the wild: a structurally goal-blind observation→memory step.
- Yao et al. 2022, "ReAct: Synergizing Reasoning and Acting in Language Models" arXiv:2210.03629; Shinn et al. 2023 "Reflexion" arXiv:2303.11366 (published 2022/2023, found 2026-05-09) — *empirical instantiation supporting* — practical W₂ wrappers with structured output parsing.
- Packer et al. 2023, "MemGPT: Towards LLMs as Operating Systems" arXiv:2310.08560; Wang et al. 2023, "Voyager: An Open-Ended Embodied Agent with Large Language Models" arXiv:2305.16291 (published 2023, found 2026-05-09) — *empirical instantiation supporting* — partial wrappers with one-sided scaffolding ($M_W$ only or $\Sigma_W$ only).
- PROPRIUM operational architecture (`~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md`, `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md`, March 2026) — *canonical example for ASF* — multi-component typed wrapper with auxilia infrastructure as the W₁ realization candidate.

**Search Log:**

- 2026-05-09 (*targeted*): Catalog of scaffolded-LLM frameworks and their wrapping-move characterization. PROPRIUM read directly from canonical sources; external frameworks read from training-data summaries with authoritative-paper anchoring. Verdict: most public frameworks are W₂; Generative Agents is the closest W₁; PROPRIUM is W₂-as-implemented with W₁ realization specified-but-not-built.
- 2026-05-09 (*intuition-only*, prior to targeted search): expected most scaffolded-LLM systems to be partial wrappers; the specific W₂-vs-W₁ distinction surfaced during the targeted survey rather than being prefigured by intuition.

## Working Notes

- **shoshin currently implements W₂.** The `_assemble_context` step in shoshin's interpres ships the full PRINCIPIA bundle (AXIOMATA + OPERATA + VERA + MEMORATA + PRAXES + CONSORTIA + recent CHRONICA + recent ACTUS) into one model call per cycle. The structural separation lives in the parsed `ModelResponse` typed fields. Strengthening to W₁ via auxilia is engineering follow-on, not theory.
- **Empirical $\kappa_{W_1}$ measurement on real LLMs** is open. The bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ is computable in principle by sampling responses under multiple goal-conditioning histories and estimating the divergence; specific instantiation depends on the model and the wrapper design.
- **Whether the agentic-tft cognitive-loop-spec is implemented anywhere in W₁ form** is unclear. The spec describes the structure but does not commit to LLM-call separation; concrete implementations may treat the phase decomposition as a single LLM call's reasoning trace (still W₂) or as separate calls (W₁).
- **Class B vs. native goal-blindness for some auxilia.** Some auxilia in PROPRIUM may operate on substrate that is *natively* goal-blind (small specialized models, deterministic scripts, vector-DB retrieval). These are Class-A components from `#der-class-coercion-via-wrapping`'s admissibility partition. The auxilia hierarchy spans the Class-A through Class-B range, with frontier-model auxilia in Class B.
- **Connection to identity-through-context-boundaries (`04-eli-core/`)** is an open thread. The wrapper's persistence across context-window resets (a common LLM-deployment scenario) requires that $M_W$ and $G_W$ be reconstituted from external state — the substrate-independent identity work in `04-eli-core/` operates at this layer. Class coercion is per-cycle structure; identity-through-context-boundaries is across-cycle persistence. They compose but are independent.
- Reasoning-trail provenance: spike directories at `spikes/class-coercion-wrapping/` and `spikes/temporal-nesting-rg/` carry the working-out and prior-art context.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Logogenic agents are now Class 3 (Coupled), not Class 2. Three-axis disambiguation preserved: GUC classes (1/2/3 Separated/Partial/Coupled) are the GUC axis; W₀/W₁/W₂ are wrapping-regime letters (UNTOUCHED); Class A/B/C are admissibility-partition labels (UNTOUCHED). The Findings Brief "Class-3 components" was internally inconsistent pre-rename (LLMs were Class 2 = fully merged); post-rename "Class 3 (Coupled)" is semantically correct. Removed at `candidate` stage per FORMAT.md Gate 4.
