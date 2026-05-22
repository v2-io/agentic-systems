# §1 cluster — verdict

*Verdict on the cluster-1 enrichment synthesis (`01-cluster-synthesis.md`), after working through the strengthen-first attempts in `02-r0-loss-derivation.md`, `03-effects-spiral-attempt.md`, `04-cross-row-check.md`, `05-fifth-facet-test.md`. Cluster: Conley 1978 + Candogan 2010 + Letcher 2019 + CPT 2021 + Omidshafiei 2019 (+ Balduzzi 2018, Papadimitriou-Piliouras 2018 as adjacent prior art).*

## Headline

**Mixed outcome — partial succeed-at-claim with one refutation:**

- **R0-loss as a structurally distinct rung in `#result-certificate-existence`'s ladder: succeeds at exact, at the linearized level.** Result 1 (three-case structural distinctness), Result 2 (Helmholtz characterization for the pure case), Result 3 (Conley anchoring) jointly land R0-loss at `status: exact`. This is the L2 rung of the synthesis's Possibility ladder. (§02)
- **Effects-Spiral conditional-derived promotion: refuted as proposed; replaced by a sharper related claim.** CPT Theorem 19 + Prop 17 do **not** derive the Effects-Spiral — they predict the *opposite* dynamic (bounded recurrence rather than unbounded mismatch growth) because the two phenomena live on different state spaces and CPT's coupling is matrix-fixed while AAT's Effects-Spiral requires state-dependent coupling. The genuine landing is the *converse* — CPT rules out the Effects-Spiral in the FTRL+constant-sum sub-scope, and FTRL × graphical-constant-sum-with-fully-mixed-Nash is a worked instance of the R0-loss regime. This is **not** the L3 of the Possibility ladder; L3 falls. (§03)
- **L4 cross-row unification: succeeds in a refined form, scoped to three of the four flagged rows.** Rows 03 (Lyapunov persistence) + 10 (adversarial tempo) + 14 (strategic composition) reduce to the certificate-interior viewed under the Helmholtz $S/A$ decomposition. Row 17 (credit assignment) is connected via a different facet (the M1 boundary, Sylvester rank-collapse) — claiming all four rows are "secretly the same" overreaches. The refined L4 finding-class is genuine and surfaces a real theorem about AAT's internal structure. (§04)
- **L5 fifth-facet of `#disc-stability-certificate`: justified in the *refinement-of-Interior-facet* form, not in the *new-fifth-peer-facet* form.** Per the spine's own "new facet or new object?" test (line 84) and the accumulation-typing precedent, the strict/loss split is a new internal structure on the existing Interior facet (Helmholtz $S/A$ decomposition of the cone interior), not a new peer facet. The four-facet structure stays four; the Interior facet gains a 2-component refinement. (§05)

## Position on the Possibility ladder

The synthesis's Possibility ladder L0–L5:

- **L0 (pointer cluster):** below this verdict's outcome.
- **L1 (recognition-tier):** below this verdict's outcome (the rung is exact, not recognition).
- **L2 (exact rung extension):** **lands.** R0-loss is exact via §02 Results 1+2+3.
- **L3 (Effects-Spiral conditional-derived):** **refuted.** §03 shows CPT Th 19 + Prop 17 do not provide the lift; they predict the dual phenomenon (bounded recurrence, not Effects-Spiral). L3 as proposed in the synthesis falls. The genuine related landing is the *no-spiral converse* + the worked R0-loss instance, which belong as Discussion notes in `#der-adversarial-destabilization` and `#deriv-strategic-composition` $\beta'$.
- **L4 (cross-row unification as finding-class about AAT):** **lands at refined form.** Rows 03/10/14 share the Helmholtz $S/A$ structure on the certificate Interior; row 17 connects through the M1 boundary facet via Sylvester (not via Helmholtz). The L4-as-stated overreached (claiming all four rows are the same); the L4-as-refined is a sharper, AAT-internal statement of what the convergence actually is.
- **L5 (fifth facet of `#disc-stability-certificate`):** **lands at refined form.** The strict/loss split is a refinement of the Interior facet (a 2-component Helmholtz decomposition), not a fifth peer facet. The spine's own "new facet or new object?" test returns "a new internal structure on an existing facet," matching the accumulation-typing precedent.

