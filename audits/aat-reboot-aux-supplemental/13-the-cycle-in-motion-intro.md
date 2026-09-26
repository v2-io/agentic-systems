# Supplemental 13 — `the-cycle-in-motion-intro`

*Finder, 2026-09-25, at `875e1ac3`. This is the companion to `~/src/aat-reboot/scratch/aux/13-the-cycle-in-motion-intro.md`. Each note is tagged with the slugs it bears on.*

## Passed checks: please add to the Working Notes of `the-cycle-in-motion-intro`

- `[the-cycle-in-motion-intro, emp-update-gain]` Checked :24's $\eta^\ast = U_M/(U_M+U_o)$ against `emp-update-gain.md:25`. The formula holds. The surrounding tier sentence (:26) doesn't; that's in the aux.
- `[the-cycle-in-motion-intro, def-adaptive-tempo]` Checked :30's $\mathcal T = \sum_k \nu^{(k)}\eta^{(k)\ast}$ against `def-adaptive-tempo.md:21`. The formula holds; the missing conditional status is in the aux.
- `[the-cycle-in-motion-intro, hyp-mismatch-dynamics]` Checked :36's $\lVert\delta\rVert_{ss} = \rho/\mathcal T$ against `hyp-mismatch-dynamics.md:34`. Holds, as the Model-D form.
- `[the-cycle-in-motion-intro, def-mismatch-signal]` Checked :20's $\delta_t = o_t - \hat o_t$ against `def-mismatch-signal.md:32`. Holds.
- `[the-cycle-in-motion-intro]` Checked :42's chapter flow against `01-aat-core/OUTLINE.md:45–54`. Same order, and all nine slugs resolve. Holds.
- `[the-cycle-in-motion-intro, def-adaptive-tempo]` Checked :32's gloss, "the rate at which the agent turns observations into useful corrections", against tempo's units ($[t^{-1}]$, a correction rate; 731548 ledger lvii). Holds. It is *better* than `def-adaptive-tempo.md:13`'s "acquires useful information".
- `[the-cycle-in-motion-intro, result-adversarial-tempo-advantage, result-adversarial-exponent-regimes]` Checked :32's "every adversarial-coupling result in Part III will depend on tempo ratios". Holds for the tempo-advantage family: exponent $b = 2$, $3/2$, or toward $1$ or $1/2$ (`result-adversarial-exponent-regimes.md:16`). "Every" is loose for M4's `#disc-adversarial-coupling-pressure`, which is about architectural class, not tempo ratios. That is minor, which is why it's here and not in the aux.

## History

- `[the-cycle-in-motion-intro]` Created in `91599699` (2026-05-12 16:52) with FE/ES/Discussion subheads. Rewritten to plain chapter prose in `ebaf24dd` (same day) after Joseph's feedback on the chapter intros (quotes in aux 08). `6ba0dcd2` changed the CIY paragraph from apologetic to declarative once `#def-pearl-causal-hierarchy` moved to Part II. `34a16b56`: "Section II" became "Part II". `b46c07a2` (2026-05-30) lifted the gold into the Working Notes. Everything else is mechanical renames and brace sweeps.
- `[the-cycle-in-motion-intro]` The first draft's Working Notes said "the mismatch-signal / decomposition / gain triad is the load-bearing structure of the chapter's middle; tempo is its synthesis; the linear ODE is the bridge to Chapter 4". The rewrite dropped that note; the skeleton it describes is still accurate.
- `[the-cycle-in-motion-intro, emp-update-gain, deriv-fisher-local-update-gain]` Timing detail: the intro narrowed the gain's exact case to Kalman at about 17:00. `9bd22ca` widened canon's exact case to Fisher-local at 21:11 the same day. No one propagated it back.

## What I left out of the aux, and why

