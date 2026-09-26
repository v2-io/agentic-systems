# Supplemental 05 — `#scope-adaptive-system`

*Finder, 2026-09-25, alongside `~/src/aat-reboot/scratch/aux/05-scope-adaptive-system.md`. Paths relative to `~/src/arch/asf/`; line numbers as of `875e1ac3`. Tags in brackets name the slugs a note bears on, for grep.*

## Checks that passed (please add to the Working Notes of `#scope-adaptive-system`)

- `[scope-adaptive-system]` Checked `depends:` against the Formal Expression. It uses $\mathcal O$, $\mathcal C_t$, $\Omega_t$ and $H$ and nothing from `#def-action-transition`, so omitting that dependency is correct (472913 :6–12 agrees). The transitive dependency through `#def-chronica` stays; see the `#scope-agency` note below on why $\lvert\mathcal A\rvert = 1$ makes that harmless.
- `[scope-adaptive-system, def-observation-function]` Checked 472913's "history-level vs per-step" sharpening (`audits/AUDIT-WORKING-472913/05-scope-adaptive-system.md:21–33`): a per-step-lossy $h$ can still identify a static $\Omega$ over time, so $H(\Omega_t \mid \mathcal C_t) \gt 0$ is strictly different from, and the operative version of, per-step loss. Holds.
- `[scope-adaptive-system, result-mismatch-decomposition]` Checked step 1's "$\mathcal C_{t-1}$ is coarser than $\mathcal C_t$, so uncertainty at prediction time is at least as large" (`result-mismatch-decomposition.md:34`). Holds for averaged conditional entropy (conditioning reduces entropy in expectation).
- `[scope-adaptive-system, example-kalman]` Checked whether canon's flagship continuous example literally fails "$H \gt 0$" under a differential-entropy reading. It doesn't: with $P^- = 4.25$, $r_H = 1$, the posterior variance is about $0.81$, and $\tfrac12\log(2\pi e \cdot 0.81) \gt 0$. The defect is general (unit-dependence), not an error in the example.
- `[scope-adaptive-system]` Checked the Discussion's cascade statement ("agency scope is the intersection of $\mathcal S_\text{adaptive}$ with…") against `scope-agency.md:25`. It's a genuine intersection, as stated.

## History

- 2026-03-12: ACT era. The LEXICON gains an "Adaptive System" entry with a four-condition MECE exclusion list (representation / observation / action choice / residual uncertainty), commit `f8760cdd`. Joseph's scope sketch put passive sensors and strictly chaotic systems out of scope (the March transcript is cited in the aux).
- Before 2026-04-02 there was a single `scope-condition` segment: four conditions, with passive observers excluded as "ACT is a theory of agency". Its excluded list already had "closed-form" and "pure computation" in today's wording, so the false vacuity rationale predates the split. B-3's verifier traces it to `da54ece`.
- 2026-04-02, `13a8bd3a`: split into adaptive ⊃ agency *within* one file, "resolves the passive-tracker inconsistency flagged in three review rounds". `4910931b` aligned the README; the exclusion partition went from four to two, and the representation condition disappeared.
- 2026-04-23, `09ace171`: the naming pilot split the file into `#scope-adaptive-system` and `#scope-agency`.
- 2026-04-25, `e39c17b5`: AF-7 added `def-chronica` to `depends:`, and the OUTLINE was reordered to match.
- 2026-05-21 `b1f599d4` (description upgrade); 2026-05-28 `34a16b56` (Section→Part); 2026-05-30 `598631e1` (gold lift).
- The body text hasn't changed since. The stage `claims-verified` dates from the 2026-04-06 Gate-2 batch (`943128df`).

## Notes for other segments (slug-tagged)

