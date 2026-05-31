# 67 - form-consolidation-dynamics

Source: `01-aat-core/src/form-consolidation-dynamics.md`

## First-pass understanding

This segment makes consolidation explicit as a between-event operating regime: replayed or internally generated pseudo-events update `M` with the objective of closing an IB compression gap, rather than minimizing immediate one-step mismatch. That is a useful distinction and it gives AAT a place to express stability-plasticity tradeoffs, replay, structural adaptation, and logogenic context turnover.

The key boundary is where replay information lives. If the replay event is synthesized entirely from the current complete state `M`, it carries no new information and only reorganizes existing structure. If it is retrieved from a replay buffer, external file, chronica store, or earlier paragraph not currently represented in active `M`, then the pseudo-event is a channel from auxiliary memory into active `M`. The segment needs to keep those two cases separate.

## Diagram attempt

The diagram distinguishes two consolidation channels. Internal replay reorganizes active state and has zero new information under state completeness. Archive replay reloads information from retained traces into the active model, so it is still a Markov update but not zero-information relative to active `M`.

## Findings and watches

- F74 candidate: the segment states consolidation is well-defined only when `nu_consol << nu_online`. That is too strong as written. Consolidation must be timescale-separated from online update, but its useful cadence may need to be fast enough relative to forgetting and event turnover; in offline windows the internal replay update rate can exceed external event rate.
- F75 candidate: the claim `I(e_replay | M_{tau-}) = 0` holds only when replay is generated from information already inside the complete active model state. Examples such as replay buffers, remembered episodes, persistent files, or re-read paragraphs can be outside active `M`; then replay carries information from auxiliary memory into `M`.
- F76 candidate: the stability-plasticity window inherits the unresolved forgetting-threshold convention from `schema-strategy-persistence`. Until the exact lower bound is settled, the feasibility-window inequality should not use the simplified `(1-lambda) > rho/R` as the structural lower bound.
- F77 soft candidate: "all finite-budget agents require consolidation for quality-preserving structural change" overstates the necessity claim. Finite-budget agents may perform incremental online structural adaptation across multiple events; consolidation is necessary under the stronger `(N1)+(N2)` cross-episode integration condition, not finite budget alone.
- Watch: the IB-optimum online-only no-go is explicitly sketch-level; the formal-expression section should avoid stronger "derived" phrasing unless the rate-distortion boundary is supplied.

## Local verdict

The regime is worth naming. Its cleanest formal version should distinguish internal reorganization from auxiliary-memory replay and should express timescale separation as a window, not simply `consolidation much slower than online`.
