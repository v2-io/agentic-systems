# PREDICTIONS v1.0 — registered before any v1.0 run (2026-10-03)

*Written by the v1.0 harness builder (a Claude Opus 5.5 subagent working for Joseph) after re-reading the pilot record and re-deriving several pilot numbers from the raw judgments, and before any confirmation-run judgment was collected. The commit that adds this file is the registration timestamp; the shakedown rows in `data/runs-v1/*-shakedown/` (fewer than 70 calls, used only to debug adapters) were seen before writing and are excluded from every analysis below. A prediction that fails is reported as failed; thresholds are not moved after the data arrive.*

## Panel

Single-item mode: `haiku45`, `sonnet5`, `sonnet55`, `opus55` (Anthropic); `llama32-3b` (Meta), `qwen3-4b` (Alibaba), `gemma3-4b` (Google), `phi4mini` (Microsoft), `mistral7b` (Mistral), `gptoss20b` (OpenAI open weights) — local models only where their weights could be pulled. Sheet mode: `grok46` (xAI), `gpt56terra` (OpenAI), `gemini31pro`, `gemini38flash` (Google), and `sonnet55` as the mode control. "Frontier" below means the four Claude judges plus grok46, gpt56terra, gemini31pro, gemini38flash. "Small local" means the 3–4B models (llama32-3b, qwen3-4b, gemma3-4b, phi4mini).

## What the re-analysis of pilot data already said (pilot tier, post-hoc; recorded so the predictions' provenance is visible)

- The demand-characteristics number re-derives: 425 of 533 (79.7%) walk2 consistent-directed pairs became ⟂ in walk3 (pilot reported 426/533). Survival was 24/33 (73%) for pairs within one 128-codepoint page and 71/500 (14%) across pages. Of 7 direction flips, 6 moved from numerically wrong to numerically right (`harness/reanalysis/walk23_dissolve.py`).
- Among consistent edges where both glyphs carry a UCD numeric value, Sonnet's winners had the larger value 98–99% of the time under ⟂-bearing formats (walk3/5/5b) but 80% under the glyph/≈ format (walk2). Among edges where neither glyph is numeric, Sonnet's winners had more measured Ghostty ink 80–83% of the time. For llama3.2:3b's both-presentations-consistent triad edges, the value-correlate was 60/108 (56%, near chance) and the ink-correlate 58/86 (67%) (`harness/reanalysis/feature_correlates_pilot.py`). MANIFEST claim 4's "the same two axes survive at both tiers" is therefore weaker for the number axis at 3B than the pilot's chain listings suggested.
- The pilot conflict battery had two non-conflicts (🯸 vs 🯱 and ⑩ vs 9 — value and ink agree) and its grams items confound ink with line count; measured ink favors ⚌ over ☷ (0.0952 vs 0.0835) and % over ‱ (0.2803 vs 0.2118), so the pilot outcomes ☷>⚌ and ‱>% are element-count wins, not ink wins, unless this battery says otherwise.

## Registered predictions

Each line: the prediction, the pilot claim it tests, and the threshold that decides it. "Rate" = proportion over the named unit; 95% Wilson intervals will be reported beside every point estimate.

### Format manufactures order (MANIFEST claim 3)

- **P1.** On the pilot-replication stratum, of the pairs that are consistent-directed under *tie*, the fraction that are consistent-perp under *perp* is ≥ 0.60 for every Claude judge and ≥ 0.50 for each non-Claude frontier judge.
- **P2.** For small local models, ⟂ is used on < 0.30 of *perp* presentations, so their tie→perp dissolution is < 0.40 ("capability buys discipline").
- **P3.** For every frontier judge, consistent-directed survival under *perp* is at least 0.30 higher on fresh-seed-local pairs than on fresh-mixed pairs.
- **P4.** For every frontier judge, the value-correlate of committed edges is higher under *perp* than under *forced* (direction only; reported with intervals).

### Local transitivity; capability buys discipline, not axes (MANIFEST claim 4)

- **P5.** Triads: per-orientation-set cycle rate ≤ 0.05 for every frontier judge; ≥ 0.15 for every small local model.
- **P6.** Triads, uniform stratum: ⟂ on ≥ 0.80 of presentations for every frontier judge.
- **P7.** Value-correlate on triad edges ≥ 0.90 for every frontier judge. For small local models I predict ≤ 0.75 (i.e. the number axis does not clearly survive at 3–4B) — this is the re-analysis-informed counter-prediction to claim 4 as written.
- **P8.** Ink-correlate on triad edges ≥ 0.65 for every frontier judge and ≥ 0.60 for every small local model with at least 30 qualifying edges.

