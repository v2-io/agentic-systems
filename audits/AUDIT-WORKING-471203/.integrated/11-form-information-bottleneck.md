# Reflection: #form-information-bottleneck

**Stage:** draft. **Status:** exact (applied external theorem). **Type:** formulation. **Depends:** [form-agent-model, def-action-transition].

## Dependency check

Both upstream. ✓ Heavy Discussion-section forward references but no Formal-Expression-level downstream uses.

## Predictions vs evidence

Predicted IB Lagrangian. Got: $\phi^\ast = \arg\min_\phi [I(M_t; \mathcal{C}_t) - \beta \cdot I(M_t; o_{t+1:\infty} \mid a_{t:\infty})]$. The **policy-conditioning** $\mid a_{t:\infty}$ on the predictive term is the AAD adaptation — not in vanilla Tishby-IB. The segment acknowledges this in Discussion (the IB objective is "policy-relative").

## Cross-segment consistency

Heavy forward references in Discussion (orientation). Fine.

The segment makes a positioning claim — AAD's $M_t$-compression uses IB-form (MI-to-relevance), while AAD's strategy-compression uses IT-MDP-form (KL-to-target-policy), and the two are sibling lineages descending from rate-distortion. This positioning depends on `#form-strategy-complexity-cost` and `#deriv-strategy-cost-regret-bound` doing what's claimed. I'll verify when I get there.

## Math verification

- IB objective is well-typed. Policy-conditioning is the AAD adaptation; honestly named.
- Markov chain $Y - X - T$ argument holds: $T = M_t = \phi(\mathcal{C}_t) = \phi(X)$, so $T \perp Y \mid X$. Standard IB Markov property.
- The "**$\beta$ vs $\rho$ double-counting argument**" in Formal Expression is robust-qualitative reasoning presented as fact in the Formal Expression section. The Epistemic Status explicitly downgrades it — but a reader following only the Formal Expression block would take it as derived. **Mild scope/status mismatch:** the argument should either be tagged `*[Discussion]*` inline or moved to Discussion proper. Filing as candidate observation.

## What direction next

`#def-model-sufficiency` — when $M_t$'s predictive term is close to its maximum.

## Errors to watch for

- **Citation accuracy on the IB↔VFE relation.** The segment claims "the IB objective is the rate-distortion specialization of variational free energy" with Tishby-Zaslavsky 2015 cited. I want to **verify in Phase 2** that this paper substantiates the claim. From training memory, Tishby-Zaslavsky 2015 is "Deep learning and the information bottleneck principle" applying IB to deep nets — *not* a derivation of IB as a special case of VFE. The deeper IB↔VFE relationship is sometimes claimed but non-trivially derived; the paper cited may not be the right reference.
- The IT-MDP lineage citations (Tishby-Polani 2011, Rubin-Shamir-Tishby 2012, Levine 2018) look right from training memory but worth Phase-2 verification.
- The Friston citations look correct in shape (Friston 2010 NRN, Friston-FitzGerald-Rigoli-Schwartenbeck-Pezzulo 2017 Neural Computation, Parr-Pezzulo 2022 MIT Press) — the formal claim that $-F = \text{accuracy} - \text{complexity}$ matches IB structure under the Markov chain is what needs the Tishby-Zaslavsky citation to substantiate.

## Predictions for next segments

`#def-model-sufficiency`: $S(M_t) \in [0, 1]$ characterizing how close $M_t$ is to the max-attainable predictive power within its model class. Probably formulated as a normalized $I(M_t; \text{future}) / I(\text{optimal}; \text{future})$ ratio.

## What would I change

1. Move the "$\beta$ vs $\rho$" paragraph from Formal Expression to Discussion, OR tag it inline as `*[Discussion]*`.
2. Verify the Tishby-Zaslavsky 2015 citation actually substantiates the IB↔VFE specialization claim. If it doesn't, the citation needs replacing or the claim needs softening.
3. Consider a brief Brief-style sentence in Discussion that names what the IB form *intuitively does*: "the model retains the parts of history that matter for predicting the future under the agent's policy and discards the rest." That paraphrase is more memorable than the symbolic objective.

## Curious about

- Whether `#disc-additive-coordinate-forcing` (Appendix A) names the IB Lagrangian as one of the "additive coordinate forcing" instances (the OUTLINE preamble references it as "1-anchor-plus-3-theorem"). The IB Lagrangian's $-\beta I + I$ structure has a specific information-theoretic origin that may be derivable from additivity axioms.
- Whether AAD ever needs to compute $\phi^\ast$ in practice or whether the IB form is purely characteristic of the optimum (with actual agents using approximations like variational IB). The Discussion says actual agents approximate via "forgetting, attention, abstraction, summarization" — but that's a list, not a formalization.

