# Audit SOP

The de-novo audit discipline, in two codependent halves — *producing* a fresh-eyes audit and *routing* what it surfaces. They were authored as a pair (each cites the other) and now live side by side under `audit.sop/`.

- [`audit.sop/de-novo.sop.md`](audit.sop/de-novo.sop.md) — **the de-novo audit walk.** How a fresh-eyes auditor reads the framework cold: first-encounter cognition, the per-segment reflection prompts (§4.4), the FINAL deliverable shape, and §7.15 — the *incidental gold* that the reflections produce alongside certified findings.
- [`audit.sop/routing.sop.md`](audit.sop/routing.sop.md) — **finding routing / disposition.** Where each finding belongs once an audit lands: the per-finding disposition enum, the evidence hierarchy (screening order, never the arbiter — truth is), the regression check, the independent-verify gate, the working-directory lifecycle + the `AUDIT-WORKING-*` gold standing gate, and §8 — the *gold lift* that routes §7.15's incidental gold per-segment into Working Notes.

**The two-track output** these encode: a de-novo audit yields (1) *certified findings* — burden-of-proof, theory-fix material → routed by `routing.sop.md`; and (2) *incidental gold* — orthogonal pedagogical / generative material → lifted per-segment into the relevant segment's `## Working Notes`. The early finding-vs-framing conflation is *itself signal* and is preserved, not sanitized.

**Before starting a de-novo audit:** use [`../../README-auditor.md`](../../README-auditor.md), not `README.md` (priming); [`../../PRACTICA.md`](../../PRACTICA.md) is auditor-safe but follow its links into TODO / PROPOSALS / CHANGELOG only *after* the audit lands. Live routing status is [`../../audits/STATUS.md`](../../audits/STATUS.md).

> [!note]
> **Convention:** the old paths `doc/de-novo-audit-instructions.md` and `doc/audit-routing-instructions.md` are now symlinks to the two pieces above, so the ~127 inbound references across the repo resolve untouched. See [`sop-creation.sop.md`](sop-creation.sop.md) for the `.sop` convention and the symlink-vs-full-move rule of thumb.
