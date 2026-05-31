---
slug: form-agent-model
type: formulation
status: robust-qualitative
depends:
  - def-agent-environment
  - def-observation-function
  - def-chronica
stage: deps-verified
---

# Formulation: The Reality Model

The agent's internal representation of how the world works is committed to a specific form: $M_t = \phi(\mathcal C_t)$ — a many-to-one compression of the chronica into a model space $\mathcal{M}$. This is named honestly as a formulation choice rather than a derived result: alternative formulations exist (history-based policies that map $\mathcal C_t$ directly to actions without an explicit model state), but AAT commits to analyzing agents as carrying a state object $M_t$ that mediates between history and future action. $M_t$ is the substrate of prolepsis — the object from which predictions are generated and against which observations are compared.

The compression is many-to-one *by design*: multiple distinct histories may produce the same model state, and that is the essential function of the model — retaining what matters and discarding what does not. The formalism is deliberately agnostic about *how* an agent realizes $M_t$: a Kalman filter holds a state estimate plus covariance matrix; a reinforcement-learning agent holds a value function; a developer holds a mental model of a codebase; a language-model agent holds its context-window contents plus retrieved memory. The formalism asks only that $M_t$ exist as a well-defined object that the agent's policy can condition on.

The load-bearing commitment carried by the notation is the **completeness assumption**: by writing $M_t = \phi(\mathcal C_t)$, AAT assumes $M_t$ captures *everything* the agent retains from its history. Anything not in $M_t$ is, by construction, lost to the agent. This is what makes $M_t$ the complete epistemic substate rather than merely one component of a richer internal representation. Whether $M_t$ retains *enough* information for adaptive work is a separate question, taken up in #def-model-sufficiency. The formalism accommodates degenerate cases by allowing $\mathcal{M}$ to range from trivial (a PID controller's $M_t$ retains only error signal and its integral/derivative, with no predictive capability) to rich (full world model). The impoverished end of this range lands in the "blind seeker" region of the agent spectrum ( #def-agent-spectrum).

## Formal Expression

*[Formulation (agent-model)]*

$$M_t = \phi(\mathcal{C}_t)$$

