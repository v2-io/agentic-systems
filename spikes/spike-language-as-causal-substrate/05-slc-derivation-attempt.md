# (SLC) Derivation Attempt — Standard Linguistic Convention via Signalling-Equilibrium

*Strengthening attempt on Theorem 1's most foundational postulate. If this lands, (SLC) lifts from postulate to derived-under-more-foundational-postulates, and Theorem 1 moves from "3 postulates" to "2 postulates + 1 derived." Sketch-level, not formal proof; the strengthening is real but conditional on a specific game-theoretic setup.*

---

## What we're trying to derive

(SLC) **Standard Linguistic Convention**: Natural languages contain a non-empty set of causal markers whose conventional semantic content corresponds to specific levels of Pearl's hierarchy (Level 1 temporal/associational, Level 2 interventional, Level 3 counterfactual).

The question is whether (SLC) is itself derivable from more foundational principles, or whether it must be taken as a postulate about how natural languages happen to be structured.

**Candidate route**: signalling-equilibrium machinery from Lewis 1969 (*Convention*), Skyrms 1996/2010 (*Evolution of the Social Contract* / *Signals*), Steinert-Threlkeld 2018, 2020 (semantic universals via signalling games for quantifier emergence), and the compositional-signalling tradition (Skyrms-Barrett-LaCroix 2018-2020).

If the equilibrium analysis of a cooperative signalling game between causal-reasoning agents produces distinct signal-classes for each Pearl level as a *necessary feature of any payoff-maximizing equilibrium*, then (SLC) is derived rather than postulated.

---

## Three more foundational postulates

The derivation does not eliminate all postulates — it replaces (SLC) with three weaker / more foundational ones:

**(SE1) Cooperative communication between causal-reasoning agents.** Two or more agents who model their environments causally (have structural causal models in Pearl's sense; possibly inexact) communicate with the goal of aligning their causal models. The payoff structure is cooperative — both agents benefit from accurate transmission. *Restrictive*: non-cooperative communication (advertising, deception, negotiation) is out of scope for the derivation. This is the right scope condition for the kind of communication (SLC) is concerned with.

**(SE2) Causal-model-update as the (or a) transmission objective.** The states that agents care to transmit include not just observable facts but causal-model content — relations of dependency, intervention, and counterfactual structure. *Defended empirically*: speakers manifestly do communicate causal claims; the question is what equilibrium-stable encoding emerges.

**(SE3) CHT-induced non-reducibility of Pearl levels in the source models.** The source-domain causal models that agents wish to transmit contain Level-1, Level-2, and Level-3 content that are not derivable from one another (Bareinboim et al. 2022 CHT). This is the same CHT result that does the work in `01-derivation.md` §4 — *applied here to the source domain* rather than to the receiver's recovery.

Under (SE1)–(SE3), the question becomes: *what signal-system emerges at equilibrium?*

---

## The signalling game

Following the structure of Lewis-Skyrms signalling games, instantiated for causal-model transmission:

**Players**: Sender $A$, Receiver $B$.

**States** ($\Theta$): elements of $A$'s causal-model space $\mathcal{M}$ — structural causal models over a shared variable set $V$. We assume $|\mathcal M|$ is finite for tractability (extension to infinite is standard via measure-theoretic generalization).

**Signal alphabet** ($\Sigma$): a finite set of signals $A$ can send. Initially unstructured; equilibrium analysis tells us what structure emerges.

**Sender strategy**: $\sigma_A: \mathcal{M} \to \Delta(\Sigma)$ — probability distribution over signals given state.

**Receiver strategy**: $\sigma_B: \Sigma \to \Delta(\mathcal{M})$ — posterior over models given signal.

**Payoff**: $u(M_A, M_B') = -d_{\text{causal}}(M_A, M_B')$ where $d_{\text{causal}}$ is some causal-model distance — for concreteness, a weighted average of:

- $d_1(M_A, M_B')$: KL divergence between Level-1 (observational) distributions
- $d_2(M_A, M_B')$: divergence between Level-2 (interventional) distributions, e.g. $\sup_X \text{KL}(P_{M_A}(Y | \text{do}(X)) \| P_{M_B'}(Y | \text{do}(X)))$
- $d_3(M_A, M_B')$: divergence between Level-3 (counterfactual) distributions, e.g. $\sup_{X,Y} \text{KL}(P_{M_A}(Y_x | X', Y') \| P_{M_B'}(Y_x | X', Y'))$

The weights $\lambda_1, \lambda_2, \lambda_3 > 0$ encode that agents care about all three levels (this is the substantive consequence of (SE2)).

