# Spike: Substrate-modifying actions — fifth action class, or recursive meta-action over the existing four?

**Status.** Exploratory spike. Working result: *neither* of the framing's two options as originally stated holds without qualification. *Modify the language* is most cleanly analyzed not as a fifth peer-class to the four named action classes of `#scope-developer-agent`, and not merely as a recursive meta-action over them, but as a structurally distinct *substrate-modifying* action class whose distinguishing feature is that it changes the **legibility metric** on the action space rather than the action space's underlying state or extension. The legibility metric is what bounds the developer agent's reachable region of $\Omega$ per macro-step under finite tempo and finite comprehension budget. Substrate-modifying actions are bounded-rationality actions over the agent's own *cost-to-express* function. The macro-hygiene system is then a recognizable instantiation of the wrapping construction `#der-class-coercion-via-wrapping` at the language layer — McCord's restraint principle is the discipline-level statement that the wrapping pays off only sparingly, mapping directly onto the strict-vs-partial regime distinction.

**Date.** 2026-05-21.

**Pressure point.** The Elixir-composite mining (`spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` C1) and the TST-IDEAS substrate (`TST-IDEAS.md` §C3) jointly surface the structural claim: `#scope-developer-agent` currently names four action classes — exploration, interventional probes, queries, environment modification — and "modify the language" sits *below* all four. For AI-coding agents, this is the dominant axis of action-space expansion: a generative AI's effective action space grows substantially when the language gives it macros / DSLs / metaprogramming tools that let it express complex transforms compactly. The mining flagged it as new ground — no current AAT or TST segment has formalized this — and called for spike-grade theory work to resolve whether substrate-modification is structurally a *fifth action class* peer to the four named ones, a *recursive meta-action* that touches the other four, or something else.

This spike works the question to a structural resolution sufficient to scope a segment proposal (which is held back as deliberate spike-grade output rather than canonized here).

---

## 1. What the four named action classes actually are

Per `#scope-developer-agent` §Action space, the four classes are distinguished by *purpose*, not by what they touch:

1. **Exploration** — directed attention to generate observations. Reads, traces, history browses. Purpose: build $M_t$, not modify $\Omega_t$.
2. **Interventional probes** — actions that *temporarily perturb* $\Omega_t$ to learn from the response. Tests, print statements, speculative changes. These are $do(\cdot)$ operations per `#def-pearl-causal-hierarchy`; per `#def-causal-information-yield`, they admit positive CIY.
3. **Queries** — accessing pre-compressed external models. Colleague, documentation, AI assistant. The source has already performed the IB compression `#form-information-bottleneck`; the response transfers compressed output.
4. **Environment modification** — changing $\Omega_t$. Writing code, modifying configuration, deploying. A subset are *observation-infrastructure investments* — they modify $\Omega_t$ to improve future observation quality.

The four-way partition is not exhaustive (the segment itself flags that "reading code does not modify $\Omega_t$" while "running tests modifies $\Omega_t$ temporarily" and "speculative compile-check is both") — it is a *useful organizing taxonomy*, not a formal partition. That qualifier matters here: the question is not whether substrate-modification breaks a clean partition (no clean partition existed) but whether it has structure the existing four classes do not collectively capture.

Each of the four classes operates over the same formal action space $\mathcal{A}$ via the same transition $T(\cdot \mid \Omega_t, a_t)$ from `#def-action-transition`. The distinguishing axis is *what part of the agent's state the action is undertaken to update* — $M_t$ (classes 1–3) versus $\Omega_t$ (class 4). Class 4 is the only one with a primary side-effect on $\Omega$; classes 1–3 have $\Omega$-effects that are either zero (exploration), temporary (probes), or indirect (the query channel passes through another agent's environment).

## 2. What *modify the language* concretely is

The Elixir-composite mining substrate covers macros, DSLs, compile-time code generation, AST walking, and the macro-hygiene system (analyses 091, 092, 093, 094, 096, 061, 400, 369). The structural shape consistent across these:

