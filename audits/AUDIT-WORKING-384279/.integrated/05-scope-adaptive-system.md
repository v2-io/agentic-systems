# 05 — scope-adaptive-system

*Type: scope. Status: axiomatic. Stage: claims-verified. Depends: [def-agent-environment, def-observation-function, def-chronica].*

## Predictions vs evidence
Predicted: broadest-scope definition pointing forward to `#scope-agency`. Found: exactly that, with two minimal conditions ($\mathcal{O}\neq\emptyset$ and $H(\Omega_t\mid\mathcal{C}_t)>0$) and explicit exclusions.

## Cross-segment consistency
Forward-refs to `#scope-agency`, `#def-mismatch-signal`, `#emp-update-gain`, `#def-adaptive-tempo`, `#result-persistence-condition`. Depends includes `def-chronica`, which transitively requires `def-action-transition`. Note: this scope explicitly says "none of which need to *act*" (line 16) — but the chronica formalism *does* include actions. The framework relies on degenerate / null actions for passive observers without saying so.

## Math verification
$H(\Omega_t\mid\mathcal{C}_t)>0$ — well-typed conditional entropy. Scope set $\mathcal{S}_\text{adaptive}$ as predicate-defined subset of (Agent, $\Omega$) pairs. No errors.

## Prose-coherence observations
1. "Section I" used (lines 16, 33, 48) — same terminology mix-with-`Part` I flagged earlier. Cumulative now: three foundational segments and the README-auditor all use "Section I"; OUTLINE.md uses "*Part*". Almost certainly a sweep that hasn't fired.
2. Considerable duplication across preamble/Formal-Expression/Discussion of the same "what's included / what's excluded / narrowing to agency" content. Within FORMAT.md cadence but feels redundant. Not a finding; observation about pedagogical voice.

## Watch list (update)
- **Passive-observer treatment of action sequence.** Scope says action not required; chronica says action interleaves with observation. The reconciliation (null actions / no-op actions for passive systems) is not made explicit anywhere I've read so far. May surface as a real issue if downstream segments invoke the chronica for purely-passive systems and need to define $a_t = \emptyset$.

## Next-segment predictions
`#scope-agency`. Will narrow to systems with Pearl-level-2 contrast: distinct actions yield distinct interventional distributions. May invoke `#def-pearl-causal-hierarchy` (Part II definition) — if so, that's a forward reference into Part II, which would be acceptable since "the agency-scope narrowing is structurally Part-II-bound."

## What I'd change
The duplication of included/excluded/narrowing content across preamble+FE+Discussion could be tightened — preamble could carry the prose narrative, FE could be just the set definition, Discussion could carry the narrowing-to-agency pointer. The current segment's structure has each of these three sections doing 80% of the same job. Not finding-worthy but observable.

## Curiosity
The exclusion of "pure mathematical-proof engine working from axioms" ($\mathcal{O}=\emptyset$) is interesting given that *AI mathematicians* are increasingly in scope. An LLM doing proof exploration has $\mathcal{O}\neq\emptyset$ (it observes its own intermediate results, the proof state, etc.). So the exclusion targets a pure-axiom-deductive engine, not anything realized as a learned model. The framing is correct but might warrant a half-sentence noting that AI-mathematician-style systems are *not* in this exclusion.

## Wandering thoughts

**On the Kalman-filter-as-canonical-example move.** Line 33 names Kalman filters as Section I subjects. A Kalman filter "knows its own dynamics" in the sense that the model matrix is given — but the *true* environment state is hidden behind partial observability + noise, so $H(\Omega_t\mid\mathcal{C}_t)>0$ holds. This means the AAT scope condition correctly admits Kalman even when dynamics are known. The framework will later claim that the persistence condition $\alpha > \rho/R$ instantiates as the Kalman stability margin. This instantiation requires that the Kalman's *known-dynamics* assumption doesn't violate adaptive-scope; the conditional-entropy framing makes this work cleanly. Good move.

**Section vs Part is now a sweep candidate.** I've seen 4-5 segments use "Section I/II/III" terminology consistently. The OUTLINE.md inside AAT uses "Part" headings. The top-level OUTLINE.md uses "Part I — Adaptation and Actuation Theory" as the AAT-level container, then refers to AAT-internal substructure (sections I/II/III). So we have:
- Top OUTLINE: AAT = "Part I"
- AAT OUTLINE: substructure = "*Part* Adaptive Systems Under Uncertainty"
- AAT segments: substructure = "Section I"
- README-auditor: substructure = "Section I/II/III"

The cleanest read: top OUTLINE treats AAT as "Part I" of the framework; AAT's internal substructure is called either "Section I/II/III" (in segment prose + README-auditor) OR "*Part*" (in AAT OUTLINE.md). The two terms are doing the same job in different places. Probably segment prose is canonical (it's the most-read), so AAT OUTLINE.md's "*Part*" headings should change to "*Section*" — OR the segment prose should change to "Part I" — OR both should stay and the top-OUTLINE distinction handles disambiguation. This is a §G process-feedback observation more than a finding: surfacing a corpus-wide terminology drift that should be normalized.

**Possible finding building.** The "Section" terminology drift is now a corpus-wide pattern. I'll formalize this as a potential finding when I see it in 5+ more segments (which I expect to).
