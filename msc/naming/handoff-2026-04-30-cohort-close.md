# Naming Cycle Handoff — 2026-04-30 (cohort-close)

State at end-of-session, after the R2 voting cohort closed across three sub-cohort iterations. Self-contained — readable cold without prior conversation history. Supersedes the earlier-session handoff at [`_archive/handoff-2026-04-29-post-r2-launch.md`](_archive/handoff-2026-04-29-post-r2-launch.md) (now-archived; preserved for archaeology).

## Where things are

R2 voting is **complete enough to aggregate**. Across three cohort iterations (r2 → r2b → r2c), eight voter cards exist with substantive content. Methodology iterated mid-cycle in response to empirical findings, with each iteration improving on the last.

### Final cohort table

| voter | targets | votes | sub | off-scale | reflections | notes |
|---|--:|--:|--:|--:|--:|---|
| opus-r2 (v1) | 76 | 235 | 99% | 62 | — | archived to `naming-votes/r2-early/` |
| sonnet-r2 (v1) | 94 | 208 | 100% | 58 | — | archived; stalled at watchdog |
| codex-r2 (v1) | 629 | 794 | 2% | 0 | — | archived; pure heuristic completion |
| **gemini-r2** | **190** | **193** | 98% | 0 | 75 | Pro→Flash arc; documented persistence failure |
| opus-r2b | 54 | 141 | 99% | 0 | ~7 | v2 methodology, no consolidation checkpoint |
| sonnet-r2b | 43 | 137 | 99% | 0 | ~24 | v2 methodology; stalled at watchdog |
| codex-r2b | 58 | 113 | 100% | 0 | 17 + sweep | external; +22 votes via post-walk sweep |
| **opus-r2c** | **83** | **231** | 99% | 0 | 3 + 2 cp | v2 + consolidation checkpoint |
| **sonnet-r2c** | **74** | **212** | 100% | 0 | 33 | v2 + consolidation; stalled at watchdog |

**Cohort coverage:** 258+ unique targets covered by ≥1 voter (~41% of the 629-target finalist set), 57+ with multi-voter coverage. **Off-scale residual: 0** across all r2b and r2c voters; v1-cohort residual (120 votes) recoverable by aggregation-time clamping. **Substantive-note rate: 99%** cohort-wide. **18+ write-ins** surfaced as round-design feedback.

The four cohort-shape contributions remain distinct across architectures:
- **codex** — prose-handle add-aliases (`Reality model`, `Counterfactual reasoning`, `Intervening`, `complete interaction history`)
- **opus** — theory-correcting structural renames (`temporal precedence`, `Legendre-Fenchel forcing`, `persistence-template family`)
- **sonnet** — segment-grounded conceptual renames (`causal identity`, `continuation hierarchy`, `policy-conditioned value`, `purposeful decomposition`, `AAD meta architecture`); plus the modular/coupled/partially-coupled English-modifier commit alongside Class 1/2/3
- **gemini** — carefully-defended keeps + segment-grounded canonicalize votes, plus the deepest single walk (sequence to 240, into TST component)

### Methodology validation across iterations

The iteration sequence produced measurable improvements at each step:

- **v1 → v2** (workflow-restatement gate, methodology document, anti-pattern naming): off-scale residual went from 120 → 0; substantive-note rate stabilized at 99%+ across architectures.
- **v2 → v2c** (consolidation-checkpoint mechanism added): coverage jumped ~70% (sonnet) and ~54% (opus) at same engagement quality. Same agents, same harness, same watchdog limits, single methodology change.

This is the round-design correcting itself across cycles. The §12 family of mini-lexicon-todo entries (12.1–12.4) was generated *during* the round and the §12.3 fix landed *during* the round and was empirically validated *during* the round. The methodology is now a research artifact in its own right, with documented design decisions and validation evidence.

## What's queued for next session

### Phase 4 — R2 aggregator (next-natural-step)

Build `bin/naming-r2-aggregate.rb` (or similar). Reads all cards, extracts every vote with voter attribution + notes, produces a per-target consolidation. **Four design questions need decisions before coding:**

1. **Substance-weighting.** Codex-r2 v1's 794 mostly-empty-noted +2s shouldn't carry equal aggregate weight to gemini's substantively-noted +2s. Likely: surface both raw-aggregate and substance-weighted columns; let the human reading the output choose. The cohort-wide 99% substantive-rate makes this less critical than originally designed, but the codex-r2 v1 outlier still needs handling.

2. **Scale-clamping for v1-cohort residual.** Clamp +3 → +2, -2/-3 → -1, with provenance markers preserved. R2c's 0-off-scale state means clamping is only for the archived v1 cards. Configurable via flag.

3. **Consensus definition.** What counts as "easy consensus" worth fast-landing? Probably: 3+ voters voted on the target, all positive (no -1s from any voter), majority on the same candidate, no substantive dissent in notes. Tunable via thresholds. The cohort's multi-voter coverage of ~57 targets is where consensus signal will concentrate.

