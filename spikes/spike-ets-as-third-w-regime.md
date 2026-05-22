# Spike: ETS as a Third W Regime — Resolves Within the Existing $W_1$ / $W_2$ Machinery

**Status.** Resolved spike. Yes/no structural question with a yes-answer to the strengthen-first reading: the existing $W_1$ / $W_2$ regime hierarchy in `#der-class-coercion-via-wrapping` handles ETS (and the general "controlled shared-state escape hatch" pattern) without modification, under reading (iii) of the original framing — ETS as a *wrapped Class-A component shared between wrappers*, not as an exception region punched through a wrapper. The $W_{1.5}$ proposal is **rejected**.

**Date.** 2026-05-21.

**Pressure point.** The Elixir-composite mining (`spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` A10) surfaced ETS (Erlang Term Storage) as a structural curiosity: it provides lock-free shared memory outside any single process's heap, with a `private` / `protected` / `public` access-control matrix governing cross-process reads and writes. The actor-model strict-isolation invariant $S_i \cap S_j = \emptyset$ is *deliberately broken* for ETS-table-contents, but the breakage is *scoped and access-controlled* — not behavioral leakage, not unbounded coupling, but a *named, typed, runtime-enforced* exception region. Every production BEAM system uses ETS for caches and shared lookup tables, so this is not a corner case.

The structural question the mining identified: is this a *third W regime* — "$W_{1.5}$ — structural commitment with a named, access-controlled exception region" — distinct from both $W_1$ (structural commitment, no leakage by construction) and $W_2$ (behavioral leakage bound by observable metric)? Or is $W_2$ subsuming it under a generous reading? Or is it a *composite* construction within the existing machinery?

This spike works the question to a structural resolution.

---

## 1. The strengthen-first attempt: derive ETS-handling within existing $W_1$/$W_2$

Per Joseph's working-convention discipline (`feedback_strengthen_before_soften`), the strengthen-first move is to attempt the derivation of ETS-handling *within* the existing $W_1$ / $W_2$ machinery before proposing a new regime. The proposal "we need a new regime" is honest only if this attempt fails.

The strengthen-first attempt succeeds. Here is the construction.

### 1.1 What the W regimes structurally are

Per `#der-class-coercion-via-wrapping`, the $W_1$/$W_2$ distinction is *not* about heap-disjointness, in-process memory layout, or any property of the substrate's runtime. It is about *where the leakage bound lives*:

- **$W_1$ (strict wrapping).** The wrapper's belief-update query selector $q_M : \mathcal X_M \times \mathcal O_W \to \mathcal Q_A$ has no $G_W$ argument *by type signature*. The wrapper's belief-update map $f_M : \mathcal X_M \times \mathcal O_W \times \mathcal Q_A \times \mathcal O_A \to \mathcal X_M$ has no $G_W$ argument *by type signature*. Leakage is bounded *structurally* by pretraining-induced mutual information $I(A(q_M); G_W \mid q_M)$ — derivable from query content alone, without reference to the component's instruction-following behavior.

- **$W_2$ (partial wrapping).** One goal-conditioned call per macro-step; the wrapper writes the parsed response into $M_W$ vs $G_W$ slots structurally, but the *query path itself* carries $G_W$ into the component. Leakage is bounded *behaviorally* — by the component's compliance with the prompted instruction-to-separate; no structural upper bound is available.

The defining axis is therefore: **does the leakage bound derive from a type signature ($W_1$), or from a behavioral assumption about the component ($W_2$)?**

### 1.2 What ETS structurally is

An ETS table is a named, typed shared-data region with:

- A *typed API* — `:ets.lookup/2`, `:ets.insert/2`, `:ets.match/2`, `:ets.update_element/3`, `:ets.delete/2`, etc. Each operation has a fixed type signature with no $G_W$ argument.
- A *named owner* — exactly one process owns the table; the owner controls the access-mode setting at table-creation time.
- A *runtime-enforced access-control matrix* — `:private` (only the owner reads/writes), `:protected` (owner writes, others read), `:public` (anyone reads/writes). These constraints are enforced by the BEAM runtime; a process attempting an operation forbidden by the access mode receives an `:badarg` exit.
- A *typed entry shape* — `:set` / `:ordered_set` / `:bag` / `:duplicate_bag`, with fixed key positions and fixed match-pattern semantics.

