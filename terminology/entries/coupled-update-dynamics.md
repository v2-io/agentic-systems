---
slug: coupled-update-dynamics
schema_version: 1
term: coupled update dynamics
name: Coupled Update Dynamics
notation: "$X_{\\tau^+} = f_{\\text{LLM}}(\\text{prompt}(X_{\\tau^-}, e_\\tau))$"
brief: The single-pass update rule for Class 3 (Coupled) agents — belief and strategy are updated simultaneously by the LLM forward pass, replacing the sequential epistemic-then-purposeful cascade.
layer: prose-symbol
status: canon
tags: [structural_concepts, logogenic]
source_type: asf
primary_source: 03-llm-core/src/def-coupled-update-dynamics.md
first_asf_mention: 03-llm-core/src/def-coupled-update-dynamics.md
see_also: [directed-separation, goal-update-coupling-class, coupled, logogenic-agent, orient-cascade]
aliases: []
do_not_confuse: [directed-separation]
---

The starting formulation for logogenic agent theory: rather than factoring the update into epistemic-then-purposeful (as in the Class 1 Separated factored form), the LLM forward pass produces a response that simultaneously encodes updated beliefs and strategic assessments.

$$X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$$

The **prompt-assembly function** $\text{prompt}(X_{\tau^-}, e_\tau)$ is where most engineering decisions live. The system prompt carrying $O_t$ appears first, placing goal-conditioning causally upstream of all subsequent processing — the mechanism by which $\kappa_{\text{processing}} \approx 1$
for transformer architectures.

The **response** is functionally decomposable post-hoc into epistemic content $r_\tau^M$,
purposeful content $r_\tau^G$, and action content $r_\tau^a$ — but this decomposition is the analyst's tool, not a description of internal processing. Chain-of-thought generation can approximate the sequential cascade behaviorally, but this is a training-shaped behavior,
not an architectural guarantee.

What is preserved from AAT: the state decomposition $X_t = (M_t, G_t)$ as an analysis coordinate, event-driven structure, and recursive update form. What changes: the orient cascade does not hold as a derived result.

Defined in [`#def-coupled-update-dynamics`](../../03-llm-core/src/def-coupled-update-dynamics.md).
