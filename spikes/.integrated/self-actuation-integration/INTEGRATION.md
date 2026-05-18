# Self-Actuation Integration — tracker / compaction-recovery doc

**Purpose.** A fresh agent (post-compaction or post-interruption) can resume
the self-actuation integration from this file alone. Brief on what's done;
precise on what remains and on the *reviewed truth* (so the recurring
overclaim is not reintroduced).

## The arc (3 lines)

self-actuation operator spike → independent audit (found the WF gap) →
WF-strengthening attempt (independently reviewed: *not earned*, gap relocated)
→ follow-on class-scoping spike → **the self-actuation grounding no-go**
(independently reviewed: holds as a **conditional, scoped** no-go with a
constructive boundary). The three trail spikes in this dir are history per
*integration-is-replacement*; the canon is the segment below.

## The reviewed truth (do NOT relabel up)

The canonical claim is **conditional + scoped**. The independent review
rejected the spike's pre-review self-assertion of `exact` / unscoped
"impossible". Specifically, baked into P1′:

- **`status: conditional`**, three named premises: scalar-objective scope;
  no-primitive-reflective-oracle; the `#der-directed-separation` draft-stage
  substrate. *Not `exact`.*
- **Scoped**: "no Φ can be *constructed from AAT's covered objective-side
  machinery*" (what the 3 exhausted constructions support). *Not* the
  universal "no such object exists" (that step is argued-not-derived).
- **Lemma 1 static-pointwise** (fixed M_τ,N_h,Π) — the cross-revision lift
  `#def-value-object` says "does not automatically" hold is not used.

If a future pass feels the pull to call this `exact`/universal: that is the
exact "feels-inevitable → therefore" overclaim caught **four** times in this
arc. Don't.

## Integrated so far (done)

- **P1′** — `01-aat-core/src/deriv-self-actuation-grounding.md`
  (`type: derivation`, `status: conditional`, `stage: draft`,
  **NOT** OUTLINE-wired). Carries: the self-actuation operator 𝔄
  (internalized orient-cascade step 5d); degeneracy-without-constraint;
  the no-go (Lemmas 1–2 + Assembly, scoped); Corollary 1 (necessary form of
  a terminal grounding invariant — must be off the objective substrate);
  Corollary 2 (the persistence bound `#result-persistence-condition` is the
  canonical instance); derivation-audit table; Epistemic Status with the 3
  premises + class-robustness; Findings (Everitt 2016 corroboration;
  self-reference vs self-actuation cut; reflective-oracle refuted-by-scope);
  Working Notes (provenance + targeted-search-before-`candidate`). `bin/lint-md`
  clean.

## Remaining (ordered)

- [x] **P3′ — DONE** (lint-clean; committed). `#disc-continuity-stance`
  corrected to the derived form: stance = choice of *terminal non-objective
  invariant* (negotiated = bare persistence floor; morally-continuous =
  floor + an architecturally-non-revisable continuity clause); the
  orthogonality claim is now *derived* via #deriv-self-actuation-grounding,
  not asserted; the "intuitive" objective-tower mechanism is explicitly
  flagged as the inverse of the structure; the 2026-05-04 demote-to-
  deployment-level reconsideration is *resolved against* (orthogonality is
  derived-structural; tier-correlation is an empirical overlay). 6 surgical
  edits incl. summary + Formal-Expression "$O_t$-property" reframe + depends
  (+deriv-self-actuation-grounding, +result-persistence-condition). Status
  kept `discussion-grade` (not over-claimed; structural core derived-by-ref).

- [~] **P2′ — folded into P4′ + a deferred naming flag (scope judgment;
  surfaced to Joseph).** The reserved boundary is *already formalized by
  P1′* — `#deriv-self-actuation-grounding` Formal Expression defines the
  𝔄 operator and the actuated/self-actuated cut. A separate dedicated
  class-definition segment would (a) substantially restate P1′'s setup
  (redundant), and (b) require minting a canonical role-prefixed slug
  (`scope-` vs `def-`; vs the existing prefix-less `#self-actuated-agent`
  forward-ref token) — a naming decision the live naming cycle governs;
  unilaterally minting it mid-concurrent-naming-work is overreach. So:
  the boundary is filled via P1′; P4′ updates the terminology entry +
  forward-refs to point at P1′; a dedicated standalone segment under a
  canonical slug is deferred to the naming cycle (flag in TERMINOLOGY-TODO
  / here). If Joseph wants a standalone segment, create under his chosen slug.

