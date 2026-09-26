# aat-reboot aux supplemental — 01 `def-agent-environment`

*Written 2026-09-25 by the finder for `#def-agent-environment` (Claude Opus 5.5), for the aat-reboot walkthrough. The coordinator's slim aux is at `~/src/aat-reboot/scratch/aux/01-def-agent-environment.md`. This file keeps what the aux left out, for Joseph's later review and for later finders: passed checks, history, slug-tagged notes, and process feedback. It's untracked by design. Paths are relative to `~/src/arch/asf/`, with line numbers as of `875e1ac3`.*

## Checks that held — please add to the Working Notes of `01-aat-core/src/def-agent-environment.md`

- **Checked that the channel-richness items the segment hands downstream (:27) are actually fixed there. They hold.**
  - $\lvert\mathcal A\rvert \geq 2$ and causal contrast are in `#scope-agency` (`scope-agency.md:25,29`).
  - Residual uncertainty $H(\Omega_t \mid \mathcal C_t) \gt 0$ is in `#scope-adaptive-system`.
- **Checked the Discussion's claim (:43) that the umbrella/tier distinction is documented in the LEXICON's *agent* entry against `terminology/entries/agent.md:18–29`. It holds.** The entry exists (created by SP-24, `04147f7e`) and says the same thing.
- **Checked the cascade-tier labels at :43 against the figure source `01-aat-core/src/img/scope-of-work.tex:187–190`. They hold.** The labels are Adaptive System / Agentic System (+ causal intervention) / Actuated Agent (+ explicit $O_t, \Sigma_t$) / Self-Actuated Agent (+ revises own $O_t$).
- **Checked the agent-spectrum labels at :43 against `def-agent-spectrum.md:27–28`. They hold.** The spectrum is reactive system / adaptive tracker / blind seeker / actuated agent.

## History of the segment

- **2026-03-11, `683503b7` / `da54ece7`.** Created as `src/agent-environment.md`, status `first-principled`, already titled "Agent-Environment Coupling". It defined the agent as "an entity satisfying three conditions", with action-affecting-$\Omega$ as condition 3. The information-loss boundary was the "constitutive commitment". The Discussion's vacuity paragraph is verbatim from this version, and B-3's verifier dates the exclusion prose to it.
- **2026-04-02, `96099515`.** Promoted to `deps-verified` (Gate 1) with `depends: []`. The Formal Expression's $\mathcal C_t$ and $\mathcal A$ usages came later, with SP-24, so Gate 1 was passed before the depends-hygiene problem 731548 flags existed. Nobody re-ran the gate after SP-24.
- **2026-04-16 → 2026-05-15.** Renames, twice over:
  - ACT → AAD → AAT: `41168527`, `08b6f409`;
  - `agent-environment` → `def-agent-environment`: the role-prefix sweep `e6adf9eb`, piloted in `09ace171`.
- **2026-05-21, `1b07dbdd`.** The summary-attempt pilot replaced ¶1–2 with the 144-walker's prose (`msc/summary-attempt/002-def-agent-environment.md`). Per Joseph, "more mental-model-scaffolding than many current segment descriptions". This was the pilot for a 135-segment sweep.
- **2026-05-28, `4e314fd2` (decision) and `04147f7e` (execution).** SP-24, which resolved audit 773921 Finding 1 (passive observers against an action-constitutive root). Path A with a structural reframe: three channels the coupling *has*. Path B (the "Entity" rename) was rejected. The LEXICON umbrella *agent* entry was added. Joseph's decision text is in the `4e314fd2` commit body; the original proposal is in `git show 4e314fd2:PROPOSALS.md` at :434–480.
- **2026-05-28, `34a16b56`.** Section → Part (scrbook hierarchy).
- **2026-05-30, `598631e1`.** Gold lift A1: the WN's "Incidental audit gold" block, sourced from 14 dirs.
- **2026-07-03, `e0e63358`.** Audit 731548 B-3 routed as SP-30.
- **2026-07-04.** The `spikes/epistemic-target-ontology/` arc (commits `76ac5c4d` … `7939df00`).
- **2026-08-12, `48c7f880`.** The boundary-integrity WN section, attributed to "an AISI-facing applications read". The commit body is empty.

## What I put in the aux, what I left out, and why

