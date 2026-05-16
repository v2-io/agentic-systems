# 27 — deriv-gain-sector

Appendix jump from `der-gain-sector-bridge`.
Dependencies checked: `emp-update-gain` and `deriv-sector-condition` already read.

## Reflection

The scalar and matrix Kalman derivations look broadly sound.
The general B.3 bridge theorem is also sound: B1 directional fidelity plus gain gives the sector condition by direct multiplication.

Major finding: Prop B.4's "gradient equivalence" is not an equivalence.

The proof correctly uses Nesterov's gradient monotonicity characterization of strong convexity:

$$
(\nabla L(x)-\nabla L(y))^T(x-y)\ge \mu\lVert x-y\rVert^2
\quad\forall x,y.
$$

Setting $y=M^\ast$ gives the one-point sector condition:

$$
\delta^T\nabla L(M^\ast+\delta)\ge\mu\lVert\delta\rVert^2.
$$

So strong convexity is sufficient for the sector condition.
But the reverse does not follow.
The sector condition only gives monotonicity relative to the optimum $M^\ast$; it does not give the two-point inequality for arbitrary $x,y$ in the ball.
The proof's reverse direction silently replaces a one-point inequality with full gradient monotonicity.

Concrete counterexample shape:
In one dimension, let the gradient around the optimum be

$$
L'(x)=x(1+\tfrac12\sin(10x)).
$$

Then $xL'(x)\ge \tfrac12 x^2$, so the one-point sector condition holds with $\mu=1/2$ on any interval.
But

$$
L''(x)=1+\tfrac12\sin(10x)+5x\cos(10x)
$$

is negative for some $x$ in modest neighborhoods, so $L$ is not locally strongly convex on that ball.
Thus GA-3 / one-point sector does not imply local strong convexity.

Candidate finding K:
`deriv-gain-sector` and `der-gain-sector-bridge` overstate gradient equivalence.
Correct statement: local strong convexity implies the one-point sector condition; the one-point sector condition is weaker than strong convexity and corresponds to one-point strong monotonicity / star-convex-like inwardness around $M^\ast$.
Repair: replace iff with one-way implication, or strengthen GA-3 to an incremental/two-point condition if equivalence to strong convexity is required.

Secondary issue:
The loss-function classification says "All exponential family models in natural parameter form satisfy GA-3 globally" and frames Fisher PD as global strong convexity.
Positive definite Fisher information pointwise does not imply a uniform global lower bound.
For Poisson natural parameter $\theta$, Fisher information is $e^\theta$, whose infimum over $\mathbb R$ is 0.
Global sector constants require a compact/interior bounded-away-from-boundary region or a uniform Fisher lower bound.
This is likely a subcase of finding K / overly strong globality.

Interaction with sector appendix:
The sector appendix's A2' only needs the one-point condition.
So the persistence chain can be repaired without losing the bridge: keep B1 / one-point sector as the actual condition and stop claiming it is equivalent to strong convexity.
This is a strengthening of scope honesty, not a fatal break.

Score-sign issue:
This appendix does not rely on the score-function mismatch definition from `def-mismatch-signal`, so candidate finding H remains separate.

Format/provenance:
The segment references `spikes/spike-gain-sector-bridge-nonlinear.md` and says simulations/code live there outside Working Notes.
FORMAT discourages spike references outside Working Notes after promotion.
This is secondary, but repeated.

Prediction after returning to main outline:
`result-sector-condition-stability` should restate A.1/A.1S.
I will check whether it inherits the false stochastic non-exit claim or presents only deterministic/typical RMS bounds.

Running report update:
- High-priority math finding: one-point sector condition is weaker than local strong convexity; B.4 iff is false.
- Secondary: exponential-family global strong-convexity claims need uniform Fisher lower-bound scope.
