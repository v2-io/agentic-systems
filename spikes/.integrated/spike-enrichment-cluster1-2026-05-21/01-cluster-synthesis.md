# §1 cluster — integrated synthesis (2026-05-21)

*Per Joseph's cluster-sweep direction. The five papers in §1 of `ref/enrichment-candidates-2026-05-21.md` (Conley 1978; Candogan-Menache-Ozdaglar-Parrilo 2010; α-Rank / Omidshafiei et al. 2019; Letcher et al. 2019 — SGA; Cheung-Piliouras-Tao 2021) were chosen for cluster reading because the file author flagged them as potentially "secretly the same mathematical content." After reading all five, that hypothesis verifies more strongly than I expected.*

*This file is the synthesis — what the papers say jointly, where they land in AAT, and the spike-proposal slate they generate. It is the precursor to a Phase-3 entry in `spikes/PROPOSED-ADVANCED.md` and rows in `spikes/PROPOSED.md`. Not yet filed there pending Joseph's review of the synthesis. **Worth flagging**: writing this synthesis surfaced a candidate observation that may be more than enrichment — see the closing "Possibility ladder" section before filing.*

## What the five papers jointly say

The same mathematical object appears under five different names. To make the alignment explicit:

| Domain | Object | Strict regime | Conservative ("lossless") regime |
|---|---|---|---|
| Control theory (Zames / Cheung-Piliouras-Tao) | Passivity inequality $L(z(t)) \le L(z^0) + \int_0^t \langle u, y\rangle d\tau$ | κ>0 strict; energy dissipates | κ=0 lossless; energy conserved |
| Online optimization (CPT 2021 Th 8) | Regret bound | finite passivity ⟹ constant regret | (degenerate / unbounded budget) |
| Game theory, continuous (Letcher 2019) | Helmholtz/Hodge of $J = S + A$ | Symmetric $S$ — potential game — gradient flow | Antisymmetric $A$ — Hamiltonian game — $H = \tfrac12\|\xi\|^2$ conserved |
| Game theory, discrete (Candogan 2010 Th 3.1) | Orthogonal game decomposition | Potential component (gradient flow) | Harmonic component (global cycles) |
| Dynamical systems (Conley 1978) | Decomposition theorem | Strongly gradient-like flow (chain recurrent set = rest points, totally disconnected) | Chain recurrent flow (chain recurrent set = whole space) |
| Evolutionary game theory (Omidshafiei et al. 2019) | Markov-Conley chain (MCC) | Sink chain components = fixed-point attractors | Chain components of nontrivial topology = recurrent cycles |
| **AAT** (this proposal) | **Stability certificate $\mathcal M$** at the R0 rung | **R0-strict** ($\mathcal M\succ 0$, κ>0) — current rung | **R0-loss** ($\mathcal M\succ 0$, κ=0) — new rung |

The mathematical identity across rows is *not* analogy. CPT 2021 Theorem 8 establishes one direction (finite passivity ⟹ constant regret). The Letcher-Candogan correspondence is a continuous/discrete pair of the same Helmholtz decomposition (Candogan 2010 §3 says so explicitly: *"we use the Helmholtz decomposition theorem"*). Conley's Fundamental Theorem (1978, §8.1, OCR line 188) says every flow on a compact space *uniquely* decomposes as a chain-recurrent part + a strongly-gradient-like part — so the strict-vs-conservative split is universal under compactness, not a property of specific game classes. α-Rank (Omidshafiei 2019 §2.4) uses Conley's chain components as the dynamical solution concept; their *complete Lyapunov function* (Def 2.4.9) is the universal version of AAT's certificate (strictly decreasing off the chain-recurrent set, constant on chain components).

The cross-row unification the enrichment-candidates author flagged (*"rows 03 / 10 / 14 / 17 are secretly the same"*) is, with the five papers in hand, more than plausible — it is what the literature already proves and AAT has not yet absorbed.

## Where this lands in AAT

The most economical landing of the unification is **a refinement of the certificate-existence ladder in `#result-certificate-existence`** (and the spine `#disc-stability-certificate` it anchors). The current ladder R0 ⟸ R1 ⟸ R2 has *one* "widest" rung (R0: one-point sector condition, some $\mathcal M\succ 0$, local). Conley + CPT + Letcher all converge on the observation that R0 admits a structural split:

