# Strengthening 1: the threshold model, Abbott against logit, and the verifier's smaller points

*2026-10-06, 17:15–17:35 MDT by the clock (`date`), the spike agent (Claude Opus 5.5), answering `de-novo-feedback-1.md`. Same snapshot as the spike, now rebuildable (§0). Every number is from a script in this directory, named where cited. Labels: **[measured]**, **[inference]**, **[open]**. The landed FINDINGS are left as they are.*

## Summary

1. **A calibrated threshold model exists** [measured, `irt.py`]. A mixture of "near-certain 0", "near-certain 1" and a graded middle with a threshold and a slope per mind passes the verifier's calibration check: single-answer disagreement, predicted out of sample, has observed-over-predicted ratios of 0.87–1.07 for every continue pair (the 1PL: 0.55–1.31), and 0.84–1.02 on triads, cohere and inhibit.
2. **Under it, flat continue splits are explained for Sonnet–Grok in both directions, but the strong reading fails** [measured, inference]. 43 observed against 35.5 predicted (95% 24–47) and 2 against 1.4 (0–4). But the model places these contexts in the graded middle, where each mind is probabilistic. It predicts Grok's next answer stops again only 0.58 of the time. So "a flat split is settled; asking again won't settle anything" does not hold. They are borderline contexts, about as informative to re-ask as an average one. This is a model reading, and it's directly testable: the 43 contexts are pre-registered with predictions (`prereg-flat-splits.json`). Haiku-without-thinking continues while Grok stops on more contexts than the model predicts (38 against 16.2, band 9–24): a mind × context departure the model doesn't capture.
3. **The triad "excess" was mostly the shared-sheet artifact the verifier suspected** [measured]. 49% of triad (item, mind) cells with repeats have two answers from one sheet. With one answer per sheet, every pair's flat splits fit except Gemini Flash declining where others commit, which is the `▁` effect.
4. **Logit beats Abbott on cohere by held-out likelihood, decisively, and mostly because of the controls** [measured, `abbott.py`]. Per answer: the catalog's Abbott model (controls as pure guessing) −0.4782, logit 2PL −0.4463, about 640 nats over 20,037 answers. Most of the gap is on shuffled controls, which are heterogeneous items, not a guess rate. Abbott with heterogeneous controls (A3) recovers most of it, and logit still wins.
5. **Minds do differ in discrimination** [measured]. Logit slopes under the joint fit: Opus 5.5, Sonnet 1.56, Haiku with thinking 1.37, Gemini Flash 0.92, Haiku without thinking 0.72, Grok 0.69, Gemini Pro 0.46. FINDINGS' "slopes nearly equal (0.82–1.16)" came from a fit against noisy item estimates, which attenuates slopes. It is withdrawn.
6. **Contiguity lean** [measured]. A per-mind offset on real contiguous runs improves held-out fit, and Grok's is the smallest on both scales. Sonnet and Haiku-without-thinking are among the largest, the pair the verifier found tilting toward the chart in `choose`. Gemini Flash sits with Haiku with thinking. Ordered by size: large Claude minds and Haiku, then Gemini, then Grok. Not a clean family split.
7. **`▁` for Gemini Pro is established by the scan itself** once item strength excludes the whole family and repeats are one per sheet: z = −7.0, rank 4 of 2,190 cells, against an empirical 0.5% quantile of −4.27 [measured, `glyphscan2.py`].
8. **Familiarity**: Grok stops more than Sonnet after unfamiliar glyphs, +1.14 ± 0.33 logit within the calibrated model [measured]. The verifier's §8 is confirmed.
9. **Gemini's tool-attempt selection** doesn't move any of these measures when its `no-lookup` re-asks are counted [measured].

## 0. The snapshot is rebuildable

