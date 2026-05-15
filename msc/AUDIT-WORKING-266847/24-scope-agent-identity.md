# Reflection: scope-agent-identity

## What the segment does

Commits AAD to singular non-forkable causal trajectories as the grounding for agent identity. Identity is not M_t (the model state, which can be copied) but C_t (the causal trajectory, which cannot be forked). Three consequences: sufficiency is trajectory-indexed, model merging is lossy by construction, and interventional access depends on singularity.

The "natural extension" to parameterization-invariance (PI) is the most technically rich part. PI + Čencov's uniqueness theorem forces the Fisher information metric on statistical-manifold sub-cases of M_t, upgrading Fisher-metric results from theorem-imported to AAD-internally-forced.

## Naming targets surfaced

The segment uses "continuity persistence" (LEXICON.md term) as distinct from structural persistence and operational persistence. This is a three-way distinction: structural persistence (machinery outpaces disturbance), operational persistence (within viable region), continuity persistence (coherent identity through time).

Looking for "agent identity" in the tracker...

Row 5 in the tracker: "agent identity | scope-agent-identity..." — this is the main target.

The segment also mentions "clone problem" — is there a named entry for this?

## The parameterization-invariance observation

The PI + Čencov pathway is the theoretically important addition. Before this segment, the gain-sector bridge depended on the Fisher information metric being chosen (or imported from Riemannian geometry). With PI as a scope-level axiom, the Fisher metric is *forced* — the gain-sector bridge results become AAD-internally-grounded rather than theorem-imported. This upgrades the epistemic status of several downstream results.

The structural analogy is precise: chain-rule-additivity forces divergence to the KL family; evidential-additivity forces additive Bayesian updating; parameterization-invariance forces the Fisher metric on statistical manifolds. Three natural axioms, three uniqueness theorems, three coordinate-forcing moves. Each follows the additive-coordinate-forcing meta-pattern (#disc-additive-coordinate-forcing).

## The clone problem

The clone problem characterization is clean and non-philosophical: at the moment of duplication, both copies are identical (same M_t, same C_t prefix). The first subsequent event creates two divergent irreversible trajectories. After that, each copy's sufficiency is measured against its own distinct history. The merge problem (reconciling incompatible causal histories) has no generally optimal solution — this is a structural constraint, not an algorithmic limitation.

This is the formalization of the "LLM weights can be copied, but the particular session cannot" observation from the earlier context-turnover reflection. The 100% context turnover problem in logogenic agents is the extreme case: every new session starts a new C_t from near-zero.

## The type/token distinction

The segment is careful: AAD's formal apparatus applies to token agents (particular sessions, particular trajectories), not type agents ("the GPT-4 model"). This has a direct consequence for aggregated claims. If you want to say something about "GPT-4 as a class," you need additional machinery (population-level dynamics, latent structural diversity from Miller's framework). The individual-session AAD results don't aggregate to type-level claims without that additional layer.

## Naming votes to cast

Row 5: "agent identity" → will need to check the card for what candidates exist.

The "continuity persistence" vs "structural persistence" vs "operational persistence" three-way distinction is a natural naming target if the three terms aren't already canonicalized. The LEXICON.md discussion should handle this, but the segment's phrasing ("continuity persistence in the sense of LEXICON.md") suggests it is.

## Wandering thoughts

The scope-level PI axiom is philosophically important: it says the theory's content doesn't depend on how you parameterize the agent's internal state. This is the coordinate-invariance commitment that distinguishes a theory of real agents from a theory of computational implementations. A theory whose conclusions change when you relabel the agent's internal variables would be a theory of the labels, not the agent.

The connection to logogenic agents (03-llm-core/) is flagged but not developed. The non-forkability argument suggests that each AI conversation session is a distinct agent in AAD's sense — the cross-session memory files (CLAUDE.md, MEMORY.md) are model summaries, not trajectory transfers. The persistence across sessions is continuity-persistence-by-proxy, not genuine causal continuity.

How valuable: 8/10 for surprise (the PI + Čencov pathway upgrading Fisher-metric results, the precise type/token distinction), 7/10 for load-bearing (scope statement, but load-bearing for downstream formalism).
