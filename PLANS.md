# ACT Development Roadmap

## Current State (March 2026)

**Adaptive systems foundation** (developed as TFT, now subsumed by ACT):
Well-developed. TF-00 through TF-11 plus appendices A-G. Simulation
battery (6 variants + Hafez bridge) has characterized the empirical
landscape:

- *Appendix A (Lyapunov/sector conditions)* is the strongest foundation —
  general, nonlinear, robust. Should be the formal backbone going forward.
- *The linear ODE* (TF-11) is a useful first approximation, correct for
  deterministic drift in the continuous-time limit, but NOT a general-case
  formulation. Under stochastic disturbances, E[|δ|] scales as ρ/√T (not
  ρ/T), giving adversarial exponent 3/2 (not 2).
- *Observation quality gates tempo advantage* — U_o collapses adversarial
  exponent from ~1.0 to ~0.2. TF-11 doesn't model this; it treats T as
  externally given rather than as a function of U_o via η*.
- *Scalar tempo is a poor summary* for anisotropic systems (72% overestimate).
  Per-dimension persistence condition is exact.
- *TF-06's gain principle* validated empirically (52% mismatch reduction
  with Riccati-optimal gain).

The implication for ACT: lean on Appendix A's sector-condition framework as
the general theory. The linear ODE is a worked example (correct in its
regime, valuable for intuition, not the general case). The stochastic
treatment (AR(1) steady-state, 3/2 exponent) should be developed as the
more physically realistic companion.

**Hafez Bridge**: Bi-predictability P is complementary to TFT, not
redundant. P measures coupling *architecture*; mismatch measures coupling
*performance*. Key findings: agency costs coherence (P drops from 0.44
to 0.27 with action), observation noise degrades P via H_f, P cannot
detect adversarial dynamics (scale-invariant). The ΔH decomposition
(forward/backward predictive uncertainty) is genuinely novel for TFT —
H_b = strategic legibility/opacity to adversaries, no current analog.
Potentially important for multi-agent adversarial work. **Caveat**: the
passive-vs-active comparison changes both state semantics (x_t → x̂_t)
and adds an action channel, so the P drop is suggestive but doesn't
cleanly isolate agency from representation choice. The architecture/
performance split is the stronger and cleaner result.

