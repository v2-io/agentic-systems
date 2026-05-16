# Reflection: scope-agency

**Segment:** `#scope-agency`

## What this does

Narrows to systems with at least binary choice AND at least one action with causal effect. The causal-effect condition uses Pearl's intervention operator — $P(o | do(a)) \neq P(o | do(a'))$ — which is exactly right because it distinguishes observational correlation from interventional contrast.

The "nominal agent" category is an important negative case: systems with binary choice but zero causal effect are nominally agents but can't benefit from Section II machinery.

## The naming question for "agency"

"Agency" is clean and correct here. The tracker row (#58) has no alternatives. "Agency" in this technical sense is the right word — it's the condition for having genuine causal effect through action, not just reactive adaptation.

## What strikes me as important

"Binary choice is necessary but not sufficient." This is the key precision. An agent that can do A or B but where A and B produce identical effects is epistemically equivalent to a passive observer. The causal-contrast condition is what makes agency meaningful.

This has implications for the "agency scope" vs. "adaptive scope" naming question throughout the framework: anywhere a segment claims something about "agents" it needs to be clear whether it means adaptive-scope or agency-scope. The scope lattice described in the OUTLINE preamble is load-bearing.

## Wandering thoughts

The scope-agency segment defines what I'd call the "Pearl threshold" — the minimum causal structure needed for the adaptive loop to generate interventional data. Below this threshold, the agent is stuck in Pearl Level 1 (associational learning); above it, the loop itself generates Level 2 data.

This connects directly to the "loop as causal engine" result later. The scope-agency condition is the *precondition* for that result — you need at least one genuinely causal action for the loop to supply Level 2 data at all.
