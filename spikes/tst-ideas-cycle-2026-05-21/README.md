# TST-IDEAS spike cycle — 2026-05-21

Cluster of 7 parallel spikes launched from [`TST-IDEAS.md`](../../TST-IDEAS.md) §7, derived from the mining cycle substrate at [`../tst-mining-2026-05-21/`](../tst-mining-2026-05-21/). **The canonical synthesis of this cycle's resolution lives in [`TST-IDEAS.md`](../../TST-IDEAS.md) §9 — read that first.** This README is a directory-level navigator; it does not duplicate the synthesis content.

## Why these are clustered

These seven spikes share substrate (the 2026-05-21 mining cycle), share a synthesis pass (`TST-IDEAS.md` §9), and cross-reference each other extensively (each spike names which sibling-spike resolutions it assumes or depends on). Treating them independently at integration time would lose the convergence — four pieces of machinery surfaced across multiple spikes from different starting points, and segment-landing decisions about wrapper-level persistence, matrix-Loewner channel bottleneck, $W_1$/$W_2$ regime hierarchy, and crash-early-as-structural-commitment have to be made consistently across the cluster. The synthesis pass at `TST-IDEAS.md` §9 enumerates the convergence points and the cross-spike seams the integration agent needs to reconcile.

**Integration discipline.** Future integration efforts should (a) read `TST-IDEAS.md` §9 first for the convergence + segment-ready inventory, (b) treat the seven spikes as one decision-batch rather than seven independent items, (c) preserve the honesty calls surfaced in §9 (generative-citation risk on $\alpha \approx 0.31$, Ebbinghaus $\tau$ unvalidated for code, vanilla GenServers ≈ Tier-1 not Tier-3, etc.).

## The seven spikes

Listed in the order recommended for *segment-landing priority* per `TST-IDEAS.md` §9, which is *not* the order they were launched in:

| # | File | One-line content | Status |
|---|------|------------------|--------|
| 2 | [`spike-class-coercion-via-supervision.md`](spike-class-coercion-via-supervision.md) | Six concrete additions to `#der-class-coercion-via-wrapping`; theorem-grade wrapper-level persistence inequality in §3 (answers "what is $\rho$ for a microservice?"). | segment-ready |
| 1 | [`spike-running-software-agent.md`](spike-running-software-agent.md) | Four candidate segments for runtime-agent chapter: scope / observation channels / persistence / tempo decomposition. Adaptive-dispatch scope cut held sharp. | segment-ready (placement decision pending) |
| 5 | [`spike-developer-tempo-channels.md`](spike-developer-tempo-channels.md) | $\mathcal T_\text{dev} = \mathcal T_\text{obs} + \mathcal T_\text{explore} + \mathcal T_\text{probe}$ from principled axis (Pearl-level × commitment-status). Refused the $W_1$/$W_2$ analogy for probe disposability. | segment-ready |
| 4 | [`spike-software-unmaintainability-bifurcation.md`](spike-software-unmaintainability-bifurcation.md) | $(K, W)$ 2-state model; bifurcation under named monotonicities; G1/G2/G3 with boxed sufficient condition $(\star)$. | segment-ready at *conditional* tier |
| 3 | [`spike-actuated-rho-regulation.md`](spike-actuated-rho-regulation.md) | Action-space partition with admission-control; cost reduces to existing sat-gap; sign-condition for when admission-control net-helps. | segment-ready pending §3.3 seam |
| 6 | [`spike-substrate-modifying-actions.md`](spike-substrate-modifying-actions.md) | Framing dissolved: sub-classification within class 4 (4a/4b/4c), not peer fifth class. Macro-hygiene as W₁ wrapping (structural analogy). | follow-on cycle |
| 7 | [`spike-ets-as-third-w-regime.md`](spike-ets-as-third-w-regime.md) | Resolved: no $W_{1.5}$ needed. The W axis is *type-of-bound* (structural-by-type-signature vs behavioral-by-compliance), not heap-disjointness vs shared-region. | resolved |