`snapshot/manifest.json` and `snapshot/kept-aids.txt.gz` (the 184,459 answer IDs kept; per-round content digests; the last commit before the snapshot, `929237f7`; the per-file digest prefixes recorded at the time). `python3 lib.py --from-manifest` keeps exactly those IDs from the current answer files and compares digests. Run at 17:15, it kept 184,459 of 184,459, and every round's content matched. Byte lengths of the answer files at snapshot time weren't recorded and can't be recovered. The ID list plus content digests replace them.

## 1. The threshold model, calibrated

**The model** (`irt.py`). For one binary decision, each item is one of three kinds:

- **C:** $P(1 \mid m) = \varepsilon_m$.
- **S:** $P(1 \mid m) = 1 - \delta_m$.
- **M:** $\operatorname{logit} P(1 \mid m, b) = \alpha_m + s_m b + \gamma_m x_i$, with $b \sim N(0,1)$ on a 33-point grid.

The class weights are $\pi$. $x_i = 1$ when the context's last glyph is more than one token in both public byte-level vocabularies (`tok.py`); $\gamma = 0$ unless the variant says "f". Fitted by EM, with nothing anchored to a mind.

**Held-out log-likelihood per answer**, 5 folds over items:

| decision | 1PL | 2PL | 1PL mixture | 2PL mixture | 2PL mixture, familiarity |
|---|---|---|---|---|---|
| continue: stop | −0.4862 | −0.4774 | −0.4776 | −0.4769 | **−0.4676** |
| triad: name a middle | −0.4714 | −0.4664 | — | −0.4656 | **−0.4650** |
| cohere: yes | −0.4244 | −0.4245 | — | −0.4257 | **−0.4195** |
| inhibit: yes | −0.5185 | **−0.4971** | — | −0.4995 | −0.4977 |

**Calibration first** (the verifier's order). For each pair, the predicted single-answer disagreement uses the item's posterior given only the *other* minds' answers:

| continue pair | 1PL, obs / pred | 2PL mixture + familiarity, obs / pred |
|---|---|---|
| Sonnet–Grok | 0.170 / 0.215 (0.79) | 0.170 / 0.166 (1.03) |
| Sonnet–Opus | 0.094 / 0.172 (0.55) | 0.094 / 0.102 (0.93) |
| Sonnet–Haiku-nt | 0.249 / 0.225 (1.11) | 0.249 / 0.252 (0.99) |
| Haiku-nt–Grok | 0.276 / 0.210 (1.31) | 0.276 / 0.262 (1.05) |
| Sonnet–Gemini Flash | 0.160 / 0.189 (0.85) | 0.160 / 0.149 (1.07) |
| Grok–Gemini Flash | 0.153 / 0.208 (0.74) | 0.153 / 0.176 (0.87) |
| Gemini Flash–Pro | 0.165 / 0.219 (0.75) | 0.165 / 0.182 (0.91) |
| Opus–Grok | 0.157 / 0.215 (0.73) | 0.157 / 0.150 (1.05) |

Triads (2PL mixture) 0.84–1.00, cohere 0.98–0.99, inhibit 0.99–1.02. The model is calibrated. The 1PL isn't, which is the verifier's finding, reproduced with a non-anchored prior.

**A second calibration** (`settled.py`). The only mind with third answers in later rounds is Grok. After two agreeing answers, its third repeats them 147/159 = 0.925 (model 0.922) after two continues, and 32/40 = 0.80 (model 0.83) after two stops. The model's within-mind noise is about right where it can be checked.

**Flat continue splits**, each mind of the pair at least 2 answers, unanimous, opposite (2PL mixture + familiarity, 400-draw band):

| pair (A, B) | A continues, B stops: obs / pred [95%] | A stops, B continues: obs / pred [95%] |
|---|---|---|
| Sonnet, Grok | 43 / 35.5 [24–47] | 2 / 1.4 [0–4] |
| Sonnet, Haiku-nt | 65 / 78.0 [62–95] | 3 / 3.3 [0–7] |
| Haiku-nt, Grok | **38 / 16.2 [9–24]** | 42 / 48.1 [37–63] |

Without the familiarity covariate, Sonnet–Haiku falls below its band (65 against 93.6, [75–110]); Sonnet–Grok fits either way. Haiku-without-thinking's fitted slope is near zero (0.26 with familiarity, −0.05 without): its stopping barely follows the shared item dimension, though it's self-consistent (retest 0.74). The Haiku–Grok excess is the one mind × context departure on continue that this model doesn't absorb [inference].

**What the flat splits are, under the calibrated model** (`flatread.py`). For the 43 Sonnet-continues / Grok-stops contexts:

- the posterior class mass is C 0.08, S 0.00, M 0.92 (for all contexts both answered: 0.42 / 0.11 / 0.47), at mean $b = +0.59$;
- the predicted probability that Grok's next answer stops again is 0.58 (median 0.62), and that Sonnet's continues again 0.81;
- one more answer reduces the posterior variance of the context's position by 0.045 for the best mind, against 0.062 on an average context the pair answered (Grok 0.030 against 0.040; Sonnet 0.015 against 0.021).

[inference] Flat splits are borderline contexts where two 2/2 runs are partly chance. They're about three-quarters as informative to re-ask as an average context: neither settled nor especially unclear. This withdraws the debrief's "asking again won't settle anything" and integration-plan item 1's "settled" premise. It rests on the model, because none of the 43 has a third answer, so it is **pre-registered** (`prereg-flat-splits.json`, 43 contexts, each with every mind's predicted next-answer probability). If each is asked once more, Grok's stop share is predicted at 0.58 [0.44–0.72] and Sonnet's continue share at 0.81 [0.70–0.91]. A Grok share near 1 would mean a real mind × context interaction the model misses.

