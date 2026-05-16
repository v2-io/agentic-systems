# Reflection: def-mismatch-signal

**Segment:** `#def-mismatch-signal`

## What this does

Formally defines mismatch as prediction error δ_t = o_t - ô_t, plus a generalization to score-function mismatch for probabilistic models.

The "zero-aporia ambiguity" Discussion is excellent and important — δ_t ≈ 0 can mean model adequacy OR confirmation bias OR channel blindness. This distinction is load-bearing for active testing and CIY.

## Naming relevance

Tracker row 36: "mismatch signal" vs "Aporia signal."

The segment's title is "Mismatch Signal" and the text calls it "the formal expression of *aporia*." The aporia connection is real and the segment honors it. But "aporia signal" as the formal name would collide with "aporia" as the cycle phase name — you'd have aporia (the phase) and the aporia signal (the quantity generated in that phase), which is a naming collision rather than a naming economy.

The variational mismatch $\tilde\delta_t$ in the score-function generalization is a separate tracker target (row 39). That row's candidate is "variational aporia" — which would differentiate the two forms using the Greek term. I'll need to read that separately.

My vote: strong keep on "mismatch signal." "Aporia signal" is a tempting alignment with the Greek vocabulary but creates a phase/signal collision that would confuse readers.

## The "gain collapse" concept surfaced here

The Discussion introduces "gain collapse — epistrophe failure" as a phenomenon name: when η → 0, epistrophe ceases. This is the concept named in tracker row 87 ("[Concept] The failure mode where η → 0 freezes learning in either of two distinguishable modes"). The Discussion gives me enough to vote on that cluster now.

"Gain collapse" is the right name — it's mechanistic (gain → 0 = collapse), it has two distinguishable modes (low U_M → spurious confidence; high U_o → sensor distrust), and it matches the language already in the segment. The alternatives in the tracker (epistemic gridlock, certainty trap, competency trap, etc.) are vivid but less precise.

## Wandering thoughts

The "resolution of epistemic opacity" note is philosophically important: the agent can't know U_o directly (that would violate the opacity axiom), so it estimates from the statistics of its own mismatch sequence. This is the bootstrap mechanism for adaptive gain — the agent estimates its own calibration from experience. This is a beautiful self-referential feature of the framework.

The domain validation table is good evidence for the "robust-qualitative" epistemic status. Exact for Kalman and conjugate Bayesian; approximate for RL; structural analogy for software development. The gradient of precision is honest and appropriate.
