# Running Final-Report Outline

This outline will change as segments are read.

## Current Audit Emphasis

- Dependency-order and declared-dependency integrity.
- Scope propagation, especially agency vs adaptive scope, Class 1 modularity, composition closure assumptions, and logogenic coupled dynamics.
- Status-label honesty: exact / conditional / formulation / hypothesis / discussion-grade.
- Selected math verification where a worked example or dense derivation looks under-audited.
- Phase-2 triangulation only after a finding survives current src review.

## Candidate Findings

- `scope-adaptive-system` uses $\mathcal C_t$ in its formal condition before `def-chronica` and without declaring the dependency.
- `scope-agency` uses `do(\cdot)` in its formal condition before `def-pearl-causal-hierarchy` and without declaring the dependency.
- Early primitives (`def-agent-environment`, `def-action-transition`, `def-chronica`) are action-coupled, while `scope-adaptive-system` and `post-causal-structure` explicitly include passive observers / zero-coupling systems.
- `post-composition-consistency` imports downstream Section III machinery and undefined symbols too early; likely split candidate.
- `def-mismatch-signal` score-function mismatch has reversed sign if intended as likelihood-increasing / Gaussian-error-equivalent direction.
- `der-action-selection` exact $a_t=\pi(M_t)$ conflicts with Section II's own $\pi(M_t,G_t)$ extension for actuated agents.
- `def-model-sufficiency` lacks a denominator-positive condition for $S(M_t)$.
- `form-event-driven-dynamics` uses $M_{\tau^-}$ without declaring `form-agent-model`.
- `deriv-sector-condition` / `result-sector-persistence-template` / `result-persistence-condition` overstate Model S local stochastic persistence by treating fixed-time tail/RMS bounds as non-exit guarantees.
- `deriv-gain-sector` / `der-gain-sector-bridge` falsely claim one-point sector condition iff local strong convexity.
- `def-adaptive-tempo` exact scalar additive tempo conflicts with its own correlation/anisotropy caveats.
- `hyp-mismatch-dynamics` references `deriv-discrete-sector-condition` in Epistemic Status without declaring it and links to the wrong filename.

## Candidate Non-Finding Observations

- The audit instructions and `CLAUDE.md` conflict on whether to read `TODO.md` at the start of an audit.
I followed the audit-specific instruction and deferred `TODO.md`.
- Recursive-update derivation is sound under C1-C3 and event-driven representation, but status language should harmonize exact/conditional and continuous-coupling caveat.
- Several promoted/draft segments cite `spikes/spike-*` files outside Working Notes, contrary to FORMAT's provenance guidance.

## Coverage Ledger

- Orientation docs read: `README.md`, `OUTLINE.md`, component outlines, `LEXICON.md`, `NOTATION.md`, `CLAUDE.md`, `FORMAT.md`.
- Segment pass through `result-persistence-condition` complete, plus appendix jumps to `deriv-recursive-update`, `deriv-sector-condition`, `deriv-gain-sector`, and `result-sector-persistence-template`.

## Final Report Shape

1. Scope and method.
2. Findings under burden of proof.
3. Integration-debt triangulation for surviving findings.
4. Bigger-picture observations and process feedback.
5. Coverage limits / what I did not verify.
