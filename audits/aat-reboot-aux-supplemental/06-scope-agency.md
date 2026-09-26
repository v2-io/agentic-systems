# Supplemental 06 — `scope-agency`

*Finder, 2026-09-25, companion to `~/src/aat-reboot/scratch/aux/06-scope-agency.md`. Paths are relative to `~/src/arch/asf/`; line numbers are as of `875e1ac3`. Each note is tagged with the slugs it bears on.*

## 1. Passed checks — please add to the Working Notes of `scope-agency`

- `[scope-agency, der-loop-interventional-access]` Checked :15 and :47 ("precisely what #der-loop-interventional-access needs … to generate Level 2 data") against that segment's current exact claim. That claim is the *availability* of the interventional-character channel, with identification gated on (C1)–(C3) (`der-loop-interventional-access.md:45`). It holds: the contrast condition is what makes the channel non-degenerate, and the segment never claims identification. `der-loop-interventional-access` doesn't list `scope-agency` in `depends:`, but it reaches it transitively through `der-causal-hierarchy-requirement`, so there is no Gate-1 gap.
- `[scope-agency, FORMAT]` Checked the import parenthetical (:30) against `doc/sop/format.sop.md:92–96`. It holds, and FORMAT's pointer to "`#scope-agency` line 30" is still accurate.
- `[scope-agency]` Checked the Pearl/Bareinboim citation against the relata markdown of Bareinboim et al. 2022 (Def. 3 and Def. 5, :193–217). The segment's use of $do(a)$ as mechanism replacement is consistent. It holds.
- `[scope-agency]` Checked the SP-28 landing (CHANGELOG :370–376 and the recovered SP-28 block, `git show 9a51728f^:PROPOSALS.md` :524–536) against :49. The paragraph matches the recorded landing, including the deliberate non-tightening. It holds.
- `[scope-agency, der-severed-actuation-dynamics]` Checked the 2026-06-11 Working Note against `04-eli-core/src/der-severed-actuation-dynamics.md:17, 37`. That segment does state its demotion against this segment's $\Omega$-routed operative reading. It holds.
- `[scope-agency, def-agent-spectrum]` Checked `#def-agent-spectrum:54`'s "Hafez's agency maps roughly to #scope-agency" against Hafez §4.1 (relata markdown :112–120). It holds as "roughly", with a difference worth adding there. Hafez's *effect* is $I(A;S'\mid S) \gt 0$, state-routed and state-conditioned, and his *choice* is $H(A\mid S) \gt 0$ (policy stochasticity), not cardinality.

## 2. History

- `[scope-agency]` Born 2026-04-01 (`4b4ded10`, "Explicitly scope causal effect into agency") inside `01-act-core/src/scope-condition.md`. Before that, the scope needed only $\lvert\mathcal A\rvert \geq 2$, and the examples included a passive Kalman filter. That same commit removed the passive Kalman and added "Nominal agents". The trigger was a codex review, and Joseph's Option-A decision is quoted in the aux. The next reviewer round surfaced a contradiction with `causal-structure.md` ("zero-coupling … still within scope when $\lvert\mathcal A\rvert \geq 2$"). The implementing agent resolved it by moving zero coupling out and keeping query-only ("nominal") coupling in (session `615ef48a`, message 834). That is the origin of both the four-row coupling taxonomy and the later "nominal" collision.
- `[scope-agency, scope-adaptive-system]` Split out of `#scope-condition` on 2026-04-23 (`09ace171`, naming pilot). Joseph's words (`~/.claude/history.jsonl:9695`): "everything downstream from scope-agency is depending on the agency scope. scope-condition doesn't make any sense."
- `[scope-agency]` Later changes:
  - 2026-05-21: description upgrade (`b1f599d4`).
  - 2026-05-28: the Pearl-import parenthetical (`34a16b56`, from audit 384279 Finding 4, which had rescinded the dependency-violation framing in favour of a "meta-documentation gap").
  - 2026-05-29: the SP-28 paragraph (`484211fb`).
  - 2026-05-30: gold lift (`598631e1`).
  - 2026-06-11: the severed-actuation Working Note (`6da798d3`).

  Audit 384279 judged Ch.1 "clean" (FINAL :175). 731548 reopened it via the layer mismatch, which was then withdrawn as SP-28-held.

## 3. Out-of-scope errors and stale items noticed

