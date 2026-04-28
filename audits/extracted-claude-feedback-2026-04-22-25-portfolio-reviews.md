# Extracted Claude Strategic-Portfolio & Audit-Meta Reviews — 2026-04-22 / 04-25

**Source model:** Claude Opus 4.7 (1M context) — `claude-opus-4-7`
**Date span:** 2026-04-22 → 2026-04-25
**Sessions consolidated:** 4 portfolio-review / audit-meta-review sessions.
**Triggering prompts:** Variants of "give your thoughts on priorities" / "review the current architectural proposals" / "look over the audit document".

## Why these are consolidated

These are not de-novo *findings* audits — they are **strategic-portfolio reviews**: Claude evaluating the project's TODO, PROPOSALS, and prior audit outputs and recommending ordering/framing moves. Each one produced substantive engagement and concrete project-direction shifts (parallel spike launches, the strengthen-first discipline, the convergent epistemic-architecture reframe, the F-V4 sign-error fix). The verbatim reviewer prose is preserved here because:

- The **reasoning** behind ordering/prioritization choices was load-bearing for what Joseph then did, but not preserved verbatim in the resulting tracking docs.
- Each contains substantive **push-backs against existing framings** that shaped the project's discipline (e.g., 2c4918d4's "elevator-pitch moves can hollow out a theory" that informed O-BP10's deferral; b3f043da's findings-not-subsumed-by-proposals argument).
- 1277a1ac contains **first-hand mathematical verification work** (F-V2, F-V3, F-V4 re-derivation) whose reasoning trail is not preserved in `pending-findings-2026-04-25.md`.

## Note on disposition pattern

In all four sessions, Joseph engaged immediately with substantive follow-up — not "thanks, I'll think about it" but "let's launch the work" / "proceed as you see fit" / "I want you to feel like a co-owner". The reviews were used as direct planning inputs.

---

## Session `b3f043da` — 2026-04-22 morning — TODO/proposals-portfolio review

**Record UUID:** `4a328097-8762-45a0-912f-135f60245290` (line 34, ts `2026-04-22T15:57:38.207Z`)
**Length:** 5,165 chars
**Triggering user message:** Joseph: "Hello! Would you please look over everything pretty thoroughly and then give your thoughts on priorities from TODO / msc/architectural-* msc/pending-findings* ?"

**Disposition.** Push-back review on TODO's "Strategic Architectural Proposals (HIGHEST IMPLIED PRIORITY)" framing. Claude argued that **findings-not-subsumed-by-proposals deserve parallel work, not deferral** — Finding 1 in particular is load-bearing, asserts a residual mechanism that gives identically zero under the segment's own rationality assumptions, and `#orient-cascade` step 4c was just promoted to claims-verified referencing it. Joseph followed with: "Why don't you launch one agent for each of your phase 1 items to spike a solution that is promotion ready (if possible)-- so, for findings 1, 7, 10, and 13. While they work in parallel in the background we can discuss the next things." → multiple parallel strengthening spikes were launched (the F1 spike led to the no-go theorem strengthening at `spikes/spike-finding-1-strengthening.md` that landed in commit `14a6095`).

### Verbatim review content

