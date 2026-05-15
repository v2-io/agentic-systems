# Reflection: #der-action-selection

**Stage:** deps-verified. **Status:** exact. **Type:** derived. **Depends:** [form-agent-model, der-recursive-update].

## Dependency check

Both upstream. ✓

## Predictions vs evidence

Predicted $a_t = \pi(M_t)$ from $M_t$-completeness. Got that, plus the Section II lift $\pi(M_t, G_t)$ via the same argument applied to $X_t = (M_t, G_t)$, plus an interesting *action fluency* concept I had not predicted: the degree to which effective action flows from the model without deliberative computation, formalized as $\Delta\eta^\ast(\Delta\tau) \approx 0$.

## Cross-segment consistency

Forward-refs `#def-pearl-causal-hierarchy`, `#der-deliberation-cost`, `#def-model-sufficiency`, `#result-persistence-condition`, `#form-complete-agent-state`, `#der-directed-separation`, `#def-agent-spectrum`. Discussion-grade.

"(Descended from TF-07.)" — **fifth instance** of the diff-voice pattern.

## Math verification

Same structure as `#der-recursive-update`'s derivation: action depends on internal state, internal state is $M_t$ by completeness, therefore $a_t = \pi(M_t)$. Standard.

## What direction next

`#def-mismatch-signal` — $\delta_t = o_t - \hat o_t$.

## Errors to watch for

- TF-XX pattern (5/17 segments now).
- Whether the "action fluency vs model sufficiency" distinction is preserved or conflated downstream.

## Predictions for next segments

`#def-mismatch-signal`: $\delta_t = o_t - \hat o_t$ where $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$. Plus the score-function variant $\tilde\delta_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$ (per NOTATION.md).

## What would I change

The fluency formalization $\Delta\eta^\ast(\Delta\tau) \approx 0$ is correct but oddly placed — it's introduced in Discussion as "formal characterization" but tagged conceptually rather than as a `*[Definition]*` block. If fluency matters downstream, it deserves its own segment or at least its own equation tag.

## Curious about

How the implicit/explicit distinction maps onto the logogenic case. Most LLM token-generation is implicit-fluent (no chain-of-thought); explicit deliberation requires explicit reasoning steps. The framework's distinction provides a clean diagnostic for "is this agent deliberating or just executing?"

## What new knowledge does this enable

- Action fluency as a measurable property (deliberation gain $\to 0$).
- The Boyd-OODA implicit-guidance-and-control connection: AAD's implicit/explicit map matches Boyd's IG&C / Decide split.

## Should the audit process change

No.

## Outline changes for FINAL

No.

## Felt value

**Mid magnitude.** The action fluency framing is a useful conceptual handle. The Boyd-OODA mapping is clean.

## What the framework now potentially contributes

A formal distinction between *what the model knows* (sufficiency) and *what the model can do effortlessly* (fluency). Most agent-theoretic frameworks conflate these; AAD separates them. This matters for:
- Robotics: a robot can have a perfect world model but require expensive planning to act.
- LLMs: most generation is implicit-fluent; reasoning is explicit-deliberative.
- Expert behavior: reflexes vs deliberation.

The structural pressure paragraph ("agents under selective pressure tend to internalize frequently-needed action patterns") is a clean derivation of why fluency develops.

## Wandering thoughts

The action fluency concept is more important than this segment's placement suggests. It's the structural justification for *why training makes systems faster* — internalized action patterns reduce $\Delta\eta^\ast(\Delta\tau)$ for routine cases, freeing tempo budget for genuinely novel situations. This is the formal version of the "automaticity" literature in cognitive psychology and the "expertise" literature in skill acquisition.

For logogenic agents: most LLM token-generation is in the implicit-fluent regime (the model's parameters encode action selection); explicit deliberation requires structured chain-of-thought. The fluency/deliberation tradeoff for LLMs is exactly what the proposed `#der-active-salience-management` segment in `03-llm-core/` (singular perturbation of token generation) might formalize.

A naming-brainstorm seed: "action fluency" is an evocative term I haven't seen in the agent-theoretic literature. Possible source: Boyd's "implicit guidance and control" is closest. The AAD-distinctive contribution is making fluency *quantitative* via $\Delta\eta^\ast(\Delta\tau) \approx 0$. Good naming.

Continuing to `#def-mismatch-signal`.
