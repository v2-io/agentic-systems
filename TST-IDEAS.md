# TST-IDEAS

*Candidate material for TST surfaced by the 2026-05-21 mining cycle of the ~960-analysis corpus at `~/src/_core/tst/planning/analysis/`. This is a substrate — not a TODO list and not a decided plan. Each entry names the structural shape of the candidate, where it would land in TST or AAT, what the convergence across mining agents was, and the honest read on what work is needed to land it.*

## How this file exists

Mining substrate is at [`spikes/tst-mining-2026-05-21/`](spikes/tst-mining-2026-05-21/), with the agent brief in `00-context.md` and four agent yields in `01–04-*.md`. Four parallel general-purpose subagents read the analyses for ~12–14 minutes each, structured findings by Class A (Joseph's named gaps) / B (worked instantiations of existing AAT machinery) / C (theory-side novel) / D (empirical anchors), and reported back. Total 81 findings, with strong convergence — 4/4 agents independently identified the OTP-supervision mapping; 3/4 agents converged on the runtime-as-agent direction, on the unmaintainability threshold, and on developer-tempo channel decomposition.

The convergence is the central methodological signal of this cycle. Per the framework's convention (`feedback_convergence_as_framework_coherence_evidence`), independent agents arriving at the same structural recognition from different starting points is evidence the pattern is in the framework, not just in one reader's head.

## Use posture

Three readings of this file are useful:

1. **Section §1 — Class A** for high-confidence segment-grade material that directly addresses gaps Joseph named or that are flagged as `--GAP--` in `02-tst-core/OUTLINE.md`. These are the strongest landings.
2. **Section §2 — Class C** for theory-side novel structure that earns its own OUTLINE slot once landed — but where landing requires real strengthen-before-soften work, not just instantiation.
3. **Sections §3–§4 — Class B / D** as a catalog of worked examples and empirical anchors that strengthen existing segments rather than warrant new ones.

The §5 Honesty section names where the corpus systematically misleads — mostly through fitted-to-narrative quantitative constants and through BEAM/OTP-substrate over-narrowing of substrate-agnostic patterns. The §6 OUTLINE-update proposals are the concrete editorial suggestions a future cycle can act on. §7 names the highest-priority spike candidates.

---

## §1 — Class A: gaps Joseph named, or `--GAP--` flagged in OUTLINE

### A1. The running software service as an adaptive-actuated agent (new chapter)

**Convergence.** 3/4 agents (Release It!, Pragmatic, Elixir-composite).

**The picture the mining converges on.** A deployed running service — GenServer + supervisor + circuit breakers + retry layer + load balancer + telemetry + autoscaler — instantiates AAT's $(M_t, O_t, \Sigma_t)$ machinery at the runtime layer. $M_t$ is the GenServer state, in-memory caches, connection-pool counts, circuit-breaker states, traffic-rate estimates. $\Omega_t$ is the request stream plus dependency-service behavior. $O_t$ is the SLO bundle (uptime, latency tail, correctness invariants). $\Sigma_t$ is the operational playbook encoded in code: retry, fail-over, shed, throttle, restart, blue/green, route-around. Observations come through the telemetry / health-check / request-arrival stream. Actions span internal recovery (open breaker, restart actor, scale pool) and external moves (return 503, blue/green swap, drain).

**Candidate segments (4):**

- `#scope-running-software-agent` — running service as $(M_t, O_t, \Sigma_t)$ with substate mapping. Parallels `#scope-developer-agent`.
- `#def-runtime-observation-channels` — telemetry / health-check / request-stream / control-plane-RPC, each with $(\nu^{(k)}, U_o^{(k)})$ profile and $\eta^{(k)\ast}$.
- `#der-runtime-persistence-condition` — $\mathcal T_\text{runtime} \gt \rho_\text{env}/\lVert\delta_\text{critical}\rVert$ for a service, with $\rho_\text{env}$ as environmental disturbance rate (request variance, dependency outage, traffic shift) and $\delta_\text{critical}$ as tolerable SLO drift.
- `#der-runtime-tempo-decomposition` — $\mathcal T_\text{runtime} = \mathcal T_\text{sense} + \mathcal T_\text{decide} + \mathcal T_\text{actuate}$, with matrix-Loewner weakest-channel bottleneck. Closes the developer-tempo gap (A4) by giving its runtime sibling.

**Where it lands.** Most naturally a new Ch.5 in `02-tst-core/` paralleling Ch.2 (the Developer Agent). The Release-It! patterns from Agent 1 are the substrate; Agent 4's GenServer A6 finding provides the concrete callback mapping.

**Honesty call worth surfacing now.** *Vanilla GenServers are closer to Tier-1 reflex than Tier-3 agent.* The structural commitment to make running services genuinely-AAT-agent rather than just static-dispatch machines is the *adaptive dispatch* property: rate limiters that adjust throttling, circuit breakers that change state, autoscalers that update replica counts, sidecars that route based on observed health. Without adaptive dispatch the running service is a fixed-strategy controller, which AAT's Part-I machinery covers but does not need the full Part-II purposeful-substate treatment. The chapter should name this distinction explicitly — TST instantiates the actuated-adaptive-agent picture only for the *adaptive-dispatch* class of running services, and the fixed-strategy class falls under Part I directly.

**Connection to Joseph's broader framing.** Joseph's framing of TST as "the software project with its own agentic properties (as it adapts and holds a model [code] of reality [runtime effects] and goals [pipelines, todos, etc.] and updates etc.)" is *larger* than this chapter — the software project as a whole is a composite of (developer + AI + running service + tooling + infrastructure). Ch.5 here is one component of that composite, not the whole thing. The full software-project-as-agent treatment is A2 below.

---

### A2. The composite developer-agent under AI augmentation (chapter extension)

**Convergence.** 4/4 agents — strongest single mining convergence.

**The picture the mining converges on.** OTP supervision trees are the textbook industrial implementation of `#der-class-coercion-via-wrapping`. A worker process is a Class-3-ish (potentially-coupled, mutable-state, can-die-arbitrarily) component; the supervisor wraps it with a discipline that promises "this child returns to $S_0$ on crash; affected siblings are scoped to the restart strategy; restart-intensity limits cap propagation of repeated failure into the parent." The whole tree is a Class 1 (Separated) composite by structural commitment, even though every individual worker has no such property in isolation. Two decades of production telecom-grade systems have converged on this construction under different vocabulary — *supervision, linking, monitoring, let-it-crash, application*.

**What this lifts into TST/AAT — six concrete additions:**

1. **Strengthen `#der-class-coercion-via-wrapping`** with OTP supervision as the canonical engineering example. The restart-strategy ↔ leakage-bound mapping spells out as: `:one_for_one` is the W₁-tightest leakage bound (single-worker damage); `:rest_for_one` propagates structurally to downstream-started workers (wider leakage); `:one_for_all` is widest, paid for by stronger coherence guarantees among siblings (consensus groups). The restart-intensity envelope (`max_restarts / max_seconds`) is the escalation rule when the tightest wrapping cannot maintain its leakage bound.
2. **Refine the segment** with the *stash pattern* as a state partition: the wrapper splits its own state into $S_{\text{essential}}$ (in W₁ regime — structurally preserved across worker resets) and $S_{\text{ephemeral}}$ (in W₂ regime — behavioral loss bounded by failure rate × volume-lost-per-failure).
3. **Land restart-intensity as the strategic-persistence bound at the wrapper level.** $\mathcal{T}_{\text{wrapper}} = 1/\text{restart-time}$ (microseconds on BEAM); $\rho_{\text{child}}$ is the child failure rate; $\lVert\delta_{\text{critical}}\rVert$ is the per-failure damage tolerance. The `max_restarts/max_seconds` envelope encodes the *strategic-persistence* boundary: outside it the wrapper's coercion construction no longer holds and the wrapper escalates. This *directly answers Joseph's "what is $\rho$ for a microservice?" question and closes the OUTLINE Ch.4 software-persistence gap.*
4. **Recognize BEAM as the *limiting case* of class-coercion-via-wrapping** where wrapping tempo cost approaches zero (microsecond-scale process spawn). The Brooks's-Law tempo-composition inequality is preserved but the cost coefficient is dominated by *human* coordination overhead (defining message protocols, debugging supervision hierarchies), not by runtime process-spawn cost. This is genuinely strengthening for `#der-tempo-composition`.
5. **Treat the composite developer-AI-test-CI system as the AAT-side analog** of OTP. The AI assistant is a Class 3 (Coupled) component (its belief-update is irreducibly goal-conditioned on the prompt). The composite is Class 1 (Separated) when (a) the AI's outputs flow into typed/parsed structures (structural commitment), (b) those are validated against goal-blind invariants (tests, type-checks, contracts), (c) invariant violations crash early rather than being silently absorbed, (d) the wrapping supervisor (developer + CI pipeline) restarts the AI on failure with bounded retries. This is W₂ in most current AI-augmented workflows; W₁ accessible when the AI is constrained to typed completion with rejection-on-parse-failure.
6. **Land Conway's Law as a GUC-class bound on multi-developer composites.** A team with high inter-member coupling produces a system with high inter-module coupling — the team operates as a Class-3-like composite, and the system inherits the structural coupling. Conway's Law in AAT vocabulary: *the system's GUC class is upper-bounded by the team's GUC class*. Derivation is plausible but not yet worked: probably via the developer-agent's $\Sigma_t$ being rich along communication paths the developer can access and impoverished along paths the developer cannot, with the system architecture emerging as the union.

**Where it lands.** Most directly as a chapter extension under Ch.2 (*Developer Agent*) in `02-tst-core/`, or as a new chapter after Ch.5 (A1) if a dedicated composite-agent treatment is warranted.

**Honesty calls.** (a) OTP supervision is W₁ when worker state is disposable (BEAM's per-process heaps make this trivially true); whether it is W₁-exact or W₁-in-the-limit needs care when transferred to substrates without disposable per-component state. (b) Crash-early as *structural commitment to goal-blindness* is a substantive claim that needs derivation: why does recovering-from-invariant-violations leak goal-state? The argument is that recovery code is goal-conditioned (it knows what the higher-level operation was trying to do), so absorbing failures inside the worker reintroduces the coupling the wrapping was meant to break. This needs a real spike, not just an assertion. (c) ETS (Erlang Term Storage) provides controlled shared-memory and is a *deliberate exception* to actor-model isolation — see C5 below for whether this constitutes a third W regime or a degenerate W₂.

---

### A3. Software persistence — the unmaintainability threshold (closes OUTLINE Ch.4 gap)

**Convergence.** 3/4 agents (Release It!, forensic, Pragmatic).

**The picture the mining converges on.** The forensic-cycle (Tornhill + North) gives the OUTLINE Ch.4 gap a *bifurcation* form: code health is *bimodal* in age. **G1** (recent, age $\lt \sim 30$ days) — knowledge fresh in developers' heads (Ebbinghaus $K(t) = K_0 e^{-t/\tau}$ with $\tau \approx 20$ days for code-knowledge), comprehension cheap. **G3** (old stable, age $\gt 1$ year) — no longer modified, comprehension unnecessary. **G2** (middle-aged, 30 days $\lt \text{age} \lt 1$ year) — knowledge faded but the code still requires modification. *G2 is the danger zone.* Empirically (Tornhill 2018, 2024): G2 files have several-times higher defect rates than G1 and G3, refactoring effort there pays back fastest.

**The structural form.** Developer-channel persistence requires *either* the developer's local $M_t$ to be fresh (recent contact, low $U_o$) *or* the code's local $\rho$ to be near zero (no incoming change pressure); the G2 region violates both, with $U_o$ rising via Ebbinghaus decay faster than $\rho$ has dropped. The chain $Q \to U_o \to \eta^\ast \to \mathcal{T}$ (already in `#der-code-quality-as-observation-infrastructure`) composes forward with the persistence inequality $\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$: codebases below the persistence threshold enter the regime named *unmaintainable* in a precise sense. The bifurcation is `#der-code-quality-as-observation-infrastructure`'s vicious-cycle hypothesis with an empirical shape.

**Candidate segment.** `#hyp-software-unmaintainability-bifurcation` or `#result-software-persistence-bifurcation` under Ch.4. Status starts at *hypothesis* tier; strengthening attempts target *robust qualitative* with the bimodal-age-distribution empirical anchor and *conditional* once the bifurcation is derived from logistic-with-contagion dynamics under stated conditions.

**Empirical anchors.** Tornhill's age-bimodality observation across .NET Core (`gc.cpp`), Linux (Intel graphics driver), Android (ActivityManagerService) case studies. Pragmatic's broken-windows cluster with the $\alpha \approx 0.31$ tech-debt-contagion claim — *flagged: generative-citation risk*, the "2024 research" cited in analysis 004 has no primary source and needs either tracking-down or downgrading to hypothesis-pending-anchor before landing in TST.

**Honesty.** The Ebbinghaus $\tau \approx 20$ days is from the original human-memory literature applied to text; its transfer to code-comprehension is plausible but unvalidated. The bimodality claim — that there is a danger-zone in the middle — is the structural content that survives translation; the specific constants are decorative. The strengthening attempt should be made first per Joseph's working convention: the bifurcation is generic to logistic-with-contagion dynamics, and deriving it under stated conditions is the strengthening-before-softening move.

---

### A4. Developer-tempo channel decomposition (closes OUTLINE Ch.2 gap)

**Convergence.** 3/4 agents (Release It! sibling, forensic, Pragmatic).

**The picture the mining converges on.** The OUTLINE Ch.2 gap $\mathcal T_\text{dev} = \mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$ has three concrete operationalizations:

1. **Probe-class typology (Pragmatic).** $\mathcal{T}_{\text{probe}}$ decomposes by probe-class $k \in \{\text{tracer}, \text{prototype}, \text{e2e}, \text{perf}, \text{ui}, \text{spike}\}$, each with its own $(\nu^{(k)}, \eta^{(k)\ast})$ — sampling rate and Bayesian gain on the targeted facet of $M_t$ or $\Sigma_t$. Disposability ($t_{\text{convert}} \gt t_{\text{reimplement}}$) is a *purity guarantee* on the probe analogous to (but structurally distinct from) AAT's W₁/W₂ leakage discipline.
2. **Chronicle-derivable channel separation (forensic).** $\mathcal T_\text{probe}$ from test-only-changing commits; $\mathcal T_\text{explore}$ from scratch-branch + revert-rate; $\mathcal T_\text{obs}$ from code-review duration (when tracked) or proxy via commit-message-comprehension-references. The chronicle's P5 exact recording (per `#obs-software-epistemic-properties`) makes the channels separable post-hoc.
3. **Matrix-Loewner weakest-channel bottleneck.** The developer's overall adaptive tempo is bounded by the weakest of the three channels — high $\mathcal T_\text{obs}$ with absent $\mathcal T_\text{probe}$ means a developer who reads the code fast but cannot verify what they have read.

**Candidate segment.** `#def-developer-tempo-channels` under Ch.2, with the per-channel $(\nu, U_o)$ tables and the chronicle-derivable operationalizations. The W₁/W₂ analogy for probe disposability lives in Discussion, *flagged as needing care* — disposability and goal-blindness are structurally different and conflating them would be a category error.

**Honesty.** The chronicle gives evidence of *what* developers committed, not *how long they spent reading* before committing. Reconstructing $\nu_\text{obs}$ from the chronicle requires an additional assumption that observation activity scales with commit activity (or with code-review-comment activity for projects that use PR review). The cleanest reconstruction is $\mathcal T_\text{probe}$ (test changes are auditable from filename); $\mathcal T_\text{explore}$ is murkier; $\mathcal T_\text{obs}$ requires explicit instrumentation that the chronicle alone does not provide.

---

## §2 — Class C: theory-side novel structure

### C1. Actuated $\rho$-regulation (new AAT segment)

**Source.** Release It! mining (Agent 1, A6).

**The structural claim.** Most AAT discussion of the persistence condition treats $\rho$ as exogenous: the environment imposes a disturbance rate, the agent must maintain tempo above the threshold. The Release It! demand-control patterns invert the picture: a running agent has actions in its repertoire that *modulate* its own incoming $\rho$. Backpressure is the agent slowing its upstream producer. Load shedding is the agent refusing observations entirely. Handshaking is the agent declaring its capacity so cooperative producers self-throttle. Token-bucket and leaky-bucket are specific implementations.

**The persistence condition becomes** $\mathcal{T} \gt \rho_{\text{effective}} / \lVert\delta_{\text{critical}}\rVert$, with $\rho_{\text{effective}} \le \rho_{\text{offered}}$ achievable via admission-control. The cost is a *satisfaction-gap* (work refused) — i.e., the agent pays in $O_t$-shortfall to preserve $\mathcal{T}$-feasibility. Self-denial-attack failures are the regime where $\rho$ spikes beyond what tempo can absorb *and* the agent lacks the actuation to push back.

**Where it lands.** New AAT segment in `01-aat-core/` — `#disc-rho-actuation` or `#deriv-actuated-disturbance-rate` formalizing the agent's action space as having an admission-control component that modulates $\rho_{\text{effective}}$ from $\rho_{\text{offered}}$. TST instantiation (`#example-backpressure-as-rho-actuation`) in the runtime-agent chapter (A1).

**This is the highest-yield genuinely-new-AAT-structure finding in the entire mining cycle.** Spike-grade work needed to land cleanly: the agent must have a refusal-action in its actuation repertoire, which is non-trivial at internal-component boundaries; the formalization of $\rho_{\text{effective}}$ as the *agent's perceived environmental disturbance rate* (not the queueing-theoretic arrival rate) needs care; the connection to the existing satisfaction-gap / control-regret split in TST is structurally clean but needs derivation.

---

### C2. C4 confounder — observer-effect / Goodhart (extends `#hyp-causal-discovery-from-git`)

**Source.** Forensic mining (Agent 2, F1 + F3).

**The structural claim.** When performance evaluation uses git-derived metrics, developers adapt their behavior to optimize the *measured* quantity, opening a wedge $D_{KL}(v_m \Vert v_r)$ between measured and real productivity. This is a new confounder class distinct from C1/C2/C3:

- **C1 (shared requirements):** common causes drive co-changes — already in segment.
- **C2 (convention-driven bundling):** developers group changes for organizational reasons — already in segment.
- **C3 (developer knowledge state):** developer's $M_t$ shapes inclusion — already in segment.
- **C4 (observer-effect / Goodhart) — NEW:** the metric system itself changes the chronicle's substrate. Measurement and reality become unidentifiable along a degenerate parameter direction — *literally* a fresh M1-identifiability-floor instance with a concrete domain anchor.

**Where it lands.** One-paragraph update to `#hyp-causal-discovery-from-git`'s confounder list. Strongest framing: when git history is used for performance evaluation, the chronicle ceases to be a clean record of developer interventions and becomes a record of joint developer-and-metric-system behavior. Causal identifiability collapses by the M1 mechanism.

This is also a *worked example for M1* with an immediate concrete domain anchor — provides a non-toy "you cannot get there from here without further interventions" example for `#disc-identifiability-floor`.

---

### C3. Substrate-modifying action class (macros / metaprogramming)

**Source.** Elixir-composite mining (Agent 4, C1).

**The structural claim.** `#scope-developer-agent` currently names four action classes: exploration, interventional probes, queries, environment modification. *Modify the language* sits below all four — it changes the substrate over which the other classes operate. For AI-coding agents, this is the dominant axis of action-space expansion: a generative AI's effective action space grows substantially when the language gives it macros / DSLs / metaprogramming tools that let it express complex transforms compactly. The macro-hygiene system is itself a wrapping construction at the language layer.

**Where it lands.** New action class in `#scope-developer-agent`, or a companion segment `#disc-substrate-modifying-actions`. Strong bridge to 03-llm-core on AI-developer action spaces.

**Honesty.** This is genuinely new ground — neither the analyses nor current TST has formalized "modify the language" as a distinct action class. The proposal needs real theory work: what is the structural difference between an action that modifies *runtime state* (current class 4) versus an action that modifies *the legible-action-space itself* (the language)? The analogy to consciousness-infrastructure work — where the substrate is the LLM's training and the action class is "modify the prompt template the future-self operates over" — is suggestive enough that this might bridge TST and 03-llm-core in a load-bearing way.

---

### C4. Multi-scale persistence in software

**Source.** Pragmatic mining (Agent 3, #9 — reversibility / architecture-flexibility).

**The structural claim.** Reversibility is preservation of optionality on the strategy DAG $\Sigma_t$ — an abstraction layer maintains a wider set of feasible architectural strategies at a cost in current overhead. The break-even has the same shape as `#der-change-investment` but specialized to *architectural* changes rather than feature changes. The architectural-volatility rate $\mu \approx 0.3$ (major shift every ~3 years) is a candidate empirical anchor for *environmental disturbance rate* at the architecture scale.

**The candidate hypothesis-tier segment.** Software has *multiple scales* of environmental volatility — feature-scale $\rho$, architecture-scale $\mu$, possibly platform-scale (decade-timescale). The persistence condition must hold at *each* scale separately, with the tightest binding the codebase's overall maintainability.

**Spike-worthy.** Not yet a segment.

---

### C5. ETS / scoped-shared-state as candidate W₁.5 regime (spike-worthy)

**Source.** Elixir-composite mining (Agent 4, A10).

**The structural question.** ETS provides lock-free shared memory outside any single process's heap. The actor model's strict isolation invariant is *deliberately broken* for ETS-table-contents. The access-control matrix (`private` / `protected` / `public`) is a scoped exception to directed separation.

Is this a *third* W regime — "W₁.5 — structural commitment with a named exception region" — or a degenerate W₂ where the shared region is the leakage and the access-control matrix specifies the rate-bound? The analyses do not address this. The ETS pattern is empirically widespread (every production BEAM system uses ETS for caches and shared lookup tables), so this is not a corner case.

**Where it lands.** Spike-worthy question for `#der-class-coercion-via-wrapping`. If a third regime is warranted, AAT segment needs updating; if W₂ subsumes it under a generous reading, the segment stays as-is with a Discussion paragraph noting controlled escape hatches.

---

### C6. Compile-time data-to-code as $\Sigma_t$-vs-$M_t$ partition (spike-worthy)

**Source.** Elixir-composite mining (Agent 4, C2).

**The structural question.** Compile-time generation moves *runtime-mutable* state into *compile-time-fixed* strategy-DAG structure. The trade-off — flexibility versus tempo — has clean AAT vocabulary in `#der-tempo-composition` but is not currently surfaced for the *strategy-structure-versus-state* axis. Does AAT have machinery for the static-vs-dynamic strategy-structure axis?

**Spike-worthy.** Not yet ready to land.

---

### C7. Property-based testing as Level-2 distributional access

**Source.** Elixir-composite mining (Agent 4, C3).

**The structural claim.** Standard example-based tests give Level-2 interventional access at specific input points; property-based tests give Level-2 access *across* a generator-defined input distribution, more closely approximating $do(X = \cdot)$ over a range. The shrinking step identifies the minimal-counterexample boundary of the property's domain of validity.

**Where it lands.** Refinement paragraph in `#obs-software-epistemic-properties` P2 distinguishing example-based from property-based test access. Small finding, useful.

---

### C8. Knowledge portfolio as developer-$M_t$ long-horizon dynamics

**Source.** Pragmatic mining (Agent 3, #4).

**The structural claim.** The developer's $M_t$-content for technology $i$ evolves under: (a) acquisition $k(t) = k_{\max}(1 - e^{-\mu t})$; (b) Ebbinghaus depreciation $\text{retention}(t) = e^{-t/S}$ multiplicatively combined with market-value depreciation; (c) technology S-curve adoption $\text{adoption}(t) = L/(1 + e^{-k(t - t_0)})$; (d) inter-technology correlation $\rho$ giving learning synergy $\text{cost}(k_2 \mid k_1) = \text{cost}(k_2)(1 - \rho k_1)$; (e) portfolio-theoretic risk-return optimization. Critical thinking is the developer's *signed-coupling-aware update* — sources with high bias-correlation get classified as structural-shock and trust-weighted down.

**Where it lands.** Candidate chapter section or extended segment on "Developer long-horizon adaptive dynamics" between Ch.2 (feature-scale time decomposition) and Ch.4 (system measures). Alternatively, the technology-adoption strand suggests a logogenic-bridge piece in 03-llm-core — what an AI developer-agent's $M_t$-decay looks like across substrate versions.

**Honesty.** The portfolio-Sharpe-ratio framing is *evocative* rather than *isomorphic*. Mapping to AAT requires the AAT-native formulation: the developer's $\Sigma_t$ over learning investments as a probabilistic causal DAG with AND/OR nodes and uncertainty-ratio updates. Spike-worthy.

---

### C9. Conway's Law as GUC-class bound on multi-developer composites

**Source.** Pragmatic mining (Agent 3, #5).

**The structural claim.** Conway's Law: $\text{Distance}(S, T) \to 0$ as project age increases, where $S$ is system architecture graph and $T$ is team communication graph. In AAT vocabulary: *the system's GUC class is upper-bounded by the team's GUC class*. Team with high inter-member coupling produces system with high inter-module coupling — operating as Class-3-like composite, system inherits the structural coupling.

**Where it lands.** Companion segment to A2 — `#hyp-conway-law-as-guc-bound` or `#der-team-coupling-bounds-system-coupling`. Requires derivation: why does team-graph structure impose itself on system-graph? Likely via per-developer $\Sigma_t$ being rich along available communication paths, impoverished elsewhere, with the system architecture emerging as the union.

---

### C10. Transformational programming as coupling-floor at code-unit level

**Source.** Pragmatic mining (Agent 3, #7).

**The structural claim.** Pure-function pipelines achieve $t_{\text{coord}} = 0$ between code units (no shared state means no synchronization). This is Class-1-like at the *code-unit level*. OO with rigorous Tell-Don't-Ask discipline is Class-2-like (bounded coupling at module boundaries). Shared-mutable-state OO is Class-3-like (structurally guaranteed coupling, only patchable behaviorally via locks, transactions, defensive copies).

**Where it lands.** Strengthens `#def-system-coupling` with the recursive observation: AAT's GUC classes apply at the agent level; this extends the same class-typology to the code-unit-within-codebase level. Worth a hypothesis-tier extension or a Discussion paragraph.

**Honesty check needed:** whether the parallel is structural (same machinery, different scope) or merely analogical (similar dynamics, different formalism).

---

### C11. Crash-early as structural-commitment for running services

**Source.** Pragmatic mining (Agent 3, #10) + Elixir-composite (Agent 4, A7).

**The structural claim.** Crash-early + supervised restart is the operational realization of *structural commitment to directed separation at the runtime layer*. Recovering from invariant violations *inside* a worker would require the worker to reason about goal-state to know what recovery is appropriate, which leaks goal-state into the belief-update path and breaks Class 1 status. Crashing instead delegates recovery to the supervisor; the worker stays Class 1, the wrapper stays Class 1, the composite remains class-coerced via wrapping.

**Where it lands.** Strengthens `#scope-continuous-operation` and the candidate `#scope-running-software-agent` from A1. Let-it-crash is the *philosophical commitment* that, given the choice, the time-optimal recovery strategy is the one driving $T_{\text{recovery}}$ down faster than $P(\text{fail})$ can be driven down — `#post-temporal-optimality` restated for running services.

---

### C12. Frequency-asymmetry + lagged co-change as residual causal signals

**Source.** Forensic mining (Agent 2, F5).

**The refinement.** `#meas-coherence-coupling` currently defines a symmetric estimator. Three forms with strictly different identifiability: *symmetric* co-change (descriptive); *asymmetric directed* $P(\Delta j \mid \Delta i)$ (interventional in favorable regimes, survives common-cause confounding by asymmetry); *temporally-lagged* $P(\Delta j \mid \Delta i, \Delta t \gt 0)$ (Granger-like, stronger interventional signal under additional regularity).

**Where it lands.** Discussion paragraph in `#meas-coherence-coupling` distinguishing the three forms and pointing at `#hyp-causal-discovery-from-git` for the residual-causal-signal interpretation.

---

### C13. Multi-repo virtual-root failure of P5 exteriorization

**Source.** Forensic mining (Agent 2, F13).

**The refinement.** P5 in `#obs-software-epistemic-properties` states that software's committed-state chronicle is partially exteriorized with cryptographic immutability. *The "partially" is important* — across repository boundaries, the exteriorization fails. There is no single hash-chain over the joint state. For distributed systems, the high-identifiability calibration-lab status partially degrades to the additional-transfer-assumption regime other domains live in.

**Where it lands.** Discussion paragraph in `#obs-software-epistemic-properties` noting P5's "exact recording" is repo-local; cross-repo causal claims face an identifiability problem similar to M1 / M3 patterns. The virtual-root reconstruction technique is itself an additional intervention the segment's framing should make explicit.

---

## §3 — Class B: worked instantiations for existing AAT machinery

These are useful as Discussion paragraphs in existing segments. They do not warrant new segments but do anchor existing claims.

- **Actor model debugging $O(n^2) \to O(n)$** anchors `#der-code-quality-as-observation-infrastructure` for cross-component-coupling-driven $Q$ degradation. (Pragmatic #11, Elixir B1.)
- **Error-as-data + `with` chain** as $H_b$ minimization at the comprehension layer. (Elixir B2.)
- **Protocols / polymorphism** as developer-agent action-class-4 extension keeping changeset size low for likely future changes. (Elixir B3.)
- **Layered architecture (data → functional core → tests → boundaries → lifecycle → workers)** as `#hyp-conceptual-alignment` instantiation with file-system / import-graph isolation as substrate. (Elixir B4.)
- **Hot code swapping** as zero-$T_{\text{recovery}}$ limit case of `#scope-continuous-operation` with developer-side $t_c$ cost during multi-version transition. (Elixir B5.)
- **Telemetry / observability** as the running service's observation function $h$ being made explicit; same $Q \to U_o \to \eta^\ast$ chain applies. (Elixir B6.)
- **Resource-balance (allocation-deallocation co-located)** as `#der-change-proximity-principle` instantiation at resource-lifecycle scale. (Pragmatic #12.)
- **Communication-quality / audience analysis / engineering daybooks** as AAT signed-coupling-aware sending + IB-compressed externalized $M_t$. (Pragmatic #13.)
- **Design-by-contract + assertions + crash-early** as unified invariant-probe + structural-commitment discipline. (Pragmatic #14.)
- **Finite-state machines** as $\Sigma_t$-as-data implementations. (Pragmatic #15.)
- **Process linking / monitoring** as the directed-vs-bidirectional failure-coupling primitive in `#der-class-coercion-via-wrapping`. (Elixir A11.)
- **Distributed Erlang** as cross-node wrapping with millisecond-scale tempo cost — empirical calibration for `#der-tempo-composition` at network scale. (Elixir A12.)
- **Process-pool patterns (Poolboy, `Task.async_stream`)** as Brooks's-Law inflection-point calibration for `#der-tempo-composition`. (Elixir A9.)
- **Tornhill's hotspot $H = f \cdot c$** as principled-decision-integration with chronicle-estimated $\lambda(F_i)$ concentrated on observed-hot files. (Forensic F4.)
- **Tornhill mock-complexity blowup** as $U_o$ destruction signal on the test-probe channel. (Forensic F11.)
- **Tornhill rising-hotspot** as non-stationarity refinement to `#der-change-expectation-baseline`. (Forensic F12.)
- **Cone-of-uncertainty + PERT** as developer-planning Kalman update. (Pragmatic #18.)
- **DSLs** as semantic-distance-collapsing wrappings strengthening `#hyp-conceptual-alignment`. (Pragmatic #8.)
- **Steady-state pattern** as runtime persistence-via-bounded-state. (Release It! A7.)
- **Bulkheads** as failure-domain $M_t$ identifiability commitment (M1 instance at runtime layer). (Release It! A4.)
- **Chaos engineering** as Pearl-Level-2 probing under deliberate disturbance at the runtime layer. (Release It! A10.)

---

## §4 — Class D: empirical anchors (citation-pending)

These provide directional empirical support for hypothesis-tier segments. *Each carries citation-tracing risk — generative LLMs invent specific constants.* Land with citation-pending flag and primary-source verification before treating as anchor-grade in any segment.

- **Tornhill Microsoft Research finding** — organizational metrics predict defects at $r \approx 0.7$–$0.8$, code-level metrics at $r \approx 0.2$–$0.3$. (Forensic F7.) Real citation; range varies between papers. Useful anchor for `#meas-coherence-coupling` Discussion.
- **Code-age defect decay** $D(c, \text{age}) \approx D_0 e^{-\text{age}/365}$ — survival-as-quality-filter. (Forensic F8.) Anchor for A3 bifurcation.
- **150-commit minimum chronicle-derivable signal** — anchor for `#meas-coherence-coupling` data requirements. (Forensic F14.) Specific constant gestural; order of magnitude robust.
- **BEAM 5 $\mu\mathrm{s}$ cold-spawn cost / 1M processes in ~5 s** — anchor for A2 point 4 (BEAM as limiting case of wrapping). (Elixir D2.) Reproducible.
- **AXD-301 "nine nines" telecom uptime** — directional anchor for supervised-actor architecture in production. (Elixir D1.) Widely-quoted but lightly-sourced; cite as "high uptime reported in production telecom systems" rather than as a specific number.
- **Architectural-volatility $\mu \approx 0.3$** (major shift every ~3 years) — candidate anchor for multi-scale $\rho$ (C4). (Pragmatic #17.) Iron→clusters→cloud→containers→serverless sequence is real; point estimate gestural.
- **PERT cone-of-uncertainty** (4× start → 2× at 20% → 1.25× at 50%) — anchor for developer-planning Kalman-update form. (Pragmatic #18.) McConnell *Rapid Development* primary source.
- **Pair-programming bug-catch rate $\approx 0.4$–$0.6$ + asymmetric trust dynamics** (losses 3× larger than gains) — anchor for Conway's Law / team-coupling. (Pragmatic #19.) Numbers gestural.
- **Tornhill $H = fc$ exponents** $\alpha \approx 0.3, \beta \approx 0.7$ — vary between analyses with no shared source. Useful directionally, not as point estimates. (Forensic F4.)
- **Broken-windows $\alpha \approx 0.31$ tech-debt-contagion** — *citation-pending, generative-citation risk*. The "2024 research with 29 developers" cited in Pragmatic analysis 004 has no primary source. Track down or downgrade before landing. (Pragmatic #16.)

---

## §5 — Honesty calls — where the corpus systematically misleads

The mining task is to extract structural content that survives translation into AAT. Several patterns in the corpus look like findings but are decoration:

- **FP-012's $(1 + \alpha)^{\text{discontinuities}}$ with $\alpha \approx 0.2$** appears across virtually every analysis where comprehension cost is mentioned. The $\alpha = 0.2$ constant is *not derived anywhere in the corpus* — it propagates as a stock framing. The exponential-cognitive-load hypothesis as a *structural* claim survives (see `#hyp-exponential-cognitive-load`); the specific constant does not.
- **Big ROI / multiplier numbers** — circuit breaker "23× ROI," actor model "10–100× debugging speedup," supervisor tree "exponentially reduced cascade probability," AXD-301 "nine nines uptime" — these are hyperbolic. Treat as directionally indicative; do not cite as empirical evidence.
- **"$(1 + r)^n$ compound interest" framing for technical debt** appears across the broken-windows and code-age clusters. *Metaphor sold as derivation.* The bifurcation in `#der-code-quality-as-observation-infrastructure` is real; the compound-interest specific functional form is decorative.
- **BEAM/OTP framing over-narrowing** — many analyses present circuit breakers, supervision trees, actor isolation as BEAM-invented when the patterns predate Erlang and apply more generally. The structural content is substrate-agnostic; the BEAM framing is one instantiation, not the source.
- **Generative-citation risk** — LLM-authored secondary analyses occasionally invent specific empirical citations ("2024 research with 29 developers...") that have no primary source. The $\alpha \approx 0.31$ broken-windows claim is the most prominent instance; the AXD-301 nine-nines number is widely-quoted but lightly-sourced. Before landing any specific constant in TST as anchor-grade evidence, the primary source must be tracked down or the claim downgraded to hypothesis-pending-anchor.

---

## §6 — Recommended OUTLINE updates

Cautious — Joseph's compact about peer-voice and discipline applies; the mining surfaces strong candidates but OUTLINE changes commit the project's structural direction and warrant his eyes before landing.

**Strong-confidence candidates for `02-tst-core/OUTLINE.md`:**

1. **New chapter slot Ch.5 — *The Running Software System as Adaptive Agent*** with `--GAP--` rows for the four candidate segments named in A1 above. Convergence: 3/4 agents.
2. **Resolve the existing Ch.4 `--GAP--` "Software persistence: the unmaintainability threshold"** by adding `#hyp-software-unmaintainability-bifurcation` as the candidate-segment row, with A3 above as the substrate. Convergence: 3/4 agents. *(Done this cycle — the existing gap row is now named with the candidate slug.)*
3. **Resolve the existing Ch.2 `--GAP--` "Developer tempo decomposition"** by adding `#def-developer-tempo-channels` as the candidate-segment row, with A4 above as the substrate. Convergence: 3/4 agents. *(Done this cycle — the existing gap row is now named with the candidate slug.)*
4. **Add a Ch.2 (or new chapter) row for the *composite developer-agent under AI augmentation*** — `#der-composite-developer-via-wrapping` or similar — with A2 above as substrate. Convergence: 4/4 agents (strongest single signal).

**Lower-confidence — open spike first, OUTLINE update after spike resolves:**

5. C1 actuated-$\rho$-regulation: open a spike on the AAT side; OUTLINE change is to `01-aat-core/OUTLINE.md` once spike resolves.
6. C3 substrate-modifying action class: open a spike to scope; new row in `#scope-developer-agent`'s action-class list or a companion segment once spike resolves.

---

## §7 — Recommended spikes

Ordered by expected leverage:

1. **`spike-running-software-agent.md`** — work the four candidate segments from A1 into segment-grade derivations. Substrate from Release It! (Agent 1) and Elixir-composite (Agent 4 A6, A7) mining. Largest single yield; highest convergence; closes Joseph's central named gap.
2. **`spike-class-coercion-via-supervision.md`** — strengthen `#der-class-coercion-via-wrapping` with the OTP supervision worked example (A2 above). Bridge restart-strategy ↔ leakage-bound mapping; restart-intensity ↔ strategic-persistence bound; stash pattern ↔ W₁/W₂ state partition. 4/4 agent convergence; strongest mining signal.
3. **`spike-actuated-rho-regulation.md`** — work C1 to segment-grade derivation. New AAT structure; only one agent surfaced it but the structural shape is clean. Persistence inequality with both sides under partial agent control; cost paid as satisfaction-gap.
4. **`spike-software-unmaintainability-bifurcation.md`** — strengthen the OUTLINE Ch.4 gap into a hypothesis-tier segment. Bifurcation derivation from logistic-with-contagion dynamics; G1/G2/G3 anchor; Ebbinghaus $\tau$ as $U_o$-decay anchor.
5. **`spike-developer-tempo-channels.md`** — work A4 into segment-grade definition. Probe-class typology; chronicle-derivable channel separation; weakest-channel bottleneck. Most direct closure of Ch.2 gap.
6. **`spike-substrate-modifying-actions.md`** — scope C3 toward a new action class in `#scope-developer-agent`. Strong bridge to 03-llm-core; could land theory-side material for AI-developer action spaces in parallel.
7. **`spike-ets-as-third-w-regime.md`** — scope C5 (lower-priority). Does class-coercion-via-wrapping need a third regime for controlled shared-state escape hatches?

---

## §8 — What is NOT in this file (intentionally)

The mining corpus has substantial volume that did not survive translation into AAT and was honestly skipped:

- Practitioner restatements of FP-001..013 that are already lifted into current AAT-grounded TST (DRY, ETC, Good Enough Software, etc.).
- Pure Elixir / BEAM syntax tutorials (pipe operator, pattern matching, list comprehension, etc.) — zero TST yield.
- Tool-specific tactical guidance (Mix configuration, Credo, Dialyzer, deployment patterns) — engineering hygiene, not theory.
- "Application to Sapientia" code blocks in each analysis — AI-generated example code, not theory.
- Aesthetic / values content (delight users, pride and prejudice, ethical development) — no structural yield.
- Refactoring-forensics that subsume into existing `#der-code-quality-as-observation-infrastructure` and `#hyp-causal-discovery-from-git` without new structural content.

The negative-space documentation lives in each agent's mining file under the *Skipped* / *Items deliberately not lifted* section; this file does not duplicate it.
