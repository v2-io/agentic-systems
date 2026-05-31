# Reflection 05 — form-event-driven-dynamics (Section I row 14)

## §4.2 dependency check

`depends: [post-causal-structure, def-observation-function, def-action-transition]` — all upstream (rows 8, 2, 3). **No backward-dependency finding.**

But: the Formal Expression uses $M_{\tau^-}$ (model state) in the event-information-content definition $\mathcal I(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$. The model symbol $M$ is defined in `form-agent-model` (row 10). Tracing transitively:

- `post-causal-structure`: depends [def-agent-environment, def-chronica] — no `form-agent-model`
- `def-observation-function`: depends [def-agent-environment] — no `form-agent-model`
- `def-action-transition`: depends [def-agent-environment] — no `form-agent-model`

`form-agent-model` is missing from both the direct depends and the transitive closure. **F-A4: form-event-driven-dynamics depends drift — missing form-agent-model.**

This is the fourth instance of the depends-list-incomplete-relative-to-Formal-Expression pattern. Summary so far:

| # | Segment | Symbol used | Defining segment missing |
|---|---------|-------------|--------------------------|
| F-A1 | scope-adaptive-system | $\mathcal C_t$ | def-chronica |
| F-A2 | form-information-bottleneck | $a_{t:\infty}$ | def-action-transition |
| F-A3 | def-model-sufficiency | $a_{t:\infty}$ | def-action-transition (propagated through F-A2) |
| F-A4 | form-event-driven-dynamics | $M_{\tau^-}$ | form-agent-model |

Four instances in the first 14 segments. This is now firmly a *systematic* discipline issue, not a few isolated misses. Recommend the report's Section B include a dedicated finding for the pattern with the recommended mechanical sweep, plus the individual instances catalogued.

## Other observation: a possibly-stale cross-reference

The Discussion's last paragraph: "This decomposition is a Section IV gap (see the three-part tempo decomposition gap in `AAD-FULL.md`)."

"Section IV" was the old TST location *before* TST was extracted to `02-tst-core/` per the project's structural reorg. `AAD-FULL.md` is not a file I've encountered in the current root directory. This reference looks stale — pointing to either a retired file or a retired numbering convention. Worth flagging.

This is a genuine finding distinct from the depends-drift pattern. Listing as F-B1 (the "B" series for non-depends-list issues):
- F-B1: form-event-driven-dynamics references "Section IV" / `AAD-FULL.md` — both appear to be retired structures from before the four-component split. Possible stale documentation.

I'll verify when the audit reaches §6.1 Phase-2 (msc/git/etc. become accessible). For now: flagged at confidence-low (the file might still exist somewhere; I haven't checked), but the "Section IV" usage is unambiguously stale per CLAUDE.md's "TST was originally absorbed as 'Section IV' but has been restored to its own space."

## Predictions vs. evidence

No specific prediction for this segment. The content is **pretty much what I expected** — multi-channel multi-rate generalization of the discrete-time recursive update. The software-specific channels table at the end is a nice domain instantiation.

## Cross-segment consistency

- Forward reference to `#der-recursive-update` (presumably row 15 area): fine.
- Forward reference to `#def-mismatch-signal`, `#emp-update-gain`, `#def-adaptive-tempo`: fine.
- The identification $\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)*} = \mathcal T$ is the segment's main bridge to adaptive tempo.

## Math verification

The event information content $\mathcal I(e_\tau) = I(e_\tau; \Omega_\tau \mid M_{\tau^-})$ is a standard mutual information (event vs. environment, conditioned on prior model state). Well-typed.

The effective adaptation rate sum $\sum_k \nu^{(k)} \cdot \eta^{(k)*}$ has units of [events/time] × [dimensionless ratio] = [1/time], consistent with $\mathcal T$ being a rate per NOTATION.md. Dimensional check passes.

## Status-label / discipline

`status: robust-qualitative` for a formulation. Honest (the qualitative claim survives across architectures; specific functional forms approximate).

`stage: deps-verified`. Given F-A4, this stage label may be aspirational — a Gate 1 audit should have caught the missing form-agent-model dependency. Either Gate 1 didn't run on this segment, or the auditor missed the $M_{\tau^-}$ usage in the Formal Expression.

## What am I now curious about?

- The $\Omega_\tau$ symbol — environment state at time $\tau$. NOTATION.md defines $\Omega_t$ for the discrete-time case. The continuous-event-time variant $\Omega_\tau$ is used here. Is the smooth-time extension formally addressed anywhere, or implicitly assumed? Not strictly required for the formulation (the rate-of-events framing handles asynchrony), but worth checking.
- The software-channel table doesn't include $\eta^{(k)*}$ values, which would tighten the connection to adaptive tempo. Is there a software-domain segment that fills in those rates? May be in TST.

## Outline updates

Adding to Section B (findings):
- F-A4: depends drift — missing form-agent-model
- F-B1: stale "Section IV" / AAD-FULL.md reference (low confidence pending verification)

Section B should now include a *meta-finding* for the F-A* pattern — depends-list discipline.

## Cadence check

One Read → reflection → next Read. Holding.

Next: Section I row 15 = `der-recursive-update`.