**Purposeful agency** (ACT's novel contribution): Exploratory sketch phase. Three convergence-
tested intent DAG formalism variants. Core structure identified (AND/OR nodes,
single-parameter edges, Orient cascade). The O_t (objective) / Σ_t (strategy)
distinction clarifies what was previously conflated under G_t. Not yet
consolidated into formal documents.

**Domain Instantiations**: TST-via-TFT mapping exists (priors/tst/via-tft/).
Needs rewriting as TST-via-ACT once the formalism stabilizes.

---

## The Rewrite: ACT as a Single End-to-End Theory

**Approach**: Not a ground-up rewrite, but a re-pass that gets framing and
ordering right from the beginning. Purpose, the agent spectrum, multi-agent
setup, and nonlinear foundations positioned correctly the first time. Much
of TFT's content survives; what changes is framing and ordering in the
early documents, and promotion of Appendix A / multi-agent from appendix
to main theory.

**Principles**:
- Monotonic concept introduction (no forward references)
- Purpose baked in from the start (the spectrum, not bolted on later)
- Sector-condition framework as primary (linear ODE as pedagogical example)
- Multi-agent as setup for theorems, not appendix bookend
- TST integrated naturally as software domain instantiation
- Epistemic honesty throughout — every claim tagged

### Document Structure (IN PROGRESS)

| Doc | Title | Source | Changes |
|-----|-------|--------|---------|
| ACT-01 | Scope: Agents Under Uncertainty | Rewrites TF-01 | **Significant.** Agent spectrum: {±model} × {±objective}. Four quadrants from the start. |
| ACT-02 | Causal Structure | Light revision of TF-02 | Add: two causal DAGs (reality + intent). Level 2 enables strategy. |
| ACT-03 | The Agent's State | **New**, replaces TF-03 | M_t + O_t + Σ_t together. IB formulation for M_t carries over. Directed separation. |
| ACT-04 | Event-Driven Dynamics | TF-04 ~unchanged | Events can update M_t, Σ_t, or both. |
| ACT-05 | Mismatch Signals | Expands TF-05 | δ_epistemic (carries over, Prop 5.1). Add δ_objective, δ_strategic. |
| ACT-06 | Update Gain and Tempo | Expands TF-06 | η* for M_t carries over. η_edge for Σ_t. Sector conditions primary. |
| ACT-07 | Persistence and Stability | **Rewrite**, promotes App A | Sector-condition threshold primary. Adaptive reserve. Stochastic regimes. Linear ODE → appendix. |
| ACT-08 | Strategy Structure | **New**, from consolidated doc | AND/OR, edge update, Orient cascade, depth fragility, observability dominance. |
| ACT-09 | Action, Deliberation, Exploration | Merges TF-07/08/09 | Action couples M_t, O_t, Σ_t. Three-way explore-exploit-pursue. |
| ACT-10 | Structural Adaptation | Revises TF-10 | Model class + strategy restructuring. Continuous spectrum. |
| ACT-11 | Multi-Agent Dynamics | **Rewrite**, promotes App F | Setup for adversarial theorems. Shared intent. Intent decomposition. Appendix F caveat on correlation. |
| ACT-12 | Adversarial Dynamics | Revises TF-11 adversarial + App A | Tempo advantage (sector form). Regime dependence. Observation gating. DAG targeting. |

**Appendices** (demoted / pedagogical):
- A: Linear ODE Approximation (demoted from TF-11)
- B: Worked Examples — Kalman (M_t only), PID (O_t only), RL (both)
- C: Operationalization Procedures
- D: Simulation Results Summary

**Software Domain Instantiation** (integrated, not separate):
TST content woven into relevant sections. Strongest claims:
- T-02 (specification bound): information-theoretic, genuinely strong
- T-04 (Bayesian baseline): E[n_future | n_past] = n_past, solid
- Code quality as observation infrastructure (novel insight from via-tft)
- Six unique properties of software as ACT domain
- Three-part tempo decomposition (T_obs + T_explore + T_probe)
- Persistence condition as unmaintainability threshold
Weaker claims (T-08 proportionality, T-09 exponential proximity) noted
as hypotheses needing validation.

### Progress Tracking

- [x] Intent DAG consolidated (scratch/04-intent-dag-consolidated.md)
- [ ] ACT-01: Scope (agent spectrum, four quadrants)
- [ ] ACT-02: Causal Structure (two DAGs, Level 2 → strategy)
- [ ] ACT-03: Agent State (M_t + O_t + Σ_t together)
- [ ] ACT-04: Event-Driven Dynamics
- [ ] ACT-05: Mismatch Signals (three types)
- [ ] ACT-06: Update Gain and Tempo
- [ ] ACT-07: Persistence and Stability
- [ ] ACT-08: Strategy Structure
- [ ] ACT-09: Action, Deliberation, Exploration
- [ ] ACT-10: Structural Adaptation
- [ ] ACT-11: Multi-Agent Dynamics
- [ ] ACT-12: Adversarial Dynamics
- [ ] Appendices
- [ ] Software domain instantiation sections

### Key Decisions Made

- ACT supersedes TFT (not "extends")
- AND/OR + single-p edges (drop WEIGHTED)
- Sector-condition framework primary (linear ODE pedagogical)
- O_t / Σ_t split (not G_t); point-valued G_t superseded
- Multi-agent is main content, not appendix
- Correlated observations as default (independence as special case)
- TST integrated as domain instantiation with epistemic regrading

### Context for Future Agents

**If you're picking this up**: The rewrite absorbs TFT's mathematical
content into ACT with better framing. Read scratch/04-intent-dag-
consolidated.md for the purposeful-agency formalism. The key insight is
that purpose (O_t, Σ_t) should be introduced alongside M_t from ACT-03
onward, even though the math for M_t can be developed independently
(directed separation). This way the reader never encounters a theory
that "lacks goals" — the spectrum is visible from the start.

**What carries over from TFT mostly unchanged**: TF-02 (causal structure),
TF-04 (event dynamics), TF-05 (mismatch, Prop 5.1), TF-06 (gain
principle), TF-10 (structural adaptation, Prop 10.1), Appendix A
(Lyapunov — this gets promoted to main). The mathematical results are
sound; what changes is framing and ordering.

**What needs real rewriting**: TF-01 (scope — add agent spectrum), TF-03
(model — introduce M_t + O_t + Σ_t together), TF-11 (tempo/persistence —
promote Appendix A, demote linear ODE), Appendix F (multi-agent — promote
to main content, fix correlation assumption).

**TST integration**: The strongest TST claims (T-02 specification bound,
T-04 Bayesian baseline) are genuinely well-grounded. The "code quality as
observation infrastructure" insight from via-tft/mapping.md is the single
most valuable novel contribution. Weaker claims (T-08 proportionality,
T-09 exponential proximity, T-06 circularity) need honest epistemic tags.

**Agentic-tft corpus** (../agentic-tft/docs 00-14): Contains cognitive
loop spec, evaluation framework, crèche concept, narrative circle, and
bootstrap problem. Relevant to AI agent domain instantiation but not yet
integrated into ACT formal documents.

---

## Validation (after rewrite stabilizes)

- Extend nonlinear sims to characterize regime boundaries
- Developer-as-ACT-agent on real codebase (software worked example)
- Test DAG health metrics against real project outcome data
- Multi-agent intent propagation simulation
- TST testable predictions: temporal ordering in fine-tuning,
  specification bound calibration, coherence-coupling measurement

---

## Issues to Resolve (from Codex review, March 2026)

### Simulation model mismatch — RESOLVED
Both deterministic and stochastic models now tested (Variants A-D):
- Deterministic drift: exponent = 2.0 confirmed (Cor 11.2 correct)
- Stochastic: exponent = 1.5 (E[|δ|] ∝ 1/√T, not 1/T)
- Original sim2's ~1.05 was non-coupling-dominant + stochastic
TF-11 updated with regime-dependence note. The question is now: which
physical domains correspond to which disturbance model?

### Central object model (high priority, in progress)
The G_t symbol has been used for three different things: desired end-state,
strategy graph, and committed intent. The O_t / Σ_t split (objective vs
strategy) is a start. Codex suggests a four-way split: M_t (world model),
D_t (desired end-state), S_t (strategy graph), I_t (committed intent).
The D_t/I_t distinction looks useful: Desire is the holistic model of what
the agent wants (including hopes, aspirations, conditional preferences,
opportunistic shortcuts); Committed Intent is the subset that focuses
action (the actual plan being executed). Desires can persist as latent
opportunities ("if this becomes feasible, grab it") without consuming
action capacity. This distinction likely becomes load-bearing in
multi-agent settings (shared desire vs shared commitment; what you tell
allies you want vs what you're actually doing). Two paths to explore;
defer pruning until multi-agent work reveals which bears more weight.

### Credibility leaks (medium, mostly fixed)
- ~~Founding notes reference ~/src/ paths~~ — FIXED
- ~~sim2 prints "R -> infinity: exponent -> 2.0" but stochastic asymptote
  is 1.5~~ — FIXED (now prints 1.5 with note about deterministic drift)
- ~~Simulation spec claims |δ| distribution is "approximately exponential"
  but stationary law is half-normal~~ — FIXED (spec now says half-normal)
- Simulation spec R-sweep prediction updated (1.5, not 2.0)

### TST reframing (medium-high, for when TST-via-ACT is written)
TST's real content is a **temporal optimization target** (minimize expected
comprehension + implementation time under repeated handoff), not a theorem
of software engineering. This is a coherent and useful domain objective,
but it does not subsume deadline asymmetry, safety-critical downside,
optionality, or irreversible loss. The strong claims:
- T-01 (temporal optimality) is tautological by construction
- T-02 (specification bound) and T-04 (Bayesian baseline) are genuinely
  well-grounded
- T-08 (time ∝ |changeset|) and T-09 (exponential proximity) are
  unvalidated proportionalities labeled as "empirical" without empirical
  data
- T-06 (change investment) has a circularity: architecture choice affects
  future change patterns, which affects n_future, which justifies the
  architecture choice
When TST becomes a domain instantiation of ACT, every claim should be
regraded with TFT-style epistemic tags. The older submodule language must
not leak back into ACT as mathematics. The strongest novel insight from
TST-via-TFT (code quality as observation-infrastructure investment that
lowers future U_o) should be preserved and highlighted.

### Consolidate DAG variants (medium)
Three competing formalism variants exist. The convergence testing identified
what's principled (AND/OR, single-p, Orient cascade) vs scaffold (node
taxonomy, specific metrics). Need one canonical treatment with alternatives
clearly demoted to reference material.

