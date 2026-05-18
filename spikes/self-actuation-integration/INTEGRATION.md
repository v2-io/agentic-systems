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

1. **P3′** — edit `#disc-continuity-stance`: land the derived correction
   (negotiated = bare persistence floor; morally-continuous = floor + an
   architecturally-non-revisable continuity clause; stance = choice of
   *terminal non-objective* invariant). Content is already derived and
   stated in P1′ Discussion; this turns that segment's orthogonality claim
   from asserted to *derived*, citing P1′. Do **not** reintroduce the
   refuted "objective-tower" picture.
2. **P2′** — fill the reserved `#self-actuated-agent` class boundary: a
   definition segment defining the self-actuated class via the endogenous
   𝔄 operator, citing P1′. The terminology entry
   `terminology/entries/self-actuated-agent.md` currently says "no segment
   yet formalizes the self-actuation operator" — that becomes false; update
   its pointer (P4′).
3. **P4′** — cross-ref pointers: `#der-orient-cascade` step 5d (𝔄 is its
   internalization, well-formed only under the grounding condition);
   `#form-objective-functional` (single-interface is what makes the no-go
   bite); `#def-agent-spectrum` (the self-actuated boundary); the
   `self-actuated-agent` terminology entry → point at P1′/P2′.
4. **Independent review** of the full drafted bundle (P1′+P2′+P3′+P4′)
   before any of it enters assembled canon. Standing discipline — a new
   conditional no-go entering the framework is independently reviewed, not
   self-certified. (This arc is the reason that discipline exists; honor it.)
5. On review-clean: wire into `01-aat-core/OUTLINE.md` (→ canon) →
   **verify the math is fully present in segments** (verify-before-archive)
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
