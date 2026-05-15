# Derivation — Pearl Level 2 Content is Structurally Recoverable from Natural Language Text

*Main result of the spike. Conditional theorem under three named postulates from linguistics. The non-trivial work is the CHT (Causal Hierarchy Theorem) application that lifts the result from "the text labels causal claims" to "the labels carry information not derivable from any associational summary."*

---

## 1. The claim, sharpened

Joseph's hypothesis, restated in a form that admits a derivation:

> **(H)** For any natural-language text $T$ satisfying ordinary conditions on use, there exists a computable function $\mathcal{C}$ such that $\mathcal{C}(T)$ is a Pearl-style structural representation containing **Level 2 (interventional) content** that is **not derivable** from any Level 1 (associational) summary of $T$. The function $\mathcal{C}$ is purely structural — it requires sequential parsing and dependency tracking, no agent-loop, no model-of-world maintenance, no recursive reasoning.

The two non-trivial claims fused into (H) are:

- **(H.a) Structural recoverability**: $\mathcal{C}$ exists and is mechanical.
- **(H.b) Non-reducibility**: $\mathcal{C}(T)$ carries Level 2 content that is **strictly more** than the joint distribution of $T$'s tokens encodes at Level 1.

(H.a) without (H.b) would be a labeling tautology — *of course* you can label any text with anything you want and call the labeling "structural." The teeth of (H) are in (H.b): the Level 2 labels carry information not retrievable from the unlabeled text by Bayesian inference alone.

The work below establishes (H) under three postulates from linguistic theory.

---

## 2. The three postulates

These are stated as postulates rather than derived, because they are facts about how human communication systems developed — not facts derivable from non-linguistic first principles. Each is well-defended in the linguistic literature.

### (SLC) Standard Linguistic Convention

Natural languages contain a non-empty set of **causal markers** whose conventional semantic content corresponds to specific levels of Pearl's hierarchy:

| marker (English; analogues in all known natural languages) | Pearl level | semantic commitment |
|---|---|---|
| *and, then, after, while* | Level 1 (temporal/associational) | $X$ and $Y$ co-occurred / preceded |
| *because, since, due to, owing to, leads to, causes, makes (it the case that)* | Level 2 (interventional) | $X$ caused $Y$; absent $X$, $Y$ would not have occurred (intervention semantics) |
| *if X had been, Y would have been; were X, Y would be* | Level 3 (counterfactual) | per Lewis 1973 / Stalnaker 1968 nearest-world semantics; $P(Y_x \mid X', Y')$ |
| *might have; could have; would still have* | Level 3 (modal) | counterfactual under possible-worlds restriction |

The claim of (SLC) is that these markers have **conventional semantic content** in Pearl's sense — established by linguistic convention, recoverable by standard compositional-semantics machinery (Karttunen 1973 on presupposition; Stalnaker 1978 on assertion; Lewis 1973 on counterfactuals; Kratzer 1981 on modals).

(SLC) is not derivable from non-linguistic principles. It is a fact about how communication systems among causal reasoners develop: any community of agents who model their environment causally and need to transmit causal models will develop linguistic markers for each Pearl level, because the markers carry information the agents need to transmit. This is a *communicative-functional* defense, not a first-principles derivation.

### (SC) Speaker Commitment

When a competent speaker uses a causal marker in a declarative context (not under irony, not under quotation, not under a question operator), they are **committed** to the conventional semantic content of the marker. This is the standard Gricean / Stalnakerian background assumption (Grice 1975 cooperative principle; Stalnaker 1978 assertion-as-conversational-update).

(SC) does serious work: it bridges from *the text contains marker M* to *the speaker has asserted the Pearl-level content of M*. Without (SC) the speaker's marker could be ironic, performative-without-commitment, or otherwise stripped of force. (SC) is empirically defended — speakers who use causal markers and then disclaim the causal commitment ("I said 'because' but I didn't mean to suggest *causation*") are *correcting themselves*, which presupposes the commitment was made.

### (CS) Compositional Structure

The semantic content of a text composes from the semantic content of its constituents according to known compositional-semantics rules (Montague 1973; Discourse Representation Theory, Kamp 1981, Kamp-Reyle 1993; Segmented DRT, Asher-Lascarides 2003).

