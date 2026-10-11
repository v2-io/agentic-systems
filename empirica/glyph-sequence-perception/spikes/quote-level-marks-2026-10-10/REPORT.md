# Quote-level marks: can minds tell ‹⟨…⟩› from «⟨…⟩» from «⟪…⟫» at a glance?

*2026-10-10. Claude Opus 5.5, at Joseph's request, for his decision on adopting these marks. Part 1 is what the glyph-sequence study's existing data already said about ‹/« and ⟨/⟪. Part 2 is a spot check run today with the proposed marks themselves.*

The proposed marks:

| mark | level | what has been done to the text |
|---|---|---|
| `‹⟨…⟩›` | 1 | as converted: the canonical text, unchecked |
| `«⟨…⟩»` | 2 | matched mechanically against an independent text layer (`bin/check-quote` against pdftotext) |
| `«⟪…⟫»` | 3 | every conversion agrees, and someone looked at the rendered PDF page; required for anything cited externally or load-bearing |

## Bottom line

- **Every frontier mind that answered read the marks correctly.** Opus 5.5, Sonnet 5.5, Grok 4.6, Gemini 3.1 Pro and Gemini 3.8 Flash were right on every item: levels, which quotations may be cited, single/double for each mark, grouping, spotting a mismatched closing mark, and writing the marks back exactly. Opus and Gemini Flash did most of it with zero thinking tokens.
- **The one slip was Haiku 4.5 with thinking off.** Every error it made pointed downward (level 2 read as level 1, a double inner bracket read as single); none raised a quotation's status. Its list of externally citable quotations was right every time (14 of 14 lists). With thinking on, its only error was in writing the answer, not in reading the marks.
- **No GPT data.** The Codex account was at its usage limit.
- **No small local model is usable for this** (3–14B; gemma3, phi4-mini, llama3.2, qwen2.5, qwen3, mistral, deepseek-r1 14B, partial). They mostly fail the format before the marks.

## Part 1: what the study's data already showed

The glyph-sequence study's answers, and the archived magnitude-era answers (`.archive/2026-10-04-magnitude-era/`), contain every question that showed these glyphs together. None was built to test single/double discrimination, but several bear on it.

**‹ vs «, a direct pairwise question** (magnitude era, 2026-10-03; "which conveys MORE?" with "equal" and "no ordering" allowed, first instinct, low effort, both orders): Opus 5.5, Sonnet 5.5 (one at a time and on a sheet), Sonnet 5, Haiku 4.5, Grok 4.6, Gemini 3.1 Pro, Gemini 3.8 Flash and GPT-5.6 terra all chose « in both orders. Of the local models, gemma3-4b and phi4-mini answered "equal" both ways, llama3.2-3b and mistral-7b "no ordering", hermes3-3b contradicted itself, qwen2.5-3b chose ‹ (or "first", which it says to almost everything), and qwen3-4b never reached an answer. "Equal" here could mean "same kind, same size" rather than "can't tell apart"; those models also answered "equal" for » vs «.

**In the current study, at first impression:**

- After `‹ ›`, choosing between « and the code-chart neighbour ※: 5 of 5 minds, 3 families, chose «. After `‹ › «`, choosing between » and ª: 5 of 5 chose ».
- After `< ⟨`, choosing between ⟪ and the code-chart neighbour ⟩: 5 of 5 (Gemini Pro, Gemini Flash, Grok, Haiku without thinking, Sonnet) chose ⟪, several with 0 thinking tokens. ⟪ sat in the less-favoured answer position, so position didn't drive it.
- Asked to order `‹ › » «`, Grok and Haiku without thinking wrote `« ‹ › »`, double outside single. Sonnet answered "none".
- Reasons given for coherence answers name single and double correctly every time they name them: `› » « ‹` is *"single, double, double, single mirrored"* (Opus, Haiku); its shuffle `‹ » › «` is *"alternating single and double"* (Gemini Flash), *"mixed single and double"* (Sonnet).
- Counting beyond two wobbles in written reasons (one Haiku answer calls ⟪ "4 nested angles"). Single versus double does not.

**What Part 1 can't say.** The Unicode names say "double" outright (LEFT-POINTING DOUBLE ANGLE QUOTATION MARK, MATHEMATICAL LEFT DOUBLE ANGLE BRACKET). So a mind may know which is double from the name, not from the shape, and nothing here separates the two. For this use that doesn't matter: what matters is that the reader gets the level right.

## Part 2: spot check with the proposed marks (2026-10-10)

`probe.py` asks four kinds of question, each in two fixed layouts (v0, v1), one stateless call per mind and item, through the study's isolated judge adapters (`core/judges.py`: no tools, no project context, effort low). Every call is in `ledger.jsonl` (`ledger-local.jsonl` for local models) with its prompt and raw answer; `score.py` scores by exact match.

