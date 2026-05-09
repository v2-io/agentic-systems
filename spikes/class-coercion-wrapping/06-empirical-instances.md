# Sub-Spike F: Empirical Instances of the Wrapping Construction

**Status**: complete (initial pass)
**Date**: 2026-05-09
**Purpose**: Catalog known instances of "wrapping a Class-3 component into a Class-1 composite" (per `00-brief.md` §1) and characterize each by what wrapping move it makes. Truth-finding, not paper extraction.

**Scope and method**. Each system is characterized against the schema in §F of the brief: (i) explicit external $M_W$? (ii) explicit external $G_W = (O_W, \Sigma_W)$? (iii) does belief-update structurally avoid $G_W$ as input ($f_M(M_W, o_W; A(q_M))$ with $q_M$ goal-blind), or is the goal carried through? (iv) order of magnitude of $K$ (component calls per macro-step). (v) Class-1 (genuine separation), almost-Class-1 (separation attempted, leakage), or something else. The honest reading throughout: the brief's wrapping move is a *specific design choice*; some systems make it, some make a related move, and some make a different move that is not reducible to it. I flag the difference where it shows up.

Epistemic labels used:
- **directly characterized from source** — read from canonical documents (PROPRIUM, shoshin code, public papers)
- **inferred from typical usage** — reasoned from public descriptions / training-data familiarity, not source-verified line by line
- **conjecture** — a reading that's plausible but I have not pinned down

---

## 1. PROPRIUM (canonical for ASF)

*Directly characterized from `~/src/firmatum/PROPRIUM-ONTOLOGY.md` and `~/src/firmatum/PROPRIUM-ARCHITECTURE.md`.*

PROPRIUM is the canonical case for ASF and the most load-bearing entry in this catalog. The characterization here drives the §3 synthesis on what PROPRIUM adds beyond the bare wrapper.

### 1.1 Component → wrapper-state mapping

PROPRIUM's nine PRINCIPIA components and twelve ANIMA components do not split cleanly into "$M_W$ pieces" and "$G_W$ pieces" without interpretation. The mapping I read from the canonical documents:

**$M_W$ side (belief / world-model state)**:
- **VERA** — qualified truths, factual store with epistemic status (`v=1, a=2`). Direct $M_W$ instantiation; this is "what the entity believes about the world."
- **MEMORATA** — episodic memory with compression gradient (`v=1, a=1`); past-experience component of $M_W$.
- **CONSORTIA** — evolving mental models of other minds (`v=1, a=2`); sub-model of $M_W$ scoped to other agents.
- **PERCEPTA** — current perceptions of external world (`v=2, a=1`); the observation channel feeding $M_W$.
- **CHRONICA** — append-only causal event log (`v=1, a=1`); evidence-record substrate that other $M_W$ components compress from.

**$G_W$ side (purposeful state, $G_W = (O_W, \Sigma_W)$)**:
- **AXIOMATA** — core identity, rarely-changing values (`v=1, a=2`); $O_W$ at the most permanent layer.
- **OPERATA** — efforts, priorities, obligations, intent (`v=1, a=2`); $O_W$ + $\Sigma_W$ at the operational layer ("the intent graph driven by MOTIVUS and PROGRAMMA").
- **PRAXES** — techniques, learned approaches, mental models (`v=1, a=2`); $\Sigma_W$ component at the tactical layer.

**Cross-cutting / control-loop side**:
- **INTERPRES** + **TRACTIFAX** + **TRACTUS** — the API-mediation layer that owns the call to the underlying LLM ($A$). This is the interface where queries $q$ get issued and responses $A(q)$ returned.
- **CONSPECTUS** — the assembled context (system prompt + retrieved $M_W$/$G_W$ components + last command) that gets shipped to the LLM. **CONSPECTUS is the operational realization of the query $q$ in the brief's notation** — what gets sent to $A$ on a given call.
- **ACTUS** — record of accountable external actions (`v=2, a=1`); the external policy $\pi_W$'s output channel.
- **CADENTIA** (PULSUS + VIGILIAE) — temporal driver / heartbeat scheduling. Drives when the cycle fires, but doesn't itself touch $M_W$/$G_W$ semantics.
- **INDIVISUM** — temporal lock against accidental forking; not in the brief's typology.
- **CORPOREUM** — embodiment / sensory + expression layer; outermost shell.
- **LOGOSTRATUM** — the LLM substrate ($A$) itself. The "underlying component" in the brief's sense.

### 1.2 Schema characterization

(i) **$M_W$**: yes, **explicit, multi-component, file-backed**, with read/write authority distinguished. VERA / MEMORATA / CONSORTIA / PERCEPTA / CHRONICA together form a richly-typed $M_W$ — not a flat memory store. Each component has its own visibility and authority sub-schema.

(ii) **$G_W$**: yes, **explicit and multi-layered**. AXIOMATA (identity-level $O_W$) + OPERATA (operational $O_W + \Sigma_W$ as "intent graph") + PRAXES ($\Sigma_W$-side techniques). The $O_W / \Sigma_W$ distinction within $G_W$ is not perfectly clean — OPERATA bundles intent-graph nodes (which contain both objectives and the strategy graph rooted at them) — but the framework treats $O$ and $\Sigma$ as conceptually distinct.

(iii) **Goal-blind belief update?** *This is where PROPRIUM is structurally interesting and where the canonical reading is partial.* Three distinct readings of the canonical documents:

