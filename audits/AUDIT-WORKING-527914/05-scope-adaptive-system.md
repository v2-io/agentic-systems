# 05 - scope-adaptive-system

Segment: `01-aat-core/src/scope-adaptive-system.md` (`#scope-adaptive-system`)

Dependencies: `def-agent-environment`, `def-observation-function`, `def-chronica`, all read. Dependency-order check passes.

## Segment Read

This segment defines AAD's outer scope: systems with observations and residual uncertainty, whether or not they have causally efficacious action. Formally, the scope requires $\mathcal O \neq \emptyset$ and $H(\Omega_t \mid \mathcal C_t) \gt 0$. That makes Section I broader than common-sense agency: passive Bayesian learners and Kalman filters without control inputs qualify.

The key distinction is that "adaptive system" is the broadest uncertainty-and-update scope, while "agency" will be a later narrowing that adds Pearl-Level-2 causal action. This segment also names exclusions: closed-form systems and pure computation.

## Predictions Vs Evidence

I predicted Section I would explicitly separate adaptive systems from agentic/purposeful systems. This segment confirms it and makes the outer boundary sharper than I expected: observation plus residual uncertainty, not action, is enough.

My earlier watchpoint about perfect observation is handled cleanly here: systems with $H(\Omega_t \mid \mathcal C_t)=0$ are excluded because adaptation would be vacuous. That is consistent with `#def-agent-environment`.

## Cross-Segment Consistency

The residual uncertainty condition directly operationalizes the information-loss boundary. The segment uses chronica as the conditioning object, so the previous definition is already doing real work.

No contradiction. One phrase to monitor is "agent" in the formal set $\{(\text{Agent}, \Omega)\}$ even though passive observers are included. The segment is clear enough that "agent" here means the bounded entity from the agent-environment definition, not yet agency in the interventional sense.

## Naming Notes

`adaptive system` is the right outer-scope name. It is plain, familiar enough, and scope-honest: the system adapts under uncertainty but need not be purposeful or causally efficacious.

This segment also introduces possible names for exclusions. `Closed-form systems` is acceptable as a descriptive exclusion, but I do not yet know whether it is a target. `Pure computation` is ordinary and probably not a term needing special naming. `Passive observers` and `nominal agents` may matter when the agency segment arrives.

The main naming risk is collapsing "adaptive system" into "agentic system" too early. The framework needs the outer term to protect Section I's scope.

## What This Enables

This segment lets later results such as mismatch, update gain, adaptive tempo, and persistence apply to systems without action. It creates a useful two-step entry into agency: adaptation first, causal action second.

For naming, it gives the class ladder a stable base. If `adaptive system` is renamed, every later class description becomes harder.

## Watchlist

- Later prose using "agent" when it means "adaptive system."
- Candidate names that add goal, agency, or action connotations to this outer scope.
- Whether `nominal agent` gets a stable definition in the next segment or remains a passing phrase.

## Wandering Thoughts

The outer-scope move is important because it prevents the framework from needing every useful adaptive dynamic to be "agency." A Kalman filter can instantiate mismatch and gain without being an agent in the stronger causal or purposeful sense. That is a scope-honesty win.

Naming-wise, this is an argument for boring terms where the taxonomy is doing work. `Adaptive system` will not dazzle anyone, but it keeps the first class broad and clean. A more vivid name would probably smuggle in exactly the wrong restrictions.

The residual uncertainty condition is a nice bridge between information theory and ordinary language. "The environment is not fully determined by the chronica" is precise and intuitive: the system's past contact with the world does not exhaust the world's current state.

I also like that pure computation is explicitly outside scope. It will matter later for language agents, because an LLM session can look like pure computation unless the prompt/response loop is treated as environment contact. The name `logogenic` will need to sit on the right side of this boundary.
