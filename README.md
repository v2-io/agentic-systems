# ACT: Agentic Cycle Theory

A mathematical framework for adaptive, purposeful agents under uncertainty — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

## What ACT Is

ACT is a unifying framework, not a new branch of mathematics. The individual mathematical tools it uses — Lyapunov stability, Kalman filtering, the information bottleneck, causal DAGs — are well-established. ACT's contribution is connecting them into a single coherent account of adaptive agency, producing specific testable predictions and a few genuinely novel formalizations along the way.

The framework unifies three aspects of agency that existing theories treat separately:

1. **Adaptive feedback dynamics** — how agents build and maintain models of reality under environmental change. Originally developed as Temporal Feedback Theory (TFT, now subsumed): mismatch signals, update gain via the uncertainty ratio, adaptive tempo, persistence conditions, adversarial dynamics. The mathematical backbone is standard (Lyapunov/sector-condition analysis); the application to general agents — not just control systems — and the specific results (uncertainty ratio, persistence threshold, adversarial scaling laws) are ACT's contribution.

2. **Actuated (purposeful or goal-driven) agency** — how agents hold, pursue, and revise goals. Objectives ($O_t$) and strategy ($\Sigma_t$) are distinct formal objects. Strategy is formalized as a probabilistic causal DAG encoding the agent's theory of how its actions produce goal-achievement. The derivation chain from adaptive foundations to purposeful architecture — showing *why* causal structure is needed, not just assuming it — is where ACT does genuinely new work.

3. **Composition and shared intent** *(research program, less mature than 1-2)* — how agents compose into larger agents and communicate purpose under uncertainty. Intent compression via the information bottleneck. Composition consistency as a structural requirement on the theory; the operational bridge (admissibility constraints, closure-to-trajectory error bounds) is still open.

Beneath all three is a single recurring pattern: **an agent persists when its internal correction outpaces external challenge.** For an individual, this means adaptive tempo must exceed the rate of environmental disturbance — the persistence condition (Section I, simulation-validated). For a composite (a team, an organization, a swarm), this means internal coordination must equilibrate faster than the external dynamics change — the composition threshold (Section III, stated as a sufficient condition, not yet formally derived).

The theory progresses from general adaptive systems through actuated agency and multi-agent composition to domain instantiations — particularly software development and AI agents operating on code.


## Where to Start

**[`CURRENT-FULL-THEORY.md`](CURRENT-FULL-THEORY.md)** — the canonical outline. The full argument claim by claim, with the current linearization, types, and development stage for each segment.

**[`WORKBENCH.md`](WORKBENCH.md)** — development state: what's written, what's open, known fragilities, spike status, prior-work migration map.

**[`FORMAT.md`](FORMAT.md)** — segment file conventions: frontmatter, document cadence, math formatting, cross-references, epistemic labeling.

**[`notation.md`](notation.md)** — all symbols used in ACT, serving as single authoritative reference.


## Structure

**The theory lives in [`src/`](src/).** Each file is one claim — an axiom, definition, theorem, or hypothesis — named by slug (`src/{slug}.md`). Claims build incrementally, like a proof. One move per file: given what came before, this one thing follows, or is defined, or restricts scope.

Five sections scope progressively:

1. **Adaptive Systems Under Uncertainty** — the general case (from TFT)
2. **Actuated Adaptive Systems** — adding objectives and strategy
3. **Composition and Coordination** — multiple agents, composite agents
4. **Evolving Software Systems** — TST regrounded in ACT's formal machinery
5. **Software-Grounded Agentic Systems** — AI agents, the recursive completion

Canonical ordering lives in `CURRENT-FULL-THEORY.md`, not in filenames. Slugs are the stable identities; the linearization will change as the theory develops.


## What ACT Contributes — Honest Calibration

ACT's value is primarily **integration**: connecting established mathematical tools into a unified account of adaptive agency. The individual pieces (Lyapunov stability, Kalman filtering, IB, causal DAGs) are known. The specific contributions fall into five categories:

1. **Synthesis that produces new structure.** The uncertainty ratio $\eta^* = U_M/(U_M + U_o)$ unifies Kalman gain, Bayesian learning rates, and RL step sizes under one principle. The persistence condition $\mathcal{T} > \rho/\|\delta_{\text{critical}}\|$ connects Lyapunov stability to agent viability. These are known mathematics applied to a new domain — their value is the unified framework, not the individual results.

2. **Genuinely novel formalizations.** The derivation that graph structure (DAGs) is *forced* by temporal ordering + probabilistic uncertainty + local revisability (not just a convenient choice). DAG acyclicity derived from finite planning horizons. The satisfaction gap / control regret split (separating "infeasible goal" from "bad strategy"). The feedback loop as a Level 2 causal engine (Bareinboim et al.'s causal hierarchy applied to agent architecture). These produce results we have not seen stated elsewhere.

3. **Quantitative predictions.** Adversarial tempo advantage exponents (2 deterministic, 3/2 stochastic, ~1 non-coupling-dominant — simulation-validated). Observation noise collapsing tempo advantage ($U_o$ drops exponent from ~1.0 to ~0.2). Structural adaptation breakdown at predicted threshold. These are testable and, where tested, confirmed.

4. **Open bridges.** The git-metrics → Lyapunov-parameters operationalization (coherence → $\alpha$, coupling → $\gamma$) is analogical, not formally proved. The composition laws are sketches. The strategy persistence schema lacks a correction function. These are flagged honestly as open problems.

5. **Formal analogs of known insights.** The model independently produces patterns that turn out to parallel Boyd's OODA dynamics, Brooks's Law, Auftragstaktik, and dual-process theory. These are suggestive — the model captures the same structural tradeoffs — but they are analogs, not derivations. Whether the model's mechanisms are the actual mechanisms behind these phenomena is an empirical question in every case.

### Key Results by Section

**Section I — Adaptive Systems** (28 segments, nearing completion). Lyapunov/sector-condition analysis — general, nonlinear, robust. The linear ODE is pedagogical, correct in its regime, not the general case. Uncertainty ratio validated empirically (52% mismatch reduction with Riccati-optimal gain). Persistence condition robust across all correction functions tested.

**Section II — Actuated Adaptive Systems** (20 segments, complete). Strategy as probabilistic causal DAG with AND/OR nodes. Orient cascade derived from information dependency. Directed separation (conditional on scope restriction). Derivation chain in `scratch/spike-v3-purposeful-agent.md`.

**Section IV — Evolving Software** (20/24 segments, in conversion from TST). Median prediction (not expectation — Pareto($\alpha=1$) mean diverges). Dual optimization with turnover multiplier. TST's claims integrated with ACT's formal machinery — not relabeled, but rederived where possible and honestly tagged where not.


## Current Status

~99 claims mapped across five sections. 89 segments at draft, 10 remaining. Sections I (28), II (20), and III (13) are complete. Section IV (20/24) is in active conversion from TST. Section V (3/6) and appendices (5/8) have source material identified.

See [`WORKBENCH.md`](WORKBENCH.md) for detailed development state, open questions, known fragilities, and prior-work migration progress.


## Repository Layout

```
act/
├── CURRENT-FULL-THEORY.md   Canonical outline — start here
├── FORMAT.md                 Segment file conventions
├── WORKBENCH.md              Development state and working notes
├── notation.md               Symbol reference
├── CLAUDE.md                 Context for AI agents
│
├── src/                      The theory — claim segments by slug
│   ├── {slug}.md             ACT segments
│   ├── old-tf-*.md           TFT source material (being absorbed)
│   └── old-tst-*.md          TST source material (being converted)
│
├── scratch/                  Working documents and spikes
│   ├── spike-v3-purposeful-agent.md    Definitive Section II derivation
│   ├── spike-agent-composition.md      Composition/holon theory
│   ├── spike-graph-uniqueness.md       DAG structure uniqueness argument
│   ├── 04-intent-dag-consolidated.md   Canonical intent DAG reference
│   ├── track-a-intent-dag/             DAG formalism variants (historical)
│   └── track-b-nonlinear-sims/         Simulation code and results
│
├── _archive/                 Superseded documents
├── refs/                     Reference papers (Hafez 2026, IBM 2025)
└── priors/                   Git submodules (historical only —
    ├── tft/                    all content copied to src/old-tf-*)
    └── tst/                    all content copied to src/old-tst-*)
```


## Operationalization — Where the Bridge Exists and Where It Doesn't

ACT's variables ($\delta$, $\eta^*$, $\mathcal{T}$, $\rho$, $\Sigma_t$, etc.) are defined abstractly. Applying the theory to any specific domain requires mapping these abstractions to measurable quantities. The operationalization gap varies significantly across the theory's sections — and honesty about where that gap is wide is essential.

**Section IV (Evolving Software) — most concrete.** Changesets, git history, code metrics, and test outcomes provide observable proxies for most variables. Mismatch has a natural proxy in failing tests and divergence between developer expectations and system behavior. Changeset size, proximity, and boundary-crossing costs are directly measurable from version control data. The dual-optimization prediction (comprehension cost dominates under high turnover) is testable with existing engineering metrics. The remaining gap: translating git-derived metrics (coherence, coupling) into Lyapunov parameters ($\alpha$, $R$) — this bridge is analogical, not formally proved. See known fragilities in [`WORKBENCH.md`](WORKBENCH.md).

**Section I (Adaptive Systems) — domain-dependent.** The persistence condition, uncertainty ratio, and adversarial scaling laws are simulation-validated in the abstract. For engineered control systems, operationalization is straightforward (the math was originally developed for them). For biological, organizational, or cognitive agents, the theory identifies the *structural constraints* a system must satisfy — but measuring $\delta$, $\eta^*$, and $\rho$ in situ requires domain-specific instrumentation that ACT does not prescribe.

**Section V (AI Agents) — the open research program.** For LLM-based agents, candidate observables exist: context window state, tool-use traces, API logs, success/failure rates, strategy revision frequency. But no one has yet written the code that computes "adaptive tempo" from an agent's runtime telemetry, or that detects when an agent has crossed its persistence threshold and needs structural adaptation (context reset, model switch, strategy overhaul). This is the highest-value operationalization target — and the most open.

**The theory's value before full operationalization.** Even where variables aren't directly measurable, the theory provides *design constraints*: what structure an agent needs (Orient Cascade ordering, satisfaction gap / control regret diagnostics, persistence monitoring), why it needs that structure (derived from the formalism, not asserted as best practice), and what failure modes to expect when the structure is absent. These constraints are actionable for agent architects today, independent of whether every variable can be tracked in real-time.


## Prior Art and Positioning

ACT builds on and connects to substantial prior work. Honest positioning requires acknowledging what's borrowed, what's bridged, and what's new.

- **Control theory** (Lyapunov, Kalman, sector conditions): ACT's Section I machinery. The mathematics is standard; the application to general adaptive agents (not just engineered control systems) and the specific results (persistence threshold, adversarial scaling laws) are ACT's extension.
- **BDI** (Rao & Georgeff): Named the agent architecture components (beliefs, desires, intentions). ACT provides dynamics — how these components evolve, interact, and degrade — which BDI does not address.
- **Active Inference** (Friston): Unifies perception and action under free energy minimization. ACT uses causal feedback dynamics with different foundations (Lyapunov stability rather than variational free energy). Expected free energy $\approx$ ACT's value + $\lambda$ CIY — a structural isomorphism suggesting shared deep structure, not a claim that one subsumes the other.
- **Causal inference** (Pearl, Bareinboim): ACT uses the causal hierarchy theorem to derive the need for causal structure in adaptive agents. The theorem is Bareinboim et al.'s; the application to agent architecture is ACT's.
- **Hafez et al. 2026**: Bi-predictability metric ($P$). Complementary — $P$ diagnoses architecture, mismatch diagnoses performance.
- **IBM "Agentic AI Needs a Systems Theory" 2025**: Articulates the need for a unified agent theory. ACT addresses several of their open challenges (subgoal emergence via DAG decomposition, residual control rights via the composition framework), though the composition results are still sketches.
- **TST**: Software domain theory. Gets full treatment in Section IV, regrounded in ACT's formal machinery. TST's claims are honestly scoped and carefully stated; ACT adds the causal mathematics and adaptive dynamics, not rigor — TST already had that.
