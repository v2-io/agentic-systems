# 33 - scope-agent-identity

Segment: `01-aat-core/src/scope-agent-identity.md`
Dependencies: `def-chronica`, `def-model-sufficiency` - satisfied.
Status observed: `type: scope`, `status: robust-qualitative`, `stage: draft`.

## Reflection

The scope claim is useful: AAT's formal results apply to token agents on singular causal trajectories, not to model types or copied parameter states. Once two copies receive different events, their sufficiency and interventional evidence are indexed to different histories. That helps separate "same weights" from "same agent."

The main precision issue is the notation around chronica. If `C_t` is a mathematical event/history sequence, then a representation of that sequence can be copied. What cannot be copied is the causal trajectory token: the actual embedded path through interventions and consequences. The segment's thesis is right if `C_t` denotes the causal token, but earlier chronica usage often reads like an ordered record. It should distinguish "trajectory itself" from "record/summary of a trajectory" to avoid making non-copyability rest on a copyable formal sequence.

## Prompt pass

Predictions vs evidence: I expected a Part I coda linking chronica and sufficiency to identity. The segment provides that and adds a parameterization-invariance axiom proposal.

Cross-segment consistency: consistent with `def-chronica` and trajectory-indexed sufficiency. The PI material back-links to `der-gain-sector-bridge`, but that earlier segment had already used PI before this scope segment appeared in outline order.

Math verification: no theorem here. The type/token distinction is structurally clear; the category-theoretic/functor formalization is explicitly not attempted.

Direction next: `impl-persistence-and-limits` should close Part I with implications; I will treat it as discussion unless it adds hidden proof kernels.

Errors to watch: conflating copied model state, copied memory record, and shared causal trajectory; using PI as if forced by this scope rather than a genuine extra axiom; working-note material from NeurIPS/cross-component files priming later audit.

What I would change: define two symbols, perhaps `C_t` for the represented chronica and `\gamma_t` for the causal trajectory token, then say sufficiency is indexed to `\gamma_t` while `C_t` is a record produced along it.

Curiosity: the non-forkability claim is a strong bridge to LLM-session identity, but it is outside the core adaptive math unless kept at scope level.

New knowledge enabled: AAT identity is token/trajectory-indexed, not state-equivalence-indexed.

Audit process change: the diagram should show a shared prefix followed by divergent causal paths, with copied state at the fork but non-transferable sufficiency after divergence.

Value feel: medium-high as scope; low as formal theorem.

## Diagram thought

The clearest diagram is a fork. A shared prefix leads to a copied `M_t`; after different events, two trajectories diverge. Each model is sufficient only relative to its own path. A small side label should mark that a record of the prefix is copyable, but the causal continuation is not shared.
