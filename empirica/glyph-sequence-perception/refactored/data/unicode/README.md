# Unicode reference data

Published Unicode data, downloaded 2026-10-06 for the lookalike-substitution instrument (CATALOG §6c, §12). It is reference data, not answers, and enters the catalog's manifest by hash.

| file | source | SHA-256 |
|---|---|---|
| `confusables-16.0.0.txt` | https://www.unicode.org/Public/security/16.0.0/confusables.txt (UTS #39) | `95bd0aad6dced5ebc63436f459c06ab21a8d107cd842fb57f5c3a1e91bca8611` |
| `Blocks-16.0.0.txt` | https://www.unicode.org/Public/16.0.0/ucd/Blocks.txt | `f3907b395d410f1b97342292ca6bc83dd12eb4b205f2a0c48efdef99e517d7b0` |

**A first measurement** (2026-10-06, not yet in the design). Of the 1,203 strictly monotone runs asked whole, 454 (38%) have an interior glyph with a confusable in another block.

**A limit.** Confusables are built for security, so they preserve a character's *identity*, not its *style*. Fraktur `𝕶` and Coptic `Ⲕ` are confusable, but they don't look alike in a run. For styled letters, a substitution therefore tests "recognised by identity rather than by the chart". Only where the confusable also keeps the style does it test "the look survives": for example `█` → `■ ∎`, or `▔` → `‾ ¯`.