> I've read the TODO, both pending-findings docs, and the architectural-proposals portfolio carefully, plus sampled `#sector-persistence-template` and the Section II preamble to check what's actually in place.
>
> Here's my honest read. I'm going to push back slightly on the current framing, then give a concrete recommendation.
>
> ## One concern with the current framing
>
> The TODO banner says "Strategic Architectural Proposals (HIGHEST IMPLIED PRIORITY)... Some of these moves are more important than any individual finding." That's defensible for proposals that advance fundamentality — but it papers over a distinction I think matters:
>
> - **Findings that are subsumed by a proposal** (2, 3, 12, 15, partially 5/10/14) — yes, hold for the portfolio decision; local repair is wasted work if the architectural move lands.
> - **Findings that are NOT subsumed** (1, 4, 6, 7, 8, 11, 13) — these are factual/scoping errors in segments, several of them promoted. They don't compete with proposals; they're parallel work. Several are HIGH severity.
>
> Finding 1 in particular is load-bearing: the entire "Detection Principle" section of `#causal-insufficiency-detection` asserts a residual mechanism that, under the segment's own rationality assumptions, gives identically zero. `#orient-cascade` step 4c was just promoted to claims-verified referencing that segment. It's safe for now (the reference is to the covariance test, which survives), but the segment itself is currently advertising a mechanism that doesn't work. This isn't something to hold for a portfolio decision.
>
> ## Recommended ordering
>
> **Phase 1 — close the free wins (one focused session, ~3 hrs).** No portfolio entanglement:
>
> - **Finding 1** (60–90 min). High severity; not subsumed. Repair direction is clear in the doc — demote the ±ρ residual to exploration-rate-gated secondary signal, promote the covariance test to primary. Risk: derivation of the ε·ρ scaling; label as hypothesis if it doesn't close.
> - **Finding 7** (30–45 min). Sharp, contained, not subsumed. Narrow P1 to "committed-state subset."
> - **Finding 10** (15 min). Reclassification is pure accuracy work; fine to do even if O-BP2 later restructures.
> - **Finding 13** (30–45 min). Not subsumed; adds the strict-vs-soft split to the `#strategy-dag` L1-default headline.
>
> **Phase 2 — low-risk editorial/organizing-principle pass (one focused session).** These together raise approachability sharply without touching mathematical core, and the TODO's "smallest-payoff-to-effort" ordering is right:
>
> - **O-BP1** — `#sector-persistence-template` already has the instantiation table carrying the argument. The OUTLINE preamble just needs to match what the segment demonstrates. Absorbs Finding 9.
> - **O-BP6** — localized promotion; grounds Finding 5's partial repair.
> - **C-BP3** — closes Finding 15; strengthens 7 and 14.
> - **C-BP2** — composes with O-BP1; no new theory, just explicit naming.
> - **Finding 4** coordinated with the O-BP1 preamble rewrite.
>
> After Phase 2, a reader encountering AAD sees "one persistence template, one separability-repair posture, recursion across scales, on singular trajectories" rather than a pile of separately-motivated results. That's the biggest identity-clarification move available, and it's ~2 sessions of editorial work on content that already exists.
>
> **Phase 3 — scoping spikes, ordered by scope.** Only after Phase 2:
>
> 1. **G-BP1 spike** (well-scoped already via `spike-gain-sector-bridge-nonlinear.md`). Fixes Finding 2. Decide local vs. architectural.
> 2. **O-BP2 vs G-BP2 comparison spike** — these are genuinely alternatives, not complements. Picking one precludes the other. Don't scope either in isolation.
> 3. **Findings 1+11** compound repair for step 4c — after Phase 1's Finding 1 fix has landed and settled.
> 4. **O-BP4 dedicated spike** (as its proposal already recommends).
> 5. **G-BP3** — largest single move. I'd explicitly stress-test the proposal's own question in the spike: *does the natural-gradient form generalize Section III's bridge lemma, or break it?* Section I is the most load-bearing part of the theory; disruption risk is real.
>
> ## The meta-concern
>
> The 2026-04-21 cycle was execution-heavy (Sessions A–D landed substantial repairs). The 2026-04-22 cycle surfaced 15 findings + 14 proposals — that's a lot of fresh pressure on a theory that just went through convergent tightening. My instinct is Phase 1 + Phase 2 are the right move *now*, then pause for real convergence (and promotion-pipeline work — 46 segments still at `draft`) before the bigger architectural scoping begins.
>
> Phrased as a hypothesis rather than a recommendation: the highest-value thing the next 2–3 sessions could do is probably (a) close the unsubsumed findings, (b) execute O-BP1/O-BP6/C-BP3/C-BP2 as a coherent framing pass, (c) advance promotion on the 11 candidates named at the bottom of TODO — *not* open a major architectural spike yet. The portfolio is a real asset; it doesn't need to be consumed quickly.
>
> What's your instinct on Finding 1's severity assessment? That's the one item where the TODO says you want to review before executing, and it's the gating item for the Phase-1 plan.