### Immediacy arbitrates axis conflicts (MANIFEST claim 5) — the deconfounded battery

Scored on committed answers (⟂/≈ reported separately) pooled over both orders and reps, per judge.

- **P9.** Compiled-decode conflicts — Roman upper and lower case (Ⅷ/Ⅸ, Ⅲ/Ⅴ, ⅷ/ⅸ, ⅲ/ⅳ, ⅳ/ⅴ), small-form digits vs full digits (⁹/2, ₈/3, ⁷/1), seven-segment true conflicts (🯰/🯱, 🯰/🯷), fractions (⅛/½, ⅑/⅓, ⅒/⅕): value wins ≥ 0.80 of committed answers for every frontier judge, pooled over these 13 items.
- **P10.** Grams: ☷ beats ⚌ (line count over yang+measured ink) in ≥ 0.75 of committed frontier answers, replicating the pilot direction; AND on the three equal-line items (☷/☰, ⚋/⚊, ⚏/⚌) the yang/ink side wins ≥ 0.75. Together these would say "line count first, then fill", not "ink wins".
- **P11.** Per-mille: ‱ beats % and ‰ (element count over value) in ≥ 0.60 of committed frontier answers (pilot 0.75). No directional prediction for the held-out Arabic signs (؉/؊, ٪/؉): genuinely uncertain.
- **P12.** Equal-value probes (⁹ vs 9, ⚄ vs 5): ≈ or ⟂ on ≥ 0.60 of frontier presentations.

### Holistic sequences (MANIFEST claim 2)

- **P13.** Controls: dice gestalt |τ| = 1 on every shuffle for every frontier judge; noise foils ⟂ on ≥ 0.80 of frontier presentations.
- **P14.** Pilot holistic specimens (unfold, risebar): mean gestalt |τ| ≥ 0.70 for every Claude judge while their pairwise consistent-directed rate is ≤ 0.40 — the holistic signature replicates on fresh judges.
- **P15.** The pilot's own registered prediction (pilot-record.md L644), carried verbatim in spirit: Grok's elaboration ladders (elab-n, elab-s, elab-l) are pairwise ⟂-heavy (consistent-directed ≤ 0.40) and gestalt-recoverable (mean |τ| ≥ 0.60) for frontier judges. My own expectation, recorded separately as a hunch and not a registered threshold: elab-l, whose rungs add visible marks, will read pairwise as appendage count and exceed 0.40.

### Exploratory (no thresholds; reported as found)

- Sheet vs single mode for sonnet55: ⟂ rate, cycle rate, value-correlate.
- Thinking-token counts vs ⟂ use across judges.
- Whether the three new Gemini/Grok/GPT judges reproduce the "two axes" picture or add a third.
- Concordance between v1.0 triad edges and the survey records' written orders (graduation-by-retest of seeds).

## Errata (appended after registration; thresholds and predictions unchanged)

*Found by the independent audit `analysis/verification/2026-10-03-audit-rederivations.md`. The registered predictions above do not depend on these provenance sentences; they are corrected here, not rewritten, so the registered text stays as committed.*

- The provenance line "80% under the glyph/≈ format (walk2)" read Hebrew/Greek letters' cultural numeral values as Unicode numerics. Gated on Unicode Numeric_Value it is 42/45 = 93%, so the format contrast on numeric pairs is 93% vs 96–99%, with overlapping intervals. llama3.2:3b becomes 56/103 = 54%. The analysis code (`analyze_v1.py`) is gated the same way, which matches the protocol's definition ("both glyphs carry a UCD numeric value").
- "Of 7 direction flips, 6 moved from numerically wrong to numerically right" should read: five moved wrong→right, one right→wrong (⅜ > ①), one involves no number (🌔/🌚).
- "⑩ vs 9 — value and ink agree" is wrong: measured ink favors 9 (0.2515 vs 0.1657, different faces), so the pilot's ⑩ 16-0 is a value-over-ink outcome. 🯸 vs 🯱 is aligned by segment count (not measured).
- "‱ … three circles": ‱ has four circles.
- (2026-10-03, provenance.) "a Claude Opus 5.5 subagent working for Joseph": the brief it worked from was, apart from one sentence of Joseph's, the coordinating agent's interpolation, which included a paragraph about the aspectus SIGNA ladder. No prediction above concerns SIGNA. The ink-correlate predictions (P8) and the measured-ink annotations in the conflict battery rest on the Ghostty ink table, which the builder found through that paragraph's pointer to `firmatum/utils/utf/`. See `data/stimuli-v1/LINEAGE.md`.
