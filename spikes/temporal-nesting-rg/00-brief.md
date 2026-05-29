# Spike Track: Temporal Nesting and the Renormalization-Group Reframe

**Status**: open — initial brief
**Date opened**: 2026-05-09
**Conversation provenance**: Joseph asked whether ASF explores nested adaptive cycles operating at different levels of abstraction simultaneously (inner fast loop advances slower outer loop). Survey found three load-bearing segments (`#der-temporal-nesting`, `#form-composition-closure`, `#der-tempo-composition`) plus the unifying machinery (`#result-sector-persistence-template`, `#sketch-multi-timescale-stability`). Discussion then surfaced a candidate elegance: AAT as a renormalization-group structure with itself as fixed point — making temporal nesting and composite formation two projections of one operation. This brief sets up that test.

**Depends on / cites**: `#der-temporal-nesting`, `#form-composition-closure`, `#der-tempo-composition`, `#result-sector-persistence-template`, `#sketch-multi-timescale-stability`, `#def-strategy-dag`, `#def-adaptive-tempo`, `#disc-composition-consistency`, `#hyp-directed-separation-under-composition`, `spikes/spike-composition-correlated-kalman.md`, `spikes/spike-bridge-lemma-contraction.md`, `spikes/spike-projection-admissibility.md`.

---

## 1. The original question (literal form)

> *"Does ASF explore how the adaptive cycle can be happening at different levels of abstraction simultaneously — i.e., an innermost loop that is advancing a slower loop?"*

Initial corpus survey (Explore agent, 2026-05-09) found:

- **Implicit treatment exists.** `#der-temporal-nesting` (`robust-qualitative`) gives the 5-level table (Reactive → Parametric → Consolidation → Structural → Architectural) and the convergence constraint $\nu_{n+1} \ll \nu_n$, citing Tikhonov 1952.
- **The formal mechanism is `K_c`.** `#form-composition-closure` carries a timescale ratio $K_c$ (micro-steps per macro-step). The `$K_c \gg 1$` regime is exactly nested-loop structure: the composite "lives at a strictly slower timescale than its sub-agents."
- **Cost-side machinery exists.** `#der-tempo-composition` (`sketch`) gives Brooks's Law in tempo units: $C_\text{coord} \geq \varepsilon^* \nu_c / \|\delta_\text{critical}\|$.
- **The strategy DAG implicitly nests.** Evidence-starvation (`#def-strategy-dag`, `#deriv-edge-credence-dynamics` Props B.2–B.3) gives deeper edges effective rate $\nu_k^\text{eff} = \nu_\text{base} \prod_{j<k}\theta_j$ — a natural per-level rate hierarchy that has never been formally connected to `#der-temporal-nesting`'s table.

**What's missing.** Three things are *asserted, not derived*:

1. **The bridge from $K_c \gg 1$ to $\varepsilon^* \to 0$.** Audit-flagged 2026-04-21 as "stranded at zero-timescale-separation." The 2026-04-22 fix introduced $K_c$ as a parameter but left the implication at the level of intuition.
2. **N-level stability composition.** `#sketch-multi-timescale-stability` cites Tikhonov but does not derive the N-level result from AAT's own template.
3. **DAG depth as temporal nesting.** Not formalized.

## 2. The candidate elegance: AAT as RG fixed point

Read (A1)–(A4) of `#form-composition-closure` literally. They demand $X_c = (M_c, G_c)$ with recursive update, well-defined macro-mismatch, well-defined macro-tempo, sector-bounded macro-correction. **Collectively: the macro-system must itself be an AAT agent.** That's the form-preservation requirement of a renormalization-group transformation.

Mapping:

| RG concept | AAT instance |
|---|---|
| Coarse-graining transformation | $\Lambda$ (projection map) |
| Form-preservation requirement | (A1)–(A4) admissibility |
| Distance from fixed point | $\varepsilon^*$ (closure defect) |
| Trajectory error bound near fixed point | Bridge-lemma $\lim\|e_m\| \leq \varepsilon^* \nu_c / \alpha_c$ |
| Scale-invariant quantity | Persistence condition $\alpha R > \rho$ (template form) |
| Recursive structure on itself | (O, Σ) decomposition: each Σ-node is a sub-objective with sub-strategy, recursing to action leaves |
| RG flow direction | $\varepsilon^*(K_c)$ as $K_c$ varies |
| Order parameter | Directed-separation classes (modular / partial / merged) |
| Discrete-RG fixed point | Hafez meta-machine ($\varepsilon^* = 0$ exactly) |

