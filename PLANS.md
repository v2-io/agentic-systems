# ACT Development Roadmap

## Current State (March 2026)

**Part I (Adaptive Systems / TFT)**: Well-developed. TF-00 through TF-11 plus
appendices A-G. Simulation battery (6 variants + Hafez bridge) has
characterized the empirical landscape:

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
Potentially important for multi-agent adversarial work.

**Part II (Purposeful Agency)**: Exploratory sketch phase. Three convergence-
tested intent DAG formalism variants. Core structure identified (AND/OR nodes,
single-parameter edges, Orient cascade). The O_t (objective) / Σ_t (strategy)
distinction clarifies what was previously conflated under G_t. Not yet
consolidated into formal documents.

**Domain Instantiations**: TST-via-TFT mapping exists (priors/tst/via-tft/).
Needs updating once ACT's formalism stabilizes.

---

## Phase 1: Consolidation (immediate)

### 1.1 Consolidate Intent DAG Formalism
Merge the three variants (00-intent-dag-formalism, 02-alt-clean-slate,
03-alt-and-or-dag) into a single canonical treatment:
- AND/OR nodes with single-parameter edges (converged)
- Bayesian edge update mirroring TF-06 (converged)
- Orient cascade (converged)
- Node taxonomy: resolve categorical vs continuous (open — pick one and
  note the alternative)
- Strategic tempo T_G from the clean-slate variant
- Health metrics (keep the principled ones, flag scaffold ones)

### 1.2 TFT Formal Rebalancing
Simulation findings (now added to TF-06, TF-11) revealed that Appendix A
is the correct general foundation, not the linear ODE. Remaining work:
- Consider developing a stochastic companion to TF-11: AR(1) steady-state
  as the primary discrete-time result, with continuous ODE as an
  approximation valid when η << 1
- Model observation quality as a factor in adversarial dynamics (T depends
  on η* depends on U_o — propagate this through the mismatch dynamics)
- Promote per-dimension persistence condition from "open question" to
  "known correct formulation" for anisotropic systems

### 1.3 Clarify the Objective / Strategy Distinction
The current documents conflate two things:
- **O_t** (objective): the target state — what the agent wants. Simple.
  A point or region in S. The port.
- **Σ_t** (strategy): the causal DAG from actions to the objective — how
  the agent plans to get there. A function of O_t and M_t. Complex.

Everyday "goal" conflates these. The PID has O_t but no Σ_t. The Kalman
filter has neither. The commander has both. Determine how much of the
existing formalism is about O_t (and should be simple) vs about Σ_t
(and should be the DAG).

---

## Phase 2: Multi-Agent Intent (highest-value next work)

### 2.1 Intent Decomposition
How does a high-level intent DAG decompose across agents? Formalize:
- Graph partitioning by inter-agent edge uncertainty
- Optimal cut minimizes uncertainty on spanning edges
- Connection to organizational design (who owns which sub-DAG?)

### 2.2 Directed Opportunism
Local grafting at OR-nodes within IB-compressed shared intent:
- How much can a subordinate's local G_t diverge?
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

---

## Phase 3: Formalization

Write up the theory properly. The structure should emerge from the content,
not be prescribed in advance. What we know: it needs to cover adaptive
systems (TFT's contribution), purposeful agency (objectives + strategy),
the Orient cascade, and multi-agent dynamics. How it's organized should be
determined by the dependency structure of the actual claims, not by analogy
to TFT's numbering scheme.

TST should be revisited as a domain instantiation of ACT once the
formalism stabilizes.

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

### Credibility leaks (medium, partially fixed)
- ~~Founding notes reference ~/src/ paths~~ — FIXED
- sim2 prints "R -> infinity: exponent -> 2.0" but stochastic asymptote
  is 1.5 — needs code fix
- Simulation spec claims |δ| distribution is "approximately exponential"
  but stationary law is half-normal — needs spec fix

### TST epistemic downgrade (medium, for when TST-via-ACT is written)
TST claims "mathematical necessity" for things depending on undefined
proxies (principled(C), n_future, change-set size as time surrogate).
When TST becomes a domain instantiation of ACT, every claim should be
regraded with TFT-style epistemic tags.

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
   High H_b = strategically opaque. This has no current TFT/ACT analog
   and could be load-bearing for adversarial multi-agent dynamics.
