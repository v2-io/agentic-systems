# Initial Predictions

Audit started 2026-04-25, agent: Claude Opus 4.7 (1M context). First agent using `msc/de-novo-audit-instructions.md` v2 (i.e., the version revised mid-conversation today; see git log on the instructions file). I'm both performing the audit and stress-testing the instructions.

## Priming bleed — disclosed up front

A truly de-novo first encounter is *not* what this audit is. The following sources were already in my context window before I encountered the §4.1 directive to avoid `TODO.md` and `PROPOSALS.md`:

1. **`CLAUDE.md` (auto-loaded by Claude Code).** This is by design and per the new §4.1 step 5. But CLAUDE.md is not a thin orientation file; it's currently a substantive architectural brief running 100+ lines under "What's Settled vs. Open" with ~70 specific commitments named — the (PI) axiom, the 1-anchor-plus-3-theorem characterization, the C-iv scope route, sub-scope α₁/α₂/β partitioning, the BH-identity primary bound, the seven elements of AAD's epistemic architecture, etc. The file functions as a primed model of the corpus. Full segment-level fresh encounter is therefore impossible for an agent reading CLAUDE.md properly; this is a structural feature of the project, not an audit failure.

2. **`MEMORY.md` (auto-loaded user memory).** Even more priming — a full timeline of cycles 2026-04-22 through 2026-04-25 with specific findings (F-V1 through F-V5), specific strategic proposals (SP-21, SP-9), and specific session character notes. This is the largest single source of bleed.

3. **`TODO.md` lines 1-400** read before I noticed the §4.1 directive to avoid it (the directive was added during the same conversation as part of the instructions revision, so I had no chance to honor it on the first pass). I now know the active F-V findings batch in detail, the pending-review spikes from the 2026-04-23/24 cycles, and the architectural recommendations.

What this means for the audit:
- I will *not* claim any of F-V1–F-V5 (or anything mentioned in CLAUDE.md / MEMORY.md / TODO.md as already known) as a "fresh finding." If I encounter the same structural issue in src, I'll note it as confirmation, not surface it as new.
- A truly de-novo finding would have to be something neither CLAUDE.md, MEMORY.md, nor the TODO sections I read have flagged. That's a higher bar than the instructions originally contemplated.
- Where I make predictions below, they're *my* extrapolations from the primed knowledge and from the OUTLINE/FORMAT/NOTATION/LEXICON reading — not naive guesses. I'll mark which is which.

I have *not* read: `PROPOSALS.md`, `msc/SPIKES.md`, `msc/pending-findings-*.md`, `msc/architectural-proposals-*.md`, prior `msc/audit-*.md` files, `msc/spike-*.md` files, any segment file, `bin/` source, ref/ contents.

## Framework topology as I understand it pre-segment-reading

**Four-component structure.** AAD (mathematical core, mature) + TST (software domain, AAD-grounded, independent) + logogenic agents (framework stage, language-constituted) + logozoetic agents (future, morally weighted persistence). Top OUTLINE assembles. CLAUDE.md notes that AAD subsumes prior work (TFT) and that 03/04 are downstream applications.

**Five-phase cycle vocabulary.** Prolepsis/Aisthesis/Aporia/Epistrophe/Praxis. The five phases name distinctions the formalism actually makes; English alternatives flatten them. Cycles are the unit of analysis.

**Six-class agent hierarchy.** Adaptive system → agentic system → actuated agent → self-actuated → logogenic → logozoetic. Each class is a scope narrowing with explicit qualifying properties. Not all narrowings are formally landed: the agentic-system boundary is "in progress" within Section I per the LEXICON ⚙ marker; self-actuated is reserved.

**Three meta-segments as cross-sectional structure.** `#disc-separability-pattern` (positive — separable core / structured repair / general open across seven ladders), `#disc-identifiability-floor` (negative — no-go theorems with AAD as unique escape), `#disc-additive-coordinate-forcing` (constructive — Cauchy-FE on AAD-internal axioms forces coordinates at multiple layers). These are AAD's "epistemic architecture" reframe per Codex/Gemini/Opus convergence (per CLAUDE.md §7).

