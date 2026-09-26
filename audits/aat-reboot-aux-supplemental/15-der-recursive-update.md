# Supplemental 15 — `der-recursive-update` + `deriv-recursive-update`

*Finder, 2026-09-25, at `875e1ac3`. Companion to `~/src/aat-reboot/scratch/aux/15-der-recursive-update.md`. Notes are tagged with the slugs they bear on, so later finders can grep for theirs.*

## Passed checks (please add to Working Notes)

- `[deriv-recursive-update]` Please add to the Working Notes of `#deriv-recursive-update`: checked the elimination argument and the Doob–Dynkin step (:60–120) as information accounting. Given C3 read as a restriction on the update's accessible information, the conclusion $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ follows. Holds. (731548 17:11 reached the same verdict independently.)
- `[deriv-recursive-update]` Checked Attack 7 (:156–158) against the recursion: an agent storing the full history updates by appending, which is recursive. Holds.
- `[deriv-recursive-update, form-agent-model]` Checked that TFT's stochastic-update triage (PRNG state in $M$; external noise arriving as an event; a genuine kernel) matches the reboot's recorded-randomness move and canon's `deriv-decomposition-uniqueness.md:22` representation. They agree: all three put the randomness in an argument of $f$.
- `[der-recursive-update]` Checked the hybrid jump-flow handling of elapsed time (Attack 6's TFT form). $\Delta\tau$ enters through the flow, so $f$ needs no time argument. Holds; it agrees with 731548 16:14.
- `[der-recursive-update, form-consolidation-dynamics]` Checked that "$\nu_{\text{consol}} \ll \nu_{\text{online}}$" and "sub-state factorization + bounded per-event budget" (body :18, :47) match `form-consolidation-dynamics.md` (scope condition; (N1) :56, (N2) :58). They match word for word.

## History

- `[der-recursive-update, deriv-recursive-update]` Both were created 2026-03-11 from TFT: `.archive/old-tf-02-causal-structure.md` §"The Recursive Update" for the body and `.archive/old-tf-recursive-update-proof.md` for the appendix, the latter at 308 lines.
  - The appendix is close to verbatim with TFT's §§1–3, 5 and 7–8.
  - TFT's §4 was compressed, and its "Necessity of the constraints" paragraph was lost. That paragraph included "Without C2 … still recursive" and the per-constraint dropping analysis that 731548 went looking for (16:18).
- Key commits:
  - `c1d9fcfd` (2026-04-22) added the Derived-vs-Chosen table and reset the stage to draft.
  - `f61e62f0` (2026-04-22) added the Kallenberg footnote.
  - `13fe2423` (2026-04-22) inserted the consolidation paragraph into the body.
  - `1ec89d82` (2026-05-20) moved the stage to claims-verified.
  - The status went exact → conditional in `af92c880` (2026-04-02) and back to exact in `34a16b56` (2026-05-28).
  - `48c7f880` (2026-08-12) annotated the gold's status-drift item as resolved.
- `[der-recursive-update]` The gold's diff-voice item ("Descended from TFT Appendix …", deriv WN :225) is already gone from the body. 731548 17:7 verified this, but the gold line isn't annotated "resolved". It's the same pattern as the gold item at :70.

## What I left out of the aux, and why

- The seven attacks in detail. The coordinator reads the appendix in full, and 731548 plus 451729 vouch that they aren't straw men.
- 731548's "record vs state" duality (16:30). The reboot's history/retention/record trichotomy already *is* that duality, made formal.
- 731548's channel-conversion reframe of external memory (17:15, :23). The reboot already has it: an external artifact read by a probing action is an observation (`history.md`).
- The 471203 "epistemic-architectural, not mathematical" naming seed. 731548 half-endorsed it and warned it's a deflation risk. It's framing, not rewrite material.
- Status-label adjudications from 451729 / 384279 / 742613. They're superseded.

## Worries for the coordinator

- `[the-reality-model, history]` Aux item (c) (information state) partly corrects a phrase that arrived through aux 09(b) ("what stochastic control calls an information state"). That usage matches Kumar & Varaiya's (P2a)-only definition. The gloss the reboot then wrote is the stronger (P2), which needs sufficiency. Please make sure whichever sense is adopted is stated with its definition.
- `[the-reality-model]` Aux (a) and (f) together suggest that commitments 1 and 2 in `the-reality-model.md` could collapse into one ("the store is its own state"). Whether to do that depends on where action-selection lands (`#der-action-selection`, sibling).
- `[retention, def-model-sufficiency]` The lemma in aux (d) is my own derivation. I checked it against Subramanian Prop. 4 and Barnett–Crutchfield App. A Prop. 7, and nobody else has verified it. If it goes into `retention.md`, it needs "future actions set from outside", which `retention.md:17` already assumes.

## Notes for other finders (slug-tagged)

- `[form-consolidation-dynamics]` :20 calls consolidation "a regime of the between-event dynamics $g_M$", but :32 defines it as jumps $f(M_{\tau^-}, e^{\text{replay}}_\tau)$ on pseudo-events. That isn't a flow. The replay draw uses agent randomness, which under the reboot's integrity clause is recorded. The "$\mathcal I(e^{\text{replay}} \mid M_{\tau^-}) = 0$" line (526815 F75, unfixed; aux 09) should also be stated relative to the world, not the draw.
- `[der-action-selection]` The behavioral half of completeness ($a_t$ depends only on $M_t$) is the Doob–Dynkin step again, with the policy's randomness recorded. 731548 17:17 predicted the segment would need to separate choice from integration.
- `[der-directed-separation, form-complete-agent-state]` Recursion of the epistemic sub-store *is* the Class 1 condition (`der-directed-separation.md:36`). `form-complete-agent-state.md:30` applies recursion to the whole $X_t$, which is always available. The Class 3 failure is the sub-store's non-recursion.
- `[form-event-driven-dynamics]` :51 attributes the recursive update to `#post-causal-structure`, a TFT fossil already noted in supplemental 07. Attack 6's event-tuple mismatch sits on this segment's definitions (:24–25).
- `[03-llm-core: def-coupled-update-dynamics, scope-logogenic-agent, disc-m-preservation]` The context is recursive and the effective beliefs are not; see aux (f). `def-coupled-update-dynamics.md:80` cites "the recursive structure" as enabling "all of AAT's recursive-update machinery" and should say which layer it means.
- `[form-composition-closure]` :161, "(A1) Macro AAT structure … with recursive update — Formulation choice (requirement)". By aux (e), a recursive macro-state always exists (take the composite's joint history). The requirement has content only with boundedness.
- `[deriv-recursive-update]` The table row :166 says C3 means "$M_{\tau^-}$ summarizes the agent's relevant past". "Relevant" is sufficiency wording. C3 only needs "everything retained".
- `[deriv-recursive-update]` :115, C2's σ-algebra form "$\sigma(\Omega_\tau) \setminus \sigma(e_\tau)$ is not in $\mathcal I$". A set difference of σ-algebras isn't a σ-algebra. The intended statement is $\mathcal I \subseteq \sigma(\text{past}, e_\tau)$, with no separate $\Omega$ term.

## Feedback on the brief and process

- The brief's "what recursion is *of*" question wasn't in it, and it didn't need to be. The frame "what he needs that the segment can't give" led straight there, because the reboot drafts had moved ahead of canon. The drafts in `~/src/aat-reboot/src/` were the most useful context I had after the segment itself. Pointing future finders to the relevant reboot drafts, as this launch message did, is high-leverage.
- The relata markdown queue was the bottleneck: Barnett was still unconverted at the end. `pdftotext -layout` on the relata PDF was a good stopgap for checking statements, but it doesn't give the markdown line ranges the brief asks for, so I cited PDF pages.
- `memorata-search --joseph` returned only agent pastes and notifications for this topic. For derivation segments inherited from TFT, the archive files are the better history source.