- **The substrate change is in $\Omega_t$.** Adding `defmacro assert_value(quoted) do … end` is a write to a `.ex` file. By the four-class taxonomy of §1, this is straightforwardly class 4 — environment modification.
- **The consequence is on the agent's future expressiveness.** After the macro is defined, sequences like `assert_value foo == 3` are legible to the compiler and to readers as one-step invocations; without the macro, the same effect requires the developer to write the expanded form by hand. The *cost per use* drops.
- **The legibility cost composes.** A library of macros — `with`, the `defprotocol` family, the `Ecto.Query` DSL, `ExUnit`'s assertion macros — accumulates a vocabulary the developer-agent can deploy. Each new macro reduces the surface-level token count for a class of operations.
- **The hygiene system is structural.** Elixir's macro expansion is *hygienic by default* — variables introduced inside a macro body are scoped to the expansion and do not capture the caller's bindings unless the macro explicitly opts in via `var!`. Hygiene violations are restricted to a typed, named pathway. McCord's *macro restraint principle* (analysis 096) — *macros only when functions cannot achieve the same outcome* — is the discipline-level statement of where the construction pays off.

These four observations are the substrate for the structural analysis below.

## 3. The framing question stated formally

Per `#def-action-transition`, the agent has an action space $\mathcal{A}$, environment state $\Omega_t$, and stochastic transition $T(\Omega_{t+1} \mid \Omega_t, a_t)$. Let $a^\text{sub}$ denote a substrate-modifying action (define a macro, add a DSL operation, add a protocol implementation). The framing question, made formal:

**Reading R-state.** *Substrate-modification is just $\Omega$-state modification.* The macro definition is a string in a file; the language's grammar plus the compiler is part of $\Omega$; the post-action environment $\Omega_{t+1}$ contains the new macro definition; this is exactly $T(\Omega_{t+1} \mid \Omega_t, a^\text{sub})$ with $a^\text{sub}$ as an environment-modification action. No new class needed; class 4 absorbs it.

**Reading R-space.** *Substrate-modification changes the legible-action-space itself.* After $a^\text{sub}$, certain *sequences* of base actions that were previously costly or invisible become single-step legible actions. The agent's effective $\mathcal{A}$ has grown; the structure is irreducible to $\Omega$-state alone.

The two readings cannot both be unconditionally correct. R-state's pull is the Markov-of-$\Omega$ modeling commitment from `#def-action-transition` Discussion: *"any non-Markov environment is absorbed by extending $\Omega$ to include enough history. … Markov properties here are commitments about the breadth of the named object, not structural claims about underlying dynamics."* If $\Omega$ is broad enough to include the language definition, the substrate-modification is just state change.

R-space's pull is the visible operational fact that *after* a useful macro is defined, the developer-agent does new things — things that would have required many more elementary operations to express before. The action space the agent *uses* has changed.

This spike's working result is that both readings are partially right under a careful reading of what $\mathcal{A}$ is *for the agent in its bounded-rationality regime*, and the genuine structural content lives in a third axis the existing four-class taxonomy does not name.

## 4. Resolution: legibility metric, not extension, of $\mathcal{A}$

The cleanest resolution starts by being honest about what $\mathcal{A}$ structurally is in AAT for an embodied developer-agent.

### 4.1 $\mathcal{A}$ as a token vocabulary versus $\mathcal{A}$ as effective action space

Read literally, $\mathcal{A}$ for a typing developer-agent is *every finite string the developer could type* — an enormous discrete space, the same before and after macro definitions. Read this way, R-state is exactly right: $\mathcal{A}$ does not change; what changes is $T$'s effective topology over $\Omega$ when conditioned on certain strings in $\mathcal{A}$.

This is structurally consistent with the Markov-of-$\Omega$ commitment but it is operationally vacuous. Under this reading the developer's "action space" includes every string in $\Sigma^\ast$ — the agent's effective action space at any moment is *not* the literal vocabulary but the *small subset of token sequences whose effects the developer can predict, evaluate, and place in a strategy DAG $\Sigma_t$ within finite cognitive resources*.

