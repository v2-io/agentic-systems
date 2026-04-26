# Running Outline for Final Report

## Phase 1 — Findings under burden of proof

*(To be populated as findings are discovered)*
- Will contain specific quotes, counterevidence search, status determination, confidence, and reasons why they stand.
- Potential focus areas based on initial predictions:
  - Math verification in Appendices.
  - Scope propagation (specifically `directed separation` into Section II/III).
  - Causal identifiability claims in strategy DAGs.

**Finding 1: Conflation of IB $\beta$ parameter with environment volatility ($\rho$)**
- **Location**: `01-aad-core/src/form-information-bottleneck.md`
- **Claim**: The parameter $\beta$ must be lowered in volatile environments (high $\rho$) to favor aggressive compression.
- **Counterevidence**: The IB objective naturally discards non-predictive information. In a volatile environment, old data loses mutual information with the future. Thus, retaining it increases $I(M; C)$ without increasing $I(M; Y)$. The optimum $\phi^*$ naturally compresses more *at fixed $\beta$*. Adjusting $\beta$ in response to $\rho$ is a double-counting error; $\beta$ represents the relative cost of memory vs accuracy, not the environment's volatility.

**Finding 2: Level 3 Counterfactuals in Software**
- **Location**: `01-aad-core/src/def-pearl-causal-hierarchy.md`
- **Claim**: `git checkout` provides ground-truth Level 3 counterfactual execution.
- **Counterevidence**: `git checkout` resets the codebase but not the full environment (e.g., developer's mind, time, external dependencies). It is a highly reproducible Level 2 intervention, but falls short of a true Level 3 counterfactual $P(y_{x'} \mid x, y)$ which requires observing what *would have happened* at the original time $t$, not trying again at $t+k$.

## Phase 2 — Integration-debt diagnosis via `msc/`

*(To be populated once findings are established)*
- Checking `msc/` documents to see if discovered gaps were actually known or addressed in spikes but not propagated to `src/`.

## Phase 3 — Bigger-picture pondering

*(To be populated after sufficient reading)*
- High-level structural observations, conceptual alignments, or missing literature connections.