- **SP-30 got the most room.** It's the only item where rewriting from the segment alone would produce a wrong segment: the vacuity sentence appears three times, and each time it reads as the natural reason for the constitutive commitment. I gave the typed proposal's essentials inline, because the coordinator may have to decide the ontology in the reboot without asf having decided it.
- **I left out the WN gold itself.** He reads it with the segment. I noted only where gold was never routed (193847 F1) and where its only home is this WN (boundary integrity).
- **I left out the SP-24 narrative.** The pilot aux already gave it (CHANGELOG:386–392). I kept only the rejection *reasons* for Path B, since one of the three reasons no longer binds a rewrite.
- **I left out the 963715 metaphysics note** (`audits/audit-findings-963715.md:271`: the boundary "presupposes a certain metaphysics of agency"). The segment's "modeling choice" sentence already answers it, and Bruineberg is the better pointer.
- **I left out the naming-vote reflections**, 308172 and 419628 (both naming-vote cycles, "no theory gold" per `.gem-hunt-trail/gold-lift-sweep-2026-05-30.md:19`), and 527914's thin walk. 527914 argues "boundary" may be more scope-honest than "coupling" as the subject-noun (`AUDIT-WORKING-527914/01-def-agent-environment.md:23`). SP-24 settled on "coupling" to match the title, but the OUTLINE row still says "Agent-environment boundary" (`01-aat-core/OUTLINE.md:23`).
- **I made one judgment call on FINDER-OBSERVED.** The "where is the boundary drawn" synthesis went into ADDITIONAL-NOTES rather than FINDER-OBSERVED, because it's a convergence I noticed, not a failed fact-check.

## Tagged notes for sibling and later segments

- `[def-action-transition, SP-30]`
  - "If $T$ were known, action selection would collapse to plain optimization over a known function" (`def-action-transition.md:14,43`) needs rewording under either SP-30 option. The verifier's side effect A: under bare totality it becomes frame-relative. The typed version turns it into a "three-way collapse map": state transparency kills filtering, law transparency kills learning, both kill adaptation (`spikes/epistemic-target-ontology/02-typed-predicate.md:164`).
  - The segment's own WN gold at :74 already calls the unknown-$h$/unknown-$T$ gloss "slightly circular".
- `[def-action-transition, def-agent-environment]` Actuation-side loss (action as intended vs as executed) has no root in canon. The source is `audits/AUDIT-WORKING-731548/02-def-agent-environment.md:33`. If `#def-action-transition` meant for a stochastic $T$ to absorb actuator noise, one sentence there would settle it.
- `[def-observation-function, SP-30, GA-1, result-mismatch-decomposition]` Three things for this sibling:
  - Under the typed ontology, $\theta_h$ has to be the observation *kernel*, not an $(h, \mu_\varepsilon)$ pair. The pair is never identifiable (02 §2.2), which also exposes the current atom's "the agent knows neither $h$ nor the distribution of $\varepsilon_t$" phrasing.
  - Under unknown observation law, GA-1 over a state-only $\Omega$ is indeterminate (`01-ga1-verification.md` §4, the twin).
  - The WN's "candidate scope-clarification" (known-$R$ Kalman violates the atom) is the thing SP-30's typed version dissolves: the atoms become graded.
- `[def-chronica, scope-adaptive-system, SP-30]` Three things:
  - Because $\mathcal C_t$ contains $o_t$, full observation gives $H(\Omega_t \mid \mathcal C_t) = 0$. That is the whole arithmetic of B-3.
  - A passive observer's chronica (no actions) has an unwritten degenerate form: `AUDIT-WORKING-628417/batch-01-ontology.md:27`; `AUDIT-WORKING-374162/01-batch-ch1-foundations-reflections.md:34`.
  - `#def-agent-environment`'s Formal Expression uses $\mathcal C_t$ without `#def-chronica` in `depends:`.
- `[scope-adaptive-system]` Four things:
  - The same false rationale sits at `scope-adaptive-system.md:16` ("minimal requirements for the … machinery to be non-vacuous"), :37, and :45 ("complete knowledge … solved problem").
  - The God's-eye convention (the predicate is evaluated by the modeler) is in this segment's WN. It becomes where the prior $\pi_0$ lives under the typed version (02 §8.2).
  - THREAD-F's missing temporal quantifier should be written per component: law-warrants decay, state-warrants stand (02 §5.3).
  - `audits/AUDIT-WORKING-628417/batch-01-ontology.md:17` has the sharpest one-liner for teaching this.
- `[scope-agency]` Audit 193847's F1(c): the "proprioception paradox". If $o_t$ carries $a_{t-1}$ cleanly, $P(o \mid do(a)) \neq P(o \mid do(a'))$ holds trivially, so the contrast may need to route *through* $\Omega$. Source: `audits/audit-findings-193847.md:117`. It was never filed in PROPOSALS or TODO.
- `[def-agent-spectrum, def-agent-environment]` Two things:
  - A *reactive system* (model absent or trivial) is an umbrella agent with trivial internal state. Whether it's inside the adaptive scope is left implicit: with no model, there's no mismatch in the model sense. A reader may ask.
  - The spectrum-tetrad naming decision is still open (`msc/decision-briefs-2026-07-15.md:152–161`; `JOSEPH-TODO.md:16`).
