# 06 — scope-agency

*Type: scope. Status: axiomatic. Stage: claims-verified. Depends: [scope-adaptive-system, def-action-transition].*

## Predictions vs evidence
Predicted: narrowing to Pearl-level-2 contrast, would use `do(·)` and forward-ref Pearl hierarchy. Found: exactly that.

## Cross-segment consistency
Forward-refs `#def-pearl-causal-hierarchy`, `#der-loop-interventional-access`, `#der-causal-hierarchy-requirement`, `#def-agent-spectrum` — all Part II segments. The segment uses the $do(\cdot)$ operator interventionally without `def-pearl-causal-hierarchy` in its `depends:` list. Body line 30 acknowledges this with the parenthetical "(where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy)."

## Dependency-graph observation (candidate finding)
The segment uses Pearl's $do(\cdot)$ operator in its Formal Expression but does NOT list `def-pearl-causal-hierarchy` in `depends:`. Two possible readings:
1. **External-prior reliance** (charitable): Pearl 2009 is treated as external known machinery, like measure theory or Bayes' rule — no depends needed because the operator is part of the technical reader's prior knowledge.
2. **Undeclared dependency** (strict): When AAT has an internal segment for an external concept (`def-pearl-causal-hierarchy` is an explicit recapitulation), the segment using that concept should declare it in `depends:`.

Per FORMAT.md Gate 1 criterion 4 ("No missing dependencies — if the Formal Expression uses a quantity defined elsewhere, that slug appears in `depends:`"), reading (2) seems indicated. The Formal Expression uses $do(\cdot)$ which has an explicit segment-level definition; that segment should be in depends. **Severity: low; type: dependency-graph violation; disposition: probably *Known-unintegrated* or editorial.** I'll watch for similar patterns in other scope segments.

## Math verification
$|\mathcal{A}|\geq 2$ and $\exists a\neq a':P(o\mid do(a))\neq P(o\mid do(a'))$ — well-typed given $do(\cdot)$ as primitive. The set-intersection form $\mathcal{S}_\text{agency} = \mathcal{S}_\text{adaptive} \cap \{...\}$ is clean.

## Prose-coherence observations
1. "Section I/II/III" terminology again (lines 17, 19, 32, 49). Pattern continues — 4 segments in a row with "Section" rather than "Part." Strong corpus-wide signal.
2. Line 19 ("Sections II and III do not — they can model, but they cannot learn causal structure or rationally plan against it") is mildly strong. Passive observers *can* learn causal structure under additional identifiability conditions (observational identification via Pearl's do-calculus rules). The claim is technically that *AAT's planning machinery* requires Level 2, not that no causal-structure learning is possible. Soft-overreach in prose; technically accurate read possible if "rationally plan against" is implicitly relativized to AAT's framework. Low-severity wording polish.

## Watch list (update)
- Pattern: cross-Part forward-refs are used liberally but inconsistently declared in `depends:`. The dep-graph linter probably reads this correctly (only direct uses), but for OUTLINE-order verification it matters whether downstream concepts are "primitive imports" or "real dependencies."

## Next-segment predictions
`#post-composition-consistency`. Postulate about composition consistency across scales. The OUTLINE marks it "(possibly out of place)" in italics — interesting. The "possibly out of place" annotation suggests the project knows this is a structural-position question, which is honest curation. Will probably formalize that AAT scope conditions apply at any level of agent description.

## What I'd change
Add `def-pearl-causal-hierarchy` to depends if reading (2) is correct — and reading (2) seems indicated by the FORMAT.md gate criterion. Alternatively, the framework could canonicalize the read that "external concepts have an AAT segment but are also treated as primitives" — but that should be stated as a convention somewhere.

## Curiosity
The nominal-agent exclusion ("choices that make no difference") is a clean exclusion criterion that I haven't seen articulated this way in the literature. Most planning literatures implicitly assume action-effect causality; AAT names it as a scope condition explicitly. Worth carrying.

## Wandering thoughts

**Pearl's $do(\cdot)$ as external-import-with-AAT-segment.** The framework's pattern for handling external imports varies. Some imports (Cauchy's functional equation, Čencov invariance, Pinsker's inequality) seem to be "primitive imports" without AAT segments. Others (Pearl's hierarchy, Cramér-Rao, the information bottleneck) have AAT segments that recapitulate at AAT's level of deployment. The convention for `depends:` declaration would naturally split on this distinction — primitive imports don't need a segment-level dependency; recapitulated-imports should. The framework's current practice seems to be partial-declaration. Worth surfacing as a §G process question.

**The four-condition agency scope (numbered 3, 4 in this segment, continuing from 1, 2 in scope-adaptive-system).** Subtle nice touch — the Formal Expression's numbered list (3, 4) continues the count from scope-adaptive-system's (1, 2). A reader walking the scope cascade in order sees a single numbered specification growing. This is a small piece of prose-coherence quality. Good.

**On the cumulative scope-cascade.** Section I has two scopes (adaptive, agency). Part II's preface names a four-tier lattice (adaptive / agency / learning-agent / Class 1 architecture). The four-tier lattice will appear when I reach Part II. The progression so far is honest about being a cascade rather than a fixed boundary — different theorems live at different rungs of this lattice. This is methodologically sophisticated: most theory frameworks claim one scope; AAT explicitly maps theorem-scope to lattice-position. Strong choice.
