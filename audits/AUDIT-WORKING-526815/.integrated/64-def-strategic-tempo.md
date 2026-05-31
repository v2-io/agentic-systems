# 64 - def-strategic-tempo

Source: `01-aat-core/src/def-strategic-tempo.md`

## First-pass understanding

This segment defines strategic tempo as the sum of per-edge observation rate, update gain, and identifiability. It mirrors adaptive tempo, but with a crucial strategy-layer difference: edge rates are endogenous to the agent's policy and gated by upstream success, exploration allocation, and causal identifiability.

The strongest part is the bottleneck warning. The scalar sum measures total corrective throughput; persistence is per-edge and weakest-link limited. The segment says this explicitly in the per-edge condition and again in the NeurIPS working note, but the headline definition still risks sounding like the sum is the effective persistence rate.

## Diagram attempt

I drew strategic tempo as two simultaneous summaries over the same edges: a throughput sum and a bottleneck minimum. The sum can look healthy while one untested or weakly identifiable edge fails the persistence condition.

## Findings and watches

- F66 candidate: `T_Sigma` is defined as a sum and described as the effective rate of useful strategy revision, but the persistence-relevant quantity is the bottleneck/min per-edge rate. The segment acknowledges this later; the headline should label the sum as throughput tempo and reserve "effective for persistence" for the bottleneck form.
- F67 candidate: "Regime-C edges contribute essentially nothing" and "an agent cannot improve parts of its strategy it cannot test interventionally" overstate the point. Observational evidence can improve associational prediction; what it cannot do, without assumptions, is validate interventional causal efficacy.
- F68 soft candidate: the `T_Sigma > |E| rho/R` necessary condition assumes homogeneous per-edge thresholds. In the heterogeneous case the necessary aggregate bound should sum the per-edge thresholds `sum_e rho_e/R_e`, while sufficiency remains bottleneck/per-edge.
- Watch: the AND-chain and OR-node formulas rely on independent/Beta-Bernoulli topology cases from `deriv-edge-credence-dynamics`, which appears much later in the AAT outline.
- Watch: the software-as-Regime-A line repeats the earlier domain overgeneralization; it holds for isolated tests and controlled deployment edges, not all software strategy edges.

## Local verdict

The definition is useful if read as aggregate corrective throughput. For persistence and adversarial concentration, the bottleneck form should be promoted into the main definition or paired with the sum at the headline level.
