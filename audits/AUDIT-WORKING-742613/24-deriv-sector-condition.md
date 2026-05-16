# 24 — deriv-sector-condition

Appendix jump from `hyp-mismatch-dynamics`.
Dependencies checked: `def-adaptive-tempo` and `def-mismatch-signal` already read.

## Reflection

This appendix proves the sector-condition Lyapunov bounds and introduces deterministic Model D and stochastic Model S.
The deterministic Lyapunov proof (Prop A.1) looks sound under local A2', bounded disturbance, and initial condition inside $\mathcal B_R$.
The adaptive reserve formula $\Delta\rho^\ast=\alpha R-\rho$ is a direct corollary and checks out.

Major stochastic finding:
Prop A.1S's stopped mean-square bound is plausible, but the segment then converts a fixed-time / stationary Markov tail bound into a bound on the probability of ever exiting $\mathcal B_R$:

> "at steady state the Markov tail bound gives $P(\tau_R \lt \infty) \leq n\sigma_w^2/(2\alpha R^2)$"

This is not correct.
For the linear scalar case inside the appendix's own scope,

$$d\delta=-\alpha\delta\,dt+\sigma_w\,dW_t,$$

the Ornstein-Uhlenbeck process has a stationary Gaussian distribution with unbounded support.
For any finite $R$ and nonzero $\sigma_w$, the process will eventually exit $[-R,R]$ with probability 1 over an infinite horizon.
So $P(\tau_R<\infty)=1$, while the claimed bound can be made arbitrarily small by taking $\alpha R^2\gg\sigma_w^2$.
The Markov inequality bounds $P(\lVert\delta(t)\rVert>R)$ at a fixed time, not the probability of ever exiting over an infinite time horizon.

Candidate finding J:
`deriv-sector-condition`'s Prop A.1S non-exit probability and the associated claim that the unstopped bound holds "with the same right-hand side up to a higher-order correction" are mathematically false for nondegenerate Brownian noise in a finite sector region.
The stopped bound can remain; the non-exit / infinite-horizon local-region guarantee needs to be replaced with finite-horizon exit probability, fixed-time tail bounds, global-sector assumptions, bounded-noise stochastic models, reflecting/truncated noise, or a statement that Model S persistence is mean-square typical-scale rather than almost-sure non-exit from $\mathcal B_R$.

This is high-impact because `hyp-mismatch-dynamics` cites Prop A.1S for stochastic steady-state scaling and region-aware justification, and downstream adversarial exponent regimes may use the stochastic persistence condition.
The $1/\sqrt{\alpha}$ RMS scaling remains correct for global linear OU; what fails is using RMS-inside-$R$ to claim low or bounded probability of ever leaving the local validity region over infinite time.

Additional process/format issue:
The Epistemic Status cites `spikes/spike-a2-prime-strengthening.md` outside Working Notes.
FORMAT says spike references belong only in Working Notes and only for unfinished work / landing context.
This is not theory-breaking, but it is a format/provenance violation in a load-bearing appendix.

Dependency/order:
The appendix contains extensive claims about `der-gain-sector-bridge`, `form-composition-closure`, `result-contraction-template`, `disc-identifiability-floor`, `disc-additive-coordinate-forcing`, and operator-theoretic classes that are not declared dependencies.
Some are contextual positioning, but the A2' grounding in sub-scope $\alpha$ explicitly relies on `der-gain-sector-bridge`, which appears later in the main outline.
If this appendix is read as a proof dependency for `hyp-mismatch-dynamics`, then a reader gets a large amount of future machinery out of order.
This may be another instance of front-loaded integration.

Interaction with score-sign issue:
The abstract sector condition $\delta^T F\ge\alpha\lVert\delta\rVert^2$ does not itself use the score mismatch sign.
However, the claimed derivation of A2' from gain-based / gradient updates in `der-gain-sector-bridge` likely will.
I need to check that bridge.

Prediction after returning to main outline:
`der-deliberation-cost` should use tempo/gain tradeoffs.
I will watch whether it relies on deterministic linear mismatch or sector bounds.

Running report update:
- High-priority math finding: Prop A.1S confuses fixed-time tail probability with ever-exit probability for stochastic processes.
