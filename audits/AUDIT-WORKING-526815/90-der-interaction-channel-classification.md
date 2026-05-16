# 90 - der-interaction-channel-classification

Source: `01-aat-core/src/der-interaction-channel-classification.md`

## First-pass understanding

This segment shifts the coupling story from emitter scalar to recipient diagnosis. The same incoming event can be a usable update, a magnitude shock, a structural shock, or ambient erosion depending on the recipient's sector radius, model-class representability, and observability floor. That is a useful decomposition because the repair differs by regime: more capacity, different model class, better filtering, or ordinary update.

The flowchart is clearer than the quantitative aggregation. The per-event regime labels are plausible as a diagnostic vocabulary, but the regime-typed `rho_eff` formula adds magnitudes, structural floors, variances, and information rates into one scalar without a common unit map. The segment also says the three boundaries are independent and force four regimes, while two tests share `I(e)` and three booleans would normally produce more combinations unless a precedence convention collapses them.

## Diagram attempt

I drew the classification as a precedence flow: first check sector magnitude, then representability, then observability. That makes the four named regimes intelligible, but it also makes clear that the four-regime result is a chosen diagnostic precedence over three boundary tests, not automatically the full Boolean partition.

## Findings and watches

- F186 clarified/partly resolved: the detailed segment defines Regime III as below observability floor and contributing to variance without usable update. The intro's "processed until tempo is consumed" wording should be aligned with this: either unobserved ambient variance or low-priority processed overhead, not both without a threshold distinction.
- F187 candidate: the three boundaries are conceptually distinct, but not independent in the ordinary variable sense because both the model-class and observability tests depend on `I(e)`. The claim should say "orthogonal diagnostic criteria" or state the independence notion.
- F203 candidate: the segment again uses mutual information notation `I(e; Omega | M)` for a realized event's information content. That repeats the earlier expected-vs-realized information issue; per-event classification needs pointwise surprise/information gain or an explicit random-variable convention.
- F204 candidate: the observability boundary `I(e) * nu^(k) >= U_o,B^(k) * c_floor` is dimensionally unclear. Information rate is being compared to observation noise/uncertainty times a constant; the threshold needs a common detection-statistic scale.
- F205 candidate: three binary boundary tests do not by themselves yield only four regimes. The file uses a precedence convention: fail magnitude first => II-a; else fail class => II-b; else fail observability => III; else I. That may be a good coarsening, but it is not "forced" by three independent boundaries.
- F206 candidate: the regime-typed `rho_B^eff` formula adds quantities with incompatible units: `||e|| nu`, `floor(M) nu`, `sigma_e^2 nu`, and `iota I(e) nu`. It needs conversion functions into the same mismatch-disturbance-rate units before summation.
- F207 candidate: the negative Regime-I term is not always structural. True cooperative information may reduce effective disturbance, but Regime-I-with-adversarial-content later in the same segment shows that an absorbable update can be harmful depending on content and alignment.
- F208 soft candidate: the class boundary `F(M_B) * I_max(M_B)` is acknowledged as heuristic. Until replaced by sufficient-statistics span or projection-to-class machinery, II-b is a useful label rather than a quantitative threshold.
- F209 candidate: the Kalman Case 1 expression says `s^2/(2r ln 2)` nats. Division by `ln 2` converts natural-log nats to bits; the unit label or formula is inconsistent.
- F210 soft candidate: the Kalman worked case sets sector parameter `alpha_B = eta_B^*`. This inherits the earlier concern that update gain is not automatically a time-normalized sector correction rate.
- F211 candidate: the declared dependencies omit `obs-gated-tempo-advantage`, but boundary (I-c), the boundary table, and recovery section invoke it as a source for the observability boundary.
- F212 soft candidate: the claim that `result-adversarial-tempo-advantage` exponent drops toward zero in the high-`U_o` limit because fewer events land in Regime II is plausible but not derived here.
- F213 watch: this segment's opacity account (`gamma_A^effective = gamma_A^max f(H_b^B)`) is cleaner than the previous `1/H_b(A) * 1/H_b(B)` statement. Track which formulation becomes canonical.
- F214 watch: references to spike material and Class-2 degradation (`kappa_processing`) should remain scope notes unless those artifacts are in the audited dependency path.

## Local verdict

The recipient-side regime vocabulary is valuable as a diagnostic coarsening. The quantitative claims need a common disturbance-rate ledger, a clarified event-information statistic, and an explicit statement that the four-regime flow is a precedence/coarsening choice.

