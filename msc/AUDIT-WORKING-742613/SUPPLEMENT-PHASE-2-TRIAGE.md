# Phase 2 Triage Supplement

Date: 2026-04-25

This supplement was written after the initial de novo pass, with the de novo embargo lifted by the user for Phase 2. I searched active tracking documents (`TODO.md`, `PROPOSALS.md`, `CHANGELOG.md`, `LOG.md`), current source segments, and `msc/` spike / pending-finding material for the main findings in `FINAL-2026-04-25.md`.

I also ran `bin/lint-outline`. Current output: 111 outline entries, 111 segment files, 0 ordering violations, 0 missing dependencies, 0 orphan segments, and 27 intentional backmatter references. That matters for the dependency findings below: several issues are not frontmatter graph failures according to current tooling; they are body-level hidden dependencies, wrong links, or "appendix reference is not really a proof-only dependency" cases.

## Triage Summary

| Finding | Phase 2 status | Practical interpretation |
|---|---|---|
| Score-function mismatch sign | **Likely new / not durably tracked** | High-confidence local math bug. I found no active TODO / proposal / spike entry identifying the sign reversal in `#def-mismatch-signal`. |
| Model S ever-exit persistence | **Partly represented, not correctly integrated** | TODO mentions Prop A.1S localization, and the disturbance spike uses fixed/stationary tail language. The promoted source overstates this into an ever-exit probability bound. |
| Gradient "equivalence" iff | **Known distinction, unrepaired offender** | Newer template/spike material correctly distinguishes one-point vs two-point monotonicity, but `#deriv-gain-sector` and bridge wording still make the false iff claim. |
| Adaptive tempo exactness | **Known caveat, formal/status mismatch** | The caveat is already in source and cross-source caveat segments; the remaining issue is that the definition/status still presents the additive scalar expression too strongly. |
| `a_t = \pi(M_t)` exactness | **Known supersession, integration debt** | Section II state-lift material explicitly supersedes this with `\pi(M_t,G_t)`, but the earlier exact segment still reads too generally. |
| Dependency/order failures | **Mixed: tooling gap + prior-noted fragments** | Current lint is clean, but it misses body-level symbol uses, wrong links, and non-proof appendix imports. Some fragments appear in older audit notes; several are not in durable TODO tracking. |
| Passive observers vs action-coupled primitives | **Known conceptual tension, integration debt** | The framework explicitly wants passive observers in adaptive scope, while early primitives still define "agent" through action effects. Needs a primitive/scope cleanup, not a new theorem. |
| Model-sufficiency denominator zero | **Likely new local well-definedness gap** | I found no active tracking entry. It is small but should be fixed because downstream ratios inherit the undefined case. |

## Finding-Level Notes

### 1. Score-function mismatch sign

I searched for score-function, likelihood-increasing direction, Gaussian-error equivalence, and mismatch-sign language across active docs, spikes, and source. Hits were ordinary references to `#def-mismatch-signal`, not a correction.

Assessment: this appears to be a new durable finding. A prior audit reflection in `msc/AUDIT-WORKING-849201/17-def-mismatch-signal.md` praised the score-function formulation rather than flagging the sign, so this was probably missed rather than tracked elsewhere.

Recommended repair: in `01-aad-core/src/def-mismatch-signal.md`, either remove the minus sign or redefine the prose so the object is explicitly a negative-gradient / loss-gradient direction. Given the current prose says likelihood-increasing and Gaussian-error-equivalent, the cleaner repair is:

```tex
\tilde{\delta}_t = \nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})
```

### 2. Model S ever-exit persistence

Relevant prior material exists, but it does not close the specific bug.

Evidence:

- `TODO.md:311` and `TODO.md:687` say "Prop A.1S region condition lifted via stopping-time localization."
- `msc/spike-disturbance-model-split.md:157-167` applies Markov's inequality to a fixed/stationary tail probability `P(||δ|| > R)`, not to `P(τ_R < ∞)`.
- `msc/pending-findings-2026-04-25.md:37-48` tracks a different Model S issue: the discrete-to-continuous variance gap, not the ever-exit probability.

Assessment: this is best classified as an integration error from spike/cautious-localization material into source. The spike-level claim "at steady state, probability outside `R` is small" became, in source, "probability of ever exiting is small." Those are mathematically different. For nondegenerate OU-like noise, the ever-exit probability from any finite ball is generally 1.

Recommended repair:

