# Pending Findings — 2026-04-21 Late

**Status**: Working note. Two substantive theoretical findings that survived the 2026-04-21 audit batch but were not executed in this session. Written to survive the TODO-04-21.md cleanup so these items are not lost.

**Date**: 2026-04-21

**Origin**:

- Gemini's second audit batch (pasted into the conversation after the first Gemini findings were added to and then removed with TODO).
- Codex's third audit batch (finding #3: `observation-ambiguity-modulation`).

Other findings from those batches were executed in this session and committed; only these two remain.

---

## Finding A — Temporal coarse-graining gap in `#form-composition-closure` (from Gemini) — RESOLVED 2026-04-22

**Resolution.** Option 3 (per-macro-step formulation with window-aware $\Lambda_o, \Lambda_a$) executed in `01-aad-core/src/form-composition-closure.md`. The segment now introduces the timescale ratio $K_c \geq 1$ alongside the admissibility conditions, rewrites $\varepsilon_x, \varepsilon_a, \varepsilon_o$ to sum over macro-steps $m$, restates (P1) at macro-step granularity, adds an explicit unit-consistency note to the bridge lemma, and records $K_c = 1$ as the previous-formulation special case (the two-Kalman instantiation continues to live there). The sector-persistence-template cross-reference now shows $e_m$ (trajectory error at macro-boundaries) rather than $e_t$. Option 2 (full Mori-Zwanzig equilibrium form) remains an optional future refinement — the current fix is clean at $K_c \gg 1$ without committing to a singular-perturbation framing. The previously described below Repair options / Recommended path / Estimated effort are retained for historical record.

### Original finding

**Problem.** `#form-composition-closure` defines the state closure defect as

$$\varepsilon_x = \mathbb E_\tau \Big[\tfrac{1}{H}\sum_{t=1}^H \big\lVert \Lambda_x(f_{\text{micro}}(X_{\text{micro},t}, o_{\text{micro},t+1})) - f_c(\Lambda_x(X_{\text{micro},t}), \Lambda_o(o_{\text{micro},t+1})) \big\rVert \Big]$$

The macro-dynamics $f_c$ is evaluated at every micro-timestep $t$, forcing synchronous micro-and-macro update cadence. But `#der-temporal-nesting` establishes that composite agents naturally operate on slower timescales ($\nu_{\text{level }n+1} \ll \nu_{\text{level }n}$); the closure-defect formulation as written cannot express a macro-agent that updates every $K \gg 1$ micro-steps. This conflicts with the singular-perturbation / Tikhonov treatment that composition-closure's own Working Notes reference (via Mori-Zwanzig spike), and it prohibits one of the primary structural benefits of composition (timescale abstraction).

**Confidence**: High (Gemini) — the equation literally iterates micro-timesteps.

**Msc context**: Timescale-separation math appears in `spikes/spike-discrete-time-sector.md`, `spikes/spike-purposeful-agent-derivation.md`, and `ref/agentic-tft/agentic-tft-ontology-unification.md` ("the faster level must complete many correction cycles before the slower level takes a single step"). None of it has been incorporated into `#form-composition-closure`'s formulation. The original composition-generating spike (`spikes/spike-agent-composition.md`) didn't bridge singular perturbation into the $\varepsilon^\ast$ definition, leaving the core expression stranded at zero-timescale-separation.

### Repair options

**Option 1: Aggregated micro-window.** Redefine $\varepsilon_x$ over a *coarse-grained* micro-window: the macro-update ingests an aggregate $\bar o_{\text{micro},t:t+K}$ (the projection of $K$ micro-observations) and the closure defect sums over macro-timesteps, not micro-timesteps. Requires specifying the aggregation operator within $\Lambda_o$ and makes $\Lambda$'s type signature $\mathcal O_{\text{micro}}^K \to \mathcal O_c$ rather than $\mathcal O_{\text{micro}} \to \mathcal O_c$.

$$\varepsilon_x = \mathbb E_\tau \Big[\tfrac{1}{\lfloor H/K \rfloor}\sum_{m=1}^{\lfloor H/K \rfloor} \big\lVert \Lambda_x(X_{\text{micro},mK}) - f_c^{(K)}(\Lambda_x(X_{\text{micro},(m-1)K}), \bar o_{(m-1)K:mK}) \big\rVert \Big]$$

**Option 2: Tikhonov equilibrium form.** Express the closure defect as a singular-perturbation residual: the inner (fast) dynamics reach quasi-equilibrium relative to the outer (slow) dynamics, and $\varepsilon^\ast$ measures the residual at the equilibrium manifold. Most principled fix; connects to the Mori-Zwanzig treatment partially covered in Working Notes.

**Option 3: Per-macro-step formulation.** Let the macro-step $T$ correspond to $K$ micro-steps; redefine $\varepsilon_x$ over macro-steps only, with $\Lambda_o$ aggregating micro-observations over the $K$-window. Simpler than option 2 but equivalent for many purposes.

### Recommended path

Option 1 or Option 3 for a clean fix; Option 2 if one wants to connect the composition theory to Tikhonov/Mori-Zwanzig explicitly. The fix touches `#form-composition-closure`'s definition directly — a non-trivial modification, not a side note. Requires re-verifying the bridge lemma for the coarse-grained form (the contraction argument should still go through because the template's Lyapunov analysis is timescale-agnostic once the disturbance rate is defined relative to the macro timestep).

### Estimated effort

90–120 minutes for Option 1 or Option 3 including bridge-lemma re-verification. 3–5 sessions for Option 2 with full Mori-Zwanzig integration.

### Why deferred

