# PROPOSED — misc detail home

Residual detail home for indexed spike efforts that are **real and un-started but neither moonshot/theory-edge** (those → [`PROPOSED-ADVANCED.md`](PROPOSED-ADVANCED.md)) **nor tied to a specific segment's Working Notes** (those keep their detail in the segment, the [`PROPOSED.md`](PROPOSED.md) index links to it). Often near-empty by design — that is expected, not a defect. Every entry here has a row in [`PROPOSED.md`](PROPOSED.md) and is reconciled with it bidirectionally (`../doc/spike-routing.md` §2-bis(3) + Refinement 10).

---

## sw-reciprocal-link-check — `bin/` enforcement for the reciprocal-link discipline

**Status:** proposed (un-started). **Added:** 2026-05-19.

The reciprocal-link discipline (every segment Working-Note strengthening / spike-proposal comment links to its `PROPOSED.md` tier; every index row links to its detail home) is currently prose-enforced only — exactly the failure mode that let `PROPOSED.md` silently drift before 2026-05-19. The teeth: a `bin/` check (Ruby, per the internal-script convention) that

- scans `*/src/*.md` Working Notes / Epistemic Status for strengthening / spike-proposal language (a small pattern set: "would land as … if pursued", "open … spike", "follow-on spike", "the named next spike", "spike target", "candidate … appendix if pursued", …) and flags any such comment with no `PROPOSED` back-reference;
- scans `PROPOSED.md` rows for a present, resolvable Details link;
- (stretch) cross-checks that `seg:<slug>`-sourced rows actually have the reciprocal back-link in `<slug>`'s Working Notes.

Output advisory (like `bin/lint-outline`), not blocking. Dogfood note: this entry *is* an indexed un-started effort, tracked by the very index whose integrity it would enforce.

## sw-wn-strengthening-sweep — one-time Working-Note sweep (process)

**Status:** in-progress (staged). **Added:** 2026-05-19.

The known WN strengthenings (Q1/Q2 in `#def-strategy-dag`, C10 in `#der-turnover-information-recursion`) are indexed and back-linked as of 2026-05-19. A full corpus sweep — every segment's Working Notes / Epistemic Status across `01-aat-core` / `02-tst-core` / `03-llm-core` / `04-eli-core` for strengthening/spike-proposal language not yet represented in the index — is staged (spike-routing task; delegable read→curate). Each found item: add an index row (source `seg:<slug>`) + the reciprocal back-link in the Working Note. This is the discipline-completion pass; until it runs, the index is complete for *known* efforts but not yet provably complete for *all* WN-resident ones — stated honestly here rather than implied done.
