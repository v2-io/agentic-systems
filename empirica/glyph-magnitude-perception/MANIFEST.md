# MANIFEST — glyph-magnitude-perception

*Entered 2026-08-25 (pilot day). Canonization contract per `empirica/README.md`.*

## What it studies

How language-model minds perceive **order among Unicode glyphs** — which glyph sequences carry monotonic magnitude perceptually, by what mechanisms, with what substrate-dependence — and, co-equally, **how measurement formats manufacture or suppress perceived order** (demand characteristics, answer-channel priors, articulation filters). The experimental object is dual: the glyph-order structure AND the measurement protocol itself.

## Claims

*Epistemic tier per FORMAT vocabulary; all currently PILOT-tier — single-day runs, pre-registration informal, no held-out confirmation yet.*

1. **[Empirical Claim (pilot)] Mechanism taxonomy of magnitude carriers.** Fill (height/width/density/fraction), count (immediate to the subitizing boundary ~3–4, decoded past it), size/angle, compiled-semantic decode, with denoted-number and ink-fill emerging as the two substrate-invariant axes in assumption-free discovery walks.
2. **[Empirical Claim (pilot)] Sequence-kind taxonomy.** Factorizable (pairwise = set-level), holistic (perceptible only with ≥~4 glyphs co-present; pairwise-blind AND salt-fragile), authored (a chosen linearization of a perceived partial order; per-reader stable, cross-reader divergent), and generator lattices ($B^4$/$B^6$/$B^8$, product grids) whose maximal chains are ladders.
3. **[Empirical Claim (pilot)] Demand characteristics, measured.** Forced-choice formats without a no-ordering option manufacture ~80% of cross-domain directed edges (426/533 dissolved when ⟂ was offered on identical pairs, Sonnet tier). Axis-naming requirements filter out confounded/unnamed aspects that motion-framed continuation recovers (⚌☱: 3/6 declines named vs 5/6 continuation unnamed).
4. **[Empirical Claim (pilot)] Local transitivity; capability buys discipline, not axes.** Within-judge triad cycle rate 1–2% (Sonnet) vs 37% (llama3.2:3b); ⟂ usage 52–57% vs 7%; yet the same two axes survive cross-consistency filtering at both tiers. Answer-channel effects dominate at small scale (3B: 2% bias-immune with ASCII </> answers vs 27% glyph-echo).
5. **[Empirical Claim (pilot)] Immediacy arbitrates axis conflicts.** Where ink and denoted value oppose, families with strong compiled decode resolve to value (Ⅸ>Ⅷ, 16-0), families without resolve to ink (☷>⚌, 16-0), weak-decode families split (‱>% 12-4). Five converging operationalizations of immediacy agree on one ranking.
6. **[Intended]** Confirmation-tier versions of 1–5 under frozen protocol v1.0 with fresh judges, fresh seeds, held-out glyph pools (see `pilot/DESIGN-scale-up.md`).

## Parameters / regime

Judges: Claude Sonnet (workflow subagents, temp default) and llama3.2:3b via ollama (temp 0/0.7, stateless per item). Pools: BMP + SMP symbol blocks, mixture sampling (structured neighborhoods + pane-local + uniform long tail). Units: counterbalanced pairs → triads with reverse cycles split across judges → whole-set gestalt reconstruction → generative continuation/extension → salted membership validation. Full instrument definitions: `pilot/DESIGN-scale-up.md` (protocol v0.9); v1.0 freeze is the next milestone.

## Consumers

None yet. Candidate landing sites: 03-llm-core (perception/representation segments); the demand-characteristics result may also inform multi-agent measurement methodology (doc/sop/multi-agent.sop.md practices).

## Provenance

Pilot session 2026-08-25 (Joseph + Fable), originating brief now at `data/surveys-v1/prompts/instr2-founding-brief.md`; the pilot's working substrate (scripts, task/key JSONs, run outputs) migrated to `harness/pilot-scripts/` + `data/judgments-v0/`; full experimental narrative at `pilot/pilot-record.md` (append-only original). All six de-novo surveys (Grok pilot, Sonnet-5 interactive, Fable, 4× workflow Sonnet) at `data/surveys-v1/` — the original `~/src/arch/{instr2.md,grok-instinctive-sequences.md,msc/*}` locations were deleted after migration (2026-08-25 evening). Shared pane tool now at `harness/tools/unicode-group`.

## Vivarium

planned (protocol maps cleanly to in-vivia judge panels).

## Provenance honesty note

Pilot Sonnet runs (Workflow batteries) recorded prompts-in-scripts and run IDs but NOT per-call temperature/model-version pins or RNG-seeded shuffles in a ledger; ollama runs recorded seeds and temp but predate the ledger. Pilot claims are therefore reproducible-in-kind, not bit-reproducible. The harness (harness/) exists to close exactly this gap before any confirmation run; per the charter, nothing above is "confirmed" until a recorded harness run exists in RUNS.md.