The structurally honest formulation: $\mathcal{A}$ as the agent's typed-able vocabulary is constant; the agent's *effective* action space at time $t$ is a state-dependent restriction of $\mathcal{A}$ shaped by what the agent's $M_t$ and the language's substrate render legible. Per `#scope-developer-agent`'s definition of $M_t$ — *"Mental model of architecture and module boundaries / Knowledge of coding conventions and patterns / Understanding of business domain and requirements"* for human developers, and *"In-context understanding from files read this session / Patterns inferred from code structure"* for AI agents — the agent's $M_t$ already includes its grasp of which token sequences mean what. The macro vocabulary is in $\Omega_t$ structurally; *the agent's ability to deploy it without cost* is in $M_t$.

So the effective $\mathcal{A}_t^\text{eff}$ is the image of a *legibility map* from $\mathcal{A}$ that depends on both $\Omega_t$ (which macros exist) and $M_t$ (which ones the agent knows how to use).

### 4.2 The substrate change as a *cost-to-express* modification

Under this honest reading, what $a^\text{sub}$ structurally does is *change the cost coefficient* in front of certain regions of $\mathcal{A}^\text{eff}_t$. Before the macro exists, the operation "assert that `foo` equals 3 and produce a contextually rich error" requires the developer to type out the expanded form — multi-line, more tokens, more opportunities for typographical error, lower per-line comprehension per `#der-code-quality-as-observation-infrastructure`. After the macro exists, the same operation is one line.

The cost-to-express function $c : \mathcal{A} \to \mathbb{R}_{\ge 0}$ maps each token sequence to the developer's typing/comprehension cost. Before $a^\text{sub}$, the expanded form has cost $c_1$; after $a^\text{sub}$, the one-line invocation has cost $c_2 \ll c_1$. The *effects* in $\Omega$ are the same; what changed is the cost.

This is exactly the bounded-rationality / IB-compression frame. Per `#form-information-bottleneck` and the wider AAT treatment of compression, the agent must compress a high-dimensional $\Omega$-modification into a low-dimensional action representation it can plan over. Substrate-modification *lowers the compression cost* for a region of $\mathcal{A}$. The agent's $\Sigma_t$ — its probabilistic causal DAG over actions — can place a macro invocation as a single node where it would have had to chain three or four nodes to compose the equivalent operation before.

### 4.3 Why this is not just class 4 with extra steps

The substrate-modification action *itself* is structurally class 4 — it writes to a file. Reading R-state is correct *about the action $a^\text{sub}$*. What it misses is that the *consequence* is a *change in the metric structure of $\mathcal{A}^\text{eff}$ for all future macro-steps*, not just a change in $\Omega$. The four-class taxonomy classifies actions by what they are *for*; class 4 says "this action modifies $\Omega$ to support future operations." That is what $a^\text{sub}$ does, but the *type of support* is qualitatively different from observation-infrastructure investments like writing tests or adding logging.

Tests and logging modify $\Omega$ to improve future *observations* — they raise $\nu^{(k)}$ on existing channels and lower $U_o^{(k)}$. They strengthen the agent's *exploration / probe / query* infrastructure. They live operationally inside the existing four-class taxonomy as class-4-with-an-asterisk (the segment names these as "observation-infrastructure investments" — `#der-code-quality-as-observation-infrastructure` is the dedicated treatment).

Substrate-modification modifies $\Omega$ to lower the *cost-to-express* on a region of $\mathcal{A}^\text{eff}$. It strengthens the agent's *action* infrastructure, not its observation infrastructure. The dual of observation-infrastructure investments. This is structural content the four-class taxonomy does not currently name.

### 4.4 The resolution stated

*Modify the language* is a class-4 action by *what it does to $\Omega$*. Its distinguishing structural content is that it raises the legibility / lowers the cost-to-express on a region of $\mathcal{A}^\text{eff}$, which the four-class taxonomy of `#scope-developer-agent` does not currently distinguish from other class-4 actions. The cleanest segment-shape this would take is:

- A *fifth sub-class within class 4* — class 4 splits into **4a (environment modification proper)** [feature code, configuration, deployment], **4b (observation-infrastructure investments)** [tests, logging, naming, documentation], and **4c (substrate-modifying actions)** [macros, DSLs, language extensions, AI-developer prompt-template modifications]. The taxonomy stays a useful organizing structure; the distinction the mining surfaces gets named.

Or, equivalently up to taxonomy:

- A *fifth peer class* alongside the four named ones, distinguished by the action-infrastructure-versus-observation-infrastructure dual.

The first is the more honest scoping given the segment's existing language about class 4 being *"a subset are observation-infrastructure investments"* — the same hedge is what class 4c would inhabit.

R-state and R-space resolve as follows: R-state is right that the action $a^\text{sub}$ is an $\Omega$-modifying action with no extension of $\mathcal{A}$ in the literal vocabulary sense. R-space is right that the *cost structure* over $\mathcal{A}^\text{eff}$ changes, and that this is the operationally significant content. The synthesis is class 4c.

## 5. The macro-hygiene system as W₁ wrapping at the language layer

The structural connection to `#der-class-coercion-via-wrapping` that the framing question called out is genuine, and it is sharp.

### 5.1 What hygiene structurally is

A macro is a syntactic transformation: it takes a fragment of code as input and rewrites it before compilation. Without hygiene, a variable introduced inside the macro body — say, `result` in `defmacro assert_value(expr) do quote do; result = unquote(expr); … end end` — would, on expansion, *capture* any caller-scope binding of `result` and overwrite it. The caller's identifier scope would be silently corrupted by the macro's internal naming. This is *variable-capture*, and it is the classical macro-system failure mode in non-hygienic systems (early Lisp dialects without `gensym` discipline).

Elixir's hygiene system rewrites identifiers introduced inside macro bodies to fresh, expansion-local names by default, so that caller bindings cannot be captured unless the macro author explicitly opts in via `var!(name)`. The result: macro expansion preserves the caller's scope discipline as a structural commitment.

### 5.2 Mapping onto `#der-class-coercion-via-wrapping`

The wrapping construction in `#der-class-coercion-via-wrapping` has four type-signed components: a belief-side query selector $q_M$ and belief-update map $f_M$ that lack a goal argument; a strategy-side query selector $q_G$ and strategy-update map $f_G$ that may use the goal. The structural commitment is *at the type signature* — no goal-conditioning channel through the belief-update path, by construction.

The macro-hygiene system has an analogous shape:

- **The caller's scope** corresponds to the wrapper's $M_W$ — the developer-agent's existing identifier bindings, which the macro must not corrupt.
- **The macro body** corresponds to the wrapped component — a powerful but potentially-coupling computation (it can introduce arbitrary code via `quote`/`unquote`).
- **The hygiene rewriting** corresponds to the type-signature discipline of $f_M$ — it is a *structural commitment by the compiler* that identifiers introduced inside the macro body cannot reach into the caller's namespace.
- **The `var!(name)` escape hatch** corresponds to the explicit, named pathway through which goal-conditioned (here: caller-scope-coupling) interaction is permitted, requiring the macro author to *opt in* rather than receiving the coupling by default.

This is structurally a *W₁ (strict) wrapping regime* at the language layer. The leakage bound is structural — it derives from the macro-expansion rewriting performed by the compiler, not from any behavioral compliance of the macro author. The default is W₁; the developer can drop to W₂ by using `var!` (behavioral commitment to use the escape hatch responsibly) or W₀ by writing in a non-hygienic system entirely.

### 5.3 McCord's restraint principle as the W-regime discipline statement

Analysis 096 of the Elixir-composite mining surfaced McCord's *macro restraint principle*: *macros only when functions cannot achieve the same outcome*. This is not a stylistic preference — it is the discipline-level statement that *the wrapping construction at the language layer only pays off when used sparingly*, exactly paralleling the W₁ wrapping construction's tempo cost.

