# Reflection: emp-update-gain

**Segment:** `#emp-update-gain`

## What this does

The update gain formula: η* = U_M / (U_M + U_o). One of the most iconic results in the framework.

Epistemic status: exact for linear-Gaussian/conjugate Bayesian; robust-qualitative otherwise. This is appropriately calibrated — the Kalman gain is literally this ratio.

## Naming relevance

Tracker row 293: "update gain" vs alternatives. I already voted from orientation; this segment confirms that vote.

"Update gain" is correct. The segment confirms: this is Kalman gain in the linear-Gaussian case. The "learning rate" alternative would create false familiarity with SGD. "Epistemic gain" would collide with "epistemic unity."

Additional confirmation: the segment's own equation label uses "uncertainty-ratio-principle" as the informal name. That's a good Brief-field gloss but not the primary name.

## New naming target surfaced: gain collapse

The Discussion's "gain collapse — epistrophe failure" section surfaces a clear concept. Tracker row 87 has many candidates. Now that I've read the defining context:

- "Gain collapse" is the right primary name — the mechanism is clear (gain collapses to 0), and the segment already uses this phrase.
- "Certainty trap" is the best alternative — more evocative for prose.
- "Epistemic gridlock" and "competency trap" are vivid but misleading (gridlock implies deadlock from competing forces; competency trap imports the wrong connotations).
- The two-mode distinction (dogmatism: low U_M → η → 0; nihilism: high U_o → η → 0) should be preserved in whatever name or alias pair gets adopted.

Voter note: the segment calls this a "gain collapse" but doesn't formally name it as such — it says "Gain collapse — epistrophe failure" as a Discussion subheading. The naming is excavated from prose rather than formally coined.

## What's excellent here

The "representation note" at the end: "The additive form operates in a representation space appropriate to the model." This is critical for the coordinate-forcing meta-segment — the update rule is only cleanly additive in the right coordinate system (natural parameter space for exponential families, log-probability for Bayesian updates, etc.). This connects to `#disc-additive-coordinate-forcing`.

## Wandering thoughts

The domain validation table is good epistemic work. The RL case being "approximate" because α doesn't adapt is honest — advanced RL methods (Adam, Bayesian RL) converge toward the optimal form, which is exactly what "robust qualitative" means. The framework is being correctly calibrated about its own precision.

The open question about "non-parametric models: for neural networks without well-defined scalar U_M" is important. This is where the framework meets its calibration-laboratory limit — software has explicit uncertainty estimates, neural networks don't by default. The logogenic agents extension will need to address this.

The connection to adaptive tempo (T = ν · η*) is important: high event rate but low gain = fast but correction-less cycle. This parallels the "turning" metaphor of epistrophe beautifully — you can observe without turning toward what you see.