**Net position: between L2 and L5, with L3 refuted and L4/L5 in their refined-not-stated form.** The exact rung lands; one of two strengthening passes refutes the synthesis's proposal and replaces it with a sharper related claim; the cross-row and fifth-facet readings land in refined form rather than as stated.

## What lands at `status: exact` (with proofs in §02–§05)

1. **R0-loss is a structurally distinct rung from R0-strict and from the M1 boundary** (§02 Result 1, three-case partition of linear-system spectrum: Hurwitz / imaginary-axis-semisimple / non-semisimple-or-mixed-strict-unstable).
2. **Pure R0-loss linearization in Euclidean metric $\mathcal M = I$ is exactly $J$ antisymmetric** (§02 Result 2; Letcher 2019 Lemma 1 + Definition 2 are the AAT-internal characterization of the pure R0-loss linearization). The general-$\mathcal M$ statement uses the $\mathcal M$-symmetric / $\mathcal M$-antisymmetric decomposition. The mixed case (partial chain-recurrent set) reduces to Conley's universal decomposition.
3. **Linear R0-loss dynamics on a compact invariant set are chain-recurrent in Conley's sense** (§02 Result 3). The R0-loss subspace is exactly the chain-recurrent component of Conley's Fundamental-Theorem decomposition (1978 §8.1).
4. **The CPT-bridge from finite-passivity to R0-loss is qualitative, not quantitative** (§02 Result 4). The synthesis's claim that CPT's storage function $L$ is "structurally identical" to AAT's certificate $V$ is **refuted at sharp form**: $L$ lives on cumulative-payoff space, $V$ on strategy-error space, and they have different functional forms. The qualitative bridge survives: any finitely-lossless DGS has its linearization at an accumulation equilibrium in R0-loss class.
5. **FTRL × graphical-constant-sum-with-fully-mixed-Nash is a worked R0-loss instance** (§03 + CPT Theorem 19 + Proposition 17). This is the concrete agent class realizing R0-loss in AAT's existing taxonomy.
6. **Rows 03 + 10 + 14 of `ref/prior-art-analysis/` share the Helmholtz $S/A$ decomposition of the certificate Interior as their unifying object** (§04). Row 17 is a facet of the same spine via the M1 boundary mechanism (Sylvester), distinct from rows 03/10/14's Interior mechanism.
7. **The strict/loss split satisfies two of three facet-tests** (§05 tests (ii) and (iii)): mutual invariance vs M1/M2/M3 (orthogonal to M3, disjoint from M1/M2) and constructive-impossibility-posture instance (R0-loss floor + SGA-as-unique-escape + structural no-go). Test (i) returns ambiguous: the strict/loss split is congruence-invariant but lives on the Jacobian side rather than the cone side.

## What is *refuted* (and should be deleted, not softened)

Per `~/.claude/memory/epistemic-discipline/integration-is-replacement.md` ("the refuted claim is deleted, not kept-softened-with-a-pointer"):

- **DELETE from the synthesis:** the claim that CPT's storage function $L$ is structurally identical to AAT's certificate $V = e^\top \mathcal M e$ (synthesis line 56, "Bridge identification (claim)"). The two functions live on different state spaces with different functional forms.
- **DELETE from the synthesis:** the proposal that `#der-adversarial-destabilization`'s Effects-Spiral can be promoted to conditional-derived via CPT Th 19 + Prop 17 (synthesis lines 40, 62, 73 etc.). CPT predicts bounded recurrence, the Effects-Spiral predicts escape; the alignment is opposite, not coincident. The Effects-Spiral strengthening remains the existing `spikes/PROPOSED.md` Tier-1 item ("state-dependent coupling + closed-form instability proof for concrete agent classes"), not subsumed by this cluster.
- **DELETE from the synthesis:** the casual reading that row 17 (credit assignment) is "secretly the same" as rows 03/10/14. Row 17 sits on a different facet (M1 boundary) with a different mechanism (Sylvester).
- **DELETE from the synthesis:** the L5 framing of the strict/loss boundary as a *fifth peer facet* of `#disc-stability-certificate`. It is a refinement of the Interior facet, not a peer.