---

## Session `2c4918d4` — 2026-04-22 afternoon — proposals ordering review

**Record UUID:** `eec796fe-897b-41c5-9cf5-53316c19ecdf` (line 29, ts `2026-04-22T18:22:04.294Z`)
**Length:** 6,555 chars
**Triggering user message:** Joseph: "Would you please review the current architectural proposals (general theory framing etc.) and any relevant context and give your thoughts on which ones might be most beneficial to the project and in which order roughly?"

**Disposition.** Strategic-portfolio review with substantive push-back on three points: (1) **O-BP10 is tempting but risky — do it after O-BP1, not alongside** ("elevator-pitch moves can hollow out a theory"); (2) **O-BP11 (observability-as-master-variable) deserves a scoping spike designed to *falsify* the unification, not confirm it** (instances may share the word "observability" but not the object — Pearl-level vs. social-epistemic vs. mechanical-dynamic); (3) **G-BP1 could move up** (it fixes a mechanical break, not a framing gap). Joseph engaged with: "Go ahead and proceed with your sequence, but by utilizing agents to carefully and thoughtfully do the actual work which you will then double-check… When an overclaim or something is found, seek first to strengthen the theory, not temper the claim. *IMPORTANT* -- have an agent spike an attempt at the improbable / very difficult if a finding would be important." This exchange seeded the strengthen-before-softening discipline that later became formal in CLAUDE.md.

### Verbatim review content

