# Working notes (append-only log of the spike, in the order things happened)

*Labels: **[measured]** computed on the snapshot (`lib.py`; taken 2026-10-06 16:36, 184,459 answers kept, 148 sealed answers dropped before anything else); **[observed]** read off examples; **[inference]**; **[guess]**.*

## 16:36 Seal note

Before `lib.py` existed I ran one count of records by kind × family over all answer files, sealed `choose` and `names` records included in the totals. It showed counts only, no answer content. From then on every script loads through `lib.py`, which drops sealed records first.

## 16:50 Joseph's clarification, relayed by the coordinator (verbatim)

> "(wrt my numbering mismatch-- apologies for any confusion-- I was basically just trying to say "look at the data, and then we'll probably need to have a model-sensitive vs agnostic finding / parameter on found sequences, or possibly something else depending on what the data is actually showing, if anything")"

Context for where findings may be used: a per-sequence quantity the catalog could carry. Not a result to aim at.

## 16:45 Agreement between minds, noise removed (`distance.py`)

For questions two minds each answered at least twice, $D = \tfrac12(w_A + w_B) - c = \tfrac12 \sum_x (p_A(x) - p_B(x))^2$, where $w$ is within-mind agreement and $c$ cross agreement. $D = 0$ exactly when the two minds answer alike. [measured]

- **Continue:** Sonnet–Opus $D = -0.01 \pm 0.01$ (n = 51), Opus–Grok $0.00$ (n = 45), Sonnet–Grok $0.054 \pm 0.007$ (n = 1,107), Haiku-without-thinking against Sonnet $0.097$, against Grok $0.108$.
- **Cohere:** Haiku-without-thinking–Grok $0.018 \pm 0.014$ (n = 487), Grok–Gemini Flash $0.009 \pm 0.032$ (n = 57); Sonnet against Grok $0.230 \pm 0.020$, against Haiku-without-thinking $0.273$, against Gemini Flash $0.292$.
- **Picks (generator minds, 5 draws each):** Sonnet–Haiku $0.131 \pm 0.007$ (same family), Sonnet–Grok $0.183 \pm 0.014$, Haiku–Grok $0.189$, Sonnet–Gemini $0.166 \pm 0.033$. Null contexts: $D/W$ about 0.6 for every pair, within or across families.

[inference] On free continuation and on yes/no recognition, the largest differences are between minds or rater styles, not families. On forced picks, there is a family component.

## 16:55 The Sonnet–Grok continue difference is bimodal [measured, observed]

Of 1,107 contexts, 1,031 have $D \leq 0.05$ and 75 have $D = 1$. Nearly all the $D = 1$ cases are Claude continuing the code chart in a block with no everyday order (Canadian syllabics, Mathematical Greek, Ethiopic, cuneiform numerals, Hangul jamo, mahjong tiles, box drawing), and Grok answering "none". Haiku and Gemini Flash side with Sonnet in most. A few are glyph choices: `十百千万 → 億` (Sonnet) against `亿` (Grok, the simplified form); `🂤…🂫 → 🂭` (Sonnet skips the knight `🂬`, as a standard deck does) against `🂬` (Grok, the chart).

## 17:05 The end-placement pattern, tested outside its examples: refuted as stated [measured]

`endplace.py`. Where Sonnet continues with the chart's next glyph, Grok stops 0.13–0.27 of the time; where Sonnet continues with another glyph, 0.24–0.31. No familiarity effect (token counts in Qwen2.5 and the 2023 Claude vocabulary, `tok.py`). The 16:55 reading ("Grok declines chart walks through unfamiliar blocks") came from the most-retested contexts, which are mostly chart walks. It is withdrawn.

## 17:15 Stopping is a per-mind threshold [measured]

`threshold.py`: binned by how determined a context is according to the *other* minds, Grok stops more than Sonnet in every bin, by roughly a constant +0.6 to +0.7 on the logit scale (top bin: 0.089 against 0.017). Gemini Flash stops like Sonnet in every bin.

`rasch.py`: $\operatorname{logit} P(\text{stop}_{m,i}) = \alpha_m + \beta_i$, with $\beta_i$ of each test context estimated from minds other than the pair compared. Flat Sonnet-continues / Grok-stops splits: observed 43, predicted 51 (95% 38–65); reverse: observed 2, predicted 10.4. Sonnet–Haiku-without-thinking: 65 against 72 [57–88]. The additive threshold model accounts for all flat commit splits on continue. Thresholds relative to Sonnet: Opus −0.02, Gemini Flash +0.51, Grok +0.80, Haiku (both conditions) +1.0, Gemini Pro +1.26.

