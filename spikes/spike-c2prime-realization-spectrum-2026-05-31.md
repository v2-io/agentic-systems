# Spike: The (C2′)-realization spectrum — is separate-substrate necessary for a structural W₁?

**Status**: exploratory / analysis complete. **Read-only on canon; no edits, no git.** No status/tier transitions proposed for landing without Joseph's gate.
**Date**: 2026-05-31
**Trigger**: spun off in `#der-logogenic-as-wrapping` Working Notes (2026-05-31, Stage-1 propagation from `fbcb36a`): *"the (C2′)-realization spectrum (is separate-substrate necessary, or do stateless-reset / state-stripping single-substrate constructions also earn it)."* Practically live because it bears on the shoshin / PROPRIUM W₂→W₁ path.
**Reads**: `#der-logogenic-as-wrapping`, `#def-auxilia-hierarchy`, `#der-class-coercion-via-wrapping` (esp. the (C2′) condition + the corrected selection-channel bound), `#disc-w1-structural-bound-boundary` (the certifiability-discontinuity no-go). Implementation reality: `~/src/shoshin/src/shoshin/{interpres,conspectus,backend}.py`; `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §6 (Auxilia Infrastructure), `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §6.2 (ANIMA / IMPERIUM).
**Sibling spikes**: `spike-w1-leakage-vacuity-2026-05-31.md` (introduced (C2′) + the no-go), `spike-w1-w2-boundary-intuition-2026-05-31.md` (the $\Theta(\varepsilon^2)$-flat / certificate-step toy).

---

## 0. What is actually being asked

The canon (post Stage-1, commit `fbcb36a`) now says the W₁ *structural* leakage bound

$$\kappa_{W_1}^{\text{sel}} = I\big(A(q_M);\, G^{\text{op}}\big) \le I\big(q_M;\, G^{\text{op}}\big)$$

is available **iff** (C2′) holds — no goal-correlated component state crosses the goal-blind ($q_M$) / goal-conditioned ($q_G$) call boundary (`#der-class-coercion-via-wrapping` Conditions; `#disc-w1-structural-bound-boundary`). In several places canon then asserts, in passing, that **separate-substrate auxilia** satisfy (C2′) "by construction" while a **single LLM sharing one persistent conversation** violates it, and notes that **stateless separate calls** also satisfy it. So three candidate realizations are floating:

- **(i) Separate substrates** — distinct model instances/processes for the belief-side ($q_M$) and strategy-side ($q_G$) calls (the auxilia hierarchy of `#def-auxilia-hierarchy`).
- **(ii) Single LLM, stateless calls** — one model, but each call gets a fresh context (no shared KV-cache, no carried conversation); the belief call and strategy call are independent invocations.
- **(iii) Single LLM, state-stripping** — one model that *does* carry context across the boundary, but the carried state is scrubbed of $\Sigma$- and $G$-content before the goal-blind call (the "$\Sigma$-channel-suppressed W₁" Working Note of `#der-class-coercion-via-wrapping`).

The live question: **is (i) necessary** for a structural (C2′)-satisfying W₁, or do (ii)/(iii) genuinely earn the structural bound at lower tempo cost? And downstream: **what is the best (C2′)-realization for PROPRIUM/shoshin** — must the W₂→W₁ path build the separate-substrate auxilia hierarchy, or can disciplined single-substrate cache/state management earn a structural bound more cheaply?

The strengthen-first instinct here cuts *against* the apparent "you need separate substrates" reading: before conceding that auxilia are necessary, attempt to show the cheaper realizations earn the same structural guarantee. The verdict below is that they can — separate-substrate is **sufficient but not necessary** — and the real necessary condition is a property of the *state*, not the *substrate count*.

---

## 1. Read (C2′) literally — it is a condition on state, not on substrate

The canonical statement of (C2′) (`#der-class-coercion-via-wrapping` Conditions):

> **(C2′) No goal-correlated cross-call state.** The component's hidden state does not carry information about the latent operator goal $G^{\text{op}}$ across the boundary between the goal-blind ($q_M$) and goal-conditioned ($q_G$) calls of a macro-step. Equivalently, $A$'s response to $q_M$ is conditionally independent of $G^{\text{op}}$ given $q_M$ and the component's *pre-call* state, and that pre-call state is itself goal-uncorrelated — either reset across the call boundary, or stripped of $\Sigma$- and $G$-content.