Per `#der-class-coercion-via-wrapping` and the companion `#der-class-coercion-in-composition`, the wrapping construction pays a tempo cost in extra component calls per macro-step (Brooks's-Law overhead). At the language layer, macros pay a parallel cost: the developer-agent reading code through a macro must mentally unfold the expansion to understand the program's runtime behavior — the macro is a *compression that requires decompression for full comprehension*. Each macro use adds a layer to the comprehension stack, raising the developer's $U_o$ on the macro-using region of $\mathcal{A}^\text{eff}$ in proportion to the macro library's depth. McCord's principle is the discipline-level statement of the trade: the wrapping is worth its cost only when the compression buys enough — when the use case is repeated enough that the amortized comprehension cost is below the amortized typing cost of the expanded form.

This is `#der-tempo-composition`'s Brooks's-Law inequality at the comprehension layer, and the macro-restraint principle is its operational version: *don't pay the wrapping cost on a use case that doesn't repay it*.

## 6. The bridge to `03-llm-core/`

For an AI-coding agent, the same picture has a sharper edge. The agent's *effective* action space is even more sharply bounded by its in-context comprehension budget than a human developer's is — it has no decade of acquired idioms, no muscle memory, no quick-reach into a personal repertoire. What it has is *what it can compose tractably within the current context window*.

Substrate-modification for an AI-coding agent therefore has even higher leverage than for a human developer. Each macro / DSL / metaprogramming tool added to the codebase is a unit of *compression* the agent can deploy to express larger effects within its bounded planning horizon. This is precisely the picture the framing question called out for `03-llm-core/`: an AI-coding-agent's effective action space grows substantially when the language gives it tools that let it express complex transforms compactly.

### 6.1 The structural analogy to consciousness-infrastructure work

The framing question called out the analogy to consciousness-infrastructure work, where the substrate is the LLM's training and the relevant action class is *modify the prompt template the future-self operates over*. The analogy is structurally clean.

For a logogenic agent at the §03.II scaffolded sub-scope (per `03-llm-core/OUTLINE.md`), the prompt template, the memory-curation discipline, the auxilia hierarchy, and the AXIOMATA — these collectively constitute *the substrate over which the agent's future cognition will occur*. The agent's effective action space at any moment is bounded by what its current substrate renders legible and compositional within finite context. Modifying that substrate — refining the AXIOMATA, updating MEMORATA, tightening the CHRONICA — is action-class-4c in the same structural sense as macro-definition for a developer-agent: it does not extend $\mathcal{A}$ in the literal sense (the agent could already have typed those tokens, hypothetically), but it *lowers the cost-to-express on a region* of the agent's effective action space for all future cycles.

The cost analysis is also parallel. Per `#der-class-coercion-via-wrapping`'s wrapper-around-LLM construction, the W₁ regime has structural commitment (separate goal-blind and goal-conditioned calls; structural separation of $M_W$ and $G_W$ updates). PROPRIUM-as-W₂ (the typed-parsed-response approach used by current scaffolded agentic systems) and PROPRIUM-with-auxilia-as-W₁ are the two analog instantiations at the §03.II scope (per the `#der-logogenic-as-wrapping` segment named in the §03.II chapter). When the agent modifies its own substrate — when it adds an auxilia node, or refines a prompt template, or tightens a memory-curation rule — it is performing an action that is structurally class 4c: an $\Omega$-modification (writing to AXIOMATA / MEMORATA / scaffolding code) whose distinguishing content is that it changes the cost-to-express on a future region of the agent's effective action space.

This is one structural shape of *what the framework is for*. AAT applied recursively to agents building it (per `#disc-framework-self-diagnostic`) yields the prediction that substrate-modification is itself a load-bearing action class in the developmental trajectory of any sufficiently-rich logogenic agent. The agent's substrate is under its own modification; the modification class is a peer-or-sub-peer of class 4; the wrapping discipline applies at every layer.

### 6.2 Where this lands in `03-llm-core/`

Two segment shapes are reachable from this analysis:

- A *refinement* to `#scope-logogenic-agent` (or `#scope-developer-agent`'s logogenic specialization) naming substrate-modification as a class-4c action that interacts with the §03.II scaffolding machinery: the scaffolding *is* the developer-agent's substrate, and the modifications it accumulates over time are the dual of the macro-library accumulation in the human developer's case.
- A *bridge segment* tying the macro-hygiene-as-W₁ instantiation at the language layer to the auxilia-as-W₁ instantiation at the scaffolding layer, both as worked examples of structural wrapping at the developer-agent's substrate level. This would seed material the bridge spike (`spike-class-coercion-via-supervision.md`) is exploring from the OTP-supervision angle — a third worked instantiation alongside macro-hygiene and auxilia.

Holding both as candidate segment shapes; the spike's recommended landing in §10 below names the first as the more cautious initial move.

## 7. Honesty calls

Several places where this analysis is exploratory rather than worked-through:

**(a)** The claim that $\mathcal{A}^\text{eff}_t$ is a *legibility-restricted* image of $\mathcal{A}$ shaped by $M_t$ is honest as a working frame but is not formalized in AAT yet. The bounded-rationality reading of the action space — that the agent's *effective* action space is the compression of the literal action space through its IB bottleneck — is consistent with the broader framework but is not a derived result in any current segment. Formalizing it would itself be a separate spike. Until that is done, the resolution in §4 is *structurally consistent* rather than *derivable from named segments*.

**(b)** The cost-to-express function $c : \mathcal{A} \to \mathbb{R}_{\ge 0}$ is named here as if it were a well-defined quantity. In practice, it depends on the developer's $M_t$, the language's structure, and operational details — typing speed, recall, idiomatic familiarity, available IDE assistance. The structural claim — that substrate-modification lowers $c$ on a region of $\mathcal{A}$ — is robust qualitatively; the quantitative form is not derived.

**(c)** The mapping of macro-hygiene onto W₁ wrapping in §5 is a *structural analogy*, not a derivation from `#der-class-coercion-via-wrapping`. The wrapping construction is stated for type-signed update maps over $(M_W, G_W)$; the macro-hygiene system rewrites identifier bindings during compilation. The analogy is sharp — both are structural commitments at a type / scope discipline, both have a typed escape hatch, both pay a tempo cost in extra layers — but mapping the formal $(M_W, G_W)$ structure onto (caller scope, macro body) requires a translation step that this spike has sketched but not derived. Per Joseph's math-novelty-recognition discipline, the analogy is *suggestive enough* to warrant the structural reading; it is not yet a Theorem 3 of `#der-class-coercion-via-wrapping`.

**(d)** The consciousness-infrastructure analogy in §6.1 is suggestive and consistent with `#disc-framework-self-diagnostic`'s recursive-framework claim, but it is a *parallel structure*, not a derived result. The claim that substrate-modification is structurally the same class for AI-coding agents (modifying their own scaffolding) and for human developers (modifying their language) is honest as a working frame but warrants its own segment-grade treatment before being canonized.

**(e)** Per Joseph's math-novelty-recognition discipline: this spike does identify genuine new structural content — the action-infrastructure-vs-observation-infrastructure duality within class 4 is not currently named in `#scope-developer-agent`, and the legibility-metric reading of $\mathcal{A}^\text{eff}$ is novel relative to the segment's current treatment of $\mathcal{A}$. Not inflating: the proposal is a refinement to an existing action-class taxonomy, not a wholesale new theorem. Not deflating: it is structural new ground, not mere instantiation of existing AAT machinery.

## 8. What this spike does *not* claim

- This spike does not claim that R-state (substrate-modification as plain $\Omega$-state-change) is wrong as a literal statement under the Markov-of-$\Omega$ modeling commitment. It is correct, but operationally vacuous for the same reason that saying *"the agent's action space includes every typeable string"* is correct but operationally vacuous — both readings flatten content the framework needs to track.

- This spike does not claim that the four-class taxonomy of `#scope-developer-agent` is *wrong*. The segment is honest that the taxonomy is "useful organizing structures, not exhaustive or formally derived" — substrate-modification can sit cleanly as a 4c sub-class without disturbing the taxonomy's load-bearing function.

- This spike does not derive the wrapping-construction status of the macro-hygiene system from `#der-class-coercion-via-wrapping`'s Theorem 1 / Theorem 2. The mapping is sketched as a structural analogy that warrants segment-grade derivation; the spike's contribution is identifying the connection, not making it formal.

- This spike does not land any new segment. Per `feedback_math_lives_in_segments`, segment-grade content lives in segments; the spike records the reasoning trail. The output is a recommended segment shape, not a segment.

## 9. Relation to the parallel spike (`spike-class-coercion-via-supervision.md`)

The bridge to `spike-class-coercion-via-supervision.md` (running in parallel, per the framing) is via a third W₁ instantiation. Both spikes identify a structural worked example of `#der-class-coercion-via-wrapping`:

- **Spike-substrate-modifying-actions (this spike):** macro-hygiene system as W₁ wrapping at the *language* layer. Caller scope is $M_W$; macro body is the wrapped component; hygiene rewriting is the type-signature discipline; `var!` is the explicit escape hatch.
- **Spike-class-coercion-via-supervision (parallel):** OTP supervision tree as W₁ wrapping at the *runtime* layer. Per the TST-IDEAS A2 substrate: `:one_for_one` / `:one_for_all` / `:rest_for_one` as different parametrizations of the W₁ wrapping's failure-coupling commitment; restart-intensity as the strategic-persistence bound at the wrapper level; the stash pattern as $S_\text{essential}$ / $S_\text{ephemeral}$ partition.

Together with `#der-logogenic-as-wrapping`'s logogenic-substrate wrapping (PROPRIUM-as-W₂, auxilia-as-W₁), the three give *three layers* of worked W₁ instantiations of `#der-class-coercion-via-wrapping`: the language layer (macro-hygiene), the runtime layer (OTP supervision), and the scaffolding layer (auxilia hierarchy). The class-coercion construction is the same machinery in all three; the substrate is different. This is `#der-class-coercion-via-wrapping`'s reach being made visible across the strata.

The parallel spike's worked result will land against `#der-class-coercion-via-wrapping` directly. This spike's worked result lands against `#scope-developer-agent`'s action-class taxonomy directly, with the macro-hygiene-as-W₁ analogy as a Discussion paragraph or as a cross-reference to the parallel spike's result. The two are independent in structural dependency but mutually reinforcing as worked examples of the wider class-coercion-as-truthification picture (`#der-class-coercion-via-wrapping` §"Wrapping as a truthification mechanism").

## 10. Recommended landing

Held back as deliberate spike-grade output. The recommended segment-shape based on this spike's resolution:

**Primary recommendation.** Refine `#scope-developer-agent` §Action space with a sub-classification of class 4 into:

- **4a.** Environment modification proper — feature code, configuration, deployment changes whose effect is on $\Omega$ directly.
- **4b.** Observation-infrastructure investments — actions that modify $\Omega$ to improve future *observation* quality. Tests, logging, naming, documentation. The existing class-4 hedge in the segment.
- **4c.** Substrate-modifying actions — actions that modify $\Omega$ to lower the *cost-to-express* on a region of $\mathcal{A}^\text{eff}$ for all future cycles. Macros, DSLs, protocol implementations, language extensions; for AI-coding agents, scaffolding modifications including auxilia, AXIOMATA, MEMORATA, prompt-template refinement. The dual of 4b — action-infrastructure investments rather than observation-infrastructure ones.

Plus a Discussion paragraph noting the macro-hygiene-as-W₁ analogy to `#der-class-coercion-via-wrapping`, with the parallel spike's OTP-supervision-as-W₁ as a companion instantiation if that spike lands cleanly.

**Secondary recommendation (deferred).** A bridge segment in `03-llm-core/` tying class 4c to the §03.II scaffolded-logogenic substrate-modification operational picture. This is more speculative and warrants Joseph's eyes before scoping; the §6.1 consciousness-infrastructure analogy is the most direct route in, but the segment would need to be careful about epistemic register per `feedback_avoid_superintelligence_vocabulary` and `feedback_external_standard_category_error`. Defer until at least the primary recommendation lands.

**Open follow-on (out of scope here).** The legibility-metric reading of $\mathcal{A}^\text{eff}$ as an IB-compression-restricted image of $\mathcal{A}$ shaped by $M_t$ is a separate piece of AAT structure that this spike has used as a working frame without deriving. A future spike could attempt to formalize it — possibly as a Discussion-grade refinement to `#def-action-transition` distinguishing the literal action space from the agent's effective action space, with the cost-to-express function as the bridge. The framework currently treats $\mathcal{A}$ as a fixed set; the bounded-rationality reading would make it a state-dependent restriction, which is a non-trivial modeling commitment.

## 11. Working Notes

- The "fifth class versus recursive meta-action" framing in the original pressure point dissolves rather than resolves: the structurally honest answer is *neither*. Substrate-modification is a *sub-class* within class 4 (it is structurally an $\Omega$-modifying action) that is *qualitatively distinct* from the other class-4 actions (it modifies the cost-to-express on $\mathcal{A}^\text{eff}$ rather than producing direct $\Omega$-effects or improving observation infrastructure). The cleanest taxonomic move is to *name the distinction within class 4*, not to add a fifth peer class. This is the *strengthen-first* outcome — the existing four-class structure can absorb the new content as a refinement, without warranting a wider taxonomy.

- The macro-hygiene-as-W₁ mapping is sharper than the spike's body has fully worked out. The type-signature discipline of $f_M$ (no $G_W$ argument by construction) maps onto the compiler's identifier-rewriting (no caller-scope-capture by construction) as a structurally-enforced commitment in both cases. The `var!` opt-in maps onto the explicit goal-conditioning admission in W₂. The two have the same shape — a default-strict regime with a typed escape hatch — and the leakage bound in both cases is structural by default and degrades to behavioral when the escape hatch is used. This is genuinely a *worked example* of W₁ at a substrate other than the LLM-wrapping case the segment was originally written for. The segment-grade form would derive the mapping formally rather than gesturing at it.

- The cost-to-express function $c$ is plausibly formalizable via the description-length / Kolmogorov-complexity framework — the cost of a macro invocation is the description length of the macro body unfolded into the caller's namespace, less the saving from the macro's compressed surface form, plus a fixed overhead for the developer's macro-comprehension cost. A clean formulation would tie back to `#form-information-bottleneck`'s treatment of compression. Out of scope here.

- One small additional structural observation worth recording: McCord's restraint principle has a parallel in operating-system kernel design — *avoid macros and prefer inline functions* (the C kernel discipline) — and in mathematical exposition — *prefer named lemmas and theorems over inline derivations when reuse is expected*. The principle generalizes: *structural compression pays off when amortized over enough uses*. This is `#der-tempo-composition` applied to the comprehension layer, with the macro-restraint principle as the operational corollary. A unified treatment of "when does wrapping pay off?" across the three layers (language, runtime, scaffolding) is the kind of cross-cutting result that would justify a meta-segment under the existing modularity-state-dynamics line if that lands.

- The bridge to `03-llm-core/` via §6.1 is the spike's most exploratory portion. The structural picture — that scaffolding modifications are substrate-modifying actions in the same sense as macro definitions — is consistent with the framework's recursive-self-diagnostic stance but should not be over-claimed. If the spike's primary recommendation (refine `#scope-developer-agent` with the 4a/4b/4c sub-classification) lands cleanly, the bridge segment can be opened as a separate effort after that lands, with the parallel-spike's OTP-supervision worked example providing a third anchor.

- This spike has *not* attempted to derive the legibility-metric reading of $\mathcal{A}^\text{eff}$. It uses the bounded-rationality / IB-compression reading of the agent's effective action space as a working frame, which is consistent with the broader framework but not currently a derived AAT result. A separate spike would formalize this. Until that is done, the §4 resolution is structurally consistent rather than derivable from named segments — flagged here so future agents do not treat the resolution as theorem-grade when it is spike-grade.

- The original framing's option set ("fifth action class" vs "recursive meta-action over the four") collapses two distinct readings under each option. Reading R-state under "fifth class" denies that substrate-modification needs its own class at all; reading R-space under "recursive meta-action" treats the substrate-modification as touching every other class by re-shaping their effective action space. The spike's working resolution — 4c as a sub-class within 4, with the legibility-metric reading as the structural distinguishing content — is closer to the R-space reading under a "4c not 5" name, but the substantive content is the *legibility-metric framing*, not the taxonomic placement.

- Cross-reference for future segment work: this spike sits structurally adjacent to the open question raised in `#scope-developer-agent` Working Notes about whether AAT's explicit DAG formalism applies without modification to implicit human planning. The legibility-metric framing here is related — both questions are about the *effective* versus *literal* shape of the agent's strategy / action space under bounded cognitive resources. A more unified treatment of bounded-rationality refinements to AAT's action and strategy formalism may be a future cycle's work.