These are not weakenings — they are corrections of overreach. The replacement claims (R0-loss as exact rung, no-spiral converse, Interior-facet refinement) are *new, true statements* that survive the strengthen-first pass.

## Segment-level landing plan

If Joseph approves the verdict, this is what should land in canonical segments (gated on his call; no canon-modifying spike commits unless he says go):

### Primary: `#result-certificate-existence`
- Add R0-loss row to the certificate-strength ladder table (per §02 final table). The row uses the exact characterization: "$A = -J$ has imaginary-axis spectrum (semisimple), other eigenvalues if any are strict-stable."
- Tier: `exact` at the linearized level. The status mirrors the existing R0/R1/R2 rungs.
- Add to Derivation section: brief proof sketch from §02 Result 1 (Lyapunov-theorem extension to non-Hurwitz $A$, three-case partition).
- Add to Epistemic Status: "exact for linear systems; the nonlinear extension follows the standard center-manifold analysis (Khalil §4.3) and is not in AAT's claim" — same scope honesty as R0-strict.

### Secondary: `#disc-stability-certificate`
- Refine the Interior facet row of the four-facet table (line 44): from "$\mathcal M \succ 0$ on the scope ball: the contraction holds" to "$\mathcal M \succ 0$ on the scope ball, Helmholtz $S/A$ decomposition: $S_\mathcal M \succ 0$ gives R0-strict contraction; $S_\mathcal M = 0$ gives R0-loss conservation/recurrence."
- Add a Discussion paragraph (parallel to the existing line 84 paragraph on accumulation-typing): "the Helmholtz $S/A$ decomposition is the spectral dual of the Interior facet, run through this segment's own test ('new facet or new object?') returns *neither* — a new internal structure on an existing facet, the spectral/representation dual of the Interior." Cite Conley 1978, Letcher 2019, CPT 2021.
- The four-facet structure stays four. Line 70 honesty-edge ("Whether exactly three obstructions exhaust the failure modes is not proved") stays unmodified (R0-loss is not a failure mode).

### Tertiary: cross-segment cross-references
- `#deriv-strategic-composition` $\beta'$ sub-scope: add Discussion note identifying the FTRL+graphical-constant-sum-with-fully-mixed-Nash case as the R0-loss instantiation of the cyclic-distributional regime, citing CPT Theorem 19. The $\beta'$ sub-scope's Poincaré recurrence is exactly R0-loss at the composite layer.
- `#der-adversarial-destabilization`: add Discussion note (the *no-spiral converse*): "CPT 2021 Theorem 19 + Prop 17 *rule out* the Effects-Spiral in the FTRL+graphical-constant-sum-with-fully-mixed-Nash sub-scope: under matrix-fixed coupling in that regime, the joint dynamic is Poincaré recurrent on bounded level sets, so $\Vert\delta_B\Vert$ does not escape past $R_B$. The Effects-Spiral requires structurally different (state-dependent) coupling and remains discussion-grade; its formalization is `spikes/PROPOSED.md` Tier-1 work, not subsumed by this enrichment cluster."
- `#def-control-regret`: add Discussion note for the CPT Theorem 8 contrapositive: "bounded control regret is the AAT-internal diagnostic that the agent's update operator has finite-passive structure; unbounded control regret means the update is not finitely-passive (potentially escaping R0-loss into the no-certificate regime)." Tier: cited (CPT Th 8).

### Working Notes / Provenance
- `#result-certificate-existence` Working Notes: add provenance entry citing this spike directory and the cluster prior art (Conley 1978, Letcher 2019, CPT 2021).
- `#disc-stability-certificate` Working Notes: add provenance entry for the Interior-facet refinement.

## What does NOT change

- The three-obstruction failure-mode analysis (M1/M2/M3 in `#disc-stability-certificate`). R0-loss is not a failure mode; it is a non-failing-but-non-contracting interior sub-region.
- The four-facet structure of `#disc-stability-certificate`. The strict/loss split refines the Interior facet, not the facet count.
- `#disc-stability-certificate` line 70 honesty-edge on exhaustiveness.
- `#disc-stability-certificate` OUTLINE preamble (the recommended-only line 118 propagation-plan step). The R0-loss refinement is small enough that the OUTLINE preamble doesn't need to change.
- `#der-adversarial-destabilization`'s Effects-Spiral tier. It stays `discussion-grade`. The CPT no-spiral converse adds a Discussion safety result but does not lift the Spiral itself.