- `[scope-agency]` Passive observers are defined as $\lvert\mathcal A\rvert \lt 2$ (:19, :44). That includes $\lvert\mathcal A\rvert = 0$, which leaves $T$ and $h$ with no action argument. $\lvert\mathcal A\rvert = 1$ is the clean formalization, and it makes the passive observer's chronica the ordinary one with constant action entries. Joseph's 2026-03-12 sketch framed passive observers as "no action choice", which is the $=1$ reading.
- `[deriv-recursive-update]` C2 is attributed to `#scope-adaptive-system` (:18, :48–52), with the argument "if the agent could access $\Omega$ directly, the residual uncertainty condition would be trivially violable". That argument is false under SP-30 (tabular RL: direct access, in scope), and arguably already false for the Formal Expression as written, since the predicate is about the history, not about access. C2's honest source is `#def-agent-environment`'s mediation commitment. It also says "lossy function of $\Omega_\tau$", and for $h$ = identity it isn't lossy. SP-30's side-effect audit didn't list this site.
- `[der-action-selection]` :25 "Under Part I scope ( #scope-adaptive-system) — where $M_t$ is the entire internal state". The scope segment doesn't say this. The likely intended source is `#form-agent-model` / `#form-complete-agent-state`.
- `[def-strategy-dag]` :187 calls strategy revision "the defining feature of an adaptive agent (`#scope-adaptive-system`)". The scope has no strategy content, and admits passive observers with no strategy.
- `[hyp-solicitable-escape, def-mismatch-signal, emp-update-gain]` :44's "zero-information channel is outside AAT's scope entirely" is not implemented by the predicate (aux FINDER-OBSERVED (a)). The conclusion the segment draws from it survives if the zero-information corner is *in* scope but vacuous (the March-2026 position): the targeting premise still can't be repaired by "no signal", since that corner carries nothing to target. Worth rephrasing from "outside scope" to "vacuous" if the predicate isn't changed.
- `[LEXICON adaptive-system]` `terminology/entries/adaptive-system.md` requires a "persistent feedback loop that corrects mismatch" and the five-phase cycle, praxis included. That's inconsistent with passive-observer inclusion and with the predicate. The brief, "Feedback loop + mismatch correction under uncertainty", has the same problem.
- `[scope-composite-agent]` :77 and :85 restate "minimal conditions for adaptive and purposeful machinery to be non-vacuous" and "it observes under residual uncertainty, and at least one action has causal effect". They inherit (d) and any rewrite of the exclusion rationale.
- `[def-agent-spectrum]` :48 says "observations and uncertainty are sufficient" for Part I. It inherits 731548's well-posed-vs-holds point.
- `[spikes/epistemic-target-ontology]` 02 §5.3 (:122) lists "$\inf_t$" among candidate THREAD-F fixes. It would exclude the tabular-RL row the same table marks "in ✓" (decaying warrant), except through the off-support-law loophole. It also says "the agent that fully learns a static MDP exits scope and honestly becomes a planner", which only holds under a pointwise-in-$t$ reading and finite-time identification. With continuous $\theta$ the posterior never becomes Dirac in finite time.
- `[03-llm-core disc-framework-self-diagnostic]` :19 and :35 rest the recursion claim on "the scope condition's universality … any system satisfying #scope-adaptive-system". It inherits whatever the rewrite does to the predicate, but nothing there needs uniformity in $t$.

## What I left out of the aux, and why

- The God's-eye / modeler's-predicate point: it's in the WN, 628417 :17, and aux 01. I only noted that it becomes "prior-relative" via $\pi_0$ (spike 02 §8.2).
- The "Agent" set-element tension: resolved upstream by SP-24, and carried in aux 01 and supplementals 00/01.
- The eq-tag question (`*[Scope (…)]*` has no FORMAT eq-tag): noted in aux 03 via `audit-findings-471203.md:253`.
- 308172 (naming vote, +2 keep on the slug) and 527914/05 (naming notes; "adaptive system is the right outer-scope name… boring terms where the taxonomy is doing work"): both favor the current name, and neither adds a finding.
- Relata: the segment cites nothing, and relata has no Ashby / Duff (BAMDP) / Kaelbling entries with markdown. The 471203 gold's "structural vs dynamics (Ashby) vs optimization (Bellman)" positioning line has no source to anchor it in relata.
- The March MECE list's "irreducible chaos … S(M_t) ≈ 0 for all M, technically in scope but vacuous" category is a second instance of the in-scope-but-vacuous corner. It's in the transcript if the rewrite wants it.

## Worries

- FINDER-OBSERVED (a) and (b) are single-agent and unverified. (b)'s GA-2 point is a direct reading of `NOTATION.md:259` and `result-persistence-condition.md:39`, so it's low risk. (a)'s claim that a constant channel satisfies $H(\Omega_t \mid \mathcal C_t) \gt 0$ is elementary, but whether canon *intends* zero-information to be excluded or vacuous is a design call: March 2026 says vacuous, July 2026 says excluded.
- If SP-30 is adopted, the natural fix for (a) is an informativeness condition. Something like "$\mathcal C_t$ is not independent of $S_t$ for some $t$" would change the predicate's form, and I haven't run it against the quadrant table. It probably interacts with off-support law in the same way.

## Feedback on the brief and process

- Telling me up front that auxes 01–03 already carried SP-30 at length, and naming the three things wanted, was the most useful sentence in the handoff. It pointed me at the consumer audit and the quantifier analysis instead of re-surfacing B-3.
- The memorata `--joseph` search found a March-2026 design record that no repo file carries (the representation condition and the in-scope-but-vacuous corner). For scope segments, pre-repo history seems to be worth a search as a matter of course.