- Replace `P(τ_R < ∞)` with a fixed-time, stationary, or finite-horizon probability statement.
- If the segment needs a local theorem, define a stopped process and state the bound only up to `t \wedge τ_R`.
- If the intended claim is true non-exit, add much stronger hypotheses, e.g. bounded/noise-vanishing-at-boundary or invariant-domain conditions. Standard additive Brownian noise will not support it.

### 3. Gradient "equivalence" iff

This issue is already well understood elsewhere in the repo, but not propagated to the offending segment.

Evidence:

- `01-aad-core/src/result-sector-persistence-template.md:70-72` correctly says AAD's sector condition is one-point anchoring and is strictly weaker than full two-point strong monotonicity.
- `TODO.md:181` records the operator-sector unification as one-point reduction of strong monotonicity and identifies AAD's one-point anchoring as distinctive.
- `msc/spike-jacobian-b1-strengthening.md:114-120`, `:195`, `:538`, and `:558` explicitly discuss the gap between one-point sector and incremental / two-point strong monotonicity.

Assessment: not new as a conceptual distinction. It is still a real source bug because `01-aad-core/src/deriv-gain-sector.md` and `01-aad-core/src/der-gain-sector-bridge.md` retain "iff / equivalence" language. The current source simultaneously contains the correct distinction in `#result-sector-persistence-template` and the false equivalence in the gain bridge.

Recommended repair: replace the iff with:

```text
Local strong convexity is sufficient for GA-3 / one-point sector.
GA-3 itself is the weaker one-point condition.
Full two-point / incremental monotonicity is needed only where composition or contraction arguments require it.
```

### 4. Adaptive tempo exactness

This is already represented as a caveat in several source locations.

Evidence:

- `01-aad-core/src/def-adaptive-tempo.md:44-50` says additive scalar tempo overcounts correlated channels and fails under anisotropic correction.
- `01-aad-core/src/disc-independence-audit.md:59` states the additive formula is an upper bound, with equality iff channels are informationally independent.
- `01-aad-core/src/result-persistence-condition.md:99` carries the caveat into persistence.
- `01-aad-core/src/der-team-persistence.md:32` and `01-aad-core/src/der-tempo-composition.md:94` propagate the multi-agent caveat.
- `PROPOSALS.md:234` proposes an "independence profile" that explicitly includes channel independence and scalar-tempo appropriateness.

Assessment: the caveat is not new. The finding is that the caveat is not integrated into the formal/status layer. `#def-adaptive-tempo` is still `status: exact` and presents the additive scalar expression as the definition rather than as nominal tempo under independence/isotropy assumptions.

Recommended repair: introduce `\mathcal T_{\mathrm{add}}` or `\mathcal T_{\mathrm{nominal}}`, define effective tempo separately, and make exactness conditional:

```text
\mathcal T = \sum_k \nu^{(k)}\eta^{(k)*}
```

is exact only under channel independence and scalar/isotropic reduction; otherwise it is an upper bound or summary statistic.

### 5. `a_t = \pi(M_t)` exactness

This is already handled in later source, but not back-propagated cleanly.

Evidence:

- `01-aad-core/src/form-complete-agent-state.md:36` defines `a_t = \pi(M_t,G_t)`.
- `01-aad-core/src/form-complete-agent-state.md:52` explicitly says `#der-action-selection` is superseded by `a_t = \pi(M_t,G_t)` after the state lift, with `a_t=\pi(M_t)` surviving for Section I agents where `G_t=\emptyset`.
- `01-aad-core/src/def-model-sufficiency.md:40` already uses the later `\pi(M_t,G_t)` standard.
- `01-aad-core/src/def-value-object.md:33-39` treats goal/objective and continuation policy as fixed parameters for the value query, which is compatible with the richer policy state when scoped carefully.

Assessment: known supersession / integration debt. The formal claim in `#der-action-selection` should be restated as `a_t=\pi(X_t)` for complete internal state, with `X_t=M_t` only in the Section I / no-purposeful-substate case.

Recommended repair: downgrade or conditionalize the `M_t`-only expression in `#der-action-selection`; add an explicit "superseded by complete-agent-state lift" note to the Formal Expression or Epistemic Status, not only Discussion.

### 6. Dependency/order failures

Current lint reports 0 ordering violations and 0 missing dependencies, so the finding is not "the existing frontmatter graph is obviously failing." The problem is that the current graph/lint contract is too coarse for what the audit instructions ask auditors to verify.

Evidence from active tracking:

