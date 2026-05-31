# 51 - der-chain-confidence-decay

Source: `01-aat-core/src/der-chain-confidence-decay.md`

## First-pass understanding

This segment applies the probability chain rule to strategy success. A multi-step chain succeeds only if each event succeeds in order, so log confidence decomposes as a sum of conditional log probabilities. Since each term is non-positive, adding required uncertain steps cannot increase aggregate confidence. The independent `p^n` table is only an illustration; the exact result is the conditional chain-rule form.

The useful consequence is structural pressure: shorter plans, parallel fallbacks, early monitoring, and investment in critical high-confidence links. The discussion then connects chain depth to later penalties: downstream evidence starvation and cognitive/description cost. Those later penalties have not been read yet, so the local exact claim remains the log-additive confidence identity.

## Diagram attempt

The diagram is a log-confidence ledger. Each step adds a non-positive log term. Certain steps add zero; uncertain steps push total confidence downward. That makes the monotone non-increase visible without overcommitting to the independent `p^n` special case.

## Findings and watches

- Soft candidate: the segment says confidence "decays" monotonically with depth. The exact probability result is monotone non-increase; strict decay requires each added required step to have conditional success probability below 1. Certain prerequisite steps add zero log penalty.
- Watch: AND-node amplification as `p^(k*d)` is illustrative unless parent chains are independent/uniform and do not share latent causes. The later strategy-DAG/correlation hierarchy needs to carry exact combination semantics.
- Watch: chain success is a fixed-plan calculation. Replanning, monitoring, retry loops, and adaptive fallback can change the relevant success event, so downstream use should be clear whether it is evaluating a static chain or an adaptive strategy.
- Watch: the coordinate-forcing and Section III corollary material is forward-linking. Treat as preview until the home segments are read.

## Local verdict

The local theorem is good and exact if phrased as log-additive probability plus monotone non-increase. The segment's broader strategic implications are reasonable but depend on later graph, correlation, and adaptive-strategy machinery.
