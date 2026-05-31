# 76 - der-tempo-composition

Source: `01-aat-core/src/der-tempo-composition.md`

## First-pass understanding

This segment translates composition closure into tempo language. The headline inequality is sub-additivity: a composite cannot have more adaptive tempo than the sum of its members, and the gap is coordination overhead. Closure defect then becomes a tempo-equivalent penalty by multiplying by macro update rate and normalizing by a critical mismatch scale.

The idea is useful, especially for Brooks's Law style claims. But the text needs one consistent accounting convention. Closure defect can be treated as extra disturbance the macro-agent must correct, or as tempo consumed by internal coordination, but several displayed consequences appear to use both perspectives at once.

## Diagram attempt

I drew aggregate sub-agent tempo flowing toward external correction, with closure defect diverting part of it into coordination. The diagram includes a warning split: count closure as a disturbance burden or as tempo overhead, but do not subtract it twice.

## Findings and watches

- F116 candidate: `der-tempo-composition` defines `C_coord = sum_i T_i - T_c`, then defines realized external tempo as `T_c^ext = T_c - C_coord`. This subtracts coordination overhead twice, giving `sum_i T_i - 2 C_coord` under the definition. If `T_c` is already realized macro-tempo after coordination overhead, external tempo should be `T_c`; if `T_c` is gross composite capacity, then `C_coord` should not be defined as `sum_i T_i - T_c`.
- F117 candidate: the segment treats closure defect both as an added disturbance `rho_eff = rho_ext + epsilon* nu_c` and as a tempo overhead `C_coord >= epsilon* nu_c / ||delta_critical||`. These are equivalent accounting views only if used separately; using both in the same persistence inequality double counts the closure burden.
- F118 candidate: the displayed "equivalent" composite persistence condition `sum T_i > (rho_ext + epsilon* nu_c)/||delta_critical||` is not equivalent when `C_coord` can exceed its lower bound or when other coordination costs exist. The safer condition is `sum T_i - C_coord > rho_ext/||delta_critical||`, with the closure lower bound giving a sufficient or necessary relaxation depending on direction.
- F119 soft candidate: `T_c <= sum_i T_i` needs assumptions about how individual tempos are measured and how information synergy is handled. If individual tempos are measured standalone, fusion or division of labor can create macro correction efficiency not visible in the sum. If measured as within-composite channel capacities, the inequality is more plausible but should be stated.
- F120 soft candidate: the statement that `epsilon*=0` makes every sub-agent correction cycle contribute directly to the macro loop is too strong. Exact representability removes closure-defect overhead, but negotiation, synchronization, redundant observations, and nonshared intent can still consume tempo unless the listed equality conditions also hold.
- F121 soft candidate: the Brooks's Law turning point `Delta epsilon* nu_c / ||delta_critical|| > Delta T_i` assumes `nu_c`, the critical scale, and all non-closure coordination costs remain fixed. That is a useful first-order condition, not a general turning point.
- Watch: the channel-independence caveat in Working Notes is important; summed scalar tempos can overcount overlapping observation channels.

## Local verdict

The segment has the right dimensional instinct, but it needs a single ledger. The clean version is either disturbance accounting or tempo-overhead accounting; mixing them makes the persistence and external-tempo formulas unreliable.
