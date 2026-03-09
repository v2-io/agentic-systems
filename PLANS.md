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

## Phase 1: Consolidation (immediate)

### 1.1 Consolidate Intent DAG Formalism
Merge the three variants (00-intent-dag-formalism, 02-alt-clean-slate,
03-alt-and-or-dag) into a single canonical treatment:
- AND/OR nodes with single-parameter edges (converged)
- **Drop WEIGHTED combination rule** — it reintroduces the two-parameter
  estimation problem (α weights) that single-p was supposed to solve. If
  k-of-n semantics are needed, model as nested AND/OR.
- Bayesian edge update mirroring TF-06 (converged)
- Orient cascade (converged)
- Node taxonomy: resolve categorical vs continuous (open — pick one and
  note the alternative)
- Strategic tempo T_G from the clean-slate variant
- Health metrics (keep the principled ones, flag scaffold ones)
- **Add identifiability section**: edges claim interventional semantics
  (p_ij = P(j | do(i), M_t)) but update from observational signals.
  State the identifiability assumptions explicitly. Note that software
  domains have genuine interventions (tests, deploys, git bisect); other
  domains (military, organizational) face confounding, delay, and
  correlation that make observational updates semantically weaker.
- **Write the Σ_t update dynamics formally**: the Orient cascade is
  described verbally but not yet given equations. This is the core novel
  contribution and needs TF-06-level rigor.

### 1.2 Adaptive-Systems Formal Rebalancing
Simulation findings (now added to TF-06, TF-11) revealed that Appendix A
is the correct general foundation, not the linear ODE. Remaining work:
- Consider developing a stochastic companion to TF-11: AR(1) steady-state
  as the primary discrete-time result, with continuous ODE as an
  approximation valid when η << 1
- Model observation quality as a factor in adversarial dynamics (T depends
  on η* depends on U_o — propagate this through the mismatch dynamics)
- Promote per-dimension persistence condition from "open question" to
  "known correct formulation" for anisotropic systems

### 1.3 Clarify the Object Model
The current documents have a **type inconsistency**: δ_goal = G_t − M_t
(point subtraction) coexists with G_t-as-DAG. These are mathematically
incompatible. Earlier point-valued formulations are superseded.

The working split:
- **O_t** (objective): the target state — what the agent wants. Simple.
  A point or region in S. The port.
- **Σ_t** (strategy): the causal DAG from actions to the objective — how
  the agent plans to get there. A function of O_t and M_t. Complex.

Everyday "goal" conflates these. The PID has O_t but no Σ_t. The Kalman
filter has neither. The commander has both.

Three additional gaps (from review):
- **Commitment state**: OR branches are options until committed; the
  formalism doesn't distinguish "considering" from "executing." The
  D_t (desire) / I_t (committed intent) split may help here — desire
  is the holistic model of what the agent wants; committed intent is
  the subset focusing action. Defer pruning until multi-agent work
  reveals which distinction bears more weight.
- **Resource budget**: costs are invoked in the scratch docs but not
  modeled. Strategy evaluation requires knowing what paths cost.
- **Temporal ordering**: the DAG encodes causal dependency but not "do A
  before B." Can the intent DAG handle action sequencing, or does it
  need a separate mechanism?

Also: **TFT's "completeness for survival" holds only for reactive
tracking.** Once survival requires multi-step strategy (evade, navigate,
acquire), the persistence condition implicitly needs Σ_t. TFT is a
necessary foundation, not a self-sufficient theory of agency even for
the survival case. This should be stated explicitly.

Mark all scratch docs still using point-valued G_t as superseded.

---

## Phase 2: Multi-Agent Intent (highest-value next work)

### 2.1 Intent Decomposition
How does a high-level intent DAG decompose across agents? Formalize:
- Graph partitioning by inter-agent edge uncertainty
- Optimal cut minimizes uncertainty on spanning edges
- Connection to organizational design (who owns which sub-DAG?)

### 2.2 Directed Opportunism
Local grafting at OR-nodes within IB-compressed shared intent:
- How much can a subordinate's local O_t/Σ_t diverge?
- The Auftragstaktik IB: compress to constraints that keep inter-agent
  edges viable while freeing intra-agent edges
- When is local divergence beneficial vs. destructive?

### 2.3 Adversarial Dynamics on DAGs
Targeting edges in the opponent's intent DAG:
- High-centrality edges as priority targets
- Inter-agent coordination edges as fragmentation points
- Effects spiral as DAG pruning faster than grafting
- Structural interpretation of tempo advantage

### 2.4 Team Persistence via DAG Redundancy
Why teams persist where individuals can't:
- Aggregate DAG has more paths (higher R_w)
- More observation channels (higher observability coverage)
- Re-routing around failed edges via sub-DAG reassignment
- Collective grafting capacity

**Caveat from Appendix F review**: The current multi-agent formulation
treats communication as additive tempo and cooperation as negative
disturbance. These are useful heuristics, but correlated reports don't
linearly increase effective tempo, and communication typically improves
estimation quality (reduces U_o) rather than literally canceling
exogenous disturbance (reducing ρ). Appendix F acknowledges independence
limits and raises correlation in trust transitivity, but these caveats
don't propagate into the persistence formulas. The Phase 2 formalization
should treat correlated observations as the realistic default and derive
the independence case as a special case, not the other way around.

---

## Phase 3: Formalization

Write up ACT as a single theory. The structure should emerge from the
content, not be prescribed in advance. What we know: it needs to cover
adaptive systems (the foundation, originally TFT), purposeful agency
(objectives + strategy), the Orient cascade, and multi-agent dynamics.
How it's organized should be determined by the dependency structure of
the actual claims, not by preserving TFT's numbering scheme or treating
"TFT + extension" as the permanent structure. ACT supersedes TFT.

TST should be revisited as a domain instantiation of ACT once the
formalism stabilizes.

**Logozoetic domain instantiation**: The agentic-tft corpus
(../agentic-tft/, docs 00-14) contains substantial prior architectural
thinking for language-based AI agents that should inform this phase:
- Cognitive loop spec (doc 11): four-phase loop with six input channels,
  attention triage, temporal structure (CADENTIA)
- Evaluation framework (doc 12): development-vs-drift diagnostics,
  mismatch trajectory as core metric
- Crèche concept (doc 06): experiential training as developmental
  prerequisite; constitutive utterance insight
- Narrative circle (doc 04): for logozoetic agents, TFT provides
  architecture but implementation operates in natural language
- Bootstrap problem (doc 14): grounding linguistic epistemic estimates
  measurably without circularity — the practical barrier to
  implementation
These are not referenced from ACT's formal documents yet but directly
relevant to any AI agent domain instantiation.

---

## Phase 4: Validation

Possible simulation and empirical work — scope TBD based on what the
theory actually claims:
- Extend the nonlinear dynamics sims to characterize the squared-advantage
  regime boundary
- Developer-as-ACT-agent on a real codebase (the "software worked example")
- Test DAG health metrics against real project outcome data
- Multi-agent intent propagation simulation

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
