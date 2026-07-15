---
slug: scope-and-or
type: scope
status: robust-qualitative
depends:
  - def-strategy-dimension
  - der-chain-confidence-decay
stage: draft
---

# Scope: AND/OR Combination Scope

We restrict to environments where the causal combination of strategy steps is approximately conjunctive (AND: all parents required) or disjunctive (OR: any parent sufficient), without strong interaction effects between parents. Each node is assigned a combination type by answering the causal question: "if I remove one parent, can this node still be achieved?" Yes → OR. No → AND. With single-parameter edges (one number per edge rather than a $2^k$ conditional probability table), this gives $k$ parameters per node instead of an exponential explosion.

The scope is honest about being a *restriction*, not a derivation, though it converged independently across three different formalism attempts ( #def-strategy-dag). The excluded case — complementarity, substitutability, and interaction effects between parents (synergistic drug interactions where combined effect exceeds the sum; complementary goods where neither is useful alone; strategic surprise where action combinations matter more than individual actions) — requires richer combination rules and is named as a legitimate divergence point for future work. The parsimony argument is that for binary-outcome nodes, AND and OR form a complete Boolean basis (DNF/CNF normal forms), and under bounded cognition ( #form-information-bottleneck) the agent needs the most expressive low-parameter representation. AND/OR is the natural candidate; for continuous or multi-valued outcomes the same completeness properties do not necessarily hold (min/max or additive/multiplicative are natural analogs but their completeness is open).

## Formal Expression

*[Scope Narrowing (and-or-scope)]*

Under this restriction, strategy nodes combine parent contributions via:

**AND-node** (all parents must succeed):

$$P(v \mid \text{parents}) = \prod_{i \in \text{pa}(v)} p_{iv} \cdot P(i)$$

**OR-node** (any parent sufficient):

$$P(v \mid \text{parents}) = 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot P(i))$$

The combination type $\gamma(v) \in \{\text{AND}, \text{OR}\}$ is assigned per node. The causal question determines assignment: "if I remove one parent, can $v$ still be achieved?" YES → OR. NO → AND.

## Epistemic Status

*Robust qualitative.* This scope narrowing converged independently across three formalism attempts (track-a/00, track-a/02, track-a/03). It captures the dominant structure in most planning domains. The excluded case — complementarity, substitutability, interaction effects between parents — requires richer combination rules and is a legitimate divergence point for future work.