- `TODO.md:6-7` and `LOG.md:94` report recent outline-ordering and dependency cleanup, with lint clean.
- `bin/lint-outline` currently reports 0 ordering violations and 0 missing dependencies.
- The linter explicitly classifies `form-consolidation-dynamics -> disc-compression-operations` as a backmatter reference, but my audit concern is that `disc-compression-operations` is not merely a proof appendix; it imports downstream conceptual machinery.
- `PROPOSALS.md:98` tracks composition-closure consolidation residue including `#post-composition-consistency`.
- `TODO.md:466` tracks "Composition timescale heuristic outruns bridge conditions" as open in `#post-composition-consistency`.

Evidence from prior local audit material:

- `msc/AUDIT-WORKING-584721/01-section-i-leaves.md:13-19` already identified `scope-adaptive-system` missing `def-chronica` and the passive-observer chronica subtlety.
- `msc/AUDIT-WORKING-584721/08-def-mismatch-signal.md:32` noted `form-event-driven-dynamics -> form-agent-model` drift as an independent dependency issue.

Assessment: this cluster is mixed. Some individual issues were seen by prior audit agents but were not promoted into durable active tracking. Others are new or at least not durably tracked, especially wrong links like `discrete-sector-condition.md` versus `deriv-discrete-sector-condition.md` and source-body references that lint does not inspect.

Recommended repair:

- Add a second lint mode for body-level canonical symbols and slug links, not just declared dependencies.
- Split backmatter references into proof-only appendices versus conceptual/meta appendices. The audit rules should not treat all Appendix A references as harmless.
- Promote the specific wrong-link and hidden-dependency cases into TODO or a small cleanup batch.

### 7. Passive observers vs action-coupled primitives

This tension is already conceptually visible in source.

Evidence:

- `01-aad-core/src/def-agent-environment.md:11` and `:23` define agents as producing actions that affect the environment.
- `01-aad-core/src/scope-adaptive-system.md:41` explicitly includes passive observers / nominal agents in adaptive scope.
- `01-aad-core/src/post-causal-structure.md:36-38` says zero-coupling systems remain inside adaptive scope if they observe under residual uncertainty.
- `01-aad-core/src/def-agent-spectrum.md:44` says passive trackers, including passive Bayesian learners with no action choices, are fully within Section I's scope.
- Prior audit notes also noticed this: `msc/AUDIT-WORKING-584721/01-section-i-leaves.md:19` and `msc/AUDIT-WORKING-742613/04-scope-adaptive-system.md`.

Assessment: this is not a newly discovered conceptual requirement. It is a terminology/primitive integration problem. The theory wants a broad "adaptive system" primitive and a narrower "agency" primitive, but the first foundational definition uses action-affecting "agent" language too early.

Recommended repair: introduce a neutral Section I primitive such as `(AdaptiveSystem, Ω)` or define an action channel as optional/degenerate until `#scope-agency`. Reserve action-effect requirements for agency-scope results.

### 8. Model-sufficiency denominator zero

I searched active TODO/proposals/spikes for denominator-zero handling around `#def-model-sufficiency`. I found downstream uses of model sufficiency and unrelated normalization/denominator issues, but no durable tracking entry for this edge case.

Assessment: likely new local well-definedness gap. It is not a large theorem-level problem, but it affects the definition and downstream ratios such as model-class fitness and structural-adaptation necessity.

Recommended repair: add a convention:

```text
S(M_t) is defined when I(C_t; o_{t+1:\infty} | a_{t:\infty}) > 0.
When the denominator is 0, predictive sufficiency is vacuous; either define S=1 by convention if the numerator is also 0, or mark the quantity undefined/not applicable.
```

The "undefined/not applicable" convention is cleaner if downstream results depend on nonzero predictive information.

## Process Feedback From Phase 2

Phase 2 materially improved the audit. Without it, I would have over-classified the gradient-equivalence and adaptive-tempo findings as new. They are better understood as integration failures: the repo already contains the correct ideas, but not in the offending formal statements.

The instructions should explicitly name this second pass as a required final step:

```text
After the de novo pass, search TODO/proposals/spikes/pending findings for each finding and classify it as new, known-but-unintegrated, already-resolved, or false-positive.
```

I would also add a durable triage vocabulary to the instructions:

- **New**: no durable tracking found; add to pending findings.
- **Known-unintegrated**: correct idea exists elsewhere; source segment still wrong.
- **Known-resolved**: source already fixed; audit finding is stale.
- **Tooling gap**: source may be structurally okay under current tools, but audit exposed a class the tools do not check.
- **Scope/status mismatch**: caveat exists in prose but not in Formal Expression / status / theorem statement.

That vocabulary would keep future Codex instances from treating every rediscovery as a fresh contradiction.
