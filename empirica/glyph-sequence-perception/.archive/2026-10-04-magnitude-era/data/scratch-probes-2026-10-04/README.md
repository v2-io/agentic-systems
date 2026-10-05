# Scratch probes of 2026-10-04 (magnitude era, stopped)

These two probes were run in a session-scratch copy of the v1.0 clean room. They are moved here so the record is complete. Both used the archived v1.0 runner (`../../harness/runner/`) with two extra entries in its stimulus table, `"ones"` and `"dress"`.

- **`ones-*`** — designed and launched by the coordinating session; not part of the method. It was the coordinator's own design, and the coordinator stopped it when Joseph's direction changed. Its stimuli: the 18 "dresses" of the digit one (`1 ¹ ₁ ① ⑴ ⒈ ❶ ➀ ➊ ⓵ １ 🄂 🯱 𝟏 𝟙 𝟣 𝟭 𝟷`), every pair in both orders, ⟂/≈ available, plus the whole set shuffled three times. Judges: opus55, sonnet55, haiku45 (partial), grok46, gemini31pro (partial), gemini38flash, llama32-3b, qwen25-3b. Read by `../../design/2026-10-04-plan/scripts/ones_probe.py`. Its findings are summarized in `../../design/2026-10-04-plan/04-joseph-questions.md`, at anecdote tier.
- **`dress-*`** — designed by the design agent (Claude Opus 5.5) as a follow-up: the same 18 dresses at values 4 and 8, plus 4-vs-5 across dresses. It was stopped within minutes when Joseph clarified that the study's own discovery loop was wanted. It holds only a few dozen calls per judge, and nothing used it. The stimulus builder is `../../design/2026-10-04-plan/scripts/dress_stimuli.py`.

The question both probe — the digit dresses — now enters the live study as a lattice seed: `../../../../data/seeds/digit-dresses.jsonl`.
