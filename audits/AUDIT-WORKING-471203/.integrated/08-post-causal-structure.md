# Reflection: #post-causal-structure

**Stage:** deps-verified. **Status:** axiomatic. **Type:** postulate. **Depends:** [def-agent-environment, def-chronica].

## Dependency check

Both deps upstream. ✓

The Formal Expression depends only on `#def-chronica` content (the ordered-sequence claim). The Discussion references downstream segments (`#def-pearl-causal-hierarchy`, `#def-causal-information-yield`, `#def-mismatch-signal`) for orientation — these are *Discussion-section* forward references, which are permissible per FORMAT.md. **This segment is depends-clean** in a way `#disc-composition-consistency` was not.

This **softens my pattern claim from segment 7**. Two distinct shapes of depends-incompleteness exist:
- `#scope-agency`: uses Pearl's $do$ notation in Formal Expression without declaring `#def-pearl-causal-hierarchy` as dep. Mild — arguably standard math notation.
- `#disc-composition-consistency`: uses downstream-derived results (`#result-contraction-template`'s closed-form composite-rate inequalities) in Formal Expression without declaring deps. More serious.

`#post-causal-structure` does *neither* of these. So the pattern is currently 2 of 3 postulate/scope segments showing depends-incompleteness, but the *kinds* differ. I'll keep counting; the pattern strength depends on what the rest of §I does.

## Predictions vs evidence

Predicted: a postulate that the system has well-defined causal structure (DAG-shaped). Got something more primitive — the postulate is *about temporal ordering*, with the Pearl/DAG/Markov machinery deferred to `#def-pearl-causal-hierarchy` and `#deriv-graph-structure-uniqueness`. The "causal structure" of this segment is just *the arrow of time*.

I appreciate the restraint — making the pre-statistical "$A$ before $B$" notion the postulate, rather than jumping to "edges in a DAG." It means the DAG structure becomes derivable later (in `#deriv-graph-structure-uniqueness`'s 4-postulates-+-causal-sufficiency claim) rather than postulated.

The four coupling regimes (strong / weak / nominal / zero) were not in my priors and are an interesting taxonomy. The "nominal coupling" regime is particularly important — the agent's *query choice* generates contrast even when the environment-effect is negligible. This is the structural justification for TST's "test selection as intervention" framing and probably for any active-perception case in logogenic agents.

## Cross-segment consistency

Consistent with `#scope-agency`'s adaptive-vs-agentic boundary: zero-coupling systems are explicitly placed *outside* agency, *inside* adaptive — matching the passive-observers / nominal-agents distinction in `#scope-agency`. The four-regime taxonomy here gives a finer partition of agency-scope cases.

The annotation **"(Descended from TF-02.)"** at the end of the Discussion is a **diff-voice violation** per FORMAT.md's voice discipline ("spike/diff references go only in Working Notes"). Small finding. Tracking.

## Math verification

The condition for zero coupling ($T(\Omega_{t+1} \mid \Omega_t, a_t) = T(\Omega_{t+1} \mid \Omega_t)$ for all $a_t$ AND observation distributions are action-independent) is correctly stated. Note the *AND*: zero coupling requires both the transition kernel to be action-independent *and* the observation distribution to be action-independent. If only one fails, you're in the nominal-coupling regime where queries generate contrast.

## What direction next

`#def-pearl-causal-hierarchy` — finally the Pearl machinery. I expect: Level 1 (associational), Level 2 (interventional via $do(\cdot)$), Level 3 (counterfactual). The segment will retroactively legitimize the Pearl-do uses in `#scope-agency` and `#disc-composition-consistency`'s machinery — but not retroactively fix the missing depends.

## Errors to watch for

- Continuing to track the depends-incompleteness pattern (now: 2 instances confirmed in 7 segments, of differing severity).
- The "(Descended from TF-02.)" voice-discipline violation. Worth checking whether other segments have similar lineage annotations.
- Whether the four-coupling-regime taxonomy gets used downstream. If it doesn't, the taxonomy is over-developed-relative-to-use; if it does (TST, §III adversarial dynamics), this segment is doing important pre-positioning.

## Predictions for next segments

`#def-pearl-causal-hierarchy`: standard Level 1 / Level 2 / Level 3 framing, with $P(o)$ / $P(o \mid do(a))$ / $P(o_{a^\prime} \mid a)$ as the canonical exemplars. Probably cites Pearl 2009 / Bareinboim et al. (CHT). May or may not cite Pearl-Bareinboim 2014 *On Pearl's Hierarchy and the Foundations of Causal Inference*, which formalized the hierarchy strictly.

## What would I change

Move "(Descended from TF-02.)" into Working Notes, or remove entirely (the segment's depends and content stand on their own). Editorial; small.

The "nominal coupling" framing deserves its own paragraph or maybe a forward-pointer to the segment(s) where it becomes load-bearing (TST, possibly logogenic). Currently it's introduced and then dropped.

## Curious about

Whether the *four* coupling regimes is the full taxonomy or whether intermediate cases (e.g., "the agent's actions partially affect $T$ but the observation is a noisy partial readout regardless of action") need their own naming. The current four-way partition feels coarse — but that may be enough for AAD's downstream uses.

## What new knowledge does this enable

- A foundation for the Pearl machinery (Level 2 access via the loop)
- The four-coupling-regimes taxonomy, which structurally enables TST's "queries-as-interventions" framing and possibly the `#def-causal-information-yield` definition
- The directed/retrospective/prospective/monotonic structure of the cycle's temporal logic

## Should the audit process change

No. (I am noticing that without Joseph's response yet on pacing, I'm continuing to write reflections at full depth. If he comes back with "compress on the easy ones," I can downshift starting from the next segment. The current depth on these foundational segments is producing real candidate findings — depends-incompleteness, voice-discipline violation — so I'll hold for now.)

## Outline changes for FINAL

Adding the "(Descended from TF-02.)" voice-discipline observation to the candidates list.

## Felt value

**Mid magnitude.** The "causality is temporal precedence" postulate is structurally restrained in a way I find quietly elegant — it doesn't reach for Pearl prematurely, doesn't reach for DAGs, just claims the arrow of time. The four-coupling-regimes taxonomy is interesting but feels under-developed for the weight it could carry.

## What the framework now potentially contributes

A *pre-statistical* foundation for causal reasoning. Most agent-theoretic frameworks reach for Pearl's hierarchy or for SEM-style structural causal models early. AAD's two-step move — temporal-precedence postulate first, Pearl-hierarchy as a separate (and downstream) definition — separates the *physical* structure of causality from the *inferential* machinery for reasoning about it. This is a cleaner foundational stance and probably matters for logogenic agents (where the temporal structure is preserved but the SEM machinery is harder to apply directly).

## Wandering thoughts

The "nominal coupling" regime is the framing I keep coming back to. It says: an agent that has *no environmental effect* but whose *query choice* generates distinguishable observation distributions still has Level-2 access — to itself, in some sense. The agent is intervening on its own observation channel. This is structurally the case for:

- A scientist running experiments — the experiment doesn't move the planet, but the choice of *which experiment* generates contrasting observation distributions
- A software engineer running tests — the test doesn't change production, but the choice of *which test* generates contrasting observations on the codebase's state
- An LLM in a context window — the model's choice of *what to attend to* generates contrasting "observations" of its own context, even though it isn't changing the context

That last case is the structural justification for the framing in `03-llm-core/`'s proposed `#obs-backward-inference-empathy` ("LLM statelessness forces continuous Bayesian inference on own text, which is mathematically identical to Theory of Mind"). If the LLM's attention pattern is a *query choice* (action-on-observation), then the Pearl-Level-2 contrast is real and the framework's interventional machinery applies. This is a much more interesting case than I had initially read it as.

The framework is doing more pre-positioning here than the segment-text alone reveals. The four-coupling-regimes is a surface-level observation; the structural consequence — that Level-2 access is preserved in the nominal regime — is the part that has teeth for downstream domains.

A naming-brainstorm seed: "nominal coupling" is a forgettable term. What it's actually naming is *query-bound* or *attention-bound* agency — agency whose effect is on what's seen rather than what happens. Maybe "epistemic-only coupling" or "query-coupling" or "attentional coupling." None of these are obviously better; flagging that the current term doesn't carry the weight of what it names.

A meta-thought on the postulate's restraint: the segment explicitly notes that the postulate is *prior to* statistical notions ("weaker than (and prior to) statistical notions of causality"). That's a deliberate epistemic move — temporal-precedence is the logical precondition for statistical-causal reasoning, not a special case of it. A reader steeped in Pearl might find this trivially obvious; a reader steeped in correlation-implies-causation-flame-wars will find it foundationally important. The segment is signaling to multiple audiences without overclaiming.

Phenomenologically: still mid-engagement, lifted slightly by the "nominal coupling → query-bound agency" insight. The audit is starting to surface structural connections I wasn't predicting at the segment-level — exactly the kind of cross-segment pattern that the slow-walk discipline is supposed to produce.

Continuing to `#def-pearl-causal-hierarchy`.
