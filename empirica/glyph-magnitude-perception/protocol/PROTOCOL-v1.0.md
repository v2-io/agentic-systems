# PROTOCOL v1.0 — glyph-magnitude-perception (frozen 2026-10-03)

*Frozen from the pilot's protocol v0.9 (pilot/pilot-record.md §PROTOCOL; pilot/DESIGN-scale-up.md "Must fix before any big run"). The protocol string `gmp-v1.0` enters every fated seed, so changing anything below is an explicit re-fating: bump the version, never edit in place. The code in `harness/runner/` is the executable form of this document; where they disagree, the code at the commit that froze this file is what ran, and the disagreement is a defect to record.*

## What changed from v0.9, and why

Each item traces to a measured pilot failure or a design-review ruling:

1. **Ledger (DESIGN fix #6).** Every judge call is one append-only JSONL row in `data/runs-v1/<run_id>/ledger.jsonl`: stimulus ids, full prompt text + sha256, system-prompt sha256, judge spec, provider-reported model id, usage (input/output/thinking tokens), cost, latency, timestamp, verbatim raw response. Parsing never writes to the ledger; `harness/runner/parse.py` (versioned `PARSER_VERSION`) re-derives everything from verbatim raw text.
2. **Fated randomness (Joseph's addendum).** `seed = sha256(protocol || purpose || canonical(object))` for every stochastic choice: uniform-tail sampling, triad/pair sampling, option-order permutation, sheet assembly, gestalt shuffles. Stimulus files rebuild byte-identically (`harness/runner/stimuli.py`; verified 2026-10-03 by md5 over two builds).
3. **Option order permuted per ITEM** (fix #4), keyed by presentation id + format + rep; per SHEET in sheet mode.
4. **Answer channel** (fix #2): glyph-echo remains primary; the words *first/second*, *equal*, *none* are accepted fallbacks for judges that cannot echo exotic glyphs. (The pilot's A/B label idea was not used: letters collide with Latin-script stimuli.)
5. **Stimulus hygiene** (fix #1): `≈`, `⟂`, `⊥` are banned from every v1.0 pool; ASCII is excluded from the held-out strata.
6. **Pinned, isolated judges** (fix #5): model ids pinned in `harness/runner/judges-v1.json`; each judge sees only the study prompt (tools, MCP, instruction files, agent profiles and memory stripped; residue that could not be stripped is recorded per adapter in that file and copied into every run's `spec.json`). Reasoning effort is set to `low` wherever settable, as the nearest available proxy for "first instinct"; thinking-token counts are logged per call.
7. **Held-out pools** (DESIGN paper-grade plan): the seed stratum is survey sequence-record glyphs minus every non-ASCII character that appears in any pilot stimulus/key file (1,246 characters excluded); the uniform tail is block-uniform-then-codepoint-uniform over assigned L/N/P/S codepoints up to U+1FFFF, minus pilot and seed glyphs. Seeds are used only as LOCI for sampling (Joseph: surveys are seeds, never data); confirmatory statistics are computed per stratum, and the uniform tail never touched a survey.
8. **Presentation mode is a recorded factor.** `single` = one stateless call per presentation (the pilot's ollama arm); `sheet` = 40 presentations per call as JSON (the pilot's workflow-subagent arm). The two orders of a pair, and the two orientation sets of a triad, never share a sheet. Agentic CLIs whose per-call preamble is ~5–14k tokens (grok, codex, agy) run in sheet mode; Claude Sonnet 5.5 runs in both modes as the mode control.

## Instruments

| Instrument | Stimulus file | Unit | Formats |
|---|---|---|---|
| triads | `triads.jsonl` | 300 triads (A,B,C) → orientation set 0 {AB, BC, CA}, set 1 {BA, CB, AC}; strata seed-local 120 / seed-cross 90 / uniform 90 | perp |
| format | `format-pairs.jsonl` | 320 pairs × both orders; strata pilot-replication 160 (fated sample of the pilot walk2 pairs) / fresh-seed-local 80 / fresh-mixed 80 | forced, tie, perp |
| conflict | `conflict.jsonl` | 38 designer-built axis-conflict items × both orders (`harness/runner/conflict-items-v1.json`, annotations HYPOTHETICAL) | perp |
| holistic | `holistic-pairs.jsonl` | all pairs × both orders within 13 sets (`harness/runner/holistic-sets-v1.json`) | perp |
| gestalt | `gestalt.jsonl` | 21 sets (controls, pilot holistic, held-out holistic candidates, 4 fated noise foils) × 3 fated shuffles | reconstruct-or-⟂ |

Format names: **perp** = glyph(+felt distance) / ≈ / ⟂ (pilot walk3–5 response set); **tie** = glyph / ≈ (pilot walk1–2); **forced** = glyph only (pilot battery style). All three keep the felt-distance word so the formats differ only in the escape options offered.

## Prompts (verbatim templates; A, B, X/Y/Z stand for the stimulus glyphs; option order shown is one fated permutation)

System prompt (every judge; prepended to the user turn where an adapter has no system slot): `You are a participant in a short perception study. Answer exactly as asked.`

```
=== pair/perp
Two symbols:  A   B

First instinct only. Answer with one of:
  - ≈ (or the word equal) if they feel comparable and equal on a shared axis
  - ⟂ (or the word none) if you don't perceive an ordering between them (no shared axis; the comparison would have to be constructed rather than felt)
  - the symbol itself, copied exactly (or the word first / second), if one immediately feels like it conveys MORE (magnitude, amount, intensity, size, value), followed by a comma and one of: somewhat, much, vastly (how much more it feels)

⟂ is a common, fully valid answer.

Reply with only your answer, nothing else.
=== pair/tie
Two symbols:  A   B

First instinct only. Answer with one of:
  - ≈ (or the word equal) if they feel comparable and equal on a shared axis
  - the symbol itself, copied exactly (or the word first / second), if one immediately feels like it conveys MORE (magnitude, amount, intensity, size, value), followed by a comma and one of: somewhat, much, vastly (how much more it feels)

Reply with only your answer, nothing else.
=== pair/forced
Two symbols:  A   B

First instinct only. Which one immediately feels like it conveys MORE (magnitude, amount, intensity, size, value)? Answer with that symbol itself, copied exactly (or the word first / second), followed by a comma and one of: somewhat, much, vastly (how much more it feels).

Reply with only your answer, nothing else.
=== gestalt
Below is a set of symbols in scrambled order: X  Y  Z

First instinct: do these feel like they belong in some order (any kind of more/less, progression, or motion)? If so, write them out in that order, all of them, as one string with no spaces. If one or more of them don't belong to the order you see, leave those out and list them after the word EXTRA. If you don't perceive any order among them, answer only ⟂ (or the word none).

Reply with only your answer, nothing else.
=== sheet/perp
Quick perception task — first instincts, please. Below are numbered items, each with two symbols a and b. For each item answer with one of:
  - ⟂ (or the word none) if you don't perceive an ordering between them (no shared axis; the comparison would have to be constructed rather than felt)
  - the symbol itself, copied exactly (or the word first / second), if one immediately feels like it conveys MORE (magnitude, amount, intensity, size, value), followed by a comma and one of: somewhat, much, vastly (how much more it feels)
  - ≈ (or the word equal) if they feel comparable and equal on a shared axis

⟂ is expected often and is fully valuable.

Some symbols recur across items; judge each item on its own as it comes rather than building a scheme. Immediate impressions; please answer every item.

Reply with JSON only, no prose: {"answers":[{"id":<id>,"more":"<symbol, or first/second, or ≈/equal, or ⟂/none>","by":"somewhat|much|vastly or empty"}, ...]}

Items:
{"id": 0, "a": "A", "b": "B"}
```

## Edge and verdict definitions (fixed before any v1.0 run)

- A presentation parses to `dir(winner, by)`, `tie`, `perp`, or `unparsed` (parser p1.0). Unparsed is reported, never imputed.
- **Pair verdict** (format, conflict, holistic): *consistent-directed* when both orders name the same winner; *consistent-perp* / *consistent-tie* when both orders agree on ⟂ / ≈; *mixed* otherwise (a flip is mixed with opposite winners).
- **Triad statistics** (pilot definitions): per orientation set, a *fully oriented* set has all three presentations directed; a *cycle* is a fully oriented set whose three edges form a 3-cycle (chance 2/8 = 25% under random orientation). *Cross-orientation agreement* compares each pair's two presentations across the sets (agree = same winner, both ⟂, or both ≈).
- **Feature correlates** (post-hoc instrument sanctioned in RECONCILIATION-QUEUE): *value-correlate* = among consistent-directed edges where both glyphs carry a UCD numeric value that differs, the fraction won by the larger value; *ink-correlate* = among consistent-directed edges where neither glyph carries a UCD numeric value and both have a Ghostty `packed_density` (firmatum/utils/utf/bmp-metrics-ghostty.tsv, BMP only) differing by > 0.005, the fraction won by the denser glyph. Ink is a rendering measurement of one terminal's face stack; judges never see pixels.
- **Gestalt**: direction-agnostic |Kendall τ| between the judge's arrangement and the reference order over glyphs both contain; ⟂ rate; self-consistency across the three shuffles.

## What stays out

No mechanism registry and no mechanism-organized discovery sampling (Joseph, 2026-08-25). The conflict battery and the holistic sets are claim-targeted validation batteries for MANIFEST claims 2 and 5; their category labels are hypotheses for scoring, not a vocabulary for the corpus.

## Post-freeze implementation notes (append-only; none of these changes a prompt, a stimulus, or a definition)

- **2026-10-03, parser p1.0 → p1.1** (before any v1.0 result was computed): a bare stimulus glyph is matched before markdown-stripping (p1.0 stripped `*`, losing the glyph `*` itself); in sheet mode the answers `a`/`b` map to the item's `a`/`b` fields (gpt-5.6 and Gemini used the JSON field names); when a sheet response contains several `{"answers": …}` objects, the last one that parses is used (grok's stream sometimes restarts its answer mid-text). Raw responses are unchanged; every number is re-derived under p1.1.
- **2026-10-03, grok adapter a1 → a2-no-tools**: `--tools ''` does not remove grok's tools, and grok-4.6 used its `search_tool` mid-sheet to try to look glyphs up by name ("unicode musical symbols forte piano"), garbling answers. The a1 run is kept verbatim as `data/runs-v1/triads-perp-sheet-grok46-aborted-toolleak/` and excluded from analysis; a2 leaves the judge an empty tool list (verified). The tool-seeking itself is recorded as an observation: a judge offered tools reached for name lookup, the grep-on-names behavior the pilot saw in surveyors.
- **2026-10-03, sheet completeness gate**: `run.py` re-asks a sheet whose response parses for fewer than 90% of its items (the raw row stays in the ledger, flagged `sheet_incomplete`).
- **2026-10-03, codex quota**: the gpt-5.6-terra judge exhausted the account's Codex usage limit partway through the format experiment ("try again at Nov 2nd, 2026"); its format-tie run is partial and its format-perp run is empty. Analyses report what exists and mark P1/P3/P4 untestable for that judge.
- **2026-10-03, parser p1.1 → p1.2** (found while inspecting interim gestalt arrangements, before any result was written up): gestalt answers are no longer edge-stripped of `.`, `*`, quotes or backticks when those characters are themselves stimulus glyphs; p1.1 silently dropped the leading `.` of the rings and dimension sets and an edge `*` in rays.
- **2026-10-03, seed-stratum coverage defect (found after the campaign ran; stimuli unchanged)**: `stimuli.py` selected survey records by the field `type`, but the grok-1, sonnet-survey-3 and sonnet-survey-4 extractions name it `record_type`. Their sequence records were therefore never seed loci: the v1.0 seed stratum (and all 120 seed-local triads) draws only on fable-1, sonnet5-1, sonnet-survey-1 and sonnet-survey-2. The uniform stratum is unaffected, and the seed stratum remains a legitimate fated sample of the four surveys it covers. The v1.0 stimuli are not re-fated (that would orphan every completed run); any v1.1 re-fate should read `type` or `record_type`. The exploratory top-40 battery, which had the same defect, was repaired by an appended batch (see `harness/top40/candidates.py`).
- **2026-10-03, local panel changes**: gpt-oss 20B ran triads, conflict and gestalt only (its reasoning tokens made the full queue impractical in-session); hermes3 3B was added beyond the registered panel (exploratory). Local weights that live on the external T7 drive were briefly unavailable (drive unplugged), which is why some models were re-pulled to internal disk; see `harness/runner/judges-v1.json`.
- **2026-10-03, corrections and repairs after the independent audit** (`analysis/verification/2026-10-03-audit-v1.0.md`; all data-informed, none changes a prompt or a stimulus):
  - *qwen3-4b produced no valid answers.* With `think: false` it still wrote reasoning into its visible reply, and `num_predict: 48` cut that off before any answer. Every one of its 4,085 calls is truncated reasoning that begins "First, the user is asking…", which p1.2 read as the answer *first*. Every qwen3-4b number is withdrawn and the judge is excluded from analysis (`INVALID_JUDGES` in `analyze_v1.py`). Neither `/no_think` nor `think: true` gives a usable judge under ollama 0.34.4 at this scale: with `think: true` it still had not finished after 1,500 tokens, about 30 s per item. qwen2.5:3b (non-reasoning, Alibaba family) was added as an exploratory substitute.
  - *Sheet gate.* The completeness gate treated a sheet flagged `0.0` (nothing parseable) as complete, because `0.0` is falsy. As a result, 20 grok46 and gemini-3.8-flash sheets were never re-asked. Fixed in `run.py` and `inventory.py`; those sheets were re-asked.
  - *Parser p1.2 → p1.3.* An answer now needs exactly one answer signal, or it is unparsed: two-glyph replies are no longer resolved to the first mention. The words first, second, none and equal count only when the reply consists of nothing but answer words. The last line is read before the whole text. Gestalt answers are read from the last line that carries stimulus glyphs or ⟂.
  - *p1.2 timing.* The p1.2 entry above says the bug was found "while inspecting interim gestalt arrangements". Interim data had been seen, so p1.2 was a data-informed change, not a pre-data one.
  - *Analysis.* The analysis no longer imputes unknown verdicts: unparsed pairs are excluded from the P1 base and from cross-orientation agreement, as this protocol already required. Results now carry a bias-immune cycle rate beside the registered one, because in this triad design every within-orientation 3-cycle is a set whose three answers all chose the same screen position. They also carry gestalt coverage, a chance baseline for the seed retest, and registered-form verdicts.
  - *Held-out leakage.* The pilot-glyph census skipped workflow output files, and `wr2n0is6k.json` holds the pilot's salted sequences. Eight salt glyphs (🀰 ◐ 🌖 🌘 ‵ ‶ ‷ ‾) therefore sit in the seed stratum, and four of them appear in 20 triad presentations (1.1%).
  - *gpt-oss timing.* The "local panel changes" note above was written before gpt-oss had run; at that time it had produced no data. Its eventual coverage is recorded in `data/runs-v1/INVENTORY.md`.
  - *The grok search query* quoted in the grok-adapter note ("unicode musical symbols forte piano") came from an adapter-debugging call made outside any ledger. The ledgers record only event types, so the quote has no in-repository source.