(CS) ensures the text's overall causal content is **assembled from** the markers and the referents they connect, rather than being some emergent property unrelated to the marker-level commitments. Compositionality is not always exceptionless (idioms, irony, metaphor), but it is the load-bearing rule for declarative discourse, which is the scope of this spike.

---

## 3. Construction of $\mathcal{C}$

Given a text $T = (t_1, t_2, \ldots, t_n)$, the function $\mathcal{C}$ proceeds in five mechanical stages. Each stage is implemented in deployed NLP pipelines today (with known error rates) — the construction is not aspirational.

**Stage 1: Syntactic parsing.** Produce a dependency parse $\Pi(T)$. Standard machinery (Universal Dependencies, e.g., spaCy / Stanza / Trankit).

**Stage 2: Discourse-referent extraction.** Produce a set $\mathcal{V}(T)$ of discourse referents — entities, events, propositions introduced by $T$. Standard DRT-style construction (van der Sandt 1992; Kamp-Reyle 1993).

**Stage 3: Coreference resolution.** For each pronoun and definite description in $T$, identify its antecedent in $\mathcal{V}(T)$. Standard coreference resolvers (Lee et al. 2017, etc.).

**Stage 4: Discourse-relation extraction.** For each clause-to-clause or sentence-to-sentence boundary, identify the discourse relation (Cause, Result, Condition, Counterfactual, Contrast, Elaboration, ...) from the explicit markers (per SLC). Where no explicit marker is present, record *no relation* — this spike does not depend on implicit-relation recovery.

**Stage 5: Graph assembly.** Construct a labeled directed graph $\mathcal{C}(T) = (\mathcal{V}(T), \mathcal{E}_1 \cup \mathcal{E}_2 \cup \mathcal{E}_3)$ where:

- $\mathcal{E}_1$ — edges from Level-1 markers (temporal, additive). Carry no interventional commitment.
- $\mathcal{E}_2$ — edges from Level-2 markers (*because*, *causes*, *leads to*, *prevented*, *resulted in*). Carry interventional commitment per (SC).
- $\mathcal{E}_3$ — edges from Level-3 markers (counterfactual conditionals, modals). Carry counterfactual commitment.

The output is a **labeled tripartite directed graph** over discourse referents, with each edge tagged by the Pearl level of the marker that produced it.

---

## 4. The Level 2 content is not Level 1 — the CHT argument

This is where (H.b) is established. We need to show that $\mathcal{E}_2$ carries information **not derivable** from $\mathcal{E}_1$ alone (or from any Level-1 joint distribution over $\mathcal{V}(T)$).

Bareinboim, Correa, Ibeling & Icard's **Causal Hierarchy Theorem** (CHT, 2022, *On Pearl's Hierarchy and the Foundations of Causal Inference*) establishes this in full generality at the level of structural causal models: there exist pairs of SCMs that induce identical Level-1 (observational) distributions but differ at Level 2. The level above is not measure-theoretically reducible to the level below.

**Lemma 1 (Two texts, same observations, different interventions).**
Consider:

- $T_A$: "The water in the kettle boiled, and the kettle whistled."
- $T_B$: "The water in the kettle boiled, **causing** the kettle to whistle."
- $T_C$: "The kettle whistled, and the water in the kettle boiled."
- $T_D$: "The kettle whistled, **causing** the water in the kettle to boil."

Under standard linguistic interpretation:

- $T_A$ and $T_C$ encode the same Level 1 content (co-occurrence of two events). The difference is narrative ordering, which (CS) cannot fully exploit because temporal-adverbial markers are weaker than causal markers and admit narrative reordering.
- $T_B$ encodes the same Level 1 content as $T_A$ and $T_C$ **plus** Level 2 content: intervening to prevent the water from boiling would prevent whistling.
- $T_D$ encodes the *opposite* Level 2 content: intervening on whistling affects boiling — physically false in the kettle case, but the text asserts it.

Under (SLC) + (SC) + (CS), $T_B$ and $T_D$ are not Level-1-equivalent to $T_A, T_C$ — but more importantly, **$T_B$ and $T_D$ are not Level-1-equivalent to each other** despite mentioning identical events. Their distinction lies entirely in the directionality of the Level-2 commitment.

By CHT, no inference from Level 1 distributions over $\{\text{boil}, \text{whistle}\}$ can distinguish $T_B$ from $T_D$. The distinction is **carried by the marker structure**, not by the token co-occurrence statistics.

