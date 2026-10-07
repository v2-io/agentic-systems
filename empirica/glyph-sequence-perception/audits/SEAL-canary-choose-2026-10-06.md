# Sealed: the canary's discriminator answers

*Committed 2026-10-06, before round c095, the first round to ask `choose` questions, had recorded. By the independent session (Claude Opus 5.5).*

**What is sealed.** Every `choose` answer whose context or candidates contain a glyph of Joseph's block-fill canary:

`▁ ▂ ▃ ▄ ▅ ▆ ▇ █ 🮆 🮅 🮄 ▀ 🮃 🮂 ▔ ▉`

The list includes `▉`, the chart's candidate at `█`.

**Why.** CATALOG v3 §13 freezes the model before the canaries are computed, so that the acceptance tests can't be met by tuning. The v3 audit (`catalog-design-v3-2026-10-06.md`, C6) pointed out that the canary's discriminator positions lead c095, so their answers will exist long before a model can be frozen. A freeze means something only if nobody has looked first.

**The commitment.** The session will not query, tabulate or display those answers until all of these hold:

1. The catalog's model (parts, strata, priors, combination rule, tier view, tolerances) is written down and committed.
2. That commit's hash is recorded below.
3. The code that computes the canary's result is committed.

No read-off reads `choose` answers today (`report/best.py` and `run.py`), so nothing surfaces them by accident. Aggregate checks over all `choose` answers that exclude these glyphs are allowed: parse rates, position bias, per-mind chart preference.

**The v3 audit also suggests** (C6) restating tests 3 and 4 procedurally: *the catalog's assignment at these positions follows from the listed answers by the frozen rules, and a hand audit agrees.* Under that form, whether the canary turns out intuitive becomes a finding the catalog reports, not a pass/fail condition. Version 4 will consider it. The seal holds either way, since knowing the answers would still steer the choices the freeze fixes.

**Model frozen at commit:** *(to be filled when it happens)*

## Addendum, 2026-10-06 (before round c096 is planned)

**Extended to the name-only order question.** Every `names` answer whose glyph set contains a canary glyph is sealed on the same terms. CATALOG v5 §7a measures the canary's name route with that question, and knowing its answers would steer the name route's rules, which the freeze fixes. The first `names` questions are planned in c096. D controls (`choose` after a neutral context) whose pair contains a canary glyph are already covered by the rule above.

**What the seal doesn't cover.** The canary's triad, pick and continue answers were public before the seal and are quoted in CATALOG §7b and §14. So the seal protects against tuning on the discriminator and name-only answers only. (Suggested by the v4 check, `catalog-design-v4-check-2026-10-06.md`.)

## Addendum, 2026-10-06 evening: the planner reads `choose` and `names` answers, blinded at the canary

From planner stochastic-1 (c102) the question planner weights candidate questions by the answers they already have, `choose` and `names` included, so "no read-off reads `choose` answers" no longer covers everything that reads them. The planner audit (`audits/planner-stochastic-2026-10-06.md`, finding 7) found the channel: how often a canary position is re-asked would have been a faint function of its sealed answers, visible in the committed `questions.jsonl`. Since stochastic-2 (c104), every `choose`, D-control and `names` candidate touching a canary glyph is weighted by its answer count alone, never by what the answers say (`priority/plan.py`, `blind()`). Since stochastic-3 (c106), neutral contexts for D controls never draw a canary glyph, and a pair once asked after one is weighted by its count alone; the taint is found from the questions files, never from answers. The catalog drops sealed answers before computing anything, as before. In c102–c103 the planner's weights at canary positions did depend on the sealed answers (that is the channel finding 7 describes, faint because the weight barely moves with them); no answer was displayed or tabulated.

## Addendum, 2026-10-06, about 21:40: insert and remove answers touching the canary

*The coordinating session (Claude Opus 5.5), from the stochastic-5 audit's P8.*

- **The new question touches the canary's discriminator.** The insert question ("can you make this sequence longer by inserting one or more missing symbols?") asked beside a canary glyph is the sealed discriminator in another form: an insertion between `█` and the next glyph says whether `▉` belongs there.
- **Where the seal's letter stops.** It covers `choose` and `names`; its spirit covers this.
- **What has already been read.** Test round p003 asked insert and remove of Joseph's own run `┉┈┄─━▬█▌▍`, which holds `█`. Three of four minds inserted `▉▊▋` between `█` and `▌`; `▉` is a canary glyph. Those answers were read and shown to Joseph and to the stochastic-5 auditor at about 20:45.
- **Interim step, reversible.** From stochastic-5, the planner asks insert and remove of no run holding a canary glyph.
- **Joseph's ruling is needed** on whether insert and remove answers touching the canary are sealed as `names` is.