---

## Key claim and argument

**Claim**: Any Pareto-optimal equilibrium of this game has signal-system $\Sigma$ partitioned into at least three structurally distinguishable subsets $\Sigma_1, \Sigma_2, \Sigma_3$, each corresponding to one Pearl level.

**Argument structure**:

**Lemma A (non-collapse of levels in the source)**: By (SE3) / CHT, two source models $M_1, M_2$ can have identical Level-1 content but differ at Level 2. To transmit the Level-2 distinction, the signal-system must contain a signal-pair $(s_1, s_2)$ with $\sigma_A(M_1)$ assigning positive probability to $s_1$ but not $s_2$, and vice versa, with $\sigma_B(s_1)$ and $\sigma_B(s_2)$ inducing different Level-2 posteriors.

If no such signal-pair exists, then the equilibrium signal-system *cannot* distinguish $M_1$ from $M_2$ at Level 2. The receiver's posterior is identical for both states. Payoff loss: at least the Level-2 component of the distance.

**Lemma B (Pareto improvement via expanding $\Sigma$)**: Suppose an equilibrium has signal-system $\Sigma$ unable to distinguish some Level-2 source-pair $(M_1, M_2)$. Then a modified signal-system $\Sigma' = \Sigma \cup \{s_2'\}$ with a new signal usable in state $M_2$ strictly improves payoff (by removing the Level-2 confusion), provided agents can coordinate on the new signal's meaning. Coordination is possible at equilibrium by hypothesis.

Therefore the original equilibrium was not Pareto-optimal. Contradiction.

By iterating Lemma B for each Level-2 source-pair and each Level-3 source-pair, any Pareto-optimal equilibrium must have signal-classes sufficient to distinguish all Level-2 distinctions in $\mathcal M$ and all Level-3 distinctions in $\mathcal M$.

**Lemma C (structural typing of equilibrium signals)**: At any Pareto-optimal equilibrium of the multi-level transmission game, the signal-system carries enough structure that signals can be *grouped* into subsets that are systematically used for transmitting Level-1, Level-2, and Level-3 content respectively. This grouping is the equilibrium-stable type-system $(\Sigma_1, \Sigma_2, \Sigma_3)$.

The grouping argument: the payoff function decomposes additively over levels ($d = \lambda_1 d_1 + \lambda_2 d_2 + \lambda_3 d_3$). The equilibrium is therefore decomposable — separate equilibria exist for the Level-1, Level-2, Level-3 sub-games. The aggregated signal-system inherits the level-structure from the component sub-games.

**Theorem-target**: Under (SE1)–(SE3), the Pareto-optimal equilibrium signal-system $\Sigma^* = \Sigma_1^* \sqcup \Sigma_2^* \sqcup \Sigma_3^*$ contains structurally distinct signal-classes for each Pearl level. The classes are conventional in Lewis's sense (sender and receiver coordinate on which signal-class encodes which level).

(SLC) follows: the markers in $\Sigma_2^*$ are causal-marker analogues of "because, causes, leads to..."; the markers in $\Sigma_3^*$ are counterfactual analogues of "if X had been, Y would have been..."; the markers in $\Sigma_1^*$ are associational/temporal analogues of "and, then, while...". The specific lexical forms are conventional and language-particular; the existence of distinct categories is equilibrium-necessary.

---

## What this derivation does establish

1. **Existence of distinct causal-marker categories at equilibrium**. Under (SE1)–(SE3), any Pareto-optimal cooperative signalling equilibrium between causal-reasoning agents has structurally distinct signal-classes for each Pearl level. This is the existence claim that (SLC) needed.

2. **The categories are not arbitrary**. They correspond precisely to the levels of Pearl's hierarchy because that is the structure of the content being transmitted. The mapping is forced by the payoff structure + CHT.

3. **Compatible with cross-linguistic universality**. The argument doesn't predict specific lexical forms; it predicts the category structure. Consistent with Comrie 1989 / Dixon 2009 / Cristofaro 2003 typological findings on the near-universality of cause/condition/counterfactual marker categories across natural languages.

4. **Foundationally, what's transmitted vs how it's transmitted**. (SE1)–(SE3) are about the structure of communication-among-causal-agents; (SLC) is about the specific encoding that emerges. The derivation shows the latter follows from the former, which is a real lift in foundationalness.

---

## What this derivation does not establish

