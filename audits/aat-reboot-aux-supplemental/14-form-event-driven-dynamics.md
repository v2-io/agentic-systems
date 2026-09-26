# Supplemental 14 — `form-event-driven-dynamics`

*Finder, 2026-09-25, alongside `~/src/aat-reboot/scratch/aux/14-form-event-driven-dynamics.md`. Paths are relative to `~/src/arch/asf/`; lines as of `875e1ac3`. Each note is tagged with the slugs it bears on.*

## Checks that passed (please add to the Working Notes of `form-event-driven-dynamics`)

- [form-event-driven-dynamics, def-adaptive-tempo] Checked the Discussion formula $\nu_{\text{eff}} = \sum_k \nu^{(k)}\eta^{(k)\ast}$ (:65) against `def-adaptive-tempo`'s Formal Expression. They are symbol-for-symbol the same object; "identical" holds as a definition. What needs scoping is only the interpretive gloss ("information gained per unit time"), per the aux.
- [form-event-driven-dynamics, der-gain-sector-bridge, deriv-discrete-sector-condition] Checked the fluid-limit algebra $R^\ast_D = \rho/(\nu\eta^\ast c_{\min}) = \rho/\alpha$ (`deriv-discrete-sector-condition.md:97–101`) against `der-gain-sector-bridge.md:43` ($\alpha = \nu\eta^\ast c_{\min}$). They are consistent; holds.
- [form-event-driven-dynamics, NOTATION] Checked units: $\nu^{(k)}$ in Hz, $\eta^\ast$ dimensionless, $\mathcal T$ in $t^{-1}$ (`NOTATION.md:234–238`). So $\nu\eta^\ast$ has the units of $\mathcal T$; holds.
- [form-event-driven-dynamics, deriv-recursive-update] Checked the claim that discrete time is "the special case of uniform-interval single-channel events". It holds for observations. For actions it holds only under zero latency: the discrete form takes the *issued* action, and the stream records completions (aux FINDER-OBSERVED (e)).
- [form-event-driven-dynamics] Checked that the two certified-track items recorded as resolved at WN :105 (the `form-agent-model` dependency; the stale "Section IV"/`AAD-FULL.md` pointer) are still resolved; holds. Also checked that `02-tst-core/OUTLINE.md` still carries the developer-tempo GAP the Discussion points to; holds.

## History

