# surveys-v1 — de-novo introspective surveys (pilot day, 2026-08-25)

Independent first-instinct surveys per the founding brief (`~/src/arch/instr2.md`): each surveyor swept Unicode panes and recorded glyph sequences with a perceived monotonic magnitude ordering, append-only, deliberately NOT reading other surveyors' output or the repo's prior unicode work (confounder discipline is part of the design — each file is one mind's unprimed perception).

| File | Surveyor | Provenance |
|---|---|---|
| fable-1.md | Fable (main session) | The pilot's full experimental record — survey PLUS all subsequent instruments/results interleaved; the pure-survey portion is roughly the sections before "ROUND 2" plus round 2's pane walk. Copied from `~/src/arch/msc/fable-magnitude-survey/sequences.md`. |
| sonnet-survey-{1..4}.md | 4× Claude Sonnet (workflow `magnitude-survey-sonnet`, wf_428f0aea, launched 15:29) | Fresh agents given instr2.md verbatim + own scratch dir + do-not-read-others instruction. Copied from `~/src/arch/msc/sonnet-survey-N/sequences.md`. |

Not yet included:
- `~/src/arch/msc/unicode-magnitude-8f3c/` — a separate surveyor (launched by Joseph, distinct from the four above; still in progress as of this snapshot, 17:42 activity). Pull its record in when it completes.
- Any surveys by other agents Joseph has collected outside this tree (he has quoted sequences from other surveyors — braille bit-fills, arrow weight ramps, /⫽⫻ — whose source files are not in this repo yet).

Snapshot copies, not live: originals remain at their msc/ paths. Naming lesson from the pilot (two uncoordinated launch tracks surprised each other in msc/): future survey dirs should carry launcher+date in the name, e.g. `survey-<model>-<launcher>-<date>-<n>/`.

Cross-survey convergence analysis: not yet done systematically (pilot noted instant convergence on circled numbers, the ▁-ramp, and circle-fill, and complementary finds like `◌○◔◑◕●` and the braille lattice variants). A proper concordance pass — sequence-level intersection/union, mechanism-family coverage per surveyor — is a v1 analysis task for the harness.

## prompts/

- `instr2-founding-brief.md` — Joseph's founding survey brief (verbatim copy of `~/src/arch/instr2.md`), the prompt behind fable-1 and (via pointer) all sonnet surveys.
- `sonnet-surveyor-brief.md` — the peer brief given to sonnet-survey-{1..4} (verbatim template from the launching workflow script); it points each agent at instr2.md as the primary and adds the immediacy distinction + confounder discipline.

## All surveys now landed (evening close-out, 2026-08-25)

| File | Surveyor | Notes |
|---|---|---|
| grok-1.md | Grok (Joseph-interactive) | THE PILOT SURVEYOR — instr2.md was based on a modified version of Joseph's discussion with him. Own taxonomy in section headers. |
| sonnet5-1.md | Sonnet 5 (Joseph-interactive) | The full-coverage survey (926 lines, ~240 group headers); received repeated don't-assume steering. |
| fable-1.md | Fable (main session) | Includes all pilot instruments/results, not just the survey. |
| sonnet-survey-{1..4}.md | 4× Sonnet (workflow) | One-shot briefs, no steering. |

Both interactive surveys are POLLUTED by design (Joseph steered mid-flight, sharpening the question itself — e.g. the density/morphings/unarticulated-axes challenge). Per Joseph: surveys are SEEDS for the stochastic walks (loci, centers of gravity for initial resources), never confirmatory data. See SCHEMA-draft.md for the structured-extraction plan.

Originals' former homes (~/src/arch/instr2.md, grok-instinctive-sequences.md, msc/unicode-magnitude-8f3c/, msc/sonnet-survey-*/, msc/fable-magnitude-survey/) were deleted after migration 2026-08-25 evening; this directory is now the canonical home. The `unicode-group` pane tool moved to ../../harness/tools/ (long-run principled home would be arch/firmatum/utils/utf/ once that area is tidied — noted so it isn't lost).
