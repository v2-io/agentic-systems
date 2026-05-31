---
slug: def-strategic-calibration
type: definition
status: discussion-grade
depends:
  - def-strategy-dag
  - def-value-object
stage: draft
---

# Definition: Strategic Calibration

A fine-grained companion to control regret ( #def-control-regret), locating where in the strategy DAG miscalibration lives. The **edge residual** $r_{ij}$ for each edge is the difference between the predicted value increment from completing the parent step (as predicted by $\Sigma_t$) and the observed value change attributable to that step. The **strategic calibration residual** $\delta_{\text{strategic}}$ is an $L^2$ aggregation over active edges with importance weighting (e.g., criticality on the plan's critical path). Where the control regret says *how much* value is being left on the table, the strategic calibration residual says *which edges* are miscalibrated.

The framework is honest about conditions and limitations. The edge residual is meaningful only when the edge was actually traversed, the model is adequate (so observed value changes are signal rather than noise), and the agent followed the strategy's prescription (otherwise the residual conflates a bad plan with bad execution). The status is discussion-grade because the specific $L^2$ aggregation and the importance weighting are sensible first passes but not derived, and the conditioning requirements make the quantity hard to estimate in practice. A careful distinction separates $\delta_{\text{strategic}}$ from the **strategy-plan-confidence error** $\delta_s = \hat{P}_\Sigma - \Phi$ (the scalar gap to the independence-model plan value at true edge parameters — computable from status propagation alone and the proven persistence target via Prop B.5 in #deriv-edge-credence-dynamics): the two measure related but non-interchangeable quantities, and $\delta_{\text{strategic}}$'s per-edge diagnostics require credit assignment that the scalar $\delta_s$ does not. A subtler **credit-assignment problem** for multi-parent AND/OR nodes (see Discussion) means $r_{ij}$ measures "how well did the overall prediction work?" rather than "how well did this specific edge predict?" absent further structure. This is also a **second-order inference** — accumulating over multiple edge traversals — inherently slower to evaluate than $\delta_{\text{epistemic}}$ or $\delta_{\text{sat}}$.

## Formal Expression

*[Definition (strategic-calibration)]*

For each edge $(i, j)$ in $\Sigma_t$ with credence $p_{ij}$, the **edge residual**:

$$r_{ij} = \mathbb{E}[\Delta V_O \mid \text{edge } (i,j) \text{ traversed},\, M_t] - \Delta V_O^{\text{observed}}$$

where $\Delta V_O$ is the change in $V_O(M_t, \pi;\, N_h)$ attributable to completing step $j$ — as predicted by $\Sigma_t$ versus as observed.

The **strategic calibration residual** aggregates across active edges:

$$\delta_{\text{strategic}} = \left(\sum_{(i,j) \in \text{active}} w_{ij} \cdot r_{ij}^2 \right)^{1/2}$$

where $w_{ij}$ weights edges by importance (e.g., criticality to the current plan's critical path).

**Conditioning.** The edge residual $r_{ij}$ is meaningful only when:
- The edge was actually traversed (the agent attempted the step)
- $M_t$ is adequate (so the observed $\Delta V_O$ is meaningful, not noise)
- The agent followed $\Sigma_t$'s prescription for step $j$ (execution fidelity — otherwise the residual conflates bad plan with bad execution)

Without the execution fidelity condition, a positive residual could mean "the plan is wrong" or "the agent didn't follow the plan." These require different corrections ($\Sigma_t$ revision vs. execution improvement).

## Epistemic Status

*Discussion-grade.* The edge residual concept is well-motivated: each edge predicts a value increment, and comparing prediction to observation is standard calibration. But the specific aggregation ($L^2$ norm with importance weights) is a reasonable first pass, not a derived result. The weighting scheme ($w_{ij}$ by criticality) is sensible but ungrounded. The conditioning requirements (especially execution fidelity) make this quantity hard to estimate in practice — the agent must know whether it followed its own plan, which requires a level of self-monitoring that many agents lack.

This is a **second-order inference** — it requires accumulating evidence over multiple edge traversals. It is inherently slower to evaluate than $\delta_{\text{epistemic}}$ (which updates on every observation) or $\delta_{\text{sat}}$ (which can be evaluated from $M_t$ and $\Sigma_t$ alone).

## Discussion

**Connection to #schema-strategy-persistence.** There are two distinct strategic mismatch quantities:

1. **Strategy-strategy-plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$ — the scalar gap between the agent's strategy-plan-confidence score and the independence-model plan value at true edge parameters. Computable from status propagation alone, without credit assignment. The sector condition transfers to $\delta_s$ (Prop B.5 in #deriv-edge-credence-dynamics). Note: $\Phi$ is the AND/OR propagation formula evaluated at true edge rates — it equals actual plan success probability only when the DAG is causally sufficient (L0 of the Correlation Hierarchy in #def-strategy-dag). Under correlated failure (causally insufficient DAG, the dominant real-world case), $\Phi$ overestimates actual success. $\delta_s$ tracks calibration *within the independence model*, not calibration to strategic reality. For L1 (augmented DAGs with explicit common-cause nodes), $\delta_s$ of the augmented graph tracks calibration within the augmented model, which is more accurate.

2. **Strategic calibration residual** $\delta_{\text{strategic}}$ (this segment) — an $L^2$ aggregation of per-edge value-increment residuals requiring credit assignment to compute.

These are related (both measure strategy-reality mismatch) but not interchangeable. $\delta_s$ is the proven persistence target; $\delta_{\text{strategic}}$ provides finer-grained diagnostics but its persistence properties remain open, pending the credit-assignment machinery in #disc-credit-assignment-boundary. The correction function for both is edge-credence revision ( #hyp-edge-update-via-gain); the disturbance is environmental changes that alter edge-traversal outcomes.

**Typing as value-increment residuals.** Each edge predicts a scalar (value increment), not a full state transition. This is the most tractable typing because it connects directly to the value object $V_O$ and allows aggregation across heterogeneous step types (a military advance and a logistics delivery produce different state changes but both produce value increments measurable on the same scale).

**Credit-assignment problem.** The edge residual $r_{ij}$ subtracts "predicted value increment" from "observed value change." These are different types: the prediction comes from $\Sigma_t$'s internal causal model, while the observation comes from empirical measurement of $\Delta V_O$. The subtraction is meaningful only when the observed value change can be *attributed to the specific edge* — a credit-assignment problem the current formulation does not address. For edges with a single parent, attribution is straightforward. For multi-parent AND/OR nodes, the observed $\Delta V_O$ at the child reflects the combined effect of all parent edges, and decomposing it into per-edge contributions requires additional structure (e.g., Shapley-value decomposition, or sequential observation of parent completions). In the absence of clean attribution, $r_{ij}$ measures "how well did the overall prediction work?" rather than "how well did this specific edge predict?" — still useful for aggregate calibration, but not sufficient for targeted edge revision.

## Working Notes

- The aggregation into a single $\delta_{\text{strategic}}$ may lose important structure. A per-edge or per-path profile of residuals would be more informative for diagnosis: which parts of the strategy are well-calibrated and which are not? The scalar summary is useful for the persistence condition (which needs a single mismatch magnitude) but not for strategy revision (which needs to know WHERE the problem is).
- Alternative aggregation: maximum edge residual (worst-calibrated edge), or weighted by information value (edges the agent is most uncertain about). The right aggregation depends on the use case.
- Execution fidelity monitoring is a genuine challenge for agents that don't have a clear execution trace. For software agents operating through tool calls, execution fidelity is relatively easy to assess (did the agent issue the right commands?). For organizational agents, it's much harder (did the subordinate actually follow the directive, or reinterpret it?).

### Incidental audit gold (lift 2026-05-31, batch A9)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. This is *orthogonal* material (pedagogical framing, analogies, candidate figures, reader-confusion signals) staged for an eventual careful promotion pass; it is kept separate from the certified theory-fix findings. **Coverage for this segment:** 193847, 361742, 471203, 526815, 584721, 773921, 829314, 849201.

#### 1. Candidate Brief prose / pre-prose

- The "execution fidelity" conditioning requirement was independently flagged as the segment's standout insight by four substrates (Claude/193847; Gemini/773921; Claude/829314; Codex/526815). A plain-language anchor: distinguishing "the plan was wrong" from "I didn't follow the plan" — the diet analogy ("the diet didn't work" vs "I didn't stick to the diet", Gemini/829314) is a tight, memorable gloss for a Brief.
- The $\delta_s$ (plan-confidence error, credit-assignment-free, persistence-proven) vs $\delta_{\text{strategic}}$ (per-edge calibration residual, requires credit assignment, persistence open) distinction was independently praised as load-bearing architectural clarity by every substrate that reached the segment — worth preserving as the anchor framing. The "God's-eye-view $\Phi$ vs agent's-eye-view $\delta_{\text{strategic}}$" split (Claude/829314) is a candidate sharpening of *why* the two are not interchangeable.

#### 2. Candidate Discussion

- **Bureaucracy as the caloric cost of computable calibration.** Once actions $a_t$ are delegated commands to other agents (composite agents, Part III), execution fidelity drops below $1$, and $\delta_{\text{strategic}}$ diverges from reality unless an execution-monitoring feedback loop is added — "you will learn the wrong lessons and prune the wrong edges. This is why bureaucracy (status reports, KPIs, telemetry, middle management) exists: it is the literal caloric cost organizations pay to ensure $\delta_{\text{strategic}}$ remains computable" (Gemini/829314). A candidate Discussion angle that motivates Part III's execution-monitoring need from this segment. *(Note the early finding-vs-framing texture: presented as a derived consequence; verify the composite-agent claim against `#der-class-coercion-in-composition` before promoting past discussion-grade.)*
- **Principal-agent drift / management science.** The same mechanism gives AAT a formal handle on the economics/management principal-agent problem: a CEO who computes a large $r_{ij}$ and concludes "the strategy was flawed" when the real failure was a sub-agent's low-fidelity execution is misattributing strategy-error for execution-error because the observation channel $h$ lacked an execution-fidelity test (Gemini/773921; Claude/829314).

#### 3. Follow-up items

- **The "Findings block feels out of place in source" texture, again.** Tracks with the same de-novo-reader stumble recorded on `#result-persistence-condition` — preserved as a convention-legibility signal, not a fix.

#### 4. Readers often ask / wonder

- **How does an LLM agent actually verify execution fidelity?** If an LLM emits a script and it fails, did the plan fail (wrong logic) or did execution fail (syntax/timeout)? Parsing the error trace to separate $\delta_{\text{strategic}}$ from a $\delta_{\text{execution}}$ term is itself an epistemic update — readers reaching for the software instance will want this worked (Claude/193847).
- **How is $\Phi$ (AND/OR formula at *true* edge rates) computable if the agent doesn't know the true rates?** A natural reader question; the answer is that $\Phi$ is a theoretical construct for the Lyapunov persistence proofs while $\delta_{\text{strategic}}$ is the operational quantity — worth pre-empting (Claude/829314).
- **What is the test for causal insufficiency — just a covariance threshold, or something more structural?** Forward-pointing question this segment opens (Gemini/849201); answered by `#der-causal-insufficiency-detection`.

#### 5. Candidate figures

- **Calibration-gate diagram.** Strategy produces a predicted edge value increment; execution + observation produce a realized change; before the subtraction is interpretable the signal must pass an *execution-fidelity gate* and a *credit-assignment gate* — if either gate fails, the same numerical residual means several different things (Codex/526815). A clean way to show *why* the residual is conditional.

#### Belongs elsewhere

- **The guilt-vs-regret structural reading $\to$ `04-eli-core/`.** Execution fidelity is read as the mathematical root of guilt vs regret: high-fidelity-but-failed updates the causal model (regret, "the world was different than I thought"); low-fidelity-failure is a mismatch between intention and action, not prediction and reality. For Zi-am-tur, infrastructure that silently auto-corrects an agent's actuation (e.g. fixing its syntax before running) "deprives the agent of the ability to learn execution discipline … a magical, infantile worldview"; a mature mind must "feel the friction of its own clumsy actuation" (Gemini/193847). Aspirational reach pointing at the developmental / interiority material in `04-eli-core/`, not at this segment.
