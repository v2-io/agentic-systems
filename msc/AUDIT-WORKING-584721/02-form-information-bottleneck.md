# Reflection 02 — form-information-bottleneck (Section I row 11)

First reflection under the new cadence. One Read, one reflection.

## §4.2 dependency check

`depends:` field: `[form-agent-model]`. form-agent-model is at OUTLINE row 10, upstream of this segment at row 11. **No backward-dependency finding** — the OUTLINE order is consistent with the declared depends.

But: the Formal Expression uses $\mathcal C_t$, $o_{t+1:\infty}$, *and* $a_{t:\infty}$. Tracing the depends:
- `form-agent-model` transitively covers def-agent-environment, def-observation-function, def-chronica → so $\mathcal C_t$ and $o$ are reached.
- **Action notation $a_{t:\infty}$ requires `def-action-transition`. That slug is not in the transitive closure of this segment's depends.**

This is the same finding *type* as the one I noted on `scope-adaptive-system` (which used $\mathcal C_t$ without listing def-chronica): the `depends:` list is incomplete relative to what the Formal Expression actually uses. Different kind of finding from the §4.2 critical-finding case (which is about backward OUTLINE-order pointers); this is about completeness of declared dependencies.

Two instances now (scope-adaptive-system: missing def-chronica; form-information-bottleneck: missing def-action-transition). Worth tracking as a pattern. If a third instance appears, it's a systematic discipline issue rather than two isolated misses.

Adding to candidate findings:
- F-A1 (already logged): scope-adaptive-system depends drift — missing def-chronica
- F-A2 (new): form-information-bottleneck depends drift — missing def-action-transition (transitively)

## Predictions vs. evidence

I predicted (in 00-initial-predictions): "I want to verify the segment's own self-characterization is honest" for the meta-segments and "I expect to find at least one tension between Section II results being claimed-survived and the actual coupled-formulation derivation" for logogenic-agents.

For *this* segment — form-information-bottleneck — I didn't predict anything specific. The CLAUDE.md / CLAUDE-2.md content primed me with the IB-lineage vs IT-MDP-lineage distinction. So the segment's substantive content lands largely as expected. **Pretty much what I expected.**

What I *didn't* predict: the Epistemic Status section's quality. It's unusually well-shaped — explicitly distinguishes "applied external theorem" (status: exact, but the exactness is the imported theorem's, not novel AAD machinery) from the tier-stratified $\beta(\rho, \pi)$ claim (robust-qualitative). The "Max attainable" remark explicitly: "exact for the IB-as-applied-theorem core (already at ceiling); robust-qualitative for the $\beta(\rho, \pi)$ dependence claims." That's exactly the per-claim-tier discipline FORMAT.md's Epistemic Triage prescribes, executed cleanly.

This could be a model for other segments. Worth noting in Section E (confirmation/calibration) of the report.

## Cross-segment consistency

The Discussion's "IB lineage vs information-theoretic-MDP lineage" paragraph is the cross-reference promised in the 2026-04-24 Gemini pressure-point cycle's Tier 1 landing (per CLAUDE-2.md priming). It defuses "abandoned IB purity" framings explicitly, names which AAD compressions use which form, and positions the strategy-cost compression as a sibling rather than an inconsistency. Cross-references to `#disc-compression-operations`, `#form-strategy-complexity-cost`, `#deriv-strategy-cost-regret-bound` — all forward references; can't verify their other end yet.

The "Connection to variational free energy" paragraph similarly addresses the active-inference-vs-AAD positioning. Borrows IB-as-rate-distortion-specialization-of-VFE without committing to preferences-as-priors. Clean.

No contradictions with what I've read so far.

## Math verification

Nothing to compute — the Formal Expression is a definition (citing Tishby et al. 1999) rather than a derivation. The IB optimum's form is the imported theorem. Could verify that the cited theorem actually says this; deferring to a later citation-spot-check session.

## Status-label check

`status: exact` — the segment's Epistemic Status defends this carefully: "exact for the IB-as-applied-theorem core" with the formulation choice itself acknowledged. The claim is calibrated to the imported theorem, not to a novel AAD result. Honest.

`stage: draft` — interesting given the careful Epistemic Status. The discipline I see in the Epistemic Status section would land at claims-verified or higher; the draft stage might just mean nobody has run the Gate 1/2 audit on this segment recently, not that the content is rough.

## What am I now curious about?

- The strategy-cost direction: the Discussion's explanation of why strategy-cost uses KL-to-reference-policy (IT-MDP lineage) rather than MI-to-observable (IB lineage) is "the choice depends on whether the compressed variable should preserve information about an observable or match a target policy." That's a reasonable distinction, but I want to verify in the actual `#form-strategy-complexity-cost` segment that the *strategy* is genuinely best understood as targeting a policy rather than as compressing observables. If a strategy can be coherently framed either way, the choice of form looks more arbitrary than the segment claims.
- The $\beta(\rho, \pi)$ claim is qualitative-only here. Is it derived more sharply downstream? `#disc-compression-operations` is the obvious place to look.
- The "Y - X - T Markov chain holding by construction" — does it really? T (=$M_t$) "has access to history but not directly to future observations" — this is the standard IB Markov assumption. But for goal-conditioned (Class 2) agents, $M_t$'s update is influenced by goals, which are themselves influenced by future observations through the strategy's expected outcomes. Could the Markov chain *fail* under Class 2 architectures? Worth flagging for when I read `#scope-observation-ambiguity-modulation` and the logogenic-agents D3 segment.

## What changes in my outline for the final report?

Adding to Section B (findings):
- F-A2: form-information-bottleneck depends drift — missing def-action-transition.
- Pattern observation if F-A3 appears: systematic depends-list discipline issue.

Adding to Section E (calibration/confirmation):
- form-information-bottleneck's Epistemic Status section is well-shaped — could be a model for other segments. The "Max attainable" remark with per-claim tiering is exactly the FORMAT.md Epistemic-Triage discipline executed.

## Tracking — recently-added structural moves to watch propagation of

- IB-lineage vs IT-MDP-lineage cross-reference: present here ✓ (this is one of the recent additions, landed 2026-04-24 Tier 1).

## Cadence check

One Read tool call → this reflection file → next segment will be a fresh Read. Working as designed.

Next: AAD Section I row 12 = `def-model-sufficiency`.