**Conclusion of Lemma 1**: There exist texts $T_B, T_D$ with identical token-co-occurrence Level-1 content whose Level-2 content (the asserted causal direction) is non-reducible by any Level-1 analysis. The marker structure carries the distinguishing information.

**Theorem 1 (Structural recoverability of Pearl Level 2 content from text).**
Under (SLC) + (SC) + (CS), the function $\mathcal{C}: T \mapsto (\mathcal{V}(T), \mathcal{E}_1, \mathcal{E}_2, \mathcal{E}_3)$ defined in §3:

(i) Is **computable** from $T$ by a deterministic procedure (syntactic parsing + DRT-referent extraction + coreference + discourse-relation extraction).

(ii) Carries **Level 2 content** in the Pearl sense: $\mathcal{E}_2$ encodes interventional commitments by the speaker.

(iii) The Level 2 content $\mathcal{E}_2$ is **not derivable** from any Level 1 summary of $T$, by CHT applied to the example pairs $T_B$ vs $T_D$ in Lemma 1 (which generalize: every Level-2 marker pair contributes a CHT-style non-reduction example).

(iv) The procedure requires **no agentic interiority**: no model-of-world maintenance across the text; no recursive reasoning; no loop. The procedure is sequential pattern recognition (parse + label) and dependency tracking (anaphora + discourse-relation chaining).

**Proof.**
(i) is established by Stages 1–5 of §3 — each stage is implemented by deployed NLP machinery. The procedure terminates in time polynomial in $|T|$.

(ii) follows from (SLC): the Level 2 markers have conventional Level 2 semantic content. (SC) ensures the speaker is committed to that content. (CS) ensures the text-level content composes from the marker-level commitments.

(iii) follows from Lemma 1 and the general CHT result: the marker-distinguishing information $T_B$-vs-$T_D$ is Level 2, and Level 2 is not derivable from Level 1 by CHT.

(iv) follows by inspection of Stages 1–5: none requires a maintained agent state. Each stage is a context-window-bounded pattern recognition or local-dependency operation. $\square$

---

## 5. What Theorem 1 does and does not establish

**Establishes** (under SLC + SC + CS):

1. **The Level 2 content is in the text.** Not derived from the text by an active reasoner — *in* the text, structurally. The text is a Pearl-Level-2-information-carrier.

2. **Recovery is substrate-agnostic.** A purely structural parser (no interiority, no loop, no model-maintenance) recovers it. So does any system that performs the same operations regardless of the architecture (transformer, RNN, hand-coded parser, person reading carefully).

3. **The recovery preserves the speaker's commitments**, not the reader's interpretation. The speaker asserted a causal direction; the text preserves the assertion; the reader receives it intact at the structural level (whether they *believe* it is a separate question, downstream of recovery).

**Does not establish**:

1. **That the Level 2 commitment is *true*.** $T_D$ ("the kettle whistled, causing the water to boil") encodes a Level 2 commitment that is causally false. Recovery is not verification. The text carries the speaker's assertion of a causal model; whether that model corresponds to the world is a separate, non-linguistic question.

2. **That every substrate recovers it faithfully.** A transformer trained on causal language may or may not deploy the encoded causal content in its generative process in a way that *uses* the Level 2 commitments. This is the right reformulation of Pearl's objection — see §6.

3. **That the recovery is unique.** Different parsers, different DRT-formalizations, different discourse-relation taxonomies will produce different graphs. The structural existence and non-reducibility properties are invariant; the specific graph topology is not.

4. **That the recovery is complete.** Implicit causal relations (carried by genre conventions, narrative coherence, real-world knowledge) are NOT recovered by the procedure of §3, which only uses explicit markers. The result is *lower-bound*: at least the explicit-marker content is recovered. Implicit content recovery requires additional machinery (and is what existing LLMs partly do).

---

## 6. The reframed Pearl objection

The standing form of Pearl's objection — *"LLMs only see associations, therefore cannot reason causally"* — rests on a category error that Theorem 1 makes precise.

Pearl's hierarchy is about **the kind of data the system has access to**: observational, experimental, structural. The argument is that observational data alone cannot ground Level 2 reasoning. This is correct (and is exactly CHT).

