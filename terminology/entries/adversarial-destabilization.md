---
slug: adversarial-destabilization
schema_version: 1
term: adversarial destabilization
name: Adversarial destabilization
notation: "$\\mathcal{T}_A > \\Delta\\rho^\\ast_B / \\gamma_A$"
brief: When an adversary's tempo times its coupling effectiveness exceeds the target's adaptive reserve, the target's correction mechanism collapses entirely.
layer: prose-symbol
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aat-core/src/der-adversarial-destabilization.md
first_asf_mention: 01-aat-core/src/der-adversarial-destabilization.md
see_also: [adaptive-reserve, team-persistence, adaptive-tempo]
aliases: []
do_not_confuse: []
---

A precise formalization of "getting inside the opponent's OODA loop": agent $A$
destabilizes agent $B$ when $A$'s adaptive tempo $\mathcal{T}_A$, scaled by coupling
effectiveness $\gamma_A$, generates mismatch in $B$ faster than $B$'s correction
machinery can absorb it — specifically, when $\gamma_A \mathcal{T}_A$ exceeds $B$'s
adaptive reserve $\Delta\rho^\ast_B = \alpha_B R_B - \rho_{B,\text{base}}$.

The failure mode is not merely "large mismatch" but structural breakdown of the
correction mechanism itself: $B$'s epistrophe can no longer outpace the adversarially
amplified aporia. When $B$ is driven past its stability boundary and its degrading
model causes erratic actions that further increase $A$'s coupling effectiveness, a
positive-feedback effects spiral can accelerate the collapse. The mechanism applies
symmetrically and admits two disturbance models: deterministic drift coupling (Model D,
threshold linear in $\alpha_B$) and stochastic noise coupling (Model S, threshold linear
in $\sqrt{\alpha_B}$).

Derived in [`#der-adversarial-destabilization`](../../01-aat-core/src/der-adversarial-destabilization.md);
the cooperative counterpart (allies reducing disturbance) lives in
[`#der-team-persistence`](../../01-aat-core/src/der-team-persistence.md).
