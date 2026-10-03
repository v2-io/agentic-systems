# MANIFEST — glyph-magnitude-perception

*Entered 2026-08-25 (pilot day); claims restated 2026-10-03 after the registered v1.0 run. Canonization contract per `empirica/README.md`.*

## What it studies

How language-model minds perceive **order among Unicode glyphs** — which glyph sequences carry monotonic magnitude perceptually, by what mechanisms, with what substrate-dependence — and, co-equally, **how measurement formats and contexts manufacture or suppress perceived order** (demand characteristics, answer-channel priors, position habits, articulation filters, judge context). The experimental object is dual: the glyph-order structure AND the measurement protocol itself.

## Claims

*Tiers: **v1.0** = registered predictions (`PREDICTIONS-v1.0.md`), one campaign, fresh judges, held-out pools, 2026-10-03 (`RUNS.md`); **pilot** = 2026-08-25, single day, informal registration. Every v1.0 claim was audited independently (`analysis/verification/`). Detail and numbers: `analysis/2026-10-03-v1.0-findings.md`, `analysis/v1.0-results.md`.*

1. **[Empirical Claim (v1.0)] Offering ⟂ removes a large share of cross-domain directed edges in every mind tested, and what survives is axis-coherent; the size of the effect depends on the judge and on the measurement context.**
   - Removal: tie-format directed pairs that became ⟂ once offered ranged from 0.28 to 0.72 across frontier judges. The pilot's own judges removed 0.77 of the same 160 pairs.
   - Context: claude-sonnet-5-5 inside an agent harness with pilot wording used ⟂ on 0.76 of presentations; the same model through an isolated CLI used it on 0.41.
   - Axis-coherence: survival was higher for within-locus than for random pairs in every testable frontier judge.
   - The pilot's "~80% manufactured" is the high end of this range, not a constant.