**Triads** (`irt.py triad-commit`). With all answers, flat splits exceed the model in many pairs, within families too (Sonnet commits / Grok declines 48 against 31.8; Grok–Flash 66 against 38.5 and 13 against 0.3; Sonnet–Opus 9 against 4.1). But 49% of (item, mind) cells with two or more answers have answers on a shared sheet, the same triad shown twice in one call. With one answer per (item, mind, sheet) (`--one-per-sheet`):

| pair (A, B) | A declines, B commits: obs / pred [95%] | A commits, B declines |
|---|---|---|
| Sonnet, Grok | 1 / 1.8 [0–4] | 48 / 48.9 [38–62] |
| Sonnet, Opus | 0 / 0.2 | 2 / 2.8 [0–6] |
| Sonnet, Gemini Flash | 10 / 12.6 [6–19] | **15 / 7.6 [3–13]** |
| Grok, Gemini Flash | 65 / 59.5 [47–74] | **7 / 1.5 [0–4]** |
| Gemini Flash, Pro | 1 / 0.1 [0–1] | 7 / 8.0 [4–14] |
| Opus, Grok | 1 / 0.3 [0–2] | 1 / 1.7 [0–5] |

What's left is Gemini Flash declining where others commit. Before deduplication, 12 of 13 such Grok–Flash items and 14 of 22 such Sonnet–Flash items held `▁` (I didn't recount after deduplication). The gapped-triple splits (Grok declines, Flash commits) fit once repeats are one per sheet: they're criterion differences at borderline items, as on continue [measured, inference].

## 2. Abbott against logit, on cohere with its shuffled controls

**Setup** (`abbott.py`): 6,216 items (real runs and shuffled controls, by set class contiguous / other), 20,037 yes/no answers from the seven first-impression minds, 1,332 can't-tell answers dropped. Every model gets the same item-distribution freedom (nonparametric weights on a 41-point grid per population). Only the link differs. 5-fold held-out over items.

