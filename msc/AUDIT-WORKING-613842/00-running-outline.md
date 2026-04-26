# Running Outline

## Candidate report shape

### 1. Scope and method

- What I read and in what order
- Source-order discipline and any bleed
- What I did not read or only sampled

### 2. Findings under burden of proof

- Placeholder for defended findings in five-element form

### 3. Integration debt vs theory gap

- For each surviving finding, whether the issue is missing theory or missing propagation

### 4. Bigger-picture assessment

- Where the framework is strongest
- Where the framework's architectural honesty is most effective
- Where the framework is still carrying more ambition than its current segment set can support

### 5. Process feedback

- What the de novo instructions improved
- What in the instructions or repo structure made clean execution harder than necessary

## Running watchlist

- Directed-separation caveat propagation into TST and logogenic-adjacent claims
- Composition scope consistency: multi-agent vs composite-agent vs adversarial / partial-opposition cases
- Status discipline in meta-segments and appendix-heavy claims
- Software calibration-lab exactness vs rhetoric
- Worked-example math in discrete-time and strategic-composition appendices
- `#def-adaptive-tempo`: additive definition vs correlated-channel caveat
- Model S persistence summaries: whether region-aware appendix results are compressed too aggressively downstream
- Earlier segments later repaired in `src` but still misleading on first encounter (`#der-action-selection` currently the clearest case)

## Current likely findings

- **Tempo-definition scope drift.**
  `#def-adaptive-tempo` defines scalar tempo by additive equality, then later states the equality is only exact under informationally independent channels and otherwise is an upper bound. This looks like a real definition-scope mismatch rather than a minor caveat.

- **Model-S summary compression.**
  `#deriv-sector-condition`'s Prop A.1S is region-aware (stopped bound + mean-square condition + non-exit estimate), but `#result-sector-persistence-template`, `#result-sector-condition-stability`, and `#result-persistence-condition` often present the stochastic result in cleaner global-looking form. Need to classify as theory gap vs integration debt, but the compression is likely reportable.

- **C-iv strategic-composite route only partially integrated.**
  `#scope-composite-agent` and `#scope-multi-agent` admit equilibrium-convergent adversarial pairs as composites via (C-iv), but several composition-layer segments still reason as if composites require shared objective `O_c`. `#deriv-strategic-composition` itself says the bridge to `#form-composition-closure` remains open, which sharpens this from "mere wording drift" to "scope extension outran full machinery propagation."

## Current non-findings / positive corrections

- The old TST↔logogenic propagation concern does **not** currently survive burden of proof. `02-tst-core/src/scope-developer-agent.md` now explicitly depends on and integrates `#scope-logogenic-agent`, `#def-coupled-update-dynamics`, and `#obs-context-turnover`.
- The discrete-time variance-gap issue cited in the audit-instruction appendix appears repaired in current `src`; the current appendix text no longer makes the older too-strong `O((\eta^\ast)^2)` claim.
- The zero-sum strategic-composition worked example appears corrected in current `src` and openly documents the earlier sign / NE error in Working Notes.