Two things are immediately visible from the text itself:

1. **(C2′) quantifies over a property of the carried state $S$, not over the number of substrates.** What it forbids is $S \not\perp G^{\text{op}}$ at the moment the goal-blind call runs. The phrase "the component carries no information about the latent operator goal across the boundary" is silent on *how many model instances* implement the component. A single instance whose cross-call state is goal-uncorrelated satisfies the predicate exactly as a fresh instance does.

2. **The condition already names two distinct discharges** — "*reset* across the call boundary" (statelessness) **or** "*stripped* of $\Sigma$- and $G$-content" (state-stripping). The disjunction is in the canon as written. So the canon's own formal statement does *not* force separate-substrate; the "by construction" auxilia phrasing in `#der-logogenic-as-wrapping` / `#def-auxilia-hierarchy` is one *sufficient* discharge, not the definition.

This is the whole answer to the necessity question in nuce, and the rest of the spike makes it precise and then asks what the realizations actually cost. The "you need separate substrates" reading is a category slip: it reads a *sufficient implementation* of (C2′) as if it were *the* condition. The condition is $S \perp G^{\text{op}}$ at the goal-blind call. Separate substrate is one way to guarantee it; it is not the only way, and it is not what the bound's derivation uses.

**Check against the derivation.** The structural bound's proof (`#der-class-coercion-via-wrapping`, *Derivation* of the W₁-selection-leakage bound; sibling `spike-w1-leakage-vacuity` §3.2) needs exactly one thing: that $G^{\text{op}} \to q_M \to A(q_M)$ is a Markov chain — i.e. that $A(q_M)$ depends on $G^{\text{op}}$ *only through* $q_M$. The no-go (`#disc-w1-structural-bound-boundary`, §"The no-go") breaks that chain only when there is a *second edge* $G^{\text{op}} \to S \to A(q_M)$ that bypasses the query. The edge exists iff the pre-call state $S$ is goal-correlated. Nothing in either argument references substrate identity. The Markov chain holds whenever $S \perp G^{\text{op}}$, whoever owns $S$.

---

## 2. The realization spectrum, against the actual condition

The condition that earns the structural bound is the single predicate

