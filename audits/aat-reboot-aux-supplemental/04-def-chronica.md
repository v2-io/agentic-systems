# Supplemental 04 — `#def-chronica`

*Finder, 2026-09-25, alongside `~/src/aat-reboot/scratch/aux/04-def-chronica.md`. Paths are relative to `~/src/arch/asf/`; line numbers are as of `875e1ac3`. Each note is tagged with the slugs it bears on.*

## 1. Checks that passed: please add to the Working Notes of `#def-chronica`

- [def-chronica] Checked the sequence form $\mathcal C_t = (o_1, a_1, \ldots, a_{t-1}, o_t)$ against `NOTATION.md:66`, `form-agent-model.md:28` and `terminology/entries/chronica.md`. They agree; holds.
- [def-chronica] Checked "the agent could not have used $o_t$ to select $a_{t-1}$" against `def-observation-function.md:23` ($o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$) and `post-causal-structure.md:13, 27`. Consistent; holds. (The postulate it rests on comes later in the outline; see the aux, FINDER-OBSERVED (b).)
- [def-chronica] Checked the entropy-collision rationale. `NOTATION.md:58` uses plain $H$ for entropy, and :212 says "$\mathcal C$ for chronica (not $\mathcal H$, to avoid collision with entropy)". The rationale is historical: PROPRIUM's name for the object was $H_t$ (`~/src/arch/proprium/INGEST/old-firmatum/PROPRIUM-ONTOLOGY-v2.md:292`). It holds as a naming reason. The gold's "tighten the rationale" item (Working Notes :89) is about wording, not a defect.
- [def-chronica] Checked "Relationship to the model" against `form-agent-model.md:24` ($M_t = \phi(\mathcal C_t)$) and `def-model-sufficiency.md:22` ($S$ as the fraction of $\mathcal C_t$'s predictive information retained). Holds.
- [def-chronica] Checked that the slugs cited in the Working Notes exist: `#scope-interiority-loop` (03), `#def-auxilia-hierarchy` (04), `#form-event-driven-dynamics`, `#def-death-as-factor-loss`. All resolve; holds. The two firmatum *paths* don't resolve (aux, FINDER-OBSERVED (f)).
- [def-chronica] Checked the `depends:` list against usage. Only the three preceding definitions are used as prerequisites; no appendix is needed. Holds. The absent `#post-causal-structure` edge is an ordering question, not a missing prerequisite in the dependency-DAG sense, because that postulate is itself downstream.

## 2. Notes for other segments

- [form-agent-model] `form-agent-model.md:62`'s Working Note still offers "$M_t = \phi(M_0, \mathcal C_t)$, or … absorbed into $\phi$" as equivalent. The 731548 verifier (`audits/AUDIT-WORKING-731548/verify/03-chronica-trichotomy-verdict.md:52–57`, disposition 2) asked that its variant warning be carried into this Working Note; that never happened. Add the extension from the aux's FINDER-OBSERVED (e): `#result-mismatch-decomposition` steps 2–3 (:35–36) also need $M_{t-1}$ to be chronica-measurable.
- [def-model-class-fitness] Verifier disposition 3 (same file :30, :56) asked for a Working-Notes follow-up: $\mathcal M$ is relative to the available update channels and timescale (frozen-weights session vs fine-tuning). A grep for "fine-tun" or "update channels" in `def-model-class-fitness.md` finds nothing, so it wasn't added.
- [scope-agent-identity] The grounding is circular with `#def-chronica`: :24 presumes non-forkability, and :48 grounds the consequences in "#def-chronica's non-forkability". Also, the Discussion at :63 says "each AI agent session starts a new causal trajectory $\mathcal C_t$ from near-zero", which reads $\mathcal C_t$ as the accessible record (the trichotomy). The 731548 relational fork-detection no-go (`AUDIT-WORKING-731548/05-def-chronica.md:27`) belongs here or at SP-27.
- [SP-27, scope-agent-identity, def-death-as-factor-loss] `PROPOSALS.md:365`'s thesis ("$\phi$ non-injective ⇒ the fork is not in the agent's accessible $\sigma$-algebra") attributes undetectability to non-injectivity. 731548/05:12 argues the fork leaves no trace in either record *whatever* $\phi$ is, so injectivity is irrelevant and detection is relational. That refutation went through no verification round (it's the auditor's own contrarian pass on the gold). Someone should check it before SP-27 lands.
- [obs-context-turnover] :34–40 "the chronica is severed at every session boundary … starts fresh". That uses $\mathcal C_t$ as the accessible record, against `#def-chronica`'s "never removed". Once the rewrite fixes the trichotomy vocabulary, this segment needs the matching term (the record severs; the trajectory doesn't).
- [def-five-constitutive-factors] :33, :43 derive factor (iv) "from #def-chronica + #def-action-transition under append-only system-governance". The governance assumption is doing the work; the abstract chronica's monotonicity is the physical-trajectory sense and gives no inviolable *record*.
- [scope-witness-bidirectional] :88 says "#def-chronica (claims-verified)"; the actual stage is `deps-verified`. Stale.
- [form-event-driven-dynamics, der-recursive-update] The ordinal/metric seam (472913 F4; ledger S34) should be resolved in one place. Note that `#der-recursive-update`'s $g_M$ gives the model a metric clock between events. So 472913's own phrase "$M_t$ is $\tau$-blind by construction" is itself too strong: $M_t = \phi(\mathcal C_t)$ is $\tau$-blind only if $\phi$ ignores the between-event evolution.
- [TODO, audits/STATUS] `CHANGELOG.md:227` and `audits/STATUS.md:23` say the chronica absorb-into-$\phi$ promotion is tracked in TODO §2026-07-03. It isn't (`TODO.md:514–526`). Whoever reconciles trackers should re-add it or mark it absorbed by the reboot.
- [INTRODUCTION] The pilot's supplemental (`00-introduction.md:364`) judged the introduction's identity sentence "Sound at its tier". That is compatible with this finder's view that the tier is robust-qualitative scope, not definitional.