- `[der-loop-interventional-access]` The Working Notes (:88) say "passive observers, nominal agents with $\lvert\mathcal{A}\rvert \lt 2$ or no causal effect". That merges the two excluded classes. $\lvert\mathcal A\rvert \lt 2$ is the passive observer; no contrast is the nominal agent.
- `[def-pearl-causal-hierarchy]` :17 attributes Level-2 availability to "the binary action requirement". Per this segment, cardinality makes the query posable, not non-degenerate. A one-clause fix, aligned with verify/05's CIY residue (:32).
- `[def-agent-spectrum, scope-agency]` :58 puts thermostats outside agency. This contradicts `scope-agency` :17 and :40; see the aux.
- `[post-causal-structure, scope-agency]` :40 says agency-scope results apply to query-only coupling, while `scope-agency:49` says the operative reading for downstream results is $\Omega$-routed. The sibling finder for `post-causal-structure` may want this; it's in my aux's FINDER-OBSERVED.
- `[example-kalman, def-causal-information-yield]` `example-kalman` depends on `scope-adaptive-system`, not `scope-agency`, yet it computes CIY, whose interventional contrast is exactly the agency condition. `#def-causal-information-yield` itself depends only on `der-action-selection` and `def-mismatch-signal`, so neither segment declares the agency premise that CIY's interventional contrast presupposes. It's a small Gate-1 question, and I haven't verified it further. `example-kalman` is also the example a $T$-only restatement of condition 4 would exclude.
- `[spike-running-software-agent]` `spikes/tst-ideas-cycle-2026-05-21/spike-running-software-agent.md:59` says statically configured load balancers and gateways "typically *not*" satisfy `#scope-agency`. Their actions plainly change the environment. The spike seems to mean "not learning-agent scope" (`OUTLINE.md:87`). It's only a spike, but if lifted it would repeat the thermostat confusion.
- `[scope-agency, TODO, JOSEPH-TODO]` Three untracked items:
  - SP-28's reserved call (already recorded in the `03-` supplemental);
  - 731548's "normative-layer reconciliation sweep" proposal (`AUDIT-WORKING-731548/07-scope-agency.md:43`), which appears in no tracker;
  - the unbound state quantifier (731548 ledger xiv), which also appears in none.
- `[scope-agency]` 731548 :27 asks whether the framework ever prices the *density* of causal contrast (one effective action versus a controllable manifold). Per-action CIY is the nearest thing. The $\exists$-form scope is the only richness quantity at scope level.

## 4. Reasoning about inclusion

- I led with the two-readings split rather than the Pearl friction. The coordinator already knows the Pearl friction. The split is what would make a rewrite wrong: picking either reading silently breaks canon somewhere, either `#post-causal-structure:40` and the Kalman CIY, or `#der-severed-actuation-dynamics` Result 1.
- Joseph's 2026-04-01 Option-A quote went in ADDITIONAL-NOTES because it is the only record I found of his intent for this condition. It postdates nothing that contradicts it. SP-28's "foundational call he can direct" was never put to him.
- The kernel restatement is my reasoning. I included it because it turns two open items (the $T$/$h$ Pearl-independence fix and SP-28's reserved call) into one well-posed choice, and binds 731548's quantifier at the same time. It is untested; see the caveats in the aux.
- Left out of the aux:
  - the gold lift's already-read items;
  - 527914 and 308172 (naming-cycle reflections; they endorse "agency", "nominal agent" and "interventional contrast" as names, with no new content);
  - 374162's quiz-verification notes (they observe that its quiz answers leaned on WN gold, not the body);
  - 628417 batch-02 (it confirms the paragraph works for a fresh reader);
  - 963715 beyond its cycle note;
  - PROPOSALS D.5 at :186–192 (the "transition into agency" entry process, which lightly touches this scope; not a rewrite input).
- I searched `memorata-search --joseph` for agency / active perception / nominal / "choices make a difference". The only on-point hits were the 2026-04-01 exchange and the 04-23 naming remark.

## 5. Feedback on the brief and process

- The brief's "check what comes up naturally" worked well here. The two biggest items (the canon split, and the 04-01 decision) came from following one citation each, not from a verification sweep.
- A small gap: the parallel finders for `post-causal-structure` and this segment share the coupling taxonomy and the "nominal" collision. The tag convention handles the overlap after the fact, but a one-line "your neighbour is X" in each brief would let each finder say "see aux 07 for Y" instead of both summarizing it.
- `relata show-markdown` prints the document to stdout on first conversion rather than returning immediately as the brief says; the file then appears under `markdown/<key>/content.md` via a symlink. It's harmless, but worth knowing so a finder doesn't dump 1,100 lines into context.
