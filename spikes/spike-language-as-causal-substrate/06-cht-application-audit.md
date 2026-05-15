# CHT Application Audit — Rigor Check on the Non-Reduction Step

*Foundational audit on the load-bearing step of Theorem 1. The CHT-style non-reduction argument in `01-derivation.md` §4 is what gives the result genuine teeth (without it, Theorem 1 reduces to a labeling tautology). Auditing the application carefully here before any promotion to a segment.*

---

## The step being audited

Theorem 1 in `01-derivation.md` rests on a non-reduction claim:

> *"The Level 2 content $\mathcal{E}_2$ is **not derivable** from any Level 1 summary of $T$, by CHT applied to the example pairs $T_B$ vs $T_D$ in Lemma 1 (which generalize: every Level-2 marker pair contributes a CHT-style non-reduction example)."*

The kettle pair:

- $T_A$: "The water in the kettle boiled, and the kettle whistled."
- $T_B$: "The water in the kettle boiled, **causing** the kettle to whistle."
- $T_C$: "The kettle whistled, and the water in the kettle boiled."
- $T_D$: "The kettle whistled, **causing** the water in the kettle to boil."

I claimed: $T_B$ and $T_D$ have the same Level 1 content, different Level 2 content; therefore by Pearl Causal Hierarchy (PCH; Bareinboim-Correa-Ibeling-Icard 2022), the Level 2 content is non-reducible to Level 1.

Audit goal: verify this claim is rigorous, not just plausible.

---

## Formal setup

To audit rigorously, I need to specify *what* is being compared at each Pearl level.

There are two distinct readings of "Level 1 content of a text" that the original spike runs together loosely. Disentangling them is the audit's main work.

**Reading (a) — Level 1 over event-variables**: The text mentions events boil and whistle. The Level 1 content under this reading is the joint distribution $P(\text{boil}, \text{whistle})$ that the speaker is committed to (or that a reader infers as the speaker's commitment).

**Reading (b) — Level 1 over the text-as-data**: The text is itself a sequence of tokens. A reader who treats the text as Level 1 observational data has access to the joint distribution over tokens. The token-level joint distribution differs between $T_B$ and $T_D$ (different markers in different positions).

The claim "same Level 1 content" applies to reading (a). At reading (b), the texts trivially differ (they are different token sequences). The non-trivial claim — and the one CHT bears on — is at reading (a).

This distinction matters: it's the difference between *"the text encodes Level 2 content via marker structure"* (the spike's claim) and *"any observation of the text gives Level 1 evidence about the world"* (trivially true). Both are true; only the first is non-trivial.

---

## Rigorous comparison at reading (a)

Working only at the event-variable level $V = \{\text{boil}, \text{whistle}\}$.

**$T_B$'s commitment**:

- Both events occurred. So the marginal that the speaker is committed to is $P(\text{boil} = 1, \text{whistle} = 1) > 0$. (How much greater than 0 depends on speaker reliability and conversational context; for cooperative truthful speakers, near 1.)
- An interventional commitment via "causing": $P(\text{whistle} = 1 \mid \text{do}(\text{boil} = 1)) > P(\text{whistle} = 1 \mid \text{do}(\text{boil} = 0))$. Intervening to make the water boil produces whistling; intervening to prevent boiling prevents (or reduces probability of) whistling.

**$T_D$'s commitment**:

- Both events occurred. Same marginal commitment.
- An interventional commitment via "causing" in the opposite direction: $P(\text{boil} = 1 \mid \text{do}(\text{whistle} = 1)) > P(\text{boil} = 1 \mid \text{do}(\text{whistle} = 0))$. Intervening on whistling affects boiling.

The Level 1 marginal $P(\text{boil}, \text{whistle})$ is the same in both cases (both events with high probability). The Level 2 interventional content is *opposite-directed* between $T_B$ and $T_D$.

**Two SCMs realizing this**:

- $\mathcal{M}_B$: $\text{boil} \to \text{whistle}$. Structural equations: $\text{boil} := U_1$; $\text{whistle} := f(\text{boil}, U_2)$ for some monotone $f$. Both events occur with high probability when $U_1, U_2$ favor positive values.

- $\mathcal{M}_D$: $\text{whistle} \to \text{boil}$. Structural equations: $\text{whistle} := U_1'$; $\text{boil} := g(\text{whistle}, U_2')$ for some monotone $g$.

By choosing the exogenous distributions $P(U_1, U_2)$ and $P(U_1', U_2')$ appropriately, the observational distributions $P_{\mathcal M_B}(\text{boil}, \text{whistle})$ and $P_{\mathcal M_D}(\text{boil}, \text{whistle})$ can be made *identical*.

This is the standard CHT example pair construction. By PCH (Bareinboim-Correa-Ibeling-Icard 2022, Theorem 1 of *On Pearl's Hierarchy and the Foundations of Causal Inference*), no Level-1 (observational) analysis of $V = \{\text{boil}, \text{whistle}\}$ can distinguish $\mathcal M_B$ from $\mathcal M_D$. They induce the same observational distribution.

The Level 2 content does distinguish them: $P_{\mathcal M_B}(\text{whistle} \mid \text{do}(\text{boil})) \ne P_{\mathcal M_D}(\text{whistle} \mid \text{do}(\text{boil}))$.

**Therefore the speaker's commitments asserted by $T_B$ vs $T_D$ correspond to two different SCMs that are PCH-non-distinguishable at Level 1 but distinct at Level 2.**

The CHT application is sound. ✓

---

## A subtler question that the audit surfaces

I called the claim "the Level 2 content is not derivable from any Level 1 summary of $T$" in the original spike. The audit reveals this is ambiguous and the precise reading matters.

**Strong reading**: For any procedure that operates only on the joint distribution of the event-variables $\{\text{boil}, \text{whistle}\}$ that the speaker is committed to, the Level 2 distinction $T_B$-vs-$T_D$ is unrecoverable. **True by PCH.**

**Weak reading**: For any procedure that operates on the text-as-tokens, the Level 2 distinction $T_B$-vs-$T_D$ is unrecoverable. **False — the marker structure is in the tokens, and any procedure that reads markers (per §3 of `01-derivation.md`) can distinguish.**

The original spike statement is sound under the strong reading and meant under the strong reading. But the wording could mislead a careful reader. Recommend the segment-promotion version revise the wording to:

> *"The Level 2 content $\mathcal E_2$ is not derivable from the joint distribution of the event-variables alone — by PCH applied to the example-pair construction in Lemma 1. The marker structure in $T$'s token sequence carries the distinguishing information; without it (as in a token-stripped or marker-suppressed summary), the Level 1 event-variable joint distribution alone cannot distinguish $T_B$ from $T_D$."*

This is the rigorous form.

---

## Generalization beyond the kettle example

The audit's most important question: does the kettle example pair *generalize*, or is it a special-case construction?

The original spike claimed "every Level-2 marker pair contributes a CHT-style non-reduction example." Auditing this:

**Generalization claim**: For any pair of events $(E_1, E_2)$ mentioned in two texts $T, T'$ differing only in the direction of an explicit Level-2 marker (e.g., "$E_1$ causes $E_2$" vs "$E_2$ causes $E_1$"), the two texts assert distinct SCMs that are PCH-non-distinguishable at Level 1 but distinct at Level 2.

**Sketch of generalization**: The construction of $\mathcal M_B$ and $\mathcal M_D$ above does not depend on specific properties of boiling and whistling. It depends on:

1. Two event-variables $E_1, E_2$ with well-defined truth-values.
2. A speaker committing to a directed causal relation between them.
3. The exogenous-variable freedom to match marginals across the two directions.

(1) is satisfied by any pair of events the speaker can mention. (2) is satisfied by any Level-2-marker pair (because/causes/leads-to and analogues). (3) is the construction freedom: for any joint distribution $P(E_1, E_2)$, both $E_1 \to E_2$ and $E_2 \to E_1$ SCMs can realize it (with appropriately chosen exogenous distributions and structural equations).

Therefore the example-pair construction generalizes uniformly to any Level-2 marker pair on any pair of events. ✓

**Edge case 1 — deterministic relationships**: If $E_2$ is deterministically determined by $E_1$ (and vice versa is impossible), then only one SCM-direction is consistent with the marginals. The other direction's text would be *contradictory*, not just causally-different. The CHT argument doesn't apply; the speaker's $T_D$ assertion would be physically impossible (and a cooperative speaker wouldn't make it).