1. **Not a formal proof, a sketch**. The equilibrium analysis is at the level of Lewis's original argument plus Skyrms's evolutionary framing. Filling in details — proving Pareto-optimality is the right solution concept here, characterizing the basin-of-attraction under replicator dynamics, showing convergence rates, handling the infinite-state generalization — requires actual game-theoretic work. This spike does not do that work; it sketches the argument.

2. **Not the specific lexical forms**. The argument predicts category existence, not the specific words. English's "because" / "if X had been, Y would have been" are conventional; other languages have different lexical realizations of the same categories. The derivation is consistent with this; it does not predict the lexicon.

3. **Not single-agent emergence**. The signalling game requires two cooperating agents. A solitary intelligence reasoning alone doesn't need to externalize causal-marker categories. The derivation explains the *communicative* emergence of (SLC), not its *cognitive* emergence (if it has one).

4. **Restricted to cooperative communication**. (SE1) is a substantive scope condition. Non-cooperative communication (deception, persuasion, advertising) plausibly destabilizes the equilibrium argument — in deceptive contexts, the sender may have incentive to *blur* level distinctions. This is a real limit; (SLC) is then defended only for the cooperative-communication core, with the non-cooperative usage understood as parasitic on the cooperative norm (Grice 1975 cooperative principle plays this role in pragmatics literature).

5. **Restricted to causal-reasoning agents**. Agents who don't reason causally don't have causal models to transmit; the signalling game doesn't apply. This is the right scope — the derivation explains causal-marker emergence in communities of causal reasoners, not in general communication systems.

6. **Does not derive (SC) or (CS)**. Speaker-commitment (SC) and compositional structure (CS) are not addressed. (SC) is a further property of how speakers use markers once the markers exist; (CS) is about how marker-bearing expressions compose. Both remain postulates of Theorem 1 after this derivation.

---

## The strengthening of Theorem 1

Theorem 1 as stated in `01-derivation.md` rests on three postulates: (SLC), (SC), (CS). After this attempt, the dependency restructures:

> **Theorem 1 (revised dependency).** Under {(SE1) + (SE2) + (SE3) + (SC) + (CS)}, the function $\mathcal{C}$ defined in §3 of `01-derivation.md` recovers Pearl Level 2 content from natural-language text that is not derivable from any Level 1 summary.

This is a strengthening because (SE1)–(SE3) are *prior to* (SLC). They explain why (SLC) takes the form it does; (SLC) is no longer a brute postulate but a derived consequence of the more foundational structure of cooperative causal communication.

The number of postulates went up (3 → 5), but the *foundationalness* of the postulates is greater — (SE1)–(SE3) are about communication structure rather than about linguistic convention, which is one floor more general.

**Honest assessment**: this is a "succeed-at-claim with caveats" yield. The sketch-level argument is convincing structurally, but the formal proof-level argument requires game-theoretic work this spike does not do. Whether to call it (a) "derivation under sketch-level argument", (b) "promotion of (SLC) from postulate to consequence", or (c) something in between is a judgment call. I lean toward (b) on the grounds that the structural argument is solid and the formal-proof-level work is filling-in-details rather than additional substance — but this is the place a careful reviewer would push hardest.

---

## Honest residuals (open work)

**R1 — Formal game-theoretic proof.** Filling in the equilibrium analysis (Pareto-optimality, replicator dynamics, ESS conditions). Tractable; standard methods apply.

**R2 — Cross-linguistic prediction**. The argument predicts category-existence universals; testing this against comprehensive typological surveys (Cristofaro 2003 *Subordination*; Comrie 1989; Dixon 2009; *World Atlas of Language Structures*) would empirically validate or constrain the derivation. Empirical work, not theoretical.

**R3 — Non-cooperative extension**. Whether (SE1)'s cooperative-communication restriction can be relaxed. Pragmatics literature (Grice 1975; the Wilson-Sperber relevance-theory tradition) treats non-cooperative usage as parasitic on cooperative norms — formalizing this in the signalling-equilibrium frame is open work.

**R4 — Connection to (SC).** Speaker-commitment (SC) is left as a postulate. There may be a parallel derivation: at equilibrium, signal use that violates the conventional-content-commitment is destabilizing — receivers learn to discount unreliable senders. This would close the (SC) gap via reputation/replicator-dynamics arguments. Worth a separate spike.

**R5 — Pre-loop LLM connection.** The derivation tells us causal-marker categories emerge in communicating populations. LLMs trained on the linguistic output of such populations inherit the categories. This composes with C4 (causal-IB consequence) to give a sharper claim: *LLMs' learned representations of causal markers preserve the equilibrium-categorical structure to the extent that structure has predictive value for next-token prediction*. Promising; needs work.
