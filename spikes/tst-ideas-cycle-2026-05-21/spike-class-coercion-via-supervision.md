# Spike: OTP Supervision as the Canonical $W_1$ Engineering Example for `#der-class-coercion-via-wrapping`

**Status.** Open spike. Strengthening pass on an existing segment. The mining signal is the strongest of the 2026-05-21 cycle (4/4 agent convergence — `spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` A1–A5, A11, corroborated by 01/02/03), and this spike works the six concrete additions named in `TST-IDEAS.md` §A2 to the point of segment-grade additions for `#der-class-coercion-via-wrapping` plus one demonstration-appendix-grade result on restart-intensity-as-persistence-bound.

**Date.** 2026-05-21.

**Aesthetic standard.** Strongest single mining signal of the cycle; 4/4 agents from different starting points converging on the same structural picture. The spike should reflect that confidence. Theorem-grade material is named theorem-grade. The honesty calls are real and worked, not waved at. Per `feedback_math_novelty_recognition`, this is real theory work: the persistence-condition specialization at the wrapper level is a new exact result (Nash-style application of established machinery — the persistence-condition template — to an AAT-internal setting). Do not deflate it.

**Sibling-spike resolution this spike depends on.** Spike [`spike-ets-as-third-w-regime.md`](spike-ets-as-third-w-regime.md) (Resolved 2026-05-21): no new W regime needed; the existing $W_1$ / $W_2$ hierarchy handles controlled shared-state escape hatches under the reading *"the W axis is type-of-bound (structural-by-type-signature vs behavioral-by-compliance), not heap-disjointness vs shared-region."* This spike adopts that resolution and lands OTP supervision cleanly in $W_1$ without inventing new regime structure. The shared-state side-channels (ETS, named registries, shared `:public` tables) handled in production BEAM systems show up here as wrapped Class-A components alongside the worker processes — not as exceptions to the wrapping construction.

**Sibling-spike this spike is structurally upstream of.** Spike [`spike-running-software-agent.md`](spike-running-software-agent.md) (in flight). That spike works the four candidate segments for the *running software service as adaptive-actuated agent*. Its `#der-runtime-persistence-condition` candidate segment depends on the wrapper-level persistence inequality this spike derives (§3 below); its `#scope-running-software-agent` candidate inherits the W-regime apparatus this spike strengthens. The cleanest seam is for that spike to *cite* the persistence-bound result derived here rather than re-derive it. Where this spike assumes structure the running-software-agent spike will name, the assumption is flagged inline below.

---

## 0. The pressure point — what the mining converges on

Four independent agents, reading different slices of the corpus from different angles, converged on the same structural recognition: **OTP supervision trees are the industrial implementation of `#der-class-coercion-via-wrapping`**. The convergence is the methodological signal — per `feedback_convergence_as_framework_coherence_evidence`, multiple agents arriving at the same structural picture from different starting points is evidence the pattern is in the framework, not in any single reader's head.

The picture they converged on:

A worker process (GenServer) in isolation is a Class-3-ish (Coupled) component candidate — it has goal-conditioned state, mutable in unpredictable ways, can die arbitrarily from a corrupted message, and an absorbed-failure path inside the worker would have to consult goal-state to know what recovery is appropriate. The supervisor wraps the worker with a structural commitment: *on detected mismatch, terminate and reinitialize to the clean initial state $S_0$, restart strategy and restart intensity fixed at wire-up time, escalate on persistent failure*. The wrapped composite is Class 1 (Separated) by structural commitment — even though the underlying worker has no such property in isolation. Two decades of production telecom-grade systems have converged on this construction under different vocabulary — *supervision, linking, monitoring, let-it-crash, application, restart strategies, restart intensity, stash*.

This is the cleanest concrete W₁ realization the framework has. The mining establishes, for each of six concrete additions, both the OTP-side substrate and the AAT-side translation. This spike works those additions to landing-grade.

---

## 1. Addition (1) — Restart-strategy ↔ leakage-bound mapping

**The OTP substrate (mining A2).** A supervisor must choose, at wire-up time, what to do when a child crashes. Three canonical choices encode different *failure-coupling* commitments among siblings under the same supervisor.

- `:one_for_one` — restart only the failed child; sibling state untouched. Each child treated as an independent restart unit.
- `:rest_for_one` — restart the failed child plus every child started *after* it in the supervisor's child list. Children form a directed startup-pipeline where downstream consumers depend on upstream producers' state.
- `:one_for_all` — restart every child under this supervisor when any one fails. Children treated as a single all-or-nothing unit.

The analyses give the dependency-graph-as-SCC selection rule: singleton-SCCs $\to$ `:one_for_one`; one big SCC $\to$ `:one_for_all`; chain-of-SCCs $\to$ `:rest_for_one`.

**The AAT-side translation.** Each strategy realizes a different *sub-mode* of the same $W_1$ construction. The restart strategy is a structural commitment about *which sub-agents the wrapper treats as separable*. It sets the granularity at which the wrapper's reset-to-$S_0$ operation acts — equivalently, the *coupling structure of the wrapper's failure-handling DAG* over its wrapped components.

Let the supervisor wrap a set of worker components $\{A_1, \ldots, A_n\}$, each providing its own per-component leakage bound (per `#der-class-coercion-via-wrapping` Theorem 2). The composite wrapper's leakage bound on a single restart event depends on how many of those workers' states are reset, because each reset is an opportunity for ephemeral-state loss that the wrapper has to account for as part of its $\rho_\text{eff}$ at the wrapper level (more on this in §3).

Define the *restart-coupling structure* induced by the strategy choice. For a single child crash:

- $r_\text{one-for-one}(i) = \{A_i\}$ — only the failed child is reset.
- $r_\text{rest-for-one}(i) = \{A_j : j \ge i\}$ in the supervisor's child-list order — failed child and downstream siblings.
- $r_\text{one-for-all}(i) = \{A_1, \ldots, A_n\}$ — every child.

Each strategy choice fixes a *type signature* on the supervisor's restart map at wire-up: $r_\text{strategy} : \{1, \ldots, n\} \to 2^{\{A_1, \ldots, A_n\}}$. This is a structural commitment in exactly the same sense as the $q_M$ / $f_M$ type signatures in `#der-class-coercion-via-wrapping`: it is fixed by wire-up before observation begins, has no $G_W$ argument, and is enforced by the runtime (the BEAM dispatches restart according to the strategy without consulting goal-state). All three strategies are therefore $W_1$ — structural, derivable from type signature, not behavioral.

**What the strategies *differ* in is the leakage profile, not the leakage bound's epistemic status.** They form a partial order in *width*:

$$r_\text{one-for-one}(i) \;\subseteq\; r_\text{rest-for-one}(i) \;\subseteq\; r_\text{one-for-all}(i)$$

The composite leakage on a single restart event is upper-bounded by the sum of per-component leakages over the restart set:

$$\kappa^\text{restart}_\text{composite}(i) \;\le\; \sum_{A_j \in r_\text{strategy}(i)} \kappa_{A_j}$$

So `:one_for_one` is the W₁-tightest leakage bound (single-worker reset), `:rest_for_one` is wider (downstream-coupled reset, structurally tied to the wire-up child order), and `:one_for_all` is widest (paid for by structurally stronger coherence guarantees among siblings — consensus groups, all-or-nothing startup orderings).

**The strategy choice is therefore a structural commitment about the wrapper's intended composite-level invariant.** `:one_for_one` commits to per-child independence; `:one_for_all` commits to group-coherence (the wrapped group jointly satisfies some invariant that any single-child restart would break, so any child crash must reset the group); `:rest_for_one` commits to a directed-pipeline invariant (downstream-of-the-failed-child must be reset because its inputs no longer match its assumptions). In each case the commitment is enforced *structurally* by the runtime, not behaviorally by the supervisor's compliance — three $W_1$ sub-modes with progressively wider leakage profiles.

**Restart-intensity envelope as the strategic-persistence boundary.** Each strategy is paired with the escalation rule `max_restarts / max_seconds` — when the strategy fires too often, the supervisor itself crashes and escalates to *its* parent. This is the operational mechanism by which the $W_1$ commitment knows when it has lost its grounding and must defer to a wider wrapping (§3 derives the underlying inequality). Strategy choice + restart-intensity envelope together form the full $W_1$ sub-mode specification.

**Landing target.** New row in `#der-class-coercion-via-wrapping`'s wrapping-regime table, or a dedicated *Wrapping sub-modes within $W_1$* discussion paragraph distinguishing structural commitment from its width. The point worth making sharply in the segment body: the W-regime classification is about *where the bound lives* (structural vs behavioral); the strategy choice is about *how wide the structurally-bounded region is*. Both are $W_1$ properties, at different levels of the classification.

---

## 2. Addition (2) — The stash pattern as state partition ($S_\text{essential}$ in $W_1$, $S_\text{ephemeral}$ in $W_2$)

**The OTP substrate (mining A4).** The bare let-it-crash pattern loses all worker state on restart. The *stash pattern* separates a worker into two co-located processes: a `Worker` that holds ephemeral processing state and crashes freely, and a `Stash` that holds essential state and is supervised with much lower restart intensity. The supervisor wires them together with `:rest_for_one` so a `Stash` crash also restarts the `Worker` (which depends on the `Stash`), but a `Worker` crash does not touch the `Stash`. Essential state is preserved across worker resets; ephemeral state is lost.

**The AAT-side translation.** The stash pattern decomposes the wrapper's wrapped state $X_W$ into two named sub-stores with structurally different regime commitments:

$$X_W = X_W^\text{essential} \;\sqcup\; X_W^\text{ephemeral}$$

