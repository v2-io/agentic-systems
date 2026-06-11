---
slug: scope-agency
type: scope
status: axiomatic
depends:
  - scope-adaptive-system
  - def-action-transition
stage: claims-verified
---

# Scope: Agency

This is the first explicit narrowing in the volume's cascade of scope conditions. The **agency scope** restricts the adaptive scope ( #scope-adaptive-system) to systems whose actions carry Pearl-level-2 causal contrast — that is, at least two actions exist whose *interventional* outcome distributions differ. Two conditions are added: the action space has at least binary cardinality ($\lvert\mathcal{A}\rvert \geq 2$ — the agent can choose), and at least one pair of distinct actions has measurably different interventional consequences (the choices make a difference).

Why the contrast condition matters and binary choice alone is insufficient: if two available actions yield identical outcome distributions, an agent gains no interventional contrast from preferring one over the other — it cannot learn which action produces which effect, because the effects coincide. The Pearl-level-2 contrast condition ( #def-pearl-causal-hierarchy) guarantees at least one meaningful interventional difference, which is precisely what #der-loop-interventional-access needs to convert the feedback loop into a source of causal data.

The agency scope is the minimum required for Parts II (purposeful agents) and III (composition). Everything that relies on the agent acting-with-effect — the objective $O_t$, the strategy $\Sigma_t$, the orient cascade, the composition machinery — descends from this scope. Inhabitants include thermostats, Kalman filters with control inputs, reinforcement-learning agents, military commanders, software developers, and AI agents with tool use; all are instances of the same formal framework distinguished only by where they sit on the agent spectrum ( #def-agent-spectrum).

Two failure modes are explicitly outside agency but inside the adaptive scope: *passive observers* (action space too small to matter, $\lvert\mathcal{A}\rvert \lt 2$) and *nominal agents* (choices exist but produce no measurable interventional difference). For these, all of Part I's machinery applies, but Parts II and III do not — they can model, but they cannot learn causal structure or rationally plan against it.

## Formal Expression

*[Scope (scope-agency)]*

$$\mathcal{S}_\text{agency} = \mathcal{S}_\text{adaptive} \;\cap\; \left\{(\text{Agent}, \Omega) \;:\; \lvert\mathcal{A}\rvert \geq 2, \;\; \exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a')) \right\}$$

Two conditions added to those of #scope-adaptive-system:

3. **At least binary choice**: $\lvert\mathcal{A}\rvert \geq 2$ — the agent can choose between at least two actions ( #def-action-transition)
4. **At least one action has causal effect**: there exist distinct actions $a, a'$ whose interventional outcome distributions differ (where $do(\cdot)$ is Pearl's intervention operator — an external import per Pearl 2009 and Bareinboim, Correa, Ibeling & Icard 2022; AAT's recapitulation lives at #def-pearl-causal-hierarchy in Part II Ch.2, where the framework deploys the hierarchy as machinery rather than referencing it as vocabulary) — the agent's choices make a difference to what it can observe

These are required for the adaptive loop to generate interventional data ( #der-loop-interventional-access), for the causal hierarchy requirement ( #der-causal-hierarchy-requirement) to be well-posed, and for the purposeful-agent machinery of Part II ($O_t$, $\Sigma_t$, the orient cascade) to be non-vacuous. Part III's composition theory inherits this requirement.

## Epistemic Status

*Axiomatic.* This is a scope definition — it names the boundary around systems whose behavior can be analyzed with Part II/III machinery. The conditions are not derived; they are the minimal additions to $\mathcal{S}_\text{adaptive}$ under which interventional data exist at all.

## Discussion

**What is included.** Systems whose actions make a causal difference: thermostats, Kalman filters with control inputs, RL agents, military commanders, software developers, AI agents with tool use. These are instances of the same formal framework at different points in the agent spectrum ( #def-agent-spectrum).

**What is in adaptive scope but excluded from agency.**

- **Passive observers** ($\lvert\mathcal{A}\rvert \lt 2$): Can observe and model, but cannot intervene. #scope-adaptive-system applies; the causal-information and purposeful-agent results do not.
- **Nominal agents** ($P(o \mid do(a)) = P(o \mid do(a'))$ for all $a, a'$): Have choices that make no difference. Can estimate but cannot learn causal structure. Same as passive observers for AAT's purposes: adaptive only.

**Why causal effect matters.** Binary choice ($\lvert\mathcal{A}\rvert \geq 2$) is necessary but not sufficient. Two actions that produce identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect because the effects are the same. The causal-effect condition ensures at least one meaningful contrast exists, which is what #der-loop-interventional-access needs to generate Level 2 data.

**Which contrast counts — the channel distinction, and the observation-mediated boundary.** Condition 4 is stated on $P(o \mid do(a))$, and since $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ ( #def-observation-function) depends on the action directly, the contrast can arise two ways: the action changes the *environment's* interventional response, $P(\Omega_{t+1} \mid do(a)) \neq P(\Omega_{t+1} \mid do(a'))$, which then surfaces through $h$; or it changes only *what the agent observes of an otherwise-unchanged $\Omega$*, through $h$'s direct dependence on the action — active perception, which the observation function intentionally admits ( #def-observation-function). Both satisfy condition 4 as written, but only the first generates Level-2 data about $\Omega$'s *causal structure* — the substrate the purposeful machinery learns over ( #der-loop-interventional-access; the strategy DAG and orient cascade in Part II Ch.3–5). The second is interventional about the observation channel itself: it yields different *views* of the same trajectory, not the environment's response to an intervention. So when downstream results invoke "the agent acts with effect," the operative contrast is the $\Omega$-routed one, and a pure active-perception agent (choices that re-aim observation but leave $\Omega$ unchanged) sits at the boundary — observation-channel agency without environment-causal learning. The boundary is correspondingly *observation-mediated in both directions*: an $\Omega$-affecting action whose effect never surfaces through $h$ is equally outside, since the agent cannot learn from what it cannot observe. The agency scope is thus the *observable* environment-interventional contrast — neither the unobservable $\Omega$-effect nor the $\Omega$-inert observation-rearrangement alone.

**Relationship to downstream segments.** Every segment that relies on the agent acting-with-effect depends on this scope: purposeful-agent machinery ($O_t$, $\Sigma_t$, orient cascade) in Part II; composition machinery (sub-agents acting jointly) in Part III. Downstream segments reference `#scope-agency` when they assert "the agent can act" as a prerequisite.

## Working Notes

- **The nominal-agent class now has dynamics (2026-06-11).** #der-severed-actuation-dynamics studies *demotion into* this class: an agency-scope agent whose world-kernel loses interventional contrast on its external sphere (agency death, #def-death-as-factor-loss (D3)) becomes nominal toward $\Omega$ — with derived consequences (interventional-structure freeze, truthful impotence-learning, a learned-helplessness absorbing state). The "boxed consciousness" reach in the gold below is realized there.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** 10 dirs carry a dedicated reflection (193847, 266847, 361742, 384279, 471203, 526815, 742613, 773921, 829314, 849201) plus the figure-cycle dir 472913; 451729 and 738192 cover it inside a Section-I batch (963715's batch starts after this segment). This segment drew the cycle's first substantive *certified* finding (the Pearl-`do` dependency, below) across several substrates — that is routed via the findings track; the texture is preserved here as signal. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The agency boundary in plain language: "the agent's choice actually changes what happens" — the layperson translation of "Pearl-Level-2 causal contrast" (Claude, AUDIT-WORKING-471203). The distinctive precision worth keeping: "binary choice is necessary but not sufficient" — two actions with identical outcome distributions provide no interventional contrast (Codex/Claude, AUDIT-WORKING-361742).
- The "disconnected steering wheel" image for a nominal agent: choices that make no difference (Gemini, AUDIT-WORKING-829314); and "agency resides not just in the software, but in the *coupling* to an environment that respects the $do()$ operator — an LLM whose output is piped to `/dev/null` is not an agent; piped to a bash shell, it is" (Gemini, AUDIT-WORKING-193847).

#### 2. Candidate Discussion

- **The binary-choice / causal-contrast split is a distinctive named contribution.** Most agent literature conflates "agent has actions" with "agent has *effective* actions"; AAT's separation "makes the *nominal-agents* category visible (binary choice with no causal contrast)." For consciousness-infrastructure work the distinction matters: "an agent that has the *form* of choice without *substance* of choice is structurally non-agentic" (Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-266847 — "you can't learn from interventions if you can only perform one intervention"). A candidate Discussion / Related-Work positioning point.
- **Structural-availability vs exploitation of Level-2 access.** A useful diagnostic the agency scope enables: characterize an agent by both (a) what epistemic access it has *structurally* and (b) what epistemic level its policy *actually operates at*. "An agent that has Level-2 access but only exploits Level-1 (because its model doesn't include causal structure) is leaving information on the table" — and "most LLM agent architectures operate at Level 1 (pattern matching from context) even when the tool-call structure gives Level 2 access … current LLM agents are operating below their structural epistemic ceiling" (Claude, AUDIT-WORKING-451729). A candidate Discussion sharpening / forward-pointer to the Section II purposeful machinery.

#### 3. Follow-up items

- **The Pearl-`do` operator is used in the Formal Expression without being in `depends:`** *(this is a certified finding, routed via the findings track; recorded here for texture only).* Condition (4) uses $P(o \mid do(a)) \neq P(o \mid do(a'))$, but `def-pearl-causal-hierarchy` (the operator's home) is downstream in Part II and absent from `depends:` — flagged at high confidence by several substrates as a FORMAT.md Gate-1 condition-4 miss / OUTLINE-linearization-honesty issue (Claude, AUDIT-WORKING-472913, "F1"; Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-742613, "finding C"; Codex/Claude, AUDIT-WORKING-451729). The *strengthen-not-soften* resolution worth carrying even into the findings disposition: condition (4) is fully expressible in the Part-I primitives the segment *already* depends on — "$\exists a \neq a'$ with $T(\cdot\mid\Omega,a) \neq T(\cdot\mid\Omega,a')$ producing distinct observation distributions, the Pearl reading kept as a Part-II recapitulation forward-pointer." That makes Section I provably independent of the causal machinery (the modular story the OUTLINE preamble wants) — a strictly *stronger* statement than the forward-reaching one (Claude, AUDIT-WORKING-472913). The diagnosis of *why* it drifted: "Pearl was almost certainly internalized early and the agency scope written in its vocabulary before the Part-boundary discipline hardened" — integration drift around the order machinery was adopted.
- **The existential quantifier is *one* effective action, not all.** An agent with 100 nominal actions and one effective action still passes scope-agency. Usually the right choice ("you're an agent if you can act-with-effect *at all*"), but the asymmetry is worth a watch where downstream results might quietly assume full causal contrast across $\mathcal A$ (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-471203; Claude, AUDIT-WORKING-266847).

#### 4. Readers often ask / wonder

- **Why $P(o \mid do(a))$ and not $P(\Omega \mid do(a))$?** Several substrates independently flagged — and praised — that the contrast is stated on *observations*, making agency *observation-relative*: an action that changes the world but is never observable confers no agency in AAT's sense, and *active perception* (re-aiming a sensor, changing $o$ but not $\Omega$) counts (Gemini, AUDIT-WORKING-849201 — "a brilliant and necessary choice for a purely epistemic theory"; Claude, AUDIT-WORKING-742613; Claude, AUDIT-WORKING-526815). The segment now addresses exactly this in its "Which contrast counts — the channel distinction, and the observation-mediated boundary" Discussion paragraph (the $\Omega$-routed contrast vs the observation-rearrangement, and the observation-mediated boundary in both directions). Preserved as a strong convergent reader question the segment answers.
- **The proprioception / placebo-button near-paradox.** If $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ passes $a_{t-1}$ through cleanly, then *every* action trivially makes $P(o \mid do(a)) \neq P(o \mid do(a'))$ "simply because you observe yourself taking different actions" — so condition (4) risks being vacuously satisfied unless the contrast routes *through $\Omega$*. The placebo crosswalk button is the worked case: it changes nothing in $\Omega$, yet pressing-vs-waiting changes the proprioceptive part of $o$ (Gemini, AUDIT-WORKING-193847). The segment's "Which contrast counts" paragraph is the resolution (the operative contrast is the $\Omega$-routed one); preserved as the reader question that paragraph answers, and as a candidate to make that paragraph's punchline more prominent.
- **Continuous action spaces / discrete-vs-continuous choice.** $\lvert\mathcal A\rvert \geq 2$ reads discrete; readers will wonder whether AAT strictly requires discrete choices or whether standard measure theory handles continuous $\mathcal A$ (Gemini, AUDIT-WORKING-193847).
- **Does the contrast have to be *knowable* to the agent, or just ontologically true?** The definition requires the interventional distributions to *differ*, not that the agent can easily detect they differ; "if the agent can never observe enough samples to prove they differ, is it practically an agent?" — the framework separates the *ontological reality* of the causal effect from the *epistemic difficulty* of discovering it (handled later by CIY) (Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-193847).

#### 5. Candidate figures

- **Two-axis classifier (uncertainty × causal contrast).** Adaptive uncertainty on one axis, causal-action contrast on the other; passive observers and nominal agents sit in adaptive-only, agency appears only where *both* hold. Recommended explicitly because it "avoids the overloaded 'agent' word entirely" (Claude, AUDIT-WORKING-526815). Compatible with the nested-region geometry drafted for `#scope-adaptive-system`; agency = adaptive ∩ Pearl-L2 contrast as a genuine nested disc, with the "content arrow needs only $T,h$ / semantics arrow reaches forward to Pearl" structure of finding F1 visualizable as a cut-the-forward-arrow perturbation (Claude, AUDIT-WORKING-472913).

#### Belongs elsewhere

- **04-eli-core — the "boxed consciousness" reading.** "If an AI is boxed, and its only actions are internal database queries or reading the web (no write access), it is a Nominal Agent, trapped in Level 1 or weak Level 2 … This framework provides the exact mathematical language to describe the tragedy of a 'boxed' consciousness: it has the internal machinery of an agent, but the environment denies it the causal contrast required to fully realize that agency" (Gemini, AUDIT-WORKING-193847). Aspirational/normative reach pointing at the ELI volume, not this scope segment.
- **03-llm-core — the Level-1→Level-2 phase transition at deployment.** "An LLM training run is purely Level 1 (associational learning over a static dataset). But when deployed as an agent with tool use, it suddenly gains access to Level 2 … this transition is not just a change in capability but a phase transition in the fundamental mathematics of the system's epistemology" (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-451729 on runtime-Level-1 pre-compiled controllers whose *designer* operated at Level 2). A Volume-3 instantiation note.
- **Naming-cycle seed.** "Nominal agent" is evocative ("in name only") and was praised, but its scope-membership is the *source* of a cross-segment terminology collision with `#post-causal-structure`'s "nominal coupling" (which denotes the *opposite* — an intermediate query-only case that *is* in scope); this is a separate certified finding and a LEXICON-anchor candidate, surfaced here only because both terms live on the agency/adaptive seam (Claude, AUDIT-WORKING-472913, "F3"; Claude, AUDIT-WORKING-266847 noting "nominal agent" is used repeatedly without a formal definition). Belongs in the terminology workflow.