| model | link | held-out log-lik per answer |
|---|---|---|
| A1 | catalog build 0: $c_{m,k} + (1 - c_{m,k})\,\theta$; controls $= c_{m,k}$ | −0.4782 |
| A2 | CATALOG §9: $c_{m,k} + (1 - c_{m,k})\,s_m\theta$ | −0.4773 |
| A3 | A2, controls with their own $\theta$ populations | −0.4541 |
| L1 | logit $\alpha_m + \beta$ | −0.4500 |
| L2 | logit $\alpha_m + s_m\beta$ | −0.4463 |
| L3 | L2 + per-mind set-class offset (controls and runs alike) | −0.4459 |
| L4 | L2 + per-mind offset on real contiguous runs only | **−0.4456** |

By population (held-out per answer):

| population | A1 | A3 | L2 | L4 |
|---|---|---|---|---|
| real, contiguous | −0.2645 | −0.2711 | −0.2656 | −0.2633 |
| real, other | −0.5135 | −0.5077 | −0.5055 | −0.5054 |
| control, contiguous | −0.4751 | −0.4517 | −0.4384 | −0.4381 |
| control, other | −0.6016 | −0.5343 | −0.5225 | −0.5222 |

[inference] The catalog's current Abbott model loses about 640 nats to L2. Most of the loss is treating a shuffled control as pure guessing at rate $c$: controls vary (some shuffles are coherent, as METHODOLOGY §4a says), and A3, which lets them, recovers most of the gap. Logit still wins with fewer parameters (L1 has 7 mind parameters, A3 has 21). On real contiguous runs, A1 and the logit models tie. Under A3, Sonnet's and Opus's guess rates fall to 0.00–0.03: their "yes" to a shuffle is better described as finding that shuffle coherent than as guessing.

**Slopes** (L2, all data): Sonnet 1.56, Opus 5.51, Haiku without thinking 0.72, Haiku with thinking 1.37, Grok 0.69, Gemini Flash 0.92, Gemini Pro 0.46. Discrimination differs about twofold between Sonnet and Grok. So CATALOG §9's intent, weighting by discrimination, is sound. What's wrong is measuring discrimination through Abbott with homogeneous controls. FINDINGS §2.4's "slopes nearly equal" is withdrawn (it came from a regression on noisy $\beta$, which attenuates slopes).

**The contiguity lean** (L4; bootstrap over items, 20 refits). Offsets on real contiguous runs, beyond the item's position and the mind's criterion:

| mind | offset (logit) | ÷ slope (item units) | answers on real contiguous runs |
|---|---|---|---|
| Sonnet | +3.16 ± 0.30 | 2.2 | 1,153 |
| Opus | +5.62 ± 2.14 | 1.2 | 240 |
| Haiku without thinking | +1.71 ± 0.21 | 2.5 | 1,131 |
| Haiku with thinking | +1.91 ± 0.48 | 1.3 | 231 |
| Gemini Flash | +1.46 ± 0.33 | 1.3 | 233 |
| Gemini Pro | +0.82 ± 0.72 | 1.9 | 48 |
| Grok | +0.69 ± 0.19 | 0.9 | 1,224 |

Only differences between minds are identified. On both scales, Grok's lean is the smallest and Sonnet's and Haiku-without-thinking's among the largest: the same two minds the verifier found tilting toward the chart in `choose` (paired against controls, +0.106 and +0.107). Two instruments agree on those two minds. The rest is scale-dependent and not a clean family split. What it rests on (code-point contiguity or self-preference) stays open.

## 3. The verifier's smaller points