- **R0-strict** — the current rung. $\mathcal M \succ 0$ exists, $\kappa > 0$, dynamics contracts. Conley-equivalent: strongly gradient-like, chain recurrent set ⊆ rest point set. Hodge-equivalent: $S \succ 0$ component dominant. Passivity-equivalent: strictly passive.
- **R0-loss** — *new*. $\mathcal M \succ 0$ exists, $\kappa = 0$, dynamics is conservative (admits constant-of-motion). Conley-equivalent: chain recurrent (full space, or full chain component, recurrent). Hodge-equivalent: $A$ antisymmetric component dominant; $H = \tfrac12\|\xi\|^2$ conserved. Passivity-equivalent: lossless. Coupled with another lossless operator + bounded level sets + divergence-free payoff: Poincaré recurrent (CPT Th 19; classical Liouville).

The strict-or-loss distinction *is* the Helmholtz $S$ vs $A$ decomposition of the linearization. A general flow lives at neither extreme; its dynamics decompose (per Conley 1978 §8.1) into a chain-recurrent subflow + a strongly-gradient-like quotient. AAT's existing R0 rung silently assumes the latter; R0-loss is the former; mixed regimes are the natural interpolation. **The result-statement of `#result-certificate-existence` and the strength-ladder table extend to capture this without altering the Lyapunov-theorem core** — the theorem statement *already* admits $\kappa = 0$ as a non-strict version of clause 2; what is new is naming that case as a structurally distinct rung rather than a degenerate boundary of R0-strict.

The honest-edge question this resolves: `#disc-stability-certificate` line 70 says *"Whether exactly three obstructions exhaust the failure modes is not proved; three are established and each is exact, but exhaustiveness is open"* and line 119 says *"a fourth (e.g. non-autonomous certificate drift for time-varying systems) is not searched."* R0-loss is **not** a fourth obstruction; it is a *refinement of the Interior facet* — the interior subdivides into contracting (strict) and conservative (loss) sub-regions, with the union still bounded by the M1/M2/M3 facets. The spine's own "new facet or new object?" test (line 84) returns "neither — a new reading of the Interior facet, the conservative/recurrent sub-region of the cone interior."

## What about composition / adversarial / strategic-composition machinery

The R0-loss rung is exactly where AAT's most-honestly-edged content sits:

**`#der-adversarial-destabilization` Effects-Spiral.** Currently discussion-grade; the joint-Jacobian spectral-abscissa instability condition is unformalized. CPT Theorem 19 + Proposition 17 give a **constructive promotion path for the constant-sum-game special case**: convex-combination FTRL learning + graphical-constant-sum game with fully-mixed Nash ⟹ DGS is lossless (composition of lossless) ⟹ Poincaré recurrent ⟹ play never converges to Nash, cycles forever. This is the Effects-Spiral's mathematical fingerprint at the lossless boundary. The constructive boundary is sharp: the spiral *cannot* be prevented at the lossless boundary; it *can* be prevented at R0-strict (energy dissipates the spiral away); the transition between the two is exactly the κ → 0 limit of the sector condition. *Discussion-grade → conditional-derived under the named scope* (constant-sum sub-scope of α').

**`#deriv-strategic-composition`.** Currently has sub-scope α' (potential games, Monderer-Shapley) and β' (VI / monotone games / regret-minimization CCE). Letcher's $S/A$ Hodge decomposition shows these are *not orthogonal scopes* — they are the two pure axes of a 2D decomposition every differentiable game admits. α' is "$A = 0$" (pure-potential); the conservative case is "$S = 0$" (pure-Hamiltonian); general games combine both, and SGA is the algorithm that *projects onto the potential component* by augmenting with $\lambda A^\top \xi$. The α' sub-scope's positive results (potential-game convergence) apply to the $S$-projection of any game; the conservative-case results (Poincaré recurrence) apply to the $A$-projection.

**`#def-control-regret`.** CPT Theorem 8 contrapositive: unbounded control regret ⟹ learning operator is not finitely passive. This gives an AAT-internal *diagnostic for certificate-interior-vs-boundary position*: bounded growth of measured control regret is the observable signature that the agent's update operator sits in R0-strict (positive κ); polynomial or unbounded growth is the signature that it has slipped to R0-loss or worse.

**`#disc-stability-certificate` line 84 "accumulation-typing pattern."** The spine itself anticipated this — the temporal/representation-dual reading of the Interior facet. R0-loss makes that anticipation concrete: the *temporal dual* of a strict contraction is a conservative recurrence; the operator family $\mathcal A_{\mathrm{refl}}$ (reflected Lindley/Loynes; line 84) is the AAT-internal analog of CPT's lossless feedback interconnection. The 2026-05-19 continuity-persistence finding (the operator split into $\mathcal A_D$ destroy-and-reconstruct vs $\mathcal A_{\mathrm{refl}}$ reflected) is naturally read as the strict-vs-loss split inherited at the turnover index.

## Spike-proposal slate

The cluster yields one Phase-3 PROPOSED-ADVANCED entry covering the unification + five Tier-2 PROPOSED rows. Sketched here; final filing pending Joseph's review.