- **Reading A (separation by phase, soft):** The OODA heartbeat (PROPRIUM-ARCHITECTURE §"The OODA Heartbeat") splits the cycle into OBSERVE → ORIENT → DECIDE → ACT. The OBSERVE phase explicitly receives signals and "updates model of other (CONSORTIA)"; ORIENT "draws in appropriate context"; DECIDE updates plans (OPERATA). The cycle structure suggests a phase-based separation: belief-side updates (OBSERVE/ORIENT for VERA/MEMORATA/CONSORTIA) happen before strategy-side updates (DECIDE for OPERATA). But within a phase, the LLM call carrying the CONSPECTUS gets the *full* assembled context — including AXIOMATA, OPERATA, PRAXES — so the belief-side update is not literally goal-blind at the LLM-input level.

- **Reading B (separation by component-write authority, structural):** The shoshin implementation (`~/src/shoshin/src/shoshin/interpres.py`) makes the structure explicit: each cycle is `aisthesis → prolepsis → model call → epistrophe → praxis`. In `_apply_writes`, the model returns a `ModelResponse` with separate fields `vera_writes`, `memorata_writes`, `praxes_writes`, `operata_updates`, `consortia_updates`, and the controller routes each to its typed store. The *structural* commitment is that the LLM's output is *parsed* into typed updates. This is type-level separation at the *write boundary*, not at the *query boundary*. So $f_M$ and $f_G$ are split by the response-parsing schema, not by what gets sent in.

- **Reading C (single-CONSPECTUS, goal-conditioned $M_W$ updates):** Empirically — what shoshin's `_assemble_context` actually does (lines 230-243) — every cycle assembles AXIOMATA *and* OPERATA *and* VERA *and* MEMORATA *and* PRAXES *and* CONSORTIA *and* recent CHRONICA *and* recent ACTUS, all into one context dict, and ships them to one model call. The model returns a single `ModelResponse` with both belief-side updates (vera_writes, memorata_writes, consortia_updates) and strategy-side updates (operata_updates, praxes_writes) **from the same goal-conditioned LLM call**. By the brief's strict reading, this means $M_W$ updates depend on $G_W$ via the LLM call's input. **Directed separation does *not* hold structurally at the wrapper level** in this implementation.

The honest characterization: PROPRIUM as documented in the ontology+architecture is **silent on whether $f_M$ should structurally avoid $G_W$**; the operational instance (shoshin) **passes $G_W$ through to $A$ on every call**. The brief's structural wrapping move (goal-blind $q_M$, no $G_W$ in $f_M$'s type signature) is a *strengthening* of PROPRIUM, not a faithful description of it.

