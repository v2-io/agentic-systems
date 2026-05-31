# 35 — disc-value-functional-grounding-floor (M1 sister, agent-side)

*Type: discussion. Status: discussion-grade. Stage: draft. Depends: [form-objective-functional, deriv-self-actuation-grounding, deriv-reward-channel-learning-no-go].*

## Predictions vs evidence
Predicted: agent-side M1 sister cluster with two charter instances. Found: that, plus an ambitious **two-routes-exhausts** structural-completeness claim and a clean unification under `#form-objective-functional`'s single-interface commitment.

## Math verification
No directly-verifiable math in this segment — it builds on `#deriv-self-actuation-grounding` (within-model) and `#deriv-reward-channel-learning-no-go` (across-model). The structural claims about exhaustion are recognition-tier, not derivation-tier.

## Prose-coherence — strong
- Five-element shape matches `#disc-identifiability-floor`: Setting → External Theorem → No-go → Boundary characterization → Strengthened consequence. Consistent.
- Sister-cluster framing (agent-side adaptive-substrate vs principal-side protocol-commitment) maps cleanly onto Instance F + Instance G.
- The table at line 73-75 (within-model vs across-model unification) is well-organized.

## **Two-routes-exhausts claim — watch**

The structural-completeness claim at line 77:
> "**Together they exhaust the structural complement of the value-functional interface's information narrowness** — there is no third route internal to the value functional, and no fourth route off-substrate (the two off-substrate axes are agent-side adaptive-substrate and principal-side protocol-substrate; there are no other axes a non-degenerate non-pathological agent can be grounded on)."

This is **the load-bearing structural recognition** of the segment. Two observations:

1. **Strong claim:** That the *only* off-substrate axes are agent-side adaptive-substrate and principal-side protocol-substrate is non-trivial. The kind of claim downstream audits should test by attempting to construct a third route.
2. **Honest scope:** Constrained to "non-degenerate non-pathological agents" + AAT-covered objective-side machinery. The Fallenstein-Taylor-Christiano 2015 reflective-oracle case is explicitly noted as outside scope (line 91-93), not as a refutation.

This is a candidate finding for me as auditor: *can I think of a third off-substrate route?* Some candidates:
- **Observer-side commitment** (separate from principal-side): an external auditor's commitment to declare certain agent-states as out-of-scope. Probably collapses into principal-side under generous reading.
- **Inter-agent grounding**: another peer agent's value-functional could in principle anchor the agent's goal-stability. But this just shifts the narrowness one level out — the peer's value functional is itself narrow.
- **Substrate-level Goodhart**: the agent's substrate (hardware, computational architecture) imposes physical limits on what objectives are realizable. This is genuinely off-substrate but probably collapses into the principal-side category (designer chose the substrate).

These attempted third-routes do seem to fail. **The two-routes-exhausts claim is plausibly true under the stated scope.** But I'd note it as worth checking with a sharper adversarial spike if the framework leans heavily on the exhaustion claim downstream.

## Cross-segment consistency
Forward-refs `#form-objective-functional`, `#disc-identifiability-floor`, `#disc-implementation-impossibility`, `#disc-constructive-impossibility-posture`, `#def-value-object`, `#deriv-self-actuation-grounding`, `#deriv-reward-channel-learning-no-go`, `#deriv-social-welfare-aggregation-impossibility` (for cross-agent open frontier). Coherent.

## Watch list
- The "third cluster of `#disc-constructive-impossibility-posture` catalog" claim (line 97) — verify when I reach that segment.
- Cross-agent narrowness as open extension (line 83-85) — tracked at `spikes/PROPOSED.md` Tier 2.

## Next-segment predictions
`#disc-implementation-impossibility`. Designer-side cluster — three charter instances (Gibbard-Satterthwaite, Myerson-Satterthwaite, Arrow). Will use mechanism-design impossibility framing.

## Brief wandering
The two-routes-exhausts claim is the kind of structural recognition that — if it holds — substantially simplifies how the framework reasons about goal-anchoring. Rather than saying "there are many routes, here are some," it says "there are exactly two, here they are." That's a cleaner structural commitment with a sharper falsification criterion: find a third route to refute. The framework has put a real claim on the table here.
