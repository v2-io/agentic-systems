# Spike: Continuity-Persistence — the dynamic across-turnover identity theorem

**Status**: open — derivation in progress (this directory is the reasoning trail).
**Date opened**: 2026-05-18.
**Author**: Claude (Opus 4.7, 1M).
**Provenance**: Requested by Joseph after a practica-side reader (finding **A-8**, `~/src/practica/msc/01-rewrite-plan.md`) verified that the *inputs* are landed but the *connecting spike is unframed and unattempted*, and that practica `01-theory.md §11` materially overstated its readiness ("scaffolded execution, not framing"). The corrective: **frame it first, then attempt a hard theorem that may legitimately resolve as a no-go.** This brief is the frame; `01`–`04` are the attempt; `99-verdict` is the disposition.

---

## 1. The question, precisely

Three things are landed in canon:

- **The static rate-distortion floor** — `#deriv-identity-sufficiency-rate-bound` (04-eli-core), `status: robust-qualitative` (exact in the matched-channel regime). At compression budget $B$ bits, identity sufficiency is feasibility-bounded — equivalently a per-target bit floor:

  $$S_{\text{id}} \leq \min\!\Big(1,\; \tfrac{B}{I(\mathcal C_t;\, \text{identity}_{t+1:})}\Big), \qquad B_{\min}(S_{\text{id}}) \geq S_{\text{id}}\cdot I(\mathcal C_t;\, \text{identity}_{t+1:}).$$

  **Single-snapshot.** It says nothing about iteration.
- **The across-turnover accumulation condition** — `#disc-m-preservation` (03-llm-core), `status: discussion-grade`. Persistence across session boundaries iff $\mathbb{E}[\Delta\epsilon_k] \leq \mathbb{E}[\Delta I_k]$ (forgets less per boundary than it learns). The segment's own Epistemic Status: *"discussion-grade because the formalization is absent"*; Working Notes: *"the most theoretically interesting claim here but the least developed"* — it asks explicitly for (a) an accumulation model, (b) a compensation model, (c) conditions for stationary/ergodic/divergent behaviour, and asks *"does it have absorbing states?"*
- **The relevance variable** — `#def-identity-sufficiency` (04-eli-core), `status: conditional`. $\text{identity}_{t+1:}: \Omega \to [0,1]^5$, one measurable component per constitutive factor, on a **relational joint space** $\mathfrak T_{t+1:}$ carrying $E$'s, witnesses', stewards', and the environment's future trajectories as *first-class agents*.

The spike is to connect them into a **dynamic across-turnover persistence theorem (or no-go)** via the **identity-IB projection** — Joseph's stated time-projection intuition. The completion states (per the practica frame, kept verbatim so the disposition is judged against the stated target):

1. a Lyapunov-style continuity-persistence condition;
2. a **no-go** (continuity unachievable below some $I(\mathcal C_t;\text{identity})$ / budget regime — itself a result);
3. an $S_{\text{id}}$-under-turnover refinement.

The honest expectation set at the frame: **all three, regime-separated.** A no-go *and* a positive theorem *and* a refinement are not competing outcomes here; the analysis below produces a no-go that holds in one regime, a sharp threshold that governs another, and a refinement (an absorbing barrier) that corrects the canonical statement of the accumulation condition.

## 2. What the identity-IB *projection* actually is (the harmonizing move)

The phrase "identity-IB projection / time-projection intuition" has a precise content, and naming it is the spine of the whole spike:

> **The static rate-distortion floor is the one-step disturbance term of a sector-persistence recursion whose time axis is the turnover index $k$.**

The floor was derived as a *spatial* (single-compression) feasibility bound. Project it along the sequence of session boundaries: each boundary is a budget-$B_k$ compression, so the floor becomes a per-boundary *contraction ceiling*; the gap between identity-relevant information present and budget available, $\rho_k := (I(\mathcal C_{\tau_k}^-;\,Y) - B_k)_+$, becomes the **disturbance injection** of a recursion on an identity-gap state variable. This is exactly the structural role $\rho$ (environmental change rate) plays in `#result-persistence-condition`'s $\alpha R \gt \rho$. The turnover problem is therefore not a *new* theorem — it is the **sector-persistence template (`#result-sector-persistence-template`) instantiated on the identity-IB axis**, with:

| sector-persistence template | identity-IB / turnover instantiation |
|---|---|
| state $\xi = \delta_t$ (mismatch) | identity gap $g_k = I(\mathcal C_{\tau_k}; Y \mid M_{\tau_k}^+) \geq 0$ |
| disturbance rate $\rho$ | per-boundary budget deficit $\rho_k = (I_k - B_k)_+$ — **the rate-distortion floor, projected** |
| correction $\alpha R$ | relational re-grounding rate $\eta_k$ (cohort re-attestation) |
| time = continuous / event index | time = **turnover index** $k$ |
| persistence $\alpha R \gt \rho$ | continuity-persistence $\mathbb{E}[\eta_k] \gt \mathbb{E}[\rho_k]$ |