$$\textbf{(C2$'$)}: \quad S_{\text{pre-}q_M} \perp G^{\text{op}},$$

where $S_{\text{pre-}q_M}$ is the component's state at the instant the goal-blind call is issued. Each candidate realization is a different *way of guaranteeing* this predicate, with a different cost profile and a different *auditability* (how hard it is to certify the predicate actually holds). Lay them on one axis — increasing reliance on substrate separation, decreasing reliance on discipline:

| Realization | How it discharges (C2′) | Cross-call state $S$ | Earns structural bound? |
|---|---|---|---|
| **(0) W₂ — shared conversation** | does not | $S \supseteq$ prior $G$-conditioned call's $\Sigma/G$ content; $S \not\perp G^{\text{op}}$ | **No** — behavioral only (the canon's "single LLM sharing one persistent conversation") |
| **(iii) State-stripping (single substrate)** | scrub $\Sigma/G$-content from carried state before $q_M$ | $S$ carried but goal-decorrelated by construction of the strip | **Yes, conditionally** — iff the strip is complete (see §3) |
| **(ii) Stateless calls (single substrate)** | fresh context per call; no shared KV-cache | $S = \varnothing$ (or fixed goal-blind init) | **Yes** — vacuously $S \perp G^{\text{op}}$ |
| **(i) Separate substrates (auxilia)** | distinct instances; $q_M$-substrate never sees $G/\Sigma$ at all | $S$ of the $q_M$-substrate is goal-blind by isolation | **Yes** — and (C2′) is an *invariant* of the architecture, not a per-step discipline |

The ordering (0) → (iii) → (ii) → (i) is *monotone in structural robustness of the guarantee* and (as §4 shows) *roughly monotone in tempo cost*. The key reading: **(ii) and (iii) sit strictly inside the structural-bound regime** — they are not W₂. They earn the *same* $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ bound (i) earns, because all three make $G^{\text{op}} \to q_M \to A(q_M)$ a genuine Markov chain. What differs across (i)–(iii) is **not the bound** but the **auditability of the (C2′) premise** — and (for (iii)) a residual risk that the discharge is incomplete.

### Necessity verdict

**Separate-substrate is sufficient but NOT necessary** for a structural (C2′)-satisfying W₁. The necessary-and-sufficient condition is $S_{\text{pre-}q_M} \perp G^{\text{op}}$. Stateless separate calls (ii) earn it vacuously on a single substrate; complete state-stripping (iii) earns it by construction on a single substrate. The auxilia hierarchy (i) is one — particularly *auditable* — way to guarantee the predicate as an architectural invariant, not the only way to satisfy it.

---

## 3. Is "stateless" too strong? — the goal-correlated component is the real condition

Joseph's sharper question: is full statelessness too strong, with only the *goal-correlated* component of the state needing clearing — so state-stripping (iii) is the real condition and full statelessness (ii) is sufficient-but-not-necessary?

**Yes.** The Markov-chain requirement is $A(q_M) \perp G^{\text{op}} \mid q_M$ given the pre-call state — which needs only $S_{\text{pre-}q_M} \perp G^{\text{op}}$, **not** $S_{\text{pre-}q_M} = \varnothing$. A component can carry arbitrary *goal-uncorrelated* state across the boundary — a cache of world-facts, a summary of the observation stream, retrieval of $G$-blind episodic memory — without reopening the leak channel. The no-go's second edge $G^{\text{op}} \to S \to A(q_M)$ requires $S \not\perp G^{\text{op}}$; if $S$ carries world-content but no goal-content, the edge has zero capacity and the DPI argument survives unchanged.

So the realization hierarchy has a clean logical structure:

$$\underbrace{S = \varnothing}_{\text{(ii) stateless}} \ \Longrightarrow\ \underbrace{S \perp G^{\text{op}}}_{\text{(iii) state-stripped} \;=\; \text{the real condition}} \ \Longleftrightarrow\ \textbf{(C2$'$)}.$$

Statelessness is the *coarsest* sufficient condition (it clears everything, goal-correlated or not); state-stripping is the *exact* condition (clear precisely the goal-correlated component, keep the rest). This matters for PROPRIUM specifically because the belief-side call *wants* world-context to make a good update — the §"Quality–separation tradeoff" of `#der-class-coercion-via-wrapping` is precisely the tension between information-rich $q_M$ and low $I(q_M; G^{\text{op}})$. **State-stripping is the realization that lets you keep the world-context while clearing only the goal-content** — it is the realization that buys the most belief-update quality per unit of structural guarantee. Full statelessness throws the world-context out with the goal-content.

### The catch: "goal-correlated" is exactly the hard thing to certify

State-stripping is the *theoretically optimal* condition but the *hardest to audit*, and this is the crux of the whole spectrum. To certify (iii) you must certify that the retained state $S$ carries **no** $G^{\text{op}}$-information — i.e. estimate $I(S; G^{\text{op}}) = 0$. Two difficulties:

1. **$G^{\text{op}}$ is latent.** Same obstruction as estimating the bound itself (sibling spike §7 "Estimator"; `#der-class-coercion-via-wrapping` Working Notes). You cannot directly measure independence from a variable you cannot observe.

2. **Decorrelating is not the same as redacting tokens.** Stripping the *literal* $\Sigma$/$G$ strings from the carried context does not guarantee $S \perp G^{\text{op}}$ — world-content can be *goal-correlated* (the "input-structure extraction" competence of `#der-class-coercion-via-wrapping` §"Two senses of component competence": a competent model infers $G^{\text{op}}$ from world-content surface form). A summary that has been written *by a goal-conditioned call* is goal-correlated even if it contains no goal tokens. This is the deep version of the leakage-source list (a)–(d) in `#der-logogenic-as-wrapping`, now operating on the *carried state* rather than the *query*: the strip must remove not just goal-tokens but goal-*correlated content*, which is a model-capability-dependent, empirically-characterized property — exactly the kind of thing that lives in a *behavioral* certificate, not a *structural* one.

So there is a subtle near-collapse: **an incompletely-verified state-strip is, certificationally, W₂-shaped** — its guarantee depends on an empirical property of the model (did the strip actually decorrelate?) rather than a structural invariant. The certifiability-discontinuity of `#disc-w1-structural-bound-boundary` applies *within* (iii): the strip either achieves $S \perp G^{\text{op}}$ (structural bound, the certificate is true) or it does not (the certificate computes the same reassuring number but is false, and only behavioral monitoring is honest). State-stripping does not escape the (C2′) wall; it relocates the question to *whether the strip is complete*, and that question is itself behavioral.

---

## 4. Tradeoffs across (i)–(iii): tempo, residual leakage, auditability

Three axes. The brief names all three; take them in turn.

### 4.1 Tempo ($K$ component-calls per macro-step)

The wrapping tempo cost (`#der-class-coercion-via-wrapping`; `#der-class-coercion-in-composition` Brooks's-Law overhead) is paid in *component calls per macro-step*, and *all three structural realizations pay the same minimal $K \ge 2$* — one $q_M$ call, one $q_G$ call. Substrate count does not change $K$:

- **(i) separate substrates**: $K = K_M + 1$ (per `#der-logogenic-as-wrapping`: $K_M$ auxilia belief-calls + 1 strategy call). Calls run on *different* substrates, so they can run **in parallel** — wall-clock tempo can be better than serial even though $K$ is the same, and the $q_M$ calls run on *cheaper* substrates (the auxilia substrate hierarchy of `#def-auxilia-hierarchy` H3 — the explicit cost-of-existence argument in `PROPRIUM-ARCHITECTURE-v2.md` §6.2: memory consolidation, pattern-recognition on 70B local, not frontier).
- **(ii) stateless single substrate**: $K \ge 2$ on one substrate, **serial** (one model). No parallelism benefit; every call pays the frontier substrate's cost. Each call also re-pays the *prompt-ingestion* cost of re-establishing context from scratch (no KV-cache reuse) — a real per-call tax that (i) avoids on its cheap substrates and (iii) avoids by carrying the cache.
- **(iii) state-stripping single substrate**: $K \ge 2$ serial, but the carried (stripped) state means the belief call does **not** re-pay full context ingestion — the cheapest *per-call* of the single-substrate options, but the strip operation itself has a cost (and if the strip is done by a model call, it is itself a $+1$ to $K$).

Net: **(i) wins on tempo** in the realistic regime — parallelism + cheap substrates for the high-frequency belief-side work — which is exactly why the auxilia hierarchy is the architecture's economic answer (the scaffolding-tax forcing function, `#def-auxilia-hierarchy` Discussion / `#disc-five-forcing-functions` F1). The single-substrate options trade that away. So separate-substrate is not necessary for the *bound*, but it is the tempo-favorable realization *when the belief-side work is voluminous and cheap-substrate-able*. When belief-side work genuinely needs frontier capability, the tempo gap narrows.

### 4.2 Residual selection-leakage $\kappa_{W_1}^{\text{sel}}$

**Identical across (i)–(iii) for a fixed query-selection policy.** The structural bound $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ is a property of the *query-selection policy* (what goal-content rides in the $q_M$ the wrapper chooses), not of how the $q_M$ call is hosted. Once (C2′) is satisfied — by *any* of (i)–(iii) — the residual leak is the same selection-channel quantity. Substrate choice does not move $\kappa_{W_1}^{\text{sel}}$; query design does.

One genuine asymmetry: realization (i)'s cheap auxilia substrates may have *different* pretraining distributions than the frontier strategy substrate, which changes the *realized* leak (the "inference effect" gap below the ceiling, `#der-class-coercion-via-wrapping` §"Two senses of component competence"). A weaker belief-side model is a *worse input-structure extractor* — it infers $G^{\text{op}}$ from query content less well — so it may sit *further below* the $I(q_M; G^{\text{op}})$ ceiling. This is a (modest, speculative) *advantage* of (i): the cheap substrate is not only cheaper, it may be a structurally weaker goal-inference channel. Discussion-grade observation, not a claim — it depends on whether the cheap substrate's *world-simulation* fidelity stays high enough to make a useful belief update while its *goal-extraction* competence drops. Flagged as a pull-on thread, not a result.

### 4.3 Auditability — the decisive axis

This is where the realizations genuinely differ, and it is the axis the necessity verdict turns on for *practice*. The question is: **can you certify that (C2′) holds?** Per `#disc-w1-structural-bound-boundary`, the entire value of (C2′)-statelessness is concentrated in *what it lets you prove*, not in marginal leakage prevented — so the realization that makes the proof *easy and robust* is the one that delivers the structural bound's actual payoff.

- **(i) separate substrates — (C2′) is an architectural invariant, certifiable by inspection.** The belief-side substrate *never receives* $G/\Sigma$ content — it has no port for it (the auxilia receives a system prompt assembled from AXIOMATA + relevant VERA/PRAXES, *not* OPERATA/strategy — `PROPRIUM-ARCHITECTURE-v2.md` §6.1). $S \perp G^{\text{op}}$ is then a *static, structural* fact about the wiring: you certify it the way `#der-class-coercion-via-wrapping` Theorem 1 certifies the closed processing path — by type signature, *no goal argument exists*. **This is the same certifiability move one level up**: just as Theorem 1 closes the $G_W \to f_M$ processing path by the $q_M$ type signature having no $G_W$ argument, separate-substrate closes the $G^{\text{op}} \to S \to A(q_M)$ state path by the belief-substrate having no $G$-input channel. Perturbation-stable, inspectable, does not depend on any per-step discipline being executed correctly. This is the analog of the certifiability boundary in the GUC-class spikes (`spike-guc-class-boundaries-intuition-2026-05-31`): the structural realization differs from a behaviorally-identical disciplined one *precisely on the `certifiable` flag*.

- **(ii) stateless single substrate — certifiable, but by an operational discipline (cache hygiene), not by architecture.** $S = \varnothing$ is checkable (was a fresh context used? was the KV-cache cleared?), but it is a *runtime property of every invocation* rather than a static property of the wiring. The certificate is "we reset the cache every call" — a discipline that can be violated by a config change, a caching optimization, a framework default that silently reuses context. It is auditable but *fragile-by-omission*: the failure mode is a performance optimization quietly reintroducing the shared cache (precisely the W₂-by-accident slide). Easier to certify than (iii), harder than (i), and the failure is silent (recall the $\Theta(\varepsilon^2)$ flatness — a leaked cache produces almost no behavioral signal while destroying the certificate).

- **(iii) state-stripping single substrate — hardest to certify; the certificate is itself behavioral.** Per §3: certifying $I(S; G^{\text{op}}) = 0$ for a stripped-but-nonempty $S$ requires establishing that the strip removed all *goal-correlated content*, not just goal-tokens — a model-capability-dependent, empirically-estimated property against a latent $G^{\text{op}}$. The (C2′) certificate here has the *same epistemic status as a W₂ behavioral bound* (it rests on an empirical property of the model), even though the *intent* is structural. State-stripping is theoretically the most information-efficient (keep world-context, drop goal-context) but it pays for that efficiency in certifiability: it is a structural bound only to the extent the strip is provably complete, and provable-completeness against a latent goal is exactly what is hard.

**The auditability ordering inverts the tempo ordering.** (i) is most auditable and most tempo-favorable; (iii) is least auditable and (per-call) cheapest-to-set-up but requires the most fragile verification; (ii) is in between on both. So separate-substrate's real advantage is not that it is *necessary* for the bound — it is that it is the realization where (C2′) is a **cheap-to-certify architectural invariant** rather than a per-step discipline or a latent-variable estimation problem. **A separate substrate is easier to certify than a state-stripping discipline on one substrate** — directly answering the brief's sub-question. That is its load-bearing virtue, and it is an *epistemic* virtue (provability), consistent with `#disc-w1-structural-bound-boundary`'s reading that the whole point of (C2′) is what it lets you prove.

---

## 5. Best (C2′)-realization for PROPRIUM / shoshin

### 5.1 Implementation reality (verified)

- **shoshin is W₂, single-substrate, single-call, full-bundle — confirmed against source.** `interpres.py::_assemble_context` builds one context dict containing AXIOMATA + active OPERATA + VERA + MEMORATA + PRAXES + CONSORTIA + recent CHRONICA + recent ACTUS, and ships it through one `backend.generate(context)` call per cycle (`receive_event`). OPERATA = operational intent/plans = $\Sigma$/$G$-content, and it rides in the *same* call that produces the belief-side writes (`vera_writes`, `memorata_writes`). The structural separation lives only at the *write boundary* (the typed `ModelResponse` fields routed by `_apply_writes`), exactly as `#der-logogenic-as-wrapping` says. There is no $q_M$/$q_G$ split. This is realization (0) — not even W₁-attempted.

- **PROPRIUM-architecture's auxilia are designed as realization (i) but not for the (C2′) reason.** `PROPRIUM-ARCHITECTURE-v2.md` §6 specifies auxilia "as separate model calls (API or local)" as *Buildable Now*, with the migration path internalizing toward attention head groups. §6.1 is the load-bearing detail: each auxilia receives a system prompt assembled from AXIOMATA + relevant VERA/PRAXES/CONSORTIA/MEMORATA — **notably not OPERATA** (the strategy/goal store). So the *architecture as specified already withholds goal-content from the belief-side auxilia* — it is (C2′)-by-construction *if the assembly discipline holds*, but the architecture document motivates auxilia by *cost* (substrate-cost hierarchy, scaffolding tax) and *abstraction* (H5 slower macro-clock), not by the directed-separation certificate. The (C2′) reading is a *new structural justification* for a design choice already made on economic grounds.

- **ANIMA's IMPERIUM/ARBITRIUM split (`PROPRIUM-ONTOLOGY-v2.md` §6.2; `#def-auxilia-hierarchy` Discussion) is the runtime-level (C2′) analog** — internal deliberation (IMPERIUM) separated from external interaction (ARBITRIUM) so the latter cannot manipulate the former's processing. That is the same "goal-correlated channel must not reach the belief update" discipline at the runtime layer. It is currently a structural *intent*, not a certified invariant.

### 5.2 Does shoshin's W₂→W₁ path *require* building the auxilia hierarchy?

**No — not for the structural bound.** Three viable paths, in increasing build cost:

1. **(ii) on shoshin's existing single backend — cheapest first step.** Split `receive_event` into two `backend.generate` calls with *separately assembled contexts*: a belief-call whose context is the (C2′)-safe subset — `_assemble_context` minus OPERATA and minus any goal-conditioned MEMORATA/CONSORTIA — and a strategy-call with the full bundle. Crucially, the two calls must **not** share a conversation/KV-cache (shoshin's `ModelBackend` protocol is stateless per call by construction — `generate(context) -> ModelResponse` takes a fresh context dict each time and holds no inter-call state, so a naive two-call split is *already* realization (ii) as long as the belief-context excludes goal-content). This earns the structural bound with **no new substrate** — it is a refactor of `_assemble_context` into `_assemble_belief_context` / `_assemble_strategy_context` plus a second backend call. The cost is tempo ($K: 1 \to 2$ serial on the frontier substrate) and the certificate is the cache-hygiene discipline of §4.3(ii).

2. **(iii) state-stripping** — only worth it if shoshin moves to a stateful/cached backend for tempo and then needs to claw back the structural bound. Given shoshin's *current* stateless-per-call backend protocol, (iii) is a solution to a problem shoshin does not yet have. Defer.

3. **(i) auxilia hierarchy** — the architecture's destination for *economic and tempo* reasons (cheap substrates for high-frequency belief work, parallelism, the cost-of-existence argument), which *also* gives the most auditable (C2′) certificate. Build this when the cost-of-existence / tempo pressure forces it, not when the structural bound is the only goal — because (ii) already delivers the bound.

### 5.3 Recommendation

**For the structural bound *as such*, shoshin should take path (ii) first: a two-call split on the existing single backend with a (C2′)-safe belief-context (OPERATA-excluded), no shared cache.** This is the minimum move that exits W₂ for a structural W₁, it is a context-assembly refactor rather than an infrastructure build, and shoshin's stateless `ModelBackend` protocol already provides the (C2′)-discharge for free as long as the belief-context excludes goal-content. The auxilia hierarchy (i) remains the *architectural destination* — but it is forced by **cost-of-existence and tempo**, not by the directed-separation certificate. Separating these two justifications is the substantive finding: **the auxilia hierarchy is necessary for sustainable-cost ELI existence; it is not necessary for the structural directed-separation bound.** The bound is available the moment the belief-side call's *context* is goal-uncorrelated and uncached, on one substrate.

The most information-efficient realization (iii, state-stripping — keep world-context, drop goal-context) is also the least auditable; recommend it *only* if a future stateful/cached shoshin backend makes the per-call ingestion cost of (ii) painful, and even then with explicit acknowledgment that its (C2′) certificate is behavioral-grade until the strip's goal-decorrelation is empirically established.

---

## 6. Does this change the auxilia-necessity story in canon? (the gated question)

**Yes — it sharpens it, and the sharpening is a correction of emphasis, not a contradiction.** Joseph gates any canon change; the following is the proposed reading, not an edit.

Several canon passages currently phrase the auxilia / separate-substrate relationship to (C2′) in a way that *invites* the "separate-substrate is necessary for the structural bound" misreading, even though the formal (C2′) statement does not say it:

- `#der-logogenic-as-wrapping` §Formal Expression: *"separate-substrate auxilia satisfy (C2′) by construction (structural bound); a single LLM sharing one persistent conversation violates it (behavioral W₂ only)"* — true as stated, but juxtaposing only the two *endpoints* (separate-substrate vs shared-conversation) and omitting that stateless-separate-calls and state-stripping on a single substrate *also* satisfy (C2′). (The §Discussion and the Epistemic Status do mention "stateless separate calls" in passing — so the omission is one of *emphasis/placement*, not a flat error.)

- `#def-auxilia-hierarchy` §Discussion ("Auxilia as the constructive realization of strict wrapping"): *"because auxilia run on separate substrates that carry no goal-correlated state across the belief/strategy call boundary, they satisfy condition (C2′) … substrate separation is therefore not only a tempo-priced way to split the calls but the very thing that earns the structural guarantee."* The clause **"the very thing that earns the structural guarantee"** is the one that over-claims: substrate separation is *a* sufficient discharge of (C2′), and the *most auditable* one, but it is **not** "the very thing that earns" the bound — the bound is earned by $S \perp G^{\text{op}}$, which stateless or state-stripped single-substrate constructions also achieve. The honest sharpening: *substrate separation makes (C2′) a cheap-to-certify architectural invariant; it is sufficient, not necessary, for the structural bound.*

**Proposed canon-change (gated, not applied):**

1. In `#der-class-coercion-via-wrapping` (or `#disc-w1-structural-bound-boundary`), add a short paragraph naming the **(C2′)-realization spectrum** — stateless reset / state-stripping / separate-substrate as three discharges of the *one* condition $S \perp G^{\text{op}}$, with the explicit statement that **separate-substrate is sufficient but not necessary**, and that the realizations differ on *auditability* (architectural invariant vs runtime discipline vs latent-variable estimation), not on the *value* of the bound. This is the natural home because the no-go segment already frames (C2′) as a certifiability question — the spectrum is the "and here are the ways to be on the right side of it, ranked by how cheaply you can certify it" companion.

2. In `#def-auxilia-hierarchy` §Discussion, soften **"the very thing that earns the structural guarantee"** to the necessity-correct form: auxilia substrate-separation is *a sufficient and maximally-auditable* discharge of (C2′); the structural guarantee is earned by goal-uncorrelated cross-call state, of which substrate separation is one (particularly clean) realization. Keep the economic/tempo justification for auxilia exactly as-is — it is untouched and remains the real necessity driver.

3. In `#der-logogenic-as-wrapping` §Formal Expression, add stateless-separate-calls and state-stripping to the *same* sentence that currently contrasts only separate-substrate vs shared-conversation, so the three-point spectrum is visible at first read rather than only in the Discussion.

These are *emphasis/scope corrections* that make the necessity structure honest; none of them weakens the bound, the no-go, or Theorem 1. The economic case for the auxilia hierarchy is entirely preserved — the finding is that it stands on *cost-of-existence and tempo*, which was always the architecture's primary justification, and that the directed-separation certificate is a *bonus* of the most-auditable realization rather than the thing that *requires* it. (Per *integration-is-replacement*: if landed, the "previously said 'the very thing that earns'" record goes to CHANGELOG / Working Notes, and the body states only the present-truth spectrum.)

**Why this is a sharpening, not a softening (strengthen-first check).** The instinct to "soften the auxilia-necessity claim" is the wrong frame. What is actually found is a *stronger* and *more useful* structural statement: the exact necessary-and-sufficient condition for the structural W₁ bound ($S \perp G^{\text{op}}$), a clean three-point realization spectrum discharging it, and the recognition that the discriminator across realizations is *auditability* — which connects directly to `#disc-w1-structural-bound-boundary`'s thesis that (C2′)'s whole value is provability. The bound, the no-go, and Theorem 1 all stand; what changes is that "you need separate substrates" is replaced by the more precise and more actionable "you need goal-uncorrelated cross-call state, and separate substrates are the cheapest way to *certify* that you have it." That is the hardest-true statement, not the easiest-honest one.

---

## 7. What I did not close

- **Estimator for $I(S; G^{\text{op}}) = 0$** (the (iii) certificate). Same latent-$G^{\text{op}}$ obstruction as the sibling spike's §7 estimator gap and the `#der-class-coercion-via-wrapping` Working-Notes decomposed-$\kappa$ estimator. The state-stripping certificate's behavioral grade is *because* this is open; closing it would let (iii) be certified structurally and would change its place on the auditability axis. Should be worked with the decomposed-estimator PROPOSED Tier-3 spike.
- **The cheap-substrate-as-weaker-goal-inferer advantage (§4.2)** is discussion-grade and speculative — it depends on the cheap belief substrate retaining enough world-simulation fidelity for a useful update while losing input-structure-extraction competence. Whether the two competences decouple favorably on real small models is empirical and connects to the PROPOSED Tier-2 decorrelation-by-construction spike.
- **Amplifying cross-call state** (the open edge of `#disc-w1-structural-bound-boundary` and `spike-w1-w2-boundary-intuition`): if retained state *amplifies* goal-content rather than carrying it linearly, the (iii) strip's residual could be super-linear rather than $\Theta(\varepsilon^2)$. Not chased here; it bears on how forgiving an *incomplete* strip is.
- **Multi-call compositional (C2′)** — a macro-step with $K_M \gt 1$ belief-calls (the realistic auxilia case) needs (C2′) to hold *pairwise* across every belief/strategy adjacency and *transitively* across the belief-call chain. The single-boundary analysis here covers the minimal $K = 2$ case; the compositional version (does goal-content leak through a *chain* of auxilia, e.g. a summarizer feeding a consolidator) connects to the wrapper-of-wrapper compositional-leakage conjecture in `#der-class-coercion-via-wrapping` Working Notes. Plausibly clean (DPI composes along the chain) but not verified.

---

## File index / cross-refs

- This file: `spikes/spike-c2prime-realization-spectrum-2026-05-31.md`
- Spun off from: `03-llm-core/src/der-logogenic-as-wrapping.md` Working Notes
- Reads: `01-aat-core/src/der-class-coercion-via-wrapping.md`, `01-aat-core/src/disc-w1-structural-bound-boundary.md`, `04-eli-core/src/def-auxilia-hierarchy.md`, `03-llm-core/src/der-logogenic-as-wrapping.md`
- Sibling spikes: `spikes/spike-w1-leakage-vacuity-2026-05-31.md` (introduced (C2′) + no-go), `spikes/spike-w1-w2-boundary-intuition-2026-05-31.md` (certifiability-discontinuity toy), `spikes/spike-guc-class-boundaries-intuition-2026-05-31.md` (certifiability-vs-behavioral boundary framing)
- Implementation reality: `~/src/shoshin/src/shoshin/interpres.py` (`_assemble_context`, `receive_event`), `~/src/shoshin/src/shoshin/backend.py` (`ModelBackend` stateless-per-call protocol); `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §6 (auxilia: separate calls, OPERATA-excluded system prompt), `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §6.2 (ANIMA / IMPERIUM-ARBITRIUM)
