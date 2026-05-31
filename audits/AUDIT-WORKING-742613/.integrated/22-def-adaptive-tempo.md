# 22 — def-adaptive-tempo

Dependencies checked: `emp-update-gain` and `form-event-driven-dynamics` already read.

## Reflection

Adaptive tempo is defined as:

$$\mathcal T=\sum_k\nu^{(k)}\eta^{(k)\ast}.$$

This is central to the framework, but the segment itself reveals that the formal expression is not generally exact:

- The channel-independence discussion says additive tempo overcounts when channels are correlated and is only an upper bound without independence.
- The scalar-vs-vector discussion says scalar tempo overestimates adaptation in anisotropic systems and per-dimension persistence is required.

Candidate finding I:
`def-adaptive-tempo` has `status: exact` and presents the additive scalar formula as the definition of effective useful-information rate, but its own Discussion states conditions under which that formula overcounts.
Repair: make the Formal Expression conditional ("under channel independence and scalar/isotropic reduction"), define $\mathcal T_{\text{add}}$ as an upper-bound / nominal tempo, or move the caveats into Epistemic Status and set `status: conditional`.

This is likely important because `result-persistence-condition`, adversarial advantage, and composition use $\mathcal T$ downstream.
If downstream results rely on scalar additive tempo without repeating independence/isotropy assumptions, margins will be overestimated.

Status:
The segment says "definition itself is not a truth-claim," but if a definition is advertised as "effective rate" and then shown to overcount, it is not merely a naming choice.
It is a conditional operationalization.

Substantive nuance:
The "speed-quality substitutability" statement is true only within the same information direction / channel independence regime.
A fast redundant channel cannot substitute for a slow nonredundant channel; a high-gain channel in the wrong dimension cannot substitute for low gain in the bottleneck dimension.

Prediction for next segment:
`hyp-mismatch-dynamics` should use $\mathcal T$ in an ODE.
I will watch whether it carries independence/isotropy and fluid-limit caveats, because this is where the additive tempo definition begins doing mathematical work.

Running report update:
- Candidate finding: adaptive tempo definition is exact only under independence/isotropy but frontmatter/formal expression present it unconditionally.