---

## Open Questions

1. Does the information bottleneck principle for shared intent produce
   non-obvious predictions about organizational communication structure?

2. Can the intent DAG formalism handle temporal dependencies (action
   ordering) as well as causal dependencies?

3. How does 100% context turnover interact with the intent DAG? O_t and
   Σ_t may survive context death (via CLAUDE.md) even when M_t doesn't.

4. Is there a "comprehension vs action" optimal allocation derivable from
   the dual-mismatch framework? Too much M_t focus delays goal-pursuit;
   too much goal-pursuit with bad M_t wastes action on wrong paths.

5. **Hafez bridge — PARTIALLY ANSWERED.** P correlates with T (monotonic,
   modest in 1D). P cannot detect adversarial dynamics (scale-invariant).
   The clean delineation: P = coupling architecture, mismatch = coupling
   performance. Remaining: can P be *derived from* ACT quantities formally
   (not just correlated)? Can ΔH (strategic legibility) be incorporated
   into multi-agent adversarial dynamics?

6. What is the relationship between ACT and active inference's prior
   preferences? Is there a formal equivalence or are they genuinely
   different?

7. **Which physical domains have deterministic vs stochastic ρ?** This
   determines whether the adversarial exponent is 2 or 3/2. Military
   (persistent adversary action) may be closer to deterministic.
   Software (sporadic requirement changes) may be closer to stochastic.
   Biological (environmental fluctuations) likely stochastic.

