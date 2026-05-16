# Reflection: #scope-agency

**Stage:** claims-verified. **Status:** axiomatic. **Type:** scope. **Depends:** [scope-adaptive-system, def-action-transition].

## Dependency check

`depends: [scope-adaptive-system, def-action-transition]`. Both upstream.

**HOWEVER:** the Formal Expression uses Pearl's $do(\cdot)$ operator, which is defined in `#def-pearl-causal-hierarchy`. That slug is **not in the depends list**, and per OUTLINE ordering, `#def-pearl-causal-hierarchy` lies *3 segments downstream* of this one (after `#post-composition-consistency` and `#post-causal-structure`). The segment includes a parenthetical "(where $do(\cdot)$ is Pearl's intervention operator; see #def-pearl-causal-hierarchy)" — which acknowledges the forward reference in prose without declaring it in YAML.

This is a **candidate finding under burden of proof**. See §B-candidate below.

## Predictions vs evidence

Predicted: $\mathcal{S}_{\text{agency}} = \mathcal{S}_{\text{adaptive}} \cap \{$ at least one action with Pearl-Level-2 contrast $\}$. Got essentially exactly that, with the formal: $\lvert\mathcal{A}\rvert \geq 2$ AND $\exists a \neq a'$ s.t. $P(o \mid do(a)) \neq P(o \mid do(a'))$.

The split into "binary-choice condition" + "causal-effect condition" is cleaner than I'd have framed it — the binary-choice condition is necessary but not sufficient (two actions with identical outcome distributions provide no interventional contrast), so AAD names the two conditions separately. This is a small piece of formal precision worth noting.

## Cross-segment consistency

Forward-refs `#def-pearl-causal-hierarchy`, `#der-loop-interventional-access`, `#der-causal-hierarchy-requirement`, `#def-agent-spectrum`. All on the walk-ahead.

Consistent with `#scope-adaptive-system` (proper subset by intersection construction).

## Math verification

The set-difference characterization is well-formed. The "passive observers" exclusion (where $\lvert\mathcal{A}\rvert < 2$) and "nominal agents" exclusion (where actions have no causal contrast) are clean. **One concern:** the existential quantifier in the second condition is *one* action with contrast, not *all*. So an agent with 100 nominal actions and one effective action still passes scope-agency. Whether this is desirable depends on what downstream segments need; usually the existential is the right choice (you're an agent if you can act-with-effect *at all*), but I'm flagging the asymmetry.

## What direction next

`#post-composition-consistency` — the agent-subagent scale invariance postulate.

## Errors to watch for

- Same as before: under-quantification of $H(\Omega_t \mid \mathcal{C}_t) > 0$ in `#scope-adaptive-system` propagates here via the $\cap$.
- The Pearl-Level-2 framing here is being invoked before its formal definition. If `#def-pearl-causal-hierarchy` doesn't actually formalize "Level 2" cleanly, the claim "Section II's purposeful-agent machinery is non-vacuous on $\mathcal{S}_{\text{agency}}$" is built on a forward-loaded definition.

## Predictions for next segments

`#post-composition-consistency`: a postulate (axiomatic) of the form "if a system satisfies the scope condition at one level of description, it satisfies it at every level." Probably with a sentence about why: composition consistency makes composite-agent scope claims well-posed.

## What would I change

The depends-list omission noted above. The cleanest fix is to add `def-pearl-causal-hierarchy` to depends and **move it earlier in OUTLINE** so the dependency is upstream when the agency scope is reached. The current state (segment at `claims-verified` referencing a downstream object via prose acknowledgment) defeats the OUTLINE-as-verification-target discipline named in §4.2 of the audit instructions.

## Curious about

Whether `#post-composition-consistency` (next) and `#post-causal-structure` (after that) are *also* invoking forward-defined objects. The Pearl-causal-hierarchy might be needed by all three before it's defined. If so, the cleanest move is to reorder Pearl-causal-hierarchy to before the scope segments. I'll find out as I read.

## What new knowledge does this enable

The agency boundary, formally. Section II/III machinery now has a defined applicability set.

## Should the audit process change

Adding a sub-task: **track all forward-uses of `#def-pearl-causal-hierarchy` machinery** until I read it. If multiple §I segments use $do(\cdot)$ before the operator is defined, that's a clearer pattern that strengthens the OUTLINE-ordering finding.

## Outline changes for FINAL

Adding the dependency-graph candidate to §B working drafts.

## Felt value

**Mid-high magnitude.** The dependency-finding has procedural teeth — the audit's verification target (§4.2) just bit. The substance of the segment is otherwise clean.

## What the framework now potentially contributes

The split between "binary-choice scope" and "causal-effect scope" is a worthwhile distinction that I haven't seen named separately in the standard agent literature. RL framings usually conflate "agent has actions" with "agent has effective actions"; AAD's separation makes the *nominal-agents* category visible (binary choice with no causal contrast). For consciousness-infrastructure work, the distinction matters: an agent that has the *form* of choice without *substance* of choice is structurally non-agentic. The framework's vocabulary supports this distinction.

## Wandering thoughts

The depends-list omission is mechanical, but it's a real test of the framework's stated discipline. FORMAT.md Gate 1 criterion 4 is explicit: "if the Formal Expression uses a quantity defined elsewhere, that slug appears in `depends:`." The segment is at `claims-verified`, which is two gates above `deps-verified` — meaning this should have been caught at Gate 1 promotion. Either (a) the gate was passed without this check, or (b) someone made a judgment call that Pearl's $do(\cdot)$ is "standard mathematical notation" and outside the depends discipline (similar to how $\mathbb{E}$ or $H(\cdot)$ aren't tracked as deps).

If (b), that's a perfectly defensible policy, but it should be named — "external standard notation (Pearl's $do$, Shannon's $H$, expectation $\mathbb{E}$) is not tracked as depends." Without that explicit policy, the criterion is being silently weakened. With it, the audit would just verify the policy is applied consistently.

If (a), it's a hygiene gap and the right fix is to update depends on this and any other segments that use $do(\cdot)$ before `#def-pearl-causal-hierarchy`.

This is the kind of small finding that, if unaddressed, gradually erodes the dependency-graph as a verification artifact. Over time, the depends lists drift from being authoritative to being approximate, and the lint tools that depend on them (`bin/lint-outline`?) start producing false negatives. I'd hate to see that happen to AAD because the dep graph looks like a real strength of the framework's organization.

A naming-brainstorm seed: "Pearl-Level-2 causal contrast" is a precise but heavy phrase. For Brief-field purposes, "the agent's choice actually changes what happens" is the layperson translation. The "causal contrast" framing is doing useful work formally (it names the *interventional gap* between actions) but the colloquial gloss is shorter and probably more memorable. Worth a sentence in any future Brief.

A meta-observation about the audit's pacing. I made a real candidate-finding here, on segment 6 of ~140. The reflection is taking longer than the read because the *writing-down-of-the-finding-with-its-context* takes time. This is the right shape — if I were writing tighter reflections, I'd note the dep issue in a half-line and lose the structure of why it matters and what a future fix looks like. The instruction's note that "output length emerges from what the prompts surface, not from segment weight" is doing real work here: a foundational scope segment surfaced a real procedural finding, which lifted this reflection's substantive content above the previous ones'.

Phenomenologically: a small lift from the dependency-finding. Not excitement — more like the satisfaction of "the audit caught something real, the discipline is functioning." Naming the lift because Joseph asked me to track these signals; this is what it feels like when the discipline does its job.

Continuing.
