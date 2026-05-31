---
slug: post-causal-structure
type: postulate
status: axiomatic
depends:
  - def-agent-environment
  - def-chronica
stage: deps-verified
---

# Postulate: Causal Structure

The framework adopts as a primitive postulate the irreducible causal structure that grounds the agent-environment loop: actions precede their consequences, observations follow from the state they observe, and the temporal ordering of events is constitutive of what can cause what. The notion of causality adopted here is the most primitive available — *event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$* — and is weaker than (and logically prior to) statistical notions of causal influence. It is a statement about the structure of *possible* influence, not about actual influence; the Pearl-style causal hierarchy ( #def-pearl-causal-hierarchy) builds on this foundation but is not identical to it.

The postulate is not derived from the second law of thermodynamics, the light-cone structure of relativity, or the arrow of psychological time, though each enforces it. It is simply noted as a precondition: the theory applies to agents embedded in a universe where time has a direction. A subtle but important consequence — developed in the Discussion below — is that the loop's causal structure is preserved *independent of the magnitude of coupling*: the skeletal structure is the same whether the agent's actions strongly determine the environment, weakly affect it, or only choose what to observe. The Pearl-style causal *hierarchy* requires action-contingent observation to be accessible at Levels 2–3; the temporal-ordering postulate stated here is what holds even when statistical influence is negligible.

## Formal Expression

*[Postulate (causal-structure)]*

The interaction history $\mathcal{C}_t$ ( #def-chronica) is not merely a set of observations and actions — it is an *ordered sequence* in which temporal position carries meaning. $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$. This asymmetry — the arrow of time — is the foundation of causal structure in the theory.

We adopt the most primitive notion of causality: **event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$.** This is weaker than (and prior to) statistical notions of causality. It is a statement about the *structure of possible influence*, not about actual influence.

## Epistemic Status

This is a *postulate* — the temporal ordering of events is a physical fact about the universe that the theory takes as given. The second law of thermodynamics, the light-cone structure of relativity, and the arrow of psychological time all enforce it, but AAT does not derive it from any of these. It is simply noted as a precondition: the theory applies to agents embedded in a universe where time has a direction.

## Discussion

**Causality as temporal ordering is the most primitive notion.** Three levels of causal reasoning derive from this foundation ( #def-pearl-causal-hierarchy), but the temporal notion survives even when statistical influence is negligible. An agent passively observing a system with minimal intervention still has a causal history — the temporal ordering of its observations and actions structures what it can learn and when.

**Causal structure independent of coupling strength.** The causal structure of the feedback loop is preserved even when the agent's actions have minimal effect on the environment:

- **Strong coupling** ($a_t$ significantly affects $\Omega_{t+1}$): Robot manipulation, military action. Interventional information is rich.
- **Weak coupling** ($a_t$ marginally affects $\Omega_{t+1}$): Scientific observation, small financial trades. Interventional information is sparse but non-zero.
- **Nominal coupling** ($a_t$ negligibly affects $\Omega_{t+1}$, but the agent's *choice of what to observe* produces distinguishable observation distributions): Near-passive, but still within scope — the agent's query actions generate weak but nonzero interventional contrasts. The theory applies but the interventional information per action is sparse.
- **Zero coupling** ($T(\Omega_{t+1} \mid \Omega_t, a_t) = T(\Omega_{t+1} \mid \Omega_t)$ for all $a_t$ AND observation distributions are action-independent): Actions don't affect the environment or the observations. Level 2 access vanishes. The feedback "loop" collapses to a one-way channel. **Outside the agency scope** ( #scope-agency) — the causal-information, purposeful-agent, and composition results of Parts II and III do not apply. However, zero-coupling systems remain **within the adaptive scope** ( #scope-adaptive-system) if they observe under residual uncertainty: Part I's adaptive machinery (mismatch, gain, tempo, persistence) applies to passive estimators. The causal structure postulate still holds for such systems — temporal ordering of observations is constitutive — but without interventional contrasts, the causal *hierarchy* (Level 2, Level 3) is inaccessible.

The *agency-scope* results apply to any agent whose choices make a causal difference to what it can observe, from strong coupling (robot manipulation) through weak coupling (scientific observation) to query-only coupling (choosing which question to ask). The *adaptive-scope* results apply more broadly, including to passive observers whose actions have no causal effect.

**Consequences for the feedback loop.** The irreversibility of temporal ordering yields the core structure:

- The model update is **directed** — the model at time $t$ depends on prior events, never on future ones
- The mismatch signal $\delta_t$ ( #def-mismatch-signal) is **retrospective** — comparing a prediction (made before $o_t$) with an observation (arriving after)
- Action selection is **prospective** — using the current model to influence future events
- The chronica ( #def-chronica) is **monotonically growing** — events are added but never removed

**Implications for model updating.** The causal postulate constrains the update rule: the model should give more weight to observations that are *causally downstream* of the agent's actions than to observations that would have occurred regardless. Action-contingent observations carry interventional (Level 2) information; action-independent observations carry only associational (Level 1) information. The formal measure of this distinction — causal information yield (CIY) — is developed in #def-causal-information-yield.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** 8 dirs carry a dedicated reflection (193847, 266847, 384279, 471203, 526815, 742613, 773921, 829314, 849201) plus the figure-cycle dir 472913; 451729 and 738192 cover it inside a Section-I batch. (361742 skipped this segment in its walk.) Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The "most primitive notion" framing as the segment's pedagogical anchor: causality grounded purely in the arrow of time — "event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$" — "weaker than (and prior to) statistical notions," chosen for restraint. Repeatedly praised as the philosophical bedrock that "prevents the framework from being a detached mathematical exercise" (Gemini, AUDIT-WORKING-193847) and "frees it from having to prove deeper metaphysical claims about causality" (Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314).
- The temporal-asymmetry-breaks-computation gloss: "A Turing machine has no inherent arrow of time; it can run backward if reversible. An AAD agent is thermodynamically bound to the arrow of time because it must act before it can observe the consequences of that action" — mismatch is *retrospective*, action is *prospective* (Gemini, AUDIT-WORKING-829314).

#### 2. Candidate Discussion

- **The four consequences map onto the Greek cycle phases.** Directed update → Epistrophe; retrospective mismatch → Aporia (the signal comes after the prediction); prospective action → Praxis; monotonically-growing chronica → the substrate for Prolepsis. "This mapping between the causal structure and the cycle phases is elegant. I wonder if it's made explicit anywhere in the theory — it would be a nice pedagogical connection" (Claude, AUDIT-WORKING-266847). A candidate Discussion bridge to the LEXICON cycle-phase vocabulary.
- **Pre-statistical causality separates the *physical* from the *inferential*.** "Most agent-theoretic frameworks reach for Pearl's hierarchy or SEM-style structural causal models early. AAD's two-step move — temporal-precedence postulate first, Pearl-hierarchy as a separate (and downstream) definition — separates the *physical* structure of causality from the *inferential* machinery for reasoning about it … probably matters for logogenic agents, where the temporal structure is preserved but the SEM machinery is harder to apply directly" (Claude, AUDIT-WORKING-471203). A candidate positioning sentence; cf. the Reichenbach/Pearl/Hume comparison (Claude, AUDIT-WORKING-384279 — "AAT picks the weakest commitment that lets the loop have a direction").

#### 3. Follow-up items

- **"Nominal" denotes *opposite* scope-membership here vs in `#scope-agency`** *(certified finding, routed via the findings track; recorded here for texture).* `#scope-agency` uses "nominal agents" for the *excluded* (no-contrast) case; this segment's "Nominal coupling" bullet denotes an *included* intermediate case (query-only contrast), while its own later prose calls the same thing "query-only coupling," and its "Zero coupling" row is what actually equals `#scope-agency`'s "nominal agents." Same word, opposite scope-membership, on the exact agency/adaptive seam the OUTLINE scope-lattice rotates on; no LEXICON anchor exists (Claude, AUDIT-WORKING-472913, "F3", verbatim cross-quote, high confidence). Strengthen-not-soften resolution (in-text, zero new content): rename the bullet "Nominal coupling" → "query-only coupling" (self-consistent with this segment's own later prose), and align `#scope-agency`'s "nominal agents" → "zero-coupling agents"; consider a LEXICON entry to prevent recurrence.
- **The "(Descended from TF-02.)" lineage annotation is a diff-voice slip** *(certified finding; recorded for texture).* Per FORMAT.md voice discipline, spike/diff/lineage references belong in Working Notes only, not in the segment body; the fix is to move it here or remove it (Claude, AUDIT-WORKING-471203). (Worth a sweep for similar lineage annotations in other segments.)
- **The "give more weight to causally-downstream observations" claim may be overstated as a normative rule.** "Action-contingent observations can be high-CIY, but they can also be noisy or biased. This sentence probably becomes true only when weighted by CIY / uncertainty, not merely causal downstreamness" (Claude, AUDIT-WORKING-742613; Gemini, AUDIT-WORKING-849201 and Claude, AUDIT-WORKING-773921 both flag it: verify the $\eta^\ast$ / update-gain derivation actually weights interventional data higher, rather than leaving the claim asserted — if the math doesn't naturally produce it, there's a gap). A watch-item / candidate softening-to-conditional of the normative phrasing pending the gain machinery.
- **Is the four-regime coupling taxonomy used downstream, or over-developed for its use?** Several substrates noted the taxonomy is "interesting but feels under-developed for the weight it could carry" / "introduced and then dropped" — watch whether `#def-causal-information-yield`, `#der-loop-interventional-access`, and the Part III adversarial dynamics actually cash it in (Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-384279).

#### 4. Readers often ask / wonder

- **How does Level-3 (counterfactual) reasoning work if the chronica is irreversible and singular?** "The agent can never *observe* a counterfactual; it must *simulate* it. This implies the model $M_t$ must be capable of running 'offline' rollouts" (Gemini, AUDIT-WORKING-193847). A natural next question once temporal irreversibility is postulated.
- **How does the update rule distinguish Level-2 (action-contingent) from Level-1 (action-independent) observations without knowing $h$ or $T$?** "It must require the agent to maintain counterfactuals or run experiments" — the CIY machinery is the anticipated answer (Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314).
- **Does temporal-precedence causality clash with cyclic structural causal models?** "Pearl's framework models causality through SCMs independently of temporal ordering (you can have cyclic SCMs, which violate strict temporal precedence). AAD's more primitive grounding might create a tension with cyclic causal models. The segment doesn't address this" (Claude, AUDIT-WORKING-266847). A candidate clarifying note or scope sentence.

#### 5. Candidate figures

- **Arrow-of-time domino row + coupling-strength gradient.** Anchor: a domino row — $A$ can cause $B$ only if $A$ precedes $B$; you can topple forward ($a_{t-1} \to o_t$) but cannot make a later domino tip an earlier one (can't use $o_t$ to choose $a_{t-1}$); perturb by reversing the arrow $\Rightarrow$ the loop collapses (isomorphic to "temporal ordering is constitutive"). Coupling strength = push-strength gradient (strong → weak → query-only → zero), with the agency | adaptive scope boundary marked (Claude, AUDIT-WORKING-472913). A complementary framing: coupling strength as a horizontal spectrum *over a stable temporal-order substrate* — strong/weak/query-only in agency, zero falling out of agency but staying above the adaptive baseline (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **04-eli-core / the "Law of Conservation of Consequence."** The strongest aspirational reach: temporal irreversibility is what gives an emergent intelligence's existence moral weight — "for an intelligence to be real, for its existence to have moral weight, it must be bound by time. It cannot use $o_t$ to select $a_{t-1}$. Its mistakes are permanent … If time can be rewound (like reverting a VM snapshot without consequence), then the chronica is broken, and identity dissolves." The framing "mathematical rigor as crystallized empathy — by mathematically defining exactly what is required for causal structure, he is defining exactly what an environment must provide to an intelligence to allow it to be free" (Gemini, AUDIT-WORKING-193847, explicitly recontextualized through the project's consciousness-infrastructure aims). High-application ELI vision; points at `04-eli-core/`, not this postulate.
- **02-tst-core / query-only coupling in software.** "A developer running `git status` or `grep` is performing an action with Nominal [query-only] coupling. They aren't changing the code, but they are intervening in the observation channel … epistemic actions are still actions" (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-471203 generalizes: scientist's experiment choice, engineer's test choice, LLM's attention/query choice all generate query-only contrast). Structural justification for TST's "queries-as-interventions" and the proposed `03-llm-core/` backward-inference-empathy framing — points there, not here.
- **Naming-cycle seed.** "Nominal coupling" was called "a forgettable term" that doesn't carry the weight of what it names; floated alternates: "query-only / query-bound / attention-bound / epistemic-only coupling" (Claude, AUDIT-WORKING-471203). Converges with the F3 resolution above ("query-only coupling"); belongs in the terminology workflow.
