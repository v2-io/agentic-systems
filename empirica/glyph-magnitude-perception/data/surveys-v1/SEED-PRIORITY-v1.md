# SEED-PRIORITY v1 — the sanctioned super-simplified strength scalar

*The one pre-approved pass-2 normalization (Joseph, 2026-08-25): a conservative per-file squash of felt strength into `seed_priority ∈ {high, medium, low}`, used ONLY for initial sampling triage. It is discarded the moment a seed has harness measurements; it never appears in any analysis; anything finer is gated by the tabled unification item in RECONCILIATION-QUEUE.md.*

Derivation rule (versioned; a classifier over pass-1 verbatim fields, replayable):

- `high`: surveyor's own top register — "very high"/"very strong"/5, unhedged.
- `medium`: mid registers ("strong", "high" with hedges, "medium-strong", "medium", 3–4).
- `low`: everything else — "low", "weak", 1–2, `marked_speculative`, `unstated`, negatives/questions (which seed the ⟂-control and battery pools, not the ladder pool).
- Conservative tie-break: hedged or mixed language squashes DOWN. Survey-4's numeric scale (self-defined predicted recoverability) maps 5→high, 3–4→medium, 1–2→low — acceptable at this coarseness precisely because the scalar carries no register claim.
- Per-surveyor calibration keys (sonnet5-1 L1364-66, fable-1 retro-calibration) apply only as DOWN-weights at this granularity (e.g. fable-1 pre-split "very strong" on denoted families: still high; fable-1 discards: low regardless of wording; sonnet5-1 convention-only-zero-visual finds: cap at medium).

Implementation is a harness-era script over extracted/*.jsonl emitting `derived/seed-priority-v1.jsonl` (record id → priority + rule-version); not hand-authored.