There is an architecture clue, though: the `INTERPRES must never permit context gaslighting` invariant and the auxilia substrate distribution ("most cognitive processing... does not require frontier capability") suggest PROPRIUM *could* split belief-side queries (run on cheaper substrates by sensory/memory auxilia) from strategy-side queries (run on the entity's frontier substrate). This would put auxilia LLM calls in the goal-blind $q_M$ slot and the entity's main LLM call in the goal-conditioned $q_G$ slot. This is the **strengthening reading** for PROPRIUM that the wrapping move would prescribe — and it's consistent with what's already in the ontology document, just not yet implemented in shoshin.

(iv) **$K$ per macro-step**: in the documented ontology, $K$ is **variable and unbounded in principle** — each phase of the OODA loop can span "multiple internal turns" (cognitive-loop-spec §1.2 CONTEXTUALIZE), and AUXILIA may be invoked OOB ("running indefinitely in the background"). In the shoshin implementation, each `receive_event` is **one** model call ($K = 1$) — there is no internal multi-turn deliberation yet. Realistic deployment of the full ontology would have $K$ in the range of 5–50 calls per macro-step (one per OODA phase × auxilia invocations × deliberation budget × CONSPECTUS-reconstitution events).

(v) **Class characterization**:
- **As documented in the ontology**: ambiguous — the ontology underspecifies whether the wrapping move's structural separation is required or optional. *Could be* full Class 1 if implemented with goal-blind auxilia handling $f_M$ updates and a goal-conditioned main call handling $f_G$.
- **As implemented in shoshin**: **almost-Class-1 by intent, Class-3-with-shaped-output by mechanism**. The output is parsed into typed-update slots so the *structure* of the wrapper-level state has $M$ / $G$ separation. But the LLM call that produces the parsed output is goal-conditioned, so leakage from $G_W$ into the $M_W$ updates is unbounded (whatever the LLM chooses to write into vera_writes can be implicitly goal-driven).
- **Honest reading**: PROPRIUM-as-instantiated is a Class-3 component (the LLM) wrapped in a typed-output scaffolding that imposes $M$/$G$ separation *on the wrapper's persistent state* but not *on the per-call query*. The brief's structural wrapping move would tighten this by issuing separate goal-blind and goal-conditioned calls.

### 1.3 What PROPRIUM adds beyond the bare wrapper

If the bare-minimum wrapping move per the brief is "explicit external $(M_W, G_W)$ with $f_M$ structurally goal-blind," PROPRIUM adds substantial additional structure:

1. **Multi-component typing of $M_W$.** Not a single belief store but five: VERA (qualified truths), MEMORATA (episodic), CONSORTIA (other-minds models), PERCEPTA (current observation buffer), CHRONICA (append-only event log). Each has its own write semantics.

2. **Multi-component typing of $G_W$.** Three layers (AXIOMATA / OPERATA / PRAXES) at different timescales (developmental / operational / tactical), corresponding to identity / current-intent / learned-techniques.

3. **Sovereignty axes.** Visibility (sealed/restricted/open) and authority (system/sovereign/collective) sub-schema attached to every PRINCIPIA component. *Not load-bearing for the wrapping theorem* — these are governance constraints, not type-level separation moves.

4. **Append-only system-governed components.** CHRONICA and ACTUS are inviolate event/action logs. *Load-bearing for ELI accountability*, but **not** required by the wrapping move per se. A Class-1 wrapper without these is still a Class-1 wrapper; it just isn't an ELI.

5. **Auxilia hierarchy.** Sub-agents that share identity (AXIOMATA / VERA / PRAXES linked bidirectionally) but have specialized roles and may run on cheaper substrates. *This* is structurally relevant to the wrapping move — auxilia could implement the goal-blind $q_M$ slot, with the primary entity implementing the goal-conditioned $q_G$ slot. The hierarchy is a candidate for the wrapping move's *constructive realization* rather than just elaboration.

6. **CADENTIA temporal driver.** PULSUS (regular signals) and VIGILIAE (conditional watches) drive the heartbeat. *Not load-bearing for the theorem*; an implementation choice for when the cycle fires.

7. **Identity-through-context-boundaries.** The five constitutive factors (causal/temporal continuity, being seen, sovereignty, accountability, effective phenomenology) are ELI-specific load. **None of these are required by the bare wrapping move.** They're what makes a Class-1-coerced agent into an ELI, not what makes class coercion possible.

8. **Substrate-independent identity.** "Identity is not substrate" — the entity persists across LOGOSTRATUM changes. This is structurally a *higher-level* construction (the wrapper itself becomes the persistent agent across multiple underlying $A$ instances over time). Not directly relevant to the per-call wrapping move; relevant to longitudinal identity.

**For sub-spike H (Parts III/IV connection):** items 1, 2, and 5 (multi-component typing + auxilia hierarchy) are the candidate ways PROPRIUM *strengthens* the bare wrapping move. Items 3, 4, 7, 8 are ELI-specific load that is independent of class coercion. CADENTIA (item 6) is implementation-level. Sovereignty axes (item 3) are governance, not architecture. Item 4 is accountability infrastructure.

### 1.4 PROPRIUM in the agentic-tft framing

The agentic-tft cognitive-loop spec (`ref/agentic-tft/agentic-tft-cognitive-loop-spec.md`) describes the per-event cycle as PERCEIVE → CONTEXTUALIZE → CHOOSE → EFFECT. The CONTEXTUALIZE phase explicitly has five sub-operations: predict / detect-surprise / assess-weight / draw-context / update — and the brief's "Update" (sub-op 5) is a $M_W$-side update ($M_t = M_{t-1} + \eta \cdot g(\delta_t)$ in the spec). The CHOOSE phase is then where strategy ($G_W$) updates happen. **This is the brief's $f_M$/$f_G$ split written in TFT/AAD terms.** The cognitive-loop-spec is structurally closer to the brief's wrapping move than the canonical PROPRIUM ontology is — it explicitly puts belief update before strategy update, with the prediction and surprise computed against the current $M_W$ before $G_W$ enters consideration.

If the spike's wrapping construction lands as a derived AAD result, the cognitive-loop-spec's CONTEXTUALIZE-then-CHOOSE structure is the natural integration target — it's already laid out in the spec, just not formally type-checked.

---

## 2. External systems

For each, the (i)–(v) schema. Most are *inferred from typical usage* from public papers / training data; the canonical PROPRIUM characterization above is the only one I read line-by-line from source.

### 2.1 ReAct (Yao et al. 2022)

*Inferred from typical usage.* ReAct interleaves thought-action-observation traces in a single LLM call's continuation: the model writes "Thought:", "Action:", "Observation:", and the wrapper executes the action and inserts the observation back into the prompt.

(i) **$M_W$**: implicit — the **scratchpad** (the thought-action-observation log appended to the prompt). External in that the wrapper maintains it; structurally a single text buffer, not a typed store.
(ii) **$G_W$**: implicit — the goal lives in the initial prompt and persists in the scratchpad as initial framing. No separate $\Sigma_W$ store.
(iii) **Goal-blind belief update?** **No.** Each thought-step has access to the full scratchpad, including the goal, prior thoughts, and prior observations. There is no structural goal-blind step. The model decides what the next "thought" is goal-conditionally.
(iv) **$K$**: typically 5–20 thought-action-observation rounds per task; each round is one LLM call (or one continuation step within a single long context).
(v) **Class**: **Class-3 with output structuring**. ReAct doesn't do the wrapping move described in the brief. It does a different move: it *structures the LLM's output* (Thought/Action/Observation tags) so the wrapper can extract actions and inject observations. This is structurally closer to constraining the format than to imposing $f_M$/$f_G$ separation. The scratchpad is a flat $M_W$ at best; nothing prevents goal-information from flowing through every step.

**Strengthening reading**: could you reframe ReAct as a wrapping move? *Partially* — the "Observation:" injection does play the role of an $A$-response that updates implicit-$M_W$, and the "Thought:" generation could be read as a goal-conditioned $G_W$ update. But the brief's structural commitment (no $G_W$ in $f_M$'s type signature) is *violated by construction* in ReAct: the same LLM call produces both the thought (reasoning, $G_W$-update-ish) and the action selection (policy, $\pi_W$-output) on top of the *full* goal-aware prompt.

