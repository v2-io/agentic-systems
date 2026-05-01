# R2 Aggregation — Table View

**Generated:** 2026-05-01T01:32:16Z
**Targets included:** 106 (filtered to ≥2 R2 voters from 629 total)
**R2 voters:** codex-r2b, gemini-r2, opus-r2b, opus-r2c, sonnet-r2b, sonnet-r2c

Single unified table. Targets in `**[ ... ]**` brackets, sorted by max(score/n) descending — the targets that accumulated the most normalized consensus appear first. Within each target, candidates are ordered by total substance (leader first). Math renders as math — table cells deliberately do not use backticks so `$inline$` math passes through to the renderer.

Filtered out (default): targets where the only master candidate is the current name (`is_keep`) and no R2 voter wrote in an alternative. These are uncontested keeps — no decision needed. Override with `--include-uncontested-keeps`.

- **Bold row** = leader (highest score)
- **▸** = candidate is the current name in the corpus (`is_keep` from master-list)
- **⊕** = at least one voter (R1 or R2) cast an `add-alias` vote on this candidate. Read the detail view: an add-alias vote means "keep the current name AND add this as a parallel handle," not "replace." Different downstream action than rename/keep/canonicalize.
- **★**: top-pick count across R2 voters
- **n-votes**: count of distinct voters who weighed in on this candidate (R1 synthetic counts as 1 alongside each R2 voter)
- **v-total**: sum of signed weights across all voters (raw tally before substance factor)
- **score**: substance-adjusted vote tally — sum of (weight × factor) across voters, where factor = (0.7 + 0.3 × effort) × (1.0 + novelty), with effort = min(1, note_chars / bullet_chars). × 1.2 for top-pick votes, × 1.2 for canonicalize votes (both multiplicative). Empty note → 0. Bandwagon → 1.0. Thoughtful → 2.0. Top-picked thoughtful canonicalize → 2.88. Write-ins land near 2.0 by construction (no bullet → effort=1, novelty=1).
- **score/n**: score normalized by total voters who weighed in on *any candidate* in this target (R1 synth counts as 1 if R1 has any votes anywhere in target). Other candidates in the target are implicit zeros. Useful for comparing across targets with different voter counts and for spotting under-engaged targets.
- **arch**: distinct R2 architectures voting on this candidate

Per-voter weights and notes live in the detail view.

See [r2-aggregate-detail.md](r2-aggregate-detail.md) for per-target full vote breakdown, notes, and rationale.

