# 60 - hyp-edge-update-via-gain

Source: `01-aat-core/src/hyp-edge-update-via-gain.md`

## First-pass understanding

This segment extends the update-gain idea from model state to strategy edges. The generic form is a conservative convex update from old edge credence toward an evidential signal, with gain controlled by edge uncertainty and observation noise. The segment is careful to say the Beta-Bernoulli case is not a literal substitution into the Gaussian/Kalman variance-ratio formula; its exact gain is the conjugate update rate `1/(n+1)`.

The strongest part is that distinction between principle and instantiation. The unresolved part is the signal function: what counts as evidence for edge `(i,j)` depends on observability and credit assignment. The segment mostly delegates that to later proof homes.

## Diagram attempt

I drew the edge update as two layers: an exact Beta-Bernoulli track in probability space, and a log-odds/evidence-additivity track that is useful only if the coordinate's random variable is the same. The diagram includes a type-check gate because that is where the segment's most likely mathematical slippage lives.

## Findings and watches

- F54 candidate: the "Parallel log-odds presentation" appears to conflate two different log-odds coordinates: log-odds that an edge hypothesis is true and logit of a Bernoulli edge success probability/posterior mean. Beta-Bernoulli updating is additive in sufficient statistics `(alpha,beta)`, while a scalar `lambda_new=lambda_old+ell(y)` needs a specified binary hypothesis and likelihood ratio. The claimed coordinate equivalence needs a type statement.
- F55 candidate: `U_edge` is a Beta variance in probability space while `U_obs proportional 1/sigma_j` is an observability/noise proxy. The ratio `U_edge/(U_edge+U_obs)` is only meaningful after mapping both into a common metric. The segment partly avoids this by treating the ratio as structural principle, but the formal definition still presents the mixed-unit formula.
- F56 candidate: the segment's epistemic-status section relies on `disc-credit-assignment-boundary`, `deriv-edge-credence-dynamics`, and `deriv-edge-update-natural-parameter` for theory-level resolution and coordinate forcing, but these are not declared dependencies. Some are intentionally forward references, yet they carry much of the advertised warrant.
- Watch: the spike note on `M_t`/edge double counting is outside the allowed AAT segment path and remains unverified in this pass.
- Watch: the i.i.d. Beta-Bernoulli assumption is stated clearly; downstream uses under drift, context dependence, or correlated edges should invoke discounting/contextualization rather than reuse the static gain directly.

## Local verdict

The probability-space Beta-Bernoulli core is defensible as a hypothesis/instantiation. The log-odds equivalence and mixed uncertainty-ratio notation need type discipline before promotion beyond discussion-grade.
