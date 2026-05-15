# Reflection: der-directed-separation

## What the segment does

Derives (conditionally) that the epistemic update f_M is goal-blind — it processes events without reference to G_t. The condition is an architectural one: whether G_t is causally upstream of f_M in the agent's processing graph. This produces a three-class architectural partition: Class 1 (modular, directed separation holds by construction), Class 2 (fully merged, fails by construction), Class 3 (partially modular, varies).

The κ_processing operationalization (conditional mutual information of G_t into M_τ+ conditional on e_τ and M_τ-) quantifies coupling for Class 3 cases. The behavioral estimator (same event under two goal states, measure epistemic divergence) is the practical measurement tool.

## The Pearl-blanket vs Friston-blanket distinction

This is the most important philosophical clarity in the segment. AAD's directed-separation condition is a Pearl-blanket move: the architectural classification names the conditional-independence structure, admits where it fails (Class 2), and provides an operational measurement. This explicitly avoids the contested Friston-blanket reading (Bruineberg et al. 2022 critique: the Friston reading overruns what the formalism delivers; the conditional-independence statement doesn't license metaphysical demarcation).

AAD's explicit Class 2 scope exit is the answer to Bruineberg's critique: the framework admits where its conditional-independence apparatus fails to license decomposition, then hands Class 2 agents to a coupled formulation (03-llm-core/) rather than treating the separation as an unenforced approximation.

## Naming targets surfaced

Several naming targets are visible from this segment:
- "directed separation" — the main concept
- Class 1 / Class 2 / Class 3 architectural classes — are these named in the tracker?
- κ_processing — is there a naming target for this?
- "processing coupling" — the formal definition
- "goal-blind" as a descriptive term for directed separation

Let me check what the tracker surfaces.

## The behavioral estimator insight

The empirical estimator for κ_processing (same event under two goal states, measure divergence in epistemic content) is a practical probe of directed separation. The segment distinguishes this from the observation ambiguity estimator A(e) — both use the same mechanical comparison (same event under different goal-primings) but the interpretation differs. This is a methodologically important distinction.

## The IDT (Information Digital Twin) engineering note

Hafez et al. 2026 demonstrates that a modular sidecar monitoring bi-predictability P and entropy change ΔH from the (S, A, S') stream detects perturbations at 89% accuracy vs 44% for reward-based monitoring. This is the empirical validation that modular monitoring of internally-merged (Class 2) agents is feasible and effective. The IDT pattern is the engineering design response to Class 2 agents: build modularity at the system level even if the component is fully merged.

## The composite-level class inheritance

Strategic composition (Class 1 sub-agents with partially-opposing objectives) produces a Class 3 composite — not because any individual sub-agent's f_M is goal-conditioned, but because each sub-agent's M_t^(i) includes a model of other sub-agents' policies, which are goal-dependent. The composite acquires across-agent coupling even when within-agent modularity holds. This is a subtle and important result: the architectural class of a composite is determined by both sub-agent class AND the scope route (alignment vs strategic).

## Comparison with κ-as-scalar prior framing

The prior framing treated coupling as smoothly tunable. The revision to a discrete architectural classification (with κ as a diagnostic for Class 3 cases only) is justified by the "why the classification is not a smooth parameter" argument: within Class 1, κ ≈ 0 under ALL distributions; within Class 2, κ is high under MOST distributions; only in Class 3 is κ genuinely variable. The revision was documented in spike-kappa-topology-insight.md.

## Wandering thoughts

The claim about LLMs (goal-conditioned epistemic updates): the example "reading code with goal 'fix auth bug' vs 'add logging'" is empirically verifiable. You could probe this with the behavioral estimator: present the same error message to an LLM under two different task priming contexts, measure how much the epistemic content of the response (what the LLM says it learned about the codebase) diverges. If the estimator shows κ ≈ 1, the LLM is Class 2 on epistemic processing.

The "deeper question" paragraph is honest: goal-conditioned epistemic dynamics (motivated reasoning, confirmation bias) are left as out-of-scope. This is the right scope restriction — not because it's not important, but because the coupled formulation is a different theoretical project (03-llm-core/) that requires its own development.

How valuable: 10/10 for load-bearing (this is THE architectural split in AAD), 9/10 for surprise (the Pearl-blanket recognition + Bruineberg positioning, the composite-level class inheritance, the IDT engineering design).