Honest scope: the CHT non-reduction applies to event-pairs that *admit* both causal directions as physically possible. For physically-impossible reverse directions ($T_D$ in the kettle case is in this edge), the speaker's claim is still parseable but is committing to a counter-physical SCM. The non-reduction argument still goes through structurally (the *asserted* SCMs differ); the resulting structural commitments are not equally believable.

**Edge case 2 — direct causal cycles**: If both directions are simultaneously asserted (feedback loops, "X causes Y and Y causes X"), the resulting graph is cyclic. Pearl's standard SCM machinery assumes acyclicity; the CHT argument as stated requires DAG structure. Non-trivial generalization to cyclic SCMs exists (Bongers et al. 2020) but is outside this spike's scope. Working scope condition: the discourse-DAG construction in §3 of `01-derivation.md` treats the cycle case via the surrounding discourse structure rather than via direct $E_1 \leftrightarrow E_2$ edges.

**Edge case 3 — same-event self-reference**: "The fire caused itself to spread" — the speaker asserts $E \to E$, a self-loop. PCH doesn't directly apply; the SCM is non-standard. Real natural-language usage of such constructions is rare and idiomatic; the spike scopes them out.

---

## The audit's net result

The CHT application is rigorous under the strong reading of "Level 1 content" (joint distribution over event-variables that the speaker is committed to). The non-reduction step survives careful scrutiny.

**Required wording update for segment-promotion**: tighten "Level 1 summary of $T$" to "joint distribution of the event-variables in $T$ that the speaker is committed to" to forestall the weak-reading confusion identified in §3 of this audit.

**Generalization is sound**: the kettle example is not a special case; it instantiates a uniform construction that applies to any Level-2-marker pair on any event-pair admitting both causal directions.

**Three honest edge cases** (deterministic, cyclic, self-referential) are surfaced and scoped out; none undermines the central result.

The CHT step is the strongest part of Theorem 1. After this audit, my confidence in it is unchanged (high). The audit's value is the wording-rigor update and the explicit treatment of edge cases — both helpful for the eventual segment-promotion but neither material to the result.

---

## Connection to AAT's broader identifiability machinery

The CHT application here is a specific instance of the project's broader [`#disc-identifiability-floor`](../../01-aat-core/src/disc-identifiability-floor.md) machinery — non-reduction at a particular causal-information layer. The audit's general principle (distinguish the variable-set at which non-reduction is claimed) is exactly the same discipline that operates in the identifiability-floor instance triage.

The discourse-DAG construction in this spike is candidate **6th instance** of the identifiability-floor meta-segment (after the five existing instances at L1-L5). Specifically: at the *linguistic-encoding layer*, the joint distribution of event-variables alone is observationally equivalent for SCMs with different causal directions; the marker structure is the *escape mechanism* that grants Level 2 access — analogous to how the loop escapes the observational floor at the operational layer (Instance 1) or how Kalman-Ho ambiguity is the canonical agent-internal architectural floor (Instance 4).

This is a notable structural finding the audit surfaces almost as a side effect: the spike's central theorem is a new instance of the identifiability-floor meta-pattern, at a layer the existing meta-segment doesn't yet cover. Worth flagging as candidate Instance 6 in follow-on routing (the meta-segment was projected at a stable endpoint of 6-8 instances per `spike-identifiability-floor-instance-triage-2026-04-24.md`).