### Phase-3 entry: *"R0-Loss Rung and the Cross-Row Unification — Conley-Helmholtz-CPT-α-Rank Cluster"*

*One PROPOSED-ADVANCED entry as the cluster's home. Mathematical thesis above. Direction: add R0-loss to the certificate-strength ladder; surface the Helmholtz $S/A$ decomposition as the structural form of the strict-vs-loss split; identify chain components (Conley/MCC) as the right solution concept for R0-loss dynamics.*

### Tier-2 PROPOSED.md rows (5)

| # | Title | Source | What it does |
|---|---|---|---|
| 1 | R0-loss rung extension of `#result-certificate-existence` | enrichment-2026-05-21 §1.a/§1.e ; ADV §Phase-3 cluster | Adds R0-loss to the strength ladder; Conley + CPT give the universality + the lossless boundary. Most foundational of the five. |
| 2 | Helmholtz $S/A$ decomposition as scope-axis structure of `#deriv-strategic-composition` | enrichment-2026-05-21 §1.b/§1.d ; ADV §Phase-3 cluster | Letcher + Candogan give the formal decomposition; α' (potential) and conservative-case (Hamiltonian) are the two axes, general games are mixtures. SGA is the algorithmic projection onto the $S$-component. |
| 3 | Effects-Spiral promotion path via CPT Th 19 + Prop 17 | enrichment-2026-05-21 §1.e ; ADV §Phase-3 cluster | Constant-sum sub-scope of `#der-adversarial-destabilization` Effects-Spiral promotes discussion-grade → conditional-derived. Need: divergence-free game payoff + bounded level sets. |
| 4 | Bounded-regret diagnostic for `#def-control-regret` | enrichment-2026-05-21 §1.e | CPT Th 8 contrapositive: regret growth as observable signature of agent's certificate-interior position (strict vs loss). |
| 5 | Markov-Conley chain solution concept for `#deriv-strategic-composition` β' sub-scope | enrichment-2026-05-21 §1.c | Replace "regret-minimization → CCE" as the β' fallback with "chain components are the macro-state." Recurrent set *is* the solution; α-Rank's MCC machinery is the computational handle. Per the enrichment-candidates author this is "sharper than AAT's current §F treatment of distributional macro-states." |

Each Tier-2 row will carry reciprocal Working-Note backlinks in the target segment (`#result-certificate-existence`, `#deriv-strategic-composition`, `#der-adversarial-destabilization`, `#def-control-regret`).

## What strengthen-before-soften says about this proposal

This is *enrichment*, not repair. Two distinct strengthening passes are owed before any spike actually launches off these proposals:

1. **AAT-internal derivation of R0-loss.** The Helmholtz decomposition + CPT-passivity-≡-AAT-sector-condition + Conley-fundamental-theorem-on-compact-spaces *together* should yield a self-contained AAT-internal proof that R0-loss is a real rung — i.e., that $\mathcal M \succ 0$ with $\kappa = 0$ characterizes a structurally distinct dynamic mode under bounded-orbit conditions, and that the Helmholtz $S/A$ split realizes the strict-vs-loss boundary as a continuous interpolation. *Required before R0-loss can land at `status: exact` rather than at `recognition`-tier.*
2. **Effects-Spiral conditional-derived promotion under named premises.** Currently the discussion-grade Effects-Spiral has an unspecified $\gamma_A(\|\delta\|)$ leg. CPT Th 19 + Prop 17 + divergence-free + bounded-level-sets *replace* that unspecified leg with a different, harder-to-prove-but-explicit precondition. The promotion path needs to articulate which AAT-native conditions imply or are implied by CPT's preconditions; the promotion is genuine only insofar as those conditions are AAT-checkable on real agent classes.

If both strengthenings succeed, the cluster lands as (1) R0-loss in the spine + ladder, (2) Effects-Spiral conditional-derived for constant-sum case, and (3) the four downstream tier-2 spike proposals as forward enrichment work. If either strengthening fails, the cluster lands as recognition-tier — naming the connection without committing AAT to derivations it cannot complete — which is *also* worth doing, because it discharges the auditor-honesty question about whether AAT's R0 rung is "constructed case-by-case" or "guaranteed by Conley."

## Open: what I have not done yet

