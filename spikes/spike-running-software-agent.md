# Spike: The Running Software Service as Adaptive-Actuated Agent

**Status.** Exploratory research spike. The four candidate-segment sketches below carry math at varying tiers: the substate mapping (§2) and the persistence condition (§4) are worked to *exact-under-stated-conditions* tier, with the conditions named in honesty; the tempo decomposition (§5) is worked to *robust qualitative* tier with the matrix-Loewner weakest-channel argument carried through but contingent on a directional-fidelity bridge the AAT side handles; the observation-channels catalog (§3) is *definitional* tier. The adaptive-dispatch / fixed-strategy boundary (§1.2) is load-bearing and held sharp.

**Date.** 2026-05-21.

**Pressure point.** The TST mining cycle of 2026-05-21 surfaced *the running software service as an adaptive-actuated agent* as a central named gap — 3/4 mining agents independently converged on a coherent picture that a deployed service (GenServer + supervisor + circuit breakers + retry layer + load balancer + telemetry + autoscaler) instantiates AAT's $(M_t, O_t, \Sigma_t)$ machinery at the runtime layer (`TST-IDEAS.md` §A1; `spikes/tst-mining-2026-05-21/01-release-it-mining.md` A1; `spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` A6 + A7). Four candidate segments are scoped:

- `#scope-running-software-agent` — runtime substate mapping.
- `#def-runtime-observation-channels` — telemetry / health / request-stream / control-plane.
- `#der-runtime-persistence-condition` — service persistence with $\rho_\text{env}$ and $\delta_\text{critical}$ defined in service terms.
- `#der-runtime-tempo-decomposition` — $\mathcal T_\text{runtime} = \mathcal T_\text{sense} + \mathcal T_\text{decide} + \mathcal T_\text{actuate}$ with matrix-Loewner weakest-channel bottleneck.

This spike sketches each, names what is exact and what needs more work, and surfaces the *adaptive-dispatch* honesty call as the load-bearing scope condition.

**Sibling-spike assumptions named explicitly.** This spike runs in parallel with five others. Where this work assumes a sibling's result:

- **Spike 2 — class-coercion-via-supervision** (logically upstream): the $W_1$ wrapping construction giving the supervised-actor composite GUC Class 1 (Separated) status is *taken as given* below. The runtime composite assembled here ($\Sigma_t$-as-supervised-actor-graph + ETS belief cache + telemetry pipeline + admission-control boundary) inherits its directed-separation status from that construction. If Spike 2 strengthens the leakage bound, the bound carries directly into the persistence inequality here.
- **Spike 3 — actuated $\rho$-regulation** (changes one side of the persistence condition): treated below as a *first-class agent action class*. §4.5 names the persistence inequality with $\rho_\text{effective} \leq \rho_\text{offered}$ achievable via admission-control. If Spike 3 lands an AAT segment formalizing this, the *result* slot points there; the *instantiation* — backpressure / load-shedding / handshaking as service actions — lands here.
- **Spike 5 — developer-tempo channels** (sibling, should converge in structural form): the developer agent and the running-service agent are the *two halves* of TST's composite-agent picture, both decomposing their adaptive tempo into channel sums with matrix-Loewner weakest-channel bottlenecks. §5 below mirrors the developer-side decomposition deliberately. Three-channel structure here (sense / decide / actuate) parallels the developer-side three-channel structure (obs / explore / probe); the *names* differ because the agents differ, but the *structural form* (additive scalar / matrix-additive tensor / Loewner bottleneck) is identical by design. Drift between the two would itself be a finding.
- **Spike 7 — ETS / W-regimes** (just resolved, no $W_{1.5}$ needed): the runtime composite's shared-state regions (ETS tables, Redis caches, distributed registries) are handled within the existing $W_1$ / $W_2$ machinery per `spikes/spike-ets-as-third-w-regime.md`. ETS as wrapped Class-A component when access-controlled and goal-blind by typed API; degrades to Class B / C with $W_2$ behavioral bound when writers are goal-conditioned. No new regime needed.

---

## 1. Setup — what the segment cluster is for

### 1.1 The picture

A running service instantiates AAT's adaptive-actuated agent machinery at the runtime layer, parallel to but structurally distinct from the developer-agent (which instantiates the same machinery at the codebase-modification layer). The substate mapping is concrete:

- $M_t$ — the service's belief state: GenServer process state, connection-pool counts, circuit-breaker states, in-memory caches, traffic-rate estimates, dependency-health beliefs, replica-set memberships.
- $\Omega_t$ — the service's environment: the request stream + dependency-service behavior + infrastructure (hosts, network, storage) + control-plane configuration.
- $O_t$ — the SLO bundle: uptime target $\geq A_\text{target}$, latency tail $\leq \ell_\text{target}$, error rate $\leq \epsilon_\text{target}$, correctness invariants (idempotency, monotonicity, conservation), plus secondary goals (cost ceiling, fairness, backpressure-respect).
- $\Sigma_t$ — the operational playbook encoded as a probabilistic causal DAG over runtime sub-strategies: retry-with-backoff, fail-over to replica, shed load via 503, throttle via token-bucket, restart actor, blue/green swap, route-around, scale pool.
- $h$ — the observation function: which telemetry, health-checks, request-arrivals, and control-plane RPCs the service ingests (and at what rate, with what noise).
- $\mathcal A$ — the action space: union of internal recovery moves (open breaker, restart actor, scale pool, evict cache) and external moves (return 503, drain, send blue/green-swap signal, emit alert, refuse work at admission boundary).

Section II of AAT (Actuated Agents) applies *exactly* under the architectural conditions named below (§1.2); Section I applies more broadly to the fixed-strategy case.

### 1.2 Adaptive-dispatch versus fixed-strategy — the scope cut

This is the load-bearing honesty call from TST-IDEAS §A1, and it must be surfaced sharply.

A vanilla GenServer with hard-coded `handle_call` clauses dispatching every request through the same fixed code path is *not* a Tier-3 adaptive-actuated agent. It has:

- $M_t$ — yes (its state field).
- $\Omega_t$ — yes (its inbox + side-effect surface).
- $\Sigma_t$ — *fixed at compile time*. The dispatch table is the strategy DAG, and it does not adapt. Every observation flows through the same predetermined path.
- $O_t$ — implicit in the code, not represented in state, not revised.

This is structurally a *Tier-1 reflex* in AAT's agent spectrum (`#def-agent-spectrum`): observation triggers fixed dispatch produces action. Section I's adaptive-tempo machinery still applies (the dispatch table is one big $K^{(k)}$ matrix in trivial form), but Section II's purposeful-substate machinery does not — there is no $G_t$ that ever updates.

The chapter applies only to **adaptive-dispatch** running services: those whose $\Sigma_t$ structure actually adapts based on observations. Three canonical classes qualify:

1. **Rate-limiting / throttling services** whose token-bucket fill rate or admission threshold adjusts based on observed downstream health or request-pattern shifts.
2. **Circuit-breaker pools** whose breaker state (closed / open / half-open) changes based on observed failure density and probing outcomes — the breaker's mode *is* a $\Sigma_t$ revision.
3. **Autoscalers / load balancers / sidecars** that update replica counts, routing weights, or health-driven steering based on observed throughput, latency, or downstream-failure signals.

Fixed-strategy services — pure data plane, statically configured load balancers, deterministic protocol gateways with no internal control loop — fall under **Section I** of AAT only. They satisfy `#scope-adaptive-system` (they have observations and uncertainty about their environment) but typically *not* `#scope-agency`'s Pearl-Level-2 contrast condition in a non-trivial way (their action distribution under each request is structurally fixed; the interventional contrast is in the request, not in the service's choice).

This is the scope condition the chapter must name explicitly in its opening segment. The risk of papering over it is real: most production services have some adaptive-dispatch component, but the *vast majority of code* in a typical service is fixed-strategy data-plane. The chapter's claims apply to the control-plane / supervisor / breaker / autoscaler layers, not to every line of GenServer code.

**Why the cut is structural, not stylistic.** The orient cascade (`#der-orient-cascade`) requires $\Sigma_t$ to be revisable in response to $M_t$ updates. A service whose $\Sigma_t$ is compile-time-fixed has no orient cascade to speak of — the cascade collapses to its first step ($M_t$ update, no $\Sigma_t$ revision, no $O_t$ feasibility check). Section II results (composition, persistence under purposeful machinery) require all three steps, which require the adaptive-dispatch property. This is the same kind of scope cut as in `#scope-agency` versus `#scope-adaptive-system`: a narrowing that *unlocks* downstream machinery rather than excluding cases.

---

## 2. Candidate segment: `#scope-running-software-agent`

### 2.1 What it is

A scope segment paralleling `02-tst-core/src/scope-developer-agent.md`. It identifies the running adaptive-dispatch service as an actuated adaptive agent in AAT's full sense, with the substate mapping spelled out term-by-term.

### 2.2 Sketch — Formal Expression block

*[Scope (scope-running-software-agent)]*

An adaptive-dispatch running software service is an actuated adaptive agent (`#def-agent-environment`, `#scope-agency`) whose state, environment, and coupling are:

**Environment ($\Omega_t$).** The full state external to the service's process state:

| Component | Change driver | Observability |
|---|---|---|
| Request stream | Upstream users, traffic patterns, attack actors | High (request log, rate gauges) |
| Dependency-service health | Other services' uptime / latency / errors | Medium (health checks, response patterns) |
| Infrastructure state | Host failures, network partitions, storage degradation | Medium (telemetry, control-plane events) |
| Configuration | Operator changes, deploy events, feature flags | High (control-plane RPC, etcd / config-store events) |
| Replica set / peers | Cluster membership, leader election | Medium (gossip, registry) |
| Time / clock | Wall-clock drift, scheduler jitter | High locally, medium relative-to-others |

The $\rho_\text{env}$ term in the persistence condition (§4) is the rate at which these components change in ways that matter for the service's belief.

**Model ($M_t$).** The service's internal belief state — the GenServer state vector, augmented with cross-process belief stores:

- Per-actor state: in-process belief about the conversation / request / connection.
- Connection-pool occupancy and per-connection health.
- Circuit-breaker states (closed / open / half-open) per downstream dependency.
- In-memory caches (often in ETS-style shared regions; per Spike 7, $W_1$ when goal-blind by typed API).
- Traffic-rate estimators and sliding-window aggregates.
- Replica-set membership and leader belief.

*Honest note.* For an adaptive-dispatch service, $M_t$ is *more explicitly representable* than for either a human or LLM agent — process state is inspectable, ETS tables are queryable, telemetry exposes most of it. This makes the service AAT's *second* high-identifiability calibration laboratory after the developer-agent / codebase pair (the first lab, per `02-tst-core/scope-developer-agent.md` Findings). Two labs gives the framework two independent calibration anchors.

**Objective ($O_t$).** The SLO bundle plus invariants:

$$O_t = \left( A \geq A_\text{target},\; \ell_{p99} \leq \ell_\text{target},\; \epsilon \leq \epsilon_\text{target},\; \text{invariants}_1, \ldots, \text{invariants}_k \right)$$

with each invariant a correctness predicate (idempotency under retry, monotonic-counter advancement, no double-charge, etc.). The SLO bundle is set at deploy time and revised on a slower timescale than $M_t$ (configuration changes, often days to weeks); within a deployment cycle $O_t$ is effectively constant.

**Strategy ($\Sigma_t$).** The probabilistic causal DAG over runtime sub-strategies (`#def-strategy-dag`). For an adaptive-dispatch service, $\Sigma_t$ has *runtime-mutable* structure — circuit-breaker states, retry budgets, throttle rates, routing weights are nodes / edges whose state changes based on $M_t$. The runtime-fixed parts (the supervision-tree topology, the message-protocol shape) are $\Sigma_t$'s *compile-time-fixed substrate* — strategy structure that is invariant to current beliefs.

Examples of in-DAG adaptive moves:

- "If failure-density on dependency $D$ exceeds threshold $\theta$, open the breaker; else closed" — an OR-node whose active branch is $M_t$-dependent.
- "Retry transient errors up to $n$ times with exponential backoff; permanent errors fail immediately" — an AND-node whose edge confidences track observed retry success rates.
- "If $p99$ latency exceeds budget, scale replica count up by $k$; else hold" — an actuation strategy whose trigger condition is $M_t$-derived.

**Observation channels ($\mathcal O$).** Four channel classes, distinguished by trigger and information type. See §3 for the full table.

**Action space ($\mathcal A$).** Five classes of service actions, distinguished by where the effect lands:

1. **Internal recovery** — actions that change the service's own state without external observable effect: open / close circuit breaker, restart actor, evict cache entry, drain connection pool.
2. **Service-level actuation** — actions that produce externally-observable response: return 503, return cached value, return degraded response.
3. **Admission-control / $\rho$-actuation** — actions that modulate the service's own *incoming* request stream: refuse work at the boundary, signal backpressure to upstream, decline new connections. (See Spike 3; this is the action class that makes $\rho_\text{effective}$ partially under the service's control.)
4. **Composition-level actuation** — actions on the runtime composite the service participates in: trigger blue/green swap, alert operators, send scale-up signal to autoscaler, ack-leader-change.
5. **Strategic actuation** — actions that update $\Sigma_t$ itself (rather than executing a fixed strategy): adjust retry budget based on observed dependency-recovery patterns, change throttle threshold based on observed traffic regime. *This is the action class that distinguishes adaptive-dispatch from fixed-strategy.*

**Mismatch signal ($\delta_t$).** Predictions versus observations:

| Situation | Prediction $\hat o_t$ | Observation $o_t$ | Mismatch $\delta_t$ |
|---|---|---|---|
| Routine traffic | Expected request rate / latency / error mix | Actual rate / latency / error mix | Regime-shift signal |
| Dependency call | Expected response time / shape | Actual response (timeout, error, slow) | Health-shift signal |
| Internal invariant | Invariant holds | Invariant violated (e.g., counter monotonicity broken) | Corruption signal |
| Deploy / config | Expected behavior under new config | Actual behavior | Deploy-event signal |

Driving $\lVert\delta_t\rVert$ toward zero through observation + $\Sigma_t$ revision is the service's adaptive work.

### 2.3 Epistemic Status

Definitional. The mapping is *exact* in the sense that each AAT quantity has a concrete identifiable runtime counterpart for the adaptive-dispatch class. The scope-cut to adaptive-dispatch services (§1.2) is what gives the mapping its exactness — without it the $\Sigma_t$ slot is vacuous.

### 2.4 Open question

The classification of an autoscaler is interesting. An autoscaler that adjusts replica counts based on observed throughput is unambiguously adaptive-dispatch. An autoscaler that adjusts replica counts on a fixed schedule (cron-based scaling) is fixed-strategy. The honest answer is that scope-membership is *per-deployment*, not *per-software-component-class* — the same autoscaler binary can instantiate either depending on configuration. The chapter should make this explicit: scope-membership requires checking the deployed configuration, not the artifact name.

---

## 3. Candidate segment: `#def-runtime-observation-channels`

### 3.1 What it is

A definition segment cataloguing the four canonical observation channels of a runtime adaptive-dispatch service, each with its $(\nu^{(k)}, U_o^{(k)})$ profile and $\eta^{(k)\ast}$ characterization. Parallels the developer-side `developer-observation-channels` block in `scope-developer-agent.md` (passive / active distinction lifted to telemetry-flow / probe-flow).

### 3.2 Sketch — channel catalog

*[Definition (runtime-observation-channels)]*

Four classes of channels, distinguished by trigger and information shape:

**Passive (always-on, environment-initiated) channels:**

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ | Information type |
|---|---|---|---|
| Telemetry (metrics + traces) | Continuous, $10^2$ – $10^5$ Hz | Low-medium (varies by instrumentation $Q$) | $M_t$-state, throughput, latency, resource use |
| Health-check (own + dependency) | Per-poll interval, 1 – 100 Hz | Low (binary or low-D vector) | Liveness, dependency-availability |
| Request stream | Per-request, 1 – $10^6$ Hz | Medium (request content is high-D) | $\Omega_t$-state, environment regime |
| Control-plane RPC | Sporadic, event-driven | Very low (typed messages from authority) | $O_t$ updates, configuration shifts |

**Active (service-initiated probe) channels:**

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ | Information type |
|---|---|---|---|
| Synthetic health-probe / smoke-test | Per-probe-interval, 0.1 – 1 Hz | Low | Targeted dependency-state |
| Half-open breaker test request | Per-recovery-window, rare | High (single sample of unknown distribution) | Regime-change detection (closed → half-open → closed transition) |
| Canary deploy traffic | Per-canary-window, slow | Medium | Counterfactual: new-version vs. current-version $\Omega_t$-response |
| Chaos / fault-injection | Per-experiment, very rare | Variable | Pearl-Level-2 interventional access to failure modes (per Release-It mining A10) |

The first two passive channels (telemetry + health) are the dominant tempo contributors in steady state — high rate, low noise. The request stream is the highest-rate channel but has the highest $U_o$ because most of its information is about *the request*, not about $\Omega_t$-state-the-service-needs-to-track. Control-plane RPC is rare but has $\eta^\ast \approx 1$ because it carries authoritative $O_t$-updates from the control-plane.

