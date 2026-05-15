---
slug: control-regret
schema_version: 1
term: control regret
name: Control Regret
notation: $\delta_{\text{regret}}$
brief: Best achievable performance minus current performance — "you're not doing it well enough."
layer: prose-symbol
status: canon
tags: [core_quantities, diagnostic]
source_type: asf
primary_source: 01-aat-core/src/def-control-regret.md
first_asf_mention: 01-aat-core/src/def-control-regret.md
see_also: [satisfaction-gap]
aliases: []
do_not_confuse: []
---

The gap between *best achievable* performance under current information and the
agent's *current* performance. Pairs with [satisfaction
gap](satisfaction-gap.md) ($\delta_{\text{sat}}$, "the world doesn't permit it")
to form a 2×2 diagnostic: any failure-to-achieve decomposes into a
strategy/execution component (control regret) and a structural-impossibility
component (satisfaction gap). The split routes interventions — control regret
says *train harder / re-plan*; satisfaction gap says *change the goal or accept
the floor*.

Defined in [`#def-control-regret`](../../01-aat-core/src/def-control-regret.md).
