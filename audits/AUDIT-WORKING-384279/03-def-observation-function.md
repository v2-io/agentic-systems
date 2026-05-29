# 03 — def-observation-function

*Type: definition. Status: axiomatic. Depends: [def-agent-environment, def-action-transition].*

## Predictions vs evidence
Predicted: $h(\Omega_t, a_{t-1}, \varepsilon_t)$, axiomatic, similar opacity sub-claim. Found: exactly that. Pattern matches def-action-transition's structure (object intro + opacity sub-definition).

## Cross-segment consistency
Forward-refs `#form-agent-model` (lines 15, 41) and `#obs-software-epistemic-properties` in `02-tst-core/` (line 43). Cross-component reference explicitly flagged with "cross-component reference, see `02-tst-core/`" — good practice, makes the reader-walkthrough trace explicit. $\mathcal{O}$ introduced here; $\mathcal{A}$ was in def-action-transition. Parallel structure clean.

## Math verification
$o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ matches NOTATION.md exactly. No errors. Active-perception dependence on $a_{t-1}$ is well-flagged as optional (line 28, 37).

## Direction
The aisthesis/action/transition triple is now complete. Next should be `#def-chronica` to introduce the interaction history, then scope segments.

## Watch list (update)
- **Equation-tag pattern confirmed.** Line 31's *[Definition (epistemic opacity)]* is the same opacity-as-definition pattern as def-action-transition line 31. Two instances now of "$h/T$ opacity" tagged as *Definition* when content reads more like *Postulate* or *Scope*. Re-classifying as a possible **finding**: the four (action/observation × intro/opacity) atomic claims have the same eq-tag pattern, and three of them are object-introductions (definitions proper) but two of them (the opacity claims) are constitutive postulates that have been bundled under the *Definition* tag. Low severity, but it's a *pattern* now, not a one-off.

## Next-segment predictions
`#def-chronica`. Will introduce $\mathcal{C}_t$ as the interaction history $(o_1, a_1, \ldots, a_{t-1}, o_t)$. NOTATION.md shows this. May also introduce $\mathcal{C}_t^{\text{commit}}$ for the TST committed-state subset — but that's a forward reference into TST so likely just a pointer.

## What I'd change
The "lossiness" framing in line 15 ("strictly lower-information observation") is slightly looser than the formal claim — strict information loss is only guaranteed when $h$ is many-to-one. A deterministic, full-information $h$ would not be lossy. The framework's scope condition is information-loss-as-norm but the per-observation $h$ could in principle be lossless on a given trajectory. Minor scope/wording polish point.

## Curiosity
The active-perception case ($h$ depending on $a_{t-1}$) is significant for the framework's eventual handling of LLM-style agents whose "observation" is the model's own forward-pass output on a context window the agent constructed. There's an interesting question whether the LLM-as-observer fits this framing cleanly — is `a_{t-1}` = the previous tokens generated, with $\Omega$ = the language manifold? I'd want `03-llm-core/` to address this.

## Wandering thoughts

**Three for three on opacity-as-definition.** Now I have three foundational segments and two instances of opacity-claims-tagged-as-definitions. This is consistent within the corpus's pattern even if it's slightly off-key against FORMAT.md. The honest read: the segment authors used *[Definition]* as the catch-all for "this introduces structure" — both object intros and constitutive postulates. That's defensible authorial choice; FORMAT.md's `definition` does extend to "Introduces a quantity, object, or notation" which doesn't quite cover "the agent doesn't know X." If I see this pattern more, I'll consider it a §G process-feedback note rather than a finding — it's a FORMAT.md vs corpus drift, not a corpus error.

**Cross-component reference handling.** Line 43's explicit "cross-component reference, see `02-tst-core/`" parenthetical is exactly the kind of thoughtful prose that compounds. A fresh reader encountering `#obs-software-epistemic-properties` would otherwise stumble looking for it in `01-aat-core/`. Good. I'd watch whether other cross-component references are similarly self-disclosing.

**The "may depend on what the agent did" framing.** This is the entire crux of why partial observability is nontrivial. The active-perception case (agent's actions affect what it sees) creates a feedback loop on the observation side that mirrors the obvious one on the action side. In control theory this is sometimes called dual control (Feldbaum); in RL it surfaces as the exploration-vs-exploitation tradeoff. Worth watching whether the framework explicitly engages dual control / Feldbaum at some point, especially in the Causal Access chapter.
