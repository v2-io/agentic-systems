# 07 — post-composition-consistency

*Type: postulate. Status: axiomatic. Stage: deps-verified. Depends: [scope-agency]. OUTLINE marks "(possibly out of place)".*

## Predictions vs evidence
Predicted: axiomatic statement of scope-invariance across levels. Found: much more — three-layer decomposition (scope/admissibility/transfer), Tier 1/2/3 classification, closed-form composite contraction rates (CC-parallel/cascade/feedback) imported from #result-contraction-template, screening test $\tau_{eq}\ll\tau_{ext}$, Brooks's Law analog. This is a substantial segment, not a one-claim postulate.

## Cross-segment consistency
Forward-refs are extensive — `#scope-composite-agent`, `#form-composition-closure`, `#result-contraction-template`, `#der-tempo-composition`, `#result-persistence-condition`, `#der-temporal-nesting`, `#der-team-persistence`, `#der-directed-separation`. All Part III (or Part I Ch.4 for persistence-condition). The segment imports Part III content heavily; this is what "possibly out of place" likely refers to.

## OUTLINE-placement observation (candidate finding)
The OUTLINE itself flags this segment as "(possibly out of place)" — a textual signal the project knows this. The segment sits in Part I Ch.1 (Coupled Loop) but its content reaches deeply into Part III machinery. Two readings:
1. **Placement is correct** because the *postulate itself* is structural and belongs with the other scope/postulate primitives (scope-adaptive-system, scope-agency, post-causal-structure). The unfortunate dependency on Part III is endemic to the topic; relegating it to Part III would lose the postulate-not-derived honesty.
2. **Placement is wrong** because a postulate that requires 8+ forward refs to be made operational is not standing on its own at the Part I level. A first-time reader hitting this in Ch.1 is being asked to import Tier 1/2/3, the contraction template, the closure defect, and the bridge lemma — none of which have been introduced.

Reading (1) is the project's current call (OUTLINE annotates the placement question explicitly). Reading (2) is the audit-worthy observation: even if (1) is right, the *prose* needs to honor that a first-time reader hasn't seen the downstream machinery. The segment's Formal Expression line 44 reads `*[Derived (Conditional on Tier 1M + admissible composition topology, from #result-contraction-template (CC-parallel) / (CC-cascade) / (CC-feedback))]*` — this is a Derived block inside a Postulate segment, citing concepts (Tier 1M, CC-*) defined hundreds of segments downstream. **Severity: medium; type: cross-segment ordering / pedagogical-flow; disposition: probably needs targeted-prose-revision to mark forward-imports as imports-of-trust rather than imports-of-content.**

## Math verification
- Parallel: $\lambda_c = \min_i \lambda_i$ with block-diag composite metric. Standard contraction-theory result. ✓
- Negative-feedback heterogeneous: $(\lambda_1 - C_1)(\lambda_2 - C_2) > k_{12}k_{21}/4$. Small-gain-style sufficient condition; the factor of 4 should derive from a quadratic-form argument. **Spot-check candidate when I reach #result-contraction-template.**
- Effective disturbance: $\rho_\text{eff} = \rho_\text{ext} + \varepsilon^\ast\nu_c$ — closure-defect contribution. Needs verification when I reach #form-composition-closure for the per-step / per-rate convention.

## Watch list (update)
- **Type-vs-content tension.** Postulate segment containing a Derived block (line 44) is structurally unusual. FORMAT.md doesn't prohibit this but the convention is that postulates state structural commitments and derivations live in derivation segments. The "Strengthening attempt — outcome" Working Note (line 97) makes this explicit: "the strengthening is achieved by binding the postulate's heuristic to the existing (CC-*) closed forms" — which is an integration-is-replacement move that *promoted the postulate's substance from heuristic to derived*. The segment honors this promotion in its body. Strong move; but the body now mixes postulate-flavor + derived-flavor + heuristic-flavor in one segment. Worth noting as a § F bigger-picture observation about how integration-is-replacement landings produce dense polyglot segments.

