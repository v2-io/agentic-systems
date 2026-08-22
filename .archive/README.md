# `.archive/` — superseded materials (formerly `_obs/`)

This directory is the project's archaeology home. It was `_obs/` until 2026-08-22. Dot-dir on purpose: it is off the default `ls` / `aspectus` surface, same class as `spikes/.archived/` and `spikes/.integrated/`. Follow a pointer, or `ls -a`.

**Frozen.** Do not sweep or "correct" names here. Prior names (ACT, AAD, old dir layout) stay as written — they are the object the document is about, not a stale label.

## Layout

- Loose files and subdirectories: superseded docs, TFT-era sources (`old-tf-*`), retired tooling, drained trackers, illustration drafts. These stay unpacked because live pointers (NOTATION, format SOP, Working Notes) still name them.
- [`msc-naming-2026-08-22.tar.gz`](msc-naming-2026-08-22.tar.gz) — the naming-cycle tree formerly at `msc/naming/` (votes, aggregates, cards, trackers, rename-plan, master-list, name-decision records). 123 files; sha256 `1357c265cfed9b8b9247ba21494c5cfb9ac89911169bf47b6e176eced39a5ff1`.
- [`abstract-agentic-b.svgz`](abstract-agentic-b.svgz) — gzip of the 91M `abstract-agentic-b.svg` illustration (44M; the one file over GitHub's 50MB warning). `gzip -dc` restores the original SVG.

To restore the naming-cycle tree at the repo root:

```
tar -xzf .archive/msc-naming-2026-08-22.tar.gz
```

That recreates `msc/naming/`. The `bin/naming-*` tools still default to those paths. The name-decision records `msc/naming/name-transition-aad.md` (ACT→AAD) and `msc/naming/collision-check-brief.md` keep "AAD" literal by construction — sweeping them would falsely read "ACT→AAT".
