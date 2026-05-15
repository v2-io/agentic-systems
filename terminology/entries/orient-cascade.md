---
slug: orient-cascade
schema_version: 1
term: orient cascade
name: Orient cascade
brief: "Within-cycle resolution order: $M_t$ update → $\\Sigma_t$ revision → $O_t$ revision."
layer: prose-symbol
status: canon
tags: [structural_concepts]
source_type: asf
primary_source: 01-aat-core/src/der-orient-cascade.md
first_asf_mention: 01-aat-core/src/der-orient-cascade.md
see_also: [directed-separation, actuated-agent, mismatch, satisfaction-gap, control-regret]
aliases: []
do_not_confuse: []
---

The expansion of [epistrophe](epistrophe.md) for actuated agents into a
multi-step cascade: first reduce the epistemic mismatch (update $M_t$), then
re-assess attainability (recompute the [satisfaction
gap](satisfaction-gap.md)), then re-evaluate the strategy (recompute [control
regret](control-regret.md)), and only if needed revise the objective $O_t$. The
ordering is *forced by information dependency* — each step's input depends on
the output of prior steps — not chosen as a design convenience.

Derived in
[`#der-orient-cascade`](../../01-aat-core/src/der-orient-cascade.md).
