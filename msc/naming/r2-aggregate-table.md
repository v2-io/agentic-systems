# R2 Aggregation — Table View

**Generated:** 2026-04-30T21:52:24Z
**Targets included:** 106 (filtered to ≥2 R2 voters from 629 total)
**R2 voters:** codex-r2b, gemini-r2, opus-r2b, opus-r2c, sonnet-r2b, sonnet-r2c

Single unified table. Targets in `**[ ... ]**` brackets, sorted alphabetically. Within each target, candidates are ordered by total substance (leader first). Math renders as math — table cells deliberately do not use backticks so `$inline$` math passes through to the renderer.

Filtered out (default): targets where the only master candidate is the current name (`is_keep`) and no R2 voter wrote in an alternative. These are uncontested keeps — no decision needed. Override with `--include-uncontested-keeps`.

- **Bold row** = leader (highest total substance score)
- **▸** = candidate is the current name in the corpus (`is_keep` from master-list)
- **R1**: synthesized R1 vote on R2 scale ({+2, +1, 0, -1}); blank = no R1 evidence
- **One column per R2 voter**: signed integer weight, blank = did not vote
- **★**: top-pick count across R2 voters
- **subst**: total substance score across R1 + R2 (Jaccard-discounted; see header of detail view)
- **arch**: number of distinct R2 architectures voting on this candidate

See [r2-aggregate-detail.md](r2-aggregate-detail.md) for per-target full vote breakdown, notes, and rationale.

