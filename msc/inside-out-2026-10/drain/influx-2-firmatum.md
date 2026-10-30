# Influx drain: firmatum, vivarium, address-theory

> **KR: G.2** in `../INTENT.md` (*stranded additions are landed at honest tier or set aside with a recorded reason*), under **I.9** (every backlog surface drained into the ledger). Canon defects go to **C.1** (C.3 for contradictions between segments), argued non-derived material to **G.0**, terminology to **F.1/F.4**, citations and outward claims to **F.2/F.3**, the truthification machinery to **I.x**. Top intent: *"Complete "in-place" refactor of ASF-- meta, all artifacts, and theory itself."* (Joseph, 2026-10-30). After a compaction, re-read `../INTENT.md`, then this file.

*Drain agent `drain-influx-2-firmatum` (Claude Opus 5.5), 2026-10-30, for the influx-2 drain coordinator, who folds this into `influx-2.md`; integrators work from the ledger items named here. Source: the scout's regional file `../influx-scout/firmatum-vivarium.md` (udon tooling corpus, verisectorium, vivarium, practica, principles, address-theory). The scout checked canon at `8e7ba56d`/`5ade664d`; every disposition here is re-checked against the primary and against canon at HEAD.*

## Questions (with the reading I proceed on)

1. **How do I attach a new source to an item that already exists?** vsect has no verb for it: `recheck` refuses an item that was opened directly or already re-checked, and hand-editing item files bypasses the record. *Reading I proceed on:* where my source only adds evidence to an existing item, I open no duplicate; I record the disposition here as LEDGER with the extra source named, so the coordinator can fold it in. Where my source changes what the item is, I open a new item on the same `segment:` that names the existing item, so `vsect open segment:<slug>` shows them side by side. A `vsect attach item:x --source "…"` (or `note --joins item:x`) would serve all nine drain agents; that is a request for the vsect builder (I.4/I.9), and I leave vsect's code alone.

## Method

Dispositions: **IN** (already in canon at HEAD, where), **DEFECT** (canon defect still present; ledger item), **ADD** (true or worth having, not in canon; ledger item at honest tier), **LEDGER** (already an open item; named), **ASIDE** (set aside, with the reason). Before every `vsect note` I check `vsect open` and `grep -ril` over `items/` for the claim.

## Dispositions

### L6. Five constitutive factors: joint sufficiency (scout's "canon drift")

**DEFECT → C.1**, item `def-five-constitutive-factors-still-offers-the-f`. At HEAD `04-eli-core/src/def-five-constitutive-factors.md` line 60 still says "the conjunction is offered as *sufficient*", and line 56 treats non-sufficiency as a softener. I found the retraction's primary, which the scout did not: `logos/03-inquiry-ai-agents/granted-agency-resubmission-notes.md` cut 2 (2026-07-08) takes "the sufficiency fallback … five factors as the necessary set, sufficiency conjectural pending operationalisation", and `logos/philosophy-papers-feedback.md` (~line 122) names why: the elimination trichotomy is the paper's weakest leg, and Di Paolo's precariousness is a category-escaping sixth candidate. The submitted Inquiry paper (`releases/rc1-submitted/inquiry-ai-agents-2026.md:136`) offers the conjunction "as the necessary set". The not-yet-resubmitted `granted-agency.md` still prefers sufficiency in footnote `suff-alt`, so logos itself is mid-move; ETHICS (vivarium A.7, D.1) is downstream and correct about the direction. Not a public-surface emergency: no hit in `FINDINGS.md`, `README.md` or `CURRENT-VOL1.md`. The item asks the integrator to try the trichotomy against the Di Paolo candidate first (strengthen-first), and raises a prior question the scout did not: in a `type: definition`, sufficiency is stipulative, yet the segment treats it as refutable, so which register the sentence is in decides the repair. The Volume 4 round-3 lane is in that volume today, and the coordinator may want to point it there.

## What was read whole, sampled, not reached

*(being written)*

## Adjacent findings and feedback

*(being written)*
