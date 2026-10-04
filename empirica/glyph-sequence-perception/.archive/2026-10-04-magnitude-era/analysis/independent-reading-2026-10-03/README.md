# reading/ — an independent reading of the glyph-magnitude-perception v1.0 data

Written 2026-10-03 by a Claude Opus 5.5 instance working only from this clean room. I did not see the original builder's analysis or the study repo. I read the zoetica source of the SIGNA notation, date-bounded memorata searches for its provenance (queries listed in `01-signa.md`), and the Ghostty ink table under `firmatum/utils/utf/`, which the protocol itself references.

| file | what |
|---|---|
| `LETTER.md` | a plain letter to Joseph, written last by re-reading the files below |
| `01-signa.md` | Joseph's question: the old signa sequence as a control |
| `02-registered-predictions.md` | P1–P15 re-derived, with verdicts and what they mean for the MANIFEST claims |
| `03-instruments.md` | what the instruments can and cannot tell apart, with evidence |
| `04-new-data.md` | what data would change what can be said, and why |
| `verification/VERIFICATION.md` | an independent adversarial pass on this reading (fresh agent, bare brief, own loader), with its scripts. I integrated its corrections into 01–04. Where they changed a claim, the old claim was removed, not kept softened. Its report is unedited, so it still describes the pre-correction text |
| `tables/` | every number cited, as produced by the scripts |
| `scripts/` | the analysis code. `python3 scripts/<name>.py` from this directory. Each script's docstring states its definitions |

**Parsing.** Every script uses the builder's parser p1.3 from `harness/runner/instruments.py` unchanged, so parse decisions are the builder's. Pairing, scoring, statistics and every definition choice are mine. Where a registered definition was ambiguous, the script's docstring and `02-registered-predictions.md` say which reading I used.

**Excluded.** qwen3-4b (invalid), `*-shakedown`, the grok tool-leak run. gpt-oss-20b has no ledgers in this copy. The pilot-condition arm is analyzed separately (`scripts/pilotcond.py`).