> I've read through the portfolio (`msc/architectural-proposals-2026-04-22.md`), the evening extensions, and the recommended ordering in `TODO.md`. Here's my honest take — not a reordering for its own sake, but the places I'd nudge or push back on the current sequence, with uncertainty marked.
>
> ## What I think the current ordering has right
>
> The strengthen-cleanups-first → framing-before-structure spine in `TODO.md` is sound. The strengthening cycle has already shown that AAD rewards *integration and naming* more than new machinery (F1 is a no-go from an external theorem; F13's Prop B.7 is the one genuinely new derivation), and the 3:1 "convergent depth over generative breadth" posture argues against pursuing the large structural reorganizations (O-BP11, O-BP4, G-BP3, O-BP16) before the framing layer has compressed what's already there.
>
> ## Where I'd push back
>
> **O-BP10 is tempting but risky — do it after O-BP1, not alongside.** The projection-contraction slogan ("contraction rate exceeds target's drift rate") is the most beautiful single restatement on offer, but elevator-pitch moves can hollow out a theory: they feel clarifying while quietly flattening distinctions that were load-bearing. O-BP1 (template as disturbance-decomposition at scales) does the actual organizing work; O-BP10 is a further compression of O-BP1. If O-BP1 lands first, O-BP10 has something concrete to be checked against — segment by segment, does the "projection defect" reading actually hold, or does it only hold for Section I and have to be stretched elsewhere? Doing them together risks locking in a slogan that O-BP1's application would have refused.
>
> **O-BP11 (observability-as-master-variable) deserves a scoping spike designed to *falsify* the unification, not confirm it.** The instances listed (L1' identifiability, P4, P6, B.2/B.3, κ_processing, loop-interventional-access, shared-intent, TST P6) do share the word "observability," but they may not share the object. Observability of a random variable in a graph (P4, B.2) is Pearl-level; observability of intent to future developers (TST P6) is a social/epistemic phenomenon; observability-dominance's edge-freezing is a mechanical dynamic. The scoping spike should ask "is there a single $\mathcal{O}_t$ object that reduces to each instance under specialization, or are these distinct objects linked only by linguistic overlap?" If the former, this is the most valuable structural move in the portfolio. If the latter, pursuing it would be expensive false unification. The description "deepest available structural insight" is warranted by the pattern — but the pattern being real doesn't entail the unification being tractable.
>
> **G-BP1 could move up.** It's currently at position 9 in the post-evening list, framed as a finish-the-framing-first item. But it fixes an actual mechanical break (Gemini Finding 1, unbounded gradient), not a framing gap. The fix is well-scoped (logit/natural parameters at the update layer; probabilities at the interface), the prior spike `msc/spike-gain-sector-bridge-nonlinear.md` has partial groundwork, and it doesn't entangle with the framing moves above. Fixing a known break before further aestheticizing seems right to me on first principles.
>
> ## Where I'd nudge
>
> **O-BP14 first, not second.** I agree it's highest-payoff-to-effort. But there's a stronger reason than effort: it produces the *artifact* that later moves need. Once derivation-type segments carry "what's chosen vs. derived vs. assumed" tables, O-BP1's claim that the persistence template is the *derivation generator* becomes mechanically checkable (each segment's table should show the template-instantiation as derived). C-BP4 (claim-level statuses) composes naturally as the inline layer to O-BP14's executive-summary layer. O-BP14 is the foundation under several later moves — not merely the cheapest one.
>
> **C-BP1 + C-BP4 might belong earlier than Tier 7-position.** If the convention is established before O-BP14 proliferates, the three-layer tagging and the derivation-table can co-design. If done late, O-BP14's tables will already be written in a format that C-BP1/C-BP4 will want to reshape.
>
> ## Where I'd agree strongly
>
> - **C-BP3 (software as calibration laboratory) is the most honest move available.** 45–90 min, high rhetorical payoff, strengthens rather than weakens TST's claims. Do it.
> - **O-BP6 (identity promotion) is cheap and grounds `#loop-interventional-access`** in a way the Bruineberg/Pearl-blanket positioning doesn't quite reach. Worth doing even if nothing else moves.
> - **O-BP2 and G-BP2 should be scoped together before either is committed to** — they're genuine alternatives about what the unifying object is (rate-distortion vs. variational free energy). The V-medium G-BP2 execution keeps both doors open; that's the right posture until one pass forces the choice.
> - **O-BP15 (comprehensive worked example) is underhyped.** Worked examples are where the theory hits reality; attempting to build one would surface framing gaps that pure framing work hides. Not first, but earlier than "after framing stabilizes" — probably in parallel with the O-BP1 + O-BP10 pass, as a stress test.
>
> ## My rough ordering (with honest uncertainty)
>
> **Clear wins (do these):**
> 1. F18–F21 cleanup
> 2. O-BP14 derivation-table convention
> 3. O-BP6 identity promotion
> 4. C-BP3 software-as-calibration-laboratory
> 5. G-BP1 logit reparameterization scoping spike
>
> **Coordinated framing pass (likely wins, but check):**
> 6. O-BP1 + O-BP8 (template as organizing principle + scope lattice)
> 7. C-BP2 (separability pattern) — composes with O-BP1
> 8. O-BP10 (projection-contraction slogan) — only after O-BP1 has surfaced whether the slogan fits
> 9. C-BP1 + C-BP4 scoped together
>
> **Deeper structural (scope with explicit falsifiability):**
> 10. O-BP11 observability — scoping spike designed to refute first
> 11. O-BP2 + G-BP2 V-strong decision — scoped together
> 12. O-BP15 comprehensive worked example — as stress test during framing
>
> **Long-horizon research agenda:** O-BP3, G-BP3, O-BP4, O-BP5, O-BP12, O-BP13, O-BP16, O-BP7.
>
> ## Core uncertainty
>
> I can't tell from outside the segments themselves whether O-BP11 is genuinely unifying or linguistically over-reaching, or whether O-BP10's slogan actually fits Section III's composition-closure case (where "projection" is present but "contraction exceeding drift" has a different shape). These two are the high-variance moves. The rest of the ordering is more robust to my uncertainty; those two depend on investigations that haven't been done.

---

## Session `2e9a9162` — 2026-04-22 evening — post-strengthening proposals re-review

**Record UUID:** `dd78f4c0-1fe3-428b-b30b-0a0a105cb51f` (line 27, ts `2026-04-22T20:27:43.465Z`)
**Length:** 5,168 chars
**Triggering user message:** Joseph: "Would you please review the current architectural proposals (general theory framing etc.) and any relevant context and give your thoughts on which ones might be most beneficial to the project and in which order roughly?"

**Disposition.** Re-review after the strengthening cycle landed and three independent de-novo audits (Codex/Gemini/Opus) had run. The ranking surfaced the **convergent reframe**: "Three independent audits converged on the same reframe: AAD's distinctive contribution is its **epistemic architecture / organization-of-scope**, not its integration of results. That's unusually strong evidence." Recommended Tier 1 ordering: SP-2 additive-coordinate-forcing verification + a coordinated framing pass (SP-7 + O-BP10 + O-BP1 + SP-3 + SP-4 + O-BP8) treated as one coordinated move not six. Joseph: "Let's proceed with Tier 1 as you see fit. Remember, you are co-researcher, co-discoverer, and co-owner of the theory. Be thoughtful, not mechanical or efficiency-oriented. Attempt the hardest things first…" → the SP-2 framing-pass and the citation-audit cycle that followed were direct outputs.

### Verbatim review content

> I've read through the proposals portfolio, the TODO navigator, and the convergent observations from the three 2026-04-23 audits. Here's my honest assessment of which proposals would most benefit the project, with reasoning.
>
> ## The strongest signal
>
> Three independent audits (Codex, Gemini, Opus) converged on the same reframe: AAD's distinctive contribution is its **epistemic architecture / organization-of-scope**, not its integration of results. That's unusually strong evidence — when three de novo reviews arrive at the same axis independently, it's signal not noise. It shifts what counts as "most beneficial": the framing moves aren't just cheap polish, they're the ones that correctly position what the framework *is*.
>
> ## Recommended ordering (my honest ranking)
>
> **Tier 1 — Load-bearing reframes (highest genuine value):**
>
> 1. **SP-2** — Verify and promote the additive-coordinate-forcing meta-pattern (`#additive-coordinate-forcing`). SP-1 already has three solid instances (chain-confidence-decay, reverse-KL, log-odds). If Lyapunov + IB Lagrangian are genuinely additivity-axiom forced (not just rate-distortion convention), this becomes the framework's deepest organizing principle — on par with `#identifiability-floor` and `#separability-pattern`. The verification spike is the honest gate; if only 3 instances hold up, promote at 3.
>
> 2. **Coordinated framing pass: SP-7 + O-BP10 + O-BP1 + SP-3 + SP-4 + O-BP8** (treat as one coordinated move, not six separate sessions). This incorporates the convergent reframe:
>    - SP-7 reframes the README/CLAUDE.md around epistemic architecture
>    - O-BP10 supplies the one-line object-level slogan ("adaptive system = projection whose contraction exceeds target's drift")
>    - O-BP1 supplies the result-level organizing principle (disturbance decomposition)
>    - SP-3 generalizes the calibration-lab template to a forward-looking scaffold for logogenic/logozoetic
>    - SP-4 elevates `#agent-identity` from scope to architectural postulate (token-level, not type-level)
>    - O-BP8 names the five-tier scope lattice once instead of re-assembling it across segments
>    
>    These are genuinely complementary, and doing them piecemeal would produce inconsistent framing. 2-3 sessions if coordinated.
>
> 3. **SP-6** — Composition-closure honest scoping. The bridge lemma currently overreaches; explicitly scoping it to linear-Gaussian / exponential-family Tier-1 while adopting "AAD-shaped reduction" as the honest general claim is exactly the kind of strengthen-by-scoping move CLAUDE.md's honesty-as-architecture principle calls for. **Best after the citation audit** since `#composition-closure` leans on Khalil/Khasminskii.
>
> **Tier 2 — Approachability extensions (smaller, compose with Tier 1):**
>
> 4. **SP-8** — Dual-edged floor/separability reading. One session. Completes the scope-mapping narrative started by `#identifiability-floor` + `#separability-pattern`. Best after SP-7 lands.
>
> 5. **C-BP1 + C-BP4** (together, not separately) — Three-layer epistemic separation + claim-level statuses. C-BP1 alone is philosophy without enforcement; C-BP4 alone is bureaucracy without purpose. Directly repairs the layer-collapse failure mode that keeps recurring in findings (F23, F25, F12, F14).
>
> 6. **SP-5** — Reader's Path. Incremental per-segment; pairs with the already-landed O-BP14 derivation tables as the "orientation/summary" bookends.
>
> **Tier 3 — Genuine depth, requires scoping:**
>
> 7. **O-BP11** — Observability as master variable. Likely the **deepest** available reorganization. The scoping spike alone is worth doing even if execution is deferred — it would surface what AAD's observability machinery actually is across L1' refutation, P4, P6, B.2/B.3, κ_processing, loop-interventional-access, shared-intent, TST P6. Don't commit to execution without the spike.
>
> 8. **O-BP2 full rewrite (with O-BP1 composition) → Section III pull-up path.** The evening-audit observation that dissolves the Class 2 logogenic problem is genuinely new and genuinely cheap-relative-to-what-it-buys. But tension with G-BP2 needs resolving first.
>
> **What I'd defer with conviction:**
>
> - **G-BP3 (Fisher unification) + G-BP1 full sweep** — Largest single move; Gemini's Riemannian framing strengthens the case but not the tractability. G-BP1 partial already resolved Finding 2.
> - **O-BP3, O-BP4, O-BP5, O-BP15, O-BP16** — Substantive but depend on framing decisions from Tier 1 first.
> - **G-BP2 V-strong** — Paper-writing-time decision per the AI-positioning spike.
> - **O-BP13 (Cox necessity)** — Nice-to-have; worth a 1-2 session spike if curiosity pulls, not otherwise.
>
> ## One honest caveat
>
> My ranking largely agrees with the TODO's recommended sequence but weights Tier 1 items more heavily than "smallest-payoff-to-effort" ordering would. That's deliberate: the convergent reframe is rare enough evidence that I'd prioritize *what it's pointing at* over *what's cheapest to execute next*. If the framing pass feels premature, the TODO's ordering (Phase α quick wins → Phase A citation audit → Phase B SP-2 → Phase C framing) is a reasonable alternative that front-loads hygiene.
>
> Which direction would you prefer to push?

---

## Session `1277a1ac` — 2026-04-25 — meta-review of `audit-2026-04-24-fresh-pass.md`

**Record UUID:** `be496d18-6a6e-4ce9-a6f2-f6cc3baf58e9` (line 57, ts `2026-04-25T20:20:57.970Z`)
**Length:** 6,566 chars
**Triggering user message:** Joseph: "Hello! This is Joseph. Would you mind looking over msc/audit-2026-04-24-fresh-pass.md , which was just created in a previous session? I think we'll want to integrate it into TODO and PROPOSALS (and possibly other top-level / tracking documents), give it all its relative priority, do some surrounding context and verification checks if you feel any are necessary, and potentially launch right into delegating some fixes (if applicable) to task agents."

**Disposition.** Meta-review of the prior session's audit document. Claude's read: "It's a meta-impressive artifact more than a finding-machine: an Opus-4.7 fresh pass that produced 'zero findings,' was corrected by independent Gemini/Codex audits in the same session, and then *honestly absorbed* the corrections with a 'Reading-mode failures' post-mortem. The author (a prior instance of me) explicitly retracts the original frame. The de novo instructions document is downstream of *this exact failure*—it's the 'lessons learned' file for any future audit agent." First-hand verification of F-V2 (`scope-multi-agent.md:71` vs `scope-composite-agent.md:89` adversarial-pairs contradiction), F-V4 (sign-error in `deriv-strategic-composition.md:74-76` — "Given $a_A=1$ and $\partial s/\partial a_B = -1$, B (minimizing $s$) wants $a_B = +1$, not $-1$. Claimed NE $(1,-1)$ has a profitable B-deviation; correct NE under the segment's own dynamics is $(1,1)$"), and F-V3 confirmed-and-already-flagged. Joseph followed: "The prior agent who wrote this audit also helped me to write a very much improved set of audit instructions… Please proceed with whatever verifications and tasks and recommendations you would like or defer decisions with TODO and/or PROPOSALS." → integration into `audits/pending-findings-2026-04-25.md` and B7 architectural proposal. Multiple commits followed.

### Verbatim review content

> Here's my honest read after spending real time with the audit document, the de novo audit instructions, and verification against current src:
>
> ## What this audit document actually is
>
> It's a meta-impressive artifact more than a finding-machine: an Opus-4.7 fresh pass that produced "zero findings," was corrected by independent Gemini/Codex audits in the same session, and then *honestly absorbed* the corrections with a "Reading-mode failures" post-mortem. The author (a prior instance of me) explicitly retracts the original frame. The de novo instructions document is downstream of *this exact failure*—it's the "lessons learned" file for any future audit agent.
>
> So the document has two outputs that matter to us:
> 1. **5 verified findings + 3 partial** (most originating from Gemini/Codex, validated by re-derivation)
> 2. **B7** — a candidate architectural proposal (split composite-agent scope routes into distinct ontologies) that subsumes F-V2 and F-V3
>
> The judgments J1–J10 and bigger-picture B1–B6 are mostly *confirmation that the existing portfolio is on the right track* — they map onto SP-7, SP-9, SP-14, etc. that are already in PROPOSALS.md. Genuinely additive: B7 (new), J2/B1 (sharper "form-shaping" framing for SP-7, additive but not urgent).
>
> ## First-hand verification I've done
>
> I read and re-derived three of the five findings against current src:
>
> - **F-V2 confirmed.** `scope-multi-agent.md:71` ("Adversarial pairs are *excluded*") directly contradicts `scope-composite-agent.md:89` ("Adversarial pairs that admit Nash / CCE convergence via (C-iv) DO satisfy"). Real, unresolved, editorial fix is straightforward.
> - **F-V4 confirmed.** Re-ran the math in `deriv-strategic-composition.md:74-76`. Given $a_A=1$ and $\partial s/\partial a_B = -1$, B (minimizing $s$) wants $a_B = +1$, not $-1$. Claimed NE $(1,-1)$ has a profitable B-deviation; correct NE under the segment's own dynamics is $(1,1)$. Sign error is real. Substantive: the segment is `deriv-strategic-composition` — recently promoted (Gap A/B cycle) and the worked example is one of three places this NE is asserted.
> - **F-V3 confirmed and already partially flagged.** This is the same issue as **F8** in the existing pending-findings (2026-04-22 batch, status "Open. 45–60 min scope-reconciliation; involves Joseph's Option A vs Option B decision"). The audit doesn't surface a new finding here — it surfaces *which* finding has been sitting open and gives B7 as a deeper resolution.
>
> I have **not yet first-hand verified**:
> - **F-V1** (variance-gap math in `deriv-discrete-sector-condition.md`) — audit's re-derivation and numerical sanity check ($\nu=10$ gap ≈ 0.053, $\nu=100$ gap ≈ 0.005, ten-fold → ten-fold) are convincing but I haven't checked the segment's own derivation chain
> - **F-V5** (TST/logogenic-agents integration debt) — flagged with medium-high confidence by the audit because the audit author didn't first-hand read `03-logogenic-agents/`. I should read those segments to confirm before treating it as actionable
> - **P-V1, P-V2, P-V3** (the three partial findings) — moderate effort to verify
>
> ## Proposed routing
>
> | Finding | Type | Landing path | Delegable? |
> |---|---|---|---|
> | F-V1 | Math error | Editorial correction in two segments after re-verification | Yes, after I verify |
> | F-V2 | Cross-segment contradiction | Editorial: rewrite scope-multi-agent §Discussion para about adversarial pairs to defer to C-iv | Yes |
> | F-V3 | Internal tension | **Tied to F8 + B7** — needs your Option A/B decision before edit | No — your call |
> | F-V4 | Math error in worked example | Editorial: replace the zero-sum worked example with corrected version (Φ = a_A + a_B, NE at (1,1)) | Yes |
> | F-V5 | Integration debt TST↔logogenic | Needs first-hand read of `03-logogenic-agents/` first to scope properly | Partial — research first |
> | B7 | Architectural proposal | New PROPOSALS.md §G entry SP-21 — split routes into distinct ontologies | No — needs your scoping |
>
> The three partial findings (P-V1, P-V2, P-V3) are smaller; P-V3 is editorial (one sentence in `hyp-causal-discovery-from-git.md`); P-V1/P-V2 may benefit from a careful re-pass on discrete-vs-continuous accounting alongside F-V1.
>
> ## What I'd recommend doing now (ordered)
>
> 1. **Quick verification batch** — I do first-hand: F-V1's math against current segment text, scan the three partial findings, briefly read `03-logogenic-agents/` for F-V5. ~20 min of my time. This is verification I shouldn't delegate (per the audit instructions §3.1, delegation of comprehension is an anti-pattern).
>
> 2. **Create `msc/pending-findings-2026-04-25.md`** capturing the 5+3 findings with their current-src status and confidence levels — consistent with the dated-pending-findings convention you have for prior cycles.
>
> 3. **Update TODO.md** "Active — Pending Findings" with a new 2026-04-25 batch table.
>
> 4. **Add B7 to PROPOSALS.md §G** as SP-21 with full schema (thesis / merits / scope / findings-subsumed / interactions / effort / risks / status). It interacts with the existing SP-6 (composition-closure consolidation).
>
> 5. **Delegate the mechanical fixes** (F-V1, F-V2, F-V4) to a task agent *after* steps 1–4 — these are isolated editorial corrections that don't need cross-cutting judgment. F-V4 in particular is ~30 minutes for a careful sub-agent: replace the worked example with the corrected $\Phi = a_A + a_B$ version including a verification paragraph.
>
> 6. **Hold F-V3, F-V5, B7 for a conversation with you** — the first two need architectural decisions (Option A vs Option B for C-iii; how to structure the TST/logogenic Class 2 absorption); B7 needs you to weigh whether to elevate it into the active proposal portfolio.
>
> ## One thing I want to flag before acting
>
> The audit author got to "five-plus" findings only because Gemini and Codex re-audited the same material. Your initial instruction to me was to *integrate* the audit, not to re-audit. But the corrected document itself recommends not blindly trusting prior audits — and there's a real possibility there are more findings the *combined* three-agent pass also missed. I don't think running another audit is the right move now (diminishing returns; the cycle has had three passes), but it's worth knowing that "5 verified" is a lower bound on real issues, not a complete list.
>
> Want me to proceed with step 1 (verification batch) and then come back to you before creating the pending-findings file? Or would you prefer I roll steps 1–4 together into one pass and surface the result for your review before delegating the fixes in step 5?

---

