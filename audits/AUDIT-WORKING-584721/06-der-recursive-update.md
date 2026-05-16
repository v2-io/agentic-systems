# Reflection 06 — der-recursive-update (Section I row 15)

## §4.2 dependency check — CRITICAL FINDING

`depends: [form-agent-model, form-event-driven-dynamics, deriv-recursive-update]`

- `form-agent-model`: row 10 ✓ (upstream)
- `form-event-driven-dynamics`: row 14 ✓ (upstream)
- **`deriv-recursive-update`: located in Appendix A, *downstream* of Section I in the OUTLINE walk.** I have not yet read it.

**F-C1 (first §4.2 critical finding):** der-recursive-update at AAD Section I row 15 lists `deriv-recursive-update` in its `depends:`, but `deriv-recursive-update` is in Appendix A — which the top-level OUTLINE places *after* Sections I, II, III. The OUTLINE's row order does not represent a topological linearization of the dependency graph at this position.

The substantive structure: der-recursive-update is the main-section *result* (Section I) that cites its full *derivation* in Appendix A. This is a common pattern in mathematical writing (result in body, proof in appendix), but under §4.2's verification target, it's a structural claim about the OUTLINE that doesn't hold. Either:
- (i) The OUTLINE row order should be revised so Appendix A derivations come *before* the Section I/II/III segments that depend on them, or
- (ii) The depends list should be relaxed: the Section I derived segment should depend only on its premises (which are upstream), not on the appendix derivation that *proves* the result; the proof is then a forward-reference, not a load-bearing dependency, or
- (iii) The OUTLINE's role as "topological linearization" should be explicitly relaxed — i.e., the framework documents that main-result→appendix-derivation back-pointers are an accepted exception.

I'm flagging this at **high confidence** as a structural inconsistency between the OUTLINE's claimed canonical order and the segment-level `depends:` data. Each main-section segment with an appendix-derivation back-pointer will exhibit the same pattern; this finding is likely to recur.

I'll continue reading der-recursive-update with the gap noted (per §4.2's procedure). Reading it without having seen `deriv-recursive-update` first means I see only the result, not the argument.

## Reading the segment under that gap

Without the appendix derivation, the Formal Expression and Epistemic Status are still legible. The segment claims that the recursive form $M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$ follows from three constraints: temporal ordering (C1), partial observability (C2), and state completeness (C3). The Epistemic Status frames C1+C2 as "eliminative" and C3 as "definitional." The full argument with seven counterexample attacks lives in the appendix derivation — which I haven't read.

I can verify the *plausibility* of the derivation from this segment alone (the constraints sound right, the conclusion follows under standard assumptions), but I cannot verify *the actual derivation* — that requires reading deriv-recursive-update, which the OUTLINE places after this segment.

## Predictions vs. evidence

I predicted in 00-initial-predictions that "the §4.2 critical finding rule" would surface multiple instances. This is the first one. **Earlier-than-expected** — I anticipated finding these in the dependency-drift sweep, not as the first §4.2-style finding emerging organically.

## Cross-segment consistency

- The "Between-event dynamics" paragraph references `#form-consolidation-dynamics` (a recently-added 2026-04-23 segment per CLAUDE-2.md priming). Cross-reference is clean — the segment surfaces the consolidation-regime extension cleanly.
- Forward references to `#def-model-sufficiency` (already read), `#emp-update-gain`, `#schema-strategy-persistence` — all consistent.

## Math verification

No numerical math to compute. The recursive-form claim is structural; verification requires the appendix derivation.

## Status-label / discipline

`status: conditional`. The Epistemic Status uses both "exact, with a partly definitional character" (in prose) and `conditional` (in frontmatter). These don't directly contradict — "conditional" could mean conditional-on-C3-being-accepted-as-definitional — but the prose framing emphasizes "exact" while the frontmatter says "conditional." Mild tension worth noting; not a finding by itself.

`stage: claims-verified` — high stage, consistent with the well-developed Epistemic Status.

## What am I now curious about?

- **Reading order of appendix derivations.** Under §4.2's directive, every Section I/II/III segment that has an Appendix A derivation as a `depends:` back-pointer triggers F-C1-style findings. If this is structural (the OUTLINE convention puts derivations in appendices), then the audit will accumulate many such findings. The honest move is to flag the *pattern* once and catalogue instances, rather than treat each as a separate critical finding.

  Should I read deriv-recursive-update *now* (out of OUTLINE order) since the depends explicitly cites it, or hold to the OUTLINE walk and reach it in Appendix A? Per §4.2: "Do not back up to read the missing dependency out of OUTLINE order; the OUTLINE's order is the verification target." So I hold.

  But this raises a question for Joseph: is the appendix-derivation pattern an accepted exception to OUTLINE-as-topological-sort? If yes, the §4.2 framing should be refined to allow appendix back-pointers as a recognized exception. If no, the OUTLINE row order needs to be revised to put appendix derivations before the main-section segments that cite them.

- The "completeness" framing for C3 — "any violation is absorbed by expanding $M_t$" — is clean rhetorically but is it actually true? If a piece of information matters for prediction but isn't in $M_t$, "expand $M_t$" is the right move, but that means the recursive form is conditional on having gotten the model class right. This is the connection to `#def-model-class-fitness` — the model class can be wrong, in which case expanding $M_t$ might require structural change. Worth tracking through `#result-structural-adaptation-necessity`.

## Outline updates

Adding to Section B (findings):
- F-C1: der-recursive-update has appendix-derivation back-pointer (`deriv-recursive-update` in Appendix A) — first §4.2 critical-finding instance. Likely a recurring pattern across main-section segments with appendix derivations.

Question for Joseph (queued for the post-segment-reading check-in): is the appendix-back-pointer pattern an accepted OUTLINE-order exception, or are these all genuine F-C-class findings warranting OUTLINE revision?

## Cadence check

One Read → reflection → next Read. Holding. No backing up to read the missing appendix dependency.

Next: Section I row 16 = `der-action-selection`.
