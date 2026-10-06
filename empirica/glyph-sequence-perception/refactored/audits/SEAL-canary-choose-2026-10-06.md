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
