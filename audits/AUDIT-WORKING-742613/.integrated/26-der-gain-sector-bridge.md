# 26 — der-gain-sector-bridge

Dependencies checked: `emp-update-gain`, `def-mismatch-signal`, and `deriv-sector-condition` already read.
Declared dependency `deriv-gain-sector` is an Appendix derivation not yet read; applying the appendix-back-pointer exception and reading it next.

## Reflection

This segment is the bridge I expected: gain update plus directional fidelity implies the sector condition.
The bridge theorem itself is straightforward:

$$F(\delta)=\eta^\ast H g(\delta),\qquad \delta^T H g(\delta)\ge c\lVert\delta\rVert^2 \Rightarrow \delta^T F(\delta)\ge \eta^\ast c\lVert\delta\rVert^2.$$

That part is sound.

Likely issue to verify in the appendix:
The segment states an exact equivalence:

$$\text{GA-3 holds with }(\alpha,R)\iff L\text{ is locally }(\alpha/\eta)\text{-strongly convex on }\mathcal B_R(M^\ast).$$

This appears too strong.
For gradient dynamics, the one-point sector condition around the optimum,

$$\delta^T\nabla L(M^\ast+\delta)\ge\mu\lVert\delta\rVert^2,$$

is implied by strong convexity, but it is weaker than full local strong convexity / two-point strong monotonicity.
A radially inward gradient field can satisfy the one-point sector condition while the Hessian is negative in some directions away from the optimum.
I will check `deriv-gain-sector` before elevating this to a finding.

Other concerns:
- This segment cites `spikes/spike-a2-prime-strengthening.md` in Epistemic Status, outside Working Notes, which repeats the FORMAT provenance issue seen in `deriv-sector-condition`.
- The discrete-sector markdown link again points to `discrete-sector-condition.md` instead of `deriv-discrete-sector-condition.md`.
- The segment imports (PI), Čencov, `scope-agent-identity`, `disc-additive-coordinate-forcing`, and other downstream machinery inside Epistemic Status. Some of this may be justified as positioning, but it is dense for a main-chain bridge segment.

Score-sign issue:
The bridge uses abstract $g(\delta)$ and B1, so it is insulated from the score sign error if $g$ is defined correctly.
If `deriv-gain-sector` uses $\tilde\delta=-\nabla\log P$ as update direction, the sign error will propagate there.

Prediction for appendix:
It should prove Kalman, gradient, and simulation bridge cases.
I will focus on the gradient equivalence and any usage of score mismatch sign.

Running report update:
- Potential finding: one-point sector condition is not equivalent to local strong convexity; strong convexity is sufficient, not necessary.