- **§5, `▁` for Gemini Pro** (`glyphscan2.py`). One answer per sheet; each item's position from minds of *other families*; the calibrated 2PL mixture for each mind's probability. Empirical z quantiles over 2,190 cells: 0.5% −4.27, 1% −3.25; sd 1.40, so the old scale was overdispersed, as the verifier said. Gemini Flash `▁` z = −18.4 (rank 1), **Gemini Pro `▁` z = −7.0 (rank 4)**; ranks 2–3 and 5 are Flash's ramp glyphs, which co-occur with `▁`. The scan alone now establishes Pro's avoidance. Sonnet's `ᚒ` (−5.6, n = 8) and `ᬌ` (−4.3, n = 24) sit at the edge of the null's tail: candidates. The mirror artefact (positive `▁` residuals for every non-Gemini mind) remains by construction, since their item positions now include Gemini.
- **§7, Gemini's tool attempts.** Counting Gemini's `no-lookup` re-asks as its answers: its continue parameters move by at most 0.2 logit, calibration ratios are unchanged, and content agreement moves from 0.928 to 0.931 (Sonnet–Flash) overall and from 0.822 to 0.821 off the chart. Within the answers that exist, the selection doesn't move these measures. The share of Gemini contexts never answered at all, and how they differ, is not measurable from answers [open].
- **§8, familiarity in the Grok reading.** In the calibrated model with familiarity, relative to Sonnet, Grok's stopping rises after an unfamiliar last glyph by +1.14 ± 0.33 logit (+0.81 ± 0.20 in item units; 20 bootstrap refits, so the SE is rough). Confirmed. Not a family pattern: in item units Grok (−0.96), Gemini Pro (−0.78) and Opus (−1.08) sit together, against Sonnet (−1.77) and Haiku with thinking (−2.33). Familiarity is the largest single gain in held-out fit on continue (−0.4769 → −0.4676).
- **§2, §3, §6, §9.** I accept them as written: content agreement is mostly shared chart successors (high off the chart too, and triads stronger than FINDINGS said); the `choose` tilt includes Haiku without thinking; Sonnet–Opus $D \approx 0$ is uninformative; and the wording points. Nothing above contradicts them.
- **§10, reproducibility.** §0 above.

## 4. What changes for the integration plan [inference]

- **Item 1 (planner).** Its premise ("a flat split is settled") is withdrawn. Its conclusion (no disagreement term) survives on a different ground: under a calibrated rater model, flat splits are ordinary borderline contexts, informative at about average rates, so they need no special term in either direction. If "most clarifying" is to mean more than precision of a share, the natural quantity is the expected information about the item's position under a calibrated per-mind model. That is the planner's current per-family $I(k, n)$ when minds are exchangeable, and different when they aren't. The pre-registered re-ask should come first: if Grok repeats its stops near 100%, flat splits are interactions after all, and they would deserve a term.
- **Item 2 (catalog combination rule).** Supported, and now by a held-out comparison: logit with a criterion and slope per mind, controls as heterogeneous items, beats the catalog's Abbott model by about 640 nats on cohere. The minimal change with most of the gain is to stop treating shuffled controls as a guess rate (A3 against A1: about 480 nats). Weights between minds would then come from fitted slopes. Tested on cohere (R) only.
- **Item 3 (per-sequence quantity).** Its "departures from the threshold model" part now has a model to depart from, calibrated. On current data the detectable departures are `▁` for Gemini (both minds) and Haiku-without-thinking's own item dimension on continue.

## 5. Failed or limited

- **The model-free settledness test has no data.** None of the flat-split contexts has a third answer. Hence the pre-registration.
- **Haiku without thinking** isn't described by a shared item dimension: slope near zero, and an unabsorbed flat-split excess against Grok.
- **The scale question.** Offsets and familiarity coefficients rank minds differently in logit units and in item units, and I can't say which scale is "the" one. Claims above are stated only where both scales agree.
- **Gemini Pro's inhibit parameters are degenerate** (α 13, slope 114: few answers, perfect separation). No claim rests on them.
- **Bootstrap SEs come from 20 refits.** They are rough.

## Files added

`irt.py`, `settled.py`, `flatread.py`, `abbott.py`, `glyphscan2.py`, `prereg-flat-splits.json`, `snapshot/manifest.json`, `snapshot/kept-aids.txt.gz`; `lib.py` gained `--from-manifest`, `irt.py` `--one-per-sheet` and `--with-nolookup`.