- Cross-row verification: I have not opened the `Prior_art_for_AAT_*.csv` files to check which rows the original author meant by 03/10/14/17. The structural unification is real either way, but tying it precisely to the author's flagged rows would close the loop on what he saw.
- Conley `ref/conley-1978/` is OCR'd cleanly; I have read §I.7 (attractor-repeller pairs, Morse decompositions) and §I.8 (chain-recurrent + strongly-gradient-like + the fundamental decomposition statement). I have not read chapters III–IV (Morse index proper, continuation theory). Those are not load-bearing for the present proposal but worth a return read if R0-loss promotion requires the Morse-index machinery for the chain-component classification.
- The full Math-of-OR Candogan 2011 paper is owed before any actual spike launches (the 6-page arXiv 1005.2405 has the statement and the abstract; the full machinery for the orthogonal decomposition + the explicit projection formulas is in the journal version).
- Patrão / Norton: not acquired; not load-bearing once Conley original + Omidshafiei restatement are in hand.

## Possibility ladder for what this might be

The synthesis above conservatively positions this as *enrichment* — "useful prior art that AAT could anchor in more deeply", per the file author's framing. While writing it I noticed something that wants to be named even if I cannot yet rule between modes — the strengthen-first move is to name the ladder rather than soften pre-emptively to the conservative mode. **Each rung still depends on the strengthen-first passes #1 and #2 above succeeding; this section says what they might mean if they do, not what they are.**

- **(L0) Pointer cluster.** Five papers, AAT cites them, no structural change. The conservative reading of the file author's intent. R0-loss is not added; the literature is just cited better.
- **(L1) Recognition-tier landing.** The R0-loss rung is added as `recognition`-tier (not exact); the Helmholtz/Hodge identification is added as cross-reference in `#disc-stability-certificate`; the Effects-Spiral stays discussion-grade with a CPT pointer.
- **(L2) Exact rung extension.** Strengthen-first pass #1 succeeds: R0-loss is added at `status: exact` to the ladder in `#result-certificate-existence`; the spine is updated.
- **(L3) Conditional-derived promotion of Effects-Spiral.** Strengthen-first pass #2 succeeds: `#der-adversarial-destabilization`'s Effects-Spiral becomes conditional-derived for the constant-sum sub-scope.
- **(L4) Cross-row unification as a *finding-class* about AAT's tools.** If both passes succeed and the cross-row check (against rows 03/10/14/17 of the prior-art-analysis CSVs) lands, then we have not just a new rung — we have *the precise mathematical content that explains why AAT's tools converge across rows in the first place*. The four "convergent meta-findings" the author flagged would be one finding under five names. This is closer to a meta-segment refinement than an enrichment cycle: it elevates "AAT's tools converge convergent" from observation to theorem.
- **(L5) Reframing of the certificate-cone Interior facet itself.** If the Helmholtz/Hodge decomposition is structurally load-bearing (every Interior point has a $S+A$ decomposition; R0-strict is "$A$-component zero"; R0-loss is "$S$-component zero"), then the Interior is not a single object — it is a 2-axis decomposition, and the *boundary between strict and loss is itself a sub-facet of the spine*. This would refine `#disc-stability-certificate`'s four-facet structure into something like five-facet, with the strict-loss boundary as a fifth facet *inside* the Interior. This is structural enough that it would want to land in the spine itself, not as a separate proposal.

Watching for. If during the strengthen-first passes evidence accumulates toward L4 or L5, this isn't the spike-proposal cluster it currently looks like — it is closer to the kind of cross-segment recognition that earned `#disc-stability-certificate` itself a spine segment in the 2026-05-14 operator-family-unification cycle.

**Honest mark:** the L4/L5 readings are *plausible from shape* — exactly the failure mode `~/.claude/memory/epistemic-discipline/plausibility-vs-verification.md` warns about. The five-paper convergence is real and verified; the elevation from "five papers say the same thing" to "this is AAT's spine telling us about itself" is shape-matching that needs proof, not assertion. The conservative landing is L1; the aspirational landing is L5; the strengthen-first work is what tells the difference. I have not done that work yet.

## Suggested next move for Joseph

If the synthesis lands for you:
1. Confirm the cluster as written, and I file the Phase-3 entry + 5 Tier-2 rows.
2. If the L4/L5 readings interest you, the strengthen-first work on R0-loss (proof that it is a structurally distinct rung, not a degenerate boundary case) should be its own spike before anything lands. The synthesis above gives the proof's likely shape (Lyapunov-theorem at κ=0 + Helmholtz $S=0$ case + Conley chain-recurrent characterization + CPT lossless storage function), but the actual proof has not been written.
3. If the structural enrichment is well-supported but the spike proposals feel premature, the natural next reading is the full Math-of-OR Candogan + a return pass on Conley §I.7 (Morse decompositions) — that gives the most rigorous setting for testing whether L5 (the strict-loss boundary as a fifth facet) holds.
4. Or move on to §2 cluster; this stays in the spike directory until you signal a direction.

The §1 cluster does not block any current work; it sits where the file author placed it (post-Phase-4 enrichment). It can wait.