| target / candidate                                                                       |     ★ | n-votes | v-total |    score |  score/n |  arch |
| ---------------------------------------------------------------------------------------- | ----: | ------: | ------: | -------: | -------: | ----: |
| **[ composition consistency ]**                                                          |       |         |         |          |          |       |
| ▸ **composition consistency**                                                            | **3** |   **4** |  **+8** | **16.2** | **4.04** | **2** |
| ⊕ Cross level coherence                                                                  |       |       4 |      -1 |     -1.8 |    -0.46 |     2 |
| Scale invariance of adaptive dynamics                                                    |       |       4 |      -3 |     -5.5 |    -1.37 |     2 |
| Holon postulate                                                                          |       |       4 |      -3 |     -5.7 |    -1.42 |     2 |
| Scale invariance                                                                         |       |       4 |      -3 |     -5.7 |    -1.44 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ aporia ]**                                                                           |       |         |         |          |          |       |
| ▸ **aporia**                                                                             | **3** |   **4** |  **+8** | **15.9** | **3.97** | **2** |
| ⊕ Aporia productive perplexity                                                           |       |       3 |      +1 |      1.3 |     0.32 |     1 |
| Discrepancy                                                                              |       |       3 |      -3 |     -4.6 |    -1.15 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ temporal software theory ]**                                                         |       |         |         |          |          |       |
| ▸ **temporal software theory**                                                           | **2** |   **3** |  **+6** | **11.7** | **3.91** | **1** |
| Temporal Software Theory (TST)                                                           |       |       3 |      +3 |      4.9 |     1.64 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ credit assignment boundary ]**                                                       |       |         |         |          |          |       |
| ▸ **credit assignment boundary**                                                         | **2** |   **3** |  **+6** | **11.7** | **3.89** | **2** |
| Credit assignment frontier                                                               |       |       2 |      +1 |      1.5 |     0.52 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ model sufficiency ]**                                                                |       |         |         |          |          |       |
| ▸ **model sufficiency**                                                                  | **3** |   **4** |  **+8** | **15.5** | **3.87** | **3** |
| ⊕ Predictive sufficiency                                                                 |       |       3 |      +3 |      4.6 |     1.16 |     2 |
| ⊕ Predictive information retention                                                       |       |       3 |       0 |        0 |        0 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ ASF (acronym) ]**                                                                    |       |         |         |          |          |       |
| **ASF**                                                                                  | **4** |   **5** |  **+9** | **19.3** | **3.86** | **4** |
|                                                                                          |       |         |         |          |          |       |
| **[ adversarial tempo advantage ]**                                                      |       |         |         |          |          |       |
| ▸ **adversarial tempo advantage**                                                        | **2** |   **3** |  **+6** | **11.5** | **3.84** | **2** |
| Superlinear tempo advantage                                                              |       |       2 |      +1 |      1.8 |     0.61 |     1 |
| Tempo advantage                                                                          |       |       2 |      -1 |     -1.8 |    -0.60 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ complete agent state ]**                                                             |       |         |         |          |          |       |
| ▸ **complete agent state**                                                               | **3** |   **4** |  **+8** | **15.1** | **3.79** | **2** |
| Purposeful state                                                                         |       |       4 |      -2 |     -3.3 |    -0.83 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ agent model ]**                                                                      |       |         |         |          |          |       |
| **Reality model**                                                                        | **4** |   **5** |  **+9** | **18.9** | **3.78** | **4** |
| ▸ agent model                                                                            |       |       4 |      -2 |     -4.7 |    -0.95 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ $G_t = (O_t, \Sigma_t)$ ]**                                                          |       |         |         |          |          |       |
| ⊕ **Purposeful substate**                                                                | **2** |   **3** |  **+5** | **11.3** | **3.77** | **2** |
| ⊕ Purposeful state                                                                       |       |       3 |      +1 |      1.2 |     0.41 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ objective functional ]**                                                             |       |         |         |          |          |       |
| ▸ **objective functional**                                                               | **3** |   **4** |  **+7** | **15.0** | **3.75** | **2** |
| Teleological objective                                                                   |       |       3 |      -2 |     -3.7 |    -0.93 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ calibration laboratory ]**                                                           |       |         |         |          |          |       |
| ▸ ⊕ **calibration laboratory**                                                           | **3** |   **4** |  **+8** | **15.0** | **3.74** | **2** |
| Software as calibration laboratory                                                       |       |       4 |      +4 |      6.1 |     1.52 |     2 |
| Calibration laboratory move                                                              |       |       4 |      +4 |      6.0 |     1.50 |     2 |
| Software calibration laboratory                                                          |       |       3 |      +1 |      1.6 |     0.41 |     1 |
| ⊕ Calibration domain                                                                     |       |       4 |      -1 |     -1.5 |    -0.38 |     2 |
| Privileged grounding domain                                                              |       |       3 |      -1 |     -2.7 |    -0.67 |     1 |
| Privileged calibration domain                                                            |       |       3 |      -1 |     -2.8 |    -0.71 |     1 |
| High identifiability testbed                                                             |       |       3 |      -1 |     -3.0 |    -0.75 |     1 |
| Calibration domain calibration lab                                                       |       |       3 |      -2 |     -3.3 |    -0.83 |     1 |
| Epistemic laboratory framing                                                             |       |       3 |      -2 |     -3.4 |    -0.85 |     1 |
| Calibration lab framing                                                                  |       |       3 |      -2 |     -3.9 |    -0.97 |     1 |
| High identifiability calibration lab                                                     |       |       3 |      -2 |     -4.0 |    -0.99 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ directional fidelity ]**                                                             |       |         |         |          |          |       |
| ▸ **directional fidelity**                                                               | **2** |   **3** |  **+6** | **11.2** | **3.74** | **2** |
| Pointing condition                                                                       |       |       2 |      -1 |     -1.6 |    -0.54 |     1 |
| Corrective alignment                                                                     |       |       2 |      -2 |     -2.6 |    -0.88 |     1 |
| Correction direction integrity                                                           |       |       2 |      -2 |     -2.8 |    -0.92 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ $\iota_{ij}$ ]**                                                                     |       |         |         |          |          |       |
| ⊕ **Identifiability coefficient**                                                        | **2** |   **3** |  **+6** | **11.2** | **3.73** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ chronica capitalized vs lowercase ]**                                                |       |         |         |          |          |       |
| **Chronica lowercase in running prose**                                                  | **3** |   **4** |  **+6** | **14.8** | **3.71** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ postulate not axiom ]**                                                              |       |         |         |          |          |       |
| **Postulate**                                                                            | **2** |   **3** |  **+5** | **10.8** | **3.60** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ model-class fitness ]**                                                              |       |         |         |          |          |       |
| ▸ **model-class fitness**                                                                | **3** |   **4** |  **+8** | **14.3** | **3.58** | **3** |
| ⊕ Class capacity ceiling                                                                 |       |       3 |      +2 |      3.6 |     0.89 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ correlation hierarchy ]**                                                            |       |         |         |          |          |       |
| ▸ **correlation hierarchy**                                                              | **3** |   **4** |  **+7** | **14.3** | **3.58** | **2** |
| Correlation hierarchy L0 / L1 / L1' / L2                                                 |       |       4 |      +4 |      6.9 |     1.74 |     2 |
| Correlation ladder                                                                       |       |       4 |      +2 |      2.6 |     0.66 |     2 |
| ⊕ Predicting exploring reasoning triad                                                   |       |       4 |      -2 |     -4.4 |    -1.10 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ deliberation cost ]**                                                                |       |         |         |          |          |       |
| ▸ **deliberation cost**                                                                  | **2** |   **3** |  **+6** | **10.7** | **3.58** | **2** |
| The simulation tax                                                                       |       |       2 |      +2 |      2.9 |     0.96 |     1 |
| Deliberation threshold                                                                   |       |       2 |      +1 |      1.8 |     0.60 |     1 |
| Deliberation drag                                                                        |       |       2 |      +1 |      1.7 |     0.58 |     1 |
| Think vs act tradeoff                                                                    |       |       2 |      -1 |     -1.6 |    -0.53 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ persistence condition ]**                                                            |       |         |         |          |          |       |
| ▸ **persistence condition**                                                              | **3** |   **4** |  **+8** | **14.3** | **3.57** | **3** |
| ⊕ Survival equation                                                                      |       |       3 |      +2 |      3.8 |     0.94 |     2 |
| The survival equation                                                                    |       |       3 |      +1 |      0.9 |     0.23 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ derivation not proof ]**                                                             |       |         |         |          |          |       |
| **Derivation**                                                                           | **3** |   **4** |  **+7** | **14.3** | **3.56** | **3** |
|                                                                                          |       |         |         |          |          |       |
| **[ AAD (acronym) ]**                                                                    |       |         |         |          |          |       |
| **AAD**                                                                                  | **3** |   **4** |  **+7** | **14.2** | **3.56** | **3** |
| Adaptation and purpose dynamics apd                                                      |       |       3 |      -3 |     -4.3 |    -1.08 |     2 |
| Adaptation and agency dynamics AAD                                                       |       |       3 |      -3 |     -4.4 |    -1.10 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ sector condition ]**                                                                 |       |         |         |          |          |       |
| ▸ **sector condition**                                                                   | **2** |   **3** |  **+6** | **10.6** | **3.53** | **2** |
| Continuous sector condition                                                              |       |       3 |      +1 |      1.0 |     0.35 |     2 |
| sector condition derivation                                                              |       |       3 |       0 |     -0.1 |        0 |     2 |
| Persistence condition                                                                    |       |       3 |      -2 |     -3.7 |    -1.24 |     2 |
| Correction sector                                                                        |       |       3 |      -2 |     -3.9 |    -1.29 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ satisfaction gap ]**                                                                 |       |         |         |          |          |       |
| ▸ ⊕ **satisfaction gap**                                                                 | **5** |   **6** | **+12** | **21.0** | **3.51** | **3** |
| Attainability shortfall                                                                  |       |       5 |      -5 |     -8.5 |    -1.42 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ adaptive cycle ]**                                                                   |       |         |         |          |          |       |
| ▸ **adaptive cycle**                                                                     | **3** |   **4** |  **+8** | **14.0** | **3.51** | **3** |
| The cycle the adaptive cycle                                                             |       |       3 |      +4 |      6.8 |     1.69 |     2 |
| Feedback cycle                                                                           |       |       3 |      -3 |     -4.2 |    -1.04 |     2 |
| Correction cycle                                                                         |       |       3 |      -3 |     -4.3 |    -1.07 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ $H_b$ ]**                                                                            |       |         |         |          |          |       |
| **Agent opacity $H_b$**                                                                  | **1** |   **3** |  **+5** | **10.5** | **3.50** | **2** |
| ⊕ Agent opacity                                                                          |     1 |       2 |      +3 |      5.4 |     1.82 |     1 |
| ▸ $H_b$                                                                                  |       |       2 |      +2 |      3.1 |     1.03 |     1 |
| ⊕ Backward opacity                                                                       |       |       2 |       0 |     -1.0 |    -0.32 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ exact / robust-qualitative / heuristic / conditional (claim tier) ]**                |       |         |         |          |          |       |
| ▸ **exact / robust-qualitative / heuristic / conditional (clai…**                        | **2** |   **3** |  **+5** | **10.5** | **3.50** | **2** |
| ⊕ Epistemic claim tier                                                                   |       |       3 |      +4 |      6.5 |     2.17 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ prolepsis ]**                                                                        |       |         |         |          |          |       |
| ▸ **prolepsis**                                                                          | **2** |   **3** |  **+6** | **10.4** | **3.46** | **2** |
| ⊕ Prolepsis anticipatory projection                                                      |       |       2 |       0 |     -0.5 |    -0.17 |     1 |
| Anticipation                                                                             |       |       2 |      -2 |     -2.7 |    -0.89 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ mismatch dynamics ]**                                                                |       |         |         |          |          |       |
| ▸ **mismatch dynamics**                                                                  | **2** |   **3** |  **+5** | **10.3** | **3.43** | **2** |
| Mismatch dynamics drift and noise regime                                                 |       |       2 |      -1 |     -2.0 |    -0.65 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Pearl causal hierarchy ]**                                                           |       |         |         |          |          |       |
| ▸ **Pearl causal hierarchy**                                                             | **5** |   **6** | **+12** | **20.5** | **3.42** | **4** |
| Causal hierarchy level                                                                   |       |       5 |      -1 |     -2.3 |    -0.38 |     3 |
| ⊕ Causal hierarchy                                                                       |       |       5 |      -2 |     -3.8 |    -0.63 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ continuity persistence ]**                                                           |       |         |         |          |          |       |
| ▸ **continuity persistence**                                                             | **4** |   **5** |  **+8** | **17.0** | **3.41** | **3** |
| ⊕ Identity continuity                                                                    |       |       5 |      +1 |      0.9 |     0.19 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ Concept: _symbol default m t in prose_ ]**                                           |       |         |         |          |          |       |
| ⊕ **Model state**                                                                        | **3** |   **4** |  **+6** | **13.6** | **3.40** | **3** |
| ⊕ Epistemic substate                                                                     |       |       3 |      +3 |      4.8 |     1.20 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ agent spectrum ]**                                                                   |       |         |         |          |          |       |
| ▸ **agent spectrum**                                                                     | **4** |   **5** | **+10** | **16.9** | **3.39** | **3** |
| Agency spectrum                                                                          |       |       4 |      +1 |      1.7 |     0.34 |     2 |
| Agent quadrant                                                                           |       |       4 |      -4 |     -6.5 |    -1.31 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ logogenic logozoetic ]**                                                             |       |         |         |          |          |       |
| ▸ **logogenic logozoetic**                                                               | **3** |   **4** |  **+8** | **13.5** | **3.37** | **3** |
| ⊕ Logogenic logozoetic distinction                                                       |       |       4 |      +5 |      9.6 |     2.40 |     3 |
| Language constituted language living                                                     |       |       4 |      -4 |     -5.6 |    -1.41 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ $\mathcal C_t$ chronica ]**                                                          |       |         |         |          |          |       |
| **$\mathcal C_t$**                                                                       | **3** |   **4** |  **+7** | **13.5** | **3.37** | **3** |
|                                                                                          |       |         |         |          |          |       |
| **[ orient cascade ]**                                                                   |       |         |         |          |          |       |
| ▸ **orient cascade**                                                                     | **5** |   **6** | **+12** | **20.1** | **3.35** | **3** |
| ⊕ The adaptive pentad                                                                    |       |       5 |      +1 |      1.1 |     0.19 |     2 |
| ⊕ The pentad                                                                             |       |       5 |       0 |      0.2 |        0 |     2 |
| ⊕ Adaptive cycle                                                                         |       |       5 |      -1 |     -3.1 |    -0.51 |     2 |
| The five turn                                                                            |       |       5 |      -5 |     -6.4 |    -1.07 |     2 |
| Adaptive cycle phase                                                                     |       |       5 |      -3 |     -6.9 |    -1.15 |     2 |
| Five adaptive cycle phase                                                                |       |       5 |      -3 |     -7.0 |    -1.17 |     2 |
| Adaptive traversal                                                                       |       |       5 |      -4 |     -7.2 |    -1.20 |     2 |
| The pentad five phase cycle                                                              |       |       5 |      -4 |     -7.9 |    -1.31 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ aporia prolepsis aisthesis epistrophe praxis ]**                                     |       |         |         |          |          |       |
| ▸ **aporia prolepsis aisthesis epistrophe praxis**                                       | **2** |   **3** |  **+5** | **10.0** | **3.34** | **2** |
| Greek rooted vocabulary                                                                  |       |       3 |      +3 |      5.6 |     1.87 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ mismatch signal ]**                                                                  |       |         |         |          |          |       |
| ▸ **mismatch signal**                                                                    | **4** |   **5** | **+10** | **16.7** | **3.34** | **3** |
| ⊕ Aporia signal                                                                          |       |       4 |      +2 |      3.6 |     0.72 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ $U_M$ ]**                                                                            |       |         |         |          |          |       |
| ⊕ **Epistemic unity**                                                                    | **2** |   **3** |  **+5** | **10.0** | **3.32** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ control regret ]**                                                                   |       |         |         |          |          |       |
| ▸ ⊕ **control regret**                                                                   | **5** |   **6** | **+12** | **19.9** | **3.32** | **3** |
| Strategy opportunity cost                                                                |       |       5 |      -5 |     -8.7 |    -1.44 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ aisthesis ]**                                                                        |       |         |         |          |          |       |
| ▸ **aisthesis**                                                                          | **3** |   **4** |  **+7** | **13.3** | **3.32** | **2** |
| ⊕ Aisthesis observation alignment                                                        |       |       3 |      -1 |     -2.9 |    -0.72 |     1 |
| Intake                                                                                   |       |       3 |      -3 |     -4.5 |    -1.13 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Concept: _structural persistence operational persistence continuity persistence_ ]** |       |         |         |          |          |       |
| ⊕ **Persistence taxonomy**                                                               | **3** |   **5** |  **+8** | **16.6** | **3.32** | **4** |
| Structural operational continuity persistence                                            |     1 |       4 |      +7 |     13.2 |     2.63 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ chronica ]**                                                                         |       |         |         |          |          |       |
| ▸ **chronica**                                                                           | **5** |   **6** | **+12** | **19.9** | **3.31** | **4** |
| Lowercase italic chronica                                                                |       |       5 |      +4 |      8.3 |     1.38 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ structural adaptation necessity ]**                                                  |       |         |         |          |          |       |
| ▸ **structural adaptation necessity**                                                    | **2** |   **3** |  **+5** |  **9.9** | **3.31** | **1** |
| Adaptation necessity                                                                     |       |       3 |      -1 |     -2.8 |    -0.92 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ formulation / definition / result / ... (segment types) ]**                          |       |         |         |          |          |       |
| **Formulation definition result etc segment type**                                       | **2** |   **3** |  **+5** |  **9.9** | **3.31** | **2** |
| ⊕ Segment typology                                                                       |       |       3 |      +3 |      5.0 |     1.67 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ information bottleneck ]**                                                           |       |         |         |          |          |       |
| ▸ **information bottleneck**                                                             | **3** |   **4** |  **+8** | **13.2** | **3.31** | **3** |
| Epistemic bottleneck                                                                     |       |       3 |      -2 |     -3.9 |    -0.98 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ adaptive tempo ]**                                                                   |       |         |         |          |          |       |
| ▸ **adaptive tempo**                                                                     | **4** |   **5** | **+10** | **16.5** | **3.31** | **3** |
| ⊕ tempo                                                                                  |       |       4 |      +4 |      7.1 |     1.41 |     2 |
| Adaptation rate                                                                          |       |       4 |      -4 |     -6.5 |    -1.29 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ $\alpha$ (sector-condition lower bound) ]**                                          |       |         |         |          |          |       |
| ⊕ **Correction rate constant**                                                           | **3** |   **4** |  **+7** | **13.2** | **3.30** | **3** |
| ⊕ Correction rate or decay rate                                                          |       |       3 |       0 |     -0.4 |    -0.09 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ update gain ]**                                                                      |       |         |         |          |          |       |
| ▸ ⊕ **update gain**                                                                      | **3** |   **4** |  **+8** | **13.2** | **3.29** | **3** |
| Epistemic gain                                                                           |       |       3 |      -1 |     -2.3 |    -0.57 |     2 |
| Update gain uncertainty ratio principle                                                  |       |       3 |      -2 |     -3.4 |    -0.86 |     2 |
| ⊕ Learning rate                                                                          |       |       3 |      -3 |     -4.0 |    -1.00 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ causal information yield ]**                                                         |       |         |         |          |          |       |
| ▸ **causal information yield**                                                           | **2** |   **4** |  **+8** | **13.1** | **3.26** | **2** |
| ⊕ CIY                                                                                    |     1 |       3 |      +5 |      7.6 |     1.89 |     1 |
| Interventional yield                                                                     |       |       3 |      -1 |     -3.0 |    -0.74 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ agent opacity ]**                                                                    |       |         |         |          |          |       |
| ▸ **agent opacity**                                                                      | **2** |   **3** |  **+6** |  **9.7** | **3.22** | **2** |
| ⊕ Emitter opacity                                                                        |       |       2 |      +1 |      1.7 |     0.57 |     1 |
| Strategic opacity                                                                        |       |       2 |      -1 |     -1.8 |    -0.62 |     1 |
| Legibility inverse                                                                       |       |       2 |      -2 |     -2.4 |    -0.80 |     1 |
| Backward predictive uncertainty                                                          |       |       2 |      -2 |     -2.4 |    -0.81 |     1 |
| Legibility inverted                                                                      |       |       2 |      -2 |     -2.8 |    -0.94 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ directed separation ]**                                                              |       |         |         |          |          |       |
| ▸ **directed separation**                                                                | **5** |   **6** | **+12** | **19.2** | **3.20** | **3** |
| ⊕ Pearl-blanket separation                                                               |       |       5 |       0 |      0.3 |        0 |     2 |
| ⊕ Goal-blind processing                                                                  |       |       5 |       0 |     -0.1 |        0 |     2 |
| Epistemic isolation of belief update                                                     |       |       5 |      -4 |     -6.9 |    -1.15 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ actuated agent ]**                                                                   |       |         |         |          |          |       |
| ▸ **actuated agent**                                                                     | **3** |   **4** |  **+8** | **12.8** | **3.19** | **2** |
| Purposeful agent                                                                         |       |       3 |      +1 |      0.6 |     0.15 |     1 |
| ⊕ Goal actuated agent                                                                    |       |       3 |      -1 |     -2.1 |    -0.54 |     1 |
| Self directed agent                                                                      |       |       3 |      -2 |     -4.0 |    -1.00 |     1 |
| Autonomous agent                                                                         |       |       3 |      -2 |     -4.0 |    -1.00 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ $U_M$ / $U_O$ / $U_\Sigma$ unity dimensions ]**                                      |       |         |         |          |          |       |
| ⊕ **Epistemic unity teleological unity strategic unity**                                 | **2** |   **3** |  **+4** |  **9.6** | **3.19** | **1** |
|                                                                                          |       |         |         |          |          |       |
| **[ logogenic agent ]**                                                                  |       |         |         |          |          |       |
| ▸ **logogenic agent**                                                                    | **2** |   **3** |  **+6** |  **9.5** | **3.16** | **2** |
| Section III logogenic agent                                                              |       |       2 |       0 |     -0.8 |    -0.25 |     1 |
| Linguistic agent                                                                         |       |       2 |      -2 |     -2.8 |    -0.95 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ observability dominance ]**                                                          |       |         |         |          |          |       |
| ▸ **observability dominance**                                                            | **3** |   **4** |  **+7** | **12.6** | **3.16** | **3** |
| ⊕ Epistemic freezing                                                                     |       |       3 |       0 |        0 |        0 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ identifiability floor ]**                                                            |       |         |         |          |          |       |
| ▸ **identifiability floor**                                                              | **2** |   **3** |  **+6** |  **9.4** | **3.14** | **2** |
| Persistence pathology                                                                    |       |       2 |      +2 |      2.6 |     0.86 |     1 |
| Epistemic lower bound                                                                    |       |       2 |       0 |     -1.0 |    -0.33 |     1 |
| Observational limit                                                                      |       |       2 |       0 |     -1.0 |    -0.33 |     1 |
| No-go theorem                                                                            |       |       2 |      -2 |     -2.8 |    -0.92 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ separability pattern ]**                                                             |       |         |         |          |          |       |
| **Separability ladder**                                                                  | **3** |   **4** |  **+8** | **12.5** | **3.13** | **2** |
| ▸ separability pattern                                                                   |       |       3 |       0 |     -1.4 |    -0.35 |     1 |
| Separable core                                                                           |       |       3 |      -3 |     -3.9 |    -0.98 |     1 |
| Separability staircase                                                                   |       |       3 |      -3 |     -4.1 |    -1.02 |     1 |
| Three rung posture                                                                       |       |       3 |      -3 |     -4.7 |    -1.16 |     1 |
| Tiered separability                                                                      |       |       3 |      -3 |     -4.9 |    -1.22 |     1 |
| Staircase                                                                                |       |       3 |      -3 |     -5.0 |    -1.25 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ effect spiral ]**                                                                    |       |         |         |          |          |       |
| ⊕ **Runaway mismatch cascade**                                                           | **1** |   **3** |  **+5** |  **9.4** | **3.12** | **1** |
| ▸ effect spiral                                                                          |     1 |       3 |      +5 |      8.8 |     2.93 |     1 |
| effects spiral                                                                           |       |       1 |      +2 |      4.0 |     1.33 |     1 |
| Adversarial feedback loop                                                                |       |       3 |      -1 |     -2.6 |    -0.86 |     1 |
| Destabilization vortex                                                                   |       |       3 |      -2 |     -3.8 |    -1.26 |     1 |
| Coupling cascade                                                                         |       |       3 |      -3 |     -4.2 |    -1.40 |     1 |
| Breakdown cascade                                                                        |       |       3 |      -3 |     -4.9 |    -1.63 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ causal insufficiency detection ]**                                                   |       |         |         |          |          |       |
| ▸ **causal insufficiency detection**                                                     | **2** |   **3** |  **+5** |  **9.3** | **3.09** | **2** |
| L0 / L1 detection                                                                        |       |       2 |      +2 |      2.8 |     0.95 |     1 |
| Latent cause detection                                                                   |       |       2 |       0 |     -0.8 |    -0.28 |     1 |
| Insufficiency detection                                                                  |       |       2 |      -1 |     -1.9 |    -0.64 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ loop ]**                                                                             |       |         |         |          |          |       |
| ▸ **Loop**                                                                               | **3** |   **4** |  **+7** | **12.3** | **3.08** | **2** |
| ⊕ Feedback loop                                                                          |       |       4 |      -4 |     -6.0 |    -1.51 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ Concept: _agentic system framework ASF top level_ ]**                                |       |         |         |          |          |       |
| **Agentic system framework**                                                             | **3** |   **4** |  **+6** | **12.2** | **3.05** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ $\phi$ ]**                                                                           |       |         |         |          |          |       |
| ⊕ **History compression**                                                                | **2** |   **4** |  **+6** | **12.1** | **3.02** | **3** |
|                                                                                          |       |         |         |          |          |       |
| **[ AAD (Adaptation and Actuation Dynamics) ]**                                          |       |         |         |          |          |       |
| ▸ **AAD (Adaptation and Actuation Dynamics)**                                            | **2** |   **5** |  **+9** | **15.0** | **3.00** | **4** |
| AAD                                                                                      |     2 |       4 |      +7 |     12.3 |     2.45 |     3 |
| AAD agentic adaptation dynamics                                                          |       |       4 |      -3 |     -5.2 |    -1.04 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ observation function ]**                                                             |       |         |         |          |          |       |
| ⊕ **Observation channel**                                                                | **2** |   **4** |  **+6** | **12.0** | **2.99** | **2** |
| ▸ observation function                                                                   |     1 |       4 |      +3 |      6.1 |     1.52 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ evidence starvation ]**                                                              |       |         |         |          |          |       |
| ▸ ⊕ **evidence starvation**                                                              | **2** |   **3** |  **+5** |  **9.0** | **2.99** | **2** |
| Downstream evidence gating                                                               |       |       2 |      +2 |      2.9 |     0.97 |     1 |
| ⊕ Depth attenuated correction                                                            |       |       2 |      +2 |      2.9 |     0.96 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ $R$ (sector-condition radius) ]**                                                    |       |         |         |          |          |       |
| ⊕ **Model-class capacity**                                                               | **2** |   **3** |  **+5** |  **8.9** | **2.95** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ Concept: _agent classes (Class 1 / 2 / 3)_ ]**                                       |       |         |         |          |          |       |
| **Architectural classes**                                                                | **2** |   **4** |  **+6** | **11.7** | **2.92** | **3** |
| ⊕ Proposal assign english modifier                                                       |       |       3 |      +4 |      7.2 |     1.79 |     2 |
| Architecture classes                                                                     |       |       3 |      +3 |      5.9 |     1.48 |     2 |
| Architectural partition                                                                  |       |       3 |      +2 |      4.0 |     1.00 |     2 |
| Goal entanglement hierarchy                                                              |     1 |       3 |      +2 |      3.7 |     0.93 |     2 |
| Modularity partition                                                                     |       |       3 |      +1 |      1.0 |     0.25 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ composition closure ]**                                                              |       |         |         |          |          |       |
| ▸ **composition closure**                                                                | **2** |   **3** |  **+5** |  **8.8** | **2.92** | **2** |
| ⊕ Coarse graining closure                                                                |       |       2 |       0 |     -0.9 |    -0.29 |     1 |
| Closure defect                                                                           |       |       2 |      -1 |     -1.9 |    -0.64 |     1 |
| Macro agent criterion                                                                    |       |       2 |      -2 |     -2.8 |    -0.94 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ gain sector bridge ]**                                                               |       |         |         |          |          |       |
| ▸ **gain sector bridge**                                                                 | **2** |   **3** |  **+6** | **11.7** | **2.92** | **1** |
| The bridge theorem                                                                       |     1 |       4 |      +3 |      5.3 |     1.32 |     2 |
| *(write-in)*                                                                             |       |       1 |      +1 |      2.0 |     0.50 |     1 |
| Bridge theorem from gain to sector                                                       |       |       3 |      -1 |     -2.2 |    -0.54 |     1 |
| Grounding (GA-3) sub-scope α and β                                                       |       |       3 |      -1 |     -2.4 |    -0.60 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Concept: _unnamed the 2×2 table of satisfaction gap vs control regret × goal a…_ ]** |       |         |         |          |          |       |
| **The 2×2 diagnostic**                                                                   | **2** |   **3** |  **+4** |  **8.7** | **2.91** | **1** |
| The cascade diagnostic or the 2×2 diagnostic                                             |       |       3 |      +2 |      3.0 |     0.98 |     1 |
| Diagnostic gap matrix                                                                    |       |       3 |      -1 |     -2.3 |    -0.78 |     1 |
| Diagnostic square                                                                        |       |       3 |      -2 |     -3.7 |    -1.25 |     1 |
| Satisfaction control table the diagnostic 2×2                                            |       |       3 |      -3 |     -3.8 |    -1.27 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ strategy dimension ]**                                                               |       |         |         |          |          |       |
| **Purposeful decomposition**                                                             | **2** |   **4** |  **+7** | **11.6** | **2.90** | **2** |
| Strategy decomposition                                                                   |     1 |       3 |      +3 |      6.3 |     1.58 |     1 |
| Objective strategy split                                                                 |       |       3 |      +3 |      4.2 |     1.04 |     1 |
| ▸ strategy dimension                                                                     |       |       4 |      -1 |     -1.4 |    -0.35 |     2 |
| Purposeful substate                                                                      |       |       3 |      -1 |     -2.3 |    -0.57 |     1 |
| Strategic dimension                                                                      |       |       3 |      -2 |     -3.7 |    -0.94 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ $f_M$ (event-driven update) ]**                                                      |       |         |         |          |          |       |
| ⊕ **Epistemic update function**                                                          | **2** |   **3** |  **+4** |  **8.1** | **2.69** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ temporal nesting ]**                                                                 |       |         |         |          |          |       |
| ▸ **temporal nesting**                                                                   | **2** |   **3** |  **+5** | **10.7** | **2.67** | **1** |
| Timescale nesting                                                                        |     1 |       4 |      +4 |      7.7 |     1.93 |     2 |
| Timescale stratification                                                                 |       |       3 |      -3 |     -4.3 |    -1.06 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ epistemic architecture ]**                                                           |       |         |         |          |          |       |
| ▸ **epistemic architecture**                                                             | **1** |   **3** |  **+5** |  **7.9** | **2.62** | **2** |
| AAD meta architecture                                                                    |     1 |       2 |      +3 |      5.8 |     1.94 |     1 |
| Meta architecture trio                                                                   |       |       2 |      +1 |      1.8 |     0.59 |     1 |
| ⊕ floor / ladder / forced-coordinates                                                    |       |       2 |      +1 |      1.7 |     0.56 |     1 |
| The meta segment triad                                                                   |       |       2 |       0 |     -1.2 |    -0.40 |     1 |
| Four discipline synthesis                                                                |       |       2 |       0 |     -1.4 |    -0.47 |     1 |
| Bounded correction architecture                                                          |       |       2 |      -1 |     -2.4 |    -0.80 |     1 |
| AAD epistemic triptych                                                                   |       |       2 |      -2 |     -2.5 |    -0.84 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ action transition ]**                                                                |       |         |         |          |          |       |
| ▸ **action transition**                                                                  | **4** |   **5** |  **+6** | **12.9** | **2.57** | **3** |
| Action channel                                                                           |       |       5 |      -4 |     -7.2 |    -1.44 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ edge update causal validity ]**                                                      |       |         |         |          |          |       |
| ▸ **edge update causal validity**                                                        | **1** |   **3** |  **+4** |  **7.7** | **2.57** | **2** |
| ⊕ Identification regime                                                                  |     2 |       3 |      +3 |      6.1 |     2.03 |     2 |
| Edge causal validity                                                                     |       |       2 |      +2 |      2.8 |     0.93 |     1 |
| Causal validity                                                                          |       |       2 |       0 |     -0.5 |    -0.15 |     1 |
| Causal edge update                                                                       |       |       2 |       0 |     -0.9 |    -0.30 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ chain confidence decay ]**                                                           |       |         |         |          |          |       |
| ▸ **chain confidence decay**                                                             | **1** |   **3** |  **+5** |  **7.7** | **2.57** | **2** |
| Log confidence additive                                                                  |     1 |       2 |      +1 |      2.1 |     0.69 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ $M_t$ ]**                                                                            |       |         |         |          |          |       |
| ⊕ **Model state or epistemic substate**                                                  | **2** |   **4** |  **+6** | **10.1** | **2.52** | **3** |
|                                                                                          |       |         |         |          |          |       |
| **[ loop interventional access ]**                                                       |       |         |         |          |          |       |
| ▸ **loop interventional access**                                                         | **1** |   **3** |  **+5** |  **7.4** | **2.48** | **2** |
| Loop causal engine                                                                       |     1 |       2 |      +3 |      5.4 |     1.79 |     1 |
| Loop as causal engine                                                                    |       |       2 |      +2 |      2.5 |     0.84 |     1 |
| ⊕ The perpetual experiment                                                               |       |       2 |      +1 |      1.6 |     0.52 |     1 |
| Interventional loop property                                                             |       |       2 |       0 |     -0.7 |    -0.25 |     1 |
| Embodiment upgrade                                                                       |       |       2 |       0 |     -0.9 |    -0.29 |     1 |
| Interventional loop access                                                               |       |       2 |      -1 |     -1.5 |    -0.51 |     1 |
| Interventional character                                                                 |       |       2 |      -1 |     -1.5 |    -0.51 |     1 |
| Adaptive loop access                                                                     |       |       2 |      -1 |     -1.5 |    -0.52 |     1 |
| Interventional feedback                                                                  |       |       2 |      -1 |     -1.9 |    -0.64 |     1 |
| Loop level2 access                                                                       |       |       2 |      -2 |     -2.9 |    -0.97 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ event driven dynamics ]**                                                            |       |         |         |          |          |       |
| ▸ **event driven dynamics**                                                              | **1** |   **3** |  **+4** |  **7.3** | **2.42** | **2** |
| event-driven dynamics                                                                    |     1 |       1 |      +2 |      4.8 |     1.60 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ recursive update ]**                                                                 |       |         |         |          |          |       |
| **Recursive update by completeness**                                                     | **1** |   **3** |  **+4** |  **7.1** | **2.37** | **2** |
| ▸ recursive update                                                                       |     1 |       2 |      +4 |      6.9 |     2.30 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Class 2 ]**                                                                          |       |         |         |          |          |       |
| ⊕ **Merged**                                                                             | **1** |   **3** |  **+5** |  **9.3** | **2.32** | **1** |
| ⊕ Coupled                                                                                |     1 |       3 |      +3 |      4.9 |     1.22 |     1 |
| Class 2                                                                                  |     1 |       1 |      +2 |      4.8 |     1.20 |     1 |
| ⊕ Integrated                                                                             |       |       3 |      -2 |     -3.7 |    -0.91 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ agent identity ]**                                                                   |       |         |         |          |          |       |
| ▸ **agent identity**                                                                     | **2** |   **5** |  **+6** | **11.6** | **2.32** | **3** |
| Causal identity                                                                          |     1 |       4 |      +4 |      7.7 |     1.53 |     2 |
| Singular causal trajectory                                                               |       |       4 |      +2 |      2.8 |     0.56 |     2 |
| Trajectory identity                                                                      |       |       4 |      +1 |      1.9 |     0.37 |     2 |
| Identity as singular causal trajectory                                                   |       |       4 |       0 |     -0.5 |    -0.10 |     2 |
| The trajectory identity scope                                                            |       |       4 |      -2 |     -3.5 |    -0.70 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ the Greek vocabulary ]**                                                             |       |         |         |          |          |       |
| **The greek philosophical vocabulary**                                                   | **1** |   **3** |  **+3** |  **6.9** | **2.31** | **1** |
|                                                                                          |       |         |         |          |          |       |
| **[ $\delta_t$ ]**                                                                       |       |         |         |          |          |       |
| ⊕ **Aporia signal**                                                                      | **1** |   **3** |  **+4** |  **6.9** | **2.31** | **2** |
| ⊕ Mismatch signal                                                                        |     1 |       2 |      +3 |      5.0 |     1.65 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ convention hierarchy ]**                                                             |       |         |         |          |          |       |
| **Continuation hierarchy**                                                               | **2** |   **4** |  **+7** | **11.5** | **2.31** | **2** |
| ▸ convention hierarchy                                                                   |     2 |       5 |      +3 |      6.2 |     1.24 |     3 |
| Evaluation hierarchy                                                                     |       |       4 |      -4 |     -5.9 |    -1.18 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ strategic calibration ]**                                                            |       |         |         |          |          |       |
| ▸ ⊕ **strategic calibration**                                                            | **1** |   **3** |  **+4** |  **6.8** | **2.27** | **2** |
| Strategic calibration residual                                                           |     1 |       2 |      +3 |      5.4 |     1.82 |     1 |
| Strategy calibration                                                                     |       |       2 |      -1 |     -2.0 |    -0.65 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Section I. Adaptive Systems Under Uncertainty ]**                                    |       |         |         |          |          |       |
| **I adaptive system under uncertainty**                                                  | **1** |   **3** |  **+4** |  **6.7** | **2.23** | **2** |
| Adaptive Systems Under Uncertainty                                                       |     1 |       1 |      +2 |      4.8 |     1.60 |     1 |
| Section I adaptive system under uncertainty                                              |       |       2 |      +2 |      3.1 |     1.04 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Concept: _unnamed the pearl-blanket reading of directed separation_ ]**              |       |         |         |          |          |       |
| **Pearl-blanket form**                                                                   | **1** |   **3** |  **+4** |  **6.6** | **2.21** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ per dimension persistence ]**                                                        |       |         |         |          |          |       |
| **Weakest link persistence**                                                             | **1** |   **3** |  **+3** |  **6.5** | **2.18** | **2** |
| Weak link persistence                                                                    |     1 |       2 |      +2 |      4.4 |     1.45 |     1 |
| Dimensional persistence                                                                  |       |       2 |      +2 |      3.0 |     1.00 |     1 |
| ▸ per dimension persistence                                                              |       |       2 |       0 |     -0.7 |    -0.24 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ causal structure ]**                                                                 |       |         |         |          |          |       |
| ▸ **causal structure**                                                                   | **3** |   **5** |  **+5** | **10.7** | **2.14** | **3** |
| temporal precedence                                                                      |     1 |       1 |      +2 |      4.8 |     0.96 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Pearl L1 ]**                                                                         |       |         |         |          |          |       |
| ⊕ **Predicting**                                                                         | **2** |   **3** |  **+3** |  **6.2** | **2.08** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ agent environment ]**                                                                |       |         |         |          |          |       |
| **Agent environment boundary**                                                           | **2** |   **4** |  **+5** | **10.2** | **2.04** | **2** |
| ▸ agent environment                                                                      |     2 |       5 |      +5 |      9.1 |     1.82 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ $M_t$ (reality model) ]**                                                            |       |         |         |          |          |       |
| ⊕ **Working model**                                                                      | **1** |   **3** |  **+3** |  **5.9** | **1.97** | **2** |
| ⊕ Reality model                                                                          |     1 |       1 |      +2 |      4.8 |     1.60 |     1 |
| ⊕ Predictive state                                                                       |       |       2 |      +1 |      1.7 |     0.56 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ $\mathcal{C}_t$ (chronica) ]**                                                       |       |         |         |          |          |       |
| ⊕ **Chronica or interaction history**                                                    | **2** |   **4** |  **+4** |  **7.8** | **1.96** | **3** |
| chronica (complete interaction history)                                                  |     1 |       1 |      +2 |      5.8 |     1.44 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Concept: _unnamed superlinear scaling of adversarial tempo advantage_ ]**            |       |         |         |          |          |       |
| **Superlinear tempo advantage**                                                          | **1** |   **2** |  **+3** |  **5.7** | **1.90** | **1** |
| Boyd's exponent                                                                          |     1 |       3 |      +2 |      3.1 |     1.04 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ Class 1 agent ]**                                                                    |       |         |         |          |          |       |
| **Modular agent**                                                                        | **1** |   **2** |  **+3** |  **5.6** | **1.86** | **1** |
| Class 1                                                                                  |     1 |       1 |      +2 |      4.8 |     1.60 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ value object ]**                                                                     |       |         |         |          |          |       |
| **Policy-conditioned value**                                                             | **1** |   **2** |  **+3** |  **5.3** | **1.76** | **1** |
| ▸ value object                                                                           |     1 |       3 |      +2 |      3.7 |     1.24 |     2 |
| Decision value                                                                           |       |       2 |      +1 |      1.9 |     0.63 |     1 |
| Trajectory value                                                                         |       |       2 |       0 |     -0.3 |    -0.11 |     1 |
| Value functional                                                                         |       |       2 |      -2 |     -2.4 |    -0.79 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ Class 1 ]**                                                                          |       |         |         |          |          |       |
| ⊕ **Modular**                                                                            | **1** |   **2** |  **+3** |  **5.2** | **1.73** | **1** |
| ▸ Class 1                                                                                |     1 |       3 |      +2 |      4.9 |     1.65 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ Class 3 ]**                                                                          |       |         |         |          |          |       |
| ⊕ **Partially coupled**                                                                  | **1** |   **3** |  **+3** |  **6.8** | **1.70** | **1** |
| Class 3                                                                                  |     1 |       1 |      +2 |      4.8 |     1.20 |     1 |
| ⊕ Scaffolded                                                                             |       |       3 |      +1 |      1.0 |     0.25 |     1 |
|                                                                                          |       |         |         |          |          |       |
| **[ chronica brief gloss ]**                                                             |       |         |         |          |          |       |
| ⊕ **complete interaction history**                                                       | **1** |   **1** |  **+2** |  **4.8** | **1.60** | **1** |
| ⊕ Interaction history chronica                                                           |       |       3 |      +1 |      1.3 |     0.44 |     2 |
|                                                                                          |       |         |         |          |          |       |
| **[ Class 2 agent ]**                                                                    |       |         |         |          |          |       |
| **Integrated agent**                                                                     | **1** |   **3** |  **+2** |  **3.6** | **1.21** | **2** |
|                                                                                          |       |         |         |          |          |       |
| **[ Pearl L2 ]**                                                                         |       |         |         |          |          |       |
| ⊕ **Intervening**                                                                        | **1** |   **1** |  **+2** |  **4.8** | **1.20** | **1** |
| ⊕ Exploring                                                                              |     2 |       4 |      +2 |      4.2 |     1.04 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ Pearl L3 ]**                                                                         |       |         |         |          |          |       |
| ⊕ **Counterfactual reasoning**                                                           | **1** |   **1** |  **+2** |  **4.8** | **1.20** | **1** |
| ⊕ Reasoning                                                                              |     1 |       4 |       0 |      0.2 |     0.05 |     3 |
|                                                                                          |       |         |         |          |          |       |
| **[ $U_o$ ]**                                                                            |       |         |         |          |          |       |
| ⊕ **Teleological coherence**                                                             | **1** |   **3** |  **+1** |  **2.7** | **0.91** | **2** |
|                                                                                          |       |         |         |          |          |       |