**What this collapses into one structure:**

- Temporal nesting (along time axis) and composite formation (across agents) become *the same operation viewed from different axes*. The 5-level table is RG depth; N-agent composition is RG width.
- The persistence template's "applies at every level" claim becomes scale-invariance of the AAT form.
- The closure-defect bridge lemma becomes "trajectories track macro-reality near the fixed point."
- (O, Σ) becomes genuinely fractal: each strategy node carries a sub-objective, and the sub-DAG is a strategy for that sub-objective, all the way down to action leaves.
- Directed separation's three classes become RG fixed-point types (stable / marginal / unstable under coarse-graining).
- Brooks's Law becomes flow-away-from-fixed-point along an unstable direction in parameter space.

## 3. Caveats — why this is currently *Pattern*, not *Tested*

Honest epistemic state: this is at "Pattern" on the AAT epistemic ladder. RG analogies are seductive — every dynamical-systems framework gets compared to RG eventually, and many of those comparisons turn out to be shallow.

Specific concerns:

- **Stationarity.** Classical RG presumes stationary or critical systems. AAT's purposeful agents are non-stationary by design. The fixed point would need to be *structural* (form preserved) rather than *dynamical* (states equilibrate). This is closer to Wilson-Fisher's structural fixed point than to thermodynamic RG, but I haven't worked out whether the distinction matters here.
- **Prior art unverified.** (P1) is already IB Lagrangian-dual, and IB has known (contested) connections to RG (Tishby et al.; Schwab et al. 2017 *PNAS* "deep learning and renormalization"). FEP has been compared to RG (Friston). Some of this content may already be in the literature. **Need verification before novelty claims.**
- **(O, Σ) recursion not yet checked against `#def-strategy-dimension`.** I think internal Σ-nodes legitimately carry sub-objectives in the formal sense, but FORMAT.md's strict definitions might or might not bear this out. Worth checking before formalizing.
- **The parameter map needs to be a flow.** "RG flow" requires a well-defined transformation $(\alpha, R, \rho, \nu, \varepsilon^*)_\text{micro} \to$ macro version. We have inequalities (weakest-link bounds, persistence conditions) but no explicit derivation that the parameters form a flow.

## 4. The load-bearing test: RG-0

**Claim under test.** $\varepsilon^*$ behaves as RG-flow distance from the AAT fixed point. Specifically:

- (i) For *transient* sources of closure defect (sub-agents not yet in steady state), $\varepsilon^*(K_c)$ should decay with $K_c$ — these are *irrelevant operators* in RG language. **Predicted form**: exponential decay in $K_c$ with rate set by the inner contraction factor $\lambda = 1 - \alpha/\nu$.
- (ii) For *structural* sources of closure defect (e.g., heterogeneous gains $\Delta K = K_1^* - K_2^* \neq 0$), $\varepsilon^*(K_c)$ should be insensitive to $K_c$ — these are *relevant operators*, structural mismatches the flow cannot absorb. **Predicted form**: $\varepsilon^*(K_c) = \text{const}$ in $K_c$, depending only on structural parameters.

If both hold, the RG framing makes a non-trivial empirical prediction about closure-defect classification, which is genuine evidence that the framing is real and not just suggestive.

**Vehicle: the two-Kalman case.** `spikes/spike-composition-correlated-kalman.md` already derives the closed form at $K_c = 1$:

- Homogeneous gains, steady state: $\varepsilon^* = 0$ at all $\rho_\text{corr}$.
- Heterogeneous gains, steady state: $\varepsilon_x^2 = (\Delta K/2)^2 [S_- - C_{+-}^2/S_+]$ — non-zero, depends only on structural parameters.

These two endpoints are *exactly* the predicted RG fixed-point structure: homogeneous = at the fixed point ($\varepsilon^* = 0$); heterogeneous = relevant operator deformation ($\varepsilon^* > 0$). RG-0a extends to $K_c > 1$ to test whether the flow has the predicted structure between these.

## 5. Spike ladder

### RG-0 (this spike track)

**RG-0a — Two-Kalman closure defect under timescale ratio $K_c > 1$.** Derive $\varepsilon^*(K_c)$ in closed form for:
- Case A (homogeneous, transient initial $P_0$): predicted exponential decay.
- Case B (heterogeneous gains $\Delta K \neq 0$, steady state): predicted $K_c$-invariance.