## Next-segment predictions
`#post-causal-structure`. Another postulate. Will probably introduce the causal-irreducibility commitment (no parallel actions producing identical effects, or something structurally similar). Probably less rich than this one — but the postulate framing has been stretched, so I won't assume.

## What I'd change
Three concrete options for the placement / density question:
1. Move this segment to the opening of Part III (Composition), where its forward-refs are no longer forward.
2. Keep this segment in Part I but strip the Derived block (line 44-52) and the screening-test specialization (line 56+) — leave them in #form-composition-closure where they belong. The Postulate stays clean here; the unpacking lives where the machinery is available.
3. Keep current placement and rewrite the body to honestly mark "the operational content is unpacked in Part III's #form-composition-closure and #result-contraction-template; what stands at this point is the structural meta-requirement that AAT predictions be cross-level-compatible."

Option (3) is the smallest editorial change and probably the right call. The OUTLINE's "(possibly out of place)" annotation is itself an honest signal that this is a known-and-considered position; the prose should reflect that the postulate-itself is here as a structural commitment and the unpacking lives downstream.

## Curiosity
The "Strengthening attempt — outcome" Working Note at line 97 is a worked instance of strengthen-before-soften landing well — the original heuristic claim ("composite bounded below by slowest sub-agent") was *replaced* (per integration-is-replacement) by the Tier 1M derived form, with the spike-style trail kept in Working Notes. This is exactly the pattern Joseph's CLAUDE.md commits to. Good record.

## Wandering thoughts

**On the postulate-that-derives-its-own-consequences move.** This segment is doing something subtle. The postulate (cross-level-compatibility) is axiomatic, but the framework recognized that without its three composition laws (tempo, persistence, mismatch), the postulate is empty. So the segment imports the composition laws from Section III and *uses* them to give the postulate operational meaning. This is methodologically thoughtful — a postulate without operational content is mere assertion. But it pushes the segment past the Postulate type. A cleaner architecture might be: a thin Postulate segment stating the meta-requirement, then a Discussion / Implications segment (perhaps `disc-composition-consistency-implications`) that imports the Section III machinery and shows what the postulate buys. Or: place the postulate at the *opening* of Section III, where its consequences are local.

**On the Tier 1/2/3 introduction.** Sub-agent Tiers are critical to this segment's content (the contraction-rate result lifts exactly for Tier 1, with degradation for Tier 2, per-domain for Tier 3). The Tiers are first introduced here in passing — the segment leans on the reader knowing what "Tier 1M" means without `#form-composition-closure` having been read. This is a hidden dependency — the segment is operationally inaccessible without the downstream Tier-classification. The forward-refs disclose this but the *prose* doesn't slow down for it. A fresh reader will skim the Tier 1/2/3 distinctions without grounding.

**On the Brooks's Law mechanism explanation.** Line 90: "Whether the specific mechanism (coordination-overhead saturation crossing the persistence threshold) is the dominant cause of Brooks's Law in practice is an empirical question." This is honest — the framework offers a *possible* mechanism for Brooks's Law via composition-consistency-failure; whether it's the dominant cause is left open. This is the project's epistemic discipline working as advertised. I appreciate it.

**On the holons reference in Working Notes line 101.** Koestler 1967 holon — "an AAT agent satisfying composition consistency *is* a holon — simultaneously a whole (analyzable as a single agent) and a part (decomposable into sub-agents)." With the immediate caveat "the term carries significant mystical baggage from later appropriations. Use sparingly." This is delightful self-aware prior-art-handling. The framework recognizes the conceptual lineage, notes the lexicographic risk, declines to appropriate the term. Exactly the right move. I'd be tempted to note this *positively* as something the framework does well in the §E "what holds" section of the FINAL.

**On segment density and reading-cadence.** This segment is ~100 lines of dense content. The seven segments I've walked so far have ranged from ~50 lines (clean definition) to ~100 lines (this one). The density is sustainable for the audit at current pace, but I notice that this segment alone exposed more potential findings than the prior six combined. The framework's depth lives in the postulate / scope segments, not in the per-object definitions. Watch.
