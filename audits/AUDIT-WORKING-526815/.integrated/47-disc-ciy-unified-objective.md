# 47 - disc-ciy-unified-objective

Source: `01-aat-core/src/disc-ciy-unified-objective.md`

## First-pass understanding

This segment presents the familiar exploration-exploitation form as value plus information: choose actions that score well under expected value while also producing causally distinctive observations. It is candid that scalar CIY is a surrogate for expected information gain, not EIG itself. The identifiability gate also carries forward the proxy segment's safety discipline: if action variation, admissibility regime, reference distribution, or stationarity fails, drop CIY or use a safer uncertainty heuristic.

The segment then says the scalar heuristic is superseded by an exact LMI-derived matrix form, `Q_O(a) + Tr(Lambda I_o(a))`, where Fisher information in relevant directions is priced by a survival-constraint shadow matrix. That is conceptually stronger than a scalar exploration bonus, but the proof-bearing derivation is elsewhere and has not been read yet under the AAT-only outline cadence.

## Diagram attempt

The helpful picture is two stacked objectives. The top is the scalar heuristic: value plus `lambda * CIY`, gated by identifiability. The lower layer is the claimed exact matrix form: value plus a directional trace product. Drawing both makes the status drift visible: the scalar form is useful vocabulary, but the exact claim belongs to the LMI/tensor version.

## Findings and watches

- Candidate finding: the Formal Expression still displays the older scalar shorthand `E[value(a) | M_t] + lambda(M_t) CIY_q(a;M_t)`, while `def-value-object` provides `Q_O` and argues that exploration pricing depends on `(M_t,O_t,N_h)`, and this segment's own Epistemic Status says the scalar form is superseded by the tensor trace-product. The segment should either make the scalar expression explicitly historical/heuristic or promote the `Q_O`/matrix form into the displayed formal expression.
- Candidate finding: the domain table overstates several "lambda reduces to" entries. A Gittins index is an action index/value in a discounted bandit, not simply the scalar weight `lambda`; information-directed sampling minimizes a regret-squared/information ratio, not a direct additive `lambda * CIY` term. These may be analogies, but "exactly derived" is too strong without a mapping.
- Watch: the survival-imperative claim `lambda_surv -> infinity as U_M -> 0` is proof-bearing but delegated to future derivations. Until those are read, this is a strong forward claim rather than established local support.
- Watch: the scalar CIY term can still be directionally wrong under the blank-wall problem; the segment says the matrix LMI fixes this. Later segments must preserve the matrix/directional caveat when making concise summary claims.

## Local verdict

The exploration-exploitation split is useful as a discussion layer, and the identifiability gate is good. The file should be clearer about which objective is the heuristic teaching form and which objective is the theorem-grade object.
