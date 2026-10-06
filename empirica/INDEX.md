# empirica INDEX — the experiment registry

*One row per experiment. `Consumers` = canon segments citing `empirica:<slug>`. `Vivarium` = rerun status: planned · reran(vivium-ref) · not-applicable. See [README.md](README.md) for the contract.*

| Experiment | Claims (one line) | Tier | Consumers | Vivarium | Status |
|---|---|---|---|---|---|
| [track-b-nonlinear](track-b-nonlinear/MANIFEST.md) | Section-I validation suite: nonlinear mismatch, adversarial-coupling exponent regimes ($b = 2$ vs $3/2$), gain gating, per-dimension persistence, causal-IB survival, Hafez bridge | empirical (validates derived results) | `#obs-section-i-validation-simulations` `#result-adversarial-exponent-regimes` `#obs-gated-tempo-advantage` `#result-per-dimension-persistence` `#deriv-causal-ib-exploration` | planned | active |
| [glyph-sequence-perception](glyph-sequence-perception/MANIFEST.md) | Which glyph sequences (unoriented linear orders, within and across glyph families) LLM minds recognise as sequences, how universal they are across LLM families, and what the recognition is independent of (the code chart, the glyphs' names). Since 2026-10-05 a context tree probed stochastically (`METHODOLOGY.md`); renamed 2026-10-04 from glyph-magnitude-perception; the magnitude era and the triad era (2026-10-04/05) are archived in its `.archive/` | none yet (no claims) | none yet | planned | running: context-tree rounds c001 on (100 by 2026-10-06), Claude, Gemini and Grok; the catalog (`CATALOG.md`) partly built |