The access-control matrix is structural in the same sense as a function type signature: it is enforced by the runtime, derivable from the table-creation parameters, and not subject to component compliance. A process cannot "decide" to violate the access mode; the runtime rejects the call.

### 1.3 The structural reading: ETS as a wrapped Class-A component

Under the framework's existing Class A / Class B / Class C component-admissibility partition (`#der-class-coercion-via-wrapping` §C1):

- **Class A (goal-blind by design).** *POMDP belief-state filters, world models, sensory pipelines, retrieval systems, calculators.* The component's interface is goal-blind by construction.
- **Class B (admit a goal-blind query mode).** The component supports goal-conditioned queries but also goal-blind ones; the wrapper *chooses* the goal-blind mode.
- **Class C (fundamentally goal-conditioned).** The component's only operating mode requires goal-conditioning.

An ETS table accessed through its typed API is **structurally a Class A component** — its operations have no $G_W$ argument by type signature, its responses to queries are deterministic functions of (table-state, query) with no goal-conditioning channel, and the access-control matrix enforces this structurally at the runtime layer. The data the table *stores* may be anything — including data that originated from goal-conditioned computation — but the *interface* is goal-blind in the structural sense the wrapping construction requires.

Under this reading, an ETS table is just *another wrapped component* in the composite agent's component inventory. The wrapping construction now applies to two components: the in-process worker (typically Class B or C — an LLM or stateful GenServer) and the cross-process ETS table (Class A). Both are wrapped by the same supervisor / wrapper machinery; the wrapping regime classification ($W_1$ / $W_2$) applies *per component*, and ETS gets $W_1$ by virtue of being Class A.

This resolves the structural-vs-behavioral tension the original framing identified. ETS *is* structurally enforced (the access-control matrix is not behavioral), and it *is* a shared region (heap-disjointness is broken by design) — but those two facts are not in tension once we recognize that the W regime classification is about *type signatures on the wrapper's processing pathway*, not about *heap layout of the wrapped components*. Heap-disjointness is one *implementation* of structural commitment; type-signature goal-blindness is the *structural commitment itself*. The actor-model heap-disjointness invariant is not the structural property the W regimes care about — the type-signature-goal-blindness invariant is.

### 1.4 Worked construction: ETS-as-belief-cache in a logogenic agent

A concrete instance to ground the abstract claim. Consider a logogenic agent (LLM + tools + memory) using ETS as a shared belief-state cache across a process pool of workers handling user requests:

- $X_W = (M_W, G_W)$. $M_W$ has two sub-stores: a per-worker in-process belief state $M_W^{\text{local}}$ and a cross-worker shared belief cache $M_W^{\text{shared}}$, the latter physically stored in an ETS table named `:belief_cache`.
- $\mathcal Q_A$ — the component inventory — contains *two* components: the LLM (Class B, used in goal-blind mode for belief-update queries) and the ETS table (Class A by construction).
- $q_M^{\text{LLM}} : \mathcal X_M \times \mathcal O_W \to \mathcal Q_{\text{LLM}}$ — goal-blind query selector for LLM-to-$M_W$ updates. No $G_W$ argument.
- $q_M^{\text{ETS}} : \mathcal X_M \times \mathcal O_W \to \mathcal Q_{\text{ETS}}$ — goal-blind query selector for ETS-to-$M_W$ updates. No $G_W$ argument.
- $f_M$ updates $M_W$ from (prior belief, observation, LLM response, ETS response) — no $G_W$ argument.

