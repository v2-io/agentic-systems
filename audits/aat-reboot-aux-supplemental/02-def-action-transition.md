# Supplemental 02 — `#def-action-transition`

*Finder, 2026-09-25. It accompanies `~/src/aat-reboot/scratch/aux/02-def-action-transition.md`. Paths are relative to `~/src/arch/asf/`; line numbers are as of `875e1ac3`. Each note is tagged with the slugs it bears on.*

## 1. Passed checks, for the Working Notes

[#def-action-transition] Please add to the Working Notes of `#def-action-transition`:

- Checked the characterization of C3 ("Markov-of-$M_t$ is forced by *defining $M_t$ as complete*"; "commitments about the *breadth* of the named object") against `01-aat-core/src/deriv-recursive-update.md:18, 22, 175` and `der-recursive-update.md:16, 41`. It holds. C3 is "state completeness", "definitional, not eliminative", from `#form-agent-model`, exactly as this segment says.
- Checked "Without loss of generality, $\Omega$ is taken to be the sufficient state" against the standard state-augmentation construction, where any process becomes Markov once its state includes its history. It holds, and it costs nothing on the $\Omega$ side because `#def-agent-environment` puts no finiteness on $\Omega$. Caveat, from the typed-target spike (`spikes/epistemic-target-ontology/02-typed-predicate.md:57`): the commitment is well-posed only *given $\theta$*, the law index. If $\theta$ is unknown and outside $\Omega$, then $\Omega$ is not Markov marginally from the agent's side, because the past reveals $\theta$.
- Checked the Epistemic Status sentence "paralleling the epistemic opacity of $h$" against `def-observation-function.md` (its atom: the agent knows neither $h$ nor the distribution of $\varepsilon_t$). It holds as a parallel.
- Checked that `depends: [def-agent-environment]` is minimal and complete for the Formal Expression, which uses only $\Omega_t$, $a_t$, $\mathcal A$ and $T$. It holds. The prose references to $h$ and `#def-observation-function` are forward references, which FORMAT sanctions (polish ledger S27).
- Checked that the THREAD-B worry in this segment's Working Notes (gold :60) was resolved by its originating auditor: `audits/AUDIT-WORKING-472913/00-running-outline.md:42`, `10-form-agent-model.md:11–35`. It holds. The segment's claim that the two Markov moves are "independent" is retro-justified, and the $M_t$-side cost lives in `#def-model-sufficiency` as $1 - S(M_t)$. Please annotate gold item :60 "resolved in its own source audit", following the convention the `#deriv-recursive-update` WN uses at :70.

## 2. History

[#def-action-transition]

- **2026-03-11.** The segment first appears as `src/action-transition.md` (`683503b7` / `da54ece7`), with `status: first-principled`. Its Formal Expression and both atoms (action-transition, transition opacity) are verbatim what stands today. The Epistemic Status sentence is also original. The "Closing the loop" and "Uncertainty about $T$ is what makes action non-trivial" Discussion paragraphs date from this era too; they're TFT/ACT-lineage text that has never been reworked. That fits 731548's "legacy language escapees" diagnosis (`audits/audit-731548-FINAL-2026-07-02.md:126`).
- **2026-04-02.** Promoted to `deps-verified` at Gate 1 (`96099515`). It has never gone past `deps-verified`.
- **2026-04-24/25.** Role-prefix sweep to `def-action-transition` (`e6adf9eb`). AF-6 (`CHANGELOG.md:1275`) added `def-action-transition` to `def-observation-function`'s depends, and swapped the OUTLINE rows so action-transition precedes observation-function. The root cause was 584721 F-A0: $h$ takes $a_{t-1}$.
- **2026-04-28/29.** Audit 471203 F3 ("implicit Markov-of-$\Omega$ never named") produced the Markov-of-$\Omega$ Discussion paragraph (`df416564`, "clarify markov properties"). It was verified in `audits/audit-findings-471203.md:369`.
- **2026-05-21.** The summary-attempt sweep expanded the one-sentence summary into the current three paragraphs (`b1f599d4`). The 2026-05-20 source paraphrase, `msc/summary-attempt/003-def-action-transition.md`, said "the lossy observation channel introduced in the previous segment". That was wrong even then; canon replaced it with a slug reference.
- **2026-05-30.** Gold lift (`598631e1`) added the Working Notes block from 10 dedicated reflections plus 472913, 451729 and 963715.
- **2026-07-03.** Audit 731548 reflection 03 (the Kalman tension) and B-3 → SP-30 (not landed).
- **2026-07-04.** Typed-target spike opened (`spikes/epistemic-target-ontology/`). It's the current candidate repair for both atoms.
- **2026-07-16.** Joseph canonicalized the term *transition opacity* (`terminology/decisions/transition-opacity/20260716T050429Z-joseph-canonicalize.md`), executing a 2026-05-04 curation decision. The entry's body gloss carries the "joint opacity" claim that audit 731548 disputes. The name decision doesn't ratify that gloss.

## 3. What I included and excluded, and why

[#def-action-transition]

- I didn't repeat the lifted gold, since he reads it in the segment. The exception is gold item :60, which the aux corrects.
- Not in the aux, as low-yield or mere listings: 542891 (a prediction only), 613842 and 738192 (the segment is named in a batch list with no content), 963715's batch file (it concerns `#scope-agency`'s Pearl dependency), 584721's F-A table (landed as AF-6), and 628417 `batch-01-ontology.md:6–8` (2026-07-20). 628417 restates "double opacity" and the THREAD-B asymmetry as praise, which reflects the gold priming 374162 noted.
- Naming-audit notes from 2026-05-15, not in the aux:
  - 308172 :9: "the current name elides the opacity claim"; the slug names the action machinery, not the opacity.
  - 419628: naming rows #53 and #132.
  - 527914 :25–27: keep the title plain; any vote target is *transition opacity*.

  These matter only if the rewrite renames the segment or splits the atom.
- On equation tags: the gold's §3 disagreement over whether `*[Definition (transition opacity)]*` should be a Postulate is still unresolved, and 731548 :9 sides with the flaggers. I left it out of the aux because the SP-30′ rewrite would recast the atom anyway.
- On the external sources: relata has no markdown for Bar-Shalom & Tse 1974, Åström 1965, Smallwood & Sondik 1973, Littman 2001 PSR, or Klenske 2015 (all paywalled or without a PDF). So the aux lists them without line ranges. `relata fetch barshalom-1974-dual --apply` might retrieve the first, if someone wants it.

## 4. Worries about what the coordinator might miss

- [#def-action-transition] The Working Notes read as a live to-do list, but at least one item (THREAD-B) is closed. The "readers ask" item on the LLM case ("doesn't the LLM case violate transition opacity?") has an answer in the WN itself ($\Omega$ contains the user). Under SP-30′ it becomes a clean *locus* statement instead: the LLM's own-context transition is law-transparent, and the opacity sits in the other agents' law and state.
- [#def-action-transition] "The agent observes via $h$ and acts via $T$" (:41) mistypes $T$: it's the environment's dynamics, with the action as one input. Together with the finder observation that `#example-kalman`'s actions enter only through $h$, this suggests the rewritten loop diagram should show $a$ feeding both $T$ and $h$.
- [#def-action-transition] If Joseph declines SP-30′ and keeps the bare totality reading, the rewrite owes the frame-relative wording (`verify/04-scope-exclusion-verdict.md:57`). If he defers, the minimal honest fix is 731548's disjunctive sentence (`AUDIT-WORKING-731548/03-def-action-transition.md:17`). Either way, "joint opacity … is what creates the need" shouldn't survive as written.
- [#def-action-transition] The learnability/smoothness follow-up in the gold (193847: "$T$ cannot be adversarial white noise") is still unhoused. Under SP-30′ it maps onto the tractability of naming $\theta$, which `02-typed-predicate.md:67` hands to `#def-model-class-fitness`.

## 5. Notes for other segments

- [#def-observation-function] The same SP-30 side effect applies to its atom. The spike also forces a sharpening: the pair $(h, \mu_\varepsilon)$ is never identifiable, so observation-law opacity should be stated on the induced *kernel* $H_\vartheta$ (`spikes/epistemic-target-ontology/02-typed-predicate.md:29`). The known-$h$ branch of the "double opacity" story is underived (`audits/AUDIT-WORKING-374162/01-batch-verification.md:9`). Its WN "candidate scope-clarification" about known-$R$ Kalman is the definitional face of the same tension (`verify/04-scope-exclusion-verdict.md:42`).
- [#example-kalman] Its dynamics $x_{t+1} = x_t + v_t$ don't depend on the action (`example-kalman.md:30`). The action only selects the sensor noise, so this agent is purely active-perception. That's fine for scope, but it's the canonical example, and it doesn't exercise the transition channel that `#def-action-transition` frames as the action channel. Its model laws are also given to the agent, which is the Kalman collision (731548 reflection 03).
- [#scope-adaptive-system] B-3 / SP-30 is the primary site; this segment is a side effect of the same repair.
- [#scope-agency] Condition (4)'s gold already notes it can be restated with Part-I primitives using $T$. Note that the Kalman-type agent satisfies it only through $h$ ($a_{t-1}$ in the observation), so a $T$-only restatement would *exclude* it. Any Part-I restatement needs "$T$ or $h$".
- [#def-chronica] It depends on this segment, which makes `#scope-adaptive-system` transitively depend on actions even though adaptive scope deliberately admits passive observers (584721 `01-section-i-leaves.md:19`; 472913 findings :131 calls the direct omission correct).
- [terminology/transition-opacity] The entry body `terminology/entries/transition-opacity.md:19` should drop "if only $T$ were unknown it could see the world directly", which contradicts the information-loss boundary, and the "joint opacity" sentence, whatever SP-30 decides. `epistemic-opacity.md` calls the three a "constitutive-opacity triad"; 731548 FINAL :130 wants one naming paragraph for it.
- [#der-recursive-update] Gold items there on status drift are annotated resolved (:70). This segment's gold has no such annotations; see §1, last bullet.

## 6. Process and brief feedback

- The brief was clear. The "unintegrated = not reflected in this segment" reading was exactly right here: every material item was *elsewhere* (a proposal, a spike, a later audit, the originating auditor's own later segments), not in the segment's own record.
- The highest-yield move was following gold items back to their source audit's *later* files. The lifted gold froze THREAD-B at first encounter, and the dissolution eight segments later never propagated. Later finders may want to check this for every "strongest item" in a gold block: grep the source dir's running outline for the thread label.
- `memorata-search --joseph` returned task-notification turns (harness-injected "user" turns) ranked as `human-user`. Joseph's actual words turned up only with query phrasing close to his own, and `~/.claude/history.jsonl` gave stable line numbers for provenance. If Joseph cares, the `human-user` class might exclude `<task-notification>` payloads.
- `relata show-markdown` on paywalled keys returns a stalled/needs-document JSON immediately, so the absence of markdown is a quick, definite answer.
- I didn't wait for the sibling aux `01-def-agent-environment.md`, and it didn't exist when I finished. Anything there about the information-loss boundary's "vacuous" rationale overlaps SP-30 (item 2 in my aux).