The repair changes a core definition in `#form-composition-closure`. Best executed with explicit review of the specific approach before committing. The existing `#form-composition-closure` is widely depended upon; a bad refactor would cascade.

---

## Finding B — `observation-ambiguity-modulation` is architecture-contaminated (from Codex) — RESOLVED 2026-04-22

**Resolution.** The definition of $\mathcal{A}(e_\tau)$ has been recast as an observation-stream property at the Bayesian-optimal level:

$$\mathcal{A}(e_\tau) = \frac{I(G;\, \Omega_\tau \mid e_\tau, M_{\tau^-})}{H(\Omega_\tau \mid e_\tau, M_{\tau^-})}$$

under a reference goal prior $P_{\text{ref}}(G)$. No reference to hypothetical $\kappa = 0$ or $\kappa = 1$ processors appears in the definition — both quantities are Bayesian-optimal properties of the observation-world joint distribution. The architectural $\kappa_{\text{processing}}$ enters only through the explicit scope-condition composition $\kappa_{\text{eff}} = \kappa \cdot \mathcal{A}$. The bias bound simplifies cleanly to $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot I(G;\Omega\mid e,M)$ — a strict refinement of the coarser bound in `#result-section-ii-survival`.

**Operational estimator** rewritten to use a reference interpreter as a measurement instrument (probing the observation's interpretive latitude under different goal-primings), not as the subject of measurement. The processor-probing form of $\hat\kappa_{\text{processing}}$ (present the same observation to the *agent under test* under different goals) has moved to `#der-directed-separation`, where it belongs canonically as a processor property.

**Holistic scan result.** Six other logogenic segments (`ai-agent-as-act-agent`, `coupled-update-dynamics`, `coupled-diagnostic-framework`, `section-ii-survival`, `m-preservation`, `context-turnover`) were checked for similar architecture-contamination patterns. None carry the same category error — they use $\kappa_{\text{processing}}$ legitimately as a scope-classification primitive or as a parameter in bias bounds. The contamination was localized to `observation-ambiguity-modulation`; the holistic pass-and-fix pattern recommended by the pending-findings note was not warranted. Downstream consumers (`section-ii-survival` line 75, `coupled-diagnostic-framework` line 87) use the product form $\kappa \cdot \mathcal{A}$ and are unaffected by the reformulation.

The below Problem / Repair direction / Estimated effort / Why deferred sections are retained for historical record.

### Original finding

**Problem.** `03-logogenic-agents/src/scope-observation-ambiguity-modulation.md` defines ambiguity $A(e)$ using *hypothetical* $\kappa = 1$ and $\kappa = 0$ processors, then uses that definition downstream. The same segment's §79 concedes that the product form is not derived and the operational definitions are only proposals. The issue: the present variable is *architecture-contaminated* — it is defined by reference to hypothetical agent architectures rather than to a property of the observation stream itself. This makes it operationally muddy and not cleanly identifiable from data.

**Confidence**: Medium (Codex). The intuition (that some observations are more ambiguous than others) is right; the operationalization as currently written conflates observation properties with processor properties.

**Msc context**: `spikes/spike-kappa-hb-operationalization.md` already separates $\kappa_{\text{selection}}$ (which events the agent chooses to attend to) from $\kappa_{\text{processing}}$ (how the agent interprets attended events). `spikes/spike-kappa-synthesis.md` argues topology class is the primary distinction and that the scalar-$\kappa$ treatment was a category error — the resolution eventually landed in `#der-directed-separation`'s Class 1/2/3 architectural classification. The cleaner split has not been propagated into `observation-ambiguity-modulation`.

### Repair direction

Recast $A(e)$ as a property of the observation event itself — e.g., the conditional entropy of the generative process given the event, or the variance of the posterior the event induces on some reference task — not as a difference between hypothetical processors. Then ambiguity is a domain quantity (observation-stream property) and the $\kappa$-modulation in the downstream formulas becomes explicit rather than built into the variable's definition.

### Estimated effort

60–90 minutes, assuming the spike material in `spike-kappa-hb-operationalization.md` can be adapted. Requires care because the downstream `section-ii-survival` scorecard references ambiguity in its error-structure analysis; the revision should preserve those cross-references.

### Why deferred

`observation-ambiguity-modulation` is in `03-logogenic-agents/`, which is framework-stage per CLAUDE.md. Other logogenic segments may make similar architecture-contaminated moves; a single-segment fix may need to be part of a broader logogenic consistency pass. Worth scoping the logogenic-wide review before executing the point fix.

---

## Notes for the next agent

- Both findings should probably be executed in a single session (they are independent and neither blocks the other).
- Both findings resolved on 2026-04-22 (see each's top stanza). This file now serves as a historical record of the 2026-04-21 audit residue and the 2026-04-22 resolution.
- Historical prioritization note (retained for context): Finding A was the more theoretically load-bearing because it corrected a real definitional bug in `#form-composition-closure` preventing the timescale abstraction that was always part of its intent. Finding B was a logogenic-framework hygiene issue that recast an architecture-contaminated definition as an observation-stream property.
- `spikes/spike-ib-unification-plan.md` is the IB scoping spike that informed `#disc-compression-operations`. It remains as the record for any future push toward full IB unification (currently deferred per the synthesis-first recommendation).
- `audits/opus-audit-2026-04-21.md` is the master audit that drove the 2026-04-21 work. Its findings §1–4 and bigger-picture synthesis §1, §2, §3, §4 (partial), §5 are all addressed in the segments. §6 is embodied in `#result-sector-persistence-template`. §7 ($G_t$ as single object) and §8 (continuous convention hierarchy) are deferred as foundational moves awaiting the right context.