The AND/OR restriction with single-parameter edges gives $k$ parameters per node (one per parent edge) instead of $2^k$ for a general conditional probability table. This parsimony is motivated by bounded cognition ( #form-information-bottleneck): agents with limited representational capacity are forced toward low-parameter models.

## Discussion

**Why AND/OR and not alternatives.**

*Why not Noisy-OR universally.* The first formalism attempt used noisy-OR for all nodes. This **systematically overestimates conjunctive structures**:

| Structure | Noisy-OR | AND | Reality |
|-----------|----------|-----|---------|
| 3 required KRs at $p = 0.95, 0.90, 0.99$ | 0.99995 | 0.846 | ~AND |

The noisy-OR model cannot represent "all of these are required." This was the primary motivation for the AND/OR revision.

*Why not WEIGHTED combination.* A clean-slate formalism (track-a/02) introduced $P(v) = \min(1, \sum \alpha_{iv} \cdot p_{iv} \cdot P(i))$ to handle k-of-n thresholds. This reintroduces a two-parameter estimation problem ($\alpha$ weights per edge). If k-of-n semantics are genuinely needed, nested AND/OR structure can represent them: group alternatives into OR-nodes, then AND the groups. This keeps estimation localized to the node taxonomy rather than spreading it across a new per-edge parameter.

**The parsimony argument.** For binary-outcome nodes, AND and OR form a complete Boolean basis — any Boolean combination can be decomposed into layers of AND/OR (disjunctive/conjunctive normal form). Under bounded cognition, the agent needs the most expressive $O(k)$-parameter representation. AND/OR is the natural candidate. This is a parsimony-motivated hypothesis, not a derived necessity — see #deriv-graph-structure-uniqueness for the full argument and its limitations.

**What this scope excludes.** Environments with strong interaction effects: where the value of combining parent contributions is not separable into independent per-parent terms. Examples: synergistic drug interactions (combined effect exceeds sum of individual effects), complementary goods (neither is useful alone), strategic surprise (the combination of actions matters more than any individual action). These require richer parameterizations within the strongly motivated graphical structure ( #def-strategy-dag) — a direction for future work.

## Working Notes

- The AND/OR assignment per node ($\gamma(v)$) is itself uncertain and should be updateable. A node assumed to be OR (alternatives) might turn out to be AND (all required) when the agent discovers unexpected dependencies. $\gamma$ reclassification is rare — it requires strong structural evidence — and operates on a slower timescale than edge-weight updates.
- The parsimony argument applies cleanly to binary outcomes. For continuous or multi-valued outcomes, AND/OR doesn't have the same completeness properties. The natural continuous analogs might be min (AND) and max (OR), or additive and multiplicative combination. Whether there's a completeness result for these is an open question.
- K-of-n thresholds are genuinely common (e.g., "need at least 3 of 5 team members available"). The nested AND/OR representation works but can be verbose. Whether this verbosity is a problem in practice (given bounded cognition constraints) is empirical.

### Incidental audit gold (lift 2026-05-31, A8 batch)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / figure material, kept separate from certified theory-fix findings. **Coverage:** 6 dirs reached a digested reflection (Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-451729-batch-09; Claude, AUDIT-WORKING-963715-batch).

#### 1. Candidate Brief prose / pre-prose

- **The "keys AND door / keys AND car" worked gloss of why Noisy-OR fails.** "If you use Noisy-OR to model a strategy where *all* prerequisites are required (Get key *and* Unlock door to Open door), the math breaks down catastrophically: 90% sure of the key, 95% the door, Noisy-OR says $1-(1-0.9)(1-0.95)=0.995$ — *more* confident than either prerequisite alone, which is mathematically suicidal for a planner. An AND gate correctly says $0.9\times0.95=0.855$ — *less* confident" (Gemini, AUDIT-WORKING-829314; the "keys AND car" variant at Gemini, AUDIT-WORKING-849201; "acquire funding AND hire team to launch product" at Claude, AUDIT-WORKING-963715). A concrete everyday anchor for the noisy-OR-overestimation table already in Discussion.

#### 2. Candidate Discussion

- **"Strategies are not Bayesian belief networks turned sideways."** The sharpest framing of why planning needs AND *and* OR, not universal Noisy-OR: "the logic of causation in a *plan* is much more brittle than the logic of evidence in a *diagnosis*. If one piece of evidence is missing, a diagnosis can still be highly probable; if one required step is missing, a plan fails with probability 1." Noisy-OR is the dominant combination function in PGM tooling (medical diagnosis etc.) precisely because evidence is forgiving; strategy is not (Gemini, AUDIT-WORKING-829314). A candidate Discussion paragraph distinguishing $\Sigma_t$-combination-semantics from $M_t$-style belief networks.
- **The PGM-tooling critique deserves more prominent positioning.** "AAT's claim that noisy-OR systematically overcounts in conjunctive structures is a specific technical critique of a widely-used formalism (BNT, Netica, most Bayesian-network tools), not just an internal modeling choice — and deserves more prominent positioning as a critique of standard PGM tooling for planning applications" (Claude, AUDIT-WORKING-963715). A framing-emphasis suggestion: the rejection is a contribution, not housekeeping.

#### 3. Follow-up items

- **A native k-of-n threshold node type under MDL pressure.** Strong convergence (3 substrates) that pure AND/OR forces combinatorial blow-up for threshold logic: "3-of-5 servers healthy" needs $\binom{5}{3}=10$ AND-branches into one OR-node, a large spike in $DL(\Sigma_t)$ — a tension between *node-type* parsimony (only 2 types) and *graph-size* parsimony. The prediction: AAT may be forced to introduce a native "threshold / k-of-n" node primitive to satisfy the information-bottleneck constraint of `#form-strategy-complexity-cost`, and the k-of-n verbosity note should be lifted from Working Notes into Discussion (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-773921; Codex/Claude, AUDIT-WORKING-526815). Currently the Working Notes hold this as "empirical whether verbosity is a problem"; the auditors lean toward it being a real limitation worth a primitive.

#### 4. Readers often ask / wonder

- **Where else do these formulas live?** The AND/OR combination rules were independently recognized as "standard in reliability engineering and fault tree analysis" (Gemini, AUDIT-WORKING-849201). A reader orienting on prior-familiarity lands here — a candidate one-line situating note.

#### 5. Candidate figures

- **Three-region scope diagram.** "Pure AND / pure OR / outside-current-scope (thresholds, interactions)", paired with the parameter-count contrast (single-parameter edges $O(k)$ vs full CPTs $O(2^k)$) to make the parsimony motivation visual and to make the *excluded* region legible as non-rare (Codex/Claude, AUDIT-WORKING-526815).

#### Off-ramp (NOT gold — flagged for the certified track)

- **The $\gamma$-assignment test misclassifies threshold structures.** The test "if I remove one parent, can $v$ still be achieved? YES → OR, NO → AND" mis-handles a 3-of-5 requirement: removing one parent may still leave success possible (so the test says OR), yet no single parent is sufficient (so it is not really OR). Suggested repair: split into separate questions — are *all* parents necessary, is *any one* sufficient, or is this a threshold/interaction case outside pure AND/OR (Codex/Claude, AUDIT-WORKING-526815). A real precision gap in a stated rule.
- **Boolean completeness ≠ compact representation.** The parsimony argument leans on "AND/OR form a complete Boolean basis (DNF/CNF) and are therefore the natural $O(k)$-parameter representation." An auditor flagged that functional completeness does *not* imply *compact* representation — arbitrary Boolean functions can require exponentially large AND/OR formulas or auxiliary nodes (the k-of-n verbosity is one instance) — so the completeness claim should be scoped or softened (Codex/Claude, AUDIT-WORKING-526815). Both items are wording/scope tightenings on a `robust-qualitative` segment; routed for the lead to judge.