## 17:30 Thresholds by question kind [measured]

`additive.py` (fitted $\alpha_m$, relative to Sonnet):
- triad, naming a middle: Gemini Pro −1.56, Haiku −1.35, Grok −1.13, Opus −0.61, Haiku-without-thinking −0.45, Sonnet 0, Gemini Flash +0.05;
- cohere, "yes" on real runs: Gemini Pro −0.09, Sonnet 0, Haiku +0.69, Gemini Flash +0.80, Opus +0.89, Haiku-without-thinking +1.21, Grok +1.30;
- inhibit, "yes" on real candidates: all within ±0.3.

Grok is conservative in continuation and betweenness and lenient in whole-run coherence. Gemini Flash and Gemini Pro sit at opposite ends on triads. Thresholds are mind × question kind, not family traits.

Triads are the one kind where flat commit splits exceed the additive prediction (Grok declines / Flash commits: 66 against 26; the reverse 13 against 0.8). The excess is as large within families (Sonnet–Opus 3.8% of items, Flash–Pro 4.2%) as across (Sonnet–Grok 2.3%, Sonnet–Flash 2.1%, Grok–Flash 5.2%); excess = (observed − predicted, both directions) / items, Gemini Flash is the common factor, and repeated triad answers come from rotations asked together, so overdispersion inflates every pair [inference].

## 17:35 Gapped triads [measured]

`gapped.py`, all triads, `▁` excluded. Share naming a middle on same-block triples with code-point gaps of 2–4: Gemini Flash 0.82, Sonnet 0.72, Opus 0.66, Gemini Pro 0.54, Haiku 0.48, Grok 0.46. When a middle is named, it's the code-point median 0.87–0.96 for every mind. The pattern read off the Grok–Gemini flat splits generalises, but as a mind-level willingness to commit, not a family trait.

## 17:40 Content against commitment [measured]

`commit.py`. Continue: 74–90% of pairwise disagreements are about whether to continue; when both frontier minds continue, the same glyph 0.93–0.99 of the time (Sonnet–Grok 0.940, Opus–Grok 0.954, Sonnet–Opus 0.957, Opus–Gemini Pro 0.987); Haiku-without-thinking 0.82–0.87. Triads: same middle 0.92–0.97 when both commit. Order lines: 77% identical between Sonnet and Grok, 17% differ in membership, about 5% reorder; the same rates within families.

## 17:50 Whose side a third mind takes [measured]

`sides.py`. Continue, Sonnet ≠ Grok: Opus sides with Sonnet 0.59 / 0.32; Gemini Flash 0.37 / 0.45 and Pro 0.32 / 0.57 with Grok. Cohere, Sonnet ≠ Grok: Gemini Flash sides with Grok 0.68, Haiku-without-thinking 0.57, Opus 0.48 / 0.41. Inhibit: Opus 0.61, Haiku 0.60, Gemini Flash 0.55 with Sonnet. Triads and continue: Gemini Pro sides with Grok against Gemini Flash. [inference] A Claude affinity exists in continuation for the two large Claude minds; elsewhere the outlier is a mind (Sonnet on cohere, Grok on inhibit, Gemini Flash on triads). Caveat: noise in one of the pair pushes third minds toward the other; Grok's continue retest is 0.86 against Sonnet's 0.94.

## 17:55 The chart test the whys spike asked for [measured]

`choose.py` (unsealed `choose` only). Paired positions: Sonnet chooses the chart's glyph 0.536, Grok 0.470 (n = 446, paired difference about 3 SE). Against own neutral controls: Sonnet +0.067, Grok −0.065, Gemini Flash −0.036, Opus −0.107 (n = 107 / 30). Every mind is near 50/50 at contested positions. The tilt is Sonnet's, not Claude's.

## 18:05 Recognition by class; the Abbott correction against a logit threshold [measured]

`cohere_class.py` (Abbott, per-mind controls by set class): every mind near ceiling on contiguous runs (0.95–0.99); on non-monotone runs Sonnet 0.37 against Grok, Gemini Flash and Opus 0.53.