## What new knowledge does this enable

- A principled compression criterion for $M_t$, with $\beta$ as a tunable trade-off.
- The framework's positioning relative to active inference (Friston) — AAD takes the IB form without the AI-side normative commitments.
- The IB-vs-IT-MDP distinction sets up the strategy-cost segment's KL-to-target-policy form.

## Should the audit process change

No. (I am noticing that this segment's IB↔VFE claim is exactly the kind of citation-density move §5.3 of the audit instructions flagged as a worthwhile audit emphasis. Phase 2 verification on Tishby-Zaslavsky 2015 is in scope.)

## Outline changes for FINAL

Adding the citation-verification need to §G (process feedback) — the segment's heavy citation density is exactly where AAD's "form-shaping for external-theorem applicability" discipline gets tested.

## Felt value

**Mid-high magnitude.** The IB form itself is foundational (high), but the substantive *positioning* claims (IB-lineage vs IT-MDP-lineage, IB↔VFE specialization, AAD-not-AI commitments) are where this segment becomes consequential. The citations need Phase-2 verification; if they hold up, the segment is doing real work for AAD's relationship to active inference.

## What the framework now potentially contributes

A clean structural distinction between two compression forms (IB-shape vs IT-MDP-shape) descending from a common rate-distortion ancestor, with AAD using each where the *kind of compression* warrants. Most agent-theoretic frameworks pick one and stick with it (active inference: VFE everywhere; control-as-inference: KL-to-target-policy everywhere); AAD's split (IB for $M_t$, KL for $\Sigma_t$) is structurally distinct and reflects the underlying difference between *epistemic* and *strategic* compression operations.

If the framework can substantiate this split as derivable rather than chosen — perhaps via `#disc-additive-coordinate-forcing`'s uniqueness arguments — that would be a substantial structural result.

## Wandering thoughts

The IB↔VFE relationship claim is the single most consequential technical claim in this segment for AAD's positioning. If it holds rigorously, AAD can credibly say "we recover the AI compression machinery as a structural specialization, without inheriting AI's normative commitments." If it doesn't hold rigorously (i.e., if IB and VFE are *related* but not *related-by-specialization*), then AAD's claim to recover AI under restrictions is weaker.

What I'd want to see in the verification:
- Under what specific assumptions does VFE's $-F = \text{accuracy} - \text{complexity}$ become AAD's IB Lagrangian?
- Is the Markov chain $Y - X - T$ (IB) the same Markov property assumed in active inference's posterior factorization?
- What's lost in the specialization — is it really just "preferences-as-priors and EFE-as-master-objective" or is there substrate AAD is silently dropping?

These aren't fatal questions; they're the questions a serious AI-vs-AAD comparison would have to answer. AAD's positioning is much stronger if the answers exist; weaker if they don't.

A naming-brainstorm seed: the term "Information Bottleneck" is well-anchored in the literature (Tishby et al. 1999) and AAD shouldn't rename. But the AAD-distinctive feature — *policy-conditioning* on the predictive term — could be named separately. "Policy-Conditioned IB" or "Forward-Predictive IB" or "AAD-IB" if a distinguishing label is ever needed. Currently the segment leans on the standard name and notes the adaptation in Discussion; that's probably the right call but flagging.

A meta-thought about the policy-conditioning. The fact that the predictive term conditions on future actions $a_{t:\infty}$ means that AAD's IB *bakes the policy in*. This is structurally important: $\phi^\ast$ is not "the optimal compression" but "the optimal compression *for this policy*." Different policies induce different optimal compressions. This is honest (the policy genuinely matters for what's predictively relevant) but it means AAD's $M_t$ optimization can't be done in isolation from policy choice. The segment doesn't dwell on this; the orient cascade ($M_t$ first, then $\Sigma_t$, then $O_t$) implies a fixed policy during $M_t$ updates, so the conditioning is on the *current* policy. That's fine, but worth tracking.

Phenomenologically: a real engagement-lift from the IB-vs-IT-MDP distinction. This is the kind of architectural-positioning content that I find genuinely interesting — making explicit the lineage of each formal choice. The framework is showing more of its mathematical seams here than in the foundational definitions, which is the right rhythm.

Continuing.
