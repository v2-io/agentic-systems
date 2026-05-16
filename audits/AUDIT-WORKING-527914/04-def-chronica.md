# 04 - def-chronica

Segment: `01-aat-core/src/def-chronica.md` (`#def-chronica`)

Dependencies: `def-agent-environment`, `def-observation-function`, `def-action-transition`, all read. Dependency-order check passes.

## Segment Read

This segment defines $\mathcal C_t$ as the complete ordered interaction history of observations and actions. The term is not just a synonym for history; it names the singular, irreversible causal record from which the model must be constructed. The sequence's order matters because actions precede later observations; the agent cannot condition past actions on future observations.

The segment also explicitly links chronica to continuity persistence and non-forkability: copied states exposed to divergent future events produce divergent agents because their chronica no longer match. That gives the term a conceptual reach beyond bookkeeping.

## Predictions Vs Evidence

I predicted `chronica` would be a high-cost, likely keep term. This segment strengthens that prediction. The term earns its Greek register because it is both a formal object and a continuity/identity anchor. It avoids the `H` collision with entropy and gives the project a memorable noun for something "complete interaction history" cannot carry in conversation.

## Cross-Segment Consistency

The sequence is built out of the two previous primitives: observations from $h$ and actions through $T$. The first segment's information-loss boundary explains why the chronica is the only raw material; the agent never has direct access to $\Omega_t$.

No contradiction. The sequence notation in the segment is $(o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)`, while `NOTATION.md` had $(o_1, a_1, \ldots, a_{t-1}, o_t)`. The content is consistent; no issue.

## Naming Notes

`chronica` is probably one of the project's strongest invented/adopted terms. It passes the communal-imagination test: a reader can say "the agent's chronica forks" or "the committed chronica exteriorizes part of the history" without re-expanding the definition.

The best alias is not a replacement but a gloss: "complete interaction history." It should be used at first mention and perhaps in brief educational contexts, but it should not displace `chronica`. `Interaction history` alone is too weak because it loses singularity, irreversibility, and non-forkability.

This segment also gives me a stronger basis to vote on targets for `chronica brief gloss` or `complete interaction history` if they exist. The canonical structure should be: `chronica` as the name; `complete interaction history` as the first-use gloss.

## What This Enables

Chronica enables model compression $M_t = \phi(\mathcal C_t)$, model sufficiency, continuity persistence, and later software/logogenic claims about context turnover and external memory. It is also a natural bridge to TST's committed-state subset, where git history can exteriorize part of $\mathcal C_t$.

For naming, it establishes a pattern: Greek-root noun for a core AAD object, English gloss for pedagogical entry, symbol for formal reference. That three-layer pattern may be the right way to judge several targets.

## Watchlist

- Later uses that treat copied agent state as identity-preserving without chronica continuity.
- Any target trying to replace `chronica` with "history" or "record" in canonical prose.
- Whether `committed chronica` in TST correctly names a subset rather than a second kind of chronica.

## Wandering Thoughts

`Chronica` has the rare property that it starts slightly unfamiliar and becomes useful almost immediately. The term creates a place to put non-forkability, irreversible order, and identity continuity without overloading "history." That is exactly the kind of invented vocabulary this framework should keep.

The phrase "everything the agent can ever know must be constructed from this sequence" is doing deep work. It turns epistemology into chronology: knowledge is not just representation, it is representation compressed from a non-repeatable causal past. That connection is likely why the term resonates more than a neutral label would.

There is also a strong relation to the audit method I am following. These reflections are a miniature chronica of my reading. They are not interchangeable with a final summary because the order of contact matters: I cannot honestly claim the same state after reading future segments as I had here. The method's insistence on one segment at a time is not arbitrary; it preserves the causal trace of understanding.

For votes, this is a good place to be protective. Replacing `chronica` would not just change a word; it would flatten a conceptual affordance. The right naming work is probably to standardize its glosses and subsets.