`cohere_logit.py`: a per-mind logit threshold alone reproduces Grok's, Gemini Flash's and Haiku-without-thinking's class pattern to within about 0.03, but not Sonnet's (contiguous 0.975 observed against 0.788 predicted; other 0.473 against 0.585). Per-mind regression $\operatorname{logit} P = a + s\,\beta_{\text{others}} + c_{\text{contig}} + c_{\text{mono}}$: slopes nearly equal (0.82–1.16), contiguity offsets Sonnet +3.14, Haiku-without-thinking +2.33, Opus +1.68, Grok +0.81, Gemini Flash +0.39; monotone offsets in the same family order.

`selfpref.py`: within sources with power (walks, written runs, pick branches), Sonnet (+1.5 to +2.2) and Haiku-without-thinking (+1.4 to +1.9) are positive throughout; Grok −1.33 (walks), −0.12 (written); Opus and Gemini mixed. Survey seeds separate perfectly, so the authorship split (self-preference) has no power. [inference] Robust: the two Claude core minds lean on code-point contiguity in whole-run recognition more than Grok. Self-preference (Panickssery et al. 2024) is not ruled out.

## 18:10 Glyph-level family specificity [measured]

`glyphscan.py`: residual of committing to a triad middle, per (glyph, mind), against the additive model. `▁` for Gemini Flash z = −19.1 (n = 98), for Gemini Pro −3.9 (n = 84); nothing else beyond z ≈ −5.5, among 2,388 cells. Flash's other ramp glyphs (z −5 to −8) vanish when triads holding `▁` are removed: spillover. The out-of-kind test (Gemini on continue contexts descending to `▂`, and on whole runs holding `▁`) has no data: Gemini answered none of the former and one of the latter.

## 18:20 Reproducible content splits [measured, observed]

`contentsplits.py`: of 453 triads and 14 continue contexts where at least two families each committed firmly (≥ 3 answers, ≥ 80%), one content split: `■▤▦` (Claude and Gemini `▦`, Grok `▤`, the code-point median). At mind level (≥ 2 answers each, unanimous, both committed): Sonnet–Grok 9 of 870 (1.0%), Sonnet–Haiku-without-thinking 30 of 743 (4.0%), Haiku-without-thinking–Grok 22 of 591 (3.7%), Sonnet–Opus 0 of 48.

The nine Sonnet–Grok splits (identified with the Unicode MCP): styled capital Chi `𝞦` against plain `Χ` after `𝞠…𝞥`; `⑽` against `⑩`; `⒧` against `ⓛ`; `億` against `亿` (twice); `↙` against `⬋`; box drawing `┦` against `┒`; card knight skipped (`🂭`) against included (`🂬`); dominoes `🂍🂎🂏🂐` → Sonnet `🂱` (an ace of hearts: an arithmetic slip) against Grok `🂑` (correct). Most share the abstract next element and differ in its form.

`dress.py`, tested on all dressed contexts: every mind keeps the last glyph's block 0.94–0.975 of the time; where Sonnet and Grok differ, both keep the dress in 129 of 176, Sonnet alone 36, Grok alone 10. Supported, but weak: Grok leaves the dress a little more often; dress is not the main axis of content splits.

## 18:25 Picks by determinacy (drill outside the kinds that suggested content-agrees) [measured]

`pickdet.py`: noise-free distance between generator minds falls with first-impression determinacy (Sonnet–Haiku 0.176 → 0.103 → 0.103; Sonnet–Grok 0.218 → 0.159); at low determinacy, cross-family 0.22–0.27 against within-Claude 0.176. High-determinacy cross-family cells have n < 10. Supported in direction, underpowered.

## 18:30 Literature [read]

Cacioli 2026 (arXiv 2603.14893): signal-detection decomposition of LLM judgements into sensitivity and criterion; calibration metrics conflate them. Panickssery, Bowman & Feng, NeurIPS 2024: LLM evaluators recognise and favour their own generations. TokSuite (arXiv 2512.20757): tokenizer choice measurably changes behaviour. Nothing found on cross-family perception of Unicode sequences.

## 17:30 (clock time) Strengthening after the verification

The verifier's report (`de-novo-feedback-1.md`) and the strengthening attempts it named are answered in `strengthening-1.md`. Correction to this log: its section times from 16:45 to 18:30 above are estimates, not clock readings, as the README says; from here on, times are from `date`.
