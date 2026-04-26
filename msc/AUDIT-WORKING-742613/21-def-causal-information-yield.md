# 21 — def-causal-information-yield

Dependencies checked: `def-pearl-causal-hierarchy`, `der-action-selection`, and `def-mismatch-signal` already read.

## Reflection

CIY is defined as expected KL divergence between interventional outcome distributions:

$$\operatorname{CIY}(a;M)=\mathbb E_{a'\sim q(\cdot\mid M)}\left[D_{\mathrm{KL}}\left(P(o\mid do(a),M)\Vert P(o\mid do(a'),M)\right)\right].$$

The segment is unusually honest about a possible confusion: CIY is action-distinguishability, not expected information gain.
That distinction matters and is well handled.

Status:
For a definition, `status: exact` is acceptable.
The learning-value relationship is explicitly labeled discussion-grade / heuristic.

Dependency propagation:
This segment depends on `der-action-selection`, so it inherits the $M$-only policy issue.
The reference distribution default $q(\cdot\mid M)=\pi(\cdot\mid M)$ is fine in Section I, but for actuated agents it probably needs $q(\cdot\mid M,G)$ or a continuation-policy convention.
This is not a separate finding; it is downstream evidence for candidate finding G.

Small formal caveat:
The claim "$\operatorname{CIY}=0$ for a passive observer" is a convention, because passive observers lack the action/comparator distribution needed for the definition.
Similarly, "$\operatorname{CIY}>0$ when actions causally alter what is observed" requires $q$ to put positive mass on alternatives whose distributions differ from $a$.
The segment later acknowledges dependence on $q$, so this is a minor precision issue.

Substantive note:
Query actions and deception are promising bridges to logogenic/composite agents, but the discussion is far ahead of formal Section III content.
Not a problem for a definition segment if treated as interpretation.

Prediction for next segment:
`def-adaptive-tempo` should combine event rate and gain.
I will check whether it uses event information $\mathcal I(e)$ or only $\nu\eta$, and whether "useful information acquisition" is measured by gain alone or requires CIY / sufficiency.

Running report update:
- CIY itself looks conceptually sound; it reinforces the `der-action-selection` $M$ vs $G$ scope issue.