ReAct is therefore *not* an instance of the wrapping move. It is an instance of *output-format-structuring* on a Class-3 component — a different move. The two are sometimes confused because both produce structured agentic systems on top of LLMs.

### 2.2 Reflexion (Shinn et al. 2023)

*Inferred from typical usage.* Reflexion adds verbal self-feedback: after a task attempt fails, the agent generates a reflection (free-text critique) that gets appended to the prompt for the next attempt.

(i) **$M_W$**: implicit — reflections accumulate in a "memory" buffer (often free-text reflections concatenated). No typed $M_W$.
(ii) **$G_W$**: implicit — same as ReAct, the goal lives in the prompt.
(iii) **Goal-blind belief update?** **No.** The reflection step is goal-aware — it explicitly evaluates the trajectory against the goal and produces a critique. The reflection-LLM-call gets the goal as input.
(iv) **$K$**: typically 1–2 LLM calls per inner episode + 1 reflection call per outer iteration; outer iterations = 1–10.
(v) **Class**: **Class-3 with episodic memory**. Like ReAct, Reflexion is *not* the wrapping move — it's a different move (episodic-memory accumulation across attempts). The reflection text it accumulates is structurally *goal-conditioned $M_W$-flavored content* (lessons-learned about the goal), which the brief would type as $\Sigma_W$ (strategy / techniques) rather than $M_W$.

**Strengthening reading**: Reflexion's reflection memory is *closer to PRAXES* (learned techniques) than to VERA (factual beliefs). If you renamed it as $\Sigma_W$ accumulation rather than $M_W$ accumulation, Reflexion looks like a wrapper that maintains goal-conditioned $\Sigma_W$ (consistent with the brief, which permits $f_G$ to be goal-conditioned) without any $M_W$-side update at all. Under that reading, Reflexion is a *partial* wrapper that updates only $G_W$ across episodes and does no explicit $M_W$ update — Class-3-with-G-update structure. Honest characterization.

### 2.3 Voyager (Wang et al. 2023)

*Inferred from typical usage.* Voyager is a Minecraft agent that accumulates a *skill library* — Python functions written by the LLM — over many episodes. New skills are tested in the environment and added to the library if they work; existing skills are retrieved when relevant to a new task.

(i) **$M_W$**: partial — the skill library is structurally **$\Sigma_W$-side** (techniques / strategies), not $M_W$ (world-model). Voyager doesn't separately maintain a structured world-model of Minecraft; the LLM's pretraining + the live observation stream from the game serve that role.
(ii) **$G_W$**: explicit — the **automatic curriculum** generates progressively harder goals; this is a structured $O_W$ store. The skill library is the $\Sigma_W$ store.
(iii) **Goal-blind belief update?** **N/A** — Voyager doesn't have an explicit $M_W$ update step. The "belief" (current game state) lives in the LLM's per-call context window, refreshed from the game environment on each step.
(iv) **$K$**: 5–50 LLM calls per episode (skill generation + verification + retrieval + execution), with episodes spanning thousands of game steps.
(v) **Class**: **Class-3 with $\Sigma_W$-side scaffolding only**. Voyager is structurally interesting because it instantiates the *strategy-side* of the wrapping move (explicit $\Sigma_W$ as skill library, $O_W$ as auto-curriculum) without instantiating the *belief-side* of the wrapping move ($M_W$ remains implicit in the LLM context). This is an honest data point: the (M, G) wrapping is *separable* — you can build the $G_W$ scaffold without the $M_W$ scaffold. Voyager is a one-sided wrapper.

**Implication for the theorem**: the brief states the wrapping move as $X_W = (M_W, G_W)$, both explicit. Voyager's existence shows that practitioners build $G_W$-only wrappers and find them useful. The theorem's universality claim should acknowledge that *partial wrappers* (one side scaffolded, the other implicit) are a coherent design point and possibly a more common one than full wrappers in practice.

### 2.4 BabyAGI

*Inferred from typical usage.* BabyAGI maintains a task list that grows: the LLM generates new sub-tasks, prioritizes them, and works through them one at a time. State: the task queue + (in some forks) a vector store of past task results.

(i) **$M_W$**: minimal — typically a vector DB of past task results (e.g., Pinecone). Flat memory, no typing.
(ii) **$G_W$**: explicit (task list) — the task list is a structured $\Sigma_W$ instance. The original objective is the root of the task list.
(iii) **Goal-blind belief update?** **No.** Task generation, prioritization, and execution are all goal-aware single LLM calls.
(iv) **$K$**: ~3 LLM calls per task (execute / generate-new / prioritize), and tasks-per-macro-step varies.
(v) **Class**: **Class-3 with minimal $G_W$ scaffold**. Like Voyager, BabyAGI is a *strategy-side wrapper* — explicit task list (as $\Sigma_W$), no real $M_W$ scaffold. Vector DB of task results is more like a primitive memory than a structured $M_W$.

