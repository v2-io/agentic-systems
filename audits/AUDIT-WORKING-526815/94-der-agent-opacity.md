# 94 - der-agent-opacity

Source: `01-aat-core/src/der-agent-opacity.md`

## First-pass understanding

This segment introduces backward predictive uncertainty `H_b^{A|B}` as observer-indexed action unpredictability: how well observer `B` can predict agent `A`'s future action. The most useful conceptual move is directional: low opacity helps cooperation because allies can coordinate, while high attacker opacity helps adversarial action because the target cannot neutralize what it cannot anticipate.

The segment also explains the earlier apparent opacity conflict. There are two directions: `H_b^{A|B}` is attacker opacity to target, while `H_b^{B|A}` is target opacity to attacker. High attacker opacity can help the attacker; high target opacity can hurt the attacker's targeting. The formalism needs to keep those directions separate and avoid compressing them into a single scalar "opacity helps/hurts."

## Diagram attempt

I drew `H_b` as a directed observer channel from `A`'s future action to `B`'s filtration. The same channel feeds opposite value stories depending on coupling sign, while a second directed channel captures target opacity to attacker. The diagram flags the entropy/normalization and multiplier assumptions.

## Findings and watches

- F246 candidate: `H_b = H(a_{A,t+tau} | F_B^t)` needs an action-space convention. For continuous actions, differential entropy is not coordinate-invariant and can be negative; parameterization-invariance and `H_b^max` normalization require discrete/quantized actions or a reference measure.
- F247 candidate: the reduction from `H_b^{A|B}(t,tau)` to Hafez's `H(S,A | S')` under IDT + ergodicity is not "direct substitution" as written. Future-action entropy conditional on an observer filtration and backward state-action entropy conditional on next state are different conditionings unless an explicit time-reversal/observer model equates them.
- F248 candidate: calling `H_b` the formal dual of observation quality `U_o` is stronger than shown. They are opposite-direction information quantities, but a mathematical duality needs a shared channel/operator relation or adjoint construction.
- F249 soft candidate: cooperative effectiveness decreasing in `H_b` is plausible for coordination, but not universal. An ally can reduce disturbance by acting independently in a delegated region without being action-legible to the receiver at each horizon.
- F250 candidate: `T_A^effective = T_A * H_b/H_b^max` makes low-opacity adversarial tempo vanish. Predictable adversarial actions can still impose disturbance; opacity should modulate coupling effectiveness or neutralization probability, not necessarily multiply all adversarial tempo to zero.
- F251 candidate: the bilateral opacity ratio `(H_b^{A|B}/H_b^{B|A})^2` can become singular when the denominator is near zero and assumes both agents' opacity enters symmetrically through the same multiplicative channel. It needs floors/saturation and a direction-specific coupling model.
- F252 candidate: the emitter-side four-regime classification is a formulation, not a derivation parallel to the recipient regimes. The segment does not yet give boundary inequalities comparable to sector/model/observability tests.
- F253 candidate: the 16-cell emitter-recipient "closed-form arg-max" is under-specified. A product of opacity-to-target and vulnerability-to-shock is a plausible score, but closed-form targeting needs edge utilities, constraints, and regime-transition probabilities.
- F254 candidate: saying this segment "closes" the `adversarial-edge-targeting` GAP is too strong unless that GAP is replaced by an actual source segment or formal optimization result.
- F255 soft candidate: the claim that Class 3 Coupled agents have high structural opacity is architecture-plausible but not guaranteed; a coupled agent can be externally predictable if policy/output dynamics are simple or heavily instrumented.
- F256 watch: Hafez/IDT empirical numbers support monitoring feasibility, not by themselves the AAT claims about Level-2 access, low-`H_b` sidecars, or opacity-sign coupling.
- F257 watch: keep attacker opacity `H_b^{A|B}` distinct from target opacity `H_b^{B|A}`. Earlier segments use both directions in different roles; conflating them creates sign errors.
- F258 watch: the source's embedded search log is useful provenance, but final audit novelty claims should distinguish searched/confirmed prior art from intuition-only search notes.

## Local verdict

The observer-indexed opacity idea is valuable, especially once directionality is explicit. The formulas need action-space entropy conventions, a careful Hafez-reduction proof, and a less brittle coupling model than raw multiplication by `H_b/H_b^max`.

