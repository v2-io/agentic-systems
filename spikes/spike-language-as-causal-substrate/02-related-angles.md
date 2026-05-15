# Related Angles — Reichenbachian Inheritance, ICM Time-Asymmetry, and Causal-IB

*Three additional angles surveyed alongside the main derivation in `01-derivation.md`. Each gives a different kind of leverage on Joseph's hypothesis. C2 is rigorous but weaker than it sounds; C3 yields directional asymmetry but not the quantitative lower bound; C4 was already AAT-internal but unsurfaced and connects the result to existing machinery.*

---

## C2 — Reichenbachian Inheritance: correlation in text inherits causal structure from source

**Claim**: If two referents $R_1, R_2$ in a natural-language corpus are statistically dependent, then in the **generative process that produced the corpus** there is a causal relation: either $R_1$ causally affected the introduction of $R_2$ (or vice versa), or there is a common cause $C$ in the source-cognitive-process that introduced both.

**Argument**: Reichenbach's Common Cause Principle (RCCP, 1956) states: if $X$ and $Y$ are statistically dependent and not directly causally related, there exists a common cause $C$ such that $X \perp Y \mid C$. Applied to the corpus-generating process:

- Corpora are produced by speaker/writer cognitive processes that select referents and structure text.
- Statistical dependencies among referents in the corpus must trace back through this selection process.
- By RCCP, every such dependency reflects a causal relation in the source — either between referents-as-modeled-in-the-source, or via a shared causal antecedent.

The corpus is therefore a **partial map** of the source-causal-structure. Lossy, biased, incomplete — but **not noise**. Every persistent statistical regularity in natural language is testimony to a causal regularity in the cognitive processes that produced the language.

**Strength**: this gives a foundational reason why bag-of-words distributional semantics works at all — and why it has limits. Distributional semantics captures Level 1 traces of source-Level-2 structure. The traces are real but underdetermine the source.

**Weakness — why this is weaker than it sounds**:

1. **RCCP has known counterexamples** (Cartwright 1979, 1989, Sober-Forster 1987): quantum-mechanical correlations, selection-bias-induced spurious dependencies, faithfully-encoded epiphenomenal correlations. The principle is a defensible methodological default, not a theorem.

2. **The "source" is fragmented and multi-author**. Natural corpora are not produced by a single causal process — they aggregate across millions of speakers with overlapping but distinct causal models. Reichenbach inheritance gives information about the *aggregated* causal-statistical structure, not about any single speaker's model. This is closer to what distributional semantics actually captures.

3. **Faithfulness is a separate assumption**. RCCP-style arguments typically assume *faithfulness* — that statistical independence in the data implies structural independence in the source. Faithfulness can fail (parameter cancellation, deterministic structure). For natural language, faithfulness is approximately but not universally true.

**Honest conclusion**: C2 is a *plausibility-strong* argument for why distributional methods capture some causal structure, not a derivation that they capture *enough* causal structure for any particular purpose. It justifies treating corpus statistics as causally informative; it does not establish a quantitative lower bound on the causal content recoverable.

**Connection to C1**: C2 is *complementary* to C1. C1 establishes that explicit-marker content is in the text directly (no inheritance argument needed). C2 establishes that implicit content — statistical structure without explicit markers — also carries causal information from the source. The two angles cover the two routes by which language transmits causal content:

- **C1 route**: speaker commits to causal claim → marker in text → recoverable by structural parsing.
- **C2 route**: speaker's causal model shapes referent selection → statistical structure in text → recoverable (lossily) by distributional analysis.

C1 is the **stronger** route — it has CHT-style non-reduction. C2 is the **broader** route — it covers content without explicit markers, but at the cost of weaker recovery guarantees.

---

## C3 — ICM Time-Asymmetry: forward-language compresses better than reversed-language, by an amount linked to causal information

**Setup**. Janzing & Schölkopf (*Causal Inference Using the Algorithmic Markov Condition*, 2010; *Elements of Causal Inference*, Peters-Janzing-Schölkopf 2017) develop **Independence of Causal Mechanism (ICM)** as a postulate distinguishing causal direction by algorithmic complexity. The principle:

For a true causal direction $X \to Y$, the conditional $P(Y \mid X)$ and the marginal $P(X)$ are *algorithmically independent*: knowing one does not shorten the description of the other. In the anti-causal direction $Y \to X$ (reading the same joint backwards), $P(X \mid Y)$ and $P(Y)$ are **not** algorithmically independent — there is a description-length penalty.

Formally (in the algorithmic-information version):
$$K(P_{XY}) = K(P_X) + K(P_{Y \mid X}) - O(1) \quad \text{(causal direction)}$$
$$K(P_{XY}) \;\lneq\; K(P_Y) + K(P_{X \mid Y}) - O(1) \quad \text{(anti-causal direction)}$$

The asymmetry between the two factorizations is the empirical signature of causal direction.

**Applied to language**. Joseph's intuition: *"giving an LLM a prompt with all of the words in reverse order is going to cause a great deal of confusion."* This is exactly the ICM signature applied to discourse:

- **Forward discourse generation** is ICM-aligned: the writer's "priors" (which referent to introduce first) are approximately independent of the "mechanisms" (how subsequent content depends on prior content). The writer picks a topic, then unfolds. Anaphoric resolution, definite-article-licensing, conditional clauses, narrative ordering — all are forward-directional.

- **Reverse discourse** breaks several mechanisms structurally:
  - Pronouns appear before their antecedents (anaphora can't resolve)
  - Definite descriptions appear before the entities are introduced
  - Conditional clauses have antecedents after consequents
  - Narrative ordering is reversed (effect before cause)

Each of these breakages requires a *longer description* in the reverse direction to encode equivalent content. Empirically, reverse-language language models have substantially higher perplexity than forward-language ones on the same data (Kaplan et al. 2020 scaling laws, and follow-on work).

**Theorem-target (C3)**:
$$K(L_{\text{forward}}) + I_{\text{causal}} \;\le\; K(L_{\text{reverse}})$$
where $L$ is a natural-language corpus and $I_{\text{causal}}$ is the causal information content of $L$ (some appropriate measure).

**What actually derives**:

The **directional asymmetry** ($K(L_{\text{forward}}) < K(L_{\text{reverse}})$) is derivable under ICM applied to the discourse-generative process — it follows from forward-anaphora-licensing alone, which gives a description-length advantage to the forward direction. This much is solid.

**What does not derive**:

The **lower bound by causal information content** ($I_{\text{causal}}$ appearing as a specific quantity on the LHS) is **not** derivable from the postulates available. The lower bound requires:

(i) A formal definition of "causal information content of a corpus" — which is non-trivial. Pearl-hierarchy levels don't translate cleanly to algorithmic-information quantities. The closest candidate is **directed information** (Massey 1990, Marko 1973), but its application to discourse causal-structure is not yet worked out.

(ii) A theorem connecting directed information of the discourse-DAG to the algorithmic-complexity-asymmetry of forward vs reverse compression. This theorem would have to do real work — it requires linking the structural causal content (C1's $\mathcal{E}_2$ edges) to a quantity that appears in the compression bound.

This is **not** a no-go in the strong sense. It is a **work-not-yet-done**, and the work has a natural home: extending the existing AAT machinery on causal-IB ([`#deriv-causal-ib-lmi`](../../01-aat-core/src/deriv-causal-ib-lmi.md), which uses directed information / mutual-information-rate machinery) to the discourse-DAG case.

**Honest summary of C3**: directional asymmetry is derived; quantitative-causal-lower-bound is a follow-on. The empirical signature (reversed-language is harder for LLMs) is consistent with the postulate but does not pin down the constant.

---

## C4 — Causal-IB Consequence: IB-optimal compressors of natural language preserve discourse-DAG structure to the extent it has predictive value

This angle was **already AAT-internal** but unsurfaced — it follows directly from existing AAT machinery applied to linguistic data. The contribution of this spike is to make the connection explicit and route it back to the logogenic-agents OUTLINE.

**Setup**. The AAT segment [`#deriv-causal-ib-lmi`](../../01-aat-core/src/deriv-causal-ib-lmi.md) establishes that under information-bottleneck compression of causally-structured data, the bottleneck-optimal representation preserves the causal structure proportional to its predictive contribution. The setup is general — it applies to any data source with underlying causal structure and any IB-optimal compressor.

**Instantiation on natural-language data**. Take the data source to be a natural-language corpus and the compressor to be any sequence model trained with a next-token-prediction objective (transformer LLM, RNN-LM, etc.). The IB-optimality of next-token-prediction-trained models is approximate but well-studied (Tishby-Zaslavsky 2015; Saxe et al. 2019; Goldfeld et al. 2019, with caveats).

Then by direct instantiation of `#deriv-causal-ib-lmi`:

**Corollary (Embedding-encoded causal structure)**:
Under approximate IB-optimality of next-token-prediction training, an LLM's intermediate representations preserve the discourse-DAG structure of the training corpus to a degree quantified by the predictive contribution of the discourse-DAG to next-token entropy.

This is a *non-trivial* claim because:

1. **It gives a quantitative target.** The amount of causal structure preserved is bounded below by the predictive value, which is empirically measurable (ablation studies on causal-marker content, controlled discourse-DAG perturbations).

2. **It connects the spike result to existing AAT machinery.** The result is not a new theorem — it is the existing `#deriv-causal-ib-lmi` instantiated on a particular data domain. The AAT framework already established this; the spike work is to surface the instantiation.

3. **It has empirical support.** The embeddings paper (`~/src/embeddings/paper.md`) demonstrates that an analogous prediction holds for *epistemic* content: a calibrated verbal-probability axis emerges in frozen pretrained pooled sentence embeddings, with cross-architecture and cross-linguistic robustness. The same paradigm should work for causal-marker content; the relevant experiments are (i) probing for cause/condition/counterfactual axes analogous to the modal axis; (ii) concept-erasure validation analogous to the predicative↔modal erasure already done.

**What this does NOT establish**:

1. **That LLMs deploy the encoded structure faithfully.** As in C1, encoded ≠ deployed. The IB result bounds what can be in the representation, not what shows up in generation.

2. **A specific quantitative bound on preserved causal information.** The "proportional to predictive contribution" framing is qualitative. Making it quantitative requires choosing a specific causal-information measure (directed information, do-calculus distinguishability, etc.) — same gap as C3.

3. **That the structure is recoverable by causal-discovery algorithms operating on embeddings.** The structure is *preserved* in the IB sense; whether it is *recoverable* by a specific algorithm is a separate computational question.

**Routing**: The cleanest landing for this is a Working Note in [`obs-evaluation-metrics`](../../03-llm-core/src/obs-evaluation-metrics.md) or a paragraph in the [`03-llm-core/OUTLINE.md`](../../03-llm-core/OUTLINE.md) Source Material section — citing the embeddings paper's epistemic-content result as the empirical paradigm and noting the analogous prediction for causal content as a near-term experimental target.

---

## Synthesis — the four angles together

| angle | what it derives | what it doesn't | strength |
|---|---|---|---|
| **C1** (discourse-act encoding) | Pearl Level 2 content is in the text, recoverable structurally, not Level-1-reducible | Implicit-relation recovery; speaker-commitment faithfulness in training distribution | **strongest** — conditional theorem under three named postulates |
| **C2** (Reichenbachian inheritance) | Statistical structure in corpora reflects causal structure in source-cognitive-processes | Quantitative lower bound; uniform faithfulness | **plausibility-strong**, foundational for distributional methods |
| **C3** (ICM time-asymmetry) | Forward-language compresses better than reversed-language | The lower bound by causal-information content remains a postulate | **partial** — directional asymmetry yields; quantitative link is work-not-yet-done |
| **C4** (causal-IB consequence) | LLM embeddings preserve discourse-DAG structure proportional to predictive value | Specific quantitative bound; deployment-faithfulness | **already AAT-internal**, this spike surfaces the instantiation |

The four together establish a richer picture than any one alone:

- **Speakers commit to causal claims in text** (SLC + SC) → **Level 2 content is in the text structurally** (C1) → **and inherited via statistical structure** (C2) → **with directional asymmetry signatures matching causal direction** (C3) → **and preserved in IB-optimal embeddings proportional to predictive value** (C4).

Each angle is a different facet of the same underlying fact: language is a substrate that **carries** causal information through multiple structural mechanisms simultaneously. Pearl's hierarchy applies to the data the system has — but the data, when the data is natural language, is not raw-observational. It is **performatively asserted causal content by speakers committed to that content**, plus **statistical inheritance from causally-structured source-processes**.

The combined picture is the strengthening Joseph's prompt was asking for.