2. **[Empirical Claim (v1.0)] Denoted number is a substrate-invariant axis among frontier minds; measured ink is a secondary correlate; neither survives at 3–7B.**
   - Frontier judges (four Claude models, Grok 4.6, GPT-5.6, two Geminis): the larger Unicode numeric value wins 0.95–1.00 of committed numeric edges. Among non-numeric edges, the denser glyph wins 0.64–0.83.
   - Small open models (llama3.2-3b, gemma3-4b, mistral-7b, hermes3-3b): both correlates are at or below chance (mistral-7b's ink correlate is 0.28).
   - Transitivity does *not* separate the tiers. Among triads whose three pairs are consistent across both presentation orders, no judge produced a cycle. What capability buys is ⟂ use, consistency across presentation order, and the axes.
3. **[Empirical Claim (v1.0)] Compiled numeric decode arbitrates axis conflicts; without it, judges fall back on counts of like elements, then fill; size dominates scattered small elements.**
   - Compiled decode wins over ink and element count for every frontier judge, pooled over 13 items (Roman numerals, seven-segment digits, fractions with large denominators, small-form digits). Exception: the Sonnet models prefer the full-size digit on subscripts (₈ vs 3).
   - Grams resolve by line count first (☷ over ⚌, against measured ink), then by yang/fill. Yang also carries a compiled semantic reading.
   - Weak-decode signs (‱ vs % and ‰) split by model family: Sonnet picks the many-circled sign, the others pick by value. ‱'s decoded quantity (per ten thousand) confounds this item.
4. **[Empirical Claim (v1.0, judge-dependent)] Some orderings are recoverable from a whole set more readily than from pairs, but which ones depends on the mind.**
   - risebar reconstructs for every Claude judge.
   - The pilot's flagship holistic specimen `-=>})|` reconstructs well only for Sonnet 5.5, and Opus reconstructs only a 4-glyph sub-order.
   - Grok's elaboration ladders are pairwise-⟂-heavy for some judges and pairwise-ordered for others.
   - "Holistic" is a relation between a sequence and a mind.
5. **[Empirical Claim (v1.0)] Whole-set honesty is not universal.** Noise sets drew ⟂ on 0.64 of frontier presentations (registered threshold 0.80). Three judges declined consistently; others imposed orders.
6. **[Empirical Claim (pilot)] Mechanism and sequence-kind taxonomies** (fill / count / size-angle / compiled decode; factorizable / holistic / authored / generator lattices) remain pilot-tier working ontologies, *not* tested as taxonomies by v1.0. Joseph's 2026-08-25 ruling keeps them post-hoc and hypothetical.
7. **[Exploratory] In qwen3-embedding, one linear "more" direction partly orders denoted number and fill ladders together.** Leave-one-family-out ρ = +0.68 after leakage removal, surviving codepoint controls. Other embedding models do not show it. Analyst-chosen ladders; not the judges' representations.

## Parameters / regime

- **Judges.** Isolated CLI or HTTP judges with tools, instruction files and memory stripped; residue is recorded in `harness/runner/judges-v1.json`.
  - Anthropic: haiku-4-5, sonnet-5, sonnet-5-5, opus-5-5.
  - xAI: grok-4.6.
  - OpenAI: gpt-5.6-terra, partial.
  - Google: gemini-3.1-pro, gemini-3.8-flash, gemma3-4b.
  - Meta: llama3.2-3b.
  - Mistral: mistral-7b.
  - Microsoft: phi-4-mini, largely unparseable.
  - Nous: hermes3-3b.
  - Alibaba: qwen2.5-3b (exploratory). qwen3-4b has no valid data.
- **Protocol** `gmp-v1.0` (`protocol/PROTOCOL-v1.0.md`, including its append-only post-freeze notes).
  - Fated randomness throughout; per-item option permutation; glyph-echo answers with word fallbacks; the ⟂ / ≈ / graded response set.
  - Single-item and 40-item-sheet modes are recorded as a factor.
- **Pools.** The seed stratum draws on four Anthropic-family surveys only (coverage defect noted in PROTOCOL); the uniform tail is block-uniform.
- **Instruments.** Triads, format experiment, conflict battery, holistic pairs, gestalt reconstruction.
- **Exploratory batteries.** Top-40 (`analysis/top40.md`) and the SIGNA consumer probe.

## Consumers

None yet. Candidate landing sites: 03-llm-core (perception/representation segments). The judge-context finding (claim 1) bears on multi-agent measurement methodology (`doc/sop/multi-agent.sop.md`).

## Provenance

- **Pilot (2026-08-25):** session with Joseph + Fable; narrative at `pilot/pilot-record.md`; raw data at `data/judgments-v0/`.
- **v1.0 (2026-10-03):** built and run by a Claude Opus 5.5 subagent commissioned through the aspectus session.
  - Ledgers: `data/runs-v1/` (inventory in `data/runs-v1/INVENTORY.md`).
  - Stimuli: `data/stimuli-v1/`.
  - Harness: `harness/runner/`.
  - Re-derivations of pilot numbers: `harness/reanalysis/`.
  - Debrief to Joseph: `debrief.md`.
- **Surveys:** `data/surveys-v1/` (seeds, never data).

## Vivarium

planned (protocol maps cleanly to in-vivia judge panels).

## Provenance honesty note

- **Pilot runs** are reproducible in kind, not bit-reproducible (see RUNS.md).
- **v1.0 runs** record every call verbatim: prompt, provider-reported model, usage and raw answer.
  - API judges ran at provider-default temperature, so they too are reproducible in kind.
  - Local judges ran at temperature 0 with a fixed seed.
- **Reasoning effort** was set low but not equalized. Haiku 4.5 thinks about 400 tokens per item; Sonnet 5 thinks none.
- **Single campaign.** Each v1.0 claim rests on one campaign; replication with an independent stimulus fate (v1.1) is the next strengthening step.