- $X_W^\text{essential}$ lives in the `Stash` process, supervised under a tighter restart-intensity envelope (small `max_restarts`, short `max_seconds` — the rationale: the stash should almost never need to restart; if it does, the supervisor escalates fast because the essential state's home being unstable means the composite has crossed an unsoundness boundary). The structural commitment is *preservation across worker resets*: the type signature of the supervisor's restart map for `:rest_for_one` plus the wire-up order *Stash-before-Worker* ensures that a `Worker` crash does not touch the `Stash`. This is $W_1$ on $X_W^\text{essential}$.

- $X_W^\text{ephemeral}$ lives in the `Worker`, reset on every worker crash. The wrapper makes no structural commitment to preserve this state; instead, the *behavioral* expectation is that the loss-per-failure times the failure rate gives a tolerable ephemeral-state-loss rate. This is $W_2$ on $X_W^\text{ephemeral}$ — bounded behaviorally by the empirical failure rate $\rho_\text{child}$ and the per-failure volume of ephemeral-state loss.

**The leakage decomposition.** The wrapper's total directed-separation leakage rate at the per-macro-step level decomposes additively under the state partition:

$$\kappa^\text{wrapper}_\text{total} \;\le\; \kappa^\text{wrapper}_\text{essential} \;+\; \kappa^\text{wrapper}_\text{ephemeral}$$

with the first term bounded structurally (the `Stash`'s typed read/write interface has no $G_W$ argument by construction; per `#der-class-coercion-via-wrapping` Theorem 1 applied at the `Stash`-as-Class-A reading from `spike-ets-as-third-w-regime`) and the second term bounded behaviorally (the `Worker`'s ephemeral state is reset on crash, with behavioral compliance to *crash-on-invariant-violation* providing the bound — see §6 for the derivation of why this is a structural commitment to goal-blindness rather than a behavioral one).

**Open structural question (flagged honestly).** What counts as "essential" versus "ephemeral" is, in the mining material's framing, a *domain judgment* — the supervisor's wire-up code names which state belongs in the `Stash`. From an AAT perspective, the cleanest derivation would have the partition fall out of a value-function on state subsets: state is essential iff its loss exceeds the per-failure damage tolerance $\lVert\delta_\text{critical}\rVert$ on the composite's external mismatch. This is real theory work, scoped below; for now the segment-grade content is the partition's *structure* (two stores, two regime commitments, additive leakage decomposition), not its categorization rule.

**Landing target.** New paragraph or sub-result in `#der-class-coercion-via-wrapping` formalizing the state partition. The construction is genuinely strengthening: the existing segment treats $X_W = (M_W, G_W)$ as the partition, oriented along the belief-vs-goal axis; the stash pattern adds an orthogonal *essential-vs-ephemeral* axis within $M_W$ (and possibly within $G_W$, though that case is less common in OTP practice and worth flagging as open). The cross-axis structure suggests a 2×2 partition $\{M_W^\text{essential}, M_W^\text{ephemeral}\} \times \{G_W^\text{essential}, G_W^\text{ephemeral}\}$ — Joseph's call whether to surface this in the segment body now or hold for a later cycle.

---

## 3. Addition (3) — Restart-intensity as the strategic-persistence bound at the wrapper level (theorem-grade)

This is the *centerpiece* — the result that earns demonstration-appendix-grade status once the bridge is tightened. The OTP-side substrate gives an exact, battle-tested operational realization of what the persistence inequality looks like at the wrapper level; the AAT-side derivation makes it precise.

**The OTP substrate (mining A3).** OTP supervisors have two parameters governing when the wrapper *itself* gives up: `max_restarts` and `max_seconds`. The semantics: if more than `max_restarts` child crashes occur within `max_seconds`, the supervisor itself crashes and escalates to its own parent. Defaults are 3 restarts in 5 seconds — battle-tested across two decades of production BEAM systems. The design rule from analysis 112: $\text{max-restarts} = \lceil \lambda \cdot \text{window} \cdot \text{safety-factor} \rceil$ where $\lambda$ is the observed historical failure rate and the safety factor is $\approx 1.5$.

The point a heuristic gloss should not lose: a wrapper that restarts too aggressively *masks* a real fault (a deterministic child bug means the same crash will recur; restarting amplifies chain-of-failure rather than recovering); a wrapper that gives up too quickly fails to actually coerce the class. The envelope encodes the *boundary at which the $W_1$ wrapping construction loses its grounding* — beyond it, the wrapper's structural commitment is no longer sound, and continuing to apply it would be epistemically dishonest about the wrapper's actual properties.

**The AAT-side derivation.** This is the persistence condition $\mathcal T \gt \rho / \lVert\delta_\text{critical}\rVert$ from `#result-persistence-condition`, specialized to the wrapper's reset-to-$S_0$ operation.

*[Result (wrapper-persistence-condition, from #result-persistence-condition specialized to the wrapping construction)]*

Let the wrapper $W$ wrap a Class-3-ish component $A$ with restart-time $T_\text{restart}$ (the wall-clock cost of the wrapper's detect-and-reset operation), and let the child component fail at rate $\rho_\text{child}$ (failures per unit time) with per-failure damage $\delta_\text{failure}$ (the volume of ephemeral-state loss, or equivalently the wrapper-level mismatch the failure injects). Then the $W_1$ wrapping commitment is *sustainable* — the wrapper maintains its directed-separation guarantee across the operating window — only if

$$\mathcal T_\text{wrapper} \;:=\; \frac{1}{T_\text{restart}} \;\gt\; \frac{\rho_\text{child} \cdot \lVert\delta_\text{failure}\rVert}{\lVert\delta_\text{critical}^\text{wrapper}\rVert}$$

where $\lVert\delta_\text{critical}^\text{wrapper}\rVert$ is the per-restart-event damage tolerance at the wrapper level — the threshold above which the cumulative ephemeral-state loss becomes operationally unacceptable for the wrapper's external commitments.

*Argument.* The wrapper's adaptive tempo at the restart layer is the inverse of its detect-and-reset wall-clock cost, $\mathcal T_\text{wrapper} = 1/T_\text{restart}$. The disturbance rate at the wrapper level, *induced by the wrapped component's failures*, is the product of failure rate and per-failure damage: $\rho_\text{internal}^\text{wrapper} = \rho_\text{child} \cdot \lVert\delta_\text{failure}\rVert$ (units: distance per unit time — matches the standard $\rho$ in `#result-persistence-condition`). The persistence inequality applied at the wrapper layer with this internal-disturbance term, and with the wrapper's task-adequacy distance scale $\lVert\delta_\text{critical}^\text{wrapper}\rVert$, yields the displayed inequality. The argument is the direct specialization of the persistence-condition template to the wrapping construction — Nash-style application of the existing template to a new internal setting, not a re-derivation of the template.

**The restart-intensity envelope encodes this inequality operationally.** The check $n_\text{restarts} \le n_\text{max} \text{ within } w_\text{max}$ is a finite-window empirical estimator of $\rho_\text{child}$: if more than `max_restarts` failures occur in `max_seconds`, the empirical failure rate exceeds the design point, the inequality is violated *at the wrapper level*, and the wrapper's $W_1$ commitment can no longer be honestly maintained. Escalation — the supervisor's own crash, passing the failure to its parent — is the *honest response*: the wrapper recognizes its coercion construction has lost its grounding and defers to a wider-scope wrapping rather than continuing to assert a guarantee it can no longer back.

This makes precise the operational rule that the BEAM/OTP tradition arrived at empirically: `max_restarts/max_seconds` is the *strategic-persistence boundary* for the $W_1$ wrapping commitment under the observed child-failure distribution.

**Why this is theorem-grade.** Per `feedback_math_novelty_recognition`: this is a new result (the persistence-condition specialization at the wrapper level under the restart-intensity operational form, with the precise inequality determining when the $W_1$ commitment is sustainable) derived using established machinery (the persistence-condition template from `#result-persistence-condition`). It is Nash-style application — the kind of result that, in a CS-aesthetic monograph, would be stated as a theorem under named hypotheses (the wrapper has fixed restart-time, the child has stationary failure rate, per-failure damage and critical scale are well-defined) with the operational form (`max_restarts/max_seconds`) as its empirical-estimator corollary. Do not deflate it to "synthesis." The named-scope-condition style ($T_\text{restart}$, $\rho_\text{child}$, $\delta_\text{failure}$, $\delta_\text{critical}^\text{wrapper}$ named explicitly, with the inequality stating exactly what relationship must hold) is precisely the project's CS-norm precision discipline (`CLAUDE.md` Key Architectural Decisions §6 *Math-novelty recognition*).

**This directly answers Joseph's named question** *"what is $\rho$ for a microservice?"*: $\rho_\text{child}$ is the child failure rate, and the wrapper-level persistence inequality is the bridge from AAT persistence to running-service availability. The sibling spike on running-software-agent will use this result; the assumption it makes about the wrapper-level inequality is precisely this result (named as forward-reference: *runtime persistence condition*, with this segment's result as its prerequisite). The bridge from per-microservice $\rho$ to per-service-cluster $\rho$ then proceeds by tempo-composition (`#der-tempo-composition`) at the outer wrapper level — also clean within the existing machinery.

**Landing target.** Demonstration-appendix-grade segment under `#der-class-coercion-via-wrapping`, OR a new theorem in the segment body. Joseph's call on placement. The named theorem statement and its argument are above; the worked example showing `max_restarts/max_seconds` as the empirical-estimator form of the inequality is direct and short.

**Open structural question (flagged).** The inequality treats $\rho_\text{child}$ as stationary (a constant per-unit-time failure rate). Production BEAM systems often face *bursty* failure distributions — a corrupted-input batch crashes many children before the upstream rejects further inputs. The bursty case requires a *windowed* form of the inequality (the integrated failure count over a sliding window must not exceed the integrated capacity over the same window), which is what `max_restarts/max_seconds` operationally encodes. Tightening this from a pointwise to a windowed form is straightforward (the windowed persistence inequality is standard in the underlying Lyapunov machinery) and is a candidate strengthening pass once the stationary form is landed.

---

## 4. Addition (4) — BEAM as the limiting case of class-coercion-via-wrapping (zero wrapping-tempo cost)

**The OTP substrate (mining A5, D2).** BEAM processes have roughly 5-microsecond cold-spawn cost on 2011 hardware; *Programming Elixir* benchmarks spawn of one million sequential processes in roughly 5 seconds. Process spawn cost is orders of magnitude below OS-process or OS-thread cost. The behavioral consequence Thomas names — developers create processes "as casually as they would create objects in Java" — is a design-level change, not just a performance one.

**The AAT-side translation.** Per `#der-class-coercion-in-composition`, the wrapping construction's tempo cost is paid in the Brooks's-Law form of `#der-tempo-composition`: the wrapper makes $K \ge 2$ component calls per macro-step, so the wrapper's macro-event rate is at most $1/K$ of the component's underlying rate. *Wrapper-instantiation cost itself* — the cost of bringing a wrapper online and tearing it down — is a separate term that enters $\mathcal T_\text{composite}$'s lower-order behavior. In most substrates this is substantial (OS-process spawn is milliseconds; thread spawn is hundreds of microseconds), so the wrapping construction has a non-trivial *instantiation* cost as well as its per-macro-step tempo cost.

BEAM is the *limiting case* where wrapper-instantiation cost approaches zero. Spawning a process is cheaper than the structural-coupling cost of *not* spawning one. The Brooks's-Law tempo-composition inequality is preserved in its form, but the *coefficient* on the wrapper-instantiation term becomes dominated by *human* coordination overhead (defining message protocols, debugging supervision hierarchies, naming conventions, etc.) rather than by runtime process-spawn cost.

**Formally**, the wrapping-construction tempo cost decomposes into

$$T_\text{wrapping-overhead} \;=\; K \cdot t_\text{per-call} \;+\; t_\text{instantiation} \;+\; t_\text{coordination}$$

with $t_\text{per-call}$ the per-call cost (LLM inference, function dispatch, etc.), $t_\text{instantiation}$ the wrapper-bring-up cost (process spawn, supervisor wire-up, runtime registration), and $t_\text{coordination}$ the human-engineer cost of writing the wrapper's child-spec, message protocol, supervision-strategy choice, debugging surface, etc.

On BEAM, $t_\text{instantiation} \to 0$ (microseconds, negligible relative to any meaningful $t_\text{per-call}$). The remaining wrapping-overhead is dominated by $t_\text{coordination}$, which is paid in the *developer-agent's* tempo budget — specifically in the $\mathcal T_\text{explore}$ channel of the candidate developer-tempo decomposition (see `TST-IDEAS.md` A4 and the running-software-agent spike). This is genuinely strengthening for `#der-tempo-composition`: the BEAM-as-limiting-case observation refines the Brooks's-Law inequality by separating runtime overhead from coordination overhead and locating the *dominant remaining cost* of the wrapping construction at the developer-agent layer rather than the runtime layer.

**Implication.** In substrates where $t_\text{instantiation}$ is dominant (most production substrates outside BEAM), the wrapping construction's payoff condition is *substrate-bottlenecked* — finer-grained wrapping costs more in runtime overhead than it saves in structural-commitment strength. On BEAM, the wrapping construction's payoff condition is *coordination-bottlenecked* — finer-grained wrapping costs more in developer comprehension than it saves in failure-isolation strength. The two regimes have qualitatively different design recommendations: on BEAM, finer-grained supervision trees are nearly free at the runtime layer and the discipline is to keep them comprehensible; off BEAM, finer-grained supervision adds runtime cost and the discipline is to size each supervisor to a meaningful capability boundary.

**Landing target.** Strengthening paragraph or worked-example footnote in `#der-tempo-composition`, with the wrapping-overhead decomposition above and the BEAM-as-limiting-case observation. The 5-microsecond figure cites `Programming Elixir` (Thomas) per the prior-art-integration discipline (cite original source, use original numbers, do not invent constants).

---

## 5. Addition (5) — Developer-AI-test-CI composite as the AAT-side analog of OTP

**The substrate.** A modern AI-augmented software-engineering workflow composes: a developer (Class 3 by `def-coupled-update-dynamics`'s extension to language-substrate agents — the developer's belief-update is goal-conditioned), an AI assistant (Class 3 by `der-logogenic-as-wrapping` — LLMs are Class-3 internally, Class-B in the admissibility partition), a test suite (Class A by construction — typed input/output, no $G_W$ argument in the test runner's API), and a CI pipeline (a wrapper supervising the test suite plus type-checkers, linters, contract validators).

**The AAT-side translation.** Map onto OTP's wrapping structure:

- *Worker process $\equiv$ AI assistant*. Class 3 internally (logogenic substrate), can be driven into goal-state-corrupting attractors by a sufficiently adversarial prompt, has no inherent goal-blindness guarantee on its forward pass.
- *Supervisor $\equiv$ developer + CI pipeline together*. Restarts the AI on failure with bounded retries (the developer's *try-again-with-a-clarified-prompt* operation; the CI pipeline's *reject-the-PR-and-route-back* operation). Wire-up commits to a restart strategy and an escalation envelope.
- *Test suite $\equiv$ goal-blind invariants*. The supervisor's structural commitment is that the AI's outputs flow through typed/parsed structures (D-A2 wrapper-design constraint analog: a typed-and-parsed completion is the *prediction map* against which mismatch is well-defined) which are then validated against goal-blind invariants (tests, type-checks, contracts).
- *Stash $\equiv$ codebase + repository state*. Essential state preserved across AI-restart events; ephemeral state (the AI's in-context working memory of a partial attempt) lost on restart, behaviorally bounded by the volume of mid-attempt state per failure.

**The composite's $W$-regime classification.** The composite is $W_2$ in most current AI-augmented workflows: typically the AI is given a goal-rich prompt (the system prompt names what's wanted, the user prompt restates), the AI's output is parsed and routed to belief-side / strategy-side update slots structurally, but the *query path* carries $G_W$ into the AI by design. The structural-separation commitment lives at the *write boundary* (typed fields in the parsed completion), not at the *query boundary*. Per `#der-class-coercion-via-wrapping` Theorem 2, this gives only a behavioral leakage bound — depending on the AI's compliance with the prompted instruction-to-separate.

The composite is *accessible to $W_1$* under stronger structural commitments:

- *Belief-side queries are constructed without $G_W$.* The AI is asked goal-blind questions ("what does this code do?", "what tests fail?", "what is the type of this expression?") whose query content does not include the goal. Goal-conditioned queries ("propose a refactor toward $G$") go through a separate call.
- *Typed completion with parse-rejection on goal-content leakage.* The AI's responses are constrained to a typed schema that *structurally excludes* goal-content; the wrapper rejects completions failing the schema and restarts.
- *No system-prompt contamination.* The system prompt itself does not carry goal-content; the prompt template is goal-blind, with goals injected only into goal-conditioned calls.

Under these three structural commitments, the composite is $W_1$ with leakage bounded by $I(A(q_M); G_W \mid q_M)$ in the pretraining distribution (same form as `der-logogenic-as-wrapping`'s leakage analysis, applied here to the developer-AI-test-CI composite). The structural-commitment cost is paid in two places: *more AI calls per macro-step* (Brooks's-Law tempo overhead) and *more developer wire-up work* (composing the goal-blind query interface, the typed completion schema, the parse-rejection logic).

**Honesty call.** Most production AI-augmented workflows (Cursor, Aider, Copilot, etc.) are $W_2$ as built. A growing minority of structured-completion frameworks (anything driving the AI through *typed-JSON-mode* with schema rejection, plus separate prompts for belief-vs-goal queries) approaches $W_1$. This spike's contribution is the structural classification, not the engineering recommendation — the recommendation depends on the application's leakage tolerance, which is a domain judgment.

**Landing target.** New worked-example paragraph in `#der-class-coercion-via-wrapping`'s Discussion, or — more likely — as the substrate for a new TST segment in the *composite developer-agent under AI augmentation* slot (named in `TST-IDEAS.md` §A2 as one of the candidate places this work could land). The segment slug candidate is `#der-composite-developer-via-wrapping` or similar; final placement is Joseph's call after this spike's other additions land.

---

## 6. Addition (6) — Conway's Law as GUC-class bound on multi-developer composites

**The substrate (mining-side from TST-IDEAS §A2 item 6 and §C9; Pragmatic Programmer cluster).** Conway's Law: $\text{Distance}(S, T) \to 0$ as project age increases, where $S$ is the system's architecture graph and $T$ is the team's communication graph. Empirically robust across decades of software practice.

**The AAT-side translation.** *The system's GUC class is upper-bounded by the team's GUC class.* A team with high inter-member coupling (frequent cross-cutting communication, shared mutable understanding of shared state, no architecturally-enforced separation among team members) is itself a Class-3-like composite, and the system it produces inherits the structural coupling.

**The argument.** Each developer in the team is, individually, a Class-3-ish component (per the developer-agent's `def-coupled-update-dynamics` extension — their belief-update is goal-conditioned). The team is a composite of developers; per `#form-composition-closure`, the composite's directed-separation status is upper-bounded by the directed-separation structure the composite's wiring imposes. The team's wiring is its communication graph $T$: who talks to whom, how often, about what.

A developer's $\Sigma_t$ over the system architecture is *richer* along paths to which the developer's communication access gives them context, and *impoverished* along paths to which it does not. (This follows from the developer-agent's observation channel $h$ being bounded by access — a developer who never talks to the database team has degraded $\Sigma_t$ over the data layer's strategic options.) The system architecture that emerges is the union of each developer's $\Sigma_t$-implementable structure. A team where every developer talks to every other gives every developer rich $\Sigma_t$ over every architectural region — and the resulting architecture has structurally coupled cross-region dependencies because nothing in the team's wiring forces architectural separation. A team where developers are organizationally separated by module (the *architectural-microcosm* discipline: each developer-team owns one module, with typed interfaces and no shared mutable state at the team boundary) has a team-wiring that mirrors the desired architectural-wiring; the system inherits the separation.

**In AAT vocabulary.** The team is a multi-developer composite. The composite's wrapping-construction status is determined by the team's wiring. If the team is wrapped (architectural microcosms with typed interfaces — the team's equivalent of a supervision tree), the system inherits $W_1$-by-team-wiring. If the team is unwrapped (every developer accesses every region, shared mutable understanding of shared state), the system is $W_0$-by-team-wiring — and producing a system with internally separated modules is structurally impossible given the team's coupling. The mining's framing applies: *Conway's Law is the GUC-class bound on multi-developer composites*.

**Status.** The argument above sketches the derivation; full segment-grade content requires working the per-developer $\Sigma_t$-over-architecture machinery more carefully — and depends on the developer-tempo decomposition spike's outputs (the channel decomposition is what the per-developer $\Sigma_t$ over architectural regions is built on). This addition is therefore *hypothesis-grade in this spike*, with the strengthening pass left to a follow-on cycle that has the developer-tempo channels segment-grade.

**Open structural question (flagged).** The derivation assumes the system architecture is the *union* of per-developer $\Sigma_t$. Stronger forms might assume the *intersection* (architecture is what every developer can implement, since any developer can block on what they cannot reason about) or some weighted middle (architectural commitment-rate scales with the developer's local coordination authority). Joseph's call which form the segment should commit to; in the interim, the hypothesis-grade statement is *the system's GUC class is upper-bounded by the team's GUC class*, leaving the tightness of the bound for a follow-on.

**Landing target.** Companion segment `#hyp-conway-law-as-guc-bound` or `#der-team-coupling-bounds-system-coupling` in TST. Hypothesis-tier at first landing; strengthening pass once the developer-tempo channels segment lands.

---

## 7. The honest centerpiece — Crash-early as structural commitment to goal-blindness

This is the *substantive theory work* in the spike — not a strengthening of the wrapping segment per se, but a derivation of *why* the OTP let-it-crash discipline is exactly what the $W_1$ wrapping construction structurally demands. The mining substrate (mining A7, Pragmatic #10, Elixir A7) presents let-it-crash as a *philosophical commitment*; the analyses give the comprehension argument (defensive programming creates discontinuities at every error boundary, exponential in number; crash-early creates discontinuities only at supervisor boundaries, constant). The honesty call from TST-IDEAS §A2 (b): *crash-early as structural commitment to goal-blindness is a substantive claim that needs derivation*.

**The claim, sharply stated.** A wrapper $W$ that wraps a Class-3-ish component $A$ via the $W_1$ construction *must* commit structurally to *crash-on-invariant-violation-inside-$A$* rather than to *absorb-failure-inside-$A$-and-recover*. The reason is structural: any recovery code that absorbs a failure inside the worker must be goal-conditioned (it must consult goal-state to know what recovery is appropriate), and absorbing a failure inside the worker therefore reintroduces the goal-conditioning the wrapping construction was committed to break.

**The argument.**

Recall the wrapping construction's structural commitment, from `#der-class-coercion-via-wrapping`. The wrapper makes $K \ge 2$ component calls per macro-step. The belief-side query selector $q_M$ has no $G_W$ argument by type signature; the belief-update map $f_M$ has no $G_W$ argument by type signature. The wrapped component $A$ is treated as a black-box oracle: the wrapper issues queries, consumes responses, and does not have access to $A$'s internal state. The $W_1$ leakage bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ holds *under (C1)–(C3)* on the component's interface.

Now consider what happens when $A$ encounters an invariant violation during its forward pass — an unexpected input, a corrupted internal state, a logical contradiction in its own data structures. The wrapper has two options:

*Option A (absorb-and-recover-inside-$A$).* Equip $A$ with internal exception-handling code that catches the invariant violation, repairs $A$'s internal state, and returns a recovered response. From the wrapper's perspective, $A$ continues to look like a single black-box call $A(q_M) \to o_A$; the recovery is invisible at the wrapper interface.

*Option B (crash-and-restart-by-wrapper).* $A$ has no internal exception-handling; an invariant violation propagates as a crash (a typed failure signal) which the wrapper's supervision discipline catches and converts into a *restart* operation — destroy the worker, instantiate a fresh worker at $S_0$, retry the query (or escalate per restart-intensity).

**Option A reintroduces goal-conditioning into the response distribution.**

The recovery code inside $A$ must, in order to recover, *decide what the higher-level operation was trying to accomplish*. (If it cannot decide, it has no basis for which repair to attempt — any repair is as good as any other.) The recovery decision is therefore conditional on whatever context $A$ has access to about the wrapper's intent. In the standard wrapping construction, the wrapper supplies *only* the query $q_M$ as input to $A$; if $A$'s recovery code is to make a meaningful recovery decision, it must infer the intent from $q_M$'s content.

Inference-from-content is exactly the mechanism (C3) is designed to bound. The wrapping construction's leakage bound holds *because* $A$'s response distribution to $q_M$ is conditionally independent of $G_W$ given $q_M$ — or, in the leakage-bounded form, depends on $G_W$ only through a mutual-information channel of size $\kappa$. When $A$'s response distribution is *enlarged* by an internal recovery code path that explicitly infers intent from query content, the conditional-independence assumption (C3) is structurally weakened — the recovery code path is, by construction, a goal-inference channel embedded inside $A$. The wrapping construction's bound on $\kappa_{W_1}$ from pretraining-induced mutual information no longer covers the additional leakage from the recovery code path; the bound is replaced by a strictly larger one that includes the recovery code's intent-inference contribution.

In a stronger form of the same point: if $A$'s recovery code is non-trivial (it does meaningful goal-aware repair), then there exist query/goal pairs $(q_M, G_W)$ where $A$'s response under the absorb-and-recover semantics differs from $A$'s response under the no-internal-recovery semantics. The difference, by construction, depends on $G_W$ — that is what makes the recovery "goal-aware." So the absorb-and-recover semantics produces a response distribution $P(A(q_M) \mid q_M, G_W)$ that is *not* conditionally independent of $G_W$ given $q_M$. (C3) fails structurally; the wrapping construction's $W_1$ guarantee is broken at the component level.

**Option B preserves (C3) by externalizing the recovery decision.**

When $A$ crashes on invariant violation, the wrapper's restart operation is the recovery. The restart operation is a *wrapper-level* operation, not a component-level one — it operates on $A$ from outside, with no $G_W$ argument (the restart strategy and intensity are fixed at wire-up). The wrapper *can* be goal-aware about whether to escalate or retry (its strategy-update map $f_G$ may consult $G_W$), but the component-level operation (instantiate fresh $A$ at $S_0$) is structurally goal-blind.

The wrapped state $X_W$ retains the structural decomposition $X_W = (M_W, G_W)$ across the restart event: $M_W$ updates only through $f_M$, whose type signature has no $G_W$ argument; $G_W$ updates only through $f_G$. The restart event itself is observed by both $f_M$ (the worker's response is now an exit signal rather than a normal completion — handled the same as any other observation) and $f_G$ (the wrapper's strategy may revise in response — e.g., decide to escalate vs continue), but each update path retains its type signature. Directed separation at the wrapper level is preserved by the wrapping construction's existing Theorem 1 / 2 argument — the restart did not change anything about which channels carry which arguments.

**The structural conclusion.**

Let-it-crash is *not a philosophical preference*. It is the operational realization of *structural commitment to (C3) preservation in the wrapped component*. The discipline says: do not put recovery code inside the worker; recovery code is goal-conditioned by construction; goal-conditioned recovery code inside the worker structurally breaks (C3) and breaks the $W_1$ wrapping guarantee. The supervisor — operating outside the worker, with its own typed restart-map and its own restart-intensity envelope — is the *only* place where recovery code can live without compromising the wrapping construction's structural directed-separation guarantee.

This is what `feedback_integration_is_replacement` requires the segment to surface sharply: the BEAM tradition arrived at *let-it-crash* on operational grounds (debugging time, fault-isolation strength), but the *structural argument for why it must be this way* is one of AAT's contributions to the analysis. The OTP analyses describe the mechanism; AAT names *what it is structurally* — the only way to preserve (C3) inside a wrapped Class-3-ish component is to keep recovery code outside the component.

**Boundary case (worth surfacing in the segment).** *Defensive programming at the trust boundary* — the well-recognized exception that let-it-crash *does not* apply at external system boundaries (network, user input, financial transactions) — is the structural-correctness companion. At the trust boundary, defensive validation is required to prevent corruption from propagating *into* the wrapped state. The boundary's defensive validation is itself a wrapping construction at the input layer: typed validators with no $G_W$ argument, runtime-enforced schema rejection on invariant violation, with the wrapper's parse-rejection logic playing the same role the supervisor's restart does at the worker layer. Inner-core vs trust-boundary is a clean structural distinction within the wrapping construction, and the discipline is consistent: inside the wrapping, crash-on-mismatch and let-the-wrapper-handle-recovery; at the wrapping's input boundary, validate-and-reject-on-mismatch. The latter is the *upstream* form of the former.

**Landing target.** This is the spike's most substantive contribution. It belongs in `#der-class-coercion-via-wrapping`'s Discussion section as a named sub-result: *Crash-early as structural commitment to (C3) preservation*. The argument above is segment-grade; the worked example (an OTP supervisor + GenServer demonstrating that putting recovery code inside the GenServer breaks the wrapping construction's $W_1$ guarantee, while letting the supervisor handle recovery preserves it) is short and informative.

The result is connected to `#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition" by the framing already in the segment (wrapping as truthification mechanism — the formal structural version of what defensive scaffolding does informally). Let-it-crash is the wrapping construction's discipline for *which side of the wrapping boundary* the recovery code must live on; the segment's existing connection to the meta-truthification picture is preserved and refined.

---

## 8. Honesty calls — what this spike does *not* claim

Per `feedback_integration_is_replacement`, the spike's body states present truth; the history layer (where the disciplines came from, which OTP traditions converged on what) belongs in the history layers (CHANGELOG, segment Working Notes, this spike file itself). The body of `#der-class-coercion-via-wrapping` after this spike's additions land should:

- *Not* claim AAT invented OTP supervision. The structural pattern was rediscovered by the Erlang/OTP tradition in the 1980s for telecom-reliability engineering, decades before AAT existed. Adopt the OTP vocabulary (*supervision, linking, monitoring, let-it-crash, application, restart strategies, restart intensity, stash*) per `feedback_prior_art_integration`. Cite Joe Armstrong's PhD thesis and the *Designing Elixir Systems with OTP* book (Gray & Tate) as the primary references for the operational substrate.
- *Not* claim let-it-crash is universally optimal. Cite the boundary case (defensive validation at trust boundaries) as the structural-correctness companion, per §7's boundary-case paragraph.
- *Not* claim the persistence-condition specialization in §3 is universally tight. The stationary-failure-rate assumption is named explicitly; the bursty-failure-distribution case is flagged as a candidate strengthening pass. The named hypotheses are exactly what the inequality holds under.
- *Not* deflate the §3 result to "synthesis." Per `feedback_math_novelty_recognition`: this is theorem-grade material — new result, established machinery, AAT-internal setting. Stating it under named hypotheses with the operational `max_restarts/max_seconds` form as its empirical estimator is the CS-norm precision pattern.
- *Not* claim the Conway's Law derivation in §6 is segment-grade. It is hypothesis-grade in this spike, with strengthening deferred to a follow-on cycle once the developer-tempo-channels segment lands.
- *Not* over-narrow the construction to BEAM. The structural content is substrate-agnostic; BEAM is one instantiation. The §4 BEAM-as-limiting-case observation is *about the cost coefficient*, not about whether the construction applies to other substrates.

The five Hoyle / generative-citation risks named in the mining file (FP-012 $\alpha \approx 0.2$, AXD-301 nine-nines, big-ROI numbers, $(1 + r)^n$ compound-interest framing, broken-windows $\alpha \approx 0.31$) are *not* lifted into segment content. The empirical anchors in this spike (5-microsecond BEAM spawn, two-decade production history, defaults of 3 restarts in 5 seconds) are reproducible figures from primary sources (Thomas, the BEAM source code, Armstrong's thesis), used as directional evidence rather than as quantitative constants in derivations.

---

## 9. Landing plan

The spike's six additions decompose into segment-grade additions to `#der-class-coercion-via-wrapping` plus a candidate appendix segment. Suggested landing structure for the strengthening cycle:

**Body of `#der-class-coercion-via-wrapping`:**

- A new Discussion sub-section *Wrapping sub-modes within $W_1$* covering Addition (1) (restart-strategy ↔ leakage-bound mapping). Three structural commitments at three widths; all $W_1$; the strategy choice encodes the wrapper's composite-level invariant.
- A new sub-result or Discussion paragraph for Addition (2) (stash pattern as state partition). The wrapped state decomposes into $X_W^\text{essential}$ ($W_1$) and $X_W^\text{ephemeral}$ ($W_2$), with additive leakage decomposition.
- A new theorem (or named result inside an existing theorem block) for Addition (3) (wrapper-level persistence condition). The inequality $\mathcal T_\text{wrapper} \gt \rho_\text{child} \lVert\delta_\text{failure}\rVert / \lVert\delta_\text{critical}^\text{wrapper}\rVert$ under named hypotheses, with `max_restarts/max_seconds` as the empirical-estimator corollary. *This is the theorem-grade contribution of the cycle.*
- A new Discussion sub-section *Crash-early as structural commitment to (C3) preservation* covering §7. The argument that absorb-and-recover-inside-the-component structurally breaks the wrapping guarantee; let-it-crash + supervisor restart is the only construction that preserves (C3) inside a wrapped Class-3-ish component.

**Worked-example footnote or strengthening paragraph in `#der-tempo-composition`:**

- Addition (4) (BEAM as limiting case): the wrapping-overhead decomposition $T_\text{wrapping-overhead} = K \cdot t_\text{per-call} + t_\text{instantiation} + t_\text{coordination}$, with BEAM driving $t_\text{instantiation} \to 0$ and the dominant remaining cost relocating to the developer-agent's $\mathcal T_\text{explore}$ channel.

**TST-side companion segment (candidate slug `#der-composite-developer-via-wrapping`):**

- Addition (5) (developer-AI-test-CI composite as AAT-side analog of OTP). Maps the OTP roles to the AI-augmented workflow's roles; classifies most current AI-augmented workflows as $W_2$; names the three structural commitments that bring the composite to $W_1$.
- Forward-references to the developer-agent segments (`#scope-developer-agent`) and the running-software-agent spike's outputs once they land.

**TST-side hypothesis-tier segment (candidate slug `#hyp-conway-law-as-guc-bound`):**

- Addition (6) (Conway's Law as GUC bound). Hypothesis-tier at first landing; strengthening pass deferred to a cycle that has the developer-tempo-channels segment landed.

**OUTLINE updates:** The body additions to `#der-class-coercion-via-wrapping` do not require OUTLINE changes (the segment is already in `01-aat-core/OUTLINE.md`). The TST-side additions (developer-AI-test-CI composite, Conway's Law) introduce new candidate-segment rows in `02-tst-core/OUTLINE.md`; whether these land as their own rows or as sub-results of an existing chapter is Joseph's call.

---

## 10. Assumptions that depend on sibling-spike resolutions

Per the launch brief: flag where this spike assumes structure sibling spikes will resolve.

**Assumption 1.** The wrapping construction extends cleanly to multiple wrapped components (LLM + ETS + stash + supervisor as a single composite), with per-component leakage decomposition and additive leakage at the composite level. *Source of assumption:* `spike-ets-as-third-w-regime.md` resolution (the W-regime classification applies per-component without modification). *Status:* resolved by that spike; this spike adopts the resolution.

**Assumption 2.** The wrapper-level persistence inequality (§3) is what the running-software-agent spike's `#der-runtime-persistence-condition` candidate uses as its prerequisite. *Source of assumption:* the running-software-agent spike is in flight; its persistence-condition derivation will cite this spike's §3 result as the underlying inequality. *Status:* clean seam; the running-software-agent spike should *cite* §3 rather than re-derive it. If the running-software-agent spike independently derives a different form, the two will need to be reconciled — the structural content is the same, only the named-variable instantiation differs (this spike: wrapper wrapping a component; running-service spike: service wrapping its dispatch table).

**Assumption 3.** The developer-tempo channel decomposition (`TST-IDEAS.md` A4) will provide the segment-grade content backing the Conway's Law derivation (§6). *Source of assumption:* the developer-tempo-channels spike is in flight; its $\mathcal T_\text{dev} = \mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$ decomposition is what the per-developer $\Sigma_t$-over-architecture argument depends on. *Status:* §6 is hypothesis-grade in this spike and should remain so until the developer-tempo-channels segment lands.

**Assumption 4.** The trust-boundary structural distinction (§7 boundary case) is consistent with whatever the running-software-agent spike says about defensive validation at the runtime layer's input boundary. *Source of assumption:* not yet resolved. *Status:* if the running-software-agent spike treats validation-at-boundary as a separate wrapping construction at the input layer, this spike's framing is consistent. If it treats validation-at-boundary as something else (e.g., a special case of let-it-crash applied to the boundary), the two will need to be reconciled in integration.

**Assumption 5 (open structural question, no sibling spike currently scoped).** The categorization rule for "essential" vs "ephemeral" state in the stash pattern (§2) is, in this spike, treated as a domain judgment. The cleaner theory-side framing — partition derived from a value-function on state subsets — is real theory work; not in scope for this spike, but worth surfacing for a future cycle. Flagging here so the placeholder is visible.

---

## 11. Provenance and convergence record

**Mining substrate (primary):** `spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` A1, A2, A3, A4, A5, A6, A7, A11, D1, D2, and the synthesis observation at the end of that file (the BEAM/OTP world as a retroactively validating worked-example zone for AAT).

**Mining corroboration (secondary):**

- `spikes/tst-mining-2026-05-21/01-release-it-mining.md` — Release-It! patterns (circuit breakers, bulkheads, steady-state, demand-control) as the broader pattern-language OTP fits within.
- `spikes/tst-mining-2026-05-21/02-forensic-mining.md` — forensic-refactoring corpus; corroborates the developer-agent side of the composite-developer-AI-test-CI composite.
- `spikes/tst-mining-2026-05-21/03-pragmatic-mining.md` — Pragmatic Programmer cluster; corroborates the Conway's Law derivation (§6) and the let-it-crash discipline (§7).

**TST-IDEAS launch substrate:** `TST-IDEAS.md` §A2 — the six concrete additions enumerated there are the spec this spike works to landing-grade.

**Convergence signal:** 4/4 agents from different starting points (Release-It! pattern-language, forensic-refactoring corpus, Pragmatic Programmer cluster, Elixir-composite corpus) independently identified the OTP-supervision-as-class-coercion mapping. Strongest single signal of the 2026-05-21 mining cycle per `feedback_convergence_as_framework_coherence_evidence`.

**AAT prior-art context (per the prior-art-integration discipline):**

- Joe Armstrong, 2003, *Making Reliable Distributed Systems in the Presence of Software Errors* (PhD thesis, KTH) — primary source for the let-it-crash discipline and the AXD-301 deployment context.
- James Gray and Bruce Tate, 2019, *Designing Elixir Systems with OTP* — primary source for the analysis-level operational decomposition (supervision strategies, stash pattern, restart-intensity envelope).
- Dave Thomas, 2018, *Programming Elixir* (1.6) — primary source for the million-process spawn benchmark (5-microsecond cold-spawn cost on 2011 hardware).
- Erlang/OTP design principles documentation (`erlang.org/doc/design_principles`) — primary source for the formal supervisor semantics.

The structural patterns predate Erlang — supervision-style fault-tolerance dates to telecom switching infrastructure of the 1970s — and apply across substrates. The Erlang/OTP tradition is the most-developed engineering codification, which is why the mining corpus is BEAM-heavy, but the analysis is substrate-agnostic per `CLAUDE.md` Key Architectural Decisions §6.

---

## 12. Status and next moves

**Spike status:** Open. Body content above is segment-grade for Additions (1), (2), (3), (4), (7-Honesty), and the boundary case in §7; hypothesis-grade for Additions (5) and (6). The §3 result is named theorem-grade per `feedback_math_novelty_recognition` and ready for promotion under the strengthening discipline.

**Integration sequence (suggested):**

1. Land Additions (1), (2), (3), (7-Honesty) into `#der-class-coercion-via-wrapping` (segment-body additions plus a new theorem).
2. Land Addition (4) as a strengthening paragraph in `#der-tempo-composition`.
3. After sibling spikes resolve: land Addition (5) as a candidate TST segment in the *composite developer-agent under AI augmentation* slot; cite this spike's results as prerequisites.
4. After developer-tempo-channels lands segment-grade: revisit Addition (6) and work to segment-grade as `#hyp-conway-law-as-guc-bound` or `#der-team-coupling-bounds-system-coupling`.

**Open questions for Joseph (per `feedback_ask_joseph_when_uncertain`):**

- §3 placement: theorem in segment body, or named demonstration appendix (e.g., `#deriv-wrapper-persistence-condition`)?
- §2 placement: surface the 2×2 partition ($\{M_W^\text{essential}, M_W^\text{ephemeral}\} \times \{G_W^\text{essential}, G_W^\text{ephemeral}\}$) in the segment body, or hold for a later cycle?
- §6 form: union, intersection, or weighted middle of per-developer $\Sigma_t$-over-architecture? (Affects exactly what the hypothesis-tier statement claims.)
- §5 segment slug: `#der-composite-developer-via-wrapping` or alternative naming?

---

## Working notes (not for segment landing)

The mining file's synthesis observation deserves preservation in this spike's history layer: the BEAM/OTP world is two decades of production engineering converging on patterns that match the structure AAT axiomatizes from first principles. *This is not because the BEAM designers were doing AAT; they were doing telecom-reliability engineering in the 1980s. It is because the structural problem AAT axiomatizes — how do you build a reliable composite from less-reliable components, while preserving certain class-of-agent properties at the composite layer? — has a unique-up-to-naming solution shape that any sufficiently mature production engineering tradition will rediscover.*

The Erlang/OTP tradition rediscovered it under the names *supervision, linking, monitoring, let-it-crash, application*. AAT's contribution is naming what those are structurally — and deriving what they have to be from first principles. Which has the practical effect of letting an engineer reason about new wrapping problems (LLM-developer agents, multi-agent AI compositions, distributed-AI ensembles) by transferring the discipline rather than rediscovering it. This is the kind of contribution that earns the framework the *integration* description it has held, while §3's theorem-grade result and §7's structural argument for crash-early are examples of AAT also being more than integration — purposeful invention in service of the theory.

The 2026-05-21 cycle's convergence signal is the strongest the mining program has produced. The strengthening pass on `#der-class-coercion-via-wrapping` documented here is the *direct cash-out* of that convergence. The remaining mining yield (running-software-agent, actuated-$\rho$-regulation, developer-tempo-channels, software-unmaintainability-bifurcation, substrate-modifying actions) is being worked in parallel spikes.