## Open edges (honestly named)

- **Mixed R0-loss case is sketched, not fully proved.** The decomposition into chain-recurrent + strongly-gradient-like is asserted via Conley's Fundamental Theorem but the explicit metric construction $\mathcal M$ in the mixed case requires more detailed center-manifold work than this spike provides. The pure case (all imaginary eigenvalues) is exact; the mixed case is *exact via Conley's theorem* but the explicit $\mathcal M$ construction is left as standard Khalil-style center-manifold analysis. Not a blocker; flagged for completeness.
- **Composition under coupled (FIC) interconnection is partial.** §02 Result 5 gives decoupled composition exactly; coupled composition under CPT-Fox-Shamma passivity machinery is regime-dependent and the synthesis's hint that "R0-loss × R0-loss is R0-loss under FIC" is true (CPT Theorem 2) but R0-strict × R0-loss under FIC is open. Not load-bearing for the present landing; flagged.
- **Discrete-time extension.** AAT's segments are continuous-time, matching CPT 2021's continuous-time FTRL framework. CPT §7 acknowledges discrete-time as open; if `03-llm-core/` ever needs R0-loss in discrete-time (token-update setting), the extension is non-trivial and currently open. Not load-bearing for the AAT-core landing.
- **Nonlinear extension.** The R0-loss rung lands at the *linearized* level, matching `#result-certificate-existence`'s scope. Nonlinear R0-loss (whether nonlinear dynamics with Case-(iii) linearization are actually Lyapunov-stable) is the standard center-manifold question (Khalil §4.3) and is not in AAT's claim. Mirrors the scope discipline R0-strict already follows.
- **Cross-row coverage.** The L4 verification was scoped to rows 03/10/14/17 as the synthesis flagged. Other interior-facet rows (04 structural adaptation, 08 composite agency, 15 persistence stance) might also fit the Helmholtz-$S/A$ unification; this spike did not check them. A follow-on cross-row pass over the full 21-row prior-art landscape would surface that. Not load-bearing for the present landing.

## Strengthen-first audit of this verdict

The verdict claims R0-loss lands at `exact` — let me run the strengthen-first check on the claim itself:

- *Can the proof be strengthened beyond linearized?* Yes, by importing Khalil-style center-manifold analysis, but that work is not done here and is not part of `#result-certificate-existence`'s scope (the segment is linearized; R0-loss inherits the same scope).
- *Can the Helmholtz characterization be strengthened beyond pure R0-loss?* Yes — the mixed case via Conley + center manifold gives a partial Helmholtz characterization, but the explicit metric construction is non-trivial. The pure case is exact; the mixed case is exact via Conley but the explicit $\mathcal M$ in mixed cases is sketched not proved. **Honest mark: §02 Result 2 is exact for pure R0-loss; the mixed-case extension is sketched.**
- *Can the cross-row L4 claim be strengthened to cover all 21 rows of the prior-art-analysis?* Possibly — see Open edges above. Not done here. **Honest mark: L4 covers 3 of 4 flagged rows; whether other rows fit is uncovered.**
- *Can the L5 strict/loss-as-refinement-of-Interior be strengthened to a new peer facet?* Test (i) in §05 returned ambiguous; tests (ii) and (iii) returned positive. The honest landing is *refinement of Interior*, matching the spine's own accumulation-typing precedent. Could be argued to be a peer facet under a different test framework, but the spine's own tests give refinement.

These honest marks are all named in the verdict's "open edges" section; the verdict itself does not overclaim.

## Why this is a strengthen-first success

The strengthen-first move was to try to lift R0-loss to exact (succeeded), to lift the Effects-Spiral to conditional-derived (refuted; replaced by sharper related claim), to verify the cross-row unification (succeeded in refined form), and to test the fifth-facet status (refined to Interior-refinement). Two of four substantive moves landed; one was refuted as proposed and replaced by a more honest claim; one landed in refined form.