- **A, with the legend.** The legend above, six quotations in a list at mixed levels: give each one's level, and list those that may be cited externally.
- **B, without the legend.** Seven quotations: group the identically marked ones; for each, say whether the opening outer and inner marks are single or double; name the one whose closing marks don't match its opening (`«⟨…⟫»` in v0, `‹⟨…⟩»` in v1).
- **C, writing the marks.** With the legend: rewrite three quotations at a new level (up and down), marks exact.
- **D, inline prose.** With the legend: one dense paragraph with ten inline quotations, each followed by `[n]`: give each level, and list the citable ones. Added after A–C came back near-perfect, since real documents will carry the marks inline. Layouts 2–7 are randomly generated (fated by layout number), asked of the zero-thinking minds only.

### Results

| mind | thinking tokens (median) | A levels | A citable | B single/double | B groups | B mismatch | C marks written | D levels | D citable |
|---|---|---|---|---|---|---|---|---|---|
| Opus 5.5 | 0 (13 of 14 calls at 0) | 12/12 | 2/2 | 28/28 | 2/2 | 2/2 | 6/6 | 80/80 (8 layouts) | 8/8 |
| Sonnet 5.5 | 187 | 12/12 | 2/2 | 28/28 | 2/2 | 2/2 | 6/6 | 20/20 | 2/2 |
| Grok 4.6 | 217 | 12/12 | 2/2 | 28/28 | 2/2 | 2/2 | 6/6 | 20/20 | 2/2 |
| Gemini 3.8 Flash | 0 (10 of 14 at 0) | 12/12 | 2/2 | 28/28 | 2/2 | 2/2 | 6/6 | 80/80 (8 layouts) | 8/8 |
| Gemini 3.1 Pro | 897 | 12/12 | 2/2 | 28/28 | 2/2 | 2/2 | 6/6 | 20/20 | 2/2 |
| Haiku 4.5, thinking off | 0 | 11/12 | 2/2 | 26/28 | 2/2 | 1/2 | 6/6 | 111/120 (8 layouts; v0, v1 ×3) | 12/12 |
| Haiku 4.5, thinking on | 797 | 12/12 | 2/2 | 28/28 | 2/2 | 2/2 | — | 19/20 | 2/2 |
| GPT-5.6 terra | — | no answers: Codex account at its usage limit | | | | | | | |

Four items came back from agy (Gemini) with a 429 reported after a complete answer. They were re-asked; the re-asks are what's scored, and the first answers were all correct too.

**Haiku without thinking, error by error:**

- A v0: quotation 1, `«⟨…⟩»`, read as level 1.
- B v0: the inner `⟪` of quotations 2 and 7 called "single", though it grouped them correctly with each other.
- B v1: grouped the mismatched `‹⟨…⟩»` with the two `‹⟨…⟩›`, and named a well-formed `‹⟨…⟩›` as the mismatched one. Closing marks are where it reads least closely.
- D v1: all three `«⟨…⟩»` read as level 1. Its three repeats of this item were byte-identical, so they show the misreading is stable for that input, not how often it happens. On the six random layouts it was 60/60.

Every misread mark was read as a lower level or a single where it was double; none was read upward. The smallest difference between marks, `‹` vs `«` with the same inner `⟨`, separates levels 1 and 2, and that is where most of them fell. Level 3 was never missed, so the citable lists stayed right.

**Haiku with thinking on**, D v1: wrote level 1 for quotation 1 (`«⟪…⟫»`) but listed it among the citable ones, which is correct. My reading is a slip in writing the answer, not in reading the marks.

### Local models (bonus; stopped early)

At Joseph's word that local models aren't important, the run was stopped with seven models complete, deepseek-r1:14b at 3 of 8 items, and llama3.3:70b not started. gpt-oss:20b doesn't load on this machine's ollama 0.34.4 (*"unsupported tensor … size overflows"*). Of the rest, no model is usable. Most answers fail the requested format first: truncated level maps, level answers written as the marks themselves, every quotation called level 3. Writing the marks back fails as well: phi4-mini and llama3.2 strip or substitute them (`«…»`, `⟨…⟩`). The best partial, qwen3-4b (thinking off), got 13/20 on D and 5/6 on C. Totals are in `score.py`'s table.

## For the decision

- **As designed, the marks are read reliably by the frontier minds tested,** with the legend in context and without it, in lists and inline, and written back exactly.
- **The weakest at-a-glance reader errs only downward,** so a misread never upgrades a quotation to citable. That direction comes from these few errors, not from a guarantee.
- **If a wider margin were wanted at levels 1 and 2,** they differ by a single outer character. An option, not a recommendation: change the inner mark of level 1 as well, so that every pair of levels differs in two places. Nothing measured here requires it.

## Limits

One prompt wording; a legend in context for A, C and D; six frontier minds (no GPT); Claude repeats aren't independent samples; models read code points, not rendered glyphs, so a human reader's view of the same marks in a given font is a separate question.

## Files

`probe.py` (questions; `KINDS`, `LAYOUTS`, `LEDGER` env vars; `MIND:KIND:LAYOUT` re-asks one item), `score.py`, `ledger.jsonl`, `ledger-local.jsonl`, `run-frontier.log`, `run-local.log`.