- `[der-directed-separation, 03-llm-core scope-channel-collapse, der-class-coercion-via-wrapping]` Two things:
  - The WN conjecture (2026-08-12): boundary permeability and GUC Class 3 may be one fact, and it isn't obvious that wrapping repairs both. Nothing else in the repo tracks it.
  - `#scope-channel-collapse` (sketch) doesn't list `#def-agent-environment` in `depends:`, though it's where the LLM-boundary question the gold keeps raising should land.
- `[example-bandit, disc-exploit-explore-deliberate, der-mood-timescale]` These disagree about where law-content lives. Per 02 §4.3, the bandit's drifting $\mu_i(t)$ are slow *state* (correctly housed), and its $\theta$ is the drift structure. Also, `#der-mood-timescale`'s $\theta_t$ is slow state, while `#disc-exploit-explore-deliberate`'s $\theta$ is law: the same glyph with opposite types (02 §9 item 5).
- `[emp-update-gain]` The escape-standpoint spike proposed a second, shorter "observation present and uninformative ≠ absent" aside there (`spikes/spike-escape-standpoint-axis-2026-07-29.md:141`), in the same family as the "both ends" aside.
- `[03-llm-core]` Audit 584721 Fresh-3: an LLM is Class 2/3 internally, but LLM + tools + memory can be Class 1 at the system level, "depends on where the agent-environment boundary is drawn" (`audits/audit-findings-584721.md:462–468`). The same observation appears in the 471203 extraction (:635).

## Stale or out-of-scope items I noticed

- **The OUTLINE row claim, "Agent-environment boundary"** (`01-aat-core/OUTLINE.md:23`), differs from the segment title, "Agent-Environment Coupling".
- **The WN's "Belongs elsewhere" bullet on Section vs Part drift is resolved.** `34a16b56` (2026-05-28) migrated to Part/Volume, so the bullet could be pruned.
- **`audits/audit-findings-742613.md:241,598`** says the passive-observer tension is "tracked via … PROPOSALS SP-6". SP-24 resolved it on 2026-05-28.
- **`scope-adaptive-system.md:70` (WN)** still records the passive-observer tension with "`#def-agent-environment`'s action-bearing 'agent'". It's resolved, but kept deliberately as a fresh-reader signal.
- **`01-aat-core/src/img/agent-environment.svg`** has pre-SP-24 labels ("Policy", an unconditional action channel), and "Full state" in the environment box.
- **Chapter 1 ("The Coupled Loop") has no chapter-intro segment**, unlike Chapter 2 (`#the-reality-model-intro`). Readers go from the two-sentence Part I stub straight into this definition.
- **The 2026-07-03 transcript** that carries Joseph's "missing noun" words sits under a project-dir name that no longer exists. memorata still finds it.

## Process and tooling notes

- **`relata show-markdown` for an unconverted key ran past a 60-second foreground timeout.** It queued and finished in the background. Launching it in the background from the start would have saved a step.
- **`memorata-search --joseph` often returns agent text that was pasted into Joseph's turns** (subagent reports he relayed). The first several hits for this segment's SP-24 decision were agent prose, not his words. It's worth reading the speaker in the text itself, not just trusting the class label.
- **Every relevant audit working dir postdating the 2026-05-30 lift is unlifted:** 731548 (explicitly not started), 628417, and 374162. For Ch.1 segments, their per-segment or batch files are the likeliest place for gold the WN doesn't have.

## Feedback on the brief

- **It worked well for this segment.** The "unintegrated means not reflected *in this segment*" reading was exactly right. SP-30 is filed against `#scope-adaptive-system`, but its rationale defect sits here three times.
- **Where the rule and the case met:** the ESSENTIAL-REMAINING rule ("files that complete the segment as it stands") gave "none" here, yet the one read I'd actually recommend before rewriting is the SP-30 spike's §§2–3. I put it under ADDITIONAL-SOURCES with a conditional ("if you take up the ontology call"). A finder may want a slot between "must read" and "optional" for "decision packages this segment's rewrite depends on".
- **The instruction to summarize the point of long primaries inline mattered most for SP-30.** Its package is about 600 lines across five files, and a pointer alone would have forced him to open all of them.
