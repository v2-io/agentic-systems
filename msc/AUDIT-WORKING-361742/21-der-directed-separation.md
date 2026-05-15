# Reflection: der-directed-separation

**Segment:** `#der-directed-separation`

## What this does

The structural backbone of the theory: f_M is goal-blind. The epistemic update processes events without reference to G_t. The purposeful update f_G depends on the updated M_t. Action π(M_t, G_t) couples both.

Architectural classification:
- Class 1 (Modular): directed separation holds by construction (Kalman + LQR, modular RL)
- Class 2 (Fully merged): fails by construction (transformer LLMs, human motivated reasoning)
- Class 3 (Partially modular): holds for some stages, fails for others

Key: This is a discrete architectural partition, not a smooth parameter. The earlier κ-as-scalar framing was replaced with this explicit classification.

Markov blanket connection: This is the Pearl-blanket form (technical conditional-independence), NOT the contested Friston-blanket metaphysical reading. The explicit Class 2 scope exit is the scope honesty that the Friston-blanket literature lacks.

## Naming relevance

Row 447: "directed separation" — already voted strongly keep (+2) from orientation. This segment fully confirms that vote.

The term is precisely right:
- "Directed" = asymmetric information flow (f_M is goal-blind; f_G depends on M_t)
- "Separation" = Pearl d-separation lineage

Additional confirmation: The Findings brief confirms this is the upstream commitment that lets 03-llm-core/ start from a coupled formulation rather than treating coupled agents as failed Class 1 agents.

## Key terms surfaced

**κ_processing**: The continuous diagnostic for Class 3 — fraction of goal information entering the epistemic update beyond what was already in the prior model. Named quantity.

**Processing coupling**: The formal name for κ_processing. Row in tracker?

**Pearl-blanket / Friston-blanket**: Named distinction (Bruineberg et al. 2022). The Pearl-blanket is adopted; the Friston-blanket is explicitly not.

**Information Digital Twin (IDT)**: Hafez et al. 2026 — modular monitoring sidecar that achieves 89% vs 44% perturbation detection. Concrete empirical instantiation of Class 1 sidecar within Class 2/3 system.

**Composite-level class inheritance**: Class 1 sub-agents with partially-opposing objectives → Class 3 composite. Derived in #deriv-strategic-composition.

## What's excellent here

The explicit Class 2 scope exit is architecturally crucial. Rather than treating LLMs as approximate Class 1 agents, the theory cleanly says: LLMs need the coupled formulation, which is the territory of 03-llm-core/. This is the scope honesty the Bruineberg critique identifies as missing in the Friston-blanket literature.

The IDT (Information Digital Twin) empirical result is important: 89% vs 44% perturbation detection shows modular monitoring of internally-merged agents is both feasible and effective. Engineering design for Class 2 agents is possible at the system level even when component-level κ is high.