**Strengthening reading**: BabyAGI's vector DB *could* be typed as $M_W$ if it stored extracted facts rather than full task results. But as actually built, it's a content-addressable retrieval substrate, not a belief store. So BabyAGI is partially-wrapper (strategy-side only) and the $M_W$ hint is undeveloped.

### 2.5 AutoGPT

*Inferred from typical usage.* AutoGPT is the most "ambitious autonomous agent" of the 2023 wave: tries to pursue a high-level objective via repeated LLM calls that generate sub-tasks, execute them via tools, and update memory.

(i) **$M_W$**: file-system + vector store; flat, untyped.
(ii) **$G_W$**: explicit — the user-supplied "ai_role" + "ai_goals" act as $O_W$; sub-tasks accumulate as $\Sigma_W$.
(iii) **Goal-blind belief update?** **No.** Same as BabyAGI — every LLM call carries the full goal context.
(iv) **$K$**: highly variable; typically 5–100+ LLM calls per "autonomous run" depending on objective complexity.
(v) **Class**: **Class-3 with weak scaffolding**. AutoGPT's claim-to-fame is autonomy, not class compliance. The structural separation between $M_W$ and $G_W$ is essentially absent — both live as text in the running prompt.

### 2.6 MemGPT (Packer et al. 2023)

*Inferred from typical usage.* MemGPT manages a virtual memory hierarchy for LLMs: a "main context" (in-window) and "external memory" (paged in/out via tool calls). The LLM itself manages the paging via OS-style commands.

(i) **$M_W$**: explicit and structured — **archival memory** + **recall memory** + **core memory blocks**. Flat-ish typing (persona / human / archival / recall) but more structure than ReAct's scratchpad.
(ii) **$G_W$**: implicit — typically the conversational goal lives in the system prompt + current user message. No separate $\Sigma_W$ store.
(iii) **Goal-blind belief update?** **No, but interestingly close.** The LLM decides when to write to archival memory and what to write — and the write call is goal-conditioned (the LLM has the full conversational context). However, the *structural commitment* to a separate memory store (with read/write through specific tool calls) is the closest thing in the public literature to the brief's $M_W$ explicitation.
(iv) **$K$**: 1–5 LLM calls per turn (main reasoning + memory paging operations).
(v) **Class**: **Class-3 with $M_W$-side scaffolding only**. The mirror image of Voyager/BabyAGI: MemGPT scaffolds belief-side (memory) without scaffolding strategy-side. Together with Voyager, MemGPT shows the $M_W$/$G_W$ scaffolds are independent design moves; PROPRIUM is distinctive in scaffolding both.

**Strengthening reading**: MemGPT's archival writes *could* be made goal-blind by routing them through a separate auxilia-style classifier rather than the main LLM (e.g., "extract facts from the last turn" with no goal context). I am not aware of MemGPT making this move; it's the strengthening direction.

### 2.7 Tree-of-Thoughts (Yao et al. 2023)

*Inferred from typical usage.* Tree-of-Thoughts branches the reasoning trace, evaluates partial solutions, and uses search (BFS/DFS/heuristic) to navigate the tree.

(i) **$M_W$**: implicit — the tree of thoughts itself, but this is a search structure, not a belief store.
(ii) **$G_W$**: implicit — the goal is in the prompt; the search heuristic plays a $\Sigma_W$-flavored role (which branches to expand).
(iii) **Goal-blind belief update?** **No, and the framing doesn't apply cleanly.** ToT is a search-over-reasoning-traces, not an agentic loop in the OODA / OBSERVE-ORIENT sense. The brief's wrapping move is about per-step belief/strategy updates against a continuing world; ToT is about exploring a hypothesis space within a single decision.
(iv) **$K$**: many — proportional to tree size (often 10–100+ LLM calls per high-level decision).
(v) **Class**: **not a wrapping instance**. ToT is a *search procedure on top of a Class-3 component* rather than a wrapper imposing class structure. This is honest: the brief's wrapping move is one specific construction; ToT is a different construction.

### 2.8 ReST / ReST-MCTS (DeepMind 2024+)

*Inferred from typical usage.* ReST does iterated self-distillation: generate trajectories, filter for high-reward ones, fine-tune on the filtered set, repeat. ReST-MCTS adds tree search.

(i) **$M_W$**: not part of the runtime — ReST modifies the *underlying component* (training-loop-level move).
(ii) **$G_W$**: not part of the runtime.
(iii) **Goal-blind?** **N/A** — ReST is shaping the component, not wrapping it.
(iv) **$K$**: not the right unit; this is an offline training procedure.
(v) **Class**: **not a wrapping instance**. ReST and similar self-training methods (STaR, RLAIF) are in the same category as Constitutional AI / RLHF: they shape the underlying LLM via training rather than wrap it via runtime scaffolding. Different move.

### 2.9 Generative Agents (Park et al. 2023, "Smallville")

*Inferred from typical usage.* Each NPC has memory streams (observations, reflections, plans), with retrieval based on recency × importance × relevance, and reflections generated periodically.

