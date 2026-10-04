# Archive — the magnitude era (2026-08-25 pilot data through 2026-10-04)

Archived 2026-10-04 at Joseph's request:

> *"Archive all of the garbage data, please, in a .archive within the glyph project. It's become untenable, IMO, to keep trying to massage something that was wrong from the beginning."*

In the same exchange he also set the new direction:

> *"Magnitude is no longer a 'critical' factor — neither is which way is 'up' — just sequencing."*

Everything here asked LLMs which glyph conveys *more*, or scored them against a direction. The study's current direction is set out in `../../PLAN.md`.

Nothing here is deleted. Paths inside these files refer to their pre-archive locations, relative to the study root; add `.archive/2026-10-04-magnitude-era/` to resolve them.

| path | what it was |
|---|---|
| `data/judgments-v0/`, `pilot/results*.jsonl`, `harness/pilot-scripts/` | The 2026-08-25 pilot judgments (magnitude-framed) and their decoders. The pilot's *method record* stays live at `../../pilot/pilot-record.md` and `../../pilot/DESIGN-scale-up.md`. |
| `data/runs-v1/`, `data/stimuli-v1/`, `harness/runner/`, `protocol/`, `PREDICTIONS-v1.0.md`, `debrief.md` | The 2026-10-03 v1.0 campaign: a confirmation track that the study's discovery loop was never meant to be. |
| `harness/top40/`, `harness/reanalysis/`, `harness/correlates/`, `analysis/` | v1.0 analyses: findings, audits, the clean-room reading, the top-40 battery, the derived views, embedding probes. |
| `MANIFEST-2026-10-03.md`, `RUNS-2026-10-03.md` | The study's MANIFEST and RUNS as they stood, with claims that rest on the data above. |
| `design/2026-10-04-plan/` | A design agent's 2026-10-04 opinion and plan, written in stages around the material above, plus two scratch-analysis scripts. Superseded by `../../PLAN.md`. |
| `data/walk-r1-stopped/`, `harness/walk-r1-stopped/` | A magnitude-framed re-run of the pilot walk, started and stopped on 2026-10-04 (~140 sheets) when the direction changed. `harness/walk-r1-stopped/METHOD.md` is the extraction of the 08-25 method from primary sources, and `../../PLAN.md` draws on it. |

**Reusable tools in here.** `harness/runner/judges.py` holds the isolated judge adapters (claude, grok, agy/Gemini, ollama, llama.cpp), and `harness/runner/fate.py` the fated-seed functions. The new harness copies them rather than importing from the archive.

**Kept live,** because none of it is garbage:

- `data/surveys-v1/`: the seed surveys and Joseph's recorded rulings;
- `harness/ingest/`: the Postgres 18 index;
- `harness/tools/unicode-group`;
- the two pilot method documents.
