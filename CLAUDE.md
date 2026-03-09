# CLAUDE.md — Context for AI Agents Working on ACT

## What This Project Is

ACT (Agentic Cycle Theory) is a first-principles mathematical theory of
adaptive, purposeful agents. It extends Temporal Feedback Theory (TFT, in
priors/tft/) with a formal treatment of goals and intent.

This is theoretical research, not software engineering. The primary artifacts
are mathematical formalisms, scratch documents developing ideas, and
simulations testing theoretical claims. Quality means rigor, honesty about
epistemic status, and clarity for future readers — not code coverage.

## The Core Insight

TFT formalizes how agents adapt to reality (mismatch signals, gain, tempo,
persistence). But it has no treatment of goals — the agent's desired future
state. ACT adds:

- **G_t** (intent) alongside **M_t** (reality model)
- Intent formalized as a **probabilistic causal DAG** (AND/OR nodes, edges
  with confidence weights p, Bayesian update via TFT's uncertainty ratio)
- The **Orient cascade**: observation -> M_t update -> G_t revision ->
  feasibility check -> goal revision
- **Shared intent** as IB-compressed purpose for multi-agent coordination

## Key Architectural Decisions

1. **TFT is Part I of ACT.** It stands alone as a complete theory of adaptive
   systems. Don't modify TFT documents; build on them.

2. **The directed separation principle.** M_t dynamics can be designed
   independently of G_t. G_t depends on M_t. Action selection couples them.
   This means TFT (Part I) is valid without Part II, but Part II requires
   Part I.

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
  back to TFT

## Important Simulation Finding

The nonlinear dynamics simulations (scratch/track-b-nonlinear-sims/) found
that **TF-11 Corollary 11.2's squared tempo advantage (exponent = 2) does
not hold at realistic parameters.** The actual exponent is ~1.0-1.3. This is
a regime-validity issue, not a refutation — the qualitative superlinearity
is robust. But the specific claim needs a caveat in TFT. This has NOT yet
been fed back to the TFT documents.

## File Organization

- `priors/` — TFT and TST as git submodules (read, don't modify)
- `refs/` — Reference papers
- `scratch/` — Working documents (numbered for chronological order)
- `scratch/track-a-intent-dag/` — Intent DAG formalism variants
- `scratch/track-b-nonlinear-sims/` — Simulation code and results
- Future: formal document sequence (ACT-00, ACT-01, ...) will live at top level

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
