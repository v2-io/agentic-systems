# Clean room — glyph-magnitude-perception, v1.0 data (assembled 2026-10-03)

This directory is a copy of the study's raw materials, made for a reader who has not seen any interpretation of the v1.0 data. It is not a git repository. The study's home is `~/src/arch/asf/empirica/glyph-magnitude-perception/`.

**What this copy leaves out.** It contains no interpretation of the v1.0 results. The original builder's results, analysis code, reports, write-ups, and the audits of them are all omitted. That is deliberate: you are being asked to read these data yourself. Files that were trimmed say so in a header comment, together with the sha256 of the full file.

## What is here

| path | what |
|---|---|
| `EMPIRICA-CHARTER.md` | the registry's charter: how experiments, MANIFESTs and RUNS work |
| `MANIFEST-pilot-2026-08-25.md` | the experiment's MANIFEST as it stood after the pilot. These are the pilot claims v1.0 was built to test. |
| `RUNS-pilot.md` | the pilot-era run log |
| `pilot/` | the pilot narrative (`pilot-record.md`), the scale-up design with Joseph's design-review addenda (`DESIGN-scale-up.md`), and the pilot's llama3.2:3b results |
| `data/judgments-v0/` | the pilot's raw judge outputs, plus the key files needed to decode them (see its README; decoders in `harness/pilot-scripts/`) |
| `data/surveys-v1/` | the seven de-novo surveys, their pass-1 extractions, the schema, and the reconciliation queue. The queue records Joseph's rulings from 2026-08-25. |
| `rulings/` | a memory note recording Joseph's 2026-08-25 ruling on articulation, categories and the feature-correlate program |
| `protocol/PROTOCOL-v1.0.md` | the frozen v1.0 protocol: prompts, instruments, definitions. It also has the post-freeze implementation notes on parser versions, adapter fixes, invalid data and quota losses. |
| `PREDICTIONS-v1.0-registered.md` | the registered predictions, verbatim (excerpt; see its header) |
| `harness/runner/` | the executable protocol. Covers fated randomness (`fate.py`), prompts and parser (`instruments.py`, parser p1.3), judge adapters and registry (`judges.py`, `judges-v1.json`), the runner (`run.py`), the stimulus builder (`stimuli.py`), the conflict and holistic item definitions, and the campaign scripts. |
| `harness/top40/candidates.py` | the selection rule for the top-40 battery (requested by Joseph) |
| `data/stimuli-v1/` | every stimulus file, with presentation ids (`pid`) |
| `data/runs-v1/<run>/` | one directory per run: `spec.json`, plus `ledger.jsonl` with one row per judge call |

## Facts you would otherwise have to rediscover

- **Ledger semantics.**
  - Each row is one call. It holds `pids`, `items` (a sheet's id→pid map), `prompt` (verbatim), `result.raw` (the verbatim answer), `result.error`, `result.usage` (including thinking tokens where reported), `model_reported` and `ts`.
  - Failed calls stay in the ledger: empty raw, an error, or a non-null `sheet_incomplete`. Resumed runs re-asked them, so a presentation can appear in more than one row.
  - `rep` distinguishes deliberate repetitions (the conflict battery ran 3 reps for API judges).
  - Parsing was never written to the ledger. `instruments.py` has the builder's parser; you are free to write your own.
- **Data that is not what its directory suggests.**
  - `*-qwen3-4b`: invalid. Every call returns truncated reasoning ("First, the user is asking…") and never an answer.
  - `*-shakedown`: adapter debugging before registration.
  - `triads-perp-sheet-grok46-aborted-toolleak`: grok had tool access in that run.
- **Missing data that is not judge behaviour.**
  - gpt-5.6-terra (via Codex) hit an account usage limit mid-campaign. Its format/tie run is partial and its format/perp run empty.
  - The Gemini CLI (agy) hit an account quota at the very end, so a few gemini-3.8-flash top-40 calls failed.
  - grok sometimes restarted or truncated its JSON mid-sheet.
  - phi-4-mini often answers at length.
- **Judge conditions were not equalized.**
  - Context residue per adapter is in `judges-v1.json`.
  - "Effort low" was set where possible, but thinking-token use differs widely across models (see `result.usage`).
  - Sheet mode (40 items per call) and single mode are recorded per run. claude-sonnet-5-5 ran both.
- **The pilot-condition arm** (`format-*-pilotcond-sonnetagent`) was claude-sonnet-5-5 run as Claude Code subagents with the pilot's wording and 80-item sheet files. Those subagents load the user's global instruction context and run at default effort. Their transcripts are not included, because they contain that private context; prompts and answers are in the ledger.
- **Stimulus lineage.** "Builder" means the agent that built and ran v1.0.

  | class | how the content was decided | sets |
  |---|---|---|
  | A | fixed by a sampling rule or taken from the pilot | `pool.json`, `triads`, `format-pairs`, `pilotcond`, the dice / ramp / unfold / risebar / rotate4 / drain / noise parts of `holistic-pairs` and `gestalt`, all `top40*` |
  | B | hand-picked by the builder | `conflict`, and the held-out candidate sets in `holistic-pairs` and `gestalt` |
  | C | a glyph sequence supplied from outside the study: a human-authored ladder from another project | `consumer-signa-*` (run label `signa`) |

  Fields like `annot`, `predict` and `intended` in stimulus files are designer hypotheses or authors' written orders, not ground truth.
- **Seed coverage.** The stimulus builder read survey records by the field `type`. Three extractions (grok-1, sonnet-survey-3, sonnet-survey-4) use `record_type`, so the seed stratum covers only fable-1, sonnet5-1 and sonnet-survey-1/2.
- **Pilot leakage.** A few pilot salt glyphs leaked into the v1.0 seed stratum; details are in PROTOCOL's notes.
- **The pilot's judges** were Claude Code workflow subagents using the model alias "sonnet". The exact model version on 2026-08-25 is unrecorded.
- **Registration timing.** PREDICTIONS was committed at 2026-10-03T20:11:37Z, and the first non-shakedown ledger row is at 20:11:59Z.