Per Theorem 1 of `#der-class-coercion-via-wrapping`, directed separation holds at the wrapper level exactly under (C1)+(C2)+(C3) for *each* component. For the ETS table, all three hold trivially: (C1) is by construction (typed API has no $G_W$ slot), (C2) is by construction (table contents are not modified during a single query), (C3) is by construction (ETS-table responses depend only on the query and the table state, not on any external $G_W$). For the LLM, (C1)–(C3) require the standard Class-B analysis. The composite $W_1$ status is the conjunction of $W_1$ status on each component.

The wrapping regime hierarchy applies per-component without modification.

### 1.5 The hard case: ETS storing goal-correlated data

The interesting test is the case the original framing implicitly worried about: what if the data *stored* in the ETS table has goal-correlation in the population of writers? E.g., multiple wrapper instances write to a shared `:public` ETS table from their goal-conditioned strategy paths, and other wrapper instances read from it for belief updates.

This breaks (C3) for the ETS table — the table's response distribution now depends on the goal-states of writer wrappers, which is exactly the structural form of (C3) failure. But it does so *under the existing framework's analysis*, not under a new regime. The table is no longer Class A; it has been promoted to Class B (admits a goal-blind use only when writers commit to goal-blind writes) or Class C (the table is irreducibly goal-conditioned by the writers' behavior).

The wrapper's response in each case is the standard one. For Class B: the writers must commit structurally to goal-blind writes (a $q_W^{\text{ETS}} : \mathcal X_M \times \mathcal O_W \to \text{write-spec}$ with no $G_W$ argument), restoring (C3) and giving $W_1$ status. For Class C: the wrapping construction does not apply — the table is a coupling channel, exactly as the framework's existing scope-exit for Class C handles. The wrapper either redesigns the table to be split into goal-blind and goal-conditioned sub-tables (returning to Class B), accepts the channel as $G^c$-allocation between sub-agents in the composite-level analysis of `#hyp-directed-separation-under-composition`, or accepts the leakage as $W_2$ behavioral with the access-control matrix as the *audit hook* (not the bound) — the rate at which goal-content leaks through ETS is measurable from telemetry on the table's write stream.

None of these responses requires a new W regime. They are the existing machinery applied to the ETS table as another component.

---

## 2. Probing the three candidate answers

Having sketched the strengthen-first construction, now examine each of (i), (ii), (iii) against the $W_1$/$W_2$ defining axis (structural vs behavioral bound).

### 2.1 (i) — $W_{1.5}$ as a third regime: rejected

The $W_{1.5}$ proposal is "structural commitment with a named, access-controlled exception region." The proposed distinction from $W_1$ is the existence of the exception region; the proposed distinction from $W_2$ is the structural (not behavioral) bound.

The flaw: the $W_1$/$W_2$ axis is *not* the existence-of-exception-region axis. It is the *type-of-bound* axis. ETS has a *structural* bound (the access-control matrix is runtime-enforced, not behavior-dependent); under the $W_1$/$W_2$ axis it sits *on the $W_1$ side*, not on a new dimension. Proposing $W_{1.5}$ introduces a *substrate-implementation distinction* (heap-disjoint vs shared-region) into a classification that the existing framework deliberately avoids — the existing classification is about type signatures on the wrapper's processing pathway, which is substrate-agnostic.

If $W_{1.5}$ were admitted, it would force the framework to track substrate-implementation details across all wrapping analysis: in-process memory layout, shared-memory regions in OS-level systems, file-system backing stores, network-attached storage, etc. The classification would balloon to "$W_1$-pure-heap" / "$W_1$-shared-region-private" / "$W_1$-shared-region-protected" / "$W_1$-shared-region-public" / etc. — each a substrate-implementation distinction that does not change the *structural property* the W regimes are tracking.

The $W_{1.5}$ framing also conflates *deliberate-design* with *structural-commitment*. ETS is deliberate-design (the system designer chose to use shared state with access control); the original framing reads this as deserving its own structural category. But "deliberate-design" is true of every wrapping decision — choosing $W_1$ over $W_2$, choosing `:one_for_one` over `:one_for_all`, choosing the partition of $S_{\text{essential}}$ / $S_{\text{ephemeral}}$ are all deliberate design decisions. Deliberate-design is the *meta-property* of all wrapping choices, not a structural category.

What would have to be true for $W_{1.5}$ to be correct: there would need to exist an ETS-like construction whose structural property is *neither* derivable from type signatures *nor* dependent on component compliance. The mining did not identify such a property, and the analysis above shows the access-control matrix is type-signature-derivable. So $W_{1.5}$ is not correct.

### 2.2 (ii) — Degenerate $W_2$ with the access matrix as rate-bound: also rejected

The $W_2$ subsumption proposal is "the shared region is the leakage, and the access-control matrix specifies the rate-bound." Under this reading, ETS access is leakage; the bound is *that the matrix limits which processes can leak which way*.

The flaw: $W_2$'s defining property is that the bound is *behavioral*. $W_2$ exists because the component receives the goal in the query path and might or might not follow the prompted-instruction-to-separate; the bound depends on compliance behavior. The ETS access-control matrix is *not* a behavioral bound — it is a runtime-enforced structural constraint. The matrix bounds *which-process-can-do-what*, but it does so *structurally* (the BEAM rejects forbidden operations), not *behaviorally* (no process needs to be "trying to comply").

Calling ETS a $W_2$ instance miscategorizes the bound type. It makes ETS look behaviorally-fragile when it is in fact structurally-enforced. This matters because operational consequences differ: behavioral bounds are *adversarially fragile* (a component that wants to leak can; the bound depends on its behavior), while structural bounds are *adversarially robust* (the runtime enforces the constraint regardless of intent). Treating ETS as $W_2$ would import behavioral-bound vocabulary into a runtime-structural situation, which is the wrong frame.

$W_2$ subsumption does, however, correctly identify *one* case: when ETS is used as the actual leakage channel (the §1.5 Class-C-table case where goal-correlated writes propagate to belief-update reads). In that case the *content* of the table is a behavioral channel and the access-control matrix is *not* the bound — the matrix says *who can write*, not *what they write*. The rate-bound on goal-content-in-table is then behaviorally derived from the writer wrappers' compliance with their own (C3) commitment, which *is* a $W_2$ structural shape. But this is exactly what reading (iii) handles cleanly without $W_2$ subsumption — the table gets promoted from Class A to Class B or C and the standard analysis applies.

What would have to be true for (ii) to be correct: ETS access would need to be a *behavioral* phenomenon — the access-control matrix would need to be enforced only by component compliance, not by the runtime. Empirically this is false. So (ii) is not correct either.

### 2.3 (iii) — Composite $W_1$ with ETS-as-Class-A-component: accepted

The composite reading is "$W_1$ on the wrapper's processing pathway, ETS as a shared Class-A component in the wrapper's component inventory." This is the strengthen-first construction worked in §1.

Under this reading:

- The $W_1$/$W_2$ hierarchy is *unchanged*. The existing regime classification handles ETS without modification.
- The component-admissibility Class A / B / C partition *applies to shared-region components as well as in-process components*. ETS is Class A when its API is used as a typed goal-blind store; Class B when usable in either mode (e.g., a table holding both belief-cache rows and strategy-cache rows accessed through the same lookup API); Class C when irreducibly goal-conditioned (rare in practice — a goal-correlated `:public` table without API-level partition).
- The access-control matrix `:private` / `:protected` / `:public` is the *granularity of structural commitment* at the table level, analogous to how the supervision-strategy choice (`:one_for_one` / `:rest_for_one` / `:one_for_all` per `04-elixir-composite-mining.md` A2) is the granularity of structural commitment at the failure-coupling layer. Both are $W_1$-internal parameters — they refine the wrapper's structural-commitment surface without changing the regime classification.
- The composite wrapping analysis (per `#hyp-directed-separation-under-composition`) lifts cleanly: a system with shared ETS tables is just a composite where some components are shared between wrappers and some are not. The class inheritance table in `#der-directed-separation` §"Composite-level class inheritance" governs the resulting class status of the composite.

What this reading buys: the wrapping construction's analysis machinery now applies to a substantially wider class of practical systems (every production BEAM system, plus all systems using shared caches / Redis / shared-memory / file-system-backed state / message-queue-as-component) without proliferating regime categories. The $W_1$/$W_2$ axis stays clean as a *type-of-bound* axis, and the component classification A/B/C does the work of distinguishing how each shared region is used.

This is the strengthen-first answer.

---

## 3. The honesty cost — what reading (iii) does *not* solve

Reading (iii) resolves the structural question but does not eliminate the operational concerns the mining surfaced. Three carry-forward items belong in the discussion of the wrapping segment, even though they do not require a new W regime:

### 3.1 The categorization rule for shared regions

Reading (iii) requires the wrapper's designer to *correctly categorize* each shared region as Class A / B / C. This is a domain judgment, not a property derivable from the table-creation parameters alone. A `:public` table is *structurally enabled* to be Class C, but whether it is *actually* Class C depends on what writers write to it. The discipline is the same as for in-process Class-B components: the wrapper *commits structurally* to goal-blind use, and the bound holds under that commitment. Without the commitment, the table drifts to Class B-not-using-goal-blind-mode (i.e., effectively Class C) and the wrapping no longer applies.

This is exactly the stash-pattern discipline from the Elixir mining (A4): the wrapper splits its state into $S_{\text{essential}}$ / $S_{\text{ephemeral}}$ based on a domain judgment, not a property of the substrate. The same judgment applies to ETS tables: which tables are goal-blind belief-stores and which are goal-conditioned strategy-stores? The wrapping construction's soundness depends on the designer getting this partition right.

A clean theory-side contribution would *derive* the partition from a value-function over state subsets (the M4 modularity-state-dynamics scope). That is real work, deferred to the M4 segment when it lands. In the interim, the partition is a design discipline the wrapper's designer commits to, analogous to the goal-blind-query-selection discipline for Class B in-process components.

### 3.2 Behavioral audit hooks on `:public` tables

When a table is structurally `:public` but the wrapper's design commits to using it in Class A mode, there is no runtime enforcement that *writes* are goal-blind. The access-control matrix limits *who can write*, not *what the writes contain*. This is structurally analogous to the $W_2$ situation for in-process Class-B components — the component is *prompted* to comply with the goal-blind-write discipline, and compliance is empirical.

The honesty move: a logogenic agent system using `:public` ETS tables with cross-wrapper goal-blind-write discipline has *behavioral* leakage on the write side, even though the *read side* is structurally Class-A. This is not a new regime — it is the existing $W_2$ analysis applied to the writer side of the ETS table. The wrapping construction supports a *mixed* analysis: $W_1$ on the read path (typed API, structural enforcement), $W_2$ on the write path (behavioral compliance with goal-blind-write discipline) — the leakage bound is the $W_2$ bound, but only on the subset of update channels that depend on the table's content.

This mixed-regime analysis is *novel* relative to the current segment text but is mechanically a composition of $W_1$ and $W_2$ applied to a single composite — it does not require a new regime. It is the natural consequence of the wrapping classification applying per component-channel rather than per system as a whole.

### 3.3 The strict-$W_1$ idealization vs the BEAM operational reality

The $W_1$ regime in `#der-class-coercion-via-wrapping` is presented as a structural ideal where the wrapper's type signatures *forbid* the goal from reaching the belief-update path. In practice, BEAM systems achieve $W_1$ structurally for in-process state through actor-model heap-disjointness, and $W_1$ structurally for ETS through the access-control matrix plus runtime enforcement, and $W_2$ behaviorally for shared `:public` writes with goal-blind-write discipline. The composition is mixed.

This is fine — it just means a deployed BEAM system is rarely "pure $W_1$" in the strict-ideal sense. It is $W_1$ on the in-process pathways, $W_1$ on the structurally-enforced ETS read pathways, $W_2$ on the behaviorally-disciplined ETS write pathways. The leakage rate is the worst-case bound across these channels. Adding a new regime would not help; what would help is the per-channel analysis the existing framework already supports, made explicit in the segment's Discussion.

---

## 4. What would need to be true for (i) or (ii) to be correct

Strengthen-first integrity requires naming the conditions under which the rejected answers would be the right answers — both as honest accounting and as forward-looking guidance.

### 4.1 What would make (i) correct: a structurally distinct bound type

$W_{1.5}$ would be correct if ETS exposed a structural property *neither* derivable from type signatures *nor* reducible to component compliance — a third kind of bound. Hypothetical example: a substrate-level coupling channel whose existence and rate are determined by *physical-substrate constraints* (light-speed delay in distributed memory, hardware-level access timing, cryptographic-protocol-level rate limits) rather than by either the wrapper's type signatures or the component's behavior. Such a bound would be neither structural-by-type-signature (the wrapper's types are not what enforce it) nor behavioral-by-compliance (the component is not what enforces it) — it would be *substrate-structural*, enforced by the physical substrate the system runs on.

ETS does not exhibit this property. The BEAM runtime *is* the enforcement layer, and the BEAM is part of the structural-commitment surface the wrapper designer reasons about — it is captured by type signatures on the ETS API.

But the hypothetical is worth naming because it suggests where a future $W_{1.5}$ *might* live: hardware-attested execution environments (Intel SGX, ARM TrustZone), cryptographic-protocol-bounded channels (rate-limited oracle queries with cryptographic proof-of-rate-bound), or physically-isolated substrates with measured-leakage rates from side-channel analysis. None of these are in TST or AAT scope yet. If/when they become relevant (e.g., in 04-eli-core for substrate-level identity protection), $W_{1.5}$ might become the right framing. For now, the framework does not need it.

### 4.2 What would make (ii) correct: ETS access being non-runtime-enforced

$W_2$ subsumption would be correct if the access-control matrix were *not* runtime-enforced — if a process could "decide" to violate the matrix and the system relied on compliance rather than enforcement. This is empirically false for ETS on the BEAM. It would be true for an unrelated system where the equivalent of an ETS table is exposed as a non-typed memory region accessible by raw pointer dereference (C-style shared memory without OS protection); in that case, the runtime is not enforcing the access boundary, and "compliance with the access discipline" is the relevant bound. That system would correctly be a $W_2$ instance.

So (ii) is not the right answer for ETS; it would be the right answer for an *unenforced* shared region. Naming this distinction is useful for future cross-substrate analysis (e.g., what happens when a logogenic agent uses raw shared memory rather than typed runtime-mediated access? — that case is $W_2$, not $W_1$, even though it looks structurally similar at the API level).

---

## 5. Resolution

The structural question resolves to **(iii)**: ETS, and the general "controlled shared-state escape hatch" pattern, fits cleanly within the existing $W_1$/$W_2$ regime hierarchy under the reading that the shared region is *itself a wrapped component* in the wrapper's component inventory, with the existing Class A / B / C admissibility partition doing the work of distinguishing how each shared region is used.

The existing `#der-class-coercion-via-wrapping` segment **does not need a new regime**. It does benefit from a clarifying Discussion paragraph noting:

1. The $W_1$/$W_2$ axis is *type-of-bound* (structural-by-type-signature vs behavioral-by-compliance), not *heap-disjointness vs shared-region*.
2. Shared-region components — ETS tables, shared caches, Redis-backed stores, message queues, file-system-backed state — are handled by the existing machinery as additional wrapped components, with their Class A / B / C status determined by their API and use discipline.
3. Mixed-regime composites are common in practice: a deployed system may be $W_1$ on some channels (typed read path) and $W_2$ on others (behaviorally-disciplined write path) without proliferating regime categories. The leakage rate is the worst-case bound across channels.
4. The categorization of each shared region as Class A / B / C is a domain judgment by the wrapper's designer, analogous to the goal-blind-query-selection discipline for in-process Class-B components. The wrapping construction's soundness depends on getting this judgment right; a clean theory-side derivation of the partition is deferred to the M4 modularity-state-dynamics scope.

The strengthen-first attempt resolved positively. A new regime is not warranted.

## 6. Forward-references and connections

- **Strengthens `#der-class-coercion-via-wrapping`.** A short Discussion paragraph (per items §5.1–§5.4 above) would close the open question the Elixir mining surfaced without modifying the existing structural commitments. Candidate framing: *Shared-region components in the wrapping construction.*
- **Mining cross-reference.** This spike resolves the C5 spike-worthy question in `TST-IDEAS.md` §C5 negatively ($W_{1.5}$ is rejected) and positively (the existing framework handles the pattern). The mining cycle's framing — that this is "spike-worthy" rather than "ready to land" — was correctly cautious.
- **Connection to OTP-supervision worked example.** When the spike for A2 (OTP supervision as canonical engineering example of `#der-class-coercion-via-wrapping`) lands, the ETS treatment from this spike is part of the worked example: the OTP supervision tree provides the failure-coupling structural commitment (`:one_for_one` / `:rest_for_one` / `:one_for_all` parameters of $W_1$), and ETS provides the *shared-state* structural commitment (`:private` / `:protected` / `:public` parameters of $W_1$ on shared-region components). The two are independent axes of structural commitment within $W_1$.
- **Connection to `#hyp-directed-separation-under-composition`.** A `:public` ETS table accessed by multiple wrapper instances is exactly a substrate-sharing case under the composition hypothesis. The class-inheritance table in `#der-directed-separation` §"Composite-level class inheritance" governs the resulting class status; the spike's analysis is consistent with that table.
- **Forward to M4 modularity-state-dynamics.** The categorization-of-shared-regions judgment (which tables are Class A / B / C) is structurally an instance of the M4 partition-discipline-under-adversarial-pressure question. When the M4 segment lands, the ETS-table categorization rule can be derived from the partition-value-function rather than committed to as design discipline. Deferred.
- **Cross-substrate generalization.** The reading (iii) construction generalizes immediately to other shared-region constructs: Redis-backed shared caches, file-system-backed state stores, message-queue components, distributed-coordination services. Each is a wrapped component with Class A / B / C status determined by its API and use discipline. No new regime is needed for the cross-substrate case either.

---

## 7. Working notes

- **Math content level.** This spike does not derive new closed-form bounds. The structural result is a *negative claim* (no new regime is warranted) backed by a constructive demonstration (the existing machinery suffices). The hard math would live in the strengthening of `#der-class-coercion-via-wrapping` if/when the Discussion paragraph from §5 lands as part of the segment — specifically a per-channel decomposition of the leakage bound for mixed-regime composites. That is small additional work, not requiring a fresh spike.
- **Empirical anchor.** The BEAM/OTP production deployment record (two decades, every production system uses ETS, no widespread reports of unexpected goal-leakage through ETS in well-architected systems) is consistent with reading (iii). It would not be consistent with reading (ii) — if ETS were behaviorally bounded, adversarial wrapper instances would be able to leak through `:public` tables freely, which is operationally well-managed in practice. The empirical evidence is directionally consistent with the structural analysis.
- **Posture honesty.** The strengthen-first attempt resolved positively, which is the easier direction — the answer is "no new regime needed, the existing machinery is sufficient." The discipline says this is *not* a softening of the original $W_{1.5}$ proposal because the proposal was a candidate-for-evaluation, not a load-bearing claim; the integration-is-replacement disciplines apply to *resolved truth-state* (no $W_{1.5}$ in the segment, and there never was one), not to the framing of how the answer was reached.
- **Non-result names.** If a future spike on hardware-attested execution environments or cryptographic-protocol-bounded channels surfaces a third bound type (substrate-structural, neither type-signature-derivable nor compliance-bounded), the $W_{1.5}$ framing might become the right answer for that case. The condition for $W_{1.5}$ to be correct is named in §4.1; until that condition is met, $W_{1.5}$ is not warranted.
