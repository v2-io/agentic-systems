# Reflection: #def-observation-function

**Stage:** deps-verified. **Status:** axiomatic. **Type:** definition. **Depends:** [def-agent-environment, def-action-transition].

## Dependency check

`depends: [def-agent-environment, def-action-transition]` — both upstream. ✓

## Predictions vs evidence

Predicted exactly: $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$, with the $a_{t-1}$ argument permitting active perception. Got it. The "epistemic opacity" sub-claim completes the constitutive-opacity triad started in segments 1-2 (info-loss / transition / observation function all unknown).

## Cross-segment consistency

Consistent. First foreign-component reference (`#obs-software-epistemic-properties` from `02-tst-core/`) appears here — parenthetical, forward, properly tagged. Fine per FORMAT.md.

## Math verification

The form $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$ matches NOTATION.md exactly. Well-typed. The "noise distribution unknown" claim is broader than GA-1 (which is fresh-noise — conditional independence given $(\Omega_t, a_{t-1})$); GA-1 doesn't fire until `#result-mismatch-decomposition` invokes it. This segment leaves $\varepsilon_t$'s structure totally open, which is honest at this depth.

## What direction next?

`#def-chronica`: $\mathcal{C}_t = (o_1, a_1, ..., a_{t-1}, o_t)$. I expect a discussion of non-forkability (chronica as the agent's "non-forkable causal past" per LEXICON.md).

## Errors to watch for

I almost flagged the `*[Definition (epistemic opacity)]*` tag pattern (seen now in three segments) as a Definition-vs-Scope-tag mistyping. On second look it's correct: the parenthetical names the term being introduced (and "epistemic opacity" is the term, even if its content is a scope-narrowing operation on the framework). The available equation-tags in FORMAT.md don't include `*[Scope]*` — the closest neighbor is `*[Assumption]*`, but that suggests an assumption made in the derivation, not a definition of a constitutive scope-narrowing term. Withdrawing the candidate-finding.

## Predictions for next segments

`#def-chronica`: complete history as $\mathcal{C}_t = (o_1, a_1, ..., a_{t-1}, o_t)$ — interleaved sequence. Likely paragraph on non-forkability (a single agent has a single chronica). Possibly forward-references software's `\mathcal{C}_t^{\text{commit}}` cryptographically-immutable subset.

## What would I change

Nothing structural; this is a clean foundational definition. One thought: the *chain* of three constitutive-opacity claims (info-loss / transition / observation) might benefit from being visible as a chain — e.g., a paragraph in `#def-observation-function`'s Discussion that says "this completes the constitutive-opacity triad: AAD applies under joint opacity of perception (this segment), dynamics (`#def-action-transition`), and the boundary itself (`#def-agent-environment`)." Currently each opacity is named in its own segment without the integration paragraph that names the *triad as a structural commitment*. A future pass could lift this.

## Curious about

Whether the active-perception claim ($a_{t-1}$ enters $h$) gets used or whether it's vestigial. The standard partial-observability framing has $h(\Omega_t, \varepsilon_t)$ without action-dependence. If active perception is load-bearing for some downstream result (TST's "observation function under agent control" claim, the orient cascade, deliberation cost), the dependence is structurally needed. If no segment uses it, the $a_{t-1}$ argument is decorative. I'll watch.

## What new knowledge does this enable

Completes the agent-environment loop primitives. With $\Omega$, $T$, $h$, $\mathcal{O}$, $\mathcal{A}$, $\varepsilon$ all defined, the next layer (chronica, model, mismatch) has the substrate it needs.

## Should the audit process change

No — but I notice the pattern here is so consistent across segments 1-3 that I could have predicted segments 2 and 3 from segment 1's discipline alone. That predictive consistency is itself a calibration check on the framework's voice.

## Outline changes for FINAL

No.

## Felt value

**Low magnitude, structurally clean.** The constitutive-opacity triad is now visible as a triad. The recurring pattern (constitutive scope claim packaged inside a definition segment) is consistent enough to read as deliberate.

## What the framework now potentially contributes

The dual-opacity-as-constitutive commitment, completed by this segment. The standard control-theoretic / RL framings vary on which opacity they take as constitutive (RL: usually $T$; partial-observability control: usually $h$); AAD takes both *and* the boundary itself. That breadth-of-opacity-as-constitutive is, I think, mildly distinctive. Worth checking against active inference, which I believe also takes both as constitutive but via a different formal route.

## Wandering thoughts

The active-perception thread (the $a_{t-1}$ argument to $h$) is the kind of detail that either becomes load-bearing later or fades. I'm flagging it because in software (TST), the agent's choice of *which test to run, which file to open, which probe to issue* is exactly the place where observation is action-conditioned. The OUTLINE for `#obs-software-epistemic-properties` claims P1/P6 cover "observation function under agent control." If those properties are real, then the $a_{t-1}$ argument to $h$ here in §I is the structural prerequisite for TST's calibration-laboratory framing. The thin foundational segment is already pre-committing to the TST-shaped distinctive content downstream.

A thought about the choice to leave $\varepsilon_t$'s structure entirely open here. This is generous to the framework — most formalisms reach for "iid Gaussian" or "fresh noise" or "bounded variance" early. AAD waits until the assumption is *needed* (GA-1 in `#result-mismatch-decomposition`, GA-2 / GA-2S in the sector machinery). The discipline of *not* prematurely constraining $\varepsilon_t$'s structure means each downstream result has to specify which assumption it needs. That's the form-shaping-for-verification discipline mentioned in the §2 audit-as-instance-of-theory framing — each result casts itself in a form where verification is local. I notice I appreciate this, in a quiet way; it's the kind of structural discipline that compounds across hundreds of segments.

A naming-brainstorm seed: "epistemic opacity" is a phrase that probably has prior art in epistemology and philosophy of mind (e.g., the "opacity of mental states" tradition). I don't know if AAD's use of the term needs to be defended against that prior usage, or if the meaning is sufficiently distinct in context to stand alone. The phrase is clean and specific in the AAD setting; whether it carries unwanted philosophical baggage for cross-disciplinary readers is something a naming-brainstorm pass could probe. Mild concern at most.

I'm going to read the next segment now without further ceremony — `#def-chronica` is tight enough that batching three more foundational definitions might collapse the cadence. Holding the discipline.