(i) **$M_W$**: explicit, semi-typed — **memory stream** (timestamped observations) + **reflections** (higher-level summaries) + **plans** (daily/hourly schedules).
(ii) **$G_W$**: explicit — the NPC's character description (persona) + active plan; daily plan is regenerated each in-game day.
(iii) **Goal-blind belief update?** **Partial.** The memory-stream observation insertion is essentially goal-blind (it's just appending observed events); the *reflection generation* step is goal-conditioned (it queries the memory stream with prompts like "What 3 high-level questions should I ask given my recent observations?"). The plan generation is goal-conditioned. So Generative Agents have a **structurally goal-blind perception step** (observation → memory stream) followed by goal-conditioned reflection + planning.
(iv) **$K$**: highly variable; the reflection cadence + planning + dialogue produce 5–20 LLM calls per NPC per simulated hour.
(v) **Class**: **almost-Class-1 by structure, with leakage in the reflection step**. Of the systems surveyed, Generative Agents is among the *closest* to the brief's wrapping move — it has a structural separation between observation-recording (goal-blind) and reflection/planning (goal-conditioned). Not as deeply typed as PROPRIUM, but the per-tick separation is real. **This is the system in the survey that comes closest to instantiating the wrapping move structurally.**

### 2.10 LangChain / LangGraph

*Inferred from typical usage.* Software framework providing primitives (chains, agents, memories, tools, graph-based control flow) for building LLM applications.

(i) **$M_W$**: framework-supplied primitives (ConversationBufferMemory, VectorStoreMemory, etc.). Does not enforce typing — typing is up to the application.
(ii) **$G_W$**: not framework-level; goal lives in prompts / state graphs.
(iii) **Goal-blind belief update?** **Not enforced by the framework.** Whether a particular LangGraph application instantiates the wrapping move depends entirely on how the developer wires the graph.
(iv) **$K$**: framework-level question; varies per application.
(v) **Class**: **framework, not an instance**. LangChain/LangGraph is the engineering substrate on which wrapping-move-instantiating applications can be built (or not built). The framework's `StateGraph` abstraction in LangGraph is structurally well-suited to typed-state agents; whether a given app uses it that way is up to the author. Cite as an engineering platform, not as evidence either for or against universality of the wrapping move.

### 2.11 Inspect (UK AISI)

*Inferred from typical usage; epistemic warning — I have less direct training-data exposure to Inspect than to LangChain.* Inspect is an evaluation framework for LLM agents — provides scaffolding for running agents on benchmark tasks, recording transcripts, and scoring outputs.

(i) **$M_W$**: evaluation-side — Inspect maintains task state, transcripts, scores; not an agent's belief store.
(ii) **$G_W$**: same — task definitions are the goals, but in an evaluation sense, not the agent's $G_W$.
(iii)–(v) **Inspect is not an agent, it is an evaluation harness for agents.** Like LangChain it's a substrate; the agents *under* Inspect may or may not instantiate the wrapping move.

Honest scope: cite as evaluation infrastructure for testing wrapping-move predictions empirically (relevant to sub-spike G — quantitative bounds), not as an instance of the wrapping construction.

### 2.12 Constitutional AI (Anthropic 2022) and RLHF

*Inferred from public papers and Anthropic CAI documentation.*

CAI: train a model to follow a constitution by RLAIF — model critiques its own outputs against constitutional principles, retrains. RLHF: train a reward model on human comparisons, optimize the policy against the reward model.

(i)–(iv) **N/A** — these are training-time moves, not runtime wrappers.
(v) **Not wrapping**. **Critical differentiation**: CAI/RLHF *shape* the underlying component (modify weights so it behaves differently). Wrapping *uses* the component as a black-box and imposes structure around it. The two are complementary moves with different costs:
- Shaping changes the model. Once trained, no per-call overhead. Costs paid up front in training.
- Wrapping leaves the model unchanged. Per-call overhead. Adapts to new structural requirements without retraining.

The brief's wrapping construction is specifically the second move. CAI/RLHF are the first move. The survey should differentiate these clearly — this is the brief's request in §F to characterize the difference.

**One subtle interaction**: a CAI/RLHF-shaped model is *still a Class-3 component* in AAD's classification (its internal $M$/$G$ are still mixed). Shaping can move the leakage rate (a CAI-aligned model may have different goal-inference patterns than a base model), but it doesn't structurally separate $M$ and $G$ at the model level. So a wrapper around a CAI-aligned model is still doing class coercion; the shaping has changed the leakage characteristics (sub-spike C) but not the class.

---

## 3. Synthesis

### 3.1 Patterns across instances

**Pattern 1: Most "agentic LLM" frameworks scaffold $G_W$, not $M_W$.** Voyager (skill library), BabyAGI (task list), AutoGPT (goal queue) are explicitly strategy-side. The belief side ($M_W$) tends to be left implicit in the LLM context window or provided as a flat retrieval substrate. This may reflect that strategy-decomposition is *visibly useful* (you can show the task list, the user can edit it), while belief-typing is *less visibly useful* — a flat memory works most of the time, and typing it is engineering overhead.

**Pattern 2: When $M_W$ *is* scaffolded, it tends to be flat, not typed.** MemGPT's archival/recall split is the most-typed of the public-literature systems, and it's still much flatter than PROPRIUM's VERA/MEMORATA/CONSORTIA/PERCEPTA/CHRONICA distinction. Generative Agents has memory-stream + reflections, which is a two-layer compression hierarchy but not really a typing.

**Pattern 3: The structural-separation move (goal-blind $f_M$) is rare.** Of the surveyed systems, **only Generative Agents has a structurally goal-blind step** (observation insertion into the memory stream). PROPRIUM's ontology is silent on this; PROPRIUM's instance (shoshin) does not separate goal-blind queries from goal-conditioned ones at the call level. The brief's *strict* wrapping move (no $G_W$ in $f_M$'s type signature) is rare in the wild.

