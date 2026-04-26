# Finding Verification

This file is the burden-of-proof staging area before the final report. I am keeping the status labels explicit so future readers can see what survived current `src` and what collapsed into "already repaired."

## Candidate F1: `#def-adaptive-tempo` over-defines the additive scalar

### Problematic passage

- `01-aad-core/src/def-adaptive-tempo.md:19` defines adaptive tempo as an unrestricted equality:
  `\mathcal T = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}`.
- The same segment later says the additive formula assumes informationally independent channels and otherwise overcounts:
  `01-aad-core/src/def-adaptive-tempo.md:44-48`.

### Counterevidence search

- The segment does acknowledge the issue itself; this is not a hidden mathematical flaw.
- `01-aad-core/src/der-team-persistence.md:32` also inherits the caveat honestly for communication tempo.
- `01-aad-core/src/result-persistence-condition.md:99` likewise warns that scalar tempo inherits the channel-independence assumption.

### Status determination

- **Still real.**

### Confidence

- **High.**
  The segment simultaneously treats the additive expression as the definition and as a conditional upper bound. That is a clean textual mismatch, not an interpretive stretch.

### Why it still stands

- The caveat does not dissolve the issue because the formal expression and frontmatter status still present the unrestricted equality as the primary definition. If the general quantity is only bounded by the sum under correlation, the corpus either needs:
  1. a restricted definition ("adaptive tempo under channel independence"), or
  2. a general definition plus additive upper-bound surrogate.

My current classification is **integration debt / definition-scope mismatch**, not a deep theory gap.

### `msc/` diagnosis

- `01-aad-core/src/disc-independence-audit.md:59` explicitly records the repair operation: under correlation, scalar tempo should be treated as an upper bound.
- `msc/pending-findings-2026-04-23.md:164` also appears to have already logged the same concern.

So this is emphatically **not** a novel missing insight. It is a propagation / landing issue: the corpus knows the caveat, but the main definition still reads stronger than the repair.

## Candidate F2: Model-S persistence summaries compress away Prop A.1S's region-awareness

### Problematic passage

- `01-aad-core/src/deriv-sector-condition.md:184-194` states Prop A.1S in region-aware form:
  stopped bound, mean-square persistence condition, and non-exit estimate.
- `01-aad-core/src/deriv-sector-condition.md:242-246` then makes the stopping-time localization explicit.
- Downstream summaries compress this into cleaner global-looking statements:
  - `01-aad-core/src/result-sector-persistence-template.md:47-49`
  - `01-aad-core/src/result-sector-condition-stability.md:41`
  - `01-aad-core/src/result-persistence-condition.md:27-29`

### Counterevidence search

- `01-aad-core/src/result-sector-persistence-template.md:90` explicitly says the Model S case uses the region-aware form and that instantiations inherit the stopping-time localization.
- So the framework does know the caveat at the template-discussion level.

### Status determination

- **Still real.**

### Confidence

- **High / medium-high.**
  The underlying mathematics appears honest in the appendix; the issue is the compression in downstream formal summaries.

### Why it still stands

- The downstream Formal Expression sections still read as if the clean mean-square limit is simply "the state satisfies ..." rather than "the stopped process satisfies ..., with unstopped use justified up to non-exit correction under the persistence condition." The later note at template level helps, but it does not fully repair the stronger-looking summary formulas where readers will often stop.

My current classification is **integration debt / scope-honesty drift**, not an error in Prop A.1S itself.

### `msc/` diagnosis

- `msc/SPIKES.md:107` says the A2' strengthening promoted the Prop A.1S region lift into `#deriv-sector-condition` and only an Epistemic Status note into `#result-sector-persistence-template`.
- `msc/spike-a2-prime-strengthening.md:142-143` explicitly says downstream consumers do not need edits.

That is useful context: the current summary compression is not accidental ignorance. It appears to be a judgment call about how much region-awareness had to propagate. My audit judgment is that the current propagation is still too weak in the formal summary layer.

## Candidate F3: C-iv strategic-composite route is admitted before closure machinery is fully reconciled

### Problematic passage

- `01-aad-core/src/scope-composite-agent.md:46-63` admits (C-iv): strategic composites whose macro-state is defined relative to equilibrium structure `\mathcal E`, not shared objective `O_c`.
- `01-aad-core/src/scope-multi-agent.md:73` says composite-level machinery applies via both alignment routes and the (C-iv) strategic route.
- But `01-aad-core/src/form-composition-closure.md:65` still says the framework applies to "the three alignment routes" and ties meaningful composite status to whether `G_c = (O_c, \Sigma_c)` is well-defined.
- `01-aad-core/src/def-unity-dimensions.md:19` and `:40` still describe scope as a three-route disjunction.
- Most importantly, `01-aad-core/src/deriv-strategic-composition.md:119`, `:135`, and `:175` say the bridge from strategic composition to `#form-composition-closure`'s closure-defect machinery is still open.

### Counterevidence search

- There is real progress, not pure contradiction:
  - `#scope-composite-agent` has the C-iv route explicitly
  - `#scope-multi-agent` distinguishes strategic composites from alignment composites
  - `#deriv-strategic-composition` is candid that the closure-defect bridge is open
- So this is not "the framework forgot C-iv." The counterevidence shows partial propagation.

### Status determination

- **Still real.**

### Confidence

- **High.**
  The contradiction is not merely between old and new segments; it is partly inside the current composition layer itself.

### Why it still stands

- The current corpus is simultaneously saying:
  - C-iv composites are in scope,
  - C-iv composites have equilibrium-based macro-state rather than shared `O_c`,
  - and some closure / unity machinery still presumes shared-objective composites while one of the main C-iv segments openly says the bridge to closure-defect remains open.

My current classification is **hybrid**:

- **integration debt** where route-count / wording / downstream references still reflect the older three-route alignment frame
- **theory-open component** where closure-defect machinery for equilibrium-statistic composites is not yet actually derived

### `msc/` diagnosis

- `msc/spike-strategic-composition.md:443` already states that the bridge from strategic composition to closure-defect is open.
- `msc/spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md:297` sharpens the adversarial / strategic regime as structurally outside the contraction-template bridge.
- `msc/pending-findings-2026-04-25.md:109` points to an architectural restructure option (`SP-21`) that would split the routes into distinct composite ontologies.

So the corpus already contains both:

- a **local repair story** ("be more careful about which machinery really propagates to C-iv")
- and a **bigger architectural option** ("stop forcing one composite ontology to do multiple jobs")

This makes F3 the most interesting finding of the pass: it is not just a stale sentence, and it is not just a missing theorem. It is a live design fork the repo has already begun to notice.

## Candidate F4: old TST↔logogenic propagation concern

### Status

- **Does not survive current `src`.**

### Why

- `02-tst-core/src/scope-developer-agent.md` now depends on:
  - `#scope-logogenic-agent`
  - `#def-coupled-update-dynamics`
  - `#obs-context-turnover`
- And the body explicitly distinguishes Class 1 human developers from Class 2 logogenic developer-agents.

This matters because the audit-instruction appendix still cites the older concern as a calibration example. In the current repo state, it reads as historical rather than live.
