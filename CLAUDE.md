# CLAUDE.md — Context for AI Agents Working on ACT

## What This Project Is

ACT (Agentic Cycle Theory) is a first-principles mathematical theory of
adaptive, purposeful agents. It supersedes and subsumes Temporal Feedback
Theory (TFT, in priors/tft/), which provides the adaptive-systems
foundation. TFT is prior work now absorbed into ACT, not a separate
co-existing theory.

This is theoretical research, not software engineering. The primary artifacts
are mathematical formalisms, scratch documents developing ideas, and
simulations testing theoretical claims. Quality means rigor, honesty about
epistemic status, and clarity for future readers — not code coverage.

## The Core Insight

The adaptive-systems foundation (from TFT) formalizes how agents adapt to
reality (mismatch signals, gain, tempo, persistence). But it has no
treatment of goals — the agent's desired future state. Even survival
requires multi-step strategy in non-trivial environments, so "TFT is
complete for survival" holds only for purely reactive tracking. ACT adds:

- **O_t** (objective — what the agent wants) and **Σ_t** (strategy — how
  it plans to get there) alongside **M_t** (reality model)
- Strategy formalized as a **probabilistic causal DAG** (AND/OR nodes,
  edges with confidence weights p, Bayesian update via the uncertainty
  ratio). The objective is simpler — a target state or region in S.
- The **Orient cascade**: observation -> M_t update -> Σ_t edge revision ->
  feasibility check -> possible O_t revision
- **Shared intent** as IB-compressed purpose for multi-agent coordination
- The O_t / Σ_t distinction is recent (not yet reflected in all scratch
  docs, which use "G_t" for both — those are superseded)

## Key Architectural Decisions

1. **ACT supersedes TFT.** TFT's adaptive-systems content is absorbed
   into ACT as the foundation layer. The TFT submodule is prior work /
   reference material — don't modify those documents, but don't treat
   "TFT" as a separate co-existing theory either. ACT is the theory.

2. **The directed separation principle.** M_t dynamics can be designed
   independently of O_t/Σ_t. O_t/Σ_t depend on M_t. Action selection
   couples them. This means the adaptive-systems layer is valid on its
   own, but the purposeful-agency layer requires it.

3. **AND/OR DAG with single-parameter edges.** Three independent formalism
   attempts converged on: AND/OR combination rules at nodes, single
   confidence weight p per edge (not the earlier two-parameter p,theta).
   The noisy-OR assumption from the first attempt is systematically
   over-optimistic for conjunctive structures.

4. **Structural change IS extreme parametric update.** In the probabilistic
   DAG, pruning (edge -> 0) and grafting (0 -> edge) are continuous
   operations on edge weights, not discrete structural events. TF-10's
   destruction-creation cycle is the rare limiting case.

## Epistemic Conventions

Follow TFT's conventions (see priors/tft/TF-00.md):
- **[Confident]**: Solid, multiple indicators converge
- **[Plausible]**: Structurally motivated, needs validation
- **[Speculative]**: Worth exploring, might not hold
- Mark what's **first-principled** (derived from foundations) vs
  **scaffold-engineering** (reasonable modeling choice, could be different)

## What's Settled vs. Open

### Settled (from convergence testing)
- Single-parameter edges with AND/OR nodes (not noisy-OR with p,theta)
- Orient cascade structure
- Compound probability decay (depth fragility)
- Observability as strategy enablement
- Directed separation

### Open
- Node taxonomy: categorical types (O/K/A/X) vs continuous properties —
  genuine design freedom, both valid
- Multi-agent intent propagation — the highest-value next work
- Goal tempo formalization
- Shared intent compression (IB for Auftragstaktik)
- How the simulation findings (squared advantage regime caveat) should feed
  back to the adaptive-systems documents

### Known Fragilities in Purposeful Agency Layer
- **Object model type error**: earlier docs define δ_goal = G_t − M_t
  (point subtraction) but the converged formalism makes Σ_t a DAG. These
  are type-incompatible. Docs using point-valued G_t are superseded.
- **Edge semantics gap**: edges claim interventional semantics
  (p_ij = P(j | do(i), M_t)) but update from observational signals
  without identifiability assumptions. Real issue in confounded domains;
  less severe in software (genuine interventions available).
- **Missing commitment/resource/temporal structure**: the formalism lacks
  commitment state (options vs. executing), resource budget, and action
  sequencing. Gap between "strategy representation" and "intention theory."
- **DAG acyclicity**: an assumption, not forced by Pearl. Real control
  loops are cyclic; acyclicity holds after time-unrolling.
- **Cognitive cost of Σ_t**: TF-03 has β for M_t compression cost; the
  intent DAG has no analog. Matters especially for finite-context agents.
- **WEIGHTED combination rule**: reintroduces two-parameter estimation
  problem. Should be dropped; use nested AND/OR for k-of-n semantics.

## Important Simulation Finding

The nonlinear dynamics simulations (scratch/track-b-nonlinear-sims/) found:

- **Cor. 11.2's exponent = 2 IS correct** under deterministic drift when
  coupling dominates base disturbance (confirmed: exponent = 1.999).
- **Under stochastic disturbances, the asymptotic exponent is 1.5** (not
  2.0) because E[|δ|] scales as 1/√T rather than 1/T.
- **When coupling doesn't dominate base noise, the exponent drops to ~1.0**
  regardless of disturbance model.
- The original sim2's ~1.05 was two effects: stochastic model + not
  coupling-dominant.

The adaptive-systems documents should note which disturbance model yields
which exponent. Qualitative superlinearity is robust across all regimes.
This has NOT yet been fed back to the TFT-era documents.

## File Organization

- `priors/` — TFT and TST as git submodules (prior work, read-only)
- `refs/` — Reference papers
- `scratch/` — Working documents (numbered for chronological order)
- `scratch/track-a-intent-dag/` — Intent DAG formalism variants
- `scratch/track-b-nonlinear-sims/` — Simulation code and results
- `../agentic-tft/` — Prior bridge work: TFT → logozoetic AI agents.
  Docs 10-14 (cognitive loop, evaluation, crèche, training design) are
  directly relevant to ACT's AI agent domain instantiation.
- Formal documents will live at top level once the theory stabilizes;
  structure should emerge from content, not be prescribed

## How to Contribute

1. Read `scratch/00-founding-notes.md` for full context
2. Read `scratch/02-prior-art-assessment.md` for positioning
3. For intent DAG work: read all three variants in `track-a-intent-dag/`
   and the convergence synthesis — the AND/OR + single-p structure is the
   current best candidate
4. For simulation work: the code runs (`python3 sim1_nonlinear_mismatch.py`,
   `python3 sim2_adversarial_coupling.py`); extend rather than rewrite
5. Mark epistemic status on all claims
6. Be honest about what you're uncertain about
