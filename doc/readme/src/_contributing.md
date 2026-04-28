## Contributing

ASF is research-stage work; contributions take a few specific forms.

**Engaging with the theory.** The most valuable contribution is *de-novo evaluation*: read segments without first reading existing audits or pending findings, form independent judgments, and surface what you find. Where you disagree with a claim or its scope, that is signal. Procedure: see [`doc/de-novo-audit-instructions.md`](doc/de-novo-audit-instructions.md). Read [`README-auditor.md`](README-auditor.md) instead of this README for the audit-safe framing.

**Adding theory content.** Segments are added under `{component}/src/` following [`FORMAT.md`](FORMAT.md) conventions: YAML frontmatter (slug, type, status, dependencies); one-sentence summary; Formal Expression with epistemic tags; Epistemic Status; Discussion; optional Findings; optional Working Notes. Promotion follows a four-gate workflow detailed in FORMAT.md. Slugs follow `{type-prefix}-{subject-noun}` and are aligned mechanically by [`bin/align-slug`](bin/align-slug).

**Spikes.** Speculative or in-progress work that is not yet ready for segment promotion lives under `msc/spike-{topic}.md`. Spikes are honest reasoning trails; results that promote out of spikes land in segments per the math-lives-in-segments discipline.

**Tooling.** Internal process scripts (build, extract, lint) are written in Ruby; community-facing tooling (simulations, reproducibility scripts) is written in Python. New scripts in `bin/` follow this convention; existing scripts that don't are not retroactively rewritten.

**Editing this README.** This file is *auto-generated* from partials under [`doc/readme/src/`](doc/readme/src/) via [`bin/build-readme`](bin/build-readme). Direct edits to `README.md` will be overwritten on the next build. To change README content, edit the relevant partial (`doc/readme/src/_<name>.md`) and re-run `bin/build-readme`, or run [`bin/refresh-all`](bin/refresh-all) to also regenerate the auto-extracted partials (`_findings-summary.md`, `_recent-progress.md`, `_known-issues.md`). Templates live in `doc/readme/*.liquid` and only change when the section *order* or *set* changes. The same discipline applies to `README-auditor.md`.

**Reporting issues.** Open an issue on GitHub or contact the project maintainer (see commit history).
