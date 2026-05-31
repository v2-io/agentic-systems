# Reflection: emp-update-gain

## What the segment does

Defines the optimal update gain as $\eta^* = U_M / (U_M + U_o)$ — the uncertainty ratio. This is labeled as "empirical claim" at the robust-qualitative level (exact for linear-Gaussian/Kalman, robust-qualitative for general adaptive systems).

This is one of the most important segments in Section I — the gain principle is what makes the adaptive machinery *calibrated* rather than arbitrary.

## Naming targets surfaced

I don't see "update gain" as a direct voting target. But the tracker shows several related things:
- Row 34: "$f_M$ (event-driven update) | Epistemic update fu..." — related to how the update function is referred to
- Row 36: "$U_M$ as model uncertainty | Model uncertainty $..." — the $U_M$ symbol naming

Let me check row 36 in the card.

## The key insights from this segment

1. **Gain collapse** ("epistrophe failure"): When the agent incorrectly estimates $U_M \to 0$ (spurious confidence), $\eta^* \to 0$ and epistrophe ceases. Mismatches arrive but aren't used. This is a named failure mode — "gain collapse" — worth tracking.

2. **The epistemic opacity resolution**: The agent needs $U_o$ to compute optimal gain, but $U_o$ is not known (epistemic opacity). The resolution: the agent estimates both from the mismatch sequence itself. This is elegant — the gain becomes endogenous.

3. **Structural reset**: After structural change, $U_M$ should spike to enable rapid re-learning. An agent that doesn't reset gain after structural change will trust a stale model — "Boyd's incestuous amplification."

4. **Overfitting as gain miscalibration**: Gain too high → fits noise; gain too low → fails to correct genuine errors.

## The simulation validation

The segment includes specific simulation numbers: "Riccati-optimal gain reduced steady-state mismatch by 52% compared to fixed gain when observation noise was moderate." This is from track-b simulations. The mention of adversarial tempo advantage (0.40 vs 0.18) with optimal vs fixed gain is also specific.

These numbers support the "claims-verified" stage label. The quantitative validation is mentioned in the segment body, which is good epistemic practice.

## Naming targets: $U_M$ as model uncertainty

Row 36 in tracker: "$U_M$ as model uncertainty | Model uncertainty $..." — this is a symbol-to-prose alias target. The term "model uncertainty" is the natural English for $U_M$.

But wait — the CLAUDE.md mentioned "$U_M$ overload" as a concept (row 3 in the card): "The symbol overload region where $U_M$ means two different things." One meaning is model uncertainty in this segment; the other is something related to unity/epistemic unity. This is a naming-cycle concern worth flagging.

Let me check: in LEXICON.md, I saw "Unity dimensions ($U_M, U_O, U_\Sigma$)" as "Epistemic, teleological, and strategic coherence between agents." So $U_M$ is used for *both* model uncertainty in Section I *and* epistemic unity (coherence between agents) in Section III. This is a symbol collision.

## Wandering thoughts

The gain dynamics pattern — convergence (decreasing $\eta^*$ as confidence grows) followed by reset after structural change — is a natural learning rhythm. The challenge is detecting *when* to reset. The mismatch signal provides the diagnostic: persistent mismatch despite adequate gain suggests structural inadequacy rather than learning inadequacy.

"Boyd's incestuous amplification" is a great reference — in military doctrine, it describes the pathology where commanders amplify their own expectations rather than updating from reality. The AAD formalization makes this precise: it's gain failure after structural change.

The domain validation table is thorough. The Kalman filter row being "exact" is the anchor — it validates that the uncertainty ratio principle is not just an analogy but a generalization of a well-understood precise result. Everything else is then a weakened or approximated version.

The RL (Q-learning) row is notable: "Fixed learning rate $\alpha$ is a degenerate constant gain — does not adapt to uncertainty." This is a known weakness of fixed learning rates. The segment is honest that this is an approximation rather than an instance.

The LLM case: how does an LLM update its model? The context window acts as $M_t$, but in-context learning doesn't involve a parameter update — the "gain" is baked into the transformer architecture's attention mechanism. For actual fine-tuning, the learning rate is the $\eta$ analog. But the uncertainty ratio principle isn't explicitly used in either case. This is where the framework's reach becomes sketch-level for logogenic agents.

How valuable: 8/10 for surprise (the gain collapse failure mode and the epistemic opacity resolution discussion are more developed than I expected), 9/10 for load-bearing.