- 2026-03-11 `be0e13d6`: created from TFT's TF-04 (`.archive/old-tf-04-event-driven-dynamics.md`). The event-driven update section went to `recursive-update`, and the channel-specific-$f$ clause was lost on the way.
- 2026-04-02 `75030010`: promoted to `deps-verified` in batch 2.
- 2026-04-25 `937743de`: AF-8 added `form-agent-model` to `depends:` (the definition conditions on $M_{\tau^-}$). AF-13 replaced the dead `AAD-FULL.md` Section-IV pointer with the TST GAP pointer. The commit body records that it searched `02-tst-core/` for the resolved decomposition and found none.
- 2026-04-29 `df416564` then `df72dcec`: the "(Descended from TF-04)" provenance line moved to Working Notes, then was deleted along with other lineage notes.
- 2026-05-21 `b1f599d4`: the two-paragraph opening was added ("multi-channel motivation concrete examples, two-new-measurable-quantities anticipates tempo"). The wording "the effective adaptation rate falls out immediately" dates from here.
- 2026-05-22 `f0c46426`: mechanical `\mathcal{…}` brace sweep.
- 2026-05-30 `b46c07a2`: gold lift A3 (twelve reflection dirs plus two batches).
- 2026-08-12 `48c7f880`: the "Both resolved" annotation (Joseph's AISI-context working-notes commit).

## Reasoning about inclusion

- [form-event-driven-dynamics, def-chronica] Why the aux leads with the rate conversion rather than F4 as filed. F4 and ledger S34 say "no published reconciliation". Their Phase-2 search skipped spikes, TODO and git (`AUDIT-WORKING-472913/15-form-event-driven-dynamics.md:49–50`), which is how they missed `deriv-discrete-sector-condition` and the 2026-05-30 bridge resolution.
  - The coordinator's `history.md:79` promises to reconcile the seam at this segment. If he writes the paragraph F4 proposed, he would re-derive what already exists, and he could still miss the real open decision: whether the agent sees $\tau$, which interacts with his integrity clause.
- [form-event-driven-dynamics] Unlifted reflections checked and left out of the aux:
  - 527914 (naming notes; its content is already in WN);
  - 374162 batch 3 and 628417 batch 3 (they restate known items);
  - 738192 and 419628 (reading lists only);
  - 613842 (only the additivity sentence, which the aux carries).
  - The 963715 and 451729 batches were in the 2026-05-30 lift.
- [form-event-driven-dynamics] The "cadentia" naming seed and the attention-as-budget reach stay in WN. 731548 pushed back on the latter (15:14: it "quietly assumes processing costs are per-event and budgeted, a resource model the framework doesn't have").

## Worries

- [form-event-driven-dynamics, der-recursive-update, form-agent-model] The horn choice (does the history carry $\tau$?) is one decision with several consequences:
  - whether $M_t = \phi(\mathcal C_t)$ holds with $g_M \neq 0$;
  - what "suspended agent" means;
  - whether $\nu$ and $\mathcal T$ are agent-estimable;
  - whether null events and timeouts can be expressed at all.

  If the rewrite treats these separately, they will drift again.
- [form-event-driven-dynamics, def-adaptive-tempo, deriv-tempo-additivity] The additive, isotropic tempo and the single-rate discrete persistence are the only Part I consumers of the multi-channel apparatus. Nothing in Part I uses asynchronous timing *as such*. That partly answers 471203's proportionality question: the channel sum is cashed, but the asynchrony is not.

## Stale or out-of-scope items noticed

- [NOTATION, deriv-discrete-sector-condition, hyp-mismatch-dynamics] `NOTATION.md:263` still lists GA-5 (fluid limit) as a live global assumption. It carries no note that `deriv-discrete-sector-condition.md:187` declares it closed (bounded, with an $O(1/\nu)$ Model-S gap).
- [der-interaction-channel-classification] 526815 F204 is still present: at :54, $\mathcal I(e)\cdot\nu^{(k)} \geq U_{o,B}^{(k)} \cdot c_{\text{floor}}$ compares an information rate with a noise scale. Also, :38 writes $\Omega$ without the $\tau$ subscript the definition carries.
- [form-consolidation-dynamics] :38 writes $\mathcal I(e_\tau^{\text{replay}} \mid M_{\tau^-})$, a different arity from the definition's $\mathcal I(e_\tau)$ with the conditioning inside.
- [der-recursive-update] `01-aat-core/src/img/recursive-update.svg` (hand-authored, no source, referenced nowhere) is titled "Recursive Update and Event-Driven Dynamics". Its caption: "Between events, the model evolves autonomously." It is the sibling's to judge.
- [polish-and-sentiment-ledger S34, audit-findings-472913 F4] Both should be updated to say that the per-event $\leftrightarrow$ per-time conversion is published (`der-gain-sector-bridge`, `deriv-discrete-sector-condition`). What remains is the variable-interval case and the agent-access question.
- [GEM-WORKING-742613] The adjudication at :71 ("No downstream segment found treating it as realized content") is factually wrong; see aux FINDER-OBSERVED (d).
- [def-chronica] The 472913 figure's "$M_t$ $\tau$-blind" label and the chronica WN's awakening story both hold only on the frozen-$g_M$ horn.

## Feedback on the brief and process

- The parent's pointer to F4, and the note in `history.md:79` saying where he intends to reconcile, were the most useful context I had. They told me what the rewrite would reach for.
- The highest-yield search was the reverse direction: appendices and segments whose `depends:` *include* this segment (`deriv-discrete-sector-condition`, `der-gain-sector-bridge`). The brief covers appendices this segment depends on. For a formulation segment, its dependents are where the claims get cashed and corrected. Later finders on formulation segments might grep `depends:` in reverse as a matter of course.
- relata's Khojasteh conversion was fifth in the queue behind a 572-page book, so the aux gives the PDF abstract, not markdown line ranges.
