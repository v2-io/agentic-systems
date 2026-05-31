# 29 — result-sector-persistence-template

Appendix jump from `result-sector-condition-stability`.
Dependencies checked: `deriv-sector-condition` already read.

## Reflection

The template usefully factors a common Lyapunov structure across AAD's persistence-flavored results.
The deterministic Model D part inherits the sound A.1 argument.

The stochastic issue from `deriv-sector-condition` is repeated and amplified here.
The Formal Expression states:

> "Model S. The state satisfies $\mathbb E[\lVert\xi(t)\rVert^2]\to n\sigma_\xi^2/(2\alpha)$ in mean square..."

under a **local** sector condition on $\lVert\xi\rVert\le R$.
That convergence is true for the global linear OU case, or for a globally valid sector condition with appropriate stochastic stability assumptions.
It is not established by a local sector condition once nonzero Brownian noise can exit the local region.
The Epistemic Status explicitly says Model S inherits "stopped bound + non-exit probability"; the non-exit probability is the false part identified in `deriv-sector-condition`.

Candidate finding J extends to this template:
`result-sector-persistence-template` should not state unstopped mean-square convergence under only local T2 and Brownian disturbance.
Correct options:
- State the stopped bound only.
- Require global T2 for the unstopped mean-square bound.
- Replace Brownian noise with bounded stochastic disturbance if the goal is local-region invariance.
- Use finite-horizon exit probabilities rather than $P(\tau_R<\infty)$.
- Treat $R^\ast_S<R$ as a typical-scale condition, not a persistence guarantee.

This matters because the template is explicitly used to transfer stochastic persistence claims to strategic, team, composition, and adversarial segments.
If the template overstates Model S, every Model S instantiation inherits the overclaim.

Additional notation issue:
T3 says $w(t)$ is disturbance in the ODE but then says Model S has $w(t)$ "a Wiener-process increment."
For SDEs the disturbance term should be written as $\sigma_\xi dW_t$, not $w(t)$ inside an ordinary differential equation.
This is partly notational, but it contributes to the local-region confusion.

Order/priming issue:
The template enumerates six instantiations, many downstream and not yet read.
Because `result-sector-condition-stability` depends on this template, the appendix exception brought a large amount of future Section II/III content into the early Section I pass.
That may be unavoidable if the template is truly a proof dependency, but it suggests the template might belong after the instantiations or should be leaner when used as an early dependency.

Prediction after returning to main outline:
`result-persistence-condition` should instantiate the deterministic linear threshold.
I will check whether it uses Model S/local stochastic claims or stays deterministic.

Running report update:
- Finding J now covers both `deriv-sector-condition` and `result-sector-persistence-template`.