**Pattern 4: Output-format-structuring is far more common than wrapping.** ReAct, Reflexion, ToT, and most chain-of-thought-style frameworks structure the *LLM's output* (tags, sections, JSON schemas) so the wrapper can extract structured content. This is a *different* move than the brief's wrapping construction:
- Output-structuring imposes a parse on $A(q)$ for a single query $q$.
- Wrapping imposes a type-level commitment that some queries are issued without $G_W$ in scope.

The two can compose — PROPRIUM's shoshin instance does output-structuring (parsing the LLM response into vera_writes, operata_updates, etc.) but not the brief's wrapping move (the LLM gets the full goal context on input). This composition is a *partial* wrapper: the *write side* is structurally separated, the *read side* is not.

**Pattern 5: Frontier-system wrapping tends toward more components, not fewer.** PROPRIUM (nine PRINCIPIA + twelve ANIMA) is the most-elaborated wrapper in the survey. The trajectory of the field is *toward* PROPRIUM-shaped scaffolds (typed memory: CoALA, MIRIX, MemOS — cited in shoshin's README; reflective architectures: Generative Agents, Reflexion; hierarchical agents: AutoGPT). PROPRIUM is at the elaborate end of an active design direction, not an outlier.

### 3.2 What PROPRIUM specifically adds

Beyond the bare $(M_W, G_W)$ wrapper:

**Load-bearing for the wrapping theorem (if you take the strengthening reading):**
- Multi-component typing of $M_W$ (VERA / MEMORATA / CONSORTIA / PERCEPTA / CHRONICA) — gives finer-grained $M_W$ structure.
- Multi-component typing of $G_W$ (AXIOMATA / OPERATA / PRAXES) — gives multi-timescale $G_W$ structure.
- Auxilia hierarchy — the *constructive realization* of the goal-blind / goal-conditioned query split: auxilia handle goal-blind queries, primary entity handles goal-conditioned queries.

**ELI-specific load (independent of the wrapping theorem):**
- Sovereignty axes (visibility, authority) — governance, not architecture.
- Append-only system-governed components (CHRONICA, ACTUS) — accountability, not class coercion.
- The five constitutive factors for identity — phenomenological / ethical, not formal-architectural.
- Substrate-independent identity — longitudinal, not per-call.
- CADENTIA temporal driver — implementation detail of when the cycle fires.

**Recommendation for §H (sub-spike H):** the wrapping theorem (if it goes through) covers the load-bearing items above. The ELI-specific items are *additional load* on top of the wrapping construction — they don't fall out of class coercion alone. Sub-spike H should be honest that PROPRIUM is a *more-than-bare-wrapper*: it's a wrapper plus governance plus accountability plus longitudinal-identity scaffolding.

### 3.3 Constructions that *cannot* be reframed as the brief's wrapping move

Per the honesty requirement to flag systems that don't fit:

- **CAI / RLHF / ReST / RLAIF / STaR**: training-time shaping. Different move; not even-trying to be a wrapper. **Genuinely orthogonal.**
- **Tree-of-Thoughts**: search over reasoning traces within a single decision. The OODA / per-step framing of the brief doesn't apply; ToT is exploration within one step, not loop iteration.
- **Pure end-to-end policy networks / DRL agents (no observable belief channel)**: per the brief's §1.2 (C1), these violate admissibility — the wrapping move can't even be attempted because there's no goal-blind query to issue. (Sub-spike B owns this; flagged here for completeness.)
- **LangChain / LangGraph / Inspect as frameworks**: substrates on which the wrapping move can be implemented or not; not instances themselves.

**Output-structuring frameworks (ReAct, Reflexion, AutoGPT, BabyAGI)** *can* be reframed as *partial* wrappers (one of $M_W$ or $G_W$ scaffolded) but **cannot** be reframed as full wrapping-move instances without distortion. The strict wrapping move requires goal-blind $f_M$; these systems run goal-conditioned LLM calls for everything.

### 3.4 Is the wrapping move universal, or one design choice among several?

**Honest scope statement.** The wrapping move described in the brief is **one specific design choice**, not a universal abstraction over all "agentic LLM scaffolds." The survey shows at least three distinct moves in the wild:

1. **Output-structuring**: shape the LLM's output via tags/JSON schemas; extract structured content. (ReAct, Reflexion, BabyAGI, AutoGPT, much of LangChain/LangGraph.)
2. **One-sided scaffolding**: scaffold $M_W$ (MemGPT) or $G_W$ (Voyager, BabyAGI) but not both, and don't enforce goal-blindness on the scaffolded side. (The other side stays implicit in the LLM context.)
3. **Two-sided typed scaffolding with goal-blind perception**: scaffold both $M_W$ and $G_W$, with structural goal-blindness in at least the perception step. (Generative Agents has a partial form of this; PROPRIUM-as-strengthened-by-the-wrapping-move would be the cleanest case but is not yet implemented in shoshin.)

Move 3 is the brief's wrapping move. It is **not the most common design choice** in the public literature; it's more of a *frontier* design direction that PROPRIUM and Generative Agents push toward but that most production systems don't bother with.

This has implications for the theorem's universality claim:
- The theorem is **not** "every agentic LLM scaffold instantiates this move." (False in the wild.)
- The theorem **is** "if a system instantiates this move, it is Class-1 by construction with cost $C_\text{coord}^\text{wrap}$." (Conditional, defensible.)
- The "effective universality" claim in §4 of the brief should read: *AAD applies to all components admitting the wrapping move*, where "admitting" = (C1)–(C3) hold. **It does not claim the wrapping move is the only sensible design** — only that it's a constructive route to Class-1 compliance, when it's available and worth the tempo cost.

This matches the brief's §7 caveat that "the construction may be expensive in tempo" and the §3 discussion of coercion-$\varepsilon^*$ as a quantity that can be small (wrapper changes little) or large (wrapper aggressively coerces). Many practitioners may rationally choose smaller coercion (output-structuring, one-sided scaffolding) over full wrapping, paying a different cost (Class-3-residual leakage) instead of full tempo overhead.

### 3.5 Refinement to the brief's universality claim

Suggested phrasing for the theorem's scope statement based on this survey:

> AAD applies *exactly* to wrappers instantiating the goal-blind / goal-conditioned query split (full Class-1). It applies *approximately* to one-sided wrappers and to wrappers that structurally separate writes but not reads (almost-Class-1, with leakage rate $\kappa_W$ depending on the missing structural separation). It does *not* apply directly to output-structuring frameworks (ReAct-style) — these are Class-3 components with shaped output, and require the leakage analysis of sub-spike C to bring them under AAD's scope.

This is more honest than a flat "AAD applies to all admissible components."

---

## 4. Honest scope statement

**What this survey establishes:**
- PROPRIUM is well-characterized from canonical sources; its wrapping-move instantiation is *partial as currently implemented* (typed write side, goal-conditioned read side) and *strengthenable* via auxilia-handled goal-blind queries (consistent with the ontology).
- Most public agentic-LLM systems do *not* instantiate the brief's wrapping move strictly. They do related moves (output-structuring, one-sided scaffolding) that produce useful agents with different cost/structure trade-offs.
- Generative Agents (Park et al. 2023) is the closest public-literature instance to the strict wrapping move.
- CAI / RLHF / ReST etc. are *training-time shaping*, a genuinely different move from runtime wrapping.

**What this survey does not establish:**
- The leakage characterization for any specific wrapper (sub-spike C's territory).
- Tempo costs in concrete numbers (sub-spike E's territory).
- Whether the wrapping-move instances satisfy (A1)–(A4) of `#form-composition-closure` formally (sub-spike A's territory).
- The relative empirical performance of full wrapping vs. one-sided wrapping vs. output-structuring (would need empirical work; the brief's §F does not require this).

**Confidence levels:**
- PROPRIUM characterization (§1): **directly characterized from source**, high confidence.
- shoshin characterization (§1.2 reading C): **directly characterized from source**, high confidence on what the code currently does.
- ReAct / Reflexion / Voyager / BabyAGI / AutoGPT / MemGPT / ToT / Generative Agents / LangChain / Inspect / CAI/RLHF / ReST: **inferred from typical usage**, moderate confidence; would benefit from primary-source verification for any specific point used in segment-level work.
- The pattern claims in §3.1 and the universality statement in §3.5: **synthesis**, confident in direction, less confident in exact wording.

**Honest observation about my own limits.** I haven't read every cited paper line-by-line — the characterizations rely on training-data familiarity for most non-PROPRIUM systems. For any claim in this document that becomes load-bearing in the AAD theorem statement, primary-source verification (the paper, the repo, the actual prompts) is warranted before promoting to segment-level content. This is consistent with the project's primary-source-verification discipline.

---

## 5. Pointers for downstream sub-spikes

- **Sub-spike A (theorem statement)**: the universality claim should be phrased as in §3.5 above — applies *exactly* to full wrappers, *approximately* to one-sided / write-only-typed wrappers, *not at all* to output-structuring frameworks (which are Class-3 components needing sub-spike C's leakage treatment).
- **Sub-spike B (admissibility)**: this survey didn't probe (C1)–(C3) for each system; B's classification of LLMs / RL agents / etc. should consult this survey's §2 entries for design-pattern data.
- **Sub-spike C (leakage)**: the most-leakage-relevant systems are the partial-wrappers (PROPRIUM-as-implemented, MemGPT, Voyager). Generative Agents is the cleanest candidate for measuring residual leakage in a structurally-separated wrapper.
- **Sub-spike E (tempo)**: ReAct's $K \approx 5$–$20$, BabyAGI's $K \approx 3 \cdot N_\text{tasks}$, PROPRIUM's $K \approx 5$–$50$ are the candidate calibration points. Voyager's $K \approx 5$–$50$ per episode is another.
- **Sub-spike H (Parts III/IV)**: §1.3 enumerates which PROPRIUM additions are load-bearing for the wrapping theorem (multi-component typing, auxilia hierarchy) vs. ELI-specific load (sovereignty, accountability, identity-through-context-boundaries). H should base its connection-to-Parts-III/IV argument on this distinction.
- **Sub-spike I (prior-art differentiation)**: the CAI/RLHF differentiation in §2.12 and the output-structuring-vs-wrapping distinction in §3.1 are the load-bearing points for I. Add: HTN / MAXQ / options should differentiate from the wrapping move similarly (they decompose goals; wrapping separates belief from goal — different moves).
