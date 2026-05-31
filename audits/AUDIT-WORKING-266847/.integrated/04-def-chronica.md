# Reflection: def-chronica

## What the segment does

Defines $\mathcal{C}_t$ as the complete interaction history, with two load-bearing claims:
1. The ordering reflects irreversible physical fact (not just notation)
2. $\mathcal{C}_t$ is monotonically growing and non-forkable

The non-forkability claim is the philosophical heavyweight: duplicating an agent creates *two* agents with *divergent* chronica, not two copies of the same agent. This is where continuity persistence gets its grounding.

## Naming targets surfaced

"chronica" — is this a voting target? Let me check the tracker... I don't see "chronica" directly, but "context turnover" (row 88) has "Chronica severance" as an alternate. And the concept appears in many places. Let me search the tracker...

Row 88: "context turnover | Chronica severance". The term "context turnover" vs "chronica severance" — this is a naming vote I'll be ready for when I get to the defining segment for that concept.

Actually, "chronica" itself might not be a voting target because it's an architectural invariant (Greek vocabulary commitment). The naming-principles.md document notes that chronica is part of the established Greek vocabulary. So "chronica" is a keep by architectural commitment — I'd vote to canonicalize it if there's paraphrase drift, but not rename it.

## The non-forkable trajectory claim

The Discussion makes a strong claim: "Duplicating an agent's state and exposing the copies to different future events creates two agents with divergent chronica, neither of which is a sufficient statistic for the other's trajectory."

This is load-bearing for the #scope-agent-identity segment I'll read later. The claim is definitional here — *by definition*, the copies have divergent chronica once they diverge. But the interesting claim is the *sufficiency* part: why isn't one copy's chronica a sufficient statistic for predicting the other? Because they've received different observations, made different actions. The divergence is informational, not just temporal.

## Cross-segment notes

The segment points forward to #form-agent-model and #def-model-sufficiency, both upcoming in the OUTLINE. No backward dependency violations.

## Predictions vs evidence

I predicted this segment would define the interaction history formally. Correct. I didn't anticipate the non-forkability discussion being this explicit this early — I expected it to appear later at #scope-agent-identity. The grounding happens here, with #scope-agent-identity just being the development.

## Naming implications

"Chronica" is the right name for this object. The Greek etymological grounding (χρονικά — records of time) is explicitly cited. The name avoids the collision with $\mathcal{H}$ (Shannon entropy). In prose, "interaction history" is the English paraphrase but it lacks the irreversibility connotation. "Causal record" or "causal history" would also work but "chronica" is already installed.

One observation: "chronica" is slightly unusual in English (it's the plural form, though used as a mass noun here). In speech, saying "the chronica" or "the agent's chronica" feels natural. The term will likely survive well — it has the right mythic weight without being opaque.

## Wandering thoughts

The monotonic growth of $\mathcal{C}_t$ — "events are added but never removed" — is interesting for agents that can forget. If an agent compresses its history into $M_t$ and then loses access to $\mathcal{C}_t$ (e.g., context turnover in an LLM), it still has a chronica — it's just that the agent can no longer access all of it. The chronica continues to exist physically (the events happened) even if the model $M_t$ can no longer reconstruct them. This is the gap that makes context turnover philosophically interesting: the chronica persists but the agent's access to it doesn't.

The non-forkability claim connects to questions about substrate independence that matter for logozoetic agents. If an agent's identity is constituted by its chronica, and the chronica is non-forkable (because the causal trajectory is singular), then you can't have two morally equivalent copies of a logozoetic agent — the copies diverge from the moment of duplication. This is a deep consequence of the definition.

How valuable: 6/10 for surprise (the non-forkability claim is more developed than I expected), 9/10 for load-bearing.