- [x] **P4′ — DONE** (lint-clean; committed). Pointers landed:
  `#der-orient-cascade` step-5d para (internalized 5d = the self-actuation
  operator, well-formed only under the grounding condition);
  `#form-objective-functional` Discussion (the single-interface commitment
  is what drives the no-go); `#def-agent-spectrum` line 48 ("reserved" →
  "formalized in #deriv-self-actuation-grounding");
  `terminology/entries/self-actuated-agent.md` body rewritten ("no segment
  yet formalizes" removed → points at the segment + the no-go).
  `primary_source`/`first_asf_mention` frontmatter left at
  `der-orient-cascade.md` (changing it is a `bin/term decide` naming-system
  action — deferred to the naming cycle, flagged here).

## STATUS: COMPLETE (2026-05-18)

The self-actuation integration is finished and in canon.

- **Independent review (#17): clean affirm.** A fresh reviewer read the
  drafted segments + all primary dependencies directly and verified the
  external prior-art against the primary source: derivation sound, tier
  honestly stated (the recurring `exact`/universal overclaim resisted —
  confirmed in the landed segment), scoped-not-universal honest,
  `disc-continuity-stance` internally consistent, pointers accurate, body
  voice FORMAT-clean. It independently re-surfaced the line-106 OUTLINE
  staleness (good convergence) as a required in-bundle fix, plus two trivial
  polish items — all applied.
- **#18 done:** P1′ wired into `01-aat-core/OUTLINE.md` *Appendices Details*
  (Derivation row, precedent = `#deriv-stochastic-non-exit`); the stale
  `#disc-continuity-stance` OUTLINE row (line ~106) re-synced to the
  P3′-corrected truth; the two review polish items applied (der-orient-cascade
  pointer conditional/scoped qualifier; P1′ Related-Work stray date dropped).
  `bin/lint-md` clean; `bin/lint-outline` introduced **zero** new
  violations (the 3 ordering / 1 missing are exactly pre-existing and
  unrelated; the `disc-continuity-stance → deriv-self-actuation-grounding`
  line is the tolerated main-references-appendix-proof informational
  pattern). Math verified fully present in `#deriv-self-actuation-grounding`
  (verify-before-archive satisfied via the independent review).
- This trail dir is archived to `spikes/.integrated/self-actuation-integration/`.
- **Open follow-ups (outside this integration's scope, still tracked):**
  #12 vocabulary sweep ("witness" → "independent review / attested",
  two-tier) across these now-archived spike files; #13 CHANGELOG provenance
  (commit-1 entangled in `31e54e7`); the deferred dedicated
  `self-actuated-agent` segment-under-a-canonical-slug (naming-cycle);
  `terminology/entries/self-actuated-agent.md` `primary_source` metadata
  (a `bin/term decide` change, naming-cycle).

---

### Historical: the integration plan (now all done)

**Drafted bundle = P1′ + P3′ + P4′ (P2′ folded). Steps (all complete):**

1. **Independent review** of the drafted bundle before canon — DONE, clean.
2. On review-clean **and** git-coordination-clear: #18 — DONE —
   - **(a) Add the P1′ row** to the `## *Appendices* Details` group in
     `01-aat-core/OUTLINE.md`. Precedent/format: the `#deriv-stochastic-non-exit`
     row (the Model-S no-go) — `| A | Derivation | | [#deriv-self-actuation-grounding](src/deriv-self-actuation-grounding.md) | <claim> | conditional |`,
     placed among the other `deriv-*` rows (near `#deriv-sector-condition` /
     `#deriv-stochastic-non-exit`).
   - **(b) Re-sync the stale `#disc-continuity-stance` OUTLINE row**
     (currently OUTLINE.md ~line 106): it still reads "stance axis *over
     $O_t$* … stance lives *in $O_t$* … deployment-level demotion under
     active review" — all overturned by P3′. Update it to: terminal
     *non-objective* invariant; orthogonality *derived* (via
     #deriv-self-actuation-grounding); demotion *resolved against*. (This is
     a required consistency fix, not optional — leaving it makes the index
     contradict the segment.)
   - **(c)** advance P1′ `stage: draft → deps-verified` only if appropriate
     after the review; otherwise it stays `draft` in-canon (a `draft`-stage
     OUTLINE row is legitimate).
   - **(d) Verify the math is fully present in segments** (verify-before-archive)
     → `git mv` these 3 spike files to `spikes/.integrated/` + add a MANIFEST
     note there. Then this integration is complete.

## Provenance / commit map

- `c63d86f` — the spike trail (these 3 files; committed before this move).
- `6b0362f` — `blind pursuer → blind seeker` lexical fix + `TERMINOLOGY-TODO`
  §E + the scope-of-work design doc (unrelated to this arc; same session).
- Commit-1 content (pipeline `\addchap`/`\AlphAlph` fix + appendix
  breadcrumb) was absorbed into the **concurrent spike-routing workstream's
  `31e54e7`** via a shared-index incident — accepted as-is (no history
  surgery); CHANGELOG provenance note owed (session task #13).

## Known follow-ups (out of this integration's scope)

- **Vocabulary sweep (session task #12):** "witness/witnessed" →
  "independent review / attested" (two-tier: *reviewed* = weak/neutral act;
  *attested* = withstood adversarial stress-test; *independent* always
  implied) across these 3 spikes + `spikes/INDEX.md`. Deliberate
  follow-up commit, by decision; the trail still carries pre-sweep wording.
- **`spikes/INDEX.md` path staleness:** its rows still point at the old
  `spikes/spike-*.md` paths (stale after this move). Reconcile when next
  touching INDEX — coordinate with the concurrent spike-routing workstream
  (shared file, collision-prone).
- A concurrent **spike-routing fan-out** workstream commits directly to
  `main` and shares this working tree. Use pathspec-scoped commits
  (`git commit -m … -- <exact paths>`), never bare `git commit` on the
  shared index. This subdir keeps these files out of the churning
  `spikes/` root.
