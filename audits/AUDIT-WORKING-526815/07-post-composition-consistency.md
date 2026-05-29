# 07 - post-composition-consistency

Segment: `01-aat-core/src/disc-composition-consistency.md`
Dependencies: `scope-agency` - declared dependency satisfied.
Status observed: `type: postulate`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

There is a small, intelligible postulate here: if AAT applies at multiple levels of description, predictions across those levels must not contradict. That core axiom is appropriate early because it constrains the theory's ambitions before composition details arrive. The opening sentence at lines 12 and the formal meta-requirement at lines 20-24 are enough to establish it.

But the segment then imports a large amount of future machinery: composite-agent scope, closure admissibility, bridge lemma, Tier 1/2/3 transfer, contraction-template topology cases, team persistence, tempo composition, and persistence-condition formulas. Those are not listed in frontmatter dependencies, yet they are not merely casual pointers; they appear inside Formal Expression and Epistemic Status as derived claims. I cannot verify them without breaking the outline order. This is stronger than "possibly out of place": the segment is trying to be both an early postulate and a late integration summary.

## Prompt pass

Predictions vs evidence: I expected an early scale-invariance postulate that might feel out of place. I found a much heavier segment: a concise postulate plus a dense downstream synthesis.

Cross-segment consistency: F1 remains live because this segment depends on `scope-agency`, so composition consistency applies to agentic/action-with-effect systems, not broad passive adaptive systems. New F2 candidate: `post-composition-consistency.md:5-7` declares only `scope-agency`, while lines 14, 28-44, 58-66, and 72-86 rely on many downstream segments not yet read.

Math verification: deliberately not performed. The segment includes concrete contraction-rate and feedback inequalities, but their proofs depend on future `result-contraction-template`, `form-composition-closure`, `der-team-persistence`, `der-tempo-composition`, and `result-persistence-condition`. Verifying now would violate the de-novo order.

Direction next: `post-causal-structure` should likely establish causal structure as irreducible. I expect it may also lean on Pearl language before the Pearl hierarchy segment, continuing the forward-reference pattern.

Errors to watch: early segments becoming mini-syntheses that defeat the row-order learning path; `stage: deps-verified` meaning only declared dependencies rather than actual semantic dependencies; postulate/status labels masking embedded derived claims.

What I would change: split this file into an early `post-composition-consistency` containing only the cross-level compatibility axiom and a later Section III or Appendix synthesis segment containing the tiered transfer/contraction material. Alternatively, list the downstream dependencies and move the row later.

Curiosity: whether the build/dependency tooling treats inline `#slug` references as dependency candidates. If not, this file shows why frontmatter-only checks can miss semantic dependency load.

New knowledge enabled: AAT wants level-invariance as a structural constraint, not merely an application domain. That gives later composition claims a clear normative target.

Audit process change: keep hidden semantic dependencies as a separate candidate type from formal frontmatter backward pointers. The protocol's critical-finding trigger is frontmatter-based, but this segment exposes a different failure mode.

Running outline change: add F2 candidate around placement/dependency status.

Value feel: mixed. The core postulate is valuable and elegant; the segment as a reading-order artifact is costly because it spoils and relies on late machinery before the audit can understand it.

## Diagram thought

The right diagram is an "early core / late payload" split. A small postulate node should sit in the current row order, while a dense cluster of future Section III and Appendix objects feeds back into the same file. The visual should make clear that the issue is not theoretical incoherence; it is canonicalization/placement pressure.
