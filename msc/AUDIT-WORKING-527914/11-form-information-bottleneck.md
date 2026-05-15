# 11 - form-information-bottleneck

Segment: `01-aat-core/src/form-information-bottleneck.md` (`#form-information-bottleneck`)

Dependencies: `form-agent-model`, `def-action-transition`, both read. Dependency-order check passes. The segment also references future segments for downstream use, but its applied-IB core is locally well-typed from chronica/model/action context.

## Segment Read

This segment binds Tishby's information bottleneck to AAD's model-compression problem: $\mathcal C_t$ is the source/history, $M_t$ is the compressed representation, and future observations conditioned on future actions are the relevance variable. The core is imported theorem, not novel AAD math.

The most useful local clarification is the $\beta$ vs $\rho$ distinction. Volatility already changes predictive mutual information through the joint distribution; changing $\beta$ should represent internal memory/computation cost, not environmental volatility. The segment also distinguishes canonical IB from the sibling information-theoretic MDP lineage used for strategy-cost compression.

## Predictions Vs Evidence

I expected IB to appear as the natural formalization of $M_t$ compression. That is confirmed. I did not expect the segment to already include a strong correction against the tempting "lower beta in high rho" story; that is a useful naming target candidate if present because the distinction prevents a common explanatory error.

## Cross-Segment Consistency

The segment sits directly on `#form-agent-model`: $M_t = \phi(\mathcal C_t)$ becomes an optimization over $\phi$. It is also consistent with `#def-action-transition` because future observations are conditioned on future actions.

One status note: frontmatter says `status: exact`, while the Epistemic Status paragraph says the IB-as-applied-theorem core is exact but the $\beta(\rho,\pi)$ dependence claims are robust-qualitative. That is probably acceptable if the segment's status is keyed to the core, but it creates a mixed-strength segment. FORMAT recommends derivation-audit tables for mixed-strength derivation segments; this is a formulation segment, so not required, but the naming target "Information Bottleneck" should not make the $\beta/\rho$ qualitative claims sound theorem-level.

## Naming Notes

`Information Bottleneck` should be kept. It is adopted prior art and directly names the method. AAD's contribution is the binding, not the term.

The phrase "IB lineage vs information-theoretic-MDP lineage" is precise but heavy. If a target asks about the sibling relationship, a prose alias like `rate-distortion sibling forms` might be tempting, but I should wait for strategy-cost segments.

The $\beta$ vs $\rho$ distinction might deserve a memorable warning name only if it recurs. As a local paragraph, "beta-volatility double-counting" would be understandable, but I do not yet know if the card has a target.

## What This Enables

This segment enables model sufficiency, shared compression operations, strategy complexity cost comparisons, and active-inference positioning. It also gives the framework a principled answer to "what does good compression mean?"

For naming, it reinforces the prior-art rule: keep external terms (`Information Bottleneck`, `rate-distortion`, `variational free energy`) rather than coining AAD-branded replacements.

## Watchlist

- Any candidate that renames `Information Bottleneck` rather than preserving prior-art attribution.
- Confusion between $\beta$ as internal cost preference and $\rho$ as environmental volatility.
- Claims that strategy-cost compression is "IB" without naming the different relevance-term shape.

## Wandering Thoughts

This segment feels like the first point where AAD's integration style becomes explicit. It does not need to prove IB; it needs to bind IB to its objects cleanly. That is a different kind of rigor from deriving a theorem. The naming should respect that by retaining the borrowed term.

The $\beta/\rho$ clarification is valuable because it blocks an appealing but wrong explanatory shortcut. In volatile environments, old history becomes less predictive through the data distribution itself. Tuning $\beta$ for volatility would count the same fact twice unless the agent's internal memory economics also changed.

The sibling-lineage distinction between IB and IT-MDP also shows why compression vocabulary can become dangerous. "Information bottleneck" is attractive as an umbrella, but decision-theoretic compression can have a KL-to-target-policy fidelity term instead of mutual information to an observable. Naming everything IB would flatten a real technical distinction.

For votes, I should mostly defend standard prior-art names here and avoid turning local warnings into grand terms unless the tracker shows an actual recurring concept.
