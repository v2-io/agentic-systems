# ACT Development Roadmap

## Current State (March 2026)

**Part I (Adaptive Systems / TFT)**: Well-developed. TF-00 through TF-11 plus
appendices A-G. The foundation is solid, with one important empirical caveat
from simulations (Cor. 11.2 regime validity).

**Part II (Purposeful Agency)**: Exploratory sketch phase. Three convergence-
tested intent DAG formalism variants. Core structure identified (AND/OR nodes,
single-parameter edges, Orient cascade). Not yet consolidated into formal
documents.

**Domain Instantiations**: TST-via-TFT mapping exists (priors/tst/via-tft/).
Needs updating once ACT Part II is consolidated.

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

### 1.2 Feed Simulation Results Back to TFT
The squared tempo advantage (Cor. 11.2) needs a regime-validity caveat.
Options:
- Add a note to TF-11 specifying the coupling-dominant, continuous-time regime
- Add a note to Appendix A referencing the simulation findings
- Consider whether the discrete-time AR(1) formula should be the primary
  result, with the continuous ODE as the approximation (inverting the current
  presentation)

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

### Simulation model mismatch (high priority)
TF-11's ODE uses deterministic disturbance ρ. The simulations use stochastic
zero-mean Gaussian increments (AR(1)/OU process). These are related but not
identical models, and the narrative incorrectly frames the sims as directly
testing TF-11's ODE. Options:
- Rewrite sims with a deterministic drift term to match TF-11's ρ
- OR be explicit that the sims test the stochastic analog, with formal
  justification of the ρ ↔ q mapping
- Either way, the exponent finding (~1.05) may change and needs retesting

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

### Credibility leaks (medium, fixable)
- sim2 prints "R -> infinity: exponent -> 2.0" but data shows ~1.06
- Simulation spec claims |δ| distribution is "approximately exponential"
  but stationary law is half-normal
- Founding notes reference ~/src/ paths instead of priors/ submodules

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

## Open Questions (not yet assigned to phases)

1. Does the information bottleneck principle for shared intent produce
   non-obvious predictions about organizational communication structure?

2. Can the intent DAG formalism be extended to handle temporal dependencies
   (action ordering) as well as causal dependencies?

3. How does the 100% context turnover problem interact with the intent DAG?
   G_t may survive context death (via CLAUDE.md) even when M_t doesn't.
   What does this mean for the cold-start protocol?

4. Is there a "goal-reality-model triangle" analog of the bias-variance
   tradeoff? Too much focus on M_t accuracy delays goal-pursuit; too much
   focus on goal-pursuit with a bad M_t wastes action on wrong paths.

5. Can Hafez's bi-predictability P be derived from or mapped to ACT
   quantities? If P = f(T, eta*, ...), that would be a strong connection.

6. What is the relationship between ACT and active inference's prior
   preferences? Is there a formal equivalence or are they genuinely different?
