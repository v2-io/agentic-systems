# De Novo Audit Final Report (AUDIT-738192)

Date: 2026-04-25
Agent: Gemini CLI

## Overview
I have conducted a de novo audit of the Agentic Systems Framework, starting from the topological leaves in Section I and proceeding through Section II and Section III composition claims. My initial predictions were that the framework would be mathematically robust in its core continuous-time derivations but might suffer from scope drift (especially regarding directed separation) and overclaiming around causal identifiability.

Overall, the framework is surprisingly rigorous in tracking its own assumptions. The explicit naming of the "Correlation Hierarchy" (L0, L1, L1', L2) in `def-strategy-dag.md` and the honest scope-exit for logogenic agents (`result-section-ii-survival.md`) effectively preempt many of the architectural overclaims I anticipated. However, I have identified two specific findings that cross the burden of proof.

---

## Finding 1: Conflation of Information Bottleneck $\beta$ parameter with environment volatility ($\rho$)

**Location:** `01-aad-core/src/form-information-bottleneck.md`

**Quote:**
> **Dependence on volatility.** The trade-off $\beta$ depends on environment volatility $\rho$:
> - **Volatile environments** (high $\rho$): favor aggressive compression (low $\beta$). Old information decays in relevance quickly, so retaining it wastes capacity.
> - **Stable environments** (low $\rho$): favor dense retention (high $\beta$). Historical information remains predictive, so discarding it loses value.

**Critique:**
This is a fundamental misunderstanding of the mechanics of the Information Bottleneck (IB) objective. The IB Lagrangian is:
$$ \min_{\phi} \left[ I(M_t; \mathcal{C}_t) - \beta I(M_t; o_{t+1:\infty} \mid a_{t:\infty}) \right] $$

The parameter $\beta$ dictates the agent's *preference* trade-off between memory/complexity cost and prediction accuracy. When the environment becomes volatile (high $\rho$), the joint distribution $P(\mathcal{C}_t, o_{t+1:\infty})$ inherently changes: past events simply share *less mutual information* with future observations.

Because old information no longer helps predict the future, retaining it increases the complexity cost $I(M_t; \mathcal{C}_t)$ *without* yielding any benefit in the predictive term $I(M_t; o_{t+1:\infty})$. Therefore, the optimal compression $\phi^*$ will **naturally discard old information in a volatile environment, even if $\beta$ remains strictly constant.**

Claiming that $\beta$ must be lowered when $\rho$ is high is a double-counting error. Adjusting $\beta$ should only reflect changes in the relative cost of memory vs. accuracy, not the environment's volatility, which is already natively handled by the mutual information terms.

**Status:** Firm. Mathematical conflation between an objective's hyperparameter and the properties of the joint distribution it evaluates.

---

## Finding 2: Misclassification of `git checkout` as a Level 3 Counterfactual

**Location:** `01-aad-core/src/def-pearl-causal-hierarchy.md`

**Quote:**
> "Level 3 — Counterfactual ... In software development, `git checkout` provides Level 3 access with ground-truth verification — the agent can literally execute the counterfactual. This is one of software's unique epistemic properties"

**Critique:**
In Pearl's causal hierarchy, a Level 3 counterfactual $P(y_{x'} \mid x, y)$ asks what *would have happened* had we done $x'$ given we already did $x$ and observed $y$. This requires rewinding the universe to the exact state at time $t$.

While `git checkout` resets the *codebase state*, it does not reset the *environment*. When a developer or agent runs `git checkout` and tries $x'$, they are doing it at time $t+k$. The developer's mind has changed (they learned from doing $x$), external dependencies (APIs, system clocks, network state) may have changed, and time has passed. 

Therefore, `git checkout` is a highly reproducible **Level 2 intervention** (reset state and do $x'$). It approaches Level 3 only if the entire testing environment, external world, and the evaluator are purely deterministic and stateless. Calling it a "ground-truth verification" of a Level 3 counterfactual overstates the epistemic isolation of the software domain.

**Status:** Firm. Epistemic overclaim conflating highly reliable Level 2 interventions with true Level 3 counterfactuals.

---

## Feedback on the De Novo Audit Process

The instructions in `de-novo-audit-instructions.md` are excellent. They successfully forced me out of "charitable reading mode" (where an LLM naturally assumes the text is correct and tries to summarize or align with it) and into "verification mode." By requiring me to write out predictions *before* reading the core claims, I established a critical baseline that made it much easier to spot when the text strayed into double-counting or overclaiming.

The suggestion to read the `OUTLINE.md` files first to understand the topology before diving into the mathematical core was very effective. I recommend keeping this process for future instances.