**The persistence inequality** $\alpha > \rho/R$ is the central result, with several closely related forms (sector condition, contraction template, critical-mass composition, persistence-cost, A2'-sub-scope partitioning). The Lyapunov-template and contraction-metric machinery do most of the heavy lifting.

**Three persistence senses.** Structural / operational / continuity. Distinct dimensions, not a hierarchy. Conflating them is a category error per LEXICON.

**Directed-separation architectural classification.** Class 1 (modular) / Class 2 (fully merged, e.g., LLMs) / Class 3 (partially modular). Section II's exact results apply to Class 1; Class 2 needs the coupled formulation that 03-logogenic-agents is supposed to develop. C-iv route added 2026-04-23 to scope-composite-agent for equilibrium-convergent strategic interaction.

## Predictions about what each component contains

### 01-aad-core (110 segments per CLAUDE.md / OUTLINE numbers)

The OUTLINE reads roughly: Section I (foundations + Lyapunov machinery), Section II (purposeful-agent layer with strategy DAG), Section III (composition under strain), Appendices A (Lyapunov / contraction / additive-coordinate machinery, mostly recent), Appendices B (worked examples).

Concrete predictions about specific segments:

- **`#deriv-discrete-sector-condition`** — appendix-A discrete-time machinery. Given F-V1 (Model S variance gap), I expect to find — when I read this segment under §4.4 prompt 3 (math verification) — that the bound is currently stated as $O((\eta^*)^2)$ in src, and that running the Taylor expansion gives $O(\eta^*)$. *But I shouldn't claim this as a fresh finding.* What I should predict is whether the mechanical fix bundle has actually landed yet — `git log` tells me commit `a6b61fb` says "audit extraction: pending-findings, mechanical fixes, SP-21" so the fix may already be in. I'll need to confirm this against src before making any claim.

- **`#deriv-strategic-composition`** — Section III equilibrium-convergence segment. F-V4 is the sign error in the zero-sum example. Same caveat as above; I'll check src directly. The CLAUDE.md says the F-V4 fix introduced a quadratic action-cost regularization that's flagged for follow-up review. I'll examine that follow-up flag.

- **`#scope-multi-agent` vs `#scope-composite-agent`** — F-V2 contradiction (one excludes adversarial pairs, the other admits them via C-iv). Same caveat.

- **`#scope-developer-agent`** (TST) — F-V5 cross-component integration debt with logogenic-agents Class 2 caveats. Same caveat.

- **`#disc-additive-coordinate-forcing`** — meta-segment, status:discussion-grade, 1-anchor-plus-3-theorem characterization per the 2026-04-23 narrowing of Opus's 5-instance conjecture. I want to verify the segment's own self-characterization is honest, especially the Lyapunov-and-IB-Lagrangian "adjacent family" framing. I expect this to be self-aware.

- **`#deriv-bias-bound`** — new appendix from the 2026-04-24 Gemini pressure-point cycle (Track 1 transport-inequality + Track 2 Fisher-Rao + Attempt E no-go). I want to verify the no-go construction (heteroscedastic-normal counterexample) actually works as claimed and that (PI) is genuinely load-bearing rather than coincidental.

- **`#deriv-graph-structure-uniqueness`** — claims the Markov property of the strategy DAG is *forced* (P3→Markov via CMC theorem) under causal sufficiency. I expect this to be the strongest single claim in Section II. I'll want to confirm the conditioning is really "only causal sufficiency" rather than smuggled additional assumptions.

- **`#result-sector-persistence-template`** — abstract template that several persistence-flavored results instantiate. I'll want to count instances and verify each instantiation actually fits the template's hypotheses, not just superficially.

- **`#scope-agent-identity`** — promoted to formal scope status with the (PI) axiom added. I want to verify (PI)'s motivation is internally coherent and not retroactively grafted.

### 02-tst-core (20 segments per OUTLINE)

I expect the calibration-laboratory framing to be the strongest move (the transfer-assumption table making non-software domains' identification relaxations explicit). I expect the persistence-condition-instantiated-in-software story (`#post-temporal-optimality` grounded by `#result-persistence-condition`) to be tight. I expect some empirical/heuristic-tier segments (`#emp-changeset-size-principle`, `#hyp-exponential-cognitive-load`) to be honestly tier-labeled but possibly underdeveloped relative to AAD-core. F-V5 contradiction with logogenic-agents I'll examine.

### 03-logogenic-agents (7 segments per OUTLINE)

The honest critical claim: directed separation *fails by construction* for LLMs (Class 2). The coupled formulation `X_{τ+} = f_LLM(prompt(X_{τ-}, e_τ))` is proposed in `#def-coupled-update-dynamics` without separation. The "16 of 24 results survive" claim from `#result-section-ii-survival` is the load-bearing positive result; "5 approximate, 2 require modification" classifies the rest. I want to read this carefully — it's where AAD touches present-day reality most directly, and any sloppy bookkeeping is high-impact. I expect to find at least one tension between Section II results being claimed-survived and the actual coupled-formulation derivation. The `#scope-observation-ambiguity-modulation` segment with $\kappa$-based bias-bound is recent (Class 2/3 specific) and depends on the new `#deriv-bias-bound` Track-2 result.

### 04-logozoetic-agents (0 segments)

No segments yet — just OUTLINE pointers to LEXICON and msc/reflections/. Audit scope here is essentially "is the framing of this section coherent?" — I'll skim and move on.

## Predictions about what's open

CLAUDE.md lists explicit "open" items: edge identifiability conditions (resolved in software, open in general); composition laws (existence required, specific forms are sketches); coupled formulation for logogenic agents; causal-IB extension; misspecification cost; tier-switching cost. These are openly named.

What I expect to find that's *not* on that list:
- **Strategic disturbance rate $\rho_\Sigma$ measurability.** Per Opus A from the 2026-04-23 audit, this is genuinely unaddressed. The trajectory guarantee depends on a parameter the framework can't observe.
- **Closure defect $\varepsilon^\ast$ as a runtime-computable quantity.** I suspect the bridge lemma's $\varepsilon^\ast$ is well-defined but operationally intractable to estimate without a reference micro-trajectory.
- **The architecture classification (Class 1/2/3) might smuggle a continuum where the framework asserts a partition.** "Partially modular" is doing a lot of work; if the underlying spectrum is continuous, the binary "exact-vs-approximate" flip at the partition is suspicious.

## Predictions about what's overclaimed

I will look hard at:
- **The "exact" status labels.** Several Section II segments carry status:exact. Per the framework's own convention, exact requires "mathematically validated under stated assumptions," but I expect at least one to leak — e.g., a segment where the formal expression is exact but the discussion makes a discussion-grade claim that bleeds into the headline.
- **The "subsumes" rhetoric in `#deriv-critical-mass-composition` and similar.** When a result is claimed to subsume earlier results as special cases, I want to verify the subsumption is exact (the special case actually drops out cleanly under the limit), not approximate or scope-bounded.
- **The transfer-assumption table for non-software domains.** TST is positioned as a privileged calibration laboratory; non-software domains "inherit under explicit transfer assumptions." I want to see those assumptions actually enumerated, or this risks being a rhetorical move rather than a structural one.
- **The C-iv scope route's universality.** Equilibrium-convergent strategic interaction admits adversarial pairs as composites; but adversarial pairs aren't always equilibrium-convergent (e.g., generic non-zero-sum games per Daskalakis 2018). The CLAUDE.md is aware of this; I want to see the segment itself say it.
- **Class 2 caveats propagation.** F-V5 (cross-component integration debt) is one instance. I expect more instances where the Class 2 scope exit is silently elided in segments that should reflect it.

## What I expect to find most novel and consequential

If the framework lives up to its claims:
- **The persistence condition $\alpha > \rho/R$** as a domain-crossing diagnostic — instantiated identically across control theory, RL, organizations, and software. This is the headline.
- **Acyclicity from temporal ordering** is a genuinely clean derivation if it holds — I'll want to verify P3→Markov under "only causal sufficiency."
- **The satisfaction gap / control regret split** as a 2×2 diagnostic — practically useful if the four corrective-action regimes really are mechanically distinguishable.
- **Detection latency $\Omega((n_{\min}+1)/\varepsilon)$** as an unescapable forced consequence of additive-coordinate-forcing composing with Beta-Bernoulli update (`#deriv-detection-latency`). If the structural-forcing claim is real, this is the strongest single piece of new content in the recent cycles — it explains a phenomenon (stability-induced myopia in persistence-trained agents) without inventing new machinery.
- **The 1-anchor-plus-3-theorem characterization of additive-coordinate-forcing.** If genuinely honest about which layer is identity vs. theorem, this is the meta-segment doing the most work.

## What kinds of findings I expect to surface

Given the priming, I won't surface the F-V findings as fresh. The honest finding-types I might catch:

1. **Math errors not yet caught.** Worked examples I haven't seen audited. The discrete-time appendix has been audited (F-V1); the continuous-time analogs probably haven't been to the same depth. The Kalman-over-Kalman derivation in `#der-interaction-channel-classification` was claimed-verified but I can re-run a simple check.

2. **Status-label drift.** Segments tagged status:exact whose Discussion contains discussion-grade claims that read as load-bearing. F-V findings flagged some of this; I expect there are more.

3. **Cross-segment drift around the (PI) axiom and the C-iv route.** F-V2 caught one instance of C-iv non-propagation. I expect (PI) — added 2026-04-23 — has not propagated everywhere it should.

4. **Frontmatter-vs-content drift.** A `depends:` list missing a slug whose content the segment uses, or listing a slug the segment doesn't actually use. The discipline is mature, but mature code has subtle drift.

5. **Discussion claims that sound structural but aren't grounded.** Per CLAUDE.md's working convention "Gate 2 must probe Discussion claims, not just derivations." I'll look for these specifically.

6. **A genuinely new structural observation.** The richest contribution would be something none of CLAUDE.md, MEMORY.md, the TODO sections I read, or the F-V findings have surfaced. I don't have a specific candidate yet — I expect one or two to emerge after substantial segment reading.

## Reading plan

Order, per §4.1 / §4.2:
1. Section I segments first (leaves of the dependency graph), then Section II, then Section III, then AAD appendices, then TST, then 03-logogenic. Skip 04 (no segments).
2. Use the OUTLINE row order as the topological-sort approximation; cross-check `depends:` per §4.3 before reading.
3. Reflection file per segment (`NN-{slug}.md`, lowercase).
4. Maintain a running outline (`00-running-outline.md`) and a "recently-added structural moves" tracking list (`00-recent-additions.md`) per §5.2.
5. Math-verify worked examples per §5.1.
6. External-citation spot-check at least once per session per §5.3.
7. At rough 80% budget, switch to triage and consult Joseph per §4.6.

Given priming, I'll specifically prioritize segments that *aren't* mentioned in CLAUDE.md / MEMORY.md / TODO — that's where genuinely fresh judgment can land.

## Meta-issue I want to surface to Joseph now

The instructions §4.1 directs the agent to avoid TODO.md and PROPOSALS.md before forming first-encounter judgments. But CLAUDE.md and MEMORY.md (auto-loaded by Claude Code) carry content of equivalent priming density to TODO.md, possibly higher. The §4.1 directive is therefore partially undermined by the project's own auto-load mechanism.

Two ways to resolve:
- **(a)** Accept that auto-load priming is structural, and the "de-novo" framing applies only to the discretionary sources (TODO, PROPOSALS, msc/spike-*, msc/audit-*). This is what I'm going to do for this session, but it lowers the de-novo bar.
- **(b)** Future audits could be invoked with a stripped CLAUDE.md / MEMORY.md to genuinely cold-start. This is operationally awkward but gives sharper de-novo passes.

I'll flag this in the final report under the "instructions stress-test" section.

---

Next file: `00-running-outline.md`. Then begin segment reading at Section I leaves.