8. **Should ΔH (Hafez's forward/backward asymmetry) become a formal
   quantity in ACT?** H_b = strategic legibility — how predictable your
   actions are from outcomes. Low H_b = transparent to adversaries.
   High H_b = strategically opaque. This has no current ACT analog
   and could be load-bearing for adversarial multi-agent dynamics.

9. **Cognitive cost of maintaining Σ_t.** TF-03 has β (compression cost
   for M_t). The intent DAG has no analog. A commander with a 500-node
   strategy DAG faces a qualitatively different cognitive load than one
   with 12 nodes, even at identical path confidences. For AI agents with
   finite context windows, this is not abstract — the DAG must fit in
   working memory or be compressed. This connects to IB-compressed shared
   intent, but for the self: how much of your own strategy can you hold?

10. **DAG acyclicity scope.** The formalism assumes acyclicity (motivated
    by Pearl), but real control loops are cyclic. Acyclicity holds after
    time-unrolling or option-level abstraction. State the assumption and
    its scope explicitly. Does the formalism break if we allow cycles
    (e.g., monitor → adjust → monitor)?

11. **δ_feasibility formalization.** Of the three proposed mismatch
    signals (epistemic, goal, feasibility), feasibility mismatch is the
    least crisp — it's a second-order inference ("trying hard with good
    model, gap not closing, therefore goal may be infeasible"). Possible
    formalization: likelihood ratio test on Σ_t's critical-path
    confidence vs. observed progress rate.