The category error is the assumption that **natural language text *is* observational data**. It is not. Natural language text is a **performative carrier of asserted causal content** by speakers committed to Level 2 (and Level 3) claims under (SLC) + (SC) + (CS). The "observational data" frame mischaracterizes the source material.

The honest reformulation:

> *Pre-loop LLMs trained on natural-language corpora have access to Level 2 (and Level 3) content **as encoded by speakers in the training text**. Whether they deploy this content faithfully in their generative process — whether the causal commitments they assert in output match the structural commitments in their training input — is an empirical question about generative faithfulness, not a categorical question about Pearl-hierarchy access.*

This reframing is structurally identical to the AAD-internal distinction between **encoded content** and **deployed content**: AAD's [`#deriv-causal-ib-lmi`](../../01-aat-core/src/deriv-causal-ib-lmi.md) and the broader IB machinery establish that an IB-optimal compressor of causally-structured data **preserves the causal structure to the extent that structure has predictive value**. The encoded content is in the compressor; whether it is faithfully deployed in downstream generation is a separate question (the deployment-faithfulness question).

Theorem 1 also composes with [`#der-loop-interventional-access`](../../01-aat-core/src/der-loop-interventional-access.md): the loop provides **fresh** Level 2 access (interventions the agent itself performs in the loop). The training-encoded Level 2 access is **inherited** — the agent does not need to perform interventions to have Level 2 content available, because the speakers in its training corpus performed (or asserted) interventions and committed to them in text. These two sources of Level 2 access are **additive in the sense of contribution-to-availability**, not in the sense of cancellable or substitutable: the inherited content is fixed at training time; the fresh content is generated session by session.

---

## 7. Open questions surfaced by the derivation

These are honest gaps; recording them avoids fall-through into "the theorem fixed everything." None breaks Theorem 1; each names a question Theorem 1 does not answer.

**Q1 — Implicit-relation recovery.** Theorem 1 covers only Level 2 content from *explicit markers*. Real natural language carries massive implicit causal content (genre conventions, narrative coherence, real-world knowledge). Recovering implicit causal content requires machinery beyond §3's procedure. How much of natural-language Level 2 content is explicit-marker-bearing vs implicit? This is empirically measurable (PDTB, RST-DT annotations exist).

**Q2 — Faithfulness of LLM deployment.** Theorem 1 establishes the content is *in* the text and *recoverable* by structural means. It does not establish that LLMs trained on such text deploy the content faithfully in generation. Empirical work (Causal Parrots, CLadder, CounterBench, Executable Counterfactuals) bears on this question; Theorem 1 says the *upper bound* of LLM causal capacity from training is bounded below by the discourse-DAG content of the training corpus, but actual deployment can underperform this bound.

**Q3 — Speaker-commitment faithfulness in the training distribution.** (SC) assumes speakers are committed to their causal markers. The training corpus includes a long tail of non-cooperative usage (irony, fiction, lies, error, hedged speculation). What fraction of training-corpus Level-2 commitments are well-grounded vs spurious? This is empirically measurable but Theorem 1 does not address it.

**Q4 — Cross-linguistic universality.** (SLC) is stated for "natural languages" — implicitly assumed universal. There is substantial literature on causal-marker inventories across languages (Comrie 1989, Dixon 2009, Cristofaro 2003) supporting near-universality of cause/condition/counterfactual marker categories, but the formal claim is not derived here. The embeddings paper's cross-linguistic robustness across 8 typologically diverse languages is suggestive but not dispositive.

**Q5 — Composition with the κ × 𝒜 bound.** Theorem 1 sits at training-time / corpus level. The AAD κ × 𝒜 architectural-bias bound ([`#scope-observation-ambiguity-modulation`](../../01-aat-core/src/scope-observation-ambiguity-modulation.md), [`#deriv-observation-ambiguity-bias-bound`](../../01-aat-core/src/deriv-observation-ambiguity-bias-bound.md)) sits at deployment-time / forward-pass level. How do the two compose? Tentative answer: κ × 𝒜 bounds the *deployment-faithfulness loss*, not the encoded content. The encoded content remains in the corpus and is in principle recoverable by the model; the bound says deployment may not fully use it under Class 2/3 architectures. This composition needs explicit work.

These five open questions are the natural follow-on routing — see [`04-no-gos-and-followon.md`](04-no-gos-and-followon.md).