- The gold already in the Working Notes (HFT tempo gloss, pipeline figure, "derived given completeness", Pearl-upstream). He's read it. 731548 marks the Pearl-upstream item **resolved** on both prongs: `scope-agency` states the convention inline, and FORMAT has an "Imported external machinery" section (`…/14-the-cycle-in-motion-intro.md:12`). That item in the Working Notes (:66) can be closed with that pointer.
- The retention/readout split of the estimation term. Aux 12 and supplemental 12 carry it; I only pointed at it.
- The Greek phase vocabulary (`TODO.md:75–105`). The intro uses none of it, and the reboot's `the-cycle.md` has already taken a position.
- `[form-event-driven-dynamics, def-chronica]` The ordinal-vs-metric clock seam. Supplementals 04 and 07 carry it.

## Notes for siblings and later finders

- `[emp-update-gain]` Two unrouted 731548 items live in `…/21-emp-update-gain.md`. One is the `type: empirical` deflation (:9). The other is the "must approximate" modal fix, located by the auditor in the *intro*, not in `emp-update-gain` (:5). Also the gullibility dual (:29), and the RL-row prediction about Adam's stale second moments as frozen $U_o$ estimates (:31), called "publishable-scale".
- `[emp-update-gain, deriv-adaptive-gain-dynamics]` Honest-activation R1/R2 (`spikes/spike-honest-activation-2026-09-23/03-derivations.md:13–55`) and the integration plan's item 1 (a possible Vol 1 appendix) bear directly on the gain segment. R5e (:137) quantifies forgetting as a floor under $U_M$, the fading-memory remedy.
- `[def-adaptive-tempo, der-deliberation-cost]` 731548 ledger xli ("interior-work blindness": tempo counts channel events only) is still alive in canon. It is the tempo-side face of the reboot's readout leg.
- `[result-mismatch-decomposition, disc-anti-collapse]` The review (`msc/ch3-calibration-note-review-2026-07-29.md:56`) says `#result-mismatch-decomposition`'s Working Notes (line ~66) already record the zero-aporia isomorphism: the agent sees $\delta_t$, not the split. Also, "active intervention is the agent's only route to estimating the split" is a *candidate* Working Note, not landed body.
- `[def-causal-information-yield]` The stale "Part II Ch.2" pointer (:27) is the same slip as the intro's :40. Both should say Part II Ch.3 (Causal Access), or better, name the chapter instead of numbering it.
- `[persistence-and-limits-intro]` Whoever takes that intro: this intro's "same shape" promise needs the $\alpha$-vs-$\mathcal T$ distinction and the two-condition split, and that intro is where it gets paid. Check whether it does.

## Worries

- `[the-cycle-in-motion-intro]` The intro's confident, fluent register makes (a)–(c) easy to carry forward unnoticed. They read as summaries, not claims. Joseph's rule for intros ("no claims … that aren't substantiated or first claimed in an actual claim segment") is exactly what they miss. If the coordinator writes his Ch.3 intro last, as planned, a mechanical check helps: grep each sentence's quantity or claim against its home segment's current Formal Expression and ES. That catches these.
- `[the-cycle-in-motion-intro, 04-eli-core]` The honest-activation spike is framed for Volume 4. Its R1 is a Part I fact about the gain law, and could be missed if integration routes everything to `04-eli-core`.

## Feedback on the brief and process

- The "intro = mental-model factor, not rewrite target" framing made the job clear. The most useful move for an intro turned out to be checking each preview against its home segment's *current* status, which is quick and gives the coordinator a map of where canon moved. Worth naming in the brief for intro finders.
- Checking the preview claims against canon *at the intro's own commit* (`git show <sha>:path`) was cheap. It separated "stale since" (unintegrated) from "wrong at birth" (finder-observed), which routes differently. That might generalize.
- It helped that earlier supplementals are slug-tagged. Grepping for Ch.3 slugs showed quickly what aux 09, 11 and 12 had already given him, so I could leave out the retention/readout split, the structure on $\mathcal M$, and $U_o$'s type.
