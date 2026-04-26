# Composition and Cross-Component Pass

## Section III: current shape

My strongest new impression from the composition layer is that the framework has now made a genuinely interesting scope move:

- adversarial / partially-opposed pairs are no longer categorically outside composite scope
- they are admitted via `#scope-composite-agent` route **(C-iv)** when the strategic interaction has equilibrium structure
- `#scope-multi-agent` has been updated to distinguish agent-level adversarial machinery from composite-level strategic-composite machinery

This is a real conceptual broadening, not a cosmetic tweak. It also creates the sharpest integration pressure in the current corpus.

## Where the pressure shows

`#scope-composite-agent` now says:

- (C-iv) strategic composites exist without shared objective `O_c`
- the macro-state is defined relative to equilibrium structure `\mathcal E`

But nearby composition machinery still often reasons in the older alignment-only idiom:

- `#form-composition-closure` still says the framework applies to "the three alignment routes" and treats ill-defined `O_c` as the reason a composite is not meaningful
- `#def-unity-dimensions` still describes the scope as a three-route disjunction and treats composition-level quantities as unavailable whenever the three alignment routes fail
- `#deriv-strategic-composition` is locally honest that the bridge from strategic composition to closure-defect machinery remains open

So the current state is not "the framework forgot C-iv entirely." The current state is subtler:

- the **scope layer** has accepted C-iv
- the **strategic-composition segment** has accepted that this route is structurally different
- but the **closure / unity machinery** still partly assumes the older shared-objective ontology

That feels like a real, high-signal integration issue.

## TST / logogenic pass

I expected to find more drift here than I actually did.

The targeted TST/logogenic pass was mostly reassuring:

- `#scope-developer-agent` explicitly depends on `#scope-logogenic-agent`, `#def-coupled-update-dynamics`, and `#obs-context-turnover`
- the AI-developer mapping now explicitly carries the Class-2 / coupled-update caveat instead of silently importing modular Section II machinery
- `#obs-software-epistemic-properties`'s calibration-lab framing is more careful than older "software is best domain" rhetoric
- `#scope-observation-ambiguity-modulation` and `#result-coupled-diagnostic-framework` are surprisingly disciplined about what survives exactly versus only approximately

This matters for the final report because one of the instruction appendix's example findings (`scope-developer-agent` ignoring logogenic caveats) no longer appears live in current `src`.

## Process notes from this pass

- `03-logogenic-agents/OUTLINE.md` still has a row-order dependency violation: `#result-coupled-diagnostic-framework` appears before `#scope-observation-ambiguity-modulation` despite depending on it.
- The global frontmatter graph still contains the 7-segment strategic-tempo SCC noted earlier, so a strict mechanical topo walk remains impossible in the active corpus.

These are process / repo-hygiene issues, not theory findings, but they matter because the new audit instructions currently assume a cleaner dependency surface than the repo actually provides.
