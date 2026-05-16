# 23 - def-causal-information-yield

Segment: `01-aat-core/src/def-causal-information-yield.md`
Dependencies: `der-action-selection`, `def-mismatch-signal` - satisfied.
Status observed: `type: definition`, `status: exact`, `stage: deps-verified`.

## Reflection

The definition is crisp: CIY is an expected KL distance between the outcome distribution under action `a` and outcome distributions under comparator actions. The segment is also unusually explicit about what CIY is not: it is not expected information gain. That distinction prevents a common exploration mistake, because an already-known but distinctive intervention has high action-distinguishability and low learning value.

The main issue is load placement. The definition itself only needs action selection and interventional outcome distributions, but the discussion pulls in the unified policy objective, communication gain, structural adaptation, sector stability, adversarial destabilization, Section III topology/game-theoretic material, and an old appendix source. Those are not declared dependencies and several are well downstream. Also, "standard quantity" should probably be phrased as "standard KL construction over interventional distributions"; CIY as a named AAT quantity appears to be the framework's construct.

## Prompt pass

Predictions vs evidence: I expected an intervention-specific information measure. The segment gives a KL distinguishability measure and carefully compares it with EIG.

Cross-segment consistency: consistent with `der-action-selection` and the earlier Pearl-forward-reference explanation. It continues to use `do(a)` before the formal Pearl hierarchy segment, but locally explains the notation.

Math verification: KL nonnegativity supports `CIY >= 0`. `CIY=0` means the chosen action's modeled outcome distribution is indistinguishable from comparator-action distributions under `q`; it is model-relative and `q`-relative. The asymmetry of KL means the direction in the definition is part of the definition, not a neutral distance.

Direction next: `def-adaptive-tempo` should say whether CIY contributes to tempo directly, through gain-weighted update information, or only through exploration policy.

Errors to watch: treating high CIY as high learning value without uncertainty gating; comparing CIY values across different reference distributions `q`; treating model-predicted intervention distributions as true causal effects without an identifiability caveat.

What I would change: keep the definition plus a short CIY-vs-EIG caveat here, then move query/deception/Section III material to later communication or adversarial segments.

Curiosity: policy-induced `q` is pragmatic, but it makes CIY partly a measure of surprise relative to the agent's own action habits, not an intrinsic action property.

New knowledge enabled: exploration in this framework is moving toward "choose actions whose outcomes are distinguishable, then gate by uncertainty."

Audit process change: the diagram should be a distribution-comparison picture with a separate uncertainty gate to EIG-like value.

Value feel: medium-high. The definition is clear; the segment is overstuffed.

## Diagram thought

The simplest useful visual is three interventional outcome distributions. CIY is the KL from the chosen action's distribution to comparator distributions averaged over `q`. A second, separate gate labeled `U_M` should show why distinguishability only becomes learning value when the model is uncertain.