The conservative move (L1 recognition-tier) would have discharged the work without testing whether R0-loss was a real rung. The strengthen-first move did the test, found the rung is real (R0-loss as exact) but the Effects-Spiral promotion is not real (its alignment with CPT was illusory).

This matches `~/.claude/memory/epistemic-discipline/integration-is-replacement.md`: the refuted Effects-Spiral promotion is **deleted** (not kept-softened-with-a-pointer), and the R0-loss rung is added with its present-truth label (`exact`) without down-tiering for novelty. The verdict's tone — naming what fell as well as what landed — is the present-truth-only posture.

## Recommended next steps

1. **Joseph reviews this verdict.** Decide whether to proceed with segment landings as outlined.
2. **If approved, two segment-landing spikes:** (a) `#result-certificate-existence` R0-loss rung extension (tier `exact`); (b) `#disc-stability-certificate` Interior-facet refinement Discussion paragraph + four-facet-table row update.
3. **Discussion-note batch:** the no-spiral converse in `#der-adversarial-destabilization`, the R0-loss instantiation note in `#deriv-strategic-composition` $\beta'$, the CPT-Theorem-8 contrapositive note in `#def-control-regret`. These are smaller, cross-reference-only edits.
4. **Filing in `spikes/PROPOSED.md`:** at most *two* Tier-2 rows from the synthesis's slate survive the verdict — (1) the R0-loss rung extension and (2) the Helmholtz-decomposition Interior-facet refinement. The other three (Effects-Spiral promotion, MCC-as-$\beta'$-solution-concept, CPT-bounded-regret-diagnostic-for-`#def-control-regret`) are either refuted (Effects-Spiral) or already covered as cross-references (the MCC and CPT-Th-8 notes don't need their own spike rows since they fit in Discussion). The synthesis's Phase-3 PROPOSED-ADVANCED entry should be rewritten in the refined-not-stated form, naming the R0-loss rung + Helmholtz Interior-refinement as the cluster's actual content.
5. **L4 cross-row extension follow-up (optional, low priority):** check whether the Helmholtz $S/A$ unification covers other interior-facet rows (04, 08, 15) beyond the four flagged. Not blocking.

## A meta-note on the synthesis

The 2026-05-21 synthesis was high-quality — it correctly identified the cluster as more than enrichment and flagged the Possibility ladder rather than soft-landing to L1 pre-emptively. The synthesis's own line 86 already named the strengthen-first move as required for L4/L5, and explicitly named the plausibility-vs-verification trap (line 97). This verdict is the strengthen-first work the synthesis asked for, and the outcome (partial succeed, one refutation, two refined-not-stated landings) is exactly what such a pass should produce — neither a triumphant "everything lands" nor a defeated "nothing lands."

The synthesis was right that the cluster is more than pointer-cluster (L0). The synthesis was right to flag the Effects-Spiral promotion as needing proof rather than asserting it. The synthesis was right that L4/L5 needed actual work. The verdict's correction of the synthesis's *quantitative* claim about CPT's storage function (that it is "structurally identical" to AAT's certificate) is the kind of correction the synthesis asked for — and the corrected version (qualitative bridge instead of quantitative identity) is itself a real and useful result.

The bigger picture this verdict adds: AAT is moving toward a **two-rung Interior** (R0-strict + R0-loss) with the Helmholtz $S/A$ decomposition as the internal coordinate. That is not a fifth facet; it is a refinement of the framework's spine that absorbs a substantial chunk of the differentiable-game-theory and dynamical-systems literature into AAT's existing vocabulary, without forcing AAT to invent new mathematics. The integration-not-invention posture of `#result-certificate-existence` is preserved; what the cluster adds is recognition that AAT's R0 rung was silently the *strict* sub-region of a more general object whose name in the broader literature is "chain-recurrent + strongly-gradient-like" (Conley) / "Helmholtz $S+A$" (Letcher) / "lossless + strict passivity" (CPT).

That is a meaningful enrichment, sharper than "five papers AAT could cite better." It is also smaller than "AAT's spine should be reorganized." The correct middle landing — R0-loss as exact + Interior-facet refinement + cross-segment notes — is what this verdict commits to.