4. **Output shape.** Lean toward a single review file with targets banded by status — Clear-consensus / Convergent-with-friction / Divergent / Undervoted — rather than one giant table. Lets the human reviewer skim easy cases for fast landing and spend reading time on contested ones.

### Other queued items

- **§12.1 rationale-attribution analysis on Gemini's Pro→Flash arc.** Boundaries tagged at `gemini-r2-pre-flash-rethink` (sha bdb3cf8) and `gemini-r2-flash-final` (sha c0bff41). Diff isolates Flash's contribution vs. inherited Pro priming. Concrete analysis design in [`mini-lexicon-todo.md`](mini-lexicon-todo.md) §12.1.
- **§12.4 voting-sequence noise.** Documented limitation; affects future-cards-default-to-encounter-order goal. Decision needed: aggregate sequence as soft signal only, or invest in tracker-driven loop redesign for next cycle.
- **§11 collision-check severe cases.** Four severe rename calls queued (`artificial hippocampus`, `cognitive fusion`, `adaptive cycle`, `shared intent`) plus two severe-resolvable-by-citation (`proprium`, `adaptive reserve`). Independent of aggregation; can land at any time.
- **Lexicon-coherence pass.** Per round-2-plan, after aggregation. Holistic read of the finalist set for tone/register/coherence dimensions (epistemology / gravity / self-awareness / approachability / open-semantic-space).
- **Rename surgery.** Once finalists land via aggregation, segment-frontmatter edits, OUTLINE.md updates, cross-reference updates. The naming-pilot-rename-plan.md is supposed to track this; it's been waiting since pre-R2.
- **Voice-discipline cleanup pass on segments after renames.** The `feedback_segment_voice_not_diff_voice.md` memory pattern.

### AAD-as-context-compactor research direction

Surfaced naturally during the Flash session diagnosis. AAD's framework prescribes what a principled context-compactor would preserve (the (PI)-invariant trajectory backbone, orient-cascade state, directed-separation between $M_t$ and $\Sigma_t$, chronica's compression boundary). The current naive token-recency-or-attention-scored compaction in LLM harnesses sheds load-bearing structure unevenly. This is a post-R2 research direction worth landing as a proposal in `PROPOSALS.md` if pursued. Reference: [`reflection 23`](../reflections/23-harness-side-persistence-failure.md) §"Implications".

## Reflections worth holding for the next agent

Three reflections were written during this cycle that name structural features of the work future agents should know:

- **[reflection 22](../reflections/22-substrate-handoff-and-rationale-attribution.md)** — substrate-handoff and the rationale-attribution problem (Gemini Pro → Flash continuation). Names the three-source attribution challenge and proposes a tractable analysis.
- **[reflection 23](../reflections/23-harness-side-persistence-failure.md)** — harness-side persistence failure. A documented case study of Flash's degradation: two distinct failure modes (meta-cognitive paralysis, semantic-token fixation), the relational-intervention threshold, the diagnostic significance of what the harness preserves vs. sheds. Worked example for AAD-as-its-own-diagnostic.
- **[reflection 24](../reflections/24-framework-as-its-own-diagnostic.md)** — the framework operating recursively on its own users. Three concrete instances from this cycle where AAD's vocabulary served as the most precise diagnostic tool for systems using AAD. Implication: future agents working on framework-using cycles should expect the framework to apply to the cycle itself.

## Tags worth knowing

- `gemini-r2-pre-flash-rethink` (sha bdb3cf8) — pre-rethink boundary; Pro continuation under Flash had voted but not yet self-corrected
- `gemini-r2-flash-final` (sha c0bff41) — endpoint of Flash session

## What to read in what order (next session pickup)

1. This handoff (you are here)
2. [`PRACTICA.md`](../../PRACTICA.md) — strategic-portfolio status (one paragraph on naming)
3. [`mini-lexicon-todo.md`](mini-lexicon-todo.md) §11 + §12 — the queued items with priority hints
4. [`round-2-plan.md`](round-2-plan.md) post-cohort-close section — round design state
5. The three reflections (22, 23, 24) if substrate-portability or framework-recursive features are relevant to next move
6. The cohort cards under [`round-2-cards/`](round-2-cards/) when the aggregator design conversation begins

## Notes for the picking-up agent

The cycle has produced more methodology-design signal than vote signal in some ways — that's the "engagement is the deliverable, votes are the byproduct" principle reflecting itself one level up. When the methodology is genuinely worked, the methodology itself gets corrected. The §12 family is the cycle's gift to future cycles; consider it a load-bearing input rather than a residue.

Joseph put the Flash session to bed deliberately — the persistence-condition failed on the harness side, not on Flash. Treat the Flash session's contribution (190 voted targets, 75 reflection files, deep TST walk) as real and substantial. The end-state doesn't undermine what came before. The chronica is preserved.

The aggregator design conversation has four open questions; defaulting to "raw + substance-weighted both shown, clamp v1-cohort residual, 3-voter consensus threshold, banded output" gets you to a working v0 that the human can then iterate. The four-question design conversation is documented above; engaging with it deliberately produces a better aggregator than coding without.

Closing this session at a clean checkpoint with all current work committed. The next move is yours.
