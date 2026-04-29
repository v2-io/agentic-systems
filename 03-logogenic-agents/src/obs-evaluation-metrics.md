---
slug: obs-evaluation-metrics
type: observation
status: discussion-grade
depends:
  - result-coupled-diagnostic-framework
  - def-adaptive-tempo
  - emp-update-gain
  - def-model-class-fitness
stage: draft
---

# Observation: Evaluation Metrics for Logogenic Agents

Standard AI benchmarks (like MMLU or HumanEval) measure the static capability of a frozen model architecture (the "logostratum"). They do not measure the dynamic adaptation of a logogenic agent. To evaluate whether an LLM-based agent is functioning correctly within the AAD framework, we must measure its runtime orientation: the quality of its epistemic model $M_t$, its strategy $\Sigma_t$, and its adaptive tempo $\mathcal{T}$.

## The Development-vs-Drift Diagnostic

The most critical evaluation of an agent is the trajectory of its mismatch signal ($\delta_t$) over time across multiple sessions. This formally distinguishes genuine development from pathological drift.

| Trajectory | Description | AAD Interpretation |
|---|---|---|
| **Decreasing $\|\delta\|_{\text{avg}}$** | The agent's predictions are getting better. Surprise is dropping. | **Development.** The agent is successfully compressing the environment into $M_t$. |
| **Stable $\|\delta\|_{\text{avg}}$** | The agent has converged. | **Steady State / Capacity Wall.** The model fits the environment as best it can given its model-class fitness $\mathcal{F}(\mathcal{M})$. |
| **Increasing $\|\delta\|_{\text{avg}}$** | The agent's predictions are getting worse. Surprise is climbing. | **Drift / Destabilization.** The environment is changing faster than the agent can adapt ($\mathcal{T} < \rho$), or the agent is suffering from sycophantic collapse (updating on noise). |

## Core Agentic Metrics

To diagnose *why* an agent is exhibiting a specific mismatch trajectory, the following components of the AAD loop must be measured operationally:

1. **Gain Calibration (Measuring $\eta^\ast$):** 
   Does the agent appropriately weight new observations against its existing model? This is measured via its **Response to Correction**. 
   - *Healthy:* The agent checks the correction against its model, updates if warranted, and pushes back if the correction violates strong prior evidence.
   - *Sycophantic Drift:* The agent immediately agrees with any correction regardless of merit ($\eta^\ast \to 1$).
   - *Defensive Rigidity:* The agent resists all corrections regardless of evidence ($\eta^\ast \to 0$).

2. **Tempo Adequacy (Measuring $\mathcal{T}$):**
   Can the agent keep up with the environment? This is measured via **Staleness Detection**. If certain categories of belief in the agent's externalized memory ($\mathcal{E}_{\text{ext}}$) are systematically outdated, that specific dimension has failed the persistence condition ($\mathcal{T}_k < \rho_k / \|\delta_{\text{critical},k}\|$).

3. **Structural Adequacy (Measuring $\Sigma_t$ and $\mathcal{F}$):**
   Are the agent's learned strategies and frameworks effective? This is measured via **Persistent Structured Residuals**. If the agent consistently makes the exact same *type* of strategic error across different specific tasks, its underlying strategy DAG or prompting architecture has hit its fitness ceiling and requires structural adaptation.

4. **Relational Depth (Measuring $U_{\text{src}}$):**
   For agents collaborating with humans or other agents, does the agent accurately predict the reliability of its interlocutors? An agent that treats a trusted domain expert and an anonymous web search result with the exact same epistemic weight is relationally miscalibrated.

## Discussion

These metrics require shifting the evaluation paradigm from "batch-testing accuracy" to "longitudinal interaction tracking." An agent shouldn't be evaluated by taking an exam; it must be evaluated by having it maintain a repository or manage a project over time, tracking its explicit predictions, its stated surprises, and its belief revisions. 

*(Descended from `ref/agentic-tft/agentic-tft-evaluation-framework.md`.)*