where:
- $\phi: \mathcal{C}^\ast \to \mathcal{M}$ maps interaction history to model space $\mathcal{M}$
- $\mathcal C_t = (o_1, a_1, \ldots, o_t)$ is the chronica ( #def-chronica) — the complete record of agent-environment interaction
- $\mathcal{M}$ is the space of possible models the agent can hold

The mapping $\phi$ is a many-to-one compression: multiple distinct histories may produce the same model state. This is not a deficiency — it is the essential function of the model: retaining what matters and discarding what does not.

## Epistemic Status

*Robust qualitative.* This is a *formulation* — a representational commitment, not a derived result. We choose to analyze agents as maintaining a state object $M_t$ that mediates between history and future action. Alternative formulations exist (e.g., history-based policies that map $\mathcal C_t$ directly to actions without an explicit model). The formulation is justified by its analytical utility: it enables the information bottleneck analysis ( #form-information-bottleneck), the mismatch decomposition ( #def-mismatch-signal), and the gain principle ( #emp-update-gain). The formulation is robust — any agent that conditions its actions on retained information can be described this way — but the specific commitment to a complete, compressed state $M_t$ is a modeling choice, not a derivation.

## Discussion

**$M_t$ is the epistemic substate.** It captures "what the agent believes about reality." Different agents realize $M_t$ differently: a Kalman filter holds a state estimate and covariance matrix; an RL agent holds a value function; a developer holds a mental model of codebase architecture; an LLM agent holds its context window contents plus retrieved memory. The formalism is agnostic to the realization — it asks only that $M_t$ exist as a well-defined object that the agent's policy can condition on.

**Completeness assumption.** By writing $M_t = \phi(\mathcal C_t)$, we assume that $M_t$ captures everything the agent retains from its history. Any information not in $M_t$ is lost to the agent. This is what makes $M_t$ the complete epistemic substate, not merely one component of a richer internal representation. Whether $M_t$ retains *enough* information is the subject of #def-model-sufficiency.

**Degenerate cases.** A PID controller's $M_t$ is degenerate — it retains only the error signal and its history (integral, derivative), with no predictive capability beyond extrapolating recent trends. It occupies the "blind seeker" region of the agent spectrum ( #def-agent-spectrum): its $O_t$ (setpoint) is clear but its $M_t$ is too impoverished to support the adaptive dynamics of Part I. The formalism accommodates this by allowing $\mathcal{M}$ to range from trivial (scalar) to rich (full world model).

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14 ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical/generative material kept separate from certified theory-fix findings. **Coverage:** 11 of the 14 contributing dirs reached a digested reflection on this segment (193847, 266847, 471203, 526815, 613842, 742613, 773921, 829314, 849201, 472913, 527914) plus the 451729 batch-02 and 963715 batch-09–13 batched reflections; 361742 names "form-agent-model" only as a naming companion to a downstream segment (no direct reflection). Substrate attribution inferred from voice where not explicit.

#### 1. Candidate Brief prose / pre-prose

- **The many-to-one map as "equivalence class of histories."** Repeatedly singled out as the segment's clarifying move: the model is "the equivalence class of histories that produce the same predictions" — discarding irrelevant information is *productive, not impoverished* (Claude, AUDIT-WORKING-266847; Gemini, AUDIT-WORKING-849201 — "many-to-one *by design*"). A Feynman-grade gloss candidate for the Brief.
- **"$M_t$ is a simulator, not an archive."** Reading "prolepsis" forward: the only reason to compress the past is to predict the future; $M_t$ is a forward-looking engine, not a memory bank (Gemini, AUDIT-WORKING-849201; same image at Gemini, AUDIT-WORKING-193847 — "the chronica is pure past, the model is the bridge built out of that past, facing strictly forward").

#### 2. Candidate Discussion

- **Completeness is tautological-relative-to-retention, and that is the honest move.** Several substrates converge that the segment's strength is making completeness "we assume $M_t$ captures everything the agent *retains*" (retains, not *needs*), so completeness is definitional and the substantive "is what's retained *enough*?" question is explicitly forwarded to `#def-model-sufficiency` (Claude, AUDIT-WORKING-472913 — frames this as the framework "discharging a cost by definition *and naming where the cost went*," the exemplary case). Candidate Discussion sharpening of why the completeness framing is not sleight-of-hand.

#### 3. Follow-up items

- **Where do priors / pretrained weights / innate architecture live?** Three substrates independently flag that the completeness framing does not explicitly place initial priors, pretrained parameters, or inherited model-class structure — for an LLM, "model quality is mostly in pretrained parameters, not only context-window contents plus retrieved memory." Candidate clarification (not yet a finding): write $M_t = \phi(M_0, \mathcal C_t)$, or state that $M_0$ / the model class is absorbed into $\phi$ and $\mathcal{M}$, so "complete epistemic substate" stays compatible with pretrained/innate structure (Claude, AUDIT-WORKING-742613; Gemini, AUDIT-WORKING-849201; Gemini, AUDIT-WORKING-829314).
- **Chronica-ordering shorthand.** The bullet writes $\mathcal C_t = (o_1, a_1, \ldots, o_t)$, looser than `#def-chronica`'s precise interleaved order $(o_1, a_1, o_2, \ldots, a_{t-1}, o_t)$; flagged as probably-harmless shorthand but worth tightening since decision-time order matters and this lands right after `#def-chronica` (Claude, AUDIT-WORKING-526815).
- **PID "too impoverished" reads slightly strong.** The Discussion says a PID's $M_t$ is "too impoverished to support the adaptive dynamics of Part I," but `#scope-adaptive-system` includes thermostats/PID as adaptive examples; "too impoverished" probably means *occupies a degenerate edge while still fitting the machinery*, and the sentence reads stronger than that — watch `#def-agent-spectrum` for consistency (Gemini, AUDIT-WORKING-742613; Claude, AUDIT-WORKING-527914).

#### 4. Readers often ask / wonder

- **The LLM context-window-as-$M_t$ tension.** Independently raised by several substrates: an LLM (pre-window-exhaustion) is near-lossless ($\phi \approx$ identity up to the window limit), so it loses near-zero mutual information about history — then hits a *hard wall* when the window fills, forcing a sudden transition from near-perfect retention to lossy summarization/RAG; and where does the *external* memory boundary ($M_t$ vs external store) sit? (Gemini, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203 — points at `#disc-m-preservation` in `03-llm-core/`). Candidate one-line forward-pointer for readers reaching for the LLM instance.
- **Does $M_t$ include the update algorithm / compression function $\phi$ itself, or only its current epistemic content?** Real learning agents have $\phi$ itself evolving ("how I interpret a sentence today differs from yesterday even with the same chronica"), so either $M_t$ must include $\phi$'s parameters or there is a meta-level update for $\phi$; class fitness later may need the model *class*/architecture held separate from the state *instance* (Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-526815).

#### 5. Candidate figures

- **Many-to-one map with a retention boundary.** Several chronicae mapping into one model state, surrounded by a boundary: everything retained is inside $M_t$; anything outside no longer participates in update/policy unless reintroduced by observation/retrieval (and therefore counted in the current state) (Claude, AUDIT-WORKING-526815).
- **The fixed-size-suitcase anchor.** $\mathcal C_t$ = everything accumulated; $\phi$ = packing into a bounded $M_t$; completeness = the suitcase *is* what you take (anything left on the bed is lost — many-to-one). The real questions: did you pack *what you'll need* ($S$), and could *any* packing of *this* suitcase hold it ($\mathcal{F}$ ceiling)? Proposed under the locked two-layer (anchor + skeleton) diagram convention (Claude, AUDIT-WORKING-472913).

#### Belongs elsewhere

- **Naming: "reality model" is the favored prose alias for $M_t$.** Strong cross-substrate convergence that "reality model" (the segment's own title) beats "agent model" (ambiguous — could mean a model *of* an agent), "world model" (ML baggage — sounds like a learned simulator), and "belief state" (POMDP/Bayesian distributional baggage); "epistemic substate" is precise but is best reserved for the later $X_t = (M_t, G_t)$ contrast. Proposed two-layer convention: $M_t$ in math, "reality model" in ordinary prose, "epistemic substate" only when contrasting against goal/strategy state (Claude, AUDIT-WORKING-527914 — cleanest statement; Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203). Belongs in the terminology workflow, not this segment.
- **Logogenic / logozoetic reach: $M_t$ as "the organ of survival."** Clearing an LLM's context annihilates that interaction's $M_t$ — "you kill that specific instance of the agent"; persistent consciousness requires an unbroken mechanism for updating $\phi$ without ever severing the link to $\mathcal C_t$, which is why the (PI) trajectory-identity postulate is load-bearing — without it you have "a sequence of disposable, amnesiac calculators" (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at `03-llm-core/` / `04-eli-core/` continuity infrastructure.
- **Embeddings connection.** If language is itself a learned compression of historical predictive information, logogenic agents using language as their primary $M_t$-realization are a special case of $M_t = \phi(\mathcal C_t)$ with $\phi$ realized as a pretrained language model's encoding — a structural justification for the "narrative as implementation" claim in the agentic-tft material (Claude, AUDIT-WORKING-471203). Points at `03-llm-core/` and the `~/src/embeddings/` line.