## Cross-spike dependencies (the integration seams)

These are the cross-references each spike explicitly names. The integration agent should resolve them as a batch:

- **Spike 1 ← Spike 2.** `#der-runtime-persistence-condition` (spike 1) *cites* the wrapper-level persistence theorem (spike 2 §3). Clean seam — runtime-agent segment uses the theorem as a prerequisite rather than re-deriving it.
- **Spike 1 ← Spike 3.** Runtime persistence condition (spike 1) interacts with actuated $\rho$ (spike 3). The runtime service's $\rho_\text{env}$ partition includes channels where admission-control is feasible (`$\rho_\text{traffic}$`) and channels where it is not (`$\rho_\text{infrastructure}$`). Spike 3 §3.3 names this *agent-internal-vs-boundary feasibility gap* as the cleanest interface.
- **Spike 1 ↔ Spike 5.** Sibling decomposition — runtime-tempo (sense/decide/actuate) is structurally parallel to developer-tempo (obs/explore/probe). Both use matrix-Loewner weakest-channel bottleneck. Cross-cite at segment landing.
- **Spike 4 ← Spike 5.** Unmaintainability bifurcation (spike 4) *consumes* spike 5's $\mathcal T_\text{dev}$. Spike 4 §8 names this; spike 5 §6.2 confirms. The bifurcation should adopt the per-channel form (matrix-Loewner weakest channel, not scalar).
- **Spike 2 Addition 6 ← Spike 5.** Conway's Law as GUC-class bound is *hypothesis-grade* in spike 2 pending spike 5's segment-landing — the per-developer $\Sigma_t$-over-architecture machinery is what spike 5 provides.
- **Spike 6 ← Spike 2.** Macro-hygiene as W₁ wrapping (spike 6 §5.2) maps onto `#der-class-coercion-via-wrapping`; spike 2 carries the refined wrapping construction the analogy lands against. Spike 6 is *structural analogy, not derivation* — landing it requires spike 2 first.
- **All wrapping-related spikes ← Spike 7.** Spike 7's resolution (no $W_{1.5}$; W axis is type-of-bound) carries forward. Spikes 2 and 6 reference this explicitly; spike 1 inherits it through the wrapping construction.

## Operational notes

- Each spike is lint-clean (`bin/lint-md`); LaTeX-not-Unicode math; one-logical-line paragraphs.
- The cycle was launched on top of the mining commit `a6774dc` (TST mining cycle of the same date); spike-cycle commit is `309f14b`; this consolidation commit is the third in the arc.
- The 7 spikes initially hit a global Anthropic API 529 overload at launch (zero tokens used, ~3.5 min internal retry exhaustion each); the cluster was relaunched after probing with spike 7 (smallest scope). The overload was substrate-level; recorded here for posterity rather than as load-bearing context.
- No segment or OUTLINE edits beyond the conservative naming of two existing `--GAP--` rows (in the mining cycle commit). Segment-landing decisions await Joseph's structural choices on placement (new Ch.5 vs Ch.4 extension; demonstration-appendix vs theorem-in-body for `#der-wrapper-persistence-condition`; etc.).

## Honesty calls preserved at the cluster level

Surfaced in [`TST-IDEAS.md`](../../TST-IDEAS.md) §9 to prevent loss at segment-landing — generative-citation risk for $\alpha \approx 0.31$ tech-debt-contagion (spike 4); Ebbinghaus $\tau \approx 20$ days transfer to code unvalidated; vanilla GenServers ≈ Tier-1 reflex not Tier-3 agent (spike 1); most current AI-augmented workflows are $W_2$ as built not $W_1$ (spike 2 Addition 5); admission-control is NOT universally net-positive (spike 3 sign-condition); G1 maintainability is NOT automatic (spike 4 §6); $\mathcal T_\text{obs}$ requires instrumentation chronicle alone does not provide (spike 5 §4.3); bursty failures need windowed form of wrapper-persistence inequality (spike 2 §3 flagged).
