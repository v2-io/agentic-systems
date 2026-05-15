# 10 - form-agent-model

Segment: `01-aat-core/src/form-agent-model.md` (`#form-agent-model`)

Dependencies: `def-agent-environment`, `def-observation-function`, `def-chronica`, all read. Dependency-order check passes.

## Segment Read

This segment formulates the agent's model as $M_t = \phi(\mathcal C_t)$: a compressed representation of retained interaction history. The title uses "The Reality Model," and the discussion calls $M_t$ the epistemic substate. The formulation is explicitly a modeling choice, not a theorem; history-based policies could be described without a separate model state, but AAD commits to $M_t$ for analytical tractability.

The main conceptual move is completeness: $M_t$ contains everything retained from the chronica. Information not in $M_t$ is lost to the agent. Model sufficiency will later ask whether the retained compression is good enough.

## Predictions Vs Evidence

I predicted that $M_t$ would need careful aliasing because "model" is generic. The segment confirms this: "reality model" and "epistemic substate" both appear, and they do different work. "Reality model" is the intuitive prose name; "epistemic substate" is the structural role once $G_t$ exists.

The segment also fits my expected pattern: chronica is raw causal record; $M_t$ is compression; sufficiency measures retained predictive information.

## Cross-Segment Consistency

This is the first direct use of chronica as input to a formal mapping. It remains consistent with the earlier complete-history definition.

One possible issue: the degenerate PID discussion says the PID's $M_t$ is too impoverished to support the adaptive dynamics of Section I, but earlier `#scope-adaptive-system` included Kalman filters and passive learners and excluded pure computation. This is probably fine because "too impoverished" means the full adaptive dynamics are limited, not that no Section I machinery applies. I will watch how the agent spectrum handles blind pursuers.

## Naming Notes

`Reality model` is a strong prose alias for $M_t$. It is more self-descriptive than "agent model," which can mean a model *of* an agent. The segment title makes this choice directly.

`Epistemic substate` is also worth keeping, but only in the later complete-agent-state context where it contrasts with purposeful substate. From this segment alone, I would not replace "reality model" with "epistemic substate"; they are different layers.

`Agent model` as a slug subject-noun is potentially ambiguous. The segment's current slug is `form-agent-model`, but the title says "Reality Model." If a target asks for `$M_t$`, I will likely prefer `Reality model` as the canonical prose alias.

## What This Enables

This enables information bottleneck, model sufficiency, mismatch, recursive update, action selection, and the later $X_t=(M_t,G_t)$ split. It also gives TST/logogenic work a clear place to talk about context windows and memory stores as model-state realizations.

For naming, it creates a useful two-layer convention: `$M_t$` in math, `reality model` in ordinary prose, `epistemic substate` when contrasting against goal/strategy state.

## Watchlist

- Candidates that call $M_t$ "world model" vs "reality model"; both are plausible, but "reality model" matches this segment.
- Whether "agent model" causes ambiguity with a model of the agent rather than the agent's model.
- Later use of "epistemic state/substate" before the complete-agent-state split is defined.

## Wandering Thoughts

This segment gives the framework its first compression architecture: chronica is too large and too literal to act from, so the agent carries a compressed state. That feels fundamental to the whole project. The question becomes not whether the model is true, but whether the compression retains what future action needs.

`Reality model` is plain in a good way. "World model" has machine-learning baggage and can sound like a learned simulator; "belief state" has POMDP/Bayesian baggage and can sound distributional; "epistemic state" is technically good but less accessible. "Reality model" tells a reader what $M_t$ is for.

The formulation-choice honesty is important. AAD is not pretending every agent literally implements an object called $M_t$. It is saying analysis becomes possible if retained history is represented as a state. That is the right kind of abstraction: useful, broad, but not over-derived.

This also sharpens my sense of logozoetic continuity: if identity lives partly in chronica and partly in compression of chronica into $M_t$, then context turnover is not just memory loss. It is a break in the compression pipeline from causal record to present self.
