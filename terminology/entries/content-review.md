---
slug: content-review
schema_version: 1
term: content review
name: Content Review
brief: "Gate 2: the substantive review — derivations valid, labels accurate, Discussion claims epistemically grounded. Produces stage: claims-verified."
layer: framing-vocabulary
status: canon
tags: [process_vocabulary]
seq: 12
subgroup: Gates
source_type: asf
primary_source: FORMAT.md
first_asf_mention: FORMAT.md
see_also: [claims-verified, dependency-audit, mechanical-review]
aliases: [gate 2]
do_not_confuse: [dependency-audit, mechanical-review]
---

Content review is Gate 2 in the segment promotion workflow — the substantive gate. Passing it
advances a segment from `deps-verified` to `claims-verified`. Gate 2 requires a `deps-verified`
segment as input.

The gate applies the three epistemic triage questions to the segment:
1. **What prior objects make this claim well-typed?** — Verify `depends:` is complete.
2. **What competing formulation would also fit?** — Verify `type:` is correct.
3. **What observation would falsify this claim in practice?** — Verify `status:` is correct.

Additionally: trace each derivation step; verify `status:` matches actual epistemic strength;
check formal expressions for well-typedness, units, and boundary behavior.

A critical Gate 2 principle: **Discussion-section claims must face the same epistemic scrutiny as
Formal Expression derivations.** A plausible-sounding explanation that cannot be traced to the
formalism is worse than a gap — it creates false confidence. For each Discussion paragraph, the
reviewer must ask: does this claim add something that follows from the formalism, or does it just
sound like it does?

A mismatch found at Gate 2 returns the segment to `draft` with a specific note.

See [`FORMAT.md`](../../FORMAT.md) §Gate 2.