Document at `01-rg-0a-two-kalman-Kc-extension.md`. **This is the load-bearing math.**

**RG-0b — Prior-art search (delegated, parallel).** Has AAT-as-RG, IB-as-RG, or FEP-as-RG already been worked out somewhere we should cite or differentiate from? Also: any prior work treating directed-separation-style modularity as an RG order parameter?

Document at `02-prior-art-rg-ib-fep.md`.

**RG-0c — (O, Σ) recursion check (only if RG-0a positive).** Verify against `#def-strategy-dimension` and `#form-objective-functional` that internal Σ-nodes legitimately carry sub-objectives in the formal sense. If yes, `#def-strategy-dag` becomes recursive AAT by construction.

Document at `03-rg-0c-strategy-recursion.md`.

**RG-0 verdict.** Synthesize at `99-verdict.md`. Decide: framing real (proceed to RG-1..4) or framing collapses to "nested cycles as template instantiation" (drop and write the simpler result).

### RG-1..4 (downstream, gated on RG-0 verdict)

- **RG-1**: State (A1)–(A4) explicitly as RG fixed-point conditions. Promote `#disc-composition-consistency` from postulate-level to derived under the fixed-point framing.
- **RG-2**: (O, Σ) recursion as the formal expression of self-similarity. New segment `#deriv-strategy-recursion` or appendix in `#def-strategy-dag`. Connects to `#der-temporal-nesting` via the depth-rate hierarchy.
- **RG-3**: Directed-separation classes as RG fixed-point types. Strengthens `#hyp-directed-separation-under-composition` by giving it the RG framing.
- **RG-4**: RG flow of the persistence condition. Subsumes original Spike B (N-level stability) by deriving `#sketch-multi-timescale-stability` as RG-flow stability.

## 6. Decision criterion

Promote the framing if:
- (a) RG-0a confirms the irrelevant/relevant operator classification on two-Kalman.
- (b) Prior-art search shows AAT-specific content beyond known IB-as-RG / FEP-as-RG analogies (we may *cite* prior work generously per AAT's prior-art-integration discipline; what matters is whether the agent-architecture specialization adds anything).
- (c) The (O, Σ) recursion holds against the formal definitions.

Drop the framing (and write only the simpler "nested cycles via template instantiation" result) if:
- $\varepsilon^*(K_c)$ does not show the predicted irrelevant/relevant separation.
- The flow framing turns out to be a strict consequence of existing IB-as-RG results with no AAT-specific content.

## 7. Original spike candidates (preserved for reference)

These were the candidates *before* the RG reframe surfaced. They remain valid as a fallback if the RG framing collapses, and several are subsumed by RG-1..4 if it holds.

| ID | Brief | Subsumed by |
|---|---|---|
| Original-A | Worked two-loop instantiation (parametric inner + strategic outer) as paper-quality example | Stays as a worked example regardless of RG verdict; would supplement RG-2 |
| Original-B | N-level stability from the template (Tikhonov-style perturbation argument adapted to AAT vocabulary) | RG-4 |
| Original-C | DAG depth as temporal nesting (formalize evidence-starvation rates as level-k tempo) | RG-2 |
| Original-D₁ | Closed-form $\varepsilon^*(K_c)$ for two-Kalman | This is now RG-0a — repurposed as the load-bearing test |
| Original-F | Failure-mode formalization (predicted oscillation when nesting is violated) | Optional; useful for falsifiability regardless of framing |

## 8. Working agreements for this spike track

- **Math lives in segments, not spikes** (per project convention). This directory is the reasoning trail. Successful results land as appendix segments or new segments under `01-aat-core/src/`.
- **Honest epistemic labels.** Each result tagged with its tier (Pattern / Hypothesis / Tested / Proved). Failed strengthening attempts documented as failures, not deleted.
- **Strengthen before softening** (per project convention). If RG-0a Case B (heterogeneous gains) does not show the predicted $K_c$-invariance, attempt to derive a *stronger* characterization before downgrading to "the framing fails."
- **Self-contained for handoff.** Future-me or future-agent should be able to pick up cold from any file in this directory.

---

## File index (filled as work proceeds)

- `00-brief.md` — this file
- `01-rg-0a-two-kalman-Kc-extension.md` — load-bearing math (in progress)
- `02-prior-art-rg-ib-fep.md` — delegated prior-art search (pending)
- `03-rg-0c-strategy-recursion.md` — (O, Σ) recursion check (gated on RG-0a)
- `99-verdict.md` — synthesis and decision (final)
