# 84 - hyp-auftragstaktik-principle

Source: `01-aat-core/src/hyp-auftragstaktik-principle.md`

## First-pass understanding

This segment turns shared intent into a communication-allocation hypothesis: when bandwidth is scarce, share purpose first, strategy second, and detailed model state last. The mechanism is shelf-life and coordination value per bit. Objectives are compact and slow-moving, while detailed plans and local models are larger and decay faster.

The qualitative principle is strong. The formula `B_O > B_Sigma > B_M` is too blunt, though. A rational allocation may prioritize objective bits first while still spending more total bandwidth on model synchronization when models are larger, noisier, or operationally critical.

## Diagram attempt

I drew the principle as marginal value per bit rather than raw bandwidth totals. The diagram shows objectives as high shelf-life/high leverage, strategy as intermediate, and model synchronization as context-dependent rather than always last in absolute allocation.

## Findings and watches

- F162 candidate: `B_O > B_Sigma > B_M` confuses priority ordering with total bandwidth allocation. IB reasoning supports sending high marginal-value, long-shelf-life objective bits first; it does not imply the total number of objective bits must exceed strategy or model bits.
- F163 candidate: maximizing composite tempo and minimizing coordination overhead are not equivalent in general. Bandwidth allocation can increase aggregate correction capacity, reduce disturbance, or change local autonomy as well as coordination overhead.
- F164 soft candidate: the ordering depends on strong assumptions about entropy, change rates, and local observability. The segment names reversals, but the formal statement should be explicitly marginal and conditional on those rates/costs.
- F165 soft candidate: the Conway's Law claim is too strong as stated. Conway's Law says system structure mirrors communication structure; deriving objective-decomposition boundaries from high `B_O` and low `B_Sigma` needs additional organizational/design assumptions.
- F166 watch: the qualitative principle inherits the unresolved IB formalization issues from `def-shared-intent`; keep it discussion-grade until the relevance variable and encoder are specified.

## Local verdict

The principle should be stated as "prioritize objective information at the margin under scarce bandwidth," not as a universal inequality over total bandwidth buckets.
