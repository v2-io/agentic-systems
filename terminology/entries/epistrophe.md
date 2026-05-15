---
slug: epistrophe
schema_version: 1
term: epistrophe
name: Epistrophe (Ἐπιστροφή) (turning-toward)
notation: "$\\eta^\\ast$"
brief: "Turning toward reality — gain-weighted update $M_t = M_{t-1} + \\eta^\\ast \\cdot g(\\delta_t)$."
layer: framing-vocabulary
status: canon
tags: [cycle_phases, greek_vocabulary]
source_type: external
primary_source: "Greek philosophical vocabulary (Neoplatonic: turning-back, conversion)"
first_asf_mention: 01-aat-core/src/deriv-recursive-update.md
see_also: [prolepsis, aisthesis, aporia, praxis, update-gain]
aliases: ["ἐπιστροφή"]
do_not_confuse: []
---

The fourth phase of the adaptive cycle: the model is updated in light of the
mismatch, weighted by the update gain $\eta^\ast$. Etymologically Greek for
"turning back" or "conversion" — the reorientation of the model toward what
reality showed.

See
[`#deriv-recursive-update`](../../01-aat-core/src/deriv-recursive-update.md)
for the update law and
[`#emp-update-gain`](../../01-aat-core/src/emp-update-gain.md) for the gain
itself.
