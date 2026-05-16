# Reflection: def-causal-information-yield

## What the segment does

Defines CIY (Causal Information Yield) as expected KL divergence between outcome distributions under different interventions — measuring *action-distinguishability*, not expected information gain (EIG). Status is exact for the definition itself, discussion-grade for the EIG relationship.

## Naming targets surfaced

Row 89: "causal information yield | CIY..." — this is the defining segment. I can now vote on this.

## The CIY vs EIG distinction

The segment's most important conceptual move is distinguishing CIY (distinguishability) from EIG (learning value). CIY can be high even when the agent already knows the outcome distributions — the distributions ARE different, but there's nothing new to learn. High CIY is necessary but not sufficient for learning value.

The $\lambda(M_t)$ weighting in the unified objective partially compensates: when $U_M$ is low, $\lambda \to 0$, suppressing exploration regardless of CIY. This makes the exploration term "behave like EIG" without being EIG. The segment is honest that this is heuristic.

This is a genuine conceptual contribution: most exploration frameworks conflate distinguishability with learning value. The distinction is sharp and practical.

## The query action class

The Discussion introduces "query actions" — asking another agent's model — as qualitatively distinct from direct environment probes. A well-targeted query can carry CIY orders of magnitude higher than individual probes because it transfers pre-compressed information.

This is important for LLM agents specifically: a large fraction of useful actions are query actions (asking a user, consulting documentation, calling an API). The CIY framework needs to handle these actions' special character.

## Naming vote thoughts for "causal information yield"

"Causal information yield" is precise:
- "Causal" — it's about interventional (Level 2) structure, not associational
- "Information" — it's measured in information-theoretic units (KL divergence)
- "Yield" — how much the action "yields" in terms of causal-structural information

The acronym CIY is used throughout and seems established. The name survives the communal-imagination test for technically-minded readers.

Alternative candidates might be "action distinguishability" (what CIY directly measures) or "interventional information content" (longer). "Action distinguishability" is more literal but loses the "yield" sense of productive outcome. "Causal information yield" is slightly grandiose but accurate.

## The adversarial mirror

The segment's closing observation: deceptive queries inject high CIY that drives model-reality mismatch upward rather than downward. The adversarial use of the query channel — exploiting high trust to inject misdirected updates — is a powerful insight.

This connection between the information-theoretic and adversarial perspectives is where the framework becomes practically interesting for AI safety.

## Wandering thoughts

The reference distribution $q$ for CIY creates a significant degree of freedom. "How different is this action from what I'd typically do?" is a fundamentally self-referential question — CIY depends on the agent's current policy, which makes CIY policy-relative in addition to model-relative.

This means two agents with the same $M_t$ but different policies have different CIY values for the same action. For exploration guidance, this seems right: an aggressive agent (wide policy) sees low CIY for actions that are extreme from a conservative agent's perspective (because the aggressive agent already considers those actions).

The query-action observation that "responses arrive already compressed in the source's representational framework, introducing a translation cost when frameworks don't align" is important. LLM-to-LLM communication involves this translation cost — the vocabularies, ontologies, and implicit assumptions of the source and receiver may not align, creating noise even in high-trust, high-CIY queries.

How valuable: 8/10 for surprise (the CIY vs EIG distinction is sharper than expected, and the query action class is a non-trivial extension), 8/10 for load-bearing.
