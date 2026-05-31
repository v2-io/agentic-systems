# 88 - der-team-persistence

Source: `01-aat-core/src/der-team-persistence.md`

## First-pass understanding

This segment formalizes the consultant/employee distinction from the intro. Communication from allies contributes to the receiver's tempo; allied action contributes by reducing the receiver's effective disturbance. The file is careful about two issues I had just flagged: additive communication tempo is explicitly an upper bound under independence/nonredundancy, and negative disturbance is repaired with `rho_i^eff = max(rho_i, 0)`.

The main remaining burden is the tempo-to-correction bridge. The segment defines distributed tempo `T_i`, but the persistence inequality is written as `rho_i^eff / alpha_i < R_i`. It says communication-improved tempo can increase `alpha_i`, but the conversion from event/gain tempo to sector correction rate is inherited from earlier unresolved alpha/tempo conventions.

## Diagram attempt

I drew the result as two ledgers feeding the persistence test. Direct observation plus communication builds `T_i`; environment, adversarial action, and cooperative action build `rho_i^eff`. A dashed bridge from `T_i` to `alpha_i` marks the remaining assumption: the team formula needs the same rate-normalization convention as the single-agent sector bridge.

## Findings and watches

- F182 resolved locally: the intro-level negative-disturbance concern is handled here by `rho_i^eff = max(rho_i, 0)`. The intro should either point to this convention or avoid presenting raw `rho_i` as an unconstrained disturbance rate.
- F189 candidate: the formal persistence condition uses `alpha_i`, while the new multi-agent machinery defines distributed tempo `T_i`. The segment needs an explicit bridge from `T_i` and communication gains to sector correction rate `alpha_i`, inheriting the earlier alpha/tempo normalization issue.
- F190 candidate: the coupling coefficients `gamma_adv` and `gamma_coop` need units and scale conventions. Since `gamma T_j` is added to/subtracted from `rho_i`, `gamma` must convert another agent's tempo into receiver disturbance rate on the same normed mismatch scale.
- F191 soft candidate: "a single cooperative event contributes through one channel or the other, not both" is too categorical for events with both causal and informational effects. The safer rule is causal allocation/no double counting: decompose the event into non-overlapping informational and environmental-intervention effects.
- F192 candidate: the coordination threshold `nu_comm eta_ji^* > Delta T_cost` repeats the tempo-as-useful-rate simplification. It lacks per-message information value/relevance, redundancy, latency, and task value terms unless those are folded into `eta` or `nu`.
- F193 soft candidate: diminishing returns from accumulating `U_src` and `U_o` across diverse sources is not general. Additional sources can increase noise and overhead, but can also reduce uncertainty through independent corroboration; the sign depends on source dependence and aggregation model.
- F194 watch: the segment correctly says the disturbance decomposition is a modeling choice. Downstream theorem-grade uses should cite the decomposition as an assumption, not as something derived from the sector template.

## Local verdict

The derivation is substantially more disciplined than the intro. It earns its conditional status if the alpha/tempo bridge, coupling units, and event-allocation convention are made explicit.