## 3. Other unlifted reflections on this segment (lower value; read so you don't have to)

- `AUDIT-WORKING-308172/03-def-observation-function-and-04-def-chronica.md:13–41` (naming cycle, 2026-05-15).
  - Votes: keep $\mathcal C_t$ +2, keep "chronica" +2, lowercase-italic in prose +2, and gloss form "interaction history (*chronica*)" +1.
  - Wandering (:35–39): non-forkability "binds the framework to a substrate-independent-but-temporal-realist position"; a fork is "one agent dying and two new agents starting from a shared $M_t$ snapshot"; and the claim is "slipped in casually in the Discussion" (which matches FINDER-OBSERVED (a)).
- `AUDIT-WORKING-527914/04-def-chronica.md` (naming cycle).
  - :25–29: "chronica" is the name and "complete interaction history" the first-use gloss; "interaction history" alone "loses singularity, irreversibility, and non-forkability".
  - :41 watchlist: whether TST's "committed chronica" names a subset (it does: `NOTATION.md:67`).
- `AUDIT-WORKING-628417/batch-01-ontology.md` (2026-07-20).
  - :12: non-forkability is "about trajectories, not byte-copyable representations".
  - :18: "identity-substance (chronica) arrives *before* epistemic substance (model)… strange relative to standard POMDP textbooks (which start with beliefs)". That's a pedagogy note for the ordering decision.
  - :26–27: the $M_0$ and passive-observer questions (both in the aux; the passive-observer point converges with the 02 finder's supplemental :57).
- `AUDIT-WORKING-374162` (quiz). Chronica questions are at `01-batch-ch1-foundations-quiz-questions.md:20, 23, 40, 43, 54`. Q40's trap ("indexed by wall-clock … gaps in operation appear as gaps in the record") has an answer key built on the segment's ordinal claim; FINDER-OBSERVED (c) makes that answer partly wrong for running agents. `01-batch-verification.md:23, 25` independently notes that the "state" wording and the fork-undetectability claim are proposed fixes or Working-Notes-only, not landed content.
- `AUDIT-WORKING-419628` mentions chronica only as naming-vote rows (#73, #21, #150, #381, #531). Nothing substantive.

## 4. History (for the record)

- 2026-03-11 `be0e13d6`: created as `chronica.md` from TFT's TF-02 (`.archive/old-tf-02-causal-structure.md:7, 125, 147`). There, non-forkability was "discussion-grade and not required for the formal theorem chain", and its development went to TFT "Appendix G" (now `#scope-agent-identity`).
- 2026-04-02 `96099515`: promoted to deps-verified.
- 2026-05-01 `c741b6c6`: TRACTUS/CHRONICA Working Note added, with Joseph's framing.
- 2026-05-01 `8b22dd53`: ordinal/metric Working Note lifted from 193847 §14.
- 2026-05-21 `b1f599d4`: description expanded from one sentence to three paragraphs, bringing the non-forkability and ordinal material into the opening.
- 2026-05-30 `598631e1`: gold lift A1.
- 2026-06-11 `ac7d07c8`: deaths rename.
- 2026-08-12 `48c7f880`: AISI candidate-spike note.
- The body has had no substantive correction from any audit. All audit-driven content lives in the Working Notes.

## 5. Reasoning about what went where

- I put the dropped tracker item and the verifier's warning first in the aux. A rewrite that softens "only raw material" in the natural way ("primary raw material", or adding $M_0$ as an argument) would silently break three landed results. It's the most consequential thing a coordinator could get wrong here without being told.
- I kept the gold already in the segment's Working Notes out of the aux. He reads it with the segment. I added only what contradicts or extends it: the THREAD-E refutation and the 731548 items.
- FINDER-OBSERVED (c) and (d) are my own. (c) rests on reading $g_M$'s "uncertainty growth over time" as metric-time dependence. I think that's plain from `der-recursive-update.md:18`, but no one else has checked it.
- The worry I'd flag: this segment is where the rewrite decides which object $\mathcal C_t$ *is* (physical trajectory, accessible record, or a random element or filtration for conditioning). Canon uses all of these under one symbol. Volume 4's identity claims need the first, `#obs-context-turnover` uses the second, and the Part I theorems use the third.

## 6. Feedback on the brief and process

- The brief worked well. "Unintegrated means not reflected in this segment" was the right reading. The biggest item here (the dropped routing) only surfaced because I checked the tracker the CHANGELOG pointed to rather than trusting it.
- `relata show-markdown` on the two PSR entries returned `needs-document` (no DOI or arXiv id; open-access fetch failed). For classic papers without DOIs, finders will usually get no line ranges.
- `sed -i ''` edits worked for me in `aat-reboot/` (the asf memory note says in-place editors silently no-op; that may be path- or sandbox-specific).
