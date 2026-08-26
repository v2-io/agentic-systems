# judgments-v0 — pilot-day raw judgment data (2026-08-25)

Rescued from session-ephemeral storage; provenance-grade [partial] (see ../../RUNS.md).

- w*.json — workflow task outputs (full judge answers, one file per battery/walk; run-id ↔ instrument mapping is in RUNS.md).
- *-chunk-*.json / *-key-*.json / *-tasks.json / walk5-triads.json / walk-pool.json / conflict-*, morph-*, gestalt-*, salt-base, continue-tasks, battery* — the stimulus sheets and answer keys REQUIRED to decode the workflow outputs (chunk answers are meaningless without their key files).
- probe*-llama3.2-3b.log + ../pilot/results*.jsonl — ollama runs ([full] provenance).
- sonnet-judge2-answers.json, results5-as-walk.json — derived intermediates.

Decoding scripts (snapshot): ../../harness/pilot-scripts/*.py (analyze/triads/discover expect to run from a dir containing the key files).
