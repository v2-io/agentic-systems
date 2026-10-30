---
kind: item
owner: C.4
opened: 2026-10-30T23:32:34Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:hyp-exponential-cognitive-load]
---

# Seed to attempt: for an AI substrate, cognitive load may be step-shaped, not exponential. 02-tst-core #hyp-exponential-cognitive-load models the k^discontinuities penalty on human working memory. An agent with a hard context limit and near-perfect in-window recall plausibly has a saturating, step-shaped cost (flat until the working set exceeds the window, then a cliff), which is a falsifiable sharpening of the cross-domain claim and is absent from both TST and 03-llm-core. First task: derive the AI-substrate form under named memory-architecture assumptions, then test it. Source: audits/polish-and-sentiment-ledger.md row S39 (gem-hunt 849201 B1 / Fresh-10, audits/.gem-hunt-trail/GEM-WORKING-849201/).
