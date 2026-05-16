# 43 - def-pearl-causal-hierarchy

Source: `01-aat-core/src/def-pearl-causal-hierarchy.md`

## First-pass understanding

This segment recapitulates Pearl's three-level hierarchy for AAT: Level 1 association, Level 2 intervention, and Level 3 counterfactual reasoning. It is explicit that the hierarchy is imported machinery, not an AAT result. AAT's intended contribution comes later: grounding Level-2 access in the adaptive loop and using regime-indexed identification strength in strategy revision.

The useful distinction is availability versus exploitation. A system may physically act on the world and thus have some interventional structure available, but it may not model, estimate, or exploit that structure. PID and LQR examples are used to separate action-coupled operation from deliberative causal reasoning.

## Diagram attempt

The diagram is a strict ladder with an AAT overlay. Level 1 predicts from history, Level 2 asks what happens under `do(a)`, and Level 3 asks what would have happened under an alternative action after an actual action/outcome pair. I added a side note at Level 2 that action-conditioned data must not be confused with do-data; this is the pressure point for AAT's loop-as-Level-2 claims.

## Findings and watches

- Candidate finding: the segment says the mismatch signal, conditioned on the agent's own action, is an interventional signal. That repeats the conditioning/intervention slippage the segment otherwise tries to avoid. A signal conditioned on an action chosen by a policy is not automatically a `do(a)` signal unless the action assignment mechanism is unconfounded, adjusted for, randomized, or otherwise identifiable.
- Candidate finding carried forward: Level-2 availability is phrased as requiring that the agent chose the action and that it was not determined by the same causes as the observation. Many real agents choose actions as functions of internal state and context that also predict outcomes. The text needs either a clean intervention/assignment condition or the weaker wording "intervention-character data whose causal effect may or may not be identifiable."
- Watch: "software `git checkout` gives Level 3 access with ground-truth verification" is too strong if read literally. It can give unusually strong counterfactual execution, but tests, environments, nondeterminism, and incomplete specs still mediate verification.
- Watch: LQR/Kalman and PID examples are useful for availability/exploitation, but later text should not use "has Level 2 access" as if it meant the controller estimates causal effects.

## Local verdict

The imported Pearl hierarchy is the right vocabulary. The local AAT adaptation needs stricter language around `do`: action-coupled feedback is the beginning of causal access, not the same thing as identified interventional knowledge.