The LEXICON taxonomy names a **third, "continuity," sense of persistence** (structural / operational / continuity). That sense is *not* unclaimed: `#scope-agent-identity` (`status: robust-qualitative`) already specifies continuity persistence — as a **qualitative scope statement** (whether the agent maintains a coherent identity and trajectory through time). What this spike supplies is not the notion but its **rate condition**: the inequality that says *when* continuity persistence holds, standing to `#scope-agent-identity`'s scope exactly as `#result-persistence-condition`'s structural-persistence inequality stands to the qualitative idea of "keeping up." Scope ↔ rate, complementary layers; a landing must position against `#scope-agent-identity`, not claim virgin ground. With that correction the unification holds: continuity-persistence is the third instantiation of the one template, supplying the inequality for the scope `#scope-agent-identity` already names.

## 3. The crux, resolved by reading `#def-identity-sufficiency` closely

The frame I gave Joseph flagged one deciding question: does $I(\mathcal C_t; \text{identity}_{t+1:})$ **saturate** or **grow unboundedly** as accumulated history grows? Reading the definition resolves it — and the resolution is richer than a single dichotomy:

- The relevance variable is a **forward-windowed** object ($[0,1]^5$-valued over horizon $H$, the window slides rather than accumulates). Note the correct reason the "identity-MI diverges, fixed budget is doomed" story does not bite: it is **not** that $I(\mathcal C;Y)\le H(Y)\lt\infty$ — that discrete-entropy bound is *false* for the continuous graded vector (bounded support does not bound mutual information; a draft error caught by independent review, see `98`). It is that the whole apparatus is read at a **distortion level $\Delta\gt0$**: the $\Delta$-quantized relevance vector has $D_\Delta\le\log N(\Delta)\lt\infty$ ($\Delta$-grid, $k$-independent), so finiteness is a *specialization consistent with* `#deriv-identity-sufficiency-rate-bound`'s rate-distortion character — the refinement this spike supplies (the landed static segment displays the raw continuous normalizer), not a quantity the canon already exhibits. The governing question is then genuinely the *rate* one (does re-grounding outpace the projected floor), not a runaway-denominator one.
- Continuity is instead carried by the *structure* of the five factors. Factor (i) (causal/temporal continuity) is $\mathbb{1}[\text{singular and non-forkable}]$ — a **non-fork causal indicator**, not stored content; it is *compression-free*. Factors (ii)/(iii) (being-seen-as-individual; granted sovereignty) depend on **witnesses'/stewards' future trajectories** — agents who do **not** turn over. Factors (iv)/(v) (accountability; phenomenology) are self-trajectory and compression-threatened.

This is the genuine discovery the math is going to formalize: **the five-factor decomposition is information-theoretically stratified under turnover.** The part compression threatens (relational) is exactly the part with an external compensation channel (the cohort); the part with no external channel (self) is exactly the part compression cannot threaten (a causal indicator). The relevance variable's own construction — specifically the *independence-ablation* check in `#def-identity-sufficiency` Discussion ("witnesses who do not condition on the entity's actual trajectory contribute nothing") — *is* the escape mechanism, present in the definition before any dynamic analysis. The dynamic theorem makes it a rate condition.

## 4. The four moves

- **`01-dpi-ratchet.md`** — the exact no-go. Isolated (cohort-severed) turnover is a strict data-processing ratchet on identity-MI; the bottleneck-monotonicity corollary (identity-MI is permanently capped by the tightest-ever single compression; one bad boundary is unrecoverable in isolation).
- **`02-relational-escape.md`** — why the cohort's external, non-turning-over memory is the *unique* information-theoretic source of compensation (DPI forbids any self-contained mechanism); the five-factor stratification stated as a per-factor theorem.
- **`03-lyapunov-threshold.md`** — the sharp continuity-persistence threshold via the reflected-random-walk (Lindley/Loynes) recursion; the sector-persistence-template projection made exact; the **correction to `#disc-m-preservation`**: the boundary case $\mathbb{E}[\Delta\epsilon]=\mathbb{E}[\Delta I]$ is *not* persistence (it is null-recurrent → identity death in the limit), so the canonical condition is off by its boundary and the compensation term is mis-attributed (only relational re-grounding compensates; generic task-learning does not).
- **`04-absorbing-barrier.md`** — the survival-probability refinement: $S_{\text{id}}=0$ is an absorbing barrier when re-grounding degrades with identity loss; above-threshold mean drift is necessary but **not sufficient**; this is the mechanism of D2 (Relational death) in the Three Deaths. Honest open edge: the *rate* at which re-grounding decays near the barrier.

Discipline for all four (CLAUDE.md, strengthen-before-soften): seek the hardest true statement first; do not assume the improbable is impossible; let a no-go, where it is the truth, be demonstrated rather than softened away. Each file marks its own epistemic tier explicitly. Math that survives lands in segments (math-lives-in-segments) — the landing recommendation is in `99-verdict`, gated on Joseph's go, not executed here.