The active channels matter disproportionately at *regime transitions*. The half-open breaker test is a single probe that decides whether to re-close the breaker; it carries high $U_o$ per sample (it's one observation from an unknown distribution) but it is *the only channel* that can detect dependency recovery, so its $\eta^\ast$ is structurally bounded above by what one sample can tell you. Chaos-engineering experiments (`spikes/tst-mining-2026-05-21/01-release-it-mining.md` A10) are Pearl-Level-2 interventions that surface failure-mode information the passive channels cannot.

### 3.3 Connection to $Q \to U_o \to \eta^\ast \to \mathcal T$

The runtime-side chain mirrors the developer-side chain from `#der-code-quality-as-observation-infrastructure`. *Telemetry quality* $Q_\text{tel}$ is the runtime analog of *code quality* — well-instrumented code has low $U_o$ on telemetry channels, badly-instrumented code has high $U_o$. The chain $Q_\text{tel} \to U_o^\text{tel} \to \eta^{\text{tel}\ast} \to \mathcal T_\text{runtime}$ predicts that under-instrumented services have collapsed runtime tempo independent of how fast their decide-and-actuate machinery is. This is the runtime-side mechanism behind the "service-failed-because-we-couldn't-see-it-failing" pattern that the Release-It corpus catalogues under transparency / observability.

### 3.4 Epistemic Status

Discussion-grade taxonomy. The channel structure is *robust qualitative* — every adaptive-dispatch service has these four channel classes in some form — but the specific $(\nu, U_o)$ values are deployment-specific. The structural claim (four classes, characterized by trigger and information shape) is the segment's load-bearing content; the example values in the tables are illustrative, not derived.

### 3.5 Open question

Whether the *active probe channels* deserve their own sub-axis distinct from the developer-side active channels (code-reading, test-execution). Both are agent-initiated and both have variable $U_o$. The structural similarity is that they're both Pearl-Level-2 access mechanisms; the difference is that runtime probes act on $\Omega_t$ (the production environment) while developer probes act on $\Omega_\text{dev}$ (a test environment or the codebase). The transfer from test-$\rho$ to production-$\rho$ is exactly the chaos-engineering motivation (Release-It mining A10, D2).

---

## 4. Candidate segment: `#der-runtime-persistence-condition`

### 4.1 What it is

A derivation segment specializing `#result-persistence-condition` to the runtime service. The substantive content is the *definition* of $\rho_\text{env}$ and $\delta_\text{critical}$ in service terms, plus the recognition that for adaptive-dispatch services one side of the inequality ($\rho$) is partially under agent control (per Spike 3).

### 4.2 Specializing the persistence inequality

Per `#result-persistence-condition`, an adaptive agent persists operationally when

$$\mathcal T \;\gt\; \frac{\rho}{\lVert \delta_\text{critical} \rVert}$$

(linear / Model D operational form, with structural persistence automatically satisfied; or under matrix correction, $\Sigma_\infty \prec D_\delta$ from `#deriv-matrix-persistence-condition`).

For the runtime service:

**$\mathcal T_\text{runtime}$** — the service's adaptive tempo, decomposed into sense / decide / actuate channels (§5).

**$\rho_\text{env}$** — the *rate of environmental change that matters for the service's belief*. Decomposes by environment-component class:

$$\rho_\text{env} \;=\; \rho_\text{traffic} \;+\; \rho_\text{dependency} \;+\; \rho_\text{infrastructure} \;+\; \rho_\text{config} \;+\; \rho_\text{adversarial}$$

with channel independence (or matrix tempo when channels share substrate — see §5.5):

- $\rho_\text{traffic}$ — request-rate variation, traffic-pattern shifts, viral spikes. Bursty, often impulse-shaped (per `spikes/tst-mining-2026-05-21/01-release-it-mining.md` C2: impulses-vs-stresses distinction).
- $\rho_\text{dependency}$ — upstream / downstream service-failure rate, latency shifts, version changes. Has its own characteristic timescales (faster than infrastructure, slower than traffic).
- $\rho_\text{infrastructure}$ — host failures, network partitions, storage degradation. Rare, high-magnitude.
- $\rho_\text{config}$ — control-plane changes, feature-flag flips, deploy events. Discrete, operator-driven.
- $\rho_\text{adversarial}$ — attack traffic, scraping, exploitation attempts. Adversarial in the AAT sense — coupled to the service's own visible posture.

The decomposition is useful precisely because the *actuation patterns* differ across components: backpressure handles $\rho_\text{traffic}$ but not $\rho_\text{config}$; circuit breakers handle $\rho_\text{dependency}$ but not $\rho_\text{infrastructure}$ directly; admission control handles $\rho_\text{traffic} + \rho_\text{adversarial}$ but not $\rho_\text{dependency}$. Per-component $\rho$ matters because per-component actuation matters. Mining material in `spikes/tst-mining-2026-05-21/01-release-it-mining.md` C2 supports this as Class-C theory-side new structure.

**$\lVert \delta_\text{critical} \rVert$** — the *per-direction* SLO tolerance:

$$\lVert \delta_\text{critical} \rVert \;=\; \text{joint slack of } \big( A_\text{target} - A_\text{floor},\; \ell_\text{target} - \ell_\text{floor},\; \ldots \big)$$

— how much $M_t$ can drift from $\Omega_t$ before the service's actions become harmful or its SLO is violated. Like all AAT $\delta_\text{critical}$ values, this is a *domain parameter* set by the SLO contract, not derived from theory. The strict-positivity comes from the SLO bundle: $\delta_\text{critical} = 0$ means the SLO admits zero tolerance, which is unsatisfiable for non-trivial services and corresponds to the *demands the impossible* case AAT excludes from operational persistence.

### 4.3 The full inequality, runtime-instantiated

The operational persistence condition for the runtime service:

$$\mathcal T_\text{runtime} \;\gt\; \frac{\rho_\text{env}}{\lVert \delta_\text{critical} \rVert} \;=\; \frac{\rho_\text{traffic} + \rho_\text{dependency} + \rho_\text{infrastructure} + \rho_\text{config} + \rho_\text{adversarial}}{\lVert \delta_\text{critical} \rVert}$$

When the inequality is satisfied, the service's belief tracks the environment tightly enough that its strategy choices remain SLO-aligned. When it fails, the service's $M_t$ drifts from $\Omega_t$ — actions are taken on stale belief — and either (a) the strategy is robust enough to absorb the mismatch (the SLO is still met by accident or by margin), or (b) the mismatch propagates into invariant violations and the service trips into the failure regime.

### 4.4 The matrix-Loewner form

Per §5 below, the scalar form is *unsafe* under cross-channel correction (e.g., when the same telemetry pipeline carries multiple $\rho$-components and shares an observation infrastructure). The canonical anisotropic form is the matrix-Loewner condition (`#deriv-matrix-persistence-condition`):

$$\Sigma_\infty \;\prec\; D_\delta \;=\; \mathrm{diag}\!\big( \delta_{\text{critical}, k}^2 \big)$$

with $\Sigma_\infty$ the stationary covariance under matrix-tempo $\mathcal T_\text{runtime}$ and matrix-disturbance $\Sigma_w$ over the per-component-$\rho$ basis. This is the form that catches the multimodal-pipeline failure mode where one $\rho$-component is capacity-starved while aggregate tempo looks fine.

### 4.5 Actuated $\rho$ — the inequality has both sides under partial agent control

Spike 3 introduces the *actuated $\rho$* refinement: the persistence inequality is no longer one-sided, because the service has admission-control / backpressure / load-shedding actions that modulate $\rho_\text{effective}$ from $\rho_\text{offered}$. The runtime-instantiated form becomes

$$\mathcal T_\text{runtime} \;\gt\; \frac{\rho_\text{effective}}{\lVert \delta_\text{critical} \rVert}, \qquad \rho_\text{effective} \leq \rho_\text{offered}$$

with the gap paid in a *satisfaction-gap* (work refused — direct cost in $O_t$-shortfall on the throughput dimension). This is the runtime form of the *cost-of-persistence* result from `#deriv-persistence-cost`: persistence has a price, and for the runtime service the price is partly information-rate (telemetry bandwidth) and partly satisfaction-gap (work-refused).

The strengthening that Spike 3 would land — formalizing admission-control as an action class that modulates $\rho_\text{effective}$ — *changes one side of the persistence inequality* in a structurally clean way. The instantiation here (backpressure, load-shedding, handshaking, token-bucket as concrete $\rho$-actuation patterns) is the engineering vocabulary; the AAT-side derivation lives in Spike 3.

### 4.6 Restart-intensity as the wrapper-level strategic persistence bound

This is a result with sharp form that comes out of the OTP-supervision mapping (`spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` A3, A1). It is *not the same inequality* as §4.3 — it operates at the *wrapper level*, governing when the wrapping construction itself sustains class-coercion versus when it escalates. Recording it here as a sibling result that the runtime persistence segment should cross-reference (assuming Spike 2 strengthens this).

For a supervisor wrapping a worker:

$$\mathcal T_\text{wrapper} \;=\; \frac{1}{T_\text{restart}}, \qquad \rho_\text{child} \;=\; \text{child failure rate}$$

The OTP `max_restarts / max_seconds` envelope encodes a strategic-persistence boundary: if the child crash rate exceeds $N_\text{max-restarts} / T_\text{max-seconds}$, the wrapper escalates. This is a *separate inequality* from the service's own SLO-persistence condition — it governs whether the W₁ wrapping construction sustains its class-coercion guarantee versus whether it gives up and propagates the failure to its own parent wrapper.

The two inequalities compose: the service's overall persistence depends on (i) the wrapping construction sustaining class-coercion (the wrapper-level inequality), and (ii) the wrapped composite's adaptive tempo exceeding $\rho_\text{env} / \lVert \delta_\text{critical} \rVert$ at the SLO level (the service-level inequality). Failure modes split: SLO violation under wrapping-sustained-but-tempo-inadequate is *operational failure with the service still nominally up*; escalation under wrapping-collapse is *the wrapper layer itself failing*, which is structurally a Section-III composition-failure rather than a Section-I persistence-failure.

### 4.7 Epistemic Status

The persistence inequality at the service level (§4.3) is *exact under the linear / Model D operational reading*, inheriting directly from `#result-persistence-condition`. The decomposition of $\rho_\text{env}$ into the five components (§4.2) is *robust qualitative* — the partition reflects engineering structure and the matching of actuation classes to disturbance classes; the precise boundaries between components are domain-specific.

The actuated-$\rho$ refinement (§4.5) is *conditional* on Spike 3 landing the AAT-side derivation; the instantiation is exact under that condition.

The matrix-Loewner form (§4.4) is *exact* under the assumptions of `#deriv-matrix-persistence-condition` (linear-Gaussian, Hurwitz $\mathcal T$, $\Sigma_w \succ 0$), with the runtime substitution being a special case rather than a generalization.

The restart-intensity bound (§4.6) is *sketch-grade* and depends on Spike 2's strengthening of `#der-class-coercion-via-wrapping` to derive the wrapper-level persistence inequality cleanly. Flagged: this is exactly the kind of result Joseph asked about in the original TST framing ("what is $\rho$ for a microservice?") and the OTP-supervision answer is structurally clean but needs a real proof, not just a heuristic mapping.

### 4.8 Strengthen-before-soften commitments

Three claims here would benefit from spike-grade work before landing:

1. **The $\rho_\text{env}$ decomposition is exhaustive** — the five components partition the disturbance space rather than enumerating examples. Strengthening attempt: derive the partition from the environment-component table in §2 plus the actuation-class table from §2 (action class 3 vs 4 vs 5) — five $\rho$-components correspond to five distinct actuation-handler patterns, and the partition is operationally meaningful because *no single actuation handles two distinct components*. If this can be derived, the segment lands at *exact*; otherwise *robust qualitative*.

2. **The matrix-Loewner form is the canonical one for this domain**, not just available in case of need. Strengthening attempt: identify whether telemetry pipelines structurally produce correlated $\rho$-component observations (the same span carrying multiple metrics), which would force the matrix form. Likely yes — but the argument needs to be made segment-level, not assumed.

3. **The actuated-$\rho$ inequality preserves the persistence-condition's qualitative regime structure** — i.e., the threshold-and-regime-transition character survives the $\rho_\text{effective} \neq \rho_\text{offered}$ refinement. Almost certainly yes (the inequality is the same with a substituted argument), but worth checking that the regime collapse below threshold still applies sharply when admission-control is at saturation.

---

## 5. Candidate segment: `#der-runtime-tempo-decomposition`

### 5.1 What it is

A derivation segment specializing `#def-adaptive-tempo` to the runtime service, decomposing $\mathcal T_\text{runtime}$ into the three operational channels of the adaptive-dispatch loop. This is structurally parallel to the developer-side decomposition $\mathcal T_\text{dev} = \mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$ (from `scope-developer-agent.md` Discussion), with the names changed to track what the service is actually doing.

### 5.2 The three-channel decomposition

*[Derived (runtime-tempo-decomposition)]*

The runtime service's adaptive tempo decomposes into three channel classes:

$$\mathcal T_\text{runtime} \;=\; \mathcal T_\text{sense} \;+\; \mathcal T_\text{decide} \;+\; \mathcal T_\text{actuate}$$

with each term aggregating $\nu^{(k)} \cdot \eta^{(k)\ast}$ over the channels of its class (or matrix-aggregate per `#def-adaptive-tempo` Tensor extension when the channel-level matrix gain operators do not share an eigenbasis).

**$\mathcal T_\text{sense}$ — the observation half.** The rate at which the service acquires environment information through its observation channels:

$$\mathcal T_\text{sense} \;=\; \nu_\text{tel} \cdot \eta_\text{tel}^\ast \;+\; \nu_\text{health} \cdot \eta_\text{health}^\ast \;+\; \nu_\text{req} \cdot \eta_\text{req}^\ast \;+\; \nu_\text{cp} \cdot \eta_\text{cp}^\ast \;+\; \text{(active-probe channels)}$$

This is structurally `#def-adaptive-tempo` applied directly to the channel catalog of §3. Typical dominant terms: telemetry (high $\nu$, low $U_o$) and health-checks (medium $\nu$, very low $U_o$).

**$\mathcal T_\text{decide}$ — the $\Sigma_t$-revision half.** The rate at which the service updates its operational playbook based on observations:

$$\mathcal T_\text{decide} \;=\; \nu_\text{decide} \cdot \eta_\text{decide}^\ast$$

where $\nu_\text{decide}$ is the rate at which the service's control loop (the breaker state machine, the autoscaler controller, the throttle adapter) fires, and $\eta_\text{decide}^\ast$ is the gain on observation-to-strategy-revision (how good the controller is at converting sensed signal into a correct $\Sigma_t$ revision). For most production services, $\nu_\text{decide}$ ranges from sub-Hz (slow autoscaler) to tens-of-Hz (per-request breaker check) and is typically the *middle* term in the three-channel sum.

**$\mathcal T_\text{actuate}$ — the action-application half.** The rate at which the service can apply revised strategy:

$$\mathcal T_\text{actuate} \;=\; \nu_\text{actuate} \cdot \eta_\text{actuate}^\ast$$

where $\nu_\text{actuate}$ is the rate at which the actuation surface can transition (breaker open/close transition rate, pool-scaling rate, blue/green-swap rate, admission-control adjustment rate), and $\eta_\text{actuate}^\ast$ is the gain on action-to-effect — how much actual $\Omega_t$ or internal-$M_t$ state-change happens per action triggered. Typically the highest-$\nu$ term for fast actuations (per-request decisions on breaker / shed) and the lowest-$\nu$ term for slow actuations (replica scale-up taking seconds, blue/green swap taking minutes).

### 5.3 Why three channels and not two

The developer side has *three* channels (obs / explore / probe). The runtime side could in principle collapse to two (sense + actuate, since "decide" is conceptually pure computation) or expand to more (sense / model-update / strategy-revision / actuate). The three-channel structure is the right one because it tracks the three operations in the adaptive-dispatch loop that have *independent rate constraints*:

- **Sense** is bottlenecked by observation-infrastructure ($Q_\text{tel}$, network bandwidth, sampling intervals).
- **Decide** is bottlenecked by control-loop tick rate and decision-procedure complexity. A breaker check is sub-microsecond; an autoscaler decision involves cross-replica state aggregation and runs on a slower cycle. Decision can lag behind sensing if the controller is more complex than the sensor.
- **Actuate** is bottlenecked by actuation-surface latency. Opening a breaker is sub-millisecond; scaling a replica pool is seconds-to-minutes; blue/green-swap is minutes.

The three rates can differ by orders of magnitude in either direction, and that *differential* is what the weakest-channel analysis captures (§5.4).

### 5.4 The matrix-Loewner weakest-channel bottleneck

This is the load-bearing result that connects the runtime decomposition to the persistence condition.

**Claim.** Under the channel-independence assumption of `#def-adaptive-tempo`, scalar $\mathcal T_\text{runtime} = \mathcal T_\text{sense} + \mathcal T_\text{decide} + \mathcal T_\text{actuate}$ is an *upper bound* on effective adaptive tempo. The matrix-Loewner persistence condition (`#deriv-matrix-persistence-condition`) is the canonical form, and it surfaces the weakest-channel bottleneck explicitly.

**Sketch.** Treat the three channels as three orthogonal coordinate directions in the runtime agent's correction-machinery basis. The matrix tempo

$$\mathcal T_\text{runtime} \;=\; \mathrm{diag}(\mathcal T_\text{sense}, \mathcal T_\text{decide}, \mathcal T_\text{actuate})$$

with corresponding disturbance covariance

$$\Sigma_w \;=\; \mathrm{diag}(\sigma_\text{sense}^2, \sigma_\text{decide}^2, \sigma_\text{actuate}^2)$$

gives stationary covariance $\Sigma_\infty$ from the Lyapunov equation (when $\mathcal T$ is diagonal, $\Sigma_\infty = \Sigma_w / (2\mathcal T)$ component-wise). The matrix-Loewner condition $\Sigma_\infty \prec D_\delta$ then reduces (per `#deriv-matrix-persistence-condition` Recovery table, row 2) to the per-coordinate condition

$$\frac{\sigma_k^2}{2\mathcal T_k} \;\lt\; \delta_{\text{critical}, k}^2, \quad k \in \{\text{sense, decide, actuate}\}$$

which fails *whichever channel is weakest*. Service-level persistence holds iff *all three* per-coordinate conditions hold; one tempo-starved channel collapses operational tempo regardless of how strong the other two are.

**The off-diagonal generalization.** When the three channels are not orthogonal in the correction-machinery basis (e.g., when sense and decide share a substrate — the same observability infrastructure carrying both telemetry and decision-loop ticks, so they're correlated), the per-coordinate form is *unsafe* per `#deriv-matrix-persistence-condition` §"Where per-coordinate is unsafe". The matrix-Loewner form catches the off-diagonal failure direction at $45°$ to the coordinate axes.

This is operationally important: it predicts that *services where sense and decide share substrate are more fragile to coordinated disturbances than per-channel analysis suggests*. The 2016 Reddit autoscaler-on-stale-ZooKeeper-data failure (`spikes/tst-mining-2026-05-21/01-release-it-mining.md` B4) is exactly this — sense and decide nominally separate, but the autoscaler's actuation rate exceeded the *correlated* sense-decide rate, creating a failure direction at $45°$ to the sense and actuate axes that per-channel analysis would have missed.

### 5.5 Governor pattern as Loewner-bottleneck discipline

The Release-It "governor" pattern (`spikes/tst-mining-2026-05-21/01-release-it-mining.md` B4) is the runtime engineering name for *rate-limit actuation tempo to match sense + decide tempo*. In the matrix-Loewner reading, it's the operational discipline that drives the actuate-axis safety margin into balance with the sense-decide axes. A high-$\nu$ actuator (autoscaler) on top of low-$\nu$ sensors creates a coordinate where $\mathcal T_\text{actuate} \gg \mathcal T_\text{sense}$ but $\sigma_\text{actuate}^2$ is *coupled to* $\sigma_\text{sense}^2$ via stale-data effects — the actuator acts on the sensor's noise, amplifying it. The governor breaks the coupling by rate-limiting the actuator below the sensor's effective sample rate.

This is a worked example for the candidate segment, structurally clean and well-attested.

### 5.6 Connection to the developer-tempo sibling (Spike 5)

The developer-side decomposition is $\mathcal T_\text{dev} = \mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$ (from `scope-developer-agent.md` Discussion; refined to `#def-developer-tempo-channels` per TST-IDEAS §A4). The runtime-side decomposition is $\mathcal T_\text{runtime} = \mathcal T_\text{sense} + \mathcal T_\text{decide} + \mathcal T_\text{actuate}$. The structural form is identical — three channels with matrix-Loewner weakest-channel bottleneck — and that identity is deliberate. The two decompositions are the *two halves of TST's composite-agent picture*: a software project as a whole is a composite of developer-agent + running-service-agent (+ infrastructure + AI tooling + CI), and each half contributes its own adaptive tempo into a Section-III composition.

If Spike 5 lands $\mathcal T_\text{dev}$ with substantially different structural form (e.g., a non-Loewner bottleneck, or a different channel count), the divergence would be itself a finding worth resolving — either the two agents have genuinely different adaptive structure (a Class-C theory result), or one of the two segments has the structure wrong.

### 5.7 Epistemic Status

The three-channel decomposition (§5.2) is *exact as a definition* under the channel-independence assumption inherited from `#def-adaptive-tempo`. The decomposition's *operational meaningfulness* — that the three rates can be independently rate-limited and that the weakest channel is the binding constraint — is *robust qualitative*: the structural argument from $\eta^\ast$-multiplied-by-$\nu$ gives the form, but the empirical magnitude of the differences across channels in real systems is what makes it operationally interesting, not theoretically inevitable.

The matrix-Loewner weakest-channel analysis (§5.4) is *exact* under the conditions of `#deriv-matrix-persistence-condition` (linear-Gaussian, Hurwitz, $\Sigma_w \succ 0$), with the runtime substitution being a direct specialization. The unsafety of per-coordinate analysis under cross-channel substrate-sharing (§5.4's off-diagonal generalization) follows directly from the counterexample in `#deriv-matrix-persistence-condition` §"Where per-coordinate is unsafe".

The governor-pattern reading (§5.5) is *worked example* — concrete, well-attested in the Release-It corpus, structurally clean.

### 5.8 What's not yet derived

The connection from $\mathcal T_\text{runtime}$ to the *service's directional fidelity* $c_\text{min}$ — the per-direction worst-case quality of correction (per `#der-gain-sector-bridge`) — is not worked here. For the linear-correction case, $\alpha = \mathcal T$ exactly and the bridge is trivial. For the saturating / sigmoid-nonlinear correction cases that appear in real circuit-breaker dynamics (the breaker has a saturating response to failure-density), $\alpha \approx 0.5 \mathcal T$ to $\alpha \approx 0.76 \mathcal T$ per the simulation results in `#result-persistence-condition`. The runtime-side specialization should pick this up rather than asserting $\alpha = \mathcal T$.

This is *spike-grade follow-on*, not segment-blocking. The segment lands the decomposition and the matrix-Loewner reading; the directional-fidelity refinement is a strengthening cycle.

---

## 6. The Honesty Call — surfaced sharply

The chapter introduction (the segment that holds `#scope-running-software-agent`) must name the adaptive-dispatch versus fixed-strategy cut explicitly. The mining substrate already supports this (`spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` A6: *"Under what conditions does the running service have genuine $G_t$ and not just a fixed dispatch table? A vanilla GenServer with hard-coded handle_call clauses has no $\Sigma_t$ adaptation — it is closer to a Tier-1 reflex than a Tier-3 agent."*) and the structural argument is clean (§1.2 above). The proposed framing in the chapter intro:

> *AAT's adaptive-actuated agent machinery applies to running software services whose operational playbook ($\Sigma_t$) is itself runtime-adaptive based on observations — rate limiters, circuit breakers, autoscalers, supervised actor systems with adaptive supervision strategies, sidecars routing on observed health. Fixed-strategy services — pure data plane, statically-configured load balancers, deterministic protocol gateways — instantiate AAT's adaptive scope (Section I) but not its agency scope (Section II), because their action-space carries no Pearl-Level-2 contrast that the service itself can exercise. This chapter is about the adaptive-dispatch class; fixed-strategy services fall under Part I of AAT directly.*

The chapter should *not* paper over this. The mining material is correct: most production services have *some* adaptive-dispatch components (the control plane, the supervisor, the breakers) and *substantial* fixed-strategy data plane (the request handlers themselves). The chapter applies to the former cleanly; treating the data plane as adaptive-dispatch would be overclaim.

The honest summary in one line: *the chapter is about the runtime's control plane, not the runtime's data plane.* That distinction is well-understood in operational practice, and naming it explicitly is the right move.

---

## 7. What's left for follow-on spikes versus what's segment-ready

### 7.1 Segment-ready now (subject to peer review)

- `#scope-running-software-agent` (§2) — substate mapping with adaptive-dispatch scope cut. Definitional. Lands at *axiomatic / scope-cut* tier.
- `#def-runtime-observation-channels` (§3) — channel catalog. Discussion-grade taxonomy. Lands at *robust qualitative*.
- `#der-runtime-tempo-decomposition` (§5, §5.2–§5.5) — three-channel decomposition + matrix-Loewner weakest-channel + governor-pattern worked example. Lands at *exact under stated linear/diagonal assumptions; robust qualitative for the operational claim*.

### 7.2 Needs sibling-spike landings first

- `#der-runtime-persistence-condition` (§4) — depends on:
  - Spike 3's actuated-$\rho$-regulation AAT segment for the $\rho_\text{effective}$ form (§4.5).
  - Spike 2's strengthened class-coercion-via-wrapping for the restart-intensity wrapper-level inequality (§4.6).
  - The $\rho_\text{env}$ five-component decomposition's exhaustiveness (§4.8 item 1) — strengthen-before-soften target.

### 7.3 Follow-on spike work surfaced by this spike

- **Strengthen the $\rho_\text{env}$ partition** — derive the five-component decomposition from the environment + action-class tables (§4.8 item 1). Strengthens the segment from robust qualitative to exact.
- **Directional-fidelity bridge for nonlinear correction** — work the $\alpha = \mathcal T$ versus $\alpha = c \cdot \mathcal T$ relationship for circuit-breaker / saturating-controller dynamics (§5.8). Needed for honest persistence-margin calculation in real breakers.
- **Cross-channel substrate-sharing in production telemetry** — empirical / theoretical work to confirm the matrix-Loewner form is the canonical one for this domain rather than convenient-when-needed (§4.8 item 2). Strengthen from robust qualitative to exact-by-derivation.
- **Composite-agent persistence** — TST's full composite-agent picture is developer + running-service + infrastructure + AI tooling + CI. Each half has its own persistence condition; the composite has a Section-III composition-level persistence. This is a chapter-after-next concern but worth flagging from here.

### 7.4 Out-of-scope for this spike (intentionally)

- The full chapter-level OUTLINE update with all four candidate-segment rows. That is editorial work for a future cycle and requires Joseph's sign-off on the chapter slot (Ch.5 of `02-tst-core/`) per TST-IDEAS §A1.
- The worked-example catalog for the chapter — the Release-It pattern catalogue gives many (circuit breakers as $\eta^\ast$-saturation, bulkheads as M1 identifiability commitment, chaos as Pearl-Level-2, etc.). Each could be its own example-segment, and the chapter as a whole would benefit from at least 2–3. This spike scopes the *core* segments; the example layer is downstream.
- The OTP-supervision class-coercion mapping. That is Spike 2's territory; this spike depends on it but does not work it.

---

## 8. Process notes

**Strengthen-before-soften commitments not yet executed.** Three substantive strengthening targets are recorded in §4.8 and §5.8. None blocks the segment's landing at the tier called out in the Epistemic Status sections, but each *could move the tier up* if worked. Per project convention (`feedback_strengthen_before_soften`), the strengthening attempts should be made before the segments land, not after — the spike-grade work is the substrate that lets the segments land cleanly.

**Aesthetic standard checked.** This spike aims at the rigor of `02-tst-core/src/scope-developer-agent.md` (substate mapping, observation channels, action classes, mismatch table, gain instantiation, all spelled out with concrete examples). The runtime chapter is the runtime-side sibling and should match that bar; the four-segment cluster sketched here is structurally parallel by design.

**Voice.** Spike file, not segment file: history is preserved here (cycle context, sibling-spike dependencies, what's tentative versus exact), not pushed into segment bodies. The segments themselves, when they land, will state the current truth without the cycle-archaeology. Per `feedback_segment_voice_not_diff_voice`, that boundary is load-bearing.

**No-go names.** None surfaced in this spike. The work is constructive throughout: there is a clean structural picture (adaptive-dispatch runtime as Section-II agent), with explicit scope cuts (adaptive-dispatch versus fixed-strategy) and explicit dependencies on sibling spikes for the parts that need more work than this spike can deliver alone.

**Files referenced (absolute paths for cross-spike sync).**

- `/Users/josephwecker-v2/src/agentic-systems/TST-IDEAS.md` §A1 — primary substrate.
- `/Users/josephwecker-v2/src/agentic-systems/spikes/tst-mining-2026-05-21/01-release-it-mining.md` — Class A findings, particularly A1, A6, A7, A2, A8, B4, C2.
- `/Users/josephwecker-v2/src/agentic-systems/spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` — A6 (GenServer substate mapping), A7 (let-it-crash as temporal-optimality), A1 (supervision as class-coercion).
- `/Users/josephwecker-v2/src/agentic-systems/01-aat-core/src/scope-adaptive-system.md` — Section I scope condition.
- `/Users/josephwecker-v2/src/agentic-systems/01-aat-core/src/scope-agency.md` — Section II scope condition (Pearl-Level-2 contrast).
- `/Users/josephwecker-v2/src/agentic-systems/01-aat-core/src/def-agent-environment.md` — agent-environment boundary.
- `/Users/josephwecker-v2/src/agentic-systems/01-aat-core/src/def-adaptive-tempo.md` — tempo definition including the tensor extension.
- `/Users/josephwecker-v2/src/agentic-systems/01-aat-core/src/result-persistence-condition.md` — central inequality being specialized.
- `/Users/josephwecker-v2/src/agentic-systems/01-aat-core/src/deriv-matrix-persistence-condition.md` — matrix-Loewner form used in §5.4.
- `/Users/josephwecker-v2/src/agentic-systems/02-tst-core/src/scope-developer-agent.md` — sibling segment to mirror in structure.
- `/Users/josephwecker-v2/src/agentic-systems/spikes/spike-ets-as-third-w-regime.md` — resolved sibling on $W$ regimes.