| target / candidate | R1 | codex-r2b | gemini-r2 | opus-r2b | opus-r2c | sonnet-r2b | sonnet-r2c | ★ | subst | arch |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **[ $\alpha$ (sector-condition lower bound) ]** |   |   |   |   |   |   |   |   |   |   |
| **Correction rate constant** | **+1** |  | **+2** |  | **+2** | **+2** |  | **3** | **6.0** | **3** |
| Correction rate or decay rate | 0 |  |  |  | +1 | -1 |  |  | 0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $\delta_t$ ]** |   |   |   |   |   |   |   |   |   |   |
| **Aporia signal** | **+1** |  | **+2** | **+1** |  |  |  | **1** | **3.8** | **2** |
| Mismatch signal | +1 |  |  | +2 |  |  |  | 1 | 2.6 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $\iota_{ij}$ ]** |   |   |   |   |   |   |   |   |   |   |
| **Identifiability coefficient** | **+2** |  | **+2** |  |  |  | **+2** | **2** | **5.6** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $\mathcal C_t$ chronica ]** |   |   |   |   |   |   |   |   |   |   |
| **$\mathcal C_t$** | **+1** | **+2** | **+2** | **+2** |  |  |  | **3** | **6.2** | **3** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $\mathcal{C}_t$ (chronica) ]** |   |   |   |   |   |   |   |   |   |   |
| **Chronica or interaction history** | **+1** | **-1** | **+2** |  | **+2** |  |  | **2** | **3.6** | **3** |
| chronica (complete interaction history) |  | +2 |  |  |  |  |  | 1 | 2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $\phi$ ]** |   |   |   |   |   |   |   |   |   |   |
| **History compression** | **+1** | **+2** | **+2** | **+1** |  |  |  | **2** | **5.8** | **3** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $f_M$ (event-driven update) ]** |   |   |   |   |   |   |   |   |   |   |
| **Epistemic update function** | **0** | **+2** | **+2** |  |  |  |  | **2** | **3.4** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $G_t = (O_t, \Sigma_t)$ ]** |   |   |   |   |   |   |   |   |   |   |
| **Purposeful substate** | **+1** |  |  |  | **+2** |  | **+2** | **2** | **4.6** | **2** |
| Purposeful state | +1 |  |  |  | -1 |  | +1 |  | 0.9 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $H_b$ ]** |   |   |   |   |   |   |   |   |   |   |
| **Agent opacity $H_b$** | **+1** |  | **+2** |  | **+2** |  |  | **1** | **4.9** | **2** |
| Agent opacity | +1 |  |  |  | +2 |  |  | 1 | 2.9 | 1 |
| ▸ $H_b$ | +1 |  |  |  | +1 |  |  |  | 1.9 | 1 |
| Backward opacity | +1 |  |  |  | -1 |  |  |  | 0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $M_t$ ]** |   |   |   |   |   |   |   |   |   |   |
| **Model state or epistemic substate** | **+1** | **+2** | **+2** | **+1** |  |  |  | **2** | **5.1** | **3** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $M_t$ (reality model) ]** |   |   |   |   |   |   |   |   |   |   |
| **Working model** | **0** | **+1** | **+2** |  |  |  |  | **1** | **2.5** | **2** |
| Reality model |  | +2 |  |  |  |  |  | 1 | 2.0 | 1 |
| Predictive state | 0 | +1 |  |  |  |  |  |  | 1.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $R$ (sector-condition radius) ]** |   |   |   |   |   |   |   |   |   |   |
| **Model-class capacity** | **+1** |  | **+2** |  |  | **+2** |  | **2** | **3.4** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $U_M$ ]** |   |   |   |   |   |   |   |   |   |   |
| **Epistemic unity** | **+1** |  | **+2** |  |  |  | **+2** | **2** | **4.4** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $U_M$ / $U_O$ / $U_\Sigma$ unity dimensions ]** |   |   |   |   |   |   |   |   |   |   |
| **Epistemic unity teleological unity strategic unity** | **0** |  |  | **+2** | **+2** |  |  | **2** | **3.4** | **1** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ $U_o$ ]** |   |   |   |   |   |   |   |   |   |   |
| **Teleological coherence** | **0** |  | **+2** |  | **-1** |  |  | **1** | **1.0** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ AAD (acronym) ]** |   |   |   |   |   |   |   |   |   |   |
| **AAD** | **+1** | **+2** | **+2** |  |  |  | **+2** | **3** | **5.8** | **3** |
| Adaptation and purpose dynamics apd | -1 | -1 |  |  |  |  | -1 |  | -2.0 | 2 |
| Adaptation and agency dynamics AAD | -1 | -1 |  |  |  |  | -1 |  | -2.3 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ AAD (Adaptation and Actuation Dynamics) ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **AAD (Adaptation and Actuation Dynamics)** | **+2** | **+2** | **+2** |  | **+1** |  | **+2** | **2** | **8.7** | **4** |
| AAD | +1 | +2 |  |  | +2 |  | +2 | 2 | 5.4 | 3 |
| AAD agentic adaptation dynamics | 0 | -1 |  |  | -1 |  | -1 |  | -2.8 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ action transition ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **action transition** | **+1** | **+1** |  | **+1** | **+1** |  | **+2** | **4** | **5.9** | **3** |
| Action channel | 0 | -1 |  | -1 | -1 |  | -1 |  | -3.6 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ actuated agent ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **actuated agent** | **+2** |  | **+2** |  |  | **+2** | **+2** | **3** | **7.1** | **2** |
| Purposeful agent | +1 |  |  |  |  | -1 | +1 |  | 0.9 | 1 |
| Goal actuated agent | +1 |  |  |  |  | -1 | -1 |  | -0.7 | 1 |
| Autonomous agent | 0 |  |  |  |  | -1 | -1 |  | -2.0 | 1 |
| Self directed agent | 0 |  |  |  |  | -1 | -1 |  | -2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ adaptive cycle ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **adaptive cycle** | **+2** | **+2** | **+2** |  | **+2** |  |  | **3** | **7.4** | **3** |
| The cycle the adaptive cycle | +1 | +1 |  |  | +2 |  |  |  | 3.6 | 2 |
| Feedback cycle | -1 | -1 |  |  | -1 |  |  |  | -2.5 | 2 |
| Correction cycle | -1 | -1 |  |  | -1 |  |  |  | -2.7 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ adaptive tempo ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **adaptive tempo** | **+2** |  | **+2** |  | **+2** | **+2** | **+2** | **4** | **9.0** | **3** |
| tempo | +1 |  |  |  | +1 | +1 | +1 |  | 3.9 | 2 |
| Adaptation rate | -1 |  |  |  | -1 | -1 | -1 |  | -3.7 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ adversarial tempo advantage ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **adversarial tempo advantage** | **+2** |  | **+2** |  |  |  | **+2** | **2** | **5.8** | **2** |
| Superlinear tempo advantage | 0 |  |  |  |  |  | +1 |  | 0.9 | 1 |
| Tempo advantage | 0 |  |  |  |  |  | -1 |  | -0.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Concept: _agent classes (Class 1 / 2 / 3)_ ]** |   |   |   |   |   |   |   |   |   |   |
| **Architectural classes** | **+1** |  | **+2** |  | **+1** | **+2** |  | **2** | **5.5** | **3** |
| Proposal assign english modifier | 0 |  |  |  | +2 | +2 |  |  | 3.4 | 2 |
| Architecture classes | +1 |  |  |  | +1 | +1 |  |  | 3.0 | 2 |
| Goal entanglement hierarchy | +1 |  |  |  | +2 | -1 |  | 1 | 1.9 | 2 |
| Architectural partition | 0 |  |  |  | +1 | +1 |  |  | 1.8 | 2 |
| Modularity partition | +1 |  |  |  | -1 | +1 |  |  | 1.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ agent environment ]** |   |   |   |   |   |   |   |   |   |   |
| **Agent environment boundary** | **0** | **+2** |  | **+2** | **+1** |  |  | **2** | **4.4** | **2** |
| ▸ agent environment | +2 | +1 | +2 | -1 | +1 |  |  | 2 | 4.3 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ agent identity ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **agent identity** | **+2** |  | **+2** |  | **+1** | **-1** | **+2** | **2** | **5.8** | **3** |
| Causal identity | 0 |  |  |  | +1 | +2 | +1 | 1 | 3.5 | 2 |
| Singular causal trajectory | +1 |  |  |  | -1 | +1 | +1 |  | 1.9 | 2 |
| Trajectory identity | 0 |  |  |  | -1 | +1 | +1 |  | 0.9 | 2 |
| Identity as singular causal trajectory | +1 |  |  |  | -1 | -1 | +1 |  | 0.2 | 2 |
| The trajectory identity scope | +1 |  |  |  | -1 | -1 | -1 |  | -1.8 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ agent model ]** |   |   |   |   |   |   |   |   |   |   |
| **Reality model** | **+1** | **+2** | **+2** | **+2** |  | **+2** |  | **4** | **8.3** | **4** |
| ▸ agent model | +1 | -1 |  | -1 |  | -1 |  |  | -2.0 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ agent opacity ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **agent opacity** | **+2** |  | **+2** |  | **+2** |  |  | **2** | **5.6** | **2** |
| Emitter opacity | 0 |  |  |  | +1 |  |  |  | 0.8 | 1 |
| Strategic opacity | 0 |  |  |  | -1 |  |  |  | -0.9 | 1 |
| Legibility inverse | -1 |  |  |  | -1 |  |  |  | -1.4 | 1 |
| Backward predictive uncertainty | -1 |  |  |  | -1 |  |  |  | -1.9 | 1 |
| Legibility inverted | -1 |  |  |  | -1 |  |  |  | -1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ agent spectrum ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **agent spectrum** | **+2** |  | **+2** |  | **+2** | **+2** | **+2** | **4** | **9.3** | **3** |
| Agency spectrum | 0 |  |  |  | +1 | -1 | +1 |  | 0.9 | 2 |
| Agent quadrant | -1 |  |  |  | -1 | -1 | -1 |  | -3.5 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Concept: _agentic system framework ASF top level_ ]** |   |   |   |   |   |   |   |   |   |   |
| **Agentic system framework** | **0** |  | **+2** | **+2** | **+2** |  |  | **3** | **4.9** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ aisthesis ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **aisthesis** | **+1** |  | **+2** | **+2** | **+2** |  |  | **3** | **6.5** | **2** |
| Aisthesis observation alignment | +1 |  |  | -1 | -1 |  |  |  | -0.6 | 1 |
| Intake | -1 |  |  | -1 | -1 |  |  |  | -2.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ aporia ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **aporia** | **+2** |  | **+2** | **+2** | **+2** |  |  | **3** | **7.8** | **2** |
| Aporia productive perplexity | +1 |  |  | +1 | -1 |  |  |  | 0.9 | 1 |
| Discrepancy | -1 |  |  | -1 | -1 |  |  |  | -2.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ aporia prolepsis aisthesis epistrophe praxis ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **aporia prolepsis aisthesis epistrophe praxis** | **+1** |  |  | **+2** |  |  | **+2** | **2** | **4.7** | **2** |
| Greek rooted vocabulary | +1 |  |  | +1 |  |  | +1 |  | 3.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ ASF (acronym) ]** |   |   |   |   |   |   |   |   |   |   |
| **ASF** | **+1** | **+2** | **+2** |  | **+2** |  | **+2** | **4** | **8.5** | **4** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ calibration laboratory ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **calibration laboratory** | **+2** | **+2** |  | **+2** | **+2** |  |  | **3** | **7.2** | **2** |
| Software as calibration laboratory | +1 | +1 |  | +1 | +1 |  |  |  | 3.9 | 2 |
| Calibration laboratory move | +1 | +1 |  | +1 | +1 |  |  |  | 3.8 | 2 |
| Software calibration laboratory | +1 |  |  | +1 | -1 |  |  |  | 1.0 | 1 |
| Privileged grounding domain | +1 |  |  | -1 | -1 |  |  |  | -0.8 | 1 |
| Calibration domain | 0 | +1 |  | -1 | -1 |  |  |  | -0.8 | 2 |
| Privileged calibration domain | +1 |  |  | -1 | -1 |  |  |  | -0.9 | 1 |
| High identifiability testbed | +1 |  |  | -1 | -1 |  |  |  | -1.0 | 1 |
| Calibration domain calibration lab | 0 |  |  | -1 | -1 |  |  |  | -1.4 | 1 |
| Epistemic laboratory framing | 0 |  |  | -1 | -1 |  |  |  | -1.8 | 1 |
| Calibration lab framing | 0 |  |  | -1 | -1 |  |  |  | -1.9 | 1 |
| High identifiability calibration lab | 0 |  |  | -1 | -1 |  |  |  | -2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ causal information yield ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **causal information yield** | **+2** |  | **+2** |  |  | **+2** | **+2** | **2** | **7.3** | **2** |
| CIY | +1 |  |  |  |  | +2 | +2 | 1 | 4.3 | 1 |
| Interventional yield | +1 |  |  |  |  | -1 | -1 |  | -1.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ causal insufficiency detection ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **causal insufficiency detection** | **+1** |  | **+2** |  |  |  | **+2** | **2** | **4.7** | **2** |
| L0 / L1 detection | +1 |  |  |  |  |  | +1 |  | 2.0 | 1 |
| Latent cause detection | +1 |  |  |  |  |  | -1 |  | 0 | 1 |
| Insufficiency detection | 0 |  |  |  |  |  | -1 |  | -1.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ causal structure ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **causal structure** | **+1** | **+2** | **+2** | **-1** | **+1** |  |  | **3** | **4.8** | **3** |
| temporal precedence |  |  |  | +2 |  |  |  | 1 | 2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ chain confidence decay ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **chain confidence decay** | **+2** |  | **+2** |  | **+1** |  |  | **1** | **4.8** | **2** |
| Log confidence additive | 0 |  |  |  | +1 |  |  | 1 | 0.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ chronica ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **chronica** | **+2** | **+2** | **+2** | **+2** | **+2** |  | **+2** | **5** | **10.9** | **4** |
| Lowercase italic chronica | 0 | +1 |  | +1 | +1 |  | +1 |  | 3.6 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ chronica brief gloss ]** |   |   |   |   |   |   |   |   |   |   |
| **complete interaction history** |  | **+2** |  |  |  |  |  | **1** | **2.0** | **1** |
| Interaction history chronica | +1 | -1 |  | +1 |  |  |  |  | 1.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ chronica capitalized vs lowercase ]** |   |   |   |   |   |   |   |   |   |   |
| **Chronica lowercase in running prose** | **0** | **+2** |  | **+2** | **+2** |  |  | **3** | **5.4** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Class 1 ]** |   |   |   |   |   |   |   |   |   |   |
| **Modular** | **+1** |  |  |  | **+2** |  |  | **1** | **2.7** | **1** |
| ▸ Class 1 | -1 |  | +2 |  | +1 |  |  | 1 | 1.9 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Class 1 agent ]** |   |   |   |   |   |   |   |   |   |   |
| **Modular agent** | **+1** |  |  |  |  |  | **+2** | **1** | **2.9** | **1** |
| Class 1 |  |  | +2 |  |  |  |  | 1 | 2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Class 2 ]** |   |   |   |   |   |   |   |   |   |   |
| **Merged** | **+1** |  |  | **+2** | **+2** |  |  | **1** | **4.8** | **1** |
| Coupled | +1 |  |  | +1 | +1 |  |  | 1 | 2.8 | 1 |
| Class 2 |  |  | +2 |  |  |  |  | 1 | 2.0 | 1 |
| Integrated | 0 |  |  | -1 | -1 |  |  |  | -1.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Class 2 agent ]** |   |   |   |   |   |   |   |   |   |   |
| **Integrated agent** | **+1** |  |  | **-1** |  |  | **+2** | **1** | **1.9** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Class 3 ]** |   |   |   |   |   |   |   |   |   |   |
| **Partially coupled** | **0** |  |  | **+1** | **+2** |  |  | **1** | **3.0** | **1** |
| Class 3 |  |  | +2 |  |  |  |  | 1 | 2.0 | 1 |
| Scaffolded | +1 |  |  | +1 | -1 |  |  |  | 1.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ complete agent state ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **complete agent state** | **+2** |  |  |  | **+2** | **+2** | **+2** | **3** | **7.3** | **2** |
| Purposeful state | +1 |  |  |  | -1 | -1 | -1 |  | -1.3 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ composition closure ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **composition closure** | **+1** |  | **+2** |  | **+2** |  |  | **2** | **4.8** | **2** |
| Coarse graining closure | +1 |  |  |  | -1 |  |  |  | 0.1 | 1 |
| Closure defect | 0 |  |  |  | -1 |  |  |  | -1.0 | 1 |
| Macro agent criterion | -1 |  |  |  | -1 |  |  |  | -1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ composition consistency ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **composition consistency** | **+2** | **+2** |  | **+2** | **+2** |  |  | **3** | **7.7** | **2** |
| Cross level coherence | 0 | +1 |  | -1 | -1 |  |  |  | -1.0 | 2 |
| Scale invariance of adaptive dynamics | 0 | -1 |  | -1 | -1 |  |  |  | -2.8 | 2 |
| Scale invariance | 0 | -1 |  | -1 | -1 |  |  |  | -2.9 | 2 |
| Holon postulate | 0 | -1 |  | -1 | -1 |  |  |  | -3.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ continuity persistence ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **continuity persistence** | **+1** | **+2** |  |  | **+1** | **+2** | **+2** | **4** | **7.6** | **3** |
| Identity continuity | +1 | +1 |  |  | -1 | -1 | +1 |  | 1.0 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ control regret ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **control regret** | **+2** |  | **+2** | **+2** | **+2** | **+2** | **+2** | **5** | **10.7** | **3** |
| Strategy opportunity cost | -1 |  |  | -1 | -1 | -1 | -1 |  | -4.8 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ convention hierarchy ]** |   |   |   |   |   |   |   |   |   |   |
| **Continuation hierarchy** | **+1** |  |  |  | **+2** | **+2** | **+2** | **2** | **6.1** | **2** |
| ▸ convention hierarchy | +1 |  | +2 |  | -1 | -1 | +2 | 2 | 2.8 | 3 |
| Evaluation hierarchy | -1 |  |  |  | -1 | -1 | -1 |  | -3.1 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ correlation hierarchy ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **correlation hierarchy** | **+1** |  |  |  | **+2** | **+2** | **+2** | **3** | **6.5** | **2** |
| Correlation hierarchy L0 / L1 / L1' / L2 | +1 |  |  |  | +1 | +1 | +1 |  | 3.8 | 2 |
| Correlation ladder | +1 |  |  |  | -1 | +1 | +1 |  | 1.9 | 2 |
| Predicting exploring reasoning triad | +1 |  |  |  | -1 | -1 | -1 |  | -1.5 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ credit assignment boundary ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **credit assignment boundary** | **+2** |  | **+2** |  |  |  | **+2** | **2** | **5.9** | **2** |
| Credit assignment frontier | 0 |  |  |  |  |  | +1 |  | 0.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ deliberation cost ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **deliberation cost** | **+2** |  | **+2** |  |  |  | **+2** | **2** | **5.8** | **2** |
| The simulation tax | +1 |  |  |  |  |  | +1 |  | 1.9 | 1 |
| Deliberation threshold | 0 |  |  |  |  |  | +1 |  | 0.9 | 1 |
| Deliberation drag | 0 |  |  |  |  |  | +1 |  | 0.9 | 1 |
| Think vs act tradeoff | 0 |  |  |  |  |  | -1 |  | -0.6 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ derivation not proof ]** |   |   |   |   |   |   |   |   |   |   |
| **Derivation** | **+1** | **+2** | **+2** |  | **+2** |  |  | **3** | **6.4** | **3** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ directed separation ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **directed separation** | **+2** |  | **+2** | **+2** | **+2** | **+2** | **+2** | **5** | **10.1** | **3** |
| Pearl-blanket separation | 0 |  |  | -1 | +1 | +1 | -1 |  | 0.2 | 2 |
| Goal-blind processing | 0 |  |  | -1 | -1 | +1 | +1 |  | -0.1 | 2 |
| Epistemic isolation of belief update | 0 |  |  | -1 | -1 | -1 | -1 |  | -2.8 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ directional fidelity ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **directional fidelity** | **+2** |  | **+2** |  |  |  | **+2** | **2** | **5.7** | **2** |
| Pointing condition | 0 |  |  |  |  |  | -1 |  | -1.0 | 1 |
| Correction direction integrity | -1 |  |  |  |  |  | -1 |  | -1.8 | 1 |
| Corrective alignment | -1 |  |  |  |  |  | -1 |  | -1.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ edge update causal validity ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **edge update causal validity** | **+1** |  | **+2** |  |  |  | **+1** | **1** | **3.9** | **2** |
| Identification regime | 0 |  | +1 |  |  |  | +2 | 2 | 2.6 | 2 |
| Edge causal validity | +1 |  |  |  |  |  | +1 |  | 1.8 | 1 |
| Causal validity | +1 |  |  |  |  |  | -1 |  | 0.1 | 1 |
| Causal edge update | +1 |  |  |  |  |  | -1 |  | 0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ effect spiral ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **effect spiral** | **+2** |  |  | **+1** | **+2** |  |  | **1** | **4.8** | **1** |
| Runaway mismatch cascade | +1 |  |  | +2 | +2 |  |  | 1 | 4.8 | 1 |
| effects spiral |  |  |  | +2 |  |  |  |  | 2.0 | 1 |
| Adversarial feedback loop | +1 |  |  | -1 | -1 |  |  |  | -0.8 | 1 |
| Destabilization vortex | 0 |  |  | -1 | -1 |  |  |  | -1.1 | 1 |
| Breakdown cascade | -1 |  |  | -1 | -1 |  |  |  | -2.1 | 1 |
| Coupling cascade | -1 |  |  | -1 | -1 |  |  |  | -2.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ epistemic architecture ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **epistemic architecture** | **+2** |  | **+2** |  |  | **+1** |  | **1** | **4.9** | **2** |
| AAD meta architecture | +1 |  |  |  |  | +2 |  | 1 | 2.8 | 1 |
| floor / ladder / forced-coordinates | 0 |  |  |  |  | +1 |  |  | 1.0 | 1 |
| Meta architecture trio | 0 |  |  |  |  | +1 |  |  | 0.8 | 1 |
| The meta segment triad | +1 |  |  |  |  | -1 |  |  | 0.3 | 1 |
| Four discipline synthesis | +1 |  |  |  |  | -1 |  |  | 0 | 1 |
| Bounded correction architecture | 0 |  |  |  |  | -1 |  |  | -1.0 | 1 |
| AAD epistemic triptych | -1 |  |  |  |  | -1 |  |  | -1.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ event driven dynamics ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **event driven dynamics** | **+1** | **+1** | **+2** |  |  |  |  | **1** | **3.6** | **2** |
| event-driven dynamics |  | +2 |  |  |  |  |  | 1 | 2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ evidence starvation ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **evidence starvation** | **+1** |  | **+2** |  |  |  | **+2** | **2** | **4.7** | **2** |
| Downstream evidence gating | +1 |  |  |  |  |  | +1 |  | 2.0 | 1 |
| Depth attenuated correction | +1 |  |  |  |  |  | +1 |  | 1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ exact / robust-qualitative / heuristic / conditional (claim tier) ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **exact / robust-qualitative / heuristic / conditional (clai…** | **+1** | **+2** |  |  | **+2** |  |  | **2** | **4.5** | **2** |
| Epistemic claim tier | +1 | +2 |  |  | +1 |  |  |  | 3.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ formulation / definition / result / ... (segment types) ]** |   |   |   |   |   |   |   |   |   |   |
| **Formulation definition result etc segment type** | **+1** | **+2** |  |  | **+2** |  |  | **2** | **4.4** | **2** |
| Segment typology | +1 | +1 |  |  | +1 |  |  |  | 2.9 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ gain sector bridge ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **gain sector bridge** | **+2** |  |  |  |  | **+2** | **+2** | **2** | **5.9** | **1** |
| The bridge theorem | +1 |  | +2 |  |  | -1 | +1 | 1 | 2.8 | 2 |
| *(write-in)* |  |  |  |  |  | +1 |  |  | 1.0 | 1 |
| Bridge theorem from gain to sector | +1 |  |  |  |  | -1 | -1 |  | -0.6 | 1 |
| Grounding (GA-3) sub-scope α and β | +1 |  |  |  |  | -1 | -1 |  | -0.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ identifiability floor ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **identifiability floor** | **+2** |  | **+2** |  | **+2** |  |  | **2** | **5.5** | **2** |
| Persistence pathology | +1 |  |  |  | +1 |  |  |  | 1.9 | 1 |
| Epistemic lower bound | +1 |  |  |  | -1 |  |  |  | 0 | 1 |
| Observational limit | +1 |  |  |  | -1 |  |  |  | 0 | 1 |
| No-go theorem | -1 |  |  |  | -1 |  |  |  | -1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ information bottleneck ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **information bottleneck** | **+2** | **+2** | **+2** | **+2** |  |  |  | **3** | **7.4** | **3** |
| Epistemic bottleneck | 0 | -1 |  | -1 |  |  |  |  | -2.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ logogenic agent ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **logogenic agent** | **+2** |  | **+2** | **+2** |  |  |  | **2** | **5.7** | **2** |
| Section III logogenic agent | +1 |  |  | -1 |  |  |  |  | 0 | 1 |
| Linguistic agent | -1 |  |  | -1 |  |  |  |  | -1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ logogenic logozoetic ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **logogenic logozoetic** | **+2** | **+2** |  | **+2** |  |  | **+2** | **3** | **7.3** | **3** |
| Logogenic logozoetic distinction | +1 | +2 |  | +1 |  |  | +1 |  | 4.1 | 3 |
| Language constituted language living | -1 | -1 |  | -1 |  |  | -1 |  | -3.3 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ loop ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **Loop** | **+1** | **+2** |  | **+2** | **+2** |  |  | **3** | **5.8** | **2** |
| Feedback loop | -1 | -1 |  | -1 | -1 |  |  |  | -3.6 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ loop interventional access ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **loop interventional access** | **+2** |  | **+2** |  | **+1** |  |  | **1** | **4.9** | **2** |
| Loop causal engine | +1 |  |  |  | +2 |  |  | 1 | 2.8 | 1 |
| Loop as causal engine | +1 |  |  |  | +1 |  |  |  | 1.9 | 1 |
| The perpetual experiment | 0 |  |  |  | +1 |  |  |  | 0.9 | 1 |
| Embodiment upgrade | +1 |  |  |  | -1 |  |  |  | 0.2 | 1 |
| Interventional loop property | +1 |  |  |  | -1 |  |  |  | 0 | 1 |
| Interventional loop access | 0 |  |  |  | -1 |  |  |  | -0.5 | 1 |
| Adaptive loop access | 0 |  |  |  | -1 |  |  |  | -0.7 | 1 |
| Interventional character | 0 |  |  |  | -1 |  |  |  | -0.9 | 1 |
| Interventional feedback | 0 |  |  |  | -1 |  |  |  | -1.0 | 1 |
| Loop level2 access | -1 |  |  |  | -1 |  |  |  | -2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ mismatch dynamics ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **mismatch dynamics** | **+1** |  | **+2** |  |  |  | **+2** | **2** | **4.8** | **2** |
| Mismatch dynamics drift and noise regime | 0 |  |  |  |  |  | -1 |  | -1.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ mismatch signal ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **mismatch signal** | **+2** |  | **+2** | **+2** | **+2** |  | **+2** | **4** | **9.0** | **3** |
| Aporia signal | -1 |  |  | +1 | +1 |  | +1 |  | 1.7 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ model sufficiency ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **model sufficiency** | **+2** | **+2** | **+2** |  |  | **+2** |  | **3** | **7.4** | **3** |
| Predictive sufficiency | +1 | +1 |  |  |  | +1 |  |  | 2.9 | 2 |
| Predictive information retention | 0 | +1 |  |  |  | -1 |  |  | 0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ model-class fitness ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **model-class fitness** | **+2** | **+2** | **+2** |  |  | **+2** |  | **3** | **7.3** | **3** |
| Class capacity ceiling | 0 | +1 |  |  |  | +1 |  |  | 1.8 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ objective functional ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **objective functional** | **+1** |  | **+2** |  |  | **+2** | **+2** | **3** | **6.8** | **2** |
| Teleological objective | 0 |  |  |  |  | -1 | -1 |  | -1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ observability dominance ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **observability dominance** | **+1** |  | **+2** |  | **+2** |  | **+2** | **3** | **6.5** | **3** |
| Epistemic freezing | 0 |  |  |  | +1 |  | -1 |  | 0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ observation function ]** |   |   |   |   |   |   |   |   |   |   |
| **Observation channel** | **+1** | **+1** |  | **+2** | **+2** |  |  | **2** | **5.7** | **2** |
| ▸ observation function | +1 | +2 |  | -1 | +1 |  |  | 1 | 3.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ orient cascade ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **orient cascade** | **+2** |  | **+2** | **+2** | **+2** | **+2** | **+2** | **5** | **10.7** | **3** |
| The adaptive pentad | +1 |  |  | +1 | -1 | -1 | +1 |  | 0.8 | 2 |
| The pentad | 0 |  |  | +1 | -1 | -1 | +1 |  | 0.1 | 2 |
| Adaptive cycle | +1 |  |  | -1 | -1 | -1 | +1 |  | -1.2 | 2 |
| Adaptive cycle phase | +1 |  |  | -1 | -1 | -1 | -1 |  | -2.0 | 2 |
| Five adaptive cycle phase | +1 |  |  | -1 | -1 | -1 | -1 |  | -2.4 | 2 |
| The pentad five phase cycle | 0 |  |  | -1 | -1 | -1 | -1 |  | -2.7 | 2 |
| The five turn | -1 |  |  | -1 | -1 | -1 | -1 |  | -2.8 | 2 |
| Adaptive traversal | 0 |  |  | -1 | -1 | -1 | -1 |  | -3.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Pearl causal hierarchy ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **Pearl causal hierarchy** | **+2** | **+2** | **+2** | **+2** | **+2** |  | **+2** | **5** | **10.6** | **4** |
| Causal hierarchy level | +1 | +1 |  | -1 | -1 |  | -1 |  | -0.7 | 3 |
| Causal hierarchy | 0 | +1 |  | -1 | -1 |  | -1 |  | -1.9 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Pearl L1 ]** |   |   |   |   |   |   |   |   |   |   |
| **Predicting** | **0** | **+2** |  |  | **+1** |  |  | **2** | **2.6** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Pearl L2 ]** |   |   |   |   |   |   |   |   |   |   |
| **Exploring** | **0** | **-1** | **+2** |  | **+1** |  |  | **2** | **1.6** | **3** |
| Intervening |  | +2 |  |  |  |  |  | 1 | 1.5 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Pearl L3 ]** |   |   |   |   |   |   |   |   |   |   |
| **Counterfactual reasoning** |  | **+2** |  |  |  |  |  | **1** | **2.0** | **1** |
| Reasoning | 0 | -1 | +2 |  | -1 |  |  | 1 | -0.2 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ per dimension persistence ]** |   |   |   |   |   |   |   |   |   |   |
| **Weakest link persistence** | **0** |  | **+2** |  |  | **+1** |  | **1** | **2.9** | **2** |
| Dimensional persistence | +1 |  |  |  |  | +1 |  |  | 2.0 | 1 |
| Weak link persistence | 0 |  |  |  |  | +2 |  | 1 | 1.8 | 1 |
| ▸ per dimension persistence | +1 |  |  |  |  | -1 |  |  | 0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ persistence condition ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **persistence condition** | **+2** |  | **+2** |  | **+2** |  | **+2** | **3** | **7.5** | **3** |
| Survival equation | 0 |  |  |  | +1 |  | +1 |  | 1.5 | 2 |
| The survival equation | +1 |  |  |  | -1 |  | +1 |  | 1.0 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ postulate not axiom ]** |   |   |   |   |   |   |   |   |   |   |
| **Postulate** | **+1** | **+2** |  |  | **+2** |  |  | **2** | **5.0** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ prolepsis ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **prolepsis** | **+2** |  | **+2** |  | **+2** |  |  | **2** | **5.7** | **2** |
| Prolepsis anticipatory projection | +1 |  |  |  | -1 |  |  |  | 0.8 | 1 |
| Anticipation | -1 |  |  |  | -1 |  |  |  | -1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ recursive update ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **recursive update** | **+2** | **+2** |  |  |  |  |  | **1** | **3.9** | **1** |
| Recursive update by completeness | +1 | +1 | +2 |  |  |  |  | 1 | 3.8 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ satisfaction gap ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **satisfaction gap** | **+2** |  | **+2** | **+2** | **+2** | **+2** | **+2** | **5** | **10.9** | **3** |
| Attainability shortfall | -1 |  |  | -1 | -1 | -1 | -1 |  | -4.8 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Section I. Adaptive Systems Under Uncertainty ]** |   |   |   |   |   |   |   |   |   |   |
| **I adaptive system under uncertainty** | **+1** | **+1** | **+2** |  |  |  |  | **1** | **3.7** | **2** |
| Adaptive Systems Under Uncertainty |  | +2 |  |  |  |  |  | 1 | 2.0 | 1 |
| Section I adaptive system under uncertainty | +1 | +1 |  |  |  |  |  |  | 2.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ sector condition ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **sector condition** | **+2** |  |  |  | **+2** |  | **+2** | **2** | **5.6** | **2** |
| Continuous sector condition | +1 |  |  |  | -1 |  | +1 |  | 0.9 | 2 |
| sector condition derivation | 0 |  |  |  | -1 |  | +1 |  | -0.2 | 2 |
| Correction sector | 0 |  |  |  | -1 |  | -1 |  | -1.8 | 2 |
| Persistence condition | 0 |  |  |  | -1 |  | -1 |  | -1.9 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ separability pattern ]** |   |   |   |   |   |   |   |   |   |   |
| **Separability ladder** | **+2** |  | **+2** | **+2** | **+2** |  |  | **3** | **7.0** | **2** |
| ▸ separability pattern | +2 |  |  | -1 | -1 |  |  |  | 0.1 | 1 |
| Tiered separability | -1 |  |  | -1 | -1 |  |  |  | -2.3 | 1 |
| Separability staircase | -1 |  |  | -1 | -1 |  |  |  | -2.4 | 1 |
| Separable core | -1 |  |  | -1 | -1 |  |  |  | -2.6 | 1 |
| Staircase | -1 |  |  | -1 | -1 |  |  |  | -2.8 | 1 |
| Three rung posture | -1 |  |  | -1 | -1 |  |  |  | -2.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ strategic calibration ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **strategic calibration** | **+1** |  | **+2** |  |  |  | **+1** | **1** | **3.9** | **2** |
| Strategic calibration residual | +1 |  |  |  |  |  | +2 | 1 | 2.8 | 1 |
| Strategy calibration | 0 |  |  |  |  |  | -1 |  | -1.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ strategy dimension ]** |   |   |   |   |   |   |   |   |   |   |
| **Purposeful decomposition** | **+1** |  | **+2** |  |  | **+2** | **+2** | **2** | **6.1** | **2** |
| Objective strategy split | +1 |  |  |  |  | +1 | +1 |  | 2.8 | 1 |
| Strategy decomposition | 0 |  |  |  |  | +1 | +2 | 1 | 2.8 | 1 |
| ▸ strategy dimension | 0 |  | -1 |  |  | -1 | +1 |  | -0.3 | 2 |
| Purposeful substate | +1 |  |  |  |  | -1 | -1 |  | -0.7 | 1 |
| Strategic dimension | 0 |  |  |  |  | -1 | -1 |  | -1.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ structural adaptation necessity ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **structural adaptation necessity** | **+1** |  |  |  |  | **+2** | **+2** | **2** | **4.6** | **1** |
| Adaptation necessity | +1 |  |  |  |  | -1 | -1 |  | -0.9 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Concept: _structural persistence operational persistence continuity persistence_ ]** |   |   |   |   |   |   |   |   |   |   |
| **Persistence taxonomy** | **+1** | **+2** | **+2** |  | **+2** |  | **+1** | **3** | **7.4** | **4** |
| Structural operational continuity persistence | +1 | +2 |  |  | +2 |  | +2 | 1 | 6.3 | 3 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Concept: _symbol default m t in prose_ ]** |   |   |   |   |   |   |   |   |   |   |
| **Model state** | **0** | **+2** | **+2** |  |  | **+2** |  | **3** | **5.7** | **3** |
| Epistemic substate | +1 | +1 |  |  |  | +1 |  |  | 2.8 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ temporal nesting ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **temporal nesting** | **+1** |  |  |  |  | **+2** | **+2** | **2** | **5.0** | **1** |
| Timescale nesting | 0 |  | +2 |  |  | +1 | +1 | 1 | 3.7 | 2 |
| Timescale stratification | -1 |  |  |  |  | -1 | -1 |  | -2.6 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ temporal software theory ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **temporal software theory** | **+2** |  |  | **+2** | **+2** |  |  | **2** | **5.9** | **1** |
| Temporal Software Theory (TST) | +1 |  |  | +1 | +1 |  |  |  | 3.0 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ the Greek vocabulary ]** |   |   |   |   |   |   |   |   |   |   |
| **The greek philosophical vocabulary** | **0** |  |  | **+1** | **+2** |  |  | **1** | **2.7** | **1** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Concept: _unnamed superlinear scaling of adversarial tempo advantage_ ]** |   |   |   |   |   |   |   |   |   |   |
| **Superlinear tempo advantage** | **+1** |  |  |  |  |  | **+2** | **1** | **3.0** | **1** |
| Boyd's exponent | +1 |  | +2 |  |  |  | -1 | 1 | 1.7 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Concept: _unnamed the 2×2 table of satisfaction gap vs control regret × goal a…_ ]** |   |   |   |   |   |   |   |   |   |   |
| **The 2×2 diagnostic** | **0** |  |  |  |  | **+2** | **+2** | **2** | **3.6** | **1** |
| The cascade diagnostic or the 2×2 diagnostic | 0 |  |  |  |  | +1 | +1 |  | 1.8 | 1 |
| Diagnostic gap matrix | +1 |  |  |  |  | -1 | -1 |  | -1.0 | 1 |
| Diagnostic square | 0 |  |  |  |  | -1 | -1 |  | -1.2 | 1 |
| Satisfaction control table the diagnostic 2×2 | -1 |  |  |  |  | -1 | -1 |  | -2.2 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ Concept: _unnamed the pearl-blanket reading of directed separation_ ]** |   |   |   |   |   |   |   |   |   |   |
| **Pearl-blanket form** | **+1** |  |  | **+1** |  |  | **+2** | **1** | **3.5** | **2** |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ update gain ]** |   |   |   |   |   |   |   |   |   |   |
| ▸ **update gain** | **+2** |  | **+2** |  | **+2** |  | **+2** | **3** | **7.3** | **3** |
| Epistemic gain | +1 |  |  |  | -1 |  | -1 |  | -0.8 | 2 |
| Update gain uncertainty ratio principle | 0 |  |  |  | -1 |  | -1 |  | -1.9 | 2 |
| Learning rate | -1 |  |  |  | -1 |  | -1 |  | -2.7 | 2 |
|   |   |   |   |   |   |   |   |   |   |   |
| **[ value object ]** |   |   |   |   |   |   |   |   |   |   |
| **Policy-conditioned value** | **+1** |  |  |  |  | **+2** |  | **1** | **2.8** | **1** |
| ▸ value object | +1 |  | +2 |  |  | -1 |  | 1 | 1.9 | 2 |
| Decision value | 0 |  |  |  |  | +1 |  |  | 0.9 | 1 |
| Trajectory value | +1 |  |  |  |  | -1 |  |  | 0.2 | 1 |
| Value functional | -1 |  |  |  |  | -1 |  |  | -1.8 | 1 |
|   |   |   |   |   |   |   |   |   |   |   |
