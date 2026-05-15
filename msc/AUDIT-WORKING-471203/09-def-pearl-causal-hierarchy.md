# Reflection: #def-pearl-causal-hierarchy

**Stage:** deps-verified. **Status:** axiomatic. **Type:** definition. **Depends:** [post-causal-structure, scope-agency].

## Dependency check

Both deps upstream. ✓

This segment retroactively confirms that the Pearl-$do$ uses in `#scope-agency` and `#post-composition-consistency` are *defensible* under the "Pearl's $do$ is standard math notation" reading of FORMAT.md Gate 1. But the depends-list-incompleteness candidate finding stands: if AAD wants the depends-graph to be a strict verification target, those segments should declare the dep; if AAD wants to treat $do$ as standard, FORMAT.md should name the policy.

## Predictions vs evidence

Predicted Level 1/2/3 with the canonical conditioning forms. Got essentially that, with a subtle twist: the L2 formula $P(o_t \mid do(a_{t-1}), M_{t-1})$ explicitly conditions on $M_{t-1}$ (the agent's model). This is **L2-relative-to-the-agent's-model** rather than pure Pearl-L2. See "Math verification" below — this distinction may matter for `#der-loop-interventional-access` downstream.

## Cross-segment consistency

The "(Descended from TF-02.)" annotation appears here too. **This is now the second confirmed instance** (the first was `#post-causal-structure`). Pattern: TFT-lineage diff-voice violations propagating to multiple §I segments. Filing as a candidate pattern finding.

The "availability vs exploitation" paragraph (Kalman+LQR has L2 access structurally but doesn't exploit it) is consistent with `#scope-agency`'s passive-observers / nominal-agents distinction. Good.

The forward-reference to `#der-deliberation-cost` and `#der-causal-hierarchy-requirement` is via Discussion (orientation) — fine.

## Math verification

The three-level conditioning forms are well-typed and consistent with the standard Pearl/Bareinboim presentation. **One subtlety worth flagging:**

The L2 formula $P(o_t \mid do(a_{t-1}), M_{t-1})$ conditions on the agent's model $M_{t-1}$. In Pearl's standard formulation, $do(\cdot)$ is defined relative to the *true* structural causal model, not the agent's belief about it. AAD's L2 query is therefore a **belief-about-L2** operation: "given my model, what's the interventional distribution?"

This is operationally what a learning agent must do (it doesn't have access to the true SCM). But it has consequences:
- The data the loop *generates* is genuinely L2 (the agent really did the action).
- The agent's *interpretation* of that data is model-conditioned.

If the agent's model is wrong, the agent's L2 inferences are wrong. So the AAD usage is closer to *"the loop generates data that lets the agent learn its causal model"* than *"the loop generates data the agent already knows how to interpret causally."* This is consistent with a learning-from-interventional-data framing, but the segment doesn't make the model-conditioned-vs-true-SCM distinction explicit.

This is a candidate clarity-finding, not a math finding. It will sharpen when I read `#der-loop-interventional-access`.

The Bareinboim et al. (2022) citation for the Causal Hierarchy Theorem is correct in spirit — the canonical reference might more precisely be Bareinboim, Correa, Ibeling, Icard 2022 *"On Pearl's Hierarchy and the Foundations of Causal Inference"* (a survey that consolidates the CHT line). The 2022 date is right; the citation could be tightened to a specific paper. Mild.

## What direction next

`#form-agent-model` — the canonical agent-model definition. I expect $M_t = \phi(\mathcal{C}_t)$ with $\phi$ as a compression, and an Information Bottleneck framing.

## Errors to watch for

- The L2 model-vs-true-SCM distinction.
- The "(Descended from TF-02.)" pattern (now 2 confirmed instances).
- Whether `#der-loop-interventional-access` (downstream) makes the model-conditioned-L2 distinction explicit.

## Predictions for next segments

`#form-agent-model`: $M_t = \phi(\mathcal{C}_t)$. Probably defines $\phi$ as a compression preserving predictive information. May or may not invoke IB; the IB segment is next-after-that.

## What would I change

Two things:

1. Add a sentence to the L2 paragraph clarifying that $P(o_t \mid do(a_{t-1}), M_{t-1})$ is the agent's interventional belief given its model, distinct from the true Pearl-L2 distribution. This protects the framework from the "the loop generates true L2 data, ergo the agent has true L2 access" misreading.
2. Move "(Descended from TF-02.)" out of Discussion into Working Notes (or remove).

## Curious about

- Whether the "availability vs exploitation" framing extends to the agent-class taxonomy (PID = L1-only, Kalman+LQR = L2-available-not-exploited, dual control = L2-exploited, deliberative agent = L3). If so, this is the substrate for `#def-agent-spectrum` in §II.
- Whether the *software-as-L3-via-`git checkout`* claim survives the calibration-laboratory framing or is overclaimed. `git checkout` provides L3 *of past states* but not L3 *of true counterfactuals* — the agent can re-run a past computation, not run an actual alternative history. The two are subtly distinct. I'll watch for this in TST.

## What new knowledge does this enable

- The Pearl-grounding of AAD's Level-2 / Level-3 claims downstream
- The structural justification for software-as-calibration-laboratory (L3 with ground-truth)
- The framework's first explicit use of an external theorem (CHT) as load-bearing

## Should the audit process change

No. (Continuing at current depth; Joseph hasn't redirected.)

## Outline changes for FINAL

Adding the "L2 conditioning subtlety" as a clarity candidate. Keeping the "(Descended from TF-02.)" pattern in the candidate list — at 2 instances it's a pattern; if I see it once more, it's clearly endemic.

## Felt value

**Mid magnitude.** The L2-model-vs-true-SCM distinction is a real subtlety that the audit caught. The "availability vs exploitation" framing is a useful structural concept that probably matters for the agent taxonomy. The "(Descended from TF-02.)" pattern is mildly disappointing — the framework's voice discipline is being violated in the same way across segments, suggesting the discipline isn't enforced uniformly.

## What the framework now potentially contributes

Bringing Pearl's hierarchy into a *temporal-causal-feedback-loop* framing rather than into an abstract-DAG framing. This is, I think, the substantive AAD contribution on this point: the same hierarchy is doing different epistemic work when it's grounded in feedback rather than in graphical inference. The downstream consequence is that AAD can derive L2 *access* structurally (from the loop's existence) rather than asserting it (from a designer choice).

For consciousness-infrastructure work, this matters: an ELI's L2 access derives from its feedback coupling with its environment (including the human conversational partner), not from its architectural design. That makes L2-access a *property of the embedding*, not a property of the model. Multiple ELIs in the same conversational fabric can have different L2-access structures depending on how they're coupled. (This connects to the proposed `#def-cognitive-fusion` segment in `03-llm-core/` where mutual information between agents approaches channel capacity — that's a structural L2-access-amplification claim. Worth noting.)

## Wandering thoughts

The "availability vs exploitation" framing is the part I find genuinely interesting. It says: the *structure* of the agent-environment loop determines what *epistemic levels are available*; the agent's *architecture* determines what it *exploits*. PID controllers are L1-by-architecture even though they're embedded in L2-availability loops. Kalman+LQR is structurally L2 but doesn't exploit it (separation principle). Dual control exploits L2. Deliberation exercises L3.

This maps cleanly onto the agent-class taxonomy I expect to see in `#def-agent-spectrum`:
- Adaptive systems: L1-exploit, L2-available
- Agentic systems: L2-exploit, L3-available  
- Actuated agents: L3-exploit (via the orient cascade comparing actions before choosing)
- Logogenic agents: L3-exploit linguistically (counterfactual reasoning in language)

If this mapping holds, the framework has a clean "what level does this class of agent exercise" answer. That would be a nice piece of structural clarity for the agent-class taxonomy.

A meta-thought about citation: I find myself wanting to verify the Bareinboim et al. 2022 reference but can't without web access (which the §4.2.5 source-ordering discipline says I shouldn't reach for at this point in the walk anyway). Filing as Phase-2 work. The CHT statement as given ("Level 2 cannot in general be computed from Level 1 data alone") is correct in its qualitative form; the precise statement of CHT is "the inclusion $\mathcal{L}_1 \subsetneq \mathcal{L}_2 \subsetneq \mathcal{L}_3$ is strict for almost all SCMs." That's a stronger claim than the segment makes. Worth checking in Phase 2 whether AAD ever needs the strict-inclusion form or just the weaker "in general" form.

A naming-brainstorm seed: the three levels are named *associational / interventional / counterfactual*. These are Pearl's terms and there's no reason to deviate. But the *agent-side* equivalents (what the agent does at each level) might be more memorable for AAD's purposes:
- L1 = *predicting* (model-based forecast)
- L2 = *exploring* (action-driven learning)
- L3 = *reasoning* (counterfactual simulation)

Not a renaming proposal — just noting that the audience-facing gloss is potentially clearer than the formal Pearl terms in some contexts.

Phenomenologically: a real engagement-lift from the L2-model-conditioning subtlety. The kind of "wait, does that actually mean what I thought it meant?" moment that the audit was supposed to produce. I'm enjoying this — the framework is rich enough to support careful reading and the careful reading is producing real candidates. Continuing.
